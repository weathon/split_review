I have carefully read the paper and verified all reviewer claims against the actual text. Here is my consolidated review.

---

## Summary

This paper identifies the problem of *hidden heterogeneity* in longitudinal counterfactual outcome forecasting — where unobserved latent factors cause outcome variation beyond what observed histories capture. The authors propose THLTS, a VAE-based method that learns the *time-shared* (mean) part of these latent factors, motivated by the limited supervision (1D outcome). THLTS is designed as a plug-in component for existing backbones (CRN, RMSN, Causal Transformer). Experiments on synthetic and semi-synthetic (MIMIC-III) data show consistent RMSE improvements when THLTS is integrated.

## Strengths

1. **Novel problem formulation.** The paper is the first to explicitly target hidden heterogeneity (latent factors unobserved in histories) for counterfactual outcome forecasting in time series. The motivation is clear: same observed histories can lead to different outcomes due to unobserved sample-specific factors. This is a genuine gap that prior work on treatment selection bias does not address.

2. **Principled design choice for limited supervision.** The key insight — learning only the time-shared component of latent factors rather than full time-varying dynamics — is well-motivated by the 1D outcome signal. Proposition 4.1 (while simple) shows that substituting the mean minimizes an upper bound on error, providing theoretical support for this design. The empirical comparison with THLTS(v) (a time-varying variant) validates that the time-shared constraint improves performance under limited supervision, especially in Figure 3.

3. **Consistent empirical improvement across diverse backbones.** THLTS improves RMSE when combined with CRN (LSTM + invariant representation), RMSN (LSTM + IPS reweighting), and Causal Transformer (Transformer + invariant representation) on both synthetic and semi-synthetic datasets (Tables 1–3). The gains grow with the strength of latent factors and with longer trajectory horizons, consistent with the paper's claims. For instance, CRN+THLTS achieves substantially lower RMSE than CRN alone across all settings.

4. **Semi-synthetic validation on real-world covariates.** Using MIMIC-III (25 vital covariates + 3 static covariates) with a semi-synthetic pipeline provides evidence that the method works with realistic covariates, not just fully synthetic data.

5. **Ablation on time-varying vs. time-shared latents.** The comparison between THLTS and THLTS(v) across varying σ_vary (Figure 3) directly tests the core design choice and shows that the time-shared constraint is beneficial when variation is small to moderate. This is a clean ablation.

## Weaknesses

### Fatal
None.

### Major

1. **Unspecified integration of THLTS with backbone models severely hampers reproducibility.** The paper states THLTS is a flexible plug-in component but provides no algorithm, pseudocode, or description of how the VAE objective interacts with each backbone's training losses. For CRN (which uses domain confusion), RMSN (IPS reweighting), and Causal Transformer (CDC loss), it is unclear: (a) whether the backbone's original loss terms are retained, replaced, or combined with the ELBO; (b) whether the backbone's sequence model parameters (ϕ) are frozen during VAE training or fine-tuned end-to-end; (c) how loss weights are set across objectives. While the ELBO in Eq. 5–6 is clearly specified, the training *pipeline* that integrates it with each backbone's existing training procedure is absent. This is a structural omission — the empirical claims cannot be reliably assessed or reproduced without these details.

2. **The causal scope is narrower than the framing implies, and the paper does not acknowledge this limitation.** The paper assumes "latent factors do not affect treatment assignment" (line 61). Under this assumption, treatment assignment is unconfounded given observed histories, and the causal identification problem is already solved — the remaining challenge is purely about improving *outcome prediction* by accounting for outcome-relevant latent factors. This is a legitimate problem, but the paper's framing as a "counterfactual outcome forecast" problem might lead readers to expect a contribution to causal identification under hidden confounding. The paper neither discusses what would happen if the assumption were violated (i.e., true unobserved confounding) nor tests this scenario, which limits the generality of claims. A clearer statement that the contribution is about improving prediction accuracy (not expanding the set of identifiable causal quantities) would better calibrate reader expectations.

### Minor

3. **Identifiability of latent factors from a 1D outcome is not discussed.** The only supervision signal for learning the sample-level latent factors ē is the scalar outcome at each time step (plus observed histories and treatments). A VAE trained to reconstruct a 1D outcome via a latent variable could learn many representations that improve reconstruction without corresponding to the true hidden heterogeneity. The paper does not analyze when the learned ē captures actual heterogeneity versus overfitting to outcome noise. Proposition 4.2 provides variational approximation guarantees under specific generative assumptions, but a discussion of identifiability or a misspecified synthetic experiment would substantially strengthen confidence in the method. (This does not invalidate the main claim, since the paper's central evidence is prediction improvement, not factor recovery.)

4. **Proposition 4.1's bound is a standard quadratic majorization and not tight.** The bound follows directly from (a+b)² ≤ 2(a²+b²) and the Lipschitz condition. While the math is correct, the paper's presentation somewhat overstates its significance ("validate the rationality of our proposed strategy"). It shows that the mean minimizes an *upper bound*, not that the mean is optimal for prediction. This weakens (but does not negate) the claimed theoretical motivation.

5. **THLTS(v) is a weak baseline for time-varying latent dynamics.** THLTS(v) uses a simple linear transformation of the previous posterior — this is a minimal departure from the time-shared model, not a strong time-varying method. Stronger baselines (e.g., Deep Markov Model, variational RNN, Deep Kalman Filter) would provide a more convincing test of the claim that the time-shared constraint is superior to principled time-varying alternatives.

### Trivial
None.

## Nice-to-Haves

- A pseudocode algorithm detailing training and inference for each backbone combination.
- Hyperparameter sensitivity analysis (σ_y, latent dimensionality d_e).
- Experiments under a *misspecified* scenario where the VAE's generative assumptions are violated, to test robustness.
- Comparison against a simple per-sample random intercept (the simplest time-shared baseline).
- Public code release.

## Removed Points

- **"The semi-synthetic dataset uses the pipeline from Melnychuk et al. (2022), which assumes a particular structure for hidden heterogeneity."** — This is a description of the data provenance, not a weakness. The paper properly cites the source, and all semi-synthetic evaluations in this field make structural assumptions.
- **Weaknesses about missing appendix, missing proofs, or absent references.** — These sections exist in the original submission; the parser strips them.
- **Formatting/style nitpicks and typographical observations.** — These are parser artifacts, not author errors.
- **"The paper would be notably stronger with even one realistic observational study where hidden heterogeneity is plausible."** — While real-world validation is always desirable, semi-synthetic evaluation on MIMIC-III covariates is standard practice in this subfield. This is a wishlist item, not a weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that fundamentally reframes the paper's contribution.

## Suggestions

1. **Provide a detailed training protocol.** Include a figure or pseudocode showing how the VAE encoder/decoder and each backbone's sequence model are composed, what loss terms are used (and with what weights), and how parameters are updated. This is the single most important step for making the paper reproducible.

2. **Clarify the scope of the causal claim.** Either rename or reframe the contribution as "improving outcome prediction under hidden heterogeneity in a causally identified setting," and add a limitations paragraph discussing what happens if the assumption that latent factors do not affect treatment is violated.

3. **Add a brief identifiability discussion or experiment.** Even showing that learned latent factors correlate with ground-truth factors in a misspecified synthetic setting would substantially increase confidence.

4. **Expand the time-varying baseline set** to include at least one principled recurrent state-space model (e.g., Deep Markov Model) to strengthen the claim about the time-shared constraint's advantage.

## Score and Decision

**Originality:** The problem identification (hidden heterogeneity in counterfactual time-series forecasting) is novel. The solution (learning time-shared latent factors via VAE) is a reasonable first attempt.  
**Importance:** The problem is practically relevant — unobserved sample-specific factors are common in healthcare, econometrics, and other domains.  
**Claims supported:** The central claim (THLTS improves prediction when added to existing backbones) is supported by the presented experiments, but the **reproducibility gap** (missing integration details) weakens confidence.  
**Soundness:** The experiments appear sound in design (10 repeats, standard deviation reported, varying settings). However, the unspecified training pipeline means the results cannot be verified independently.  
**Clarity:** The paper's core idea is communicated clearly, but the critical implementation details are missing.  
**Value:** The idea is valuable and the empirical results are promising, but the paper needs substantial revision on reproducibility before it can serve as a reliable reference.

The paper identifies a genuine gap and proposes a sensible, empirically validated solution. However, the missing specification of how THLTS combines with each backbone's training procedure is a significant reproducibility concern that prevents the paper from being accepted in its current form. The contribution is real but not so exceptional that it overrides this structural omission. With a detailed training protocol and clarifications of scope and identifiability, this could be a solid acceptance.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>