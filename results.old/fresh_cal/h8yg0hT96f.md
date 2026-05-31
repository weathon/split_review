Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper introduces a new approach to Bayesian Optimal Experimental Design (BOED) via an "expected posterior" distribution — a geometric mixture of posteriors over simulated outcomes. The authors derive a new gradient estimator for the Expected Information Gain (EIG) that avoids nested estimation issues, and integrate it with bi-level optimization to obtain a single-loop sampling-optimization procedure. The method is demonstrated in two settings: a density-based source localization task (with quantitative baselines) and a data-based MNIST image reconstruction task using a diffusion model prior — the latter being the first application of BOED with a diffusion-based generative model.

## Strengths

- **Novel EIG gradient estimator via expected posterior.** The paper derives a new expression for the EIG gradient (Equation 14) using an importance sampling proposal that is a geometric mixture of posteriors over simulated outcomes. This estimator avoids the nested Monte Carlo or per-posterior MCMC costs of prior approaches (Goda2022, Ao2024). The connection showing that the two prior approaches are special cases of the same unified framework (Section 3) is a useful contribution.

- **First extension of BOED to diffusion-based generative models.** The paper introduces a sampling operator for the expected posterior using conditional diffusion models (Equation 19, Section 3.3) and demonstrates sequential design with a diffusion prior for high-dimensional image reconstruction. This opens the data-based BOED setting that prior work could not handle.

- **Strong quantitative results in the density-based setting.** In the source localization task (Section 5.2, Figure 2), CoDiff outperforms RL-BOED, VPCE, PASOA, and SMC on all reported metrics (SPCE, SNMC, Wasserstein distance). The improvement is substantial: approximately 30% higher SPCE than RL-BOED and two orders of magnitude lower Wasserstein distance.

- **Single-loop optimization without EIG lower bounds.** Algorithm 2 presents a principled bi-level optimization procedure that alternates single steps of sampling and design update, eliminating the need for inner-loop convergence and avoiding EIG lower-bound approximations. The formalism of sampling operators (Section 4) provides a clean framework for analyzing the approach.

- **The expected posterior admits the same samplers as individual posteriors.** The score of the expected posterior is a convex combination of posterior scores (Equation 17), so Langevin and diffusion samplers apply without added complexity. This is operationalized concretely in both settings (Equations 22–23 for Langevin, Equation 19 for diffusion).

## Weaknesses

### Fatal
None.

### Major

- **The diffusion-based BOED experiment is only qualitatively validated.** The MNIST image reconstruction task — the paper's headline demonstration of data-based BOED — provides no quantitative metrics. There is no reconstruction error (PSNR, SSIM, MSE), no estimated EIG, and no quantitative measure of posterior concentration. The paper explicitly states "our evaluation is mainly qualitative" (line 376). While a comparison against random designs is shown visually in Figure 1, the reader cannot assess whether the optimized designs meaningfully outperform a simple heuristic, nor can the magnitude of the improvement be evaluated. Given that the abstract and conclusion prominently claim "the first access to data-based BOED" and "superior accuracy," this gap weakens the paper's central claim.

### Minor

- **The choice of weights ν_i for the expected posterior is not discussed.** The paper introduces free weights ν_i (with ∑ν_i = 1) in Equation (12) and uses them in the Langevin and diffusion updates (Equations 22–23, 19), but never specifies how they are set in the experiments (presumably uniform) or analyzes sensitivity to this choice. Since the weights directly affect the expected posterior and thus the gradient estimator, this merits at least a brief discussion.

- **Baseline configuration details are limited.** The source localization experiment compares against RL-BOED, VPCE, and PASOA, but the paper does not specify how these baselines were configured, tuned, or whether their hyperparameters were optimized. The Wasserstein distances for RL-BOED and VPCE are computed using a separate tempered SMC posterior (as described in the paper), which is reasonable but could interact with the comparison. Greater transparency would strengthen the superiority claims.

- **Runtime comparison with baselines is not provided.** The paper reports per-step times for CoDiff (2.9s for source localization, 7.3s for MNIST) but does not report comparative runtimes for the baselines. Since the conclusion claims "lower computational cost compared to state-of-the-art methods," this claim is unsupported without runtime data for the baselines.

- **The single-loop algorithm's behavior under approximate sampling is acknowledged but not analyzed.** The paper notes (lines 152–157) that p and q are rarely at their stationary distributions and references Marion2024 for the theoretical framework. However, no analysis is given of the bias or convergence properties when the sampling operators are applied only one step per design update in the BOED context. The practical success in the source localization experiment is encouraging, but the conditions under which the single-loop procedure is reliable remain unspecified.

### Trivial
None.

## Nice-to-Haves

- For the diffusion experiment: adding a quantitative metric (e.g., reconstruction MSE vs. number of experiments, or estimated EIG using a held-out estimator) and evaluating on multiple digits (not just one) would substantially strengthen the paper's headline claim.
- Adding a sensitivity analysis for the ν_i weights would clarify whether the method is robust to this choice.
- A brief discussion of when the single-loop approximation is expected to be reliable (e.g., under fast-mixing samplers) would improve credibility.

## Removed Points

- **"Lack of a random baseline in the diffusion experiment" (from Harsh Critic #2):** Factually incorrect. Figure 1 (fig:mnist_comp) explicitly compares "Optimized vs. random designs" — the caption states: "Optimized vs. random designs: measured outcome y (2nd vs. 3rd column)." A random baseline is present in the paper.
- **"Without resorting to lower bound approximations is overstated" (from Section-by-Section notes):** The paper genuinely does not use EIG lower bounds (the approach taken by Foster2019 and others). Self-normalized importance sampling is a standard technique whose bias is well-understood; characterizing the method as not using EIG lower-bound approximations is accurate.
- **"No step sizes, no number of inner iterations" / missing hyperparameters:** The paper is a conference submission; implementation details and additional experimental configurations are standardly deferred to the appendix, which is stripped by the PDF parser. Reproducibility concerns at this level of granularity are not appropriate for review of the extracted main text.
- **"Lemma G (assuming it exists in the appendix)":** Removed per the rule that the parser strips these sections; they exist in the original submission.
- **"Missing related works":** Cannot be confirmed without external knowledge; removed per instructions.
- **Strength Finder item about "the single most important piece of evidence is the derivation and its concrete instantiation with diffusion models":** This conflates two different contributions and overstates the weight of the (qualitative) diffusion experiment. The paper's strongest evidence is the quantitative source localization experiment; the diffusion experiment is a proof-of-concept.

## Novel Insights

The reviewers' perspectives do not introduce genuinely novel observations beyond the paper's own contributions. The core tension identified — that the method's most novel application (diffusion-based BOED) lacks rigorous quantitative validation — is an evaluation gap noted by the paper itself ("our evaluation is mainly qualitative"). The contrast between the strong density-based results and the qualitative diffusion experiment mirrors the paper's own framing. No reviewer insight uncovers a hidden flaw or unexpected strength not evident from reading the paper.

## Suggestions

1. Add quantitative metrics to the MNIST experiment: report reconstruction MSE (or PSNR/SSIM) as a function of the number of experiments, and compare against the random baseline and a simple heuristic (e.g., select the pixel with highest posterior variance).
2. Run the diffusion experiment on multiple MNIST digits and report aggregate statistics, not just one example.
3. State the ν_i values used in the experiments and briefly discuss the sensitivity of results to this choice.
4. Include wall-clock runtime comparisons for all baselines in the source localization task, or at minimum note that the runtime claim in the conclusion is supported only by the method's own timing.
5. Add a brief paragraph discussing when the single-loop approximation can be expected to work (e.g., when sampling operators mix sufficiently fast), referencing the conditions in Marion2024 that the paper builds on.

## Score and Decision

The paper makes a genuine technical contribution — the expected posterior gradient estimator and single-loop algorithm are novel, well-motivated, and validated in the density-based setting. The extension to diffusion-based BOED is a promising proof-of-concept but is not quantitatively validated, which weakens the paper's headline claim. The paper is a solid submission with an evaluation gap that is significant but addressable.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>