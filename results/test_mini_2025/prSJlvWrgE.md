## Summary

This paper proposes Drift2Matrix, a framework that models concept drift in co-evolving time series through kernel-induced self-representation. The core idea is to learn a representation matrix Z for each sliding window such that Z is regularized to have k-block-diagonal structure (via spectral Laplacian regularization), where each block corresponds to a latent concept. Concepts are identified by applying spectral clustering to Z, and concept drift is tracked by observing how series transition between concept blocks across windows. The framework is evaluated on 12+ datasets spanning finance, energy, traffic, and weather, achieving competitive forecasting accuracy against 7 baselines including concept-aware models (OneNet, OrbitMap) and forecasting models (N-BEATS, Informer).

## Strengths

1. **Novel and principled formulation of concept drift as matrix optimization**: Drift2Matrix transforms concept identification into a block-diagonal matrix recovery problem with Laplacian regularization (Eq. 3, Theorem 4.1). This is a conceptually clean departure from ensemble-based (OneNet) or predefined-concept (OrbitMap) approaches, and the theoretical link between the regularization $\|\mathbf{Z}\|_k = \sum_{i=N-k+1}^N \lambda_i(\mathbf{L}_Z)$ and k-block-diagonality provides a principled foundation absent from prior concept-drift methods.

2. **Broad and competitive forecasting evaluation**: Table 1 reports RMSE across 30 dataset/horizon settings spanning diverse domains. Drift2Matrix achieves the lowest RMSE on roughly half of these settings (e.g., SyD 0.315 vs OneNet 0.317, MSP 0.663 vs OneNet 0.751, Weather 96 0.737 vs 0.744), and is consistently among the top-2 methods on most others. Given that the paper frames forecasting as a downstream validation task rather than the primary goal, this breadth is a genuine strength.

3. **Interpretable concept dynamics**: Figures 1–2 demonstrate that the learned representation matrices exhibit visible block-diagonal structure that evolves across windows, and the concept-tracking visualizations (e.g., Stock1 heatmap showing C2 and C5 appearing only in W6 during COVID-19) provide explicit interpretability about how series distributions shift. This level of mechanistic insight is absent from black-box or ensemble-based drift methods.

4. **Demonstrated cross-series information transfer**: Section 6.4 and Figure 3 show that Drift2Matrix can anticipate a second anomalous volatility event for stock ULTA by leveraging inter-series correlations, a capability that single-series drift models lack. This provides empirical evidence for the co-evolving design rationale.

## Weaknesses

### Fatal
None.

### Major

1. **Core contribution (concept identification) is not directly evaluated where ground truth exists.** The synthetic dataset SyD is specifically constructed with "controllability of the structures/numbers of concepts and the availability of ground truth" (Section 6.1). This is the ideal setup to measure concept identification accuracy (e.g., adjusted Rand index, normalized mutual information, or clustering purity against ground-truth concept assignments). Yet the paper only provides visual heatmaps (Fig. 1) and uses forecasting RMSE as a proxy. Forecasting accuracy conflates the downstream forecast procedure (Eq. 6) with the upstream concept identification — a method that identifies wrong concepts could still forecast well through an expressive forecasting rule. This is the central gap in the empirical validation of the paper's primary claim (Q1). The paper admits "for real datasets, we lack the ground truth" but SyD is not a real dataset — it was designed precisely to provide ground truth. This omission significantly weakens the evidence for the claimed effectiveness of concept identification.

### Minor

2. **Eq. 2 contains a mathematical inconsistency in the stated equality.** The paper writes:
   $$\frac{1}{2} \|\Phi(\mathbf{S}) - \frac{\alpha}{2} \Phi(\mathbf{S}) \mathbf{Z}\|^2 = \frac{1}{2} \text{Tr}(\mathcal{K} - \alpha \mathcal{K} \mathbf{Z} + \mathbf{Z}^T \mathcal{K} \mathbf{Z})$$
   Expanding the left side (using $\mathbf{Z}=\mathbf{Z}^T$) yields $\frac{1}{2}\text{Tr}(\mathcal{K} - \alpha\mathcal{K}\mathbf{Z} + \frac{\alpha^2}{4}\mathbf{Z}^T\mathcal{K}\mathbf{Z})$, so the quadratic term coefficient is off by a factor of $4/\alpha^2$. This does not invalidate the method — the right-hand side of Eq. 2 is a well-defined objective that can be optimized directly, and the implementation likely uses the correct form — but the stated algebraic equality is incorrect, and the left-side motivation is misleading. This should be corrected.

3. **The "consistently outperforms" claim in Section 6.3 is overstated.** The paper states "our model consistently outperforms the other models, achieving the lowest forecasting error on most datasets." Examining Table 1, OneNet matches or beats Drift2Matrix on roughly 12–15 out of 30 settings (ELD, CCD, EQD, ETTh2 192/336, ETTm1 96/336/720, Traffic 192/336, Weather 720, and others). Drift2Matrix does not "consistently outperform" — it is competitive with OneNet, leading on a slim majority of settings, often by narrow margins. The claim should be moderated.

4. **No confidence intervals or variance reported for forecasting results.** Table 1 reports only point estimates of RMSE without standard deviations or statistical significance tests. Many differences are in the third decimal place (e.g., SyD: 0.315 vs 0.317), making it impossible to assess whether observed differences are meaningful. This is a standard reporting gap.

5. **Theoretical guarantee for k-block diagonal (Theorem 4.1) is imprecise.** The regularization $\|\mathbf{Z}\|_k = \sum_{i=N-k+1}^N \lambda_i(\mathbf{L}_Z)$ penalizes the sum of the k smallest eigenvalues of the Laplacian. Setting these to zero guarantees *at least* k zero eigenvalues, meaning *at least* k connected components (blocks). The theorem's statement "equivalent to Z being k-block diagonal" would need the additional condition that the data term prevents the (k+1)-th eigenvalue from collapsing to zero. The paper's proof glosses over this distinction. In practice the data fidelity term would prevent over-segmentation, but the theoretical claim as stated is imprecise.

6. **The hyperparameter ρ (concept granularity) is introduced but never ablated.** Section 3 mentions ρ as a tunable parameter controlling whether drift is detected as gradual (more concepts) or abrupt (fewer concepts). No experiment shows how varying ρ changes the identified concepts or forecasting results. This is a missing ablation for a parameter central to the method's behavior.

### Trivial

7. The "kernel representation layer" in the Auto-D2M extension (Section 4.3) is described as a fully connected layer without bias or non-linear activation — which is a linear self-expression layer, not a kernel mapping in the RKHS sense. The "kernel" naming is potentially misleading here, though the standalone Drift2Matrix does use an actual kernel.

8. Theorems 5.1 and 5.2 add little substance: Theorem 5.1 states permutation equivariance (a basic property of self-representation), and Theorem 5.2 ("preserving local manifold structure") is stated without a precise mathematical claim or proof in the main body.

## Nice-to-Haves

- **Compare against subspace clustering methods** (SSC, LRR, kernel SSC) that also produce block-diagonal self-representation matrices for multi-cluster structure learning. This would help position Drift2Matrix within the broader literature.
- **Ablate the kernel choice**: The paper uses a Gaussian kernel but does not compare against linear or polynomial kernels. Since the kernel is central to the nonlinear modeling claim, this ablation would strengthen the paper.
- **Ablate the transition probability components** (Ψ and Λ in Eq. 4): A simpler forecasting rule (e.g., mean of past concept values) would help isolate the contribution of the probabilistic transition model.
- **Add quantitative metrics for the online forecasting experiment** (Section 6.4), such as cumulative RMSE or regret over time, rather than purely qualitative visual inspection.

## Removed Points

- **Criticism that the method is not reproducible because the objective function is ill-defined (from Critical Issue 1)**: The right-hand side of Eq. 2 is a clean, well-defined convex objective. The notational inconsistency in the "=" to the left-hand side does not make the optimization problem ill-defined or the method unreproducible. Removed because the underlying problem (coefficient mismatch) is real but the "fatal" framing is disproportionate.
- **Criticism about the k-block diagonal regularization systematically over-estimating the number of concepts**: This is a theoretical nuance that is unlikely to cause problems in practice because the data fidelity term penalizes over-segmentation. Removed the "concept identification pipeline depends on exactly k blocks" alarmism, while keeping the theoretical imprecision as a minor note.
- **Criticism that N-BEATS beats Drift2Matrix on ETTh2 720**: Noted in the main weakness about overstated claims (merged).
- **Criticism that "no evidence" is provided for integration with transformers/CNNs/RNNs**: The paper explicitly limits to an autoencoder example as a demonstration, not a claim of exhaustive compatibility. The paper states "can be easily integrated into most deep learning backbones" — the autoencoder example supports this as a proof of concept.
- **Criticism that the motion segmentation experiment (Hopkins155) is "disconnected"**: It demonstrates the method's generality as a multi-cluster structure learning technique, which is a valid form of evaluation.
- **Criticism about the limitation that the method fails with few variables**: The paper honestly acknowledges this limitation in the conclusion. Citing a paper's own stated limitation as a weakness is circular.
- **Strengths from Strength Finder that were too generic**: The claim about "leveraging cross-series correlations to predict unseen rare events" is kept as a supporting strength since it's empirically demonstrated. Generic statements about "addressing an important problem" removed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a clear tension: the paper proposes a genuinely novel framework (kernel self-representation → block-diagonal structure → concept identification) but does not evaluate its core claim directly even where ground truth is available. This is not a "your idea is wrong" criticism but a "you didn't measure what you claim to have done" criticism, which is the central issue in determining the paper's quality.

## Suggestions

1. **Add quantitative concept identification metrics on SyD**: Compute adjusted Rand index or normalized mutual information between the Drift2Matrix-assigned concept labels and the ground-truth concept assignments on SyD. This is the single most impactful addition — it directly validates the core contribution.
2. **Correct Eq. 2**: Either remove the $\frac{\alpha}{2}$ from the norm and write $\frac{1}{2}\|\Phi(\mathbf{S}) - \Phi(\mathbf{S})\mathbf{Z}\|^2$ (with absorbing α into the regularization), or fix the expansion coefficients to match the norm.
3. **Moderate the forecasting claim**: Replace "consistently outperforms" with language like "achieves competitive or best results on a majority of settings."
4. **Report standard deviations** (from multiple runs or bootstrap) for the RMSE results in Table 1.
5. **Add a ρ ablation experiment** showing how the number of identified concepts and forecasting accuracy change with ρ.
6. **Refine Theorem 4.1 and its proof** to acknowledge that the regularization enforces ≥ k blocks, with the data term ensuring exact k.

## Score and Decision

**Calibration Anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| w2C7gJqaai.md (ESE) | 2.33 | R1 (low) | Much weaker — vague proposal with minimal evaluation |
| UoGv8d3MMy.md (MCCE) | 3.00 | R1 (low) | Weaker — limited evaluation scope |
| UCeZMMyjm2.md (TSRM) | 4.50 | R1 (mid) | Similar score band, comparable breadth but less novelty |
| 7U5QE9T4hI.md (LEAF) | 5.33 | R1/R2 (mid) | Most comparable — similar topic, D2M has cleaner framework and broader eval, but LEAF has more rigorous evaluation of core claim |
| URCfZ2NgaR.md (SKI-CL) | 5.33 | R1/R2 (mid) | Similar topic and score band, D2M has novel contribution |
| qVyjN01x4P.md (TFPS) | 5.40 | R2 (mid) | Similar topic (pattern shifts), D2M's approach is cleaner but shares evaluation gaps |
| 7psWohxvxp.md (PRO-DSC) | 6.25 | R2 (mid-high) | Stronger — rigorous theory and evaluation on core claim; accepted poster |
| IRL9wUiwab.md (TSFM) | 6.00 | R1/R2 (mid) | Interesting analysis paper, different genre |

**Round 1 bracket:** 3.5–7.5 (clearly above rejected papers scoring 2-3, clearly below strong accept papers scoring 8).

**Narrowing to final score:** Compared to the most relevant anchors (LEAF 5.33, TFPS 5.40, SKI-CL 5.33), Drift2Matrix has a cleaner methodological contribution and broader dataset coverage, but a larger gap in evaluating its core claim (no quantitative concept ID metric despite ground truth). Compared to PRO-DSC (6.25, accepted), it lacks the same level of rigorous core-claim evaluation. The paper is slightly above the rejected time-series papers in this space but not enough to clear the acceptance bar.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>