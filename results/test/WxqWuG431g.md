Now I have a thorough understanding of the paper and can cross-check each claim.

## Summary

This paper investigates the geometric structure of sparse autoencoder (SAE) feature vectors (decoder weights) from Gemma-2 models at three spatial scales: an "atomic" scale searching for parallelogram/trapezoid ("crystal") structure in feature differences, a "brain" scale testing whether functionally similar features (those co-occurring in documents) form spatially localized lobes, and a "galaxy" scale analyzing the eigenvalue spectrum and clustering entropy of the full point cloud.

## Strengths

**1. Brain-scale analysis is thorough and the results are statistically striking.** The paper uses five different co-occurrence affinity measures, spectral clustering from functional similarity (not spatial information), and quantifies spatial modularity using both adjusted mutual information and logistic regression prediction from position to lobe label. The significance tests (954 and 74 standard deviations against null) are convincing and well-designed, with proper random permutation and random feature direction baselines. The lobe specialization analysis (Figure 5 showing code/math vs. text lobes) adds interpretable validation.

**2. Comprehensive comparison of co-occurrence affinity measures.** The systematic comparison of Jaccard, Dice, overlap, Phi, and simple matching coefficients (Section 4, Figures 4 and 5) provides practical guidance for the community on which metric best captures functional similarity for lobe discovery. The finding that Phi coefficient works best is non-obvious and empirically grounded.

**3. Clustering entropy analysis reveals layer-dependent structure.** The k-NN entropy estimation (Section 5.2, Figure 8) showing middle layers have lowest clustering entropy provides a complementary metric to the eigenvalue analysis and reinforces the finding that SAE feature structure varies meaningfully across layers.

**4. The LDA-based method for removing distractor features is a useful procedural contribution.** The identification of the "distractor feature" problem (e.g., word length dominating difference vectors) and the use of LDA to project these out is demonstrated to dramatically improve parallelogram/trapezoid quality in activation space (Section 3, Figure 1). This methodological insight has value independent of whether the SAE crystal application is fully validated.

## Weaknesses

### Major

**1. The atomic-scale claim about crystals in the SAE feature point cloud is not substantiated by the evidence presented.** The paper's abstract and introduction state that the "atomic" small-scale structure contains "crystals" (parallelograms/trapezoids) in the concept universe of SAE features. However:

- The paper initially searched for crystals in SAE features and "found mostly noise" (line 71).
- It then pivots to analyzing *activation differences* from the Todd et al. dataset of word-level prompts (lines 72-78), not the SAE decoder vectors themselves. Figure 1 shows LDA improving parallelogram quality in this *activation* space.
- The connection back to SAE decoder vectors is never made. The one table that would show candidate SAE feature trapezoids (Table 1, labeled "Examples of Trapezoids found in Layer 0 of Gemma-2-2b SAE after LDA") is entirely commented out, with an author note requesting a single-word example be added.
- The abstract and conclusion assert the crystal claim as established, but the evidence as presented supports only the weaker claim that "distractor features can hide existing crystals in activation space, and LDA can recover them there."

The LDA method applied to activations is a valid contribution, but the paper's central framing — that SAE feature vectors themselves form crystals — lacks direct evidence. This is not a minor gap; it is one of the three core claims being only partially supported. (The paper could be reframed to present the atomic section as exploratory/methodological rather than as an established finding.)

**2. The galaxy-scale null hypothesis does not properly account for the unit-norm constraint on SAE features.** The paper explicitly states that features are "unit-norm decoder feature vectors" (line 19 footnote) — i.e., they live on a high-dimensional sphere. The galaxy-scale analysis (Section 5) tests against the null that the point cloud is drawn from an "isotropic multivariate Gaussian distribution" (line 241) and compares observed eigenvalues to Wishart-distribution predictions. However, an isotropic Gaussian distribution does not lie on the sphere; its support is all of ℝ^D. The spherical constraint itself induces correlations among coordinates and changes the expected eigenvalue spectrum. A null model should respect the spherical geometry (e.g., uniform random points on the sphere, or shuffling coordinates across features while preserving marginal norms). The power-law observation and its layer-dependence are interesting and may survive with the correct null, but as presented, it is unclear how much of the deviation from the Gaussian null is due to genuine structure versus the constraint that the points are normalized. This needs to be addressed before the galaxy-scale claims can be properly evaluated.

### Minor

**1. The three scales are treated independently with no inter-scale synthesis.** The paper does not discuss whether features that form crystals tend to belong to specific lobes, whether the steepest power-law slope in middle layers coincides with higher "crystallinity," or whether the clustering entropy relates to the eigenvalue power-law slope. Since these are three analyses of the same point cloud, the absence of any cross-discussion (a half-page synthesis) weakens the paper's intellectual contribution.

**2. The paper uses only Gemma-2 2B and 9B models, and the main results rely on 2B.** While this is a defensible starting point, some statement about expected generality to other architectures or SAE training methods would strengthen the paper. (Not a dealbreaker, but worth noting.)

**3. Lack of a non-parametric or shuffled baseline for the crystal search.** The LDA improvement on activations is visually clear (Figure 1), but there is no quantitative comparison against random quadruplets or a null distribution to establish that the post-LDA parallelograms are better than chance. Adding such a baseline would significantly strengthen the atomic section even in its current form.

### Trivial

None.

## Nice-to-Haves

- Report the fraction of candidate concept quadruplets from SAE decoder vectors (not just activations) that satisfy parallelogram/trapezoid conditions before and after LDA, with a baseline from random quadruplets.
- For the galaxy scale, replace the isotropic Gaussian null with a null that respects the unit-norm spherical constraint (e.g., random unit vectors uniformly distributed on the sphere).
- Test robustness of the brain-scale lobe partitions to different block sizes (128 vs. 512 tokens) and context lengths.
- Include the currently commented-out table of SAE feature crystal examples once completed.

## Removed Points

- **"Power-law eigenvalue decay inconsistent with isotropic Gaussian" (Strength Finder strength #3):** Removed because it conflicts with a verified weakness (Weakness #2 above — the null does not account for the spherical constraint). The observed power-law is real, but the comparison to Wishart/isotropic Gaussian is not a valid test of whether the structure is surprising given the data type.
- **"Incompleteness of the manuscript" (Harsh Critic's Critical Issue #3):** This is noted under Major Weakness #1 (the atomic claim is unsubstantiated) rather than as a standalone "manuscript is incomplete" critique. Commented-out content in a submission is not itself a scientific flaw — the issue is what evidence is absent, not that placeholders exist.
- **Critic's claim that the paper "cannot be judged complete":** Overstated. The brain and galaxy sections are fully presented and evaluable. The incompleteness is specific to one of three claims, which is covered under Major Weakness #1.

## Novel Insights

The most interesting observation from the review process is the asymmetry in rigor between the three scales. The brain-scale analysis is the gold standard for this kind of work: multiple complementary metrics, meaningful null distributions that respect the data structure, and significance quantification. The galaxy-scale has the right idea (quantify shape and clustering) but applies a null that doesn't match the data constraints — yet the underlying observation (power-law eigenvalue decay, layer-dependent slope) is novel enough that fixing the null is likely to preserve the finding, not destroy it. The atomic scale is where the mismatch between claim and evidence is largest: the paper diagnoses a real problem (distractor features) and proposes a plausible fix (LDA), but applies it only to activations rather than to the SAE decoder vectors that the crystal claim is about. This suggests the atomic section could be its own follow-up paper rather than a third equal pillar in this one. The paper would be stronger if it either (a) completed the atomic analysis or (b) honestly reframed it as a methodological preliminary with the crystal claim deferred.

## Suggestions

1. **Complete the atomic-scale analysis on SAE decoder vectors directly.** Take the existing pipeline (compute difference vectors from SAE features, apply LDA to remove distractor directions, cluster parallel vectors) and report concrete results with the SAE feature dictionary, not just activation differences from the Todd dataset. Include the SAE crystal table and a null baseline from random quadruplets.

2. **Fix the galaxy-scale null** by comparing observed eigenvalue spectra to those of uniform random points on the sphere (or a shuffled-coordinate baseline) rather than to an isotropic Gaussian. Re-report the power-law slopes and confirm they survive the corrected null.

3. **Add a synthesis paragraph** in the conclusion (or a new subsection) discussing potential relationships between the three scales: e.g., do more "crystalline" features belong to specific lobes? Do layers with steeper eigenvalue power laws also have lower clustering entropy? This would significantly raise the paper's intellectual contribution.

4. **Reframe the atomic section** to honestly present it as exploratory/methodological (identifying the distractor problem and proposing LDA as a solution) rather than as an established SAE feature crystal finding, unless the SAE feature evidence is added.

## Score and Decision

The paper identifies an interesting and underexplored question — whether SAE feature spaces have geometric structure beyond random placement — and presents strong evidence at the brain scale. The galaxy-scale observation is plausible but needs a corrected null. The atomic-scale claim as currently stated is not supported by the presented evidence. The paper would benefit from completing one analysis (atomic scale on SAE features) and fixing one analysis (galaxy scale null). In its present form, the gap between the paper's claims and its evidence is too large for acceptance, but the core ideas are promising.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>