## Summary

This paper proposes CodeUnlearn, a zero-shot machine unlearning method that introduces a discrete codebook bottleneck (with sparse autoencoders) into a transformer language model, then performs unlearning by removing codebook entries statistically enriched for a target topic. The method is tested on T5-small for English-to-French translation of literary texts across seven topics (love, Julien, Captain, Poor, Wish, White, Black). The core idea — discretizing activations to enable targeted code removal — is novel and well-motivated, but the evaluation is substantially insufficient to support the central claims.

---

## Strengths

- **Novel architectural design for controllable information flow.** The codebook is deliberately placed *after* the residual connection (Section 3.2), which prevents the residual stream from bypassing the discrete bottleneck. This is a non-trivial architectural decision that addresses a real challenge in using bottlenecks in transformers, and is well justified in the text.

- **Principled code-selection procedure.** The paper defines an enrichment ratio (Equation 11) comparing activation frequencies in target vs. control datasets, and uses a chi-squared test to filter codes to remove (Section 3.5). The combination of a log-odds style ratio with a statistical significance test provides a cleaner foundation for code selection than simple frequency-based heuristics.

- **Systematic ablation over code-removal strength.** The paper varies \(S'\) from 8 to 104 (removing 0.064% to 0.828% of the codebook), and reports performance at each level across multiple metrics (BLEU, METEOR, BERTScore, BartScore). This gives a clear picture of the trade-off between unlearning strength and model degradation.

- **Genuine novelty of the approach.** Using discrete codebook representations for zero-shot unlearning in language models — rather than in image classifiers — is a genuinely new direction. The method is amortized: once the codebook is trained, unlearning a new topic requires only forward passes and code deletion, no gradient computation.

---

## Weaknesses

### Major

- **No comparisons to any baseline unlearning method.** The paper evaluates only its own codebook model before vs. after code removal. There are no comparisons to existing unlearning methods (gradient ascent on target data, model editing approaches like ROME/MEMIT, fine-tuning without target data, logit suppression, or even a simple random-code-removal baseline). The abstract claims the method is "effective" and provides "a baseline for unlearning in language models," but without any comparison, these claims are unsupported. This is the single most significant weakness: the paper cannot know whether the observed degradation is better or worse than what a trivial alternative achieves.

- **The evaluation conflates "damaging performance on a concept" with "removing knowledge of that concept."** The paper measures unlearning success by whether the model produces incorrect translations of target words. This is evidence of performance degradation, not necessarily knowledge removal. The codebook is placed in only the third encoder layer of T5-small, and the claim in Section 3.4 that joint training ensures "the entire model relies on the codebook's representation" is asserted without evidence. Other layers (especially earlier encoder layers and the decoder) could retain the target information. The paper provides no probing, membership inference, or alternative-prompting tests to verify that the knowledge is genuinely gone rather than temporarily suppressed. For example, the example in Table 1 ("le mettre en état" for "love him") shows a garbled translation, which is consistent with the model having lost the concept — but also consistent with the model's processing path being corrupted while the information persists elsewhere in its weights.

- **Collateral damage on non-target data is severe for several topics, contradicting the paper's characterization.** The paper claims "minimal impact" on non-target performance, but the normalized numbers in Table 2 tell a different story. For "Julien": non-target BLEU drops 65.70%, non-target METEOR drops 64.38%, non-target BERT-P drops 94.63%. For "Wish": non-target BLEU drops 87.65%, non-target BART drops 133.35%. These are not small side effects. While some topics (Captain, White, Black) show more modest non-target drops, the overall pattern undermines the claim that the method preserves unrelated capabilities. The normalized metrics also obscure absolute performance, making it difficult to assess how much utility remains.

### Minor

- **Chi-squared test applied to 25,000 codes at p<0.05 without multiple comparison correction.** With 25,000 hypothesis tests at α=0.05, one expects ~1,250 false positive enrichments by chance. The enrichment ratio (R>0) provides a second filter, but the paper does not discuss this issue or apply corrections (Bonferroni, Benjamini-Hochberg). This could lead to removing codes that are not genuinely topic-related.

- **Control dataset construction by word replacement is a rough proxy.** The paper creates \(D_{\bar{T}}\) by replacing target-topic words in \(D_T\) with unrelated words. This can alter syntax, semantics, and discourse structure beyond the target concept, potentially causing codes to be identified for spurious reasons. For example, replacing "love" with "hate" changes the sentence's meaning entirely, not just the topic word.

- **Evaluation on only one task (translation) and one model (T5-small).** Translation is a narrow proxy for the kinds of knowledge removal the motivation discusses (medical, financial, biological agent risks). The paper does not test on open-ended generation, question answering, or text completion — tasks where unlearning would be more practically relevant. The use of a 60M-parameter model also raises questions about scalability.

- **Metrics are reported only as normalized improvements, not absolute scores.** The normalization (0 = zero-shot model, 1 = codebook model) makes it hard to interpret the actual quality of outputs. Raw BLEU, METEOR, BERTScore, and BartScore values should be reported alongside normalized values.

- **The choice to place the codebook in the third encoder layer is not ablated.** The paper cites prior work on feature hierarchy (Templeton et al., 2024) to justify this choice, but does not test alternative layers. The results could be sensitive to this architectural decision.

- **"First work" claim is too strong without baselines.** The abstract claims this is "the first work that successfully enables unlearning specific topics with contextual relevance in an LM." Given the lack of baselines, this overstates the contribution.

### Trivial

- The specific default value of \(S\) (number of top codes summed during inference) is never stated; only \(S \geq 1\) is given in Section 3.1, while the experiment section reports \(S'\) values separately.
- The \(L_1\) penalty (Equation 7) is on code vector entries, not on the number of active codes. The paper accurately describes this as encouraging "sparse internal feature representations within each codebook vector," but a reader might expect sparsity in code *selection* given the context.

---

## Nice-to-Haves

- Adding a membership inference attack or probing-based verification to determine whether target information persists elsewhere in the model after code removal would substantially strengthen the paper's central claim.
- Testing on a broader range of tasks (e.g., question answering, text completion) and at least one larger model (e.g., T5-large or Llama) would improve generalizability evidence.
- Demonstrating that the method can handle sequential unlearning of multiple topics without excessive degradation would validate the "amortized" claim.
- A baseline where random codes are removed (at the same rate as topic-enriched codes) would help isolate whether the enrichment procedure itself adds value beyond random disruption.

---

## Removed Points

- *"The method damages rather than unlearns (conflating reproduction with translation)"* — This concern about construct validity is already captured in Weaknesses (Major), but the reviewer's framing of "damages" vs. "unlearns" is noted; the paper does define unlearning as making the model perform worse on target information (Section 3, line 62: "ensures that the model can no longer effectively handle prompts that contain the target information"), so there is a definitional match.
- *"Only generative tasks are evaluated, not discriminative tasks"* — The paper's scope is explicitly language models for complex language tasks (translation), so evaluating on classification is outside scope.
- *"Synonym evaluation shows inability to distinguish"* — This is reframed in the review as a nuanced finding rather than a pure weakness; the paper presents it as a feature (contextual relevance) and acknowledges it.
- *"Topics are not sensitive information"* — While true, this is a limitation of the chosen benchmarks rather than a methodological flaw; it's noted as part of the narrow evaluation concern.
- *"No analysis of what removed codes represent"* — This would strengthen the paper but is a nice-to-have, not a weakness of the experiments as designed.

---

## Novel Insights

The most interesting observation from synthesizing the reviews is the fundamental tension this paper surfaces in the discrete-bottleneck approach to unlearning. "Unlearning via Sparse Representations" (TLBPjECC5D, avg 5.25) proposed nearly the same mechanism for image classifiers — discrete bottleneck, remove codes — and was also criticized for "weak unlearning" (the model's backbone weights remain unchanged). This paper extends the idea to language models, which raises the bar for evidence: in image classification, removing a class can be verified straightforwardly via accuracy on held-out images; in language, "knowing" a concept is distributed across syntax, semantics, and context, making it far harder to verify removal. The current paper does not clear this higher bar. More broadly, the sparse-bottleneck family of unlearning methods appears caught between two stools: if the bottleneck is narrow enough to enable clean code-concept mapping, it degrades model quality; if it is wide enough to preserve quality, superposition of meanings in codes undermines the interpretability argument. This paper embodies that tension clearly.

---

## Suggestions

1. **Add at least one baseline comparison** — even a simple one (e.g., fine-tuning the base model on target data with random labels, or logit suppression for target tokens) would contextualize the results enormously.
2. **Verify knowledge removal beyond translation degradation** — probe hidden states for target concepts after unlearning, test with novel paraphrases, or run a membership inference attack.
3. **Report absolute metric values** alongside the normalized improvements so readers can assess real output quality.
4. **Address multiple comparisons in the chi-squared test** by applying a correction (Benjamini-Hochberg or Bonferroni) and reporting how many codes survive.
5. **Ablate the codebook layer placement** to justify why the third encoder layer specifically.

---

## Score and Decision

### Calibration

**Round 1 — Bracketing:** Three queries on machine unlearning topics returned:
- Weak band (avg < 3.5): papers at 1.67–3.00 (simple classification unlearning, mostly withdrawn)
- Middle band (3.5–7.5): papers at 4.00–5.25 (SUN at 4.00, "Unlearning via Sparse Representations" at 5.25, "Who's Harry Potter?" at 5.25)
- Strong band (7.5+): papers at 8.00–9.00 (top-tier oral papers with rigorous evaluation)

Initial bracket: 3.5–5.5.

**Round 2 — Narrowing (4.0–6.0):** Pulled anchors closer to the paper's approach:
- "Unlearning via Sparse Representations" (5.25) — very similar concept (discrete bottleneck, remove codes), but includes baselines (SCRUB), three datasets, and cleaner class-unlearning evaluation. The current paper is strictly weaker on evaluation quality.
- "Who's Harry Potter?" (5.25) — LM unlearning for concrete copyrighted content, larger model (Llama2-7b), multiple benchmarks. Better evaluation than the current paper.
- "SUN" (4.00) — training-free subspace unlearning, has baselines but criticized for weak motivation. Comparable evaluation quality to the current paper, but the current paper has a more novel approach.
- "Learn while Unlearn" (4.75) — generative LM unlearning, has baselines.

The current paper is weaker than both "Unlearning via Sparse Representations" (5.25) and "Who's Harry Potter?" (5.25) primarily due to the complete absence of baseline comparisons. It is comparable to SUN (4.00) in overall rigor but has a more novel core idea. Final score: **3.5**.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>