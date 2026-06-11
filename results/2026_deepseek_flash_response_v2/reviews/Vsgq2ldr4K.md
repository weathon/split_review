Now let me compile the final review.

## Summary

This paper proposes Power Sampling, a training-free MCMC-based inference algorithm that samples from the power distribution p^α of a base LLM. The key idea is that base models contain latent reasoning capabilities that can be elicited by sharpening their distribution via exponentiation and Metropolis-Hastings sampling with a block-wise progressive scheme. The method is evaluated against GRPO-based RL posttraining on reasoning benchmarks (MATH500, HumanEval, GPQA) and AlpacaEval 2.0 across three model families (Qwen2.5-Math-7B, Qwen2.5-7B, Phi-3.5-mini-instruct), showing competitive single-shot performance and superior multi-shot diversity.

## Strengths

1. **Theoretical clarification of power distributions vs. low-temperature sampling (Proposition 1).** Section 4.1 rigorously proves that low-temperature sampling is *not* equivalent to sampling from p^α, via the "sum of exponents vs. exponent of sums" contrast (Eq. 7 vs. 8). The concrete toy example (Example 1) cleanly illustrates how the two samplers make opposite token choices, providing clear intuition for why power distributions favor tokens with fewer but higher-likelihood future paths — a property plausibly useful for reasoning. This is a genuine conceptual contribution that clarifies a common misconception.

2. **Training-free single-shot accuracy competitive with RL-posttraining across multiple benchmarks and model families.** Table 1 shows power sampling on Qwen2.5-Math-7B achieving 74.8% on MATH500 (GRPO: 78.5%), 57.3% on HumanEval (GRPO: 53.7%), and 38.9% on GPQA (GRPO: 39.9%). On out-of-domain tasks (HumanEval, AlpacaEval 2.0), power sampling consistently matches or exceeds GRPO across all three model families. These results support the paper's central claim that base models' reasoning capabilities are underutilized by standard sampling.

3. **Pass@k diversity preserved while maintaining strong single-shot performance.** Figure 5 shows that power sampling's pass@k accuracy continues rising with k (reaching ~0.98 at k=16), matching the base model's multi-shot ceiling, while GRPO plateaus at ~0.90. This directly demonstrates that the method avoids the diversity collapse known to afflict RL-posttraining — achieving "the best of both worlds" in single-to-few-shot accuracy and sample diversity. This is arguably the paper's cleanest and most practically significant result.

4. **Block-wise progressive MCMC scheme (Algorithm 1) to handle high-dimensional token spaces.** The progressive annealing through intermediate distributions π_k (Eq. 10–11) is a practical adaptation of tempered MCMC to the autoregressive setting, explicitly designed to mitigate exponential mixing times in high-dimensional sequence spaces (Section 4.3). The token budget estimate (Eq. 12) provides a principled characterization of the inference-time compute cost.

5. **Generalization to non-verifiable domains.** Results on AlpacaEval 2.0 (Table 1) show power sampling outperforming GRPO across all three model families (e.g., 2.88 vs. 2.38 for Qwen2.5-Math-7B), while GRPO requires a verifiable reward and is limited to domains where ground-truth verification is available. This supports the claim of broad applicability beyond easily verifiable domains.

## Weaknesses

### Fatal
None.

### Major

1. **N_MCMC — the core algorithmic hyperparameter — is not reported.** Despite being a required input to Algorithm 1 and central to the token budget estimate in Eq. (12), the actual value of N_MCMC used in experiments is never stated anywhere in the main paper. The paper says only "relatively small values of N_MCMC" (end of Section 4.3). Without this number, the reader cannot: (a) assess whether the inference-time compute cost is reasonable, (b) reproduce the results, or (c) evaluate sensitivity of the method to this parameter. This is the single most important experimental parameter of the method and its absence is a significant gap that must be filled.

2. **The GRPO baseline on Phi-3.5-mini-instruct appears not to have converged, weakening the "outperforms RL" generalizability claim.** In Table 1, GRPO on Phi-3.5 achieves 40.6% on MATH500 (base: 40.0%, +0.6%) and 13.4% on HumanEval (base: 21.3%, a *regression* of −7.9 percentage points). These numbers indicate the GRPO training did not produce meaningful improvement for this model on two of three reasoning benchmarks. While GRPO did improve on GPQA (27.3% → 35.9%), the claim that power sampling "outperforms GRPO by up to +59.8% on HumanEval" relies on a baseline that effectively failed. This does not invalidate the Qwen results, but it substantially weakens the claim that the advantage generalizes across model families. The paper should either fix the Phi-3.5 GRPO baseline with properly tuned hyperparameters or honestly discuss this failure as a limitation of the RL method rather than presenting it as evidence of power sampling's superiority.

3. **No compute-accuracy tradeoff or cost-normalized comparison.** The paper acknowledges inference-time scaling (Eq. 12) as "a new axis for inference-time scaling" but provides no wall-clock time, FLOP counts, or cost-normalized comparison against GRPO. With the token budget formula ≈ N_MCMC · T²/(4B) and T=3072, B=192, the per-sequence cost scales as N_MCMC · ~12,288 generated tokens for a single ~680-token output — clearly a different compute regime from GRPO's single forward pass. A comparison against best-of-N independent sampling from the base model at matched compute budgets would isolate what the MCMC structure specifically buys beyond brute-force resampling.

### Minor

4. **Low-temperature sampling already captures a large fraction of the gain.** For Qwen2.5-Math-7B on MATH500: Base=49.6, Low-temp=69.0 (+19.4), Power=74.8 (+5.8 on top of low-temp), GRPO=78.5. Low-temperature alone captures ~67% of the gap from base to GRPO. The paper could more clearly acknowledge that the main empirical contribution over the low-temperature baseline is meaningful but incremental (~6 points on MATH500), rather than framing the story primarily as "matching RL from scratch."

5. **Discrepancy between pass@1 in Figure 5 and single-shot accuracy in Table 1 suggests non-trivial variance.** Figure 5 shows power sampling at k=1 achieving ~72% on MATH500, while Table 1 reports 74.8% for the same condition. Similarly, GRPO shows ~75% in Figure 5 vs. 78.5% in Table 1. No error bars, standard deviations, or statistical significance tests are provided anywhere in the paper. Given the modest test-set sizes (HumanEval: 164, GPQA Diamond: 198), this is a concern for assessing whether observed differences between methods are meaningful.

6. **No MCMC convergence diagnostics.** The paper acknowledges that MCMC can have exponential mixing times in high-dimensional spaces (Section 4.3) and proposes the block-wise scheme to mitigate this, but provides no empirical diagnostics — acceptance rates, autocorrelation, effective sample size, or trace plots — to verify that the chain actually mixes and converges toward p^α in practice with the chosen B and N_MCMC.

7. **No comparison to best-of-N independent sampling.** Given the paper's thesis that "your base model is smarter than you think," a natural baseline is to draw k independent samples from the base model and select the best by likelihood or majority voting. Such a comparison would isolate whether the specific MCMC structure provides benefits beyond spending more compute on independent draws. This baseline is absent.

### Trivial

8. **Single qualitative example in Table 2.** The one cherry-picked HumanEval example carries limited evidential weight and could be moved to the appendix.

## Nice-to-Haves
- Provide a compute-accuracy Pareto curve varying N_MCMC to characterize the inference-time scaling behavior.
- Report MCMC diagnostics (acceptance rates, trace plots) to verify convergence to the target distribution.
- Report confidence intervals or error bars for all main results.
- Include best-of-N independent sampling as a baseline.
- More clearly separate in-domain vs. out-of-domain claims with explicit discussion of the Phi-3.5 GRPO training issue.

## Removed Points
- "Criticism about appendix references (A.4, A.5) not being visible in the main paper" — removed per hard rule: the parser strips appendices; the original submission contains them.
- "Speculation that Eq. (12) underestimates cost because every MH step requires evaluating base model likelihood on full prefix" — removed as unsupported speculation not verifiable from the paper.
- "Abstract framing undersells inference-time cost" — removed as a framing opinion, not a concrete weakness.
- "Figure 5 analysis only shown for one model on one dataset with appendix reference" — removed per hard rule about stripped appendices.
- "N_MCMC=5-10 yields 90-190× cost speculation" — removed as speculative since N_MCMC is unknown; the criticism about N_MCMC being missing is retained as Major #1.

## Novel Insights
The reviews surface an interesting tension: the paper's strongest contribution (the theoretical distinction between power distributions and low-temperature sampling, and the clean pass@k diversity result) is somewhat undercut by its weakest empirical choices (missing hyperparameter, a GRPO baseline that failed on one model family, and no cost analysis). The Phi-3.5 results are particularly problematic because the GRPO baseline regressed on HumanEval, yet the paper's "outperforms by +59.8%" headline relies on this. Separately, the pass@k preservation finding deserves more emphasis: it addresses a known failure mode of RL-posttraining that the community cares about, and the evidence for it is clean and free of the calibration issues that plague the single-shot comparison.

## Suggestions
1. **Report N_MCMC explicitly** for all experiments, along with a sensitivity analysis showing how performance varies with this parameter.
2. **Add a compute-accuracy Pareto curve** varying N_MCMC, with wall-clock time or token cost on the x-axis, including a baseline of best-of-N independent sampling at matched compute budgets.
3. **Address the Phi-3.5 GRPO baseline** — either retrain with properly tuned hyperparameters, or clearly discuss that the GRPO training did not converge for this model and explain why the Qwen results are the primary evidence.
4. **Add MCMC diagnostics** (at minimum, acceptance rates) to demonstrate the chain actually mixes toward p^α.
5. **Report confidence intervals or error bars** for all main results, especially on smaller test sets (HumanEval: 164, GPQA Diamond: 198).

## Score and Decision

**Round 1 (Bracketing):** Initial bracket placed the paper between approximately 4.5 and 6.5, based on comparisons against anchors at 3.00 (well below), 5.00 (Large Language Monkeys, clearly weaker in novelty), 5.75 (Inference Scaling Laws, comparable quality but different task), and 6.60 (TSMC, similar methodology but cleaner empirical story).

**Round 2 (Narrowing):** Compared against anchors at 5.67 (Inference-Aware Fine-Tuning for BoN — narrower evaluation, weaker theoretical contribution, thus the paper under review is stronger), 5.75 (DAB Controlled Decoding — comparable quality but different domain), and 5.75 (Flow of Reasoning — rejected despite reasonable avg score). The paper under review is stronger than the BoN and Flow of Reasoning papers due to broader evaluation and stronger theory, but its empirical gaps (missing N_MCMC, Phi-3.5 baseline) prevent it from reaching the 6.60 level of the TSMC paper.

**Final score:** The paper has a genuine theoretical contribution and convincing pass@k diversity evidence, but the evaluation is incomplete in ways that directly affect the headline claims. The missing hyperparameter and questionable baseline should be fixable, and the core method is interesting. Score reflects a solid submission with gaps that a revision should address.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>