Now I have verified the key claims against the paper. Let me produce the consolidated review.

## Summary

This paper introduces IterRef, a test-time scaling method for discrete diffusion models that uses Multiple-Try Metropolis (MTM) with noising-denoising transitions to iteratively refine intermediate states toward reward-aligned distributions. The method is evaluated on two language diffusion models (MDLM, LLaDA-8B) and one image diffusion model (MaskGIT) across multiple reward functions, consistently outperforming baselines (FK, SVDD, SoP, BoN). The authors provide a convergence guarantee (Proposition 1) under a reversibility assumption, and ablate design choices including refinement timestep selection and the iteration-vs-particle trade-off.

## Strengths

- **Consistent and substantial empirical improvement across models, tasks, and modalities.** Figure 2 shows IterRef outperforming all baselines on both MDLM and LLaDA-8B across four language tasks at matched NFE budgets. Section 4.2 reports that with MDLM, IterRef at 2T NFEs exceeds all baselines at 32T NFEs on Sentiment, CoLA, and Perplexity — up to 16× efficiency. Table 1 shows IterRef achieving the highest CLIPScore with MaskGIT at every budget (e.g., 35.8 vs. 34.8 for FK at 16 NFEs).

- **Theoretical grounding.** Proposition 1 provides a convergence guarantee showing that the MTM-based iterative refinement asymptotically converges to the optimal reward-aligned intermediate distribution \(p^*(x_t)\) — a property not established for prior particle-based guidance methods (Section 3.1).

- **Practical efficiency innovations.** Section 3.3 details how the tailored balancing function (Eq. 2) eliminates the need to resample backward proposals (halving per-iteration cost), and how rejected proposals automatically reuse the existing proposal pool without resampling.

- **Actionable insights about discrete diffusion dynamics.** Table 2 shows that applying IterRef at later denoising stages (0.1T) outperforms early-stage application, and even distribution across all steps works best overall — a finding that differs from continuous diffusion where early steps dominate. Table 3 demonstrates that increasing iterations \(k\) yields larger gains than increasing particles \(N\) under the same compute budget.

- **Cross-modality validation.** The method is demonstrated on both language (MDLM, LLaDA-8B) and image (MaskGIT) domains, increasing confidence in the generality of the approach.

## Weaknesses

### Fatal

None.

### Major

- **Single-try Metropolis–Hastings baseline is missing.** With the chosen balancing function, the MTM acceptance rule simplifies to \(\min(1, \exp((r(x_t')-r(x_t))/\alpha))\) and the importance weights become uniform — essentially drawing \(N\) proposals and picking one uniformly, then accepting/rejecting by reward difference. Without a comparison against a single-proposal MH baseline operating at the same total compute, the paper cannot demonstrate whether the multiple-try machinery (as opposed to the simple noising-denoising transition kernel) is responsible for the gains. This is a missing control that weakens the claimed novelty of the MTM instantiation.

- **No uncertainty quantification.** All reported numbers in Figure 2, Table 1, and Table 3 are point estimates without error bars, confidence intervals, or significance tests. For the language experiments (3 seeds, 15 prompts, 20 samples each = 300 generations per condition), the results could exhibit substantial variance. The absence of any measure of variability makes it impossible to assess whether reported improvements are statistically significant, especially for comparisons where margins are narrow.

### Minor

- **Aggregated NFE reporting in main figures.** The main results (Figures 1(b), 2, Table 1) report "NFEs" as a single aggregated count, counting generative model calls and reward model calls identically. The paper explicitly acknowledges in Section 3.3 that this "may obscure meaningful differences" and states that Appendix C.4 provides wall-clock time analysis. However, the primary narrative and visualizations use aggregated NFE, and readers cannot distinguish between generative and reward costs from the main paper alone. This is a presentation concern given the paper's own acknowledgment; disaggregated reporting in the main figures would improve clarity.

- **Intermediate reward approximation unvalidated.** The paper approximates the intractable intermediate reward \(r(x_t) = \alpha \log \mathbb{E}_{x_0 \sim p_\theta(\cdot|x_t)}[\exp(r(x_0)/\alpha)]\) via a single \(x_0\) prediction (Section 3.1, line 121), but provides no analysis of how this approximation error affects the method's behavior or convergence. For long sequences, a single-point estimate could be noisy.

- **Reversibility assumption not verified.** Proposition 1 assumes "\(q\) and \(p_\theta\) form a reversible Markov kernel," which is a strong condition unlikely to hold exactly for learned discrete diffusion models with time-inhomogeneous forward processes. The paper does not provide empirical evidence (e.g., symmetry checks) that this approximately holds for the tested models. This does not invalidate the method's empirical success but limits the force of the theoretical guarantee.

- **Hyperparameter details for baselines are not specified.** The paper states baselines are "favorably configured by following the original papers" (Section 4.1) but does not provide a table of the hyperparameter settings used per task. This makes reproducibility harder and leaves open questions about tuning fairness.

- **Refinement schedule \(\mathcal{U}\) for main experiments is not stated.** The paper introduces \(\mathcal{U}\) as a flexible design choice but does not specify which schedule was used in the main results (Figures 2, Table 1). Table 2 studies \(\mathcal{U}\) post-hoc, but the reader cannot determine what schedule produced the headline results.

### Trivial

None.

## Nice-to-Haves

- A single-try MH variant as a control baseline (addressed under Major above).
- Disaggregated cost reporting (generative vs. reward model calls) alongside aggregated NFE in the main paper.
- Error bars on all quantitative results.
- Empirical verification of the approximate reversibility of the learned kernel for the models used.
- Ablation measuring the impact of the single-point \(x_0\) approximation of \(r(x_t)\) vs. multi-sample estimates.
- Clarifying the \(\mathcal{U}\) schedule used in each main experiment.

## Removed Points

- **"The MTM framework reduces to simple MH and the added complexity is unearned."** This criticism misreads the paper. Generating \(N\) proposals and selecting via weighted sampling provides better mixing and exploration than single-try MH, which is the well-known advantage of MTM. The missing single-try baseline is a valid request (kept above), but the claim that "the extra complexity of multiple tries is unnecessary" without evidence is speculative, not a verified weakness.

- **"Pool reuse may break detailed balance."** The paper explicitly justifies reuse by noting the candidates were drawn i.i.d. from \(K(x_t,\cdot)\) and the state is unchanged upon rejection. This reasoning is correct — conditional independence given \(x_t\) means the pool remains a valid proposal set. The criticism is factually incorrect.

- **"The paper does not discuss how \(\mathcal{U}\) is chosen."** The paper does discuss this: Section 3.2 states \(\mathcal{U}\) is flexible, and Section 4.4 systematically studies different choices of \(\mathcal{U}\) in Table 2. The absence of the specific \(\mathcal{U}\) for main experiments is a separate (minor) transparency issue, retained above.

- **"No comparison against Wang et al. (2025) on remasking."** This asks for a concurrent-work comparison. The paper cites Wang et al. (2025) as "beginning addressing these challenges" in related work but does not claim to benchmark against it. Requesting a baseline that was likely released concurrently with or after this submission is beyond reasonable scope.

- **"The paper should evaluate on a diversity reward to see if IterRef reduces diversity."** This is a good future direction but beyond the scope of the current paper, which focuses on reward maximization.

- **"CoLA favors late-stage refinement and this needs explanation."** The paper reports this empirical finding (Table 2). Hypothesizing about the cause is a suggestion for deeper analysis, not a weakness of the presented work.

- **Various formatting/style nitpicks from the harsh critic** (y-axis labels, unit scales, figure formatting) are parser artifacts or minor presentation issues that carry no weight in evaluation.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the paper that the authors themselves do not already make.

## Suggestions

1. **Add a Metropolis–Hastings baseline.** Run IterRef with \(N=1\) (single proposal, no multiple-try selection) at equivalent compute to isolate the benefit of the MTM machinery from the benefit of the noising-denoising transition kernel itself.

2. **Report disaggregated costs.** In the main figures, show either (a) separate curves for generative-model calls vs. reward-model calls, or (b) wall-clock time on the x-axis, for at least the LLaDA-8B experiments where the cost asymmetry is largest.

3. **Add error bars.** Compute results over multiple random seeds and show standard deviation or confidence intervals on all line plots and tables. At minimum, report the variance across the 15 prompts used.

4. **State the \(\mathcal{U}\) schedule for each main experiment.** Without this, the primary results are not replicable from the main paper.

5. **Provide a hyperparameter table for all baselines per task** in the main text or appendix.

6. **Validate the intermediate reward approximation** by comparing single-point \(x_0\) estimation against a multi-sample estimate on a small subset of data, and report the correlation.

7. **Discuss what happens when the reversibility assumption fails** and whether the method still works (since the empirical results suggest it does).

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>