Now I have all the evidence I need. Let me produce the consolidated final review.

## Summary

This paper studies the grokking phenomenon through the lens of neural network robustness. It claims a theoretical connection between l₂ weight norm decay and grokking via robustness (Lemma 4.1 / Theorem 4.2 / Corollary 4.3), proposes input-perturbation training to accelerate generalization, reports that standard training on modulo addition fails to learn commutativity before grokking (while perturbation training does), and introduces Perturb Mutual Information (PMI) and Perturb Entropy (PE) as metrics that correlate with the grokking phase transition.

## Strengths

- **Discovery that standard training fails to learn commutativity before grokking.** Section 5.1/Figure 5 shows that on the modulo addition dataset, standard training does not produce commutative predictions (a+b vs b+a) until test accuracy spikes, while perturbation training learns commutativity immediately after training accuracy reaches 100%. This is a non-obvious mechanistic finding. The abelian degrok regularizer (Figure 6) further confirms commutativity is a necessary condition — directly enforcing it accelerates training even more than the perturbation method.

- **Perturbation-based training demonstrably accelerates generalization on two grokking settings.** Section 4.2/Figure 4 shows that adding Gaussian noise to inputs (with an adaptive schedule σ = max(λ₁(1−train_acc), λ₂)) speeds up the rise of test accuracy on both MNIST and the Modulo Addition dataset compared to standard training. The method is simple and provides a concrete proof-of-concept that robustness-enhancing interventions can reduce the grokking delay.

- **New information-theoretic metrics (PMI and PE) that change sharply at the grokking phase transition.** Definitions 6.3 and 6.4 introduce PMI and PE based on matrix-based information theory on perturbed feature gram matrices. Figures 8 and 9 show both metrics undergo a sharp change precisely when test accuracy rapidly increases, in contrast to the smoother, earlier decay of the l₂ weight norm. The ablation on α (Figure 10) confirms the trend is stable across α values.

## Weaknesses

### Fatal
None.

### Major

1. **Corollary 4.3 is post-hoc curve-fitting, not a validated theoretical prediction.** The corollary assumes the arbitrary functional form ‖W*‖²S(W*) = max²{a − b log₁₀(train-steps), 0}/(4n) with no derivation from training dynamics. The parameters a = 1925 and b = 500 are chosen without justification to make the predicted curve match the real accuracy (Figure 3). Any theory with two free parameters chosen post-hoc can fit a sigmoidal shape; this does not constitute evidence for the proposed robustness mechanism. This undermines the paper's central claimed contribution of a "theoretical explanation" for grokking's phase transition.

2. **The perturbation-based degrokking method lacks critical baselines.** Section 4.2 compares perturbation training only against standard training. There is no comparison to other straightforward methods that might accelerate grokking — e.g., tuning weight decay strength, increasing learning rate, using dropout, label smoothing, Mixup, or simply training with different initialization seeds. Without these comparisons, it is unclear whether the speedup is specific to perturbation's robustness effect or is achievable via other common regularization techniques. The claim that perturbation training is an effective "degrokking" strategy is uncontextualized.

3. **No error bars or multiple seeds are reported anywhere.** All results appear to be from single runs. Given the chaotic behavior observed in the logits distance for the perturbed model (Figure 7b) and the staircase-like curve on the algorithmic task (noted but "left for future work"), reproducibility is a concern. The claimed speedup on MNIST (Figure 4) may be marginal or non-significant; without error bars this cannot be assessed.

4. **The new metrics (PMI, PE) change simultaneously with test accuracy, not before it.** The paper claims these "correlate better" with grokking than l₂ weight norm. However, the l₂ norm decays before grokking (which could serve as an early warning signal), while PMI/PE change sharply at the same time as test accuracy rises. A metric that moves in lockstep with the phenomenon is a measurement of it, not a superior indicator for monitoring or prediction. The paper does not compute any quantitative correlation measure (e.g., time-lagged cross-correlation) or demonstrate that PMI/PE could predict grokking onset in advance.

### Minor

1. **The commutative law analysis is not tested on other algorithmic tasks.** The discovery about commutativity learning is specific to modulo addition. The paper does not test whether analogous necessary conditions exist for other group operations (e.g., subtraction, composition) or whether the same analysis applies to the MNIST setting where no such symmetry exists. This limits the generality of the explanation for why perturbation training works.

2. **The connection between commutativity learning and perturbation training is correlational, not causal.** The abelian degrok regularizer (Figure 6) shows that directly enforcing commutativity speeds up training. The paper then argues this explains perturbation training. However, it does not ablate whether learning commutativity is *sufficient* for grokking, or whether perturbation training also induces other beneficial properties (e.g., learning other symmetries, increasing loss landscape smoothness). The representation analysis (Figure 7) actually shows the two methods converge to *different* representations (chaotic vs. stable logits), weakening the claim that they work through the same mechanism.

3. **The adaptive noise schedule is not ablated.** The paper uses σ = max(λ₁(1−train_acc), λ₂) with no comparison to fixed noise levels. The perturbation strength is large on the algorithmic task (σ up to 0.4 on token embeddings) and much smaller on MNIST (σ up to 0.06), but no sensitivity analysis is provided. It is unclear whether the adaptive component matters or whether constant noise at an appropriate level would perform similarly.

### Trivial
None.

## Nice-to-Haves

- A real theoretical derivation showing that robustness *causes* grokking (rather than correlating with it) would substantially strengthen the paper. This would require showing that under the training dynamics, the network's robustness on training data converges to a level sufficient to generalize, and that this convergence triggers the phase transition.
- Controlled experiments that isolate the effect of robustness — e.g., comparing perturbation training to adversarial training, Jacobian regularization, or other methods known to directly control the Lipschitz constant — could establish whether the speedup is indeed driven by robustness.
- Demonstrating that PMI/PE can predict the onset of grokking *before* test accuracy rises (e.g., by showing they cross a threshold earlier, or correlate with time-to-grok across hyperparameter settings) would transform them from descriptive measurements into genuinely useful indicators.

## Removed Points

- **Theorem 4.2 contains an incomplete expression (ε(W*) = min{1, }).** The garbled text / missing symbols in the PDF extraction are parser artifacts, not author errors. The original submission is assumed to contain a complete expression. *Removed per hard rule: parser formatting artifacts.*

- **No proof or proof sketch is provided for Theorem 4.2 / Corollary 4.3.** Proofs that were present in the original submission's appendix may have been stripped during PDF-to-text conversion. *Removed per hard rule: missing proofs in appendix.*

- **The paper speculates that data augmentation explains why grokking is uncommon.** The paper phrases this as "It may also explain why..." — a hedged conjecture, not a claimed result. This was flagged as a weakness but does not constitute a substantive flaw in the paper's core contributions. *Removed as overly speculative criticism of a hedged statement.*

- **The PMI/PE metrics are computationally expensive.** While true, this is a practical limitation the paper acknowledges (Section 6: "relatively high computation overhead"), and the paper proposes batch-wise approximations to address it. The computational cost does not invalidate the metrics' utility as research tools. *Demoted from weakness.*

- **The critic claims the l₂ weight norm is a better signal because it changes earlier.** This misinterprets the paper's claim. The paper says l₂ norm correlates "not in a timely way" (i.e., it changes too early/smoothly to be a precise indicator), whereas PMI/PE are claimed as *better indicators* (more tightly coupled to the phenomenon), not as *predictors*. The paper's claim is internally consistent even if the practical value is limited. *Removed from weaknesses; subsumed into Major weakness #4.*

- **Generic area-of-concern sweep criticisms** (e.g., "could the metric be measuring a proxy", "are confounders controlled") that lack concrete anchors in the paper text. *Removed per filtering discipline.*

## Novel Insights

The primary novel insight from the reviews is that the paper's most valuable contribution is not its theoretical framework (which is weak) but its *empirical discoveries* — particularly the finding that standard training fails to learn commutativity before grokking, and that perturbation training induces commutativity learning early. This observation opens a concrete, testable mechanistic hypothesis about grokking: that grokking corresponds to the moment the model transitions from a memorized lookup-table strategy to one that respects the algebraic structure (commutativity) of the operation. The fact that the abelian degrok regularizer (which directly enforces commutativity) outperforms even the perturbation method strongly suggests commutativity is a key bottleneck. The weakness is that this insight is currently tied to a single task (modulo addition), and the paper does not establish whether this mechanism generalizes.

## Suggestions

1. **Reframe the paper as an empirical investigation** and downgrade the theoretical claims. Remove or substantially caveat the claim of providing a "theoretical explanation" of grokking. The Lemma 4.1 bound connecting weight norm to robustness is fine as a motivating observation, but Corollary 4.3 should be clearly labeled as a post-hoc fit, not a derivation. The paper's genuine contributions (commutativity finding, perturbation method, new metrics) stand on their own.

2. **Add baselines** comparing perturbation training to tuning weight decay, dropout, label smoothing, or other standard regularization techniques. Without this, the degrokking claim is unsubstantiated.

3. **Report results across multiple seeds** with error bars. This is essential given the chaotic dynamics observed (staircase curves in Figure 4b), chaotic logits in Figure 7b).

4. **Ablate the adaptive schedule** against fixed noise levels to understand whether the adaptive component matters and how sensitive the method is to σ.

5. **For the PMI/PE metrics**, demonstrate some practical utility — e.g., show they can predict grokking time across different hyperparameter configurations, or show they correlate with time-to-grok in a quantitative (not just visual) sense.

6. **Test the commutativity analysis** on at least one other algorithmic task (e.g., modulo subtraction, which is also commutative) to establish generality.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>