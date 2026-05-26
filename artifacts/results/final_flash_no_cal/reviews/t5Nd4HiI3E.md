## Summary

This paper identifies a genuine problem in aligning large reasoning models (LRMs): the intractable marginal preference objective is approximated by a single sampled reasoning trace, producing high-variance gradients that destabilize training. The authors propose BVPO, which mixes a high-variance trace-based gradient estimator with a low-variance "empty-trace" gradient estimator (obtained by disabling reasoning) via a convex combination. The paper provides theoretical analysis showing that this combination reduces trace-induced variance (Theorem 1), derives an MSE-optimal mixing weight (Theorem 2), and links these statistical improvements to tighter SGD convergence bounds (Theorems 3–4). Empirically, BVPO achieves large and consistent gains over DPO and SimPO across three LRM sizes on AlpacaEval 2 (up to +7.8 points) and Arena-Hard (up to +6.8 points), while also modestly improving math reasoning performance.

## Strengths

1. **Well-motivated, under-explored problem.** The paper is the first to systematically analyze gradient variance from trace sampling as a distinct challenge in LRM alignment. The problem framing is clear and the intuition for mixing trace-based and empty-trace gradients is sound.

2. **Clean and theoretically grounded approach.** Theorem 1 provably shows that any nontrivial mixture (α ∈ (0,1)) strictly reduces trace-induced conditional variance when Var(gₜ) > 0. Theorem 2 provides a closed-form MSE-optimal mixing coefficient with a strict-domination guarantee (Corollary 1). The link between MSE and SGD convergence bounds (Theorems 3–4) is a principled connection that strengthens the algorithmic motivation.

3. **Strong and consistent empirical results.** Across three LRMs (1.5B, 7B, 8B) and two alignment benchmarks, BVPO consistently outperforms both DPO and SimPO. The improvements are substantial (up to 7.8 points on AlpacaEval 2 LC Win Rate for the 7B model) and hold in both *Thinking* and *NoThinking* inference modes (Table 1). This robustness across model scales and deployment scenarios is a key strength.

4. **Reasoning preservation and improvement.** Table 2 shows that alignment with BVPO (trained only on general conversational data) does not degrade reasoning ability and in fact improves average math reasoning performance by up to 4.0 points over the base model. This directly addresses a practical concern with alignment for LRMs.

5. **Evaluation in both Thinking and NoThinking modes.** Reporting results with and without reasoning traces at test time provides a complete picture of the method's behavior across deployment scenarios, strengthening empirical confidence.

## Weaknesses

### Fatal
None.

### Major

1. **Gap between the theoretical optimal α* and the practical algorithm.** Theorem 2 derives α* in terms of bias vectors (bₜ, bₑ) and covariance matrices (Σₜ, Σₑ, Σₜₑ) that depend on the *unknown* true marginal gradient μ = ∇ℒₘ. The paper provides no procedure to estimate these quantities or adapt α during training. In experiments, α is treated as a freely tuned hyperparameter (the specific value is deferred to the appendix, which was stripped here). This disconnect means the MSE-optimality guarantees do not directly apply to the empirical results. While the theory still provides a principled justification for why mixing helps, the "optimal" framing is overclaimed relative to what is actually implemented. A discussion of this limitation and possible estimation strategies (or a simpler practical rule) would significantly strengthen the paper.

### Minor

1. **Computational overhead not discussed.** BVPO requires two forward passes per update (one with trace generation, one with reasoning suppressed). The paper calls the method "drop-in" but does not quantify this overhead or compare it against the baselines. Practitioners need this information to assess the cost–benefit trade-off.

2. **Single-run results without error bars or multiple seeds.** Standard practice for large-model alignment papers, but the absence of variance estimates limits confidence in the precise magnitude of the reported gains. For the largest improvements (e.g., 7.8 points) this is less concerning, but for smaller differences (e.g., Table 2, 7B: BVPO 62.3 vs. DPO 61.0) it would be helpful to know whether the gap is stable.

3. **Empty-trace gradient using responses sampled with reasoning enabled.** The paper uses the same preference pairs (y⁺, y⁻) for both trace-based and empty-trace losses. Since these responses were generated with reasoning, their probability under the empty-trace condition may be low, which could affect gradient magnitudes. The paper does not analyze this (though the empirical results suggest it is not a practical problem). A brief diagnostic (e.g., average log-probability under empty-trace) would address the concern.

### Trivial
None.

## Nice-to-Haves

- An empirical sensitivity analysis showing how BVPO's performance varies with α (e.g., a sweep over α ∈ {0, 0.25, 0.5, 0.75, 1}) would help clarify the practical importance of the mixing weight.
- A comparison against a multi-trace estimator (e.g., averaging over 2–3 sampled traces rather than 1) would further contextualize the source of BVPO's gains.
- The method's applicability to other preference optimization algorithms (SimPO, KTO) beyond DPO could be briefly discussed or demonstrated.

## Removed Points

These points were raised in the source reviews but are removed or downgraded per the filtering criteria:

- **"The main text does not state the α value used."** → Removed. The paper explicitly says "Additional experimental details are provided in Appendix C"; the appendix was stripped by the parser, so this information exists in the original submission.
- **"Hyperparameters (β, learning rate) not described; possible unfair tuning."** → Removed. These details are standard for the appendix (stripped). The rule against penalizing missing appendix content applies.
- **"Empty-trace responses may have extremely low probability causing numerical instability."** → Removed. This is a speculative concern without supporting evidence; the empirical results show the method works, and the paper provides variance diagnostics in Appendix B.
- **"Could the metric be measuring a proxy?" / "Are confounders controlled?"** → Removed. These are area-of-concern sweeps without a specific anchor in the paper.
- **Strength "Method is drop-in and algorithm-agnostic."** → Demoted from a core strength to the Removed Points section because the verified weakness (computational overhead not discussed) conflicts with the "drop-in" characterization.
- **"Method agnostic to preference optimization algorithm."** → This is true but generic; many gradient-combination methods are algorithm-agnostic. The real value is in the specific bias–variance motivation.
- **"Theoretical link between MSE and SGD convergence."** → A supporting strength but not a primary contribution; the SGD bounds are standard adaptations of Karimireddy et al. (2022).

## Novel Insights

The key insight that emerges from reading the paper alongside the reviews is that the main contribution is more practical than the theoretical framing suggests. The theoretical optimal-α result is a standard convex-combination optimization; its value is primarily motivational. What is genuinely novel and empirically validated is the *specific combination* of a trace-based gradient (which targets the true marginal but is noisy) with an empty-trace gradient (which is low-variance but biased). The consistent 5–8 point improvements across model sizes and inference modes constitute the strongest evidence that trace-induced variance is a real bottleneck and that this particular mixing strategy is an effective remedy. The paper would be better served by framing this as a well-motivated heuristic with theoretical support, rather than as an "optimized" method whose optimality cannot be realized in practice.

## Suggestions

1. **Address the theory–practice gap.** Add a paragraph discussing that the optimal α* depends on unknown quantities, and either provide a practical estimation procedure (e.g., using a held-out validation set to tune α, or an online adaptation scheme) or explicitly acknowledge that α is treated as a hyperparameter and report its value and sensitivity.

2. **Quantify the computational cost.** State the number of forward/backward passes per update for BVPO vs. the baselines and discuss the practical trade-off.

3. **Add variance estimates.** Report results with at least 2–3 seeds (or provide empirical evidence that the variance is low) to strengthen confidence, especially for smaller deltas.

4. **Report the α value and a sensitivity analysis.** Even if deferred to the appendix, the chosen α and a sweep over values would greatly improve reproducibility and help readers understand the method's robustness.

## Score and Decision

The paper addresses a timely and underexplored problem, proposes a clean and intuitive solution, backs it with sound (if not directly actionable) theory, and demonstrates strong, consistent empirical gains across multiple model scales and benchmarks. The main weaknesses—the theory–practice gap in the "optimal" mixing weight and the lack of computational cost discussion—are significant but do not undermine the core empirical contribution. These issues are addressable and should be fixed before final publication. The paper makes a clear positive contribution to the field.

**Score:** 7.0

**Decision:** Accept

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>