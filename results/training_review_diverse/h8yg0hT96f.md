Now I have all the information needed. Let me synthesize the final review.

## Summary

The paper introduces CoDiff, a gradient-based Bayesian Optimal Experimental Design (BOED) method. The core contributions are: (1) a new EIG gradient estimator using an *expected posterior* distribution (a geometric mixture of posteriors across simulated outcomes) that avoids nested Monte Carlo estimation; (2) a single-loop sampling-optimization procedure inspired by bi-level optimization; and (3) the first extension of BOED to diffusion-based generative models, enabling data-based BOED where only samples (not closed-form densities) are available. The method is evaluated on a source localization task (density-based) and an MNIST image reconstruction task (data-based).

## Strengths

- **Novel expected-posterior EIG gradient estimator that avoids nested Monte Carlo.** The paper derives a gradient expression (Eq. expGMC, Section 3) where the expected posterior serves as an importance sampling proposal. Unlike prior approaches (Goda 2022, Ao 2024), this estimator requires only one batch of joint samples and one batch from the expected posterior, rather than running separate MCMC chains for each simulated observation. The expected posterior minimizes a weighted sum of KL divergences to the per-observation posteriors (Lemma G), providing a principled rationale for its use as a proposal.

- **First single-loop sampling-optimization procedure for BOED without lower-bound approximations.** The paper casts EIG maximization as a bi-level optimization over distributions and proposes Algorithm 2 (single loop), where one sampling step alternates with one SGD step on the design. On the source localization task (Section 5.1, Figure 2), CoDiff achieves ~30% higher SPCE and substantially lower Wasserstein distance versus RL-BOED, VPCE, PASOA, and SMC baselines, using only N+M=400 total samples.

- **First extension of BOED to diffusion-based generative models.** By plugging a pre-trained diffusion model into the sampling operators (Eq. 17-20), the method handles data-based BOED where the prior is only available through samples. The MNIST image reconstruction task (Section 5.2, Figures 1 and 4) demonstrates sequential mask placement optimization with a diffusion prior — a scenario infeasible for all prior BOED frameworks requiring closed-form prior densities.

- **Contrastive interpretation.** The paper frames design optimization as making the expected posterior "as different as possible" from the prior (Figure 2), connecting BOED to noise-contrastive estimation and providing intuitive understanding of the optimization dynamics.

## Weaknesses

### Major

- **MNIST experiment lacks quantitative evaluation.** The image reconstruction demonstration (Section 5.2) is purely qualitative. The paper claims to "extend BOED to diffusion-based generative models" and the MNIST experiment is the primary evidence for this claim, yet it provides no reconstruction metrics (PSNR, SSIM, classification accuracy) vs. number of experiments, and no comparison against random designs or simple greedy baselines. The paper acknowledges the evaluation is "mainly qualitative" but given that this is the paper's most novel contribution, quantitative validation is essential to make the case convincing.

- **Missing computational cost comparison for baselines in the source localization experiment.** CoDiff's per-step runtime (2.9s with 400 samples) is reported, but no runtimes or computational budgets are reported for the baselines (RL-BOED, VPCE, PASOA, SMC). The Wasserstein distance improvement (two orders of magnitude) could partially reflect asymmetric computational budgets rather than algorithmic superiority. The SPCE and SNMC metrics (which measure design quality independently of posterior sampling) partially mitigate this concern, but the missing cost-equivalence data weakens the overall empirical case.

### Minor

- **No formal analysis of gradient estimator bias/variance.** The estimator (Eq. expGMC) uses self-normalized importance sampling and the same joint samples to define the expected posterior, creating a dependency that is not analyzed. While the paper situates itself within prior work that uses biased gradient oracles (citing Demidovich 2023, Liu 2024, Ao 2024), the absence of any theoretical or small-scale empirical analysis of the estimator's reliability leaves a gap in the methodological foundation. This is a common gap in ML methods papers but worth noting.

- **Single-loop convergence not justified.** The transition from nested (Algorithm 1) to single-loop (Algorithm 2) is described as "inspired by bi-level optimization," but the inner "problem" is sampling from distributions that depend on the current design — not a tractable optimization with a defined objective. The paper cites Marion et al. 2024 for the framework but does not analyze whether the coupled dynamics converge. The use of the DiGS kernel (a non-standard augmentation) to improve Langevin mixing suggests basic Langevin is insufficient, partially undermining the claimed simplicity. These are standard empirical compromises rather than fatal flaws, but they merit explicit discussion.

### Trivial

None.

## Nice-to-Haves

- A controlled comparison in the source experiment where baselines are given matched computational budgets (same number of likelihood evaluations per step, same number of design steps) would cleanly resolve the cost-equivalence concern.

- Ablation studies on key hyperparameters — particularly the effect of reducing N (joint samples) or M (expected posterior samples) — would provide practical guidance and strengthen confidence in the method's robustness.

- For the MNIST experiment, even a simple quantitative baseline (e.g., random design with the same diffusion-based posterior reconstruction) with MSE as a function of experiments would significantly strengthen the contribution.

- A discussion of when the expected posterior importance sampling proposal is likely to have high or low variance would help users understand the method's limitations.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Critique about the "expected posterior" minimizing KL being about variance, not KL** (from harsh critic's Section-by-Section notes): The paper states that the expected posterior minimizes the weighted sum of KLs, which is a property of *the best approximation in the KL sense*. The critic's claim that "in importance sampling one cares about variance, not KL" is a reasonable observation but overstates the issue — a KL-optimal proposal is standard practice for importance sampling, and the paper's claim that this "leads to an efficient importance sampling proposal" is standard, not unsupported. However, the critic is right that no variance analysis is provided. This is folded into the Minor weakness above.

- **Critique about "the paper should also cover Y / domain Z / additional tasks" type demands**: The critic's suggestion to add more baselines for the image problem (greedy heuristic based on expected posterior variance) is a reasonable nice-to-have but not a weakness — the paper explicitly notes that "previous methods do not apply" to this setting. This is moved to Nice-to-Haves.

- **Critique that the two orders of magnitude improvement is "suspiciously large"**: This is speculative with no evidence. The paper's figures clearly show the gap, and large improvements from a fundamentally different approach are not inherently suspicious. Removed as unsupported speculation.

- **Critique about the Lemma G being in the appendix**: This is a parser artifact — the lemma exists in the original submission's appendix which is stripped by the parsing process. Removed per the rule about missing appendix content.

## Novel Insights

None beyond the paper's own contributions. The reviews surface genuine concerns about experimental completeness but do not reveal novel insights about the method that the authors themselves missed.

## Suggestions

1. Add quantitative metrics (PSNR, SSIM, or downstream classification accuracy) to the MNIST experiment, comparing CoDiff-optimized designs against random designs and at least one simple baseline (e.g., maximum variance selection). A plot of reconstruction quality vs. number of experiments would be the most valuable addition.
2. Report per-step runtimes or total computational budgets (number of likelihood evaluations, number of MCMC steps) for all baselines in the source localization experiment to demonstrate cost-equivalent comparison.
3. Add a small-scale synthetic experiment (e.g., 1D Gaussian model with known ground-truth EIG gradient) to empirically assess the bias and variance of the proposed gradient estimator relative to alternatives. This would directly address the most significant methodological concern.

## Score and Decision

The paper introduces genuinely novel ideas — the expected posterior gradient estimator and the single-loop BOED procedure — and provides strong empirical validation on the density-based source localization task. The extension to diffusion models, while timely and interesting, is supported only by qualitative results, which weakens the paper's most ambitious claim. The missing computational cost comparisons for baselines further temper the empirical evidence. These are significant but addressable gaps. The core methodological contribution is novel and interesting enough to warrant acceptance, with the expectation that the quantitative gaps will be addressed in a camera-ready version.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>