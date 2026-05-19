- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have thoroughly verified the paper content against all reviewer claims. Let me produce the final consolidated review.

## Summary

GNeRP proposes a Gaussian-based representation of surface normals within an SDF-based neural 3D reconstruction framework for reflective objects. The key idea is to model normals in a local neighborhood as 3D Gaussians (mean and covariance), splat them to 2D in the image plane, and supervise these 2D Gaussians using polarization priors (AoP and DoP). A DoP-based reweighting strategy adaptively balances radiance and polarization losses. The paper also contributes a new multi-view dataset (PolRef) with polarimetric images and ground truth meshes. Results on four reflective scenes show quantitative improvements over existing methods.

## Strengths

- **Strong empirical results across multiple baselines.** Table 1 shows GNeRP achieves the best Chamfer Distance on all four scenes (mean 1.35 vs. second-best Ref-NeuS at 2.34), outperforming both standard neural reconstruction methods (NeuS, VolSDF), reflective-object methods (NeRO, Ref-NeuS), and a polarization-based method (PANDORA). The margin is substantial and consistent.

- **DoP reweighting strategy is well-motivated and ablated.** The paper identifies that polarization priors are noisy in diffuse-dominant regions (low DoP) and informative in specular-dominant regions (high DoP). The reweighting (Eq. 9) adaptively modulates the color and polarization losses by $(1-\rho)$ and $\rho$ respectively. Ablation in Table 2 shows that reweighting consistently improves over naive supervision (e.g., on Cow: reweighted L_mean 1.94 vs. L_mean 2.72; on Snorlax: 1.81 vs. 2.03).

- **New PolRef dataset fills a clear gap.** Existing polarization datasets (PANDORA) lack ground truth for quantitative evaluation. The PolRef dataset provides 4 scenes with SLA-printed objects (\(\pm 0.1\) mm tolerance), radiance images, and aligned polarimetric information, enabling the reported quantitative comparisons.

- **Covariance decomposition provides interpretable geometry cues.** SVD of the splatted 2D covariance yields eigenvalues (DoA) and eigenvectors that correlate with geometric edges and local shape directionality (Figure 1e), supporting the claim that the representation captures high-frequency detail beyond scalar normals.

## Weaknesses

### Fatal

None. While the paper has significant technical concerns, none individually invalidate the empirical contributions to a degree warranting a fatal classification. The mathematical concerns below are major but addressable.

### Major

- **The volume rendering compositing of 2D Gaussians (Eq. 7, line 121) is mathematically unjustified.** The paper composites Gaussians along a ray via weighted sums of means and covariances independently: \(\hat{\mathcal{G}}(\mathbf{u}) = \mathcal{N}(\sum T_i\alpha_i \mathbf{n}_p(\mathbf{x}_i), \sum T_i\alpha_i \hat{\mathbf{\Sigma}}_p(\mathbf{x}_i))\). This does **not** produce the covariance of a mixture distribution — the covariance of a mixture includes an additional cross-term \(\sum w_i (\mu_i - \bar{\mu})(\mu_i - \bar{\mu})^T\) that is omitted without justification. The paper presents no derivation, citation, or empirical justification for this operation, despite claiming it as a Gaussian compositing. If the operation is intended as simple feature aggregation, the Gaussian formalism and the splatting derivation (Eq. 4–5) become unnecessary. This undermines the paper's core technical claim. **This is the most significant weakness; the authors must either derive the correct compositing, acknowledge the approximation and justify why it works, or reframe the representation as non-probabilistic feature aggregation.**

- **The splatting of normals from 3D to 2D (Eq. 5, line 111) uses the EWA Jacobian \(\mathbf{J}\), but normals do not transform like positions under perspective projection.** The paper states \(\mathbf{J}\) is a "normal projection matrix" citing [ppa], but the EWA splatting framework was designed for position-based attributes (color, opacity). The paper claims to "prove our normal-based 3D Gaussians are exactly splatted to 2D Gaussians" but provides no actual proof or justification for how normals — which transform via the inverse transpose of the position Jacobian in differential geometry — are handled by \(\mathbf{J}\mathbf{W}\). This weakens the theoretical connection between the 3D representation and the 2D polarization supervision.

- **Missing hyperparameter values and sensitivity analysis.** The loss function (Eq. 9) has four weighting parameters \(\alpha, \beta, \gamma, \delta\) (and an additional \(\beta'\) in \(\mathcal{L}_{cov}\)). None of these values are reported. Without them, the experiments are not reproducible. No sensitivity analysis is provided.

### Minor

- **Notation inconsistency in the covariance loss.** Degree of anisotropy (DoA) is defined as \(\Lambda_0/\Lambda_1\) (line 141), but \(\mathcal{L}_{cov}\) uses the inverse ratio \(\hat{\Lambda}_1/\hat{\Lambda}_0\) (line 146) without explanation. The eigenvector alignment term \(\langle\hat{\mathbf{V}}, \widetilde{\mathbf{V}}\rangle\) does not handle sign ambiguity (eigenvectors are defined only up to sign), which can cause training instability.

- **No sensitivity analysis for the supersampling parameter \(M=6\).** The paper uses \(M=6\) (four points around the ray plus adjacent points along it) for covariance estimation but provides no ablation or justification for this choice.

- **No discussion of limitations or failure cases.** The paper does not discuss when the method might fail — e.g., scenes with very low DoP (fully diffuse), strong inter-reflections, or objects with no polarization signal. The dependence on object masks is also not discussed as a practical limitation.

- **Only four quantitative evaluation scenes.** While this is partially justified by the scarcity of suitable datasets with both polarization and ground truth, the claimed "large margin" improvement would be strengthened by more diverse evaluation data.

### Trivial

- The eigenvector subscript in the DoA definition appears as \(\boldsymbol{\Lambda_0}/\boldsymbol{\Lambda_1}\) rather than \(\boldsymbol{\Lambda}_0/\boldsymbol{\Lambda}_1\) (minor formatting issue).

## Nice-to-Haves

- Ablate the Gaussian compositing against simpler alternatives (e.g., directly supervising SDF normals with a polarization-based L1 loss on azimuth angle, without the Gaussian formalism) on all four scenes to isolate the benefit of the covariance term from the compositing mechanism.
- Report confidence intervals or multiple-run statistics for quantitative results.
- Show qualitative results from the PANDORA dataset (if available in the supplementary material).

## Removed Points

- **"No comparison with von Mises–Fisher distributions"**: This is scope creep — the paper is not about BRDF modeling but about neural 3D reconstruction. The critique demands evaluation against a representation not used in any competing method in this domain.
- **"PANDORA results not shown in main text"**: The paper states the PANDORA dataset has no ground truth for quantitative evaluation. Qualitative results are likely in the appendix (stripped by the parser). Cannot verify this as a missing weakness.
- **"No confidence intervals"**: Single-run evaluation is standard in this area. This is not a meaningful weakness.
- **"NeRO without masks may not be optimal"**: The paper explicitly notes this (*) in the table and explains the reason. This is transparent reporting, not a weakness.
- **"Only four scenes" framing as a major issue**: The paper provides justification for the limited scene count and uses available datasets appropriately. This is a common limitation acknowledged as minor above.

## Novel Insights

None beyond the paper's own contributions. The reviews raise substantive mathematical concerns about the Gaussian compositing and splatting but do not offer new theoretical perspectives or alternative solutions that were not already implicit in the criticisms.

## Suggestions

1. **Address the compositing issue directly.** Either (a) derive the correct compositing including the cross-covariance term, (b) reframe the aggregated mean and covariance as learned features rather than a probabilistic Gaussian, or (c) add an empirical justification (e.g., a toy experiment) showing the approximation is empirically sufficient. This is the single most important change.

2. **Clarify the normal projection matrix.** Provide the explicit form of \(\mathbf{J}\) and justify why the EWA splatting Jacobian (designed for positions) applies to normals, or use the correct transformation (inverse-transpose Jacobian for a surface mapping).

3. **Report all hyperparameter values** (\(\alpha, \beta, \gamma, \delta, \beta'\)) and ideally include a sensitivity study for at least one scene.

4. **Fix the notation inconsistency** between the DoA definition (\(\Lambda_0/\Lambda_1\)) and the loss (\(\Lambda_1/\Lambda_0\)), and address the eigenvector sign ambiguity in \(\mathcal{L}_{cov}\) (e.g., by using \(|\langle\hat{\mathbf{V}}, \widetilde{\mathbf{V}}\rangle|\)).

5. **Add a limitations paragraph** discussing scenarios where the method would struggle (low-DoP objects, missing masks, etc.).
