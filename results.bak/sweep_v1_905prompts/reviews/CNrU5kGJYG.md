Now I have sufficient calibration data. Let me synthesize the final review.

---

## Summary

This paper proposes TrojanTO, the first systematic study of action-level backdoor attacks against trajectory optimization (TO) models in offline RL — specifically Decision Transformer (DT), Graph Decision Transformer (GDT), and Decision ConvFormer (DC). The method operates as a post-training attack using three components (trajectory filtering, batch poisoning, and alternating training) to inject backdoors with a very low poisoning rate (0.3%). Evaluated across six D4RL environments, TrojanTO achieves an average CP of 0.701, substantially outperforming the baselines Baffle (0.342 CP) and IMC (0.551 CP).

## Strengths

- **First systematic study of action-level backdoors for TO models.** The paper correctly identifies and fills a gap: existing RL backdoor attacks rely on reward manipulation during training, which is ineffective against TO models that minimize reconstruction loss over sequences. The post-training threat model is well-motivated and practically relevant as TO models scale.

- **Comprehensive and well-designed evaluation.** Experiments span 6 environments (locomotion, navigation, manipulation) × 3 TO model architectures × 3 target action types, with results averaged over 3 seeds. Table 4 shows TrojanTO achieving the highest CP in 14 of 18 task-model combinations. The ablation study (Table 5) cleanly isolates the contribution of each component.

- **Low attack budget with high effectiveness.** TrojanTO uses only 0.3% poisoned trajectories while achieving ASR of 0.719 on average — a meaningful efficiency improvement over Baffle's 10% poisoning rate. The persistent backdoor results (Table 6) and trigger perturbation robustness (Table 7) further demonstrate the method's practical viability.

- **Honest investigation of design factors.** Section 4 provides a useful empirical study of how target action selection, trigger dimensions/values, and reward manipulation affect attack success. The finding that reward manipulation is ineffective against TO models is empirically grounded (Figure 1), and the paper transparently surfaces the extreme sensitivity to trigger dimension choice (Table 2).

## Weaknesses

### Major

- **ASR threshold ε is not specified in the main text.** Equation (2) defines ASR using a threshold ε on the absolute difference between predicted and target actions, but the numerical value of ε is never stated in the main paper. Since ASR depends directly on ε — a large ε (e.g., 0.5 in normalized action space) would label nearly any output a success, while a small ε (e.g., 0.01) makes high ASR genuinely meaningful — the headline numbers are uninterpretable without this parameter. Even if ε is specified in a stripped appendix, the main text must state it. This is a simple reporting oversight but a critical one.

- **The comparison with Baffle is uncontrolled for poisoning rate, weakening the efficiency claim.** TrojanTO uses 0.3% poisoned trajectories while Baffle uses 10% (a 33× difference). The paper presents this as evidence of "superior stealth and attack efficiency," but Table 4 does not include a controlled comparison where both methods operate at the same poisoning rate. Without such an ablation, the performance gap (CP 0.701 vs 0.342) cannot be cleanly attributed to the method rather than to the vastly different poisoning budgets. The paper should provide results for TrojanTO at 10% and for Baffle at 0.3% (or as close as Baffle allows). The paper mentions a poisoning-rate ablation in Appendix J (stripped) but for TrojanTO only, not a joint comparison.

### Minor

- **Standard deviations are missing from the main results table.** Table 4 reports only means without error bars. Given known high variance in DRL evaluations and the fact that CP is a harmonic mean, standard deviations (or other uncertainty quantification) should be reported for the main results. (Other tables, e.g., Tables 6 and 7, do include stds, making the omission in Table 4 more conspicuous.)

- **The defense discussion is too thin.** Section 6.5 states "fine-tuning is the most effective defense" and relegates all details to a stripped appendix. For a security paper, the main text should at least summarize the magnitude of defense effectiveness (e.g., how much fine-tuning degrades ASR and BTP). As written, this section is a placeholder.

- **Trigger dimension selection is not evaluated under unfavorable conditions.** Table 2 shows that dimension choice dramatically affects ASR (from 0.915 to 0.000), and (1,2,3) is selected because it performs best in a preliminary search. The paper does not evaluate TrojanTO's performance under randomly sampled or adversarial dimension choices, which limits understanding of the method's robustness. The paper acknowledges this sensitivity but does not characterize what an adversary would do when favorable dimensions are not available.

- **The threat model does not fully clarify where the adversary's trajectory dataset comes from.** Section 3.3 states the adversary "modifies the pretrained model parameters without access to the original training dataset," but Section 5.1 describes trajectory filtering over a dataset. The paper should explicitly state whether the adversary uses a separate, publicly available trajectory set for backdoor training.

### Trivial

- The legend in Figure 1 has a duplicated label ("w/ RM-4" appears twice).
- Table 5 row labels are slightly inconsistent (GTD vs GDT between tables).

## Nice-to-Haves

- Include a controlled poisoning-rate comparison between TrojanTO and Baffle (e.g., both at 0.3%, both at 10%).
- Evaluate TrojanTO under several randomly sampled (not just best-performing) trigger dimension sets to characterize brittleness.
- Report defense results in the main text in compressed form.

## Removed Points

- **"Reward manipulation claim overclaimed" (Harsh Critic #4):** The paper's Figure 1 shows near-identical curves across all reward manipulation strategies. The claim that reward manipulation has "negligible impact" is well-supported by the data. This criticism is speculative and removed.
- **"Trigger dimension overfitting/retrospective selection" framed as fatal flaw:** The paper transparently reports the sensitivity and discusses it; this is an honest limitation, not a fatal error. Demoted from the critic's framing to Minor.
- **Missing related works:** No external verification available; rule says not to mention.
- **Formatting/typo criticisms:** Parser artifacts, not author errors.
- **Speculative gaps about what the appendix might or might not contain:** Removed as non-verifiable from main text.

## Novel Insights

None beyond the paper's own contributions. The key insight — that reward manipulation is ineffective against TO models and that trigger-action coupling is the critical design dimension — is the paper's own finding, not a synthesis from the reviews.

## Suggestions

1. **Specify ε in the main text** (e.g., the first sentence of Section 3.4 or in the metrics definition) and briefly justify the choice.
2. **Add a controlled poisoning-rate comparison** between TrojanTO and Baffle — at minimum, show TrojanTO at 10% and Baffle at 0.3% (or as close as technically feasible).
3. **Include standard deviations in Table 4** to match the reporting standard used in Tables 6 and 7.
4. **Provide a summary of defense results in the main text** (e.g., "fine-tuning for 10 epochs reduces ASR from 0.99 to X while preserving BTP at Y").
5. **Clarify the origin of the trajectory dataset** used for backdoor training in the threat model description.

## Score and Decision

**Round-1 bracket:** The paper sits above 4.0 (the Temporal Logic AD anchor, a less comprehensive attack paper) and below 7.0 (anchors in that range are unrelated theoretical papers). Narrowest plausible range: 5.0–6.5.

**Round-2 narrowing:** Anchors clustered at 5.25–5.75. Compared to:
- *Tree-based Action-Manipulation Attack* (5.75, Reject): TrojanTO has a broader evaluation (6 envs × 3 models vs 2 envs) but lacks theoretical guarantees. Comparable quality; TrojanTO slightly stronger empirically.
- *A Change of Heart* (5.50, Reject): Different domain, similar methodology paper. TrojanTO has more comprehensive evaluation.
- *Robust DRL against Behavior Manipulation* (5.50, Reject): Attack/defense paper; TrojanTO's evaluation is broader.
- *Backdoor Contrastive Learning via Bi-level Trigger Optimization* (5.75, Accept): Similar bi-level optimization methodology, comparable breadth of evaluation and similar types of weaknesses (missing details, limited coverage on some dimensions).

TrojanTO is positioned comparably to these ~5.75 anchors. Its evaluation scope is a strength; the missing ε and uncontrolled Baffle comparison are the main weaknesses, both fixable. The paper is stronger than the 4.0–5.0 range but not quite at the 6.5+ level due to unresolved evidential gaps.

**Final score:** 6.0 — solid contribution with fixable weaknesses; recommended for acceptance with major revision.

**All anchors consulted:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| uw5U7FfTRf (BaDLoss) | 3.00 | 1 | Image backdoor detection; lower relevance and quality |
| RfYD6v829Y (TrojanRAG) | 3.40 | 1 | LLM backdoor; different domain |
| S5JCqTJyKj (Deferred Backdoor) | 3.00 | 1 | Image backdoor; lower relevance |
| 66e22qCU5i (Certified Copy) | 3.00 | 1 | Image backdoor; lower relevance |
| em0gAL8fbK (Temporal Logic AD) | 4.00 | 1 | Most directly comparable; TrojanTO is stronger empirically |
| X2x2DuGIbx (Multi-level Certified Defense) | 6.75 | 1 | Defense paper with theory; different contribution type |
| AKAlVyunxA (SHINE) | 5.75 | 1 | DRL backdoor defense; TrojanTO comparable quality |
| HZnnHDrBXD (Tree-based Action-Manip.) | 5.75 | 1,2 | TrojanTO has broader evaluation but lacks theory |
| 8BAkNCqpGW (Policy Gradient for POMDP) | 8.00 | 1 | Unrelated topic |
| 9pW2J49flQ (DeepLTL) | 8.00 | 1 | Unrelated topic |
| ZtOnddFVT3 (Self-Alignment) | 4.67 | 2 | Different topic |
| UhW2wA1pRV (Robust DRL) | 5.50 | 2 | Comparable quality; TrojanTO has broader evaluation |
| ZyPRwskBli (Backdoor in Seconds) | 4.75 | 2 | Model editing; less comprehensive |
| BxLK1M1f8T (Doctor) | 5.00 | 2 | Different topic (offline RL method) |
| ExUC9dQJhQ (Certified Robustness) | 6.00 | 2 | Different topic (certified defense) |
| BPHcEpGvF8 (Demystifying Backdoor) | 5.75 | 2 | Theory paper; different domain |
| oxjeePpgSP (Backdoor CL) | 5.75 | 2 | Similar methodology; comparable quality |
| Gf4KZIqLHD (A Change of Heart) | 5.50 | 3 | Comparable backdoor paper; TrojanTO evaluation broader |
| CiiLchbRe3 (Understanding Pretrained Transformer) | 5.25 | 3 | Different topic |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>