- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 6, 5
Now I have a complete picture. Let me produce the consolidated review.

---

## Summary

This paper introduces the Riemannian Diffusion Mixture (RDM), a generative framework on Riemannian manifolds that constructs a diffusion process as a mixture of bridge processes. The key innovations are: (1) constructing bridge processes (Logarithm bridge and Spectral bridge) on manifolds without requiring heat kernel estimation, (2) deriving the mixture drift as a weighted mean of tangent vectors toward data points, and (3) a two-way bridge matching training objective that avoids divergence computation and enables scaling to high dimensions. Experiments on spheres, tori, protein data, and general closed manifolds demonstrate competitive or superior performance while using dramatically fewer in-training simulation steps compared to deterministic flow models.

## Strengths

- **No heat-kernel approximation required**: The Logarithm bridge (Eq. 4) and Spectral bridge (Eq. 6) are defined using the logarithm map or spectral distances, bypassing the intractable heat kernel that previous Riemannian diffusion models (RSGM, RDM) rely on. This is a concrete and well-motivated advance.

- **Scalable training without divergence computation**: The two-way bridge matching objective (Eq. 13–14) reduces training to simple regression of tangent-vector drifts. This eliminates the need to compute the Riemannian divergence (or its stochastic estimator), which cripples prior methods in high dimensions. The paper demonstrates scaling to tori of dimension 10⁴ (Section 4.3).

- **Geometric interpretation of the mixture drift**: The drift of the mixture process is derived as a weighted mean of tangent vectors pointing toward data points (Figure 1, Eq. 7). This provides an explicit geometric intuition connecting the generative process to the data distribution, in contrast to score-based models where the drift is a learned score function without such direct interpretation.

- **Unification with Riemannian Flow Matching**: The paper shows RFM emerges as the zero-noise limit of the mixture process (Section 3.3), establishing a theoretical bridge between stochastic diffusion and deterministic flow frameworks on manifolds.

- **Dramatic reduction of in-training simulation steps on general manifolds**: On triangular meshes (Section 4.4), the method achieves superior performance using only 15 in-training simulation steps (5% of the steps needed by RFM), yielding a ×12.8 speedup. This empirically validates that stochasticity in the mixture process reduces the need for fine-grained trajectory simulation compared to deterministic flow models.

## Weaknesses

### Fatal
None.

### Major

- **The backward bridge drift η^y_b is used in the training objective but never explicitly defined.**  
  The two-way bridge matching objective (Eq. 13, line 162–163) contains terms for both the forward bridge drift η^x_f (defined in Eq. 4/6) and the backward bridge drift η^y_b, where the latter appears without an explicit formula. The paper states that the time-reversed process can be derived from the score function (line 128), but for the specific Logarithm and Spectral bridges used in training, η^y_b is not given. While the backward bridge can be inferred by symmetry — the bridge Q^{x,y} conditioned on both endpoints should be time-reversible with the drift having the same functional form but with endpoints swapped — the paper should state this explicitly and address any manifold-specific issues (e.g., whether the eikonal identity ||∇d_g||=1 holds for the geodesic distance on both the forward and backward path, and whether the cut-locus affects backward simulation). Without this specification, the training algorithm is partially underspecified, and practitioners cannot independently verify or implement the backward direction. **This is a clear gap that should be resolved in revision.**

### Minor

- **The theoretical KL guarantee (Girsanov argument) is not rigorous for singular drifts.**  
  The paper claims (line 166, line 192) that minimizing the two-way bridge matching objective guarantees minimizing KL divergence via a Girsanov-type argument. The Logarithm bridge drift has a singularity at t→T (the factor σ²_t/(τ_T−τ_t) diverges), which may violate standard integrability conditions (e.g., Novikov condition) required for Girsanov's theorem on manifolds. The paper should either: (a) provide a limiting/regularization argument showing the guarantee holds in an approximate sense, (b) cite relevant theorems that handle such singular drifts, or (c) acknowledge this limitation and reframe the objective as a surrogate loss justified by empirical performance (as is common in the diffusion bridge literature). This does not invalidate the method — many bridge-based objectives have this theoretical gap — but the current framing as a guaranteed KL minimizer is overstated.

- **The "most probable endpoint" claim (Eq. 7) lacks theoretical justification.**  
  The prediction formula (Eq. 7, line 117) is presented as "the most probable endpoint" of the mixture process given the current state, but the paper provides no derivation or proof that this quantity corresponds to a mode of the conditional distribution p(z|X_t). The formula is geometrically intuitive as an expected direction projected onto the manifold via the exponential map, but calling it the "most probable endpoint" is a stronger claim. The authors should rename it (e.g., "geodesic mean prediction") or provide supporting reasoning.

- **The ablation comparing uniform-time vs. importance-sampled time (Table time_weight_abl) conflates two different objectives.**  
  The paper claims (line 184–185) that the uniform-time variant drops in performance because it does not maximize likelihood, while the time-scaled (importance-sampled) objective does. However, the uniform-time variant minimizes an unweighted regression loss that is *not* guaranteed to bound the same KL divergence. The comparison therefore demonstrates that two different losses perform differently, not specifically the effect of the time distribution q. This does not undermine the method's success, but the framing of the ablation as isolating the effect of q should be softened.

- **Cut-locus limitations are acknowledged in a footnote but their practical implications are not discussed.**  
  The paper notes (footnote, line 64) that the logarithm map is only defined when the endpoint is not in the cut locus of the current state. For the sphere (antipodal points) and general meshes, this is a genuine practical concern that can cause numerical instability when samples are near the cut locus. A brief discussion of how this is handled in practice (e.g., by projecting away from the cut locus, or by noting that the probability of exactly hitting the cut locus is zero) would improve rigor.

### Trivial

- None beyond typical formatting and \input-stripping artifacts attributable to the PDF extraction process.

## Nice-to-Haves

- A brief pseudocode or diagram for the two-way simulation (especially the backward direction) would significantly improve reproducibility.
- A comparison with the simplified score matching approaches for Riemannian diffusion (e.g., De Bortoli et al. 2022's Varadhan-based approximations) could help contextualize the contribution more clearly.
- Quantitative results (KL divergence or Wasserstein distance) for the high-dimensional tori experiment (Figure 3 Right), which is currently described qualitatively.

## Removed Points

- **Criticism that the Spectral/Logarithm bridge equivalence claim is mathematically wrong**: REMOVED — This criticism contains a mathematical error. The Spectral bridge denominator is ||∇d_w||² (squared norm of the gradient of the *distance*, not the squared distance). For geodesic distance d_g, ||∇d_g|| = 1 (eikonal equation) and ∇(d_g²) = −2·exp⁻¹(z), so the Spectral bridge drift *does* correctly recover the Logarithm bridge drift. The critic's computation assumed the denominator was ||∇(d_g²)||², resulting in a different expression. The paper's claim (line 87) is correct.

- **Missing experimental tables (Tab. 1–3) and Algorithm 1**: REMOVED — These are \input-included files stripped by the PDF extraction parser. They exist in the original submission.

- **Cut-locus not addressed**: REMOVED — The paper already acknowledges this in a footnote (line 64).

- **Missing related works or comparison with more recent methods**: REMOVED — The paper cites relevant prior work including RSGM, RDM, RFM, CNFM, etc. The reviewer's speculation about unreferenced works cannot be verified and should not be a weakness.

- **Formatting/style nitpicks and speculation about unreleased resources**: REMOVED per guidelines.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's detailed mathematical critique was largely standard (e.g., Girsanov conditions for singular drifts, reverse drift specification) and did not surface issues beyond what the paper itself could address with clarifications.

## Suggestions

1. **Explicitly define η^y_b** for the Logarithm bridge and Spectral bridge. State the formula and note whether any manifold-specific conditions affect the backward direction (e.g., cut-locus asymmetry, non-constant curvature).
2. **Acknowledge the Girsanov/singular-drift gap** explicitly and either provide a limiting argument or soften the claim from "guarantees to minimize KL" to "the objective is a surrogate loss derived from a KL bound" with appropriate theoretical caveats.
3. **Rename or qualify the "most probable endpoint"** (Eq. 7) to reflect that it is a geodesic-mean prediction rather than a proven mode of the conditional distribution.
4. **Clarify the time-ablation** by noting that the uniform-time variant optimizes a different (unweighted) objective, so the comparison demonstrates the importance of the appropriate loss weighting rather than simply the effect of the time distribution q.
