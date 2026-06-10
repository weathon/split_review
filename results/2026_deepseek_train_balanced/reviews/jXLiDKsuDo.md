## Summary

SimBa proposes a three-component architecture (RSNorm, residual feedforward blocks with pre-layer normalization, post-layer normalization) designed to inject simplicity bias into deep RL networks, enabling effective parameter scaling. The paper's strongest evidence is a controlled scaling experiment (Figure 1b) showing SAC+SimBa's performance improves monotonically with network width (0.1M→17M parameters) while SAC+MLP degrades, supported by a 51-task benchmark across three RL paradigms.

## Strengths

1. **Controlled scaling experiment directly tying architecture to scalability** (Figure 1b, lines 48–57): Varying network width from 0.1M to 17M parameters shows SAC+SimBa consistently improves while SAC+MLP degrades. This is the paper's cleanest evidence that the architecture — not the algorithm — enables scaling.

2. **Fourier-based quantification linking simplicity bias to performance** (Figure 4, Section 4.1): The paper measures simplicity scores for each architectural component and shows a monotonic relationship: higher simplicity scores correlate with higher returns (residuals +50pts, layer norm +150pts, all components +550pts). This provides a mechanistic explanation for why SimBa works, backed by 100 random initializations and 10 seeds.

3. **Replay-ratio scaling without periodic resets** (Section 6.3, Figure 10): SimBa's performance improves monotonically with replay ratio (2, 4, 8, 16) even without periodic resets — a regime where BRO fails without resets — and with resets outperforms BRO at RR10. This is a genuinely novel finding that goes beyond prior work.

4. **Systematic observation normalization ablation** (Section 6.1, Figure 8): RSNorm is compared against 5 alternatives (LayerNorm, BatchNorm, env-wrapper RSNorm, fixed initial statistics, oracle statistics). Only RSNorm matches oracle performance, and the paper provides a clear explanation for why env-wrapper RSNorm underperforms (inconsistent statistics in off-policy replay buffer).

5. **Actor vs. critic scaling analysis** (Section 6.2, Figure 9): Isolates scaling width vs. depth for actor and critic separately, showing critic width scaling is effective while actor scaling is not, with a mechanistic explanation (depth adds non-linear components that reduce simplicity bias). This yields actionable design guidance.

## Weaknesses

### Fatal

None.

### Major

1. **No aggregate numerical results table for the 51-task benchmark**: The paper's headline claim — that SAC+SimBa "matches or surpasses state-of-the-art off-policy RL methods across 51 continuous control tasks" — is supported only by a scatter plot (Figure off_policy_scatter) plotting per-task performance against computation time. There are no tables reporting mean returns, IQM, median scores, or win rates across task categories. The commented-out text (lines 234–244) mentions plans to report IQM and mean scores using the RLiable package, but the actual paper delivers no such aggregates. Without them, the reader cannot assess the *magnitude* of SimBa's advantage, the variance, or the consistency of improvement across DMC, MyoSuite, and HumanoidBench. The scatter plot shows distributional information but does not substitute for precise aggregate reporting. This is the single most significant gap in the paper's evaluation.

### Minor

2. **Thin on-policy and unsupervised RL experiments**: The on-policy evaluation (Section 5.2) uses only one environment (Craftax) with one baseline (PPO+MLP). The unsupervised RL evaluation (Section 5.3) uses only one task (DMC Humanoid) with one baseline (METRA). Neither compares against alternative architectures (e.g., PPO+LayerNorm, PPO+BRO, or additional unsupervised methods). The claim of broad applicability "across three RL paradigms" is weakened by the limited depth of two of the three paradigms.

3. **No documentation of SimBa's hyperparameter selection**: The paper states (line 232) that baselines use "the authors' reported results or run experiments using their recommended hyperparameters," but does not explain how SimBa's own architecture hyperparameters (width, depth, hidden dimension, learning rate) were chosen. The default setup (actor depth=1, critic depth=2, actor width=128, critic width=512) appears in the ablation section but without any record of how these defaults were determined. If SimBa's hyperparameters were tuned on DMC-Hard and then reported on the same tasks, the comparison against baselines using default hyperparameters may not be fair.

4. **"Strongly correlated" claim lacks a correlation coefficient or significance test**: Line 213 states "the scalability of each architecture was strongly correlated with its simplicity bias score" without providing any quantitative correlation measure (e.g., Spearman's ρ, Pearson's r) or significance test. Given RL's high variance, formal significance testing would strengthen this claim.

5. **Main BRO comparison uses the weaker variant without sufficient framing**: The primary off-policy benchmark (Figure off_policy_scatter) compares against BRO-Fast (replay ratio 2) and justifies this as compute-fair. The ablation (Section 3.5) does compare against BRO at RR10, but the main text's framing ("matches or surpasses SOTA") does not make sufficiently clear that the primary comparison uses a compute-matched weaker variant of BRO. The later ablation shows SimBa outperforms BRO at RR10, but the main text should be more explicit.

### Trivial

None.

## Nice-to-Haves

- Adding per-task error bars or uncertainty markers to the scatter plot would improve interpretability.
- Extending on-policy and unsupervised evaluations to 2–3 environments each with at least one additional baseline architecture would substantially strengthen the breadth claim.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Variance update formula error (Harsh Critic)**: The critic claimed the Welford update formula (line 150: σ_t² = (t-1)/t (σ_{t-1}² + (1/t)δ_t²)) has an error. Verifying against the standard Welford update shows the paper's factorization is mathematically equivalent. **Removed as factually wrong.**

- **Simplicity bias 2D measurement limitation (Harsh Critic)**: The critic argued the Fourier measurement on 2D inputs does not generalize to high-dimensional RL observations. However, the paper empirically validates the correlation against actual RL performance (Figure 4b), which is the relevant check. The 2D measurement follows the established methodology of Teney et al. (2024). **Removed because the paper partially addresses this through empirical validation.**

- **"Bitter Lesson" framing is grandiose / overclaims novelty (Harsh Critic)**: Subjective opinion about appropriate framing, not a substantive weakness connected to any specific experiment or result. **Removed as subjective framing concern.**

- **Spectral normalization cost characterization (Harsh Critic)**: The critic disagreed with the paper's characterization that spectral normalization is "computationally intensive." This is a subjective assessment and not tied to a specific experimental claim. **Removed.**

- **Generic strengths about "important problem" / "interesting question" (Strength Finder)**: Dropped as generic/superficial. Only concrete, evidence-backed strengths retained.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a numerical results table** with mean, median, IQM, and 95% stratified bootstrap CIs per benchmark (DMC-Easy&Medium, DMC-Hard, MyoSuite, HumanoidBench) using the RLiable methodology. This is the single highest-leverage improvement and directly addresses the major weakness.

2. **Document hyperparameter selection** for SimBa: state whether architecture hyperparameters were fixed across all tasks or tuned, and if tuned, on which tasks and how extensively.

3. **Add a correlation coefficient** (e.g., Spearman's ρ) for the simplicity bias vs. performance relationship in Figure 4b, with a significance test.

4. **Clarify the BRO comparison framing**: explicitly state in the main results section that the primary comparison uses BRO-Fast (RR2) for compute fairness, and cross-reference the ablation showing SimBa outperforms BRO at RR10.

5. **Expand on-policy and unsupervised evaluations** with at least one additional environment each and at least one additional baseline to strengthen the breadth claim.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>