Now I have a thorough understanding of the paper and can evaluate each of the critic's claims against the actual text.

## Final Consolidated Review

## Summary

This paper introduces a new approach to gradient-based Bayesian Optimal Experimental Design (BOED) that replaces nested estimation loops with a single joint sampling-optimization procedure. The key technical innovations are: (1) an "expected posterior" distribution that serves as an efficient importance sampling proposal for EIG gradient estimation, (2) a new tractable EIG gradient expression derived from this expected posterior, and (3) integration of this framework with diffusion-based generative models. Experiments on a source localization task show substantial improvement over baselines, while a proof-of-concept on MNIST image reconstruction illustrates the potential of extending BOED to generative-model priors.

## Strengths

- **Novel EIG gradient estimator via the expected posterior**: The paper introduces the expected posterior distribution (Eq. 7) and derives a new gradient expression (Eq. 6) that avoids the nested estimation issues plaguing prior work. The expected posterior is shown (Lemma G, referenced) to minimize a weighted sum of KL divergences to the target posteriors, providing a principled justification. This is the core theoretical contribution.

- **Single-loop sampling-optimization algorithm**: Algorithm 2 replaces the costly nested loops of prior BOED methods by alternating one step of Langevin/diffusion sampling with one SGD design update. This is a practical algorithmic advance that directly addresses the computational bottleneck of BOED, supported by a bi-level optimization perspective (Section 4).

- **Strong empirical results in the density-based setting**: On the source localization benchmark (Section 5.1, Figure 4), CoDiff achieves a ~30% improvement in SPCE over RL-BOED, significantly higher SNMC, and two orders of magnitude lower Wasserstein distance across 100 rollouts. These results cleanly demonstrate that the method outperforms state-of-the-art approaches in a standard BOED setting.

- **First extension of BOED to diffusion-based generative models**: The paper shows how to sample from the expected posterior using conditional diffusion models (Eq. 14) and demonstrates the first data-based BOED application on high-dimensional images (Section 5.2). This opens a new direction for BOED in settings with complex, high-dimensional priors that were previously inaccessible.

## Weaknesses

### Fatal

None.

### Major

- **The MNIST image reconstruction experiment lacks quantitative evaluation.** The paper presents only qualitative comparisons with random designs (Figure 1, Figure 5) and explicitly states the evaluation is "mainly qualitative" (line 376). No numerical metrics (PSNR, SSIM, reconstruction MSE, or EIG estimates) are reported for the optimized vs. random design sequences. Since "first extension to diffusion-based generative models" is a headline contribution claim, the absence of any quantitative evidence that the optimized designs actually outperform random ones undermines this claim. The experiment demonstrates feasibility but not efficacy.

### Minor

- **The gradient estimator's SNIS bias is acknowledged but not analyzed.** The paper claims "without resorting to lower bound approximations" (lines 7, 443), yet the estimator in Eq. (\ref{expGMC}) uses self-normalized importance sampling, which introduces bias for finite M. The paper notes that biased gradient oracles have been used in prior work (lines 62–63) but provides no empirical or theoretical analysis of how this bias affects the optimization trajectory or the quality of the final designs. While this does not invalidate the method (many successful stochastic optimization methods use biased gradients), it is a gap that would strengthen the paper to address.

- **The Wasserstein distance comparison in the source localization experiment uses different posterior samplers for different methods.** CoDiff's Wasserstein is computed from its own Langevin+DiGS samples, while baselines (RL-BOED, VPCE, Random) use tempered SMC on their design sequences. As the paper notes, this was necessary because those methods don't provide their own posterior samples. However, the SPCE and SNMC metrics — which compare design sequences only — are unaffected by this choice and already show clear improvement. The Wasserstein comparison is thus a secondary concern, but a cleaner experimental design would use the same posterior inference for all methods' design sequences.

- **The single-loop procedure lacks convergence justification.** The transition from the nested-loop (Algorithm 1) to the single-loop (Algorithm 2) is motivated by analogy to bi-level optimization (Marion et al.), but no theoretical conditions are given under which the single loop converges to a stationary point of the EIG. Given that this is an empirical paper addressing a known hard problem, the lack of theory is not fatal, but providing a heuristic argument or empirical convergence check would strengthen the presentation.

### Trivial

None.

## Nice-to-Haves

- Report error bars or confidence bands for the SPCE/SNMC/Wasserstein curves over the 100 rollouts in Figure 4 (currently only medians are shown).
- For the MNIST experiment, include a simple quantitative comparison (e.g., reconstruction MSE over several trials for optimized vs. random designs, or an EIG estimate) to substantiate the claim.
- Clarify in Section 3 whether the expected posterior is updated every gradient step or only at certain intervals in the sequential setting.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Unfair comparison invalidates claimed superiority"** (Harsh Critic #1) — **Removed as factually incorrect.** The critic claims the Wasserstein comparison confounds design optimization with posterior sampling quality. However: (a) the SPCE and SNMC metrics, which the paper also reports and which show ~30% improvement, are computed from **design sequences only** and are not affected by posterior sampling choices (paper explicitly states this at lines 371–372); (b) for the Wasserstein metric, the baselines receive SMC posterior sampling (a strong, principled method) while CoDiff uses its own sampler — if anything, this asymmetry favors the baselines. The critic's claim that the "two-orders-of-magnitude improvement may reflect the choice of posterior sampler" is not supported by the paper's design.

2. **"Lemma 1 referenced but not provided"** — **Removed.** The lemma (referenced as \ref{lem:G}) would be in the appendix, which was stripped by the parser. The instruction explicitly states to remove such criticisms.

3. **"Single loop completely lacks theoretical justification"** — **Weakened and moved to Minor.** The paper discusses the connection to bi-level optimization (lines 257–261) and cites relevant literature. The lack of convergence proof is a limitation but the paper does not claim theoretical convergence — it is an empirical methods paper.

4. **Formatting/style nitpicks** (notation heaviness, "no error bars") — **Removed per hard rules.**

5. **"Goda et al. / Ao et al. connection is insightful"** — Moved from Strengths to here. This is a reasonable observation about the related-work discussion but is not a core strength of the paper's own contribution.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an insight about the paper that the authors themselves do not already state.

## Suggestions

1. **Add quantitative evaluation for the MNIST experiment.** This is the most impactful change: report reconstruction MSE or PSNR over multiple trials for optimized vs. random design sequences, or at minimum provide EIG estimates (e.g., SNMC) for both conditions. The current qualitative comparison is insufficient to support the claim of "first extension to diffusion-based generative models" as a validated contribution.

2. **Add a small ablation on gradient bias.** On the source localization task (or a simpler synthetic problem with tractable EIG), compare the proposed biased gradient estimator against a lower-bound baseline (e.g., Foster et al.) in terms of final design quality, to demonstrate that the bias does not harm optimization.

3. **Clarify the Wasserstein comparison.** Either add a variant where all methods' designs are evaluated using the same posterior sampler (e.g., SMC for all), or explicitly state in the main text why the current approach is reasonable.

4. **Report error bars for Figure 4.** The paper reports medians over 100 rollouts; adding quartiles or confidence bands would improve interpretability.

## Score and Decision

The paper presents a novel methodological contribution (expected posterior gradient estimator + single-loop optimization) that is well-motivated, theoretically grounded, and convincingly validated in a standard density-based BOED task. The extension to diffusion models is novel and potentially impactful, but the experimental evidence for this extension is preliminary (qualitative only). The weaknesses are addressable and do not invalidate the core contributions.

**Originality**: High — the expected posterior and its use for gradient estimation is new.  
**Importance**: High — scaling BOED to generative-model priors addresses a real bottleneck.  
**Claims support**: Moderate — strong for density-based BOED, weak for data-based BOED.  
**Soundness**: Good — the theory is sound; the main experiment is clean.  
**Clarity**: Good — well-organized, notation is careful if dense.  
**Value**: High — the method provides practical efficiency gains and opens a new direction.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>