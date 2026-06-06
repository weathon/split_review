Now I have the full paper. Let me write the consolidated final review based on the paper content and the reviewer inputs.

---

## Summary

TrojanTO is the first post-training, action-level backdoor attack against Trajectory Optimization (TO) models in offline RL. The paper identifies that, unlike traditional RL backdoors that exploit reward manipulation, effective backdoors against TO models hinge on trigger design and target action selection. The proposed method combines three components — trajectory filtering, batch poisoning, and alternating trigger/model optimization — to implant backdoors efficiently using only 0.3% of trajectories in a post-training setting. Evaluation spans three TO architectures (DT, GDT, DC) across six D4RL environments.

---

## Strengths

1. **Empirical insight that reward manipulation is irrelevant for TO model backdoors.** Section 4.3 and Figure 1 empirically confirm that varying reward manipulation strategies (RM-4, RM-8, RM-16) produce essentially identical ASR and BTP curves across DT, DC, and GDT on Walker2d, motivating the paper's design focus on trigger and target action. This is a genuinely novel empirical finding that cleanly justifies departing from the standard RL backdoor paradigm.

2. **Meaningful breadth of evaluation.** Table 4 covers three TO architectures (DT, GDT, DC) and six D4RL environments (Hopper, HalfCheetah, Walker2d, AntMaze, Kitchen, Pen), with results averaged over three seeds and three target action types, giving a credible breadth of coverage for an adversarial method paper.

3. **Ablation studies isolate each module's contribution.** Table 5 provides clean, quantitative evidence: removing alternating training (AT) drops average ASR from 0.719 to 0.507; removing batch poisoning (BP) drops it to 0.528; removing trajectory filtering (TF) reduces BTP from 0.914 to 0.850. The synergy among modules is well-evidenced.

4. **Comprehensive factor analysis motivates the design.** Tables 1–3 systematically study target action type, trigger dimension, and trigger value in isolation. The finding that boundary actions ('1', '-1') are trivially easy while interior actions are hard (e.g., 'fixed random' achieves only 0.243 ASR on Walker2d without optimization) provides principled grounding for the paper's method and sets up a more rigorous evaluation than prior work that only tested boundary actions.

5. **Extended attack scenarios increase practical relevance.** Table 6 demonstrates persistent backdoor operation for up to 15 steps with minimal CP degradation. Table 7 shows robustness to up to 10% multiplicative trigger noise (ASR ≥ 0.870 on Hopper and 0.777 on Walker2d), an important stress test for real-world applicability.

---

## Weaknesses

### Fatal
None.

### Major

- **Oracle trigger dimension selection creates selection bias in the main results.** Table 2 sweeps six dimension sets over HalfCheetah and Walker2d and finds dimensions (1,2,3) are dramatically superior (0.915/0.880 ASR vs. 0.000/0.013 for competing sets). The paper then fixes (1,2,3) for all subsequent experiments, including Table 4. This means the headline results are conditioned on a configuration identified by sweeping the same environments used for evaluation. In practice, an adversary deploying TrojanTO without this oracle search could find catastrophically worse results — Table 2 itself shows this gap can be 0.000 vs. 0.915. The paper notes "Additional attempts at dimension selection methods are detailed in Appendix F," but this is a core methodological concern: the main Table 4 results should either (a) show robustness over randomly sampled trigger dimensions, (b) show performance using the dimension selection procedure from Appendix F, or (c) make explicit that this selection is part of the adversarial capability and characterize its cost. As written, the main claimed numbers may represent a best-case scenario rather than the method's expected performance.

### Minor

- **Comparison across different threat models is legitimate but the framing of the 105% improvement claim is misleading without disambiguation.** Section 6.1 reports: "a substantial improvement of approximately 105.0% compared to Baffle." The paper correctly categorizes Baffle as a Pre-training attack and TrojanTO as Post-training in Section 3.3, but the headline in Section 6.1 presents the comparison without repeating this distinction. A reader could reasonably interpret this as same-setting superiority. The actual argument — that TrojanTO achieves higher CP *with lower adversarial access* (no training loop, only post-training model modification) — is the stronger and more interesting claim, and should be stated front-and-center in Section 6.1. The IMC comparison is the more controlled same-stage comparison and deserves clearer prominence.

- **The evaluation of reward manipulation irrelevance (Section 4.3) is conducted with target type '1' only.** Figure 1 uses target type '1' (boundary action), which Table 1 shows achieves near-100% ASR trivially even without optimization. This means the conclusion "reward manipulation is ineffective" is demonstrated in the easiest possible condition. While the section's conclusion is likely still valid for harder target types (since the TO model's training objective doesn't interact with rewards), this is not shown. A brief note or a single result with 'arithmetic' target type would substantially strengthen this empirical claim.

- **Table 6 (persistent backdoor) shows zero standard deviation across three seeds for most conditions, which warrants a clarifying note.** Conditions k=0, k=5 for Hopper and HalfCheetah report $\pm 0.000$. For boundary target type '1', very high consistency is plausible, but zero variance across three distinct random seeds across 100 episodes each is notable. A brief explanation (e.g., saturated ASR and BTP under this easy target type) would preempt confusion.

### Trivial

- **Section 6.5 (defense)** summarizes the defense evaluation in a few sentences with no quantitative numbers in the main text. The claim that "fine-tuning is the most effective defense" is unsupported without at least one key number (ASR drop or amount of fine-tuning data required). While the full results are in the appendix, the main paper would benefit from at least one quantitative anchor.

---

## Nice-to-Haves

- **Disaggregating Table 4 by target action type in the main paper** (in addition to the appendix Table 24) would let readers directly assess where TrojanTO's improvement is largest — specifically on the hard interior targets that motivated the work — versus the trivially easy boundary case. This would not change the conclusions but would substantially strengthen the evidentiary case for the method's core contribution.

- **The threat model assumption** that the adversary can "manipulate the agent's input observation to insert the trigger" at inference time (Section 3.3) is stated but not illustrated with even one realistic scenario. A brief example (e.g., sensor spoofing in a robotic deployment, or a compromised observation pipeline in a software stack) would ground the practical relevance.

- **A brief analysis of trigger dimension selection via the Appendix F method**, showing the gap (if any) between oracle (1,2,3) selection and automated selection performance, would directly address the major concern and could be added compactly in the main paper as a single-row addition to an existing table.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh critic: "Baffle comparison is fundamentally unfair / conflates threat models."** Partially removed/demoted. The paper is transparent about the different threat model stages in Section 3.3. The comparison is legitimate as a demonstration that TrojanTO achieves higher CP with strictly less adversarial access. The framing issue is real but minor; retained as a Minor concern about phrasing in Section 6.1, not as a fatal flaw.

- **Harsh critic: "BTP of 0.914 / summary numbers include easy boundary targets that inflate aggregate."** This concern applies equally to all three methods (Baffle, IMC, TrojanTO) since all are evaluated over the same three target types. It does not selectively inflate TrojanTO's advantage, so it is not a fairness issue. The averaging structure is standard; removed.

- **Harsh critic: "Reward manipulation conclusion is 'slightly misleading.'"** The specific claim (that the figure shows reward manipulation is *unnecessary*, not *ineffective*) is genuinely subtle but the distinction doesn't change the takeaway or the method design. Retained only as a minor note that the analysis uses the easy target type.

- **Strength Finder: "105% improvement over Baffle is the single most compelling piece of evidence."** Partially removed as a standalone strength — this comparison is across threat models. The strength is real but better characterized as TrojanTO outperforming Baffle *despite using less adversarial access*, which is a meaningful claim.

---

## Novel Insights

The paper's most genuinely novel empirical observation — that reward manipulation is irrelevant for backdooring TO models because their behavior-cloning objective is decoupled from reward signals — cleanly separates the TO model threat landscape from traditional RL backdoor theory. This insight is well-supported by Figure 1's consistency across three architectures. Additionally, the systematic demonstration that trigger *dimension selection* (Table 2) can cause ASR to collapse from near-perfect to zero is a practically important finding for the broader backdoor literature: in high-dimensional continuous observation spaces, trigger geometry matters as much as trigger magnitude, a result with implications beyond TO models.

---

## Suggestions

1. **Address trigger selection bias** by running Table 4's main results using the Appendix F automated dimension selection method, then comparing against the oracle (1,2,3) choice. If the gap is small, that substantially strengthens confidence in the results; if large, the paper should report both.

2. **Add one quantitative number** to Section 6.5's defense discussion — e.g., "after fine-tuning on X% clean data, ASR drops from 0.719 to Y" — so the main paper is self-contained on this dimension.

3. **Strengthen Section 4.3** by replicating the reward manipulation experiment for a non-boundary target type (e.g., 'arithmetic') to confirm the finding holds in the general case, not only for the trivially easy boundary target.

4. **Revise Section 6.1** to lead with the comparison against IMC (the matched post-training baseline), and explicitly frame the Baffle comparison as "TrojanTO achieves higher CP with strictly weaker adversarial access (no training loop required)."

---

## Score and Decision

**Originality:** Strong. Post-training action-level backdoor for TO models is a genuinely novel attack paradigm; the reward-manipulation-irrelevance finding is new.

**Importance:** High. Security of large pre-trained TO models is a timely and growing concern; supply-chain attacks are practically motivated.

**Claims supported:** Mostly, but with one methodological gap — the oracle trigger dimension selection is not sufficiently disclosed or resolved in the main paper, which means the main Table 4 numbers may overstate expected performance.

**Soundness:** Good. The three-component design is coherent and ablated. The alternating training approach is clearly derived. The evaluation is sufficiently broad.

**Clarity:** Good overall. Section 3.3 is clear about threat model stages. Section 6.1 framing could be improved.

**Community value:** High. First systematic treatment of post-training backdoors for TO/offline RL, with code in supplementary.

The paper makes a genuine and timely contribution; the oracle trigger selection is the primary methodological concern and is addressable in a revision. This does not invalidate the core claim but does qualify the headline numbers.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>