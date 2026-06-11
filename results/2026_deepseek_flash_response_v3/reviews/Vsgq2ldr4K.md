Now let me write the final consolidated review.

**Calibration Anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| Ze4aPP0tIn (TSMC for Math) | 6.60 | R1, R2 | Similar MCMC-for-reasoning method. Current paper is slightly weaker — broader scope but more empirical gaps. |
| tQqLV2N0uz (Reprompting Gibbs) | 5.40 | R1 | Clearer theory and broader evaluation than this anchor. Current paper is stronger. |
| VNckp7JEHn (Inference Scaling Laws) | 5.75 | R2 | Comparable quality. This anchor has cleaner compute analysis; current paper has stronger theory. |
| 0xUEBQV54B (Repeated Sampling) | 5.00 | R2 | Current paper has substantially more novelty and theoretical depth. |
| DQfHkEcUqV (Extrapolative MCMC) | 4.75 | R1, R2 | Current paper is clearly stronger — more sound evaluation and clearer contribution. |
| 3OyaXFQuDl (Compute-Optimal Sampling) | 7.00 | R2 | Current paper is weaker — this anchor has much more comprehensive analysis. |
| D7PQ54l5Q1 (MCMC Inverse Problems) | 4.75 | R2 | Different domain but comparable technical depth. Current paper is stronger. |

**Round 1 bracket:** 4.5–6.5  
**Round 2 narrowing:** Compared against Ze4aPP0tIn (6.60, stronger in empirical rigor) and VNckp7JEHn (5.75, comparable). Current paper's genuine theoretical novelty (Proposition 1) is a clear strength, but evaluation gaps (missing N_MCMC, Table 1/Figure 5 discrepancy) pull it down. **Final score: 5.5.**

---

## Summary

This paper proposes "power sampling," an MCMC-based inference-time algorithm that targets the power distribution p^α of a base LLM without any training. The method uses Metropolis-Hastings with random resampling and a block-wise progressive scheme to approximately sample from this sharpened distribution. Empirically, the authors demonstrate that on MATH500 (the GRPO training domain), power sampling comes close to matching GRPO (74.8% vs 78.5% for Qwen2.5-Math-7B), while outperforming GRPO on out-of-domain tasks (HumanEval, AlpacaEval) and preserving generation diversity that RL collapses.

## Strengths

- **Proposition 1 and Example 1 (Section 4.1):** The paper provides a precise mathematical proof that low-temperature sampling is *not* equivalent to sampling from the power distribution p^α, with a concrete two-token counterexample showing that p^α prefers tokens with few high-likelihood future paths while temperature sampling prefers tokens with many lower-likelihood completions. This clean theoretical contribution is pedagogically valuable and establishes the target distribution as genuinely distinct from the commonly-used temperature heuristic.

- **Pass@k analysis (Figure 5, Section 5.3):** The paper demonstrates that power sampling avoids the diversity collapse afflicting GRPO. GRPO's pass@k on MATH500 saturates at ~0.90 for k≥4 and stays flat, while power sampling continues rising to ~0.98 at k=16, matching the base model's ceiling. This provides strong empirical evidence that the method achieves "the best of both worlds": single-shot performance comparable to RL without sacrificing multi-shot diversity.

- **Mechanistic evidence (Figure 4):** The histograms of log-likelihood and confidence under the base model confirm that power sampling samples from higher-likelihood regions than the base model while retaining distributional spread, whereas GRPO concentrates mass at a single peak. This validates the intended algorithmic behavior.

- **Algorithm transparency:** Algorithm 1 is clearly specified, and the closed-form expected token generation cost (Equation 12) provides practitioners with a concrete understanding of the inference-time compute tradeoff.

## Weaknesses

### Major

- **N_MCMC value not reported.** The paper never states the number of MCMC steps used in the experiments (Algorithm 1's N_MCMC), despite mentioning it as a key hyperparameter. This is a critical omission for a method whose main dimension of improvement is "inference-time scaling" (line 203). With T=3072 and B=192, Equation 12 shows that even N_MCMC=5 yields ~61K generated tokens per response. Without this value, readers cannot assess the compute budget or the practical efficiency of the method relative to simpler approaches.

- **Discrepancy between Table 1 and Figure 5 for k=1.** For Qwen2.5-Math-7B on MATH500, Table 1 reports power sampling accuracy as **0.748** (74.8%), while Figure 5 reports k=1 pass@k as **0.72** (72%). These should be the same quantity. The 2.8 percentage point gap is unexplained and undermines confidence in the reported numbers. If these come from different runs or configurations, variance should be reported and explained.

### Minor

- **Phi-3.5-mini GRPO baseline issues.** GRPO on Phi-3.5-mini shows negligible improvement on MATH500 (0.400 base → 0.406 GRPO) and actually *degrades* on HumanEval (0.213 base → 0.134 GRPO), suggesting the RL training did not meaningfully take for this model. The paper's headline claim of "+59.8% on HumanEval" for Phi-3.5 is computed against this weak baseline (0.134). The paper does note it used hyperparameters "selected from Abdin et al. (2024)" to avoid training instabilities, but the resulting comparison inflates the apparent margin of improvement. The Qwen2.5 results are unaffected, but Phi-3.5 comparisons should be more carefully caveated.

- **Abstract lacks precision about in-domain vs out-of-domain comparison.** The abstract states the algorithm "nearly match[es] and even outperform[s] those from RL on a wide variety of single-shot tasks, including MATH500, HumanEval, and GPQA" without distinguishing that GRPO was only trained on MATH. The body and Figure 1 caption are transparent about this distinction (explicitly calling out in-domain vs out-of-domain), but the abstract's framing is broader than the evidence supports. This is a presentation fix.

- **No limitations or failure cases discussed.** The paper presents uniformly positive results without any discussion of when power sampling might fail, which tasks or models it might degrade, or what its failure modes are. A brief limitations section would strengthen credibility.

- **No response format/parsing procedure described.** For MATH500 and HumanEval, extracting the final answer from reasoning traces is non-trivial. The paper does not describe the parsing procedure, which is important for reproducibility.

### Trivial

None.

## Nice-to-Haves

- A sweep over N_MCMC (and perhaps B) showing how performance and diversity vary with compute budget would substantially strengthen the paper and address the missing hyperparameter.
- Comparing against simpler inference-time methods (best-of-N, self-consistency, majority voting) would help isolate whether the MCMC machinery is the reason for improvement or whether simpler strategies achieve similar gains.
- Reporting variance (e.g., across random seeds) for the main results, which would also clarify the Table 1/Figure 5 discrepancy.

## Removed Points

- **Criticism about GRPO comparisons being misleading on OOD tasks (Harsh Critic #1):** The paper explicitly states GRPO is trained only on MATH (line 268) and Figure 1's caption distinguishes in-domain vs out-of-domain. The body is transparent; only the abstract lacks this precision. However, downgraded from "Evidential" to a minor presentation note.
- **Criticism about random resampling of early tokens:** Speculative algorithmic concern not clearly supported by analysis in the paper. The block-wise progressive approach partially addresses this.
- **Criticism about acceptance ratio computational overhead:** This is an inherent property of the algorithm, not a weakness; the paper provides a token-cost estimate that implicitly accounts for it.
- **Criticism about missing related works (best-of-N, self-consistency):** Removed per policy — not verifiable from paper alone.
- **Strength about "addressing an important problem" (generic):** Removed as insufficiently specific to the paper's contributions.

## Novel Insights

The harsh critic's observation that the Phi-3.5 GRPO baseline may not have trained successfully is an important nuance that the paper itself glosses over. Combined with the missing N_MCMC values, this points to a broader concern: the paper's empirical evaluation, while broad in coverage, lacks the depth and precision needed to fully substantiate the central claim. The pass@k diversity preservation result (Figure 5) emerges as the paper's strongest and most novel finding — it is unaffected by the GRPO-training-domain issues and is mechanistically supported by the likelihood/confidence histograms (Figure 4). The theoretical distinction between power distributions and low-temperature sampling (Proposition 1) is a genuine contribution regardless of the empirical gaps.

## Suggestions

1. Report the N_MCMC value(s) used in experiments and provide a compute-performance ablation sweep.
2. Explain the discrepancy between Table 1 (0.748) and Figure 5 (0.72), or report variance across runs.
3. Add explicit caveats about the Phi-3.5 GRPO baseline's limited training success.
4. Qualify the abstract's claims to distinguish in-domain from out-of-domain comparisons.
5. Add a brief limitations section discussing failure cases and compute requirements.
6. Compare against best-of-N and self-consistency baselines in a revision.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>