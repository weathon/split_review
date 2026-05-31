Now let me produce the final calibrated review.

## Summary

The paper trains a stable sparse autoencoder on DINOv2 to extract a 32,000-unit concept dictionary — the largest interpretability demonstration for a vision foundation model to date. It analyzes how downstream tasks (classification, segmentation, depth) recruit these concepts, revealing functional specialization (Elsewhere negation, border detectors, monocular depth cue families). It then examines the geometry and statistics of the concept space, finding systematic departures from the near-orthogonal ideal of the Linear Representation Hypothesis (LRH). Finally, it proposes the Minkowski Representation Hypothesis (MRH) as an alternative geometric account where tokens behave as sums of convex regions around archetypal landmarks.

## Strengths

1. **Largest-scale SAE-based interpretability study for a vision foundation model.** The 32,000-unit dictionary with stable SAE training (convex-hull constraint on atoms) is a significant engineering contribution. The dictionary itself, described in Section 2, is released as an interactive visualization and constitutes a valuable resource for the community.

2. **Rigorous quantitative analysis of departures from LRH.** Sections 4–5 systematically document that DINOv2's concept space diverges from the Grassmannian ideal: heavier-tailed coherence than baselines (Fig. 4, bottom-left), sharp singular-value decay indicating anisotropic capacity, low Hoyer scores confirming distributed (not neuron-aligned) atoms, task-specific subspaces with faster spectral decay than random subsets (Fig. 11), and smooth per-image token structure that position alone cannot explain (Fig. 25). These analyses are the paper's strongest contribution.

3. **Discovery of functionally specialized concept subsets.** The identification of Elsewhere concepts (implementing conditional negation for classification), border concepts forming tight subspaces for segmentation, and three families of monocular depth cues (projective, shadow-based, frequency transitions) for depth estimation is genuinely novel. Even the qualitative evidence is compelling as a discovery, though it needs quantitative reinforcement.

4. **Formal connection between multi-head attention and convex geometry.** Proposition 1 proves that multi-head attention's output is a Minkowski sum of convex polytopes formed by each head's value set, providing a mechanistic basis for MRH that is grounded in the architecture itself, not just a phenomenological observation.

5. **Non-identifiability result with practical implications.** Proposition 2 shows that Minkowski decomposition is non-unique from activations alone, which usefully constrains what interpretability methods can recover without architectural signals.

## Weaknesses

### Major

1. **Task-specific concept analysis (Section 3) relies on insufficiently supported qualitative evidence.** The Elsewhere concept claim that activations "vanish if the object is removed" is stated without quantitative evaluation across multiple images, classes, or controls. The paper asserts "all the concepts among the top-50 consistently localize along object contours" for segmentation but provides no boundary-alignment metric (e.g., mean distance to nearest contour). The depth cue analysis identifies three families via perturbation, but the mapping from perturbation type to claimed cue family (e.g., "median blurring removes shadows") is not independently validated — median blurring also removes texture and fine details. These qualitative observations are presented as *results* ("we discovered clear specialization"), not just motivating examples, yet the evidence is predominantly illustrative. This weakens the paper's first stated contribution.

2. **MRH is presented as a central contribution but is insufficiently empirically validated.** Proposition 1 is a mathematical observation about attention's structure (every attention head outputs convex combinations of its values), not a discovery specific to DINOv2's actual behavior. The empirical evidence for MRH (k-NN geodesics in Fig. 26 left, Archetypal Analysis vs. SAE in Fig. 26 middle, Gram block structure in Fig. 26 right) is too briefly described — the text gives no details on how AA was fit, how reconstruction error was measured, or over how many images. The paper's title names "Minkowski Geometry" and the structure presents MRH as a co-equal third contribution, but the evidence does not yet support that status. (The Discussion does call MRH a "working hypothesis," which partially mitigates this.)

### Minor

3. **No ablation of SAE sparsity level (k=8).** How sensitive are the geometric analyses (coherence distributions, spectral decay, task subspace spectra) to this hyperparameter choice?

4. **All results use final-layer activations only.** Layer-wise evolution of concept specialization or geometric departure from LRH would be informative and is not examined.

5. **Many quantitative comparisons lack error bars.** The paper uses a single trained model and single SAE seed. Bootstrapping or multiple seeds would establish that the reported patterns (coherence differences, spectral decay rates) are stable.

6. **Domain shift between SAE training and downstream datasets.** The SAE is trained on ImageNet-1k tokens; analyses of segmentation (ADE20k) and depth (NYU) use the same dictionary without discussion of whether domain shift affects concept coverage.

### Trivial

None.

## Removed Points

*Criticisms about missing appendix content:* The appendix is stripped by the parser; concerns about missing details that clearly belong in the appendix cannot be verified from what is on the page.

*Criticism that straight-line vs. k-NN geodesics is expected for "many types of structure":* This is speculative reasoning about what the evidence *could* mean rather than a specific flaw in what the paper actually reports.

*Criticism that the AA-vs-SAE comparison is "not directly comparable":* The criticism is based on insufficient detail in the main text, but that detail likely exists in the (stripped) appendix.

*Strength Finder generic strengths about "important problem":* Removed as lacking concrete, paper-specific content.

*Criticism about the interactive demo not being released:* The paper explicitly states it will be released upon acceptance.

## Novel Insights

The paper's core empirical finding — that DINOv2's learned concept space departs systematically from the Grassmannian ideal assumed by LRH, showing heavier-tailed coherence, task-aligned anisotropy, and smooth per-image token structure not reducible to positional encoding — is a genuinely novel characterization of how a major vision foundation model organizes its internal representations. The MRH formalization, while preliminary, connects these empirical patterns to a concrete mechanistic account rooted in attention's convex-combination structure, and the non-identifiability proposition usefully clarifies the limits of activation-only interpretability. The discovery of Elsewhere, border, and depth-cue concepts demonstrates that the dictionary captures functionally meaningful structure, even if the evidence for these specific claims would benefit from quantification.

## Suggestions

1. **Quantify the task-specific analyses.** For Elsewhere concepts: measure concept activation change before/after causal masking over ≥100 images per class with a shuffle control. For border concepts: compute average boundary alignment (e.g., mean distance to nearest contour) across top-100 concepts. For depth cues: use controlled synthetic stimuli where only one cue varies, or show that the three UMAP clusters are *differentially* sensitive to perturbation types in the expected direction.

2. **Either substantially strengthen MRH empirical evidence or reframe it.** A more convincing test would be to (a) explicitly fit an MRH model (head-wise archetypes and convex combination weights) and compare held-out reconstruction to the SAE, or (b) demonstrate that DINOv2's attention weights reliably induce block-convex code structure. Alternatively, reframe MRH as a forward-looking hypothesis/deferred validation rather than a co-equal contribution, which the geometric analysis alone already justifies as a discussion.

3. **Add SAE sparsity (k) ablation and layer-wise analysis.** Show that the key geometric findings (coherence, spectral decay, task specialization) are robust across k ∈ {4,8,16} and examine how concept specialization evolves across DINOv2 layers.

4. **Report uncertainty.** Add bootstrapped confidence intervals or results across multiple training seeds for the key quantitative comparisons.

## Score and Decision

**Calibration anchors consulted across all rounds:**

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| Scaling and evaluating sparse autoencoders | tcsZt9ZNKD.md | 1.75 | R1 | Much weaker; less substantive analysis |
| Understanding Skill Adaptation in Chess (SAE) | Wxl0JMgDoU.md | 2.50 | R1 | Much weaker; narrower scope and findings |
| Conceptualize Any Network | wZiH43e5Ah.md | 3.00 | R1 | Weaker; generic concept extraction framework |
| Automatically Identifying and Interpreting Sparse Circuits | 89wVrywsIy.md | 3.40 | R1 | Weaker; narrower contribution |
| Simple mechanisms for representing concepts | vogtAV1GGL.md | 5.75 | R1 | Comparable; both propose representation hypotheses with partial validation |
| **The Representation Geometry of Features and Hierarchy in LLMs** | bVTM2QKYuA.md | **6.75** | R1 | Stronger; tighter theory-to-experiment pipeline with clear validation |
| What do vision transformers learn? A visual exploration | 4aJg9e4nvF.md | 4.75 | R1 | Comparable but less ambitious; more qualitative |
| **The Geometry of Tokens in Internal Representations of LLMs** | an3jH2qD2r.md | **6.00** | R1 | Comparable scope but different domain; that paper was rejected for unclear motivation |
| Sparse Autoencoders Find Highly Interpretable Features in LMs | F76bwRSLeK.md | 4.80 | R2 | Topically closest; similar SAE methodology but less comprehensive geometry analysis |
| Compute Optimal Inference in SAEs | ghH6YYDs15.md | 4.67 | R2 | Weaker; theoretical focus with less empirical breadth |
| Towards scientific discovery with dictionary learning | uDIiL89ViX.md | 5.60 | R2 | Comparable; similar dictionary learning approach but different domain |
| **Task structure and nonlinearity determine representation geometry** | k9t8dQ30kU.md | **6.75** | R2 | Stronger; tighter experimental design with clear causal conclusions |
| **Discriminating image representations with principal distortions** | ugXGFCS6HK.md | **6.20** | R2 | Comparable; both introduce novel methods for analyzing representation geometry |

**Round 1 bracket:** The paper sits between the weak band (<3.5, clearly below) and the strong band (>7.5, clearly above). Plausible range: 4.5 – 7.0.

**Round 2 narrowing:** The most topically similar papers are the SAE-for-interpretability paper (4.80, accepted but mixed reviews) and the representation geometry papers (6.00–6.75). The paper under review is more comprehensive than the SAE paper but less cleanly executed than the 6.75 geometry paper. It is comparable to or slightly below the 6.00 geometry-of-tokens paper (which was rejected) when accounting for evidentiary gaps in the qualitative task analysis and under-validated MRH.

**Final score:** 5.5. This reflects the paper's genuine contributions (largest SAE dictionary for vision, novel geometric characterization of departures from LRH, interesting qualitative discoveries of functional specialization) while accounting for the significant evidentiary gap in the task-specific analysis claims and the MRH being promoted beyond its current support level.

**Decision:** Reject. The paper has a solid empirical core (Sections 2, 4, 5) and interesting ideas, but the gap between claims and evidence in Section 3 (task-specific concept analysis) and the over-weighting of the under-validated MRH as a co-equal contribution are significant enough to fall below the acceptance bar in current form. These issues are fixable — the paper could be a strong candidate after quantifying the task analyses and either strengthening MRH validation or appropriately reframing it — but in its present state the claims outstrip the evidence.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>