Now I have a thorough understanding of the paper and can verify the reviewers' claims against the actual text. Let me produce the final consolidated review.

---

## Summary

This paper proposes SHINE, a backdoor defense for deep reinforcement learning (DRL) that combines explanation-based trigger identification with constrained policy retraining. SHINE uses a two-stage explanation method (step-level via EDGE, then feature-level via a learned Bernoulli mask) to identify backdoor triggers from failing trajectories, then retrains the policy using a constrained objective (Eq. 4) that aims to improve poisoned-environment performance while bounding clean-environment degradation. Experiments across seven environments (Atari, MuJoCo competitive, SMAC cooperative) and three attack types show SHINE outperforms existing defenses (NC, FeatureRE, direct retraining, and Bharti et al. 2022) and preserves clean-agent performance.

## Strengths

- **First unified defense covering both perturbation-based and adversarial-agent backdoor attacks in DRL.** The paper correctly identifies that prior DRL-specific defenses (Bharti et al., 2022; Guo et al., 2022) each handle only one attack family (Section 1, Section 2). SHINE is evaluated against both types across single-agent, two-player competitive, and multi-agent cooperative environments (Section 4.1), demonstrating generality that no previous work achieves.

- **Strong empirical results across diverse settings.** In Table 2, SHINE consistently achieves the highest operating-environment performance while preserving or improving clean-environment performance (e.g., Pong: 11.0 operating / 13.2 clean vs. best baseline Direct Retraining at 6.8 / 4.1). SHINE also maintains clean-agent performance when applied to non-backdoored agents (Table 3), which is a practically important property since users cannot know a priori whether an agent is backdoored.

- **Practical threat model without requiring a clean environment.** The paper explicitly motivates why assuming access to a clean environment is unrealistic in DRL (Section 3.1, self-driving car example). SHINE operates entirely in the operating environment, which is a stricter and more practical assumption than prior work (e.g., Bharti et al., 2022 requires a clean environment).

- **Robustness to attack variations.** Exp-IV (Figure 2) tests eight variants of trigger patterns, sizes, and poison rates; SHINE shows only marginal performance variation and consistently outperforms baselines, supporting practical deployability.

- **Theoretical analysis of clean-performance retention.** Theorem 2 provides a bound connecting KL divergence on clean states to clean-environment reward difference, giving principled motivation for the retraining constraint, and the empirical results are consistent with this analysis.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Mismatch between Theorem 2 (max-KL) and the practical constraint (expected KL in Eq. 4).** Theorem 2 bounds the clean-environment performance difference by the *maximum* KL divergence over clean states, but Eq. 4 uses an *expected* (average) KL divergence. Since the max is always ≥ the expectation, the expected-KL constraint does not directly enforce the max-KL bound. The paper states "By solving Eqn. 4, we theoretically guarantee" the performance bound (line 108), which overstates what the theory actually certifies. This is a standard relaxation in the RL community (cf. TRPO's own theory-practice gap), but the paper should acknowledge the gap or provide justification (e.g., a concentration bound). As is, the theoretical claim is technically imprecise.

2. **No analysis of how trigger-identification errors affect downstream retraining.** The step-level explanation (EDGE) identifies "critical time steps" under the assumption that failures are trigger-induced, but failures could also arise from exploration noise, stochastic transitions, or the agent's suboptimal base policy. The paper does not analyze false-positive or false-negative rates for per-state classification (clean vs. poisoned), nor how such errors would affect the KL constraint in Eq. 4, which depends on correct clean-state identification (Section 3.3, line 110). The F1 scores in Table 1 measure trigger-pattern reconstruction, not per-state classification accuracy — these are different metrics. The strong empirical results mitigate this concern, but the analysis gap weakens the claimed theoretical-practical alignment.

3. **Missing experimental comparison with Guo et al. (2022) in adversarial-agent environments.** Guo et al. (2022) is the only other DRL-specific defense for adversarial-agent attacks. The paper correctly notes it only handles that one attack type (Section 2), which is exactly why it is a relevant baseline for the adversarial-agent experiments (Sumo-Humans, You-Shall-Not-Pass, Run-To-Go-Ants). Including this comparison would directly test SHINE's claim of practical superiority. The paper's core contribution (generality across attack types) does not hinge on beating Guo et al., but the omission leaves the empirical evaluation incomplete relative to the most relevant prior work.

4. **Several hyperparameters and thresholds are unspecified.** (a) The threshold for selecting "critical time steps" via mixing-weight ranking (Section 3.2, "top mixing weights" — top-k or top-%?); (b) the threshold for classifying states as clean vs. poisoned during retraining (Section 3.3, "within a certain threshold"); (c) the regularization coefficient λ for the elastic-net penalty in the feature-level explanation (Section 3.2). These are needed for reproducibility.

5. **Exp-IV sensitivity analysis is limited to one environment (Pong).** While the eight attack variations within Pong are informative, the sensitivity of the method to attack variations in other environments (e.g., MuJoCo or SMAC) is not tested.

### Trivial
- The paired t-test is mentioned (line 132) but p-values are not reported.
- Standard deviations for F1 scores in Table 1 are mentioned as reported but not visible in the text version.
- The adaptive-attack discussion (Section 5) is qualitative and lacks quantitative comparisons against a successful adaptive attack.

## Nice-to-Haves
- An analysis of per-state classification accuracy (clean vs. poisoned) would bridge the gap between trigger-pattern F1 scores (Table 1) and the downstream retraining guarantee.
- A discussion of the max-KL vs. expected-KL gap (perhaps noting it mirrors TRPO's theory-practice distinction) would improve theoretical honesty.
- Reporting p-values for the paired t-test mentioned in the experimental design.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The adaptive-attack section is speculative"** — The Discussion section is precisely where speculation and future work belong. The paper honestly acknowledges the limitations of its adaptive-attack analysis. Not a weakness.
- **"The paper does not describe how mixing weights are thresholded"** — This is a valid missing-detail point, folded into Weakness #4 above rather than standing alone.
- **"NC and FeatureRE cannot handle continuous action spaces"** — The paper explicitly states this (line 126). This is the paper's own description of baseline limitations, not an author oversight.
- **"The paper should also include LIME-based explanation baselines"** — The paper already discusses this in its Limitations section (line 184) as future work. This is scope creep beyond what the paper claims to deliver.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one genuinely novel observation: the tension between Theorem 2 (which guarantees clean-performance retention under max-KL) and Eq. 4 (which uses expected KL) is not merely a presentation gap but a structural one — it means the paper's theoretical guarantee does not, without further argument, actually follow from the optimization problem solved. This is a deeper point than a typical "clarify this sentence" and, if addressed (e.g., by showing that the expected-KL constraint empirically implies a max-KL bound under the policy's occupancy distribution), could strengthen both the theory and the paper's trustworthiness. No other novel insight emerges beyond what the paper itself provides.

## Suggestions

1. **Address the max-KL / expected-KL gap.** Either change Eq. 4 to constrain the maximum KL divergence (and discuss the practical difficulty of doing so), or provide a justification (e.g., a Lipschitz or concentration argument) showing that the expected-KL constraint bounds the max-KL deviation with high probability. At minimum, explicitly acknowledge the gap and note it as a relaxation consistent with prior work (Schulman et al., 2015).

2. **Add a comparison against Guo et al. (2022)** in the adversarial-agent environments (Sumo-Humans, You-Shall-Not-Pass, Run-To-Go-Ants). Even if adaptation is needed (e.g., to handle continuous triggering vs. one-shot), showing that SHINE is competitive would significantly strengthen the evaluation.

3. **Report per-state classification accuracy** for the clean-vs.-poisoned distinction used during retraining (Section 3.3). This would directly validate the critical intermediate step between trigger identification and retraining, and clarify the gap between full-trigger F1 (Table 1) and per-step reliability.

4. **Specify all thresholds and hyperparameters** needed for reproducibility: the critical-step selection rule (e.g., top-k or percentile), the clean/poisoned state classification threshold, and the elastic-net regularization coefficient λ.

## Score and Decision

**Originality:** 7/10 — The combination of explanation-based trigger restoration with constrained retraining is novel for DRL backdoor defense. The method is not entirely unprecedented (explanation + retraining has been explored in classification), but the adaptation to the sequential RL setting and the unification across attack types is a genuine contribution.

**Importance of research question:** 8/10 — DRL backdoor attacks are a real security concern, and practical defenses that don't require clean environments address an important gap.

**Claims support:** 6/10 — The empirical results are strong and well-demonstrated. The theoretical claims are partially weakened by the max-KL/expected-KL gap and the uncharacterized trigger-identification reliability. The central claim (first unified defense that works) is supported.

**Soundness of experiments:** 7/10 — Good breadth across environments and attack types, proper baselines (though missing Guo et al.), 3 seeds, and a sensitivity analysis. Minor reproducibility gaps (missing hyperparameters). The missing baseline comparison is the main limitation.

**Clarity of writing:** 7/10 — Well-structured and generally clear. Theoretical sections could be more precise about the gap between guarantees and practice.

**Value to community:** 8/10 — A practical, well-evaluated DRL defense that works across multiple attack types and environments will be useful to practitioners and provides a solid baseline for future work.

The paper makes a clear, well-motivated contribution to DRL security. The weaknesses identified are real but addressable and none are fatal: the theory-practice gap in the KL constraint is a standard relaxation, the missing baseline comparison is an omission but not a refutation, and the uncharacterized trigger-identification errors are partially mitigated by strong end-to-end results. With minor revisions addressing these points, the paper would be solid.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>