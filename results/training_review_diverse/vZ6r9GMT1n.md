Now I have all the information needed. Let me verify the key claim about Theorem 1 carefully.

The paper defines "opposite action" on line 132: the attacker either "accept[s] a bad update or reject[s] a good one" — i.e., making a mistake. Higher probability of the attacker making a mistake = more robustness.

**Monotonicity check**: Let R = (2ν/μ) * (‖∇_{h(x)}(L∘g)‖² / ‖∇_x(L∘f)‖²). The argument to arctan is -(R)^{-0.5} = -1/√R. As R increases, -1/√R increases (from -∞ toward 0). Since arctan is monotonically increasing, arctan(-1/√R) increases with R. Since P(opposite action) "positively correlates with" this arctan value, P(opposite action) increases with R. Higher R → more attacker mistakes → more robustness. The monotonicity is correct. The harsh critic's claim of a sign error misunderstands that "opposite action" is defined as the attacker making a mistake (beneficial to defense), not the attacker succeeding.

Now I'll write the consolidated review.

---

## Summary

This paper proposes a lightweight defense against query-based black-box attacks by injecting Gaussian noise into intermediate hidden features at inference time, rather than perturbing the input as in prior randomized defenses (RND, SND). The core contributions are (1) a theoretical analysis (Theorem 1) linking the defense's effectiveness to the ratio of defense-to-attack noise variance and the ratio of gradient norms at the hidden layer versus the input, and (2) extensive empirical validation across 4 architectures (VGG19, ResNet50, ViT, DeiT), 2 datasets (ImageNet, CIFAR10), 3 score-based attacks (Square, NES, SignHunt), 2 decision-based attacks (RayS, SignFlip), and adaptive EOT attacks. The results consistently show that feature-space randomization outperforms input-space randomization at matched clean-accuracy drops.

## Strengths

1. **Consistent empirical advantage over input noise defense.** Across nearly all model–attack–dataset combinations, the feature defense achieves higher robust accuracy than input defenses at the same clean-accuracy drop. For example, VGG19 on CIFAR10 under Square attack at 4% clean drop: 62.8% (feature) vs. 39.8% (input); on ImageNet at 2% drop: 22.2% vs. 17.8%. This advantage holds for both score-based and decision-based attacks, demonstrating that the core idea is broadly effective.

2. **Theoretical framework connecting defense to gradient structure.** Theorem 1 provides a principled explanation of why feature noise helps, relating the probability of misleading the attacker to the ratio of noise variances and the ratio of gradient norms at the hidden layer vs. the input. This goes beyond prior randomized defenses (RND, SND) which rely solely on empirical motivation, offering a mechanistic understanding.

3. **Robustness against adaptive EOT attacks.** The defense retains superior robustness even when the attacker averages over multiple queries (M=5, M=10) to cancel randomness. E.g., VGG19 under Square with M=5 and 1000 queries: feature defense 53.0% vs. input defense 24.2%. This shows the defense is not trivially bypassed by adaptive strategies, strengthening practical relevance.

4. **Broad evaluation scope.** The paper evaluates against 5 attack types (including both score-based and decision-based), 4 architectures spanning CNNs and transformers, and 2 datasets. It also includes a comparison with AAA defense for decision-based attacks and combines the defense with adversarial training, showing orthogonal gains.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **No uncertainty quantification for robustness numbers.** Neither standard deviations nor confidence intervals are reported for any robustness result. Given that both the defense (noise sampling) and attacks (random search in Square, random probes in NES/SignHunt, random sign flips in SignFlip) involve substantial randomness, many comparisons differ by only 1–3 percentage points (e.g., DeiT Square at 1% drop on ImageNet: 69.1% feature vs. 67.2% input). Without variance estimates, it is impossible to assess whether these differences are statistically significant. This weakens the strength of the empirical evidence.

2. **Empirical support for the theoretical prediction is qualitative, not quantitative.** Table 5 (labeled `tab:layerwise_fix_scale`) shows a general trend that layers with higher gradient norms tend to yield higher robustness, consistent with Theorem 1. However, the trend is not perfectly monotonic (e.g., VGG layer 15 has lower GradNorm than layer 12 but higher SignHunt robustness: 37.4% vs. 29.4%), and no correlation coefficient or statistical test is provided. The theory predicts a specific functional relationship involving the ratio R = (2ν/μ)·(gradient norm ratio), but the experiments only vary one factor at a time (ν or the layer/position) without directly testing the predicted form. The theoretical claim therefore remains partially unvalidated.

3. **The assumption E[f_rand(x)] = f(x) is stated without sufficient justification.** The paper assumes that injecting zero-mean noise into intermediate features preserves the expected output exactly (Assumption 1). While the paper acknowledges this holds "when the variance of injected noise is small" (line 126–127), the assumption is non-trivial for deep non-linear networks: even small noise can produce biased expectations after passing through non-linear activations (ReLU, softmax, etc.). A brief discussion of when this approximation is reasonable (e.g., near-linear regions of the decision boundary) would strengthen the theoretical framing.

4. **The formal statement of Theorem 1 uses imprecise language.** The theorem states that the probability "positively correlates with" an arctan expression — but "positively correlates with" is not a precise mathematical relationship. This leaves ambiguity about whether the relationship is a linear correlation, a monotonic function, or an explicit formula. Moreover, since the arctan expression is negative-valued (ranging from -π/2 to 0), a probability cannot literally equal this value. A more rigorous statement (e.g., "the probability is a monotonically increasing function of ..." or an explicit formula) would improve clarity. This does not invalidate the theorem (the monotonic reasoning is correct — see verification above), but it is a presentation weakness.

### Trivial
None.

## Nice-to-Haves

- **Ablation on number of perturbed layers.** The current method perturbs all layers in set H. An experiment exploring whether perturbing a single carefully chosen layer (e.g., based on gradient norm) is as effective as perturbing multiple layers would strengthen the practical guidance.

- **Varying noise distribution and covariance.** Only isotropic Gaussian noise is tested. A brief experiment with other noise distributions (uniform, Laplace) or layer-dependent covariance would demonstrate robustness to hyperparameter choices.

- **Computational overhead measurement.** The defense is described as "lightweight" but no inference-time latency or memory overhead numbers are provided relative to input noise defenses. Adding these would strengthen the practical case.

- **Analysis of failure cases.** The paper acknowledges that on ResNet50 (ImageNet, Square) and DeiT (CIFAR10, NES), input defense sometimes matches or slightly exceeds feature defense. The paper's own theory (gradient norm ratios) should be able to explain these cases, but no explanation is offered. Doing so would strengthen the claim that the theory captures the mechanism.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic's claim of a sign error in Theorem 1.** The critic argues that the monotonicity is inverted and that a negative arctan cannot be a probability. This is incorrect: the paper defines "opposite action" (line 132) as the attacker accepting a bad update or rejecting a good one — i.e., making a mistake, which benefits the defense. Higher probability of opposite action = more robustness. The monotonicity is correct as verified above: as R = (2ν/μ)·(gradient ratio) increases, -1/√R increases toward 0, arctan increases, and the probability (which "positively correlates with" this value) increases. The paper does not claim the arctan value IS the probability, only that they are monotonically related. The criticism is based on a misreading.

- **Criticism about "unfair comparison" and baseline breadth.** The critic faults the paper for not comparing against other feature-level randomized defenses. The paper explicitly scopes its comparison (line 206: "the empirical robustness comparison of all adversarial defenses is beyond the scope of the paper") and focuses on the most natural baseline (input noise). This is a defensible scope choice, not a weakness.

- **Criticism about the assumption E[f_rand(x)] = f(x) being "stated without justification."** The paper explicitly adds the qualifier "When the variance of injected noise is small" (line 126) and notes that noise "diffuses but does not shift the prediction." The assumption is caveated. (The issue is retained in a downgraded form in Minor #3 as a suggestion for further justification, not as a flaw.)

- **Strength Finder's inflated claim about "six model architectures."** The paper evaluates 4 architectures (VGG19, ResNet50, ViT, DeiT) on each dataset. While line 210 says "6 victim models," only 4 are listed. This appears to be either a typo in the paper or a parsing artifact. The strength claim still holds for 4 architectures, so this does not weaken the contribution.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself does not articulate.

## Suggestions

1. **Add statistical rigor.** Report means and standard deviations over at least 3–5 random seeds for the main robustness tables. This is especially important because the comparisons are often close (1–3 percentage points) and both the defense and attacks involve randomness.
2. **Sharpen Theorem 1's statement.** Replace "positively correlates with" with a precise monotonicity statement: "the probability is a monotonically increasing function of ..." or provide an explicit formula. Clarify that the expression is not the probability itself but determines its monotonic behavior.
3. **Directly test the predicted relationship.** Design a controlled experiment fixing the gradient ratio and varying ν/μ, reporting the empirical attack success rate alongside the predicted monotonic trend (e.g., with a Spearman correlation). This would turn the theory from motivational into predictive.
4. **Justify the clean-accuracy drop choices.** The paper uses 1%/2% on ImageNet and 2%/4% on CIFAR10 without explanation. A brief rationale (e.g., "to ensure comparable absolute accuracy loss across datasets") would help.

## Score and Decision

The paper makes a solid contribution: the idea of shifting randomization from input space to feature space is simple yet effective, the empirical evaluation is broad, and the theoretical analysis (while imprecise in its formalization) provides useful mechanistic insight. The main shortcomings are the lack of uncertainty quantification and the gap between the theory's predictions and their empirical validation. Neither weakness is fatal — both are addressable — but they reduce the strength of the evidence as presented. The paper is a clear accept at a solid venue; the weaknesses warrant minor revision rather than rejection.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>