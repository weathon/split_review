## Summary

The paper proposes incorporating kinematic priors into trajectory forecasting by reparameterizing the GMM output head: instead of predicting positions directly, the network predicts kinematic quantities (velocity components, acceleration components, or speed+heading) and obtains positions via differentiable Euler integration. Three formulations are derived, with analytical error bounds for the nonlinear speed+heading case. Experiments on the Waymo Motion Dataset using a downscaled version of the Motion Transformer (65M→2M params) show modest gains (~2% mAP on full data) and larger gains in low-data regimes (~12% mAP on 1% data).

## Strengths

1. **Clean and well-motivated idea with strong low-data results**: The core idea—reparameterizing the prediction space through kinematic quantities—is sensible and elegantly explained. The 1%-data experiments (Table 2) show substantial, consistent improvements (~12% mAP, 12.5% minADE, 27.8% minFDE for Formulation 1), clearly demonstrating that kinematic priors help when data is scarce. This is the paper's strongest empirical evidence.

2. **Noise robustness advantage for the acceleration formulation**: Table 3 demonstrates that Formulation 2 (acceleration components) degrades least under input noise perturbation. This is a distinct, practically relevant benefit that aligns with the paper's motivation about real-world sensor noise.

3. **Analytical error bounds for the nonlinear approximation**: Section 4.3 derives a clean Lagrange error bound (R(x) ≤ σ²_θ/2) for the linear Taylor approximation of sin/cos in Formulation 3, providing formal grounding for an otherwise heuristic linearization step.

4. **Simple, easy-to-integrate design**: The method modifies only the GMM output head—no changes to the backbone feature extractor, no additional inputs, no extra loss terms. This makes it straightforward to implement within existing frameworks.

## Weaknesses

### Major

1. **Mathematical error in uncertainty propagation (all formulations)**: The derivation in Section 4.2.1 (Eq. 4) gives σ_x^{t+1} = σ_x^t + σ_{v_x}^t·Δt. However, with independent noise sources ε_x, ε_v ~ N(0,1)—which the notation implies—the correct formula is σ_x^{t+1} = sqrt((σ_x^t)² + (σ_{v_x}^t·Δt)²). The sum of two independent zero-mean Gaussians has variance equal to the sum of variances, not the square of the sum of standard deviations. This linear addition of standard deviations is mathematically incorrect and propagates through all formulations. Because this error affects the covariance structure of the position distributions used in the training objective, the quantitative results may not reflect the claimed method. The paper never acknowledges or discusses this.

2. **Evaluation on a heavily downscaled model contradicts the "SOTA improvement" framing**: The paper downscales MTR from 65M to 2M parameters (a 97% reduction, line 220) and evaluates on this weakened baseline. The paper claims to improve "state-of-the-art" methods, but a 2M-parameter transformer is not remotely representative of SOTA trajectory forecasting. The paper itself concedes (line 281) that "model complexity and dataset size will eventually out-scale the effects of the kinematic prior." If the authors believe their own conjecture, then the central experimental result (~2% mAP gain on the full dataset with a 2M model) does not support the stated contribution of improving SOTA trajectory forecasting. It supports the more modest claim that kinematic priors help when capacity is artificially constrained. The experiments cannot answer whether the benefit persists at actual SOTA scale.

3. **No absolute performance numbers are reported**: All three tables report only "% difference" relative to the baseline. Without absolute mAP, minADE, and minFDE values, readers cannot assess whether a 2% improvement on the downscaled baseline brings performance closer to actual SOTA levels or is merely a small gain on a weak model. The Waymo leaderboard has established absolute metrics—failing to report them makes the practical significance of any claimed gain impossible to calibrate.

4. **Only one base architecture tested despite claiming agnosticism**: The paper states (line 87) that the method is "agnostic to the design of the learning framework" and "can be implemented in any of the SOTA methods above" (line 42). Yet only MTR is evaluated. Demonstrating the approach on even one additional architecture (e.g., an LSTM-GMM or a different transformer) is necessary to substantiate the claim of architecture agnosticism.

5. **Formulation 3 uses a mathematically questionable approximation without validation**: The paper claims (line 195) that the product of two independent standard normal random variables "produces an unnormalized Gaussian PDF with mean 0 and variance 1/2, per the proof from (Bromiley, 2003)." This is incorrect: the product of two independent standard normals follows a distribution proportional to K₀(|z|) (modified Bessel function), not a Gaussian. (Bromiley 2003 discusses the product of Gaussian *PDF functions*, not the distribution of the product of Gaussian *random variables*—a category error.) Furthermore, even as a moment-matching approximation, the stated variance is 1/2 while the true variance of the product of two standard normals is 1. The paper does not validate this approximation against a Monte Carlo estimate. This weakness only affects Formulation 3, which is not the best-performing variant, but it undermines the theoretical rigor of the paper.

6. **Only vehicles are reported despite training on all three classes**: The paper trains on vehicles, pedestrians, and cyclists (line 227) but reports results only for vehicles (line 243, 260). The bicycle model is applied to all classes, including pedestrians, where it is clearly inappropriate. While the paper acknowledges this limitation ("leave discerning between the three... to future work"), it means the evaluation does not cover the multi-class setting that the Waymo benchmark actually evaluates.

### Minor

1. **No statistical significance or variance reporting**: All results appear to come from a single training run per configuration. With improvement margins as small as 2% on some metrics, and with downscaled models that may be sensitive to initialization, the absence of multiple seeds or standard deviations is a gap. The reader cannot know whether the observed improvements are reliable or could reverse under different randomness.

2. **Bicycle model parameter L is introduced but never used**: Line 61 introduces the Bicycle Model parameter L (vehicle length), but L never appears in any equation or subsequent derivation. The actual kinematics used reduce to a simple velocity-based update without steering angle or wheelbase. This disconnect between the model introduced and the model actually used should be acknowledged.

3. **The noise experiment tests a different claim than stated**: Table 3 adds noise to input positions at *evaluation time* to measure degradation. This tests robustness of the *trained model* to input perturbations, not whether kinematic priors help *during training* with noisy data. These are different questions. Additionally, Formulation 1 with interpolation is explicitly excluded from this experiment (line 270) because "the noise added would not be proportional"—a post-hoc exclusion that should have been addressed by designing the experiment differently.

### Trivial
- None beyond standard formatting artifacts from the PDF extraction process.

## Nice-to-Haves
- Compare against a simple smoothness/acceleration regularization baseline (adding a loss term that penalizes non-smooth trajectories) to distinguish the benefit of the reparameterization from any mechanism that correlates predictions across timesteps.
- Validate Formulation 3's Gaussian approximation via Monte Carlo sampling.
- Run the core experiment at the full 65M-parameter scale to determine whether the benefit persists at actual SOTA model capacity.

## Removed Points
- *Criticism about missing related work* (e.g., "would benefit from a more targeted discussion of prior attempts to integrate kinematic constraints"): Removed per rules against requiring missing references.
- *Criticism about the "prior" framing not being a Bayesian prior*: Removed as a semantic nitpick; "prior" is used in the common loose sense of "prior knowledge."
- *Strength about "model-agnostic design demonstrated on a competitive baseline"*: Removed because the claim of agnosticism is contradicted by the verified weakness that only one architecture was tested.
- *Strength about "the paper addressed an important problem"*: Too generic; removed per filtering rules.
- *Criticism about the error bound being "disconnected from actual prediction error"*: The bound is correctly derived for the sin/cos linearization itself, which is a standard Taylor remainder bound. The paper does not claim it bounds overall prediction error. Demoted to removed.
- *Criticism about the noise experiment's "post-hoc exclusion" being severe*: The exclusion is acknowledged by the paper and affects only one variant; kept as minor in the final review but the stronger framing was removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions
1. Correct the standard deviation propagation formula: σ_x^{t+1} = sqrt((σ_x^t)² + (σ_{v_x}^t·Δt)²) for independent noise sources, or explicitly state and justify the assumption of perfectly correlated noise (ε_x = ε_v) if that is intended.
2. Report absolute metric values alongside relative differences.
3. Run at least the Formulation 1 experiment at the full 65M-parameter scale to determine whether the benefit holds at SOTA capacity.
4. Validate the Formulation 3 Gaussian approximation against a Monte Carlo estimate.
5. Add results for pedestrian and cyclist classes, or explicitly scope the paper to vehicles only throughout.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>