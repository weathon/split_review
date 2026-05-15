Now I have all the information needed. Let me produce the consolidated review.

---

## Summary

This paper proposes Conservative Density Estimation (CDE), an offline RL algorithm that combines DICE-based distribution correction with an explicit upper bound on the stationary distribution density in out-of-distribution (OOD) state-action regions. The method derives closed-form optimal importance ratios with bounded concentrability, avoids iterative Bellman bootstrapping, and decouples value learning from policy extraction. Empirical results on D4RL tasks show strong performance, especially in sparse-reward and scarce-data settings (e.g., maintaining high rewards with only 1% of trajectories where baselines collapse).

## Strengths

- **First explicit pessimism mechanism in stationary distribution space.** Prior conservative methods (CQL) apply pessimism in Q-value space; DICE methods (OptiDICE) use implicit f-divergence regularization. CDE instead imposes an explicit density constraint $d^\pi(s,a) \leq \epsilon\mu(s,a)$ on OOD state-actions (Eq. \ref{eq:cde_end}) and enforces it via a Lagrange multiplier whose closed-form solution is given in Proposition 2. This is a genuine conceptual contribution that connects two previously separate lines of work.

- **Theoretically bounded OOD importance ratios.** Proposition 1 and Theorem 1 prove that CDE's optimal importance ratio is bounded on OOD state-actions, directly addressing the concentrability issue that plagues standard DICE methods. This is not assumed but derived from the method's optimization structure.

- **Strong empirical results under data scarcity.** Figure 1 (subdataset results) shows CDE maintains high performance even with 1% of trajectories on Maze2D and sparse-MuJoCo tasks, while OptiDICE, CQL, and other baselines degrade sharply. This is the most compelling evidence for the method's practical value.

- **Closed-form solutions enable convex optimization and avoid Bellman compounding.** Propositions 1 and 2 give closed forms for $w^*$ and $\lambda^*$, converting policy evaluation into a convex minimax problem. This avoids the iterative Bellman updates that cause compounded approximation error in value-based methods — a structural advantage in sparse-reward settings.

- **Decoupled training improves stability.** Algorithm 1 separates value learning from policy extraction, unlike interleaved actor-critic methods. The paper notes this "reduces the compounded error amplified by the interleaved optimization" (Section 3.2, line 171), which is supported by the stable convergence observed across tasks.

## Weaknesses

### Fatal
None.

### Major

- **The abstract and introduction overclaim empirical results.** The abstract states CDE "consistently outperforms baselines" on sparse-reward and scarce-data tasks. However, Table 1 shows CQL outperforms CDE on hammer-human (4.4 vs. 1.9) and door-human (9.9 vs. 7.7), and BCQ beats CDE on pen-expert (114.9 vs. 105.0). On hammer-expert and relocate-expert, differences are within one standard deviation. CDE is strong and competitive, but the claim of *consistent* outperformance across all settings is not supported by the reported data.

- **The transition from the constrained problem (Eqs. 2a–2c) to the final objective (Eq. 6) involves a heuristic substitution not rigorously justified.** The paper starts with $D_f(d^\pi\|d^\mathcal{D})$ and directly replaces it with $D_f(d^\pi\|\hat{d}^\mathcal{D})$ where $\hat{d}^\mathcal{D}$ is a mixture $\zeta d^\mathcal{D}+(1-\zeta)\mu$. This change is presented as a practical choice to address support mismatch (line 90), but the paper does not derive it from or prove equivalence to the original constrained problem. The theoretical analysis (Propositions 1–2) then analyzes this altered objective. This gap does not invalidate the method — the density constraint via $\lambda$ *is* preserved in Eq. (6) — but it weakens the claimed logical chain from motivation to implementation. The paper would benefit from either a derivation showing the modified objective is a relaxation/bound on the constrained problem, or an honest reframing.

- **The sparse-MuJoCo task conversion is non-standard and unvalidated.** MuJoCo tasks are converted by binarizing rewards based on a 75th-percentile return threshold (line 229), creating a proxy sparse-reward benchmark. This threshold is arbitrary, and no sensitivity analysis is provided (e.g., what happens at 50th or 90th percentile?). While all methods are evaluated on the same conversion, the resulting task properties — and whether they genuinely test "sparse reward" capability — are unclear. Validation on standard sparse-reward benchmarks (D4RL Kitchen, AntMaze, or original Adroit sparse rewards) would substantially strengthen the evaluation.

### Minor

- **Performance gap bound (Theorem 3) is not actionable.** The bound depends on $\operatorname{TV}(d^\mathcal{D}(s)\|d^*(s))$, the total variation between the data state marginal and the optimal policy's state marginal. This quantity is a property of the dataset and the problem, not controlled by CDE. The $e_N$ term converges at rate $N^{-1/(4+h)}$, which is slow. The theorem identifies relevant factors but does not provide insight into why CDE outperforms alternatives or how to improve it.

- **Missing ablation: isolating the effect of the OOD density constraint.** The method uses both (a) a mixture proposal distribution $\hat{d}^\mathcal{D}$ and (b) the explicit $\lambda$-constrained density bound. Without an ablation that removes the constraint (e.g., setting $\epsilon=\infty$ or $\zeta=1$), it is unclear how much of the empirical gain comes from the proposed density constraint versus from the broader proposal distribution alone.

- **Baseline scores for Table 1 are partly sourced from original papers rather than re-run in a unified pipeline** (line 234). This introduces uncontrolled differences in evaluation frequency, seed selection, and trajectory counts. The sparse-MuJoCo results (Table 2) are re-run and more trustworthy. For a paper making state-of-the-art claims, re-running all baselines under identical conditions would be stronger.

- **Several implementation details are omitted from the main text.** The OOD action distance threshold $\Delta a$ and the number of OOD samples $n$ per state (line 86, line 156) are defined symbolically but their specific values are not given. The behavioral cloning architecture for $\pi^\mathcal{D}$ is not described. These may be in the (stripped) appendix, but their absence from the main paper limits immediate reproducibility.

### Trivial
None.

## Nice-to-Haves

- An ablation of CDE with $\zeta=1$ (no OOD mixture in the proposal) to isolate the effect of the density constraint from the broader proposal distribution.
- Sensitivity analysis on the 75th-percentile reward threshold used for sparse-MuJoCo conversion.
- Additional validation on standard sparse-reward benchmarks (D4RL Kitchen, AntMaze) to decouple the method's sparse-reward capabilities from the specific task conversion.
- Empirical verification of the bounded importance ratios (Proposition 1) by plotting $\tilde{w}^*(s,a)$ on OOD vs. in-distribution samples.
- Reporting of training time and convergence speed compared to baselines.

## Removed Points

These points from the reviews were removed and should be treated with caution:

- **"The original constraint is no longer directly enforced"** (Harsh Critic Point 1) — Removed because it is factually incorrect. The $\lambda$ term from the OOD density constraint is present in the final objective (Eq. 6, line 95). The method does enforce the bound via the Lagrange multiplier.

- **"The central claim of explicitly applying pessimism in the stationary distribution space is not supported"** (Harsh Critic Point 1) — Removed because it is contradicted by the paper's methodology: the $\lambda$ constraint directly bounds the stationary distribution density in OOD regions, and Proposition 2 shows how $\lambda^*$ clips OOD advantages, which controls the stationary distribution.

- **Missing derivations for Propositions 1 and 2** (Harsh Critic Point 3a/3b) — Removed per hard rules. Proofs reside in the appendix, which was stripped by the PDF parser.

- **Missing related works (MomentumDICE, BCDICE, COMBO)** (Harsh Critic Notes) — Removed per hard rules: we cannot verify existence or confirm the paper's omission without external sources.

- **Formatting and style nitpicks** — Removed per hard rules. Parser artifacts are not author errors.

- **"OptiDICE already applies pessimism in stationary distribution space implicitly"** — This conflates implicit f-divergence regularization, which constrains the ratio $d^\pi/d^\mathcal{D}$ over the *data support*, with CDE's explicit density bound on a *separate OOD distribution* $\mu$ whose support is disjoint from $d^\mathcal{D}$. The distinction is substantive and the paper adequately explains it.

- **Strength Finder's "state-of-the-art performance" claim** — Kept but qualified in Strengths above. CDE achieves best or near-best results on many tasks but not universally; the strength is genuine when scoped appropriately (Maze2D, scarce-data settings) rather than claimed broadly.

## Novel Insights

Beyond the paper's own contributions, the most interesting cross-cutting observation from the reviews is that CDE reveals a fundamental tension in DICE-based offline RL: the very importance sampling ratios that enable distribution correction become unbounded when dataset coverage is poor, and fixing this requires either broader proposal distributions (which introduce approximation error) or explicit density constraints (which add complexity). CDE's mixture proposal approach is one practical resolution, but the reviews highlight that the theoretical justification for why this particular resolution preserves the original optimization goal remains incomplete. This points to a broader open question: can one design a principled objective that jointly optimizes the proposal distribution and the density constraint, rather than fixing the mixture coefficient heuristically?

## Suggestions

1. **Reframe the methodological motivation honestly.** Rather than claiming the final objective (Eq. 6) derives from the constrained problem (Eqs. 2a–2c), present the mixture proposal as a practical relaxation and provide either (a) a proof that it lower-bounds the original constrained objective, or (b) an empirical justification with ablations that isolate the constraint's effect.

2. **Tone down the "consistently outperforms" language.** Replace with precise claims: "achieves best or near-best results on X out of Y tasks, with particularly large margins on Maze2D and scarce-data settings."

3. **Add an ablation with ζ=1** (no OOD mixture) to disentangle the effect of the density constraint from the broader proposal distribution. This single experiment would substantially clarify what drives CDE's gains.

4. **Provide hyperparameter values** for Δa and n in the main text (or clearly reference the appendix section containing them). Report the behavioral cloning architecture and training schedule.

5. **Validate on at least one standard sparse-reward benchmark** (e.g., D4RL Kitchen) without modifying the reward structure, to demonstrate generalizability beyond the 75th-percentile conversion.

6. **Re-run all baselines** in a unified codebase for Table 1, or at minimum flag which scores are re-run vs. sourced from prior papers with error bars.

## Score and Decision

The paper presents a genuinely novel integration of explicit pessimism into the stationary distribution space — a conceptual contribution that bridges conservative Q-learning and DICE methods. The bounded-importance-ratio theory and the strong scarce-data results (Figure 1) are the most compelling elements. However, the submission has two weaknesses that prevent acceptance in its current form: **(a)** the logical gap between the constrained problem and the final objective is not addressed, and **(b)** the empirical claims are overstated ("consistently outperforms") relative to the actual results. These are not fatal — the method is sound and the empirical core is strong — but they require a substantive revision (reframing plus ablations) rather than minor corrections. The paper should be a **weak accept** with expectation of revisions, or a **borderline reject** if the room holds the bar at "claims must be precisely supported by evidence." I recommend weak accept given the novelty and the strength of the scarce-data results, but the authors must address both the methodological framing and the overclaiming.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>