- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8
## Summary

This paper tackles generalizable reinforcement learning under both distribution shifts and state/action space expansions — a genuinely broader and harder problem than typical transfer RL. The authors propose CSR, which learns causal latent representations with structural masks \(D\), introduces a task-specific change factor \(\boldsymbol{\theta}_i\) to capture distribution shifts, and uses a three-step strategy (detect shift → expand latent space if needed → prune irrelevant variables) to adapt autonomously. Experiments on CartPole, CoinRun, and 5 Atari games show positive results.

## Strengths

- **Addresses a genuinely broader scenario than prior work.** Most transfer RL methods assume fixed state/action spaces. CSR explicitly handles both distribution shifts and space expansions (adding new latent variables), which is a meaningful step toward more practical generalization. The CoinRun motivating example (new enemies = state expansion) is well-chosen and clearly communicated.

- **Strong empirical results on CartPole across all four task types.** Table 1 shows CSR achieves perfect scores (500/500) on tasks with distribution shifts (Task 2), state expansion (Task 3), and action expansion (Task 4), while baselines fail on the expansion tasks. The "Minimum Adaptation Steps" column (2k–10k samples for CSR vs. non-convergence for baselines) provides concrete evidence of sample-efficient adaptation.

- **CoinRun and Atari results are consistently positive.** CSR outperforms all baselines (Dreamer, AdaRL, DQN, SPR, EfficientZero) on CoinRun (Fig. 2b) and on all 5 Atari games tested (Table 2), suggesting the method's benefits are not limited to a single environment.

- **Self-adaptive expansion strategy is ablated and shown superior.** Fig. 2(d) compares Random, Deterministic, and Self-Adaptive expansion strategies, with SA yielding the best normalized returns. This ablation directly supports the claim that automatically determining the number of new causal variables helps.

- **Pruning driven by learned structural masks improves learning efficiency.** Fig. 2(c) shows that CSR with structural embeddings \(D\) achieves faster and higher cumulative reward than CSR without \(D\), validating that the causal graph pruning component contributes positively.

## Weaknesses

### Fatal
None.

### Major

- **The detection mechanism (distribution shift vs. space expansion) is a critical component that receives no direct validation.** The method hinges on a single thresholded comparison: update only \(\boldsymbol{\theta}_i\), compute prediction error \(\mathcal{L}_{\text{pred}}\), and compare it against \(\tau^\star\) (the source task's final prediction loss). If below threshold → distribution shift; otherwise → space expansion. The paper provides **no analysis of whether this decision rule actually works correctly**: no prediction error distributions for shift vs. expansion tasks, no confusion matrices, no threshold sensitivity analysis, no ablation that compares the gated decision against "always expand" or "always update \(\boldsymbol{\theta}_i\)". The threshold \(\tau^\star\) inherited from the first task is never shown to generalize reliably across tasks with different difficulty levels (e.g., a large distribution shift could push error above threshold and trigger a spurious expansion). Since the entire three-step pipeline depends on this first decision, its lack of validation is a significant gap.

- **The Atari evaluation is limited to 5 of 26 games without a principled justification.** The paper states "we select five representative games" but does not explain why the remaining 21 are excluded or how representativeness is assessed. Given that Atari 100k is a standard benchmark with public scores for all games, the claim of "outperforming state-of-the-art baselines" (abstract, line 4) is only supported for 5 games. The missing games could dilute or challenge the reported advantage.

- **Missing ablation of the detection decision itself.** The ablation study tests two things: presence of structural embeddings \(D\) (Fig. 2c) and choice of expansion strategy (Fig. 2d). The most central design choice — whether the detection step (update \(\boldsymbol{\theta}_i\) vs. expand) actually helps — is not ablated. A natural control (e.g., always run both steps and compare) would isolate whether the gated decision improves performance over simpler alternatives. Without this, the benefit of the adaptive detection remains unquantified.

### Minor

- **The handling of action-space expansions is underspecified.** The paper mentions action expansions in CartPole Task 4 (adding force values), and Section 3.2 states "action variables are observable, we can directly obtain the relevant information when the action space expands." However, no concrete mechanism is given for how the policy output layer is reconfigured when the action set changes (e.g., discrete-to-larger discrete), or how the world model adapts to new actions. The CartPole results saturate at the maximum score (500/500) for all tasks, making it difficult to assess whether the action expansion was meaningfully challenging.

- **The pruning definition classifies self-loop-only variables as "non-compact," which may be overly restrictive.** The definition in Section 3.3 states that a variable is compact only if it influences \(o_t\), \(r_{t+1}\), or *other* state variables \(s_{j,t+1}\) (\(k \neq j\)). Variables that influence only themselves over time (self-loops) are pruned. Such variables could still be essential for long-horizon tasks through temporal accumulation. The impact of this design choice is not discussed or ablated.

- **The binary mask \(D\) learning procedure has an unresolved ambiguity.** The paper describes \(D\) as "binary masks" but learns them via continuous optimization with L1 sparsity regularization (\(\mathcal{J}_{\text{reg}}\)). The text says regularization "induces certain entries of \(D\) to transition from \(1\) to \(0\) during model estimation" (line 206), but it does not explain whether final masks are obtained by thresholding continuous values, whether the \(D\) parameters are constrained to \([0,1]\), or how the transition from continuous to binary is handled during the forward pass (element-wise product with binary masks). While the overall approach is reasonable, this ambiguity makes exact reproduction harder without guessing.

### Trivial
None.

## Nice-to-Haves

- A detection accuracy analysis (prediction error distributions for shift vs. expansion tasks, threshold sensitivity) would substantially strengthen the core claim.
- Reporting results on additional Atari games (even a few more with mode/difficulty variations) would broaden the empirical support.
- A baseline that handles space expansion (e.g., a Dreamer variant that adds latent dimensions upon high prediction error) would help isolate the benefit of the causal structure.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The causal graph structure D is never concretely specified or optimized."** — Factually incorrect. The paper explains (lines 200–206) that \(D\) is learned via L1 regularization (\(\mathcal{J}_{\text{reg}}\)) that pushes entries toward zero during joint optimization. The critic's concern about binary-vs-continuous ambiguity is retained above as Minor; the stronger claim that it is "never explained" is removed.
- **"The theorems are stated without proof (presumably in appendix)."** — Removed per the hard rule that missing appendix content should not be penalized.
- **"Fails to discuss work on non-stationary RL or meta-learning with latent variable models."** — Removed per the hard rule against flagging missing related works.
- **"The hyperparameters λ_KL, λ_reg, and the threshold τ⋆ are not reported."** — Removed per the hard rule against nitpicks about undisclosed hyperparameters; τ⋆ is discussed in the detection validation gap above.
- **"representation model q_α conditions on θ_i, but this is not clearly motivated"** — Subjective design opinion; removed as strawman.
- **"The paper overclaims by saying 'we explore a wider range of scenarios'"** — The paper does test action expansion in CartPole Task 4; the claim is supported, though the saturated metric is a fair point (retained elsewhere as Minor).
- **Strength Finder: generic/superficial strengths.** Generic phrasing like "This paper addressed an important problem" removed; only concrete, evidence-backed strengths retained.
- **Cherry-picking accusations (Atari).** The critic's characterization of "potential cherry-picking" is speculative and removed; the concrete concern about limited coverage (5/26 games) is retained.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the key gap (unvalidated detection step) and the scope limitation (5/26 Atari games), but these are straightforward observations rather than novel syntheses.

## Suggestions

1. **Validate the detection step directly.** Report the prediction error distributions for distribution-shift tasks and space-expansion tasks separately. Show a confusion matrix or at least a per-task breakdown of whether CSR's detection decision was correct. Analyze sensitivity to the threshold \(\tau^\star\) (e.g., vary it and measure impact on downstream performance).

2. **Expand the Atari evaluation** to at least the subset of games that have documented mode/difficulty variations, or provide a clear justification for the 5 selected games (e.g., they are the only ones with non-trivial space expansions).

3. **Add an ablation of the detection decision.** Compare CSR's gated decision (update \(\boldsymbol{\theta}_i\) vs. expand) against at least one control: (a) always expand, (b) always update \(\boldsymbol{\theta}_i\), or (c) run both steps.

4. **Clarify the \(D\) learning procedure.** State whether \(D\) parameters are constrained to \([0,1]\), how continuous values are mapped to masks during the forward pass, and whether post-training thresholding is applied.

5. **Discuss the self-loop pruning issue.** Acknowledge whether variables with only self-influence can be useful for long-horizon tasks, and consider ablating this decision.
