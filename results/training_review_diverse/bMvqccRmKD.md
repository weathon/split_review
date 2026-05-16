I have thoroughly verified the reviewer's claims against the paper. Let me now synthesize the final consolidated review.

## Summary

This paper studies RL generalization under both distribution shifts and state/action space expansions — a broader setting than prior work that typically assumes fixed state/action spaces. The proposed CSR framework uses a world model augmented with causal structural masks (D matrices) and a domain-specific change factor (θ), together with a three-step self-adaptive strategy that (1) detects whether the environment change is a distribution shift or a space expansion, (2) expands the causal graph with new variables if needed, and (3) prunes irrelevant variables via causal graph pruning. Theoretical identifiability results (Theorems 1–3, Corollary) provide formal grounding. Experiments on simulated environments, CartPole, CoinRun, and 5 Atari games show CSR outperforming baselines including Dreamer, AdaRL, SPR, and EfficientZero.

## Strengths

- **Explicit formulation and handling of state/action space expansion in RL generalization.** The paper identifies a gap in prior transfer RL — most methods assume fixed state/action spaces — and formally defines space expansions alongside distribution shifts. The CartPole results (Table 1) provide concrete evidence: CSR achieves perfect 500.0 scores on all four tasks (including Task 3 where friction is added as a new state variable and Task 4 where the action space expands), while AdaRL (the strongest baseline) scores only 410.0 on Task 3 and 407.5 on Task 4, and is marked as failing to adapt within limited steps.

- **Theoretical identifiability guarantees for the learned causal model under three scenarios.** The paper provides component-wise identifiability theorems for the source world model (Thm 1), for the domain-specific factor θ_i under distribution shifts (Thm 2), for newly added state variables under space expansions (Thm 3), and for simultaneous shifts (Corollary 4). These theorems distinguish the framework from purely heuristic adaptation methods.

- **Self-adaptive expansion strategy (SA) outperforms fixed or random expansion.** The ablation study (Fig. 4d) shows SA yielding the highest normalized average training episodic return across all environments, demonstrating that the algorithm's design for autonomously determining expansion size is effective.

- **Ablation confirming the benefit of explicit causal structure (D matrices).** Fig. 4c shows that removing the structural masks D from the world model leads to slower and lower cumulative reward in Atari games, isolating the contribution of the causal graph pruning step.

- **Clear problem motivation with a real-world analogy.** The CoinRun difficulty progression (Fig. 1) effectively illustrates the distinction between distribution shifts (obstacle/background changes) and space expansions (new enemies), making the two-scenario taxonomy easy to understand.

## Weaknesses

### Fatal
None.

### Major

- **Ambiguity in the evaluation protocol undermines interpretability of the empirical claims.** The "Minimum Adaptation Steps" metric in CartPole (Table 1) is confusing: Dreamer achieves a score of 397.6 on Task 2 and 311.6 on Task 3 — non-trivial scores — yet is marked with \XSolidBrush ("fails to adapt"). The paper never defines what constitutes successful adaptation versus mere score achievement. For Atari, the paper states "We then train these models on the source task and generalize them to downstream target tasks" without specifying whether baselines received any fine-tuning on target tasks, or whether they were evaluated zero-shot (which would make the comparison with CSR's three-step adaptation unfair). This lack of clarity weakens the evidence for CSR's claimed advantages. The paper would be substantially stronger with a clear, equalized adaptation protocol for all methods and learning curves for CartPole analogous to those shown for CoinRun.

- **Gap between theoretical identifiability results and practical implementation.** Theorem 2 explicitly assumes linear additive transitions (matrix form: s_t = A s_{t-1} + B a_{t-1} + C θ_i^s + ε^s_t), while the practical CSR algorithm uses a neural network world model (p_β) trained via variational inference. Theorem 3 requires newly added variables to be differentiable functions of [o_t, r_{t+1}], but the method does not enforce this constraint. The paper does not discuss which assumptions are violated in practice or why the neural approximation might still recover identifiable representations. This disconnect makes the theory section feel decoupled from the method rather than providing actionable guarantees.

- **Limited evaluation scope on Atari.** Only 5 out of 26 Atari games are tested. The paper calls these "representative" but provides no justification for the selection. Given that mode/difficulty variations across all 26 games would be the natural benchmark for the paper's claims about distribution shifts and space expansions, this narrow evaluation limits the generality of the empirical conclusions.

### Minor

- **Detection threshold sensitivity unanalyzed.** The threshold τ^★ is set as "the final prediction loss of the model on the source task M_1" — a single scalar from one model fit. Its variability across seeds and its robustness to changes in model capacity are not studied. A slight shift could cause misclassification between distribution shift and space expansion, which is the core decision the method relies on.

- **Computational cost of SA expansion acknowledged but unquantified.** The paper admits "each search step requires extensive training time, making the search process highly time-consuming" but reports no wall-clock time, number of search steps required per task, or comparison to non-expansion baselines in terms of total computation. This is relevant to the claim of "low-cost policy transfer."

- **Number of random seeds not reported.** Standard deviations are given for CartPole and Atari (Table 1, Table 2), but the number of seeds is never stated. The zero-variance entries (CSR at 500.0 ± 0.0 across all four CartPole tasks) suggest a ceiling effect; without seed counts it is unclear how reliable these numbers are.

- **Action space expansion handling is under-specified.** The paper says "Given that the action variables are observable, we can directly obtain the relevant information when the action space expands" but does not detail architectural changes: how the action embedding layer is expanded, whether D^{a→s} structural matrices are extended, or whether this expansion is detected automatically or requires manual specification.

- **Binary mask estimation process lacks precision.** The regularization term J_reg pushes D entries toward zero via L1 penalty, and the paper states "the presence of J_reg induces certain entries of D to transition from 1 to 0 during model estimation." It is unclear whether hard-thresholding is applied post-training or whether the masks are implicitly thresholded via optimization. This matters for whether pruning is truly a hard structural change or a soft weighting.

### Trivial
None.

## Nice-to-Haves

- A sensitivity analysis of the detection threshold τ^★ (e.g., relative increase in prediction loss rather than absolute value).
- Learning curves for CartPoe comparable to those shown for CoinRun, so the "Minimum Adaptation Steps" metric can be visually verified.
- An analysis of the learned causal graphs for a simple environment (e.g., CartPole friction addition) to demonstrate that the pruning retains task-relevant variables.
- Reporting of computational cost (wall-clock time, search steps) for the SA expansion strategy.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Baselines were evaluated zero-shot"** — The harsh critic claims baselines were given zero adaptation steps while CSR received fine-tuning. This is not supported by the paper. AdaRL explicitly shows 4k adaptation steps on CartPole Task 2, and all baselines have non-trivial scores on target tasks, indicating they received some form of adaptation. The critic's stronger claim of "almost certainly unfair" is an overstatement. The real issue is lack of clarity in the protocol, which is preserved as a Major weakness above.

- **"Hyperparameters and implementation details entirely absent"** — The harsh critic notes these are missing from the main text, but this is standard practice when an appendix (stripped by the parser) contains them. The paper references Algorithm \ref{alg:framework} which would be in the appendix.

- **"Code availability not stated"** — This is a reproducibility wishlist item, not a methodological weakness.

- **"Number of random seeds not reported"** — Kept in Minor above (it is a genuine omission), so listed here only for the stronger version of this criticism.

- **"The paper does not discuss nonstationary changes"** — The paper explicitly acknowledges this as a limitation in the conclusion (Section 6). This is a deliberate scope choice, not a weakness.

- **"Dreamer achieves 397.6 on Task 2 — how can it fail to adapt?"** — The underlying concern (unclear metric) is preserved in Major above. The specific framing as a contradiction is softened: the \XSolidBrush denotes failure to adapt under limited training steps, which is compatible with achieving a moderate score that is below the target threshold.

- **Several section-by-section notes** (e.g., "reader must infer structure from equations," "writing is clear enough") are editorial observations that are either acknowledged as non-issues by the critic themselves or are too vague to constitute actionable weaknesses.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the evaluation protocol.** State explicitly for each experiment: how many fine-tuning steps each method received on target tasks, what threshold defines successful "adaptation" (vs. merely reporting a score), and whether all methods were given the same budget. Provide learning curves for CartPoe analogous to CoinRun to let readers verify the "Minimum Adaptation Steps" metric visually.

2. **Bridge the theory-practice gap.** Add a paragraph discussing which identifiability assumptions are violated by the neural implementation and why the algorithm may still recover useful causal structure (e.g., neural networks can approximate linear functions, the differentiability condition is a sufficient but not necessary condition).

3. **Report seed counts and computational costs.** State the number of random seeds used throughout. Report wall-clock time for the SA expansion strategy versus baselines, and the typical number of search steps required.

4. **Expand Atari experiments or justify the selection.** Either test on more games or provide explicit justification for why the chosen 5 games are representative of the distribution-shift/space-expansion scenarios.

## Score and Decision

This paper tackles a relevant and under-explored problem — generalizable RL under both distribution shifts and state/action space expansions. The CSR framework is well-motivated, the three-step strategy is principled, and the theoretical identifiability results (despite being disconnected from the implementation) demonstrate conceptual depth. The empirical results consistently show CSR outperforming strong baselines across multiple environments.

The primary weakness is not in the method but in the presentation of the evaluation, which is ambiguous enough to raise questions about whether the baselines were compared fairly. However, a close reading of the paper shows that baselines did receive adaptation steps (AdaRL at 4k on CartPole Task 2, baseline scores on target Atari tasks are non-trivial), so the critic's claim of "zero-shot" evaluation is not supported. The real issue is that the paper would benefit from greater clarity in its experimental reporting — specifying budgets, defining success thresholds, and providing learning curves for CartPoe.

The method is sound, the contributions are clear, and the weaknesses are addressable through clarification rather than requiring new experiments. I recommend acceptance with a request for clarifications on the evaluation protocol.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>