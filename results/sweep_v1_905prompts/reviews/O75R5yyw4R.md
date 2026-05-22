Now I have a thorough understanding of the paper and the calibration landscape. Let me write the consolidated review.

**Round 1 bracket:** This paper is clearly above the 3.0–3.5 band (rejected papers with fatal flaws) and well below the 7.5+ band (top-tier papers). The plausible range is **3.5–7.5**.

**Round 2 narrowing:** The paper is substantially stronger than SVDD (3.80, reject) — which had fatal flaws like unfair α setting, biased approximations, and weak marginal gains over BoN. It is comparable to "Simple and Controllable Uniform Discrete Diffusion" (5.25, accept) — both have meaningful contributions alongside clear weaknesses. It is weaker than DDPP (6.25, accept) which had stronger theoretical grounding and wet-lab validation.

**Final score: 5.5** — slightly above the 5.25 anchor because the method (MTM-based iterative refinement for discrete diffusion) is more novel, the empirical gains are larger and more consistent, and the analysis (timestep sensitivity, k vs N) provides genuine insight. The score is held below 6 because of the unaddressed theoretical gap and missing statistical rigor.

---

## Summary

This paper introduces IterRef, a test-time scaling method for discrete diffusion models that uses Multiple-Try Metropolis (MTM) with a noising-denoising transition kernel to iteratively refine intermediate states toward reward-aligned distributions. Unlike prior trajectory-based methods (SMC, importance sampling) that commit to states in a single forward pass, IterRef corrects misaligned tokens *in situ* by proposing multiple candidates from a noise-denoise kernel, selecting via reward-weighted sampling, and accepting/rejecting with a Metropolis correction. Experiments on MDLM, LLaDA-8B (text) and MaskGIT (images) show consistent gains over FK, SVDD, SoP, and BoN across toxicity, sentiment, CoLA, perplexity, and CLIPScore — with particularly striking advantages at low compute budgets.

## Strengths

- **Consistent and often dramatic empirical wins across modalities and backbones.** On MDLM, IterRef at 2T NFE matches or exceeds all baselines at 32T NFE on Sentiment, CoLA, and Perplexity (Figure 2a). On LLaDA-8B, the method scales strongly with compute on Toxicity and CoLA (Figure 2b). On MaskGIT, IterRef improves CLIPScore by 1.0–1.6 points over the next best baseline at every budget (Table 1). These results are the paper's strongest evidence and are genuinely impressive.

- **Novel and well-motivated method design.** IterRef is the first application of Multiple-Try Metropolis to discrete diffusion refinement. The noising-denoising kernel (adding noise via forward process, then denoising with p_θ) is a clever instantiation of the predictor-corrector paradigm that creates controlled exploration without leaving the model's manifold. The balancing function simplification (Eq. 2–3) that eliminates backward proposals and yields an acceptance ratio that depends only on reward differences is a genuine algorithmic contribution.

- **Practical insight: later denoising stages matter more for discrete diffusion (Table 2).** The discovery that applying IterRef at later timesteps (0.1T) outperforms early-stage application, and that evenly-spaced application is often best, contrasts with continuous diffusion where early steps dominate. This is a non-obvious, domain-specific finding that can guide practitioners on where to allocate compute.

- **Fine-grained scaling analysis (Table 3, Figure 4).** The study showing that increasing iteration count *k* dominates particle count *N* (e.g., LLaDA-8B Toxicity: 3.3→54.0 with k=1→8, N=32→4, versus negligible gains from the reverse scaling) empirically validates the iterative refinement principle and gives actionable guidance.

## Weaknesses

### Major

- **The convergence guarantee (Proposition 1) depends on an unsubstantiated reversibility assumption.** The paper claims that "q and p_θ form a reversible Markov kernel" — but for standard absorbing-state discrete diffusion models (MDLM, LLaDA, MaskGIT), the forward process q only adds mask tokens and the learned denoiser p_θ is an approximation of the time-reversal, not an exact one. The composition K(x_t, x_t') = Σ_{x_s} q(x_s|x_t) p_θ(x_t'|x_s) is therefore not guaranteed to be reversible with respect to any distribution, let alone p^*(x_t). The paper provides no justification that this assumption approximately holds, nor does it bound the error in the stationary distribution when reversibility is violated. This undermines the strongest theoretical claim (convergence to the optimal distribution) and reduces it to a heuristic with MCMC intuition rather than a verified guarantee. The paper's contribution statement hedges ("under certain assumptions"), but the gap is significant enough that it should be discussed explicitly and, if possible, addressed with empirical diagnostics or a milder theoretical claim.

- **No statistical rigor in the evaluation.** All results are reported as point estimates with no confidence intervals, standard deviations, or significance tests. Given the stochastic nature of both the MTM acceptance mechanism and the diversity of reward landscapes, the reader cannot assess whether the reported gaps between IterRef and baselines are reliable or fall within noise. This is especially concerning for metrics like CoLA and Toxicity where class proportions can induce substantial variance. The paper says "each sampled 20 times" for language tasks, but this is reported as a single mean — using those 20 samples to compute a standard error or bootstrap CI would be straightforward and would significantly strengthen the evidence.

- **Baseline adaptation details are missing for SoP.** Search-over-Path (Ma et al., 2025) was originally designed for continuous diffusion. The paper lists it as a baseline for discrete diffusion (MDLM, LLaDA, MaskGIT) but provides no description of how it is adapted to the discrete setting. This makes it unclear whether the comparison is fair and hampers reproducibility. The other baselines (BoN, FK, SVDD) are better established in discrete settings.

### Minor

- **No ablation of the MTM acceptance mechanism.** The paper attributes IterRef's success to iterative refinement with the Metropolis correction, but does not test a variant that simply takes the best of N proposals at each iteration without the acceptance step. This would help isolate whether the benefit comes from the noising-denoising exploration, the reward-weighted selection, or the detailed-balance correction. Without this, it is unclear how much the MCMC theory contributes beyond a beam-search-like procedure.

- **Missing empirical diagnostics of the MTM chain.** Since the reversibility assumption is questionable, the paper should at minimum report acceptance rates at different timesteps or provide other diagnostics (e.g., trace plots, autocorrelation) to show the chain is mixing reasonably. This would build confidence that the method is not merely doing blind exploration.

- **Hyperparameter sensitivity for α and the noising step size is not studied.** The paper analyzes k and N extensively but does not examine how performance varies with the temperature α (which controls KL regularization strength) or the noising magnitude (the choice of s relative to t in the kernel). These could critically affect the reward-diversity trade-off and the exploration range.

- **NFE aggregation conflates generative and reward model costs.** The paper treats all function evaluations equally, but acknowledges (Section 3.3) that in large models like LLaDA-8B, generative calls dominate while in smaller models like MDLM, the costs are comparable. While a wall-clock analysis is promised in Appendix C.4 (stripped), the main paper's NFE-based comparisons conflate meaningfully different resource profiles. The authors should separately report generative-model calls and reward-model calls in the main text.

### Trivial

- None that survive filtering.

## Nice-to-Haves

- An ablation comparing IterRef with "take the best of N proposals without Metropolis correction" to isolate the value of the acceptance step.
- Reporting standard deviations or bootstrap confidence intervals for the main results (Figure 2, Table 1, Table 3).
- A brief discussion of whether the reversibility assumption approximately holds under specific conditions (e.g., when the noising step is small, or when p_θ is well-calibrated).

## Removed Points

The following points from the inputs were removed:

- **"Pool reuse breaks detailed balance" (Harsh Critic):** The paper's pool-reuse-on-rejection strategy is valid because when a proposal is rejected, the state x_t does not change, so an old pool drawn i.i.d. from K(x_t, ·) remains an i.i.d. sample from the same kernel. The acceptance formula (Eq. 3) further eliminates the need for backward proposals. The critic's concern about "dependence on past samples" appears unfounded given these design choices.

- **"Baselines favor IterRef at low compute by design" (Harsh Critic):** The critic's claim that BoN at NFE=2 is "trivial" applies equally to all methods at minimum compute — the comparison is about how methods scale from that baseline. The paper configures baselines "favorably" per their original papers, which is standard practice. The SoP adaptation concern is retained (above, Major), but the general fairness concern is overstated.

- **"Computational cost conflates generative and reward model calls" (Harsh Critic):** The paper explicitly acknowledges this limitation in Section 3.3 and points to a wall-clock analysis in Appendix C.4. The criticism adds no information beyond what the paper already states.

- **Generalized "the evaluation lacks rigor" framing (Harsh Critic):** Retained as the specific, verifiable concern about missing confidence intervals (Major). The sweeping "conclusions may be correct, but evidence does not convincingly support them" was replaced with the concrete statistical point.

- **Generic strengths from Strength Finder (e.g., "the paper addressed an important problem"):** Removed as superficial. The four retained strengths are all grounded in specific, verifiable paper content.

## Novel Insights

Beyond the paper's own contributions, the most striking emergent finding from the review is that **the method's practical success is largely decoupled from its theoretical framework.** The reversibility assumption that powers Proposition 1 is not satisfied by the actual models used, yet the method delivers strong, consistent results. This suggests either that (a) the MTM chain converges to a distribution close enough to p^*(x_t) despite the violation, or (b) the iterative noising-denoising process is effective chiefly because it creates structured exploration (noising adds diversity, denoising returns to plausible states), and the Metropolis correction is a relatively minor component — an interpretation supported by the paper's own finding that iterations *k* matter more than particles *N*. A clean ablation of the acceptance mechanism would resolve this ambiguity and substantially strengthen the paper's narrative.

## Suggestions

- Address the reversibility gap directly: either bound the stationary distribution error under approximate reversibility, or reframe the method as empirically grounded (remove the strong convergence claim) and provide empirical chain diagnostics (acceptance rates, trace plots) to compensate.
- Add bootstrap confidence intervals or standard deviations to all main results (Figure 2, Table 1, Table 3). With 20 samples per prompt for language tasks, this is computationally cheap and would dramatically improve rigor.
- Describe how SoP is adapted to discrete diffusion, or replace it with a baseline whose discrete adaptation is documented (e.g., DSearch, Particle Gibbs from Dang et al. 2025).
- Add the MTM-ablation experiment (best-of-N proposals without the Metropolis correction) to isolate whether the acceptance step matters.

## Score and Decision

**Round 1 bracket:** The paper sits between weak anchors (~3.0, fatal-flaw rejects) and strong anchors (~8.0, top-tier papers). Initial bracket: **(3.5, 7.5)**.

**Round 2 anchors used for narrowing:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| SVDD (2fgzf8u5fP) | 3.80 | R1 | Current paper is stronger — no unfair α-setting, larger empirical gains, more thorough analysis |
| Plug-and-Play (4hFT4rfG40) | 3.75 | R1 | Current paper is much stronger — broader evaluation, more baselines, better theory |
| Dreamguider (Hpu3KIX8Am) | 4.00 | R2 | Current paper is stronger — more novel method, larger scope |
| Simple Uniform Discrete Diff. (i5MrJ6g5G1) | 5.25 | R2 | Comparable — both have meaningful contributions alongside clear weaknesses; current paper is more novel methodologically |
| DDPP (Ombm8S40zN) | 6.25 | R1 | Current paper is weaker — DDPP has stronger theory (training-based), more rigorous experiments, wet-lab validation |
| Controlled Denoising (MBDH5zyxHM) | 4.60 | R2 | Current paper is stronger — more consistent results, better-motivated method |
| Scaling MDMs (WNvvwK0tut) | 6.50 | R2 | Different focus (scaling laws), not directly comparable |

**Final score: 5.5**

The paper makes a clear contribution — a novel, well-motivated test-time scaling method for discrete diffusion with strong empirical results across modalities. However, the unsubstantiated reversibility assumption undermines the theoretical guarantee, and the lack of statistical rigor weakens the evidence. The contribution is real but not as solid as the framing suggests. Score 5.5 reflects a paper that is clearly above the rejection threshold for this area but has issues that prevent a higher score.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>