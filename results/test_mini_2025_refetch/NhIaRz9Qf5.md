I now have sufficient calibration data. Let me compile my final review.

## Summary

SEAKR proposes an adaptive Retrieval-Augmented Generation framework that uses the Gram determinant over hidden states of the `<EOS>` token (sampled k=20 times) as a "self-aware uncertainty" signal. This signal drives three components: (1) whether to retrieve, (2) which retrieved snippet to use (re-ranking by uncertainty reduction), and (3) which reasoning strategy to select. On complex multi-hop QA (2WikiMultiHopQA, HotpotQA), SEAKR achieves 36.0% and 39.7% F1 with LLaMA-2-7B, outperforming the best baseline (DRAGIN) by 6.0 and 5.5 points respectively. On simple QA the gains are smaller or absent.

## Strengths

- **Novel and well-motivated uncertainty estimator for adaptive RAG.** The Gram determinant over internal representations of the `<EOS>` token (Section 3.4, following INSIDE) is an elegant way to capture generation consistency at the representation level, avoiding the "same semantics, different wording" problem that afflicts output-level perplexity or probability measures. The paper argues convincingly that internal-state signals are more informative than output-probability triggers.

- **Substantial and consistent gains on complex QA.** On 2Wiki (36.0% F1, +6.0 over DRAGIN) and HotpotQA (39.7% F1, +5.5 over DRAGIN), the improvements are large and appear robust (Table 1). The tuning-free SEAKR also dramatically outperforms the fine-tuned Self-RAG (19.6% and 17.5% F1 on those datasets), demonstrating that self-awareness from internal states generalizes across task distributions without domain-specific training.

- **Ablation study isolates the contribution of each component.** Table 3 shows that removing self-aware re-ranking (– S.A. Re-rank) degrades F1 from 37.8→35.0 on 2Wiki and 38.1→36.6 on HPQA, while removing self-aware retrieval (– S.A. Retrieval) degrades to 35.7 and 37.6. This provides concrete evidence that dynamic integration (re-ranking and reasoning selection) is at least as important as the retrieval trigger itself.

- **Scaling with stronger backbones.** Table 4 shows SEAKR with LLaMA-3-8B-Instruct achieves 48.1% F1 on 2Wiki (vs. 37.8% with LLaMA-2-7B-Chat), indicating the uncertainty mechanism synergizes with model capacity.

## Weaknesses

### Fatal
None.

### Major

- **The self-aware re-ranking mechanism's core assumption is not validated.** The paper selects the retrieved snippet that *minimizes* self-aware uncertainty, implicitly equating "uncertainty reduction" with "provides the correct missing information." This is not tested systematically. A snippet could reduce uncertainty by being confidently wrong—e.g., presenting a plausible but incorrect date that the model, lacking contradictory knowledge, commits to consistently. The paper provides a single case study (Table 5) where the selection works correctly, but no analysis of how often the selected snippet is actually correct vs. confidently misleading. Since re-ranking is claimed to be the most important component (larger ablation impact than retrieval itself), this unverified assumption weakens the central conclusion. The authors should either provide a human-annotated analysis of re-ranking selection accuracy or an automatic proxy (e.g., how often the selected snippet enables the correct final answer compared to alternatives).

- **No statistical grounding for any reported result.** The paper reports only point estimates. No confidence intervals, error bars, or significance tests are provided anywhere. This is especially consequential for: (a) IIRC, where the F1 gain over DRAGIN is only 0.6% (23.5 vs. 22.9); (b) NaturalQuestions, where SEAKR (34.4% F1) trails Self-RAG (35.1%) and is within rounding distance of FLARE (34.3%); (c) the ablation study, run on only 500 samples per dataset, where component rankings are not monotonic across datasets (e.g., on HPQA, removing self-aware retrieval yields 37.6 vs. 38.1 full, nearly overlapping). Without variance estimates, the reader cannot assess whether any of these differences are reliable.

- **Computational cost is high and unquantified.** Each uncertainty estimate requires k=20 forward passes (sampling k generations, extracting hidden states of `<EOS>`). The pipeline may make multiple such estimates per question. While the paper notes using vLLM for parallel inference (Section 4.1.3), there is no analysis of: average number of forward passes per query, wall-clock time, or generation budget relative to baselines. Without this, the practical trade-off between SEAKR's accuracy gains and its expense cannot be evaluated. This is particularly relevant because cheaper alternatives (e.g., using per-token max softmax probability or predictive entropy of the pseudo-generation) could potentially achieve comparable results.

### Minor

- **Threshold sensitivity not analyzed across datasets.** The retrieval threshold δ (> –6) is tuned on a subset of NQ and applied to all other datasets (Section 4.1.1, Figure 3). The paper provides no analysis of how sensitive results are to δ on complex QA datasets, where uncertainty distributions likely differ from simple QA. If δ requires dataset-specific tuning, the "tuning-free" framing is weakened.

- **The IIRC result is weak despite the paper's claims.** SEAKR improves by only 0.6% F1 over DRAGIN on IIRC (Table 1), and the paper acknowledges this is due to numerical reasoning difficulty. While this is not a flaw per se, the headline claim ("outperforms existing adaptive RAG methods") is not uniformly supported across all datasets.

- **FLARE re-implementation for complex QA.** FLARE is re-implemented with the IRCoT strategy to support multi-step reasoning (Section 4.1.2). This modification is acknowledged but may disadvantage FLARE, since the original design was single-step. A comparison on tasks where the original FLARE applies would strengthen the evaluation.

- **Pseudo-generation query construction is underspecified.** The paper says "tokens in r indicating high uncertainty due to their low probability are identified and removed" (Section 3.1) but does not define what threshold or criterion determines "low probability."

### Trivial
None.

## Nice-to-Haves
- A direct comparison of the Gram-determinant uncertainty with a cheaper output-level measure (e.g., predictive entropy of the pseudo-generation) under the same retrieval and integration framework would clarify whether the added cost is justified.
- A limitations section would be helpful, especially given the computational overhead and the unvalidated re-ranking assumption.
- Reporting the average number of retrieval calls per query for SEAKR vs. baselines (e.g., IRCoT always retrieves; SEAKR retrieves selectively) would partially contextualize the cost.

## Removed Points

- **"Re-ranking conflates uncertainty with correctness — fatal"** → Downgraded from "critical issue" to Major. The concern is valid and well-stated, but it is not fatal because the ablation (Table 3) provides empirical evidence that the re-ranking mechanism works on aggregate. It needs better validation, not a complete invalidation of the paper's claims.
- **"Computational cost is not acknowledged — fundamental limitation"** → Moved to Major. The critic's framing as "fundamental" is too strong; vLLM parallel inference partially mitigates cost, and the paper does not claim efficiency. The real issue is lack of quantification.
- **"Distribution shift of Self-RAG limits comparison"** → Removed. The paper acknowledges this (Section 4.2.1) and it is an inherent characteristic of Self-RAG, not a flaw in SEAKR. The critic also acknowledges this is "not the authors' fault."
- **"Gram determinant formula not in main text"** → Removed. The appendix is stripped by the parser, a known review-process artifact.
- **"No discussion of entropy-based uncertainty"** → Removed. The paper includes LN-Entropy in the ablation (Table 3).
- **"No limitations section"** → Moved to Nice-to-Haves.
- **Strength Finder generic strengths** → Some generic strengths (e.g., "tuning-free generalization") were retained because Table 1 concretely supports them. The strength about "bypasses surface-form variability" is specific and well-evidenced.

## Novel Insights

The harsh critic's observation that the re-ranking mechanism's validity hinges on an unverified assumption (uncertainty reduction = correctness) is the most penetrating insight across both reviews. The strength finder's emphasis on the ablation study revealing that self-aware re-ranking has a *larger* impact than self-aware retrieval is also noteworthy and potentially under-explored in the paper itself — the authors claim this shows "the crucial aspect of designing effective knowledge integration," but this is also the component whose mechanism is least validated. The tension between the two reviewers on this point is productive: the method may genuinely improve performance, but we do not yet understand *why* in a scientifically satisfying way.

## Suggestions

1. **Validate the re-ranking mechanism systematically.** For a sample of questions, manually annotate whether the snippet with lowest uncertainty is (a) correct and contributes to the answer, (b) correct but redundant, or (c) incorrect but reduces uncertainty (confidently wrong). Report selection accuracy. This is the single most important addition.

2. **Add error bars or confidence intervals** to all main results and ablation tables (bootstrap over questions). Without these, the marginal gains on IIRC and NQ cannot be evaluated.

3. **Quantify computational cost.** Report the average number of forward passes (or wall-clock time) per query for SEAKR vs. each baseline. Compare with a cheap ablative variant (e.g., using max softmax probability instead of the Gram determinant for the same pipeline). This would clarify the practical trade-off.

4. **Analyze threshold robustness.** Show how performance on complex QA (2Wiki, HPQA) varies with δ around the chosen value. If the method is robust, this strengthens the "tuning-free" claim; if not, the limitation should be acknowledged.

---

## Score and Decision

### Calibration Anchors

| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| Reward-RAG (oqRe1KvD17) | 3.00 | 1 (weak) | Much weaker — incremental RAG fine-tuning with no clear novelty |
| EDU-RAG (a2rSx6t4EV) | 2.33 | 1 (weak) | Much weaker — a benchmark paper, not a method paper |
| CtrlA (QYvtX2XA8p) | 4.50 | 1 (mid) | Most directly comparable (adaptive RAG via internal representations). SEAKR has stronger complex QA results and more novel uncertainty estimation. **SEAKR > CtrlA** |
| Exploring Knowledge Boundaries (M1ZMwDqvSe) | 4.33 | 2 (mid) | Similar topic (when to retrieve) but uses a trained classifier. SEAKR has a more elegant approach and better results. **SEAKR > this** |
| Auto-RAG (jkVQ31GeIA) | 5.50 | 1 (mid) | Comparable quality and scope. Auto-RAG uses fine-tuning; SEAKR uses internal states. Similar empirical strength. **SEAKR ≈ Auto-RAG** |
| Measuring LM Uncertainty (tZk3LnvVtK) | 5.60 | 2 (mid) | UQ paper with clarity issues. SEAKR has a clearer application and stronger empirical setup. **SEAKR ≈ this** |
| Generating with Confidence (XJiN1VkgA0) | 6.00 | 2 (mid) | Better experimental rigor (std dev reported). SEAKR has stronger applied contribution but weaker statistics. **SEAKR < this** |
| Chain-of-Knowledge (cPgh4gWZlz) | 6.00 | 2 (mid) | Accepted poster. Stronger across-the-board execution. **SEAKR < this** |
| Do I Know This Entity? (WCRQFlji2q) | 9.00 | 1 (strong) | Far stronger — mechanistic interpretability with causal validation, oral paper |
| Retrieval is Accurate Gen. (oXYZJXDdo7) | 7.00 | 2 (mid) | More novel paradigm, broader evaluation. **SEAKR < this** |

**Round 1 bracket:** 3.5–7.5 → narrowed to 4.5–6.0 based on comparison with CtrlA (4.5) and Auto-RAG (5.5), which are the most directly comparable papers.

**Round 2 narrowing:** Positioning relative to Auto-RAG (5.5), Measuring LM Uncertainty (5.6), and Generating with Confidence (6.0) places SEAKR at 5.5. The paper has a genuinely novel technical contribution and strong results on complex QA, but the lack of statistical grounding and the unvalidated re-ranking assumption prevent it from reaching the 6.0 tier.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>