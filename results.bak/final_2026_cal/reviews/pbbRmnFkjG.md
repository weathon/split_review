Now I have a solid calibration understanding. Let me write the final consolidated review.

## Summary

This paper presents a large-scale empirical study of DINOv2's internal representations using a stable sparse autoencoder (RA-SAE) to extract a 32,000-unit concept dictionary. The study proceeds in three parts: (1) analysis of task-specific concept recruitment, revealing "Elsewhere" concepts for classification, border detectors for segmentation, and three families of monocular depth cues; (2) geometric and statistical characterization of the dictionary, documenting departures from the idealized Linear Representation Hypothesis (higher coherence, sharp spectral decay, antipodal pairs, distributed atoms); and (3) proposal of the Minkowski Representation Hypothesis (MRH), where tokens behave as Minkowski sums of convex regions around archetypal landmarks, grounded in the multi-head attention mechanism. The paper releases the concept dictionary as an interactive visualization tool.

## Strengths

1. **Rich, methodical empirical study of task-specific concept organization.** Section 3 and Figure 11 provide converging quantitative evidence that classification, segmentation, and depth estimation recruit distinct, low-dimensional concept subspaces with measurable geometric signatures (higher intra-task cosine similarity, faster eigenvalue decay). The identification of "Elsewhere" concepts (off-object firing that disappears under causal masking), border detectors for segmentation, and three monocular depth cue families (projective, shadow, frequency) constitutes genuinely novel descriptive findings about how DINOv2 organizes knowledge.

2. **Systematic geometric diagnostics of departures from LRH.** Section 4 thoroughly characterizes the dictionary's inner-product distribution (heavier tails than random and Grassmannian baselines), singular-value spectrum (sharp decay), Hoyer scores (distributed atoms), and the weak correlation between co-activation and geometric affinity (Z^T Z vs. D D^T). These measurements are reproducible, well-baselined, and provide concrete evidence for the paper's central empirical claim that DINOv2's representations are not purely sparse and near-orthogonal.

3. **Clean positional encoding analysis.** Section 5 shows that per-image PCA structure is not reducible to positional information: projecting tokens orthogonally to the learned positional subspace leaves the PCA organization largely intact, and positional directions appear only in intermediate PCs. This convincingly rules out a trivial explanation and points to genuine semantic/archetypal structure.

4. **Proposition 1 connects MRH directly to the multi-head attention mechanism.** The proof that multi-head attention outputs are Minkowski sums of convex combinations per head is a genuine theoretical insight that ties the proposed geometry to the known computation of the architecture, not merely to post-hoc analysis.

5. **Resource contribution.** The 32,000-concept dictionary released as an interactive visualization (Appendix L) is a concrete tool for the research community, supporting the claim of scale beyond prior vision interpretability efforts.

## Weaknesses

### Major

1. **The Minkowski Representation Hypothesis receives disproportionate narrative weight relative to its empirical support.** The paper's title ("Into the Rabbit Hull: From Task-Relevant Concepts in DINO to Minkowski Geometry"), abstract, and contribution list give MRH roughly equal billing to the well-supported empirical findings. However, the evidence for MRH is limited to three preliminary tests (k-NN geodesics, Archetypal Analysis reconstruction, block structure in the Gram matrix) that are each consistent with many alternative geometric hypotheses (low-dimensional manifold, soft clustering, capsule-like routing). The paper acknowledges MRH as a "working hypothesis" in the text, but the title and framing do not reflect this provisional status. Proposition 1 shows that multi-head attention *can* realize MRH, but does not show that the *learned* activations *do* satisfy the strong structural conditions of Definition 1 (few active tiles, block-convex codes). This is not a fatal issue—the empirical contributions stand on their own—but the paper would be strengthened by clearly separating the well-supported empirical core from the speculative MRH proposal, e.g., by moving MRH to a forward-looking discussion section or adjusting the title.

2. **The SAE's geometric properties may partially reflect training procedure artifacts, and this threat is not discussed.** The stable SAE enforces non-negative codes, k=8 sparsity, and a convex-hull constraint on atoms. Each injects strong inductive biases: antipodal pairs (cos ≈ -1) are a known side effect of non-negative sparse coding where atoms must flank data to represent anticorrelated features; higher coherence than random/Grassmannian baselines could reflect the convex-hull constraint forcing atoms inside the data convex hull, naturally increasing similarity. The baselines (random, Grassmannian) do not share these constraints, so the observed "departures from LRH" may partly reflect SAE *design* rather than DINOv2's intrinsic geometry. This does not invalidate the findings, but the paper should discuss this confound explicitly rather than remaining silent on it.

### Minor

3. **The depth cue family analysis is qualitatively identified.** The three monocular cue families (projective, shadow, frequency) are derived via UMAP visualization and hand inspection of perturbation responses. No quantitative validation (e.g., statistical significance of differential responses across perturbation types, or clustering stability measures) is provided. The claims would be strengthened by showing that perturbations affect each family differentially in a measurable, statistically significant way.

4. **No limitations section.** The paper lacks a systematic discussion of its own limitations: the single architecture (DINOv2-B), the SAE's inductive biases, the preliminary nature of MRH validation, and the qualitative nature of some analyses (depth cue families, border concept clustering). While the Discussion section mentions "focused on a single architecture," this is minimal for a paper making broad claims about representation geometry.

5. **The "Elsewhere" concept interpretation is stronger than the evidence warrants.** The paper claims these concepts "implement learned negation" or "conditional negation." The evidence (off-object firing that disappears under causal masking) is consistent with several interpretations—distributed off-object evidence, background statistics contingent on object presence, or simple foreground-background contrast. The paper does acknowledge "another interpretation being distributed off-object evidence" in the Figure 2 caption, but the narrative throughout treats the negation framing as a substantive discovery. This is a modest overinterpretation.

### Trivial

6. The claim about "largest interpretability demonstration for a vision foundation model to date" depends on a demo that will be released upon acceptance and cannot be assessed at review time. Remove this claim or provide in-paper evidence.

7. The linear probe projection method for quantifying concept importance is deferred to the appendix; a short main-text description would improve readability.

## Nice-to-Haves

- A control comparing Gram spectrum decay to a null model conditioned on the sparsity pattern and marginal frequencies of Z (not just shuffled baselines).
- Showing that similar geometric properties hold when using a different dictionary learning method (e.g., a vanilla SAE with stability checks, or direct spectral analysis of activations without dictionary factorization).
- A direct test of whether per-image activation sets admit a sparse Minkowski decomposition over head polytopes by examining intermediate-layer activations or attention weights.

## Removed Points

- **Criticism about "largest interactive interpretability demo" not being assessable** (Harsh Critic, Section 1): This is valid in the sense that the demo isn't available at review time, but the paper states it will be released upon acceptance. The resource contribution is real. I've downgraded this to a trivial weakness above rather than treating it as a major flaw. The demo claim should be tempered, but it doesn't undermine the paper.

- **Criticism that Proposition 1 is trivial ("any transformer satisfies this")** (Harsh Critic, Section 6): This misreads the contribution. Proposition 1 shows that MRH is *realizable* by the architecture, not that any transformer empirically satisfies its strong form. This is a legitimate theoretical grounding for the hypothesis, and the paper does not overclaim it.

- **Criticism that the Gram block structure is vague** (Harsh Critic, Section 6): The paper observes block structure in the empirical Gram matrix, consistent with MRH. The criticism that "any sparse code with grouped co-stimulation will show block structure" is correct but this is precisely what MRH predicts. The test is weak but not invalid—it's a necessary-condition check.

- **Strength Finder claim about "largest interactive interpretability demo"** (Strength Finder, Core strength 3): This is an artifact of unverifiable claims at review time. The resource is a genuine strength but the "largest" qualifier should be tempered.

- **Strength Finder claim about "conditional negation" providing "intervention-based evidence"** (Strength Finder, Supporting strength 3): This overstates what the causal masking experiment shows. The paper's own Figure 2 caption uses careful language ("suggestive of a causal effect," "another interpretation being distributed off-object evidence"), which is more measured than the Strength Finder's framing.

## Novel Insights

None beyond the paper's own contributions. The reviewers' analyses largely recapitulate the paper's strengths and weaknesses without adding a novel synthesized insight that goes beyond what the authors themselves present. The most useful observation from the reviews is the SAE artifact concern (Weakness 2 above), which the paper itself does not discuss—this is a genuine blind spot that the harsh critic identified and that deserves author attention.

## Suggestions

1. **Rebalance the narrative.** Move MRH to a clearly separable position (e.g., a forward-looking Section 6 clearly labeled as a hypothesis with preliminary evidence), and adjust the title to reflect that MRH is a proposed hypothesis (e.g., "Toward a Minkowski Representation Hypothesis" or dropping MRH from the title entirely).

2. **Add a Limitations section** discussing: (a) single-architecture focus; (b) SAE inductive biases as potential confounds; (c) preliminary nature of MRH evidence; (d) qualitative nature of depth cue family identification; (e) lack of human evaluation for concept interpretability.

3. **Quantity the depth cue family analysis** with statistical tests showing that the three clusters respond differentially to controlled perturbations.

4. **Tone down the "Elsewhere" concept claims.** Replace "implementing conditional negation" with language more commensurate with the evidence, e.g., "suggestive of a form of off-object evidence that depends on object presence."

## Score and Decision

**Calibration round 1 (bracketing):** Searched for "sparse autoencoder vision transformer interpretability concept dictionary." Low band (<3.5) returned papers scoring 1.5–3.33 (rejected/withdrawn). Middle band (3.5–7.5) returned papers scoring 4.0–6.0 (mix of rejects and poster accepts). Top band (>7.5) returned papers scoring 8.0 but on unrelated topics (text-to-3D, RL, visual geometry). Initial bracket: 4.5–7.0.

**Calibration round 2 (narrowing):** Searched for "vision foundation model interpretability geometric representation analysis" and "mechanistic interpretability vision transformer concept discovery" within (5.5, 7.5). Retrieved anchors at 6.0–6.5 on related interpretability topics. Compared the paper under review to these anchors:
- *On the Limits of SAEs* (6.0, Poster): Clear theoretical contribution with limited empirical scope. The current paper has richer empirical breadth but weaker theory.
- *Uncovering Conceptual Blindspots Using SAEs* (6.0, Poster): Application-focused SAE analysis. The current paper is more original in its geometric hypothesis.
- *Latent Concept Disentanglement in Transformer-based LMs* (6.5, Poster): Strong controlled-experiment analysis on simpler tasks. The current paper tackles a messier real model with commensurate methodological rigor.
- *Hierarchical Concept-based Interpretable Models* (6.0, Poster): Methodological contribution with standard evaluation. The current paper has more novel descriptive findings.
- *M-CBM* (5.5, Poster): Pipeline paper with limited novelty. The current paper is more original.

The paper under review is stronger in empirical breadth and originality than most 6.0 anchors, while its weaknesses (MRH over-weighting, SAE artifact silence) prevent it from reaching the 7+ tier. I place it at **6.5**.

All anchors retrieved:
| Anchor ID | Score | Round | Comparison |
|---|---|---|---|
| tWe5owhOyU | 2.0 | R1 | Weak SAE paper, much weaker |
| cPesWJLEAG | 3.0 | R1 | Withdrawn, much weaker |
| Rngn25PSdd | 1.5 | R1 | Rejected, much weaker |
| Vk7IDXKgX3 | 3.33 | R1 | Withdrawn, much weaker |
| BXzUi2QZ7z | 4.0 | R1 | Rejected ViSAE, weaker empirical contribution |
| gdEWoxhb70 | 5.5 | R1 | M-CBM, pipeline contribution, less original |
| rxiWsoM6Cx | 4.0 | R1 | Withdrawn, weaker |
| DjefrO8TJr | 5.0 | R1 | Sparse CLIP, similar quality but simpler contribution |
| DSOTgzeH3w | 6.0 | R2 | SAE theory paper, cleaner theory but less empirical breadth |
| NHP2Y8IVMU | 5.5 | R2 | IVPT, similar quality but narrower scope |
| h61OIERd38 | 6.0 | R2 | HiCEM, similar tier but less original findings |
| k3SEVOW2Dg | 6.5 | R2 | Latent concept disentanglement, comparable quality |
| 2sNrnTTEcv | 6.0 | R2 | Conceptual blindspots, similar tier but different domain |
| VSPLa2Sito | 6.0 | R2 | CAVE, similar tier but different topic |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>