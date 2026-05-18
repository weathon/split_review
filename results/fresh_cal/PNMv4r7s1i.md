I have all the information needed. Let me now compose the final consolidated review.

## Summary

This paper proposes Behavior-Supported Policy Optimization (BSPO), a method to mitigate reward over-optimization in RLHF. The core idea is to model the "behavior policy" as the next-token distribution of the reward training dataset, then use a behavior-supported Bellman operator that penalizes Q-values for out-of-distribution (OOD) actions while preserving in-distribution (ID) ones. The paper provides theoretical guarantees (contraction, fixed-point properties, monotonic improvement to the optimal behavior-supported policy) and empirically evaluates BSPO across three proxy model scales against five baselines.

## Strengths

1. **Novel OOD detection via behavior policy.** The paper defines the behavior policy as the next-token distribution of the reward training dataset (Section 3.1) and empirically shows that the proxy model's preference accuracy drops from 75.91% for supported responses to 58.10% for unsupported ones. This provides a principled, data-driven OOD detection mechanism specifically for reward prediction in LLMs, which prior techniques could not do.

2. **Behavior-supported Bellman operator with differentiated ID/OOD handling.** Equation (1) and Theorem 2 define an operator that, at its fixed point, sets OOD state-action values to Q_min while preserving ID values for behavior-supported policies (Corollary 2). This is a cleaner approach than KL penalties or ensemble methods, which also penalize ID actions.

3. **Monotonic improvement guarantee to the optimal behavior-supported policy.** Theorem 3 proves that the policy optimization in Equation (3) yields strict monotonic improvement until reaching the optimal behavior-supported policy π_β^*. This theoretical guarantee is absent from prior regularization methods (KL penalty, CPPO, ensembles).

4. **Empirical avoidance of reward over-optimization across multiple proxy model scales.** Figure 3 shows BSPO achieving sustained gold reward growth at all three model sizes (774M, 1.1B, 2.7B), while all five baselines (PPO, KL-Penalty, CPPO, ENS-UWO, ENS-WCO) exhibit plateauing or decline. BSPO achieves the highest gold reward in every setting.

5. **Lightweight joint model (ScoreLM) for reward and behavior distribution.** ScoreLM adds minimal overhead by retaining the original LM head alongside a reward head (Figure 2), with comparable accuracy to a standard reward model (Figure 2b). This makes the method practical for existing RLHF pipelines.

6. **Direct causal evidence linking BSPO to reduced OOD generation.** Figure 4(b) tracks the average number of behavior-unsupported actions per response during RL: baselines show a sharp spike at the onset of over-optimization, while BSPO maintains consistently low counts throughout training.

7. **Superior performance at larger KL divergence distances.** Figure 4(c) shows BSPO avoids over-optimization even when the policy is far from the initial model, whereas KL-penalty methods fail at any distance that ventures beyond the ID region. This highlights that directly modeling the ID region (via β) is more effective than a generic distance constraint.

## Weaknesses

### Fatal
None.

### Major

1. **Missing specification of how β(a|s) > 0 is determined during RL.** The paper defines β as the next-token distribution of the reward training dataset (empirical distribution). In Section 4, ScoreLM is trained to approximate this distribution using a softmax output head. However, the paper does not specify how the binary condition β(a|s) > 0 in Equations (1) and (7) is checked during RL when using ScoreLM's predictions. Since a softmax output assigns technically non-zero probability to every token, without a threshold or binarization mechanism the condition would always be true, rendering the operator equivalent to the standard Bellman operator. Conversely, Section 3.1's analysis appears to use the empirical (count-based) distribution where zeros are meaningful. The paper must clarify whether (a) a threshold ε > 0 is applied to predicted probabilities, (b) the empirical training-data distribution is used for states that appear in the data, or (c) some other mechanism is employed. This gap affects reproducibility and the practical validity of the theoretical guarantees. (Reference: Section 3.1 lines 47-53, Section 4 lines 121-127, Equations 1 and 7.)

2. **Lack of error bars or multi-seed results for the main experimental claims.** The primary empirical evidence (Figure 3: gold reward curves across three model scales, Figure 4a: win rates, Figure 4b: OOD action counts, Figure 4c: KL comparison) is presented as single trajectories without error bars, confidence intervals, or any indication of variance across multiple runs. The paper reports standard deviation across four repetitions only for ScoreLM accuracy (Figure 2b). Given the known variance in RLHF training, it is impossible to assess the statistical reliability of the reported improvements. The paper should report means and variances across at least 3–5 random seeds for all central results. (Reference: Figure 3 caption, Section 5.2 lines 182-184, Figure 4 captions.)

### Minor

3. **Imprecise claim about "no impact on ID ones."** The abstract and introduction state that BSPO "penaliz[es] all OOD values without impacting the ID ones." However, Theorem 2 shows that for any policy π, the fixed point Q_β^π satisfies Q_β^π(s,a) ≤ Q^π(s,a) for ID actions (bounded above by, not necessarily equal to, the standard Q-value). Exact equality holds only at the fixed point for behavior-supported policies (Corollary 2). During iterative policy optimization before reaching a behavior-supported policy, ID actions could receive slightly lower values. The paper should replace the absolute "without impacting ID ones" with a precise statement that specifically characterizes the fixed-point behavior for behavior-supported policies. (Reference: Abstract line 4, Section 1 line 19, Theorem 2, Corollary 2.)

4. **Missing hyperparameter disclosure for baselines.** The paper does not provide a table of hyperparameter settings for the five baselines (PPO, KL-Penalty, CPPO, ENS-UWO, ENS-WCO), such as the KL penalty coefficient, ensemble size, or CPPO reward threshold. Without this, it is unclear whether baselines are fairly configured. A supplementary table would improve reproducibility and confidence in the comparison fairness. (Reference: Section 5.1 lines 180-181.)

### Trivial

5. **No variance reported for the 75.91% vs. 58.10% accuracy comparison in Section 3.1.** While these percentages are informative, the paper does not report the number of comparison pairs or any variance measure, making it difficult to assess the precision of these estimates. (Reference: Section 3.1 line 53.)

6. **The claim of being "the first method that uses value regularization to address reward over-optimization" (Section 1 contributions) is an overreach.** KL penalties and constrained reward methods also indirectly regularize value functions, though through different mechanisms. While BSPO's approach is novel in using the behavior-supported Bellman operator, the "first" framing is unnecessary and invites debate.

## Nice-to-Haves

- An ablation study removing the language modeling loss from ScoreLM to isolate its effect on OOD detection and downstream over-optimization would strengthen the claim that this auxiliary objective helps.
- A comparison with more recent methods such as weight-averaged reward models (Ramé et al., 2024) or lightweight uncertainty quantification (Zhang et al., 2024b), both cited in the related work, would strengthen the evaluation.
- A brief report of computational overhead (training time, parameter count) relative to standard PPO would substantiate the claim of "negligible additional overhead."

## Removed Points

These points were identified by reviewers but are removed for the following reasons:

- **Softmax makes β(a|s)>0 "always true" → method "vacuous" (Harsh Critic #1, fatal framing):** This claim misunderstands the paper. β is defined as the *empirical* next-token distribution from the reward training dataset (Section 3.1, line 47), not as the raw softmax output of ScoreLM. The empirical distribution has genuine zeros for tokens that never appear in a given context. ScoreLM is trained to approximate this distribution, and in practice a threshold would be applied. The critic conflates the true β (empirical) with its neural approximation. The implementation gap is real and retained as Major Weakness #1 above, but the "vacuous" characterization is factually incorrect and removed.

- **Criticism about "unfair comparison" asymmetries favoring baselines:** None of the identified comparison issues were asymmetric in favor of the author's method. The missing hyperparameter disclosure (Major Weakness #4) is retained as a legitimate concern.

- **Formatting artifacts / typos / parser errors:** Multiple garbled text segments appear (e.g., line 30) but these are PDF extraction artifacts, not author errors.

- **"Not yet released" or "cannot be independently verified" style claims about cited models/tools:** No such claims appeared in the reviews; the paper provides code in supplementary material.

- **Missing related works:** Not included; cannot be externally verified.

- **Requests for appendix proofs or appendix details that are stripped by the parser:** Not applicable; all proofs are in the main paper.

- **Strength Finder strength about the problem being "important" without specific evidence:** No such generic strengths were present; all listed strengths have concrete supporting evidence from the paper.

## Novel Insights

The most valuable observation emerging from the reviews is the tension between the theoretical definition of β (as an empirical distribution with exact zeros) and its practical approximation (a neural network with softmax outputs that assigns non-zero probability everywhere). This is not just a presentation issue — it reveals a genuine design consideration that the paper must address: how to bridge the discrete empirical support of the training data with the continuous function approximation needed for generalization during RL. The theoretical analysis (Corollaries 1 and 2) cleanly characterizes the ideal case, but the missing link to practical implementation is the paper's most significant unresolved issue. The second insight is that the "no impact on ID ones" framing, while approximately correct at the fixed point for converged behavior-supported policies, over-promises during the iterative process where ID values can be bounded above but not equal — a nuance that should be explicitly managed.

## Suggestions

1. **Clarify the β(a|s) > 0 condition during RL.** Specify whether a threshold ε is applied to ScoreLM's predicted probabilities, and if so, show the sensitivity to ε via an ablation. Alternatively, describe how the empirical training-data distribution is used during RL (e.g., caching n-gram statistics or using the dataset's empirical β directly for seen contexts with the learned approximation for unseen ones).

2. **Add multi-seed results with error bars.** Run all algorithms (BSPO and baselines) with at least 3 random seeds and report mean ± standard deviation (or shaded error bands) for gold reward, proxy reward, win rate, and OOD action counts. If computational constraints prevent this for all settings, provide it for at least one representative proxy scale (e.g., 774M).

3. **Precisify the claim about ID values.** Replace "without impacting ID ones" with a more precise statement such as: "At the fixed point for any behavior-supported policy, the behavior-supported Q-values for ID actions coincide with the standard Q-values (Corollary 2); during iterative optimization, ID values are bounded above by the standard values (Theorem 2), with the gap closing as the policy approaches a behavior-supported policy."

4. **Provide a hyperparameter table** listing the settings used for all baselines (KL coefficient, ensemble size, CPPO threshold, BSPO α, learning rates, etc.) to enable reproducibility and fair comparison.

5. **Consider adding** an ablation removing the language modeling loss from ScoreLM to isolate its contribution to downstream performance.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>