## Summary

This paper proposes PC (Perplexity Consistency) and RPC (Reasoning-pruning Perplexity Consistency), two confidence estimation methods for LLM reasoning. PC replaces the Monte-Carlo count in self-consistency (SC) with the LLM's token-level probability of each observed answer, aiming to reduce estimation variance under small sample sizes. RPC additionally prunes low-probability reasoning paths using a Weibull mixture model. Experiments on 7 benchmarks (math and code) with InternLM2-Math-Plus and DeepSeek models show PC consistently outperforming standard SC, while RPC further improves on math but not code tasks.

## Strengths

- **Intuitive and well-motivated core idea.** Replacing the crude Monte-Carlo frequency estimate (which has variance ψ(1-ψ)/n) with the LLM's own token-level probability (a deterministic value given the observed path) is a clean insight for reducing variance in self-consistency confidence. The paper clearly identifies the "resource-constrained" setting (small n, no calibration set) and motivates why existing solutions fall short.

- **Consistent empirical improvements for PC across all settings.** Across four math datasets (MATH, MathOdyssey, OlympiadBench, AIME) and three code datasets (HumanEval, MBPP, APPS), using two model families (InternLM2-Math-Plus 1.8B/7B, DeepSeek-Math 7B, DeepSeek-Coder 33B), the PC method outperforms SC, PPL, and verbalized confidence in accuracy, often by non-trivial margins (Figures 4, 7, 8; Tables 2–3). The gains appear across multiple sample sizes and temperatures, not a single cherry-picked configuration.

- **No calibration set requirement.** Unlike temperature scaling and other post-hoc methods that require held-out data, PC is "data-free" in the sense that it only needs the LLM's own next-token probabilities, which are available at inference time. This is a genuine practical advantage.

## Weaknesses

### Major

1. **Theorems 1–3 are stated without substantiation, and Theorem 1 contains an internal contradiction.**  
   - **Theorem 1** claims "PC achieves lower estimation error than SC" but the displayed inequality is 𝔼[(ψ̂₁−ψ)²] ≤ 𝔼[(ψ̂₂−ψ)²] — meaning SC (ψ̂₁) has *lower or equal* MSE, directly contradicting the theorem's stated claim. Moreover, the condition "With a proper assumption" is never specified in the paper, making the theorem vacuous.  
   - **Theorem 2** asserts O(1/n²) convergence for PC versus O(1/n) for SC, with no proof, derivation, or even a sketch of the argument. The key step — showing that the bias of ψ̂₂ (the missing probability mass of unobserved consistent answers) decreases fast enough — is not addressed.  
   - **Theorem 3** states an upper bound with a term O(e^{(1−r/2)}), where r appears only as a parameter defining the threshold. The paper claims this implies "exponential in n" convergence, but the bound as written does not depend on n (if r is constant) and the relationship between r and n is unspecified. No proof is provided.  

   These theorems are presented as a central contribution ("theoretical analysis guarantees…"), but the paper provides no mechanism to verify them. The gap between the strength of the claims and what is actually demonstrated is substantial.

2. **No error bars, confidence intervals, or statistical significance reported anywhere.** For a paper whose entire motivation is *variance reduction*, the absence of any empirical quantification of variance is a critical omission. All reported accuracy and ECE numbers are point estimates without standard deviations, making it impossible for the reader to assess whether the reported improvements are meaningful or within noise. This directly undercuts the paper's central thesis.

3. **The PC estimator's bias is never quantified.** ψ̂₂ sums token-level probabilities only over *observed* consistent answers. Consistent answers that were not sampled contribute zero mass, introducing a systematic downward bias that SC (unbiased) does not have. The paper acknowledges this only obliquely in the abstract ("only a small scale of bias induced") but provides no analysis, no quantification, and no empirical decomposition of bias versus variance. The entire narrative is framed as "variance reduction," which is misleading without also characterizing the bias that is introduced.

### Minor

4. **RPC's Weibull mixture assumption is not empirically justified.** The paper cites Bendale & Boult (2016) from open-set recognition but provides no evidence that LLM token-level probabilities actually follow a two-component Weibull mixture. For small n, the paper resorts to a Truncated Mean fallback (line 252), acknowledging that the MLE fitting is unstable precisely in the resource-constrained regime that motivates the work. This undercuts the claimed practical advantage.

5. **RPC fails to improve over PC on code tasks.** The paper reports this honestly (Figure 8) and offers a plausible explanation (low-probability code paths are already filtered by compilation errors). However, this means RPC's pruning mechanism is not general and only works under specific conditions that are not well-characterized. The scope of RPC's claimed advantage is narrower than the paper's narrative suggests.

6. **The recommendation to use high temperatures with RPC (line 280) partially conflicts with the resource-constrained framing.** High temperatures increase sampling variance and thus require larger n, while the paper's motivating scenario is small-n settings. The paper does not discuss this tension.

### Trivial

None.

## Nice-to-Haves

- Decompose MSE into bias² + variance for PC and SC across different n values. This would directly validate whether the introduced bias is indeed "small" and whether the variance reduction is consequential.
- Show the empirical distribution of token-level probabilities for a few examples and compare it to the fitted Weibull mixture to justify the parametric assumption.
- Report wall-clock time or FLOPs for PC vs. SC, since PC requires computing token-level probabilities for every sampled path (which SC does not).

## Removed Points

These points were flagged to be removed; treat them with caution:

- *"Tables 2 and 3 are embedded images whose numerical values cannot be verified."* → Parser artifact. The original submission would have proper tables; this does not reflect a paper flaw.
- *"No comparison against temperature scaling / Platt scaling."* → The paper explicitly scopes out methods that require a calibration set, which is a core part of the problem definition. This is a scope choice, not a missing baseline.
- *"Derivation details about the PC estimator equation (198) having subtle issues."* → This is subsumed by Weakness #3 (bias quantification) — merged.
- *"Missing proofs in the appendix."* → The main text presents theorems without sufficient context (conditions, derivations). This is captured in Weakness #1.
- *Various formatting/style nitpicks, typos concerns.* → Parser artifacts or below the threshold for a review.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the core tension: the paper presents itself as having rigorous theoretical backing, but the theorems are stated without the conditions or derivations needed to evaluate them. The empirical results for PC are reasonably consistent and suggest the idea has merit, but the lack of variance reporting makes it impossible to judge the magnitude of the claimed benefit.

## Suggestions

1. **Either prove the theorems or remove them.** If proofs exist in the appendix, move a sketch of the key steps and the explicit conditions into the main text. If they cannot be rigorously established, remove the theorem claims and present the convergence-rate discussion as heuristic motivation.
2. **Fix Theorem 1's inequality** — the displayed inequality contradicts the theorem's claim.
3. **Report error bars or standard deviations** for all experimental results, ideally over multiple sampling seeds. This is essential for a paper about variance.
4. **Quantify the bias of ψ̂₂ empirically** by comparing PC estimates against a large-n Monte Carlo oracle (e.g., n=4096) on a subset of problems.
5. **Empirically justify the Weibull mixture** by showing the actual distribution of token-level probabilities and a goodness-of-fit measure.

## Score and Decision

The core idea — using exact token-level probabilities to reduce variance in self-consistency — is sensible and the empirical results for PC are reasonably consistent across tasks and models. However, the paper dramatically overclaims on theory: three theorems are presented as formal guarantees but are unsubstantiated, and one contains a mathematical contradiction. The complete absence of variance reporting in an empirical paper about variance reduction is a significant methodological gap. The RPC component is only validated on math tasks and its central assumption is not tested. In its current form, the paper does not meet the standard for a top venue.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>