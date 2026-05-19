- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 5, 8, 6
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes ASID, a three-stage sim-to-real transfer pipeline: (1) train an exploration policy in simulation by maximizing Fisher information (A-optimal experiment design), (2) deploy it for a single real-world episode and perform optimization-based system identification (REPS/CEM), (3) train a downstream task policy in the refined simulator for zero-shot real-world transfer. The core insight is that exploration policies (which only need to probe informative states) transfer across the sim-to-real gap more reliably than task-specific policies, enabling accurate parameter identification from minimal real-world interaction. The paper evaluates on four manipulation tasks (sphere striking, rod balancing, articulation inference, shuffleboard) in both simulation and on a real Franka robot.

## Strengths

- **Fisher-based exploration produces demonstrably better coverage of informative regions than prior active exploration.** In the multi-friction sphere task (Section 4.2, Figure 3/4), the ASID exploration policy achieves roughly uniform visitation across all friction zones, while the mutual-information-based baseline of Kumar et al. (2019) barely leaves the starting region. This directly validates the claim that Fisher information maximization yields trajectories that excite multiple unknown parameters.

- **Simulation results (Table 1) show ASID's full pipeline significantly outperforms all baselines and ablations on downstream tasks.** On rod balancing, ASID + SysID achieves near-zero tilt error (0.00°–0.72°), versus 4.20°–15.34° for random exploration. On sphere striking, ASID attains 28% success versus ≤11% for every alternative (random exploration, Kumar et al. 2019, domain randomization, and ASID with a learned estimator). The consistent margin across tasks and the ablation replacing optimization-based SysID with a learned estimator (which drops ASID to 11%) isolates the contribution of the full pipeline.

- **Real-robot experiments confirm the pipeline transfers to physical hardware.** On rod balancing (Table 2), ASID succeeds on 6/9 trials across varying mass distributions while domain randomization fails on all 9. On shuffleboard (Table 3), ASID hits the target zone 7/10 times versus 3/10 for domain randomization. These results demonstrate the method is practical on real hardware.

- **The method generalizes beyond physical parameters to structural unknowns such as articulation geometry.** Section 4.2 shows that on the laptop articulation task, ASID's exploration policy interacts with the laptop 80% of the time compared to 20% for a naïve baseline, and the paper notes that downstream articulation inference (e.g., Ditto) succeeds on this collected data.

## Weaknesses

### Fatal
None.

### Major

- **The implementation of Fisher information maximization as a PPO objective is underspecified.** The paper (Section 4.1, line 187) states "we rely on standard policy optimization algorithms, such as PPO" to solve $\argmin_\pi \mathbb{E}_{\theta\sim q_0}[\mathrm{tr}(\mathcal{I}(\theta,\pi)^{-1})]$. However, $\mathrm{tr}(\mathcal{I}(\theta,\pi)^{-1})$ is a non-decomposable function of the trajectory-level Fisher information matrix — it cannot be expressed as a sum of per-timestep rewards in any obvious way. The paper never explains how this quantity is computed from sampled trajectories (e.g., empirical Fisher estimation from a batch of rollouts? episodic reward at the end of each trajectory? per-step approximation?) or how it feeds into the PPO loss. Since this is the paper's central algorithmic contribution — the mechanism by which exploration policies are learned — the omission significantly hinders reproducibility and makes it difficult to verify whether the method is actually implementing the claimed objective. This detail belongs in the main text, not an appendix (which is stripped from this version). 

### Minor

- **The absolute success rate on simulated sphere striking (28%) is low, and the paper does not directly measure identification error.** While ASID's 28% is a substantial relative improvement over the best baseline (≤11%), the task is fully simulated where "real" dynamics are known and the simulator can be perfectly matched. Without reporting parameter estimation error (e.g., RMSE of identified friction), the reader cannot tell whether the 72% failure rate stems from inaccurate system identification (which would undercut the value of Fisher exploration) or from inherent task difficulty/stochasticity (which would not). Reporting identification accuracy directly would strengthen the evidential link between exploration quality and downstream success.

- **The real-world evaluation compares ASID only against domain randomization, not against random exploration or the Kumar et al. baseline.** While simulation experiments already compare against these additional baselines, the real-world experiments alone cannot isolate whether the improvement is due to Fisher-based exploration specifically or simply due to performing *any* system identification after data collection. Including a random exploration baseline in the real world (even with fewer trials) would substantially strengthen the central empirical claim.

- **The rod balancing real-world task uses a static pick-and-place primitive (a single choice of grasp point), not a learned closed-loop policy.** This is structurally simpler than the simulation tasks where PPO-trained policies are used. The paper does not discuss whether the method would scale to real-world tasks requiring multi-step feedback control, and the shuffleboard task similarly uses a single predicted force value. 

- **The finite-difference gradient approximation for non-differentiable simulators (line 186) is mentioned but its computational cost, accuracy, and effect on the learned exploration policy are not assessed.** Since finite differences require multiple forward simulations per state-action pair per parameter dimension, the practical overhead for high-dimensional parameters is unclear.

### Trivial
None.

## Nice-to-Haves

- Report identification accuracy directly (e.g., parameter RMSE) for simulation experiments to complement downstream task metrics.
- Include a random exploration baseline in real-world experiments, even with limited trials.
- Analyze failure cases (e.g., why 3/9 rod-balancing attempts failed; which conditions caused the sphere-striking failures).
- Vary the number of exploration episodes (1, 2, 5) to empirically demonstrate that a single episode suffices.
- Provide some form of confidence bounds for the 1D rod-balancing simulation results (Table 1 already includes ± std for all metrics, which is standard).

## Removed Points

*Criticism about the comparison to Kumar et al. (2019) being "incomplete and potentially misleading":* This criticism misreads the paper. The paper clearly distinguishes between "Kumar et al. 2019" (their full pipeline of exploration + learned estimator) as a row in Table 1, and "ASID + estimator" (ASID exploration + Kumar's learned estimator) as a separate ablation. The baseline is well-disambiguated and the comparison is fair.

*Criticism about theoretical gap between Cramer-Rao bound and REPS/CEM not being an unbiased estimator:* The paper explicitly acknowledges this limitation ("we argue that solving... with this form... is a very intuitive objective"). The Cramer-Rao bound is used as *motivation* for the objective, not as a claim that REPS/CEM achieves it. Every experimental design paper that uses Fisher information as a heuristic faces the same gap; this is not specific to ASID.

*Criticism about not comparing to other active exploration methods (model-based RL):* The paper references this comparison at line 59 ("we show in Section C that these can perform significantly worse") and contains an explicit comparison that was presumably in the appendix (stripped by the parser).

*Criticism that "the central claim — that exploration policies transfer better than task policies — is not formally supported":* This is a qualitative insight presented as motivation, not as a formal theorem claim. The paper's experimental evidence (exploration policies succeeding while DR fails in real-world tasks) provides empirical support for this intuition.

## Novel Insights

None beyond the paper's own contributions. The two reviewers broadly converge on the paper's strengths (Fisher-based exploration coverage, simulation results showing consistent margin over baselines, real-world validation) and weaknesses (underspecified PPO implementation of the Fisher objective, thin real-world baseline set, lack of direct identification error analysis). The harsh critic's attempt to frame the 28% sphere-striking rate as a fatal weakness is undercut by the fact that every baseline sits below 11% — the relative improvement is real even if absolute performance is modest. Similarly, the concern about Kumar et al. baseline conflation is factually incorrect given how clearly the paper distinguishes the two comparisons.

## Suggestions

1. **Specify the Fisher objective implementation.** This is the single highest-impact improvement for the camera-ready version. Describe how $\mathrm{tr}(\mathcal{I}(\theta,\pi)^{-1})$ is computed from trajectory samples, how it is shaped into an objective for PPO (episodic reward, batch-level meta-objective, or per-step approximation), and whether the Fisher matrix is estimated from a single trajectory or a batch. This detail is necessary for the paper's core contribution to be reproducible.

2. **Add direct identification error analysis for simulation experiments.** Report parameter RMSE (or a similar metric) alongside downstream task performance. This would allow readers to verify that Fisher exploration actually reduces parameter estimation error, and to understand whether the 72% sphere-striking failure rate is due to identification error or task stochasticity.

3. **Include at least one additional baseline in real-world experiments.** Testing random exploration (or the ASID + estimator ablation) on the real robot, even with a reduced number of trials, would directly isolate the effect of Fisher-based exploration and address the most significant gap in the real-world evidence.
