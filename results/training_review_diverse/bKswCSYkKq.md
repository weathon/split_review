Now I have a thorough understanding of the paper and can verify the reviewer claims against the actual content. Let me produce the final consolidated review.

## Summary

This paper addresses the stability-plasticity dilemma in Deep Reinforcement Learning (DRL) by introducing NBSP (Neuron-level Balance between Stability and Plasticity). The method identifies "RL skill neurons" — neurons whose activation patterns correlate with task performance — via a goal-oriented scoring function, then freezes these neurons via gradient masking while using experience replay to preserve prior knowledge. Evaluated on Meta-World and Atari benchmarks across two-task sequences, NBSP achieves near-perfect retention of the first task while successfully learning the second, outperforming EWC, ANCL, and an importance-weight-based variant. An ablation study further reveals that applying NBSP to the critic network is more critical than applying it to the actor.

## Strengths

- **First neuron-level method addressing both stability and plasticity in DRL.** The paper correctly identifies that prior work (Sokar et al., Nikishin et al.) focuses on plasticity only or operates at the network level. This is the first work to simultaneously target both at the granularity of individual neurons, as stated in the abstract and supported by the related work discussion.

- **Consistent and strong empirical results on two diverse benchmarks.** On Meta-World, NBSP achieves near-1.0 success rates on both the first and second tasks across all four task pairs (Figure 4). On Atari, NBSP obtains higher normalized returns than all baselines (Figure 7). The evaluation spans both continuous control (Meta-World/SAC) and discrete action spaces (Atari/DQN), demonstrating cross-domain applicability.

- **Insightful actor-critic analysis.** The ablation in Section 4.3 (Figure 6) systematically compares NBSP-Actor, NBSP-Critic, and full NBSP, showing that the critic is the more critical module for balancing stability and plasticity. The paper provides mechanistic reasoning tied to the recursive update of the critic and its role in guiding the actor (Section 4.3 paragraph 3), which is both novel and well-reasoned.

- **Comparison against Importance-based NBSP validates the identification method.** The paper includes an ablation that replaces the proposed RL-skill-neuron score with importance weights from Paik et al. (2019). The superior performance of the proposed method (Section 4.2, Figures 4 and 7) provides empirical evidence that the goal-oriented scoring function identifies more task-relevant neurons than a generic importance measure.

- **Simple, architecture-agnostic design.** NBSP requires no auxiliary networks, additional trainable parameters, or complex architectural modifications. Gradient masking and experience replay are standard techniques, making integration into existing DRL algorithms straightforward. The approach is compatible with any architecture that uses neuron-level operations.

## Weaknesses

### Fatal
None.

### Major

- **Key hyperparameters are unspecified, harming reproducibility and interpretability.** The paper states that "the number of RL skill neurons varies depending on the complexity of the task" (Section 3.2) but never specifies how many were selected in the reported experiments — not even a percentage, threshold, or adaptive criterion. The interval `k` for experience replay in Eq. (6) is not given numerically. The evaluation step `T` in Eq. (1) is not specified. Without these details, the method cannot be reproduced, and sensitivity to these choices is unknown. This is the single most significant weakness because it undercuts the paper's claimed advantage of being "parameter-free" — the method in practice has at least two critical knobs (number of skill neurons, replay interval) whose settings are undisclosed.

- **Baseline methods may not have been properly tuned for DRL.** EWC (Kirkpatrick et al., 2017) and ANCL (Kim et al., 2023) are from supervised continual learning and were designed for classification tasks, not actor-critic RL. The paper reports no hyperparameter search for these baselines (e.g., the regularization coefficient in EWC is critical and dataset-dependent). Without this, the claim that NBSP "significantly outperforms" these methods is difficult to evaluate fairly — the gap could partly reflect poor adaptation of the baselines rather than inherent superiority of NBSP. DRL-specific continual learning methods (e.g., policy distillation, Progress & Compress) are also not included as baselines.

- **The identification of RL skill neurons is correlational and lacks causal validation.** The Score in Eq. (3)–(4) measures how often a neuron's activation being above/below its mean coincides with the agent's performance being above/below its mean. This is a purely correlational measure. The comparison with Importance-based NBSP shows relative superiority but does not establish that these neurons causally encode task-specific skills. A direct causal test (e.g., ablating identified neurons and measuring performance drop on the first task vs. ablating random or low-scoring neurons) would validate the core premise. Without this, the mechanism of freezing these neurons to "preserve encoded knowledge" rests on an assumption that the paper does not independently verify.

### Minor

- **The ablation of gradient masking versus experience replay is incomplete.** Section 4.3 compares Base, Replay-Only, and NBSP (gradient masking + replay). There is no Mask-Only condition. The paper claims a "prominent role of gradient masking technique" (Section 4.3), but this conclusion requires a Mask-Only ablation to isolate its contribution from the combination effect. The improvement could theoretically come from the interaction rather than masking alone.

- **Evaluation is limited to two-task sequences.** Only four task pairs on Meta-World and four game pairs on Atari, each with exactly two sequential tasks. The stability-plasticity dilemma becomes substantially more challenging with longer sequences (5–10 tasks) where accumulated forgetting and gradual depletion of free neurons compound. The paper's claim of "generalization ability" (Section 4.4) would be strengthened by at least one longer sequence.

- **"Stably mastering" the task is not defined.** Section 4.1 states training continues "until reaching a predefined maximum step or stably mastering the task" but never defines the criterion for "stably mastering." If this criterion varies across seeds or task pairs, it introduces uncontrolled variation in training length, affecting fairness of comparisons.

- **Excluding the last layer is not justified.** Section 3.2 states that neurons in the last layer are excluded from the ranking, but no rationale is given. This is a non-trivial design choice — the last layer's neurons directly determine the output and could encode task-specific knowledge that should be frozen.

- **No statistical significance testing.** The paper claims NBSP "significantly outperforms" baselines (abstract, Section 4.2) but reports no statistical tests (e.g., Mann-Whitney U, bootstrapped confidence intervals) for the comparisons in Figures 4 and 7. The standard error bars are informative but do not constitute significance testing.

- **"Relevance" of Atari game pairs is not defined.** Section 4.4 mentions "two irrelevant and two relevant game pairs" but never defines what relevance means in this context or discusses how task similarity might affect the method's behavior.

### Trivial

- `T` (the evaluation step/accumulation batch size in Eqs. 1–3) is not specified numerically. This affects the stability of the score estimates.
- The claim of being "parameter-free" is slightly overstated — the method requires computing and storing running statistics (mean activation, mean performance) and identifying skill neurons, adding computational overhead even if no new trainable parameters.
- The paper does not report computational overhead (time/memory) of the neuron identification process, though this is acceptable for a methods paper.

## Nice-to-Haves

- A Mask-Only ablation condition to isolate gradient masking from experience replay would strengthen the contribution.
- Longer task sequences (e.g., 5 tasks) would demonstrate scalability beyond the simplest two-task setting.
- A sensitivity analysis on the number of skill neurons (e.g., 5%, 10%, 20%, adaptive threshold) would clarify how critical this hyperparameter is.
- Including DRL-specific continual learning baselines (e.g., policy distillation, Progress & Compress) would strengthen the evaluation.
- Raw scores (not just normalized) for Atari experiments would aid interpretability.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"NBSP appears to have zero variance" and "suspiciously perfect first-task performance."** The paper reports standard error bars on all bar charts (Figure 4 caption explicitly states "the bar length reflects the standard error"). Near-1.0 success with low variance is internally consistent for simple Meta-World tasks when the method is designed for knowledge retention. This is not a weakness.
- **"The paper does not report raw scores for Atari."** The paper uses normalized scores as standard in the Atari literature (following Mnih et al., 2015). This is a standard practice, not an omission.
- **"Eq. (4) treats positive and negative correlation symmetrically... a neuron whose activation always coincides with poor performance would yield a high score."** The paper explicitly acknowledges this design choice ("it overlooks neurons that exhibit a negative correlation with the goal but still carry valuable task-related knowledge") and deliberately takes the max(Acc, 1-Acc) to capture both types. The reviewer raises a conceptual concern, but the paper's design is intentional and explained.
- **"The paper does not discuss whether finer-grained per-weight masking could be more flexible."** This is a speculation about an alternative design, not a weakness of the current method.
- **"The experience replay formulation uses batch-switching (R(t) at specific intervals) rather than mixing."** This is a design choice, not a flaw. The paper clearly describes its formulation.
- **"The paper claims NBSP is parameter-free but identifying skill neurons adds memory and compute."** The claim refers to no additional *trainable parameters*, which is accurate. The computational overhead is a minor practical consideration, not a contradiction.
- **"The paper doesn't mention DRL-specific CL methods" under Section-by-Section Notes.** This is already covered in the baseline tuning concern above (Major weakness).
- **"ANCL and EWC are from supervised CL and not DRL-native."** This is already captured in the Major weakness about baseline tuning.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel perspective that the paper itself does not already articulate. The harsh critic's observation that the critic's recursive update (via target network EMA) explains its outsized role in stability is already discussed in Section 4.3.

## Suggestions

1. **Specify all key hyperparameters:** Add the number/percentage of skill neurons selected, the replay interval `k`, and the evaluation step `T` to the experimental configuration. Include a sensitivity analysis for the number of skill neurons.
2. **Add a Mask-Only ablation** to isolate the contribution of gradient masking from experience replay.
3. **Add a causal validation experiment:** Ablate identified RL skill neurons (set to zero or remove) after training and measure performance drop on the first task, comparing against ablation of random or low-scoring neurons.
4. **Tune baselines properly** with a hyperparameter search (especially EWC's regularization coefficient) and/or include DRL-native baselines. Report the search ranges and final values.
5. **Define the "stably mastering" criterion** concretely (e.g., success rate > 0.95 for 10 consecutive episodes).
6. **Add longer task sequences** (3–5 tasks) for at least one domain, even a single sequence, to show the method does not degrade with more transitions.
7. **Justify the exclusion of the last layer** from skill neuron identification.
8. **Add statistical significance tests** (e.g., bootstrapped confidence intervals) for the main comparisons.
9. **Define "relevance" for Atari game pairs** and discuss how task similarity affects the method.

## Score and Decision

The paper addresses a well-motivated problem with a novel, intuitive approach. The core idea — identifying task-relevant neurons via a goal-oriented correlation score and freezing them — is creative, and the empirical results on two-task sequences are compelling. The actor-critic analysis is a genuine contribution that provides actionable insight for future DRL continual learning.

However, the paper has three significant issues that prevent acceptance in its current form: (1) the lack of causal validation for the central construct of "RL skill neurons," (2) unspecified key hyperparameters that harm reproducibility, and (3) concerns about whether baselines were properly tuned. These are addressable but not trivial. The evaluation is also narrower than the claims suggest (only two-task sequences).

The paper does not have fatal flaws — the approach is sound, the results are credible where presented, and the weaknesses are fixable. But as submitted, the evidence supporting the core contribution is incomplete, and the missing hyperparameter details prevent independent verification.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>