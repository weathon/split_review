## Summary

The paper proposes IWOCS (Incremental Worst-Case Search), a meta-algorithm that decomposes robust MDPs into a sequence of non-robust (static) RL problems. Under sa-rectangularity and stationary policies, the static and dynamic models are equivalent. IWOCS exploits this by incrementally identifying worst-case transition models, solving a standard MDP for each, and combining their value functions via a pointwise min. A deep RL instantiation using SAC + CMA-ES/grid search is evaluated on MuJoCo benchmarks, reporting competitive normalized worst-case scores.

## Strengths

- **Clean conceptual framework for decoupling robustness into static subproblems**: The insight that robust MDPs can be solved via a sequence of non-robust solves (using the static/dynamic equivalence and no-duality-gap property) is well-motivated and clearly presented. The meta-algorithm design makes it applicable to any RL solver, and the algorithmic description (Algorithm 1) is precise.

- **Non-trivial convergence guarantee for a non-contractive method**: Property 2 (lines 203–208) proves the Q_i sequence is monotonically decreasing and bounded below by Q*_𝒯, guaranteeing convergence even though IWOCS is not a Bellman contraction. This is a meaningful formal property for an algorithm not based on robust Bellman backups.

- **Competitive empirical results across multiple benchmarks**: IWOCS* achieves the highest aggregate normalized worst-case score (2.04 ± 0.11 vs M2TD3's 1.0 ± 0.13) and outperforms all baselines on 7/11 environments for worst-case performance (Table 1). On average performance (Table 2), IWOCS* achieves 3.13 aggregate vs M2TD3's 0.45.

- **Practical handling of out-of-distribution Q-function values**: The predictive-coding-based indicator function (lines 282–287) addresses the problem that different Q_{T_j} networks are trained on different replay-buffer distributions, preventing extrapolation errors in unseen state regions. This is a concrete practical contribution that prior work (M2TD3, M3DDPG) does not address.

- **Explicit complexity comparison with RVI**: The analysis (lines 248–256) formalizes when IWOCS can be computationally advantageous — when the per-state-action cost c of min_T is large, IWOCS replaces expensive robust Bellman backups with cheaper per-state min_T solves (O(M(n_S² n_A log(1/ε)/log(1-γ) + c n_S n_A)) vs O(c n_S² n_A log(1/ε)/log(1-γ))).

## Weaknesses

### Fatal
None.

### Major

- **No raw (unnormalized) scores reported anywhere in the paper.** All results in Tables 1 and 2 are normalized as (v−v_TD3)/|v_M2TD3−v_TD3|, which by construction sets M2TD3 to 1.0 and TD3 to 0.0 on every environment. Without raw scores, the reader cannot assess the absolute scale of the improvements. The normalization denominator varies per environment, and the aggregate "2.04-fold improvement... over M2TD3" (line 333) is a ratio of normalized scores, not an absolute performance ratio — the phrasing is misleading. This omission makes a central empirical claim unverifiable from the data presented.

- **The theoretical framework relies on sa-rectangularity, but the main MuJoCo experiments explicitly violate it.** The entire theoretical motivation — static/dynamic equivalence, no-duality gap, the min-max reformulation — depends on sa-rectangular uncertainty sets (Section 2). A footnote on line 303 states the MuJoCo environments "do not respect the rectangularity assumption," but the paper provides no discussion of what happens to IWOCS's guarantees or behavior under non-rectangular uncertainty, why the method should still be expected to work, or what the Q_i bound means in this regime. This creates a structural gap between the theoretical motivation and the empirical evaluation.

- **Near-zero standard errors on several environments are unexplained.** On InvertedPendulum 2D, IWOCS* shows 2.82 ± 0.00 across 10 random seeds (Table 1). On Hopper 2D, IWOCS* shows 6.52 ± 0.01. These values involve SAC training, CMA-ES optimization, and Monte Carlo rollouts — zero or near-zero variance across seeds is unusual for deep RL and requires an explanation (e.g., whether this is an artifact of normalization, whether the task is extremely stable, or whether seed variation was limited).

### Minor

- **Imprecise phrasing of the headline result.** Line 333 states "IWOCS* permits a 2.04-fold improvement... over the state-of-the-art M2TD3." Since M2TD3 is fixed at 1.0 by construction, a score of 2.04 means IWOCS* improves over TD3 by 2.04× *as much as* M2TD3 improves over TD3 — not that IWOCS* is 2.04× better than M2TD3 in absolute performance. The metric is clearly defined (lines 323–327), but the "over M2TD3" phrasing invites misinterpretation.

- **The predictive coding threshold ρ_j is never specified or ablated.** Line 285 cuts off mid-sentence ("details about tuning ρ_j") with no sensitivity analysis. This threshold controls which (s,a) pairs each Q-function is considered valid for, making it a consequential design choice whose impact is unexamined.

- **Substantive discussion is left in commented-out (\iffalse) blocks.** Lines 430–437 (ablation narrative), 441–449 (convergence tracking), and 463–476 (variance exploration) are all wrapped in \iffalse and absent from the submission. While the numerical comparison between IWOCS (CMA-ES) and IWOCS* (grid search) *is* present in Tables 1 and 2, the associated qualitative discussion and convergence analysis are missing. These sections contain relevant analysis that should be active.

- **On 4/10 seeds for Humanoid Standup 2, IWOCS terminates after one iteration** because the worst-case MDP found for π₁ is identical to T₁ (Table 2, seeds 6–9). The paper discusses this (lines 458–461), but it limits exploration of the uncertainty set for a substantial fraction of runs, going against the central motivation of iteratively covering worst-case models.

- **Q_i is proven to be an upper bound on the true robust value function** (Property 1: Q_i ≥ Q*_𝒯̃_i ≥ Q*_𝒯), meaning the candidate policy may be *overly optimistic* about its robustness. The paper acknowledges this but does not discuss practical implications or how large this gap might be in the empirical results.

### Trivial
- Line 76 has a spurious closing brace after the no-duality gap equation — a formatting artifact.
- The complexity analysis (lines 248–256) places its caveats in the active text, which is proper.

## Nice-to-Haves
- Reporting raw scores alongside normalized scores would resolve the most significant evaluation concern.
- Ablating the ρ_j threshold for the predictive coding indicator would strengthen confidence in the method's robustness to this choice.
- A controlled experiment under sa-rectangularity (beyond the toy Windy Walk) would help bridge theory and practice.
- A brief discussion of why the method might work without sa-rectangularity would address the theory-evaluation gap.

## Removed Points
These points were flagged by reviewers but are removed or demoted after cross-checking against the paper; treat them with caution:

- *"Ablation study results are not actually provided"* — the numerical comparison between IWOCS (CMA-ES) and IWOCS* (grid search) IS present in Tables 1 and 2. The commented-out text was narrative only. Demoted.
- *"Baselines not re-run by the authors"* — This is standard practice for benchmarking against published methods when sample budgets are aligned. Removed.
- *"No statistical significance testing"* — Not standard for deep RL benchmark papers of this type. Removed.
- *"Complexity argument does not carry over to deep RL"* — The paper itself notes (line 251) that comparisons "should be taken with a grain of salt." Demoted.
- *"Choosing T_{i+1} is acknowledged to be a heuristic prone to failure"* — This is self-disclosed in the paper (lines 211–218), not a hidden weakness. Removed.
- *Strength Finder: "Empirical dominance over prior robust RL methods"* — Tempered by normalization concerns; kept as "competitive empirical results" rather than "dominance." Removed from strengths.
- *Strength Finder: "Versatility through algorithm-agnostic design"* — Generic property of any meta-algorithm. Removed as a strength.

## Novel Insights
None beyond the paper's own contributions. The core insight — that robust MDPs can be solved by incrementally building a discrete set of candidate worst-case MDPs and solving each as a standard (non-robust) problem — is the paper's primary contribution. The reviews surface a gap between clean theory (under rectangularity) and practically-relevant evaluation (where rectangularity is violated), and identify evaluation transparency issues, but do not introduce genuinely novel analyses beyond what the paper provides.

## Suggestions
1. **Report raw (unnormalized) worst-case scores** alongside the normalized scores for all methods and environments. This single change would address the most significant weakness in the evaluation.
2. **Add a discussion of the rectangularity gap**: explain what the method's guarantees are (or are not) when the uncertainty set is not sa-rectangular, and why the approach can still be expected to work.
3. **Explain the near-zero variance** on InvertedPendulum 2D and Hopper 2D. Clarify whether the ± values are standard deviation or standard error, and discuss the experimental factors that produce this stability.
4. **Activate the commented-out sections** — the ablation discussion, convergence tracking, and variance exploration are substantive and would strengthen the paper.
5. **Specify and ablate the ρ_j threshold** used in the predictive coding indicator function.
6. **Rephrase "2.04-fold improvement over M2TD3"** to more precisely reflect what the normalized metric captures.

## Score and Decision
MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>