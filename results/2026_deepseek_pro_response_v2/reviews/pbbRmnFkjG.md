Now I have a clear picture. Let me finalize the review.

**Round 1 bracket**: 6.0 – 7.5  
**Round 2 narrowing**: The paper is clearly stronger than imT03YXlG2 (6.50, SAE for CLIP — narrower scope, less rigorous methodology) and comparable to bVTM2QKYuA (6.75, geometry/ polytope extension of LRH with mixed reviews 8,6,8,5), but below cmXWYolrlo (7.50, geometric invariance hypothesis with stronger theory) and well below 5Ca9sSzuDp (8.00, polished CLIP decomposition with universal 8s). Our paper has more extensive empirical work than bVTM2QKYuA but its MRH proposal is similarly preliminary and the connection between SAE analysis and MRH is loose.

**Final score: 6.5** — the paper makes a substantial empirical contribution (largest vision SAE interpretability effort) with creative methodology, but the MRH framing as the paper's headline contribution outpaces the actual evidence.

---

## Summary

This paper trains a stability-constrained sparse autoencoder (SAE) on DINOv2-B activations to produce a 32,000-atom concept dictionary — the largest such interpretability effort for a vision foundation model. Using this dictionary, the authors analyze how downstream tasks (classification, segmentation, depth estimation) recruit functionally specialized, low-dimensional concept subspaces, revealing task-specific patterns such as "Elsewhere" concepts for classification and distinct monocular depth cue families. They then examine concept geometry and statistics, finding departures from the idealized sparse/near-orthogonal Linear Representation Hypothesis (LRH). Motivated by these departures, they propose the Minkowski Representation Hypothesis (MRH): tokens behave as sums of convex regions around archetypal landmarks, a geometry constructively realized by multi-head attention (Proposition 1), and provide preliminary empirical signals consistent with this picture.

## Strengths

- **Large-scale stable SAE operationalization at unprecedented scale**: The paper trains an SAE with 32,000 atoms on DINOv2-B (d=768, t=261) achieving R² > 88%, with the dictionary constrained to conv(A) to ensure stability. This directly addresses known SAE instability problems (Paulo & Belrose, 2025; Papadimitriou et al., 2025) and represents the largest concept dictionary released for a vision foundation model.

- **Causal depth-cue discovery via controlled perturbations**: Section 3 applies targeted image transformations (median blurring, edge-preserving smoothing, high-pass filtering) that isolate specific monocular depth cues, then measures concept activation changes and clusters them via UMAP. This reveals three functionally interpretable families (projective geometry, shadow-based, frequency-transition cues), providing causal evidence — not mere correlation — that DINOv2 internally encodes interpretable 3D-perception primitives from 2D self-supervised training alone.

- **Positional hypothesis cleanly eliminated**: Section 5 trains linear decoders to predict token coordinates, extracts a positional subspace, and projects tokens orthogonally to it. The finding that PCA organization persists after this projection, combined with positional directions appearing only at intermediate PCs (3–5), rules out the parsimonious alternative that smooth token geometry merely reflects positional encoding.

- **Constructive architectural basis for MRH (Proposition 1)**: The proposition shows that multi-head attention natively produces Minkowski sums — each head outputs a convex combination (softmax over values), and summation across heads yields an activation in the Minkowski sum of projected head polytopes. This follows directly from the attention mechanism and gives the MRH proposal concrete mechanistic grounding rather than merely a phenomenological description.

- **Task-recruited subspaces are quantitatively low-dimensional**: Figure 11 demonstrates that for each task, the eigenvalue spectrum of the top-100 task-aligned concepts decays significantly faster than random subsets from the same dictionary, and intra-task pairwise similarities are higher than random baselines — showing the observed functional specialization is systematic, not cherry-picked.

- **Causal validation of "Elsewhere" concepts**: The paper applies causal masking (Petsiuk et al., 2018) to show that Elsewhere concept activations vanish when the object is removed, ruling out the interpretation that they are merely generic background detectors.

- **Grassmannian baseline via TAAP algorithm**: The DD^T density comparison uses a Grassmannian baseline generated via the TAAP algorithm (Massion & Massart, 2025), providing a principled reference point for testing departures from near-orthogonal LRH geometry rather than relying on random baselines alone.

## Weaknesses

### Fatal
None.

### Major
- **MRH empirical evidence is preliminary and the connection to the earlier SAE analysis is thin**: The paper's three-part structure (task analysis → geometry diagnostics → MRH proposal) is ambitious, but the bridge from the SAE-based concept analysis to the MRH is largely motivational rather than empirically tested. The MRH empirical evidence (Figure 26: geodesic interpolation, Archetypal Analysis vs SAE, code Gram blocks) is preliminary and described only briefly in the main text. Proposition 1 establishes that attention *can* produce Minkowski sums — which follows almost definitionally from softmax and summation — but the central claim that DINOv2's learned representations *do* follow MRH rather than LRH is not directly tested against the 32k-concept SAE dictionary that the paper spent Sections 2–4 building. The paper acknowledges MRH as a "working hypothesis," but the title and framing center MRH while the weight of actual evidence supports the SAE concept analysis. This mismatch between framing and evidence weakens the overall argument.

### Minor
- **Single architecture limits generality**: All experiments use DINOv2-B. While the paper acknowledges this (Section 7), Proposition 1 is grounded in generic attention mechanics — a preliminary demonstration on another ViT variant would strengthen the claim that the observed task specialization and geometric patterns generalize beyond a single model.

- **Depth-cue interpretation relies on post-hoc UMAP clustering**: The perturbation → activation change → UMAP pipeline for identifying monocular cue families is creative, but UMAP is sensitive to hyperparameters and the resulting clusters are interpreted post-hoc. The paper does not discuss stability across UMAP runs or alternative clustering validation methods.

- **"Elsewhere" concept evidence remains qualitative**: While the causal masking experiment is a nice touch, the evidence is presented through a handful of qualitative examples in Figure 2. A quantitative summary (e.g., fraction of classification concepts exhibiting this behavior, average activation change under masking across classes) would strengthen the claim that this is a recurring phenomenon rather than an anecdotal observation.

### Trivial
- The paper occasionally uses phrasing like "we can show" / "we observe" when the detailed supporting evidence (Lemma 1, Lemma 2, Figure 26 details) is in stripped appendices. Brief inline summaries of key appendix results would improve standalone readability.

## Nice-to-Haves
- Testing MRH predictions directly against the SAE dictionary — e.g., checking whether SAE concept atoms cluster into convex polytopes whose Minkowski sum approximates token activations — would close the loop between the paper's two major contributions and dramatically strengthen the narrative.
- Quantitative metrics for the "Elsewhere" phenomenon across all ImageNet classes would move this from anecdotal to systematic.
- A second ViT architecture (e.g., DINOv2-S or a CLIP-pretrained ViT) would test generalizability.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Strength Finder item about Archetypal Analysis outperforming SAE**: The AA vs SAE comparison is referenced at Figure 26, which is in a stripped appendix. While the paper describes this result in the main text (line 163), the evidence cannot be verified from the provided materials. This point was folded into the major weakness about MRH evidence being preliminary.

- **Strength Finder generic claims**: Removed strengths that were merely restatements of the paper's goals ("this paper addressed an important problem," "this paper targeted an interesting question") without concrete, verifiable evidence. Also removed the "Archetypal Analysis outperforms SAE" as a standalone strength — kept only as part of the broader MRH empirical evidence context.

- **Harsh Critic input**: The harsh critic output was truncated (only a grep preamble was provided), so no harsh critic weaknesses were available to filter. All weaknesses were derived from direct reading of the paper.

## Novel Insights
None beyond the paper's own contributions. The paper's most original observation is the connection between multi-head attention's operational mechanics and Minkowski sum geometry (Proposition 1), which reframes attention composition in geometric terms. However, Proposition 1 is largely definitional — it follows directly from softmax producing convex combinations and multi-head summation — so its novelty lies in the reframing rather than in a deep theoretical discovery.

## Suggestions
- Reframe the paper to center the SAE concept dictionary and task analysis as the primary contribution, with MRH as an exploratory direction. This would better match the actual evidence distribution and avoid the title/ content mismatch.
- Add a quantitative summary table for the "Elsewhere" concept phenomenon: per-class masking effect sizes, fraction of top concepts exhibiting the pattern.
- Discuss UMAP stability for the depth-cue clustering: report results across multiple UMAP runs or use alternative clustering validation.
- If space permits, include a brief inline summary of Lemma 1, Lemma 2, and the Figure 26 results in the main text rather than relying entirely on appendix references for key MRH evidence.

---

## Calibration Summary

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| SAE scaling | tcsZt9ZNKD | 1.75 | R1 | Not comparable (NLP SAE scaling, outlier scores) |
| SAE chess transformers | Wxl0JMgDoU | 2.50 | R1 | Weaker; narrow domain-specific SAE application |
| SAE circuit analysis | 89wVrywsIy | 3.40 | R1 | Weaker; less comprehensive methodology |
| Concept extraction CAN | wZiH43e5Ah | 3.00 | R1 | Weaker; less rigorous concept framework |
| SAE CLIP ViT adaptation | imT03YXlG2 | 6.50 | R1, R2 | **Most comparable**; similar SAE-for-ViT approach but narrower scope, less rigorous SAE. Our paper is stronger. |
| SAE SDXL Turbo | Ch8s4FdUXS | 4.40 | R1 | Weaker; limited scope, single architecture, qualitative |
| SAEs not canonical | 9ca9eHNrdH | 7.00 | R1 | Stronger; crisp theoretical contribution |
| SAE compute optimal | ghH6YYDs15 | 4.67 | R1 | Less relevant; theoretical SAE analysis |
| Sparse Feature Circuits | I4e82CIDxv | 8.00 | R1 | Stronger; polished, comprehensive, strong applications |
| CLIP text decomposition | 5Ca9sSzuDp | 8.00 | R1 | Clearly stronger; well-executed, universal 8s |
| ViT registers | 2dnO3LLiJ1 | 8.00 | R1 | Stronger; clean insight, broad impact |
| Transformer reasoning | STUGfUz8ob | 7.60 | R1 | Stronger; deeper theoretical results |
| Geometry features LLMs | bVTM2QKYuA | 6.75 | R2 | **Highly comparable**; also extends LRH with polytope geometry, mixed reviews. Our paper has more extensive empirical work but similar hypothesis-preliminary-evidence structure. |
| Geometric Inductive Biases | cmXWYolrlo | 7.50 | R2 | Stronger; deeper theory, more focused experiments |
| RSVC similarity | ih3BJmIZbC | 6.80 | R2 | Comparable quality; concept-based interpretability |
| Dictionary learning microscopy | uDIiL89ViX | 5.60 | R2 | Weaker; narrower domain application |
| TDL framework | uqxBTcWRnj | 6.50 | R2 | Comparable; dictionary learning with symbolic knowledge |
| MLSAE | XAjfjizaKs | 6.50 | R2 | Comparable; SAE methodology contribution |
| Task structure geometry | k9t8dQ30kU | 6.75 | R2 | Less directly comparable; learning dynamics |
| Unified representation space | FrFQpAgnGE | 7.00 | R2 | Slightly stronger; cleaner contribution |
| Visual info VLMs | chanJGoa7f | 7.00 | R2 | Slightly stronger; more focused analysis |

**Round 1 bracket**: 6.0 – 7.5 (between imT03YXlG2 at 6.50 and 5Ca9sSzuDp at 8.00).

**Round 2 narrowing**: The paper sits closest to bVTM2QKYuA (6.75) — both propose geometric extensions of LRH with preliminary evidence — but our paper has substantially more extensive empirical work (32k dictionary, 3-task analysis, geometry diagnostics) while sharing the weakness of a hypothesis that outpaces its empirical grounding. It is clearly stronger than imT03YXlG2 (6.50, narrower SAE analysis) and clearly below cmXWYolrlo (7.50, stronger theory). **Final score: 6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>