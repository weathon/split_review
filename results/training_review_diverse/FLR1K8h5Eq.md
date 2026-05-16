Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper addresses the problem of hidden heterogeneity in longitudinal counterfactual outcome forecasting — the case where unrecorded latent factors cause the expected outcome conditional on observed histories to differ from the true individual outcome. The authors propose THLTS, a VAE-based plug-in module that learns a time-shared (per-sample constant) latent representation to capture these hidden factors, and can be combined with any existing sequence-model-based counterfactual forecaster. Experiments on synthetic and semi-synthetic (MIMIC-III) data show consistent RMSE improvements when THLTS is integrated into RMSN, CRN, and Causal Transformer.

## Strengths

1. **Well-motivated problem with clear formalization.** The paper identifies a genuine gap in existing longitudinal counterfactual forecasting literature: existing methods implicitly assume all outcome-relevant factors are captured in observed histories. Section 3 formalizes this as hidden heterogeneity (Equation 1), and Figure 1 provides an intuitive illustration of how identical observed histories can mask divergent individual outcomes. This motivation is novel and practically relevant.

2. **Principled design choice with theoretical motivation.** Proposition 4.1 derives an upper bound showing that using the mean of time-varying latent factors minimizes the worst-case prediction error increase when replacing time-varying factors with a constant. This formally grounds the "time-shared" strategy. Proposition 4.2 then shows that under additive zero-mean noise on the latent factors, maximizing the VAE ELBO recovers the true posterior and outcome distribution — connecting the theoretical insight to a practical inference framework.

3. **Flexible plug-in design validated across multiple backbones.** THLTS is architecture-agnostic (the forecast process in Section 4.3 does not depend on the specific sequence model). The paper validates this by integrating THLTS into three different backbones (RMSN, CRN, Causal Transformer) and showing consistent improvements across all of them in Tables 1–3.

4. **Comprehensive experimental evaluation.** The paper evaluates under multiple settings: varying latent factor strength (Table 1), varying trajectory horizon (Table 2), time-varying latent dynamics (Figure 3), and a semi-synthetic MIMIC-III benchmark (Table 3). The inclusion of the THLTS(v) ablation directly tests the core design hypothesis. Experiments use 10 repeated runs with reported standard deviations.

## Weaknesses

### Fatal
None.

### Major

1. **Weak baseline for the "time-shared vs. time-varying" claim.** The paper argues that learning time-shared factors is preferable to learning time-varying factors, and supports this with the THLTS(v) baseline. However, THLTS(v) is constructed by simply applying a linear layer to transform the previous posterior parameters — this is a trivial time-varying model, not a genuine time-varying latent variable model (e.g., a recurrent VAE with learned transition dynamics, or a deep state-space model). The comparison therefore does not adequately test the paper's central thesis that "sacrificing flexibility improves performance." A stronger time-varying baseline is needed to convincingly demonstrate that the time-shared constraint is a beneficial regularizer rather than a design that merely outperforms a poorly-specified alternative. This weakens confidence in the paper's core design insight.

### Minor

2. **Underspecified integration with backbone models.** The paper describes THLTS as a "flexible component" that can be plugged into arbitrary counterfactual forecast models, but never states whether the backbone parameters (the representation function $\phi(\cdot)$, e.g., LSTM/Transformer) are pre-trained and frozen, fine-tuned, or trained jointly from scratch with the THLTS loss. The training objective in Section 4.3 (Equation 5) only explicitly involves the encoder $q_\varphi$ and decoder $g_\rho$ parameters. How $\phi$ is updated (or not) during training is essential for reproducibility and fair comparison. This should be clarified with an explicit training algorithm.

3. **Semi-synthetic experiment generation is underspecified.** The MIMIC-III experiment reports a parameter $\alpha_g$ controlling the strength of latent factors (Table 3) but does not describe how the hidden factors $\mathbf{e}_t$ are generated, how they are removed from the observed covariates, or how $\alpha_g$ is operationalized. The paper only states that the pipeline from Melnychuk et al. (2022) is used, without describing the specific adaptation for introducing hidden heterogeneity. This omission makes it difficult to assess whether the experimental setup fairly tests the method or inadvertently favors it.

4. **Missing key hyperparameters.** The paper does not report the latent dimension $d_e$, the number of posterior samples $m$ used during forecasting (Section 4.3, "Forecast Process"), or the value of the outcome noise hyperparameter $\sigma_y$. These are necessary for reproducibility and should be included.

5. **Synthetic data treatment effect term is garbled.** The description of the outcome generation (Section 5.2) contains "$= CE(2t-1)+ a_t^{(i)}$" which appears to be a rendering artifact. The intended formula for the time-decaying treatment effect is unclear, making the synthetic data generation ambiguous at a critical point.

6. **Strong assumption about hidden factors and treatment is stated but not discussed.** The paper assumes (Section 3) that latent factors do not affect treatment assignment, which means the hidden factors are not confounders. This is a strong assumption — if it fails, standard causal identification fails and the method would produce biased estimates. The paper states this assumption but does not discuss its implications, limitations, or how violations would affect the method's validity. This should be acknowledged.

7. **KL divergence notation inconsistency in Proposition 4.2.** The ELBO expression in Proposition 4.2 writes $D_{KL}(p_\rho(\bar{\mathbf{e}}|\mathbf{H}_t) \, | \, q_\varphi(\bar{\mathbf{e}}|\mathbf{H}_t, \mathbf{a}_t, \mathbf{y}_t))$ with a plus sign. The standard VAE ELBO uses $D_{KL}(q \, || \, p)$ with a minus sign. The actual training objective (Section 4.3) correctly uses $D_{KL}(q \, || \, \text{prior})$, so this is a notational error in the proposition, not an implementation error, but it should be corrected.

8. **Limited comparison when improvements are within one standard deviation.** In several cases (e.g., Table 1, CRN with strength 1: $\mu=4.519$ vs $4.433$ with std $\sim$0.28–0.33), the improvement from adding THLTS is within one standard deviation of the baseline. The paper relies on 10 repeated runs but does not report paired significance tests or confidence intervals. A brief statistical comparison would strengthen the claims.

### Trivial

- The claim of being "pioneer work" (Introduction) is slightly overstated given Bouchattaoui et al. (2023) addresses a related problem; the differentiation provided in Related Work is adequate but the "pioneer" framing is unnecessary.

## Nice-to-Haves

- An ablation that uses a fixed standard Gaussian prior at all time steps (instead of the sequential prior update using $\mu_{t-1}, \sigma_{t-1}$) would help isolate the benefit of the sequential posterior-update mechanism.
- Runtime comparisons or a note on training time would help practitioners assess the practical cost of adding the THLTS module.
- A discussion of latent non-identifiability (multiple latent representations can explain the same outcomes) would strengthen the limitations section.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Theoretical justification is not as tight as claimed (Critic Issue 4).** The critic argues the bound is "loose (factor of 2)" and "does not imply optimality of the forecast." However, the paper clearly states the bound is an *upper bound* and that the mean reaches the "minimal value" of that bound — this is mathematically correct. The bound is a design justification, not a claim of predictive optimality. The critic also claims "the bound assumes the true $e_t$ are known, which they are not" — this is standard for theoretical analysis; bounds routinely depend on unobserved quantities and their purpose is to motivate the design, not to be computed. This criticism is removed as it misinterprets the role of the theoretical analysis.

- **Figure 3 legibility concern (Section-by-Section Notes).** The critic says the figure is "not legible in the extracted text." The figure is an image embedded in the PDF; legibility issues are parser artifacts, not author errors. Removed per hard rule.

- **"CE(2t-1)+ at(i) is garbled" (Section-by-Section Notes).** This is a parser rendering artifact. Removed per hard rule on formatting/parser issues. (However, the *substance* that the synthetic outcome generation formula is unclear at this point is retained as Minor Weakness #5.)

- **Proposition 4.1 bound "does not translate directly to RMSE."** RMSE is simply the square root of the mean squared error; the sum-of-squares bound translates directly. Removed as pedantic.

- **Strength Finder's generic framing.** Some framing in the Strength Finder ("clear motivation and problem illustration") is kept as a supporting observation, not a core strength. The four core strengths listed above are all well-evidenced and specific.

## Novel Insights

The reviews surface one noteworthy observation beyond the paper's own contributions: the paper's core thesis about time-shared vs. time-varying latent factors is supported by an interesting theoretical argument (Proposition 4.1) but the empirical validation of this specific trade-off is weaker than the overall validation of THLTS as a useful module. The paper convincingly shows that adding THLTS improves existing models, but the claim that *time-shared is better than time-varying* specifically is not as strongly evidenced because the time-varying baseline (THLTS(v)) is too simple. A reviewer insightfully notes that this distinction matters because the paper's motivation (limited supervision from a 1D outcome) is a genuine challenge for time-varying latent variable models — and a proper time-varying baseline would test whether it's the dimensionality constraint or the specific design of THLTS(v) that drives the performance gap.

## Suggestions

1. Provide pseudo-code or an explicit algorithm showing how backbone parameters are handled during THLTS training (frozen, joint, or fine-tuned).
2. Add a proper time-varying baseline (e.g., a recurrent VAE or deep state-space model with learned latent transitions) for the synthetic experiment in Figure 3 where the ground truth dynamics are known.
3. Fully specify the semi-synthetic data generation: how latent factors $\mathbf{e}_t$ are introduced, how $\alpha_g$ controls their effect, and whether they are removed from the observed covariates.
4. Report all missing hyperparameters: $d_e$, $m$, $\sigma_y$, and any regularization parameters.
5. Clarify the synthetic outcome generation formula to resolve the garbled "CE(2t-1)+ a_t^{(i)}" notation.
6. Add a brief limitations paragraph discussing the assumption that latent factors do not affect treatment, and the implications if this assumption is violated.

## Score and Decision

The paper identifies a genuine and underexplored problem, proposes a clean and flexible solution, and demonstrates consistent improvements across multiple backbones and experimental settings. The weaknesses are real but fixable: the primary methodological gap is the weak time-varying baseline used to support the core design claim, and the primary evidential gaps are underspecified experimental details. These do not invalidate the paper's main contribution (that THLTS improves existing counterfactual forecasters), but they weaken the secondary claim about the time-shared design's superiority. With the suggested revisions, the paper would be substantially stronger. Given the novelty of the problem framing, the clean method, and the breadth of experimental validation, the paper merits acceptance contingent on addressing the major and minor concerns.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>