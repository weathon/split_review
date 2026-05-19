- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6
Now I have a thorough understanding of the paper and all reviewer claims. Let me construct the final consolidated review.

## Summary

This paper proposes DRIMA, a distributed training with decentralized execution (DTDE) approach for cooperative multi-agent reinforcement learning. The core idea is a "conflict-triggered differential reward interaction" (DRI): agents exchange scalar differential rewards with neighbors and, when the signs of the differential rewards disagree (indicating "conflict"), reshape their individual reward to the neighbor-averaged reward. This is intended to prevent the joint policy from converging to saddle Nash equilibria. The method is evaluated on matrix games, MPE, and SMAC with DQN, DDPG, A2C, and MAPPO.

## Strengths

- **Novel and simple mechanism for cooperative reward reshaping.** The conflict-triggered condition — using sign disagreement between an agent's differential reward and its neighbors' averaged differential reward — is intuitive and clearly motivated. The method exchanges only scalars, making communication efficient. (Section 3.1)

- **Clear demonstration on a two-player Prisoner's Dilemma.** Section 3.2 provides a worked gradient-analysis showing how, at a specific policy point (p=0.4, q=0.8) with the (0,18) sample, DRI reshapes gradient directions to align with the global optimum rather than the saddle NE. Figures 1-2 visualize the reward surfaces and the mechanism. (Section 3.2, Figures 1-2)

- **Empirical attainment of global optima in matrix games.** Figure 3 shows that DRIMA variants of DQN, DDPG, and A2C all reach the global optimum in both Prisoner's Dilemma and the Maintain game, whereas their independent counterparts converge to poor saddle equilibria. (Section 4.1, Figure 3)

- **Ablation confirms the necessity of the conflict trigger.** The "Dri-naive" variant (constant averaging without the sign-based trigger) performs substantially worse than DRIMA in MPE, especially at larger scales. This provides direct evidence that the conflict-detection mechanism, not simple averaging, drives the improvement. (Section 4.2, Figure 4, line 207)

- **Compatibility demonstrated across multiple algorithm families.** DRIMA is shown with DQN (value-based), DDPG (deterministic policy), A2C (stochastic policy), and MAPPO (on-policy actor-critic), spanning discrete and continuous action spaces. (Sections 4.1-4.3)

## Weaknesses

### Fatal
None.

### Major

- **Unsupported claim of "provable convergence."** The abstract and introduction state that DRIMA "possesses provable convergence" (lines 10, 23). The paper contains no theorem, proof, or rigorous convergence argument. The only substantive mention of convergence is a reference to Qu et al. (2020) that "ensures the scalability and provable convergence of networked MARL" (line 173) — this concerns a different framework and is not adapted or shown to apply to DRIMA. This is a clear overclaim. Either a convergence theorem under stated assumptions must be provided, or the claim must be retracted.

- **Theoretical claim about eliminating saddle equilibria in general Markov games is not convincingly established.** The paper's main theoretical content (Section 3.2) is a worked example analyzing one specific policy point in a two-player Prisoner's Dilemma under a particular sigmoidal parameterization. This demonstrates the mechanism's behavior in one instance but does not constitute a general proof that DRIMA eliminates saddle equilibria in multi-agent Markov games. Section 3.3 attempts to extend the result via mean-field theory, but the derivation stops at writing down the reshaped TD update equations; the crucial claim that "the stationary points of solution space only contain local optimum, global optimum, and inflection ones" (line 175) is asserted without any derivation or proof. The gap between the paper's ambitious theoretical claims and the actual evidence provided is substantial.

- **Weak CTDE baselines in MPE.** The '-Ctde' baseline is described as "using a global reward that sums up all agents' rewards for learning" (line 198). This is not centralized training with a centralized critic — it is independent learning with a shared reward, which is known to struggle with credit assignment. The paper cites MADDPG (Lowe et al., 2017) in the introduction but does not compare against it or any other proper CTDE method with a centralized action-value function. Calling this baseline "CTDE" is misleading, and the claim that DRIMA "outperforms CTDE" in MPE rests on a strawman comparison.

- **No experimental comparison against other DTDE methods.** The paper positions DRIMA in the DTDE family and discusses consensus-based methods, mean-field RL, and GNN-based approaches as prior work (Section 1), yet evaluates against none of them. To demonstrate that DRIMA advances the state of the art in distributed MARL, comparison against at least one existing DTDE algorithm is necessary. As it stands, the reader cannot assess whether DRIMA is competitive with, or superior to, other distributed approaches.

### Minor

- **Limited statistical rigor.** All experiments use only 5 random seeds (line 182). Median win-rate curves are reported without confidence intervals, interquartile ranges, or variance bands. For SMAC in particular, where run-to-run variance is known to be high, this is insufficient to support claims of outperformance (e.g., the 5m_vs_6m result).

- **No diagnostic analysis of the conflict trigger itself.** While the Dri-naive ablation is useful, there is no analysis of how often the conflict trigger fires during training, whether the sign condition correlates with actual conflict, or how sensitive results are to the sign-based criterion. The sign of a single sample's deviation from a running mean is noisy, especially early in training. Understanding the trigger's behavior would strengthen confidence in the mechanism.

- **Discounted reward implementation not fully specified.** The paper develops the theory under the average-reward formulation and notes that it "can be generalized to the discount-reward one" (line 58). However, the conflict detection relies on the sign of (r^i - μ̄), and it is not specified how μ̄ should be estimated or interpreted in the discounted setting. This is a gap in reproducibility for the experiments, which almost certainly use discount factors.

### Trivial
None.

## Nice-to-Haves
- Comparison against other reward-shaping methods (e.g., Chu et al. 2020, Hostallero et al. 2020) would strengthen the experimental positioning.
- An analysis of communication cost (number of messages exchanged, total bandwidth) would quantify the claimed efficiency.
- Analysis of whether the SMAC and MPE tasks actually contain saddle equilibria that are problematic for independent learning would directly support the saddle-avoidance narrative.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **Criticism that "the case when sgn(x)=0 is undefined"** — The paper explicitly defines sgn(0)=0 in Eqn. (2) (line 80). This criticism is factually incorrect.

2. **Several generic concerns from the harsh critic** framed as area-of-concern sweeps without concrete anchors (e.g., general statements about "insufficient evaluation rigor" that aren't pinned to specific figures or claims beyond what is already captured above in the statistical rigor point).

3. **"Provable convergence" claim reframed as a Fatal flaw** — While the overclaim is real and significant, it does not invalidate the paper's core contribution (the DRI mechanism itself). It is a major overstatement that requires retraction or proof, not a fatal error. It has been correctly elevated as a Major weakness above.

## Novel Insights

The two reviews are largely consistent in identifying the core tension: the paper has an interesting and well-motivated algorithmic idea, but its presentation significantly overreaches on theoretical guarantees while underdelivering on experimental rigor. Neither reviewer provides genuinely novel insight beyond what the paper's own contributions and limitations surface. The conflict-triggered mechanism itself — using sign disagreement of differential rewards as a lightweight signal for when to coordinate — is the paper's most valuable conceptual contribution.

## Suggestions

1. **Retract the "provable convergence" claim** unless a proper theorem and proof (even under restrictive assumptions) are added. Present the method as empirically grounded rather than claiming theoretical guarantees that are not provided.

2. **Add proper CTDE baselines in MPE**, particularly MADDPG, and compare DRIMA against at least one existing DTDE method (e.g., a consensus-based or mean-field approach). Without these comparisons, the work cannot be evaluated against the state of the art.

3. **Increase the number of random seeds** (to at least 10) and report confidence intervals or interquartile ranges on all learning curves. For SMAC, consider reporting both median and mean win rates with variance.

4. **Add a diagnostic section** analyzing the conflict trigger: how often it fires, how the firing rate evolves during training, and whether firing correlates with improvements in joint reward.

5. **Specify the discounted-reward implementation** precisely, including how μ̄ is maintained and used in TD updates when γ < 1.
