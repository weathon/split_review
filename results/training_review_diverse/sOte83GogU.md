Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper generalizes uniform downsampling with anti-aliasing to signals on arbitrary finite groups. It introduces: (a) an algorithm for selecting a proper subgroup given a group and downsampling rate (Algorithm 1 + Claim 1), (b) a Subgroup Sampling Theorem (Claim 2) that defines bandlimited-ness and perfect reconstruction for subgroup subsampling, and (c) an optimization-based equivariant anti-aliasing filter. Experiments on rotated MNIST and CIFAR-10 with G-CNNs show that incorporating this downsampling reduces parameter count while maintaining or improving accuracy and equivariance.

## Strengths

1. **Novel theoretical generalization of downsampling to arbitrary finite groups**: The Subgroup Sampling Theorem (Claim 2) and the definition of bandlimited signals with respect to a subgroup generalize the classical Nyquist-Shannon sampling theorem beyond abelian/cyclic groups to all finite groups. Example 3 verifies that for cyclic groups the method correctly reduces to standard low-pass + subsampling. Prior sampling theorems for groups (Chen et al. 2015, Dodson 2007) covered only abelian or specific groups, so this is a genuine advance.

2. **Concrete algorithm for subgroup selection with provable guarantees**: Algorithm 1 and Claim 1 provide a principled method to produce a proper subgroup given a group and an integer rate R, with mild conditions ensuring proper subsampling. This addresses the ambiguity in prior subsampling approaches (Cohen & Welling 2016, Xu et al. 2021) which lacked a notion of "subsampling by a factor of R." The ablation in Table 3 shows the proposed heuristic improves accuracy over alternative choices in most settings.

3. **Equivariant anti-aliasing operator that improves both equivariance and accuracy**: The anti-aliasing filter obtained by solving optimization (15) is designed to be G-equivariant and to prefer smooth basis functions. Table 2 shows that incorporating anti-aliasing reduces equivariance error (L_Equi) and improves accuracy on the full orbit (acc_orbit) and locally augmented test set (acc_loc) across multiple sampling rates and datasets, compared to subsampling without anti-aliasing.

4. **Empirical validation of perfect reconstruction**: Table 1 numerically confirms Claim 2 — after anti-aliasing and subsampling, the reconstructed signal matches the bandlimited original signal to numerical precision for both cyclic and dihedral groups, directly connecting theory to practice.

5. **Visualization connects anti-aliasing to classical signal processing**: Figure 3 shows that the anti-aliasing filter for downsampling C₁₆ to C₈ resembles a sinc-like low-pass filter, reinforcing that the proposed operation is a true generalization of classical anti-aliasing.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Theory-practice gap in the anti-aliasing filter is not quantified**: The optimization (15) relaxes the equality constraint of the Reynolds operator (which guarantees exact equivariance) into a penalty term. Consequently, the resulting filter is not guaranteed to satisfy Eq. (10) exactly or to be exactly equivariant. The paper validates end-to-end reconstruction (Table 1) but does not report how close the optimized ℳ is to satisfying the theoretical conditions — e.g., the residual of the equivariance penalty or the reconstruction error for signals bandlimited with respect to this approximate ℳ. This gap is common in practice (the paper itself notes "ideal anti-aliasing operators are often approximated"), but quantifying it would strengthen the connection between theory and implementation.

2. **Xu et al. (2021) baseline is deferred to the appendix**: The comparison most relevant for establishing the advantage over prior group subsampling work appears only in §A2.1 rather than the main Table 2. While the paper's primary contribution is anti-aliasing (which Xu et al. do not address), and its anti-aliasing can be retrofitted to their subsampling scheme, placing this comparison in the main results would more directly substantiate the claim of improvement over existing group subsampling.

3. **Subgroup selection heuristic is ad-hoc and not theoretically grounded**: The heuristic (factorizing R and selecting the generator with largest order that satisfies Claim 1) is described and ablated in Table 3, but the paper does not explain *why* maximizing the number of generators in the subgroup is beneficial. The ablation shows the heuristic does not universally outperform other choices (e.g., D₂₄, R=4 at layer 3). The paper honestly notes this is a heuristic, but the lack of theoretical justification weakens confidence in its generality.

4. **No quantitative report of model size reduction or computational cost**: The paper states that subsampling "significantly reduces the parameter count" but does not report actual parameter counts or FLOPs for the models in Table 2. The Limitations section mentions quadratic time complexity for subgroup selection but does not report wall-clock times or the overhead of applying the anti-aliasing filter during training/inference for the groups used (C₂₄, D₂₄). Adding these numbers would help readers assess practicality.

### Trivial

- The definition of "non-redundant powers" in Claim 1 could benefit from a concrete example showing when the conditions fail and the output is not a proper subgroup. (The paper references §A4 for illustration, which is reasonable given space constraints.)
- The notation in Eq. (15) (elementwise absolute value combined with Diag) is dense; an explicit example would improve readability.

## Nice-to-Haves

- Adding a comparison with the Xu et al. (2021) subsampling baseline to the main results table (Table 2) would strengthen the empirical story for readers who may not consult the appendix.
- Reporting the equivariance error of the anti-aliasing filter itself (not just the whole network) and the residual of the relaxed equivariance constraint would directly address the theory-practice gap.
- A brief discussion of how the choice of generating set affects the Laplacian (and thus the smoothness objective) would clarify a subtle design choice.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"CIFAR-10 digit removal consistency"**: The critic asks whether the same digit removal is applied to CIFAR-10. CIFAR-10 is a natural image dataset without digit-symmetry issues; the digit removal is specifically motivated for MNIST (digits 1/2/4 cause label conflicts under rotation/reflection). This criticism reflects a misunderstanding of the paper. **Removed.**

- **"Full model not described"**: The paper describes the Full baseline (no subsampling) and directs readers to §A7 for implementation details. This is standard practice. **Removed as overly nitpicky.**

- **"No discussion of Laplacian choice"**: The generating set affects the Laplacian, but the generating set is fixed for a given group. This is a non-issue. **Removed.**

- **"No analysis of computational cost"**: The Limitations section explicitly states the quadratic time complexity. The critic missed this. The paper does not report wall-clock times, which is a valid wish but not the gap the critic claimed. **Downgraded to Minor weakness #4.**

- **"Anti-aliasing filter implementation not specified"**: The filter is mathematically defined as 𝒫_ℳ = ℬ(ℬ^†ℬ)⁻¹ℬ^† applied to feature maps — a linear projection operator. The paper states it is applied to feature maps before subsampling. The mathematical specification is clear, though the critic's point about computational overhead is fair. **Weakened to Minor weakness #4 (computational cost).**

- **"Should report reconstruction error for non-bandlimited original signal"**: Table 1 already reports reconstruction with and without anti-aliasing, which covers this. **Removed — already addressed.**

- **Strength Finder outputs about perfect reconstruction and sinc visualization**: These are evidence-based and kept as Strengths 4 and 5. No generic strengths to remove.

## Novel Insights

Beyond the paper's own contributions, the reviews highlight an interesting tension: the paper presents a clean theoretical framework (Subgroup Sampling Theorem with perfect reconstruction guarantees) but then applies it through a relaxed optimization whose approximation quality goes unmeasured. This is a recurring pattern in works that bridge group theory and deep learning — the theory provides a principled foundation, but practical deployment requires approximations whose fidelity is rarely quantified. A useful contribution in follow-up work would be to characterize the gap between the theoretical reconstruction guarantee and the empirical approximation, perhaps by bounding the equivariance error of the optimized filter as a function of the penalty weight λ.

## Suggestions

1. In a camera-ready version, add the Xu et al. subsampling comparison to the main results table (even if only for a representative setting), and include parameter counts and approximate FLOPs for each model.
2. Quantify the approximation quality of the anti-aliasing filter: report the residual of the equivariance constraint after optimization and the reconstruction error for signals bandlimited w.r.t. the optimized ℳ.
3. Provide a concrete worked example of the subgroup selection and anti-aliasing for a small non-cyclic group (e.g., D₆ or D₈) to help readers connect the math to the algorithm.

## Score and Decision

The paper makes a genuinely novel theoretical contribution — extending sampling theory and anti-aliasing to all finite groups — that is principled, clearly explained, and validated through both numerical verification and downstream classification experiments. The weaknesses (missing baseline from main table, unquantified approximation gap, ad-hoc heuristic) are real but minor and do not undermine the core theoretical contribution. The paper is honest about its limitations. It represents solid research that will be of value to the equivariant deep learning community.

**Originality**: High — first to generalize sampling theorem and anti-aliasing to arbitrary finite groups.  
**Importance**: Moderate-to-high — addresses a real gap in G-CNN architecture design.  
**Claims support**: Good — theoretical claims are proven and numerically validated; empirical claims are supported by experiments but would benefit from an additional baseline.  
**Soundness**: Good — theory is sound; experiments are appropriate for a methods paper.  
**Clarity**: Good — writing is clear despite the dense subject matter; some notation could be simplified.  
**Value to community**: Positive — provides both theoretical grounding and practical recipes for downsampling in equivariant networks.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>