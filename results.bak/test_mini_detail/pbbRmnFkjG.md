Now I have all the data I need. Let me write the final consolidated review.

## Summary

This paper trains a stable sparse autoencoder (RA-SAE) on DINOv2 to extract a 32,000-concept dictionary, analyzes how downstream tasks (classification, segmentation, depth estimation) recruit specialized geometric subspaces, and then characterizes the dictionary's geometry — finding higher coherence than Grassmannian baselines, sharp spectral decay, and dense positional signals that deviate from the sparse near-orthogonal Linear Representation Hypothesis. On the basis of these departures, the paper proposes the Minkowski Representation Hypothesis (MRH), showing that multi-head attention naturally produces Minkowski sums of convex polytopes, and provides preliminary empirical evidence (archetypal analysis, block-structured codes) consistent with this picture. The paper is ambitious, well-motivated, and covers considerable ground.

## Strengths

1. **Scale and fidelity of concept extraction**: The paper trains a stable SAE on DINOv2 with 32,000 atoms and achieves R² > 88% reconstruction fidelity using a BatchTopK encoder (Section 2). The RA-SAE design constrains atoms to lie in the convex hull of real activations, guaranteeing reproducible and geometrically faithful dictionaries. This is the largest concept dictionary for a vision foundation model to date, and the release of the interactive demo is a meaningful community contribution.

2. **Task-specific geometric subspaces with functionally specialized concept types**: The paper quantifies how classification, segmentation, and depth estimation each recruit distinct, low-dimensional subspaces of the dictionary. It identifies: (i) "Elsewhere" concepts for classification that fire off-object yet depend on the object's presence, (ii) border concepts for segmentation that form a tight embedding cluster, and (iii) three monocular cue families for depth estimation via controlled perturbation analysis (projective, shadow-based, frequency transitions). The quantitative support (intra-task similarity, eigenvalue decay much faster than random subsets, Figure 11) is solid.

3. **Empirical deviation from the idealized sparse near-orthogonal LRH**: The paper provides multiple diagnostics showing the dictionary is more coherent than Grassmannian and random baselines (Figure 4A), has a sharply decaying singular value spectrum (Figure 4B), low Hoyer scores confirming distributed atoms (Figure 4D), and dense low-norm positional concepts (Figure 4 top-left). These findings constitute a genuine empirical contribution to understanding DINOv2's internal representations.

4. **Theoretical grounding of MRH in multi-head attention**: Proposition 1 formally shows that multi-head attention outputs are Minkowski sums of convex polytopes (each head produces a convex combination of its values, and heads are summed). This architectural connection is a genuine insight, regardless of how fully the empirical evidence supports MRH as a complete model.

## Weaknesses

### Major

1. **Gap between MRH claims and the evidence**: The MRH is presented as a proposed alternative representation geometry, but the empirical support is weaker than the framing suggests.
   - **Proposition 1 vs. Definition 1**: The MRH definition (Def. 1) requires an overcomplete archetype set partitioned into *tiles* with *sparse tile activation* (|S| ≪ m). However, Proposition 1 maps heads directly to tiles — there are exactly H heads, all are active, so |S| = H. This does not satisfy the sparse-tile condition of the formal definition. The connection between MHA and MRH is thus looser than "directly implements" implies.
   - **The three empirical tests are weak confirmations**: (a) Straight-line interpolation leaving the data manifold is consistent with many non-convex geometries, not specifically Minkowski sums of convex polytopes. (b) Archetypal analysis matching SAE reconstruction with ~10 archetypes is interesting but both methods are linear reconstruction techniques with sparsity constraints; the agreement may simply indicate tokens live near a low-dimensional subspace. (c) The Gram block structure (Figure 26 right) is mentioned qualitatively but not quantified (no normalized block-diagnostic statistic compared to baselines).
   - **The paper does hedge** — the abstract says "present it as a working hypothesis" and Section 6 says "If, and this is an assumption, the Minkowski Representation Hypothesis holds" — so the tone is not as overreaching as the harsh critic suggested. Nevertheless, the Section 6 "Implications for Interpretability" reads as drawing definitive consequences from an unsubstantiated hypothesis, and the overall narrative arc (from departures from LRH → MRH proposal) suggests more support than the evidence provides.

2. **Relationship between the SAE dictionary D and the MRH archetype set A is unclear**: The paper trains a 32,000-atom SAE dictionary D and uses it for the task-specific analysis and geometric characterization. Then MRH introduces an "overcomplete archetype set A" partitioned into tiles. Are the 32,000 SAE atoms meant to correspond to the archetypes? Or is the dictionary a different object? This ambiguity is central to understanding whether the SAE analysis (which occupies most of the paper) is compatible with MRH, and the paper does not clarify it.

### Minor

3. **Causal interpretation of "Elsewhere" concepts is somewhat strong**: The main text says the Elsewhere concepts vanish when the object is removed, "indicating a conditional negation" (Section 3). The figure caption hedges ("another interpretation being distributed off-object evidence"), but the main text claims a specific implemented function. The evidence does not distinguish between (a) genuine "not-object" computation and (b) a learned background feature that happens to be suppressed when object statistics shift after masking. This is a presentation issue rather than a substantive flaw, but it reflects a pattern of drawing stronger inferences than the evidence strictly supports.

4. **Missing quantification of Gram block structure**: The paper claims "clear block structure" in the code Gram matrix (Figure 26 right) as evidence for MRH's tile-sparsity condition, but provides no quantitative metric (e.g., modularity, silhouette score, or comparison to random baselines). This is the only direct evidence for the tile-sparsity condition, and it is presented qualitatively.

5. **Depth cue families identified via UMAP are labeled too definitively**: The perturbation-UMAP analysis identifies three clusters of concepts responding to different perturbations, which the paper labels as "projective geometry cues," "shadow-based cues," and "frequency-based cues." The paper acknowledges in Appendix C.3 that this is interpretive, but the main text language ("three families of monocular cues," Section 3) presents them as established categories without validation against known depth stimuli or human annotation.

### Trivial

6. The choice of dictionary size (32,000) and sparsity level (k=8) is not discussed or justified. This is a minor omission.

## Nice-to-Haves

- The geodesic interpolation test (Figure 26 left) could be strengthened by discussing alternative explanations (e.g., a low-dimensional smooth manifold) and explaining why MRH specifically is a better fit.
- The paper could benefit from a brief discussion of how MRH differs from or builds on prior convex conceptual spaces work (Gärdenfors, Park et al.) beyond citation.
- Validating the depth cue families by checking correlation with known depth maps (e.g., NYU) or by showing that perturbing those concepts changes depth predictions would significantly raise confidence.

## Removed Points

- **"The paper is over-scoped"**: This is a structural preference, not a weakness. The paper's three-part structure is ambitious but coherent, and each part contributes to the overall narrative. The harsh critic's suggestion to cut the MRH section is a strategic recommendation, not a flaw in the paper as submitted.
- **"Missing discussion of prior work on convex conceptual spaces"**: The paper cites Gärdenfors (2004) and Park et al. (2025) in Section 6. The critic wants more comparison, but this is more of a scope request than a genuine weakness.
- **"Proposition 2 is a standard fact"**: While Proposition 2 (non-identifiability of Minkowski decomposition) is a known mathematical observation, its value is in the implication for interpretability — that single-layer concept extraction is underdetermined. This is a useful framing even if the underlying math is standard.
- **"The Grassmannian baseline is not explained"**: The paper references the TAAP algorithm and Appendix F. For a main conference paper, this level of detail is appropriate.
- **Strengths from the Strength Finder that were removed**: "Non-identifiability result" (overstated — it's a standard mathematical fact), "Discovery of antipodal pairs" (interesting but presented as an observation, not a core claim), "Systematic causal perturbation analysis for depth" (interesting but the paper presents it as qualitative).

## Novel Insights

The most interesting synthesis emerging from the reviews is the tension between the paper's two main contributions. The empirical study of DINOv2's concept space (task-specific subspaces, statistical and geometric properties) is well-supported and genuinely novel — it provides the largest-scale look at how a vision foundation model organizes its internal features. The MRH proposal, on the other hand, is a thought-provoking but under-evidenced conjecture. These two contributions sit uneasily together: the empirical work suggests the representation is more complex than sparse near-orthogonal coding, but not yet that it is specifically a Minkowski sum of convex polytopes with sparse tile activation. The paper would be stronger if it presented MRH as a motivating speculation that future work should test, rather than as a settled alternative framework with implications already drawn. The architectural connection (Proposition 1) is a genuine insight that could stand alone as a theoretical observation, independent of the empirical evidence.

## Suggestions

1. **Recalibrate MRH framing**: Present MRH as a motivated conjecture/hypothesis, not as a conclusion. Move the "Implications for Interpretability" section to a discussion of what would follow *if* MRH were true, and explicitly state what evidence would be needed to test it. This would better match the strength of the evidence.
2. **Quantify the Gram block structure**: Report a normalized block-diagnostic statistic (e.g., silhouette score or modularity) for the code Gram matrix, with comparison to shuffled baselines.
3. **Clarify the relationship between D and A**: Explain whether the 32,000 SAE atoms are the MRH archetypes, or whether the archetypes are a different object, and how the SAE analysis fits into the MRH framework.
4. **Tone down Elsewhere causal language**: Replace "implements conditional negation" with "is consistent with a conditional negation interpretation" or similar phrasing throughout.
5. **Add alternative explanations for the geodesic test**: Discuss why the result (straight-line interpolation leaving the data manifold) is consistent with MRH but also with other non-convex geometries, and what would distinguish them.

## Score and Decision

**Calibration report:**

**Round 1 (Bracketing, 3 queries, all on "DINO interpretability SAE concepts"):**
- Low band (<3.5): Papers at 2.5–3.0 (weak concept interpretability papers, all Reject/Withdrawn)
- Mid band (3.5–7.5): Papers at 4.3–7.3 (mix of Poster/Spotlight and Reject; e.g., SAE evaluation at 7.0 Poster, concept bottleneck at 4.67)
- High band (>7.5): Papers at 8.0–8.2 (Oral, e.g., "Scaling and evaluating sparse autoencoders" 8.2, "Interpreting CLIP" 8.0)

**Round 1 bracket**: The paper sits well above the 2.5–3.0 band (those are much weaker papers) and below the 8.0+ band (those are exceptionally clean, well-executed papers). The plausible range is 4.5–7.5.

**Round 2 (Narrowing, 2 queries on "vision transformer interpretability concept geometry"):**
- Lower half (4.5–6.5): "Uncovering hidden geometry in Transformers via disentangling position and context" (5.33, Reject), "GeoCon" (6.33, withdrawn), various concept bottleneck papers (4.75–5.0, Reject)
- Upper half (6.5–8.0): "Geometry of Categorical and Hierarchical Concepts in LLMs" (6.75, Accept Oral), "Enhancing Pre-trained Representation Classifiability" (7.33, Accept Spotlight), "Task structure and nonlinearity" (6.75, Accept Poster)

**Anchors read in full:**
- **"Geometry of Categorical Concepts in LLMs" (6.75, Oral)**: Clean mathematical formalization and empirical validation of concept geometry in LLM unembedding space. More rigorous but narrower scope. The paper under review is more ambitious but less cleanly executed — comparable quality but different tradeoffs.
- **"Task structure and nonlinearity" (6.75, Poster)**: Systematic empirical study of representation geometry in 2-layer networks. Clean but limited scope. Our paper is broader and more ambitious but less systematic.
- **"Towards Principled Evaluations of SAEs" (7.0, Poster)**: Well-executed SAE evaluation framework but limited to IOI task. Our paper covers more ground but has more framing issues.
- **"Enhancing Pre-trained Representation Classifiability" (7.33, Spotlight)**: Very clean execution of a focused idea (IIS metric). Our paper is less cleanly executed.

**Final score**: The paper is above the 5.33–6.33 range (which includes papers with significant execution problems or very narrow scope) but below the 7.0–7.33 range (which includes papers with very clean execution within a focused scope). The paper's ambition and breadth are genuine strengths, but the MRH-evidence gap and framing issues prevent it from reaching the 7+ tier. Score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>