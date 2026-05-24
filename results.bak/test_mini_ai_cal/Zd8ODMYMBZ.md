Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper proposes FaviComp, a training-free evidence compression method for RAG that uses ensemble decoding — interpolating token-level logits between a smaller compression model (summarizing retrieved documents) and the target model (generating context from parametric knowledge) — to produce compressed evidence with lower perplexity for the target model. Experiments on five open-domain QA datasets show consistent improvements over recent compression baselines, with gains of up to 23.91%. The method's ability to integrate parametric knowledge when retrieved evidence is incomplete is supported by a Hits-based analysis (Figure 3).

## Strengths

1. **Clean, training-free method backed by an intuitive principle.** FaviComp uses logit interpolation (Eq. 2) with a single tunable coefficient α to balance compression-model output and target-model preferences. The mechanism is clearly motivated by the empirical finding that lower target-model perplexity on the compressed evidence correlates with better downstream performance (Figure 2). The method requires no training and can be plugged into any RAG pipeline.

2. **Consistent improvements across diverse settings.** FaviComp outperforms recent compression baselines (RECOMP, CompAct, LongLLMLingua) on five open-domain QA datasets using three different target-model families (Llama3-8B, Mistral-7B, Mixtral-8x7B), with accuracy gains up to 23.91%. The ablation varying α (Figure 2) cleanly shows that α=0.5 (balanced ensemble) outperforms both extremes across NQ, HotpotQA, and MuSiQue.

3. **Pertinent analysis of parametric vs. non-parametric knowledge integration (Figure 3).** The Hits-based analysis is the paper's strongest evidence: FaviComp outperforms Zero-shot Summarization and CompAct on the evidence-irrelevant (Hits=0) subset where retrieved documents lack the answer, while matching them on the evidence-relevant (Hits=1) subset. This directly demonstrates that the target model's parametric knowledge is effectively injected during compression — a capability absent in prior compression methods that only summarize what is in the retrieved documents.

4. **Model-agnostic and higher compression rates.** FaviComp works with different model families (Llama, Mistral) and achieves higher compression rates than Zero-shot Summarization (Section 4.4), showing that the ensemble strategy produces both more effective and more concise summaries.

## Weaknesses

### Fatal

None.

### Major

1. **The claimed equivalence between Zero-shot Summarization and FaviComp with α=0 is inaccurate for two of the three model pairs.** The paper states (Section 3.3): "Zero-shot Summarization is instructed to summarize the evidence set into a concise summary based on the question, using the same LM as the target model. This is equivalent to FAVICOMP with α=0." However, Section 3.2 specifies that FaviComp uses *separate* compression models (e.g., Llama3.2-3B-Instruct) that are smaller than the target model (e.g., Llama3-8B-Instruct) for pairs (1) and (2). Zero-shot Summarization uses the larger target model as the summarizer; FaviComp with α=0 uses the smaller compression model. These are different models with different capabilities. The equivalence only holds for pair (3), where both models are the same Mistral-7B-Instruct.

   **Why this matters:** The paper repeatedly uses this equivalence (Sections 3.3, 4.1, 4.4, 5, line 122, line 129) to frame the ensemble as outperforming both individual sources (α=0 and α=1). Figure 2's α=0 corresponds to the *smaller* compression model, not the stronger Zero-shot Summarization baseline that appears in the main results tables. This does **not** invalidate the main empirical finding — FaviComp (α=0.5) still beats Zero-shot Summarization (which uses a better summarizer) as a separate baseline, making the comparison *conservative*. However, the persistence of this imprecise equivalence claim throughout the paper misrepresents what the α variation in Figure 2 shows, and it conflates two distinct ablations (using a weaker model vs. using the target model). The paper should either correct the claim or restrict the equivalence to pair (3).

### Minor

2. **"Evidence compression" framing overstates what the method does.** FaviComp's compressed evidence can include content generated solely by the target model's parametric knowledge (e.g., the "Skeptic" example in Table 2), even when that content has no basis in the retrieved documents. The paper acknowledges this as a feature (Section 2.1: "seamlessly integrating parametric knowledge"), but the persistent framing as "compression" is imprecise — the output is a hybrid that may *augment* rather than merely *compress* the evidence. This does not weaken the contribution but would benefit from more precise terminology (e.g., "familiarity-aware evidence fusion").

3. **No discussion of failure cases or limitations.** The paper does not discuss settings where FaviComp might underperform (e.g., when both models are uncertain and ensemble decoding amplifies noise, or when the target model's parametric knowledge is confidently wrong and overrides correct evidence). Similarly, the computational cost of running two LMs during compression decoding is not quantified — the method is "training-free" but requires simultaneous inference with two models, which may be expensive in practice.

4. **The pair (3) same-model ablation is deferred to the appendix.** The most informative setup for isolating the ensemble effect (compression model = target model, pair 3) is only mentioned as being in Appendix §B.1, which is stripped by the parser. If available, this ablation would partially address the Major weakness above and should be featured in the main paper.

5. **No variance or significance information.** Given the many comparisons (5 datasets, 3 model pairs, multiple baselines), confidence intervals or significance tests would help assess the reliability of reported gains, especially for smaller improvements.

### Trivial

6. The paper would benefit from an explicit statement that the token-level ensemble is feasible because both models use compatible tokenization (which holds for the three chosen pairs but may not generalize).

## Nice-to-Haves

- **Run a clean same-model ablation in the main paper** (compression model = target model) for all datasets, not just pair (3) in the appendix. This would cleanly isolate the ensemble effect from model capacity differences.
- **Quantify the computational overhead** of running two LMs during compression decoding (latency, FLOPs, memory), to help practitioners assess the trade-off.
- **Add error bars or bootstrapped confidence intervals** for the main results.

## Removed Points

These points from the input reviews are removed with justification:

1. **"The paper does not specify whether baselines like RECOMP and CompAct use the same target model and retriever"** — This is a reasonable default assumption in experimental ML papers; no evidence suggests otherwise. Removed as a generic concern without concrete anchor in the paper.

2. **"No discussion of missing appendix content (prompts, training details)"** — Parser artifact; the original submission contains these. Removed per hard rules.

3. **"Missing results for model pair (3) across all baselines"** — The paper states these are in Appendix §B.1, which is stripped by the parser. Removed per hard rules.

4. **"Criticism about tokenization compatibility between different LMs"** — The paper only uses same-family models (Llama/Llama, Mistral/Mistral/Mixtral). The critic acknowledges this is likely compatible. This is a minor point the paper could mention but not a substantive weakness. Removed as a generic concern.

5. **"Zero-shot Summarization description contradicts itself"** — After verification, the description is consistent: it says Zero-shot Summarization uses the target model. The issue is specifically about the *equivalence* claim, which I have retained as Major Weakness #1 above. Removed as redundant.

6. **Strength Finder's "Higher compression rate than equivalent zero-shot summarization"** — This strength propagates the same imprecise equivalence claim that is the paper's main weakness. When a strength and a verified weakness disagree on the same point, the weakness wins. Demoted; the compression rate comparison is still a strength, but the "equivalence" framing is removed.

7. **Strength Finder's generic strengths about "important problem"** — These lack specific evidence. Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews converge on the paper's stated findings but surface a persistent terminological imprecision (the α=0 equivalence) that the paper would need to address in revision.

## Suggestions

1. **Correct the α=0 equivalence claim.** Either: (a) explicitly state that the equivalence only holds when the compression model and target model are the same (pair 3), or (b) re-frame Zero-shot Summarization as a separate baseline rather than claiming it corresponds to α=0 in the FaviComp framework. The main results (Table 1) remain valid as a baseline comparison regardless, because FaviComp (α=0.5) still outperforms Zero-shot Summarization even though Zero-shot Summarization uses a stronger summarizer.

2. **Move the same-model ablation (pair 3, where compression model = target model) from the appendix to the main paper.** This isolates the ensemble effect from model capacity differences and would directly support the "familiarity" thesis.

3. **Rename or qualify the "compression" framing** to reflect the method's dual nature: it both compresses evidence and injects parametric knowledge. "Familiarity-aware evidence fusion" or a similar precise term would avoid overclaiming.

4. **Add a limitations paragraph** discussing potential failure cases (e.g., when the target model's parametric knowledge is wrong, or when both models are uncertain) and the computational cost of dual-model decoding.

---

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):**
- Weak band (score < 3.5): 4 papers at avg 3.00 — topics include KV cache compression, fact verification, decoding-free selection, context-as-draft. These papers have fundamental flaws or very thin contributions. **This paper is clearly stronger.**
- Middle band (3.5–7.5): 4 papers — NUGGET2D (5.67), EvidenceBench (5.50), EATQA (4.67), RCC (4.00). These are papers with solid ideas but meaningful weaknesses.
- Strong band (7.5+): 4 papers at 8.00 — theorem proving, controlled generation, VLM analysis. **This paper is not at this level.**

Initial bracket: **4.5 to 6.5**.

**Round 2 (Narrowing within bracket):**
- RagVL (6.00, sim 0.74): Multimodal RAG pipeline with major weakness about conflated baselines. Similar-level weakness to FaviComp's α=0 issue. RagVL has more extensive empirical validation but a more complex pipeline. **FaviComp is slightly weaker — the α=0 claim touches the paper's framing more centrally.**
- DRAG (5.25, sim 0.73): RAG framework with underspecified training procedure as major weakness. DRAG's weakness is more severe (core component underspecified). **FaviComp is stronger than DRAG.**
- Mamba Retriever (5.75, sim 0.72): Clean paper with only minor weaknesses. **FaviComp has a more substantive weakness than Mamba Retriever.**
- DDR (6.00, sim 0.68): Differentiable data rewards for RAG. Comparable paper quality with clean experiments. **Comparable to DDR but with a more central clarity issue.**
- Gray-box fine-tuning (5.50, sim 0.68): Clean contributions with minor weaknesses. **Comparable quality.**

The narrowing pass confirms the paper sits in the **5.0–6.0** range. It is stronger than papers with underspecified core components (DRAG at 5.25, RCC at 4.00) but weaker than papers with fully clean framing (Mamba Retriever at 5.75). The α=0 equivalence imprecision brings it down relative to otherwise comparable papers.

**Final score: 5.5** — The paper's core idea is sound and the empirical results are meaningful, but the persistent imprecise claim about the α=0 equivalence undermines the clarity of the presentation and requires correction. This places the paper below the clean accept threshold.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>