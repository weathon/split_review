## Summary

TrojanTO proposes the first post-training action-level backdoor attack against Trajectory Optimization (TO) models in offline reinforcement learning. The method uses trajectory filtering, batch poisoning, and alternating training (trigger-model co-optimization) to implant backdoors with a claimed low poisoning budget (0.3% of trajectories). Experiments across three TO architectures (DT, GDT, DC) on six D4RL tasks show TrojanTO achieves an average composite score (CP) of 0.701, compared to 0.342 for Baffle and 0.551 for IMC.

## Strengths

1. **First post-training backdoor formulation for TO models (Section 3.3)**: The paper identifies a realistic supply-chain threat scenario where an adversary modifies a pretrained model without access to training. Prior RL backdoor work (Baffle, TrojDRL) requires access to the training loop or dataset, making this a genuinely underexplored and practically relevant threat vector.

2. **Empirical finding that reward manipulation is irrelevant for TO model backdoors (Section 4.3, Figure 1)**: The paper shows that ASR/BTP trajectories are essentially invariant across multiple reward manipulation strategies for DT, DC, and GDT models. This finding departs from all prior RL backdoor literature and directly motivates the paper's design choice to omit reward modification.

3. **Component-level ablation study isolates each module's contribution (Section 6.2, Table 5)**: Removing alternating training drops ASR from 0.719 to 0.507; removing batch poisoning drops ASR to 0.528; removing trajectory filtering drops BTP from 0.914 to 0.850. These non-overlapping degradations confirm each component serves a distinct role.

4. **Broad model and environment coverage (Table 4)**: Results span Transformer-based (DT), graph-based (GDT), and convolutional (DC) architectures across locomotion (Hopper, HalfCheetah, Walker2d), navigation (AntMaze), and manipulation (Kitchen, Pen) tasks, reducing architecture-specific concerns.

## Weaknesses

### Major

1. **ASR threshold ε is never specified (Section 3.4, Equation 2)**: The attack success rate is defined using a threshold ε: an attack succeeds only if every component of the output action is within ε of the target action. The value of ε is never stated in the main paper. Since ASR is one of the two components of the headline CP metric, every quantitative result in Table 4 depends on this parameter. Without knowing ε, the reader cannot determine whether ASR=0.719 represents genuinely precise control or a loose tolerance. If ε is large relative to the action space scale, the metric becomes trivial and the reported improvements over baselines lose meaning. This is the single most consequential missing detail — it is not an appendix nicety but a prerequisite for interpreting all reported results.

2. **Threat model ambiguity: source and denominator of "0.3% of trajectories" (Section 3.3)**: The adversary is described as operating "without access to the original training dataset" while using "a minimal set of poisoned trajectories (e.g., 0.3%)." The paper never specifies (a) where these trajectories come from, (b) what the 0.3% is a fraction of, or (c) how obtaining them is consistent with the claimed post-training no-access threat model. If the adversary samples from the D4RL dataset (which is publicly available), they effectively have access to data distributionally similar to the original training data, undercutting the "no access" framing. If the adversary collects trajectories from the environment via a proxy policy, the required capabilities and associated distribution shift are not discussed. The attack budget claim is unverifiable without the denominator.

### Minor

3. **Main results table (Table 4) omits variance**: The central experimental result reports averages over 3 random seeds and 3 target actions with no standard deviations, despite the authors clearly having per-seed data (Tables 6 and 7 include ± values). Without variance, it is impossible to tell whether several reported differences are statistically meaningful — e.g., DT-Hopp: TrojanTO CP=0.365 vs Baffle CP=0.313; DT-Pen: TrojanTO CP=0.664 vs IMC CP=0.667 (TrojanTO is lower).

4. **Trigger dimensions selected post-hoc (Section 4.2)**: The paper tests multiple trigger dimension choices and fixes (1,2,3) because it yields the highest ASR. Table 2 shows ASR ranges from 0.000 to 0.915 depending on dimension. This amounts to selecting the evaluation configuration based on the metric it measures. In a realistic attack, the adversary would not know which dimensions are optimal a priori. The reported ASR numbers likely represent an upper bound achievable with oracle knowledge.

5. **Comparison with Baffle conflates qualitatively different attack types**: Baffle is a policy-level backdoor (concerned with degrading long-term returns) while TrojanTO is an action-level backdoor (forcing a specific action at a specific step). The CP metric combines ASR and BTP, but ASR measures fundamentally different phenomena for these two attack types. The claimed "105% improvement over Baffle" would be more interpretable if accompanied by a within-paradigm baseline (e.g., naive fine-tuning with the backdoor loss but without TF/BP/AT).

6. **Low ASR on AntMaze is not discussed**: TrojanTO's ASR on AntMaze is notably low (DT: 0.296, GDT: 0.334), and on DC-Ant, IMC (0.718) outperforms TrojanTO (0.572). The paper does not discuss why the method struggles in sparse-reward navigation tasks, which is a meaningful limitation.

### Trivial

7. **Figure 1 legend duplicates "w/ RM-4"**: The legend lists this label twice (in orange and green), which appears to be a labeling error.

## Nice-to-Haves
- The defense analysis (Section 6.5) is purely qualitative; reporting post-fine-tuning ASR/BTP would strengthen it.
- A mechanistic discussion of why boundary actions ('1', '-1') yield near-perfect ASR while interior actions ('0') yield much lower ASR (Table 1) would enrich the empirical analysis.
- Specifying which D4RL dataset variant (medium, medium-replay, medium-expert) is used for each environment.

## Removed Points
- The harsh critic's complaint about the defense section being thin was removed because the paper states results are in Appendix B.1 (stripped by the parser).
- The critic's complaint about post-training attacks being "inherently easier" than pre-training attacks was removed as speculative.
- The critic's characterization of the persistent backdoor section as "inflated" was removed — it is a reasonable empirical extension even if conceptually straightforward.
- General claims about missing baselines that are not specifically grounded in the paper text were removed.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- State the value of ε in the main paper, justify it relative to the action space scale, and ideally plot ASR as a function of ε.
- Clarify the threat model: specify where the adversary's trajectories come from and what "0.3%" is a fraction of.
- Add variance (std dev or confidence intervals) to Table 4.
- Add a within-paradigm baseline (e.g., standard backdoor fine-tuning without TF/BP/AT) to isolate the contribution of TrojanTO's design.
- Discuss the AntMaze failure case — understanding why the method struggles in sparse-reward settings would strengthen the paper.

## Calibration Anchors
**Round 1 (bracketing)**:
- Low band: Certified Copy (3.00), Deferred Backdoor (3.00), Gradient Storm (3.00), LeBD (3.25)
- Middle band: SHINE (5.75), Universal Jailbreak Backdoors (5.75), Professor X (5.20), LPS (5.50)
- High band: DeepLTL (8.00), Emergent Planning (8.00), Curiosity Red-Teaming (8.00)

**Round 2 (narrowing)**:
- BALD (6.25): More comprehensive attack framework across multiple LLMs and embodied tasks; TrojanTO is substantially less comprehensive
- LPS (5.50): Backdoor sample selection with thorough evaluation but some defense concerns; TrojanTO has more significant evaluation gaps (ε unspecified)
- Robust DRL Behavior Manipulation (5.50): Attack+defense with theoretical analysis; TrojanTO lacks comparable theoretical backing
- SHINE (5.75): DRL backdoor defense with theoretical guarantees; TrojanTO has a genuine contribution but the ε issue is a gap SHINE does not have

**Round-1 bracket**: between 3.5 and 6.5 (above weak band, below strong band)
**Round-2 narrowing**: TrojanTO is weaker than the 5.5-5.75 anchors (SHINE, LPS, Robust DRL) due to the unstated ε value and threat model ambiguity; stronger than the 3.0-3.25 weak anchors
**Final score**: 4.5

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>