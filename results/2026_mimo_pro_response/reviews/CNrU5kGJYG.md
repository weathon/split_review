## Summary
This paper proposes TrojanTO, the first post-training action-level backdoor attack against Trajectory Optimization (TO) models in offline RL (Decision Transformer, GDT, Decision ConvFormer). It employs trajectory filtering, batch poisoning, and alternating training to implant backdoors at only 0.3% poisoning rate. The paper also provides a systematic empirical investigation of key factors (target action selection, trigger design, reward manipulation) influencing backdoor efficacy against TO models.

## Strengths
- **Systematic factor analysis (Tables 1–3, Figure 1):** A well-designed ablation study isolates target action selection, trigger design, and reward manipulation. Table 1 reveals boundary target actions yield near-100% ASR while interior actions can drop to 0.110. Tables 2–3 show trigger dimensions and values are critical. Figure 1 demonstrates reward manipulation has negligible impact on ASR or BTP—a key insight distinguishing TO model backdoors from traditional RL backdoors.
- **High attack effectiveness at minimal poisoning (Table 4):** TrojanTO achieves CP=0.701 at 0.3% poisoning rate—a ~105% improvement over Baffle (0.342 CP at 10%) and ~27% over IMC (0.551 CP). ASR=0.719 and BTP=0.914 at this low rate demonstrate both effectiveness and stealth.
- **Novel post-training threat model (Section 3.3):** The three-stage taxonomy (pre-training, during-training, post-training) is practically motivated by escalating TO model scale. The insight that TO models minimize reconstruction loss rather than optimizing rewards makes reward-manipulation attacks architecturally incompatible, supported empirically by Figure 1.
- **Cross-architecture robustness (Table 4):** Consistent performance across DT, GDT, and DC, while baselines show critical failures in specific settings (IMC→0.013 CP on DT/Hopp; Baffle→0.000 CP on DT/Walk). TrojanTO wins 15/18 model-environment combinations.
- **Clean component ablation (Table 5):** Each component has a distinct, justified contribution—AT enhances effectiveness (removing it drops ASR from 0.719 to 0.507), while TF and BP enhance stealth (removing them drops BTP from 0.914 to 0.850/0.836).

## Weaknesses

### Fatal
None.

### Major
- **ASR threshold ε is not specified in the main text.** The ASR metric (Eq. 2, line 82-86) uses threshold ε to determine when a predicted action "matches" the target action, but ε's value is never stated in the main body—not in Section 3.4 (Experimental Setup) or anywhere else in the text. The paper writes "within a threshold ε" but never gives a number. For a security paper where ASR is the primary attack metric driving all experimental claims, this is a significant omission. While the BTP metric (normalized returns, Eq. 3) provides indirect validation that ε is not trivially permissive (if it were, benign actions would also match and BTP would degrade), the complete absence of ε makes ASR and CP values difficult to independently assess. This is trivially fixable and should be addressed.

- **Trigger dimension choice is underspecified and potentially cherry-picked.** Table 2 shows dimension choice swings ASR from ~0.90 (dimensions 1,2,3) to 0.00 (dimensions 1,10,14). The paper fixes (1,2,3) for all subsequent experiments across all environments and models without explaining why these dimensions consistently outperform or validating that the same triple is always optimal. The main text acknowledges this briefly ("Additional attempts at dimension selection methods are detailed in Appendix F") but provides no practical heuristic or justification in the main body. Since this single choice can mean 90% vs. 0% ASR, the generalizability of reported results is uncertain.

- **Performance inversions in specific settings are unacknowledged.** TrojanTO dominates on average but loses in several specific settings: DT/Kitchen (Baffle CP=0.766 vs. TrojanTO 0.614, line 236), DC/Ant (IMC CP=0.752 vs. TrojanTO 0.559, line 251), DC/Pen (IMC CP=0.655 vs. TrojanTO 0.477, line 253). The paper highlights where baselines fail but never discusses these inversions. The 15/18 win rate is still strong, but presenting only favorable comparisons overstates dominance. A balanced discussion would strengthen the paper.

### Minor
- **Defense analysis entirely in appendix (Section 6.5, line 324-326).** The main text claims "fine-tuning is the most effective defense" and that "other methods proved largely ineffective" but provides zero data—everything is delegated to Appendix B.1. For a security paper, at least headline defense results should appear in the main text.
- **Figure 1 only shows Walk environment (line 162).** Section 4.3's claim that reward manipulation is ineffective is central to the paper's motivation, yet it is supported with only one environment in the main text ("More results are provided in Appendix K.1").
- **Persistent backdoor counterintuitive results unexplained (Table 6, lines 300-303).** k=15 shows slightly higher CP than k=10 for Hopp (0.880 > 0.847) and Walk (0.973 > 0.928), which is surprising and unexplained.

## Nice-to-Haves
- Running Baffle at 0.3% poisoning rate as a controlled comparison would separate method quality from the poisoning-rate advantage.
- Testing additive noise (not just multiplicative) in the trigger perturbation analysis.
- Sensitivity analysis of ASR at multiple ε values.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Baseline comparison asymmetry (Baffle at 10% vs. TrojanTO at 0.3%):** The harsh critic flagged this as unfair, but per the filtering rules, asymmetry that favors the baseline should be removed. Here, Baffle uses MORE data (10% poisoning) and still performs worse—this asymmetry favors TrojanTO's efficiency claim. The paper explicitly frames this as an efficiency demonstration (line 270: "underscoring TrojanTO's superior stealth and attack efficiency"). A controlled ablation running Baffle at 0.3% is kept as a nice-to-have.
- **IMC adaptation methodology unexplained:** The paper describes IMC (Pang et al., 2020) as inspiration for alternating training (Section 5.3) and the adaptation IS the alternating training framework itself, which is fully described with the bi-level optimization (Eq. 7) and MI-FGSM trigger learning (Eq. 8).

## Novel Insights
The paper's most genuinely novel observation is that reward manipulation—the central attack vector for traditional RL backdoors—is negligible for TO models (Section 4.3, Figure 1). This is non-obvious because RTG is a standard conditioning signal in TO models; the finding that modifying it has minimal effect on backdoor efficacy redirects attention to trigger design as the critical factor. Combined with the systematic demonstration that target action selection and trigger dimension/value are the dominant factors, this provides a clear roadmap for future TO model backdoor research and defense.

## Suggestions
1. Specify ε prominently and ideally report ASR at multiple threshold values.
2. Add a table or figure showing defense results (especially fine-tuning) in the main text.
3. Discuss the settings where baselines outperform TrojanTO to present a balanced view.
4. Add at least one more environment's reward manipulation results to the main text.

## Calibration Report

**Round 1 — Bracketing (6 queries):**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Temporal Logic backdoor in offline RL | em0gAL8fbK | 4.00 | 1 | Similar topic (backdoor in offline RL), narrower scope, weaker evaluation. TrojanTO is stronger. |
| BATTLE adversarial DRL | rp5vfyp5Np | 4.25 | 1 | Related RL security, but adversarial (not backdoor) focus. TrojanTO is more novel. |
| SHINE backdoor defense | AKAlVyunxA | 5.75 | 1 | Defense paper, narrower scope. TrojanTO's contribution is broader. |
| Tree-based action attack | HZnnHDrBXD | 5.75 | 1 | Continuous RL attack with theory, but weaker experiments. TrojanTO has stronger empirical support. |
| Demystifying Poisoning Backdoor | BPHcEpGvF8 | 5.75 | 1 | Theoretical backdoor analysis, accepted. TrojanTO is comparable in contribution. |
| BALD backdoor on embodied LLM | S1Bv3068Xt | 6.25 | 2 | Very comparable—first-of-its-kind backdoor attack on decision-making systems, broad evaluation, similar weakness patterns. Accepted. |
| Multi-level certified defense | X2x2DuGIbx | 6.75 | 2 | Defense paper for offline RL with theoretical guarantees. Stronger theory, comparable practical contribution. |

**Bracket: 5.5–6.5.** TrojanTO is clearly above the 4.0–4.25 papers (broader evaluation, more systematic analysis, novel threat model). It is comparable to BALD (6.25, Accept) which also had limited defense analysis and specificity issues but was accepted as first-of-its-kind. TrojanTO's 3-architecture × 6-environment evaluation and ablation study are thorough, but the unspecified ε threshold and underspecified trigger dimension choice pull it slightly below BALD.

**Final score: 6.0** — solid contribution with addressable weaknesses, slightly below BALD due to the ε specification gap but above the rejected backdoor papers in the 4.0–5.75 range.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>