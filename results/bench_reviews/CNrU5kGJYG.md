Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper proposes TrojanTO, the first post-training action-level backdoor attack against Trajectory Optimization (TO) models in offline RL (Decision Transformer, Graph Decision Transformer, Decision ConvFormer). The key insight is that existing RL backdoor attacks (which rely on reward manipulation) fail against TO models due to their sequence modeling nature and large scale. TrojanTO instead uses three components — trajectory filtering, batch poisoning, and alternating trigger-model optimization — to inject backdoors with high effectiveness and stealthiness. The evaluation covers 6 D4RL environments and 3 TO model architectures.

## Strengths

- **First systematic study of action-level backdoors for TO models.** The paper identifies a genuinely underexplored threat vector — post-training backdoor injection into trajectory optimization models — and demonstrates that existing reward-manipulation-based attack paradigms are fundamentally incompatible with TO models (Section 4.3, Figure 1). This finding is actionable for the security community.

- **Clear empirical identification of key factors for backdoor success.** Section 4 systematically analyzes three factors (target action selection, trigger design, reward manipulation) and shows that trigger design (dimensions + values) and target action choice are critical, while reward manipulation is negligible. This provides concrete guidance for both attackers and defenders.

- **Strong empirical results across diverse settings.** TrojanTO achieves an average CP of 0.701 vs 0.342 (Baffle) and 0.551 (IMC) across 3 TO architectures and 6 D4RL environments (Table 4), using only 10 trajectories (~0.3% poisoning rate). The ablation study (Table 5) cleanly isolates the contribution of each component.

- **Comprehensive evaluation scope.** The paper tests 3 model architectures (DT, GDT, DC), 6 environments spanning locomotion, navigation, and manipulation, and includes persistent backdoor attacks, trigger perturbations, and defense evaluations — substantially broader than prior RL backdoor work.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **ASR threshold ε is not reported.** Equation (2) defines ASR using an unspecified threshold ε for action proximity. The paper never states its value. While relative comparisons between methods hold (same ε), the absolute ASR numbers are uninterpretable without ε. For continuous action spaces (e.g., HalfCheetah with 6 action dimensions spanning different ranges), a loose threshold could inflate ASR. The authors should report ε and ideally perform sensitivity analysis. *(Note: this same issue was flagged in the "Angel or Demon" human review [avg 4.0] as a minor weakness, confirming this is a known but non-fatal gap.)*

- **BTP metric is problematic for environments with low clean returns.** BTP is the ratio of backdoored to clean policy return, clipped to [0,1]. For Ant (clean return: 0.58 for DT) and Kitchen (clean: 1.39 for DT) — see Table 14 — the clean policy itself performs poorly. A high BTP (e.g., 0.987 for DT-Ant in Table 23) simply means both policies are equally bad, not that the backdoor is stealthy. Using D4RL normalized scores (0–100) would be more informative. This inflates the apparent stealthiness on low-performing tasks but does not affect the core attack effectiveness claims (ASR).

- **No variance reported in main results tables.** Table 4 and Table 5 report only point estimates without standard deviations or confidence intervals. The paper states results are averaged over 3 seeds and cites Henderson et al. (2018) on RL variance, yet the main tables omit ± values. Some supplementary tables (e.g., Tables 6, 7, 20, 21) do include std, making the inconsistency in the main paper noticeable.

- **Section 4 analysis uses inconsistent attack methods across environments.** Table 1 uses Baffle for Half and Walk but TrojanTO for Hopper (see Appendix I.1). While the qualitative conclusion (boundary actions work best) holds across both methods, the inconsistency weakens the rigor of the "revisiting" experiment as a controlled analysis.

### Trivial
- "Poisoning rate" terminology (0.3%) is slightly imprecise — the adversary generates 10 trajectories via environment interaction, not by corrupting 0.3% of an existing dataset. The paper explains this clearly in Appendix C.1, but the abstract phrasing could be clarified.

## Nice-to-Haves
- **Sensitivity analysis on ASR threshold ε** would strengthen the metric substantially.
- **D4RL normalized scores for BTP** would fix the inflation on Ant/Kit and align with offline RL conventions.
- **Controlled baseline where Baffle operates as a post-training attack** with the same 10-trajectory budget would isolate the effect of attack method from threat model, though the current comparison (Baffle at 10% poisoning) is already standard.

## Removed Points
*These points are flagged to be removed, treat them with caution:*
- **Criticism that fine-tuning defeats the attack (Section 6.5):** The paper openly acknowledges fine-tuning as the most effective defense (line 863) and treats it as an expected finding. Many backdoor attacks in the literature are mitigated by fine-tuning; this does not invalidate the attack's novelty or effectiveness under the stated threat model (where the defender does not fine-tune).
- **Criticism that Section 6.5 defenses are too narrow (missing trigger inversion, attention head pruning):** The paper tests five defense methods, which is thorough for an attack paper. Demanding specific defenses beyond this scope is a nice-to-have, not a weakness.
- **Criticism about batch poisoning transition selection mechanism:** The paper explicitly states "single, random transition within each batch" and the mechanism is clearly described. The concern about training/evaluation mismatch misunderstands the design — batch poisoning is intentionally designed to avoid OOD contexts.
- **Criticism that Baffle comparison is uncontrolled (Appendix J.4):** The paper shows that even at 90% poisoning rate, trajectory poisoning fails on Half and Walk, so the issue is not merely the rate.
- **Criticism about "0.3%" terminology conflating data collection with poisoning:** The paper clearly explains that 10 trajectories are used, and 0.3% is a derived comparison to dataset size for context.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Specify ε and report ASR across a range of ε values** (e.g., 0.01, 0.05, 0.1) to make ASR fully interpretable.
2. **Replace raw-return-based BTP with D4RL normalized scores** (or add them alongside) for Ant and Kitchen environments, where clean returns are near-minimal.
3. **Add standard deviations to Table 4 and Table 5** in the main paper.
4. **Harmonize attack methods in Section 4** (Table 1) or explicitly justify the inconsistency.

## Score and Decision

### Calibration Anchors

| Path | Avg Human Score | Comparison |
|------|----------------|-----------|
| /home/wg25r/review_agent/human_reviews_2026/Z3SH1xlFs6.md | 6.50 | "Beware Untrusted Simulators" — similar RL backdoor topic, had theoretical proofs and real hardware validation but narrower empirical scope. This paper has broader evaluation but no proofs. Comparable quality. |
| /home/wg25r/review_agent/human_reviews_2026/YM23GVqQqj.md | 3.00 | "Stealthy Backdoor Attack in RL via Bi-level Optimization" — outdated literature, limited environments. This paper is substantially stronger. |
| /home/wg25r/review_agent/human_reviews_2026/6R42MRRs50.md | 4.00 | "Angel or Demon" — inconclusive analysis of interventions on backdoors. This paper has clearer contributions and better scope. |
| /home/wg25r/review_agent/human_reviews_2026/DotYL0mTxZ.md | 5.00 | "Stealthy World Model Manipulation" — first paper on world model poisoning but had white-box limitation. Similar novelty level; this paper has stronger empirical evaluation. |
| /home/wg25r/review_agent/human_reviews_2026/AC6lDj5dzl.md | 5.50 | "Robust DRL against Adversarial Behavior Manipulation" — accepted poster with solid experiments but limited novelty according to some reviewers. Comparable quality. |
| /home/wg25r/review_agent/human_reviews_2026/QQdn8nNqgi.md | 3.50 | "Clean-Action Backdoor Attacks on VLA Models" — withdrawn, weaker evaluation. This paper is notably stronger. |
| /home/wg25r/review_agent/human_reviews_2026/hkZpskx9mL.md | 3.50 | "Optimization-based Trajectory Deviation Attacks" — rejected, limited scope. This paper is stronger. |
| /home/wg25r/review_agent/human_reviews_2026/BxrhsH3uzB.md | 3.60 | "Backdoors in RLVR" — withdrawn, limited connection to offline RL. This paper is more substantial. |

This paper makes a clear, novel contribution to an underexplored security problem. The weaknesses (unspecified ε, BTP metric issue on low-performing tasks, missing variance in main tables) are real but fixable and do not threaten the core claims. The paper is comparable in quality to the 5.5–6.5 anchors — stronger than rejected papers in similar topic areas but with presentation and methodological gaps that prevent it from reaching the top tier.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>