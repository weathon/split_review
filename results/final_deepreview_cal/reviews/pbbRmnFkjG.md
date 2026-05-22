Now I have enough calibration data. Let me write the final consolidated review.

## Summary

This paper trains a 32,000-concept sparse autoencoder on DINOv2-B activations (using a stable SAE with convex-hull constraints) and uses it to analyze how downstream tasks recruit different concept subsets, characterize the geometry of the concept space, and propose the Minkowski Representation Hypothesis (MRH). The three main contributions are: (1) task-specific functional specialization findings — "Elsewhere" concepts for classification, border concepts for segmentation, and monocular depth cue families for depth estimation; (2) a systematic geometric characterization showing the dictionary departs from a purely sparse, near-orthogonal ideal; and (3) a formal proposal of MRH as a geometric hypothesis where tokens lie in Minkowski sums of convex polytopes, with theoretical grounding in multi-head attention.

## Strengths

- **Task-specific functional specialization at scale.** The paper identifies three distinct families of concepts selectively recruited by different tasks — Elsewhere concepts for classification (with causal masking evidence), border detectors forming coherent subspaces for segmentation, and three families of monocular depth cues (projective, shadow-based, frequency-based) for depth estimation. This goes beyond generic concept attribution to show how specific representations are recruited by specific tasks, enabled by the large dictionary.

- **Systematic quantitative characterization of geometry.** The paper provides concrete geometric diagnostics against multiple baselines (random, Grassmannian, shuffled): dictionary coherence with heavier tails (Figure 4A), sharply decaying singular-value spectrum (Figure 4B), low Hoyer scores confirming distributed atoms (Figure 4C), and antipodal pairs forming signed axes (Appendix G). These analyses are thorough and directly challenge a purely sparse, near-orthogonal view.

- **Theoretical grounding of MRH in attention mechanics.** Proposition 1 formally connects multi-head attention to Minkowski sums — each head produces convex combinations, and summing heads yields a Minkowski sum. Proposition 2 proves the non-identifiability of Minkowski decomposition from final activations alone, a useful negative result for interpretability. This theoretical scaffolding is clean and connects to known literature on convex conceptual spaces.

- **Rigorous ruling out of positional confounding.** Section 5 carefully shows that projecting tokens orthogonally to the positional subspace leaves PCA organization largely unchanged (Figure 25), and positional directions typically appear only among intermediate PCs (PCs 3–5 in Figure 24). This experimentally eliminates the simplest alternative explanation for the smooth token geometry.

- **Stable SAE design with in-distribution guarantee.** The RA-SAE constraint (atoms in convex hull of real activations, via 128k k-means centroids) yields R² > 88% reconstruction while addressing reproducibility issues that plagued prior SAE interpretability work. This methodological care strengthens the empirical foundation.

## Weaknesses

### Major

- **The concept dictionary is trained exclusively on ImageNet-1k activations, which limits the task-comparison analysis.** The SAE is trained on DINOv2 patch-token activations from 1.4M ImageNet-1k images (Section 2). The subsequent analysis then asks which of these 32k concepts are recruited by classification (ImageNet-1k), segmentation (ADE20k), and depth estimation (NYU Depth). This creates a coverage bias: concepts useful for segmentation or depth that are rare or absent in ImageNet natural images will never appear in the dictionary. The qualitative findings (Elsewhere, border, monocular cue concepts) are partially robust because they are verified through visual inspection and perturbation analysis, but the quantitative claim that segmentation and depth use "more compact, localized regions" of the concept space (Figure 1, Figure 11) could be driven by dictionary coverage rather than genuine representational properties. The paper does not discuss this limitation. A control experiment — retraining the SAE on a more diverse image set or training probes on original (not SAE-reconstructed) embeddings — would substantially strengthen the evidence.

### Minor

- **The Minkowski Representation Hypothesis is presented as a central contribution but its empirical support is thin.** The paper's title, framing, and structure place substantial weight on MRH. Yet the direct empirical tests (straight-line vs. k-NN geodesics, Archetypal Analysis matching SAE, Gram block structure) are confined to three brief paragraphs with all figures in the appendix (Figure 26). These observations are consistent with MRH but also with other sparse, locally linear models. The paper is transparent that MRH is a "working hypothesis" and the implications section begins with "If, and this is an assumption," but the narrative momentum still positions MRH as a primary destination rather than a speculation. The theoretical account (Proposition 1) shows that attention *can* realize MRH, not that DINOv2 *does*. Stronger tests — e.g., verifying that tokens are exact Minkowski sums of identifiable head polytopes via attention weights — would be needed to elevate MRH from hypothesis to finding.

- **Qualitative taxonomies rely on cherry-picked examples and limited quantitative validation.** The Elsewhere concept's "conditional negation" claim (Figure 2) is supported only by a brief mention of causal masking without quantitative results. The monocular cue clusters (Figure 3) are derived via UMAP on perturbation responses, which is exploratory and can produce spurious groupings. The paper would be stronger with quantitative clustering validation (e.g., silhouette scores, stability across SAE training seeds or perturbation strengths) and baseline checks showing random perturbations do not produce similar clusters.

- **The causal evidence for Elsewhere concepts is suggestive but incomplete.** The paper states these concepts "disappear when the object is removed (via causal masking), providing evidence suggestive of a causal effect realizing conditional negation." A perturbation study showing that upweighting an Elsewhere concept changes classifier output in a specific direction (e.g., reducing confidence for the corresponding class) would substantially strengthen this interpretation.

### Trivial

- The claims about "largest interpretability demonstration for a vision foundation model to date" and the "interactive demo" are presentation choices better suited for a project page than the paper's scientific claims.
- The comparison between co-activation (ZᵀZ) and geometry (DDᵀ) is noted to have a guaranteed positive correlation proportional to tr(AᵀA) (Footnote 1), which the paper correctly acknowledges but could discuss more upfront.

## Nice-to-Haves

- Comparing against an unconstrained SAE or sparse PCA to rule out the possibility that the observed geometric departures from LRH (higher coherence, sharp spectral decay) are artifacts of the SAE's convex-hull constraint rather than intrinsic to DINOv2's representation.
- Adding a dedicated limitations section that acknowledges the ImageNet-only training bias and the speculative nature of MRH.
- Demonstrating that the monocular cue clusters are reproducible under different random seeds of the SAE or different perturbation strengths.
- Using attention weights to directly verify MRH's block-convex code structure by reconstructing per-head convex combinations and checking that their sum matches the token.

## Removed Points

- **SAE artifacts driving LRH departures (Harsh Critic #3):** The claim that the convex-hull constraint biases the dictionary toward higher coherence is speculative and unverified. The SAE reconstructs DINOv2 activations with R² > 88%; the dictionary geometry reflects what is needed to faithfully represent the data. The comparison to Grassmannian baselines is a standard test of the LRH idealization. Comparison against an unconstrained SAE would be nice (moved to Nice-to-Haves) but the absence is not a flaw.
- **"Co-activation vs. geometry correlation is intrinsic" (Section-by-section):** The paper already addresses this algebraically in Footnote 1, noting the correlation is proportional to tr(AᵀA). The critic's point is therefore already acknowledged.
- **"Proposition 2 undermines SAE analysis" (Section-by-section):** The paper never claims the SAE decomposition is unique or that it recovers ground-truth factors. Proposition 2 is a useful negative result about interpretability from single layers, not a contradiction of the SAE approach.
- **"Largest interpretability demonstration" self-serving:** A style nitpick; the paper's contributions speak for themselves.
- **Missing appendix discussion:** The parser strips appendix content; the original submission has them.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Address the coverage bias directly.** Either retrain the SAE on a more diverse dataset (including ADE20k and NYU Depth images or a general mix) and verify the task-specific findings replicate, or run a control showing that probes trained on original DINOv2 embeddings (not SAE-reconstructed) project similarly into the SAE basis. This would bound the artifact concern.

2. **Either strengthen the MRH experiments or rebalance the paper's framing.** Provide direct tests that discriminate MRH from competing hypotheses — e.g., using attention weights to verify per-head convex combinations sum to the token, or showing that steering saturates at predicted polytope boundaries. Alternatively, clearly frame MRH as a speculative discussion / future direction and foreground the empirical dictionary analysis as the core contribution.

3. **Add quantitative validation for the qualitative taxonomies.** For Elsewhere concepts, include a perturbation experiment with quantitative results. For monocular cue clusters, report cluster validity indices (silhouette scores) and stability under different random seeds and perturbation strengths.

## Score and Decision

**Calibration report:**

Round 1 — Bracketing:
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Wxl0JMgDoU (skill adaptation in chess SAE) | 2.50 | R1 | Much weaker; narrower scope, unclear contribution |
| 89wVrywsIy (hierarchical tracing) | 3.40 | R1 | Weaker; preliminary method with limited validation |
| wZiH43e5Ah (conceptualize any network) | 3.00 | R1 | Weaker; framework paper with limited empirical depth |
| UbLvSPMvMA (cosine loss for sparse) | 1.67 | R1 | Much weaker; method paper with limited evaluation |
| imT03YXlG2 (CLIP SAE adaptation) | 6.50 | R1, R2 | Comparable; similar SAE-for-vision approach, similar methodological concerns, narrower scope |
| ghH6YYDs15 (amortisation gap in SAEs) | 4.67 | R1 | Weaker; theoretical analysis of SAEs, not interpretability |
| Ch8s4FdUXS (SDXL Turbo SAE) | 4.40 | R1 | Weaker; limited model scope, heavy reliance on qualitative analysis |
| F76bwRSLeK (SAE for LLMs) | 4.80 | R1 | Weaker; less ambitious, lacks downstream task analysis |
| tcsZt9ZNKD (scaling SAEs) | 8.20 | R1 | Stronger; rigorous scaling laws and evaluation |
| I4e82CIDxv (sparse feature circuits) | 8.00 | R1 | Stronger; causal intervention framework |
| 5Ca9sSzuDp (CLIP text decomposition) | 8.00 | R1 | Stronger; cleaner decomposition approach |
| 2dnO3LLiJ1 (Vision Transformers Need Registers) | 8.00 | R1 | Stronger; cleaner problem + solution |

Round 2 — Narrowing (bracket [5.5, 7.0]):
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| vogtAV1GGL (concept indexing mechanisms) | 5.75 | R2 | Weaker; theoretical with limited empirical validation |
| bkdWThqE6q (interpretable transformer) | 6.00 | R2 | Comparable; specific architecture contribution vs. broad analysis |
| an3jH2qD2r (token geometry in LLMs) | 6.00 | R2 | Weaker in contribution clarity; rejected for unclear motivation |
| CexatBp6rx (concept-based interpret. networks) | 6.40 | R2 | Comparable; visualization technique with solid evaluation |
| ih3BJmIZbC (representational similarity via concepts) | 6.80 | R2 | Stronger; cleaner evaluation and more focused claims |
| 9bmTbVaA2A (V-IP with LLMs) | 5.75 | R2 | Comparable; different approach to interpretability |

The initial bracket was [5.5, 7.0] based on the clear evidence that the paper is substantially stronger than the <3.5 anchors but not at the level of the >7.5 anchors. After narrowing with the second round, the paper sits in the 6.0–6.5 range. Compared to the 6.0 token-geometry paper (rejected for unclear motivation), the current paper has far clearer and more impactful contributions. Compared to the 6.5 CLIP SAE paper (accepted), it is comparably ambitious but with more speculative elements (MRH) that pull it slightly down. The paper is closest to the 6.0 benchmark.

Round 1 bracket: 5.5–7.0. After round 2 narrowing, the paper is closest to the 6.0 level, reflecting a solid contribution with room to tighten the support for its most ambitious claims.

**MY FINAL SCORE: <score>6.0</score>**
**MY FINAL DECISION: <decision>Accept</decision>**