## Summary

This paper trains a 32,000-atom stable sparse autoencoder (RA-SAE) on DINOv2-B and uses it for three purposes: (1) characterizing how downstream tasks (classification, segmentation, depth estimation) recruit functionally specialized concept subspaces—revealing "Elsewhere" concepts for classification, border detectors for segmentation, and three monocular depth cue families; (2) analyzing the geometry of the learned dictionary against Grassmannian baselines, finding departures from the idealized orthogonal structure predicted by the Linear Representation Hypothesis; and (3) proposing the Minkowski Representation Hypothesis (MRH), where tokens behave as Minkowski sums of convex polytopes realizable by multi-head attention. The paper also releases an interactive 32k-concept dictionary visualization.

## Strengths

1. **Large-scale SAE concept dictionary for a vision foundation model.** The paper trains a 32,000-atom RA-SAE on DINOv2-B (d=768) with R² > 88% reconstruction fidelity (Section 2, line 57), representing a substantial scale increase over prior vision SAE work. The dictionary is released with an interactive visualization.

2. **Discovery of functionally specialized task subspaces with concrete qualitative findings.** The analysis reveals that classification exploits "Elsewhere" concepts (off-object features that depend on object presence), segmentation concentrates on border detectors forming coherent low-dimensional subspaces, and depth estimation draws on three distinct monocular cue families (projective, shadow-based, frequency transitions) identified via controlled perturbations (Section 3, Figures 2-3). The depth cue perturbation analysis is particularly well-designed and yields neuroscience-aligned findings.

3. **Systematic multi-diagnostic geometric characterization against Grassmannian baselines.** The paper benchmarks the learned dictionary against random and Grassmannian (TAAP) baselines on four complementary diagnostics: pairwise similarity distributions (heavier tails), singular-value spectrum (sharp decay), Hoyer sparsity scores (distributed, not neuron-aligned), and UMAP organization (weak modularity) — all in Section 4, Figure 4. This multi-metric comparison is more thorough than typical geometric analyses in the SAE literature.

4. **Formal derivation that multi-head attention constructs Minkowski sums.** Proposition 1 (Section 6, lines 155-161) proves that each attention head outputs a convex combination of its values, and multi-head summation yields a Minkowski sum of head polytopes. This provides a concrete architectural grounding for MRH and is the paper's strongest theoretical contribution.

5. **Clean isolation of positional vs. non-positional contributions to per-image token geometry.** By training linear decoders to predict token coordinates and projecting orthogonal to the positional subspace, the paper shows that PCA structure in token embeddings is largely preserved after removing position (Section 5, lines 121-135; Figure 25), demonstrating that the observed smooth token structure is not merely a position-encoding artifact.

## Weaknesses

### Fatal

None.

### Major

1. **The SAE's convex-hull constraint confounds the evidence against LRH.** The RA-SAE explicitly constrains D ∈ conv(A) (line 55), meaning dictionary atoms must lie in the convex hull of real activations. The departures from Grassmannian structure (higher coherence, heavier-tailed inner products) that the paper attributes to DINOv2's representations may partly reflect this parametrization constraint rather than an inherent property of the model. The paper does not control for this — it never compares against a standard SAE (without the convex-hull constraint) to verify whether the geometric findings persist. This weakens the central claim that the dictionary "departs from a near-orthogonal/Grassmannian picture" as evidence against LRH. Without this control, the observed geometry could be as much a property of the RA-SAE as of DINOv2.

2. **Unresolved tension between 88%+ SAE reconstruction fidelity and the claim that LRH is substantially violated.** The SAE is a linear sparse reconstruction model achieving R² > 88%. If the representation space truly resisted a sparse linear decomposition, a linear SAE would not reconstruct it well. The paper acknowledges some LRH-consistent findings (antipodal pairs, low Hoyer scores, line 34) but never explicitly reconciles how 88%+ explained variance is compatible with the assertion that representations "question a purely sparse-coding view" (line 34) and motivate an entirely different geometric hypothesis. The paper would benefit from clarifying whether the MRH-relevant structure lives in the 12% unexplained variance or is visible even within the explained component.

### Minor

3. **The Elsewhere "conditional negation" claim outruns the evidence.** The abstract states that classification exploits "Elsewhere concepts that implement object negation" (line 9), and the introduction says they "implement learned negation" (line 33). The supporting evidence is occlusion-based (Petsiuk et al. 2018, RISE), which is attribution—not causal intervention. Showing that a feature is suppressed when an object is occluded is compatible with multiple mechanisms. The figure caption hedges ("suggestive," "another interpretation being distributed off-object evidence," line 51), but the abstract and contributions list use language the evidence does not support. Stronger causal evidence (e.g., activation patching) or softened claims would resolve this.

4. **MRH receives prominent billing but only preliminary empirical evidence.** Despite the title ("Into the Rabbit Hull... to Minkowski Geometry"), the three-part structure placing MRH as a co-equal contribution, and abstract-level prominence, the empirical evidence for MRH (Section 6, lines 163-164) is thin: (a) geodesic paths staying near the data support is consistent with any nonlinear manifold model, not specifically MRH; (b) Archetypal Analysis matching SAE reconstruction with ~10 archetypes speaks to intrinsic dimensionality, not Minkowski-sum geometry; (c) block structure in code Gram matrices could arise from the BatchTopK sparsity constraint (k=8 active codes) rather than MRH's predicted tile structure. The paper honestly calls MRH a "working hypothesis" (line 9) but the organizational emphasis is disproportionate to the evidence.

5. **Methodological tension between Parts 1-2 (concepts as linear directions) and Part 3 (concepts as landmarks/regions).** Part 1 quantifies task recruitment via alignment scores (inner products with concept directions). Part 3 argues that concepts are "points and regions, not directions" (line 165) and that inner-product-based evidence is the view MRH departs from. The paper never explains how the linear-probe-based analyses of Sections 3-4 relate to the landmark-based view of Section 6 — whether they remain valid as approximations under MRH or whether MRH would supersede them.

6. **The claim that "usage influences geometry but is not the dominant organizing principle" rests partly on a mathematically forced correlation.** The paper's own footnote (line 123) acknowledges that corr(Z^T Z, DD^T) is "guaranteed to be positive" and "may be an intrinsic property of linear reconstructive methods." If the correlation is mathematically forced, finding a positive (even weak) correlation is not informative about the hypothesis — the test cannot produce a null result. This undercuts one of Section 4's main conclusions.

### Trivial

7. **The qualitative claim that "all the concepts among the top-50 consistently localize along object contours" (line 81) would benefit from quantitative measures** — number of images examined, annotation protocol, inter-rater agreement.

8. **Hyperparameter choices (c=32,000, k=8) are stated without justification or ablation** showing sensitivity of the main findings. However, this is common practice in large-scale SAE work.

## Nice-to-Haves

- A control experiment comparing the RA-SAE against a standard SAE (without D ∈ conv(A)) to verify that the geometric departures from Grassmannian structure are not a constraint artifact.
- Explicit reconciliation of the 88%+ R² with the claimed LRH violations.
- Proper causal intervention (activation patching) on Elsewhere concepts, or softening of the causal claims.
- Error bars and significance tests on quantitative comparisons (e.g., intra-task concept alignment).

## Removed Points

These points were identified by reviewers but are removed per filtering rules:

- "Layer selection not specified" — Removed: this detail may appear in the appendix (stripped by parser). Per hard rules, removed.
- "Proposition 2 is a standard result, not a novel finding" — The paper cites Smilansky (1987) and presents the non-identifiability result for its *interpretability implications*, not as novel mathematics. Removed as mischaracterization.
- "Steering saturation claim references LLM research without DINOv2 experiments" — The paper presents this as an implication and connects to existing literature, not as an original experiment. Not a valid weakness.

## Novel Insights

The most novel insight from the reviews is the observation that the paper's three parts rest on potentially incompatible premises about what concepts are: Part 1 treats concepts as linear directions (via alignment scores), while Part 3 argues concepts are landmarks/convex regions, not directions. This tension is nowhere addressed in the paper and would need resolution for the paper to be internally coherent. A second genuinely novel observation is that the SAE's convex-hull constraint (D ∈ conv(A)) creates a circularity risk: the geometric findings used to argue against LRH may partly reflect the SAE's parametrization rather than DINOv2's intrinsic geometry.

## Suggestions

1. Restructure the paper to foreground the empirical findings (task-specific concept recruitment, geometric diagnostics) and position MRH as a speculative discussion/synthesis rather than a co-equal third contribution. The current framing overclaims relative to the evidence.
2. Add a control experiment comparing the RA-SAE against a standard SAE without the convex-hull constraint. This is the single highest-leverage experiment the paper could add.
3. Soften the Elsewhere "negation" claims in the abstract and introduction to match the observational evidence, or add proper causal intervention experiments.
4. Explicitly address the relationship between the linear-probe-based analyses (Parts 1-2) and the landmark-based MRH view (Part 3).
5. Discuss the 88% R² tension: would a linear SAE reconstruct so well if LRH were substantially violated?

## Calibration Anchors

### Round 1 — Bracketing
The following anchors were retrieved to bracket plausible score ranges:

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| tcsZt9ZNKD.md — "Scaling and evaluating sparse autoencoders" (GPT-4 SAE scaling) | ~8.2 | R1 (strong) | Much more rigorous and foundational SAE work; our paper is substantially weaker |
| I4e82CIDxv.md — "Sparse Feature Circuits" | 8.0 | R1 (strong) | Highly rigorous causal circuit analysis; not directly comparable |
| 1Njl73JKjB.md — "Towards Principled Evaluations of Sparse Autoencoders" | 7.0 | R1 (strong) | More principled evaluation framework; our paper is less rigorous |
| imT03YXlG2.md — "Sparse autoencoders reveal selective remapping of visual concepts" | 6.5 | R1 (middle) | Most comparable — both apply SAEs to vision transformers. Our paper is more ambitious but less clean methodologically; slightly weaker |
| F76bwRSLeK.md — "Sparse Autoencoders Find Highly Interpretable Features in Language Models" | 4.8 | R1 (middle) | Foundational SAE paper; our paper has more empirical substance in vision domain |
| Ch8s4FdUXS.md — "Unpacking SDXL Turbo" | 4.4 | R1 (middle) | SDXL SAE paper rejected for limited scope; our paper is clearly stronger |
| wZiH43e5Ah.md — "Conceptualize Any Network" | 3.0 | R1 (weak) | Concept extraction framework; our paper is substantially stronger |
| Wxl0JMgDoU.md — "Understanding Skill Adaptation in Transformers Using SAEs" | 2.5 | R1 (weak) | Chess SAE paper; our paper is substantially stronger |

**Round 1 bracket: (5.0, 6.5)**

### Round 2 — Narrowing
Anchors retrieved inside the bracket:

| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| imT03YXlG2.md — "Sparse autoencoders reveal selective remapping of visual concepts" | 6.5 | R2 | Most directly comparable (vision SAE). Our paper is slightly less clean and has more overclaiming issues → below 6.5 |
| 1Njl73JKjB.md — "Towards Principled Evaluations of Sparse Autoencoders" | 7.0 | R2 | More rigorous but different domain (LLMs); our paper has richer empirical findings but less methodological rigor |
| uDIiL89ViX.md — "Towards scientific discovery with dictionary learning" | 5.6 | R2 | Microscopy DL paper with mixed reviews; our paper is comparably ambitious with similar methodological concerns |
| uqxBTcWRnj.md — "Bridging Neural and Symbolic Representations with TDL" | 6.5 | R2 | Different sub-area; not directly comparable |
| 4aJg9e4nvF.md — "What do vision transformers learn?" | 4.75 | R2 | ViT visualization paper with less novelty; our paper is clearly stronger |
| 9dFCm4uZo8.md — "Exploring Compositionality in Vision Transformers" | 5.33 | R2 | ViT compositionality paper of similar ambition; our paper has stronger empirical contributions |
| bkdWThqE6q.md — "A Simple Interpretable Transformer" | 6.0 | R2 | Interpretable-by-design method paper; different contribution type |

The paper is closest in profile to `imT03YXlG2.md` (6.5, vision SAE) but is held back by the two major methodological concerns (SAE constraint confound, 88% R² tension) and overclaiming on Elsewhere concepts and MRH. It is clearly stronger than `4aJg9e4nvF.md` (4.75) and `9dFCm4uZo8.md` (5.33), and slightly stronger than `uDIiL89ViX.md` (5.6). The final score of 5.5 places it below `imT03YXlG2.md` (6.5) due to the unresolved methodological issues, but above the mid-5 rejected papers due to the genuine empirical and theoretical contributions.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>