Now I have sufficient calibration. Let me finalize my assessment. Here's my bracket:

**Round 1 bracket:** 5.5–7.5 based on comparison with weak anchors (2.5–3.4) and strong anchors (8.0+).

**Round 2 narrowing:** 6.0–7.0. The 6.50 SAE-on-CLIP paper is clearly weaker (less content, narrower scope). The 6.75 "Representation Geometry" paper has a tighter thesis and better theoretical support but less empirical breadth. The 7.50 "Geometric Inductive Biases" paper is clearly stronger. This paper lands close to the 6.75 anchor — comparable in ambition but with a more speculative central thesis.

**Final score: 6.5.** The paper has genuine empirical contributions (large concept dictionary, task-specific analysis, clean PCA observations), but the MRH — presented as a headline contribution — is not yet sufficiently substantiated. The evidence for MRH specifically (vs. other geometric accounts) is preliminary, and the SAE used for analysis has inductive biases that interact with the convex-geometry claims.

---

## Summary

This paper trains a stable sparse autoencoder (RA-SAE) on DINOv2 to extract a 32,000-concept dictionary — the largest interpretability resource for a vision foundation model to date. Using this dictionary, the authors analyze how classification, segmentation, and depth estimation recruit distinct, low-dimensional subsets of concepts, identifying specific concept families: "Elsewhere" negation concepts, border detectors, and three families of monocular depth cues. They examine the geometry and statistics of the concept space, finding higher coherence and anisotropic capacity than expected under a purely sparse, near-orthogonal Linear Representation Hypothesis. Motivated by these departures, as well as smooth per-image PCA structure on raw token embeddings, they propose the Minkowski Representation Hypothesis (MRH): tokens behave as Minkowski sums of convex polytopes spanned by archetypal landmarks, a geometry naturally realized by multi-head attention.

## Strengths

- **Large-scale, publicly released concept dictionary.** The 32,000-atom RA-SAE achieves R² > 88% reconstruction on DINOv2-B activations, providing the largest interactive interpretability resource for a vision foundation model. The dictionary is accompanied by a promised interactive visualization tool. This is a genuine infrastructure contribution to the interpretability community.

- **Concrete, interpretable concept families per task.** The identification of "Elsewhere" concepts (Figure 2, left) — which fire off-object and vanish when the object is causally masked — is a clear, specific finding with causal support. The border concepts for segmentation (Figure 2, right; Figure 10) and three families of monocular depth cues (projective, shadow-based, frequency transitions; Figure 3) provide testable structural claims about what DINOv2 encodes and how tasks recruit it.

- **Compelling model-native PCA analysis (Section 5).** The per-image PCA maps (Figure 5) show smooth, semantically aligned token trajectories connecting a small set of extremal points — observed directly on raw DINOv2 token embeddings, not through the SAE lens. The thorough positional subspace analysis (Figure 6, Figure 24, Figure 25) demonstrates that positional information collapses to a low-dimensional sheet and that removing it does not destroy the smooth PCA structure. This is clean, well-executed, and provides model-native evidence for interpolative geometry.

- **Rich empirical characterization of concept space geometry.** The dictionary diagnostics (Figure 4) — heavier-tailed pairwise similarities vs. random/Grassmannian baselines, sharp singular-value decay, low Hoyer scores, smoothly decaying co-activation spectrum — provide a detailed picture that usefully complicates the simple sparse-coding view. The task-specific subspace analysis (Figure 11) showing that intra-task concepts are more aligned and have faster-decaying eigenspectra is particularly informative.

- **Well-organized narrative and clear writing.** The paper unfolds in a logical progression: operationalize LRH → discover task-specific concept usage → observe geometric departures → examine model-native token geometry → propose MRH as a synthesizing hypothesis. The exposition is clear and the figures are informative.

## Weaknesses

### Fatal

None.

### Major

- **SAE inductive bias interacts with MRH claims.** The RA-SAE enforces that dictionary atoms lie in the convex hull of real activations (D ∈ conv(A)), uses non-negativity constraints on codes (Z ≥ 0), and parametrizes D via a row-stochastic matrix. These constraints inherently bias the discovered representation toward convex-combination structure. While Section 5 provides model-native evidence (PCA on raw tokens), the key MRH empirical tests (k-NN geodesics, Archetypal Analysis reconstruction, code Gram block structure; Figure 26) and much of the geometry analysis (Figure 4) all operate on SAE-derived representations. The paper does not include ablation experiments — e.g., varying the SAE design, testing on alternative dictionary learning methods, or verifying that key geometric properties hold in the raw activation space — that would allow a reader to separate SAE artifacts from model-native geometry. This matters because the SAE is the instrument through which the paper discovers structure it then attributes to DINOv2.

- **MRH is presented as a headline contribution but the evidence is preliminary.** The paper's title invokes "Minkowski Geometry" and Section 6 presents MRH as a culminating contribution. Yet the three empirical tests (Figure 26) are described only qualitatively and are consistent with many geometric accounts — prototype-based models, sparse coding with non-orthogonal atoms, generic low-dimensional manifolds — not uniquely with Minkowski sums of convex polytopes. Proposition 1 is an observation about attention mechanics (which the paper itself calls "elementary," line 175) rather than a restriction on how concepts are actually encoded. The paper would be substantially stronger if MRH were positioned as a forward-looking discussion point that synthesizes the empirical findings, rather than as a central claim whose evidence is not yet discriminating. As written, there is a mismatch between the strength of the framing and the strength of the supporting evidence.

### Minor

- **Depth cue analysis is qualitative and correlational.** The three monocular cue families (Figure 3) are identified via hand-picked perturbation types (median blur, high-pass filter, edge-preserving smoothing) and UMAP clustering. There is no causal test showing that perturbing these concept clusters actually changes depth predictions, nor a demonstration that the clusters independently predict depth outputs. The analysis is suggestive and valuable as exploration, but it remains at the level of observation rather than mechanism.

- **Co-activation/geometry correlation analysis has a built-in confound.** The paper reports a weak correlation between the co-activation matrix Z^T Z and geometric affinity DD^T (Figure 13) as evidence that co-occurrence does not strongly shape geometry. However, as the paper's own footnote (line 137) notes, this correlation is algebraically related to the trace of the activation covariance and is guaranteed positive — making it an unreliable metric for the claimed independence. The conclusion that "usage influences geometry but is not the dominant organizing principle" may be overstated relative to what this particular metric can support.

- **Proposition 1 provides limited explanatory power.** The result that multi-head attention outputs are Minkowski sums of convex sets follows directly from the definition of attention (convex combination per head, summation across heads). The paper acknowledges this (line 175). While the connection between architecture and MRH is worth noting, it does not constitute a theoretical result that constrains or predicts representational structure.

### Trivial

None.

## Nice-to-Haves

- A causal test for the depth cue families: ablate concept activations corresponding to each family and measure the effect on depth prediction quality. This would transform the depth cue analysis from correlational to mechanistic.
- A control experiment training an SAE without the convex-hull constraint (or with a standard ℓ₁ sparsity penalty) and comparing the resulting geometric properties (coherence, spectrum, k-NN geodesics) to assess how much of the observed structure is SAE-induced.
- A more extensive comparison of MRH against competing geometric accounts — e.g., showing that a prototype-based model or a sparse-directional model cannot reproduce specific patterns that MRH predicts.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Alignment metric deferred to appendix — cannot judge."** REMOVED. The appendix is stripped by the parser; this is a review-process limitation, not an author error.
- **"UMAP visualizations distort global structure."** REMOVED as a standalone criticism. The paper explicitly notes this limitation in the Figure 1 caption ("Although UMAP only preserve local geometry"). The authors use UMAP appropriately as a visualization tool, not as a quantitative metric.
- **"Grassmannian baseline (TAAP algorithm) not explained in main text."** REMOVED. The paper references Massion & Massart (2025) and notes details are in Appendix F, which is standard practice. This is not a substantive weakness.
- **"Proposition 1 adds no force to MRH as a representation hypothesis."** REMOVED as overstated. The connection between attention architecture and MRH is a legitimate observation, even if elementary. Moved to Minor with appropriate framing.
- **"Non-identifiability result is well-known."** REMOVED. Even if the mathematical fact is known in convex geometry, applying it to interpretability (showing that single-layer concept extraction is underdetermined) is a valid contribution. The paper uses it to motivate structure-aware interpretability tools.
- **"Interactive demo not available to reviewers."** REMOVED per hard rules: the paper promises release upon acceptance. This is not a valid criticism.
- **"LRH does not strictly predict zero coherence or flat spectrum."** REMOVED. The paper doesn't claim LRH predicts zero coherence — it treats LRH as an idealized baseline and shows departures from it. This is a reasonable comparative approach.
- **"SAE stability not backed by quantitative comparisons across runs."** REMOVED. The paper references prior work (Fel et al., 2025) establishing RA-SAE stability. Reproducing those stability experiments is not necessary for this paper's contribution.
- **"The paper does not discuss effect of using only ImageNet-1K for dictionary training."** REMOVED. This is a scope-expansion request. 1.4M ImageNet-1K images is a substantial and standard dataset for vision model analysis.

## Novel Insights

The most genuinely novel contribution is the combination of a large-scale concept dictionary with task-specific functional analysis, revealing that different downstream tasks (classification, segmentation, depth) recruit distinct, low-dimensional subspaces with identifiable concept families. The "Elsewhere" concept — a conditional negation mechanism that fires off-object yet depends on the object's presence — is a concrete, causally supported finding that challenges standard attribution assumptions and suggests a specific functional role for what might otherwise be dismissed as background features. The per-image PCA analysis showing smooth interpolative token geometry that persists after removing positional information is a clean, model-native observation that independently motivates geometric accounts beyond pure sparse coding.

## Suggestions

- The paper would benefit from reframing: either (a) strengthen MRH with discriminating experiments that test predictions unique to Minkowski geometry (e.g., piecewise-linear surfaces with formally flat faces in token space, saturation behavior predicted by convex cell boundaries), or (b) reposition MRH as a discussion-section synthesis while elevating the concept dictionary, task analysis, and PCA observations as the primary contributions. Option (b) would better align claims with evidence and is likely lower-risk.
- Add a minimal causal test for the depth cue families: ablate each cluster's concepts and measure depth prediction change.
- Include an ablation varying the SAE design (e.g., removing the convex-hull constraint) to bound how much of the observed geometric structure is SAE-induced vs. model-native.
- Clarify in the text that the co-activation/geometry correlation metric (Section 4, Figure 13) has the built-in confound identified in the footnote, and temper the conclusion accordingly.

## Score and Decision

**Anchor comparison:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| `Wxl0JMgDoU` (SAE for chess skill) | 2.50 | R1 | Much weaker: narrow domain, limited contributions |
| `89wVrywsIy` (Hierarchical Tracing SAE circuits) | 3.40 | R1 | Weaker: less empirical breadth, less novel findings |
| `UbLvSPMvMA` (Cosine Loss for sparse binary) | 1.67 | R1 | Much weaker |
| `ghH6YYDs15` (Compute Optimal Inference SAE) | 4.67 | R1 | Weaker: synthetic-heavy, limited real-model experiments |
| `Ch8s4FdUXS` (SAE for SDXL Turbo) | 4.40 | R1 | Weaker: narrower scope |
| `bkdWThqE6q` (Interpretable Transformer) | 6.00 | R2 | Weaker: single-method, narrower contribution |
| `imT03YXlG2` (SAE on CLIP adaptation) | 6.50 | R1/R2 | Weaker: less content, less analysis depth |
| `vogtAV1GGL` (Simple mechanisms for concepts) | 5.75 | R2 | Weaker: less empirical grounding |
| `bVTM2QKYuA` (Representation Geometry LLMs) | 6.75 | R2 | Comparable: tighter thesis, better theory; our paper has more empirical breadth but less theoretical rigor |
| `9ca9eHNrdH` (SAEs Not Canonical) | 7.00 | R1 | Slightly stronger: crisper thesis, well-executed experiments |
| `cmXWYolrlo` (Geometric Inductive Biases) | 7.50 | R2 | Stronger: clear hypothesis, strong theory, extensive experiments |
| `tcsZt9ZNKD` (Scaling SAEs) | 8.20 | R1 | Much stronger: definitive contribution |
| `I4e82CIDxv` (Sparse Feature Circuits) | 8.00 | R1 | Much stronger |
| `2dnO3LLiJ1` (Vision Transformers Need Registers) | 8.00 | R1 | Much stronger |

The paper sits between the 6.50 and 6.75 anchors: stronger than the CLIP SAE adaptation paper (more content, more analysis depth, larger resource) but slightly weaker than the Representation Geometry paper (less theoretical rigor, more speculative central thesis). The empirical contributions — particularly the concept dictionary, task analysis, and per-image PCA observations — are substantial and well-executed, but the MRH is presented too prominently relative to the strength of its supporting evidence.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>