Now let me run calibration searches to anchor the score.Now I have enough calibration data. Let me synthesize everything into the final review.

---

## Summary

This paper proposes **Power Sampling**, a training-free, dataset-free, verifier-free inference-time algorithm for eliciting reasoning from base LLMs. The method targets the "power distribution" p^α, which upweights high-likelihood sequences more aggressively than low-temperature sampling (proven formally in Proposition 1), and approximates sampling from it via a block-wise Metropolis-Hastings MCMC procedure. Empirically, across three base model families (Qwen2.5-Math-7B, Qwen2.5-7B, Phi-3.5-mini-instruct) and four benchmarks (MATH500, HumanEval, GPQA, AlpacaEval 2.0), the method nearly matches GRPO on in-domain MATH reasoning and outperforms it on out-of-domain tasks, while preserving generation diversity (pass@k).

---

## Strengths

1. **Proposition 1 and Example 1 constitute a concrete, non-trivial theoretical contribution.** The formal proof that low-temperature sampling ≠ power distribution sampling (via the "exponent of sums" vs. "sum of exponents" distinction in Eqs. 7–8) is immediately useful for practitioners who have assumed these are equivalent. Example 1 makes this tangible with a two-token vocabulary where p^α prefers token `a` while p_temp prefers `b`.

2. **The block-wise MCMC algorithm (Section 4.3, Algorithm 1) cleanly addresses the dimensionality problem.** Rather than running a single Markov chain over T=3072-length sequences, it uses sequentially growing intermediate distributions π_k over prefixes of length kB, so each MCMC stage starts from a well-initialized warm chain. This is a principled design choice that reduces the effective dimension of each sampling problem.

3. **Empirical breadth across model families and benchmarks is solid.** Table 1 covers three structurally different base models (math-specialized, general-purpose, instruction-tuned) and four diverse evaluation domains including a non-verifiable LLM-judged task (AlpacaEval 2.0), making the results difficult to attribute to a lucky model-benchmark pairing.

4. **The method generalizes beyond verifiable domains.** On AlpacaEval 2.0, power sampling outperforms GRPO across all three model families (Table 1), demonstrating applicability outside the curated math datasets on which RL is typically trained. This is a genuine advantage that the paper articulates clearly.

5. **The likelihood/confidence histograms in Figure 4 provide mechanistic insight.** The observation that power sampling outputs cluster in a similarly high-likelihood region as GRPO outputs (with more distributional spread) directly tests the "distribution sharpening" hypothesis motivating the method, and Figure 5's pass@k curves confirm that diversity is preserved while single-shot accuracy improves.

---

## Weaknesses

### Fatal

*None.* The core claim that the power distribution is a useful inference-time target for reasoning, and that MCMC can approximately sample from it, is supported by both theory (Proposition 1) and empirical results (Table 1). No individual issue invalidates the paper's contribution entirely.

### Major

1. **N_MCMC is never stated in the main text, making the compute cost per output completely unquantifiable.** The paper itself derives (Eq. 12) that expected token generation scales as N_MCMC · T²/(4B). With T=3072 and B=192 (Section 5.1), this gives N_MCMC · 12,288 tokens per output — but N_MCMC is never given. A reader cannot determine whether power sampling uses 5× or 500× more inference compute than a single GRPO forward pass. The framing "training-free" is technically accurate but elides that the training cost may be replaced by a potentially enormous per-query inference cost. The paper's central comparison — training cost versus inference cost — requires this number to be interpretable. Every result in Table 1 and Figure 5 is difficult to contextualize without it.

2. **The Phi-3.5-mini-instruct GRPO baseline is a clearly suboptimal trained model, weakening one of three key comparisons.** Table 1 shows GRPO reduces HumanEval from 0.213 (base) to 0.134 — a 37% regression — while improving MATH500 by only 0.6 percentage points. The paper acknowledges "training instabilities" and mentions using "hyperparameters that avoid training instabilities and converge to improvement over a large number of epochs" (Section 5.1), but the resulting model is plainly degraded on coding. Outperforming this collapsed baseline on HumanEval (+59.8% headline claim) does not constitute evidence that power sampling outperforms properly-trained GRPO. Two of three model families (Qwen2.5) have credible GRPO baselines; the Phi-3.5 comparison does not.

### Minor

1. **The pass@k diversity comparison (Figure 5, Section 5.3) is compute-asymmetric without acknowledgment.** Each of the k samples for power sampling involves a full MCMC chain with O(N_MCMC · T²/4B) generation cost, while k GRPO samples require k simple forward passes. The figure caption presents GRPO's lower pass@16 (0.90 vs. 0.98) as evidence of "diversity collapse," but this advantage may partly or fully reflect that power sampling is allocated far more total compute per question at high k. The paper should either equalize total compute or explicitly flag this asymmetry.

2. **The abstract and introduction overstate the out-of-domain results.** The abstract says the method "matches and even outperforms" RL; Section 5.2 reports "outperforms on HumanEval by up to +59.8%." However, GRPO is trained only on the MATH training split (Section 5.1), so HumanEval and GPQA are out-of-domain for GRPO. A math-trained RL model underperforming on coding is expected, not surprising. The paper does acknowledge the distinction ("in-domain reasoning" vs. "out-of-domain") in Figure 1's caption and Section 5.2, but this caveat is not adequately carried forward into the framing of abstract, introduction, or headline numbers.

3. **No statistical significance reporting on any result.** GPQA Diamond has only 198 questions; a 1-percentage-point difference corresponds to ~2 questions. The Qwen2.5-7B MATH500 gap (GRPO: 0.740, ours: 0.706) is described as "on par" without any test of whether the 3.4pp difference is within noise. With 500 MATH questions and a binomial model, a 3.4pp gap is in fact statistically significant (p < 0.05), which would mean GRPO actually *wins* on the in-domain benchmark — but the paper does not address this.

4. **No MCMC convergence diagnostics.** The paper correctly identifies that exponential mixing times are a risk for high-dimensional discrete MCMC (Section 4.3), then resolves this with the block decomposition — but provides no empirical evidence that the chain has actually mixed. Acceptance rates, trace plots of sequence log-likelihood over MCMC steps, or autocorrelation estimates would substantiate the convergence claim. Without these, the algorithm's performance could plausibly be dominated by the quality of the GRPO-temperature-proposal initialization rather than MCMC mixing.

### Trivial

- The AlpacaEval 2.0 results use a different proposal temperature (τ=0.5 instead of 1/α) with no ablation; this is a minor transparency issue noted in passing in Section 5.1 but not quantified.

---

## Nice-to-Haves

- A plot of accuracy vs. total token generation budget (for both power sampling and GRPO amortized over calls) would be the single most impactful addition, converting a qualitative "training-free is good" claim into a concrete compute-efficiency result.
- Ablating N_MCMC in the main paper (rather than deferring to the appendix) would directly demonstrate the inference-time scaling behavior and give the missing compute context.
- Acceptance rate curves over MCMC iterations as a proxy for convergence would strengthen the theoretical justification for the block decomposition.
- The AlpacaEval 2.0 LLM-judge comparison is sensitive to response length; a brief discussion of response length distributions for this benchmark would rule out that the power sampling win is a length artifact.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic, "out-of-domain framing as a key weakness"** — partially valid (demoted to Minor above), but the paper does explicitly acknowledge the in/out-of-domain distinction in Figure 1 caption and Section 5.2; the issue is mainly that the abstract and intro don't carry the caveat forward strongly enough.

- **Harsh Critic, "no formal result connecting high-likelihood sequences to correct reasoning"** — removed as scope creep. The paper explicitly frames this as an empirical hypothesis motivated by prior work (He et al., Yue et al.); demanding a formal proof for an empirical systems paper is non-standard. The correlation in Figure 4 is offered as observational evidence, not proof.

- **Harsh Critic, "circularity risk — base model trained on math data"** — speculative. The observation that GRPO outputs are high-likelihood under the base model is explicitly discussed and empirically shown in Figure 4; the paper uses this as support, not a circularity problem.

- **Strength Finder, "block-wise MCMC algorithm addresses exponential mixing"** — partially retained as strength, but downgraded because the claim lacks empirical verification (no convergence diagnostics). Kept as a design-choice strength, not a proven-effectiveness strength.

- **Strength Finder: generic strength about the problem being important** — removed per filtering rules.

---

## Novel Insights

The key genuinely novel insight is the precise distinction between low-temperature sampling and power distribution sampling, formalized in Proposition 1. This is not folklore: the paper provides an explicit proof showing that the conditional weights for next-token prediction under p^α (sum of exponents, Eq. 7) differ fundamentally from low-temperature (exponent of sums, Eq. 8), with the consequence that p^α implicitly accounts for the quality of all future completions when selecting the current token. This connects directly to the "pivotal token" literature and provides a theoretical rationale for why sampling from p^α, rather than low-temperature decoding, should benefit multi-step reasoning. If the compute transparency issues are resolved, this observation could become a widely-cited conceptual contribution to inference-time methods.

---

## Suggestions

1. **Report N_MCMC explicitly** and add a table or figure showing wall-clock time or total tokens generated per output for power sampling vs. GRPO inference. If possible, plot accuracy vs. total inference compute (FLOPs or tokens) with GRPO's training cost amortized over N calls.
2. **Address the Phi-3.5 GRPO run**: either retrain with better hyperparameters (HumanEval should not regress 37%) or explicitly scope the Phi-3.5 comparison out of the "matches GRPO" headline claim.
3. **Add error bars or binomial confidence intervals** on all benchmark results, especially GPQA Diamond (198 questions). Clarify whether the Qwen2.5-7B MATH500 gap (3.4pp) is within noise.
4. **Add acceptance rate or log-likelihood trace plots** for Algorithm 1 to empirically verify that the MCMC chain mixes within N_MCMC steps.
5. **Move the in-domain/out-of-domain caveat to the abstract** so the "outperforms RL" claim is immediately qualified.

---

## Score and Decision

**Calibration anchors:**

| Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| Planning with MCTS for LLMs | sdpVfWOUQA.md | 3.00 | R1 (low) | Much weaker — no novel theory, smaller scope |
| LLM Self-Correction | pTyEnkuSQ0.md | 5.25 | R1 (low) | Weaker — controversial claim without strong empirical grounding |
| LLM Monkeys (repeated sampling) | 0xUEBQV54B.md | 5.00 | R1+R2 (mid) | Weaker — simpler idea (just scaling N), no algorithmic novelty |
| Inference Scaling Laws | VNckp7JEHn.md | 5.75 | R1+R2 (mid) | Comparable — solid empirical study, reports compute carefully, but less algorithmic novelty |
| Inference-aware Fine-tuning BoN | 77gQUdQhE7.md | 5.67 | R2 (mid) | Comparable — more technically complete (reports all hyperparameters), but narrower scope |
| Self-Improvement Sharpening | WJaUkwci9o.md | 8.00 | R1 (high) | Stronger — formal theoretical contributions (minimax optimality), cleaner empirical validation |
| SMC for LLM Control | xoXn62FzD0.md | 8.00 | R1 (high) | Stronger — thorough compute analysis, more controlled ablations, clean theoretical framing |

**Round 1 bracket:** 5–8 (plausibly better than mid-band papers on algorithmic novelty, but clearly below 8.0 papers on rigor and transparency).

**Round 2 narrowing:** The paper is clearly above the 5.0–5.75 anchors (LLM Monkeys, Inference Scaling Laws) due to a stronger algorithmic and theoretical contribution (Proposition 1, block-MCMC design). But it is meaningfully below the 8.0 anchors (SMC control, sharpening mechanism) because: (a) N_MCMC is missing, preventing any compute comparison; (b) one of three GRPO baselines is demonstrably failed; (c) no convergence diagnostics; (d) no statistical significance testing. The out-of-domain framing inflation further weakens the headline claim. The paper sits closer to 6.0–6.5, nearer the top of the mid-band but not at the 8.0 tier.

**Final score: 6.0** — A legitimate and interesting contribution with a clear algorithmic idea and solid empirical scope, but with significant transparency gaps (especially missing N_MCMC) that prevent the central compute-efficiency claim from being assessed. These are addressable in revision, but in the current form the headline claim is not fully supported by the evidence presented.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>