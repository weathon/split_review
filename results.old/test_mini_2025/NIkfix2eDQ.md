Now I have enough calibration data. Let me construct the final review.

---

## Summary

This paper studies loss of plasticity in continual learning. The authors prove that linear function approximation and deep diagonal linear networks avoid loss of trainability (Theorems 1 and 2), then propose *deep Fourier features* — replacing every activation layer with the concatenation [sin(z), cos(z)] — to dynamically balance the trainability of linearity with the expressiveness of nonlinearity. Experiments on CIFAR10, CIFAR100, and tiny-ImageNet across diminishing-label-noise and class-incremental settings show that deep Fourier features improve continual learning performance, particularly on the hardest benchmarks.

## Strengths

- **Theoretical results for linear and deep diagonal linear networks (Theorems 1–2).** The paper proves that linear function approximation does not suffer from loss of trainability on a sequence of tasks (Theorem 1), and extends this to deep diagonal linear networks — a non-convex case (Theorem 2). This provides formal grounding for earlier empirical observations that linear methods sustain plasticity, and clarifies that the nonlinearity of gradient dynamics is not the primary cause of plasticity loss.

- **Novel, well-motivated architectural proposal (deep Fourier features).** The concatenation of sin and cos in every layer is cleanly motivated: for any pre-activation z, either sin(z) or cos(z) is locally well-approximated by a linear function with error ≤ 0.05 (Proposition 1). This "adaptive linearity" is an elegant solution to the tension between linearity (needed for plasticity) and nonlinearity (needed for representation power). The idea goes well beyond earlier uses of Fourier features only at the input layer.

- **Strong empirical results, especially on tiny-ImageNet.** In the class-incremental setting (Figure 6, left), deep Fourier features substantially outperform all baselines (CReLU, L2, ReDO, Shrink&Perturb, SpectralReg, standard ReLU) across 80 tasks on tiny-ImageNet. The method learns faster on early tasks and continues to improve on later tasks — a pattern that clearly demonstrates sustained plasticity. The gap is particularly large on the hardest benchmark, which is where the problem is most meaningful.

- **Sensitivity analysis connecting trainability and generalization (Figure 7).** The paper systematically studies how regularization strength interacts with trainability. The finding that deep Fourier features maintain high trainability under strong regularization — where standard networks collapse — is a genuine insight that explains *why* the method works well with regularization.

## Weaknesses

### Fatal
None.

### Major

- **Unit sign entropy definition is mathematically incorrect (Definition 1).** The paper defines ℍ(sgn(h(x))) = 𝔼_{p(x)}[sgn(h(x))] and states that the maximum value is 1 when the unit is positive on half the inputs. If sgn ∈ {−1, +1}, then 𝔼[sgn] = 0 when the sign is equally split. The stated definition does not match the claimed properties. The quantity being computed in the inset of Figure 3 (plotted values ~0.6–0.9) is clearly some measure of sign diversity, but calling it "entropy" and defining it as the raw expectation of the sign is formally wrong. Since this metric is used as a diagnostic in Section 4.1 to motivate the need for adaptive linearity, the paper should either correct the definition or reframe the analysis using a well-defined quantity (e.g., 1 − |𝔼[sgn]|, or the fraction of positive activations, or the actual binary entropy H(p) = −p log p − (1−p) log(1−p) with p = P(sgn > 0)).

### Minor

- **The "approximate embedding" of a deep linear network (Corollary 1) is not rigorously established in the main text.** Proposition 1 shows that for any z, either sin or cos is well-approximated by a linear function over [z−π/4, z+π/4]. However, which unit (sin or cos) is approximately linear depends on z, and z is input-dependent. The resulting "embedded deep linear network" would therefore be input-dependent — not a fixed linear network using the same parameters for all inputs. Moreover, the paper does not analyze how the per-unit approximation error propagates through depth. Without the appendix proof (which is inaccessible in this format), the claim as stated in the main text is plausible but not fully substantiated. The paper's empirical results stand on their own, but the theoretical framing of Corollary 1 is weaker than advertised.

- **Limited empirical validation for general deep linear networks.** Section 3.3 uses a single experiment on a linearly separable subset of MNIST to claim "empirical evidence for trainability of general deep linear networks." While this is positioned as a sanity check, the section heading overstates the evidence. A deeper empirical investigation (more datasets, varying difficulty) would strengthen the bridge between the theoretical results for the diagonal case and the claim about general deep linear networks.

- **The paper does not fully specify which regularization setups apply to each method in the main comparisons.** Deep Fourier features are described as being used "combined with regularization," and the sensitivity analysis (Figure 7) uses spectral regularization. But for the main comparisons (Figures 5 and 6), it is not entirely clear whether the baselines receive the same degree of hyperparameter tuning for their regularizers, or whether the deep Fourier method benefits from regularization tuning that the baselines do not receive.

### Trivial

- The paper uses the notation "desin" to refer to sin with α = 0.5 in Figure 4, which is confusing — it is not clear what "desin" means or why α = 0.5 is chosen rather than systematically varied.

## Nice-to-Haves

- A parameter-matched ablation (halving the width of the standard ResNet-18 to match the deep Fourier network's effective width) would further clarify that the gains come from the activation function itself, not from parameter count differences. The paper acknowledges the asymmetry but does not control for it. (Note: the asymmetry favors the baseline with more parameters, so this does not undermine the results — it would only strengthen the evidence to control for it.)

- A task-boundary-free evaluation (e.g., pixel-permutation changing every step) would test whether deep Fourier features generalize to settings without explicit task boundaries.

- An analysis of representation quality (e.g., effective rank of hidden activations) would empirically support the claim that deep Fourier features "balance linearity and nonlinearity" rather than just being linear in practice.

## Removed Points

- **Parameter count confounding (from the Harsh Critic's point 3):** Removed because the asymmetry favors the baseline (ReLU has more parameters), not the author's method. The paper explicitly states "this provides an advantage to the nonlinear baseline." If anything, this makes the deep Fourier results stronger.

- **Missing appendix proof (from Harsh Critic's point 2):** Removed per instruction — the parser strips appendix content from all papers; it exists in the original submission.

- **"The abstract's claim is not new" (from Harsh Critic's Section-by-Section Notes):** Removed per instruction — this is a generic observation that prior work used linear baselines, but the paper's contribution is the theoretical proof for the deep diagonal case and the proposed deep Fourier features, not the discovery that linear methods are plastic.

- **"No analysis of representation quality" (from Missing Parts):** Moved to Nice-to-Haves — this is a suggestion for additional analysis, not a weakness of what the paper does present.

- **"Missing baseline: ResNet-18 with sin activation alone" and "Missing ablation on number of Fourier components":** Moved to Nice-to-Haves — interesting suggestions that would add completeness but not core flaws.

- Various formatting/style nitpicks and speculative criticisms about unreleased artifacts: Removed.

## Novel Insights

The most interesting observation from the reviews is that the harsh critic's strongest analytical critique (the unit sign entropy definition) and the paper's strongest empirical contribution (the sensitivity analysis in Figure 7) point in opposite directions. The definitional error is real but confined to a supporting diagnostic; the sensitivity analysis shows an unusual and well-documented phenomenon — deep Fourier features remain trainable under regularization strengths that collapse standard networks — that does not depend on the entropy metric at all. A paper with this empirical finding would survive even if the entire unit sign entropy framing were removed. The reviewers agree that the method works; the debate is about how well the theory justifies it.

## Suggestions

1. **Fix Definition 1.** The unit sign entropy definition must be corrected. Options: (a) define a "sign diversity" metric ρ = 1 − |𝔼[sgn(h(x))]| ∈ [0, 1], which is 1 when the sign is equally split and 0 when the sign is constant; or (b) compute the binary entropy H(p) = −p log₂ p − (1−p) log₂(1−p) where p = P(sgn(h(x)) > 0); or (c) simply use the fraction of positive activations and rename the metric accordingly. Do not call it entropy if the formula does not compute entropy.

2. **Clarify the "approximate embedding" claim (Corollary 1).** Either provide a brief argument in the main text for why the input-dependence of the linear approximation does not break the embedding (or why it is acceptable), or soften the claim to match what is actually proven. An empirical plot comparing a deep Fourier network's activations to the best-fit deep linear network at initialization and during training would also help.

3. **Add a parameter-matched ablation.** Include a baseline where the standard ResNet-18's width is halved to match the deep Fourier network's effective width. This will definitively separate the activation function effect from the capacity difference.

4. **Clearly state the regularization protocol for every method** in the main experiment table, ideally in a dedicated column or footnote. The reader should know whether each baseline received individual hyperparameter tuning for its regularizer.

## Score and Decision

**Calibration summary:**

| Anchor Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| Towards Perpetually Trainable Neural Networks (KIq6p9iv2q) | 5.75 | R1, R2 | Weaker than current paper — less novel method (LN+L2), weaker experiments, similar topic |
| Rethinking Stability-Plasticity (YFdopzmpdr) | 5.20 | R1, R2 | Weaker — proposal is architectural splitting rather than activation function design |
| KAC: Kolmogorov-Arnold Classifier (qFeeJ2ZQiH) | 4.33 | R1 | Weaker — narrower scope (classifier only), less thorough experiments |
| Is multitask learning all you need (Pin2kdWloe) | 5.75 | R2 | Weaker — theoretical contribution limited to convex case, experiments on toy problems |
| Primal-Dual Continual Learning (GicZtgSlJW) | 5.00 | R2 | Weaker — mixed reviews on novelty, less comprehensive experiments |
| Critical Learning Periods (Aq35gl2c1k) | 7.25 | R2 | Stronger — cleaner theoretical analysis, no mathematical errors, but addresses a different question |
| Function-space Parameterization (2dhxxIKhqz) | 6.67 | R2 | Comparable — accepted with somewhat limited experiments but strong technical contribution |
| Optimal Protocols for CL (rhhQjGj09A) | 7.00 | R2 | Stronger — theoretically rigorous with optimal control framing |

**Round-1 bracket:** (3.5, 7.5) — the paper is clearly above the weak-anchor band (<3.5) and below the top band (>7.5).

**Round-2 narrowing:** The paper compares favorably to the 5.75–6.0 reject-range papers (stronger novelty and experiments than "Perpetually Trainable" and "Is multitask learning all you need"). It is weaker than "Critical Learning Periods" (7.25, accepted) due to a mathematical error in a supporting definition. It is comparable to "Function-space Parameterization" (6.67, accepted) in terms of overall impact, though the weakness profile differs (the current paper has cleaner experiments but a definitional error; the comparison paper had cleaner math but smaller-scale experiments).

The paper has a genuine contribution (novel activation design + strong empirical results + supporting theory) marred by a clear mathematical error in a non-core diagnostic. The error does not invalidate the main claims but requires correction. On the ICLR scale, this places the paper around the acceptance threshold — the strengths (novelty, experimental breadth, theoretical grounding for the linear case) outweigh the weaknesses (definitional error, partially justified embedding claim).

**Final score: 6.5 — Accept.** The paper would benefit from the suggested revisions but the core contribution is sufficiently novel and well-supported.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>