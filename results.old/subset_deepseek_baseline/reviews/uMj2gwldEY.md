## Summary

This paper proposes a federated deep reinforcement learning framework (FL-DDPG) for multi-UAV formation control in dynamic wildfire tracking. It augments the DDPG algorithm with a performance-weighted federated averaging scheme that prioritizes model parameters from UAVs that maintain better formation stability. Simulations with three and five UAVs show that FL-DDPG improves formation uniformity (2.5 m spacing variance vs. 14 m) and average episode reward (−122.21 vs. −355.45) compared to standard independent DDPG.

## Strengths

- **Relevant and practically motivated problem** – Multi-UAV coordination for wildfire monitoring is an important and timely application area.
- **Novel weighted aggregation design** – The idea of using formation deviation to weight federated model updates is clever and directly addresses the non-IID challenge arising from asymmetric fire fronts.
- **Clear architectural decomposition** – The separation of high-level DDPG planner and low-level controller, along with selective federation of only velocity-related parameters, is well described and motivated.
- **Quantitative performance advantage** – The results show a large reduction in spacing variance and a notable improvement in average reward compared to standard DDPG, suggesting the method provides meaningful gains.

## Weaknesses

### Fatal
None.

### Major

1. **Insufficient baselines** – The paper compares only against independent DDPG. No comparison is made with other multi-agent RL algorithms such as MADDPG, QMIX, VDN, or even a standard FedAvg version of FL-DDPG. Without these, it is impossible to determine whether the claimed improvements come from the federated framework, the performance-weighted aggregation, or simply from having more training data. This is the most critical weakness.

2. **Lack of ablation study** – The paper does not isolate the contribution of the performance-weighted aggregation from the base FL-DDPG. A comparison against FL-DDPG with equal-weight FedAvg is essential to validate the core claim. The weight formula (Eq. 12) uses the same spacing error that already appears in the reward (Eq. 10), creating a potential double-counting effect that is not discussed.

3. **Limited experimental rigor** – The paper reports results from a single run (no mention of random seeds, confidence intervals, or multiple trials). The simulation time is very short (10 s for 3 UAVs, 20 s for 5 UAVs). The fire front model is described as being based on FARSITE, but the actual simulation uses a level-set propagation with a constant spread rate and an assumed wind angle; the connection to real data is unclear. The absence of these details weakens the reliability of the conclusions.

4. **Overstated claims** – The paper states that FL-DDPG “significantly outperforms” DDPG and enables “real-time, large-scale coordination”, yet the experiments are limited to small numbers of UAVs (3 and 5) over short durations in a simplified 2D setting. Scalability to tens or hundreds of UAVs in realistic conditions is not demonstrated. Communication costs and aggregation frequency are not quantified.

### Minor

- The motivation for federating only velocity-related parameters (θᵢ,ᵥ and θᵢ,ₖᵥ) is plausible but not empirically justified. The heading controller parameters (K_φ) could also affect spacing, and their exclusion should be discussed or ablated.
- The reward function includes a large penalty for entering burned areas (C = 100), but the curves in Figures 4 and 6 are normalized to [0,1] – the relationship between normalized curves and raw reward values is not explained, making it hard to interpret the trajectories.
- Table 2 reports inter-UAV distances that are all around 90–111 m for a fire front that appears to have a radius of ~50 m (from Figure 3 axes of ±100 m). The desired formation spacing is not given, so the reader cannot assess whether these distances are reasonable.
- A remark in Section 3 provides high-level motivations for federated learning (implicit regularization, variance reduction) but no theoretical justification specific to the proposed weighting scheme.

### Trivial
None.

## Nice-to-Haves

- Compare against at least one modern multi-agent RL algorithm (e.g., MADDPG) to contextualize performance.
- Add an ablation: FL-DDPG with equal-weight FedAvg vs. the proposed weighted version.
- Report results over multiple random seeds (≥5) with error bars.
- Provide the desired formation spacing value and explain how it is chosen relative to the fire front size.
- Discuss communication overhead (number of aggregation rounds, bytes transmitted) and any latency implications for real-time control.

## Novel Insights

None beyond the paper’s own contributions.

## Suggestions

- Repeat all experiments with 5–10 random seeds and report means and standard deviations for inter-UAV distance variance and average reward.
- Include an ablation that replaces the performance-weighted aggregation (Eq. 12) with standard FedAvg to isolate the benefit of the weighting scheme.
- Compare against an established multi-agent RL baseline (e.g., MADDPG that shares a centralized critic) under the same environment settings.
- Clarify the fire model: explicitly state whether the level-set simulation uses the FARSITE-derived spread rate continuously or whether FARSITE provides only initial conditions.
- Report the desired formation spacing and justify why uniform spacing is the optimal coverage strategy for asymmetric fire fronts.

## Score and Decision

**Score: 4 (borderline reject)**  

**Decision: Reject**

The paper addresses an interesting and practical problem and proposes a sensible architectural extension. However, the experimental validation is insufficient to support the claimed superiority: only one weak baseline is used, no ablation is performed, and the empirical setup lacks the statistical rigor expected for a top-tier venue (single run, short simulation, limited scale). The core idea of performance-weighted aggregation may have merit, but the paper needs substantially stronger evidence (multiple baselines, ablations, uncertainty quantification) before it can be accepted.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>