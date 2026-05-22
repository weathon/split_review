Now let me produce the final consolidated review.

## Summary

The paper proposes **Thoughtbubbles**, a transformer variant that learns to dynamically fork residual streams during pretraining, creating parallel "bubbles" of computation for tokens that need more processing. The forking decisions are trained via a scoring mechanism that attenuates attention and residual updates, forcing the model to allocate higher scores to more important tokens. Experiments at 150M–772M scales on OpenWebText and peS2o show consistent perplexity improvements over parameter-matched and computation-matched (copy-3/copy-5) baselines, and the model allocates more forks to tokens with higher output entropy.

## Strengths

1. **Novel idea with a clean mechanism.** Forking residual streams into parallel latent "bubbles" controlled by learnable scores (Sections 2.3–2.4) is architecturally distinct from serial pause-token insertion. The attenuation mechanism (Eq. 8–10) provides a principled way to train the scores through the LM loss without explicit supervision beyond language modeling.

2. **Consistent perplexity gains across all settings.** Table 1 shows Thoughtbubbles achieves the lowest validation perplexity in all 12 configurations (2 datasets × 3 sizes × 2 budgets). Notably, the 319M κ=4L model (20.23 perplexity on OpenWebText) beats the 772M baseline (21.22), demonstrating the method's effectiveness.

3. **Entropy-computation correlation provides a sanity check.** Figure 5 shows a positive correlation between fork count and output entropy (measured both by the forking model and an independent baseline), supporting the claim that the model allocates computation to genuinely uncertain tokens. The concave shape (fewer forks at the highest entropy) is also plausibly explained.

4. **Forking behavior is functionally integrated.** Figure 4 shows the parent token attends to its children with attention scores an order of magnitude higher than to other tokens, indicating the forked streams are actively used in computation rather than being inert filler.

5. **Dynamic forking preserves autoregressive quality.** Section 5.1 and Figure 6 demonstrate that scaling the forking budget proportionally to input length avoids the distribution shift between blockwise and autoregressive decoding.

## Weaknesses

### Major

- **Missing comparison to adaptive-computation baselines (pause tokens, thinking tokens).** The paper positions itself against pause-token methods (Herel & Mikolov 2024; Goyal et al. 2024; Sun et al. 2025) in the introduction and related work, yet the only non-parameter-matched baseline is copy-3/copy-5 — a trivial approach that duplicates the *entire* input rather than adaptively allocating extra computation. Without a comparison to a model that inserts pause tokens at fixed positions with matched FLOPs, it is impossible to determine whether the *adaptivity* of Thoughtbubbles drives the gains, or simply having extra parallel residual streams at any position would produce similar results. This gap substantially weakens the paper's contribution claim.

- **Non-differentiable top-k selection is not fully resolved.** The forking mechanism (Section 2.3) uses a hard top-k to select which residual streams survive. Gradients flow through the surviving streams' scores via the attenuation mechanism (Eq. 8–10), but streams that are dropped receive no gradient signal. The paper acknowledges this "Top-K Gradient Bottleneck" in the Limitations section and mentions "training time randomization and noise" as a mitigation, but does not specify whether this mitigation was actually implemented, how it works, or evaluate its impact. Without a clear description of how the discrete selection is trained, the reader cannot fully assess whether the forking behavior is learned in the intended way or emerges from other factors.

- **No variance or significance reporting.** All results in Table 1 are single-point estimates. Given that many improvements are modest (e.g., perplexity 21.22 vs 20.19 for 772M OpenWebText), and some downstream tasks show mixed or negative results (BLiMP, PIQA), it is impossible to assess whether the gains are systematic or within the range of random seed variation. The copy-5 baseline itself shows non-trivial improvements over the parameter-matched baseline (e.g., 21.22→20.90 for 772M OpenWebText), raising the question of whether any method that increases effective depth yields similar gains.

### Minor

- **Forking layer placement is unablated.** Forking layers are placed only after layers 3, 7, and 11 (Section 3.1), with no ablation or empirical justification for this specific pattern. The paper notes this choice is discussed in Appendix B (not available), but the main text provides no analysis. Different placement patterns could produce substantially different results.

- **The "FLOPs-matched" claim for κ=4L vs. copy-5 is not justified.** The paper states these are "roughly FLOPs-matched" (Table 1 caption), but copy-5 multiplies sequence length by 5 at every layer, while Thoughtbubbles has variable sequence length up to κ=4L, often less. No detailed FLOPs estimate is provided, making the claim difficult to verify.

- **Entropy-fork analysis is purely correlational.** Figure 5 shows a correlation between fork count and entropy, but there is no baseline showing what the correlation would look like under random forking, and no causal intervention (e.g., disabling forks at inference) to demonstrate that forks directly cause the perplexity improvements. The concave shape at highest entropy is hand-waved rather than explained with evidence.

- **Attention analysis (Figure 4) is consistent with proximity.** The finding that the parent token attends strongly to its children is partially confounded by their physical proximity (placed immediately to the left) and the causal mask structure. While this does not undermine the claim that children are used, the paper overinterprets the evidence.

### Trivial

None.

## Nice-to-Haves

- An ablation where forking is disabled at inference time (forced to keep only one stream per token) to causally demonstrate that the forks drive the perplexity gains.
- Reporting the distribution of fork counts per token across layers (how often does the model saturate or empty the budget?) to reveal whether the scores are meaningfully differentiated.
- Concrete examples with fork counts overlaid on sentences, letting readers judge whether forked tokens are indeed "difficult" (rare words, ambiguous positions).
- Comparison to a model with uniformly more layers at matched parameter count, to isolate the effect of adaptivity from the effect of additional compute alone.

## Removed Points

- **"Figure 4 does not demonstrate useful computation because children are within the attention window"** — Removed because being within the attention window does not explain *why* attention to children is an order of magnitude higher than to other tokens. The finding is genuine evidence of functional integration, even if partially confounded by proximity.
- **"Hardware efficiency limitation" critic** — Removed as the paper acknowledges this as a secondary limitation (Section 8: "Time-matched evaluations"). It is not a methodological flaw.
- **"Related work omission" (Universal Transformers, etc.)** — Removed because the paper does cite these works in Section 6 (Related Work: "Dehghani et al., 2019; Csordás et al., 2024"). The claim of being "first" is qualified to the specific combination of features (unsupervised + dynamic + parallel + latent).
- **"Scaling to billion-parameter models and reasoning benchmarks"** — Removed as scope creep; the paper acknowledges hardware limitations and the 772M scale is reasonable for a methods paper.
- **"Autoregression analysis on a small subset"** — The paper shows this in Figure 6, and the analysis is described as a demonstration, not a full evaluation. Removed as a strawman.
- **"Missing appendix details"** — Removed per instructions (parser strips appendices).

## Novel Insights

None beyond the paper's own contributions — the reviews do not surface any genuinely novel observation that the authors missed. The primary insight from the cross-review is that the gradient bottleneck, while acknowledged, is more central than the paper treats it, and that the evaluation would be much stronger if pause-token baselines were included.

## Suggestions

1. **Add a pause-token baseline.** Train a model with fixed-position pause tokens (matching the extra compute budget) to directly compare adaptive (Thoughtbubbles) vs. non-adaptive (pause tokens) parallel computation. This is the most critical addition to establish the value of adaptivity.
2. **Report variance across 3–5 seeds** for at least the largest model sizes. Without this, the reader cannot evaluate whether the gains are systematic.
3. **Clarify the gradient flow through top-k.** State explicitly whether the current implementation uses a straight-through estimator, Gumbel-softmax, or relies solely on the attenuation-based gradient signal through surviving streams. If the "training time randomization and noise" mitigation was used, describe it and show its impact.
4. **Add a no-fork ablation** where the model is evaluated with forking disabled (\kappa = L at inference) to causally attribute the gains to the forking behavior.
5. **Ablate forking placement** (e.g., every layer vs. only early layers vs. only late layers) to justify the current choice.

## Score and Decision

This paper introduces a genuinely novel architectural idea — learning to fork residual streams for dynamic parallel computation — and provides consistent empirical evidence of its benefits across model scales and datasets. However, the evaluation is weakened by the absence of comparison to the most relevant prior art (pause tokens), the lack of variance reporting, and the unresolved gradient-flow issue through the top-k selection. These are addressable but significant gaps.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>