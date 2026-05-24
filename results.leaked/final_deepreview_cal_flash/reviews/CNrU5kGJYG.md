Now I have a thorough understanding of the paper. Let me construct the consolidated review.

## Summary

This paper presents TrojanTO, a post-training action-level backdoor attack against Trajectory Optimization (TO) models in offline RL. The method uses alternating training (bi-level optimization of trigger and model parameters), trajectory filtering, and batch poisoning to implant a trigger-target action mapping with a very low poisoning rate (0.3%). The paper provides a systematic factor analysis showing that target action and trigger design are critical while reward manipulation is ineffective for TO models, and demonstrates effectiveness across 6 D4RL tasks and 3 TO architectures (DT, GDT, DC).

## Strengths

- **First systematic study of action-level backdoors for TO models in offline RL.** This is a genuinely underexplored threat vector. The paper identifies why existing RL backdoor methods fail against TO models (reward manipulation is ineffective; TO models use sequence-level reconstruction loss rather than Bellman updates) and leverages this insight in the attack design.

- **Low poisoning rate with strong attack effectiveness.** TrojanTO achieves an average CP of 0.701 and ASR of 0.719 across 6 D4RL tasks using only 0.3% poisoned trajectories, compared to Baffle's 10% rate. This represents a meaningful improvement in stealth and efficiency.

- **Informative factor analysis (Section 4).** The systematic investigation of target action types, trigger dimensions/values, and reward manipulation provides actionable knowledge for the community. The finding that reward manipulation is unnecessary for TO model backdoors (Figure 1) is a non-obvious insight given how central reward manipulation is to traditional RL backdoor literature.

- **Comprehensive evaluation design.** Experiments span 6 D4RL tasks (locomotion, navigation, manipulation), 3 TO architectures (DT, GDT, DC), 3 target action types, and include ablation studies (Table 5), persistent backdoor analysis (Table 6), trigger perturbation robustness (Table 7), and defense evaluation. Code is provided.

- **Clean ablation study.** Table 5 clearly shows the contribution of each component: removing alternating training drops ASR from 0.719 to 0.507; removing batch poisoning drops BTP from 0.914 to 0.836. This convincingly validates the design choices.

## Weaknesses

### Major

- **Threat model inconsistency between claim and experimental setup.** The paper states (Section 3.3): *"the adversary aims to implant a backdoor into the pretrained TO model without access to the original training dataset."* However, the method's trajectory filtering and batch poisoning operate on trajectories explicitly derived from the same D4RL datasets that were used to train the clean models. The paper never specifies what data the adversary actually possesses, whether it is disjoint from the training data, or whether the attack depends on the fine-tuning distribution matching the training distribution. This is not a fatal flaw — the core "post-training" claim (modifying a pretrained model outside the training loop) stands — but it is a significant overstatement in the threat model framing. The experimental evaluation does not demonstrate the attack under a realistic data-access constraint where the adversary's fine-tuning data is clearly separated from the original training distribution.

- **Unfair and inadequately described baseline comparisons.** Two issues compound each other: (i) **Baffle** is a pre-training, *policy-level* backdoor, yet it is evaluated on the *action-level* ASR metric (Eq. 2). No description is given of how Baffle was adapted to output a specific target action. Unsurprisingly, it performs poorly (average CP 0.342). (ii) **IMC** is originally an image-classification backdoor; the paper provides no detail on how it was adapted to the RL/TO setting (trigger injection, loss functions, sequence handling). Without this, the reader cannot assess whether IMC was implemented fairly. Together, these issues make it impossible to attribute TrojanTO's performance advantage to its specific design choices rather than to an inadequate comparison. Additionally, a natural strawman — fine-tuning with a fixed (non-learned) trigger and backdoor loss, without alternating optimization — is absent; the ablation removes components but does not isolate this simple baseline.

### Minor

- **ASR threshold ε not specified.** Equation (2) defines ASR using a threshold ε, but no value is reported in the main text. While this likely appears in the appendix, the main text should state the value, and ideally show sensitivity of ASR to this threshold.

- **Trajectory filtering heuristic not empirically validated.** The paper assumes longer trajectories are more representative of successful behavior (Section 5.1) but provides no empirical justification. An ablation showing the effect of different length thresholds or comparing against alternative filtering strategies would strengthen the claim.

- **Fine-tuning as an effective defense is acknowledged but not discussed as a limitation.** Section 6.5 and Appendix B.1 report that fine-tuning removes the backdoor, which substantially reduces the real-world threat if end users fine-tune the model. This point should be discussed in the main text as a limitation of the attack, not relegated to the appendix.

### Trivial

- None beyond what is covered in Minor.

## Nice-to-Haves

- A discussion of computational cost (training epochs, wall time) would help assess the practicality of the attack.
- The target action study (Section 4.1) is limited to 6 types; a sweep over random actions from the full action space would strengthen the generality claim.
- The trigger dimension analysis (Table 2) is reported for only two tasks; the optimal trigger dimensions may be environment-dependent.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic's "structural flaw — cannot be fixed by experiments":** While the threat model inconsistency is real, it IS fixable: the authors can clarify what data the adversary has, and the experimental evaluation can be strengthened with a disjoint-data experiment. Calling it "structural" and "cannot be fixed" overstates the severity. **Moved from Fatal to Major.**

- **Criticism that Baffle's average CP is 0.342 "does not constitute a meaningful comparison":** The comparison is weak but not meaningless — it shows that an existing RL backdoor method adapted to action-level evaluation performs poorly, which is informative. The fault is in the lack of adaptation description, not the comparison itself. **Kept as Major but re-framed.**

- **Strength Finder's claim about "Post-training attack paradigm decoupled from training":** This is an overstatement. The method fine-tunes the model, so it is not "decoupled from training" but rather decoupled from the *original* training loop. The paper itself acknowledges this (it calls it post-training). This is valid as stated but slightly imprecise. **Kept but noted.**

- **Several minor criticisms from harsh critic about appendix placement, not discussing computational cost, limited target action diversity — these are valid but Minor/Nice-to-have.** **Moved to appropriate tiers.**

- **Criticism that persistent backdoor is "just a consequence of the trigger staying in context for k steps":** This is accurate but the paper explicitly says this (Section 6.3): "the maximum duration is fundamentally bounded by the TO model's finite context window." The paper does not oversell this as a new attack type. **Removed.**

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder both converge on the same core assessment: the paper's main novel contribution is identifying that action-level backdoors for TO models require attention to target action and trigger design, not reward manipulation, and demonstrating a working method with very low poisoning rates. The factor analysis in Section 4 is the most insightful part and genuinely advances understanding of TO model security.

## Suggestions

1. **Resolve the threat model contradiction.** Explicitly state what data the adversary is assumed to have. If the adversary can obtain a small number of trajectories from the same environment (e.g., from a public benchmark or by rolling out a low-quality policy), say so. Add an experiment where the fine-tuning data is clearly disjoint from the training data (e.g., use the "medium-expert" variant for training and "medium" for fine-tuning, or vice versa) to demonstrate the attack does not require access to the original training distribution.

2. **Fix the baseline comparisons.** (a) Describe how Baffle and IMC were adapted for the TO setting, including trigger injection, loss functions, and training loops. (b) Add a simple baseline: fix the trigger values (random or handcrafted), do not perform alternating training, and train with the same loss. This directly isolates the benefit of the alternating training and learned trigger.

3. **Report the ASR threshold ε** used in Eq. (2) and discuss its impact on results.

4. **Discuss the fine-tuning defense in the main text** as a limitation of the attack's persistence, with suggestions for potential countermeasures or analysis of when fine-tuning is or isn't practical for end users.

## Score and Decision

Calibration anchors used (all rounds):

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|-------------------------|
| `em0gAL8fbK` (temporal logic backdoor, offline RL AD) | 4.00 | 1 | Weaker — higher poisoning rate (15%), more unrealistic threat model assumptions |
| `HZnnHDrBXD` (tree-based action manipulation attack) | 5.75 | 1,2 | Comparable — different strengths (they have theory, we have broader experiments); our experimental scope is larger (6 tasks vs 2) but we lack theoretical guarantees |
| `UhW2wA1pRV` (robust DRL behavior manipulation) | 5.50 | 1,2 | Comparable — both have attack+ablation+defense; our evaluation is more comprehensive across tasks/models |
| `rp5vfyp5Np` (BATTLE, behavior-oriented attacks) | 4.25 | 1 | Stronger than this paper — more tasks, more thorough evaluation |
| `X2x2DuGIbx` (certified defense offline RL) | 6.75 | 1 | Not directly comparable (defense paper with theoretical certification) |
| `S1Bv3068Xt` (BALD, backdoor attacks on embodied LLM systems) | 6.25 | 2 | Stronger — more comprehensive threat surface exploration, multiple attack vectors, though different domain |
| `oxjeePpgSP` (bi-level trigger optimization, contrastive learning) | 5.75 | 2 | Comparable — both propose trigger optimization via bi-level objective; our RL domain experiments are broader |
| `AKAlVyunxA` (SHINE, backdoor shielding for DRL) | 5.75 | 2 | Not directly comparable (defense paper) |
| `5e0yWSNGIc` (certified training in RL) | 5.33 | 2 | Not directly comparable |

**Round-1 bracket:** [4.0, 6.25] — the paper is clearly stronger than the weakest anchor (em0gAL8fbK at 4.00) and weaker than the strongest relevant anchor (S1Bv3068Xt at 6.25).

**Round-2 narrowing:** All anchors in the [4.5, 6.5] band place the paper between 5.5 and 6.0 in comparable quality. The threat model inconsistency and baseline concerns prevent it from reaching the level of S1Bv3068Xt (6.25), while its empirical scope and novel factor analysis place it above the weaker anchors.

**Final score:** 5.5

The paper addresses a timely and underexplored problem, presents a well-structured method, and provides the most comprehensive empirical evaluation of action-level backdoors for TO models to date. However, the threat model inconsistency (claiming "without access to the original training dataset" while using data from the same public benchmarks) and the inadequate baseline comparisons undermine the credibility of the evaluation. These issues require substantial revision. With a clarified threat model, fairer baselines, and better documentation of experimental details, this would be a solid paper.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>