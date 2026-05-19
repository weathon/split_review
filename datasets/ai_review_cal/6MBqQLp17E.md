- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8, 8, 6
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes the first O(N) algorithm for topological masking of linear attention transformers on general graphs, using graph random features (GRFs). The key idea is to parameterize the topological mask as a learnable power series of the weighted adjacency matrix, then approximate it with sparse random-walk-based features. The paper proves concentration bounds and sparsity guarantees for GRFs, and demonstrates empirical gains on ImageNet, iNaturalist, Places365, and large-scale point cloud dynamics (>30k particles).

## Strengths

- **First O(N) topological masking algorithm for general graphs.** The paper rigorously proves (Corollary 1, Sec. 3.3) that GRFs yield a feature matrix with O(N) nonzeros for any graph with bounded maximum degree/edge weight, improving on prior O(N log N) methods restricted to structured graphs (trees, grids). The FLOPs plot (Fig. 2) empirically validates the linear scaling.

- **Novel theoretical results for graph random features.** Theorem 1 provides the first known exponential concentration bound for GRFs, with a rate independent of the graph size N. Combined with the sparsity lemma (Lemma 1), this provides rigorous theoretical grounding for the O(N) complexity claim — a contribution potentially of independent interest beyond transformers (e.g., geometric Gaussian processes).

- **Principled, learnable mask parameterization.** The mask defined as a power series of the weighted adjacency matrix (Eq. 3) subsumes popular graph kernels (heat, diffusion, p-step random walk) and is learnable end-to-end. This marries flexibility with strong structural inductive bias.

- **Consistent empirical gains across modalities.** On ImageNet (Table 1), GRF-masked linear attention improves +3.7% over unmasked linear, matching or beating far more expensive O(N log N) alternatives. On point cloud dynamics with >30k particles, the GRF Interlacer qualitatively and quantitatively outperforms both vanilla transformer and message-passing baselines.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core contributions — a novel O(N) masking algorithm with first-known concentration bounds and positive empirical results — are sound.

### Minor

- **The 1-WL expressivity claim is not formally justified.** The paper states (Sec. 3.3, lines 308–309) that GRF transformers are "more expressive than standard graph neural networks and unmasked transformers" because they can distinguish 1-WL-indistinguishable graphs "because their adjacency matrices and hence masks differ." While intuitively plausible, this argument skips key reasoning: whether the mask approximation preserves distinguishability, and whether the attention mechanism can exploit any resulting differences. The claim as written is an assertion, not a proof, and the paper's contribution does not depend on it. The authors should either provide a careful justification or soften the claim to "the mask depends on the full adjacency matrix, providing a richer inductive bias than standard GNNs."

- **Point cloud evaluation lacks quantitative summary statistics.** The SSIM plot (Fig. 6) is described qualitatively ("GRFs outperform... baselines") without reporting numerical values, error bars, or multiple-seed statistics. While the rendered rollouts (Fig. 5) are visually informative, a reader cannot assess the variance or statistical significance of the reported advantage. This weakens the otherwise compelling claim.

- **Proof sketch for Theorem 1 is very brief in the main text.** The derivation of the McDiarmid bound (lines 243–248) states the high-level approach but does not show the L1-norm bound or the McDiarmid condition explicitly. While the full proof is relegated to the appendix (standard practice), the sketch is so terse that a reader cannot verify the argument's correctness from the main text alone. Expanding the sketch to show the key bounding step would improve credibility.

- **ImageNet model architecture is not summarized in the main text.** The paper reports 74.1% for softmax attention (Table 1), which is low relative to modern ViT standards, and defers all architecture details to the appendix. While the relative comparisons (+3.7% over unmasked linear) are the principal evidence, stating the model size (e.g., layers, hidden dim, patch size, training epochs) in the main text would help readers assess the regime of evaluation.

### Trivial

- The paper reports single-seed results for the ViT experiments (Table 1) without error bars. Given the randomness in GRF sampling and training, multiple seeds would strengthen confidence, but this is standard for large-scale ImageNet-scale experiments.

## Nice-to-Haves

- Reporting SSIM as a table of mean ± std at selected timesteps for the point cloud experiment.
- A brief analysis of failure cases (the paper mentions long-horizon blurring but does not discuss where GRF masking specifically struggles).
- Explicit specification of the random walk sampling mechanism (e.g., "at each step, halt with probability p_halt, else transition to a uniformly random neighbor") in the main text.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"Insufficiently supported concentration bound as a methodological gap"* — The harsh critic labeled this a "methodological gap" and "critical issue." However, the paper states the theorem, defines all quantities, gives a proof sketch, and references the appendix for the full derivation. The structure (theorem + sketch + appendix proof) is standard for ML conference papers. The sketch could be more detailed but the absence of a full derivation in the main text is not a methodological gap; it is a presentation brevity issue (already captured as a minor weakness above).

- *"Low ImageNet baseline accuracy as an evidential issue"* — The critic suggested the low absolute accuracy (74.1%) indicates a "very small model" and questioned the "practical relevance." However, the paper's claim is about *relative improvement* over matched baselines (+3.7% over unmasked linear). The comparison is controlled (same architecture, varying only the masking method), so the absolute performance level does not affect the validity of the relative comparison. Model architecture is deferred to the appendix, which is standard.

- *Strength Finder's "Expressiveness beyond 1‑WL"* — This conflicts with the verified weakness that the 1‑WL claim is not formally justified. Following the rule that "when a strength and weakness disagree, the weakness wins," this strength is dropped.

- *All formatting/style nitpicks, grammar/typo criticisms, and complaints about missing appendix content* — These are parser artifacts, not author errors.

## Novel Insights

The most interesting observation emerging from the reviews is a tension in the paper's positioning: the theoretical apparatus (concentration bounds, sparsity guarantees) is leveraged to argue for O(N) complexity, but the experimental evaluation emphasizes *accuracy improvements* over baselines, not speed or memory benchmarks at scale. The FLOPs plot (Fig. 2) is a hardware-agnostic proxy, but actual wall-clock time comparisons for large graphs would more directly demonstrate the practical benefit of the O(N) guarantee. Neither reviewer raised this, but it is a meaningful gap between the paper's strongest theoretical selling point and its empirical support.

## Suggestions

1. **Soften the 1-WL expressivity claim** — either provide a rigorous argument or rephrase as "provides a richer topological inductive bias than standard GNNs."
2. **Add numerical SSIM values** (mean ± std across seeds) to the point cloud evaluation, summarizing at key rollout timesteps.
3. **Expand the Theorem 1 proof sketch** in the main text to show at least the key inequality in the McDiarmid argument (the L1-norm bound expression).
4. **Add a one-line summary of the ViT architecture** (e.g., "6-layer ViT with hidden dim 384, patch size 16") to the main ImageNet results section for context.
5. **Consider reporting ImageNet results with error bars** across 2–3 seeds to quantify variance from GRF sampling.
