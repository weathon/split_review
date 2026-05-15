Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

This paper proposes NN-ResDMD, a method that learns Koopman operator eigenpairs by directly minimizing the spectral residual (from ResDMD) as a loss function, using feedforward neural networks to parameterize the dictionary functions. The key idea is to optimize dictionary functions toward spectral accuracy rather than prediction error (as in EDMD), eliminating the need for manual basis selection and post-hoc spectral filtering. Experiments on a pendulum system, turbulence data, and neural recordings from mice visual cortex demonstrate improved performance over EDMD, Hankel-DMD, ResDMD, and Kernel ResDMD.

## Strengths

- **Direct spectral residual minimization for Koopman eigenpairs**: NN-ResDMD computes eigenpairs by minimizing the spectral residual directly (Section 3.2, Equation 3.5), avoiding the need to filter precomputed results from other methods as ResDMD does. This is a principled and well-motivated departure from the standard ResDMD pipeline.

- **Automatic basis function learning via neural networks**: The method uses an FNN to parameterize dictionary functions and optimizes them to minimize the spectral residual (Section 3.2). This addresses a real practical limitation of EDMD-based methods — the need for manual dictionary selection — which is particularly valuable for high-dimensional systems where optimal basis functions are unknown a priori.

- **Promising performance across diverse systems**: The pendulum experiment (Section 4.1) shows that NN-ResDMD captures the full Koopman spectrum with 300 observables versus ~964 for ResDMD. In turbulence (Section 4.2), the method produces a first Koopman mode that qualitatively captures the global pressure field pattern. The neural dynamics experiment (Section 4.3) provides evidence of better clustering of brain states across multiple mice, with lower Davies-Bouldin indices reported for NN-ResDMD across all five subjects (Figure 6F).

- **The paper acknowledges limitations**: Section 5 honestly discusses several shortcomings (hyperparameter sensitivity, deterministic nature, lack of noise model), which is better than overclaiming.

## Weaknesses

### Fatal

None.

### Major

1. **Uncontrolled experimental comparisons — different numbers of eigenfunctions across methods.** In the neural dynamics experiment (Section 4.3), the compared methods use vastly different numbers of eigenfunctions: NN-ResDMD uses 501, Hankel-DMD uses 50, EDMD+RBF uses 1301, and Kernel ResDMD uses 299. The Davies-Bouldin Index is sensitive to the number of points and dimensionality. No controlled experiment is performed with equal eigenfunction counts across methods, making it impossible to attribute the lower DBI to the method rather than to this confound. The paper also does not specify whether DBI is computed on the original eigenfunction features or on the MDS-reduced 2D embedding — if the latter, the metric is unreliable for comparing methods.

2. **Unsubstantiated claim about theoretical guarantees.** The paper states that NN-ResDMD "retains the theoretical convergence guarantees" of ResDMD (Section 3.2). ResDMD's guarantees (Colbrook & Townsend, 2024) concern the spectral residual as a convergence measure for a *fixed* dictionary as data or dictionary size increases. NN-ResDMD introduces a dictionary learned via non-convex gradient descent on a finite dataset. No analysis is provided to show that the learned dictionary satisfies the assumptions (closedness, denseness) needed for these guarantees to apply, nor is it established that the optimization reaches a minimizer yielding low residual. This claim is stated without justification and could mislead readers about the theoretical strength of the method.

3. **Turbulence comparison is purely qualitative.** Section 4.2 presents a single Koopman mode from NN-ResDMD alongside a claim that Kernel ResDMD "is unable to produce a Koopman mode similar to the first Koopman mode from NN-ResDMD." No quantitative error metrics (e.g., spatial correlation with the true pressure field, signal-to-noise ratio, or residual values for all methods) are provided. The Kernel ResDMD comparison result is referenced to "the original work" rather than shown directly. This weakens the evidence for the claimed superiority on this system.

### Minor

1. **Imprecise presentation of the optimization derivation in Section 3.2.** The paper states that "the optimal Koopman matrix $\tilde{K}$ is obtained by minimizing" the total residual $J$, and that $\tilde{K} = G^\dagger A$ follows from this. The derivation is deferred to Appendix A.2 (which is stripped by the parser). In the main text, the equivalence $J = \frac{1}{m}\|(\Psi_Y - \Psi_X K)V\|_F^2$ relies on the eigenfunction normalization mentioned on line 117 (where the paper notes "Without loss of generality, we consider [φ] has been normalized"). The text could be clearer about this assumption and about why $G^\dagger A$ is the appropriate matrix (the dependence of $V$ on $K$ makes a direct "minimization of J" claim without additional justification potentially misleading to readers). The actual algorithm — alternating between computing the standard EDMD matrix $K = G^\dagger A$ and updating $\theta$ via gradient descent on the spectral residual — is sound, but the presentation of the derivation should be tightened.

2. **Pendulum pseudospectrum visualization lacks quantitative detail.** The shaded region (pseudospectrum) is shown without specifying the error tolerance $\varepsilon$ used. The paper also does not compare NN-ResDMD against baseline methods at equal basis counts or equal total parameter counts (the neural network has many more trainable parameters than the 300 coefficients of the fixed dictionary, making the comparison of "300 vs 964 basis functions" somewhat misleading without accounting for parameter count).

3. **No ablation or controlled experiments to isolate the contribution of the spectral residual loss.** The pendulum experiment could be strengthened by comparing NN-ResDMD against (a) the same neural network architecture with fixed random weights, and (b) a dictionary learned via EDMD with the same architecture but trained on the prediction-error loss $\|\Psi_Y - \Psi_X K\|_F^2$ instead of the spectral residual loss. Such ablations would disentangle the benefit of learning from the benefit of the specific spectral-residual objective.

4. **Missing details about the clustering evaluation pipeline.** The paper does not fully specify how eigenfunctions are converted to feature vectors per trial for clustering, nor whether the DBI is computed on the original eigenfunction coefficients or on the MDS-reduced embedding. This is needed for reproducibility.

### Trivial

- Several inline references appear garbled (e.g., "Section 7.1 for a justification" on line 180), likely due to the parsing process, not author error.

## Nice-to-Haves

- A synthetic experiment with a known discrete Koopman spectrum (e.g., a linear system with known eigenvalues) would allow direct quantitative error measurement (e.g., Hausdorff distance between computed and true eigenvalues).
- A runtime/scalability benchmark as a function of state dimension would support the claimed scalability.
- Reporting the evolution of the loss $J(\theta)$ and Koopman eigenvalues during training, along with sensitivity to random seeds, would improve reproducibility.

## Removed Points

- **"The derivation of the optimal Koopman matrix is mathematically inconsistent" (Critical Issue 1 from harsh critic).** The paper states on line 117 that eigenfunctions are normalized ($\|\phi\|=1$, garbled by parser). With this normalization, $J = \frac{1}{m}\|(\Psi_Y - \Psi_X K)V\|_F^2$ follows correctly (the denominator in each squared residual becomes $m$). The claim that $\tilde{K} = G^\dagger A$ minimizes $J$ is imprecise as a standalone statement (since $V$ depends on $K$), but the actual method is sound: $K$ is computed as the standard EDMD matrix and $J$ is used as the loss to train $\theta$. The derivation is referenced to Appendix A.2 for full details. This is a presentation issue, not a mathematical inconsistency, and has been moved to Minor Weakness #1 above.

- **"No attempt is made to control for the number of features" and "DBI on the 2D embedding" (from critical issue 2).** The claim about uncontrolled comparisons is retained as Major Weakness #1, but the specific assertion that DBI is computed "on the 2D MDS embedding" is not clearly supported by the paper text — the paper separates MDS (for visualization) from DBI (for quantification), and it is ambiguous what DBI input features are. This specific sub-point is removed.

- **"Missing appendix" claims.** The parser strips appendices; the paper likely contains Appendix A.2 as referenced. Criticisms about absent appendices are removed per instructions.

- **Pure formatting/style nitpicks, typos, and missing figure content.** Removed per instructions.

- **Criticisms about "not yet released" or nonexistent references.** Not applicable; the paper cites published works and open datasets.

- **"The claim about unfair comparison with other methods" when the asymmetry favors baselines.** Not applicable.

## Novel Insights

None beyond the paper's own contributions. The core observation — that spectral residuals from ResDMD can be used as a differentiable training objective for neural network dictionaries — is the paper's contribution itself.

## Suggestions

1. **Run a controlled synthetic experiment** where the Koopman spectrum is known exactly (e.g., a linear system or a well-understood nonlinear oscillator). Compare all methods with equal numbers of eigenfunctions, and report quantitative errors (e.g., mean absolute eigenvalue error, Hausdorff distance of pseudospectra).

2. **Conduct an ablation study** in the pendulum setting that isolates the effect of the spectral residual loss from the effect of neural network learning. Compare: (a) NN-ResDMD, (b) same network with fixed random weights, (c) network trained on the EDMD prediction-error loss $\|\Psi_Y - \Psi_X K\|_F^2$, (d) EDMD with a manually chosen dictionary of matched size.

3. **Perform a controlled eigenfunction count experiment** on the neural dynamics data: run all methods with the same number of eigenfunctions (e.g., 50 or 100) to verify that the DBI improvement is not an artifact of higher dimensionality.

4. **Clarify the DBI computation pipeline** explicitly: state whether DBI is computed on the original eigenfunction coefficients or on MDS-reduced features; describe how time-series eigenfunctions are aggregated into per-trial feature vectors.

5. **Tone down or qualify the theoretical guarantee claim.** Acknowledge that ResDMD's convergence guarantees apply to fixed dictionaries and do not automatically extend to dictionaries learned via non-convex optimization.

6. **Add quantitative metrics to the turbulence comparison:** report residual values for all methods and spatial correlation with the known pressure field.

## Score and Decision

This paper presents a well-motivated and reasonable idea — using spectral residuals as a loss to learn Koopman dictionaries — and demonstrates potential on three distinct systems. However, the experimental evaluation has significant confounds (different eigenfunction counts across methods, purely qualitative turbulence comparison, lack of ablations) that weaken the central empirical claims. The theoretical guarantee claim is stated without justification. These issues are addressable with additional experiments and clarifications, but as presented, the paper does not provide fully convincing evidence for its claimed advantages.

**Score: 5.0**

**Decision: Reject**

The core idea has merit, and I would encourage the authors to strengthen the evaluation (controlled eigenfunction counts, ablations, quantitative metrics) and resubmit. The contribution is worthwhile but the current experimental evidence does not support the strength of the claims made.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>