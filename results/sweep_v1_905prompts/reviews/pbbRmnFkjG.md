Now I have enough calibration. Let me write the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal

### Major

### Minor

### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me now construct the full review.

---

**Analysis of reviewer claims against the paper:**

**Claim 1: "Elsewhere" negation evidence is weak.** 
The paper says (line 65): "providing evidence suggestive of a causal effect realizing conditional negation (another interpretation being distributed off-object evidence)." And (line 93): "they vanish if the object is removed, indicating a conditional negation." The paper does acknowledge an alternative interpretation. The claim is hedged but still somewhat overconfident given the evidence described in the main text (one reference to causal masking, no quantification). This is a real weakness but milder than the harsh critic frames it. VERIFIED, keep as Minor/Major.

**Claim 2: MRH evidence is thin.**
The paper provides three tests briefly (line 177): geodesics vs straight-line interpolation, Archetypal Analysis comparison, and Gram matrix block structure. These are described in 3 sentences plus a figure reference. The paper says "preliminary empirical evidence" in the discussion. The harsh critic is correct that these tests don't distinguish MRH from alternatives. VERIFIED, keep as Major.

**Claim 3: SAE/MRH tension.**
The paper uses SAE (LRH-based) as its main analytical tool throughout Sections 2-4, then in Section 6 proposes MRH which questions whether linear directions are the right unit of analysis. The discussion acknowledges this implicitly (line 191: "extracting concepts from single layers is insufficient—proper decomposition requires signals from the entire network structure") but doesn't fully resolve the tension. VERIFIED, keep as Major.

**Claim 4: Segmentation/depth analysis is qualitative.**
The paper does provide some quantitative evidence: eigenspectrum comparisons (Figure 11), cosine similarity comparisons. But these are partial and don't include ablation studies or statistical tests. VERIFIED, keep as Minor.

**Criticisms to remove:**
- Missing appendix content references (stripped by parser) → REMOVE
- Proposition 1 being "elementary" and "definitional" → The paper shows a non-trivial connection between attention mechanism and Minkowski sums. REMOVE as factual inaccuracy.
- LRH as "straw man" → Paper is clear about testing against idealized LRH. REMOVE.
- Formatting/style nitpicks → REMOVE.
- Missing implementation details/hyperparameters (stripped appendix) → REMOVE.
- Computational cost/reproducibility (stripped appendix) → REMOVE (with partial exception for the single model/layer concern, which is a real scope limitation).

Let me write the final review now.## Summary

This paper operationalizes the Linear Representation Hypothesis (LRH) for DINOv2 using a stable sparse autoencoder (RA-SAE), extracting a 32,000-concept dictionary — the largest such interpretability resource for a vision foundation model to date. Using this dictionary, the authors make three main contributions: (1) they identify task-specific functional specializations — "Elsewhere" concepts for classification, border detectors for segmentation, and three monocular depth-cue families for depth estimation; (2) they provide quantitative geometric diagnostics showing the dictionary departs from idealized sparse near-orthogonal structure (higher coherence, sharp spectral decay, dense positional concepts); and (3) they propose the Minkowski Representation Hypothesis (MRH), where tokens behave as sums of convex regions around archetypal landmarks, and show that multi-head attention constructively realizes this geometry.

---

## Strengths

- **Large-scale, reproducible SAE dictionary for DINOv2.** The use of a RA-SAE (convex-hull constraint on atoms, R² > 88% fidelity) yields a 32,000-unit concept dictionary that is geometrically consistent and in-distribution. This directly addresses well-known SAE instability issues and provides an empirical resource whose scale is genuinely novel for vision foundation models.

- **Discovery of task-specific concept subspaces with converging quantitative evidence.** The paper shows that classification, segmentation, and depth estimation recruit distinct, low-dimensional subspaces of the concept dictionary (Figure 1, Figure 11). The identification of "Elsewhere" concepts (off-object activation that depends on the object's presence), border concepts forming tight clusters in embedding space with faster spectral decay than random baselines, and three monocular depth cue families via controlled perturbations (projective, shadow-based, frequency transitions) goes beyond simple attribution and reveals structured functional organization.

- **Quantitative geometric diagnostics that challenge idealized LRH.** The paper compares the learned dictionary against random and Grassmannian baselines (using the TAAP algorithm) and finds heavier-tailed pairwise similarities, sharply decaying singular values, and low Hoyer scores (Figure 4). The identification of dense but low-norm positional concepts as outliers and the weak correlation between co-activation and geometry (Figure 13) are concrete, measurable departures from purely sparse near-orthogonal representations.

- **Formal connection between multi-head attention and Minkowski sums.** Proposition 1 shows that each attention head outputs a convex combination of values and that multi-head outputs sum to a Minkowski sum of head polytopes. This provides an explicit mechanistic grounding for the MRH and connects to prior work on convex conceptual spaces and population geometry.

---

## Weaknesses

### Major

1. **The MRH is presented as a main contribution but the empirical evidence is insufficient to distinguish it from alternative geometric descriptions.** Three tests are offered (geodesics vs. straight-line interpolation, Archetypal Analysis reconstruction, Gram matrix block structure — Figure 26), but each is described in a single sentence and none is quantitatively compared against a baseline that would differentiate MRH from, say, a low-dimensional manifold or affine subspace account. The paper acknowledges this in the Discussion ("preliminary empirical evidence") but Section 6 occupies a full section and the title itself references "Minkowski Geometry." There is a mismatch between the prominence of the claim and the strength of the evidence. This is the paper's most significant weakness.

2. **Unresolved tension between the SAE-based analysis and the MRH.** The paper builds its entire empirical characterization (Sections 2–4) on the LRH/SAE framework, treating concepts as sparse combinations of near-orthogonal directions. Section 6 then proposes MRH, under which concepts are "points and regions, not directions" and the SAE decomposition may be non-identifiable (Proposition 2). The paper does not address whether the SAE atoms retain meaning under MRH, or whether the observed task-specific subspaces would even exist under that alternative geometry. This cuts across the paper's two halves and weakens internal coherence.

3. **The "Elsewhere" conditional negation claim is intriguing but the causal evidence is thin.** The paper states that Elsewhere concepts "vanish if the object is removed (via causal masking)" and interprets this as "conditional negation." The evidence is a single parenthetical reference to Petsiuk et al. (2018) with no quantification, no control for confounds (e.g., correlated background statistics, contrast computation), and no comparison to a null baseline. The paper does hedge ("evidence suggestive of," "another interpretation being..."), but the abstract and introduction state the finding more assertively as implementing "object negation." Either stronger causal evidence or a more cautious framing is needed.

### Minor

1. **The segmentation and depth analyses would benefit from more quantitative validation.** The border concept analysis (Figure 2, Figure 10) provides eigenspectrum and similarity comparisons (Figure 11), which is good. But there are no ablation studies (e.g., removing border concepts from a segmentation probe and measuring performance drop), no robustness checks across random seeds or datasets, and no statistical tests for the clustering of depth cue families. The findings are plausible and suggestive, but fall short of rigorously establishing functional specialization.

2. **All analyses use a single SAE (32k atoms, k=8 active codes) on a single model (DINOv2-B) at a single layer.** It is unclear how sensitive the findings are to the number of atoms, sparsity level, layer choice, or model size. A discussion of these factors or a sensitivity analysis would improve credibility. (This is acknowledged as a scope limitation, but the extent to which the MRH conclusions depend on these choices is nontrivial.)

3. **The reconstruction fidelity of 88% R² means that 12% of activation variance is lost; the paper does not discuss whether this could affect the geometric diagnostics in Section 4.** Since the MRH arguments rely on geometric properties of the dictionary, systematic reconstruction errors could potentially influence the observed coherence, spectral decay, and other patterns.

---

## Nice-to-Haves

- For the "Elsewhere" concepts, a proper causal test (e.g., comparing causal masking to random masking with quantitative metrics) would turn an intriguing observation into a well-supported finding.
- For MRH, a decisive test would verify whether tokens can be expressed as Minkowski sums of per-head convex hulls, with the decomposition aligning with actual attention weights. Alternatively, reframing MRH as a brief speculation in the Discussion rather than a main contribution would resolve the prominence/evidence mismatch.
- The paper promises an interactive visualization upon release, which is a valuable community resource.

---

## Removed Points

- **Missing appendix content (details of masking procedure, hyperparameters, etc.):** The parser strips these sections from all papers; they exist in the original submission. Removed per rule.
- **Proposition 1 dismissed as "elementary" or "definitional":** The proposition shows a non-trivial correspondence between the attention mechanism and Minkowski sums; this is a valid mathematical connection, not a trivial restatement. Removed.
- **LRH treated as a "straw man":** The paper is explicit about testing against *idealized* LRH (near-orthogonal, Grassmannian). This is a clear target, not a straw man. Removed.
- **Style/formatting nitpicks and requests for more figures or different organization:** Removed per rule.
- **Reproducibility concerns about undisclosed hyperparameters in stripped appendices:** Removed per rule.

---

## Novel Insights

Beyond the paper's own contributions, the most striking observation across the reviews is this: the paper may be trying to do two valuable things at once — build a high-quality empirical map of DINOv2's concept space and propose a new geometric theory — but these two projects pull in different directions. The SAE-based analysis is most naturally interpreted under the LRH framework it operationalizes, while the MRH undermines that very framework. Neither the paper nor the reviewers fully resolve whether the MRH is genuinely incompatible with the SAE analysis or whether the SAE atoms could be reinterpreted as landmarks or boundary points of MRH polytopes. This tension, rather than being a flaw per se, could be the seed of a more interesting follow-up: a paper that re-analyzes the SAE dictionary *through the lens of MRH* to see whether the observed structure (high coherence, task-aligned subspaces, antipodal pairs) is naturally explained by convex polytope geometry.

---

## Suggestions

1. **Resolve the prominence/evidence mismatch for MRH.** Either (a) add a decisive test that distinguishes MRH from alternative geometric descriptions (e.g., check whether each token can be expressed as a Minkowski sum of per-head convex hulls with decomposition aligning with attention weights), or (b) reframe MRH as a brief speculation in the Discussion and reposition the paper's main contribution as the empirical mapping of DINOv2's concept space.

2. **Reconcile the SAE and MRH frameworks.** Discuss whether SAE atoms could correspond to landmarks or boundary points of MRH polytopes, whether the observed task-specific subspaces would persist under MRH, and what the status of the Section 2–4 analyses is if the MRH is true.

3. **Add quantitative validation for the "Elsewhere" and segmentation claims.** For Elsewhere concepts, a quantitative causal test comparing concept activation with and without object masking (vs. a random-masking baseline) would significantly strengthen the claim. For segmentation, an ablation study removing border concepts from the probe and measuring performance drop would move the analysis from suggestive to convincing.

---

## Score and Decision

**Calibration:** Round 1 bracketing placed the paper between low-scoring vision SAE/interpretability papers (1.67–3.40) and strong ones (8.00–8.20). Round 2 narrowing compared the paper against accepted papers at 6.40–6.80 (CLIP SAE concept remapping, representational similarity via concepts) and rejected papers at 4.40–4.83 (SDXL Turbo SAE, "What do vision transformers learn?"). The paper under review has richer and more novel content than the rejected papers in the 4.4–4.8 range (discovery of task-specific specializations, geometric diagnostics, MRH proposal) but weaker empirical validation and greater internal tension than the accepted papers at 6.4–6.8. Final score: 5.5.

**Evaluation axes:** The paper is strong on originality (concept dictionary scale, task specialization findings, MRH proposal), the importance of the research question (what does DINOv2 represent internally?), and value to the community (released dictionary and interactive demo). The claims are moderately supported — the empirical mapping is solid but incompletely validated, and the MRH is undersupported relative to its prominence. Clarity is reasonable though the paper tries to cover too much. The experiments are sound in design but could benefit from more rigorous validation and ablations.

<score>5.5</score>
<decision>Reject</decision>