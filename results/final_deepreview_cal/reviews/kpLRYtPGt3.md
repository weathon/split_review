## Summary

Neon introduces a post-hoc method for improving generative models by fine-tuning on self-generated synthetic data and then *reversing* the resulting parameter shift via negative extrapolation. The key insight is that mode-seeking inference samplers (temperature <1, top-k/p, CFG, finite-step ODE solvers) create a predictable anti-alignment between synthetic-data and real-data population gradients. Reversing the self-training update therefore reduces true-data risk. The method is architecture-agnostic, requires no auxiliary models, no inference modifications, and uses <1% additional training compute. Applied to xAR-L on ImageNet-256, Neon achieves a new SOTA FID of 1.02.

## Strengths

- **Elegant, counterintuitive core idea with strong empirical payoff.** The discovery that self-training degradation is a structured, anti-aligned signal that can be inverted — rather than mere noise — is genuinely novel. This is validated by the 2D Gaussian toy study (Figure 2), the Taylor-expansion analysis (Section 3.1), and consistent FID improvements across every tested architecture and dataset (Figures 3, 5, 7). The visual improvement in Figure 1 is striking.

- **Remarkable breadth of empirical validation.** Neon is demonstrated on diffusion (EDM-VP), flow matching, autoregressive (xAR, VAR), and few-step (IMM) models — four fundamentally different generative paradigms — across CIFAR-10, FFHQ-64, ImageNet-256, and ImageNet-512. This breadth strongly supports the claim of universality. The xAR-L result (1.28 → 1.02 FID, surpassing UCGM's 1.06) is particularly compelling.

- **Mechanistic insight through precision-recall decomposition.** Figure 4 and Figure 6 show that Neon systematically trades precision for recall, peaking near the FID optimum — exactly what the theory predicts (redistributing mass from over- to under-represented modes). This is not just a black-box improvement; the paper explains *how* it works.

- **Well-designed ablation studies.** Cross-architecture transfer (Figure 8: flow/IMM synthetic data improves EDM-VP), robustness to base model quality (Figure 9: Neon helps even models trained on 60% of real data), insensitivity to synthetic data quality (Figure 10: FID stays near-optimal across a wide γ range), and the CIFAR-10C null result (structured corruptions do not produce the anti-alignment signal) together provide strong evidence that the mechanism is specifically tied to self-generated mode-seeking bias.

- **Practical efficiency.** Neon uses as few as 1k synthetic samples for autoregressive models, <1% additional training compute in all settings, and requires no real data, no auxiliary models, and no inference modifications.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims are well-supported.

### Minor

- **Joint optimization of \(w\) and \(\gamma\) not fully decomposed for autoregressive models.** For the xAR and VAR results (Section 4.2), the reported FID comes from a joint grid search over the merge weight \(w\) and the classifier-free guidance scale \(\gamma\). The paper partially addresses this for VAR-d16 (Figure 6 shows \(\gamma\)-only optimization yields FID 3.01 vs. 2.01 with joint tuning), but does not report the best base-model FID achievable by re-tuning \(\gamma\) alone for xAR-L and xAR-B under the same grid. Since xAR-L's baseline FID of 1.28 was already reported with optimized CFG by Ren et al. (2025), this is unlikely to change the conclusion, but explicitly reporting it would cleanly isolate Neon's contribution. The paper would be stronger with a one-sentence note: "Re-tuning \(\gamma\) alone on the base xAR-L model under our grid yields FID X, confirming that most of the 1.28 → 1.02 improvement comes from Neon."

- **Theoretical guarantee for diffusion/flow models rests on the unverified A-MONO condition.** Theorem 2's applicability to diffusion and flow models depends on the curvature-density coupling condition A-MONO (footnote 2, Appendix B.7), which is not verified empirically or argued to be plausible beyond a brief statement. The abstract's phrasing "We prove that Neon works because…" could be read as claiming an unconditional guarantee. In practice the paper is transparent about the assumption (it appears explicitly in the footnote), but the framing in the abstract and contribution list slightly overpromises relative to what is actually proved. Adjusting the abstract to "We prove that, under natural assumptions, mode-seeking samplers induce anti-alignment…" would be more precise without weakening the contribution.

### Trivial

- Figure 4 caption has a small error: it states "\(w = -1\) corresponds to the model directly trained on synthetic data, i.e., \(\theta_{\text{Neon}} = \theta_r\)." In fact, \(w = -1\) gives \(\theta_{\text{Neon}} = \theta_s\), not \(\theta_r\). The description for \(w = 0\) is correct. This is clearly a typo in the caption and does not affect the interpretation of the figure.

## Nice-to-Haves

- A direct empirical measurement of anti-alignment (\(s = \langle r_d, P r_s \rangle\)) on a real model (e.g., approximating the population gradients on CIFAR-10 with a small EDM model) would bridge the theory and experiments more directly and turn the theoretical motivation into an empirically grounded mechanism.

- A head-to-head comparison against one directly competing self-training improvement method (e.g., DDO on the same EDM-VP CIFAR-10 checkpoint) would help readers calibrate Neon's practical advantage over prior work in the same problem space. However, this is not essential for the paper's contribution, since Neon's primary claims are about universality and simplicity (not about beating DDO at its own game), and DDO cannot even be applied to flow matching or IMM.

- A principled heuristic for selecting \(w\) without access to real-data features (e.g., monitoring divergence during synthetic fine-tuning) would make Neon deployable in settings where FID cannot be computed.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Missing comparison to DDO/SIMS is a structural gap in experimental design" (Harsh Critic).** REMOVED as a major/fatal concern. The paper distinguishes Neon from these methods conceptually (no inference modifications, architecture-agnostic, no auxiliary models) and positions its contribution as introducing a new paradigm rather than beating specific prior methods. A direct comparison would be a nice-to-have, not a prerequisite for validating Neon's core claims. Furthermore, DDO cannot be applied to flow matching or IMM, so a universal comparison is impossible.

- **"The co-optimization issue looms large / could shift the paper's quantitative conclusions" (Harsh Critic).** DEMOTED to Minor. The paper addresses this for VAR-d16, and the magnitude of improvement (especially xAR-L's 1.28 → 1.02, surpassing the previous SOTA of 1.06) makes it highly unlikely that CFG re-tuning alone accounts for most of the gain.

- **"The theoretical guarantee is conditional on an unverified assumption and does not directly explain the full method" — framed as a serious evidential gap (Harsh Critic).** DEMOTED to Minor. The paper explicitly states the A-MONO assumption in a footnote. The theory functions as a well-structured motivation; the empirical results stand independently.

- **"Figure 9's claim that Neon can compensate for a 40% reduction in real data is slightly oversold" (Harsh Critic).** REMOVED. The paper states the result carefully: "a model trained on only 30k real samples (FID 1.87) and improved with Neon nearly matches the baseline model trained on the full 50k dataset (FID 1.85)." This is a factual statement about what was observed and is not presented as a claim that Neon *replaces* real data better than all other methods.

- **Generic strength claims from the Strength Finder** (e.g., "the paper addressed an important problem," "the paper targeted an interesting question"). REMOVED as too generic.

## Novel Insights

The most genuinely novel insight from this paper — beyond its own stated contributions — is the reframing of model collapse as a *structured diagnostic signal*. Rather than treating self-training degradation as a pathology to be avoided, Neon shows it is a predictable consequence of mode-seeking inference that reveals precisely where the model's probability mass is concentrated versus where it should be. This inverts the conventional wisdom about synthetic data: the very property that makes naïve self-training fail (mode-seeking bias) is what makes the degradation direction informative. This perspective may generalize beyond generative models to any setting where inference procedures introduce systematic biases that manifest in fine-tuning trajectories.

## Suggestions

- Add a one-sentence note reporting the best base-model FID achievable by re-tuning \(\gamma\) alone for xAR-L under the same grid search protocol, to cleanly isolate Neon's contribution.
- Soften the abstract's "We prove that Neon works" to "We prove that, under natural conditions, mode-seeking samplers induce anti-alignment…" to accurately reflect the conditional nature of the diffusion/flow-matching result.
- Fix the Figure 4 caption: \(w = -1\) corresponds to \(\theta_s\), not \(\theta_r\).
- Consider a small-scale experiment measuring \(s = \langle r_d, P r_s \rangle\) empirically on a CIFAR-10 model to directly validate the anti-alignment claim.

## Score and Decision

**Bracketing (Round 1):** Searched across three score bands on topics related to self-training, synthetic data, generative model improvement, and parameter extrapolation. Compared against anchors:
- Low band: TJHB4ySVZM (3.40, rejected) — Neon is dramatically stronger.
- Middle band: svIdLLZpsA (6.00, accepted), 2o58Mbqkd2 (7.33, accepted) — Neon is clearly stronger than both in originality, breadth, and empirical quality.
- High band: et5l9qPUhm (8.00, rejected), WJaUkwci9o (8.00, accepted), 6O3Q6AFUTu (8.00, accepted) — Neon is comparable to or stronger than these.

**Narrowing (Round 2):** Pulled anchors in (6.0, 8.5). Compared against:
- 2o58Mbqkd2 "SuperDiff" (7.33, accepted) — Neon has broader validation and cleaner results.
- et5l9qPUhm "Strong Model Collapse" (8.00, rejected) — Neon has substantially more practical impact.
- WJaUkwci9o "Self-Improvement/Sharpening" (8.00, accepted) — Both have novel theoretical frameworks; Neon has far more extensive empirical validation.
- 6O3Q6AFUTu "NoiseDiffusion" (8.00, accepted) — Comparable originality; Neon's evaluation is significantly broader.

Neon sits at the strong end of the 8.0 band: its combination of a novel, counterintuitive idea, theoretical motivation, SOTA empirical results, and comprehensive ablations across four model families places it among the strongest papers in its cohort. The verified weaknesses (joint optimization not fully decomposed, A-MONO assumption not verified, figure caption typo) are genuine but minor.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>