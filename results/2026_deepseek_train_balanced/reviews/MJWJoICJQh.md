## Summary

The paper proposes QC-SAC, a hybrid learning method combining Soft Actor-Critic (SAC) with a Q-compared behavior-cloning objective (QCO) that weights demonstration data by the Q-value difference between the demonstration action and the current policy's action, discarding detrimental demonstrations when the difference is negative. Additional components include Q-network training from demonstrations (QNfD) and selective dataset expansion with successful episodes (SDDU). The method is evaluated on two urgent hazardous driving scenarios — oversteer control with collision avoidance (OCCA) and time-trial race (TTR) — showing improvement over BC, SAC, and BC-SAC baselines.

## Strengths

- **QCO weighting mechanism is a principled solution to the immature-demonstration problem.** Equation (4) defines the weight $C(s_d,a_d) = \max(Q^-(s_d,a_d) - Q(s_d,\pi_\phi(s_d)), 0)$, which applies BC loss only when the demonstration action has a higher Q-value than the current policy's action, and discards harmful demonstrations otherwise. The use of L1 loss (rather than log-probability) to avoid divergence with out-of-distribution actions from immature demonstrations is a practical and sensible design choice (Section 3.1, lines 77–85).

- **Ablation study systematically isolates QCO, QNfD, and SDDU.** Section 4.3 tests each component: removing QCO leaves baselines far below QC-SAC even with QNfD and SDDU applied; removing QNfD causes severe performance degradation (confirming accurate Q-estimation is necessary for QCO); removing SDDU causes overfitting after ~2000 episodes. This provides mechanistic insight beyond a generic ablation check.

- **Two diverse environments with complementary metrics reduce simulator-specific concerns.** OCCA uses IPG CarMaker (realistic vehicle dynamics) evaluating obstacle-avoidance success rate; TTR uses CARLA evaluating lap time and completion rate. Consistent superiority across both strengthens the empirical case (Sections 4.1–4.2).

- **Failure decomposition in OCCA is transparent.** The paper reports the raw 81.8% success rate alongside the adjusted 99.0% figure, and provides video examples of the "physically impossible" failure cases (Section 4.1, line 160; Figure 5a). This is more informative than binary success/failure reporting alone.

## Weaknesses

### Fatal

None.

### Major

- **The 99.0% "near-optimal" claim is not rigorously justified.** The paper reports an 81.8% raw success rate for QC-SAC in OCCA, then argues that 87 of 91 failures (95.6%) were "physically impossible" because the obstacle "completely block[s] the path in the direction of the vehicle's skid," yielding an adjusted 99.0% rate. However: (a) no formal characterization of the reachable set under the vehicle dynamics, nor any oracle-based upper bound, is provided to validate the "impossible" classification; (b) baseline failures are not similarly classified — if BC-SAC's 327 failures also include physically impossible cases, the reported 2.36× ratio is inflated. The paper honestly reports the raw number, but the "near-optimal" framing and the adjusted 99.0% figure are conclusions the current evidence does not fully support (Section 4.1, line 160).

- **Focused Experience Replay (FER) is a confound that is not controlled across baselines and not ablated.** Section 3.4 introduces FER as a component of QC-SAC, but the paper never states whether the baselines (BC, SAC, BC-SAC) also use it. If FER is exclusive to QC-SAC, some or all of the measured improvement could come from FER rather than QCO/QNfD/SDDU. Critically, the ablation study (Section 4.3) removes QCO, QNfD, and SDDU but never removes FER, so the ablation cannot distinguish whether the proposed components are individually necessary or whether FER is doing much of the work.

- **Baseline set is too narrow for the claimed contribution, and prior work is mischaracterized.** The paper compares against BC, SAC, and BC-SAC. Several methods in the literature are designed specifically for learning from imperfect/noisy demonstrations — including DQfD (Hester et al., 2018) and Gao et al. (2018) — all cited in the paper's own references. The paper claims HL techniques "require nearly optimal demonstration data or, even if noisy, must contain optimal demonstration data" and cites Gao et al. (2018) in support (line 13), but Gao et al.'s method is explicitly titled "Reinforcement Learning from Imperfect Demonstrations" and is designed for this setting. This mischaracterization, combined with the omission of these methods as baselines, means the reader cannot assess whether QC-SAC's QCO mechanism improves over existing approaches to the imperfect-demonstration problem.

### Minor

- **"World-first" claims are unsubstantiated.** The paper asserts QC-SAC is "the world-first safe-advanced autonomous driving technology capable of controlling a vehicle oversteer safely and avoiding obstacles ahead" (abstract, line 5–6; introduction, line 16; conclusion, line 190). No exhaustive literature review is provided to support this claim. The paper discusses drift-control works (Cutler & How 2016; Cai et al. 2020; Zhang et al. 2018) and notes they focus on path-tracking rather than integrated obstacle avoidance (line 29), which provides context but does not constitute proof of "world-first" status. These claims add no scientific substance and should be removed.

- **Reward functions and success metrics are not defined.** The paper reports a "control & avoidance success rate" (line 160) but never specifies what constitutes success (any collision-free trajectory? staying within lane boundaries? reaching a goal location?). The reward functions for OCCA and TTR are not described. Without these details, the reader cannot interpret what the Q-function is learning or whether the reported metric is appropriate.

- **Human baseline is from non-expert drivers, undercutting the "expert human" framing.** The abstract characterizes UHS as "difficult even for expert human drivers" (line 4), but the reported human baseline of ~15% success rate (line 160) comes from the same untrained drivers (using a racing wheel) who collected the demonstration dataset — not from professional or expert drivers. This weakens the comparison.

- **SDDU has no mechanism to remove low-quality demonstrations added early in training.** Early episodes added to the demonstration dataset when the reward threshold is low may anchor the policy to mediocre behavior. The dataset grows without bound, and there is no pruning mechanism. The monotonic-improvement argument (Eq. 7, line 121) assumes higher-reward episodes are also better for behavioral cloning, which may not hold if a high-reward episode exploits a brittle strategy that is hard to clone.

### Trivial

None.

## Nice-to-Haves

- An oracle-based or MPC-based upper bound on OCCA performance would either validate or refine the 99.0% claim.
- A discussion of limitations — particularly sim-to-real transfer, sensor noise, and actuation latency — would strengthen the paper given its safety-critical framing.

## Removed Points

These points were flagged for removal. They are listed here for transparency but do not affect the assessment.

- **Dangling "2" and "3" superscripts (line 31, line 41).** These are parser-induced formatting artifacts from PDF extraction. The original submission likely had proper footnotes. Removed per hard rules on formatting artifacts.
- **Missing reproducibility details (network architecture, learning rates, hyperparameters).** These are typically in the appendix, which the parser strips from all papers. Removed per hard rules.
- **"No discussion of real-world deployment challenges" (Harsh Critic's "Missing Parts").** This demands addressing problems outside the paper's stated scope. Demoted to Nice-to-Have.
- **Strength Finder's generic praise ("addressed an important problem," "targeted an interesting question").** Removed as superficial. Only concrete, evidence-grounded strengths are retained.

## Novel Insights

None beyond the paper's own contributions. The cross-review analysis reveals that the QCO mechanism is widely recognized as the paper's strongest and most original idea, while the main weaknesses cluster around evaluation thoroughness (FER confound, baseline selection, lack of oracle upper bound) and overclaiming (99.0% adjustment, world-first assertions) — not around the core method's soundness.

## Suggestions

1. **Remove or rigorously justify the 99.0% adjustment.** Either provide an oracle-based upper bound (e.g., an MPC or expert policy with full state information that establishes what fraction of scenarios are physically solvable) or report only the raw 81.8% as the primary result and treat the decomposition as a secondary analysis with appropriate caveats.
2. **Ablate FER from QC-SAC and state explicitly whether FER is applied to all baselines.** If FER was used for all methods, clarify this in the text; if not, re-run baseline experiments with FER to eliminate the confound.
3. **Add at least one baseline from the imperfect-demonstration literature** (e.g., DQfD adapted for continuous control, or Gao et al. 2018) to properly situate QC-SAC's contribution.
4. **Define the reward functions and success metrics explicitly** for both OCCA and TTR scenarios.
5. **Remove all "world-first" claims** and replace with specific, verifiable statements about what the method achieves relative to the cited prior work.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>