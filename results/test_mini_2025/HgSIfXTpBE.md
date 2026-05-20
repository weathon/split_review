Now I have all the anchors I need. Let me compile the final review.

**Bracket determination from Round 1**: The paper sits between the weak anchors (scores 1.5–3.17, papers with fundamental flaws or low relevance) and the strong anchors (scores 7.6–8.0, papers accepted as Oral/Spotlight with comprehensive evaluations). The middle band anchors (scores 5.0–5.75) are most relevant: these are papers on non-Euclidean representation learning with some methodological contributions but also notable weaknesses. **Initial bracket: 4.5–6.5.**

**Round 2 anchors** within this bracket: Sparse hyperbolic representation learning (5.00), Balanced Hyperbolic Embeddings (5.50), Manifold Learning via Foliations (5.00), Neural Tangent Kernels for Axis-Aligned Tree Ensembles (5.50), Spectro-Riemannian GNN (5.75). Comparing against these, the current paper has a cleaner contribution than the Sparse hyperbolic paper (which had limited applications), is on par with Balanced Hyperbolic Embeddings in terms of contribution clarity, and is slightly below Spectro-Riemannian GNN (accepted poster) due to the evaluation confound. **Final score: 5.5.**

Here is the final review.

---

## Summary

The paper extends decision trees and random forests to product manifolds (Cartesian products of Euclidean, hyperspherical, and hyperbolic spaces) using an angular reformulation of splits. Data and decision boundaries are parameterized by angles in 2D subspaces of the ambient embedding space, providing a unified splitting rule that guarantees geodesic convexity. The method is evaluated on 57 benchmarks spanning classification, regression, and link prediction on synthetic data, graph embeddings, mixed-curvature VAE latent spaces, and empirical data.

## Strengths

- **First DT/RF algorithm for product manifolds.** The angular formulation (Section 3.4) enables a single tree to allocate splits across component manifolds independently, respecting the product geometry. This is a non-trivial extension of single-manifold (hyperbolic-only) DTs and fills a clear gap: inference tools for product manifold embeddings are scarce.

- **Unified splitting rule across all constant-curvature manifolds.** Expressing splits as thresholded angles in 2D projections (Eq. 15–16) covers Euclidean, hyperbolic, and hyperspherical spaces within a single framework. The paper introduces the first DTs for hyperspherical space (Section 3.3). The geometric motivation is clear and Figure 2 effectively illustrates the split geometry.

- **Broad empirical evaluation.** The paper benchmarks across 57 tasks (Table 1) — 11 single-curvature classification, 11 single-curvature regression, 24 product manifold classification, 11 product manifold regression — covering synthetic data, graph embeddings, VAE latent spaces, and empirical datasets. On single-curvature benchmarks, product DTs/RFs rank first in 21/22 cases with Bonferroni-corrected significance (Figures 3–4).

- **Interpretable decision boundaries.** Figure 5 shows that on the S² land/water classification task, the product RF produces smooth, geodesically coherent boundaries while Euclidean and tangent RFs exhibit blocky artifacts and k-NN is highly fragmented. This gives concrete qualitative evidence of the benefit of manifold-aware splitting.

## Weaknesses

### Fatal
None.

### Major

- **Oblique split confound on Euclidean components invalidates a clean geometric comparison.** The paper's implementation considers all \(\binom{D}{2}\) 2D projections (Section 4.3, line 522). For a Euclidean component with the trivial lift \(\phi(\mathbf{u}) = (1, \mathbf{u})\), projections onto \((x_i, x_j)\) with \(i,j > 0\) yield splits of the form \(\tan^{-1}(u_i/u_j) \in [\theta, \theta+\pi)\) — which are **oblique** (linear boundaries through the origin in the original Euclidean space). The CART baselines (Ambient, Tangent) use axis-aligned splits only. Therefore, on any benchmark containing a Euclidean component — which includes all product manifolds with \(\mathbb{E}^D\) — the comparison confounds two sources of advantage: (1) manifold-aware geometry, and (2) more expressive (oblique) split selection. The paper never acknowledges this confound or controls for it, e.g., by restricting Euclidean components to \((x_0, x_d)\) projections only, or by including an explicit oblique Euclidean DT baseline. The paper's own future work (line 613) mentions "oblique decision trees" as underexplored, indirectly confirming that obliqueness is not currently isolated. This does **not** invalidate results on purely non-Euclidean manifolds (spherical, hyperbolic), but it substantially weakens the evidence on product manifold benchmarks containing Euclidean components.

- **"Maximum-margin" claim is asserted without evidence.** The abstract and contribution list (lines 15, 39) state that splits are "maximum-margin." The paper justifies geodesic convexity (line 250) but provides no proof, analysis, or reference for the maximum-margin property. This is a substantive claim presented as fact without support.

### Minor

- **No empirical comparison against prior hyperbolic DTs.** The paper extends Chlenski et al. (2024) hyperbolic DTs but does not compare against them on hyperbolic benchmarks. A side-by-side comparison would verify that the angular reformulation does not degrade performance and would clarify what is new.

- **Product manifold results are competitive, not dominant.** Product DTs/RFs are top-1 on only 18/35 (~51%) of product manifold benchmarks (Table 1). k-NN wins on all 8 Synthetic multi-K classification cases, PolBlogs, and multiple link prediction tasks (Table 2). When Product wins, margins are often small (0.1–0.5 F1). The abstract's characterization as "straightforward yet powerful new tools" oversells the evidence on product manifolds. The paper reports these numbers transparently; the issue is one of framing.

- **Ambiguity in the set of candidate projections.** Section 3 (line 252) describes splits using projections onto \(\{x_0, x_d\}\), while Section 4.3 (line 522) says it considers all \(\binom{D}{2}\) projections. The paper never resolves this discrepancy or states the exact set used per component manifold. This directly relates to the oblique split confound above and affects reproducibility.

### Trivial
None.

## Nice-to-Haves

- An ablation on Euclidean data comparing: (a) restricted to \((x_0, x_d)\) projections only (axis-aligned equivalent), (b) all \(\binom{D}{2}\) projections, vs. an explicit oblique Euclidean DT baseline.
- Error bars or significance tests on the product manifold results in Tables 2 and 3.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about y-axis range exaggeration in Figures 3–4**: The harsh critic claims the y-axis range (0.2–0.8) exaggerates differences because values are around 0.3–0.4. Showing the full plausible range of the metric is standard practice. **Removed.**
- **Criticism about missing appendix content (midpoint formula derivation)**: The reviewer questions the Euclidean midpoint formula and says verification requires the Appendix. The parser strips appendices; the paper claims equivalence is proved in Appendix C. **Removed per rule.**
- **Concern that synthetic data sampling may introduce artifacts favoring angular splits**: The critic says "the method is only described in the appendix." Since appendices are stripped, this is not a valid criticism of the submission. **Removed.**
- **Concern about signature selection creating a "selection effect"**: The paper uses the standard embedding pipeline (Gu et al., 2018) applied equally to all methods. No evidence that it specifically favors Product DT/RF. **Removed as speculative.**

## Novel Insights

The most interesting observation from synthesizing the reviews is the tension between the paper's framing of its angular method as a "natural" geometric extension — where Euclidean splits are claimed to be "completely equivalent to thresholding in the basis dimensions" (Section 3.1) — and the actual implementation's use of all \(\binom{D}{2}\) projections, which for Euclidean components introduces oblique splits that go beyond axis-aligned thresholding. This means the paper is simultaneously doing two things: (1) enabling manifold-aware splits in non-Euclidean components via the angular formulation, and (2) implicitly enabling more expressive (oblique) splits in Euclidean components — and evaluating them together without disentanglement. The paper's own future work mentioning "oblique decision trees" as a separate direction inadvertently highlights that this confound exists.

## Suggestions

1. **Address the oblique split confound.** Restrict Euclidean components to \((x_0, x_d)\) projections only in one ablation, and compare against an explicit oblique Euclidean DT baseline. If the advantage persists with axis-aligned-only splits, the geometric-awareness claim is clean.
2. **Substantiate or remove the "maximum-margin" claim.** Provide a brief proof or reference.
3. **Add a comparison against Chlenski et al. (2024) hyperbolic DTs** on hyperbolic benchmarks.
4. **Resolve the discrepancy** between Section 3 and Section 4.3 on the set of candidate projections used.
5. **Tone down the framing** on product manifold results to match the evidence: competitive but not decisively superior to k-NN.

## Score and Decision

**Anchor comparison** (all anchors retrieved across rounds):

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| Manifold Kernel Rank Reduced Regression | 3.00 | R1 | Much weaker — limited scope, poor clarity |
| Learning from A Single Graph | 3.17 | R1 | Weaker — narrower contribution |
| Sparse Hyperbolic Representation Learning | 5.00 | R1/R2 | Similar theoretical contribution level but less empirical breadth; this paper is slightly stronger due to broader evaluation |
| Manifold Learning via Foliations | 5.00 | R2 | Similar score range but less practical contribution |
| Balanced Hyperbolic Embeddings | 5.50 | R1/R2 | Similar quality — both have genuine contributions but evaluation concerns |
| Neural Tangent Kernels for Tree Ensembles | 5.50 | R2 | Similar — solid theory but limited experimental validation |
| **Spectro-Riemannian GNN (CUSP)** | **5.75** | **R1** | **Similar topic (mixed-curvature models); accepted as poster. CUSP had presentation issues but no evaluation confound. This paper has a cleaner contribution but a more substantive evaluation issue.** |
| Residual Deep GPs on Manifolds | 7.60 | R1 | Significantly stronger — cleaner theory and evaluation, accepted Oral |
| Compositional Entailment Learning (Hyperbolic) | 8.00 | R1 | Much stronger — comprehensive experiments, accepted Oral |

**Round 1 bracket**: 4.5–6.5. **Round 2 narrowing**: The paper is above the 5.0 anchors (sparse hyperbolic, manifold foliations) due to broader empirical validation and a clearer practical contribution, but below the Spectro-Riemannian GNN (5.75, accepted poster) because the evaluation confound is more significant than the presentation issues that held back CUSP. The paper's core contribution is genuine and the angular formulation is elegant, but the oblique split confound prevents the evaluation from cleanly supporting the geometric-awareness claims on product manifold data.

**Final score: 5.5.** This reflects a borderline paper — above clear rejects (3.0–4.0) but with a substantive evaluation issue that needs to be resolved before the paper can be confidently accepted. The paper would benefit from a major revision addressing the confound and toning down unsubstantiated claims.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>