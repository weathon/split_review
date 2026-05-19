Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes HuRi, an adaptive risk-aware distributional reinforcement learning method for humanoid robot locomotion. It dynamically adjusts the risk sensitivity parameter β of a Wang distortion function by combining Inter Quartile Range (to measure intrinsic uncertainty from the return distribution) and Random Network Distillation (to measure parameter/state-novelty uncertainty). The method is trained on a simulated Zerith-1 humanoid robot using PPO with a distributional critic and tested under out-of-distribution forces, loads, and terrain variations, with deployment on a real robot.

## Strengths

1. **Novel combination of IQR and RND for adaptive risk sensitivity**: The paper's core idea — using two distinct uncertainty signals (IQR from the quantile return distribution for intrinsic uncertainty, RND for parameter/novelty uncertainty) to modulate β online — is technically sound and goes beyond prior methods that use fixed risk parameters. The design choice is well-motivated (lines 91–115).

2. **Robustness validated under challenging out-of-distribution conditions**: Table 1 shows HuRi achieving the highest success rates across all six disturbance conditions (continuous 0–100 N forces and sudden 150–200 N impacts on centroid, hands, feet), with the largest margin seen under sudden hand disturbance (93.6% vs. 87.0% for next-best). The test disturbances far exceed the training range ([0,10] N), making these results meaningful (lines 148, Table 1).

3. **Real-world sim-to-real transfer with substantively challenging loads**: On the Zerith-1 robot, HuRi maintains stable locomotion under a 15 kg centroid load (~42% of body weight) and 3 kg per foot loads at speeds up to 0.9 m/s — scenarios far exceeding training distributions — with lower velocity errors than baselines (Table 2, lines 177–186).

4. **Ablation isolates RND's contribution**: The comparison HuRi (90.86 avg return) vs. HuRi w/o RND (86.93) in Figure 3 demonstrates that the RND uncertainty module provides a measurable improvement beyond IQR-only adaptation, supporting the claim that both uncertainty sources are beneficial.

5. **Velocity tracking validated under combined disturbances**: Figure 4.C tests simultaneous load and friction variation — a more complex scenario than single-factor tests — and HuRi maintains the lowest linear and angular velocity errors.

## Weaknesses

### Fatal
None. The method is coherent, the core idea is sensible, and there is meaningful experimental evidence. The issues below are significant but correctable.

### Major

- **Missing fixed-β Wang baseline undermines the central claim about adaptivity.** The paper's core contribution is *adaptive* risk sensitivity — yet no experiment compares HuRi against a version using the *same* Wang distortion function with a *fixed*, well-tuned β. The baselines are: PPO (no risk), CVaR0.5 (different distortion, fixed risk), and HuRi w/o RND (still adaptive via IQR). This conflates three variables: (a) Wang vs. CVaR distortion, (b) adaptive vs. fixed β, and (c) IQR+RND vs. IQR-only. Without a fixed-Wang baseline, the reported gains could plausibly come from the Wang function itself rather than from adaptivity. This is the single most critical missing experiment. (Lines 133–135 confirm the baseline set; no fixed-Wang condition appears.)

- **Critical hyperparameters unspecified.** The IQR module discretizes intrinsic uncertainty into three levels (β_IQR ∈ {−1, 0, 1}) using thresholds t_min and t_max (line 97). These values are never reported, and no sensitivity analysis is provided. Since β_IQR directly determines the agent's risk preference (risk-seeking, neutral, or risk-averse), this is not a trivial implementation detail — it is essential for reproducibility and for assessing whether the method is robust to this design choice. Similarly, the combined loss function (Section 3.4, lines 122–124) lists individual terms (L_quantiles, L_expectation, L_surrogate, L_entropy) but never states their relative weights or the full equation.

- **Real-world experiments lack statistical rigor.** Table 2 reports success rates and velocity errors but provides no trial counts, no confidence intervals, and no description of how success/failure is determined for physical experiments. The lateral impact success rate for HuRi is 65% — this is a relatively modest success rate, and the gap over HuRi w/o RND (50%) and CVaR0.5 (40%) is based on unreported trial counts. Without this information, the real-world results are suggestive but not conclusive. (Lines 170–186; Table 2.)

### Minor

- **RND's known pitfall with domain randomization variables is not discussed.** The critic state s^{critic} includes e_t, the domain randomization variables (line 43). The RND predictor takes s^{critic} as input and may learn to use e_t to predict the target, making the prediction error small even for genuinely novel states. This is a known limitation of RND in randomized environments and is not acknowledged.

- **Training is limited to plane terrain only** (line 140: "All experiments are training on plane terrain"). The method is tested on uneven terrain only in a qualitative analysis (Figure 5), not in the comparative evaluation. The paper's own conclusion (line 193) acknowledges this as a limitation. However, since adaptive risk sensitivity would be most valuable precisely on varied terrain, the experimental scope weakens the claim's generality.

- **Figure 5 analysis is qualitative and from a single trial.** The claim that IQR(uneven) > IQR(push) > IQR(plane) and the corresponding β dynamics are shown for a single illustrative run without error bars or statistics (lines 160–165). While the pattern is intuitive, it does not constitute a rigorous validation of the adaptive mechanism.

- **β range not discussed.** β = β_IQR + β_RND yields values in (−1, 2) since β_IQR ∈ {−1,0,1} and β_RND ∈ (0,1) (lines 97, 108, 114). The paper does not discuss whether β is clipped or whether values outside [−1,1] produce meaningful distortions with the Wang function.

### Trivial

- **Section 3.1 labels a POMDP definition as "Theorem"** (line 32), which is a mislabeling — it is a definition, not a theorem. This does not affect the science.

## Nice-to-Haves

- A comparison against at least one contemporary method from the cited related works on distributional RL for legged locomotion (e.g., Schneider et al. 2024, Long et al. 2024) would strengthen the positioning.
- Reporting training time and inference overhead for HuRi vs. baselines (RND adds two forward passes per step).
- A failure analysis for the 35% lateral-impact failure cases in the real robot would help understand the method's limitations and guide future improvements.

## Removed Points

These points from the reviewers were identified for removal after cross-checking against the paper:

1. **"The formula for the quantile energy distance lacks explanation of indices i,j"** — Removed. The paper states that θ and 𝒯θ are derived from Z_θ and 𝒯Z_θ (line 69), which is sufficient for an expert reader familiar with quantile energy distances; the reference to Schneider et al. (2024) provides details.

2. **"Missing algorithm table for SR(λ)"** — Removed. The paper references Algorithm 2 for SR(λ) and notes it was provided in the appendix (line 63). Per policy, the appendix exists in the original submission and is not accessible due to parser stripping, not author omission.

3. **"Missing related works on adaptive risk in non-robot domains (Morimura et al. 2010)"** — Removed. Per policy, missing related work citations cannot be verified externally and should not be flagged.

4. **"The claim of being 'first' is too broad"** — Partially removed as a standalone weakness. The paper qualifies this with "To the best of our knowledge" (line 18), and the claim is specific to *humanoid robot* adaptive risk-aware policy learning, which is a narrow enough scope. The broader point about insufficient baselines is already covered under Major weakness #1.

5. **"No analysis of computational cost"** — Moved to Nice-to-Haves. This is relevant but not a core flaw affecting the paper's validity.

6. **"No failure analysis for real-world falls"** — Moved to Nice-to-Haves. This is a suggestion for improvement, not a weakness in the current work.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the need for tighter experimental design but do not introduce a new framing or unexpected synthesis not already present in the paper.

## Suggestions

1. **Add a fixed-β Wang baseline.** Train HuRi with β ∈ {−0.5, 0, 0.5, 1.0} (sweep) and compare against the adaptive version on the same evaluation suite. This directly tests the core claim and is the single most important addition.
2. **Report t_min and t_max** and provide a sensitivity analysis varying these thresholds ±50% to show robustness.
3. **Provide the complete loss function** with all term weights in the main text.
4. **Report trial counts and confidence intervals** for all real-world experiments. Even 10–20 trials per condition with bootstrap CIs would substantially strengthen Table 2.
5. **Discuss the RND/domain-randomization confound** and, if possible, run a variant that excludes e_t from the RND input to verify the mechanism is not compromised.

## Score and Decision

The paper proposes a genuinely interesting method for adaptive risk sensitivity in humanoid locomotion. The combination of IQR and RND for online β modulation is well-motivated, and the results show promising robustness under challenging disturbances. However, the evaluation has a structural gap: the core claim requires isolating adaptivity from other confounds (distortion function choice, presence of any risk-awareness), and no fixed-β Wang baseline is included. Critical hyperparameters and loss function details are omitted, and the real-world evidence lacks statistical grounding. These issues are fixable with additional experiments and specification, but the paper in its current form does not provide sufficient evidence for its central claim.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>