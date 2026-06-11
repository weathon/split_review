Now I have a clear picture. Let me finalize the review.

**Round 2 comparisons:**
- vs. uDIiL89ViX (5.60): Our paper is clearly stronger — more ambitious scope, richer empirical findings, Grassmannian baselines.
- vs. ih3BJmIZbC (6.80): Our paper delivers more concrete findings and a theoretical hypothesis. Comparable or slightly stronger.
- vs. chanJGoa7f (7.00): Similar quality. Our paper is more ambitious but less coherent; the VLM paper is cleaner but narrower.

**Bracket narrowing:** The paper lands between 6.5–7.0. The unresolved SAE/MRH tension and under-evidenced MRH hypothesis pull the score down from where the empirical contributions alone would place it. I'll assign **6.5**.

---

## Summary
This paper operationalizes the Linear Representation Hypothesis (LRH) in DINOv2 using a stable sparse autoencoder (RA-SAE) to extract a 32,000-concept dictionary, then analyzes (1) how downstream tasks recruit concepts — revealing "Elsewhere" negation concepts for classification, border detectors for segmentation, and three monocular depth cue families — (2) concept geometry statistics showing systematic departures from pure LRH via Grassmannian-baselined comparisons, and (3) proposes the Minkowski Representation Hypothesis (MRH) where token embeddings lie in Minkowski sums of convex polytopes, grounded architecturally in multi-head attention (Proposition 1). The dictionary and an interactive visualization are released.

## Strengths
- **Controlled perturbation design for depth cue decomposition.** The paper applies targeted image perturbations (median blurring to remove shadows, edge-preserving smoothing to preserve contours, high-pass filtering to emphasize projective geometry) and reveals three functionally distinct concept clusters — projective geometry, shadow-based, and frequency-transition concepts (Figure 3; Section 3). This goes beyond passive correlation to causal decomposition.
- **Rigorous Grassmannian-baselined geometry analysis.** Rather than merely observing non-orthogonality, the paper benchmarks dictionary geometry against random and Grassmannian frames (via the TAAP algorithm), showing heavier-tailed pairwise inner products and sharply decaying singular values in D (Figure 4, Section 4). Grassmannian frames mathematically minimize mutual coherence, making this a principled baseline that makes observed departures from LRH quantitatively meaningful.
- **Clean separation of positional from semantic token structure.** Section 5 shows positional information compresses to a 2D sheet in final layers (Figure 6) and that projecting tokens orthogonal to the positional subspace leaves per-image PCA structure largely unchanged. This directly rules out the alternative explanation that smooth token geometry is purely positional.
- **Architectural grounding of MRH through Proposition 1.** The paper demonstrates that multi-head attention — headwise convex combinations summed across heads — directly constructs Minkowski sums. This connects the proposed geometry to the transformer mechanism rather than treating MRH as an external metaphor.
- **Large-scale, reproducible resource.** The 32,000-concept dictionary with R² > 88% reconstruction fidelity using the stable RA-SAE variant is a substantial engineering contribution with commitment to public release of both dictionary and interactive visualization.

## Weaknesses

### Fatal
None.

### Major
- **MRH empirical evidence is preliminary relative to its centrality.** The paper's most ambitious contribution is the Minkowski Representation Hypothesis, positioned as one of three pillars of the contribution (abstract, Section 6). Yet the empirical support (lines 163–164, Fig. 26) consists of three experiments described at a qualitative level: a k-NN geodesic vs. linear interpolation comparison, an Archetypal Analysis vs. SAE reconstruction comparison, and observation of block structure in code Grams. The interpolation result is described as "only the latter remain near the data support" without distance metrics or statistical testing; the AA result states "matches or exceeds SAE reconstruction" without reporting actual reconstruction values or image counts; the block structure claim has no null distribution. While the paper appropriately calls MRH a "working hypothesis," the evidence presented cannot distinguish it from several alternative geometric descriptions. For a paper that places MRH alongside the empirical concept atlas as a co-equal contribution, this evidential gap is significant.
- **Unresolved tension between SAE methodology (built on LRH) and MRH thesis.** Sections 2–4 depend entirely on SAEs — an operationalization of LRH — to extract concepts and analyze task usage and geometry. But Section 6 argues the LRH picture is inadequate and proposes convex-region geometry instead. If MRH holds, the SAE-derived concept dictionary that underpins the entire task analysis (Section 3) may be a mis-specified decomposition. The paper never directly addresses this structural tension: the "Elsewhere," "border," and "depth cue" concept interpretations are all artifacts of an LRH-based method, and under MRH their interpretation could change fundamentally. The paper acknowledges this obliquely in the Discussion (line 177: "if true, extracting concepts from single layers is insufficient") but does not resolve it or discuss the conditions under which SAE-derived concepts remain meaningful under MRH.

### Minor
- **Single-layer, single-model scope.** The analysis is confined to one layer of DINOv2-B. Whether findings generalize across layers, model scales, or architectures (DINOv1, CLIP, MAE) is unexplored. This limits claims about how DINOv2 represents in general.
- **Proposition 1 formalizes existing architectural knowledge.** That attention heads compute convex combinations and multi-head summation yields a Minkowski sum is definitionally true of the transformer architecture. The proposition usefully formalizes this, but it demonstrates architectural *capability* rather than confirming that learned representations actually organize according to MRH. The gap between "can realize" and "does realize" remains the central empirical challenge.
- **Causal evidence for "Elsewhere" concept interpretation is preliminary.** The paper appropriately hedges: "providing evidence suggestive of a causal effect" (Figure 2 caption, line 51). Given how prominently this finding is featured (abstract, Figure 2, Section 3), readers should be aware the causal claim is not settled. The paper correctly signals this uncertainty, but the interpretive weight placed on the finding exceeds the current evidence.
- **The task-alignment score methodology is not presented in the main text.** The alignment-score computation that underpins Section 3's quantitative claims (top-100 concepts, spectrum comparisons, Figure 11) is deferred to Appendix C.1, making these claims difficult to evaluate from the main body alone.
- **No baseline concept extraction method.** Comparing SAE-derived concepts against alternative decomposition methods (e.g., PCA, k-means on activations, or a non-sparse autoencoder) would strengthen the claim that SAE-derived concepts are genuinely more interpretable or functionally meaningful rather than just different.

### Trivial
- The Discussion (Section 7) reads primarily as a summary rather than engaging with limitations, methodology trade-offs, or concrete paths forward.
- The claim that findings have "immediate relevance for the substantial body of research and applications that depend on DINOv2 representations" (line 179) is vague and unsupported by concrete examples in the text.

## Nice-to-Haves
- Human validation of concept interpretability would substantially strengthen the qualitative claims about "Elsewhere" and "border" concepts.
- Studying multiple layers rather than a single one would broaden the contribution and test whether the observed patterns are layer-specific.
- For MRH: quantitative reconstruction comparisons with null baselines, explicit falsification tests, and concrete predictions that an LRH model would get wrong.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Harsh Critic Issue 3 (Definition 1 not falsifiable):** REMOVED. The three conditions (Minkowski sum structure, block-convex codes, block-structured Grams) are concrete and testable; condition (iii) is directly tested in Fig. 26. The claim that the definition offers no falsification conditions is incorrect — violating any of the three conditions would count against MRH.
- **Strength Finder overstatement about "causally verified" Elsewhere concepts:** MODERATED. The paper uses hedging language ("suggestive"), not "verified." Moved to Minor weakness reflecting the appropriate uncertainty level.

## Novel Insights
None beyond the paper's own contributions. The review process did not surface insights not already present in the paper.

## Suggestions
- Add an explicit section or paragraph addressing the SAE/MRH methodological tension: under what conditions do SAE-derived concepts remain meaningful if MRH holds? This would substantially improve the paper's internal coherence and could be addressed in rebuttal.
- Provide quantified metrics (not just qualitative descriptions) for the three MRH experiments referenced in Section 6, even if relegated to the appendix.
- Consider either deepening the MRH evidence to match its prominence in the paper, or repositioning MRH as a speculative hypothesis with architectural motivation while letting the empirical concept atlas carry the primary contribution.

---

## Calibration Anchor Summary

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| wZiH43e5Ah (CAN concept extraction) | 3.00 | R1 | Our paper substantially stronger — more rigorous methodology, broader scope, Grassmannian baselines |
| fmWVPbRGC4 (Local vs distributed) | 5.67 | R1 | Our paper more ambitious — richer empirical findings across three tasks plus theoretical hypothesis |
| uDIiL89ViX (Dictionary learning microscopy) | 5.60 | R2 | Our paper clearly stronger — more systematic analysis, better baselines, more novel contributions |
| ih3BJmIZbC (RSVC representational similarity) | 6.80 | R2 | Comparable quality; our paper delivers more concrete findings but has a structural tension RSVC doesn't |
| chanJGoa7f (Interpreting VLMs) | 7.00 | R2 | Similar quality level; VLM paper is cleaner and more coherent, our paper is more ambitious but less resolved |
| GjfIZan5jN (Enhancing classifiability) | 7.33 | R2 | Stronger than our paper — more polished, coherent, with clearer methodology-to-claims mapping |
| 5Ca9sSzuDp (CLIP decomposition) | 8.00 | R1 | Substantially stronger — polished, coherent, clear applications, no structural tensions |

**Round 1 bracket:** 5.5–7.5. **Round 2 narrowing:** 6.5–7.0. The paper's empirical contributions (task-specific concept analysis, Grassmannian-baselined geometry diagnostics, controlled perturbation design) are strong and place it above the 6.0 range. But the under-evidenced MRH hypothesis and the unresolved SAE/MRH methodological tension prevent it from reaching the 7.0+ range where papers with more coherent contributions sit. **Final: 6.5.**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>