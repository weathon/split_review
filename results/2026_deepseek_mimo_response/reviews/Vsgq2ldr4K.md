Now let me write the final review.

## Summary
This paper proposes "Power Sampling," a training-free MCMC algorithm that approximately samples from the power distribution p^α of a base LLM at inference time. Motivated by the distribution-sharpening hypothesis — that RL post-training merely sharpens the base distribution — the method explicitly samples from a sharpened distribution to recover similar gains. The paper demonstrates competitive results on MATH500, HumanEval, GPQA, and AlpacaEval 2.0 across three base models, claiming parity with GRPO-posttrained models while preserving multi-shot diversity.

## Strengths
- **Clean theoretical contribution: Proposition 1 rigorously distinguishes power distribution sampling from low-temperature sampling (Section 4.1, Eqs. 4–8).** The proof shows low-temperature sampling computes an "exponent of sums" (Eq. 8) while power distribution sampling requires a "sum of exponents" (Eq. 7). Example 1 concretely demonstrates the two strategies can make opposite sampling decisions on a two-token vocabulary. This clarifies a common misconception and provides the theoretical foundation for the method.

- **Pass@k diversity advantage over GRPO (Figure 5, Section 5.3).** Power sampling's pass@k grows from ~0.72 at k=1 to ~0.98 at k=16, while GRPO plateaus at ~0.90. This directly demonstrates RL-level single-shot performance without the diversity collapse that characterizes RL post-training.

- **Consistent empirical results across three model families and four benchmarks (Table 1).** Power sampling matches GRPO on in-domain MATH500 (e.g., 74.8% vs 78.5% for Qwen2.5-Math-7B) while outperforming on out-of-domain tasks (HumanEval 57.3% vs 53.7%; AlpacaEval 2.88 vs 2.38). Consistency across Qwen2.5-Math-7B, Qwen2.5-7B, and Phi-3.5-mini-instruct strengthens broad applicability claims.

- **Principled autoregressive blocking strategy to address MCMC mixing times (Section 4.3, Eq. 10–11).** The progressive construction of intermediate distributions π_k that seed the next MH process is a well-motivated approach to the exponential mixing time problem in high-dimensional token sequence spaces.

- **Mechanistic connection to reasoning via critical windows and pivotal tokens (Section 4.1).** The explanation that p^α upweights tokens with fewer but higher-likelihood future paths connects to known phenomena about pivotal tokens and reasoning failures, providing an intuitive explanation for why the method works.

## Weaknesses

### Fatal
None

### Major
- **Missing compute analysis: N_MCMC value never reported, total inference cost unquantified.** The paper provides the formula E[tokens] = N_MCMC · T²/(4B) in Eq. 12, with T=3072 and B=192 set in Section 5.1, but never reports the actual N_MCMC used in any experiment. With T=3072 and B=192, each sample requires roughly N_MCMC × 12,288 forward passes — potentially 50–100x more compute than a single autoregressive generation. Since GRPO is a one-time training cost amortized over all queries while power sampling pays per-query, the comparison is incomplete without quantifying this overhead. Readers cannot assess whether observed gains come from the MCMC mechanism or simply from spending substantially more inference compute.

- **No comparison to inference-time compute baselines (best-of-N, majority voting).** The paper positions itself as an inference-time scaling method but omits comparisons to best-of-N sampling from the base model, majority voting, or low-temperature sampling at matched compute budgets. Since power sampling consumes many forward passes per query, a compute-matched comparison would clarify whether the MCMC machinery is necessary or whether brute-force sampling achieves the same gains. The low-temperature baseline in Table 1 is welcome but operates at standard (not matched) compute.

- **No MCMC convergence diagnostics reported.** The paper acknowledges the risk of exponential mixing times (Section 4.2) and proposes autoregressive blocking to mitigate it, but reports no acceptance rates, trace plots, or convergence tests. If the MH chain has not converged to p^α, the samples are not from the stated target distribution and the theoretical motivation dissolves. Acceptance rates are directly observable in Algorithm 1 (line 8: "if u ≤ A(x', x) then accept") and would be straightforward to report.

### Minor
- **No hyperparameter sensitivity analysis or variance estimates.** The method has key hyperparameters α, B, and N_MCMC. The paper reports α=4.0 and B=192 as "empirically found" but provides no sensitivity analysis. Since the paper criticizes RL for requiring "extensive hyperparameter sweeps," demonstrating robustness is important. Additionally, since MCMC is stochastic, variance across runs should be reported.

- **Weak GRPO baseline for Phi-3.5-mini-instruct.** For this model, GRPO barely improves on MATH500 (0.400→0.406) and degrades on HumanEval (0.213→0.134), suggesting suboptimal RL training. While the paper notes using hyperparameters from Abdin et al. (2024) to avoid instabilities, the weak results make this comparison less informative.

- **Generalizability claim to non-verifiable domains is weakly supported.** The abstract claims "broad applicability beyond easily verifiable domains," but the only non-verifiable benchmark is AlpacaEval 2.0, judged by GPT-4-turbo — itself a form of automated verification.

## Nice-to-Haves
- Reporting wall-clock time per query for practical usability.
- Comparing against RL models trained on broader domains (not just MATH) to test out-of-domain advantages more fairly.
- Including acceptance rate statistics per block to illuminate MCMC mixing behavior.

## Removed Points
These points are flagged to be removed, treat them with caution.
- None removed; all major reviewer points were verified against the paper and found valid.

## Novel Insights
The paper's most novel insight is the formal proof (Proposition 1) that low-temperature sampling and power distribution sampling target fundamentally different distributions — the former uses "exponent of sums" while the latter uses "sum of exponents" — and that this distinction has practical consequences: tokens with fewer but higher-likelihood future paths are preferred under p^α but not under low-temperature sampling. Combined with the pass@k diversity results showing power sampling achieves GRPO-level single-shot performance while preserving multi-shot diversity, the paper makes a genuine contribution to understanding the relationship between base model capabilities and RL post-training.

## Suggestions
- Report the value of N_MCMC used in all experiments and compute total per-query inference tokens using Eq. 12.
- Add a compute-matched comparison: generate the same total number of tokens using best-of-N from the base model and compare accuracy.
- Report MH acceptance rates per block as a convergence diagnostic.
- Add a sweep over α and N_MCMC showing accuracy–compute tradeoffs.
- Report variance across multiple runs for the stochastic power sampling results.

## Score and Decision

### Calibration Anchors

**Round 1 (bracketing):**
| Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| Large Language Monkeys | 0xUEBQV54B.md | 5.00 | 1 | Inference-time compute scaling study; our paper has more theoretical novelty |
| Inference Scaling Laws | VNckp7JEHn.md | 5.75 | 1 | Compute-optimal inference analysis; our paper has stronger algorithmic contribution but less compute analysis |
| Inference-Aware Fine-Tuning for BoN | 77gQUdQhE7.md | 5.67 | 1 | Inference-aware fine-tuning; our paper has stronger empirical results |
| Extrapolative Sequence Transformations via MCMC | DQfHkEcUqV.md | 4.75 | 1 | MCMC for sequence generation; our paper has cleaner theory and stronger LLM results |
| SMC for Controlled Generation | xoXn62FzD0.md | 8.00 | 1 | SMC for constrained generation; significantly more thorough evaluation |
| Efficient RL with LLM Priors | e2NRNQ0sZe.md | 6.25 | 1 | LLM priors for RL; somewhat relevant |

**Round 1 bracket: 5.0 – 7.0**

**Round 2 (narrowing):**
| Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| Smaller, Weaker, Yet Better | 3OyaXFQuDl.md | 7.00 | 2 | Compute-optimal sampling for training; more thorough analysis than our paper |
| SequenceMatch | FJWT0692hw.md | 6.00 | 2 | Autoregressive sequence modeling with backtracking; comparable novelty level |
| Let's Be Self-generated via Step by Step | ixoIAOcTSx.md | 5.67 | 2 | Training-free reasoning with CoT; our paper has stronger algorithmic novelty |
| Reprompting | tQqLV2N0uz.md | 5.40 | 2 | Automated CoT via Gibbs sampling; our paper has cleaner theory |

**Round 2 narrowed bracket: 5.5 – 6.5**

**Final score: 6.0** — The paper has genuine theoretical novelty (Proposition 1) and surprising empirical results that exceed the 5.0–5.75 range papers. However, the critical missing compute analysis and absence of inference-time baselines prevent it from reaching 7.0+, where papers like "Smaller, Weaker, Yet Better" (7.0) demonstrate more thorough evaluation including compute-matched comparisons. The paper would likely score significantly higher if the authors report N_MCMC, add compute-matched baselines, and provide convergence diagnostics.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>