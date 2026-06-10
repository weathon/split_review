Here is my analysis and final review.

## Summary

This paper proposes combining $1/\sqrt{L}$ residual branch scaling with $\mu$P (Maximal Update Parameterization) to enable optimal hyperparameters to transfer simultaneously across both width and depth in residual networks. The authors provide empirical evidence on convolutional ResNets and Vision Transformers across CIFAR-10, Tiny ImageNet, and ImageNet, and support their findings with a theoretical analysis extending Dynamical Mean Field Theory (DMFT) to characterize the joint infinite-width/infinite-depth limit.

## Strengths

- **Figure 1(b) provides a clean, direct experimental demonstration** of the central claim: under the proposed $1/\sqrt{L}+\mu$P parameterization, the optimal learning rate forms a consistent region across a width (32–512) × depth (4–32) grid, whereas standard $\mu$P (Figure 1(a)) shows clear depth dependence. This is the single most important piece of evidence and directly supports the paper's thesis.

- **Extension of DMFT to the joint $N,L\to\infty$ limit** is a genuine theoretical advance. Proposition 1 derives the limiting stochastic integral equation for preactivations with a continuous "layer time" parameterization, going beyond prior work (Bordelon et al. 2022) that only characterized the infinite-width/finite-depth limit. This provides a principled foundation for why hyperparameters might transfer.

- **Exact closed-form solution for deep linear ResNets** (Section 4.3.2) provides an analytical expression for kernel updates after a single gradient step, with convergence shown for depths up to ~100. This is one of the few tractable solutions in the feature-learning (non-kernel) regime and validates the DMFT approach.

- **Quantified convergence rate** (Figure 6b): The finite-size approximation error is bottlenecked by width for small $N$ and decays as $\mathcal{O}(L^{-1})$ for sufficiently large $N$, giving practitioners concrete guidance.

- **Transfer demonstrated for multiple hyperparameters and schedules**: Momentum, feature learning rate $\gamma_0$, cosine annealing schedules, and warmup strategies all show transfer, extending beyond the simple constant-learning-rate setting.

- **Systematic comparison with normalization layers** (Figure 2): Shows that while BatchNorm/LayerNorm partially aid depth transfer, the $1/\sqrt{L}$-scaled version yields more reliable consistency across both width and depth.

## Weaknesses

### Fatal

None.

### Major

- **Empirical evidence relies primarily on training loss and short training durations.** The paper's central claim is about hyperparameter *transfer*, which practitioners care about for full training runs. Most experiments are limited to 10–20 epochs (explicitly acknowledged in Section 6). While this is transparently stated as a limitation, the abstract and introduction present the transfer claim as a flat assertion without this caveat. A single experiment extending to convergence (e.g., 200 epochs on CIFAR-10) would substantially increase confidence that the phenomenon is not an early-time artifact. Additionally, the primary evidence (Figures 1, 2, 3) shows training loss/accuracy, not test metrics — test loss is only shown for 250 steps in one figure (Figure 7). For a practical claim about hyperparameter transfer, test-set evaluation is the relevant quantity.

- **No quantitative transfer metrics.** All evidence for the core claim is visual: readers must judge whether optimal learning rates "look similar" across depths in contour plots. The paper would be significantly strengthened by metrics such as: (a) variance of the optimal learning rate across depths, (b) relative loss penalty for using a fixed LR across depths vs. per-depth optimum, or (c) the range of depths for which a single LR achieves within X% of the per-depth optimum. Without such measures, the strength of the transfer claim is difficult to assess objectively.

- **Theoretical support does not directly prove hyperparameter transfer.** The DMFT analysis shows that the proposed parameterization admits a well-defined joint infinite-width/infinite-depth limit where feature updates are $\mathcal{O}(1)$. This motivates why hyperparameters *might* transfer, but does not constitute a proof — a gap the paper itself acknowledges ("it remains an open problem theoretically why hyperparameters transfer across widths and depths even when the actual predictions/losses differ," line 321). The paper would benefit from a clearer separation between what the theory proves (a limit exists) and what it motivates (hyperparameter transfer).

### Minor

- **Missing experimental setup details.** The paper lacks a dedicated section specifying architectures (exact filter counts, number of blocks, patch sizes for ViTs), hyperparameter grids, learning rate ranges, batch sizes, dataset splits, and optimization details. For example, "We use this residual convolutional architecture in figures..." (line 152) without defining it. A practitioner cannot reproduce these results from the main text. While some details may be in the appendix (which the parser strips), the main text should contain sufficient information.

- **Weight decay claim does not match the figure.** The text (line 176) states that Figure 6 plots dynamics for "momentum, weight decay, and the feature learning rate $\gamma_0$," but the figure caption only lists subfigures for (a) momentum and (b) $\gamma_0$, with no visible weight decay result. This is a minor inconsistency but should be corrected.

- **Exact solvable case is far from experimental setting.** The deep linear ResNet solution (Section 4.3.2) involves linear activations, a single training example, and a single gradient step. While the paper acknowledges this is a special case, the distance between this setting and the nonlinear, multi-class, multi-step experiments is not discussed. The claim that this "directly validates the DMFT approach" (line 277) would benefit from tempering.

### Trivial

- **Figure 2 uses $\beta_\ell = 3/\sqrt{L}$ rather than $1/\sqrt{LN}$** from the main parameterization, "to increase feature learning at finite depth." While explicitly stated, this modification makes the comparison to other normalization baselines less clean, since the parameterization itself has changed.

## Nice-to-Haves

- A concrete predictive check from the DMFT theory (e.g., the shape of the optimal LR as a function of depth predicted by the limiting dynamics) that could be compared against experimental results would substantially tighten the theory-experiment coupling.
- Reporting test accuracy at convergence for a subset of configurations would greatly strengthen the practical claim.
- Weight decay transfer results should be included or the claim should be removed.

## Removed Points

- *"The ViT experiments do not cleanly support the thesis — the primary baseline (ViT + μP + LayerNorm) already transfers."* The paper explicitly acknowledges this (line 174, citing Yang et al. 2021). The novel contribution is (1) transfer without normalization layers and (2) non-saturating depth scaling, which the paper clearly distinguishes. This criticism is based on a misreading.

- *"The paper's theoretical section should be reframed as a separate contribution."* The paper already presents the theory as motivation, not proof, and explicitly acknowledges the gap (line 321). The theory showing size-independent dynamics is directly relevant to the transfer claim.

- *"The μP-to-convolutional mapping is unclear."* Table 1 clearly specifies the scaling rules; applying them to channels (the width dimension in CNNs) is standard practice and well-understood by the target audience.

- *"[Various formatting/style nitpicks]"* — removed per formatting rules.

- *"Strength: the paper addressed an important problem."* Generic; removed.

- *"Strength: the paper's limitations section is honest."* Sycophantic/superficial; removed.

## Novel Insights

None beyond the paper's own contributions. The strength finder and harsh critic raise the same key tension: the paper's empirical support is suggestive but not fully commensurate with the strength of its claims. The most interesting insight that emerges from reading across both inputs is that the $1/\sqrt{L}$ scaling seems to provide benefits orthogonal to normalization layers — it avoids the depth saturation that normalization-based approaches exhibit — which is a genuinely practical observation that the paper could foreground more prominently.

## Suggestions

1. Add a quantitative transfer metric: for each depth $L$, find $\eta^*(L)$ and compute the relative loss penalty $\mathcal{L}(\eta^*(L_0), L) / \mathcal{L}(\eta^*(L), L)$ for using a reference depth's optimal learning rate. This directly answers "how much does transfer cost?"

2. Extend at least one experimental setting (e.g., CIFAR-10 ResNets) to converge fully (100+ epochs) and verify that the optimal learning rate is stable from early to late training.

3. Report test accuracy systematically for the main learning rate transfer experiments (Figures 1, 2, 3).

4. Add a table with complete experimental specifications: architectures, hyperparameter grids, learning rate ranges, batch sizes, dataset splits, and optimizer settings.

5. Either include the weight decay experiment in Figure 6 or remove the text claim.

6. Clarify in the abstract and introduction that the empirical evidence is based on 10–20 epoch training, or add longer runs.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>