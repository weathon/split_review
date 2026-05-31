## Summary

This paper investigates the internal representations of DINOv2 through three lenses: (1) training a stable Sparse Autoencoder (SAE) on DINOv2-B to extract a 32,000-concept dictionary and analyzing how downstream tasks recruit different subsets; (2) characterizing the statistical and geometric properties of the learned concept space; and (3) proposing the *Minkowski Representation Hypothesis* (MRH) as an alternative to the Linear Representation Hypothesis, arguing that token activations behave as Minkowski sums of head-wise convex polytopes over archetypal landmarks rather than sparse combinations of near-orthogonal directions.

---

## Strengths

- **Scale and tooling.** The 32k-concept SAE dictionary and its interactive visualization represent the largest mechanistic interpretability demonstration for a vision foundation model. This is a genuine infrastructure contribution to the community.

- **Task-specific concept analysis (Section 3) is compelling.** The "Elsewhere" concept discovery—tokens that fire off-object yet vanish when the object is causally removed—is a novel, concrete finding that challenges attribution-map interpretations. The border-concept characterization for segmentation is quantitative (coherence, eigenspectrum), not merely anecdotal. The perturbation-based decomposition of depth cues into three functional clusters (projective geometry, shadow-based, frequency transitions) is creative, methodologically transparent, and connects to visual neuroscience.

- **Geometric analysis (Section 4) uses appropriate baselines.** The comparisons of dictionary coherence against random and Grassmannian baselines (via TAAP), the singular-value spectrum analysis, the Hoyer score audit, and the separation of positional vs. semantic structure are carried out rigorously and jointly build a coherent case that LRH is an incomplete description.

- **Positional structure analysis is a nice standalone finding.** The observation that DINOv2's positional encoding compresses from high-rank in early layers to a near-2D sheet in the final layers (Figure 6) is elegant and well-supported.

---

## Weaknesses

### Fatal
None.

### Major

**1. Proposition 1 (multi-head attention realizes MRH) is tautological.** Each attention head outputs a convex combination of its values by construction; the sum of heads is therefore a Minkowski sum by definition. No assumption about the data or training is needed—this holds for any attention-based model regardless of what it has learned. Presenting this as a "theoretical account" supporting MRH overstates its significance; it merely shows MRH is *architecturally consistent*, not that it is *empirically realized* with meaningful factorizations.

**2. Methodological circularity for MRH.** The stable SAE explicitly constrains the dictionary D ∈ conv(A), meaning every atom is by construction a convex combination of observed activations. Discovering subsequently that token clouds are well-approximated by convex combinations of these same atoms (the Archetypal Analysis comparison in Fig. 26) is at least partly an artifact of the imposed constraint rather than independent evidence for MRH. The paper does not disentangle these two sources.

**3. MRH empirical evidence is too preliminary to support the proposed implications.** The three tests offered (geodesic vs. linear interpolation, AA vs. SAE reconstruction, block structure in Gram matrices) are individually suggestive but collectively insufficient. The interpolation test does not control for the intrinsic dimensionality of the data manifold. The AA reconstruction comparison lacks statistical error bars or ablations over the number of archetypes. The block structure in Fig. 26 (right) is described qualitatively. Given that the implications section draws strong practical conclusions (steering saturates at landmarks, decomposition requires per-head access), a stronger empirical foundation is warranted.

**4. Non-identifiability (Proposition 2) undermines the practical utility of MRH.** The paper proves that Minkowski decompositions of X are generally non-unique, then concludes that "estimating individual concept contributions from final activations alone is underdetermined." This is a significant limitation for the proposed interpretability implications. The paper does not explain how the proposed per-head access resolves the non-identifiability in practice.

### Minor

- The "Elsewhere" concept causal analysis (Figure 2) is described as "evidence suggestive of a causal effect"; a more systematic experiment varying the masking procedure across more images and classes would strengthen this. The current evidence relies on visual inspection of a few examples.
- The claim that "classification draws from a broader span of the dictionary than segmentation or depth" (Section 3) is interesting, but the analysis uses top-k recruited concepts without controlling for the difference in linear probe dimensionality or task complexity. A controlled comparison would make this more rigorous.
- The comparison between co-activation geometry (Z⊤Z) and dictionary geometry (DD⊤) (Section 4) is an interesting negative result, but the footnote conceding algebraic confoundedness (the correlation is ∝ tr(A⊤A)) partially explains the observed weak correlation without the authors following up on whether the residual signal is meaningful.

### Trivial
None.

---

## Nice-to-Haves

- Replication of the core task-specialization findings on DINOv2-L or another ViT backbone would substantially increase confidence in the generality of the conclusions.
- A more careful separation between the circular effect of the convex SAE constraint and genuinely discovered convex structure would strengthen the MRH narrative.
- A concrete example of "archetypal steering" vs. "directional steering" (Figure 7, right) with quantitative evaluation (e.g., downstream task performance or faithfulness metric) would validate the practical implications of MRH.

---

## Novel Insights

The most genuinely novel observation in the paper is the *Elsewhere concept* finding: DINOv2 learns concept detectors that fire off-object in a manner that is causally conditioned on the object's presence—implementing a form of learned negation not captured by standard attribution maps. This has direct implications for how we interpret activation maps and how explanations can mislead. Separately, the layerwise collapse of positional encoding to a near-2D sheet, and the discovery that this low-dimensional position signal explains little of the smooth PCA organization of token clouds, is a clean negative result that points usefully toward the role of semantic content in shaping the representation manifold.

---

## Suggestions

- Provide error bars or cross-run stability measurements for the concept count and downstream alignment scores; the stable SAE is motivated partly by reproducibility, and concrete stability numbers would make that motivation payoff visible.
- Extend the MRH empirical tests to control for the SAE's built-in convex constraint; e.g., compare AA fitting quality against standard (unconstrained) SAE atoms to see whether the constraint drives the result.
- Clarify the relationship between MRH and LRH more formally; specifically, show under what conditions LRH features can be recovered as limiting cases of MRH landmarks, which would position MRH as a proper generalization rather than a replacement.

---

## Score and Decision

The paper makes solid, reproducible empirical contributions in Sections 3–4 that stand on their own. The "Elsewhere" concept finding, the three-family depth cue analysis, and the geometric characterization of the learned dictionary all advance understanding of DINOv2 in concrete ways. The MRH framework is a thought-provoking working hypothesis, and the paper is appropriately transparent about its preliminary nature. However, the theoretical centerpiece (Proposition 1) is essentially tautological, the circularity between the SAE construction and the MRH evidence is not resolved, and the empirical MRH tests are too weak to bear the weight of the proposed implications. These are real limitations but do not invalidate the empirical contributions.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>