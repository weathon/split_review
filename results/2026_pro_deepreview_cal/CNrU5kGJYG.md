Now I have a thorough understanding of the paper and good calibration anchors. Let me compile the final review.

---

## Summary

This paper proposes TrojanTO, the first action-level backdoor attack against Trajectory Optimization (TO) models in offline RL. The attack operates post-training (modifying a pre-trained model rather than poisoning training data), uses only 0.3% of trajectories, and employs three components: trajectory filtering (to preserve benign performance), batch poisoning (for trigger consistency), and alternating training (to jointly optimize trigger and model). The authors first conduct empirical studies showing that target action choice and trigger design are crucial while reward manipulation is negligible for TO models. Experiments across six D4RL environments and three TO architectures (DT, GDT, DC) demonstrate an average CP of 0.701, substantially outperforming baselines Baffle and IMC.

## Strengths

- **Systematic empirical investigation of backdoor factors (Section 4):** The paper convincingly demonstrates that target action selection (Table 1), trigger dimension/value choice (Tables 2-3), and trigger optimization method (Table 3) significantly affect ASR, while reward manipulation has negligible impact (Figure 1). These findings genuinely counter assumptions inherited from traditional RL backdoors and justify the subsequent attack design.

- **Strong empirical results with very low attack budget:** TrojanTO achieves an average CP of 0.701 across 6 environments and 3 TO model architectures using only 0.3% poisoned trajectories, substantially outperforming Baffle (0.342 CP, 10% poisoning) and IMC (0.551 CP). The method scales across architectures (DT, GDT, DC) and diverse target action types.

- **Clean ablation study (Table 5):** The component ablation isolates each module's contribution clearly — removing AT drops ASR from 0.719 to 0.507, removing BP drops ASR to 0.528, and removing TF or BP degrades BTP, directly validating the design rationale.

- **Extension to multiple attack scenarios:** The persistent backdoor attack (Table 6) demonstrates the trigger-target coupling remains robust for up to k=15 sustained steps, and trigger perturbation experiments (Table 7) show gradual rather than brittle degradation under noise, strengthening the practical threat claim.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The ASR threshold ε is not stated in the main text.** Equation (2) defines ASR using a threshold ε (the per-dimension tolerance within which an output action counts as matching the target), but the numeric value of ε never appears in the main text. This is a reporting gap — the metric is well-defined and the value is presumably in Appendix I, but readers of the main text cannot assess what "success" means quantitatively. The authors should state ε explicitly in Section 3.4 and justify its choice relative to the action-space scale. (Note: this is a presentation issue, not a fatal flaw; the metric definition is clear and the results are comparative, so the relative rankings are interpretable even without the absolute ε.)

- **BTP normalization via return ratio can mask absolute degradation.** BTP is computed as the average of per-episode ratios G_k(π̂)/G_k(π). While this is common in the backdoor literature, ratios can obscure the absolute performance drop when clean returns vary across episodes or environments. The paper would benefit from also reporting absolute returns for both clean and backdoored policies alongside the normalized ratio.

- **Uneven ASR across task-model combinations is not discussed.** TrojanTO on DT-Hopper achieves only 0.362 ASR and 0.365 CP (Table 4) — the attack fails more often than it succeeds in this setting. The paper's claim of broad effectiveness would be strengthened by acknowledging and analyzing which task/target-action properties cause lower success rates, rather than relying solely on averages that conceal this variance.

- **Defense evaluation (Section 6.5) is a single paragraph.** The main text mentions that fine-tuning is the most effective defense among several tested methods, but defers all details, results, and analysis to Appendix B.1. For a security paper, the defense evaluation deserves more space in the main text to help readers assess the practical severity of the threat.

### Trivial

- The threat model (Section 3.3) could be more precise about what data the adversary uses for post-training — the paper says "a minimal set of poisoned trajectories (e.g., 0.3%)" but doesn't clarify whether these come from the original training distribution or a separate source accessible to the attacker.

## Nice-to-Haves

- Report sensitivity of ASR to varying ε thresholds to validate that conclusions are robust to the specific threshold choice.
- Include absolute return values alongside the normalized BTP ratio.
- A breakdown of ASR by target-action type (similar to Table 1) for the main TrojanTO results would provide richer insight into where the attack succeeds and struggles.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"ASR metric is undefined, rendering evaluation invalid"** — REMOVED as Fatal. The metric is explicitly defined in Equation (2) with ε as a parameter. The specific numeric value is a reporting detail, likely in the stripped Appendix I. The harsh critic's claim that "all ASR figures are vacuous" is an overstatement; the comparative results remain meaningful regardless.

2. **"BTP normalization via return ratio obscures true stealthiness / is unstable when returns are small or zero"** — DEMOTED to Minor. The ratio normalization is standard practice in the backdoor literature and D4RL environments have well-defined positive returns. The claim that "returns may be sparse or negative" in AntMaze/Kitchen rendering ratios "meaningless" is speculative — the paper's reported BTP values (0.45-1.0) are internally consistent with the claims.

3. **"Adaptation and fairness of baselines insufficiently described"** — REMOVED. Implementation details for Baffle and IMC are in Appendix I, which is stripped by the parser. Per hard rules, absent-appendix criticisms are removed.

4. **"Defense section is a placeholder; key results should be moved from appendix"** — REMOVED. The defense details are in Appendix B.1. Per hard rules, criticisms about content deferred to stripped appendices are removed.

5. **"Reward manipulation experiments relegated to appendix" / "experimental setup relegated to appendix"** — REMOVED. Per hard rules, appendix-deferred content criticisms are removed.

6. **"The persistent backdoor bound is obvious from the model design"** — REMOVED. This is a subjective criticism that the paper already acknowledges ("the maximum duration is fundamentally bounded by the TO model's finite context window," line 318-319).

7. **"Trigger perturbation study would benefit from a baseline of random untrained triggers"** — DEMOTED to Nice-to-Have. This is a reasonable suggestion but the experiment as conducted (showing gradual degradation under noise) is sufficient to support the robustness claim.

8. **"Post-training term merits more precise comparison with model-editing backdoors"** — REMOVED. This is a literature-nuance nitpick that doesn't affect the paper's contribution.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder largely confirm rather than extend the paper's claims — the key insight that reward manipulation is irrelevant for TO model backdoors (confirmed by Figure 1) is the paper's own finding and is well-supported.

## Suggestions

- State ε explicitly in Section 3.4, justify it in terms of the action-space scale (e.g., as a fraction of the action range), and ideally include a sensitivity analysis showing how CP varies with ε in an appendix figure.
- Report absolute clean and backdoored returns alongside the BTP ratio in Table 4 or a supplementary table.
- Add a brief discussion of the DT-Hopper low-ASR case in Section 6.1, explaining whether it stems from task difficulty, model architecture, or target-action interaction.
- Expand Section 6.5 with at least a summary table of defense results (even if detailed methods remain in the appendix) to give the reader a self-contained picture of the attack's resilience.

## Score and Decision

**Calibration anchors used:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| Temporal Logic Backdoor (em0gAL8fbK) | 4.00 | R1 (mid) | Weaker — high poisoning rate (15%), unrealistic threat model, limited evaluation |
| DIFF2 (Gf4KZIqLHD) | 5.50 | R1 (mid) | Weaker — stealthiness issues, unrealistic threat model requiring full training access |
| Efficient Backdoor (vRyp2dhEQp) | 5.75 | R2 (low) | Comparable scope but TrojanTO has broader evaluation |
| VLOOD (tZozeR3VV7) | 6.33 | R2 (mid) | Closest anchor — similar "first backdoor on X architecture" contribution; VLOOD has cleaner threat model, TrojanTO has more extensive ablation and attack scenarios |
| DAM (dqMqAaw7Sq) | 7.00 | R2 (high) | Stronger — more complete contribution with theoretical grounding and defense solution |

**Round 1 bracket:** 5.0–7.0 (clearly above the 4.0 anchor, clearly below the 8.0+ theoretically-grounded papers)

**Round 2 narrowing:** 6.0–6.5. TrojanTO is roughly comparable to VLOOD (6.33). Both are "first to demonstrate X backdoor on Y architecture" papers with solid empirical evaluation. TrojanTO has more extensive ablation and attack scenarios, but VLOOD has a cleaner threat model. The ε-reporting issue and thin defense section pull TrojanTO slightly below VLOOD.

**Final score: 6.0.** The paper makes a solid, well-executed contribution — the first action-level backdoor for TO models, backed by systematic empirical investigation and extensive evaluation. The methodology is sound and the ablation study is strong. However, the missing ε in the main text, the thin defense evaluation, and the uneven performance on some task-model pairs prevent it from reaching the 6.5+ range where papers typically demonstrate more complete contribution packages (theoretical analysis, more thorough defense treatment, or broader architectural coverage).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>