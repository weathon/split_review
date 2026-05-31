## Summary
This paper proposes **Power Sampling**, a training-free inference-time algorithm that approximates sampling from the *power distribution* p^α of a base LLM via Markov Chain Monte Carlo (Metropolis-Hastings with random token resampling). The key hypothesis is that RL post-training merely "sharpens" the base model distribution; by explicitly targeting this sharpened distribution at inference, one can match RL performance without training. Across Qwen2.5-Math-7B, Qwen2.5-7B, and Phi-3.5-mini, power sampling nearly matches or outperforms GRPO on MATH500, HumanEval, GPQA, and AlpacaEval 2.0, while maintaining generation diversity that RL collapses.

---

## Strengths

- **Elegant theoretical framing.** Proposition 1 formally proves that low-temperature sampling does not sample from the power distribution p^α (sum-of-exponents vs. exponent-of-sums distinction). The worked Example 1 makes this distinction concrete and immediately illuminating, connecting it to "pivotal tokens" / "critical windows" phenomena in reasoning.

- **Compelling empirical results.** Table 1 shows +25.2% on MATH500 and +51.9% on HumanEval (Phi-3.5) over the base model, reaching near-GRPO performance training-free. The results are consistent across three model families.

- **Pass@k diversity advantage is a genuine "best-of-both-worlds" result.** Figure 5 is compelling: GRPO's pass@k saturates around 0.90 while power sampling reaches 0.98, matching the base model ceiling. This directly addresses a known, long-standing weakness of RL post-training identified in prior work.

- **Verifier-free scope.** Unlike best-of-N or self-consistency, power sampling requires no external reward signal or output aggregation, enabling it to operate on unverifiable tasks (AlpacaEval 2.0). The consistent outperformance on AlpacaEval is a notable demonstration.

- **Clean sequential annealing strategy.** The block-by-block intermediate distribution annealing (Eq. 10–11) is a sensible and principled way to control MCMC mixing time in a high-dimensional token space. The intuition and algorithm are clearly presented.

---

## Weaknesses

### Fatal
None.

### Major

1. **Missing compute-matched baselines.** The expected token count per sample scales as O(N_MCMC · T²/4B) (Eq. 12). With T=3072 and B=192, this is O(N_MCMC · 12,288) tokens per question — substantially more compute than a single standard inference. A critical missing ablation is: what does Best-of-N sampling from the base model (N chosen to match the same compute budget) achieve? For verifiable tasks (MATH500, HumanEval), best-of-N with a majority vote or oracle selector is a natural strong baseline. Without it, the reader cannot attribute gains to the MCMC exploration vs. simply consuming more compute tokens.

2. **Out-of-domain comparisons against domain-mismatched GRPO.** When the paper claims power sampling "outperforms GRPO on HumanEval (+59.8%)" and AlpacaEval, the RL baseline is GRPO trained exclusively on MATH. This is an inherently unfair comparison for HumanEval and AlpacaEval. Domain-matched GRPO (trained on code for HumanEval, or RLHF for general tasks) could plausibly exceed power sampling in those domains. The paper uses the term "out-of-domain" honestly, but the headline claim of outperforming RL overstates the finding.

3. **Hyperparameter sensitivity unanalyzed.** The three key hyperparameters α, B, and N_MCMC are set to α=4, B=192, N_MCMC not reported directly, with separate values for AlpacaEval. No ablation is provided to assess sensitivity. The performance claim depends entirely on an undisclosed N_MCMC; reporting it and showing robustness to variation is essential.

### Minor

1. The claim that MCMC convergence holds under the stated proposal is theoretically justified (irreducibility + aperiodicity), but there is no empirical convergence diagnostic showing that the chain has mixed in the block sizes used. Autocorrelation plots or acceptance rate statistics would strengthen the MCMC validity argument.

2. Only 7B-scale models are evaluated. Whether the method scales beneficially to larger models (where base capabilities are stronger) or degrades is unknown.

3. The single-shot evaluation protocol for power sampling (which internally uses many model calls) is not entirely analogous to a true "single shot" — the framework conflates inference-time compute with single-output appearance. Clearer terminology (e.g., "single-output" vs. "single inference call") would avoid confusion.

### Trivial
None worth listing.

---

## Nice-to-Haves

- Include explicit wall-clock time or FLOPs per question for power sampling vs. GRPO inference, enabling practitioners to assess the practical compute tradeoff.
- Report N_MCMC explicitly and provide a pass@1 accuracy vs. N_MCMC scaling curve to validate inference-time scaling behavior.
- A comparison against self-consistency (majority voting at matching compute budget) on MATH500 and HumanEval would contextualize where the gains come from.

---

## Novel Insights

The central novel insight — that the power distribution p^α is the *correct* formal target for distribution sharpening, and that low-temperature sampling is demonstrably *not* equivalent to it — is sharp and underappreciated. The proof hinges on a fundamental asymmetry: low-temperature sampling exponentiates marginal probabilities (which average over future paths), while the power distribution exponentiates full-sequence probabilities (which account for individual futures). This distinction means the power distribution implicitly encodes look-ahead preferences, biasing early tokens toward those with *few, high-probability futures* rather than *many, mediocre futures* — a property that directly maps onto the "pivotal token" failure mode identified in reasoning literature. This reframes the discussion around inference-time compute: rather than "run more samples and aggregate," the right question is "which single sequence should we select?" The MCMC framework operationalizes this distinction without requiring a verifier, which is the paper's most practically impactful contribution.

---

## Suggestions

- Report N_MCMC and provide a brief sensitivity analysis for α ∈ {2, 4, 8} and N_MCMC ∈ {5, 10, 20} to help future practitioners adopt the method.
- Add a compute-matched best-of-N baseline (or self-consistency) that uses the same total token budget to properly isolate the contribution of MCMC exploration.
- Clearly distinguish "single output" from "single inference call" in the evaluation framing to prevent misinterpretation.

---

## Score and Decision

The paper makes a genuinely surprising and theoretically grounded claim: training-free MCMC-based power sampling can match RL post-training. The Proposition 1 insight is clean, the empirical results are strong, and the diversity preservation result is directly applicable to a known RL weakness. The two major weaknesses — missing compute-matched baselines and the misleading out-of-domain comparisons against domain-mismatched GRPO — are substantive but do not invalidate the core contribution. The method's verifier-free applicability is particularly notable for unverifiable settings. On balance, this paper offers enough new knowledge to the community to merit acceptance.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>