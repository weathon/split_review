Here is my consolidated review.

---

## Summary

This paper introduces DDOT, a diffeomorphic mesh deformation framework that replaces the conventional Chamfer distance loss with the sliced Wasserstein distance (SWD) computed on meshes represented as probability measures — including an oriented varifold encoding that captures both position and normal orientation. The authors provide a non-asymptotic convergence bound (Theorem 1) showing that SWD achieves a parametric rate of O(m^{-1/2} + L^{-1/2}) independent of the ambient dimension, unlike standard Wasserstein distance. Experiments on three brain MRI datasets (ADNI, OASIS, TRT) for cortical surface reconstruction show improved geometric accuracy (ASSD: 0.202 mm vs. CortexODE's 0.234 mm on ADNI left WM) and an exceptionally low self-intersection ratio (<10⁻⁴%).

## Strengths

- **Novel mesh-as-probability-measure representation with oriented varifolds**: The paper proposes three ways to encode meshes as probability measures (continuous, empirical, and discrete via oriented varifold — Section 3.1). The varifold representation incorporates both 3D position and unit normal orientation into a discrete measure, providing a richer approximation of the mesh surface than random point sampling. This genuinely generalizes the common set-based approach.

- **Theoretical convergence analysis for SWD on mesh measures**: Theorem 1 provides a non-asymptotic bound on the error between the SWD of empirical measures and the SWD of continuous mesh measures, showing a rate of O(m^{-1/2} + L^{-1/2}). While the error decomposition (sample error + Monte Carlo error) is standard in the optimal transport literature, the paper's contribution is adapting this analysis to the mesh setting and using it to justify SWD's sample efficiency relative to Wasserstein distance, which suffers from O(m^{-1/d}) curse of dimensionality.

- **Substantially lower self-intersection ratio while maintaining or improving geometric accuracy**: On both ADNI and OASIS datasets, DDOT achieves a self-intersection ratio of <10⁻⁴% (Table 1), which is roughly 100× better than CortexODE (0.013%) and 580× better than CFPP (0.058%), while simultaneously achieving the best ASSD (0.202 mm vs. 0.234 mm for CortexODE on ADNI left WM). This empirical result — even if the causal link to the loss function needs further isolation — is a notable improvement over prior diffeomorphic methods that still produce non-trivial self-intersections.

- **Consistency on test-retest (TRT) data**: On the TRT dataset, DDOT achieves the best EMD (0.780 mm) and ASSD (0.229 mm) among all compared methods including FreeSurfer and learning-based baselines, demonstrating more reproducible morphological measurements across repeated scans of the same subject.

## Weaknesses

### Major

1. **Suspiciously low variance on ADNI Left WM EMD for the proposed method.** In Table 1 (ADNI, left WM), the EMD for DDOT is reported as `0.728 ± 0.013` — a standard deviation of ~1.8% of the mean. Every other method on the same metric has a standard deviation at least 5× larger relative to its mean (CortexODE: `0.803 ± 0.136`, ~17%; CFPP: `0.912 ± 0.435`, ~48%). On OASIS, the same method shows normal variance (`0.418 ± 0.192`, ~46%), and even on ADNI Right WM the variance is reasonable (`0.702 ± 0.068`, ~10%). This anomalous near-zero variance on a single metric/dataset/hemisphere combination requires explanation: is the test set small? Is EMD computed differently for the proposed method? Is the variance across subjects or across random seeds? Without clarification, the quantitative claims on ADNI EMD cannot be fully trusted.

2. **Self-intersection improvement is not causally linked to the proposed loss via ablation.** The paper reports a SI ratio of <10⁻⁴% — a dramatic improvement over CortexODE (0.013%) — and attributes this to the SWD loss and probability measure representation. However, the ablation study (Table 3) only evaluates EMD and SWD metrics across four conditions (SWD on point samples, CD on varifold, Sinkhorn on varifold, SWD on varifold). No SI numbers are reported for any ablated condition. Without measuring SI for each ablation variant, the reader cannot determine whether the SI improvement comes from the SWD loss, the varifold encoding, the diffeomorphic flow, the specific training configuration, or some combination thereof. This is the single most important missing experiment, as the SI result is the paper's headline strength.

3. **Running time comparison may use an unfair CD implementation.** The paper claims CD has O(m²) complexity and its running time plot (Figure 2) appears consistent with quadratic scaling. However, state-of-the-art mesh deformation frameworks compute CD using approximate nearest-neighbor methods (KD-tree or GPU-based approaches) that achieve near O(m log m) or O(m) complexity. The paper does not describe the CD implementation used in the timing experiment (naive double loop vs. KD-tree vs. GPU). If a naive implementation was used, the comparison is misleading and the claimed computational advantage of SWD over CD loses practical significance. This weakens the motivation for SWD's practical efficiency edge.

### Minor

4. **The claim that "a similar property is not able to be derived for Chamfer" (line 134) is too strong.** The paper states that a sample complexity bound like Theorem 1 cannot be derived for Chamfer distance because it "cannot be generalized to compare meshes." This overstates the case: Chamfer distance on sampled point sets could, in principle, be analyzed via concentration inequalities on nearest-neighbor distances, and the paper does not attempt such an analysis. The claim should be qualified.

5. **The value of the number of projections L in SWD is not reported or ablated.** The paper defines L (line 117) as the number of random projections used in the Monte Carlo approximation of SWD, and Theorem 1 explicitly depends on L. Yet the paper never states what value of L is used in experiments, nor studies its effect on geometric accuracy or training time. Since the Monte Carlo approximation is central to the method's efficiency and accuracy, this is a notable omission.

6. **Sinkhorn baseline in ablation lacks key implementation details.** The ablation study compares against "Sinkhorn on O.V." but does not report the entropic regularization parameter used in the Sinkhorn algorithm. The choice of regularization parameter can substantially affect both approximation quality and computational behavior, making this baseline hard to interpret or reproduce.

7. **Theorem 1's second term involves an unbounded variance term.** The bound in Theorem 1 is `O(m^{-1/2} + L^{-1/2})`, but the L⁻¹/² term involves `E[Var[W_p(...)]^{1/2} | X, Y]`, which is conditioned on the sampled points and left unbounded. While this is a standard form in the SWD literature, calling the rate a clean "fast statistical rate" without caveats about the variance term is imprecise.

8. **The identified limitation about "deterministic supports correlated with mesh resolution" (Section 6) is vague.** The limitation section mentions that the method works best on "deterministic supports correlated with mesh resolution" and that this "introduces stochastic memory during training." This is hard to interpret concretely and does not address the more practical concern — the anomalous ADNI variance — which should have been discussed as a limitation.

### Trivial

None beyond the parser-artifact issues discussed below.

## Nice-to-Haves

- **Ablation on self-intersection ratio**: Adding SI numbers to the ablation study (for each combination of loss function and representation) would directly support the paper's central claim about SI improvement.
- **Statistical significance tests**: Given overlapping standard deviations in some comparisons (e.g., ADNI left WM SWD: Ours 0.420±0.273 vs. CortexODE 0.436±0.403), paired tests (e.g., Wilcoxon signed-rank) would strengthen the claim that improvements are not due to chance.
- **Sensitivity study on the number of projections L**: Reporting how geometric accuracy and training time vary with L would make the method easier to adopt.
- **Qualitative comparison of self-intersections**: A figure showing self-intersecting faces for CortexODE/CFPP vs. DDOT would directly support the SI claims.
- **Comparison with CortexODE using SWD loss**: Ablating the loss function in a fixed architecture (e.g., replacing CD with SWD in CortexODE) would isolate the effect of the loss from the network architecture.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Duplicate tables appearing twice in the extracted text**: The reviewer noted that Tables 1 and the ablation table appear identically twice. This is a PDF parsing artifact — the appendix content is duplicated by the extraction tool, not an author error. The original submission does not have this issue.
- **"The ODE formulation and feature encoding are adapted from CortexODE — the novelty lies in the loss function"**: This is a correct description of the contribution, not a weakness. The paper is transparent about building on CortexODE.
- **Demand to evaluate on other deformation tasks (shape registration, non-rigid tracking)**: This is scope creep. The paper explicitly scopes its experiments to cortical surface reconstruction (abstract, lines 31-32) and notes potential broader applicability as future work (Section 6).
- **Formatting/style nitpicks about the wrapfigure readability**: Parser/formatting artifact.
- **Missing related works citation (Nadjahi et al., 2020)**: The instruction prohibits raising missing related works concerns without external sources to confirm relevance.
- **The bound in Theorem 1 being "not a new result"**: The paper presents this as supporting analysis, not as a novel mathematical contribution. Its value is in adapting SWD analysis to the mesh setting, not in advancing optimal transport theory per se.

## Novel Insights

None beyond the paper's own contributions. The reviews surface useful methodological concerns but do not reveal any fundamentally new perspectives on the paper's approach or results.

## Suggestions

1. **Explain the near-zero variance on ADNI Left WM EMD.** Clarify the test set size, whether the variance is across subjects or seeds, and whether the EMD metric is computed identically for all methods. If the number is correct, provide a plausible explanation (e.g., the test set is small, or the EMD computation uses a different algorithm than the one used for baselines). If an error is found, correct it.

2. **Add SI metrics to the ablation study.** Report self-intersection ratios for each ablation condition (SWD on P.S., CD on O.V., Sinkhorn on O.V., SWD on O.V.) so the reader can attribute the SI improvement. This is the single most impactful addition.

3. **Clarify the CD implementation used in the running-time experiment.** State whether KD-tree, GPU-accelerated, or naive nearest-neighbor search was used. If a naive O(m²) implementation was used, re-run the comparison with an optimized CD and report both.

4. **Report the value of L (# projections) and study its effect.** State the L value used in all experiments and show how geometric accuracy and runtime vary with L.

5. **Report the Sinkhorn regularization parameter** used in the ablation baseline.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Weak Accept</orange>