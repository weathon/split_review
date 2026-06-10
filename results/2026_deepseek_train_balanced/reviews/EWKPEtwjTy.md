## Summary

This paper proposes a discrete-action actor-critic architecture for continuous RL tasks. Action dimensions are discretized into uniformly-spaced atoms; a stochastic actor outputs per-dimension probability matrices; twin distributional (C51-style) critics are combined with a clipped double-Q procedure adapted to categorical value distributions. The model achieves a mean score of 324.8 on BipedalWalkerHardcore-v3 (claimed highest on the OpenAI Leaderboard as of May 2024) and competitive results on MuJoCo benchmarks.

## Strengths

1. **State-of-the-art result on BipedalWalkerHardcore-v3 with controlled baselines**: The paper reports a mean score of 324.8 over 10,000 evaluation trials (Section 5.2, line 220). Critically, SAC, TD3, and TQC baselines were trained under identical conditions — same environment, same 20-million-step budget, same hardware — providing an apples-to-apples comparison for the paper's main result.

2. **Trap-or-Cheese diagnostic cleanly illustrates a specific algorithmic advantage**: Section 5.1 presents a minimal task where SAC (mean −1.0, always walks into the trap) fails while the discrete model succeeds (mean 0.5). This provides an interpretable demonstration that the discrete action representation avoids the "averaging good actions yields a bad action" failure mode.

3. **Ablation study validates necessity of key components**: Figure 6 (right) ablates the twin critics ("Single Critic") and replaces the discrete actor with a continuous one ("Normal Actor"), showing degraded performance in both cases. This provides causal evidence that both components contribute to the reported performance.

4. **Novel mathematically specified exploration strategy**: Section 4.4 defines a heuristic exploration method (Equations 9–11) that couples action entropy to distributional confidence, with a formalized switch condition based on cumulative probability thresholds.

5. **Principled adaptation of clipped double Q-learning to the distributional setting**: Section 4.2 works through the full procedure — twin categorical critics, cumulative distribution selection via max-of-CDFs, projection onto the atom grid, and cross-entropy training.

## Weaknesses

### Fatal

None.

### Major

1. **Critical experimental details are entirely absent, preventing reproducibility**: The paper does not report the values of any key hyperparameters — the number of action atoms *m*, the number of value atoms *N*, value bounds V_MIN/V_MAX, network architecture (layer sizes, activations), learning rate, batch size, replay buffer size, target update frequency, entropy coefficient *β*, or scaling factor *h*. Furthermore, the number of independent random seeds is never stated for any experiment; only a single mean over evaluation episodes is reported without variance. These omissions mean the experiments cannot be reproduced or fully evaluated.

2. **MuJoCo comparison uses externally reported baseline numbers, not controlled re-runs**: The paper states (Section 5.3, Table 2) that "The data of SAC, TD3, TQC is from (Kuznetsov et al., 2020)." The claim of "comparable results" on MuJoCo is therefore not supported by a controlled experiment where all methods share the same architectures, training timesteps, hyperparameter budgets, and evaluation protocol. The training curves (Figure 7) show only the proposed model's performance with no baseline overlays.

### Minor

1. **Missing variance information for the main BipedalWalkerHardcore-v3 result**: The score of 324.8 is reported as a mean over 10,000 evaluation trials without standard deviation or confidence intervals. Baseline scores from the paper's own controlled runs are in an image-only table without variance. Statistical significance cannot be assessed.

2. **"Trap or Cheese" experiment has limited evidentiary scope**: Only SAC is tested as the continuous baseline (Section 5.1, line 211). SAC with properly tuned temperature can learn to avoid interpolating between modes — this is not a fundamental limitation of continuous action spaces. The paper provides no quantitative analysis linking this toy problem to the actual failure mode in BipedalWalkerHardcore-v3; the connection remains a plausible post-hoc narrative rather than a demonstrated cause.

3. **The max-of-CDFs mechanism is not compared against alternatives**: The paper takes the pointwise max of two CDFs (Section 4.2, Equation 5) as the distributional analog of TD3's min-Q. While the idea is plausible, no justification is given for why this specific operation is the right analog, and no ablation compares it against alternatives (min of CDFs, averaging critics, min of expected values).

4. **No sensitivity analysis of the core design parameter *m***: The number of action atoms *m* is defined (Section 4.1) but never specified numerically, and no experiment analyzes how performance varies with different values of *m*. The same applies to the number of value atoms *N*.

5. **Exploration module is not ablated**: The heuristic exploration strategy (Section 4.4) is a significant method component, but its contribution is never isolated. The ablation study (Figure 6 right) only tests twin critics and the discrete actor.

6. **Policy update may collapse the value distribution**: The actor update (Section 4.3, Equation 7) pushes cumulative probability toward 0 for all lower atoms, which in principle drives all probability mass to the highest atom *z_N*. The paper does not discuss whether this causes instability or whether the exploration mechanism adequately counteracts it.

### Trivial

None.

## Nice-to-Haves

- Report results with variance across at least 5 independent seeds.
- Run all MuJoCo baselines under identical controlled conditions, or clearly delimit the MuJoCo results as preliminary/incomplete.
- Add an ablation comparing max-of-CDFs against min-of-CDFs and critic averaging.
- Add a sensitivity analysis of action granularity *m*.
- Isolate the exploration module in an ablation experiment.

## Removed Points

The following points from the reviewer inputs were removed with justification:

- **Garbled gradient expression (line 133)**: Flagged by the harsh critic as a garbled equation. Per filtering rules, formatting artifacts from PDF extraction are parser errors, not author errors.
- **"Text never states numerical baseline scores" for BipedalWalker**: Table 1 is an embedded image in the original submission; text extraction cannot read it. The table exists in the paper.
- **Criticism that "Normal Actor" ablation may confound comparison**: The paper states this ablation uses the paper's own twin critic network (line 229), so the comparison cleanly isolates the actor component. The concern is addressed in the paper.
- **Generic area-of-concern sweep criticisms** lacking concrete anchors in the paper's content (e.g., "could the metric be measuring a proxy?").
- **Strength Finder's generic/superficial strengths** that were not backed by specific evidence (e.g., "addresses an important problem").

## Novel Insights

The most revealing synthesis across the reviews is the tension between the paper's genuine conceptual novelty and its lack of experimental rigor. The discrete-action + distributional-critic combination is a genuinely interesting design, and the BipedalWalkerHardcore-v3 result is impressive. However, the failure to report basic experimental parameters (m, N, seeds, hyperparameters) means the work cannot currently be evaluated as rigorous science. The "Trap or Cheese" diagnostic is evocative but the reviews collectively reveal it conflates two issues: (1) the interpolation problem in continuous action spaces (which is real), and (2) the role of distributional critics vs. scalar critics in handling multimodal returns — the paper's main success likely comes from the combination of both mechanisms acting together, not from action discretization alone.

## Suggestions

1. Report all hyperparameters (m, N, V_MIN/V_MAX, network architecture, learning rates, batch sizes, β, h, target update frequency) in a dedicated table.
2. Run all MuJoCo baselines under controlled conditions, or clearly demarcate the MuJoCo results as preliminary.
3. Report means and variances across at least 5 independent seeds for all experiments.
4. Add an ablation comparing the max-of-CDFs operation against min-of-CDFs and critic averaging.
5. Add a sensitivity analysis of action granularity m across a range of values (e.g., 3, 5, 10, 21).
6. Isolate the exploration module in an ablation experiment.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>