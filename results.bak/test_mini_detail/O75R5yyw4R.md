## Summary

This paper proposes IterRef, a test-time scaling method for discrete diffusion models that uses Multiple-Try Metropolis (MTM) with noising-denoising transitions to iteratively refine intermediate states toward a reward-aligned distribution. The method is evaluated across three backbones (MDLM, LLaDA-8B for text; MaskGIT for images) on multiple reward-guided generation tasks. IterRef consistently outperforms existing baselines (FK, SVDD, SoP, BoN) at matched compute budgets, often by wide margins, and includes an analysis of which noise levels matter most for discrete diffusion refinement.

## Strengths

- **Consistent and substantial empirical gains across modalities and backbones.** Figure 2 shows IterRef outperforming all baselines on CoLA, Toxicity, Sentiment, and Perplexity across both MDLM and LLaDA-8B. On three of four MDLM tasks, IterRef at 2T NFEs surpasses all baselines at 32T NFEs. The same pattern holds for MaskGIT image generation (Table 1). This breadth of consistent improvement is the paper's strongest evidence.

- **Effectiveness under low compute budgets.** The paper's claim of "8× faster" scaling (Figure 1b) is supported: on Toxicity with MDLM, IterRef at 4T NFEs matches FK at 32T NFEs. This is practically meaningful for resource-constrained applications.

- **Insightful analysis of discrete diffusion dynamics.** Table 2 shows that applying IterRef at later denoising stages (near 0.1T) is most effective, and that evenly-spaced application is not always optimal. This contrasts with continuous diffusion (where early steps dominate) and provides a genuine insight into discrete diffusion behavior.

- **Practical computational strategies.** The pool reuse mechanism (Section 3.3) and selective refinement via effective timesteps reduce overhead without (as claimed) breaking the MTM framework. The separate reporting of generative vs. reward model calls shows practical awareness.

## Weaknesses

### Major

- **No error bars or statistical significance measures for language experiments.** The paper reports only means from what appears to be 3 seeds × 15 prompts × 20 samples = 900 generations per condition (Section 4.1: "3 seed, 15 controllable prompts, each sampled 20 times"). However, Figures 2, 4, 5 and Tables 1–3 report only point estimates. Given that some differences between methods at the same NFE are modest (e.g., Table 1 CLIPScore differences of 1–2 points at NFE=8), the reader cannot assess whether gains are significant. This is the most impactful weakness — it does not invalidate the results but substantially weakens the evidence.

### Minor

- **The practical transition kernel is underspecified.** The kernel $$K(x_t, x_t') = \sum_{x_s} q(x_s|x_t) p_\theta(x_t'|x_s)$$ is defined with only "$t < s$" but does not specify how much larger s is or how this parameter is chosen. In practice, s controls how aggressively the method noises and then re-generates, which affects the exploration-exploitation balance. The paper does not discuss this choice or its impact. (Contra the harsh critic: the kernel IS implementable via ancestral sampling — noise forward to x_s, then denoise step-by-step back to x_t'. Sampling from it does not require evaluating the density p_θ(x_t'|x_s) explicitly.)

- **The intermediate reward approximation is unanalyzed.** The paper states (Line 121): "Intermediate rewards r(x_t) can approximate by evaluating the reward function on the diffusion model's prediction of x_0." This is standard practice (also used by FK and SVDD), but the paper makes no attempt to quantify how well r(hat{x}_0) approximates the true log-expected future reward, or under what conditions this approximation breaks down. A small-scale analysis would strengthen the contribution.

- **No ablation of the pool reuse strategy.** Section 3.3 claims that when a proposal is rejected, "we simply reuse the previously generated sampling pool." This is presented as an advantage, but it is never ablated — does reuse degrade quality compared to fresh proposals? The fixed N vs. k comparison (Table 3) is informative but does not isolate the effect of pool reuse.

- **The number of denoising steps s–t is never specified or ablated.** The kernel requires choosing a specific noising distance (how many steps to noise forward). This is a free parameter whose impact is not studied.

### Trivial

- The notation "2T NFEs" on lines 204–205 could be read as "2×T NFEs" where T is the number of denoising timesteps (1000 for MDLM). Figure axes indicate the x-axis represents NFEs with values 1–32, suggesting T refers to a unit of measurement rather than the total timesteps. This ambiguity should be resolved.

## Nice-to-Haves

- A comparison against FK or SVDD with more particles at matched NFE budgets (the harsh critic's suggestion #3) would strengthen the "8× faster" claim by ruling out the possibility that baselines are suboptimal due to hyperparameter tuning for other budgets.

## Removed Points

- **"Kernel is not implementable"** — This criticism from the harsh critic is factually incorrect. The kernel K(x_t, x_t') = Σ q(x_s|x_t) p_θ(x_t'|x_s) can be sampled from by (1) noising forward x_t → x_s via q, and (2) denoising step-by-step from x_s back to x_t using the reverse process. The critic confused density evaluation with sampling. The paper's clever balancing function λ makes K cancel out in the acceptance ratio (Eq. 3), so only sampling from K is needed, not evaluation.
- **"Convergence guarantee does not apply to the practical algorithm"** — Overstated. Proposition 1 is an asymptotic convergence guarantee for the inner MTM chain at a fixed timestep t, which is standard for MCMC-based methods. The overall process combines these refinements with standard denoising steps. The practical algorithm runs finite iterations (k=4,8,16), which is no different from any practical MCMC method — asymptotic guarantees are the norm.
- **"Missing related works"** — The paper cites all relevant prior work in Sections 2, 3, and 5 (FK, SVDD, SoP, SMC, DSearch, DTS, PG-DLM). Per the instructions, I cannot penalize missing references without external confirmation.
- **Missing appendix content** — The parser strips appendix sections (references, proofs, additional experiments) from all papers; these exist in the original submission.
- **Formatting nitpicks** and speculations about unreleased artifacts are removed per the guidelines.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's main claimed "fatal flaw" (kernel not implementable) is factually incorrect upon examination, and the remaining weaknesses (no error bars, underspecified parameters) are addressable in revision. No genuinely novel meta-level insight emerges from the cross-review.

## Suggestions

1. **Add error bars, standard deviations, or confidence intervals** to all figures and tables reporting language experiment results. At minimum, report the variance across the 3 seeds in a supplementary table and overlay ±1σ on the line plots in Figures 2 and 4.
2. **Clarify the practical kernel implementation.** State explicitly that sampling from K is done by (a) noising from x_t to x_s via q(x_s|x_t) for a chosen s, then (b) running the reverse process step-by-step from s back to t. Discuss the choice of s as a hyperparameter and its effect.
3. **Add a small-scale analysis of the intermediate reward approximation.** Compare r(hat{x}_0) vs. a Monte Carlo estimate of the true log-expected reward for a subset of prompts/timesteps.
4. **Ablate the pool reuse strategy.** Compare with a version that always draws fresh proposals on rejection.

## Score and Decision

**Calibration details:**

*Round 1 (Bracketing, 3 queries, score bands <3.5, 3.5–7.5, >7.5):*

Low-band anchors (avg < 3.5):
- KqTzfiNjWU (avg 2.00, Withdrawn) — Inverse problems with "restorer guidance," much weaker contribution.
- W4djmqKZC6 (avg 3.00, Reject) — Pixel-accelerated diffusion, incremental at best.
- mzJAupYURK (avg 3.00, Withdrawn) — Consistency tuning via TD learning, limited innovation.
- edx7LTufJF (avg 2.50, Withdrawn) — Low-rank diffusion fine-tuning.

Middle-band anchors (avg 3.5–7.5):
- 2fgzf8u5fP (avg 3.80, Reject) — SVDD: derivative-free guidance. Similar task setting but major theoretical concerns (α=0, unanalyzed bias, unfair baselines). IterRef's empirical results are stronger and its theory less problematic.
- D7PQ54l5Q1 (avg 4.75, Withdrawn) — MCMC for inverse problems with diffusion. Limited novelty (applying standard MCMC). IterRef has broader empirical scope and a more novel algorithmic contribution.
- XsgHl54yO7 (avg 6.50, Poster) — Discrete Guidance for discrete-space diffusion/flow. Similar contribution level. Discrete Guidance has cleaner theory; IterRef has broader domain coverage (text + image vs. molecules/proteins). Comparable overall.
- vi3DjUhFVm (avg 7.25, Spotlight) — DAS: SMC-based test-time alignment for (continuous) diffusion. More thorough experimental methodology (error analysis, multiple domains) and cleaner framing. IterRef is specific to discrete diffusion, which is a harder setting, but DAS is more polished.

High-band anchors (avg > 7.5):
- nHESwXvxWK (avg 8.50, Oral), OlzB6LnXcS (avg 8.00, Oral), fV0t65OBUu (avg 8.00, Oral), DJSZGGZYVi (avg 9.00, Oral) — All at oral/strong-accept level. IterRef is clearly below this tier.

*Round 2 (Narrowing, 2 queries, score range 4.5–7.5):*
Returned D7PQ54l5Q1 (4.75), MBDH5zyxHM (4.60), i8bdPSmOwk (5.33), vi3DjUhFVm (7.25) and XsgHl54yO7 (6.50), 1pTlvxIfuV (5.50), rMOhA1JNPo (6.50), e2ONKX6qzJ (6.00). The paper comfortably exceeds the ~4.5–5.5 papers (stronger evidence, more coherent contribution) while falling short of the 7.25 DAS paper (no error bars, weaker theory-practice alignment). It sits alongside the 6.0–6.5 papers (e.g., Discrete Guidance at 6.50).

The paper achieves what it claims: a new test-time scaling method for discrete diffusion with strong empirical evidence. The theoretical framing is appropriate for an empirical paper (Proposition 1 is a standard MCMC convergence result applied to this setting). The main weaknesses are the lack of statistical reporting and underspecified implementation details for the kernel—both addressable in revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>