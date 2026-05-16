Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

## Summary

This paper proposes Drift2Matrix, a kernel-induced self-representation framework for identifying latent concepts, tracking concept drift, and forecasting in co-evolving time series. The method uses a kernelized self-representation objective with block-diagonal regularization (enforcing k-block structure in the representation matrix) to identify concepts, then tracks their evolution across sliding windows using a probabilistic model, and forecasts future values by weighting past observations by concept membership. The paper reports strong forecasting results (lowest RMSE on 11/14 datasets) and qualitative demonstrations of concept identification.

## Strengths

- **Theoretically grounded concept identification via block-diagonal regularization**: Theorem 4.1 formally shows that the regularization term \(\sum_{i=N-k+1}^{N}\lambda_i(\mathbf{L}_{\mathbf{Z}})\) equals zero iff the representation matrix \(\mathbf{Z}\) is \(k\)-block diagonal, establishing a principled link between the optimization objective and the number of distinct concepts. This is a formal guarantee absent from many heuristic concept-drift methods.

- **Strong forecasting accuracy across diverse real-world datasets**: Table 1 reports that Drift2Matrix achieves the lowest RMSE on 11 of 14 datasets, outperforming dedicated concept-drift methods (Cogra, OneNet, OrbitMap) and high-capacity deep learners (Informer, N-BEATS). The margins on datasets like Stock1 (0.07 vs. 0.11) are substantial.

- **Ability to forecast concepts unseen in a single series by leveraging inter-series correlations**: The online forecasting experiment on Stock2 (Fig. 3) shows Drift2Matrix correctly anticipating a second anomalous high-volatility event after observing the first anomaly in a related series, demonstrating a capability that single-series drift models lack without periodic patterns.

- **Interpretable output**: The block-diagonal representation matrices and t-SNE visualizations of concept clusters allow analysts to trace which series belong to which concept and observe drift as blocks shift over time — offering transparency beyond black-box forecasting models.

- **Flexible deep learning integration**: Section 4.3 describes an Autoencoder variant (Auto-D2M) where the kernel representation layer is implemented as a trainable linear layer, making the approach plug-and-play for existing architectures.

## Weaknesses

### Fatal
None.

### Major

- **Mathematical inconsistency in the kernel objective (Eq. 2)**: The paper states \(\frac{1}{2}\|\Phi(\mathbf{S})-\frac{\alpha}{2}\Phi(\mathbf{S})\mathbf{Z}\|^2 = \frac{1}{2}\operatorname{Tr}(\mathcal{K}-\alpha\mathcal{K}\mathbf{Z}+\mathbf{Z}^{\top}\mathcal{K}\mathbf{Z})\). The correct expansion yields \(\frac{1}{2}\operatorname{Tr}(\mathcal{K}-\alpha\mathcal{K}\mathbf{Z}+\frac{\alpha^2}{4}\mathbf{Z}^{\top}\mathcal{K}\mathbf{Z})\). The \(\alpha^2/4\) factor is missing from the last term. The paper claims \(\alpha\) "preserves the local manifold structure" and defers explanation to §5.2, but §5.2 provides no derivation or justification. This is a structural issue in the core formulation: if the objective function is incorrectly specified, it undermines confidence in the entire method. The authors must clarify whether this is a typo, whether \(\alpha\) is implicitly set to 2, or whether the expansion was intended differently.

- **No direct quantitative evaluation of concept identification or drift tracking**: The paper states three core objectives: (O1) identify concepts, (O2) track their drift, and (O3) forecast. Yet the primary quantitative experiment (Table 1) evaluates only forecasting (O3). For the synthetic dataset (SyD), where ground-truth concepts are available, no quantitative metric (e.g., NMI, ARI, concept-transition accuracy) is reported — only qualitative visualizations (Fig. 1). The paper itself concedes: "For real datasets, we lack the ground truth for validating the obtained concepts." This is an evidential gap: the paper's claimed novelties (concept identification and drift tracking) are not directly validated, and forecasting RMSE alone is an insufficient proxy.

### Minor

- **Ad-hoc drift probability mechanism (Eq. 4–5)**: The probability \(P(\mathbf{C}_r\to\mathbf{C}_m|\dots)\) combines an "immediate risk" \(\Psi\) and a "global transition likelihood" \(\Lambda\) defined via heuristic min/max ratios. While not invalid, this component is presented without derivation from any statistical principle (e.g., maximum likelihood, Bayesian updating) and lacks sensitivity analysis for its free parameters (e.g., \(\tau\) in Eq. 6). The notation in Eq. 4 is also needlessly confusing (summing over \(\zeta\) in the numerator but \(\zeta_1,\zeta_2\) in the denominator).

- **Missing standard deviations / error bars in forecasting results**: Table 1 reports only point estimates (RMSE), with no indication of variance across runs. Given the stochastic nature of some baselines (e.g., neural methods), this makes it difficult to assess whether performance differences are statistically significant.

- **Confusing baseline presentation**: The paper claims evaluation "against seventeen different models" but then names only seven (ARIMA, KNNR, Informer, N-BEATS, Cogra, OneNet, OrbitMap) and does not list the remaining ten. The phrase "Results for the extended Auto-D2M are included but not part of the comparison" is also unclear.

- **Auto-D2M integration lacks full specification**: Section 4.3 does not state whether the self-representation matrix \(\Theta_{\mathbf{s}}\) in the deep learning variant inherits the symmetry and non-negativity constraints (\(\mathbf{Z}=\mathbf{Z}^\top\ge0\), \(\operatorname{diag}(\mathbf{Z})=0\)) from the original formulation, nor how the number of concepts \(k\) is determined in this variant. This raises reproducibility concerns.

### Trivial

- **Theorem 5.1 (permutation invariance)**: This result is immediate from the formulation and does not constitute a substantive theoretical contribution.
- **No analysis of the \(\rho\) hyperparameter**: The paper introduces \(\rho\) to control gradual vs. abrupt drift but provides no empirical or analytical study of its effect.
- **The phrase "paradigm shift" in the contributions (end of §1)** overstates what is validated by the evidence presented.

## Nice-to-Haves

- **Direct concept-evaluation metrics**: For the synthetic dataset, report NMI or ARI between discovered and ground-truth concepts, along with drift-transition accuracy. This would significantly strengthen the paper's core claims.
- **Ablation isolating each component**: Separately evaluate the contribution of kernelization, block-diagonal regularization, the immediate-risk term \(\Psi\), and the global likelihood \(\Lambda\).
- **Computational complexity and runtime analysis**: The method involves eigenvalue decomposition per window; the paper mentions complexity analysis in §6.5 (point 7) but does not present it in the main text.
- **Sensitivity analysis for \(\tau\) and \(\alpha\)**: Show how forecasting performance varies with these parameters.
- **Replace the heuristic drift formulas with a principled framework** (e.g., Bayesian update, hidden Markov model), or at minimum provide a clearer derivation and justification for the min/max construction in \(\Lambda\).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Theorem 5.2 proof is relegated to the appendix"**: This is standard practice for conference papers; the parser strips appendices. The paper format is not a weakness.
- **"The paper should also cover Y / domain Z"**: Demands to expand the scope beyond what the paper sets out to do are not valid criticisms.
- **"The 'paradigm shift' claim overstates the contribution" (as a separate weakness)**: While noted above under Trivial for completeness, the substantive point is not that the phrasing is immodest but that the evaluation does not fully support the claimed contributions — this is already captured by the Major weakness on evaluation.
- **Notation confusion about \(\zeta\) in Eq. 4**: The summation indices are clearly defined (\(\zeta_1,\zeta_2\in\{1,\dots,k\}\)), and the numerator versus denominator structure is standard normalization. The reviewer's confusion appears to stem from a misreading.
- **Criticism that Theorem 4.1 does not guarantee correct \(k\) blocks under noise**: The theorem states a formal property of the regularizer (zero iff \(k\)-block diagonal). That it does not also provide guarantees under noise is not a flaw — it is a standard scope limitation of such formal statements.

## Novel Insights

None beyond the paper's own contributions. The reviews surface an important structural trade-off: the paper's most novel claim (principled discovery of latent concepts and their drift) is also its least validated aspect, while its strongest empirical evidence supports a secondary objective (forecasting). This tension is the central issue any revision must resolve.

## Suggestions

1. **Fix the expansion in Eq. 2**: Correct the missing \(\alpha^2/4\) factor, or if \(\alpha\) is intentionally constrained (e.g., \(\alpha=2\)), state this explicitly and explain the design rationale. Provide a derivation showing how the stated form arises.
2. **Add direct concept-evaluation metrics for the synthetic dataset**: Report NMI, ARI, or similar metrics between discovered and ground-truth concepts, and accuracy of detected drift transition points.
3. **Add error bars or confidence intervals** to the forecasting results in Table 1.
4. **Clarify the baseline list**: Either list all 17 models explicitly or correct the text to match the actual number of baselines.
5. **Perform an ablation study** (can be in appendix) isolating the contribution of the kernelization, block-diagonal regularization, and drift-adaptation components.

## Score and Decision

The paper addresses an important problem with a novel formulation that has genuine theoretical grounding (Theorem 4.1) and demonstrates strong forecasting performance. However, the mathematical inconsistency in the core objective (Eq. 2) and the lack of direct validation for concept identification and drift tracking — which the paper lists as primary contributions — are significant weaknesses. The paper would need a major revision addressing these issues before it could be accepted.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>