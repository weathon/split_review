## Summary

This paper proposes Difference Back Propagation (DBP), which replaces the derivative of the sigmoid activation (a(1-a)) in the backward pass with a finite-difference ratio computed via the inverse sigmoid: dl/dz = (a' − a)/(z' − z) · dl/da, where a' is the updated activation after one gradient step and z' = inv_sig(a'). The authors argue that this "difference-based" gradient better respects the functional relationship between pre- and post-activation values under finite learning rates, and that it inherently avoids the sigmoid vanishing gradient problem by bypassing multiplication by the saturating derivative.

---

## Strengths

- **Novel use of inverse activation functions for gradient computation.** The idea of replacing the local derivative with a secant slope computed through the inverse of the activation function is unconventional and, to my knowledge, not explored in prior backpropagation literature. This opens a distinct direction for modifying backward passes.

- **Principled circumvention of the sigmoid's vanishing-derivative mechanism.** In DBP, the gradient signal propagated through the sigmoid does not contain the factor a(1-a). When a(1-a) → 0 but dl/da is non-zero (the classic vanishing regime), the DBP ratio (a′−a)/(z′−z) remains non-zero because it depends on dl/da rather than on the saturated derivative. This is a genuine structural difference from standard backprop, and the neuron trajectory plots in Figure 3 are consistent with this effect (z-values drifting less far into saturation).

- **Theoretical relaxation of the differentiability requirement.** The paper correctly notes that if a forward function has an inverse, DBP can be applied without computing its derivative, which in principle allows training with non-differentiable or even discontinuous activation functions. This is noted as a theoretical possibility (not demonstrated experimentally), but it is a distinctive conceptual contribution.

- **Practical awareness of numerical challenges.** The paper explicitly discusses the need to clamp a to (10⁻¹⁶, 1−10⁻¹⁶) to avoid overflow in the inverse sigmoid, mentions Taylor expansion as a potential solution near the boundaries, and describes handling the z′−z = 0 case. This shows the authors are aware of implementation pitfalls.

---

## Weaknesses

### Fatal

None. The method is well-defined and the core idea is not mathematically invalid — it is a particular choice of gradient surrogate. However, several major weaknesses collectively prevent acceptance.

### Major

- **The method's motivation is not properly grounded, and its properties are not analyzed.** The paper treats the fact that z_updated ≠ inv_sig(a_updated) under standard backprop as an "inconsistency" (Eq. 4, Figure 1) that needs fixing. But this is an expected property of first-order optimization with a finite step — the gradient at (z, a) does not align the updated values to lie on the function graph. Whether this "inconsistency" is actually harmful is never argued, let alone demonstrated. Meanwhile, DBP introduces a backward pass that depends on the learning rate η (since a′ = a − η·dl/da and z′ = inv_sig(a′) both depend on η), yet the paper never justifies why a learning-rate-dependent gradient signal is desirable, nor does it analyze how this changes the optimization dynamics. The method's relationship to any known optimization principle (e.g., proximal point, implicit gradient, target propagation) is absent.

- **No theoretical analysis of convergence or fixed points.** For a paper proposing a new learning algorithm, there is zero analysis: no convergence guarantees (even for convex models or linear networks), no characterization of fixed points, no discussion of whether the DBP update corresponds to the gradient of any objective function, and no analysis of how the learning-rate-dependent backward pass interacts with step-size choice. The weight update in DBP involves (dl/da)² and scales as η² rather than η (since a′−a = −η·dl/da), which is a fundamentally different dynamical system from gradient descent — this is never discussed or analyzed.

- **Experimental evidence is far too weak to support the claims.** The core experiments are on a (1,2,1) network and a (1,2,2,1) network trained on 100 synthetic points. There are no error bars, no multiple runs with different seeds, no statistical tests, and no train/validation split. The transformer experiment (AG News, d_model=32, 2 layers, 4 heads) is still a very small model, and the paper provides no details about the optimizer, learning rate schedule, or whether the same η was used for both the DBP backward computation and the weight update step. The reported improvements are marginal (zoomed-in plots in Figure 5 show gaps on the order of ~0.2–0.5% accuracy). With no repeated trials, these differences could easily stem from noise or hyperparameter sensitivity.

- **The claimed advantage of preventing gradient vanishing is not tested in relevant regimes.** Vanishing gradients in sigmoid networks become a serious problem in deep architectures (5+ layers). The paper's deepest network has two nonlinear layers. No experiment demonstrates that DBP helps train a deep sigmoid network where standard backprop fails, nor does the paper compare against standard remedies (e.g., careful initialization, batch normalization, or simply switching to ReLU). Without such evidence, the claim remains unsubstantiated.

- **The DBP weight update is never analyzed for its effect on multi-layer learning dynamics.** The paper only modifies the gradient through the activation; how this modified signal changes the effective weight updates, interacts across layers, or affects the loss landscape is not examined. Given the unusual η² scaling noted above, the behavior of DBP in deeper networks is unpredictable from the paper's analysis.

### Minor

- **No ablation of the numerical constraints.** The paper clamps a to [10⁻¹⁶, 1−10⁻¹⁶] and replaces zero divisors in (z′−z) with 1. These heuristics could dominate the method's behavior when the sigmoid saturates, yet no experiment isolates their effect (e.g., by comparing DBP with vs. without clamping, or testing sensitivity to the clamping threshold).

- **No discussion of computational overhead.** Computing inv_sig(a′) and the ratio (a′−a)/(z′−z) requires extra operations per activation backward pass compared to the cheap multiplication a(1-a)·dl/da. For large models this overhead could be non-negligible, but it is not mentioned.

- **The claim about non-differentiable activations is asserted but not tested.** The paper states DBP works for "any function that has an inverse function, even for those functions that are not derivable or even continuous," and mentions leaky ReLU as an example. No experiment demonstrates DBP training with a non-differentiable activation.

- **The transformer experiment is underspecified.** No optimizer name, learning rate, schedule, or batch size is reported; it is unclear whether the same η is shared between the DBP computation and the weight optimizer step, or whether different η values were tried.

- **Overclaiming in the conclusion.** The paper states DBP "has shown a better performance" and is "more accurate" — but the evidence shows marginal improvements on tiny problems, with no replication.

### Trivial

- The introduction enumerates large-scale datasets and models (ImageNet, BERT, V-MoE) as motivation, but the experiments never connect to scaling or efficiency. This creates a mismatch between the framing and the actual contribution.

---

## Nice-to-Haves

- A comparison of DBP against standard backprop + techniques that mitigate sigmoid saturation (e.g., normalized initialization, batch normalization) would help isolate whether the benefit comes from the modified gradient or simply from altered effective step sizes.
- Analyzing DBP on a deep sigmoid network (5–10 layers) where standard backprop is known to struggle would directly test the vanishing-gradient claim.
- The paper would benefit from connecting DBP to related ideas such as target propagation, implicit differentiation, or finite-difference gradient approximations, to place the method in context.
- Reporting multiple random seeds with error bars and a statistical comparison (e.g., paired t-test across runs) would greatly strengthen the empirical case.

---

## Removed Points

These points were flagged by the reviewers but are removed (with justification):

1. **"No new method for performing backpropagation has been proposed" is factually incorrect.** — The paper says "To our knowledge, no new method…" which is a qualified statement and a throwaway line in the introduction. This is a nitpick, not a substantive weakness. **Removed.**

2. **Missing code / not released at review time.** — Per policy, criticisms that question the existence or release status of artifacts cited in the paper are removed. **Removed.**

3. **The paper does not compare to other finite-difference or implicit gradient methods.** — This is scope creep; the paper does not claim to survey such methods. **Removed.**

4. **"The ratio (a′−a)/(z′−z) will still vanish if dl/da is small enough."** — While technically true, this misrepresents the claim. The vanishing gradient problem in sigmoids is that a(1-a) → 0 even when dl/da is large. DBP removes a(1-a) from the backward pass, so it avoids the *sigmoid-specific* vanishing mechanism. This criticism is factually misleading. **Removed.**

5. **No comparison with ReLU, batch normalization, or better optimizers.** — The paper's scope is a modified backward pass for sigmoid; demanding it outperform ReLU-based architectures is outside scope. **Removed/Moved to Nice-to-Haves.**

6. **The paper should test on Leaky ReLU or step function.** — Untested, but this is a request for additional experiments, not a flaw in what is presented. **Moved to Nice-to-Haves.**

---

## Novel Insights

Beyond the paper's own contributions, no genuinely novel insight emerges from the reviews that the paper itself does not already provide. The core tension — whether the "inconsistency" that DBP addresses is a real problem or a natural property of first-order methods — is noted but not resolved by either the paper or the reviews.

---

## Suggestions

1. **Add a proper theoretical section.** At minimum: (a) derive the effective weight update in terms of dl/da and show its relationship (or lack thereof) to the true gradient; (b) characterize fixed points — do they coincide with those of standard backprop? (c) analyze how the η² scaling affects stability and step-size choice, perhaps by relating DBP to a modified ODE.

2. **Run controlled experiments with error bars.** Train the same architectures with multiple random seeds (at least 10), report mean and standard deviation of final loss/accuracy, and include a statistical significance test. This is essential for a paper claiming a performance advantage.

3. **Test on a deep sigmoid network** where vanishing gradient is known to prevent training (e.g., 8–10 fully-connected layers with sigmoid on MNIST). If DBP succeeds where standard backprop fails, this would be strong evidence for the vanishing-gradient claim.

4. **Ablate the clamping heuristics.** Compare DBP with different clamping thresholds and verify that the method's behavior is not dominated by these numerical fixes.

5. **Provide full experimental details for the transformer experiment:** optimizer, learning rate, schedule, batch size, number of training steps, and whether DBP's η for the backward pass is the same as the optimizer's learning rate.

---

## Score and Decision

The paper introduces a genuinely different approach to computing the backward pass through sigmoid activations, and the idea of using inverse functions to construct finite-difference surrogates has some conceptual novelty. However, the paper is held back by: (1) a motivation that conflates a natural property of first-order optimization with a flaw, without justifying why fixing it is beneficial; (2) a complete absence of theoretical analysis of the proposed update's convergence, stationarity, or optimization properties; (3) experiments that are far too weak — single runs, no error bars, tiny networks, marginal improvements, and no testing in the regimes where the claimed advantages (vanishing gradient avoidance) would matter. The gap between the paper's framing (large-scale bottlenecks) and its evidence (toy problems) is vast. The contribution, while novel in concept, is not sufficiently supported for publication.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>