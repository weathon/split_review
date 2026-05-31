## Summary

The paper addresses preference alignment of Large Reasoning Models (LRMs), where the correct marginal objective over reasoning traces is intractable and the standard trace-based DPO surrogate suffers from high gradient variance. The proposed method, BVPO, linearly combines a high-variance trace-based gradient estimator with a low-variance empty-trace estimator (obtained by conditioning the model on an empty reasoning trace via `<think></think>`). The mixing weight is theoretically motivated through bias–variance MSE minimization, and the framework is connected to SGD convergence bounds. Empirically, BVPO improves AlpacaEval 2 win rate by up to 7.8 points and Arena-Hard by up to 6.8 points over DPO/SimPO baselines, and also improves math reasoning across six benchmarks.

---

## Strengths

- **Timely and well-motivated problem.** LRM alignment is an emerging but understudied challenge, and the paper correctly identifies that trace-induced gradient variance is a concrete bottleneck when applying DPO to models that emit long, stochastic reasoning chains. Appendix B (referenced in the text) provides empirical evidence of variance elevation in log-probability distributions when traces are present.

- **Simple, practical, and effective method.** Mixing two losses in a convex combination is trivially implementable as a drop-in extension. The empirical gains are consistent across three models (1.5B, 7B, 8B) and across both alignment benchmarks (Table 1) and math reasoning benchmarks (Table 2), with the latter being a particularly useful safeguard showing reasoning is not degraded.

- **Multi-benchmark alignment evaluation.** Testing in both Thinking and NoThinking modes on Arena-Hard and AlpacaEval 2, while simultaneously verifying reasoning preservation on AIME 24/25, AMC, Minerva, OlympiadBench, and MATH-500, is thorough for the alignment context.

---

## Weaknesses

### Fatal
None.

### Major

1. **The theoretical optimal α is not practically computable, and its practical use is unvalidated.** Theorem 2 derives α_unc in terms of tr(Σ_e − Σ_te), ‖b_e‖², b_t⊤b_e, and 𝔼[‖g_t − g_e‖²], none of which are directly estimable during training (since b_e and b_t depend on the true marginal gradient µ = ∇ℒ_m, which is intractable). The paper does not explain how α is chosen in experiments or whether it was tuned as a hyperparameter. The gap between the theoretical MSE-optimal α* and the empirical α renders the core theoretical contribution partly disconnected from the practical method.

2. **The condition η L = 1 in Theorem 4 is unrealistic and weakens the algorithmic-optimality claim.** The convergence bound in Theorem 3 requires η ≤ 1/L for feasibility; the condition η L = 1 is the degenerate boundary case, rarely satisfied in practice. At this boundary, minimizing MSE is equivalent to minimizing the convergence error floor, which is a mathematical tautology rather than a usable prescription. For η L < 1, the connection between MSE minimization and per-step convergence error minimization no longer holds exactly.

3. **Alternative variance-reduction mechanisms for the observed gains are not ruled out.** BVPO in practice is equivalent to training with a mixture of trace-based and no-think preference data. This is a form of multi-mode data augmentation — co-training the model to behave well in both Thinking and NoThinking modes simultaneously. The NoThinking performance gains are expected by construction. The reasoning that Thinking gains arise from gradient variance reduction rather than from regularization, data diversity, or mode mixing is not supported by ablations (e.g., varying α, directly measuring gradient variance during training, or comparing with a baseline that adds no-think SFT data without preference labels).

### Minor

1. **Theorem 1 is trivially true.** Var_r(αg_t + (1−α)g_e) = α² Var_r(g_t) follows immediately from g_e being a deterministic constant w.r.t. trace sampling. Framing this as a formal theorem overstates its depth.

2. **Baseline coverage is limited.** Among DPO variants, only SimPO and vanilla DPO are tested; KTO (mentioned in related work) and TGDPO are omitted. More importantly, there is no comparison with simpler variance-reduction baselines such as multi-sample trace averaging (though this is more expensive) or gradient clipping on the trace-based loss.

3. **The bias of g_t w.r.t. g_m is not acknowledged.** The paper informally treats g_t as "approximating" the marginal gradient via Monte Carlo, but log(Σ_r π_θ(r,y|x)) ≠ 𝔼_r[log π_θ(r,y|x)] (Jensen's inequality gap), so g_t is itself a biased estimator of g_m. The entire theoretical apparatus treats g_t as having bounded bias, but this is not formally justified.

### Trivial
- The improvement claim of "up to 4.0 points on six math reasoning benchmarks" refers to the average across all six for the 7B model; individual benchmark gains are more modest, and Minerva on the 8B model shows a slight regression.

---

## Nice-to-Haves

- Ablation showing performance across a sweep of α values would both validate that the optimal α is near the empirically used value and help practitioners choose α without a grid search.
- Direct measurement of gradient variance during training (e.g., gradient norm variance per step) would provide evidence that variance reduction is the actual mechanism driving improvements.
- Comparison with a "data augmentation" baseline (mixing trace-based and no-think supervised data without the preference-optimization framing) would help isolate the effect of the variance reduction gradient combination.

---

## Novel Insights

The paper's most interesting insight is that LRM alignment has a structurally different variance profile from standard LLM alignment: long and stochastic reasoning traces cause joint log-probability fluctuations that dwarf those of final answers alone. By proposing an empty-trace estimator — which amounts to querying the same pretrained model but in its "no-think" mode — the paper provides a computationally free, low-variance control variate that can be mixed with the trace-based gradient. While the gradient mixing idea is a classical statistical device, its instantiation via `<think></think>` prompting to suppress traces is a practically novel construction tailored to the LRM setting. The finding that preference-optimizing with general conversational data in this mixed regime also improves math-reasoning performance (rather than degrading it) is genuinely surprising and of practical value for deployment pipelines.

---

## Suggestions

- Clearly state how α is set in all experiments (hyperparameter sweep, fixed default, or theoretical estimate) and report sensitivity.
- Provide a practical approximation or heuristic for the optimal α based on empirical quantities (e.g., estimating 𝔼[‖g_t − g_e‖²] from a small calibration set).
- Include a training-curve comparison (loss, gradient-norm variance) between DPO and BVPO to visually corroborate the variance-reduction hypothesis.
- Qualify the η L = 1 assumption in Theorem 4 and discuss the gap for realistic η < 1/L.

---

## Score and Decision

BVPO identifies a real and underexplored problem (LRM alignment variance), proposes a clean and practical solution (empty-trace mixing), and demonstrates consistent empirical gains across multiple models and benchmarks. The theoretical apparatus, while imperfect (optimal α is not practically computable, Theorem 4 requires an unrealistic condition, the core mechanism is not fully disambiguated from data augmentation), provides sufficient principled motivation. The method is ready for adoption, and the problem framing should stimulate further work on LRM-specific alignment methods.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>