## Summary

This paper trains a stable sparse autoencoder (SAE) on DINOv2-B with 4 registers to extract a 32,000-atom concept dictionary, claimed as the largest interpretability demonstration for a vision foundation model. Using this dictionary, the authors analyze how downstream tasks (classification, segmentation, depth estimation) recruit concepts, revealing functional specialization including "Elsewhere" concepts for classification (conditional negation), border concepts for segmentation, and three families of monocular depth cues (projective, shadow-based, frequency transitions). The geometric characterization reveals departures from the idealized near-orthogonal structure assumed by the Linear Representation Hypothesis (LRH). Motivated by these departures, the paper proposes the *Minkowski Representation Hypothesis (MRH)* as a working hypothesis: token embeddings behave as Minkowski sums of convex regions around archetypal landmarks, with multi-head attention constructively realizing this structure (Proposition 1).

## Strengths

1. **Scale of interpretability analysis**: The 32,000-atom SAE dictionary for DINOv2 is the largest such demonstration for a vision foundation model, with well-specified training details (c=32,000 atoms, k=8 active codes, R²>88% reconstruction, line 57). This concretely advances beyond prior SAE-based studies that were predominantly on language models or smaller-scale vision analyses.

2. **Novel discovery of "Elsewhere" concepts**: The identification of concepts that fire off-object yet depend on the object's presence, vanishing under causal masking (line 79, Figure 2), is a non-trivial finding about how DINOv2 supports classification. This goes beyond identifying simple object-part detectors and suggests a form of learned conditional negation.

3. **Systematic isolation of three monocular depth cue families**: The perturbation-based methodology (median blurring for shadows, edge-preserving smoothing for contours, high-pass filtering for projective geometry) to functionally decompose depth-supporting concepts into three families (Section 3, lines 83-93, Figure 3) is creative and links DINO's internal features to known visual neuroscience principles.

4. **Rigorous geometric characterization with baselines**: The comparisons against both random and Grassmannian baselines (Figure 4) — heavier-tailed inner products, sharper singular-value decay, task-aligned anisotropy — provide quantitative evidence that DINO's concept space departs from the idealized sparse-coding view. The weak correlation between co-activation and geometric similarity (lines 97-107) is a genuinely interesting empirical finding.

5. **Controlled ablation of positional confounding**: The analysis training linear decoders to predict token coordinates, isolating a positional subspace, and then showing that PCA structure persists after projecting it out (Section 5, lines 119-136, Figure 25) actively rules out the simplest confound for the observed token geometry.

6. **Formal theoretical grounding for MRH**: Proposition 1 (lines 155-159) cleanly shows that multi-head attention (headwise convex combinations summed across heads) constructively realizes a Minkowski sum structure. Proposition 2 (lines 167-170) provides a useful non-identifiability result with practical implications for interpretability tool design.

## Weaknesses

### Major

1. **The Minkowski Representation Hypothesis is over-represented relative to its evidentiary support.** While the paper honestly calls MRH a "working hypothesis" in the abstract and discussion, it appears in the paper's title, is listed as a core contribution (line 31), and is the declared destination of the paper's narrative arc. The main-text empirical evidence for MRH consists of three sentences (line 163) referencing three tests (k-NN geodesics, Archetypal Analysis vs. SAE reconstruction, block structure in code Gram matrices) — all pointing to appendix figures with no quantitative values reported in the main body. The theoretical connection (Proposition 1) is insightful, but the empirical validation is too thin for the prominence the hypothesis receives. This creates a mismatch between the paper's packaging and its evidentiary content. The paper's SAE dictionary and task analyses stand independently, but the MRH framing inflates the contribution beyond what is demonstrated.

### Minor

2. **"Elsewhere" concept interpretation is qualitatively compelling but quantitatively thin.** The claim that Elsewhere concepts implement "conditional negation" with a "causal effect" (line 79: "they vanish if the object is removed, indicating a conditional negation") is based on a qualitative observation. No numerical comparison of activation magnitudes before/after masking, no sample size, and no statistical test are reported. The paper does acknowledge an alternative interpretation ("distributed off-object evidence") in a parenthetical in the figure caption, but the main text and abstract (line 9: "classification exploits 'Elsewhere' concepts that implement 'object negation'") present the stronger interpretation as settled. This would benefit from quantitative grounding — at minimum reporting mean activation differences and effect sizes across many images/classes.

3. **No quantitative overlap measure for task-specific concept sets.** The paper states tasks recruit "different subsets" with "minimal overlap" (line 33) and quantifies that "classification draws from a broader span of the dictionary" (line 65), but no Jaccard similarity or similar metric between the top-k task-specific concept sets is reported. This leaves the "functional specialization" claim less precise than it could be.

4. **Tension between SAE analysis and MRH is acknowledged but not grappled with in the empirical sections.** Proposition 2 shows that under MRH, the SAE decomposition of activation space is one of infinitely many possible factorizations — the concepts extracted are non-identifiable from final activations alone. The discussion (line 177) notes this, but the empirical sections do not address whether specific findings (e.g., Elsewhere concepts, depth cue families) could be artifacts of the SAE's particular factorization rather than genuinely reflecting DINOv2's internal computation.

### Trivial

None.

## Nice-to-Haves

- The depth perturbation analysis would benefit from a control condition (e.g., color jitter) that should not affect depth estimation, to confirm that observed clusterings reflect genuine depth cue specialization rather than sensitivity to different image distortion types.
- Reporting confidence intervals or bootstrap estimates for the geometric comparisons against random and Grassmannian baselines would strengthen the statistical claims.
- Including key numbers from the MRH empirical tests in the main text (e.g., "AA with ~10 archetypes achieves reconstruction R² of X% vs. SAE's Y%") would help readers assess the evidence without having to locate the appendix.

## Removed Points

*These points were flagged by the reviews but removed after verification against the paper, with reasoning.*

- **Task-alignment metric definition deferred to appendix (Harsh Critic)**: The paper transparently defers the metric to Appendix C.1 (line 63). The appendix is present in the original submission; the parser strips it. Per instructions, this criticism is removed.
- **"No statistical significance for geometric comparisons" (Harsh Critic)**: The paper provides clear visual evidence against baselines (Figure 4) with appropriate methodology. While confidence intervals would strengthen the claims, the presentation as-is is standard for empirical analysis papers. Moved to Nice-to-Haves.
- **Strength about MRH "empirical tests" (Strength Finder)**: The claim that "Empirical tests of MRH against data" is a core strength overstates what is demonstrated. The tests are preliminary and referenced only to appendix figures. This strength conflicts with verified weakness #1 and is removed.

## Novel Insights

The most interesting synthesis from the reviews is the structural tension between the paper's two main contributions. The SAE-based analysis operationalizes LRH and produces a concrete, visually interpretable dictionary. The MRH proposal, however, implies that such a decomposition is fundamentally non-identifiable (Proposition 2). The paper acknowledges this but does not engage with the practical consequence: could the specific findings about Elsewhere concepts, border concepts, and depth cue families be artifacts of the SAE's inductive biases rather than faithful reflections of DINOv2's computation? This tension, if developed, could point toward a more nuanced understanding of what SAE-based interpretability actually recovers — a theme that connects to ongoing debates in the mechanistic interpretability community.

## Suggestions

1. Strengthen the "Elsewhere" concept analysis with quantitative measurements: report mean activation on-object vs. off-object across N images and M classes, with and without causal masking, including effect sizes and variability across classes.
2. Either (a) tone down the MRH's prominence in the title (e.g., "… and Toward Minkowski Geometry") and introduction, or (b) move key quantitative results from the appendix MRH tests into the main text to better match its billing.
3. Report Jaccard similarity or another overlap metric between the top-k concept sets recruited by different tasks to sharpen the "functional specialization" claim.
4. Add a brief discussion in Section 3 or 4 acknowledging that the non-identifiability result (Proposition 2) raises the possibility that specific SAE-discovered concepts reflect the factorization's inductive biases — and why the authors believe their findings are nonetheless robust.

## Score and Decision

**Calibration anchors used across rounds:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Sparse Autoencoders Find Highly Interpretable Features in Language Models | F76bwRSLeK.md | 4.80 | R1 | Weaker than this paper: narrower scope (language models only), less comprehensive analysis |
| What do vision transformers learn? A visual exploration | 4aJg9e4nvF.md | 4.75 | R2 | Weaker than this paper: less concrete findings, shallower methodology |
| A Simple Interpretable Transformer for Fine-Grained Image Classification | bkdWThqE6q.md | 6.00 | R2 | Not directly comparable (method paper); comparable overall quality |
| Task structure and nonlinearity jointly determine learned representational geometry | k9t8dQ30kU.md | 6.75 | R1/R2 | Slightly stronger: cleaner hypothesis-testing loop, though on simpler models |
| The Representation Geometry of Features and Hierarchy in Large Language Models | bVTM2QKYuA.md | 6.75 | R2 | Slightly stronger: more rigorous theoretical development with formal definitions and theorems; empirical validation better matched to claims |
| Geometric Inductive Biases of Deep Networks | cmXWYolrlo.md | 7.50 | R2 | Stronger: cleaner hypothesis with extensive theoretical and empirical development |
| Interpreting CLIP's Image Representation via Text-Based Decomposition | 5Ca9sSzuDp.md | 8.00 | R1 | Stronger: well-executed analysis with practical applications, no major weaknesses |

**Round 1 bracket:** [5.5, 7.5]. The paper is clearly above the weaker empirical interpretability papers (4.5–5.0) and below the top-tier hypothesis papers with cleaner claim-evidence alignment (7.5–8.0).

**Round 2 narrowing:** Compared against anchors at 6.0–7.5, the paper sits near the lower end of this range. Its empirical contributions (task analysis, geometric characterization) are solid, but the MRH-evidence gap creates a mismatch between packaging and content that papers at 6.75+ avoid.

**Final score:** 6.0. The paper makes genuine contributions — the 32k-concept dictionary, the task-specific analyses (Elsewhere concepts, border concepts, depth cue families), and the geometric characterization are all novel and well-executed. Proposition 1 connecting attention to Minkowski sums is a genuine theoretical insight. However, the MRH is over-represented relative to its support, and the Elsewhere interpretation would benefit from quantitative grounding. These are fixable weaknesses in a paper whose core empirical contributions are real and valuable.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>