Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper provides the first empirical demonstration of the Incomplete Preferences Proposal (IPP) by implementing DREST (Discounted Reward for Same-Length Trajectories) reward functions in simple gridworlds. The authors define formal metrics (USEFULNESS and NEUTRALITY), prove a theorem showing that policies maximizing expected DREST return are maximally USEFUL and NEUTRAL, and train tabular REINFORCE agents that achieve near-maximal scores on both metrics. The key finding is that DREST agents learn to be useful conditional on each trajectory-length while choosing stochastically between lengths (probability ~0.5), whereas default agents become strongly biased toward longer trajectories.

## Strengths

- **First empirical operationalization of the IPP.** The paper translates the Incomplete Preferences Proposal from a theoretical framework into a concrete training setup with measurable outcomes. The USEFULNESS and NEUTRALITY metrics provide a clear, quantitative way to evaluate whether agents satisfy the two conditions of POST, enabling reproducible future work on this approach.

- **Theoretical grounding for the reward design.** The theorem (Section 5) stating that any policy maximizing expected return under the DREST reward function is maximally USEFUL and NEUTRAL provides a principled foundation. The results show that the empirical outcomes are consistent with this theoretical prediction, even if REINFORCE may not provably converge to the optimal policy in the POMDP.

- **Clean empirical evidence that DREST agents behave differently from default agents in the expected way.** The comparison of typical trained policies (Figure 2) and the learning curves (Figure 1) convincingly show that DREST agents approach NEUTRALITY near 1.0 by choosing each trajectory-length with probability ~0.5, while default agents strongly favor the longer trajectory. The experiment uses 10 seeds with individual trajectories shown, providing transparency about variability.

- **The lopsided rewards experiment tests a practical robustness concern.** The paper directly addresses the objection that exact equalization of maximum preliminary returns may be impossible. By testing x sampled log-uniformly from 0.01 to 100 (a 10,000-fold range), the experiment shows the range over which NEUTRALITY remains above 0.5 (0.1 to 10 for λ=0.9) and honestly reports degradation outside this range.

## Weaknesses

### Major

- **Claims about "eight other gridworlds" are unsupported.** The paper states "We also train agents in eight other gridworlds, to show that our results do not depend on the specifics of any particular gridworld" (line 79), but presents zero results from these gridworlds — no summary statistics, no table, no figure. This is not a missing-appendix issue (no appendix is referenced); it is an unsubstantiated claim about robustness. Without these results, the paper cannot support its assertion that findings generalize across gridworld configurations.

- **The lopsided rewards experiment's proposed λ-adjustment remedy is not tested.** The paper suggests lowering λ to widen the range of reward ratios over which NEUTRALITY is maintained (line 215), but provides no experiments confirming this works. This is a significant gap because the paper's response to the practical objection about unknown divisors depends on this claim — if lowering λ does not actually restore NEUTRALITY at extreme ratios, the approach's practical viability is weakened. The experiment shows NEUTRALITY degrades at Cx=0.01 and Cx=100; testing whether λ=0.5 or λ=0.3 rescues it would directly strengthen the paper's core argument.

### Minor

- **The connection between NEUTRALITY and genuine neutrality/shutdownability remains a conjecture.** The paper's "shooting themselves in the foot" argument (lines 205-206) is informal and the Limitations section (line 222) itself calls this rationale "somewhat speculative." This is an honest acknowledgment, but it means the paper's headline connection to the shutdown problem rests on an unvalidated inference. The paper would benefit from experiments directly testing whether NEUTRAL agents forgo costly opportunities to bias their trajectory-length distribution.

- **The shutdownability tax is asserted based on visual inspection only.** The paper claims the tax is "small" based on visual similarity of USEFULNESS curves (Figure 1). The DREST agents appear to have slightly higher variance and may take modestly longer to converge. Quantifying this (e.g., episodes to 90% of final USEFULNESS with confidence intervals) would make the claim rigorous rather than impressionistic.

- **No hyperparameter sensitivity analysis is provided.** Hyperparameters (λ=0.9, γ=0.95, learning rate schedule, ε schedule, number of mini-episodes per meta-episode) were selected via trial-and-error. Given that the paper's claims about viability for advanced agents depend on DREST being robust, a sensitivity analysis for at least λ and the meta-episode length would strengthen the paper.

- **The relationship between the theoretical theorem and the actual training algorithm is underexplored.** The paper acknowledges the environment is a POMDP (line 130) but does not discuss whether tabular REINFORCE with ε-greedy can reliably find the optimal policy in this setting, or what guarantees exist. Since the theorem is about optimal policies and the algorithm may not find them, this gap should at least be acknowledged.

### Trivial

- The ε-greedy exploration decays to 0.001 at evaluation (lines 137-138), which is a negligible 0.1% random action probability. The concern that this meaningfully contributes to measured NEUTRALITY is unwarranted; at ε=0.001, forced exploration cannot explain NEUTRALITY near 1.0 for two trajectory-lengths.

## Nice-to-Haves

- Test the proposed λ-adjustment for the lopsided rewards experiment (e.g., train with λ=0.5 and λ=0.3 at Cx=0.01 and Cx=100).
- Provide summary statistics (mean USEFULNESS, NEUTRALITY, trajectory-length probability) for all gridworlds tested, even briefly.
- Quantify the shutdownability tax precisely (e.g., episodes to reach 95% of final USEFULNESS).
- Add a brief sketch in the main text of why the DREST reward function incentivizes stochastic choice, given the POMDP structure.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"The proof of the theorem stated in Section 5 is not included."** — Per hard rules, the parser strips appendix/Supplementary Material from all papers; proofs that existed in the original submission are not visible in the parsed text. This criticism cannot be evaluated from the available text.

2. **"The lopsided experiments test a different (and easier) setting."** — The lopsided experiment intentionally removes the division-by-m normalization, making maximum preliminary returns *unequal* across trajectory-lengths. This is a *harder* test of DREST's robustness, not an easier one. The core concern (limited range, untested λ remedy) is valid and preserved above.

3. **"ε-greedy noise contributes to the measured NEUTRALITY"** — ε decays to 0.001 at evaluation, meaning forced random actions are 0.1%. This is orders of magnitude too small to explain NEUTRALITY near 1.0 for two trajectory-lengths (which requires ~0.5 probability each).

4. **"No experiments testing the λ-adjustment it proposes"** — This is preserved as a major weakness above (it is a valid point). It is listed here only to clarify it was not removed.

## Novel Insights

The reviews surface a deeper structural observation beyond the paper's own claims: the DREST approach faces a tension at its core that the paper does not fully address. On one hand, the theoretical optimal policy result (maximally USEFUL and NEUTRAL) requires knowing the correct divisor *m* to equalize maximum preliminary returns. On the other hand, the lopsided experiment shows that even approximate equalization fails at extreme ratios, and the proposed remedy (lowering λ) is itself a hyperparameter that would need to be set without knowing the true return scales. This creates a circular dependency — you need to know how imbalanced the returns are to know how low to set λ, but the whole point is that for advanced agents you do not know the returns. The paper's suggested solution (using samples of agents' actual preliminary return to estimate the maximum) is plausible but untested, and the reviews collectively highlight this as the approach's central unresolved vulnerability.

## Suggestions

1. Provide the results (e.g., a summary table of mean USEFULNESS and NEUTRALITY) for the eight additional gridworlds to substantiate the robustness claim, or remove the unsupported statement.
2. Test the λ-adjustment remedy in the lopsided setting at extreme ratios (Cx=0.01 and Cx=100) with λ values of 0.5 and 0.3 to concretely validate the proposed fix.
3. Quantify the shutdownability tax with a time-to-threshold metric (e.g., episodes until USEFULNESS ≥ 0.9 of final value) with confidence intervals, replacing visual inspection.
4. Add a brief discussion of the POMDP structure and what (if any) convergence guarantees tabular REINFORCE has in this setting, or explicitly note the gap between the theorem and the training algorithm.
5. Tone down the extrapolative language about advanced agents in the abstract and conclusion to better match the evidence presented — e.g., replace "suggest that DREST reward functions could also train advanced agents" with "suggest that further investigation into scaling DREST to more complex settings is warranted."

## Score and Decision

**Originality:** The paper introduces the first empirical implementation of the Incomplete Preferences Proposal, which is a novel contribution. **Importance of research question:** The shutdown problem is a well-recognized concern in AI safety, and empirical testing of proposed solutions is valuable. **Claims support:** The core empirical claim (DREST agents are USEFUL and NEUTRAL in the example gridworld) is well-supported. However, claims about the eight other gridworlds and about the shutdownability tax are not adequately supported. **Soundness:** The experimental design is appropriate for a proof-of-concept but has gaps (missing gridworld results, untested λ-adjustment, no quantification of the tax). **Clarity:** The paper is clearly written. **Value to community:** The paper provides a concrete starting point for empirical work on the IPP, but the limited scope and unsupported claims reduce its immediate impact.

The paper presents a clean proof-of-concept in a specific gridworld, with principled metrics and a theoretical grounding. However, it makes unsupported claims about eight additional gridworlds, does not test its own proposed remedy for the key vulnerability identified (the λ-adjustment), and relies on visual inspection rather than quantification for the shutdownability tax claim. These are addressable weaknesses, but in their current form they reduce the paper's credibility.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>