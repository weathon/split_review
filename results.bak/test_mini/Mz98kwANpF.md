Now I have sufficient calibration data. Let me compile the final review.

**Calibration Summary:**
- Round 1 bracket: I initially bracketed this between 3.5 and 7.5
- Round 2 narrowed it to 4.0-5.5 based on comparison with mtLoRA (5.50, Accept), MeTA-LoRA (4.50, Reject), ThanoRA (4.00, Reject), PEML (4.00, Reject)
- Final score: 5.0 — the paper is notably stronger than the 4.0 reject papers, but weaker than mtLoRA (5.50, accepted) due to the lack of variance reporting.

Here is my full review.

---

## Summary

This paper challenges the prevailing paradigm in multi-task LoRA that advocates for architectural diversity and separation of task-specific knowledge. Through a series of empirical experiments, the authors first show that M-LoRA—a simplified multi-head variant with high inter-head similarity—outperforms diversity-enforcing methods like R-LoRA and HydraLoRA. They further demonstrate that a standard single-adapter LoRA with sufficiently increased rank matches or exceeds the performance of complex multi-component architectures. Motivated by these findings, the authors propose Align-LoRA, which adds an explicit alignment loss (KL divergence or MK-MMD) to encourage task-shared representations in the low-rank space. Experiments on multiple model families (Qwen2.5, LLaMA2, LLaMA3) at various scales (3B–14B) show that Align-LoRA consistently outperforms baselines while using fewer trainable parameters and incurring zero inference overhead.

## Strengths

**1. Counter-intuitive finding that directly challenges an active research direction.** The paper presents compelling evidence (Figure 2, Table 1) that M-LoRA achieves the highest inter-head cosine similarity (~0.85) while simultaneously achieving the best performance (75.45 avg vs. R-LoRA's 74.67 and HydraLoRA's 74.04). This directly contradicts the diversity-enforcing philosophy of methods like R-LoRA and provides a well-supported refutation of a widely-held assumption in the multi-task LoRA community.

**2. Clean demonstration that multi-component architectures may be unnecessary.** Tables 2 and 3 systematically show that a standard single-adapter LoRA with rank scaled to match parameter counts (e.g., LoRA† rank=30 on LLaMA2-7B: 42.21 vs. R-LoRA 42.24; LoRA^10 on Qwen2.5-7B: 49.51 vs. R-LoRA 49.51) achieves competitive or superior performance. This is a simple but important sanity check for the field.

**3. Strong empirical results for Align-LoRA across multiple model families and scales.** Table 4 shows consistent gains: A-LoRA-K achieves 50.28 vs. next-best 48.44 on Qwen2.5-7B BBH, and 48.84 vs. 45.42 on LLaMA3-8B BBH, all with fewer parameters (0.20% vs. 0.25%). Table 5 corroborates these results on an 8-task benchmark at both 3B and 7B scales. The consistent pattern across 3 model families, 3 model scales, and 2 benchmarks is genuinely impressive.

**4. Robustness of the alignment principle validated through two distinct metrics.** Both A-LoRA-K (KL divergence) and A-LoRA-M (MK-MMD) improve upon baselines, showing the effect is not an artifact of a specific statistical distance. The hyperparameter λ sensitivity analysis (Figure 3) shows robust performance across a 50× range (0.01 to 0.50).

**5. Practical zero-overhead advantage is explicit.** Align-LoRA introduces no additional modules at inference time—it merges completely into the backbone—unlike MoE-based multi-component variants whose routers prevent merging. This practical benefit is clearly articulated and quantified.

## Weaknesses

### Fatal
None.

### Major

**1. No statistical significance or variance reporting across any experimental result.** Not a single standard deviation, confidence interval, or indication of multiple runs is reported in any table or figure in the main text. Given that some per-task improvements are modest (e.g., A-LoRA-K's 0.64-point gain over M-LoRA on Task 6 of Table 5 with Qwen2.5-3B), the reader cannot determine whether these reflect genuine superiority or random variation. This is the most significant weakness: the paper's core claims rest entirely on point estimates. The paper would be substantially strengthened by reporting results over at least 3 seeds with means and standard deviations.

**2. Missing direct same-rank ablation of the alignment loss.** In Table 4, A-LoRA-K (rank 8, 0.20% params) is compared against LoRA (rank 10, 0.25% params). While showing that A-LoRA-K with fewer parameters outperforms a higher-rank LoRA is a stronger result, the clean ablation—LoRA rank 8 vs. A-LoRA-K rank 8, holding rank constant—is not presented in the main text. Without this, a skeptical reader could question whether the improvement is partly attributable to architectural differences beyond the alignment loss itself. (Note: LoRA rank 8 results do appear in the *different* experimental setup of Table 3, but the direct ablation within the same setup used for Table 4 is absent.)

### Minor

**3. The theoretical analysis (Section 5.3) is an incremental application of standard bounds.** The generalization bound in Section 5.3 is a straightforward adaptation of domain adaptation bounds (Ben-David et al., 2006) to the multi-task LoRA setting. The insight that minimizing distribution discrepancy Δ(D_i, D_j) tightens the bound is exactly what the method is designed to do, so the bound provides a formal restatement rather than non-trivial theoretical insight. The paper fairly describes this as a "theoretical analysis" rather than overclaiming, but calling it a "novel generalization bound" is overstated.

**4. The Gaussian assumption for task representations is not justified or tested.** The alignment loss models batch-wise task representations as multivariate Gaussians with diagonal covariance (Section 5.1). This is computationally convenient but no justification is given for why representations in the low-rank space would be Gaussian. A sensitivity analysis to this assumption (e.g., comparing with non-parametric alternatives) or discussing potential failure cases (small batch sizes, non-Gaussian representations) would strengthen the method's credibility.

**5. The M-LoRA head count is not stated in Section 3.** The paper refers to M-LoRA having "multiple B heads" but does not specify the number of heads used. (Presumably it follows R-LoRA's configuration, but this should be stated explicitly.)

### Trivial
None.

## Nice-to-Haves
- Provide a quantitative measure of distribution alignment during training (e.g., plot pairwise KL divergence over training steps) to verify that ℒ_align actually reduces cross-task distribution discrepancy and correlate this with downstream performance.
- Include a discussion of how tasks are batched for the alignment loss computation, particularly when batch sizes per task are small and empirical mean/variance estimates may be noisy.
- The paper would benefit from analysis on more heterogeneous task mixtures (e.g., mixing generation and classification tasks) to test the limits of the alignment approach.

## Removed Points

The following points from the input reviews were removed:

- **"No statistical significance... the single most important weakness... non-negotiable"** — Retained as a Major weakness (it is real), but downgraded from the critic's "non-negotiable rejection" framing. Single-seed reporting is common practice in LLM fine-tuning papers due to computational cost; it weakens the paper but is not automatically fatal. Retained in weakened form as Weakness #1.

- **"The alignment loss is not directly ablated against the same-rank LoRA baseline"** — Retained as Weakness #2 but significantly weakened. The paper's comparison (A-LoRA-K rank 8 outperforming LoRA rank 10) is *stronger* than a same-rank comparison would be, not weaker. The missing comparison is a completeness issue, not a validity threat.

- **"The theoretical analysis is incremental... does not strengthen the paper's contribution"** — Retained as Minor weakness #3. The bound is indeed standard and the claim of "novel" is overstatement, but this does not threaten the paper's core claims.

- **Reproducibility nitpicks about undisclosed hyperparameters** — Removed per hard rules. The paper states implementation details are in Appendix G, which the parser removed.

- **"The M-LoRA variant is a reasonable ablation... the improvement is modest"** — This is an observation, not a weakness. Removed.

- **"Missing appendix" concerns** — Removed per hard rules (parser strips appendices).

- **"Strength: Theoretical generalization bound directly motivates the method"** — Removed from strengths, as the bound contributes little beyond what the method already does by design.

- **Generic/unsupported strengths from Strength Finder** — Several strengths that were generic ("addressed an important problem") or sycophantic were removed.

## Novel Insights

The strongest synthesis insight from the review input is that the paper's narrative arc—starting from a surprising empirical observation (diversity hurts), testing its limits (rank scaling matches multi-component), and then building a method on the revised hypothesis—is fundamentally sound and well-executed. However, the evidential floor is lower than it should be for the strength of the claims made. The paper is essentially telling two stories with different evidential standards: the "diversity is not needed" observation is robustly supported by multiple converging lines of evidence (similarity analysis, rank scaling, M-LoRA performance), but the "alignment actively helps" claim rests on point estimates without variance. These two parts should be decoupled in evaluation.

## Suggestions

1. **Report error bars.** Add results over at least 3 random seeds with means and standard deviations for all tables. This is the single change that would most strengthen the paper.
2. **Add a direct same-rank ablation for Table 4.** Report "LoRA (rank=8, 0.20%)" alongside A-LoRA-K (rank=8, 0.20%) in the same experimental setup.
3. **Tone down the "novel generalization bound" claim.** Describe Section 5.3 as a theoretical motivation connecting alignment to generalization rather than a novel technical contribution.
4. **Acknowledge the Gaussian assumption** and discuss when it might break down (e.g., small per-task batch sizes during training).

## Score and Decision

**Score calibration details:**

| Anchor Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| RQUwj3HdUm (Task Matrices) | 2.50 | 1 | Significantly weaker; largely different topic |
| Wr1IDzjttB (ABMLL) | 2.00 | 1 | Significantly weaker |
| aiJtxcNbqB (MultiLoReFT) | 3.00 | 1 | Weaker; multimodal, less clean narrative |
| x5HDAixMaK (Kron-LoRA) | 2.00 | 1 | Significantly weaker |
| **L3RSb9yTlL (mtLoRA)** | **5.50** | **1,2** | **Most comparable. mtLoRA has more thorough evaluation and ablations, but the current paper has a cleaner narrative. Current paper is slightly weaker (~0.5 pts) due to lack of variance reporting.** |
| x6c72680uD (MeTA-LoRA) | 4.50 | 1,2 | Current paper is notably stronger—clearer narrative, better empirical scope, simpler method |
| 6XoyxxAfv3 (ThanoRA) | 4.00 | 1,2 | Current paper is stronger—more model families, cleaner results |
| 2tgeU3xO1r (World Reps) | 4.50 | 1 | Different topic |
| lnH5YFPcxZ (PEML) | 4.00 | 2 | Current paper is stronger—better results, cleaner method, no expensive NAS |
| M4t2JUMlfI (Neural Collapse) | 6.50 | 2 | Different topic (theoretical), not comparable |
| pZj2DhfaVD (EWC-LoRA) | 6.00 | 2 | Stronger empirical methodology, but different topic (continual learning) |

**Round 1 bracket:** The paper sits between the weak anchors (avg 2–3) and the strong anchors (avg 8), with the most relevant anchors in the 4.0–5.5 range. Initial bracket: 3.5–7.5, narrowed to 4.0–5.5.

**Round 2 narrowing:** After reading all 5 middle-band anchors in full, the paper is clearly stronger than MeTA-LoRA (4.50, Reject), ThanoRA (4.00, Reject), and PEML (4.00, Reject). It is somewhat weaker than mtLoRA (5.50, Accept Poster), which has more thorough evaluation and variance reporting. Final score of 5.0 reflects this positioning.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>