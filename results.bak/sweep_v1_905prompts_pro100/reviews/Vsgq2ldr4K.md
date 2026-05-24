Now I have all the information I need. Let me compile the final review.

---

## Summary

This paper proposes a training-free sampling algorithm that elicits strong single-shot reasoning from base LLMs by sampling approximately from a power distribution p^α via a progressive Metropolis-Hastings MCMC procedure. The key insight is that RL posttraining can be understood as "distribution sharpening," and that a base model's sharpened distribution p^α — which the paper carefully distinguishes from low-temperature sampling (Proposition 1) — already contains high-quality reasoning traces. Across three model families and four benchmarks (MATH500, HumanEval, GPQA, AlpacaEval 2.0), the method achieves single-shot performance approaching GRPO on in-domain tasks and outperforming it on out-of-domain tasks, while crucially preserving pass@k diversity that GRPO collapses.

## Strengths

- **Genuinely novel theoretical distinction between power distribution sampling and low-temperature sampling.** Proposition 1 and the worked Example 1 cleanly demonstrate that low-temperature sampling (exponent-of-sums) is not equivalent to sampling from p^α (sum-of-exponents), and Observation 1 articulates why this matters for reasoning — p^α upweights tokens with few but high-likelihood future paths, helping avoid critical-window failures. This is a crisp, self-contained contribution.

- **Well-designed progressive MCMC algorithm that exploits autoregressive structure.** Algorithm 1 uses a sequence of intermediate distributions to avoid the exponential mixing times that plague high-dimensional MCMC, and the expected token cost formula (Eq. 12) transparently captures the compute-quality tradeoff. The algorithm is clean and the MH construction with random resampling proposals is principled.

- **Broad and consistent empirical validation.** The method is evaluated across three distinct model families (Qwen2.5-Math-7B, Qwen2.5-7B, Phi-3.5-mini-instruct) and four benchmarks spanning math, code, science, and general helpfulness. Gains are substantial and near-universal: +25.2% MATH500 on Qwen2.5-Math, +51.9% HumanEval on Phi-3.5-mini, and consistent AlpacaEval improvements.

- **Important pass@k diversity finding with clear practical implications.** Figure 5 shows that power sampling preserves the base model's pass@k curve (saturating near 98% by k=16) while GRPO stagnates at ~90%. This directly addresses the known diversity-collapse problem of RL posttraining and demonstrates a "best of both worlds" property: near-RL single-shot performance without sacrificing multi-shot potential.

## Weaknesses

### Fatal

None.

### Major

- **Missing compute-matched inference baselines.** The paper frames power sampling as an inference-time compute scaling method (Eq. 12 estimates ~N_MCMC·T²/4B tokens per sample, which is substantially more than a single forward pass), but provides no comparison to alternative ways of spending that same token budget. Natural baselines include best-of-N low-temperature sampling (selecting the sample maximizing p^α), majority voting over low-temperature samples, or simply generating many low-temperature trajectories. Without these, the reader cannot determine whether the gains stem specifically from the MCMC procedure sampling approximately from p^α, or from any method that expends more inference compute. This matters because the paper's central narrative is that the power distribution — not just extra compute — is what elicits reasoning.

### Minor

- **N_MCMC value not reported.** The paper treats N_MCMC as a hyperparameter in Algorithm 1 and derives the token cost formula in terms of it, but never states what value was used in experiments. The paper only says it finds a B that works for "relatively small values of N_MCMC" — this is insufficient for reproducibility and makes the compute cost opaque.

- **No MCMC convergence diagnostics.** The paper does not track whether the chain is actually mixing toward p^α — no acceptance rates, no effective sample size estimates, no tracking of p^α(x) over MCMC steps. While the empirical results are positive, such diagnostics would substantiate the claim that the method is sampling from the intended distribution rather than performing local hill-climbing.

- **Algorithm 1 contains a notation error.** Line 7 computes the acceptance ratio using π_k, but at that stage sequences x and x' have length (k+1)B and the target should be π_{k+1}. This is likely a typo (the text on line 225 correctly says "we wish to sample from π_{k+1}") but should be corrected.

- **GRPO baselines are math-specialized; out-of-domain framing could be more precise.** The paper acknowledges (line 276) that GRPO models were posttrained "on the MATH training split," so HumanEval and AlpacaEval are genuinely out-of-domain. However, the abstract and introduction could more explicitly note that the "outperformance" is relative to a deliberately math-specialized RL baseline, not a general-purpose one. The paper already uses the terms "in-domain" and "out-of-domain," which helps, but a sentence clarifying this tradeoff would improve accuracy.

- **No hyperparameter sensitivity analysis.** The choices of α=4.0, B=192, and the AlpacaEval-specific proposal temperature τ=0.5 are stated but not ablated. Showing how performance varies with these choices (especially α) would strengthen confidence that the reported numbers aren't cherry-picked.

### Trivial

None.

## Nice-to-Haves

- Confidence intervals or multiple random seeds for the main results, particularly given the stochastic MCMC sampler and modest dataset sizes (MATH500 has 500 questions, GPQA Diamond has 198).
- A Limitations section discussing (i) the computational overhead relative to single-pass inference, (ii) the requirement for full-sequence likelihood computation (which may not be available via API), and (iii) scenarios where base model likelihood may not correlate with reasoning quality.
- Compute-matched pass@k curves showing whether best-of-N low-temperature sampling also preserves diversity or whether this property is unique to the MCMC approach.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about q(x|x') computation feasibility through APIs** — REMOVED. The paper uses open-source models (Qwen2.5, Phi-3.5-mini) where full token-level probabilities are accessible. This is a speculative concern about API limitations not relevant to the paper's experimental setup.
- **Demand for "other inference-time scaling methods" comparison (tree search, guided decoding, self-consistency)** — REMOVED as a standalone weakness and merged into the compute-matched baseline concern. The core issue is compute normalization, not comparing against every inference method in the literature.
- **Criticism that the gap between power sampling and low-temperature is "modest" (5.8pp)** — WEAKENED. A 5.8pp improvement on MATH500 from a training-free method is substantively meaningful and not "modest." This is retained only insofar as compute-matching would clarify whether the gap widens or closes.
- **"Ethical and broader-impact considerations are not discussed"** — REMOVED. Not standard for a methods paper in this area, and the paper's use of existing open-source models at inference time doesn't raise novel ethical concerns beyond the standard energy-cost discussion.
- **Strength Finder's claim that "the choice of block size B and MCMC steps is empirically justified"** — REMOVED. The paper does not actually report N_MCMC or provide ablations for B, so this claimed strength is not supported by the text.

## Novel Insights

Beyond the paper's own contributions, the most novel insight emerging from the synthesis of reviews is that the pass@k preservation result (Figure 5) may be the paper's strongest contribution, perhaps even more significant than the single-shot performance. The fact that power sampling's pass@k curve not only avoids GRPO's diversity collapse but actually matches the base model's curve while offering much better single-shot performance suggests something deeper: the MCMC procedure may be preserving the support of the base distribution while reweighting it, which is precisely what one would want from a "sharpening" operation that doesn't discard modes. This has implications beyond the current paper — it suggests a general principle for designing inference-time methods that improve quality without sacrificing diversity, and could motivate future work on sampling algorithms that provably preserve distributional support.

## Suggestions

- The strongest single improvement would be a compute-matched comparison: pick a total token budget (e.g., the expected tokens from Eq. 12 for your chosen N_MCMC), allocate it to best-of-N low-temperature sampling with p^α-based selection, and report single-shot accuracy. If power sampling still wins, that substantially strengthens the claim. If it doesn't, the paper's framing needs adjustment but the method may still be valuable for its pass@k properties.
- Report N_MCMC explicitly and provide at minimum the acceptance rate of the MCMC chain, which is trivial to log and would give readers confidence in convergence.
- Fix the π_k → π_{k+1} notation in Algorithm 1, line 7.

## Score and Decision

**Originality:** High. The theoretical distinction between power distribution and low-temperature sampling is crisp, and applying MCMC to sample from p^α of a base LLM is a creative synthesis of ideas from Bayesian inference and LLM reasoning.

**Importance:** High. The question of whether base models already contain strong reasoning capabilities is central to current debates about RL posttraining. A positive answer, even partial, would shift how the community thinks about training vs. inference compute.

**Claim support:** Moderate-to-strong. The empirical results consistently show improvements over base and low-temperature sampling across diverse benchmarks. The central weakness — missing compute-matched baselines — leaves open whether the MCMC procedure specifically or just extra inference compute drives the gains, but does not invalidate the core finding that base models can be made to reason much better without training.

**Soundness:** The methodology is principled but the experimental protocol has gaps (missing N_MCMC, no sensitivity analysis, no MCMC diagnostics). These are addressable.

**Clarity:** Well-written with clear mathematical exposition. The Proposition 1 proof is easy to follow and the algorithm is well-specified (modulo the π_k notation issue).

**Value to community:** The idea that base models contain untapped reasoning accessible through better sampling is likely to influence both the sampling and RL posttraining communities, regardless of whether this specific MCMC algorithm becomes the standard approach.

### Anchor comparison

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| sdpVfWOUQA (MCTS Planning) | 3.00 | R1 | Much weaker — fundamental methodological issues, confused claims |
| 0xUEBQV54B (LLM Monkeys) | 5.00 | R1 | Weaker — narrow contribution (coverage curves), limited novelty |
| VNckp7JEHn (Inference Scaling Laws) | 5.75 | R1/R2 | Weaker — mostly empirical, math-only, modest novelty |
| HHKboqbkec (Bayesian ToM) | 5.75 | R2 | Different domain, not directly comparable |
| Ze4aPP0tIn (TSMC for Math) | 6.60 | R2 | Similar quality — novel SMC method but narrower eval (2 math benchmarks), needs trained reward model. Paper under review is broader in scope and fully training-free |
| IssPhpUsKt (Rep Engineering) | 6.80 | R2 | Different approach, comparable quality |
| nnVO1PvbTv (Think-on-Graph) | 7.00 | R2 | Different paradigm (KG-augmented), comparable quality |
| 7xCSK9BLPy (MBR Decoding) | 7.33 | R2 | Slightly stronger — better experimental rigor, thorough ablations, but less novel method |
| xoXn62FzD0 (SMC for LLMs) | 8.00 | R1 | Stronger — cleaner evaluation, more thorough ablations |
| FBkpCyujtS (min-p Sampling) | 8.50 | R1 | Stronger — simpler but highly influential, strong adoption evidence |

**Round 1 bracket:** 5.0–8.0. The paper is clearly stronger than the weak/middle anchors (LLM Monkeys at 5.0, Inference Scaling Laws at 5.75) but below the strong SMC anchor at 8.0.

**Round 2 narrowing:** The TSMC paper (6.60) and MBR paper (7.33) are the closest comparators. The paper under review has broader evaluation than TSMC and greater novelty than MBR, but weaker experimental rigor than MBR. It sits between them, closer to the top of that range due to genuinely novel theoretical contribution and the important pass@k diversity finding.

**Final score: 7.0.** The paper makes a novel, well-motivated contribution with broad empirical support. The experimental gaps (missing compute-matched baselines, unreported N_MCMC, missing diagnostics) are real but addressable and do not undermine the central contributions. This is a solid accept.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>