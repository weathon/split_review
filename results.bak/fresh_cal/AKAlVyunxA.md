Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

SHINE proposes a postmortem backdoor shielding method for deep reinforcement learning. It first identifies backdoor triggers via a two-stage explanation pipeline (step-level EDGE explanation followed by feature-level concrete-distribution mask optimization), then retrains the policy with a KL-constrained objective that theoretically guarantees improved performance under poisoning while bounding clean-environment degradation. The method is evaluated against three attack types across seven environments.

## Strengths

- **Novel two-stage trigger restoration that does not require a clean environment.** The paper's core contribution is a pipeline that first uses EDGE to identify critical timesteps within trajectories, then learns a binary feature mask via a concrete-distribution relaxation (Theorem 1) to isolate trigger features. This removes the impractical clean-environment assumption required by prior DRL defenses (Bharti et al., 2022; Guo et al., 2022). (Section 3.2, Theorem 1)

- **Theoretical guarantee for clean-performance preservation.** Theorem 2 bounds the clean-environment performance difference between original and retrained policies by the maximum KL divergence over clean states, directly supporting the paper's claim that SHINE preserves the agent's effectiveness in pristine environments. (Section 3.3, Theorem 2)

- **Consistent empirical outperformance over baselines across diverse settings.** Table 2 shows that SHINE-retrained agents achieve the highest operating-environment reward across all seven benchmarks (Atari Pong/Breakout/Space Invaders, SMAC QMIX/COMA, MuJoCo You-Shall-Not-Pass/Sumo-Humans/Run-To-GO-Ants), outperforming NC, FeatureRE, and direct retraining in every case.

- **No degradation on clean agents.** Table 3 shows that applying SHINE to already-clean agents produces only minor performance changes (often improvements), validating the practical claim that users can apply SHINE without needing to determine whether an agent is backdoored. (Section 4, Exp-III)

- **Robustness across attack variations.** Figure 2 shows SHINE's retraining performance across eight attack variations (different trigger patterns, sizes, poison rates) in Atari-Pong, with marginal performance variation and consistent outperformance over baselines. (Section 4, Exp-IV)

- **Applicability to both major backdoor attack categories.** SHINE is evaluated against perturbation-based attacks (single-agent Atari, multi-agent SMAC) and adversarial-agent attacks (two-player competitive MuJoCo), covering discrete and continuous action spaces. (Tables 1–2)

## Weaknesses

### Fatal

None.

### Major

- **Gap between theoretical guarantee and practical enforcement of the clean-state constraint.** Theorem 2 bounds clean-environment performance by the KL divergence over clean states, but the retraining algorithm (Section 3.3) does not actually access clean states — it approximates the constraint by comparing current state features against the restored trigger τ and classifying states as clean/poisoned via an unspecified threshold (line 110: "If their difference is within a certain threshold"). The paper provides no analysis of how classification errors (false positives/negatives in trigger identification) propagate to the performance guarantee. This disconnect weakens the theoretical contribution: the theory and the empirical algorithm operate under different assumptions, and the reader cannot assess how much the guarantee degrades under imperfect trigger identification.

### Minor

- **Underspecified criterion for collecting/selecting trajectories for trigger restoration.** The paper's intuition is built on "failing trajectories" (Section 3.1), and EDGE uses trajectory rewards as supervision to identify critical timesteps. In practice, the method collects trajectories and lets EDGE rank timesteps by mixing weights. However, the paper does not specify how many trajectories are collected, what reward distribution triggers "failure," or whether low-reward trajectories are explicitly filtered or handled implicitly by EDGE's model fitting. For a clean agent, EDGE would still identify "critical" timesteps even though no trigger exists — the paper's empirical evidence (Table 3) shows this works, but the algorithmic description is ambiguous about the selection logic.

- **Abstract claims comparison with Bharti et al. (2022) that the experiments do not support.** The abstract (line 16) states SHINE "outperforms... a state-of-the-art DRL defense (Bharti et al., 2022)," yet the experimental section explicitly excludes Bharti et al. from the baselines (line 126–127: "Bharti et al. (2022) requires accessing clean environments"). While excluding Bharti et al. is justifiable given different assumptions, claiming outperformance without an experimental comparison is misleading. The evaluation would be stronger if it included Bharti et al. on the subsets where it applies (perturbation-based attacks on discrete-action environments) to quantify the cost of SHINE's no-clean-environment assumption.

- **Sensitivity analysis limited to one environment.** Exp-IV (Figure 2) tests attack variations only on Atari-Pong against two baselines (Direct retraining and NC). To support the claim of "generalizability and practicability," the paper should test at least one additional environment (e.g., a MuJoCo environment for adversarial-agent attacks or SMAC for multi-agent perturbation attacks).

### Trivial

- **Underspecified threshold for clean/poisoned state classification.** The retraining algorithm (line 110) mentions "a certain threshold" for comparing feature values against the restored trigger τ but does not specify what threshold is used or how it is set. This is important for reproducibility.

- **Adversarial-agent trigger recovery is described only briefly.** Lines 85–86 describe identifying "a continuous trigger-present time slice in each trajectory" but do not explain how the slice boundaries are determined from EDGE's per-step importance scores or what threshold is used to define "continuous."

- **Missing ablation: is the feature-level explanation necessary?** The paper uses both step-level (EDGE) and feature-level (mask) explanations. An ablation that retrains using only step-level localization (masking random features at trigger-present timesteps) would clarify whether the fine-grained feature identification is essential.

## Nice-to-Haves

- Compare against Bharti et al. (2022) on the applicable subset (perturbation-based attacks in discrete-action Atari environments) to quantify the performance gap between SHINE's no-clean-environment setting and methods that assume access to a clean environment.
- Analyze how errors in trigger identification (false positives/negatives in the restored mask) affect the retraining guarantee — either through a theoretical bound incorporating classification error or a simulation with controlled mask degradation.
- Report the KL constraint threshold ε and its sensitivity, as the paper mentions hyperparameter sensitivity analysis (line 145) but does not present the results in the parsed text.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that the defender "knows the agent is backdoored in advance."** The paper explicitly states "we do not assume the knowledge of whether the shielding agent is backdoored or not" (Section 3.1, line 48) and applies the same pipeline to arbitrary agents (Table 3). The critic's inference that the method requires knowing the agent is backdoored is factually incorrect based on the paper's stated procedure.
- **Criticism that EDGE "was not designed for backdoor trigger identification."** Repurposing methods for new applications is standard research practice. The paper does not claim EDGE was designed for this purpose, only that its per-timestep importance scores are useful for localizing trigger-present timesteps. This is not a weakness.
- **Criticism about missing standard deviations for Table 3.** The paper explicitly states "We repeat each experiment 3 times with different random seeds and report the mean and standard deviation" (line 145). The parsed text cannot render the image-based table, so the std values are not visible, but they exist in the original submission.
- **Claim about the method's "structural gap" regarding trajectory selection.** The method does not require an explicit "failing trajectory" pre-filter — it collects trajectories with their rewards and uses EDGE's reward-supervised model to assign per-timestep importance. The intuitive "failing" language does not translate to a missing algorithmic component.

## Novel Insights

The most interesting observation emerging from these reviews is that SHINE's two-stage explanation approach creates a unique failure mode for adaptive attacks — the attacker cannot easily bypass both the step-level (EDGE) and feature-level (concrete mask) components simultaneously, because they operate on fundamentally different representations (temporal importance vs. spatial feature saliency). The paper's discussion of dynamic-trigger attacks (Section 5) correctly identifies this, but the reviews do not surface any deeper analysis of why this dual structure is resilient.

## Suggestions

1. Clarify the trajectory collection and "failing trajectory" language in Section 3.2 — specify exactly what the method collects, whether explicit filtering is applied, and what role trajectory reward plays in EDGE's timestep selection.
2. Either include Bharti et al. (2022) as a baseline on the subset where it applies (discrete-action Atari, perturbation-based attacks) or remove the claim of outperformance from the abstract.
3. Add a brief discussion in Section 3.3 on how clean/poisoned classification errors (from imperfect trigger identification) affect the guarantee in Theorem 2.
4. Report the threshold used for clean/poisoned state classification and the KL constraint value ε in the main text or appendix.
5. Extend Exp-IV to at least one additional environment (e.g., a MuJoCo adversarial-agent scenario) to support the generalizability claim.

## Score and Decision

The paper makes a genuine contribution — it is the first DRL backdoor defense that handles both perturbation-based and adversarial-agent attacks without requiring a clean environment, a practically motivated setup. The two-stage explanation + retraining pipeline is well-conceived, and the experiments demonstrate consistent results across seven environments. The weaknesses (theory-practice gap in the clean-state constraint, underspecified trajectory selection, and a misleading abstract claim about Bharti et al.) are real but addressable. None of them invalidate the core contribution or the strong empirical evidence.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>