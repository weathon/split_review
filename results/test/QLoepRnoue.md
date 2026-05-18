Now I have a comprehensive understanding of the paper and have verified all claims against the actual paper content. Let me write the final consolidated review.

---

## Summary

This paper proposes Hyper-Dimensional Function Encoding (HDFE), a training-free method that encodes continuous (Lipschitz) functions into fixed-length complex vectors by mapping samples through a fractional-power encoding and aggregating via weighted superposition and binding operations. HDFE is claimed to satisfy sample invariance, decodability, and distance preservation. The method is evaluated on two tasks: PDE solving (competitive with FNO, outperforming MGKN/PCANN) and point cloud normal estimation (12-15% error reduction over PointNet, 1.7-2.5% improvement over SOTA when used as a plug-in).

## Strengths

- **Relaxation of VFA's restrictive functional form.** The paper clearly identifies and overcomes a key limitation of VFA, which requires functions to be of the form \(f(x)=\sum_k\alpha_k K(x,x_k)\). HDFE targets the much larger class of Lipschitz functions. The constant-function counterexample (Section 2) concretely demonstrates why this matters. This is a principled theoretical advance.

- **Strong empirical performance on two diverse domains.** On PDE solving (Section 3.1), HDFE achieves ~55% lower prediction error than MGKN and PCANN and is competitive with FNO when decoding is required. On point cloud normal estimation (Section 3.2), replacing PointNet with HDFE yields average error reductions of 12% and 15% on two benchmarks, and integrating HDFE into the SOTA network (HSurf-Net) further improves by 2.5% and 1.7%. These are substantiated, significant quantitative improvements.

- **No training required for encoding.** HDFE produces the vector representation without learned parameters (abstract, Section 1). This enables plug-and-play use in scarce-data scenarios and distinguishes HDFE from prior frameworks that require encoder training.

- **Works on both mesh-grid and sparse data.** The method is evaluated on dense grid-sampled PDE solutions and on sparse point cloud data, overcoming a limitation of grid-based methods like FNO. This versatility is explicitly demonstrated with quantitative results.

## Weaknesses

### Fatal

None.

### Major

1. **Theoretical gap: implicit function encoding does not satisfy the Lipschitz assumption that underlies all stated guarantees.** The paper claims to generalize HDFE to implicit functions (Section 2.2), justifying this by defining an auxiliary explicit function \(g(x)=1\) if \(f(x)=0\) and \(g(x)=0\) otherwise. The paper explicitly states (line 84) that "Throughout the section, we assume the functions are \(c\)-Lipschitz continuous" and builds sample invariance, decodability, and distance-preservation theorems on this assumption. However, \(g\) is an indicator function — it is discontinuous everywhere on the boundary of the zero set and therefore not Lipschitz. The paper provides no argument that the theoretical properties (Theorem 1, Theorem 2) transfer to this setting. The normal estimation experiment (Section 3.2) uses HDFE to encode point cloud patches, which the paper frames as an implicit function task; the strong empirical results here are not clearly backed by the paper's theoretical claims. This creates a gap between the theory and one of the two main applications. A clarified account of how or whether sample invariance holds for set/point-cloud encodings is needed.

### Minor

2. **Unsupported geometric claim about the iterative refinement.** Algorithm 1 and the surrounding text (line 168) assert that the iterative refinement procedure produces "the center of the smallest ball containing all the sample encodings." No reasoning, citation, or sketch is provided for why repeatedly adding the farthest-point encoding to the sum would converge to the smallest enclosing ball's center. For points on the complex unit circle (which the fractional-power encoding produces), the center of the smallest enclosing ball is generally interior to the sphere, while the normalized sum lies on the sphere — these are not obviously related. The paper's core claims about sample invariance do not depend on this specific geometric interpretation, but the claim as stated is misleading and unsubstantiated.

3. **Theorem 2 (distance preserving) is imprecisely stated in the main text.** The theorem asserts \(\|f-g\|_{L_2} \approx b - a\langle\mathbf{F},\mathbf{G}\rangle\) without defining the constants \(a\) and \(b\) or specifying conditions on the random matrices \(\Phi,\Psi\), the parameters \(\alpha,\beta\), or the embedding dimension \(N\) under which the approximation holds. While a rigorous derivation may exist in the appendix (which the parser strips), the main-text statement alone is too vague to be evaluated as a theorem — it reads more as a conjecture or heuristic. The paper would benefit from specifying the dependence on these quantities in the main statement.

4. **Algorithm 1 omits specification details.** The algorithm's stopping criterion "while \(\min_i \langle \mathbf{F}, z_i\rangle\) still increases" does not clarify whether the minimum is compared against the previous iteration's value or the initial value. The algorithm also does not specify whether \(\mathbf{F}\) is re-normalized within the loop; since the final encoding is normalized (Eq. 4) and the similarity metric \(\langle\cdot,\cdot\rangle\) is used for stopping, the behavior differs depending on whether normalization occurs at each step or only at the end. These ambiguities hinder exact reproduction.

### Trivial

- Theorem 2 uses the notation \(\mathbf{G}\) for the encoding of function \(g\), but this symbol is not defined earlier in the paper and could be confused with the kernel matrix notation used elsewhere.

## Nice-to-Haves

- The "scale to high-dimensional input" discussion (Section 4.4) claims HDFE mitigates the curse of dimensionality via low-rank subspace arguments, but no experiment supports this. A small synthetic demonstration (e.g., encoding a function on a 10D domain with low intrinsic dimension) would strengthen this claim.
- The paper could explicitly state how the iterative refinement's behavior changes with embedding dimension \(N\), since the geometry of high-dimensional spheres likely affects the "smallest ball" interpretation.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The iterative refinement does not produce a weighting scheme"* — Factually incorrect. Adding a sample encoding with multiplicity is equivalent to assigning it higher weight. The algorithm produces \(\mathbf{F} = \sum_i w_i z_i\) where \(w_i\) is the multiplicity of sample \(i\).
- *"Proofs of Theorem 1 and Theorem 2 are absent"* — The parser strips appendix/supplementary sections from all papers. The proofs are assumed to exist in the original submission.
- *"The similarity measure \(\langle\mathbf{F}, z_i\rangle\) is not defined"* — The paper defines \(\langle\cdot,\cdot\rangle\) as the similarity between vectors (line 105) and uses cosine similarity for decoding (line 142). For complex vectors, the Hermitian inner product is the standard choice.
- *"The paper never describes how the PDE itself is encoded"* — The PDE benchmark provides PDEs via coefficient functions (initial condition, permeability field). Encoding the PDE means encoding this coefficient function using HDFE, which is described in the architecture paragraph (Section 3.1). This is standard in the neural operator literature.
- *"Theorem 2 is very likely false"* — Without access to the (stripped) appendix containing the derivation and conditions, this assertion is unverifiable. The criticism about imprecision in the main-text statement is kept as Minor #3 above.

## Novel Insights

The reviews surface a tension between the paper's theoretical framing and its actual experimental usage. The "implicit function" framing for the normal estimation experiment is where this gap is sharpest: the paper could reframe point cloud encoding as encoding an empirical distribution of points (a well-studied HDC primitive) rather than encoding an implicit function \(f(x)=0\). This reframing would eliminate the Lipschitz concern while preserving the practical contribution. Separately, the iterative refinement algorithm bears a resemblance to the "farthest-point sampling" used in some kernel herding and coreset methods — a connection the paper does not discuss but that could provide a principled foundation for its claims.

## Suggestions

1. **Clarify the theoretical status of implicit function encoding.** Either (a) provide a separate argument for why sample invariance holds for set/point-cloud encodings without the Lipschitz assumption, or (b) explicitly restrict the theoretical guarantees to explicit Lipschitz functions and treat the implicit / point-cloud encoding as a heuristic (with empirical justification only).
2. **Either substantiate or remove the "smallest ball" geometric claim.** If the algorithm truly converges to the center of the smallest enclosing ball, provide a citation or a brief proof sketch. If not, describe what the algorithm actually achieves (e.g., "equalizes the similarity of \(\mathbf{F}\) to all sample encodings") without invoking unsupported geometry.
3. **Specify the constants in Theorem 2 or reframe it as an empirical observation.** If the exact form depends on \(\alpha,\beta,N\) and the random matrices, say so in the main statement.
4. **Clarify Algorithm 1** by adding a normalization step inside the loop if one is used, and specifying the comparison baseline for the stopping criterion.
5. **Add a small synthetic experiment** demonstrating the distance-preservation claim (Theorem 2) on functions with known \(L_2\) distances, to build trust in the isometry property.

## Score and Decision

The paper introduces a genuinely novel and well-motivated approach to function encoding, with strong empirical results across two distinct domains and clear advantages over the closest prior work (VFA). The main weaknesses — the implicit-function theoretical gap and the unsupported geometric claim about the iterative refinement — are real but not fatal: the empirical contributions stand on their own, and both issues are addressable through clarification and reframing rather than new experiments. The paper would benefit from tightening the theoretical presentation but already contains a solid contribution.

**Score**: 6.0 — Weak accept. The paper makes a useful contribution but has significant gaps in presentation and theoretical rigor that should be addressed before publication.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>