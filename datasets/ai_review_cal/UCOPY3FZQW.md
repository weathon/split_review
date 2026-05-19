- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes VMCF (Visible Multilayer Concept Factorization), a multilayer extension of Concept Factorization for image clustering. The key ideas are: (1) an adaptive graph regularizer (ACF) that learns a self-representation matrix Q to preserve sample-level locality without manual graph construction, (2) a 2D feature extraction step using bidirectional 2DPCA on the learned basis images to preserve pixel-level spatial structure, and (3) a multilayer architecture that gradually reduces dimensionality layer by layer. Experiments on four image databases (AR, MIT CBCL, CMU PIE, ETH80) show VMCF outperforming seven baselines (both shallow and deep CF variants) in clustering accuracy and F-score.

## Strengths

- **Consistent empirical advantage across diverse datasets and settings.** VMCF achieves higher clustering accuracy and F-score than all seven baselines on each of the four databases (Tables 2–5, Figures 3–6), across cluster counts K=2 to 10. This is not cherry-picked on a single dataset — the pattern holds across face and object databases with different sizes and characteristics. The margin of improvement is visible from the reported curves and averaged tables.

- **Well-motivated architectural design addressing genuine limitations of prior CF.** The paper identifies three concrete problems with existing CF methods: (i) graph-regularized CF requires manual neighborhood parameter selection, (ii) vectorizing images discards pixel-level spatial structure, and (iii) one-shot dimensionality reduction loses information. VMCF's three components (adaptive graph via learned Q, 2DPCA on basis images, multilayer gradual reduction) directly target these problems, giving the framework clear motivation.

- **Principled optimization framework.** The paper derives multiplicative update rules for W, V, and Q using a Lagrangian-KKT approach (Section 4), which is the standard technique for nonnegative matrix factorization-style problems. The derivation provides a clear roadmap for optimization, even if the specific equations contain transcription errors (see Weaknesses).

## Weaknesses

### Fatal
None.

### Major

- **Optimization update rules contain verifiable derivation errors and dimensional inconsistencies.** This is the paper's most serious problem. The gradient for W (Eq. 12) writes `2X^T X W V^T` where the correct derivation gives `2X^T X W V V^T` — a missing V factor. More critically, the KKT condition for V (Eq. 14) gives `(X^T X W V V^T)_{ik} v_{ik} - (X^T X V^T)_{ik} v_{ik} + α(VL)_{ik} v_{ik} = 0`, which **does not follow from the (correct) V gradient** in Eq. (12). The gradient gives `(W^T X^T X W V)_{ik} v_{ik} - (W^T X^T X)_{ik} v_{ik} + α(VL)_{ik} v_{ik} = 0`. The paper substitutes `X^T X V^T` (N×r) for `W^T X^T X` (r×N) and `X^T X W V V^T` (N×r) for `W^T X^T X W V` (r×N). Since V is r×N, `X^T X V^T` is N×r — the indices (i,k) reference a transposed shape. This is not a cosmetic typo: the update rule for V (Eq. 15) as written cannot be implemented correctly based on the stated dimensions, and the W update (Eq. 11) similarly uses a dimensionally inconsistent term `X^T X W V^T`. The implementation likely uses correct formulas (given the positive results), but the paper as presented is not reproducible from its own equations. The authors must provide corrected update rules and confirm dimensional consistency.

- **No ablation study to isolate the three claimed innovations.** The paper attributes VMCF's performance to three components: adaptive graph regularization, 2D feature extraction on basis images, and multilayer gradual reduction. None is ablated. Without a variant that replaces the adaptive graph with a fixed graph, a variant that omits 2DPCA (flattening basis images directly), and a single-layer variant, the source of any performance gain is unknown. The multilayer structure alone (already present in MCF, GMCF, DSCF-net) could account for all improvements.

- **Key hyperparameter α is unspecified for experiments.** The trade-off parameter α between the reconstruction term and the adaptive graph regularizer is introduced in Eq. (7) as `α ≥ 0`, appears in the update rules, but is never assigned a value or described how it was selected. The experimental setup (Section 5.1) specifies target dimensions and the number of layers but omits α. Without this information or a sensitivity analysis, the reader cannot assess whether results depend on fine-tuning or are robust.

- **No measures of statistical significance.** Results are reported as single averaged values (Tables 2–5) with no standard deviations, confidence intervals, or significance tests, despite averaging over "20 random initializations" (line 142). Given the random subset selection of categories and the stochastic nature of K-means clustering on learned representations, variability should be reported.

### Minor

- **The locality-preservation rationale for both the adaptive graph and 2DPCA is asserted, not justified.** The term `||V - VQ||_F^2` with only nonnegativity and zero-diagonal constraints is a self-representation criterion; it is not argued or shown to preserve local manifold structure. The paper does not explain why this specific formulation captures locality better than existing graph-regularized or LCC-based methods. Similarly, the claim that 2DPCA "preserves pixel-level locality" (Section 3.3) is stated without explanation or evidence — PCA-based projections are global variance-maximizing, and their locality-preservation property is not obvious. If there is a theoretical or empirical basis for these claims, it should be provided.

- **The category selection protocol is underspecified.** The paper states (line 142): "For each number K of clusters, we randomly choose K categories from each database." It is unclear whether this random selection is performed once per K or repeated (e.g., with the 20 K-means initializations). If once, results depend heavily on a single draw — especially problematic given the absence of variance reporting.

- **The word "Visible" in the title is never defined.** It appears in the title and abstract but receives no explanation or motivation. If it refers to the basis images being visualizable, this should be stated explicitly.

- **The adaptive weight matrix Q has no row-sum or normalization constraint.** While this does not necessarily cause unbounded growth (the objective penalizes reconstruction error), it departs from standard graph/affinity matrix conventions and makes the "adaptive graph" interpretation less grounded. A brief justification would help.

### Trivial
None.

## Nice-to-Haves
- Parameter sensitivity analysis for α and for target per-layer dimensions.
- Specification of per-layer architecture (concept counts, target dimensions) for baseline multilayer methods MCF, GMCF, and DSCF-net, to ensure the comparison is calibrated.
- A controlled experiment measuring neighborhood preservation in the learned representation to substantiate the locality-preservation claims.
- Reporting standard deviations alongside averaged clustering metrics.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"Fatal structural flaw" framing from the harsh critic**: The claim that the optimization error "invalidates the method" and that the paper "should not be accepted in its current form" overstates severity. The error is in the writeup of the update equations, not necessarily in the implementation. The general framework and optimization approach (Lagrangian + KKT + multiplicative updates) remain sound. The weakness is retained as Major (not Fatal) because a corrected derivation is straightforward and the paper's core claims do not depend on the specific notational form of the updates.
- **"Uncontrolled comparison with deep baselines" about unspecified per-layer dimensions**: The paper does state (line 163) that the three-layer setting follows previous works (Zhang et al., 2021; Zhang et al., 2020), which provides a reference. This weakens the criticism. Demoted from major to removed.
- **"Q could allow unbounded growth"**: Since Q is learned by minimizing `||V - VQ||_F^2`, it is implicitly bounded by the data. The multiplicative update rule preserves whatever scale emerges from the optimization. This concern is not a concrete flaw without evidence of instability. Removed.
- **Strength Finder's generic/superficial strengths**: The claim that "extensive numerical experiments" and "acceptable runtime" are strengths is generic and lacks specificity. Also the claim that the adaptive graph "eliminates manual neighborhood tuning" conflicts with the weakness that the adaptivity mechanism is not validated — demoted to removed as the weakness is more specific.
- **Strength Finder's claim about "derivation of multiplicative update rules"**: While true that derivations are presented, the fact that they contain errors means this claimed strength is invalid. Removed.

## Novel Insights
The reviews surface a tension not discussed in the paper itself: the adaptive graph regularizer `||V - VQ||_F^2` and the 2DPCA step are both justified via "locality preservation" but operate through entirely different mechanisms (self-representation vs. global variance maximization). This raises a question the paper never addresses: are these two mechanisms complementary or potentially working at cross-purposes? An ablation study that isolates each component would not only validate the contributions but also reveal whether their combination is synergistic.

## Suggestions

1. **Correct all update rule equations in Section 4.** Re-derive the KKT conditions for W and V from the gradients, ensure dimensional consistency, and verify that the published equations match the implemented code. The corrected V update should follow from `∂L₁/∂V = 2W^T X^T X W V - 2W^T X^T X + 2α V L` yielding `v_{ik} ← v_{ik} (W^T X^T X)_{ik} / (W^T X^T X W V + α V L)_{ik}` (or equivalent consistent form). The W update gradient should use `V V^T` not `V^T`.

2. **Add an ablation study** with at minimum these three variants: (a) VMCF minus adaptive graph (replace with fixed k-NN graph), (b) VMCF minus 2DPCA (flatten basis images directly), (c) single-layer VMCF. This is essential to substantiate the claimed contributions.

3. **Specify α** and report sensitivity over a range (e.g., {0.001, 0.01, 0.1, 1, 10}) to demonstrate robustness.

4. **Report standard deviations** or confidence intervals for all clustering metrics. If the random category selection is repeated, clarify this and average accordingly.
