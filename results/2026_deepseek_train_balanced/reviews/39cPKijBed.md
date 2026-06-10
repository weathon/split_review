## Summary

This paper proposes Time-dependent Importance reWeighting (TIW), a method for training diffusion models on biased datasets when a small unbiased reference set is available. The key idea is to estimate a **time-dependent** density ratio between perturbed biased and unbiased distributions (using a time-conditioned discriminator), then use this ratio both as a reweighting term and as a score-correction term in the denoising score-matching objective. Theorem 1 proves this objective is equivalent to standard score-matching on the unbiased distribution up to a constant. Experiments on CIFAR-10/100 (long-tail), FFHQ (gender skew), and CelebA (gender+hair-color bias) show improvements over time-independent importance reweighting (IW-DSM) and other baselines.

## Strengths

- **Theorem 1 and its corollary** (Section 3.2, Eq. 8): The paper provides a clean theoretical proof that the proposed TIW-DSM objective is equivalent to standard score-matching on the *unbiased* distribution up to a constant, with a corollary guaranteeing that the optimal score network recovers $\nabla\log p_{\text{data}}^t$. This is non-trivial and gives a rigorous foundation for the method.

- **Clear diagnostic motivation via 2D toy experiment** (Section 3.1, Figure 2): The controlled toy example quantitatively demonstrates that time-dependent density ratio estimation reduces integrated MSE to 39.1% of the time-independent baseline. The visualization of overconfident vs. well-calibrated discriminator predictions at different diffusion times directly supports the paper's central claim about why time-dependent estimation helps.

- **Strong empirical results on constructed-bias settings**: On CIFAR-10 LT with 5% reference, TIW-DSM achieves FID 11.51 vs. IW-DSM 15.79 (—4.28 gap) and DSM(obs) 12.99. On CIFAR-100 LT and FFHQ (80%/90% gender skew), the improvements are consistent across all reference sizes. These are clean settings where the bias is known and controlled, and the gains are substantial.

- **Diagnostic analysis of why IW-DSM fails** (Section 4.4, Figure 7): The histogram showing >75% of $D_{\text{bias}}$ samples receive weight <0.01 at $\sigma(t)=0$ but receive meaningful weights at larger $t$ provides direct mechanistic evidence for why time-independent reweighting underperforms. This both explains the baseline's failure and reinforces the paper's core insight.

## Weaknesses

### Major

- **No error bars, confidence intervals, or multiple-seed results anywhere in the paper.** Every experimental claim — including FID differences as small as 0.03 (CelebA: 2.40 vs. 2.43) and ablation margins of 0.07–0.16 — rests on single-run point estimates. Given that FID is known to have non-negligible variance across training seeds and sampling seeds, the absence of any uncertainty quantification makes it impossible to assess whether the reported improvements are statistically reliable. This is particularly problematic for the CelebA experiment (see below) and the ablation comparisons.

- **CelebA benchmark results are weak and somewhat ambiguous.** The true subgroup proportions are (46.5/29.6/11.5/12.4). TIW-DSM produces (31.0/27.8/20.1/21.1). While TIW-DSM achieves the best FID (2.40), its latent statistics over-correct the bias: it systematically over-represents the minority subgroups (F-B and M-B) at the expense of the majority (F-NB). The total absolute deviation from true proportions is 34.6 for TIW-DSM vs. 37.0 for DSM(ref) — a modest difference. Moreover, the FID gap between TIW-DSM (2.40) and IW-DSM (2.43) is 0.03, which is within the typical noise range for single-run FID evaluations. The paper's claim of "mitigating the bias that actually exists in the common benchmark" is qualitatively supported but quantitatively weak.

- **Discriminator architecture, training cost, and interaction with score model training are not reported.** The method requires training a separate time-conditional discriminator $d_\phi(x_t, t)$ on perturbed data from both $D_{\text{ref}}$ and $D_{\text{bias}}$ across the full diffusion time range. The paper provides no details about: (a) the discriminator's architecture (size relative to the score network, input embedding for time, number of parameters), (b) its training procedure (number of iterations, learning rate, whether it's trained before or jointly with the score model), (c) the total compute overhead. These are needed to assess practical utility and reproducibility.

### Minor

- **The ablation study shows the reweighting term contributes little beyond score correction alone.** From Table 4.3: Full (W+C) vs. C-only yields FID differences of {0.11, 0.07, —0.16, 0.08} across the four reference sizes, with C-only actually *better* at 25% reference. The W-only variant at small reference sizes performs *worse* than DSM(obs) (13.27 vs. 12.99 at 5%). The paper accurately reports these numbers and acknowledges that C-only "showed quite good results," but the framing as "dual roles" overstates the contribution of the weighting term. The genuine innovation is the time-dependent score correction; the reweighting is at most a secondary benefit. The paper would benefit from acknowledging this more directly.

- **Different $\alpha$ sweep ranges for TIW-DSM and IW-DSM in the bias-FID tradeoff experiment** (Figure 6, caption): TIW-DSM sweeps $\alpha \in \{0.25,0.5,1,2,2.5\}$ while IW-DSM sweeps $\alpha \in \{0.125,0.5,0.25,1\}$. The different ranges and the non-monotonic ordering of the IW-DSM set make direct comparison harder to interpret. A shared sweep with overlapping values would be cleaner.

- **The score-correction identity derivation (Eq. 9 vs. Eq. 8) is described succinctly but requires careful reading.** The connection between the score-matching objective on $p_{\text{bias}}^t$ with the correction term and the denoising objective could be expanded slightly, especially noting that the optimality guarantee (Corollary 1) assumes the *exact* density ratio $w_{\phi^*}^t$, while in practice an estimate is used, and the effect of this estimation error is not characterized.

### Trivial

- The $\alpha$ sweep set for IW-DSM is listed as $\{0.125,0.5,0.25,1\}$ — the ordering is non-monotonic, suggesting either a typo or inconsistent formatting.
- The caption for Table 4.3 has a typo in "ablation."

## Nice-to-Haves

- Reporting results with at least 3 random seeds and showing mean ± std for FID would greatly strengthen the paper's empirical claims.
- Adding a table comparing discriminator size, training cost (GPU-hours), and number of parameters to the score network would help practitioners assess the overhead.
- The CelebA analysis could be enhanced by including additional metrics beyond FID (e.g., FID per subgroup, or distribution-level distance metrics) to corroborate the debiasing claim.

## Removed Points

These are flagged for removal; treat with caution.

1. **Criticism that reweighting term being superfluous "undermines the claimed dual-role contribution" (Harsh Critic, point 1)** — The paper's core contribution is the time-dependent density ratio. The ablation data is transparently reported. The claim that both components together "perform best in most cases" is factually accurate (3 of 4 settings). The critic overstates the framing issue. Nevertheless, the observation that C-only nearly matches the full method is retained as a Minor weakness above.

2. **"The practical feasibility of the time-dependent discriminator is not discussed" framed as a critical issue** — Retained in modified form (Major weakness about missing architecture/training details) but the framing as a fatal flaw is removed. Missing implementation details are a reproducibility concern, not a fatal flaw.

3. **Claim that DSM(ref) is "arguably closer to the true distribution" than TIW-DSM on CelebA** — The total absolute deviation from true proportions is 34.6 (TIW-DSM) vs. 37.0 (DSM(ref)). TIW-DSM is closer overall, though the critic's observation that DSM(ref) is closer on 2 of 4 individual subgroups is factually correct. Modified accordingly in the retained weakness.

4. **Strength Finder strength #3 (ablation study listed as a strength)** — The ablation data is informative and worth keeping as evidence that the paper provides transparent analysis. It does not directly conflict with the weakness since both accurately describe the same data from different perspectives.

## Novel Insights

The harsh critic's observation that the score-correction-only ablation nearly matches the full method, combined with the density-ratio analysis (Figure 7), yields an insight not fully articulated in the paper: the main failure mode of IW-DSM is that its density ratio at $t=0$ is degenerate (most weights near zero), and the score-correction mechanism — enabled by the *time-dependent* density ratio — is what actually fixes the objective. The reweighting term is secondary because the score-correction identity $(\nabla\log w^t_\phi)$ is what structurally transforms the biased-data objective into the unbiased-data objective. This suggests that future work should focus on improving the time-dependent score correction rather than the reweighting mechanism.

None beyond the paper's own contributions and the synthesized insight above.

## Suggestions

1. **Add multi-seed results with error bars** for all main experiments, particularly the ablation study and CelebA benchmark. Without these, the reported improvements at the 0.03–0.16 FID level cannot be distinguished from noise.

2. **Provide full discriminator details** in the main text or appendix: architecture, parameter count, training procedure, compute budget, and whether it is trained jointly or pre-trained.

3. **Re-center the narrative** around time-dependent score correction rather than "importance reweighting." The ablation evidence shows the weighting term contributes marginally; the score correction is the engine. A name like "Time-Dependent Score Correction for Debiased Diffusion Models" would better reflect what the method actually does.

4. **Re-evaluate the CelebA experiment**: either run multiple seeds to establish whether the 2.40 vs. 2.43 gap is real, or add additional quantitative metrics (per-subgroup FID, Coverage, etc.) to support the claim of debiasing. Consider discussing why the latent proportions over-correct relative to the true distribution.

5. **Use consistent $\alpha$ sweep ranges** for the tradeoff analysis to enable fair visual comparison.

## Score and Decision

The paper makes a real and well-motivated contribution: showing that time-dependent density ratio estimation alleviates the density-chasm problem in debiasing diffusion models, and proving that the resulting objective is equivalent to score-matching on the unbiased distribution. The CIFAR and FFHQ experiments are strong. However, the absence of any error bars, the weak and ambiguous CelebA results, the missing discriminator details, and the ablation showing the reweighting term is nearly superfluous all prevent the paper from meeting the full bar of a top venue in its current form. The core idea is publishable but needs strengthening.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>