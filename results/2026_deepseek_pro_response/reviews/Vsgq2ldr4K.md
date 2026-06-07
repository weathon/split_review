Now I have enough comparison anchors. Let me compile the final review with score.

**Round 1 Bracket:** 5.5–7.0

**Round 2 Narrowing:**
- Twisted SMC (6.60): Our paper has broader evaluation and cleaner theory; comparable quality but our N_MCMC issue is a specific gap. Slightly below.
- Inference-Aware Fine-Tuning (5.67): Our paper is clearly stronger (more models, more benchmarks, training-free, novel algorithm).
- Inference Scaling Laws (5.75): Our paper is somewhat stronger (novel algorithm, broader benchmarks).

**Final assessment:** The paper's genuine contributions (Proposition 1, MCMC sampling algorithm, consistent gains across 3 model families, pass@k diversity preservation) are substantial. However, the two major weaknesses — opaque reporting of \(N_{\text{MCMC}}\) and absence of compute-matched baselines — prevent it from reaching the 7.0+ tier. The paper lands at **6.0**, above the 5.0–5.75 cluster (which had weaker or less novel contributions) but below the 7.0+ papers (which had more rigorous methodology and fewer reproducibility gaps).

---

## Summary
This paper proposes a training-free, inference-time sampling algorithm that elicits reasoning capabilities from base LLMs by targeting the *power distribution* \(p^\alpha\) via a Metropolis-Hastings MCMC procedure with progressive block-wise resampling. The central empirical finding is that sampling from \(p^\alpha\) can achieve single-shot reasoning performance comparable to GRPO posttraining — and can even outperform GRPO on out-of-domain tasks — while preserving generation diversity that RL methods sacrifice.

## Strengths
- **Clean theoretical contribution (Proposition 1):** The paper provides a crisp proof that low-temperature sampling does not sample from \(p^\alpha\), identifying the "sum of exponents" vs. "exponent of sums" distinction. The worked two-token example (Example 1) makes this concrete and directly motivates why MCMC targeting \(p^\alpha\) should outperform naive temperature scaling.
- **Consistent empirical gains across three model families and four benchmarks (Table 1):** Power sampling lifts MATH500 from 49.6% → 74.8% (Qwen2.5-Math-7B), 49.8% → 70.6% (Qwen2.5-7B), and 40.0% → 50.8% (Phi-3.5-mini-instruct). Gains on HumanEval are even larger. The inclusion of a low-temperature baseline confirms that power sampling provides value beyond simple temperature scaling (e.g., MATH500: 69.0% → 74.8%).
- **Power sampling matches or exceeds GRPO on single-shot reasoning without training (Table 1):** On Qwen2.5-Math-7B, power sampling (74.8%) nearly matches GRPO (78.5%) on in-domain MATH500. On out-of-domain tasks, power sampling outperforms GRPO: HumanEval 57.3% vs. 53.7%, AlpacaEval 2.88 vs. 2.38. The pattern holds across all three models.
- **Pass@k analysis demonstrates preserved generation diversity (Figure 5):** Power sampling pass@k rises from ~0.72 at k=1 to ~0.98 at k=16, tracking the base model's asymptotic performance. In contrast, GRPO plateaus at ~0.90 by k=8. This addresses a known weakness of RL posttraining — redistribution of pass@k into pass@1 at the cost of diversity — and shows power sampling does not suffer from this tradeoff.
- **Longer reasoning traces emerge without explicit length incentives (Section 5.3):** On MATH500 (Qwen2.5-Math-7B), power sampling averages 679 tokens — nearly identical to GRPO's 671 and substantially longer than the base model's 600. That pure sampling from \(p^\alpha\) induces this behavior without reward shaping for length is an intriguing corroboration of the connection between high-likelihood regions and reasoning capability.

## Weaknesses

### Fatal
None.

### Major
- **\(N_{\text{MCMC}}\) is never given a concrete value, making results irreproducible and compute cost opaque.** The paper introduces \(N_{\text{MCMC}}\) as a central hyperparameter in Algorithm 1, provides a formula for expected token cost that depends on it (Eq. 12: \(\mathbb{E}_{\text{tokens}} \approx N_{\text{MCMC}} T^2 / (4B)\)), and describes it as a lever in the \(B\) vs. \(N_{\text{MCMC}}\) tradeoff — yet never reports what value was used in any experiment. The only guidance is the qualitative statement that the method works for "relatively small values of \(N_{\text{MCMC}}\)." This is a straightforward reproducibility failure.
- **No compute-matched baseline — performance gains are confounded with inference-time compute budget.** The headline claim is that base models can match RL "by pure sampling." But power sampling consumes substantially more inference compute than standard decoding (Eq. 12 scales with \(N_{\text{MCMC}}\)), and the paper provides neither wall-clock time, FLOP counts, nor a compute-controlled comparison (e.g., best-of-\(N\) from the base model at equal total token budget). Without such a baseline, one cannot distinguish between "the base model knows more than we thought" and "spending more compute helps." This undermines the central thesis.

### Minor
- **GRPO baseline for Phi-3.5-mini-instruct is minimally informative.** GRPO posttraining produces negligible improvement on MATH500 (0.400 → 0.406) and degrades HumanEval (0.213 → 0.134). The paper attributes this to "out-of-domain" degradation, but the MATH500 result — which is in-domain (trained on MATH) — shows essentially no gain. This suggests the GRPO training for this model did not converge properly, inflating the apparent advantage of power sampling on this model. The other two models show proper GRPO gains, so this does not threaten the overall conclusion but weakens one data point.
- **No sensitivity analysis for key hyperparameters.** The paper states \(\alpha = 4.0\) was found empirically to be "most performant" but provides no sweep. The same applies to \(B\) and \(N_{\text{MCMC}}\). The reader cannot assess how brittle performance is to these choices. The proposal temperature differs between reasoning tasks (0.25) and AlpacaEval (0.5), suggesting task-specific tuning that slightly undercuts the "broadly applicable" framing.
- **The connection between \(p^\alpha\) and RL posttraining remains correlational.** The paper motivates power sampling by the hypothesis that RL sharpens the base distribution, but never tests whether GRPO's output distribution actually resembles \(p^\alpha\) beyond the likelihood histogram in Figure 4. Both methods producing higher-likelihood samples is consistent with many sharpening mechanisms. This does not invalidate the empirical results but means the conceptual narrative remains suggestive.

### Trivial
- **Algorithm 1, line 7 uses \(\pi_k\) instead of \(\pi_{k+1}\) in the acceptance ratio.** The candidate sequences are of length \((k+1)B\) but the target distribution referenced is \(\pi_k\) (defined for length \(kB\)). This is almost certainly a pseudocode typo and should be corrected.
- **No limitations section.** The paper makes strong claims without a dedicated discussion of limitations (white-box access requirement, sensitivity to hyperparameters, computational cost).

## Nice-to-Haves
- A compute-matched baseline (best-of-\(N\) or majority voting at equal token budget) would directly answer whether power sampling extracts more reasoning per unit of compute than simply drawing more samples.
- A controlled synthetic experiment (e.g., a token environment where critical-window tokens are known) to provide causal evidence for the mechanism claimed in Observation 1.
- Reporting wall-clock time alongside accuracy for all experiments.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"Irreducibility argument is misleading" (from Harsh Critic):** The harsh critic claims resampling can only modify tokens within the current block. However, Algorithm 1 line 5 samples \(m \in \{1, \dots, (k+1)B\}\) uniformly, which includes the full prefix — resampling can start from position 1 within each block's MCMC phase. The prefix is only frozen *between* blocks (line 10). The irreducibility argument in the paper is therefore technically correct for each sub-chain. Removed.
- **"Distribution-sharpening narrative is correlational, not causal" rated as fatal:** Demoted to Minor with softening, as the paper uses sharpening as motivation (citing prior work) and makes the empirical claim that power sampling achieves RL-like results — which Table 1 supports regardless of mechanism. The correlational nature does not invalidate the empirical contribution. The harsh critic's framing as a fatal/critical issue was disproportionate.

## Novel Insights
The paper's core insight — that sampling from \(p^\alpha\) via MCMC can recover RL-like single-shot performance while maintaining base-model diversity — is genuinely novel and challenges assumptions about where reasoning capabilities reside. The pass@k analysis (Figure 5) showing that power sampling achieves GRPO-level single-shot accuracy while preserving the base model's asymptotic multi-shot performance is a compelling finding that suggests a new axis for inference-time compute scaling. The Proposition 1 distinction between "sum of exponents" and "exponent of sums" provides a clean theoretical lens that could inform future work on inference-time sampling strategies.

## Suggestions
- Report \(N_{\text{MCMC}}\) explicitly for all experiments and add a compute-matched baseline (e.g., best-of-\(N\) from the base model at equal total token budget). This is the single most important addition.
- Add a brief sensitivity analysis for \(\alpha\), \(B\), and \(N_{\text{MCMC}}\) — even a coarse grid would help readers assess robustness.
- Fix the Algorithm 1 line 7 typo (\(\pi_k \to \pi_{k+1}\)) and add a short limitations paragraph.
- Consider treating the Phi-3.5 results as supplementary given the problematic GRPO baseline, and foregrounding the Qwen2.5 results which are clean and convincing.

## Score and Decision

**Calibration anchors used:**

| Anchor Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| Large Language Monkeys (0xUEBQV54B) | 5.00 | R1 | Our paper is stronger: novel algorithm, theory, broader benchmarks |
| Inference-Aware Fine-Tuning (77gQUdQhE7) | 5.67 | R2 | Our paper is clearly stronger: 3 models vs 1, 4 benchmarks vs 1, training-free |
| Inference Scaling Laws (VNckp7JEHn) | 5.75 | R1/R2 | Our paper somewhat stronger: novel algorithm, broader benchmarks, pass@k analysis |
| COrAL (0JjsZC0w8x) | 5.75 | R2 | Different topic; our paper has broader evaluation |
| Conformal Language Modeling (pzUhfQ74c5) | 6.25 | R2 | Different topic with formal guarantees; less directly comparable |
| Mutual Reasoning (6aHUmotXaw) | 6.25 | R2 | Different approach (MCTS); our paper has cleaner theory |
| Twisted SMC (Ze4aPP0tIn) | 6.60 | R2 | Closest comparator. Both use MC for reasoning, both have compute opacity. Our paper has broader benchmarks and cleaner theory, but N_MCMC gap is a more specific reproducibility issue. Slightly below. |
| Smaller, Weaker, Yet Better (3OyaXFQuDl) | 7.00 | R1/R2 | Our paper is weaker: this paper has rigorous compute-matched design |
| SMC for Controlled Generation (xoXn62FzD0) | 8.00 | R1 | Our paper is clearly weaker: less rigorous methodology, reproducibility gap |

**Round 1 Bracket:** 5.5–7.0  
**Round 2 Narrowing:** The paper sits between Inference Scaling Laws (5.75) and Twisted SMC (6.60), closer to the latter in contribution quality but held back by the unreported \(N_{\text{MCMC}}\) and missing compute-matched baseline. The core idea and results are stronger than the 5.0–5.75 cluster but the reproducibility gap prevents the paper from reaching the 7.0 tier.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>