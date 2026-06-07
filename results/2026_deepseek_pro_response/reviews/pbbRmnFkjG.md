Now I have a clear picture. Let me finalize the review.

**Bracket analysis:**

The paper under review sits between the 4.75 anchor (ViT visualization — limited novelty, borrowed methods, isolated findings) and the 6.50 anchors (PatchSAE on CLIP and SAE Match — focused, well-executed, but narrower scope). Our paper's SAE deployment and geometric analysis are clearly stronger than the 4.75 anchor — larger scale, more rigorous baselines, causal evidence, and a genuine theoretical contribution. But the paper is weaker than the 6.50 anchors in one critical respect: the central theoretical claim (MRH) is under-supported and the paper itself presents it as a "working hypothesis." The PatchSAE paper (6.50) delivers fully on its more modest claims; our paper promises MRH in the title but only delivers preliminary evidence for it. This mismatch between ambition and evidence pulls the score down.

**Final score: 5.5**

---

## Summary
This paper extracts a 32,000-concept dictionary from DINOv2 using a stabilized sparse autoencoder (SAE) and uses it to analyze task-specific concept recruitment across classification, segmentation, and depth estimation. The SAE-based geometric diagnostics reveal departures from the strict Linear Representation Hypothesis (LRH), motivating the authors to propose the Minkowski Representation Hypothesis (MRH): token embeddings are Minkowski sums of convex polytopes around archetypal landmarks, a geometry constructively realized by multi-head attention (Proposition 1). The paper offers qualitative discoveries about task-specific concepts, rigorous geometric characterization benchmarked against Grassmannian baselines, and a formal architectural grounding for MRH, while acknowledging MRH as a working hypothesis with preliminary evidence.

## Strengths
- **Large-scale, well-grounded SAE deployment**: 32k-concept dictionary from DINOv2 using a stabilized SAE (Fel et al., 2025) with convex-hull constraints, achieving R² > 88% reconstruction. The scale and operational care (convex-hull anchoring, k-means centroid approximation, BatchTopK projection) are substantial.
- **Causal perturbation evidence for "Elsewhere" concepts**: Classification concepts that fire off-object are shown to vanish when the object is removed via causal masking (line 79, Figure 2), establishing conditional dependence rather than trivial background correlation.
- **Controlled perturbation experiments isolate three families of monocular depth cues**: Targeted image-space perturbations (median blurring, edge-preserving smoothing, high-pass filtering) reveal functionally distinct clusters — projective geometry, shadow-based, and frequency-transition cues (Section 3, Figure 3) — providing strong evidence for interpretable 3D primitives emerging without explicit 3D supervision.
- **Rigorous geometric diagnostics against proper baselines**: Dictionary coherence, singular value spectra, and Hoyer scores are benchmarked against both random baselines and Grassmannian frames generated via the TAAP algorithm (Section 4, Figure 4), elevating geometric claims beyond qualitative description.
- **Orthogonal projection cleanly rules out position as the explanation for smooth token geometry**: Linear decoders for token coordinates extract a positional subspace, and PCA structure is preserved after orthogonal projection (Section 5). Positional subspace compression from high-rank to ~2D across layers is documented (Figure 6).
- **Proposition 1 provides a crisp architectural grounding for MRH**: The formal connection that each attention head outputs a convex combination of values and multi-head summation yields a Minkowski sum is an elementary but non-obvious bridge between Transformer architecture and representational geometry.

## Weaknesses

### Fatal
None.

### Major
- **MRH empirical support is preliminary and title-central**: The three empirical tests for MRH (k-NN geodesics, Archetypal Analysis vs SAE reconstruction, block structure in code Grams) are described in a single paragraph (line 163) referencing Figure 26 in the stripped appendix. The paper labels MRH as a "working hypothesis" (abstract, line 9) and prefaces implications with "if, and this is an assumption, the Minkowski Representation Hypothesis holds" (line 165). The title centers MRH, but the evidence does not yet distinguish it from alternative geometric models. The AA reconstruction matching SAE with ~10 archetypes per image is consistent with many low-dimensional geometries, not specifically MRH.
- **The SAE-based task analysis does not directly support MRH**: The paper's argument structure connects its parts indirectly — the SAE analysis identifies departures from LRH, and these motivate MRH. But the task-specific findings (Elsewhere concepts, border detectors, depth cue families) are observations about *which* concepts exist, not about the geometric regime in which they are organized. The SAE analysis and the MRH proposal remain somewhat distinct contributions bundled together rather than a single integrated argument.

### Minor
- **Task-specific concept analysis is largely qualitative**: The three headline findings of Section 3 are presented through examples and visualizations without systematic quantification (what fraction of top-k concepts fall into each category, consistency across images/classes). The alignment score used to rank concepts by task importance is deferred to Appendix C.1 (stripped), so the reader cannot evaluate its definition. The paper includes some quantitative analysis (Figure 11 for task concept spectra), but the specific qualitative categories are not quantified.
- **Section 5 stops at ruling out position without testing the proposed mechanism**: The paper gestures toward DINO/iBOT prototype assignments as a mechanism for the observed PCA structure (line 137) but does not test whether prototype assignments actually explain the smooth token geometry.

### Trivial
- The discussion section (Section 7) is largely a restatement of findings and does not grapple substantively with limitations, alternative interpretations, or open questions.

## Nice-to-Haves
- Systematic quantification of task-specific concept categories (fraction of top-50 concepts that are "Elsewhere," how this varies across classes).
- Testing whether DINO/iBOT prototype assignments explain the PCA structure observed in Section 5.
- SAE stability analysis across multiple training runs.
- A clearer statement of what would falsify MRH and distinguish it from relaxed LRH and other geometric models.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"Proposition 1 is definitional, not a discovery"** — The harsh critic argues MRH is merely a restatement of Transformer architecture. While Proposition 1 does formalize an architectural property, the contribution is in making the connection between that property and a representational hypothesis. The paper does not claim to have "discovered" that attention outputs convex combinations; it claims this architecture *realizes* MRH. This is a valid theoretical bridge, not a flaw.
- **"Three parts do not cohere into a single argument"** — The paper's structure is: SAE enables task and geometry analysis → geometry analysis reveals departures from LRH → departures motivate MRH. This arc is stated explicitly (lines 34-35, 177). The connection is present, even if the SAE findings do not directly test MRH. The looseness concern is captured under Major Weakness 2.
- **"LRH is set up as a strawman"** — The paper operationalizes LRH using Grassmannian frames (line 41) drawn from the cited literature (Park et al., 2024; Elhage et al., 2022). It also acknowledges that some diagnostics are "compatible with a linear sparse-coding view" (line 34). This is a comparison against a formal baseline, not a strawman.
- **"The paper provides no evidence its own SAE is stable"** — The paper cites Fel et al. (2025) for the stabilized SAE method and reports R² > 88%. Additional stability runs would strengthen the paper but claiming "no evidence" is incorrect.
- **"Causal masking never described in the main text"** — The main text (line 79) states "they vanish if the object is removed" and Figure 2 caption cites Petsiuk et al. (2018). The description is present, though brief.
- **"k=8 choice stated without justification"** — This is a standard hyperparameter choice. Justification would be nice but its absence is not a substantive flaw.
- **"The Discussion is a summary, not a genuine discussion"** — This is a presentation preference, already noted under Trivial.
- **"The paper would benefit from a limitations section"** — The paper notes the single-architecture limitation (line 179). Additional limitations discussion would help but is not a flaw.

## Novel Insights
The paper's most novel observation is the formal connection in Proposition 1 — that multi-head attention constructively realizes Minkowski-sum geometry — which bridges architectural mechanism and representational structure in a way that is both elementary and previously unarticulated. The empirical finding that concept geometry (DD^T) correlates only weakly with co-activation (Z^T Z) is also a genuine discovery about the organizing principles of learned dictionaries, suggesting that usage patterns are not the dominant force shaping representational geometry.

## Suggestions
- The paper would benefit from committing more clearly to its primary contribution. The strongest version is the SAE empirical study with MRH as a motivated interpretive lens in the discussion, rather than as a co-equal contribution centered in the title.
- If the authors want to center MRH, they should move the empirical MRH tests (Figure 26) into the main paper and derive predictions that distinguish MRH from relaxed LRH, not just from idealized LRH.
- Add systematic quantification to the task-specific concept categories in Section 3 (fraction of top-k concepts per category, consistency across images, sensitivity to SAE hyperparameters).

## Anchor Comparisons
- **4aJg9e4nvF** (4.75, Round 2): ViT visualization study. Our paper is clearly stronger — larger scale, more rigorous baselines, causal evidence, theoretical contribution.
- **89wVrywsIy** (3.40, Round 1): Hierarchical tracing with SAEs. Our paper is clearly stronger — more comprehensive evaluation, proper baselines, theoretical grounding.
- **imT03YXlG2** (6.50, Rounds 1 & 2): PatchSAE on CLIP. Most comparable. Our SAE work is more comprehensive (larger dictionary, more tasks, more rigorous geometry), but the MRH claim is under-supported relative to this anchor's more modest and fully-delivered claims. Our paper is slightly weaker overall.
- **MDvecs7EvO** (6.50, Round 2): SAE Match for cross-layer feature alignment. Focused, well-executed method paper. Our paper is more ambitious in scope but less focused. The under-supported MRH claim puts our paper slightly below this anchor.
- **I4e82CIDxv** (8.00, Round 1): Sparse Feature Circuits. Our paper is clearly weaker — less thorough evaluation, no practical downstream application, central claim under-supported.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>