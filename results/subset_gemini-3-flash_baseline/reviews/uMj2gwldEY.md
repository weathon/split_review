## Summary
The paper proposes a Federated Deep Reinforcement Learning (FLDRL) framework for multi-UAV coordination in wildfire tracking. It introduces a performance-weighted federated aggregation scheme for the Deep Deterministic Policy Gradient (DDPG) algorithm, where model updates from UAVs maintaining better formation stability are prioritized. The method specifically federates parameters related to velocity and control gains to handle the non-IID data distributions caused by asymmetric wildfire fronts.

## Strengths
- The research addresses a high-impact real-world problem (wildfire tracking) where decentralized coordination and data privacy/bandwidth are practical constraints.
- The introduction of a performance-weighted aggregation scheme (Equation 12) is a sensible adaptation of Federated Learning for multi-agent control, moving beyond simple parameter averaging to reward-based weighting.
- The use of a realistic wildfire propagation model (FARSITE) calibrated with historical data (Kilmore East fire) adds empirical weight to the simulation results.
- The selective federation strategy—focusing on velocity and control gain parameters—demonstrates a targeted approach to solving the specific problem of inter-UAV spacing.

## Weaknesses
### Major
- **Lack of Baselines:** The paper only compares the proposed FL-DDPG against independent DDPG. It lacks comparisons against established Multi-Agent RL (MARL) algorithms designed for coordination, such as MADDPG or MAPPO. While the authors mention VDN, they do not provide a quantitative comparison.
- **Limited Evaluation Metrics:** The evaluation relies heavily on cumulative rewards and a single snapshot of inter-UAV distances. More robust metrics for formation control (e.g., time-to-formation, success rate under varying wind speeds, or communication overhead analysis) are missing.
- **Clarity on Training vs. Execution:** The paper is slightly ambiguous regarding whether the federated aggregation happens during an offline training phase or during real-time "online" adaptation. If it is online, the impact of communication latency and synchronization on the low-level control loop is not discussed.

### Minor
- **Sensitivity Analysis:** The performance-weighted scheme depends on a scaling parameter $\sigma$. The paper does not provide a sensitivity analysis on how different values of $\sigma$ affect convergence or stability.
- **Reward Function Complexity:** The reward function (Equation 10) contains multiple components ($\gamma_1, \gamma_2, \gamma_3$). While the authors state these are "empirically tuned," the paper would benefit from a brief discussion on the stability of the learning process given these competing objectives.

## Nice-to-Haves
- A visualization of the "asymmetric" fire front evolution over a longer time horizon to better demonstrate how the weighted aggregation handles non-IID data.
- Discussion on the scalability limit (e.g., testing with 10 or 20 UAVs).

## Novel Insights
The primary novel insight is the application of performance-weighted federated aggregation specifically to the control-gain and velocity-related parameters of a DRL policy. By identifying that formation stability in asymmetric environments is primarily a function of velocity regulation, the authors show that selective parameter federation can stabilize multi-agent systems where standard independent learning fails. This bridges the gap between decentralized RL and cooperative control by using the FL server as a "soft" coordinator rather than a centralized trainer.

## Suggestions
- Include a comparison with MADDPG to demonstrate that the FL approach offers benefits (like communication efficiency or robustness to non-IID data) over standard centralized-training-decentralized-execution (CTDE) methods.
- Provide a plot showing the variance of the weights $w_i$ over time to illustrate how the server shifts its "trust" between different UAVs as the fire front evolves.

## Score and Decision
The paper presents a sound and well-motivated application of FLDRL to a complex robotics task. The performance-weighted aggregation is a meaningful contribution to the MARL/FL literature. While the baseline comparison is narrow, the results are promising and the problem setting is highly relevant to the ICLR community.

MY FINAL SCORE: 6.0
MY FINAL DECISION: Accept