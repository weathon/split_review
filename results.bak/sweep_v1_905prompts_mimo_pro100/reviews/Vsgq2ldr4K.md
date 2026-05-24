Now I have all the information needed. Let me write the final review.

## Summary

This paper proposes Power Sampling, a training-free MCMC algorithm that targets the power distribution p^α of a base LLM to boost single-shot reasoning performance at inference time. The method uses a block-wise progressive Metropolis-Hastings procedure that iteratively resamples token subsequences, and demonstrates on three model families that it can nearly match GRPO on in-domain tasks (MATH500) and outperform it on out-of-domain tasks (HumanEval, GPQA, AlpacaEval 2.0), while preserving the diversity that RL posttraining typically destroys.

## Strengths

- **Clean theoretical insight distinguishing power sampling from low-temperature sampling (Proposition 1, equations 7–8, Example 1).** The paper rigorously proves that low-temperature sampling produces an "exponent of sums" over future paths while p^α produces a "sum of exponents," and the concrete two-token example makes the practical consequence vivid: power distribution upweights tokens with few but high-likelihood future completions, while low-temperature upweights tokens with many low-likelihood completions. This is a non-trivial observation that clarifies a common misconception and directly motivates the algorithm.

- **Strong empirical results on Qwen2.5 models without any training (Table 1).** On Qwen2.5-Math-7B, Power Sampling achieves 74.8% on MATH500 (vs. GRPO's 78.5%), 57.3% on HumanEval (vs. 53.7%), 38.9% on GPQA (vs. 39.9%), and 2.88 on AlpacaEval 2.0 (vs. 2.38) — all from a training-free method. Results hold across Qwen2.5-7B as well. The on-par or superior performance on out-of-domain tasks is particularly noteworthy given that GRPO trains specifically on MATH.

- **Compelling pass@k diversity analysis (Figure 5).** The pass@k curve for Power Sampling strictly dominates both the base model and GRPO, reaching ~0.98 at k=16 compared to GRPO's ~0.90. This directly addresses a documented limitation of RL posttraining and demonstrates that single-shot gains come without sacrificing multi-shot diversity — achieving "the best of both worlds."

- **Practical algorithm design with progressive intermediate distributions (Section 4.3, equation 10).** The block-wise progressive approach is well-motivated by the exponential mixing time problem in high-dimensional MCMC, and the cost formula (equation 12) provides a concrete way to reason about the computational tradeoff.

- **Likelihood/confidence analysis connecting to the distribution sharpening hypothesis (Figure 4).** The histograms show Power Sampling samples from high-likelihood, high-confidence regions of the base model, with more spread than GRPO — empirical support for the thesis that base models already contain strong reasoning capabilities that standard sampling underutilizes.

## Weaknesses

### Fatal
None.

### Major

- **Missing N_MCMC specification — the key hyperparameter is never reported.** Algorithm 1 lists N_MCMC as a hyperparameter, and Equation 12 shows the expected token count scales linearly with it. Section 5.1 specifies T_max = 3072, B = 192, α = 4.0, and the proposal distribution, but never states the value of N_MCMC. The paper even acknowledges in Section 4.3 that this value matters ("In Section 5, we empirically find a value for B that makes Algorithm 1 performant for relatively small values of N_MCMC") but the empirical section omits it. Without this value, no reader can reproduce the results, and critically, no reader can assess the computational cost — which is the central question for any inference-time scaling method.

- **No computational cost analysis or comparison.** This is an inference-time scaling method that trades compute for quality. Equation 12 gives the expected token generation cost, but the paper never reports actual token counts, wall-clock time, or a cost-adjusted comparison. Without knowing N_MCMC, one cannot even estimate whether the method uses 5× or 50× the inference compute of a single autoregressive sample. A single GRPO training run is expensive upfront but the trained model is then used at standard inference cost indefinitely; the paper never engages with this tradeoff. For a paper whose core claim is that Power Sampling "matches and outperforms GRPO," failing to report or discuss the computational cost is a significant gap that changes how the results should be interpreted.

- **The GRPO baseline for Phi-3.5-mini-instruct appears undertrained, inflating the headline results.** From Table 1, GRPO on Phi-3.5 achieves 0.406 on MATH500 (barely above the base model's 0.400) and 0.134 on HumanEval (catastrophically below the base model's 0.213 — GRPO *hurts* performance). The paper notes these hyperparameters were selected to "avoid training instabilities and converges to improvement over the base model over a large number of epochs," yet the MATH500 result shows essentially no improvement and HumanEval shows severe degradation. The Phi-3.5 column therefore inflates Power Sampling's apparent advantage — the +51.9% HumanEval headline number and the +59.8% "outperforms on HumanEval" claim in the text partly depend on this weak baseline. While the Qwen results are genuinely strong, the paper should either acknowledge this caveat more prominently or remove the inflated Phi-3.5 comparative claims.

### Minor

- **No error bars or variance estimates on any result.** Both Power Sampling and GRPO are stochastic. The differences between methods on Qwen models are sometimes small (e.g., 74.8 vs. 78.5 on MATH500, 38.9 vs. 39.9 on GPQA), and without variance estimates it is impossible to assess whether these differences are meaningful.

- **No convergence diagnostics or hyperparameter sensitivity analysis.** For MH algorithms, acceptance rate is a standard diagnostic — if most proposals are rejected, the chain barely moves. No such analysis is provided. Similarly, there is no sensitivity analysis for α, B, or N_MCMC (notably impossible without the value, reinforcing the Major weakness above). A plot of accuracy vs. N_MCMC would directly address whether the method is "close enough" to p^α or doing something else entirely.

- **Connection to "critical windows" and "pivotal tokens" (Section 4.1) is asserted but not verified.** The paper claims that power sampling's preference for tokens with few but high-likelihood future paths relates to resolving critical windows, but doesn't verify this empirically. The connection is suggestive but somewhat hand-wavy.

### Trivial
None.

## Nice-to-Haves

- A cost-adjusted comparison showing, e.g., how many base-model samples could be drawn with the same compute budget as one Power Sampling output, and whether base-model best-of-N can match Power Sampling's single-shot accuracy.
- An analysis of how the response length observation (679 vs. 671 tokens) arises — whether the power distribution naturally favors longer correct solutions or whether this is an artifact of the sampling procedure.
- Discussion of the AlpacaEval 2.0 results' sensitivity to LLM-as-judge biases, especially for the Qwen2.5-7B comparison (8.59 vs. 7.62) which may be within noise for such evaluations.

## Removed Points
These points are flagged to be removed — treat them with caution:

- "Missing related works" — removed per rule: cannot confirm existence of unstated related work.
- "Formatting/style nitpicks" — removed per rule: parser artifacts, not author errors.
- Criticisms about the existence/availability of cited tools/models — removed per rule.
- Generic concerns like "could the metric be measuring a proxy?" — removed: area-of-concern sweep without concrete anchor.

## Novel Insights

The paper's core theoretical contribution — the sum-of-exponents vs. exponent-of-sums distinction (Proposition 1) — is genuinely novel and provides a rigorous mathematical foundation for why power sampling differs from temperature scaling in a way that matters for reasoning. Combined with the empirical demonstration that training-free inference-time MCMC can match RL-level single-shot performance while preserving diversity, this makes a substantive point: base models' reasoning capabilities are systematically underexploited by standard sampling. This reframes the question of "what does RL teach models?" as "what does RL surface from existing model capabilities?" — a question the paper partially answers through its likelihood/confidence analysis.

## Suggestions

1. **Report N_MCMC and provide a full cost analysis.** This is the single most important improvement. Report the actual value used, plot accuracy vs. N_MCMC, and compare wall-clock time / token counts against a single autoregressive sample. Frame the contribution honestly based on the actual cost ratio.
2. **Add a properly tuned GRPO baseline for Phi-3.5 or soften the Phi-3.5 claims.** If re-running GRPO is infeasible, at minimum add a prominent caveat that the Phi-3.5 GRPO baseline may be undertrained and that the large comparative gains on that model should be interpreted cautiously.
3. **Add error bars.** At minimum for the main Table 1 results — even 3-5 seeds would substantially strengthen the paper's claims.
4. **Include convergence diagnostics.** Report acceptance rates across blocks and a plot of performance vs. N_MCMC. This would both address the Major weakness and provide practical guidance for users of the method.

## Score and Decision

### Evaluation Axes

**Originality:** High. The core idea of sampling from p^α of a base LLM via MCMC for reasoning tasks is novel and well-motivated. The sum-of-exponents vs. exponent-of-sums insight (Proposition 1) is a genuine theoretical contribution.

**Importance of research question:** High. Understanding whether RL-posttraining learns genuinely new capabilities or merely surfaces existing ones is a central question in LLM research. A training-free alternative to GRPO would be practically significant.

**Well-supported claims:** Moderate. The Qwen results are compelling, but the missing N_MCMC, absent computational cost analysis, and weak Phi-3.5 GRPO baseline prevent full support for the headline claims.

**Soundness of experiments:** Moderate. The benchmarks are appropriate and the experimental design is reasonable, but the missing hyperparameter, absent error bars, and no convergence diagnostics are notable gaps.

**Clarity of writing:** Good overall. The theoretical sections are clearly presented and Example 1 is effective. The experimental section is readable but omits critical details.

**Value to research community:** High if the cost question is resolved. The theoretical insight alone is valuable; if the computational cost turns out to be modest, the contribution is very strong.

### Calibration

**Round 1 bracket:** Between 5.5 and 7.5.

**Round 2 anchors (topically relevant, score 5.5–8.0):**
- "Large Language Monkeys" (5.0, rejected) — similar topic (inference-time scaling) but weaker contribution; our paper has a more novel method and theoretical foundation.
- "Inference Scaling Laws" (5.75, accepted) — compute-optimal inference analysis; our paper has a cleaner core insight and more striking empirical results.
- "Controlled LLM Decoding via Discrete Auto-regressive Biasing" (5.75, accepted) — related sampling method; our paper addresses a more impactful question.
- "Controllable Generation via Locally Constrained Resampling" (6.0, accepted) — MCMC-based method for LLMs; our paper tackles a more fundamental question about base model capabilities.
- "Learning How Hard to Think" (6.50, accepted) — adaptive inference-time compute; our paper has a stronger theoretical contribution but weaker experimental completeness.
- "Energy-Based Diffusion LM" (6.75, accepted) — novel sampling method; comparable theoretical novelty, but our results are more practically impactful.
- "Smaller, Weaker, Yet Better" (7.00, accepted) — compute-optimal sampling; both papers have strong insights but different weaknesses (theirs: limited models; ours: missing cost analysis).
- "Syntactic and Semantic Control via SMC" (8.0, accepted) — MCMC for LLM generation; stronger experimental completeness and broader tasks, but less ambitious core claim.
- "Min-p Sampling" (8.5, accepted) — practical sampling innovation; much broader adoption and cleaner evaluation, but a simpler contribution.

**Positioning:** The paper's core theoretical contribution and Qwen results are stronger than the 5.75 anchors but the missing N_MCMC and absent cost analysis are more serious gaps than anything in the 6.5–7.0 anchors. The broken Phi-3.5 GRPO baseline further weakens the evaluation. This places the paper at approximately 6.5 — a clear contribution with a good idea and promising results, but needing significant experimental revision to fully support its claims.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>