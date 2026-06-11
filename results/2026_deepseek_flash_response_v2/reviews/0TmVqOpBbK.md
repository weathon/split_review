## Summary

This paper proposes a conditional scaling law that incorporates architectural parameters (normalized hidden size, MLP-to-attention ratio, GQA) into the Chinchilla framework, enabling prediction of the accuracy–inference-efficiency trade-off for dense decoder-only transformers. The authors train over 200 models from 80M to 3B parameters, fit their proposed law, and use it to guide architecture search. The resulting models (Panda-1B/3B, Surefire-1B/3B) outperform retrained LLaMA-3.2 architecture baselines under the same training budget, achieving up to 2.1% higher average accuracy and up to 42% higher inference throughput.

## Strengths

1. **Held-out predictive validation across three scale gaps.** The two-step conditional scaling law is validated on progressively larger held-out sets: fitting on 80M→predicting 145M (MSE 0.0002, Spearman 0.89), 80/145M→297M (Spearman 0.79), and 80–297M→1B (Spearman 0.75) (Figure 6). These are concrete, multi-scale held-out evaluations demonstrating that the law generalizes beyond the fitting range without requiring re-fitting.

2. **Simultaneous accuracy and throughput improvements over a specific baseline.** Panda-1B achieves 57.0% vs LLaMA-3.2-1B's 54.9% average accuracy across 9 tasks (Table 1). Surefire-3B delivers up to 42% higher inference throughput than LLaMA-3.2-3B (Figure 7). These are directly measured improvements under identical training setups, not extrapolations.

3. **Systematic documentation of U-shaped relationships.** Figures 4–5 provide controlled experiments at three model sizes (80M, 145M, 297M) showing U-shaped curves for both hidden size and MLP-to-attention ratio. The optimal normalized hidden size is stable across model scales — a nontrivial empirical finding that grounds the scaling-law design.

4. **Honest ablation of fitting-data strategy revealing scale sensitivity.** The paper tests fitting on 80M–1B vs. only 1B data to predict 3B, finds Spearman drops to 0.50 in the former case (Figure 8), and transparently reports this. Rather than hiding this limitation, the authors use it to derive a practical guideline (fit on models ≈1/3 the target scale).

5. **Cross-hardware and cross-framework throughput validation.** Efficiency gains are verified on both A100 and H200 GPUs using both vLLM and SGLang (up to 47% with SGLang on H200), demonstrating that the architectural advantages transfer across serving stacks and hardware platforms.

6. **Practical handling of GQA's discrete behavior.** The paper acknowledges GQA does not follow a consistent continuous relationship with loss and handles it via explicit local search (Algorithm 1) rather than forcing it into the analytical framework — a pragmatic design choice.

## Weaknesses

### Fatal
None.

### Major

1. **Training token budget inconsistency for 3B models.** Section 4 states: "All models are trained on $100N_{\text{non-emb}}$ tokens ($5\times$ Chinchilla optimal)." For a 3B model this implies 300B tokens. Yet Section 5.1 repeatedly states 3B models are "Trained on 100B tokens" (lines 257, 259, 265). The abstract also bounds the token range at "8B to 100B training tokens" (line 9), consistent with a 100B cap but inconsistent with the $100N_{\text{non-emb}}$ rule. If a fixed 100B cap was used for 3B models while smaller models followed $100N$, then (a) the 3B models are trained at $\sim$33× Chinchilla rather than 5×, and (b) the scaling law is being validated at a different training-token regime than the one on which the smaller models were fit. This inconsistency must be resolved before the experimental conditions can be properly evaluated.

### Minor

2. **Scaling law's rank-ordering degrades across large scale gaps.** When fitting on 80M–1B models and evaluating on 3B, the Spearman correlation is 0.50 (Figure 8, left)—barely above chance for ranking architectures. While the paper acknowledges this and shows fitting on closer-scale (1B) data restores high correlation, the claim that the law "reliably predicts optimal architectural choices" (abstract) needs the qualification that reliable prediction depends on fitting models within a similar size range to the target. The law does not extrapolate universally across large scale gaps.

3. **No variance or confidence intervals on downstream accuracy.** The headline improvements (e.g., Panda-1B's 57.0% vs 54.9%, Panda-3B's 62.5% vs 61.9%) are reported as single numbers without per-task breakdowns or confidence intervals in the main paper. Without knowing per-task variance, it is unclear whether the 0.6% gap at 3B is statistically significant across 9 tasks.

4. **Separability assumption validation is deferred.** The core formulation (Eq. 3) assumes separable effects of $d_{\text{model}}/\sqrt{N}$ and $r$ on loss. The paper notes that joint non-separable formulations were tested and did not improve performance (line 237, referring to Appendix J). However, the paper does not quantify how much the predicted optima would shift under a joint model in the main text. While the appendix likely contains this analysis in the original submission, the main text's treatment of this foundational assumption is thin.

### Trivial

5. **Presentation of accuracy gains.** The abstract states "up to 2.1% higher accuracy" for an absolute improvement of 2.1 percentage points (57.0% vs 54.9%). This usage is conventional in ML but is ambiguous (the relative improvement is 3.8%). Similarly, the "42% higher inference throughput" is a peak value at specific batch sizes on A100; the paper does report ranges elsewhere but the headline figure lacks this context.

## Nice-to-Haves

- A sensitivity analysis showing how much the predicted optimal $d_{\text{model}}/\sqrt{N}$ and $r$ change under the non-separable formulation vs. the separable one, to directly validate the separability assumption in the main paper.
- Discussion of whether the architectural recommendations would change under longer training horizons (e.g., Chinchilla-optimal token budgets rather than the 5× regime used here).

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Separability assumption "under-justified" with criticism about joint formulation being in appendix.** The reviewer claimed the joint formulation results are missing. The appendix exists in the original submission; the parser strips it. The paper explicitly states joint formulations were tested and did not improve performance. The conceptual concern about separability is kept (Weakness 4, Minor), but the criticism about missing appendix content is removed per hard rules.
- **LLaMA-3.2 comparison framing as "misleading."** The paper clearly states it retrains LLaMA-3.2 architecture variants under its own setup (Section 4), using phrases like "open-weight LLaMA-3.2-1B baseline configs." The comparison is properly scoped.
- **"42% higher inference throughput needs qualification" / "What happens at longer training horizons?"** The paper already says "up to 42%" and provides cross-hardware/framework ablation. Longer-training questions are outside the paper's stated scope. Demoted to nice-to-have or removed.
- **"2.1% vs 2.1 percentage points" as a major issue.** Standard usage in ML literature. Kept only as a trivial presentation note.
- **Strength Finder's generic strengths** (e.g., "addressed an important problem," "targeted an interesting question") — dropped as not specific enough.
- **Criticism that the paper "overstates limitations of prior work" (Bian et al.).** The paper's criticism of Bian et al. is specific and valid (only aspect ratio, no hidden size or GQA). Not a valid weakness.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Resolve the training token budget inconsistency: clarify whether the $100N_{\text{non-emb}}$ rule applies to all model sizes or only those up to 1B, and if a fixed 100B cap was used for 3B models, state this explicitly with justification.
2. Add per-task breakdowns or confidence intervals for the downstream accuracy results in the main paper, especially for the 3B comparison where the gap is only 0.6% absolute.
3. Present a direct comparison of the separable model's predicted optima vs. a non-separable joint model in the main paper to validate the separability assumption.
4. Qualify the "reliably predicts" claim in the abstract to reflect that the law's predictive accuracy depends on fitting models at a similar scale to the target.

## Score and Decision

**Calibration anchors:**

*Round 1 — Bracketing:*
| Anchor | Score | Relevance | Comparison |
|--------|-------|-----------|------------|
| FiRST (Router-Selective Transformers) | 3.00 | Latency reduction | Much weaker; our paper has far more empirical scope and clearer contribution |
| MixAttention | 2.00 | KV-cache reduction | Much weaker |
| Ternary LM at Scale | 2.86 | Ternary quantization | Different topic, lower quality |
| Efficient Deploying LLMs with Risk | 3.00 | Risk-controlled deployment | Much weaker |
| **Language models scale reliably with over-training** | **6.50** | **Chinchilla extension, 104 models, held-out eval** | **Topically closest. Our paper has larger max scale (3B vs 6.9B but trained more models), downstream evaluations, and concrete architectural findings. Comparable or slightly stronger.** |
| Scaling Laws for Downstream Performance | 4.25 | Downstream prediction | Weaker; less rigorous validation |
| Hitchhiker's Guide to Scaling Laws | 5.20 | Scaling law best practices | Our paper has stronger novel contribution |
| Bayesian scaling laws for ICL | 6.00 | ICL scaling | Less directly relevant |
| **Scaling Laws for Precision** | **8.00** | **Precision-aware scaling** | **Cleaner execution with no methodological concerns. Our paper has a token budget inconsistency and weaker 3B extrapolation, preventing this tier.** |

*Round 2 — Narrowing:*
| Anchor | Score | Relevance | Comparison |
|--------|-------|-----------|------------|
| **Rethinking Sparse Scaling** | **6.67** | **Chinchilla extension, sparse pretraining** | **Very relevant. Similar profile (extends Chinchilla, 80+ configs). Our paper has larger scale (3B vs 500M), downstream evaluations, but has the token budget inconsistency.** |
| Not All Attention is Needed | 5.50 | Layer pruning | Weaker; limited novelty |
| Learning How Hard to Think | 6.50 | Adaptive compute allocation | Different topic |
| CoreInfer | 6.25 | Sparse activation inference | Different topic |
| W-PCA for Lightweight LMs | 6.75 | NAS for LMs | Different methodology |

**Round 1 bracket:** 5.5–7.0

**Round 2 analysis:** The two most topically similar anchors — "Language models scale reliably with over-training" (6.50) and "Rethinking Sparse Scaling" (6.67) — are accepted papers with comparable methodology (Chinchilla extension, extensive empirical sweeps). Our paper compares favorably on several dimensions (larger max parameter scale for fitting data, downstream evaluations, concrete architectural findings, cross-hardware validation) but has one concrete unresolved issue (training token budget inconsistency) and a meaningful limitation (weak extrapolation across large scale gaps). These prevent it from reaching the 7+ tier where papers like "Scaling Laws for Precision" (8.00) sit with no methodological concerns raised. Our paper sits below the 6.50–6.67 anchors due to the unresolved inconsistency, but above the 5.0–5.5 range where papers have more fundamental weaknesses.

**Final Score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>