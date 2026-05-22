Now I have sufficient calibration data. Let me produce the final consolidated review.

---

## Summary

TrojanTO proposes the first systematic study and practical attack framework for action-level backdoors against Trajectory Optimization (TO) models in offline RL. The paper identifies that existing RL backdoor methods (which rely on reward manipulation) are ineffective for TO models due to their sequence-modeling nature, and introduces a post-training attack combining trajectory filtering, batch poisoning, and alternating training. The attack achieves high ASR (0.719 average) with only 0.3% poisoned trajectories — a 30× reduction over the best baseline Baffle — across three TO architectures (DT, GDT, DC) and six D4RL environments.

## Strengths

- **First systematic study of action-level backdoors for TO models**: The paper identifies and experimentally validates that trigger-target coupling matters while reward manipulation is irrelevant for TO models (Section 4, Figure 1, Tables 1-3). This is a novel, domain-specific insight that directly motivates the method design.

- **Extremely low poisoning rate with high attack success**: TrojanTO achieves 0.719 average ASR at 0.3% poisoning, versus Baffle at 0.369 ASR at 10% poisoning (Table 4). This combination of efficacy and stealth is the paper's strongest empirical result.

- **Comprehensive and well-ablated evaluation**: The paper evaluates 3 TO models × 6 D4RL environments × 3 target actions (Table 4), plus component ablations clearly showing each module's contribution (Table 5), persistent backdoor analysis (Table 6), trigger perturbation robustness (Table 7), and defense analysis (Section 6.5).

- **Consistent outperformance across diverse settings**: TrojanTO achieves the highest average CP (0.701) compared to Baffle (0.342) and IMC (0.551) over all model-environment combinations (Table 4), with particular strength in locomotion tasks where it often reaches ASR > 0.99.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Ambiguous trajectory source relative to threat model**: The threat model states the adversary operates "without access to the original training dataset" (Section 3.3), yet the method relies on "given an initial set of N trajectories" (Section 5.1) and the adversary's capability mentions "a minimal set of poisoned trajectories" (Section 3.3). The paper never clarifies where this trajectory set comes from — whether it is separately collected (e.g., by rolling out the clean policy in the environment), drawn from a different public dataset, or contradicts the stated threat model. This gap prevents full evaluation of the threat model's internal consistency. It is the most significant clarity issue in an otherwise well-specified paper.

- **Missing standard deviations in main results table**: Table 4 reports only point estimates over three seeds without variance, while later tables (6, 7) include standard deviations. Given the well-known variance in RL results, the absence of stds or confidence intervals in the primary comparison table limits the reader's ability to assess the reliability of reported improvements over baselines.

- **Trigger dimension generalizability**: The paper fixes optimal trigger dimensions to (1,2,3) based on Table 2, which tests only two locomotion environments (HalfCheetah, Walker2d) with one target action type ('arithmetic'). It is unclear how an adversary would identify effective dimensions in a black-box setting or whether (1,2,3) generalizes to environments with qualitatively different state representations (e.g., AntMaze navigation, Kitchen manipulation). The paper mentions alternative selection methods in Appendix F (stripped), but a brief discussion in the main text would strengthen the practical relevance.

### Trivial
- Table 6 (persistent backdoor) reports only the composite CP score without showing ASR and BTP separately. Decomposing the harmonic mean would clarify whether CP degradation with increasing k is driven by ASR drops or BTP shifts.

## Nice-to-Haves

- The persistent backdoor analysis could be strengthened by reporting ASR and BTP separately.
- A brief discussion of how pseudo triggers (mentioned in Section 6.4) could affect stealthiness in practice would be valuable.
- A simple heuristic for trigger dimension selection (e.g., random sampling with multiple attempts) would improve the attack's practicality.

## Removed Points

These points were raised by reviewers but removed per filtering rules. They may be valid depending on appendix content not accessible to this review.

1. **Missing ASR threshold ε**: The harsh critic noted ε in Equation 2 is unspecified. Per the reproducibility statement, implementation details including metric thresholds would be in Appendix I, which the parser strips. Removed per the hard rule about appendix content.

2. **Missing implementation details (inner steps, λ)**: The harsh critic noted the alternating training description lacks specific parameter values. These details likely reside in Appendix I. Removed per the appendix rule.

3. **Baseline fairness (trigger dimensions)**: The harsh critic asked whether Baffle and IMC used the same trigger dimensions. The paper states "Following Baffle... we use a fixed trigger dimensionality of 3" (Section 4.2). Removed as already addressed.

## Novel Insights

None beyond the paper's own contributions. The paper's key insight — that reward manipulation is irrelevant for backdooring TO models while trigger-target coupling drives effectiveness — is well articulated and supported by the empirical studies.

## Suggestions

- Clarify the origin of the trajectories used for backdoor fine-tuning and explicitly state how this aligns with the "without access to the original training dataset" constraint in the threat model.
- Add standard deviations or confidence intervals to Table 4, or explain why they are omitted.
- Briefly discuss in Section 5 or 6 how an adversary would select trigger dimensions in practice without the full experimental setup.

## Score and Decision

**Calibration Anchors (all rounds):**

| ID | Avg Score | Round | Comparison |
|---|---|---|---|
| uw5U7FfTRf | 3.00 | R1 (weak) | BaDLoss backdoor detection — weaker; narrower scope |
| RfYD6v829Y | 3.40 | R1 (weak) | TrojanRAG — weaker; different domain (LLM), less systematic |
| S5JCqTJyKj | 3.00 | R1 (weak) | Deferred backdoor — weaker; different domain |
| 66e22qCU5i | 3.00 | R1 (weak) | Certified Copy backdoor — weaker; CV domain |
| em0gAL8fbK | 4.00 | R1 (mid) | Multi-vehicle backdoor in offline RL — weaker; higher poisoning rate (15%), narrower scope |
| X2x2DuGIbx | 6.75 | R1 (mid), R2 | Certified defense in offline RL — stronger theory, comparable experiments, accepted |
| AKAlVyunxA | 5.75 | R1 (mid), R2 | SHINE backdoor defense in DRL — narrower experiments, rejected |
| HZnnHDrBXD | 5.75 | R1 (mid), R2 | LCBT action-manipulation attack — only 2 environments, no comparisons, rejected |
| S1Bv3068Xt | 6.25 | R2 | BALD backdoor on embodied LLMs — comparable novelty claims, accepted |
| vRyp2dhEQp | 5.75 | R2 | Efficient backdoor in DNNs — CV domain, less relevant |
| LsTIW9VAF7 | 5.80 | R2 | Clean-image backdoor — CV domain, less relevant |
| tZozeR3VV7 | 6.33 | R2 | Backdooring VLMs with OOD data — CV+LLM domain, accepted |
| 29LC48aY3U | 6.00 | R2 | Backdoor for LLMs with knowledge distillation — LLM domain, rejected |

**Round 1 bracket**: Between "weak" anchors (~3.0–3.4) and "strong" anchors (~8.0), with middle anchors at 4.0–6.75. Narrowest plausible range: 5.5–7.0.

**Round 2 narrowing**: Compared to accepted papers at 6.25 (BALD) and 6.75 (certified defense), TrojanTO has stronger novelty in its domain than BALD (genuinely first to study TO backdoors), broader experiments than both, but lacks theoretical guarantees that the 6.75 paper had. The closest peers in the 5.75–6.25 range (SHINE, LCBT) have narrower scope and were rejected.

**Final score**: 6.5. The paper is clearly above the "weak accept" threshold, with well-supported novelty, comprehensive experiments, and only minor addressable weaknesses. It sits between the 6.25 accepted paper (BALD) and the 6.75 accepted paper (certified defense) — stronger than the former in experimental rigor, slightly below the latter in theoretical depth, but with practical significance (0.3% poisoning rate) that neither matches.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>