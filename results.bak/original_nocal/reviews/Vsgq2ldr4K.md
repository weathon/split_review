Now I have a thorough understanding of the paper and can evaluate each reviewer claim against the paper's actual content. Let me write the final consolidated review.

## Summary

This paper proposes a training-free inference-time sampling algorithm (Metropolis-Hastings with blockwise iterative token resampling) that samples from the *power distribution* \(p^\alpha\) of a base LLM, and shows that this can achieve single-shot reasoning performance comparable to or better than RL-posttraining (GRPO) on MATH500, HumanEval, GPQA, and AlpacaEval 2.0 across three model families (Qwen2.5-Math-7B, Qwen2.5-7B, Phi-3.5-mini-instruct). The algorithm also avoids the diversity collapse characteristic of RL-posttraining, maintaining strong pass@k performance.

## Strengths

1. **Clear theoretical contribution distinguishing power sampling from low-temperature sampling.** Proposition 1 and Example 1 (Section 4.1) rigorously show that the power distribution \(p^\alpha\) (sum of exponents) differs from low-temperature sampling (exponent of sums), and demonstrate through a concrete constructed example how power sampling upweights tokens with fewer but higher-likelihood future paths. This insight is well-motivated and pedagogically effective.

2. **Training-free method achieves results competitive with RL-posttraining across multiple models and benchmarks.** Table 1 shows that power sampling matches GRPO on the in-domain MATH500 (e.g., 74.8% vs. 78.5% for Qwen2.5-Math-7B), outperforms GRPO on HumanEval (57.3% vs. 53.7%) and AlpacaEval 2.0 (2.88 vs. 2.38), and generalizes across three distinct model families. The method requires no RL training loop, no curated dataset, and no verifier.

3. **Algorithm avoids the diversity collapse characteristic of RL-posttraining.** Figure 5 shows that power sampling's pass@k curve lies strictly above GRPO's for all k > 1 (e.g., 0.98 vs. 0.90 at k=16 on MATH500), demonstrating that the method "gets the best of both worlds" — strong single-shot performance without sacrificing multi-shot diversity. This is a genuine advantage over RL-posttraining.

4. **Method is training-free, dataset-free, and verifier-free.** As stated in Section 1 and embodied in Algorithm 1, the approach requires only a base model, a proposal distribution, and likelihood evaluations — no RL training, no reward model, no verifier, no curated dataset. This broadens applicability to domains where verifiable rewards are unavailable.

## Weaknesses

### Fatal
None.

### Major

1. **Core hyperparameter \(N_{\text{MCMC}}\) is never specified.** Algorithm 1 lists \(N_{\text{MCMC}}\) (number of MCMC steps per block) as a key hyperparameter alongside \(B\) and \(\alpha\), and Section 5.1 specifies \(T_{\max}=3072\), \(B=192\), and \(\alpha=4.0\), but never states the value of \(N_{\text{MCMC}}\) used in any experiment. Since the total inference cost scales as \(\approx N_{\text{MCMC}} T^2 / (4B)\) (Equation 12), this is critical for both reproducibility and understanding the compute budget. Without this value, readers cannot assess the computational cost of the method.

2. **No compute-controlled baselines to isolate the mechanism from raw compute expenditure.** The method uses substantially more inference-time token generation than standard sampling (Algorithm 1 generates multiple candidate sequences per block across \(N_{\text{MCMC}}\) steps). Yet the only comparisons are to low-temperature sampling (one forward pass) and GRPO. There are no baselines that match the token budget using simpler strategies such as best-of-\(N\) sampling with the same total generated tokens, self-consistency/majority voting, or rejection sampling with a likelihood threshold. Without such controls, it is unclear whether the gains come from the specific power-distribution MCMC mechanism or simply from spending more inference compute. The paper acknowledges using "additional compute at inference time" (line 211), but this question deserves direct experimental isolation.

### Minor

3. **No variance or confidence intervals reported.** Table 1 reports point estimates without standard errors, confidence intervals, or multi-run variability. The same applies to Figure 5's pass@k curves. While single-run evaluation is common practice in some LLM benchmarks, the absence of any variance quantification makes it impossible to judge the statistical reliability of the improvements, especially on smaller benchmarks like GPQA (198 questions) and HumanEval (164 problems).

4. **GRPO underperforms the base model on HumanEval for Phi-3.5-mini-instruct without discussion.** In Table 1, GRPO achieves 0.134 on HumanEval vs. the base model's 0.213 for Phi-3.5-mini-instruct — GRPO is *worse* than doing nothing. This is a notable anomaly given that GRPO was trained on MATH (coding-adjacent) data and raises questions about training stability or hyperparameter choice for this model. The paper does not address or explain this.

5. **No MCMC diagnostics reported.** The paper does not report acceptance rates, trace plots, or any convergence diagnostics for the Metropolis-Hastings chain. Given the high-dimensional token space (\(T=3072\)), concerns about mixing time (which the paper itself raises in Section 4.3) are left unexamined. Without these diagnostics, there is no evidence that the chain actually converges to the target distribution \(p^\alpha\) in practice.

### Trivial
None.

## Nice-to-Haves

- **Ablation with simpler sharpening strategies at matched compute:** Compare power sampling to (a) rejection sampling accepting sequences with above-threshold log-likelihoods, and (b) beam search with width matched to compute budget. This would isolate whether the MCMC machinery specifically targeting \(p^\alpha\) is more effective than cheaper alternatives that also spend extra compute pushing outputs toward high-likelihood regions.
- **MCMC acceptance rate and convergence plots:** Reporting these would help validate that the chain actually mixes to \(p^\alpha\) with the chosen \(B\) and \(N_{\text{MCMC}}\).
- **Response length distributions:** The paper notes that power sampling naturally produces longer responses (Section 5.3). A histogram of response lengths across methods would strengthen this observation and help verify that the AlpacaEval 2.0 length-controlled score is not being confounded.
- **Apply to larger (70B-class) models** to confirm scaling behavior and rule out model-specific artifacts.

## Removed Points

These points from the reviewers are removed with justification:

- **"pass@k decreases after k=15 for GRPO — impossible with standard definition"** — Removed as factually wrong. The table in Figure 5 shows GRPO pass@k monotonically non-decreasing (0.89 → 0.90 → 0.90), consistent with the standard definition. The critic misread the table.
- **"AlpacaEval 2.0 scores may be confounded by response length"** — Removed. The paper explicitly states (line 274) that AlpacaEval 2.0 uses a "win rate ... normalized for the length of the model response" (length-controlled win rate), directly addressing this concern.
- **"Base models not instruction-tuned, making AlpacaEval an odd benchmark"** — Removed. Evaluating base models is the entire point of the paper (testing whether latent capabilities exist without instruction tuning). This is not a weakness.
- **"Computing \(p_{\text{prop}}(\mathbf{x}|\mathbf{x}')\) in acceptance ratio is insufficiently specified"** — Removed. The symmetry argument in the paper (line 189) is standard for MCMC with random-resampling proposals: both forward and backward proposal probabilities for resampling at index \(m\) are the product of conditional probabilities from the proposal LLM, which is straightforward to compute. This is not a reproducibility barrier for an audience familiar with MCMC.
- **"Mixing time concerns make convergence an unverified assumption"** — Weakened. The paper acknowledges this concern (Section 4.3) and proposes the blockwise intermediate-distribution approach to mitigate it. The practical concern is real, which is why I retain the "no MCMC diagnostics" point as a Minor weakness, but the a priori theoretical concern does not independently undermine the paper.
- **"Observation 1 is speculative and not experimentally validated"** — Removed. Observation 1 is a conceptual interpretation of the difference between power and low-temperature sampling, supported by a concrete worked example (Example 1) and a formalization in Appendix A.2. It is the motivating intuition, not an empirical claim requiring experimental verification.
- **"GRPO results are from a different source — are they the same checkpoints?"** — Removed. The paper explicitly states (line 276) that GRPO baselines use the implementation and default hyperparameters from Shao et al. (2025) for Qwen models, and hyperparameters from Abdin et al. (2024) for Phi-3.5. The source is properly cited.
- **"Pass@k may need the unbiased correction formula"** — Removed. The paper uses the standard empirical definition ("correct if at least one of k samples is accurate"), which is a valid estimator when k independent samples are drawn per problem. The unbiased correction (from the original pass@k paper) is needed only when estimating from n>k samples, which is not the setting here.
- **"Low-temperature comparison is not compute-matched"** — Merged into Major weakness #2 (compute-controlled baselines). This is a specific instance of the broader compute-baseline issue, not a separate weakness.
- **"AlpacaEval 2.0 scores span a wide range without explanation"** — Removed. Different models naturally produce different quality responses; the wide range simply reflects the different capabilities of the base models used. No further explanation is needed.
- **"All baselines missing (best-of-N, self-consistency, beam search, rejection sampling)"** — Merged into Major weakness #2 (compute-controlled baselines).
- **"The claim that base models are smarter than you think collapses into 'spending more compute'"** — Not removed, but substantially weakened below the original framing. See Major weakness #2 for the actual concern. The claim does not "collapse" because (a) the paper's comparison to GRPO is about training-free vs. training-based quality, not compute efficiency, and (b) the diversity advantage (pass@k) is a distinct benefit that does not automatically follow from spending more compute. The compute-baseline gap is real but the reviewer's framing exaggerates it.
- **Strength from Strength Finder: "Analyses show power sampling naturally produces longer traces"** — Removed as a minor observation unsuited for a top-tier strength. It is a descriptive finding, not a core claim.
- **Strength from Strength Finder: "Quantifies computational cost via Equation (12)"** — Removed because the quantification is incomplete without specifying \(N_{\text{MCMC}}\), which is itself missing from the paper.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the same set of issues (missing \(N_{\text{MCMC}}\), compute-controlled baselines, no error bars) and the same strengths (theoretical insight, empirical competitiveness, diversity preservation). There is no genuinely novel observation that emerges from synthesizing the reviews beyond what the paper itself communicates.

## Suggestions

1. **Specify \(N_{\text{MCMC}}\) for all experiments** in the main text. This is the single most important fix for reproducibility.
2. **Add compute-matched baselines:** best-of-\(N\) sampling with \(N\) chosen to match the total tokens generated by Algorithm 1. Even a single such comparison (e.g., on MATH500 with Qwen2.5-Math-7B) would substantially strengthen the attribution of gains to the power-distribution mechanism rather than raw compute.
3. **Report variance:** bootstrap confidence intervals or standard errors over multiple seeds for Table 1 results, particularly for smaller benchmarks (HumanEval, GPQA).
4. **Explain the anomalous GRPO result** on HumanEval for Phi-3.5-mini-instruct (GRPO 0.134 < base 0.213).
5. **Add MCMC diagnostics:** report acceptance rates for the Metropolis-Hastings steps in Algorithm 1, and verify convergence via log-likelihood trace plots for a representative sample.

## Score and Decision

The paper makes a genuine conceptual contribution (distinguishing power distribution sampling from low-temperature sampling as a target for reasoning), designs a clever algorithmic framework to approximate it, and shows compelling empirical results across multiple models and tasks. The main concerns — missing \(N_{\text{MCMC}}\), lack of compute-controlled baselines, and no variance reporting — are significant but addressable and do not invalidate the core claims. The paper's contribution is solid, and the weaknesses are typical of a first submission that can be straightforwardly fixed.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>