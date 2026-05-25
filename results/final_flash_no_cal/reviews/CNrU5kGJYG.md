Now I have a thorough understanding of the paper. Let me construct the consolidated review following all the instructions.

---

## Summary

TrojanTO proposes the first action-level backdoor attack against trajectory optimization (TO) models operating in high-dimensional continuous action spaces. Operating under a post-training (supply-chain) threat model, it uses alternating training to couple triggers with target actions, trajectory filtering to preserve benign performance, and batch poisoning for trigger consistency. The method achieves high attack success (ASR 0.719) and stealth (BTP 0.914) with only 0.3% poisoned trajectories across six D4RL environments and three TO architectures (DT, GDT, DC).

## Strengths

- **First action-level backdoor attack for TO models with a practical post-training paradigm.** TrojanTO is the first method designed explicitly for action-level backdooring of TO models at the post-training stage, decoupling the attack from expensive retraining. This is a genuinely novel contribution. **Evidence:** Section 1 defines the gap; Table 4 shows TrojanTO achieving ASR 0.719 with 0.3% poisoning vs. Baffle's 0.369 ASR at 10% poisoning.

- **Systematic factor analysis revealing that reward manipulation is ineffective for TO models.** Section 4 rigorously shows that target action selection and trigger design are the critical factors, while reward manipulation has negligible impact (Figure 1, Tables 1–3). This insight, which contradicts the mechanism of prior RL backdoors, directly motivates and validates TrojanTO's design choices.

- **Consistent and broad empirical validation.** Table 4 reports results across 6 environments × 3 architectures × 3 target actions, with TrojanTO achieving the highest average CP (0.701) versus Baffle (0.342) and IMC (0.551). The ablation study (Table 5) cleanly isolates the contribution of each component, and the persistent backdoor (Table 6) and trigger robustness (Table 7) analyses extend the evaluation beyond single-step attacks.

- **Comprehensive and well-motivated methodological design.** Each component (trajectory filtering, batch poisoning, alternating training) is motivated by a specific challenge (distribution shift, OOD trigger contexts, weak trigger–action coupling), and the ablation confirms each contributes meaningfully.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Evaluation metric does not directly measure the "catastrophic outcomes" invoked in the motivation.** The ASR (Eq. 2) measures whether the model outputs an action within an ε-ball of a target action — it does not measure whether that action degrades task performance, causes episode termination, or produces the irreversible harm mentioned in Section 3.2. Boundary actions like '1' that receive high ASR are assumed to be harmful, but the paper does not verify this. While ASR is the standard metric in the backdoor literature and the paper's core claim is about *action-level control*, the gap between the motivational language and the evaluation weakens the impact of the threat demonstration.

- **The fine-tuning vulnerability constrains the practical threat window but is under-discussed.** Section 6.5 reports that "fine-tuning is the most effective defense" in a single sentence, with details deferred to the appendix. Since standard fine-tuning can neutralize the backdoor, the attack's practical relevance is limited to scenarios where the model is deployed frozen. The threat model (supply-chain attack) is valid, but the abstract, introduction, and conclusion do not acknowledge this constraint, giving an inflated impression of the attack's robustness. An explicit bound (e.g., "poses a significant risk to deployed frozen models") would improve accuracy.

- **The headline Baffle comparison conflates objective mismatch with superiority.** Table 4 shows TrojanTO surpassing Baffle by ~105% in CP, but Baffle is a *policy-level* backdoor designed to degrade long-term returns, not to execute a specific target action. Adapting it to an action-level objective and then reporting the gap as a pure performance advantage is technically valid but asymmetric. The paper notes Baffle is policy-level (Section 2), but the 105% framing in Section 6.1 ("substantial improvement of approximately 105.0% compared to Baffle") would benefit from a clear caveat that the gap largely reflects the inapplicability of policy-level methods to action-level tasks, rather than only TrojanTO's methodological superiority.

- **The paper does not analyze cases where TrojanTO underperforms baselines.** TrojanTO achieves lower CP than IMC on DC-Ant (0.559 vs. 0.752) and DC-Pen (0.969 vs. 0.977). The paper does not discuss why this occurs — whether due to a conflict between trajectory filtering and the data distribution of those tasks, or some other factor. Including failure case analysis would deepen the evaluation.

### Trivial
None.

## Nice-to-Haves

- Augment ASR with an outcome-based metric (e.g., degradation in episode return or task completion rate under trigger activation) for a subset of environments. This would directly connect the attack metric to the "catastrophic outcome" narrative.
- Disaggregate the main results (Table 4) by target action type so readers can see whether performance is uniform across '1', 'fixed random', and 'arithmetic' targets or concentrated on a subset.
- Provide a more detailed characterization of the fine-tuning defense: how much data is needed, what is the computational cost, and does fine-tuning degrade benign performance? This would help practitioners assess the attack's real-world constraints.

## Novel Insights

None beyond the paper's own contributions. The finding that reward manipulation is ineffective for TO models and that the attack core lies in trigger–action coupling is the paper's key insight, and it cleanly redirects future attack/defense research in this space.

## Suggestions

1. Recalibrate the threat-model language: add a sentence bounding the attack's relevance to frozen-deployment scenarios in the abstract and conclusion.
2. Add a supplementary analysis showing that the target actions used in evaluation (especially boundary actions) actually produce measurable performance degradation or task failure.
3. Include a brief discussion of the DC-Ant and DC-Pen cases in Section 6.1 or as a separate paragraph.

## Score and Decision

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>