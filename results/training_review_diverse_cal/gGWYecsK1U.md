Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the consolidated review.

---

## Summary

This paper introduces Integrative Decoding (ID), a decoding-time method for improving factuality in open-ended LLM generation. ID works by: (1) sampling multiple responses from the LLM, (2) constructing augmented inputs by prepending each sampled response to the original prompt, and (3) concurrently processing these inputs and aggregating their logit predictions at each decoding step to select the next token. The method is evaluated on three open-ended benchmarks (TruthfulQA, Biographies, LongFact) across six LLM families, consistently improving factuality, with absolute gains of up to +11.2%, +15.4%, and +8.5% respectively. ID also demonstrates favorable scaling behavior (performance improves log-linearly with more samples) and high inference efficiency relative to comparable ensemble methods.

## Strengths

- **Consistent and substantial factuality gains across diverse models and tasks.** ID improves factuality on TruthfulQA (+3.7–10% by %Truth), Biographies (+1.1–15.4% by %Accuracy), and LongFact (+1.6–8.5% by F1@128) across six LLM families (LLaMA2/3, Mistral2, Qwen2, Gemma2, GLM4), as shown in Table 1. These are not cherry-picked results — the improvements hold across the entire model zoo.

- **Performance scales log-linearly with the number of sampled responses.** The paper demonstrates a consistent log-linear relationship between ID's performance and the number of integrated samples *k* on the Biographies dataset across all six LLMs (Figure 3, §3.3). This mirrors the inference-time scaling behavior observed in exact-match self-consistency and is something USC and SR fail to sustain — their performance often degrades with more samples.

- **High inference efficiency relative to comparable methods.** ID achieves 1.13 ms/token latency (only ~11× slower than greedy decoding), substantially faster than SE-SL (8.37 ms) and SE-RG (7.28 ms), while USC achieves 0.93 ms/token (Table 4). This efficiency stems from avoiding iterative prompting or chain-of-thought verification.

- **Does not harm language coherence.** In human evaluation against greedy decoding, ID wins or ties in >90% of cases across all six models and never loses more than ~12% (Table 2). This confirms that the token-level logit aggregation preserves fluency.

- **Robust across model scales and sampling strategies.** ID yields gains consistently on models from 3B to 72B parameters (Qwen-2.5 series, LLaMA-2-13B/70B, Mistral variants) and remains effective under different temperature and nucleus sampling configurations (§3.2, §3.5).

## Weaknesses

### Fatal
None.

### Major

- **Unequal comparison on LongFact confounds the claimed robustness to document-level generation.** On the LongFact benchmark, the paper sets *k*=16 for ID but *k*=4 for USC, SR, and FSC (line 166), explicitly because long responses push those baselines past context-length limits. The paper acknowledges this discrepancy but does **not** report ID's performance at *k*=4 on LongFact, nor does it provide a scaling curve on LongFact analogous to the one shown for Biographies. Since the paper's own results demonstrate that ID's performance improves log-linearly with *k*, the reported gains on LongFact (up to +8.5% F1@128) are confounded by the 4× sampling budget advantage. The claim that ID is "robust to document-level generation tasks" (§3.2, bullet 3) therefore rests on weaker evidence than the other claims. The authors could fix this by providing ID at *k*=4 on LongFact, or by designing a variant of the baselines that can accommodate more samples (e.g., via summarization/truncation). Without this, the LongFact results — which are central to the paper's claim of generality across text lengths — do not fully support the conclusion as currently presented.

### Minor

- **The core theoretical assumption (Eq. 3) is asserted but not validated.** The paper claims that `log p_θ(y | [x; r_j; x]) ∝ f̄(y, r_j) + α·G(x, y)` (Eq. 3), i.e., the model's log-probability when prompted "with reference to" a sampled response is proportional to the sum of consistency with that response and coherence. This is acknowledged as an assumption (line 104: "This assumption is reasonable because...") and is supported indirectly by the self-consistency and coherence evaluations (Tables 2–3). However, the proportionality itself is never directly tested — e.g., by measuring the correlation between the predicted log-probability and an externally measured consistency score on a small annotated set. This does not invalidate the paper's empirical contribution (the method works regardless), but it leaves the theoretical derivation somewhat undersupported relative to the formalism the paper invests in it.

- **Limited discussion of failure modes.** The paper does not analyze scenarios where ID might degrade performance — e.g., if all sampled responses contain a shared hallucination, ID's aggregation mechanism could reinforce rather than dilute the error. A brief analysis of failure cases or a comparison to an oracle that picks the best single sampled response would help readers calibrate the method's boundaries.

### Trivial

None.

## Nice-to-Haves

- The comparison with DoLa on open-ended generation is somewhat tangential; DoLa is a contrastive-layer method designed for more structured factual recall and predictably underperforms on free-form generation. The space could be better used for ablations (e.g., ID at *k*=4 on LongFact).
- The paper's framing of "unlocking the potential of self-consistency in open-ended generation tasks" slightly overstates novelty, given that USC, SR, FSC, and SE already target open-ended text. The paper's actual contribution is a more efficient and scalable instantiation of the same principle — which is genuinely useful, but the novelty is primarily in the decoding mechanism rather than the conceptual insight.
- An analysis of whether ID affects performance on tasks requiring creativity, opinion, or diversity (where the method's self-consistency bias might be detrimental) would be a useful boundary-condition discussion.

## Removed Points

- **DoLa comparison is tangential / takes up space** — opinion-based, not a verifiable weakness.  
- **Vanilla baseline is "not the right baseline"** — the Vanilla (temperature sampling) condition is a legitimate neutral baseline showing the baseline self-consistency level; the reviewer's suggested alternative (averaging logits over multiple forward passes of the *same* input) would be a different ablation question, not a correction.  
- **"Novelty is in engineering, not conceptual insight"** — subjective framing judgment that inappropriately minimizes a legitimate methodological contribution.

## Novel Insights

None beyond the paper's own contributions. The method is clean and the experiments are well-executed, but the reviews do not surface a genuinely novel analytical perspective not already present in the paper.

## Suggestions

1. **Add a LongFact ablation with ID at *k*=4.** This is the single highest-impact fix. Showing that ID at *k*=4 still outperforms baselines at *k*=4 (or at least obtains comparable gains) would cleanly separate the method's advantage from the unequal sampling budget and fully support the document-level robustness claim. If the gap narrows substantially, the authors should discuss this honestly.

2. **Validate the core assumption (Eq. 3) on a small subset.** Measure the correlation between `log p_θ(y | [x; r_j; x])` and an oracle consistency score (e.g., GPT-4 judged) on 50–100 Biographies examples. Even a modest correlation would substantially strengthen the theoretical grounding; the absence of correlation would signal that the method works for reasons other than those claimed.

3. **Add a failure-case analysis.** A short paragraph or small table showing when ID hurts performance (e.g., when all sampled responses share the same hallucination) would improve the paper's completeness and help practitioners understand the method's limitations.

## Score and Decision

The paper presents a clean, well-motivated decoding method with strong and consistent empirical results on two of three benchmarks (TruthfulQA, Biographies) under fair comparisons. The LongFact comparison has a real confounding issue that undermines the document-level robustness claim in its current form, but this is fixable. The method is efficient, scales well, and preserves fluency — all genuine merits. I recommend **minor revision** to address the LongFact comparison before acceptance.

**Originality**: 7/10 — the idea of aggregating logits across reference-augmented inputs is novel and elegant.  
**Importance**: 8/10 — improving factuality in open-ended generation is an important problem.  
**Claims support**: 6/10 — the core claim about document-level robustness is weakened by the unequal comparison.  
**Soundness**: 7/10 — experiments are otherwise thorough; the gap in the theoretical derivation does not undermine the empirical results.  
**Clarity**: 8/10 — well-written and easy to follow.  
**Value**: 7/10 — the method is practical and likely to be adopted by practitioners.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>