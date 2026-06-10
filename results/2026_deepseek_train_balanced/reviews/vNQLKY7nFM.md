Here is my consolidated review.

---

## Summary

This paper proposes learn2mix, a training strategy that dynamically adjusts class proportions within mini-batches based on real-time class-wise error rates. The method updates mixing parameters at each epoch via α^t = α^{t-1} + γ(L(θ^{t-1})/sum − α^{t-1}), biasing batch composition toward harder classes. Experiments span classification (6 datasets), regression (3), and reconstruction (3), with comparisons to classical training, focal loss, and SMOTE.

## Strengths

- **Proposition 2.3 provides a non-trivial formal characterization of the mixing parameter dynamics.** Under strong-convexity and Lipschitz-gradient assumptions, the paper proves α^t → α* = L(θ*)/𝟙^T L(θ*) — the adaptive proportions converge to a distribution proportional to the optimal class-wise losses (Eq. 9). This gives the method a principled anchor beyond heuristic intuition, and the result is specific to the learn2mix update (not a generic convergence property).

- **Broad empirical scope across three task families.** The paper tests on 6 classification datasets (3 balanced + 3 imbalanced), 3 regression datasets, and 3 image reconstruction datasets, with consistent qualitative trends favor-ing learn2mix. The range of tasks is broader than typical class-imbalance papers which focus solely on classification.

- **Cyclic selection mechanism (Eq. 12-13) is a concrete solution to a practical implementation challenge.** When α varies across epochs, the modular wrap-around index τ_i^p = (τ_i^{p-1} + α_i M) mod α̃_i N ensures uniform, repeatable sampling without exhaustion. This bridges the mathematical formulation to a working algorithm (Algorithm 1).

- **Classification benchmarks against focal loss and SMOTE baselines (Table 1).** The paper compares against two established class-imbalance methods across all six classification datasets, showing consistent improvements (e.g., CIFAR-100 at epoch 90: 15% accuracy vs. 13.3% focal, 13.4% SMOTE).

## Weaknesses

### Major

- **The theoretical analysis rests on strong-convexity assumptions that are violated in every experiment, yet is presented as supporting empirical claims.** Propositions 2.3, 2.5 and Corollary 2.4 all assume each class-wise loss L_i(θ) is strongly convex in θ with Lipschitz-continuous gradients. The paper then evaluates exclusively on neural networks (LeNet-5, ResNet-18, transformers, autoencoders) trained with Adam on non-convex objectives. The abstract states "Our empirical findings are supported by theoretical analysis," but the theory's assumptions do not hold for any experiment conducted. This is not a minor gap — it means the theory section, as presented, does not connect to the paper's actual claims. The paper never acknowledges this limitation or discusses whether the results have any bearing on the experimental setting.

- **No statistical rigor in empirical evaluation.** Every result in Tables 1-2 and Figures 2-3 appears to be from a single run. No standard deviations, confidence intervals, or multiple random seeds are reported anywhere. For claims about convergence speed — inherently noisy and sensitive to initialization — single-run results are insufficient. The reader cannot assess whether reported advantages (e.g., learn2mix reaching 75% accuracy on MNIST in 14 epochs vs. 20 for classical) are systematic or within run-to-run noise. This is a baseline expectation for empirical papers at ICLR.

- **No wall-clock time comparison despite a resource-constrained motivation.** The paper motivates learn2mix by "resource-constrained environments" and "training efficiency," but reports only epoch counts. The per-epoch overhead of: (i) per-class loss computation at each epoch (Algorithm 1, line 15), (ii) the cyclic selection mechanism, and (iii) per-batch class-stratified sampling is never quantified. If the method adds even modest per-epoch overhead, epoch-count reductions could translate to net slowdowns. This omission directly undermines the stated motivation.

- **Proposition 2.5's condition is untestable, making the result practically vacuous.** Eq. (8) contains ‖θ^t − θ*‖ — the distance to the unknown optimal parameters — plus α̃^T(L(θ^t)−L(θ*)) and (L(θ^t)−L(θ*)), both also requiring θ*. The paper never checks whether this condition holds in experiments, nor provides guidance for when the method should or should not be applied. The "if and only if" framing implies that when the condition fails, learn2mix is provably worse than classical training, yet readers have no way to know which regime they are in. The existence claim for γ ∈ (0, β] with β deferred to the appendix further weakens the result's practical value.

### Minor

- **The outsized regression gains are unexplained.** On the synthetic Mean Estimation task, learn2mix achieves test error 2.0 after 100 epochs vs. 13.0 for classical (a 6.5× gap). On Wine Quality: 2.5 vs. 5.0 at 200 epochs. These improvements are dramatically larger than the classification gains (typically a few percentage points or a few epochs). The paper offers no analysis of why the method produces such disproportionate improvements in regression, nor does it rule out the alternative explanation that the classical baseline has poorly chosen hyperparameters for those tasks. Focal loss and SMOTE baselines are also absent for regression and reconstruction tasks.

- **No ablation or sensitivity analysis for the mixing rate γ.** Despite γ being the central hyperparameter controlling how aggressively class proportions adapt, no experiment studies sensitivity to γ on any dataset. The specific γ values used are deferred to the (stripped) appendix.

- **Discrepancy between the mathematical formulation and algorithmic implementation of the α update timing.** Definition 2.2 states α^t = α^{t-1} + γ(L(θ^{t-1})/sum − α^{t-1}), using the previous epoch's losses. Algorithm 1 computes class-wise losses *after* the model update (line 15 after line 13) and then updates α using the *new* losses (line 16). The algorithm effectively implements α^{t+1} = α^t + γ(L(θ^{t+1})/sum − α^t) — a different recurrence than the one analyzed theoretically. This notational inconsistency means the mathematical analysis may not exactly describe the implemented procedure.

### Trivial

- The specific learning rate η and mixing rate γ for each experiment are not reported in the main text. Deferring to the appendix is acceptable for full tables, but the main experimental section should state at least representative values.

## Nice-to-Haves

- A comparison against a simpler one-shot adaptive baseline (e.g., compute class-wise errors after one epoch, then statically oversample the worst classes for remaining epochs) would isolate whether the continuous adaptation mechanism is actually beneficial.
- Training-vs-test error curves would substantiate the "reduced overfitting" claim, which is currently asserted without direct evidence.

## Removed Points

Several criticisms from the harsh review were removed after cross-checking:

1. **"Convergence thresholds chosen post hoc to favor learn2mix"** — Removed as speculative. Different datasets inherently require different accuracy targets (CIFAR-100 maxes out much lower than MNIST), and the same threshold is compared across all methods per dataset. No evidence of manipulation.

2. **"The theoretical results do not distinguish learn2mix from classical training"** — Partially incorrect. Proposition 2.3's convergence of α to L(θ*)/sum *is* specific to learn2mix; the critic's claim that this is just "any gradient method converges under strong convexity" misses the α-dynamics result which is novel.

3. **Generic area-of-concern framings** — Removed speculative criticisms that lacked concrete anchors in the paper (e.g., "could the metric be measuring a proxy?"). These arose from the critic's category-driven sweep, not from identified problems in the text.

4. **Missing appendix content complaints** — Removed per instructions. The appendix is stripped by the PDF parser, not absent from the submission.

5. **Pure formatting nitpicks** — Removed.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one structural tension worth noting: the paper's theoretical framing (strong convexity → global convergence guarantees) and empirical framing (fast neural network training) operate in orthogonal regimes, yet the paper bridges them only with the phrase "supported by theoretical analysis." This exposes a recurring challenge in ML papers — providing rigorous analysis that genuinely informs practice rather than running on parallel tracks. The learn2mix idea may well be effective for reasons unrelated to the convexity analysis (e.g., as a form of adaptive importance sampling that reduces gradient variance on hard classes), but the paper does not explore this alternative framing.

## Suggestions

- **Replace or reframe the theory section.** Either adapt the analysis to the non-convex setting (e.g., analyze gradient variance, or frame as importance sampling), or explicitly acknowledge that the theoretical results assume strong convexity and state clearly that this does not hold for the neural network experiments. Do not claim the theory "supports" empirical findings without disclosing this gap.
- **Report all experiments with at least 5 random seeds, with means and standard deviations.** This is non-negotiable for convergence speed claims.
- **Report wall-clock time per epoch and total training time** alongside epoch counts.
- **Add a sensitivity analysis for γ** on at least one dataset (e.g., vary γ ∈ {0.01, 0.05, 0.1, 0.2, 0.5} on MNIST classification).
- **Add focal/SMOTE baselines to regression and reconstruction tasks** for consistency.
- **State all hyperparameter values (η, γ, architecture details) in the main text.**

## Score and Decision

The core idea has intuitive appeal and the empirical scope is admirably broad. However, the paper has decisive weaknesses at ICLR's bar: the theoretical analysis is structurally disconnected from the experiments (strong convexity assumed; neural networks used), the central comparison rests on single-run results with no variance estimates, the resource-constrained motivation is undercut by absent wall-clock measurements, and Proposition 2.5's key condition is untestable in practice. These issues collectively prevent the paper from making a convincing case for its claims. A substantially revised version could be competitive, but the current evidence does not support acceptance.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>