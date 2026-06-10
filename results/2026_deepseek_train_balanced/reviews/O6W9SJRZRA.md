## Summary

This paper introduces RioT, an Explanatory Interactive Learning (XIL) method for mitigating confounders in time series models. The key novelty is extending XIL to the frequency domain — computing IG attributions in time, applying FFT, and penalizing explanations at annotated frequencies. The paper also contributes P2S, a real-world industrial sensor dataset with naturally occurring confounders and expert annotations. Experiments on UCR/UEA classification datasets, Darts forecasting datasets, and P2S show that RioT improves test performance over the confounded baseline.

## Strengths

- **Novel frequency-domain XIL extension.** Prior XIL methods (RRR, RBR, HINT) operate only on the spatial domain. By applying FFT to IG attributions and defining a right-reason loss on real/imaginary components (Eqs. 4–5), RioT enables feedback on confounders that are not spatially separable. The FFT is invertible and differentiable, so gradients backpropagate to model parameters (line 116). This is a genuine conceptual advance.

- **P2S dataset fills a real gap.** P2S (Section 3.2, lines 142–147) is a sensor dataset from an industrial high-speed press where production speed acts as a naturally occurring confounder, with confounding regions annotated by a domain expert. No prior time series dataset provides explicitly annotated real-world confounders, making this a standalone contribution independent of the method.

- **Empirical breadth across tasks and architectures.** The evaluation spans classification (FCN, OFA) and forecasting (TiDE, PatchTST, NBEATS), on both synthetic and real confounders. Quantitative improvements include MSE drops of up to 56% on Energy forecasting and test accuracy gains on P2S with partial and full feedback (Tables 1–3).

- **Well-executed ablations on feedback efficiency and noise robustness.** The paper tests RioT with as little as 5% annotated samples (Fig. 6) and with up to 10% random/incorrect feedback (Fig. 7), showing the method is not brittle or dependent on exhaustive annotations. These experiments directly address practical deployment concerns.

- **Combined spatial+frequency feedback outperforms single-domain feedback for dual confounders.** Table 4 shows that when data is confounded in both time and frequency, single-domain feedback is insufficient while combined feedback significantly improves performance, validating the dual-domain design.

## Weaknesses

### Fatal
None.

### Major

1. **No comparison against any alternative deconfounding method.** The paper evaluates RioT only against a "no mitigation" baseline and an "unconfounded ideal." It does not compare against a direct adaptation of RRR (Ross et al., 2017) to time series, even though RioT's spatial component (Eq. 3: 1/D Σ (e(x)·a(x))²) is functionally identical to RRR's penalty. RRR is a general method — plugging in a time-series-appropriate explainer is straightforward. The paper cites RRR in related work (line 46) as a prior method but never benchmarks against it. Similarly absent are comparisons against other XIL methods (RBR, HINT), data augmentation, input masking, or adversarial debiasing. Without any such baselines, the evidence supports only the claim that "regularizing against a known confounder is better than doing nothing" — a much weaker claim than what the paper asserts about RioT's effectiveness as a specific method.

2. **The frequency-domain contribution (claimed as a central novelty, contribution 3) is validated only on synthetic data with perfect annotations.** The controlled experiments add synthetic shortcuts to UCR/UEA and Darts datasets with *perfect* annotation masks that exactly match the synthetic confounder (line 174). The only real-world test (P2S, Section "Removing Confounders in the Real-World") tests exclusively spatial confounders. The frequency-domain component — which the paper presents as overcoming "the important limitation that confounders must be spatially separable" (line 31) — receives no evaluation on real data with naturally occurring frequency-domain confounders. This gap undermines the strongest claim of novelty.

3. **No reporting or sensitivity analysis of the critical λ hyperparameters.** The combined loss (Eq. 6) is L = L_RA + λ₁ L_RR^sp + λ₂ L_RR^fr, where λ balances task performance and explanation alignment. This is the central tuning parameter that controls the method's behavior. The paper never states what λ values were used across experiments, nor provides any ablation or sensitivity analysis. For a method whose entire mechanism is a weighted penalty term, this omission makes it impossible to assess how sensitive the results are to this choice, and hinders reproducibility.

### Minor

1. **No quantitative measure of explanation alignment.** The paper claims the model focuses on "right reasons" after revision (Fig. 4, qualitative explanation plots) but provides no quantitative metric (e.g., overlap between explanations and the annotated confounder region before vs. after revision). This makes the "right reasons" claim partly subjective.

2. **The frequency-domain mechanism's indirectness is not examined.** The process penalizes the FFT of IG attributions, effectively asking the model to stop using time-domain patterns whose Fourier representation has energy at annotated frequencies. The paper does not discuss whether the model could learn to *hide* frequency usage from IG (a known failure mode of explanation-based penalties) or simply shift to different frequency representations. This is a conceptual gap worth noting but not fatal since the empirical results speak for the synthetic cases.

3. **The "surpassing unconfounded" result on TiDE/Energy (line 198) is acknowledged but not analyzed.** While the paper correctly notes this likely reflects a regularization effect rather than specific confounder mitigation, the interpretation of results conflating both effects is not disentangled, weakening the precise attribution of improvements to confounder mitigation alone.

### Trivial
None.

## Nice-to-Haves
- Wall-clock training time comparison (with and without RioT) since computational cost is claimed to be minimal but never measured.
- An ablation comparing alternative aggregation strategies for forecasting explanations (max, recency-weighted) vs. the default averaging.

## Removed Points
*These points are flagged to be removed; treat them with caution.*
- **"IG with absolute value modification not justified in main text"** — ruled trivial; deferring implementation details to an appendix is standard practice.
- **"Forecasting attribution averaging not ablated"** — moved to Nice-to-Haves; a single aggregation strategy is acceptable for a first presentation of the method.
- **"Unusual 56/14/30 split"** — removed as a nitpick; this is a standard 80/20 of the 70% training set.
- **Various formatting/style nitpicks** — removed per instructions as parser artifacts.
- **Criticisms about missing appendix content** — removed per instructions; the parser strips those sections from all papers.
- **"Frequency surpassing unconfounded raises a red flag"** — weakened to Minor since the paper itself acknowledges the regularization effect at line 198.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Add at least two baselines:** (a) a direct adaptation of RRR to time series (same IG explainer, same loss form — isolates what RioT's specific design choices add), and (b) a simple input-masking baseline (remove confounded timesteps from training data). This is the single highest-leverage improvement.
2. **Test the frequency-domain component on a real dataset** with naturally occurring frequency confounders (e.g., audio with a consistent background tone). If none exists, explicitly discuss this limitation and why synthetic results should be trusted.
3. **Report the λ values used** and include a sensitivity analysis (3–5 values) showing how performance varies with λ.
4. **Add a quantitative explanation alignment metric** (e.g., percentage of attribution mass falling outside the annotated confounder region before vs. after revision).

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>