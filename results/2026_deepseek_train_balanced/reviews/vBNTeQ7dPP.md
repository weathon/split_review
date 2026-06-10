## Summary

This paper proposes Lyapunov-based Actor-Critic (LAC), a model-free RL algorithm that enforces a sample-based Lyapunov stability condition as a soft constraint during policy optimization. The method learns a Lyapunov critic function alongside the policy, using either a finite-horizon sum-of-costs or the value function as the Lyapunov candidate. The paper evaluates LAC on CartPole, HalfCheetah, FetchReach, Swimmer, Minitaur, and a synthetic biology gene-regulatory-network (GRN) tracking task, showing that LAC-trained policies are substantially more robust to parametric variations and external disturbances than SAC and SPPO baselines.

## Strengths

- **Consistent and impressive empirical robustness across diverse environments (Section 6.3, Figures 4–6):** Across six domains, LAC policies maintain tracking precision or low cost under parametric variations (pole length, promoter strength), process noise, and periodic impulsive disturbances, where SAC, SPPO, and LQR baselines fail. In CartPole (Figure 4a–b), LAC keeps the pole upright at all varied lengths while SAC fails in every case. In Halfthe disturbance robustness evaluation (Figure 5), LAC achieves lower death rates and cumulative costs than all baselines across a range of disturbance magnitudes. These results are the paper's strongest contribution and provide genuine evidence that enforcing a Lyapunov-style constraint yields policies with better robustness properties.

- **Demonstration on a nontrivial and previously underexplored domain — synthetic biology gene regulatory networks (GRN) (Section 6, Figures 1d, 2, 4c–d, 6):** The GRN repressilator is a 6-dimensional stochastic nonlinear system with oscillatory dynamics where SAC often fails to converge during training (Figure 1d). LAC policies converge reliably, produce state trajectories that track the reference (Figure 2), and generalize to unseen reference signals (sinusoids of periods 150/400, constant references 8/16) where SAC policies fail (Figure 6). This goes beyond standard MuJoCo benchmarks and demonstrates applicability to a qualitatively different control problem.

- **Empirical evidence that the Lagrange multiplier λ converges to zero (Appendix Section S4, Figure S10):** Across all 7 environments, the value of λ drops to zero at convergence, providing an empirical check that the learned policy approximately satisfies the Lyapunov decreasing condition. This bridges the gap between the theoretical condition and the training outcome.

- **Ablation study on Lyapunov candidate choice (Section 6.5, Figure 7):** The paper compares time horizons N ∈ {5, 10, 15, 20, ∞} in CartPole and finds that shorter horizons yield more robust controllers, providing practical guidance for deploying the method.

## Weaknesses

### Major

- **Theorem 1 does not provide a novel, checkable stability condition.** The theorem claims that if (2-2) holds — i.e., E_{s∼μ_π}(E_{s′∼P_π}L(s′)−L(s)) ≤ −α₃ E_{s∼μ_π}c_π(s) — then the system is stable. But the proof (lines 93–113) shows the left-hand side telescopes to lim_{N→∞}(1/N)(E_{P(s|ρ,π,N+1)}L(s)−E_{ρ(s)}L(s)) = 0, reducing the inequality to 0 ≤ −α₃ lim_{t→∞}E c_π(s_t), which forces lim_{t→∞}E c_π(s_t)=0 — i.e., exactly the definition of stability (Definition 1). The Lyapunov function L cancels out entirely; the condition adds no analytical power beyond restating the definition. The claim (lines 121–124) that this is a "novel criterion that can be verified through sampling" is misleading — to verify (2-2) you would need samples from the stationary distribution μ_π = q_π, which requires knowing the closed-loop dynamics or having infinite data from the converged system, the very thing stability is supposed to guarantee. The theorem is mathematically correct but does not deliver the "data-based stability guarantee" promised in the title and abstract.

- **The algorithm uses a sample-based constraint disconnected from the theorem's guarantees.** The constraint in the actual algorithm (Equation 164) replaces the stationary-distribution expectation E_{s∼μ_π} with an empirical average over the replay buffer D, which contains data collected under past policies, not the current policy π_θ's stationary distribution. The paper claims (line 168) that this is "also unbiased estimation" of Theorem 2-2, but this is incorrect unless the replay buffer's state distribution equals μ_{π_θ}, which it does not during off-policy training. No theoretical argument links satisfaction of this empirical constraint to satisfaction of the original stability condition. The Lagrange multiplier method (Equation 171) is a soft penalty — it encourages constraint satisfaction but provides no guarantee, despite the termination condition in Algorithm 1 ("until constraint (164) is satisfied"). The paper's theoretical framing suggests a stability guarantee, but the actual algorithm provides a heuristic that works empirically without the claimed theoretical support.

### Minor

- **Selective evaluation of SAC baselines in robustness tests.** The paper states (line 307): "To make a fair comparison, we removed the policies that did not converge in SAC and only evaluate the ones that perform well during training." This introduces an asymmetry: non-converged LAC runs are not removed (the paper claims LAC always converges), but SAC failures during training are excluded from the robustness comparison. The correct protocol would be to train both methods 10 times and test all resulting policies in varied environments, reporting both the fraction that remain stable and the mean performance across all runs. While this issue actually makes the comparison *conservative* for the paper's claims (SAC looks better than it truly would), it should still be disclosed and ideally addressed.

- **The Lyapunov candidate choice varies across tasks** (different N for CartPole/GRN/CompGRN vs. value function for HalfCheetah/Swimmer/Minitaur), introducing a tuning dimension that SAC does not have. The ablation (Section 6.5) partially addresses this, but the paper does not provide guidance on how to select the candidate a priori or whether the results are sensitive to this choice.

### Trivial

- The paper cites the "Abelian theorem" (line 73) to claim that Cesàro convergence follows from ordinary convergence. This is a standard Cesàro summation result that does not require the Abelian theorem; the reference is imprecise but inconsequential.

## Nice-to-Haves

- An ablation that compares LAC vs. LAC without the Lyapunov constraint (i.e., removing the λ-term) would isolate the effect of the stability condition from the other architectural choices.
- Directly measuring the empirical Lyapunov drift E_D[L_c(s′,a′)−L_c(s,a)+α₃c] during and after training (rather than relying on λ→0 as a proxy) would give a more direct sense of how well the constraint is satisfied.
- A candid acknowledgement of Theorem 1's limitations would strengthen the paper — the value is in using the Lyapunov framing as a learning signal, not in providing a new way to verify stability without dynamics.

## Removed Points

- The harsh critic's claim that the SAC robustness comparison is "cherry-picked" and "inflates the apparent robustness gap": REMOVED because filtering non-converged SAC runs actually makes the comparison MORE conservative for the paper's claims. The criticism is directionally wrong about the effect. The point about protocol transparency is retained as a Minor weakness.
- The harsh critic's point about the theorem's proof needing "completeness regarding what happens when the limit in Definition 1 fails to exist": REMOVED because this is a standard theoretical assumption common to the literature and not a specific flaw of this paper.
- Strength Finder's claim that Theorem 1 "resolves the 'infinity' barrier to using Lyapunov's method in model-free RL": REMOVED because the theorem does not provide a practically checkable condition (see Major weakness above). The strength is retained in adjusted form: the paper provides a Lyapunov-based learning framework that works empirically.

## Novel Insights

None beyond the paper's own contributions. The key insight — that enforcing a sample-based Lyapunov decreasing condition as a constraint in policy optimization yields improved robustness — is the paper's core contribution, and the reviews do not surface a deeper theoretical or methodological observation beyond what the paper already states.

## Suggestions

1. Recalibrate the theoretical claims throughout the paper. Theorem 1 is correct but does not provide a "data-based stability guarantee" that can be verified independently — it should be presented as motivation for the learning signal, not as a verification tool.
2. Address the gap between Theorem 1 and the algorithm by providing (a) a discussion of why the replay buffer approximation is reasonable in practice, and (b) a measure of how well the empirical constraint is actually satisfied.
3. In the robustness evaluation, either test all trained policies (including SAC runs that did not converge during training) or clearly report the convergence rates alongside the robustness results.

**MY FINAL SCORE: <score>5.0</score>**
**MY FINAL DECISION: <decision>Reject</decision>**