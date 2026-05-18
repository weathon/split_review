Now I have all the evidence I need. Let me write the final consolidated review.

---

## Summary

This paper introduces Inverse-Att, a Theory-of-Mind-inspired MARL method where agents learn to infer the attention weights of other agents via an inverse attention network, then use those inferred weights to update their own attention and actions. The method is evaluated across five multi-agent tasks in MPE (cooperative, competitive, and mixed) using a mix-and-match protocol, with additional human experiments. The core empirical finding is that Inverse-Att consistently and substantially outperforms MAPPO, IPPO, MAA2C, ToM2C*, and Self-Att baselines across all environments.

## Strengths

- **Novel integration of attention-based ToM in MARL.** The paper operationalizes Theory of Mind through explicit attention-weight inference rather than Bayesian belief modeling, using end-to-end neural network training. This is a genuine departure from prior ToM approaches (Section 2.1) and is concretely instantiated in the three-phase pipeline (Figure 1, Algorithm 1).

- **Consistent and substantial empirical gains across all five tasks.** In Table 1, Inverse-Att achieves the highest average reward in every environment and role (8/8 comparisons), often by large margins (e.g., Spread: 404.14 vs. runner-up Self-Att 283.89; Navigation: 497.96 vs. 328.24). These results are supported by mix-and-match evaluation over 2×10⁶ steps per task with random sampling from a multi-method agent pool.

- **Human experiments showing competitive ad-hoc cooperation.** When paired with human participants in 5 roles across 3 environments, Inverse-Att achieves the highest average reward in 4 of 5 roles, including near-zero penalty for the Adversary sheep role (−0.8 vs. MAPPO's −48.8 and Self-Att's −8.0). While sample-limited, this provides complementary evidence beyond simulation-only evaluation.

- **Scalability demonstrated across population sizes.** The method maintains its advantage over Self-Att and MAPPO across 2, 3, and 4 agents in Spread, Adversary, and Grassland (Tables 2–4), showing the approach does not degrade with group size.

- **Inverse network prediction accuracy validated.** Figure 5 shows the inverse network predicts the top-priority goal with near-100% accuracy and top-two accuracy remains very high across environments, supporting the claim that the inverse network successfully learns the mapping from observations/actions to attention weights for self-attention agents.

## Weaknesses

### Fatal
None.

### Major

- **The inverse attention network's application to non-attention agents in mix-and-match evaluation is undertheorized, weakening the scientific claim about the mechanism.** The IW network is trained exclusively on data from Self-Att agents during Phase 1 (line 129: "Using the dataset D, which is agent's own data collected during the training process of Phase 1, we train the IW_i network"). In mix-and-match evaluation, Inverse-Att agents are paired with MAPPO, IPPO, MAA2C, and ToM2C* agents — none of which have an attention-weight-based internal state of the kind the IW was trained to predict. The paper states that inference is applied to "agents of the same type" (lines 84, 121, 136, 147), but this refers to role/team identity (e.g., both are sheep), not algorithmic architecture. The paper does not discuss whether the IW network's outputs are meaningful when processing observations from MAPPO agents that lack attention representations, nor does it provide evidence (e.g., via correlation analysis or ablation) that the performance gain in cross-method settings stems from attention inference rather than from the UW_i network learning to use the IW's output as a generic coordination signal. The Limitations section (line 377) acknowledges "attention inference is limited to the same type of agents" but uses "type" ambiguously. Since the mix-and-match results constitute a central part of the evaluation (Table 1, all five tasks), this gap significantly undermines the paper's causal claim that Inverse-Att works because of ToM-based attention inference in the cross-method setting. The authors should either: (a) provide evidence that the IW generalizes to non-attention agents, (b) restructure the analysis to separate same-architecture from cross-architecture pairings, or (c) explicitly reframe the claim for cross-method scenarios.

### Minor

- **The evaluation metric is not precisely defined.** The paper reports "average reward" (line 212) without specifying whether this is per-agent cumulative reward per episode, per-team cumulative reward, or per-step average. While the critic's claim about zero-sum inconsistency is incorrect (it misunderstands the mix-and-match design — different methods occupy different roles in different episodes, so per-method averages are not expected to satisfy the game's per-episode zero-sum property), the paper would benefit from stating explicitly: "All reported rewards are average cumulative reward per episode, averaged over 1000 evaluation episodes, with per-agent statistics broken down where applicable." The current lack of precision is a clarity gap, not a fatal error.

- **The human experiment is underpowered.** With only 5 participants and 5 episodes per role, the standard deviations are large and often comparable to the mean differences (e.g., Spread: Self-Att 272.0±30.41 vs. Inverse-Att 332.3±17.13; Grassland Wolf: Self-Att 197.9±12.76 vs. Inverse-Att 185.7±30.45). This is appropriately presented as supplementary evidence, but the paper should explicitly note the small sample size as a limitation rather than stating "our model demonstrates superior cooperation with humans" as a primary result.

- **The inverse accuracy analysis (Figure 5) only evaluates on Self-Att agents.** While this is appropriate for validating that the IW learns its intended mapping, it does not address the generalization concern raised above (Major weakness). The paper should acknowledge this limitation in the accuracy analysis discussion.

### Trivial
None.

## Nice-to-Haves

- An ablation that feeds zeroed or random "inferred" weights through UW_i to isolate the benefit of actually using the IW's output (partially addresses the Major weakness).
- A discussion of whether the inverse network's predictions are used only at inference time or also during Phase 3 training (the algorithm suggests the latter, but this could be clarified).

## Removed Points

These points from the reviews are removed for the following reasons:

- **Critic Issue 3 (GF representation as a confounding factor):** The GF representation is described in the Environment section (line 195: "The key distinction lies in our application of the GF function atop raw observations, resulting in a gf representation"). It is part of the environment's observation space for all agents, not a method-specific feature. The critic's claim that "Self-Att and Inverse-Att are the only methods using GF" is factually incorrect — all baselines operate in the same environment with the same observations. Removed as factually wrong.

- **Critic's claim of "internal inconsistency" in reward sums:** The critic argues wolf + sheep rewards should sum to zero in the Adversary game. This misunderstands the mix-and-match protocol: per-method averages come from different episode compositions (a MAPPO wolf faces various sheep methods; a MAPPO sheep faces various wolf methods). There is no expectation of zero-sum consistency across rows. Removed as factually wrong.

- **Strength Finder's claim that human experiments demonstrate "superior ad-hoc cooperation" as a core strength:** This is slightly overstated (Inverse-Att does not win in Grassland Wolf), so it is downgraded to a more qualified statement in Strengths above. The original overclaim is removed.

- **Generic strength phrasing about "addressing an important problem":** The Strength Finder's supporting strengths are concrete and evidence-backed, so no generic removals needed beyond the above.

## Novel Insights

The most striking observation is the nonlinear marginal return of adding more Inverse-Att agents (Spread table): team rewards jump from 109 (0 Inv-Att, scale 4) to 1140 (4 Inv-Att) — a 10× improvement. This suggests that attention-aware agents create a positive coordination synergy beyond what additive individual improvement would predict, and importantly, that this does not collapse into the "cognitive loop" instability the authors worry about. This emergent property is arguably more interesting from a multi-agent systems perspective than the individual method-level comparisons.

## Suggestions

1. **Address the mechanism gap for cross-method inference directly.** Either provide evidence (via a controlled experiment) that the IW produces useful signals even for non-attention agents, or explicitly reframe the claims to distinguish between same-architecture and cross-architecture settings. A simple diagnostic would be to train an IW on data from multiple policy types and compare its accuracy against the current single-type IW.

2. **Define the evaluation metric precisely** in a single sentence at the start of Section 6.3, e.g.: "All reported rewards are the mean cumulative per-agent reward per episode, averaged over 1000 evaluation episodes (200 steps each), with 95% confidence intervals computed across 3 seeds."

3. **Report the inverse network's prediction accuracy for cross-method inputs** (even if ground-truth attention is unavailable for non-attention agents, one could report whether the inferred weights correlate with downstream task-relevant quantities).

4. **Expand or qualify the human experiment.** Add an explicit limitation statement about the small sample size, and consider presenting the results as a pilot illustration rather than a primary evaluation.

## Score and Decision

Based on my assessment: the paper introduces a novel and interesting method, the empirical gains are substantial and consistent, and the core idea (attention-based ToM via inverse networks) is well-motivated. However, the Major weakness — the unexplained application of the inverse network to non-attention agents in the central mix-and-match evaluation — leaves the paper's mechanistic claims under-supported. This does not invalidate the empirical results (which are strong), but it prevents the paper from being fully convincing about *why* the method works. With a clear discussion or additional analysis addressing this, the paper would be strong. In its current form, the contribution is solid but the scientific framing exceeds what the evidence supports.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>