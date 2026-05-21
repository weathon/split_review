Now I have sufficient calibration data. Let me write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

The paper proposes TrojanTO, the first post-training action-level backdoor attack against Trajectory Optimization (TO) models in offline RL. TrojanTO uses trajectory filtering, batch poisoning, and alternating training to inject backdoors that force target actions upon trigger activation while maintaining benign performance, achieving high attack success rates with only 0.3% poisoned trajectories across DT, GDT, and DC models on six D4RL environments.

## Strengths

- **First systematic study of action-level backdoors for TO models.** The paper identifies a genuine gap: existing RL backdoors rely on reward manipulation or training-time access, neither of which is compatible with TO models' sequence modeling paradigm. The post-training threat model is well-motivated and practically relevant, especially as TO models grow in scale.

- **Well-designed method with validated components.** TrojanTO's three modules (trajectory filtering, batch poisoning, alternating training) are principled and each is validated by a clear ablation study (Table 5). Removing any component degrades ASR or BTP measurably — e.g., removing batch poisoning drops ASR from 0.719 to 0.528, and removing trajectory filtering drops BTP from 0.914 to 0.850. This gives confidence that the design choices are not arbitrary.

- **Comprehensive evaluation across diverse settings.** The paper evaluates on 3 TO model architectures (DT, GDT, DC) × 6 D4RL environments (locomotion, navigation, manipulation) with 3 target action types and 3 random seeds. TrojanTO achieves an average CP of 0.701. The persistent backdoor analysis (Table 6) and trigger perturbation robustness (Table 7) provide useful additional characterization of the attack's behavior.

- **Informative factor analysis.** Sections 4.1–4.3 systematically study how target action selection, trigger dimensions, and reward manipulation affect backdoor efficacy in TO models. The finding that reward manipulation is largely irrelevant (Figure 1) is a novel insight that correctly motivates the method's design away from traditional RL attack paradigms.

## Weaknesses

### Fatal
None.

### Major

- **ASR definition depends on an unspecified threshold ε.** Equation (2) defines ASR using a threshold ε for action-component proximity to the target action, but ε is never reported in the main text. Since ASR is the primary effectiveness metric and values reach 1.000 (e.g., HalfCheetah), the reader cannot assess whether this reflects genuinely precise action control or a loose threshold. The authors must report ε and justify its value relative to the action space scale. If ε was specified in the (stripped) appendix, it should be in the main text.

- **IMC baseline adaptation is underspecified.** IMC (Pang et al., 2020) was originally designed for image classification. The paper does not describe how IMC was adapted to the trajectory optimization setting — what triggers were used, how the alternating optimization was configured, or whether hyperparameters were tuned for fair comparison. Without this, the reader cannot determine whether IMC is a competitive baseline or an unfairly weak one. Since TrojanTO draws inspiration from IMC (Section 5.3), this gap is particularly significant.

### Minor

- **No variance reported in the main results table.** Table 4 reports only point estimates for ASR, BTP, and CP, despite stating that results are averaged over three random seeds. Tables 6 and 7 include ± standard deviations, making the omission in Table 4 conspicuous. Given known training noise in RL (Henderson et al., 2018), the stability of TrojanTO's average CP of 0.701 is unclear — is this 0.701±0.01 or 0.701±0.05?

- **Defense analysis is superficial in the main text.** Section 6.5 states that fine-tuning is the most effective defense and other methods (pruning, provable defense, spectral analysis, activation clustering) are "largely ineffective," but provides no quantitative results. If these results are in the appendix, a summary (e.g., "fine-tuning reduces ASR from X to Y while maintaining BTP of Z") belongs in the main text to make the defense section informative.

- **Factor analysis for reward manipulation uses a single environment.** Figure 1 only shows Walker2d; the claim that reward manipulation is "negligible" would be stronger with evidence across multiple environments. The paper references Appendix K.1 for more results, which is stripped.

### Trivial
None.

## Nice-to-Haves
- A controlled experiment matching Baffle's poisoning rate to TrojanTO's 0.3% (or vice versa) would cleanly separate the method's advantage from the budget advantage. The current comparison (0.3% vs 10%) is transparent and still informative — Baffle uses 33× more data yet performs worse — but matched-rate data would tighten the claim.
- Reporting computational cost (training epochs, wall-clock time) would strengthen the practical threat scenario narrative.
- A sensitivity analysis for the trigger-learning stopping criterion (half the training budget) would be informative.

## Removed Points
- **"Uncontrolled baseline comparison (Baffle at 10% vs 0.3%)"**: The paper is fully transparent about the different poisoning rates and the comparison is still meaningful — it shows TrojanTO achieves higher ASR and BTP at 1/33rd the data budget. This does not invalidate the claim of "superior stealth and attack efficiency." The paper does not claim matched-rate superiority over Baffle. Removed per the rule that asymmetry favoring the baseline is not a weakness.

- **"Trigger dimensionality of 3 not justified"**: The paper explicitly states it follows Baffle's convention (Section 4.2: "Following Baffle, we use a fixed trigger dimensionality of 3") and provides a comprehensive analysis across dimension choices in Table 2. Removed — this is addressed.

- **"Stopping condition after half training budget seems arbitrary"**: A sensitivity analysis would be nice but the paper's ablation study already validates the overall method's effectiveness. This is a hyperparameter choice, not a flaw. Removed as speculative.

- **"Trigger robustness limited to multiplicative noise"**: The paper explicitly characterizes this as a starting point and reports gradual degradation. Testing other noise distributions would strengthen the paper but is not a weakness. Removed.

- **"Missing related works"**: Instructions prohibit mentioning missing related works. Removed.

- **"No analysis of detection evasion / trigger visibility"**: These are beyond the stated scope — the paper studies attack effectiveness and stealth (defined as BTP), not evasion of detection methods. Removed per scope rule.

- **All formatting/style/typo criticisms**: Parser artifacts, not author errors. Removed.

- **Strength Finder's generic strengths**: "important problem," "timely topic" — removed as generic/superficial.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Report ε and justify its value relative to the action space scale in the main text.
2. Add a paragraph describing IMC's adaptation to the TO setting (triggers, hyperparameters, optimization loop).
3. Include standard deviations in Table 4 or add a note explaining their omission.
4. Add a brief quantitative summary of defense results (pre-/post-fine-tuning ASR and BTP) to Section 6.5.
5. (Optional) Add a figure comparing TrojanTO vs Baffle at the same 0.3% poisoning rate to eliminate any ambiguity in the comparison.

## Score and Decision

**Calibration details:**

Round 1 bracket: [5, 6.5].

Anchors retrieved (all rounds):
1. **Temporal Logic Multi-Vehicle Backdoor (em0gAL8fbK, 4.00, Reject)**: 15% poisoning rate, weaker threat model, less comprehensive evaluation. TrojanTO is clearly stronger.
2. **Tree-based Action-Manipulation Attack (HZnnHDrBXD, 5.75, Reject)**: Theoretical guarantees but only 2 low-dim environments, no baseline comparisons. TrojanTO has stronger empirical evaluation but lacks theory. Comparable quality overall.
3. **Multi-level Certified Defense (X2x2DuGIbx, 6.75, Accept)**: Strong theoretical defense with DP guarantees but addresses a different problem. TrojanTO is a weaker paper due to missing evidential details.
4. **Backdoor in Seconds / Model Editing (ZyPRwskBli, 4.75, Reject)**: Clever but narrow approach with limited applicability. TrojanTO is substantially stronger.
5. **BALD - Embodied Agents Backdoor (S1Bv3068Xt, 6.25, Accept)**: Comprehensive framework with multiple attack vectors, strong evaluation. TrojanTO has comparable empirical scope but more presentation gaps.
6. **SHINE - Backdoor Shielding (AKAlVyunxA, 5.75, Reject)**: Defense paper with theoretical claims. TrojanTO addresses a different (attack) problem; comparable quality.
7. **Robust DRL against Behavior Manipulation (UhW2wA1pRV, 5.50, Reject)**: Both attack and defense, theoretical analysis, but limited empirical scope. TrojanTO has broader empirical evaluation.

Round 2 narrowed the bracket to [5.5, 6.25]. The paper's contributions are genuine and the method is well-designed, but the missing ε threshold for ASR, underspecified IMC baseline, and missing variance in the main results table weaken the evidential presentation. These are fixable gaps. Comparing against the anchors, TrojanTO sits between the 5.75 papers (which have complementary strengths like theory but weaker empirical work) and the 6.25 BALD paper (which has fewer presentation gaps). The score reflects a paper with clear value that falls short of full confidence in its current presentation form.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>