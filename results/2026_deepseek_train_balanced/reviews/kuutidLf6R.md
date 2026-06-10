## Summary

This paper identifies a genuine limitation in existing data attribution methods for diffusion models (particularly D-TRAK): using scalar loss functions as the model output for attribution discards dimensional information and conflates predicted-distribution shifts with the data distribution itself. The authors propose Diffusion Attribution Score (DAS), which measures training-sample influence via the KL-divergence between noise-predictor distributions, and derive a tractable approximation using linearization, Newton's method, and the Sherman–Morrison formula. Experiments across CIFAR, CelebA, and ArtBench datasets with DDPMs and Stable Diffusion show consistent LDS improvements over D-TRAK, and a counterfactual visualization experiment provides orthogonal evidence that DAS-identified influencers produce larger actual image changes.

## Strengths

- **Principled diagnosis of why D-TRAK's loss-based attribution is flawed.** Section 4.1 (Eq. 7–8) decomposes D-TRAK's loss-based approximation into the true KL-divergence between predicted distributions minus a cross-entropy term involving the data distribution $q$. This shows rigorously that D-TRAK conflates the effect of data removal with the effect of the data distribution itself — a counterintuitive finding prior work noted but did not explain.

- **Toy experiment directly validates the core hypothesis.** Section 5.4 measures Pearson correlation between actual $L^2$ image distance and (a) loss differences ($r = 0.257$) vs. (b) noise predictor output differences ($r = 0.485$). This provides direct evidence that the proposed output function captures actual generation changes nearly twice as well as the loss-based approach — and is a clean, interpretable experiment.

- **Counterfactual visualization provides evaluation orthogonal to LDS.** Section 5.6 shows that removing DAS-identified top-1000 influencers yields larger $L^2$ distances (10.58 vs. 8.97 on CIFAR-2) and lower CLIP similarities (0.71 vs. 0.77) than D-TRAK. This evidence does not depend on the Simple Loss metric used in LDS and directly demonstrates that DAS identifies more causally influential training samples.

- **Consistent improvements across multiple datasets and architectures.** DAS outperforms D-TRAK on all reported settings (CIFAR-2/+9.33%, ArtBench-2/+8.39%, CelebA/+5.1%, CIFAR-10/+12.67%, ArtBench-5/+10.21% on validation sets). Notably, DAS with only 10 timesteps often beats D-TRAK with 100 timesteps, underscoring the method's efficiency advantage beyond just accuracy.

## Weaknesses

### Fatal
None.

### Major

- **LDS evaluation uses the very output function the paper criticizes.** The paper argues that Simple Loss "cannot represent such a contribution accurately" (abstract) and "introduces error" (Section 5.4), yet the main LDS evaluation (line 260) adopts "the output function setup from D-TRAK, setting $f(z^{\text{test}},\theta)$ as the Simple Loss for fairness." This creates a significant tension: if Simple Loss truly is a poor measure of distributional change, then high LDS on Simple Loss does not directly support the paper's central claim. The counterfactual visualization experiment (Strength 3) partially mitigates this concern, but the paper's primary quantitative evaluation metric does not align with its own theoretical framework. The authors should either (a) also report LDS using a ground-truth output function consistent with DAS (e.g., the noise predictor output norm), or (b) explicitly justify why Simple Loss is a valid evaluation target even if it is invalid for attribution.

### Minor

- **Unvalidated approximations in the derivation chain.** The derivation from KL-divergence (Eq. 9) to the computable DAS formula (Eq. 16) involves three leaps: (1) KL→$\mathbb{E}[\|\epsilon_\theta - \epsilon_{\theta_{\setminus i}}\|^2]$ (asserted without derivation), (2) linearization of the noise predictor, and (3) a single Newton step to estimate $\theta^* - \theta_{\setminus i}^*$ using the noise predictor output as the objective function. Each step is a plausible approximation, but none comes with an error bound, diagnostic test, or direct validation (e.g., comparing the Newton-step approximation against actual leave-one-out retraining on a small-scale experiment). While this level of heuristic approximation is common in influence-function work, the paper's claim of "rigorous theoretical analysis" (abstract) is overstated.

- **Varying random seeds across datasets make cross-dataset comparisons unreliable.** The paper notes (line 287) that CIFAR-10 and CelebA LDS evaluations use only 1 random seed per subset, while other datasets use 3 seeds. The paper acknowledges this may cause inaccuracies, but this means the reported improvements on CIFAR-10 (+12.67%) and CelebA (+5.1%) may have larger uncertainty than indicated. Standardized evaluation across all datasets would strengthen the claims.

- **CLIP-based candidate screening conflates content similarity with causal influence.** The acceleration technique in Section 4.3 uses CLIP similarity to select the top-1,000 training samples most similar to the target, then computes DAS only on this subset. A training sample that is visually dissimilar but causally influential (e.g., shaping texture or composition priors) would be screened out. This technique is presented as auxiliary (not used in the main comparison), and its LDS evaluation only measures ranking within the CLIP-selected set — a much easier task than identifying influential samples from the full dataset. This should be clearly caveated or evaluated separately.

### Trivial

- **The identity matrix $I$ in Eq. 8 (D-TRAK formula) is confusing.** The paper states D-TRAK "simplifies the residual term to an identity matrix," but the resulting notation $\phi(z)^\top(\Phi^\top\Phi)^{-1}\phi(z^{(i)})I$ mathematically reduces to multiplying by $I$, which is a no-op. It is clear what is intended (replacing the scalar residual $r^{(i)}$ from TRAK with a simplified identity residual), but the presentation is ambiguous and should be clarified.

- **No dedicated limitations/discussion section.** The paper presents only positive results and acknowledges limitations only in passing (line 287 on seeds, line 271 on timestep trade-offs). A brief limitations paragraph discussing when DAS might underperform or what assumptions could break would improve credibility.

## Nice-to-Haves

- **Report absolute LDS values alongside percentage improvements.** The paper reports only relative gains (e.g., "+9.33%") without the absolute baseline LDS scores. While the missing tables (images not parsable) likely contain these numbers, the absolute values should be stated in the text for readers to assess practical significance.

- **Include a compute-controlled comparison.** DAS uses projection dimension $k=32768$, the same as D-TRAK in the main comparison, so the comparison is controlled along that dimension. However, reporting wall-clock time or total gradient computation cost would help practitioners assess the practical cost-benefit tradeoff.

## Removed Points

*These points were flagged by reviewers but are removed or downgraded per the filtering rules:*

- **"No absolute value reporting"** — The tables (Tables 1–3) are embedded as images in the PDF. This is a text-extraction artifact, not an author omission. The absolute numbers exist in the submission.
- **"Derivation missing proof in appendix"** — The paper references a proof in the appendix (line 166). The appendix was stripped by the parser; it exists in the original submission.
- **"Comparison may be unfair because DAS uses more compute"** — The main comparison (line 280) limits DAS to projection only at the same dimension $k=32768$ used by D-TRAK. DAS and D-TRAK use the same projection method and dimension; the comparison is controlled.
- **"Toy experiment shows only weak support"** — The finding $r=0.485$ vs. $0.257$ (nearly 2×) is meaningful evidence for a single-proxy experiment on 60 samples. The critic's framing that "76% of variance is unexplained" is misleading when comparing correlations.

## Novel Insights

None beyond the paper's own contributions. The paper's central insight — that scalar loss-based attribution in diffusion models loses dimensional information and conflates distribution shifts with data distribution — is itself the key novel observation. The reviews do not surface a separate insight not already present in the paper.

## Suggestions

1. **Align the LDS evaluation with the paper's own theory.** Report LDS using an output function consistent with DAS (e.g., the squared norm of the noise predictor output, $\mathbb{E}_{t,\epsilon}[\|\epsilon_\theta(x_t,t)\|^2]$) alongside the Simple Loss results. This would resolve the central inconsistency and directly test whether DAS improves prediction of the quantity it was designed to measure.

2. **Validate the Newton-step approximation on a small-scale experiment.** On CIFAR-2, actually retrain leave-one-out models for a subset of training samples and compare $\theta^* - \theta_{\setminus i}^*$ against the Newton-step estimate. Even a single figure showing this correlation would substantially increase confidence in the core approximation.

3. **Standardize the LDS evaluation protocol** by using the same number of random seeds across all datasets, and report confidence intervals or standard deviations over the $M$ subsets to establish statistical significance.

4. **Add a brief limitations paragraph** discussing when DAS might fail (e.g., if linearization is poor far from convergence, or if the Gauss-Newton approximation degrades).

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>