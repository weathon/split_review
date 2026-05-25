Now I have all the information I need. Let me compile the final authoritative review.

## Summary

This paper introduces PI-CCA, a replay-free continual learning method for vision-language models that preserves cross-modal alignment by storing a compact certificate of top-k canonical correlations and subspaces. During adaptation, it enforces spectral and subspace-angle consistency with this certificate using only mini-batch statistics, and improves prompt-robustness via averaging over prompt perturbations. The method achieves state-of-the-art results among replay-free methods across four VL-CL benchmarks (MTIL, X-TAIL, VLCL, ConStruct-VL), with thorough ablations confirming the contribution of each component.

## Strengths

- **State-of-the-art replay-free performance across diverse benchmarks.** Tables 1–2 show PI-CCA achieving the highest Avg/Last/Transfer on MTIL and X-TAIL, best I2T/T2I R@1 on VLCL, and best FA/AF on ConStruct-VL among all replay-free methods, even surpassing a synthetic-replay baseline (GIFT) on retrieval without storing or generating data. The improvements are consistent (≈1.6–2.3 p.p. over the next-best replay-free method on MTIL).

- **Comprehensive ablations confirm the necessity of each component.** Table 3 systematically removes each loss term: removing the spectral term (λ₁=0) drops MTIL Avg by 2.5 p.p., the subspace term (λ₂=0) by 2.2 p.p., and the prompt-invariance term (λ₃=0) by 1.5 p.p. The ablation also tests certificate EMA, covariance EMA, spectral moments, Hungarian vs. sorted pairing, and sketch type, showing each contributes meaningfully.

- **Demonstrated prompt-robustness mechanism.** Figure 4 provides clear evidence that the ℒ_pi loss flattens degradation under increasing perturbation strength. At s=1.0, PI-CCA improves R@1 by +2.44 p.p. (ID) / +2.51 p.p. (OOD) and reduces AF by ≈1.10 (ID) / 0.96 (OOD) relative to the variant without ℒ_pi, confirming the explicit invariance objective works.

- **Certificate-capacity Pareto analysis shows efficient design.** Figure 2 maps the (k,h) trade-off across 35 configurations, identifying (k=64, h=256) as a Pareto-knee that achieves 76.8 MTIL Avg with ≈1.2 GB peak memory and ≈320 ms step time, demonstrating the "small yet sufficient" certificate claim.

- **Robustness to task ordering.** Figure 5 shows narrow IQRs (≈0.4 p.p. for Avg, ≈0.5 p.p. for Last) over 20 random task orders, confirming that PI-CCA does not rely on a favorable order.

## Weaknesses

### Fatal
None.

### Major

1. **Reported perfect correlations in Figure 3 require explanation.** The scatter plots report Pearson r = 1.00 and Spearman ρ = 1.00 for subspace-angle drift vs. performance drop (two of four panels), and r = 0.99 / ρ = 1.00 for spectral drift. Exact 1.00 is suspicious for real data, even with two-decimal rounding, and the paper does not explain how such perfect fits arise. The sweep perturbs quantities (certificate size, EMA rates, loss weights) that simultaneously affect both the drift metrics and the performance metrics, raising the possibility of a mechanical/endogenous relationship rather than an independent causal link. This figure is presented as central evidence for the "geometry→performance" thesis. The authors should: (a) report the raw data and show residuals, (b) clarify whether these are rounded values, and (c) ideally run an independent evaluation (e.g., artificially perturbing the certificate at test time and measuring downstream performance) to break the endogenous link. Without clarification, this evidence for the causal claim is weakened.

2. **Baseline comparison setup is not disclosed.** The paper never states whether competing methods (ZSCL, Mod-X, C-CLIP, etc.) were re-implemented with the same backbone, LoRA adapters, and training budget, or whether numbers are taken from original papers that may use full fine-tuning, different backbones, or different prompt templates. Since PI-CCA uses LoRA (which itself regularizes and reduces forgetting), and since the gap to the next-best replay-free method on MTIL is only ≈1.6 p.p., the relative contributions of the certificate vs. the LoRA-based backbone become unclear. The paper should explicitly disclose the baseline-configuration protocol and, ideally, provide controlled comparisons with the same backbone/LoRA setup for the top baselines.

### Minor

1. **No variance estimates for Table 1 (MTIL / X-TAIL).** Unlike Table 2 (which reports ± intervals), Table 1 reports point estimates only, making it impossible to assess whether the reported gaps (e.g., 76.8 vs. 75.2) are statistically significant. The paper should at minimum report standard deviations over multiple seeds.

2. **"Constant-memory" phrasing is ambiguous.** The certificate itself is O(hk) and constant in d, but the method also maintains EMA covariance matrices Σ_vv, Σ_tt, Σ_vt of size O(d_v² + d_t² + d_v d_t), which are not constant. The abstract and contributions claim a "constant-memory path" / "constant-memory consolidation mechanism" without clarifying that this refers to the certificate. The text should explicitly state which components have constant memory and note the O(d²) streaming statistics.

3. **Eigen-decomposition of averaged sketched projectors (Eq. 6) is not analyzed.** The prompt-invariant certificate takes top-k eigenvectors of the *average* sketched projector. Averaging projectors does not commute with eigen-decomposition, so the approximation quality of this step relative to the true prompt-invariant canonical subspace is not quantified. A brief analysis or empirical validation would strengthen confidence.

4. **Hyperparameter values and selection procedure for λ₁, λ₂, λ₃, η, ξ, α, β are not justified in the main text.** While the paper references Appendix §A.3 for sensitivity analysis (stripped by parser — assumed to exist), the main text does not state whether these were fixed globally or tuned per benchmark, or what validation signal was used. This makes it harder to assess the risk of overfitting to the evaluation metrics.

5. **The sketch-based subspace loss (Eq. 10) is acknowledged as a heuristic surrogate but lacks formal justification in the main text.** The paper states that the Frobenius distance in sketch space is a "surrogate" and mentions near-isometric sketches. While this transparency is appreciated and the method works empirically, the connection to principal-angle preservation is asserted without a distortion bound or synthetic validation in the main body. This is acceptable as an empirical design choice but limits the theoretical grounding of the central subspace-preservation mechanism.

6. **The "model without certificate terms still outperforms many baselines" observation cuts in an ambiguous direction.** The critic noted that the ablated model (w/o spectral and subspace terms) still achieves 74.3 MTIL Avg, which beats several prior methods (e.g., ZSCL at 72.5). This can be read either as evidence that LoRA carries much of the performance (undermining the certificate's importance) or as evidence that the base training recipe is competitive and the certificate provides meaningful additive gains (2–3 p.p.). The paper would benefit from discussing this explicitly.

### Trivial

- The optimality condition for the sorted spectral pairing surrogate ("optimal for convex costs") is stated without citation or proof; this is a minor technical imprecision.
- The streaming whitening description mentions eigenvalue flooring and Newton–Schulz iteration but does not detail the effect on gradient propagation.
- The Pareto sweeps (Fig. 2) are not explicitly described as being run over the full multi-task sequence vs. a single-task proxy.

## Nice-to-Haves

- Controlled baseline experiments with identical backbone/LoRA configuration and training budget.
- Independent causal evidence for the geometry→performance link (e.g., direct certificate perturbation at test time rather than correlating drift with performance from the same sweep).
- A formal distortion bound (e.g., via Johnson–Lindenstrauss) or synthetic validation for the sketch-based subspace distance surrogate.
- Full hyperparameter sensitivity table (λ₁, λ₂, λ₃, η, ξ, α, β) in the main text or a prominently placed appendix reference.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Complaints about missing appendix content (A.3 sensitivity analysis, A.4 theory).** The harsh critic faults the paper for relegating theoretical analysis and sensitivity experiments to the appendix, which is not visible to the reviewer. Per the review guidelines, the parser strips appendix content from all papers; these sections exist in the original submission. Criticisms that the paper lacks theoretical guarantees or sensitivity analysis that are deferred to the appendix are therefore invalid as stated.
- **"The paper mentions 'performance drop on a held-out zero-shot suite' but does not report it in the main tables."** The paper states in §4.1 that PD is reported, and it appears as a metric in Figure 4. The level of detail is consistent with common practice.
- **Criticism that ablation drops are "modest" (2–3 points).** In continual learning benchmarks, 2–3 point improvements are standard and meaningful. Moreover, the ablations demonstrate that *each* component contributes, which is the paper's claim — the criticism that the gains are "small" is a matter of interpretation, not a flaw.
- **Point about "the model without any certificate terms still outperforms many baselines" as a weakness.** This confounds two separate aspects: the strength of the base training recipe (which is a systems-engineering choice, not a flaw) and the additive benefit of the certificate (which the ablations cleanly isolate). It is not a valid weakness of the paper.
- **"Missing related works" suggestion.** Per guidelines, missing related works cannot be evaluated without external sources.
- **Reproducibility nitpicks about trivial implementation details (e.g., exact optimizer settings, training logs).** These are standard to defer to the appendix and code release.

## Novel Insights

None beyond the paper's own contributions. The core conceptual insight — reframing forgetting as alignment-geometry drift and preserving CCA invariants via a compact certificate — is the paper's own contribution, and the reviews do not add a new perspective beyond validating its significance and noting some methodological concerns.

## Suggestions

1. **Clarify Figure 3.** Report correlations with more precision (e.g., r = 0.9997), provide residual plots, and ideally add an independent validation that breaks the endogenous link between drift metrics and performance metrics.
2. **Disclose baseline protocol.** State explicitly whether benchmark numbers are taken from original papers or re-computed, and if re-computed, share the configuration (backbone, LoRA, optimizer, LR schedule).
3. **Add variance to Table 1.** Provide standard deviations over at least three runs for MTIL and X-TAIL.
4. **Clarify "constant-memory" scope.** Precisely state that the certificate is O(hk) but the EMA covariances are O(d²), or discuss whether covariances can also be sketched.
5. **Include a brief analysis of the averaged-projector eigen-decomposition (Eq. 6).** Show empirically or theoretically that the top-k eigenvectors of the average sketched projector approximate the prompt-invariant canonical subspace.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>