Now let me do calibration searches to score the paper.Now I have enough to write the final review. Let me synthesize everything.

---

## Summary

TrojanTO proposes the first action-level, post-training backdoor attack against Trajectory Optimization (TO) models in offline reinforcement learning. It identifies that reward manipulation is irrelevant for TO models (which optimize reconstruction loss, not reward), and that effective backdoors hinge on trigger design and target action selection. The method combines three components — trajectory filtering, batch poisoning, and alternating trigger/model co-optimization — and demonstrates consistent attack success across six D4RL environments and three TO architectures (DT, GDT, DC) with only 0.3% poisoning rate.

---

## Strengths

- **Novel post-training paradigm, first-of-its-kind.** The paper identifies a concrete gap: existing RL backdoor attacks bind to the training loop via reward manipulation (incompatible with TO models), and no post-training backdoor method has been proposed for TO models. The threat model in Section 3.3 is well-scoped and practically motivated. The paper explicitly categorizes pre-training (Baffle), during-training, and post-training (TrojanTO) stages.

- **Empirical insight on key factors backed by systematic evidence.** Tables 1–3 systematically demonstrate that target action type, trigger dimensions, and trigger values each cause large ASR shifts, while Figure 1 shows reward manipulation leaves ASR/BTP essentially unchanged across three TO architectures. This analysis grounds the design choices of TrojanTO and is the most scientifically valuable section of the paper.

- **Comprehensive evaluation breadth.** Table 4 covers 6 D4RL environments × 3 TO architectures × 3 random seeds × 3 target action types, an appropriate scope for an empirical security paper. TrojanTO consistently achieves higher CP than both baselines across almost all settings.

- **Ablation studies isolate each component's contribution.** Table 5 shows removing alternating training drops ASR from 0.719 to 0.507; removing batch poisoning drops ASR to 0.528; removing trajectory filtering degrades BTP. The contributions are not redundant and the component decomposition is coherent.

- **Extended attack scenarios.** Tables 6 and 7 test persistent backdoor activation (up to 15 steps, minimal CP degradation) and trigger perturbation robustness (ASR > 0.87 under 10% relative noise), adding practical realism to the evaluation.

---

## Weaknesses

### Fatal
None.

### Major

- **Baseline comparison conflates different threat models in headline claims.** Section 3.3 correctly categorizes pre-training (Baffle), during-training, and post-training (TrojanTO) as distinct stages. Yet Section 6.1 presents "105% improvement in CP over Baffle" and directly compares TrojanTO's 0.3% poisoning rate against Baffle's 10% as if these measure the same adversarial budget. Baffle's 10% refers to poisoning the *training dataset before model training begins*; TrojanTO's 0.3% is the fraction of trajectories used for post-training fine-tuning on an already-trained model. These represent different access assumptions and costs. The comparison is useful for context but is framed as a performance race between comparable systems, which it is not. IMC (Pang et al., 2020) is a closer post-training baseline, but it is a general input-model co-optimization technique originally not designed for RL; a brief justification for why it is the appropriate post-training baseline would strengthen this comparison.

- **Trigger dimension selection is oracle-guided and potentially optimistic.** Table 2 shows dramatic ASR sensitivity to trigger dimensions (ASR ranges from 0.000 to 0.915 on HalfCheetah depending on the chosen dimension triplet). The paper then fixes dimensions (1,2,3) for all subsequent experiments based on this sweep over the same environments. This is a form of oracle selection: the configuration used in the main results (Table 4) was chosen by scanning for the best-performing option in the same experimental setup. Whether the adversary realistically performs this sweep, and at what cost, is not discussed in the main text. This is acknowledged in Section 4.2 with a reference to Appendix F, but given that trigger dimensions are one of the two key design choices, this discussion belongs in the main paper. The key question — does TrojanTO generalize to non-oracle trigger dimension choices, or does its superior CP rely on this sweep — is not answered in the main text.

### Minor

- **Main evaluation averages over easy and hard target actions without stratification.** As shown in Table 1, boundary target actions ('1' and '-1') achieve near-100% ASR even under naive conditions. Table 4 reports results averaged over three target types including '1', so a portion of TrojanTO's reported 0.719 ASR comes from the trivially easy boundary case that essentially any method can exploit. The hard cases — 'fixed random' and 'arithmetic' targets — are deferred to Table 24 in the appendix. At minimum, the main paper should distinguish easy vs. hard target types in its summary claim; the paper's actual advance is largest for hard, interior target actions.

- **Zero standard deviations in Table 6 are unexplained.** Entries such as $0.922 \pm 0.000$ (k=0), $0.898 \pm 0.000$ (k=5), and $0.973 \pm 0.000$ (k=15) across three seeds imply perfectly identical outcomes. For a stochastic simulation environment this is unusual and warrants a brief clarifying note (e.g., whether these environments are deterministic, whether seeds affect only training, etc.).

- **Defense evaluation in Section 6.5 is too compressed.** The section reports only that "fine-tuning is the most effective defense" without stating how much fine-tuning data is required, what the resulting ASR drop is, or whether this constitutes a practical defense. The practical robustness of TrojanTO against fine-tuning — a natural step in model deployment — is a critical question that should have at least one key number in the main text.

### Trivial
- Figure 1's alt-text caption states "all conditions converge around 80-100% ASR," which is not quite consistent with the paper's stated conclusion ("reward manipulation is ineffective"). More precise framing: reward manipulation is *unnecessary* (it neither helps nor hurts). The current framing could mildly mislead readers.

---

## Nice-to-Haves

- A disaggregated main results table separating boundary ('1') from interior ('fixed random', 'arithmetic') target actions would sharpen the scientific contribution by showing where TrojanTO specifically advances the state of the art.
- A discussion or experiment showing attack performance across randomly sampled trigger dimensions (rather than oracle-selected (1,2,3)) would demonstrate that alternating training is robust to imperfect trigger initialization, which is the practical claim.
- At least one concrete real-world deployment scenario where the inference-time trigger injection assumption is realistic (e.g., a compromised sensor pipeline or adversarial patch on a robot's visual input) would strengthen the threat model motivation.
- A brief note in the main defense section quantifying how much fine-tuning data reduces ASR below a practical threshold.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Strength Finder: "105% improvement represents a genuine advance."** Retained as a general quantitative reference but demoted because the comparison conflates different threat models, so the 105% figure is not a clean measure of improvement over a matched competitor.

- **Harsh Critic: "Section 4.3 framing is misleading — if all conditions achieve high ASR, TrojanTO's contribution is undermined."** Removed as a standalone weakness. Figure 1 uses trigger dimension (8,9,10) — precisely the *suboptimal* dimension configuration identified in Table 2. In that setting, reward manipulation doesn't help OR hurt, confirming insensitivity. TrojanTO's contribution comes from the learnable trigger + alternating training, not from reward manipulation avoidance alone. The observation that reward manipulation is unnecessary (not merely "ineffective") is a minor framing issue, not a methodological flaw.

- **Harsh Critic: "Adversary's inference-time capability is unjustified."** Retained only as a Nice-to-Have. The assumption is standard in trigger-based backdoor literature and is not uniquely problematic here.

- **Strength Finder: "Broad applicability to DT, GDT, and DC underscores scalability."** Kept in strengths but with a more specific anchor (Table 4 CP values).

---

## Novel Insights

TrojanTO surfaces a practically important architectural insight: because TO models optimize a reconstruction loss over action-state-RTG sequences (rather than a reward-based Bellman objective), reward manipulation — the central attack vector in virtually all prior RL backdoor work — is entirely orthogonal to their vulnerability. The real attack surface lies in the trigger design and target action selection. This implies that the entire existing defense literature on reward-signal monitoring and manipulation detection is inapplicable to TO models as a defense paradigm, opening a distinct defense research agenda. The systematic factor analysis in Section 4 (Tables 1–3 + Figure 1) is the most transferable contribution of the paper, independent of whether TrojanTO's specific implementation is adopted.

---

## Suggestions

1. Restructure Table 4's summary text to acknowledge that Baffle operates under a different threat model; present TrojanTO's improvement over IMC (the post-training baseline) as the primary quantitative claim.
2. Add a secondary main table or paragraph stratifying CP across boundary vs. interior target action types to clarify where the method's advance is largest.
3. Move the trigger dimension discussion from Appendix F to the main paper with a brief experiment showing performance under random dimension selection.
4. Explain the zero standard deviations in Table 6 with one sentence.
5. Add at minimum one quantitative result in Section 6.5 (e.g., ASR after fine-tuning on X% clean data drops to Y) rather than deferring all numbers to the appendix.

---

## Calibration Anchors and Score Derivation

**All retrieved anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| em0gAL8fbK (temporal logic backdoor, offline RL) | 4.00 | R1 | Weaker than paper under review — narrower scope, weaker evaluation, less novel threat model framing |
| HZnnHDrBXD (tree-based action-manipulation, continuous RL) | 5.75 | R1 | Similar empirical focus on continuous action spaces; theoretically grounded but narrower than paper under review |
| X2x2DuGIbx (certified defense, offline RL poisoning) | 6.75 | R1/R2 | Accepted; stronger theoretical guarantees; paper under review has comparable empirical scope but no formal guarantees |
| UhW2wA1pRV (robust DRL against adversarial manipulation) | 5.50 | R1 | Rejected; similar empirical RL security scope; paper under review has more novel threat model and broader evaluation |
| ZyPRwskBli (post-training backdoor, large pre-trained models) | 4.75 | R2 | Rejected; most similar threat model (post-training) but in vision/classification; paper under review more thorough |
| vRyp2dhEQp (efficient backdoor in real-world scenarios) | 5.75 | R2 | Borderline accept; comparable empirical backdoor work; paper under review has clearer contribution framing |
| LsTIW9VAF7 (stealthy clean-image backdoor, few poisoned) | 5.80 | R2 | Rejected; similar low-budget backdoor attack framing; paper under review has more novel threat model |
| phAlw3JPms (data corruption in offline RL via sequence modeling) | 6.50 | R2 | Accepted; similar setting (sequence modeling in offline RL); stronger methodological contribution |

**Round 1 bracket:** 5–7.

**Round 2 narrowing:** The most topically similar accepted paper is phAlw3JPms (6.50) on sequence modeling in offline RL — that paper has a cleaner, more complete methodological story. X2x2DuGIbx (6.75) is also accepted but has provable guarantees the paper under review lacks. The rejected papers (ZyPRwskBli 4.75, LsTIW9VAF7 5.80, vRyp2dhEQp barely accepted at 5.75) bracket the lower end. The paper under review is stronger than ZyPRwskBli (more thorough, genuine first-of-its-kind contribution in RL), roughly comparable to vRyp2dhEQp and LsTIW9VAF7 in empirical rigor, but below phAlw3JPms in the clarity and strength of its quantitative claims due to the oracle trigger selection and cross-threat-model comparison issues. These methodological presentation issues prevent a score above 6.

**Final score: 5.5** — A genuine first contribution with thorough empirical coverage, but the main quantitative claims are weakened by oracle trigger selection and cross-threat-model comparisons that are not resolved in the main text. Borderline between accept and reject; revision addressing the trigger selection and evaluation stratification would substantially strengthen the paper.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>