## Summary

This paper provides a complete, constructive characterization of polynomial (and, via Stone-Weierstrass, continuous) equivariant tensor-to-tensor functions under the diagonal action of O(d), the indefinite orthogonal group (including the Lorentz group), and the symplectic group. The parameterization uses invariant-theoretic tools (isotropic tensors, Kronecker deltas, Levi-Civita symbols) rather than Clebsch–Gordan coefficients, making it dimension-agnostic and applicable to non-compact groups. The authors instantiate this framework for the practically important vector-input case (Corollaries 1 and 3) and demonstrate on three problems — stress-strain constitutive modeling, path-signature estimation, and sparse vector recovery — that the resulting equivariant models substantially outperform non-equivariant baselines and, in several settings, prior specialized methods.

## Strengths

- **Complete theoretical characterization across multiple groups.** Theorem 1 and Corollary 1 give an explicit parameterization of O(d)-equivariant polynomial tensor functions using isotropic tensors, avoiding the dimension-limited (d=2,3) Clebsch–Gordan machinery of e3nn/escnn. Theorem 2 and Corollary 3 extend this to the indefinite orthogonal group (including Lorentz) and symplectic group — genuinely new territory where representation-theoretic methods are far less developed. This is the paper's core contribution and is well-supported mathematically.

- **Principled practical instantiations for vector inputs.** Corollary 1 reduces the general construction to a tractable form: for output tensor rank k' ∈ {1,2,3,4}, the function is a linear combination of outer products of input vectors and Kronecker deltas, with coefficients being scalar functions of invariant inner products. The complexity is explicitly stated (O(k'! n^{k'} (Q d n^2 + d^{k'}))), and all experiments operate within this feasible regime. The bridge from heavy invariant theory to implementable ML architectures is well-engineered.

- **Consistent and often dramatic empirical improvement.** Table 1 shows the proposed method achieving test error 4.057×10⁻⁶ (n=5,000) on the stress-strain problem — over an order of magnitude better than the prior TFENN and nearly two orders better than the best non-equivariant baseline. Table 2 shows O(d) and Lorentz path-signature errors of 0.002 and 0.005, compared to 0.255 and 1.391 for same-width MLPs. Table 3 demonstrates that the learned equivariant model outperforms sum-of-squares methods when the strict SoS assumptions are violated (e.g., Accept/Reject with Random covariance: 0.938 vs 0.610).

- **Extension to groups beyond O(3).** The Lorentz and symplectic extensions are non-trivial and open up new application domains (special relativity, classical/quantum mechanics) that prior equivariant ML toolkits cannot address. The path-signature experiment with Lorentz symmetry is a concrete demonstration of this reach.

## Weaknesses

### Fatal
None.

### Major

- **No experimental comparison to Clebsch–Gordan-based equivariant methods (e3nn, escnn).** The paper discusses these methods in the related work, acknowledges they are "more memory efficient" and states "the computational and approximation power should be equivalent," but provides no experimental evidence for the O(d) case where they apply. For the stress-strain problem (3D, O(3) symmetry), an e3nn baseline would be natural; omitting it means the reader cannot assess whether the invariant-theoretic parameterization offers any practical advantage over the established approach on its own domain. The paper's claim of practical utility for O(d) is therefore under-supported by the experiments. This does not invalidate the Lorentz/symplectic contributions (where e3nn/escnn do not apply), but it leaves a significant gap in the empirical validation for the orthogonal case.

### Minor

- **Path-signature experiment under-documented in the main text.** The truncation level M is used in the metric definition (1/M ∑_{k=1}^M …) but its value is not stated in the main text. The "Discrete (24)" baseline's meaning (presumably n=24 sample points and the discrete Riemann-sum approximation) is not explained. The MLP baselines' input representation (flattened vectors of all coordinate points? differences?) is not specified. The appendix (I.2) is referenced but was stripped by the parser. While the appendix likely contains these details, the main text should convey enough for a reader to understand what was done.

- **"Ours (Diag)" variant sometimes outperforms the full model.** In Table 3 (e.g., Bernoulli-Gaussian / Diagonal covariance: Diag 0.914 vs Full 0.463; Accept/Reject / Diagonal: Diag 0.589 vs Full 0.465), the variant that uses only norms (diagonal inner products) substantially outperforms the full model using all pairwise inner products. This suggests overfitting or noise in the off-diagonal features. The paper reports this honestly but does not analyze it.

- **Scalability discussion is honest but brief.** The complexity analysis (O(k'! n^{k'} …)) is given, and the paper notes that k' ∈ {1,2,3,4} captures practical cases. However, no approximation strategies or truncation heuristics are discussed for cases where the output order is higher or the number of input vectors is large. A brief note on how practitioners might handle larger settings (e.g., sampling input vectors, learning the q functions with weight sharing across permutations) would be helpful.

### Trivial

- The metric in Table 2's caption contains a parser artifact: "\frac{d_F}{d_F}" should clearly be some normalization by dimension (likely 1/d² or similar). This is a rendering issue in the extracted text, not a substantive error.

## Nice-to-Haves

- A direct comparison to e3nn/escnn on the stress-strain or path-signature O(d) problems would substantially strengthen the paper, even if results are comparable.
- A brief ablation or discussion of why the Diag variant outperforms the full model in some sparse-vector settings would improve interpretability.
- A short "Limitations" subsection (factorial complexity for high output order, restriction to vector inputs in Corollaries 1/3) would be a welcome addition, though much of this content is already present.

## Removed Points

These points were flagged by the input reviewers but are removed here:

- **Clebsch–Gordan methods being "specific for SO(d) and O(d) for d=2,3" phrasing being inaccurate.** The paper's characterization is fair; the representation-theoretic framework does generalize to any compact group, but the cited implementations (e3nn, escnn) are indeed limited to d=2,3. This is a minor scope clarification, not a weakness.
- **Figure 1 caption typo (S_k vs S_{k'}).** The caption text correctly uses S_{k'}. Any rendering issue in the figure itself would be a parser artifact, not an author error.
- **Entire-function vs. polynomial gap (Theorem 2 vs. experiments).** Remark 1 explicitly addresses this by noting that polynomials suffice via Stone–Weierstrass, and that the MLP parameterization is a practical approximation. The paper is clear on this point.
- **Related works being missing.** As the external reviewer lacks access to the full literature and the paper's reference list was partially stripped, this cannot be evaluated. Per the hard rules, this criticism is removed.
- **Missing appendix content / proofs.** Per the hard rules, appendix sections are stripped by the parser; they exist in the original submission.
- **Theoretical contribution being derivative.** The paper's characterization for O(d), Lorentz, and symplectic groups goes beyond prior work (Villar et al. covered O(d) scalars; Pearce-Crump covered O(d)/SO(d)/Sp(d) but only for equal input/output tensor powers). The specific formulation for ML use is original.
- **"Not yet released" code.** The paper explicitly states the code is available at a GitHub URL. Criticism of release status is removed per the hard rules.

## Novel Insights

The synthesis of the two reviews reveals a tension that is worth noting: the harsh critic's core objection (missing e3nn baseline) and the strength finder's strongest praise (general characterization for multiple groups) are two sides of the same coin. The paper is most novel where no baseline exists (Lorentz, symplectic), but the O(d) experiments — the bulk of the numerical evaluation — would benefit from comparison to existing methods precisely because O(d) is the well-studied case. This asymmetry between where the theory is most novel (non-compact groups) and where the experiments are most conventional (O(d) stress-strain, sparse vectors) is the paper's main structural limitation. A productive path forward would be to either (a) add an e3nn baseline for the O(d) experiments to close the loop, or (b) focus the experimental narrative more heavily on the Lorentz/symplectic cases where the method's advantage is clearest.

## Suggestions

1. Add an e3nn or equivariant baseline to at least one O(d) experiment (stress-strain is natural) to substantiate the claim of comparable performance.
2. State M (truncation level), n (sample points), and the MLP input representation in the main text for the path-signature experiment.
3. Add a brief discussion of the "Ours (Diag)" outperforming "Ours" in the sparse-vector setting — does this reflect overfitting, and how could a practitioner guard against it?
4. Include a short limitations paragraph explicitly stating the factorial scaling with k' and the restriction to vector inputs in the practical corollaries.
5. Clarify the metric normalization in Table 2.

## Calibration Report

**Round 1 (Bracketing):** Three queries on "equivariant neural networks tensor learning group symmetry invariant theory" with score filters:
- High < 3.5: returned anchors at 3.33 (symmetric tensor network, reject), 2.00 (learned polarization, reject), 2.40 (gauge theory GNN).
- Low 3.5 to high 7.5: returned anchors at 5.50 (binary forms, reject), 5.00 (universality of equivariant nets, accept poster), 6.50 (approximate equivariance, reject), 6.67 (symmetry increase, accept poster).
- Low > 7.5: returned anchors at 8.50 (rotation estimation), 8.00 (permutation-equivariant geometry), 8.00 (quantum), 8.00 (text-to-3D) — topic-mismatched.

**Initial bracket:** 5.0 – 7.0.

**Round 2 (Narrowing):** Two queries targeting (4.5,6.5) and (5.5,7.5):
- Retrieved anchors: 5.00 (antisymmetric tensors, reject, scores 4,8,6,2), 5.60 (approximate symmetry, accept poster), 6.00 (AdS-GNN, accept poster), 6.50 (approximate equivariance, reject), 6.67 (symmetry increase, accept poster).

**Comparison:** The paper is stronger than the antisymmetric-tensors paper (5.00, reject) — more groups, more experiments — and stronger than the binary-forms paper (5.50, reject) — broader group coverage and more diverse validation. It is comparable to AdS-GNN (6.00, accept poster) and the symmetry-increase paper (6.67, accept poster) in overall quality, while the theoretical contribution is broader in scope. The missing e3nn baseline prevents it from reaching the 7+ tier, but the core theory is sound and the Lorentz/symplectic extensions are genuinely novel.

**Final score anchored:** between the 5.00–5.60 papers (weaker) and the 6.50–6.67 papers (comparable), slightly closer to the upper end because the theoretical contribution is more general and better-validated than the antisymmetric/anchor papers in the lower band.

**Anchors retrieved:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| MQucws0B1g.md | 3.33 | R1 | Much weaker — single experiment, narrower theory |
| hFBQTUrycC.md | 2.00 | R1 | Much weaker — different topic, no experiments |
| q95Hql3QBk.md | 2.00 | R1 | Much weaker — theoretical only, no experiments |
| QxoyccprRp.md | 2.40 | R1 | Much weaker — different architecture focus |
| anvRacYUHe.md | 5.50 | R1/R2 | Weaker — SO(3) only, fewer experiments |
| Q2D1PI6zY1.md | 5.00 | R1/R2 | Weaker — pure theory, no experiments |
| HVKB5DM5n7.md | 6.50 | R1/R2 | Comparable quality, different approach (approx equivariance) |
| dUgq4bLY4X.md | 6.67 | R1/R2 | Comparable quality, different contribution (symmetry increase analysis) |
| HufTLkTOJh.md | 5.00 | R2 | Weaker — narrower scope (permutation equivariant antisymmetric tensors), toy experiments |
| ncOJYFcleS.md | 5.60 | R2 | Weaker — theoretical analysis rather than constructive architectures |
| EIyvsL5Cue.md | 6.00 | R2 | Comparable — accepted, similar quality but different symmetry type (conformal) |
| jz3d7nvtGz.md | 6.50 | R2 | Comparable — accepted, different focus (subgroup equivariance) |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>