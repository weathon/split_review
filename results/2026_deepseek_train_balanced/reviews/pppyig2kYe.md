## Summary

This paper proposes DeLUCA, a deep architecture for joint clustering and completion of high-dimensional data with missing entries under a Latent Union of Subspaces (LUoS) model. The architecture augments a DSC-net-style auto-encoder with a "pseudo-completion layer" that flattens and imputes incomplete input data via partially connected layers, enabling a subspace clustering network to operate on data that standard masking cannot handle. The paper claims 40%+ improvements in clustering accuracy over baselines on three face/object datasets (COIL20, Extended Yale B, ORL).

## Strengths

- **Identifies a genuine architectural bottleneck and proposes a concrete solution.** The paper correctly observes (Section 2.3, lines 83–84) that under high missing-data regimes, every feature contains missing entries, so masking any neuron with missing values would mask all neurons, rendering the network inoperable. The proposed solution — flattening the input and using partially connected layers to produce placeholder imputations before feeding into the auto-encoder (lines 85–87) — is a novel engineering contribution that addresses a real obstacle to applying auto-encoder-based subspace clustering to incomplete data.

- **The Latent UoS model is a principled generalization.** The paper explicitly frames the standard UoS model as the special case where the embedding is the identity map (Section 2, lines 45–46). This is a conceptually clean extension that correctly recognizes that real data may not lie near a UoS in its original space but may do so after a non-linear embedding.

- **Consistent pattern of reported empirical advantage.** Across all three real datasets (COIL20, Extended Yale B, ORL) and all missing-data proportions (20%–80%), the paper reports that DeLUCA outperforms all 10 baseline methods, with clustering accuracy advantages cited at 40%+ (lines 138, 142, 149) and reconstruction improvements of 5%–60% (line 158). These claims are consistent even if their verifiability is limited (see Weaknesses).

## Weaknesses

### Major

**1. No numerical results presented — all evidence is figure-only.**
The paper makes bold quantitative claims ("40% improvement," "enhancements ranging from 40% to 80%") but contains zero numerical tables reporting accuracy, completion error, standard deviations, or sample sizes. Every result is conveyed through figures (Figures 1, 5, 6, 7) whose values the reader cannot independently extract or compare against future work. For a paper whose entire contribution is empirical — a new method that purportedly beats existing approaches by enormous margins — this is a structural deficiency. The central claim cannot be verified from the paper as written.

**2. The most relevant baseline (DSC-net) is omitted.**
DeLUCA is explicitly built upon DSC-net (Ji et al., 2017) by adding a pseudo-completion layer (line 36: "we modify the DSC-net architecture... by introducing a unique pseudo-completion layer"; line 51: "the pseudo-completion layer... is where we mostly contribute"). Yet DSC-net is not included as a comparison baseline. Without comparing against DSC-net operating on the same data with a standard imputation preprocessing step (mean, SoftImpute, or zero-fill), it is impossible to determine whether the pseudo-completion layer is responsible for claimed gains, or whether DSC-net itself with any reasonable missing-data handling would perform similarly.

**3. No ablation study for the claimed main contribution.**
The pseudo-completion layer is stated to be the paper's primary contribution (line 51). No ablation experiment isolates its effect — no comparison against a version that replaces it with mean imputation, zero imputation, or SoftImpute preprocessing while keeping the rest of the architecture fixed. Without this, there is no evidence that the pseudo-completion layer drives the reported performance.

**4. Insufficient specification for reproducibility.**
Multiple architectural and training details are absent (Section 2.3): the optimizer, initial learning rate, batch size, number of training iterations, auto-encoder depth and layer widths, activation functions (beyond ReLU in the pseudo-completion layer), and the latent dimension *r* are never reported. The regularization parameters λ₁ and λ₂ are said to be "determined by iterative refinement" (line 72) but no values or ranges are given. The description of partially connected layers (line 87: "each $\mathbf{x}_{j}^{\Omega}$ nodes at $m$ intervals... were interconnected") is not precise enough to reconstruct the connectivity pattern. These omissions prevent independent reproduction or assessment of the method.

### Minor

**5. No evidence that the model actually recovers a latent UoS structure.**
The paper's core theoretical claim is that the method finds "a UoS in a latent space that can fit a non-linear embedding of the original data" (abstract). No analysis shows what the latent space looks like, whether the learned representation Z exhibits UoS structure, or what the self-expressive coefficient matrix Θ reveals. The framework is asserted but not demonstrated.

**6. Ambiguous norm notation in the loss function.**
The loss function (line 69) uses $\|\Theta\|_2$, which is ambiguous between the spectral norm (standard notation) and the Frobenius norm. The text calls it an "$\ell_2$ norm" (line 72). Since these have different optimization properties and the paper departs from SSC's standard $\ell_1$ regularization, this ambiguity should be resolved.

**7. SimpleFill listed as a baseline for image data.**
SimpleFill (last observation carried forward) is listed among the baselines (line 113) evaluated on image datasets (COIL20, Yale B, ORL). LOCF is a time-series imputation method; it has no sensible application to unordered image data, raising questions about the appropriateness of the baseline suite.

**8. Synthetic data underperformance is rationalized rather than analyzed.**
The paper reports that baselines "slightly outperform" DeLUCA on synthetic data (line 132) and explains this by saying the synthetic setup was customized to favor baselines (line 111–112). The more scientifically informative approach would be to analyze *why* this occurs — e.g., is the linear UoS assumption of baselines too rigid for real data but ideal for linear synthetic data? Does the auto-encoder's non-linearity hurt on data that is truly linear? The paper misses an opportunity to provide insight.

### Trivial

- None beyond the formatting issues attributable to the PDF extraction process.

## Nice-to-Haves

- Include DSC-net as a baseline with standard imputation preprocessing. This is the most informative comparison for isolating the contribution of the pseudo-completion layer.
- Perform an ablation replacing the pseudo-completion layer with mean/zero/SoftImpute preprocessing.
- Report the chosen hyperparameters (λ₁, λ₂, learning rate, architecture geometry, optimizer) so the work can be reproduced.
- Visualize the learned latent representation Z and the self-expressive coefficients Θ to demonstrate the claimed latent UoS structure.
- Analyze why DeLUCA underperforms baselines on synthetic (linear-UoS) data but outperforms them on real data — this pattern is potentially interesting and could strengthen the paper if properly explained.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Characterization of prior work is overly broad and dismissive"* — This is standard introductory style for a short paper; not a substantive weakness.
- *"The claim that none of these methods can handle large amounts of missing data is not supported by a reference"* — It IS supported by a reference (Pimentel-Alarcon & Nowak, 2016, cited at line 12). Removed because factually incorrect.
- *"Writing quality is uneven / use of superlatives"* — Style/presentation nitpick; parser artifacts may have introduced some issues. Removed per formatting nitpick rule.
- *"Related work section is loosely organized"* — Subjective opinion about organizational style rather than a specific, verifiable weakness.
- *"The comparison on synthetic data may be rigged in DeLUCA's favor on real data"* — Speculative; the paper's own explanation (baseline-favoring synthetic setup) is a valid experimental design choice for demonstrating robustness.
- *"Memory usage claim is unsubstantiated"* — While technically true, this claim appears once in the abstract and is not central to the paper's contribution.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add at least one table reporting exact clustering accuracy and completion error (with standard deviations over multiple missingness patterns and random seeds) for DeLUCA and every baseline at every missing-data proportion tested. This is the single most impactful improvement.
2. Include DSC-net as a baseline, with the same data preprocessed by a reasonable imputation method (e.g., mean, SoftImpute, zero-fill). Without this, the contribution of the pseudo-completion layer cannot be isolated.
3. Add an ablation experiment that replaces the pseudo-completion layer with simple imputation while keeping the auto-encoder and self-expressive layers fixed.
4. Report the missing architectural and training details (optimizer, learning rate, batch size, layer sizes, latent dimension, regularization parameter values).
5. Clarify the norm notation in the loss function: distinguish $\|\Theta\|_2$ (spectral) from $\|\Theta\|_F$ (Frobenius) if the latter is intended.
6. Provide a visualization or quantitative analysis of the latent space Z and self-expressive matrix Θ to substantiate the claim that a latent UoS structure is being recovered.

**MY FINAL SCORE: <score>3.5</score>**
**MY FINAL DECISION: <decision>Reject</decision>**