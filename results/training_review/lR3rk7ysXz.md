Now I have a thorough understanding of the paper and all reviewer claims. Let me synthesize the final review.

## Summary

The paper investigates diffusion models for anomaly detection and proposes Diffusion Time Estimation (DTE), an approach that replaces the iterative denoising computation of DDPM with a single-pass neural network that predicts the diffusion time (equivalently, noise level) of an input. DTE is derived from an inverse Gamma posterior over noise variance, connected theoretically to kNN, and evaluated on all 57 ADBench datasets. The key findings are that DTE achieves competitive anomaly detection performance while providing orders-of-magnitude faster inference than DDPM, and that it outperforms prior deep learning methods in the semi-supervised setting.

## Strengths

- **Drastic inference speedup with competitive accuracy**: DTE achieves the fastest inference among all methods evaluated (Figure 1) while matching or exceeding the performance of DDPM and all prior deep learning baselines on the 57-dataset ADBench benchmark. This directly supports the paper's central claim that DTE is a scalable alternative to DDPM.

- **Extensive and rigorous empirical evaluation**: The paper evaluates on all 57 ADBench datasets spanning tabular, image, and natural language data, in both unsupervised and semi-supervised settings, reporting mean AUC ROC over 5 seeds. This breadth is substantially more thorough than typical anomaly detection papers and strengthens the generalizability of the claims.

- **Principled probabilistic derivation connecting diffusion time to anomaly scores**: The derivation of the posterior over noise variance (inverse Gamma distribution with shape parameter d/2−1 and scale parameter related to distance from the data manifold) provides a theoretical foundation that goes beyond heuristic reconstruction distances. The connection to kNN through the non-parametric estimator (same anomaly ranking) offers interpretability and explains why DTE can match kNN's strong performance.

- **Competitive with both classical and deep learning methods**: DTE outperforms all prior deep learning methods (DeepSVDD, DAGMM, DROCC, GOAD, ICL) and is competitive with the top classical method (kNN) in the semi-supervised setting. This is notable given the well-documented difficulty of deep methods matching classical approaches on tabular data (ADBench).

## Weaknesses

### Fatal
None. The training-inference distribution concern (trained on noisy x_t, applied to clean test inputs) raised by the harsh critic is not fatal — the paper provides justification ("provided that the noisy samples cover the entire feature space, this procedure should also capture potential anomalies," §3), and the method's mechanism is sound: the model learns a function mapping any point in ℝ^d to its equivalent diffusion timestep, which serves as a distance-to-manifold proxy. However, the paper would benefit from clearer exposition (see Minor weaknesses below).

### Major
None that threaten the core claims. The paper's experimental results, speed advantage, and theoretical grounding are substantiated.

### Minor

1. **Ambiguity about test-time input processing**: The paper states that the parametric models are trained on noisy samples x_t (with known timestep t) but does not clearly explain how test-time inference handles clean (non-noisy) inputs. The justification that noisy training samples "cover the entire feature space" (§3) implicitly addresses this — the model learns a distance-to-manifold proxy — but the paper should explicitly state whether test inputs are (a) fed as-is (clean), (b) noised with a fixed small σ before being input to the network, or (c) averaged over multiple noise realizations. This ambiguity weakens the otherwise clear theoretical narrative. This is addressable in a revision and does not undermine the empirical results.

2. **DDPM baseline may be sub-optimally configured**: The paper acknowledges that "the choice of timestep at the start of reverse diffusion is arbitrary, yet it can significantly affect the anomaly detection performance" (§3) and uses a fixed 25% of maximum timestep across all datasets. While an ablation study is referenced (in the stripped appendix), the reported DDPM results (median AUC ~0.75–0.8) could be depressed relative to what per-dataset tuning might achieve. Since DTE is explicitly compared against DDPM on both performance and speed, this weakens the claim that DTE "outperforms" DDPM.

3. **Inverse Gamma approximation not validated**: The derivation uses a log-sum-exp → max approximation (Eq. 3) and then replaces max with k-nearest-neighbor mean in practice (Eq. 4). The paper does not measure how well the inverse Gamma distribution with fixed shape (d/2−1) fits the empirical posterior over diffusion time on real data. Figure 4 shows the analytical vs. non-parametric posterior for one dataset but does not quantify the goodness-of-fit of the inverse Gamma assumption itself. The categorical model (§3.3) abandons this assumption, suggesting the authors themselves recognize its limitations.

4. **Overstated framing of DDPM performance**: The abstract claims DDPMs "are performant" on anomaly detection, yet Figure 2 shows DDPM with median AUC around 0.75–0.80 in the semi-supervised setting — below several classical methods and DTE. While "performant" is relative, the framing could better match the empirical results.

### Trivial

- The d > 2 restriction for the inverse Gamma shape parameter is acknowledged (§3.1: "this analysis is only valid for three or higher dimensions") but the paper does not check which ADBench datasets have d ≤ 2 or discuss any special handling. Given that the vast majority of tabular datasets have far more than 2 features, the impact is likely negligible but the omission is notable.
- The "Choice of representation" discussion (important for interpreting the image dataset results) is relegated to the appendix; it would benefit from a brief mention in the main text.

## Nice-to-Haves

- A sensitivity analysis of the number of bins for the categorical model would strengthen claims about robustness.
- Measuring the divergence (e.g., KL) between the empirical posterior of diffusion time and the fitted inverse Gamma with fixed shape would validate the theoretical derivation.
- Testing whether adding a small fixed noise to test inputs before feeding to the parametric model improves or degrades results.

## Removed Points

The following points from the harsh critic were checked against the paper and removed for the stated reasons:

- **"Non-parametric DTE reduces to kNN, undermining claimed novelty"**: The paper transparently acknowledges this connection (§3.2: "the anomaly rankings given by these methods are identical") and presents it as a theoretical insight, not a standalone novel contribution. The claimed novelty is the parametric DTE framework, which is a new method. No novelty claim is undermined.

- **"Unaddressed domain restriction in the analytical posterior"**: The paper explicitly states "as a > 0 ⇒ d > 2, this analysis is only valid for three or higher dimensions" (§3.1). The limitation is acknowledged, not unaddressed. Whether any ADBench dataset has d ≤ 2 is a fair question but the critic's framing as "unaddressed" is inaccurate.

- **"DDPMs are 'performant' not supported by the paper's own results"**: The paper's results show DDPM outperforming several deep baselines (DeepSVDD, DAGMM) and being competitive with classical methods. "Performant" is a relative term that is reasonably supported by the data.

- **"Training-inference mismatch breaks the core narrative"**: As analyzed above, the paper's justification (training on noisy samples covering the entire space) is sufficient for the method to work. The approach is sound; the paper would benefit from clearer exposition but the narrative is not "broken."

- **Missing related works**: Removed per instructions — I cannot independently verify the existence or relevance of unspecified methods.

- **All formatting/style nitpicks**: Removed per instructions (these are parser artifacts, not author errors).

## Novel Insights

The harsh critic's concern about test-time input handling, while not fatal, points to a genuine gap in the paper's exposition that could confuse readers. More interestingly, the fact that the categorical model — which makes no distributional assumptions — empirically outperforms the theoretically-motivated inverse Gamma model suggests that the primary value of DTE may lie not in its probabilistic derivation but in its ability to learn a diffusion-time proxy via a simple classification/regression objective. This raises the question of whether the inverse Gamma derivation is necessary at all, or whether direct regression of diffusion time (ℓ₂ loss) with a standard neural network would suffice. The paper's Figure 4 shows that the ℓ₂ regression model has high bias for small timesteps, providing some evidence that the inverse Gamma parameterization matters, but the categorical model (which abandons the inverse Gamma form) performs best overall. This tension between theoretical elegance and practical effectiveness is an interesting nuance.

## Suggestions

1. **Clarify test-time inference**: Explicitly state whether test inputs are fed as-is or with added noise. If as-is, explain that the model learns a function over the entire ℝ^d and that a clean input's predicted timestep measures its distance from the data manifold by proxy — the model was trained on noisy samples at all distances and therefore generalizes. If noise is added, specify the noise level and justify the choice.

2. **Tune or ablate the DDPM starting timestep per dataset**: Either perform per-dataset tuning and report the best results, or run a grid over starting timesteps for a representative subset of datasets to demonstrate that the fixed 25% choice is not artificially deflating DDPM's performance.

3. **Validate the inverse Gamma assumption**: Compute the KL divergence between the empirical posterior (kernel density estimate from noisy samples) and the fitted inverse Gamma with the assumed shape parameter for several datasets, ideally spanning different dimensionalities.

## Score and Decision

The paper makes a genuine contribution: DTE is a computationally efficient anomaly detection method with a theoretical basis, strong empirical validation on 57 datasets, and a clean connection to kNN. The weaknesses are addressable — the most significant is the need for clearer exposition of test-time inference, not a fundamental flaw. The paper's claims are well-supported by its experiments.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>