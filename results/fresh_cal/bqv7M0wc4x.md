Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper introduces ICL-TSVD, a continual learning method that bridges the empirically strong RanPAC approach with the theoretically principled Ideal Continual Learner (ICL) framework. The key idea is to lift pre-trained ViT features via random ReLU layers, then continually truncate the singular value decomposition of the lifted feature matrix before solving a minimum-norm least-squares problem. The method addresses the ill-conditioning of random ReLU features that causes instability in both RanPAC and the naive min-norm ICL formulation. The paper proves finite-sample bounds on training and generalization errors and demonstrates strong empirical results across 8 datasets and multiple incremental settings.

## Strengths

- **Provable bounds on estimation and generalization**: Theorems 1 and 2 provide explicit upper bounds on training MSE and test error that depend on the truncation ratio γ_t and the accumulative truncated eigenvalue mass a_t. These bounds are derived under minimal assumptions and apply to the continual (not just offline) setting, which is a genuine theoretical contribution over prior PCR analyses that consider only one-shot truncation.

- **Consistent and substantial empirical outperformance**: In Table 1, ICL-TSVD (without first-session adaptation) achieves higher final accuracy than RanPAC on all 12 dataset×increment combinations, with gaps exceeding 16 points on StanfordCars (74.21 vs 58.03, B-16 Inc-5). Table 2 extends this to the extreme Inc-1 setting where ICL-TSVD maintains strong performance (avg. 77.65% vs RanPAC's 66.00%) and RanPAC catastrophically fails on StanfordCars (1.19%).

- **Strong hyperparameter stability**: Figure 5(a) shows ICL-TSVD's accuracy is nearly constant for truncation percentages from 1% to 99%, in sharp contrast to the min-norm ICL baseline that collapses when small eigenvalues appear. Figure 5(b) demonstrates that combining TSVD with ridge regression makes the method practically immune to the choice of λ, addressing a core weakness of RanPAC.

- **Efficient continual implementation with scalability advantage**: Algorithm 1 maintains truncated SVD factors via a fixed-size matrix B̃_t without storing past data. The complexity analysis (O(E(k_{t-1}+m_t)²) vs RanPAC's O(E³)) is verified empirically in Figure 6, where ICL-TSVD is up to 1000× faster at matched embedding dimensions.

- **Detailed spectral diagnosis of instability**: Section 3 provides clear empirical evidence linking the emergence of tiny eigenvalues (order 10⁻⁵) to accuracy collapse in the min-norm ICL solution, and identifies the distinct failure modes of ICL (numerical errors) vs RanPAC (double descent/generalization errors).

## Weaknesses

### Major

- **Asymmetric embedding dimensions in the primary comparison (Table 1)**: ICL-TSVD uses E=100,000 while RanPAC uses its default E=10,000. The paper is transparent about this and argues it is fair because ICL-TSVD is more efficient, so it can afford a larger E. However, this confounds two factors: the TSVD mechanism and the larger embedding dimension. RanPAC's accuracy also improves with E (as noted in its original paper), so part of the observed gap could be attributable to E rather than to TSVD. The paper does not provide controlled comparisons at matched E values (e.g., E=10,000 or E=20,000 for both methods) to isolate the TSVD benefit. This weakens the headline claim of "uniformly outperforms" — the claim is factually correct for the settings tested, but its attribution to TSVD specifically is not fully disentangled from the E difference.

- **No variance or uncertainty quantification**: All accuracy numbers in Tables 1 and 2 are single-point estimates with no standard deviations, confidence intervals, or indication of multiple random seeds. While the large gaps (e.g., StanfordCars Inc-1: 1.19 vs 74.44) are clearly robust, many differences in the 1–3 point range cannot be assessed for statistical significance. The paper criticizes RanPAC's cross-validation failures using specific examples but does not provide evidence of ICL-TSVD's own stability across random seeds, data splits, or draws of the random matrix P.

### Minor

- **Theory-assumption gap**: The theoretical guarantees (Theorems 1–2) are derived under a noisy linear regression model (Y = W*H + ε) with a ground-truth weight matrix W*. The actual method is applied to multi-class classification with one-hot labels via MSE loss. The paper acknowledges this gap and argues that the linear model is adequate based on empirical success, but no formal connection is established. The bounds involve unknown quantities (‖W*‖_F, ‖ε‖²) that are not estimated, so the theory provides qualitative insight (the role of γ_t and a_t) rather than a verifiable guarantee for the classification setting.

- **No evaluation of sensitivity to the random projection matrix P**: The method relies on a random Gaussian matrix P ∈ ℝ^{E×d}. Different draws of P could affect the eigenvalue spectrum and thus the truncation behavior. The paper does not evaluate this source of randomness.

- **Limited architectural scope**: The method is evaluated only with ViT-B/16 backbones on vision tasks. The extent to which ICL-TSVD generalizes to other architectures (e.g., ConvNeXt, Swin) or modalities is unexplored.

### Trivial

None beyond formatting artifacts introduced by the PDF extraction process.

## Nice-to-Haves

- A controlled experiment comparing ICL-TSVD and RanPAC at multiple matched embedding dimensions (e.g., E=10,000, 20,000, 50,000) to isolate the contribution of TSVD from the contribution of larger E.
- Error bars (3–5 random seeds) for a representative subset of the main table settings.
- An ablation comparing the continual SVD approximation (via B̃_t) against the exact offline ICL-TSVD to quantify approximation loss.
- A brief practical guide for setting the truncation percentage ζ (e.g., based on eigenvalue threshold δ).

## Removed Points

The following points were identified in the input reviews but are removed from the main evaluation for the reasons stated:

- *"Figure 1c uses exact SVD which is a known unstable procedure for ill-conditioned matrices"* — This is precisely the paper's point: it demonstrates that the instability exists, motivating TSVD. Not a weakness.
- *"The theoretical bounds are self-referential because γ_t and a_t are defined in terms of B̃_t"* — Data-dependent bounds are standard in learning theory. This is not a flaw.
- *"The paper only asserts numerical errors are the main cause without rigorous demonstration"* — The paper provides training-loss explosion evidence (Figure 2) that coincides with eigenvalue emergence, which is reasonable empirical support for the claim.
- *"Missing related works"* — Cannot be verified without external sources.
- *"Missing appendix content or proofs"* — The parser strips these; they exist in the original submission.
- *"RanPAC instability claim is overstated"* — The paper documents specific failure cases with evidence (accuracy matrices with near-zero columns, Inc-1 collapse); this is not overstatement.
- *"Formatting/style nitpicks"* — Parser artifacts, not author errors.

## Novel Insights

The two reviews largely converge on the main strengths and weaknesses. The most useful insight from synthesis is that the paper's central empirical claim rests on a comparison where an uncontrolled variable (embedding dimension E) varies alongside the method. This does not invalidate the contribution — the paper is transparent about the different E values and provides a pragmatic justification — but it means the most crisply interpretable evidence for TSVD's benefit comes from the stability analysis (Figure 5) and the Inc-1 results (Table 2), where the stability advantage is dramatic and cannot be explained by E alone. The theory is a genuine contribution to the continual PCR literature but is best understood as qualitative insight rather than a formal classification guarantee. Overall, the paper makes a solid contribution with a clearly identified problem, a simple and effective fix, and both theoretical and empirical support.

## Suggestions

1. **Run a controlled E experiment**: Compare ICL-TSVD and RanPAC at E=10,000 and E=20,000 (where RanPAC is still computationally feasible) on 2–3 key datasets. This would directly isolate TSVD's contribution and substantially strengthen the paper.
2. **Add error bars**: Report means and standard deviations over at least 3 random seeds for a representative subset of settings (e.g., 3 datasets × 2 increments). This is standard practice and would address a significant methodological concern.
3. **Add a random P sensitivity analysis**: Show that test accuracy is stable across 3–5 draws of the random matrix P.
4. **Acknowledge the theory gap more explicitly**: State that the theory provides sufficient conditions for small error under a linear model, and note that the connection to classification is empirical rather than formal.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>