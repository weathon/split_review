## Summary

This paper proposes two conservative variants of Forward-Backward (FB) representations for zero-shot RL—VC-FB and MC-FB—that apply CQL-style regularization to suppress overestimation of out-of-distribution state-action values. On uniformly subsampled 100K-transition datasets from the ExORL benchmark, the conservative variants improve over vanilla FB by 150% (VC-FB) and 137% (MC-FB) in aggregate IQM, and surprisingly outperform the single-task CQL baseline (120% and 111% respectively) despite lacking task-specific reward labels during pre-training, while matching FB performance on full 10M-transition datasets.

## Strengths

- **Clear diagnostic evidence linking OOD overestimation to FB's degradation on small data (Figure 2, Section 3)**: The paper quantifies the overestimation problem directly—showing log Q-values rising as dataset size and quality decrease, which contradicts the actual rollout performance. This grounds the motivation for conservatism in evidence rather than speculation.

- **Ablation comparing three conservative variants reveals mechanistic insight (Table 2, Section 5)**: VC-FB > MC-FB > DVC-FB performance correlates with the degree to which task vectors are drawn from the prior distribution $\mathcal{Z}$ rather than from backward-model-derived $B(s_+)$. This goes beyond black-box comparison and identifies *why* VC-FB works best.

- **Multi-task agent outperforming a single-task CQL baseline (Figure 4)**: VC-FB reaches 120% of CQL's aggregate IQM while lacking task-specific reward labels and maintaining policies for all tasks. This is a non-obvious result—the performance profiles show stochastic dominance over vanilla FB—and it advances the state of the art in zero-shot offline RL.

- **Transparent reporting of limitations**: The paper admits the 3× computational overhead, notes learning instability, discloses that the 150% aggregate gain is heavily driven by the RND dataset (253%), and reports that FB still achieves only 80% of offline TD3. This candor increases credibility.

- **Performance profiles (Figure 4, right) and IQM with bootstrap CIs**: Following best practices (Agarwal et al., 2021), the evaluation uses statistically principled aggregation rather than raw means, making the evidence more reliable.

## Weaknesses

### Major

- **No evidence that the CQL baseline was properly tuned (Section 4.2)**. The paper's headline claim—that a multi-task agent outperforms a single-task analogue—rests entirely on the comparison against CQL. CQL's $\alpha$ hyperparameter is known to be sensitive to dataset quality, yet no hyperparameter search, sensitivity analysis, or tuning procedure is reported for CQL (or offline TD3). Without this detail, the reader cannot assess whether the comparison is fair or whether CQL was run with defaults that are suboptimal for the 100K-transition regime. This weakens the paper's most striking advertised result.

### Minor

- **Mismatch between motivating scenario and experimental evaluation (Section 1 vs. Section 4.1)**. The paper motivates the problem with "real datasets...usually small and lack diversity" produced by "existing controllers" or "task-directed agents" that systematically undersample regions of the state-action space. However, the main experiments uniformly subsample 100K transitions from large exploratory datasets (RND, DIAYN, RANDOM) that were explicitly designed to maximize coverage—preserving the diversity profile of the original data. The didactic example (Section 3.1) does test a systematically narrowed dataset, but it is an extreme caricature (removing all left actions) on a single toy domain. The paper demonstrates that conservatism helps when data is *scarce*, but it does not convincingly test its central motivating claim about structurally *narrow* datasets.

- **Full-dataset results (Table 1) rely on only 3 seeds**, while the paper itself uses 5 seeds for the main 100K experiments. The performance differences on RND ($+2\%$) and DIAYN ($+5\%$) are small enough that 3 seeds provide weak evidence. While the conclusion ("no worse than FB") is likely correct, the statistical support is thinner than it should be.

- **The didactic example (Section 3.1), while useful for intuition, is an extreme intervention** (removing *all* left actions from one action dimension) that does not correspond to any real dataset characteristic. The paper acknowledges it is "engineered for exposition," but this still leaves a gap between the intuitive problem illustration and the actual experimental setup.

### Trivial

- None.

## Nice-to-Haves

- A plot showing the dynamics of the Lagrangian $\alpha$ during training on full vs. small datasets would clarify whether the method is self-regularizing or the conservatism simply becomes negligible on large data.
- Comparing against a broader set of offline RL methods (IQL, BCQ) would strengthen the baseline set, though the current comparison against CQL is the most direct.

## Removed Points

These are flagged to be removed. Treat with caution:

- **"Outperforms task-specific baseline claim is narrower than advertised"** — The paper explicitly defines CQL as the single-task baseline in Section 4.2 and transparently reports FB achieves 80% of TD3. The abstract's phrasing is consistent with the paper's own definitions. This is factually inaccurate as a criticism.
- **"Conceptual gap about CQL substitution being indirect"** — The paper explicitly states "substituting $F(s,a,z)^\top z$ for $Q$ in Equation 7" and the substitution is transparent. The paper does not claim equivalence; it claims adaptation.
- **"Lagrangian $\alpha$ dynamics not described in main text"** — Deferred to appendix, which is standard practice for top-venue papers.
- **"150% aggregate heavily driven by RND"** — The paper transparently decomposes results by dataset and domain in Figure 5 and discusses this directly. Transparency is a strength, not a weakness.
- **"No comparison against other offline RL methods (IQL, BCQ, BRAC)"** — The paper compares against CQL (the most directly relevant conservative method) and offline TD3 (the strongest single-task baseline on ExORL). Adding more baselines is a nice-to-have but not a weakness.

## Novel Insights

The paper's most interesting finding is not merely that conservatism helps FB, but that the *source* of the task vector $z$ in the penalty term determines effectiveness on small datasets. The ablation (Table 2) reveals that VC-FB ($z\sim\mathcal{Z}$) outperforms MC-FB ($z\sim\mathcal{Z},\;B(s_+)$ combined) which outperforms DVC-FB ($z\sim B(s_+)$ entirely). This shows that when data is scarce, the backward model $B(s_+)$ provides poorer task coverage than sampling from the prior $\mathcal{Z}$, a finding that is specific to the FB architecture and not derivable from CQL intuition alone. This is a genuinely insightful diagnostic that future FB work can build on.

## Suggestions

1. Run a hyperparameter sweep for CQL (and report it) or provide a sensitivity analysis showing that the comparison is robust across CQL $\alpha$ values. Alternatively, report the $\alpha$ values used and justify why they are appropriate.
2. Add an experiment that tests the motivating scenario directly: subsample from a near-optimal controller (e.g., a trained TD3 policy's replay buffer) to create a dataset that has narrow coverage concentrated near high-reward regions, and evaluate whether conservative FB still helps.
3. Run the full-dataset experiments (Table 1) with 5 seeds instead of 3 to firm up the statistical evidence for the "no worse than FB" claim.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>