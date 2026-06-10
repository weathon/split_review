Now I have enough data to calibrate. Let me compile the final review.

**Calibration summary:**

Round 1 bracketing anchors:
- Weak band (< 3.5): DABF (3.0), Certified Copy (3.0), TrojanRAG (3.4), LeBD (3.25) — all rejected, weaker backdoor papers
- Middle band (3.5–7.5): Temporal Logic Multi-Vehicle Backdoor (4.0, reject), SHINE (5.75, reject), Tree-based Action-Manipulation (5.75, reject), Robust DRL (5.50, reject)
- Strong band (> 7.5): GNNCert (8.0), Curiosity Red-teaming (8.0), Interpretable Planning (8.0) — all accepted, different domains

Round 2 narrowing anchors:
- Efficient Backdoor Attacks DNN (5.75, accept) — accepted despite similar score to rejected papers
- Multi-level Certified Defense Offline RL (6.75, accept) — defense paper in offline RL, strong theoretical guarantees
- Wicked Oddities clean-label backdoor (6.00, accept) — selective poisoning, limited datasets
- Confidence-driven Sampling backdoor (5.67, reject) — sampling strategy paper
- Tackling Data Corruption Offline RL (6.50, accept) — robustness of DT to corruption
- Certified Robustness Data Poisoning (6.00, reject) — provable guarantees

**Initial bracket (Round 1):** 5.5–7.0 — clearly above the rejected 4.0 paper and the rejected 5.75 papers, comparable to accepted papers in 5.75–6.75 range.

**Narrowed bracket (Round 2):** 5.5–6.5. TrojanTO is stronger than the rejected 5.67 Confidence-driven Sampling paper and the 5.75 SHINE paper (rejected). It's comparable to Wicked Oddities (6.0, accepted) — both are attack papers with novel contributions but evaluation limitations. It's somewhat below the Multi-level Certified Defense (6.75, accepted), which offers stronger theoretical contributions.

TrojanTO's key advantages: first post-training attack on TO models (genuine novelty), systematic factor analysis, comprehensive cross-architecture evaluation, 0.3% poisoning rate.

TrojanTO's key disadvantages: cross-paradigm comparison framing, oracle trigger dimension choice, missing ε in main text.

Final score: **6.0** — comparable to Wicked Oddities (6.0, accepted). The paper makes a genuine first-of-its-kind contribution with strong empirical analysis, but the major weaknesses (comparison framing, dimension selection) are real and prevent a higher score.

---

## Summary
This paper proposes TrojanTO, the first post-training action-level backdoor attack against Trajectory Optimization (TO) models in offline RL, using alternating training, trajectory filtering, and batch poisoning to implant backdoors with only 0.3% data poisoning. The paper also provides a systematic empirical study identifying key factors (target action choice, trigger design, reward manipulation) affecting backdoor effectiveness against TO models.

## Strengths
- **Systematic factor analysis before method proposal (Section 4, Tables 1–3, Figure 1):** The paper methodically investigates how target action choice, trigger design, and reward manipulation affect backdoor efficacy in TO models. Table 1 reveals non-obvious findings — interior target actions (e.g., type '0' on Walk: 0.11 ASR) are far harder to implant than boundary actions (type '1': 0.993). Figure 1 demonstrates reward manipulation has negligible effect, confirming TO models' inherent insensitivity to reward-based attacks. This principled analysis directly motivates design choices and distinguishes the work from prior RL backdoor research that centered on reward manipulation.

- **High attack effectiveness at an order-of-magnitude lower poisoning rate (Table 4):** TrojanTO achieves average CP of 0.701 at 0.3% poisoning, versus Baffle's 0.342 at 10% poisoning and IMC's 0.551. The gap is especially pronounced on challenging settings: Baffle achieves 0.000 CP on Walk-DT while TrojanTO reaches 0.957.

- **Cross-architecture generalizability (Table 4):** TrojanTO achieves average CPs of 0.649 (DT), 0.640 (GDT), and 0.814 (DC), outperforming both baselines on each architecture. This demonstrates effectiveness is not tied to a single model design. In contrast, IMC drops to 0.013 CP on DT-Hopp and Baffle collapses to 0.000 on DT-Walk.

- **Clean component ablation (Table 5):** Each module's contribution is validated through targeted ablation. Removing alternating training causes the largest ASR drop (0.719→0.507), while removing trajectory filtering and batch poisoning primarily degrades BTP (0.914→0.850 and 0.836), clearly separating attack-effectiveness and stealth-maintaining roles.

## Weaknesses

### Fatal
None.

### Major
- **Cross-threat-model comparison framing is misleading:** TrojanTO is a post-training attack with direct parameter access, while Baffle is a pre-training data-poisoning attack operating at a fundamentally different stage with different adversary capabilities. The paper acknowledges this in Section 3.3, but then presents Table 4 as a head-to-head comparison, claiming "a substantial improvement of approximately 105.0% compared to Baffle" (Section 6.1). Furthermore, Baffle is a policy-level backdoor (minimizing returns) evaluated on ASR, an action-level metric it was not designed to optimize. The paper should reframe the comparison to honestly demonstrate that (a) the post-training paradigm is more effective for TO models, and (b) within that paradigm, TrojanTO's specific design choices contribute meaningfully — the ablation in Table 5 already partially does this but is overshadowed by the cross-paradigm comparison.

- **Attack depends on favorable oracle trigger dimension choice:** Table 2 reveals ASR swings from 0.915 (dimensions 1,2,3) to 0.000 (dimensions 1,10,14) on HalfCheetah, and from 0.880 to 0.013 on Walker2d. The "All Dimensions" variant yields ASR=0.000. The paper fixes dimensions (1,2,3) for all subsequent experiments without providing a practical mechanism for dimension selection. While Appendix F reportedly explores selection methods, the main paper's results depend on this specific favorable choice, which limits the real-world threat model and somewhat undermines "broad applicability" claims.

### Minor
- **ASR threshold ε not specified in main text:** Equation 2 defines ASR with threshold ε but the main text never assigns a numerical value. This parameter directly determines ASR difficulty — a larger ε trivially inflates the metric. While likely in the appendix, presenting ASR results without specifying ε in the main text hinders interpretability.

- **No standard deviations in Table 4:** Despite averaging over 3 random seeds, Table 4 does not report standard deviations. Tables 6 and 7 do report ± values, making the omission inconsistent. Some settings show near-zero CP for baselines and it's unclear whether these are consistently zero or variable.

- **Notation inconsistency for λ:** In Equation 1, λ balances attack and stealth loss (higher λ = more stealth weight). In Equation 7, λ weights the attack loss (higher λ = more attack emphasis). In line 203, L = L_p + λL_c (higher λ = more clean emphasis). The mathematical role of λ flips between formulations, creating confusion about what the method optimizes.

- **Defense evaluation deferred entirely to appendix (Section 6.5):** The paper claims fine-tuning is the most effective defense while others are largely ineffective, but presents zero quantitative defense results in the main text. For an attack paper, the defense landscape is critical for assessing real-world impact. A summary table should be in the main text.

## Nice-to-Haves
- Report per-target-action results prominently rather than averaging over three target types, since Section 4 shows target action choice dramatically affects ASR.
- Provide a concrete supply-chain threat scenario for when a user would load a compromised TO model and where the attacker injects the trigger.
- Show ASR sensitivity to ε (even a single figure) to demonstrate results are not artifacts of a permissive threshold.
- Adapt a post-training backdoor method from supervised learning as an additional baseline for a fairer within-paradigm comparison.

## Removed Points
These points are flagged to be removed, treat them with caution.
- None removed; all included weaknesses were verified against the paper.

## Novel Insights
The paper's most genuinely novel contribution is the systematic demonstration that reward manipulation — the dominant attack vector for traditional RL backdoors — is negligible against TO models (Figure 1), and that the real attack surface lies in trigger-target action coupling rather than reward signal manipulation. This reframes the backdoor threat model for the growing class of TO/sequence-model-based RL agents and is likely to influence future security research in this area. The three-tier categorization (pre-training, during-training, post-training) of RL backdoor intervention stages is also a useful conceptual contribution.

## Suggestions
- Reframe Table 4 comparisons to emphasize the post-training paradigm's advantages rather than claiming head-to-head superiority over Baffle.
- Add standard deviations to Table 4 for consistency with Tables 6–7.
- Include the ε threshold value and ideally a sensitivity analysis in the main text.
- Present a defense results summary table in the main text (Section 6.5).
- Discuss dimension selection methods from Appendix F in the main paper to address the oracle choice concern.

## Anchor Papers Retrieved

| Round | Path | Avg Score | Comparison |
|-------|------|-----------|------------|
| 1 | S5JCqTJyKj (DABF) | 3.0 | Weaker — deferred backdoor, limited evaluation |
| 1 | 66e22qCU5i (Certified Copy) | 3.0 | Weaker — narrow focus, limited novelty |
| 1 | RfYD6v829Y (TrojanRAG) | 3.4 | Weaker — backdoor in LLMs, limited evaluation |
| 1 | 7vKWg2Vdrs (LeBD) | 3.25 | Weaker — defense in YOLO, limited scope |
| 1 | em0gAL8fbK (Temporal Logic Backdoor) | 4.0 | Weaker — 15% poisoning rate, limited environments |
| 1 | AKAlVyunxA (SHINE) | 5.75 | Weaker — defense paper with theoretical gaps |
| 1 | HZnnHDrBXD (Tree-based Attack) | 5.75 | Weaker — narrower evaluation |
| 1 | UhW2wA1pRV (Robust DRL) | 5.50 | Weaker — limited novelty |
| 1 | IGzaH538fz (GNNCert) | 8.0 | Stronger — different domain, certified defense |
| 1 | 4KqkizXgXU (Curiosity Red-teaming) | 8.0 | Stronger — different domain, LLM security |
| 2 | vRyp2dhEQp (Efficient Backdoor DNN) | 5.75 | Comparable but TrojanTO more novel (first in TO) |
| 2 | pE6gWrASQm (Adversarial Training) | 6.50 | Stronger — different domain |
| 2 | ysue5S6cVS (Confidence-driven Sampling) | 5.67 | Similar scope, TrojanTO more comprehensive |
| 2 | LsTIW9VAF7 (GCB clean-image) | 5.80 | Comparable scope, TrojanTO broader evaluation |
| 2 | X2x2DuGIbx (Certified Defense Offline RL) | 6.75 | Comparable contribution level, different focus |
| 2 | phAlw3JPms (Data Corruption Offline RL) | 6.50 | Stronger contribution in adjacent domain |
| 2 | 1Z3C49JQVf (Wicked Oddities) | 6.00 | Most comparable — attack paper with novel setting, accepted |
| 2 | ExUC9dQJhQ (Certified Robustness Poisoning) | 6.00 | Comparable but rejected — narrower contribution |

**Bracket:** Round 1 placed the paper between 5.5 and 7.0. Round 2 narrowed to 5.5–6.5. TrojanTO is clearly above the rejected 5.67 and 5.75 anchors and comparable to the accepted Wicked Oddities (6.0). It is somewhat below the Multi-level Certified Defense (6.75) which offers stronger theoretical contributions. Final score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>