Now I have all the information needed to cross-check claims against the paper. Let me produce the final consolidated review.

---

## Summary

This paper investigates the grokking phenomenon (delayed generalization after overfitting) through a robustness lens. It makes four main contributions: (1) a theoretical argument linking $l_2$ weight norm decay to grokking via robustness bounds, (2) a perturbation-based training method (adding Gaussian noise to inputs) that accelerates generalization, (3) an analysis showing that learning the commutative law of modulo addition underlies the speed-up, and (4) new metrics (Perturb Mutual Information and Perturb Entropy) derived from robustness and information theory that are claimed to correlate better with grokking than weight norm. The paper studies both the MNIST image classification task and the Modulo Addition algorithmic dataset.

## Strengths

- **Novel connection between grokking and network robustness.** Lemma 4.1 provides a formal inequality linking weight norm, sharpness, and input-gradient magnitude (adapted from Ma & Ying, 2021). Theorem 4.2 then argues that as weight norm decreases, the neighborhood radius $\epsilon(W^*)$ increases, enabling more test samples to fall within a robust classification region. This provides a principled conceptual framework connecting the previously heuristic observation of weight norm decay to grokking, beyond existing explanations (Liu et al., 2022b; Nanda et al., 2023; Thilak et al., 2022).

- **Perturbation-based training demonstrably accelerates grokking.** Figure 4 shows a clear and dramatic speed-up of generalization on both MNIST and the Modulo Addition dataset when Gaussian noise is added to inputs during training, compared to standard training. The effect is visually unambiguous and reproducible.

- **Discovery that standard training fails to learn the commutative law before grokking.** Figure 5 reveals a genuinely surprising finding: during standard training on the modulo addition task, the model does not correctly predict $a+b = b+a$ (the "abelian test") on the training set until the moment it groks. This contradicts the natural intuition that the model would learn the simpler commutative property first.

- **Causal evidence via abelian regularization.** Figure 6 shows that adding an explicit MSE regularizer enforcing $f(a+b) \approx f(b+a)$ at the logit level speeds up grokking — even outperforming the perturbation-based method. This provides causal evidence that learning the commutative law is a bottleneck for grokking on this task, strengthening the explanatory claim.

- **Ablation on entropy order $\alpha$ (Figure 10) confirms metric robustness.** The trends in PMI/PE are stable across different $\alpha$ values and hold on the test dataset, showing the observations are not artifacts of a specific hyperparameter choice.

## Weaknesses

### Fatal
None.

### Major

- **Corollary 4.3 is post-hoc curve-fitting, not a derivation.** The corollary assumes a specific parametric form $\|W^*\|_F^2 S(W^*) = \frac{\max^2\{a - b \log_{10}(\text{train-steps}), 0\}}{4n}$ with hand-picked constants $a=1925$, $b=500$ — fitted to match the exact shape of one grokking curve on the Modulo Addition dataset — and then "predicts" the same curve. This is circular: the parameters are tuned to the very curve being predicted. The functional form is unmotivated, the constants are dataset-specific, and no independent verification on other runs or datasets is provided. This weakens the paper's first claimed contribution substantially; the paper would be stronger if it either derived the form or acknowledged this as an illustrative toy example rather than a validated theoretical result.

- **No quantitative evidence that PMI/PE "correlate better" than weight norm.** The paper claims PMI and PE "correlate better with the grokking process" than the $l_2$ weight norm, but supports this claim only with visual inspection of Figures 8 and 9. No correlation measure (Pearson, Spearman, or time-lag cross-correlation with test accuracy) is computed. The actual test accuracy curve also changes sharply at grokking time, so a visual comparison is insufficient to establish superiority over weight norm. A quantitative analysis is directly feasible and would either substantiate or refute the central claim of Section 6.

### Minor

- **No comparison of perturbation method against other simple regularizers.** The paper attributes the speed-up to "enhanced robustness" but does not compare against standard regularization techniques such as dropout, weight decay (beyond what the optimizer already applies), label smoothing, or fixed-strength noise. Without these baselines, it is unclear whether the benefit is due to *robustness specifically* or to any form of regularization that prevents overfitting. This weakens the mechanistic claim.

- **Adaptive perturbation schedule is ad-hoc and task-specific.** The hyperparameters $(\lambda_1, \lambda_2)$ differ by nearly an order of magnitude between MNIST $(0.06, 0.03)$ and the Modulo Addition dataset $(0.5, 0.4)$, with no sensitivity analysis or principled justification for these choices. This makes the method feel tuned per-task rather than principled.

- **The MSE theory (Section 4.1) does not directly cover the cross-entropy experiments.** The theoretical analysis uses MSE loss, but the main modulo addition experiments and the commutative-law analysis use cross-entropy loss. While the MNIST experiments use MSE (partially covering the gap), the paper acknowledges this mismatch (line 49) but does not address how the bounds might differ under cross-entropy. This makes the theory's relevance to the paper's central algorithmic dataset uncertain.

- **The explanation linking perturbation to commutative-law learning is incomplete.** The paper shows that (a) perturbation helps learn the commutative law earlier (Figure 5), and (b) explicitly enforcing the commutative law speeds up grokking (Figure 6). However, no mechanism explains *why* input-space noise specifically drives the emergence of a commutative representation. Point (b) provides causal evidence that the commutative law matters, but the chain from noise $\to$ commutative learning remains a black box.

- **No ablation on the number of perturbation samples for PMI/PE computation.** The paper notes that only one perturbation sample is used per batch for efficiency (line 203). This could introduce high variance in the metric estimates, and no analysis shows that the results are stable under different random seeds or more samples.

### Trivial
None.

## Nice-to-Haves

- A comparison between the proposed PMI/PE and simpler alternatives (e.g., feature variance under perturbation, gradient magnitude) would help clarify what specific information-theoretic quantity adds.
- Extending the commutative-law analysis to other algorithmic tasks (e.g., modulo multiplication or permutation groups) would test whether the finding generalizes beyond addition.

## Removed Points

- **"Theorem 4.2 is incomplete — the definition of $\epsilon(W^*)$ is missing a term."** The formula in the parsed text is garbled; this is a PDF parsing artifact. The original submission contains the complete expression. Removed per hard rule about parser artifacts.
- **"The perturbation method should be compared against methods the reviewer prefers."** Not removed — the request for standard baselines (dropout, weight decay) is reasonable. Kept in Minor.
- **"The abelian test on logits (Figure 7) doesn't explain why the difference matters."** The paper explicitly states the purpose: to verify that standard and perturbed training learn different representations despite similar accuracy. This is a valid justification. However, the analysis could go deeper — kept as implicitly addressed in the incomplete explanation point.
- **"The paper should also study X / Y / Z additional tasks."** Scope-creep demands. The paper covers two canonical settings consistent with prior grokking literature.

## Novel Insights

Beyond the paper's own contributions, the most noteworthy insight emerging from this review is the tension between the paper's two claims about the commutative law. The abelian regularizer experiment (Figure 6) provides *causal* evidence that learning the commutative law is a bottleneck, yet the perturbation method — whose success the paper attributes to exactly this mechanism — outperforms the explicit regularizer only on one metric dimension (the regularizer works *better* according to Figure 6). This raises the question: if explicit commutative-law regularization works even better than perturbation, what unique advantage does perturbation offer? The paper does not resolve this, and it suggests the full story may involve additional factors beyond commutative-law learning alone.

## Suggestions

1. Either remove Corollary 4.3 or reframe it explicitly as a toy illustration (not a validated prediction), or provide independent verification on held-out runs/datasets and motivate the parametric form.
2. Compute a quantitative correlation measure (e.g., normalized cross-correlation with time lag) between PMI/PE and test accuracy, and compare to the same measure for weight norm. This is a low-cost, high-impact addition that would directly support or refute the central claim of Section 6.
3. Add at least one alternative regularizer baseline (e.g., dropout at comparable strength, or fixed-strength noise without the adaptive schedule) to the perturbation experiments. This would help isolate whether the benefit is due to robustness or regularization.
4. Provide a sensitivity analysis for the adaptive perturbation hyperparameters, or replace the ad-hoc schedule with a simpler principled alternative.

---

**MY FINAL SCORE:** <pineapple>5.0</pineapple>
**MY FINAL DECISION:** <orange>Reject</orange>