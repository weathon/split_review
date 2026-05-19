- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3
Now I have all the information I need. Let me construct the final consolidated review.

## Summary

This paper proposes a structured initialization for Vision Transformers (ViTs) that embeds a convolutional inductive bias into attention maps via initialization alone, without architectural changes. The key idea is to initialize each attention head's Q and K weights so that the softmax attention map approximates an impulse convolution matrix, solved through a fast optimization using positional encoding as pseudo input. A theoretical condition (Proposition 1) is derived linking embedding dimension, rank, and filter basis size to explain why random spatial filters work in ConvMixer, motivating the approach.

## Strengths

- **Novel theoretical grounding for random filters in ConvMixer (Proposition 1):** The paper derives a concrete condition \(D \ge k f^2\) under which learning only channel-mixing weights suffices, providing a formal rationale that prior empirical work lacked. This cleanly motivates the connection between ConvMixer's spatial mixing and ViT's multi-head attention.

- **Conceptually clean method that preserves architectural flexibility:** The impulse-initialization approach injects a CNN inductive bias entirely through initialization, leaving the ViT architecture unchanged. This is a principled alternative to architectural modifications (convolutional stems, hybrid layers) and avoids reliance on pre-trained models, unlike mimetic initialization.

- **Clear evidence that more heads amplify the benefit:** Table 2 (larger_cifar100) shows Imp.-3 achieves 75.97% on ViT-S/h6 vs. 73.86% for Mimetic (+2.11%), and 75.40% on ViT-S/h16 vs. 72.72% for Mimetic (+2.68%). These gaps are substantial and grow with head count, directly validating the theory that more heads provide more linearly independent filters.

- **Systematic ablation of pseudo input design:** Table 3 (pseudo_input) evaluates nine combinations of pseudo inputs across two Q/K sharing strategies, cleanly identifying positional encoding as the best default (90.39% average). This provides strong empirical support for a non-obvious design choice.

- **ConvMixer validation supports the core premise:** Table 4 (tab:conv) shows impulse filters rival random filters (within 0.5–1.8% of end-to-end trained ConvMixers) while rank-deficient box filters fail, experimentally confirming that impulse filters are a valid structural proxy for the theoretical analysis.

- **Visual confirmation of structured attention maps:** Figure 3 (fig:vis_attn) shows that impulse-initialized attention maps exhibit off-diagonal peaks aligned with convolutional structure, while mimetic initialization primarily strengthens the main diagonal and random initialization shows no pattern.

## Weaknesses

### Fatal
None.

### Major

- **No variance reporting across any experiment:** Every reported accuracy is from a single run with no error bars, confidence intervals, or multiple-seed averages. This is consequential because several key comparisons show small margins (e.g., Imp.-5 vs. Mimetic on ImageNet-1K: 74.40 vs. 74.34, a 0.06% difference; on CIFAR-100: 70.46 vs. 70.40, a 0.06% difference). ViT training on small data is known to have non-negligible seed sensitivity, so these differences could reflect noise rather than systematic improvement. While many configurations show larger gaps (2–9% over Trunc Normal, 2%+ over Mimetic on larger models), the absence of any variance reporting weakens the overall evidential quality and makes it impossible for readers to assess robustness. The paper's central claim of state-of-the-art performance would be substantially strengthened by reporting mean ± std over at least 3 seeds.

### Minor

- **"State-of-the-art" claim is scoped too broadly relative to the evidence:** The paper claims "state-of-the-art for data-efficient ViT learning" (abstract, contributions, conclusion) but only compares against three *initialization* baselines (Kaiming Uniform, Trunc Normal, Mimetic). Approaches that improve ViT data efficiency through architectural means (convolutional stems, hybrid architectures, or distillation like DeiT) are discussed in related work but not compared or contextualized quantitatively. The claim should be scoped to *initialization strategies* for ViT on small data, which would accurately reflect the experimental comparison set.

- **Initialization optimization is under-characterized:** The optimization step solving for \(Q_{\text{init}}, K_{\text{init}}\) is a core component, yet:
  - The final MSE approximation error between the optimized softmax attention and the target impulse matrix is never reported, so readers cannot assess how well the optimization succeeds before training.
  - No sensitivity analysis is provided for optimization hyperparameters (learning rate, number of iterations). While the paper states the optimization is fast (~5s), understanding how robust the final attention quality is to these choices would aid reproducibility.
  - The paper acknowledges in its Limitations that attention maps become blurrier with depth (due to pseudo-input mismatch), but does not quantify this degradation or study whether shallower vs. deeper layers benefit differently from the initialization.

- **Attention evolution during training is not shown:** The visualization (Fig. 3) only shows initial attention maps before training. The paper claims the method preserves "flexibility" (the attention can adapt away from the impulse structure during training), but no evidence of this evolution is provided. Showing that the constraint does not permanently restrict the model would strengthen the flexibility claim.

### Trivial

- The Proposition 1 derivation explicitly omits activations, normalizations, and skip connections (acknowledged by the authors). This is a heuristic intuition rather than a formal theorem — the framing as a "proposition" is somewhat strong.

## Nice-to-Haves

- A simple baseline: could the attention map be directly clamped to an impulse-like pattern instead of solving an optimization for Q and K? The paper could comment on whether such a direct approach works.
- Reporting the MSE loss value from the initialization optimization for representative configurations.
- Adding a brief analysis of how attention evolves across training (e.g., visualizing attention maps at initialization vs. after 50/100/200 epochs).

## Removed Points

- **"No code provided" (Harsh Critic):** Removed per the rule against reproducibility nitpicks about large artifacts impractical to include. The algorithm pseudocode (Algorithm 1) is sufficiently detailed.
- **Criticism that softmax-probability and impulse-binary mismatch is "inherently limited":** Removed as factually incorrect. An impulse convolution matrix (as defined in the appendix) has exactly one non-zero entry per row, which sums to 1 — this is a valid one-hot probability distribution that softmax can approximate arbitrarily well in the limit.
- **Criticism about missing comparison with simple baselines for pseudo input (directly setting attention to impulse):** Moved to Nice-to-Haves as it is a speculative baseline, not a concrete identified flaw.
- **Strength Finder generic praises ("important problem", "well-motivated"):** Removed as generic/superficial. Specific strengths retained above.

## Novel Insights

The most interesting observation emerging from the reviews is the *scalable head-count interaction*: the method's margin over baselines grows substantially with more heads, yet the paper's theoretical Proposition 1 was derived for ConvMixer (channel count \(D\)) and mapped to ViT via the notion that "heads ≈ unique filters." A genuinely novel angle that neither the paper nor the reviewers fully pursue is whether this mapping suggests an explicit design rule for ViTs — e.g., that for a given patch size and kernel dimension \(f\), the number of heads should satisfy \(h \ge f^2\) for the initialization to be fully expressive. The data in Table 2 is consistent with this threshold effect but the paper does not test it directly.

## Suggestions

1. **Add multiple seeds (3–5) to all main experiments and report mean ± std.** This is the single highest-leverage addition. Even if resources are limited, adding seeds for the CIFAR-10/100 core comparisons would transform the evidential quality.
2. **Report the final MSE approximation error** from the Q/K optimization for at least one representative configuration to show the quality of the impulse approximation.
3. **Tighten the "state-of-the-art" language** to reflect the comparison scope — e.g., "state-of-the-art among initialization strategies for data-efficient ViT learning" or "competitive with or superior to existing initialization methods."
4. **Show attention map evolution during training** in the rebuttal or camera-ready version to validate the flexibility claim.
