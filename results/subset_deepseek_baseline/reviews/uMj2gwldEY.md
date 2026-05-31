## Summary
This paper proposes a federated deep reinforcement learning (FL-DDPG) framework for coordinating multiple UAVs in wildfire tracking. The method combines a DDPG-based path planner with a performance-weighted federated averaging scheme that assigns higher aggregation weights to UAVs achieving better formation stability. Simulations for 3 and 5 UAVs show reduced spacing variance and improved cumulative rewards compared to independent DDPG.

## Strengths
- The application domain—wildfire monitoring with multi-UAV coordination—is practically relevant and well-motivated.
- The idea of using federated learning to enable collaborative policy updating without sharing raw sensor data is sensible for distributed robotics.
- The performance-weighted aggregation based on formation deviation is a clear and interpretable design choice.
- Results on formation spacing variance (2.5 m vs. 14 m) and average reward (−122.21 vs. −355.45) are indicative of meaningful improvement over the independent DDPG baseline.

## Weaknesses

### Fatal
None.

### Major
- **Insufficient baselines and controls.** The only comparison is against independent DDPG. Many stronger multi-agent RL baselines exist for continuous control: MADDPG, QMIX (with continuous extensions), VDN, or even simple centralized training with shared critics. Without comparisons to these or to standard FedAvg, it is impossible to attribute gains to the specific weighting scheme rather than to the mere presence of parameter sharing.
- **No statistical rigor.** Results are reported for what appears to be a single run (no error bars, no multiple seeds). DRL is inherently stochastic; claims of improvement cannot be assessed without reporting mean, variance, or confidence intervals across independent trials.
- **Limited evaluation scope.** Only 3 and 5 UAVs are tested, which does not convincingly demonstrate scalability to “large-scale” operation. The paper does not analyze the effect of federation frequency, aggregation period, or $\sigma$ sensitivity. The selective federation of only velocity-related parameters is not justified by ablation; other parameters (e.g., heading-related) could be equally critical.

### Minor
- The performance-weighted aggregation (Equation 12) is a simple exponential of spacing deviation. While effective, this is a minor variation of standard client weighting in federated learning and does not constitute a novel algorithmic contribution.
- The simulation uses a synthetic wind assumption ($\pi/4$) rather than actual wind data from the cited Kilmore East fire, which weakens the claim of realism.

### Trivial
- The paper mentions “Black Friday bushfire” but the cited reference (Cruz et al., 2012) is actually about “Black Saturday”; this inconsistency is likely a copy-paste error.

## Nice-to-Haves
- An ablation comparing FL-DDPG with the proposed weighting against FL-DDPG with uniform (FedAvg) weighting would cleanly isolate the effect of the weighting scheme.
- A plot showing the evolution of the federated aggregation weights over time would help interpret which UAVs drive the global model.
- Analysis of the communication overhead (bytes exchanged, round latency) would strengthen the practical motivation.

## Novel Insights
None beyond the paper’s own contributions. The observation that weighting aggregation by formation stability improves multi-UAV coordination is intuitive and the experimental demonstration is useful, but the insight is not theoretically surprising.

## Suggestions
- Add MADDPG and FedAvg baselines, and report results over at least 5 random seeds with mean ± std.
- Test on larger fleets (e.g., 10–20 UAVs) and vary the degree of fire asymmetry.
- Perform a sensitivity analysis of the key hyperparameters $\sigma$, $\tau_g$, and the federation period.
- Include an ablation where all actor/critic parameters are federated (not just velocity-related ones) to justify selective federation.

## Score and Decision
The paper addresses a relevant application but the technical contribution is incremental and the empirical evaluation is insufficiently rigorous for a top venue. The core idea—weighted parameter aggregation based on formation error—is straightforward, and the lack of proper baselines and statistical analysis undermines the validity of the claims.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>