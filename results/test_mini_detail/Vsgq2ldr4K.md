Now I have enough calibration data. Let me write the consolidated review.

**Round 1 bracket**: I placed the paper between 3 and 7 (weak anchors at ~3, strong anchors at ~8). My explicit bracket: between 4 and 6.5.

**Round 2 narrowing**: I pulled anchors in (4.5, 6.5) and (5.0, 7.5). The most comparable papers are Hint Marginalization (5.75, Reject), Flow of Reasoning (5.75, Reject), and Inference Scaling Laws (5.75, Poster). The paper under review has a stronger theoretical contribution than Hint Marginalization but weaker experimental rigor. It has a more novel core idea than Inference Scaling Laws but lacks the compute-equivalent analysis and error bars of that paper.

**Final score**: 5.0. The paper sits at the boundary — the theory/algorithm contribution is interesting but the experimental evaluation has multiple gaps (missing N_MCMC, no inference-time baselines, no compute cost analysis, GRPO data asymmetry) that prevent it from reaching the 6+ range of accepted posters.

---

## Summary

This paper proposes a training-free inference-time sampling method — "power sampling" via MCMC — that samples from a sharpened version of a base LLM's distribution ($p^\alpha$) to elicit reasoning capabilities. The key theoretical insight is that the power distribution is distinct from low-temperature sampling (Proposition 1), and that it preferentially upweights tokens with few but high-likelihood future paths — a behavior suited for reasoning. The paper introduces a block-wise Metropolis-Hastings algorithm (Algorithm 1) that makes power distribution sampling tractable for long sequences, and shows across three base models and four benchmarks that this approach achieves single-shot reasoning performance competitive with GRPO-based RL posttraining, while preserving generation diversity.

## Strengths

1. **Clean theoretical distinction between power distribution and low-temperature sampling (Proposition 1, Section 4.1).** The paper proves that low-temperature sampling does *not* sample from $p^\alpha$, and provides a concrete example (Example 1) showing that the power distribution preferentially upweights tokens with few but high-likelihood future paths — a behavior that the authors argue is valuable for reasoning. This formalizes a gap that was implicit in prior work and directly motivates why a dedicated MCMC sampler is needed.

2. **Empirical results across multiple models and benchmarks (Table 1).** The paper tests three base models (Qwen2.5-Math-7B, Qwen2.5-7B, Phi-3.5-mini-instruct) on four benchmarks (MATH500, HumanEval, GPQA, AlpacaEval 2.0). On MATH500 (the GRPO training domain), power sampling achieves 74.8% vs GRPO's 78.5% for Qwen2.5-Math — a credible "nearly match" result. On out-of-domain tasks, power sampling consistently outperforms GRPO (e.g., HumanEval: 57.3% vs 53.7% for Qwen2.5-Math). These results are presented with a low-temperature sampling baseline, showing a clear improvement over that as well.

3. **Diversity preservation is convincingly demonstrated (Figure 5, Section 5.3).** The pass@$k$ curves show that power sampling continues to improve with more samples (reaching ~98% at $k=16$), while GRPO saturates at ~90%. This directly addresses the known diversity-collapse problem of RL posttraining and shows that power sampling achieves strong single-shot performance *without* sacrificing multi-shot coverage.

4. **Practical algorithm design for high-dimensional token spaces (Algorithm 1, Section 4.3).** The block-wise MCMC procedure with intermediate distributions (Equation 10) is a sensible engineering contribution that avoids exponential mixing times by progressively extending the sequence length. This makes a theoretically intractable target ($p^\alpha$ over sequences up to 3072 tokens) practically feasible.

## Weaknesses

### Fatal
None.

### Major

1. **Missing critical hyperparameter: N_MCMC (number of MCMC steps per block).** Algorithm 1 takes $N_{\text{MCMC}}$ as an input hyperparameter, and Equation (12) shows that total token cost scales as $O(N_{\text{MCMC}} \cdot T^2/B)$. However, Section 5.1 reports $B=192$, $T_{\max}=3072$, and $\alpha=4.0$, but **never states what $N_{\text{MCMC}}$ was used** in any experiment. Without this value, the results are not reproducible and the computational cost of the method is unknowable. Even moderate $N_{\text{MCMC}}$ (say 10–100) implies hundreds of thousands to millions of additional forward tokens per output sequence — a cost that could easily dwarf simpler inference-time methods. This is a structural omission that must be resolved.

2. **No comparison to other inference-time methods.** The paper compares power sampling only to GRPO (a training-based method) and low-temperature sampling. It does **not** compare against standard inference-time baselines such as best-of-N sampling (with or without a verifier), self-consistency, majority voting over multiple samples, or any other MCMC-based controlled generation method (e.g., Zhao et al. 2024, Faria et al. 2024, which are cited in the related work). Since the proposed method is itself inference-time, these are the natural competitors. If a simpler approach like sampling 16 times with majority voting already matches power sampling's single-shot accuracy at lower cost, the claimed advantage would collapse. The paper must address this to demonstrate that its specific MCMC procedure is better than simpler alternatives.

3. **GRPO baseline trained only on MATH creates an asymmetric comparison.** The GRPO baseline is posttrained **only on the MATH training set**. When power sampling "outperforms" GRPO on HumanEval (coding) and AlpacaEval 2.0 (general helpfulness), this is partly expected: GRPO has not seen any coding or general-domain training data, while power sampling draws from the base model's full pretraining distribution. The paper frames this as "out-of-domain generalization" but does not sufficiently caveat the "outperform" claims in the abstract and conclusion. At minimum, the authors should clearly state that the GRPO baseline is a MATH-only model and that out-of-domain comparisons favor power sampling by design. A stronger evaluation would include a GRPO model trained on a diverse task mixture.

4. **No compute-cost analysis beyond a token-count formula.** The paper acknowledges the token cost formula (Equation 12) and qualitatively describes the compute tradeoff, but provides **no actual measurements of runtime, FLOPs, or relative inference cost** for the reported results. Given that GRPO requires hours of training but then only a single forward pass per test sample, while power sampling may require thousands of forward passes, a meaningful comparison must account for total compute. Without this, it is unclear whether the method's gains are simply an artifact of spending orders of magnitude more computation than the baseline.

5. **Phi-3.5-mini-instruct GRPO baseline appears ineffective.** On MATH500, the GRPO model for Phi-3.5 achieves only 40.6% vs the base model's 40.0% — a negligible improvement that suggests the RL training did not converge properly (the paper notes using hyperparameters that "avoids training instabilities," which itself suggests instability was a known issue). This means the Phi-3.5 "outperform" comparisons (e.g., HumanEval: 73.2% vs 13.4%) may simply reflect a broken baseline rather than a meaningful advantage of power sampling. The authors should either explain this discrepancy or exclude the Phi-3.5 GRPO comparisons.

### Minor

1. **No error bars or statistical significance reported.** All results in Table 1 and Figure 5 are point estimates. Several performance differences are small (e.g., GPQA: 38.9% vs 39.9% for Qwen2.5-Math), and it is unclear whether these are within noise. Given that MCMC sampling introduces additional randomness from acceptance/rejection decisions, error bars would be especially informative.

2. **No analysis of acceptance rates or MCMC mixing diagnostics.** The MCMC acceptance ratio $A$ (Equation 9) determines how effectively the chain explores the target distribution. The paper does not report acceptance rates, convergence diagnostics, or any measure of how well the chain mixes. Without this, it is unclear whether $N_{\text{MCMC}}$ is adequate or whether the chain is merely proposing and rejecting candidates near its initialization.

3. **Missing ablation of $N_{\text{MCMC}}$ and block size $B$.** The paper sets $B=192$ (derived from $T/16$) but provides no ablation showing how performance varies with $B$ or $N_{\text{MCMC}}$. These are the primary hyperparameters controlling the compute-quality tradeoff, and their effects are uncharacterized.

4. **Prompting strategy for baselines is not described.** The paper does not specify what prompting strategy (e.g., chain-of-thought, zero-shot) was used for the base model and GRPO baselines. If the base model is evaluated without CoT prompting while GRPO uses it, the comparison could be confounded.

### Trivial
None.

## Nice-to-Haves
- The paper could discuss the specific failure modes or tasks where power sampling underperforms, rather than only showing positive results.
- Training GRPO on a diverse task mixture (MATH + HumanEval) would make the comparison more equitable.
- A comparison with zero-shot CoT prompting for the base model baseline would clarify the prompting setup.

## Removed Points

- **Internal coherence (motivation vs. results):** The critic argued that Figure 4 and 5 show power sampling produces a different distribution from GRPO, contradicting the paper's sharpening hypothesis. However, the paper never claims power sampling *replicates* the GRPO distribution — it claims it achieves comparable *accuracy* while preserving diversity. The broader distribution (Figure 4) and continued pass@k improvement (Figure 5) are presented as *features*, not bugs. → **Removed** — misunderstanding of the paper's claims.

- **MCMC irreducibility concern (Section 4.2):** The critic argued the proposal distribution may not be irreducible. However, the paper notes that "with some probability we can always resample as early as the beginning of $x$," and the proposal LLM $p_{\text{prop}}$ with temperature $1/\alpha > 0$ assigns nonzero probability to every token, ensuring full support. → **Removed** — not a practical concern.

- **AlpacaEval length bias:** The critic claimed AlpacaEval 2.0 scores are length-biased and power sampling's longer outputs inflate its score. However, the paper explicitly states: "The resulting score is a win rate of model responses normalized for the length of the model response." AlpacaEval 2.0 uses length-controlled (LC) win rate by default. → **Removed** — factually incorrect.

- **Pass@k catches up at k=16:** The critic presented this as a weakness. In fact, the paper's claim is that power sampling preserves diversity while improving single-shot accuracy. The fact that base model catches up at $k=16$ shows diversity is preserved — this is consistent with the paper's claims. → **Removed** — mischaracterized strength.

- **Cherry-picked qualitative example:** The paper shows one example in Table 2. Single qualitative examples are standard practice in LLM papers and do not constitute a weakness. → **Removed**.

- **Missing related works:** Cannot be verified without external sources. → **Removed** per instructions.

## Novel Insights

An interesting observation that emerges from comparing the harsh critic's analysis with the paper's presented data is that the power sampling distribution is *qualitatively different* from the RL-trained distribution in ways the paper does not fully explore. Figure 4 shows power sampling produces outputs with broader likelihood and confidence spread than GRPO (which is highly concentrated), and Figure 5 shows dramatically different pass@k behavior (monotonically increasing vs. saturating). The paper frames these differences as strengths, but they also suggest that the "sharpening hypothesis" — the idea that RL simply sharpens the base distribution — is at best a partial explanation. Power sampling sharpens differently and less aggressively than RL, yet achieves comparable single-shot accuracy. This raises a deeper question the paper does not address: *why* does this particular form of sharpening (via $p^\alpha$) produce reasoning gains, given that it does not mimic RL's distribution? The paper's analysis (Figure 4) hints that correctness correlates with high-likelihood regions, but it does not establish a causal link. Characterizing the precise relationship between power-distribution sampling and reasoning success would be a valuable direction for future work.

## Suggestions

1. **Report $N_{\text{MCMC}}$** for all experiments, along with the resulting average token cost per output. This is the single most important missing detail.
2. **Add comparisons to inference-time baselines** — at minimum best-of-N, self-consistency (majority voting), and repeated random sampling with simple aggregation. This would establish that the MCMC machinery is providing a genuine benefit over simpler alternatives.
3. **Report error bars** (e.g., bootstrap confidence intervals or standard deviations across multiple runs) for all main results, especially where performance differences are small.
4. **Provide an ablation study** showing how performance and token cost vary with $N_{\text{MCMC}}$ and block size $B$.
5. **Address the Phi-3.5 GRPO anomaly** — either explain why GRPO barely improved over the base model, or present results without that model's GRPO comparisons.
6. **Clearly caveat the GRPO data asymmetry** in the abstract and conclusion. A statement like "GRPO was trained only on MATH, which places it at a disadvantage on out-of-domain tasks" would suffice.
7. **Report MCMC acceptance rates** to characterize chain mixing behavior.

## Score and Decision

**Round 1 bracket**: 4.0 – 6.5. The paper is clearly above the rejected 2–3 range papers in the corpus (weak motivation, thin experiments, ungrounded claims) but below the strong 7.5+ papers (comprehensive evaluation, multiple baselines, error bars, compute analysis).

**Round 2 calibration anchors**: The most comparable papers are Hint Marginalization (5.75, Reject) — which has a similar inference-time sampling approach but was rejected for narrow evaluation — and Flow of Reasoning (5.75, Reject) — which proposes training-based diversity but was rejected for insufficient benchmark demonstration. The paper under review has a stronger theoretical contribution than either (Proposition 1 is a genuine insight) but weaker experimental rigor (missing $N_{\text{MCMC}}$, no inference-time baselines, asymmetric GRPO comparison). It is weaker than the accepted 6+ posters (Inference Scaling Laws at 5.75, Smaller/Weaker at 7.0, Language Model Decoding as Direct Metrics Optimization at 6.25), which all provided more thorough evaluation frameworks.

**Final score**: 5.0. The core idea is novel and the theoretical motivation is solid, but the experimental evaluation has multiple significant gaps that prevent it from meeting the acceptance bar in its current form. The paper would be substantially strengthened by addressing the major weaknesses above, particularly the missing $N_{\text{MCMC}}$, lack of inference-time baselines, and compute-cost analysis.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>