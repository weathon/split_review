## Summary
This paper proposes Predictive Differential Training (PDT), which integrates Koopman operator theory into neural network training by predicting weight updates several epochs ahead via Dynamic Mode Decomposition (DMD), then selectively applying those predictions only to parameters where the prediction quality satisfies a quantity criterion (predicted change > SGD change) and a direction criterion (predicted change direction aligns with SGD). The core novelty is a per-parameter masking strategy that prevents the gradient explosion that plagues prior Koopman-based training approaches. Experiments on FCN, AlexNet, ResNet-50, and ViT-Base (CIFAR-10 and ImageNet-1K) with SGD, momentum, and Adam show that PDT reaches the baseline's best training loss in fewer epochs.

## Strengths
1. **Novel and well-motivated masking strategy.** The quantity-and-direction criteria (Eqs. 8–9) for selectively applying Koopman predictions are a principled response to the known failure mode of prior Koopman-based training (gradient explosion in deeper networks). The intuition — not all parameters' dynamics are equally predictable — is clean and practically grounded.

2. **Controlled ablations confirm the masking strategy is responsible for stability.** Figures 6 and 7 present two key comparisons: (a) PDT vs. randomly selected subsets of weights with increased learning rates, and (b) PDT vs. randomly selected subsets of Koopman-predicted weights. In both cases, random selection causes instability or NaN values, while PDT maintains stable training. This directly proves that the specific masking criteria, not merely the use of predictions or larger step sizes, drive the improvement.

3. **Demonstrated across diverse architectures, optimizers, and datasets.** The method is tested on FCN, AlexNet, ResNet-50, and ViT-Base with SGD, momentum-SGD, and Adam on CIFAR-10 and ImageNet-1K. This breadth is adequate to support the plug-in claim.

4. **Hyperparameter sensitivity is systematically studied.** Section 4.4 (Figure 9) examines prediction steps (τ), prediction interval, starting epoch, and past snapshot counts, revealing interpretable trends (e.g., τ beyond 9 steps causes gradient explosion) and providing practical guidance for using PDT.

5. **Computational complexity analysis is provided.** Section 3.3 shows that the SVD cost is O(N × h²) with h ≤ 10, which is subsumed by epoch-level training cost O(S × N), justifying the feasibility claim.

## Weaknesses
### Fatal
None. The core contribution (selective masking for Koopman-based weight prediction) is novel, and the central claim of faster convergence in epochs-to-target-loss is supported by experimental evidence.

### Major

1. **No test-set evaluation is reported.** The abstract claims "lower training/testing loss," and Section 4.1 is titled "Generalization Study," yet no test loss, test accuracy, or any generalization metric appears anywhere in the paper. The evaluation reports only training loss curves and wall-clock runtime. Without test-set results, a reader cannot assess whether the accelerated convergence preserves or degrades generalization. This is the most significant gap in the paper and directly undermines one of the stated claims.

2. **Wall-clock runtime analysis is incomplete and potentially contradictory.** The paper claims acceleration but focuses on epochs-to-target-loss. The runtime comparison (Table 1) appears to show mixed results — the harsh reviewer notes that some configurations may show marginal or negative runtime savings — but the paper does not discuss when or why the DMD overhead might offset the epoch savings. The claim at line 172 that "the overhead introduced by the DMD is effectively compensated by the acceleration in loss reduction" is asserted rather than demonstrated with a breakdown of time spent on DMD vs. SGD. This needs concrete accounting.

### Minor

1. **Narrow baseline set.** PDT is compared only against the base optimizer without PDT. A natural and simpler baseline is a uniform learning-rate increase (tuned to match PDT's average effective step size) applied to all parameters, which would isolate whether the benefit comes from the *selective* application of predictions or merely from a larger effective step size. The random-acceleration ablation (Figure 6) partially addresses this by showing that accelerating a *random subset* fails, but a *uniform* LR increase across all parameters is a different and still-missing baseline.

2. **Masking criteria are under-analyzed.** The direction criterion (Eq. 9) requires *every intermediate* predicted step to align with the one-step SGD direction — an extremely rigid condition. The masked-ratio curves in Figure 5 show that this criterion is mostly satisfied only in early training, after which the ratio drops sharply. The paper acknowledges this pattern (lines 231–232) but does not analyze whether PDT's gains could be replicated by a simple short-duration high-LR warmup phase — a much simpler method. The question of whether PDT delivers meaningful acceleration beyond what a cheap initial high-LR strategy would achieve is left unaddressed.

3. **Limited statistical presentation.** The paper states that experiments used 5 random seeds, but (a) the training loss curves in Figure 5 do not show variance (no error bars or shading), and (b) the hyperparameter study in Figure 9 appears to show single runs. This makes it difficult to assess the stability of the reported results.

4. **Toy example is conceptually disconnected from PDT.** Section 3.2 illustrates differential learning by simply increasing the learning rate for a subset of variables in a 6-variable function minimization. This is not how PDT works — PDT uses Koopman-based prediction, not LR adjustment. The example is pedagogically useful for the concept of differential updates but could mislead readers about the actual mechanism of PDT.

### Trivial

- The notation in Eqs. 8–9 is slightly ambiguous: $\|\mathbf{w}_{i+\tau}^{\mathrm{pred}}-\mathbf{w}_{i}^{\mathrm{pred}}\|$ compares two predicted weights at different times, while $\|\mathbf{w}_{i+1}^{\mathrm{opt}}-\mathbf{w}_{i}^{\mathrm{opt}}\|$ compares two SGD-derived weights. Clarifying the superscript conventions would help.
- Figure 1 shows an appealing loss-landscape comparison, but the paper does not explain how the landscape was generated or which metric determines "better."
- The reference to "CosineAnnealingLR scheduler" in Figure 5 captions — this is a common choice but its interaction with PDT (both modulate effective step size over time) is not discussed.

## Suggestions
1. **Add test-set results** — report final test accuracy/loss for all configurations in Table 1, ideally with confidence intervals across the 5 seeds already used.
2. **Add a uniform-LR-increase baseline** tuned so the average effective step size matches PDT's, to isolate the benefit of selective attention.
3. **Provide a wall-clock time breakdown** showing time spent on DMD vs. forward/backward passes, explaining any configurations where PDT is slower.
4. **Ablate the two mask components separately** (quantity-only vs. direction-only) to understand their individual contributions.
5. **Add error bars/shading** to all experimental curves, especially the hyperparameter study in Figure 9.

## Score and Decision

**Overall assessment:** The paper presents a genuinely novel idea — selectively applying Koopman-based weight predictions using per-parameter prediction-quality criteria — and provides evidence that this masking strategy prevents the gradient explosion that scuttles prior Koopman training approaches. The ablations (random acceleration, random mask) are well-designed and support the core claim. However, the evaluation has significant gaps: most critically, no test-set metrics are reported despite the abstract claiming "lower training/testing loss," and the runtime analysis lacks the detail needed to assess practical efficiency. The baseline set is narrow. These issues are substantial but addressable, and the core methodological contribution is solid enough to warrant revision rather than rejection.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept
