---
job_id: a993eec7-0aff-4d0c-b668-5ca865b2e0e8
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: pbbRmnFkjG.pdf
paper: Into the Rabbit Hull: From Task-Relevant Concepts in DINO to Minkowski Geometry
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, centered on representation learning, sparse coding, interpretability of learned representations, and geometric analysis of vision transformer features.

## Minimum Quality
Pass ✅. The paper contains an abstract, introduction, methodological setup, substantial empirical analysis, qualitative and quantitative results, and a discussion; while I have concerns about overclaiming and incomplete validation, these rise to the level of reviewable weaknesses rather than desk-reject flaws.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden instructions, suspicious reviewer-directed text, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies the internal representation structure of DINOv2-B by training a stable sparse autoencoder over final-layer token activations, producing a 32k-concept dictionary that the authors use to analyze how downstream tasks recruit concepts. The paper reports task-specific patterns, including “Elsewhere” concepts for classification, boundary-focused concepts for segmentation, and three families of monocular depth cues for depth estimation, together with several geometric diagnostics of the learned dictionary and token manifolds. Motivated by departures from a purely sparse, near-orthogonal view, the paper then proposes the Minkowski Representation Hypothesis (MRH), a working hypothesis that interprets token representations as sums of convex regions associated with archetypal landmarks.

## Strengths
1. The paper is ambitious in scope and unusually rich in empirical probing. Training a 32k-concept SAE over DINOv2 token activations and then using that dictionary to examine task specialization, token-type specialization, and geometric structure is a meaningful systems-level analysis that many readers in representation learning and interpretability will find valuable.

2. The paper is at its strongest when it stays empirical and descriptive. In particular, the task-specific analyses are interesting and often visually compelling. **Figure 2** provides a clear qualitative contrast between the classification-side “Elsewhere” concepts and the segmentation-side border concepts, and **Figure 3** offers an intuitively organized view of depth-related concept families. Even if some interpretations remain somewhat speculative, these figures make a plausible case that downstream tasks draw on different parts of the learned dictionary.

3. The dictionary-level geometry analysis is broad and thoughtful. **Figure 4** combines multiple diagnostics, conditional energy versus firing count, Gram-spectrum behavior, coherence comparisons, singular values, and Hoyer scores, and collectively argues that the learned concept space is neither a simple neuron-aligned basis nor a fully incoherent Grassmannian-style packing. This is a useful empirical contribution regardless of whether one accepts the later MRH framing.

4. The paper goes beyond semantic concept discovery and examines token roles. The register-only / cls-only / spatial-token analyses in **Figures 14-17** are interesting and suggest that concept specialization is tied not only to semantic content but also to architectural token function. This is a nice addition that differentiates the work from purely class-centric concept analyses.

5. The authors are commendably careful, in a few places, to phrase MRH as a “working hypothesis” rather than an established theory. That restraint matters. **Figure 26** is particularly useful in this regard: it does not prove MRH, but it does present several empirical patterns that are at least compatible with a convex/archetypal view.

6. Presentation is generally strong from a visual communication standpoint. **Figure 1** does a good job of introducing the paper’s central theme, namely that different tasks recruit distinct regions of concept space. The figures are numerous, varied, and in many cases helpful for understanding the authors’ intended interpretation.

## Weaknesses
1. The paper’s central transition, from descriptive concept analysis to the Minkowski Representation Hypothesis, is not sufficiently supported by the evidence in the main paper. Up through Sections 3-5, the paper presents interesting observations about SAE concepts and token geometry. But the jump in **Section 6** to MRH is much larger than the evidence warrants. The core proposition, **Proposition 1 on Page 9** and its appendix version **Proposition 3**, mostly formalizes the elementary fact that attention outputs convex combinations of values and sums them across heads. That fact is true, but it is quite a long way from showing that the actual learned activation set of DINOv2 is well modeled by a sparse sum of head-specific convex polytopes with meaningful “tiles.” In particular, the proposition assumes fixed per-head value sets and a reachability condition for the simplex interior, whereas in real transformers the values themselves are input-dependent and the full block includes residual streams and MLPs. So the theory here is more of an existence-compatible argument than a model-specific explanation. That matters because the paper’s headline framing pushes readers toward a geometry-level reinterpretation of DINOv2, yet the main evidence is still observational and indirect.

2. Several empirical claims are stronger than what the presented evidence can justify, and the paper too often treats suggestive visual patterns as mechanistic conclusions. For example, the “Elsewhere” interpretation in **Figure 2 (left)** and expanded **Figure 8** is interesting, but the paper phrases it as implementing learned negation or fuzzy spatial logic. The actual evidence shown is that certain concepts activate off-object and disappear under object removal. That supports conditional dependence, but it does not uniquely imply negation as opposed to other forms of context-sensitive coding, distributed evidence, or suppression patterns. Similarly, the claim in **Figure 5** that “PCA is a linear operator, it cannot fabricate curvature” is rhetorically striking but not actually sufficient to support the broader conclusion being drawn. Per-image PCA colorings can reveal smooth variation, but they do not by themselves establish low-dimensional convex interpolation structure. The paper repeatedly converts “compatible with” into “suggesting a dedicated mechanism,” and that overreach weakens the scientific value.

3. The quantitative evaluation is underdeveloped for a paper making this many strong claims. A notable issue is the near absence of standard results tables in the main paper. There is no table summarizing reconstruction quality versus baselines, no table quantifying stability across SAE runs, no table summarizing the strength and variance of the task-alignment findings, and no compact quantitative comparison of MRH-related diagnostics. Instead, the paper relies heavily on visual figures and narrative interpretation. This is not merely a stylistic preference. It makes it difficult to assess effect sizes, uncertainty, robustness, and whether the findings are systematic or cherry-picked. For instance, **Figure 11** claims that intra-task concepts are more aligned and lie in lower-dimensional subspaces than random subsets, which is an important result, but the main paper does not provide statistical confidence intervals, sensitivity to the “top-100” cutoff, or comparisons across multiple probe trainings. Given that the paper’s contribution is largely empirical, the lack of more standard quantitative summarization is a real limitation.

4. The paper does not sufficiently benchmark its SAE operationalization choices, even though many conclusions depend on them. On **Page 4**, the factorization is specified with nonnegative, \(k\)-sparse codes and a dictionary constrained to an approximate convex hull, using \(c=32000\), \(k=8\), 128k centroids, and a single-layer encoder with BatchTopK. These are consequential design choices, yet the main paper provides essentially no ablation on dictionary size, sparsity level, centroid approximation quality, or comparison against more standard SAE variants. The claim that the learned dictionary is “stable” is inherited from prior work rather than demonstrated in the main paper. Since much of the paper’s argument rests on interpreting the geometry of the learned dictionary \(D\), the reader needs stronger evidence that the observed geometry is not an artifact of this very specific constrained SAE setup. Without this, it is hard to know whether the reported departures from LRH reflect DINOv2 itself, or the geometry induced by the chosen dictionary-learning method.

5. There are important notation and mathematical clarity issues that make parts of the paper harder to trust than they should be. The main dictionary-learning objective on **Page 4** is
\[
\min_{Z,D}\|A-ZD\|_F^2 \quad \text{s.t. } Z\ge 0,\ \|Z_i\|_0\le k,\ D\in \mathrm{conv}(A),
\]
which is fine at a high level, but several downstream definitions become muddled. In **Appendix C.1 (Pages 21-22)**, the paper switches notation between \(k\), \(c\), and class count in a confusing way: \(Z\in\mathbb{R}^{nt\times k}\), \(D\in\mathbb{R}^{k\times d}\), \(W\in\mathbb{R}^{c\times d}\), \(W' \in \mathbb{R}^{k\times c}\), and then \(\phi=\mathbb{E}(Z)W'\in\mathbb{R}^c\). This is dimensionally repairable, but the overloading of \(c\) and \(k\) is sloppy and makes the theoretical justification of “concept importance” harder to follow than necessary. Likewise, in **Appendix B.1 (Page 20)**, the unified dictionary-learning objective writes \(A \approx ZD^T\) after earlier adopting the row-atom convention \(A \approx ZD\); the text acknowledges conventions, but the presentation still becomes inconsistent. These are not fatal algebraic errors, but they matter in a paper that leans heavily on geometric and theoretical interpretation.

6. Some theoretical statements are either too informal or technically shaky in the way they are connected back to actual transformers. A concrete example is **Lemma 2 / Page 41**, which states that affine maps preserve MRH structure and then comments that “many norm become affine in evaluation, once mean/variance are held fixed.” This is, at best, a very loose statement in the context of LayerNorm/RMSNorm, whose normalization factors remain input dependent in the usual transformer computation and are not simply fixed affine maps on arbitrary activations. Since the paper invokes these results to argue that archetypal structure propagates through realistic transformer blocks, such shortcuts matter. More broadly, **Proposition 2 / Page 9** on non-identifiability is mathematically fine as a generic statement about Minkowski decompositions, but it does not actually help validate MRH for DINOv2; it mainly says that if one adopts this view, decomposition from final activations alone is ill-posed. This further underscores that the theory is presently explanatory framing rather than supported characterization.

7. The evidence for low-dimensional token geometry is visually attractive but not well controlled against alternative explanations. **Figures 5, 18-25** show per-image PCA maps with smooth object-aligned color transitions, and **Figures 24-25** attempt to remove positional effects. This is suggestive, but there are multiple unresolved issues: per-image PCA can induce visually smooth maps even when the underlying geometry is not especially special; the removal of a learned positional basis is only one confound; and the paper does not quantify how much of the effect remains under stronger controls or across layers and datasets. The statement on **Page 8** that the representation is “not purely relative” because of alignment across similar images in **Figure 5** is especially under-argued. The figures are nice, but the paper asks them to carry too much conceptual load.

8. The paper’s positioning relative to LRH is occasionally muddled. In several places the authors say they do not claim to “contradict” LRH, but the narrative still repeatedly frames the empirical findings as challenging a “purely sparse, near-orthogonal” picture. The issue is that the implemented SAE already imposes convex-hull and nonnegativity constraints that are not neutral with respect to geometry. So when the paper observes heavier-tailed coherence or sharp singular value decay in **Figure 4**, it is not entirely clear how much should be attributed to DINOv2’s intrinsic representation versus the representation recovered by this particular SAE. To convincingly argue for a shift away from LRH, I would want a stronger separation between properties of the model activations \(A\) and properties induced by the chosen factorization \((Z,D)\).

9. The exposition is vivid and engaging, but sometimes too blog-like for a paper making substantial theoretical claims. Terms such as “into the rabbit hull,” “fuzzy spatial logic,” “passport-like concepts,” and “the shape of an image” make the paper memorable, but they also occasionally blur the line between metaphor and scientific claim. This is not a style complaint for its own sake. In a paper that already pushes beyond the evidence at several points, a more disciplined separation between observation, interpretation, and conjecture would improve clarity and credibility.

## Questions
1. The paper’s main scientific risk is that many conclusions may depend heavily on the particular SAE formulation. Could the authors provide main-paper evidence, not just appendix discussion, on the robustness of the core findings to SAE design choices? In particular, how stable are the task-specific subspaces in **Figures 1 and 11** and the dictionary-geometry conclusions in **Figure 4** when varying \(c\), sparsity \(k\), or removing the convex-hull constraint on \(D\)? If the main claims persist across such variants, my confidence would increase substantially.

2. For the “Elsewhere” concepts, what exactly is the quantitative criterion for calling a concept “Elsewhere,” and how common are such concepts across classes and seeds? **Figures 2 and 8** are compelling examples, but they remain example-driven. A rebuttal that includes a class-level prevalence statistic, an automatic detector, and a comparison against alternative interpretations such as generic context dependence or background suppression would materially strengthen this part of the paper.

3. The theoretical move from attention convexity to MRH seems too quick. Can the authors clarify what in their view is genuinely model-specific evidence for MRH, beyond the generic fact that attention outputs convex combinations of values? For example, is there direct evidence at the per-head level that the relevant codes are block-convex in the sense of **Definition 1**, rather than merely sparse in some post hoc archetypal fit?

4. The paper repeatedly argues for low-dimensional task-recruited subspaces using **Figure 11**. Could the authors report sensitivity of these spectra and pairwise-similarity histograms to the choice of top-\(N\) concepts, probe initialization, and dataset split? Right now the results look plausible, but it is hard to judge robustness from the main paper.

5. On the mathematical side, please clean up the notation around the concept-importance derivation in **Appendix C.1**. As written, \(k\), \(c\), and class count are overloaded enough to create confusion. A precise restatement with consistent dimensions would help. Also, please clarify whether the attribution equivalence claims require any assumptions beyond linearity of the probe and fixed concept basis.

6. For the positional-basis removal experiment in **Figures 24-25**, can the authors provide a quantitative metric of how much “smooth structure” remains after projection, rather than relying mainly on qualitative maps? For example, neighborhood preservation, manifold dimension estimates, or cross-image alignment metrics before and after removal would help evaluate whether the effect is genuinely non-positional.

7. A more mundane but important question: why are there essentially no compact quantitative tables in the main paper? For a paper with many empirical claims, a table summarizing reconstruction, stability, task-subspace metrics, and MRH-support metrics would make the work easier to assess and much stronger.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None beyond ordinary considerations for releasing interpretability tools. The paper studies representations in a pretrained vision model and does not introduce a new deployment-facing system or sensitive human-subject protocol in the main paper.

## Soundness Rating
3: good. The paper contains a substantial amount of careful empirical work and some mathematically correct observations, but several central interpretive claims, especially around MRH and mechanistic conclusions from visual evidence, are not fully supported at the strength stated.

## Presentation Rating
3: good. The paper is visually strong and generally readable, but notation is inconsistent in several mathematical sections, and the writing sometimes slips from empirical observation into metaphor-driven overinterpretation.

## Contribution Rating
3: good. The large-scale concept analysis of DINOv2 and the task-specialization findings are worthwhile contributions to the interpretability and representation-learning community, even though the proposed geometric reframing currently feels more like an interesting hypothesis than a validated new theory.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The empirical analysis is broad, interesting, and likely valuable to the community, and I do think there is a real contribution here. However, the paper overreaches in places, under-quantifies several key claims, and does not yet convincingly establish the stronger geometric interpretation that it foregrounds.

## Reviewer Confidence
4: confident. I am confident in this assessment and checked the main technical and empirical claims carefully, though some of the appendicial geometric arguments and implementation details would still benefit from author clarification.