Now I have all the evidence I need to verify claims against the paper. Here is my consolidated review.

---

## Summary

This paper defines the problem of trajectory prediction with noisy observations and proposes NoisyTraj, a plug-and-play denoising framework that combines (1) a mutual-information-based loss (inspired by the Information Bottleneck) that encourages denoised observations to be predictive of clean future trajectories while being distinguishable from noisy inputs, (2) a masked reconstruction loss to preserve trajectory structure, and (3) a ranking loss that forces predictions from denoised observations to outperform those from noisy ones. Experiments on ETH/UCY and SDD across Gaussian, Poisson, mixed, and multiplicative noise show consistent improvements when NoisyTraj is added to GraphTern and EqMotion backbones.

## Strengths

1. **Addresses a practical and underexplored problem with clear empirical motivation.** Figure 1 quantifies a dramatic performance collapse (e.g., FDE on ETH/UCY rising from ~0.35–0.45 m to ~0.60–0.75 m under Gaussian noise σ=0.4). This cleanly establishes why noisy observations matter and justifies the new problem formulation.

2. **Proposes a theoretically grounded denoising objective.** The method derives a tractable upper bound for an Information Bottleneck-style objective (Eq. 10) using CLUB for the upper bound on I(X_obs; X̂_obs) and MINE for the lower bound on I(X̂_obs; Y_fut). This goes beyond heuristic filtering (smoothing, thresholding) by using a principled information-theoretic criterion.

3. **Demonstrates strong and consistent empirical performance across diverse noise settings.** Tables 1–4 show that NoisyTraj+GraphTern and NoisyTraj+EqMotion outperform both the original backbones and wavelet/EMA denoising baselines under Gaussian noise (σ=0.2, 0.4), Poisson noise, mixed noise, and multiplicative noise. Every comparison favors NoisyTraj.

4. **Shows plug-and-play compatibility and cross-noise generalization.** The module integrates without modification into two architecturally distinct backbones. Table 5 shows that training on Gaussian noise (σ=0.4) and testing on different distributions (σ=0.2 Gaussian, Poisson λ=0.4) still yields superior performance (ADE 12.78 vs. GraphTern 14.77 on Poisson test), supporting the claim of noise-agnostic behavior.

5. **Ablation study cleanly attributes gains to each component.** Table 3 shows a monotonic improvement: baseline GraphTern ADE 0.58 → +MI loss 0.54 → +reconstruction 0.52 → +ranking loss 0.49, confirming that each proposed loss contributes positively.

6. **Ranking loss is a novel self-supervision signal.** The idea of using a margin-based loss to force denoised predictions to be better than noisy predictions (Eq. 17) jointly improves both the denoising module and the prediction backbone — a design not seen in prior trajectory prediction or denoising work.

## Weaknesses

### Fatal
None.

### Major

1. **The mutual information objective uses future trajectories Y_fut as the "clean pattern" reference without validating that X̂_obs actually approximates the clean *observed* trajectories S_obs.**  
   The paper defines the clean observed trajectories as S_obs (line 55: "X_obs = S_obs + N") but maximizes I(X̂_obs; Y_fut) rather than I(X̂_obs; S_obs). The justification is that Y_fut is "clean" and shares underlying motion dynamics with S_obs, but this is asserted rather than argued. Since S_obs is known in the synthetic-noise setting, the paper should directly measure the denoising error (distance between X̂_obs and S_obs) and compare it against the noisy input and other denoising methods. Without this validation, the claim that the method genuinely recovers clean *observed* trajectories (as opposed to learning a noise-robust representation that is simply good for prediction) is not fully supported. The qualitative results (Figure 3) suggest the method does produce visibly smoother trajectories, but a quantitative comparison against known ground-truth S_obs would strengthen the core claim significantly.

2. **The paper mentions outperforming "Kalman" as a denoising baseline (line 282) but never introduces Kalman smoothing as a baseline in the methodology section (lines 215–216 list only Wavelet and EMA).**  
   This inconsistency makes it unclear whether Kalman was actually included in the experimental comparison or whether this is a writing error (possibly "Wavelet" was intended). Either way, the evaluation section needs a clear specification of all baselines and their results.

### Minor

3. **Reconstruction loss targets the noisy observations at masked locations (Eq. 12: reconstructs X_obs ⊙ (1−M_obs), not S_obs).**  
   The paper argues this "preserves structure information," but since the target is the noisy signal itself, the loss could partially counteract the denoising objective by encouraging the model to reproduce noise patterns at masked locations. The ablation (Table 3) shows the loss helps empirically, suggesting the joint optimization works in practice, but the theoretical motivation needs clarification: (a) why the reconstruction target is X_obs rather than the known-clean S_obs, and (b) how the loss avoids preserving noise in the unmasked portion. An ablation comparing reconstruction targets (noisy vs. clean) would resolve this.

4. **No variance or confidence intervals reported for any experimental result.**  
   Tables 1–5 report only point estimates of ADE/FDE. Given the stochasticity of noise injection, model training, and the min-over-K selection for multi-modal prediction, it is impossible to assess whether observed improvements are statistically significant. While single-run evaluation is common in trajectory prediction, the main empirical claim (that NoisyTraj consistently improves prediction under noise) would be substantially strengthened by reporting means and standard deviations over multiple seeds.

5. **Hyperparameters (α, β, δ, γ, margin Δ, mask ratio) are neither reported numerically nor ablated.**  
   The margin Δ appears in Eq. 17 but its value is never given. The trade-off parameters α, β, δ, γ appear in Eq. 18 but are not reported. The mask ratio M (number of masked locations) is also unspecified. While not every hyperparameter needs exhaustive ablation, a complete paper should at minimum report the values used and preferably include a sensitivity analysis for the most critical ones.

### Trivial

6. **Line 282 mentions "Kalman" but the baselines section (lines 215–216) only introduces Wavelet and EMA.** This inconsistency should be resolved — either add Kalman as a properly described baseline or correct the text.

7. **Line 314 writes "EWA" where "EMA" is clearly intended.**

## Nice-to-Haves

- **Validate direct denoising quality.** In the synthetic noise setting, S_obs is known. Compute the error between X̂_obs and S_obs and compare it against the error between X_obs and S_obs, and against Wavelet/EMA denoising. This would directly confirm that the method actually recovers clean observed trajectories (beyond just improving prediction).

- **Add Kalman smoothing as a denoising baseline** (or clarify the existing mention). Kalman filtering/smoothing is a natural and principled baseline for trajectory denoising and would strengthen the comparison.

- **Ablation: reconstruction target.** Compare L_rec targeting X_obs (noisy) vs. targeting S_obs (clean, available in the synthetic setting) to clarify whether the reconstruction loss is helping despite or because of the noisy target.

- **Controlled experiment: replace Y_fut with a different clean reference** (e.g., held-out clean observation segments from the training set) to test whether the future is a special or necessary reference for the MI objective.

- **Sensitivity analysis** for the most important hyperparameters (α, β, δ, γ, Δ, mask ratio).

- **Discussion of limitations:** the assumption that Y_fut is clean, the controlled nature of the noise injection (all noise is additive and relatively mild), and how the method might behave with missing data or extreme outliers.

- **Computational cost** of training the MI estimators (CLUB + MINE networks) should be briefly discussed.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Conceptual validity of mutual information objective — data leakage concern."** The critic argues that maximizing I(X̂_obs; Y_fut) could leak future information into X̂_obs, making prediction artificially easier. However, this misunderstands the training setup: during training the TPB sees (X̂_obs, Y_fut) pairs and learns to predict Y_fut from X̂_obs — the same supervision signal used in standard trajectory prediction. There is no "leakage" because Y_fut is the training target, not a test-time input. If X̂_obs encodes information predictive of Y_fut, that is the intended behavior of any feature extractor for prediction. The concern would only be valid if the MI objective allowed X̂_obs to encode Y_fut in a way unavailable from clean observations, but no evidence of this is provided. **[Removed: the criticism misunderstands the training setup; no actual leakage mechanism is identified or demonstrated.]**

- **"Equation (3) is missing the variance parameter."** This refers to the CLUB bound. The paper's Eq. (3) states the general bound; the variational approximation q_φ would parameterize a specific distribution (e.g., Gaussian with estimated variance), which is standard. The full parameterization is likely in the appendix. **[Removed: nitpick about presentation detail; the missing variance is a standard implementation detail deferred to the appendix, which is common practice.]**

- **"The derivation assumes q_φ is a variational approximation... but the paper never specifies how this conditional distribution is parameterized."** Same as above — this is an implementation detail (what architecture q_φ uses) that would be in the experimental setup or appendix. The reviewer does not show that this omission leads to irreproducibility. **[Removed: minor implementation detail, standard to defer to appendix.]**

- **"The paper does not discuss the computational cost or stability of training these mutual information estimators."** Not a substantive weakness — many papers do not discuss computational cost. **[Removed: not a flaw that affects the paper's contribution.]**

- **"The paper would benefit from a discussion of how the method could be adapted when future observations are also noisy."** The paper explicitly assumes Y_fut is clean (line 55: "we simplify the problem by assuming Y_fut are clean"). Criticizing a paper for not solving a problem it explicitly scoped out is scope creep. **[Removed: outside the paper's stated scope.]**

- **"The claim about handling 'arbitrary types of noise' is too strong since only four types are tested."** The paper says "in principle" (abstract line 6) and tests Gaussian, Poisson, mixed, and multiplicative noise across multiple noise strengths. This is a reasonable demonstration for a single paper. **[Removed: the claim is appropriately qualified ("in principle") and the coverage is adequate for the claim made.]**

- **"Missing are standard denoising baselines like a Kalman smoother."** This is a valid suggestion but belongs in Nice-to-Haves rather than Weaknesses, since Wavelet and EMA are reasonable baselines and the paper's method is about learned denoising, not about comparing against all possible signal-processing filters. **[Moved to Nice-to-Haves.]**

## Novel Insights

None beyond the paper's own contributions. The reviews do surface a genuine concern about whether the method truly recovers clean *observed* trajectories or simply learns noise-robust features that improve prediction — this is a useful critical lens but it challenges rather than extends the paper's claims.

## Suggestions

1. **Measure denoising error directly.** Compute the L2 distance between denoised X̂_obs and known-clean S_obs in all synthetic noise settings, and report it alongside Wavelet/EMA denoising. If this error decreases significantly, the denoising claim is fully validated. If it does not, the paper should reframe its contribution as "learning noise-robust representations for prediction" rather than "denoising trajectories."

2. **Report all hyperparameter values** (α, β, δ, γ, Δ, mask ratio) and run experiments with at least 3 random seeds, reporting means and standard deviations.

3. **Clarify the reconstruction loss motivation** — either change the target to S_obs (known in the synthetic setting) or provide a clear argument for why reconstructing the noisy signal at masked locations helps remove noise at unmasked ones. An ablation comparing both targets would be ideal.

4. **Resolve the Kalman baseline inconsistency.** Either add Kalman smoothing as a properly described, tabulated baseline or correct line 282.

## Score and Decision

The paper tackles a genuinely important and underexplored problem with a novel and well-motivated approach. The empirical results are consistent, the ablation is clean, and the plug-and-play compatibility is practically valuable. The main weaknesses are (a) insufficient validation that the method actually recovers clean *observed* trajectories (as opposed to learning prediction-friendly features), and (b) incomplete reporting of hyperparameters and statistical variance. These are addressable in revision and do not invalidate the core contribution.

I recommend **weak accept** with a request for the authors to address the denoising validation and reporting gaps in the final version.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>