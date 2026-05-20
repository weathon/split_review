Now I have a thorough understanding of the paper, the reviews, and the calibration anchors. Let me write the final consolidated review.

---

## Summary

This paper introduces Neon (Negative Extrapolation from Self-Training), a remarkably simple post-hoc method that improves generative image models by: (i) briefly fine-tuning on the model's own synthetic data to obtain degraded weights θ_s, then (ii) extrapolating *away* from those degraded weights via θ_Neon = θ_r − w(θ_s − θ_r). The method is supported by a theoretical proof that mode-seeking inference samplers (temperature < 1, CFG, top‑k, finite-step ODE solvers) create anti-alignment between synthetic-data gradients and real-data population gradients, making negative extrapolation reduce the true data risk. Empirically, Neon yields consistent FID improvements across four model families (diffusion, flow matching, autoregressive, few-step) on CIFAR-10, FFHQ, and ImageNet, including a state-of-the-art FID of 1.02 on ImageNet-256 for the xAR-L model using only 0.36% additional compute.

## Strengths

- **Extreme simplicity with no architectural or inference overhead.** Neon requires only a single round of synthetic data generation, brief fine-tuning, and a post-hoc parameter merge. No auxiliary models, no inference-time modifications, no likelihood computations, and the method works identically across all tested architectures. This is a clean, elegant contribution.

- **Consistent, large improvements across four model families on three datasets.** The paper demonstrates FID gains on diffusion (EDM-VP: 1.78→1.38 on CIFAR-10, 2.39→1.12 on FFHQ-64), flow matching (3.5→2.32), autoregressive (xAR-L: 1.28→1.02, surpassing UCGM's 1.06), and few-step models (IMM: 4-step FID nearly matching 8-step baseline). The 1.02 FID on ImageNet-256 for xAR-L is a genuine new state-of-the-art for that architecture.

- **Principled theoretical grounding.** Theorems 1 and 2 connect mode-seeking samplers to anti-alignment (cos φ < 0) and establish sufficient conditions for Neon's improvement. The analysis goes well beyond intuition: it formally characterizes when interpolation (w < 0) is needed versus extrapolation (w > 0), and the toy Gaussian visualization (Figure 2) makes the geometric intuition accessible.

- **Precision-recall analysis convincingly explains the mechanism.** Figures 4 and 6 show that Neon trades precision for recall by redistributing probability mass, correcting the mode-seeking bias of common samplers. The joint tuning of w and CFG scale γ (Figure 6) reveals that these parameters control complementary dimensions of the precision-recall frontier.

- **Cross-architecture transferability and robustness.** Section 4.4 demonstrates that synthetic data from one architecture (flow matching, IMM) improves another (EDM-VP), with theoretical justification in Appendix B.8. Figures 9-10 show robustness to base model quality and synthetic data quality, making the method practical.

## Weaknesses

### Fatal
None.

### Major

- **Selection of the extrapolation weight w requires FID computation on real data, partially undermining the "no additional real data" claim.** The paper states in line 183 that 10k real samples are used for hyperparameter search over w, and Figure 4 shows FID varies substantially with w. The paper's headline claim of "requires no additional real data" and "requires no access to the original training data" is technically about *training* data, but the method as evaluated cannot work without a real validation set to tune w. A truly data-free evaluation (e.g., fixed w=1 across all experiments) is never reported, making it unclear whether the method would succeed when no real data is available for tuning. This is the paper's most significant unresolved gap.

- **No direct experimental comparison against existing self-improvement methods.** The related work discusses DDO, SIMS, Discriminator Guidance, and Self-Play Fine-Tuning, yet none of these are compared on the same benchmarks. For instance, DDO (Zheng et al., 2025) reports FID improvements on autoregressive models — the paper does not show whether Neon outperforms DDO on xAR-L or VAR. While the paper correctly notes that some of these methods are architecture-specific (e.g., DDO requires likelihood-based models), a comparison on the overlapping architecture class would be the most straightforward way to substantiate the claimed advantage. Without this, the contribution's incremental value over prior self-training methods is unclear.

### Minor

- **No random-direction ablation to verify that the synthetic-fine-tuning direction is special.** The paper claims that the direction θ_s − θ_r is anti-aligned with the real-data gradient, but never tests whether a random direction of the same norm in parameter space produces comparable gains. The CIFAR-10C ablation (corrupted real images show no improvement) partially addresses the concern, but a random-weight-direction control is the most direct test of the claimed mechanism and is absent.

- **The theoretical sufficient conditions (small model error ‖ε‖ and negative cos φ) are not verified in the experimental setups.** The paper acknowledges this by testing beyond the theory's regime (Figure 9 shows Neon works even when the base model is far from optimal), and notes the theory provides sufficient conditions, not necessary ones. Still, key quantities like the alignment s = ⟨r_d, P r_s⟩ are never measured in experiments, leaving a gap between theory and empirical practice.

### Trivial

- Figure 4 caption contains a likely error: "w = −1 corresponds to the model directly trained on synthetic data, i.e., θ_Neon = θ_r" — from Equation (2), w = −1 gives θ_Neon = θ_s, not θ_r. While this may be a parser artifact, the inaccuracy should be corrected.

- The FID-optimal w in Figure 4 appears to be approximately −0.5 (consistent with the caption's w-axis labeling), but the paper elsewhere discusses w > 0 for "negative extrapolation." The negative sign convention for w is correct (Equation 2), but the notation could cause confusion without careful reading.

## Nice-to-Haves

- Reporting results with a fixed default w (e.g., w=1) across all benchmarks would help assess whether the method is usable in truly data-free settings.
- A direct comparison against DDO on xAR-L (or another overlapping architecture) would significantly strengthen the positioning.
- A random-direction baseline in weight space (same norm as θ_s − θ_r) would cleanly verify the claimed anti-alignment mechanism.
- Testing on a text-to-image model (e.g., Stable Diffusion) would broaden the impact.

## Removed Points

- *"Reproducibility concerns about undisclosed hyperparameters"* — The paper provides detailed experimental setup references (Appendix C). Hyperparameter details for standard training recipes are appropriately deferred.
- *"Missing related works"* — Cannot verify whether works flagged as missing exist. The paper's related work section is appropriate for the scope.
- *Formatting/style nitpicks about figure axes, grammar, and whitespace* — These are standard ICLR parser artifacts, not author errors.
- *"The w=−1 caption error undermines the paper's accuracy"* — This is retained as a trivial weakness above, not amplified further.
- *Strength Finder claims that are generic (e.g., "this paper addressed an important problem")* — Removed as they lack specific evidence.

## Novel Insights

The strongest synthesis across the reviews is that Neon's main vulnerability is the *tension between its claim and its practice* around data requirements. The paper claims "no additional real data" yet relies on FID computed on real data to tune w. This is not fatal — most practical settings have validation data — but it means the paper oversells the headline claim. The other weaknesses (missing baseline comparisons, missing random-direction control) are standard empirical gaps that strengthen but do not invalidate the core contribution. The most interesting observation is that the paper's *simplicity* is simultaneously its greatest strength and its most easily fixable point of criticism: the method is so straightforward that adding the missing baselines and ablations is clearly feasible and would substantially raise the paper's quality.

## Suggestions

1. **Report results with a fixed default w** (e.g., w=1) across all benchmarks, or show that the optimal w is stable across datasets/architectures. This would directly address the data-free usability concern.
2. **Add a random-direction baseline:** replace θ_s − θ_r with a random vector of the same norm and measure FID change.
3. **Compare against DDO** (or another method) on the xAR-L/ImageNet-256 benchmark where both apply.
4. **Correct the Figure 4 caption**: w = −1 corresponds to θ_Neon = θ_s, not θ_r.

## Score and Decision

**Calibration anchors** (calibration_search results, all from the human_reviews_2026 directory):

| Path | Avg Score | Comparison to this paper |
|------|-----------|-------------------------|
| `yfk6c39omW` (Escaping Model Collapse) | 5.20 | Similar topic (model collapse/synthetic data), but experiments are limited to linear regression + MNIST. Neon's expts are far broader and include SOTA results, making it the stronger paper. |
| `NJ3OiroVDa` (ERBP, model collapse unification) | 4.00 | Unifying theoretical framework with weak experiments (frozen toy LLM only). Neon has both theory and strong experiments. |
| `iSO1WFjSKh` (Collapse Errors in diffusion) | 4.00 | Empirical study of deterministic sampler collapse; limited theory, no new method. Neon proposes a novel method and achieves SOTA. |
| `6r0VuH8gGT` (Balancing Fidelity/Diversity) | 3.00 | Synthetic data selection for downstream tasks, narrow scope. Neon is broader, deeper, and has stronger results. |
| `ZX6XEfBidf` (MEPS/LDH, image generation) | 2.00 | Fundamentally unclear mathematics and weak experiments. Neon is incomparably stronger. |
| `VaS6xcDrTb` (Rotation estimation) | 8.50 | Very strong theoretical paper, different domain. While excellent, Neon is more impactful in scope and potential use. |
| `EwdWR6lfvW` (Generate Any Scene) | 5.00 | Data engine for scene graph driven generation. Different type of contribution. Neon has stronger empirical backing. |
| `qBORZkk28r` (InterSyn dataset) | 6.00 | Dataset contribution for interleaved generation. Different contribution type, similar quality level. |

Relative to these anchors, the paper sits comfortably above the 5-band (model collapse/synthetic data papers) and is on par with or slightly above the 6-band papers. The weaknesses (w-tuning on real data, missing comparisons) are real but do not approach the severity of papers at score 3–4. The paper is not at the 8+ level of exceptional contributions like `VaS6xcDrTb`, but it is a solid, well-executed contribution with a novel method, good theory, and strong experiments across diverse settings.

**Score: 6.5** — The paper introduces a simple, elegant method with strong theoretical grounding and extensive empirical validation across four model families, including a new SOTA on ImageNet-256 for xAR-L. The main weaknesses — the tension between the "no additional real data" claim and the need for real FID data to select w, and the absence of direct comparisons against related self-improvement methods — are significant but addressable and do not undermine the core contribution.

**Decision: Accept**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>