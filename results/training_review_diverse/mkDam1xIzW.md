Now I have verified the paper content against all reviewer claims. Let me produce the consolidated review.

---

## Summary

This paper introduces Probabilistic Geometric Principal Component Analysis (PGPCA), a generalization of PPCA that models high-dimensional data distributed around a nonlinear manifold (rather than around a Euclidean mean). The key technical contribution is an EM algorithm whose M-step reduces to PPCA's closed-form updates because all manifold information condenses into a single matrix Γ(q). PGPCA supports two "distribution coordinates" (EuCOV and GeCOV), and the paper shows that comparing their log-likelihoods can distinguish which coordinate system better describes the data. Validation is provided on simulated loop/torus manifolds and on mouse head-direction neural recordings.

## Strengths

1. **Clever theoretical reduction of the nonlinear-manifold problem to PPCA's framework.** The derivation showing that ℒ₁ᴹ (Eq. 13) has the same functional form as PPCA's log-likelihood, with all manifold information summarized in Γ(q), is mathematically elegant. This allows the loading matrix C and noise σ² to be computed with PPCA's closed-form solutions (Eqs. 15–16), preserving PPCA's theoretical guarantees while extending to nonlinear manifolds. This is a genuine generalization, not a minor tweak.

2. **Statistical distinguishability of coordinate systems is convincingly demonstrated in controlled simulations.** On simulated data where the true model is known, PGPCA with the correct K(z) consistently achieves higher log-likelihood than with the incorrect one, backed by paired t-tests (Figure 2B: p < 1.7×10⁻¹²; Figure 2D: p < 3.1×10⁻⁴). The effect holds across model dimensions m ∈ [0,10] and when p(z) is jointly learned (Figure 3). This validates that the EM algorithm can recover the correct distribution coordinate in controlled settings.

3. **PGPCA is the first PPCA extension that models data *around* a manifold with deviation and noise**, unlike prior work (PPGA, torus PPCA) that assumes data lie precisely on the manifold. This fills a genuine methodological gap, particularly for neural data where activity is known to scatter around low-dimensional manifolds.

4. **Real neural data results are consistent and suggestive.** Across mice, PGPCA with GeCOV consistently outperforms PGPCA with EuCOV at all dimensions (Figures 4B, 4D). While the statistical support is weaker than in simulations, the pattern is systematic and aligns with the paper's central claim that geometric coordinates better capture firing-rate distributions around the head-direction ring manifold.

## Weaknesses

### Fatal
None.

### Major

- **Real-data evidence lacks uncertainty quantification and cross-validation, weakening the "hypothesis testing" claim for the real-data setting.** The paper frames PGPCA's ability to choose between EuCOV and GeCOV as "hypothesis testing" (Sections 1, 4, 5). For the real neural data, the evidence consists of point estimates of log-likelihood without confidence intervals, standard errors, or cross-validation (Figures 4B, 4D; Table 2). Since the manifold is fitted from the same data used for PGPCA evaluation, the log-likelihood advantage of GeCOV could partly reflect overfitting rather than genuine superiority. The simulation results (with t-tests) support the method's validity in principle, but the real-data claims are not held to the same statistical standard. Adding cross-validated log-likelihoods with error bars or a bootstrap test would materially strengthen the paper.

### Minor

- **The GeCOV construction is described through examples but not stated as a general mathematical definition.** From Figure 1 and the text, GeCOV at point z on an l-dimensional manifold embedded in ℝⁿ is implicitly defined as an orthonormal matrix whose first l columns span the tangent space and remaining n−l columns span the normal space. This is clear from the examples (loop, torus), but a reader implementing the method for a novel manifold would benefit from an explicit statement: "GeCOV: K(z) = [e₁(z), …, e_l(z), e_{l+1}(z), …, e_n(z)] where {e₁(z),…,e_l(z)} is an orthonormal basis of T_zM and {e_{l+1}(z),…,e_n(z)} is an orthonormal basis of N_zM." This is easy to add and would eliminate ambiguity.

- **The discretization parameters M and landmark selection are unspecified.** The paper introduces M landmarks {z₁:ᴍ} and discretizes p(z) as a Dirac-delta mixture (Eq. 9) but never states how many landmarks were used in the experiments or how they were chosen (uniform sampling? density-weighted?). This makes the experiments difficult to reproduce and leaves open the question of sensitivity to this discretization. A brief simulation varying M would address this.

- **The manifold fitting pipeline for the real neural data is described only by reference to prior work.** While referencing Chaudhuri et al. (2019) for preprocessing is acceptable, the paper does not describe how the 1D loop manifold was fitted from the 10-dimensional firing rates, nor does it evaluate sensitivity to manifold-fitting errors. Given that the manifold is the backbone of the model, this is a gap in the experimental description, though not a fatal one.

### Trivial

- The paper uses the term "hypothesis testing" loosely to mean model comparison via log-likelihood (i.e., selecting the coordinate system with higher likelihood). This is not classical hypothesis testing with null distributions. Clarifying this distinction (e.g., "model selection" or "coordinate comparison") would prevent confusion. This is noted already in the Major section above in terms of statistical rigor; here it is a labeling issue.

## Nice-to-Haves

- A brief simulation varying the number of landmarks M to demonstrate stability of the EM solutions.
- Reporting log-likelihood values with standard deviations across multiple EM restarts (or cross-validation folds) for the real data.
- A short derivation or citation showing how to compute tangent/normal bases from a spline or fitted manifold representation, to make the GeCOV implementation more self-contained.

## Removed Points

These points are flagged to be removed — treat them with caution:

1. **"GeCOV is not defined with sufficient generality to be a structural/fatal flaw."** The critic called this a "structural flaw" making the method irreproducible. This is an overstatement. The paper clearly defines GeCOV through examples (Figure 1 caption: tangent vector + normal vector for a loop; two tangents + one normal for a torus) and states the orthonormality condition K(z)'K(z) = I_n. The general principle (columns of K(z) form bases of tangent and normal spaces) is evident. While an explicit formula would improve clarity, the method as described is implementable for the manifolds considered (loop, torus), and the general idea is clear. Downgraded to Minor.

2. **"No statistical inference for hypothesis testing."** The critic claimed "no confidence intervals, standard errors, or formal test" is provided. This is factually incorrect for the simulations: Figure 2B reports a paired t-test (p < 1.7×10⁻¹²) and Figure 2D reports p < 3.1×10⁻⁴. The paper does provide formal statistical tests for its core simulation results. For the real data, the concern is valid and is kept in Major. The critic's blanket statement is removed.

3. **"No run time, EM iterations, or convergence criteria reported."** Factually incorrect: Figure 2C clearly states the models "converge within 40 EM iterations." The paper does report convergence behavior.

4. **"Steps from (12) to (13) are skipped."** This is a standard level of mathematical exposition for a method paper. The derivation follows standard trace manipulations, and the paper notes the key result. No actual error or gap is identified.

5. **"Isotropic noise assumption is strong and not discussed."** This assumption is inherited from PPCA and is standard for the framework. The paper is not required to re-justify every assumption it inherits from its predecessor.

6. **"Introduction promises derivation never materializes"** (about geometric coordinate). The GeCOV concept is defined and used throughout Sections 3 and 4. The critic misread.

7. Various formatting/style nitpicks from the Section-by-Section notes that do not affect the paper's substance.

## Novel Insights

The most interesting observation that emerges from the reviews — beyond the paper's own contributions — is that PGPCA's central theoretical trick (absorbing all manifold information into Γ(q) so PPCA's closed-form solutions still apply) is more important than the specific choice of GeCOV versus EuCOV. The method's real value may lie in its generality: any orthonormal coordinate system K(z) can be plugged in. The paper mentions this flexibility in the conclusion but does not emphasize it. The reviews collectively highlight that the paper's contribution is somewhat bifurcated — the EM derivation is a clean piece of work, but the experimental validation is strongest where the manifold is known (simulations) and weakest where it matters most (real data with fitted manifolds). This tension is the paper's most important unresolved issue.

## Suggestions

1. **State the GeCOV definition explicitly as a formula** (tangent-space basis + normal-space basis) rather than only through examples. This takes one line and eliminates all ambiguity.
2. **Add cross-validation or bootstrap uncertainty for the real neural data.** Report log-likelihood differences Δ = LL(GeCOV) − LL(EuCOV) with a confidence interval across cross-validation folds or multiple EM restarts. This would directly address the overfitting concern and strengthen the "hypothesis testing" framing.
3. **Report the number of landmarks M used in each experiment and the selection method.** Add a brief sensitivity analysis (e.g., vary M by a factor of 2 or 5) in the supplement.
4. **Retitle "hypothesis testing" as "coordinate system selection" or "model comparison"** to avoid implying formal null-hypothesis testing where none is performed.

## Score and Decision

The paper presents a mathematically sound generalization of PPCA with an elegant EM derivation, and it convincingly validates the method on simulated data with known manifolds. The key weaknesses are: (a) the real-data evidence for GeCOV superiority lacks uncertainty quantification and cross-validation, making the "hypothesis testing" claim prematurely strong for the most practically relevant setting; and (b) several implementation details (landmark selection, GeCOV's formal definition) are underspecified. These are real but addressable gaps — none invalidates the core method or its theoretical contribution. The paper would benefit from one round of revision focused on tightening the real-data evidence and clarifying definitions, but its core contribution is solid and the experiments on simulated data provide genuine validation.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>