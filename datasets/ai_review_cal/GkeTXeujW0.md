- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 3, 5
Here is my final consolidated review.

---

## Summary

The paper proposes CausalDiffusion, a diffusion model that generates multivariate time-series along with ground-truth causal graphs by embedding a Vector Autoregressive (VAR) structure into the denoising network's output. The model produces initial timesteps and coefficient vectors, then reconstructs the remaining time-series via a VAR recurrence. Causal graphs are extracted from the learned coefficients via percentile-based thresholding. The paper evaluates against CAUSALTIME and CR-VAE on three datasets, showing competitive or superior time-series fidelity (MMD, Discriminative Score) and better causal graph false-positive rates, and provides a benchmark of 12 TSCD algorithms on the generated data.

## Strengths

1. **Novel architectural design for causally-aware generation.** Embedding a VAR(τ) structure directly into the denoising network's output (Section 4.2) is a clever way to make the generative process causally interpretable by design. The model generates initial timesteps and coefficients simultaneously in one forward pass, then reconstructs the series via VAR — this cleanly ties the causal graph extraction to the model's internal representations rather than requiring post-hoc explainability tools. The inference time is 15× faster than CAUSTIME (18.20s vs 287.91s on Henon, Table 1) because graph extraction is simultaneous with generation.

2. **Strong empirical results on multiple metrics.** In Table 1, the best CausalDiffusion variant (OUR W/L2 W/DTW) achieves the lowest MMD on all three datasets (e.g., 0.0049 vs 0.0390 for CAUSALTIME and 0.0066 for CR-VAE on Henon), the best or near-best Discriminative and Predictive Scores, and the best GC-FPR and Graph-FPR across all datasets. These results are supported by 10 seeds with reported means and standard deviations.

3. **Relaxes the stationarity assumption.** Unlike CR-VAE (which learns a single fixed causal matrix), CausalDiffusion generates a unique causal graph per sample (Section 4.3, Definition 4.1). This is a meaningful departure from prior work and better reflects real-world settings where causal relationships may vary across time windows.

4. **Practical utility demonstrated through a TSCD benchmark.** Section 6 benchmarks 12 causal discovery algorithms on CausalDiffusion-generated data (Table 2), showing that no algorithm achieves near-perfect scores — supporting the paper's motivation that existing synthetic benchmarks are too easy and more challenging ones are needed.

5. **Introduction of GC-FPR and Graph-FPR metrics.** These metrics (Section 5.3) account for samples that may not exhibit a known causal effect, which is a principled approach for evaluating causal graph realism when not every time window shows the phenomenon.

## Weaknesses

### Major

1. **Threshold sensitivity for graph extraction is not analyzed.** Definition 4.1 introduces parameters ρ (dataset-level percentage) and p (sample-level percentile) that determine which VAR coefficients are considered causal. The paper does not report what values of ρ and p were used for the main results in Table 1, nor does it analyze how GC-FPR and Graph-FPR vary across different thresholds. Section 6 mentions a "top 1% approach" was also tested, but the results are not shown in the main paper. Without sensitivity analysis, the quantitative graph-quality claims rest on unreported free parameters. This is the most significant weakness because it directly affects the interpretation of the core evaluation.

### Minor

2. **Graph evaluation confounds generative quality with extraction method.** CausalDiffusion extracts graphs from internally generated VAR coefficients, while CAUSALTIME uses DeepSHAP (a post-hoc explainability tool). The comparison on GC-FPR and Graph-FPR therefore reflects differences in both the generative model AND the graph extraction procedure. The paper attributes the improvement to "our model" (Section 5.4), which conflates two components. While comparing full end-to-end pipelines is valid, the extent to which the better graph metrics come from the generative distribution vs. the extraction method is unclear. The paper would be strengthened by showing that the time-series themselves carry better causal signal — e.g., by training a VAR model on the outputs of all methods and extracting graphs via the same percentile procedure.

3. **Benchmark ground truth is model-derived.** The TSCD benchmark (Section 6) uses CausalDiffusion's own extracted graphs (strongest 15% of connections) as the ground truth for evaluating discovery algorithms. This creates circularity: the benchmark measures how well algorithms recover the patterns the paper's thresholding procedure identifies, rather than an externally verified causal structure. The paper partially mitigates this by also using datasets with known causal relationships (Henon, Rivers), but the main benchmark table relies entirely on model-derived labels.

4. **Limited to linear causal relationships (acknowledged but not tested on nonlinear systems).** The paper acknowledges this limitation (Section 7), but the impact is not assessed. The Henon dataset (which has squared terms in its equations) provides implicit evidence that the model can approximate some nonlinear structure linearly, but the paper does not test on a system where the true causal graph is known to involve specifically nonlinear relationships that a VAR model cannot capture. This would be useful for scoping the method's applicability.

5. **Architecture of the denoising network (DENθ) is unspecified.** The paper does not describe whether DENθ is a Transformer, CNN, MLP, or another architecture, nor how the coefficient output is dimensionally structured beyond the textual description. This hurts reproducibility.

6. **No statistical significance tests.** With 10 seeds reported, the paper could include simple significance tests for the key comparisons (e.g., CausalDiffusion vs. CAUSALTIME on MMD and Graph-FPR). Many differences are modest, and significance tests would clarify which improvements are systematic.

### Trivial

- The cross-correlation metric is defined only as "MAE between the correlation values" without specifying the lags considered.
- The paper uses both "CausalDiffusiom" (typo in the abstract, line 8) and "CausalDiffusion" — minor but should be fixed.

## Nice-to-Haves

- Applying a consistent graph extraction method (e.g., percentile-based VAR coefficients) to all generative models would disentangle generative quality from extraction methodology.
- A threshold sensitivity analysis (ρ = 1%, 5%, 10%, 20%) on the Henon dataset where ground truth is known would substantially strengthen confidence in the graph extraction procedure.

## Removed Points

These points were flagged by reviewers but removed after verification:

- **"Henon chaotic maps have linear causal terms"** (from Harsh Critic): Factually incorrect. The Henon equations (Section 5.1) contain squared terms, making the causal relationships nonlinear. The paper's VAR model provides a linear approximation of these nonlinear dynamics, which actually makes the positive results on Henon more notable, not less.

- **"Not autoregressive claim is misleading"**: The paper (line 125) correctly states that the generation framework is not autoregressive because the denoising network produces all initial timesteps and coefficients simultaneously in one forward pass. The subsequent VAR-based reconstruction is a post-processing step, not an autoregressive generation loop. The critic's reading conflates post-processing with generation.

- **"First diffusion model claim is overstated"**: Li et al. (2023) uses a VAE, not a diffusion model; Cheng et al. (2024) uses normalizing flows, not a diffusion model. The claim "first diffusion model capable of generating causally related time-series" is precise and accurate.

- **"Outperforming on graph metrics could reflect DeepSHAP noise"**: While this is a valid concern about confounded evaluation (retained as Minor Weakness #2 above), the critic framed it as a "structural issue" that invalidates the comparison. The paper compares end-to-end pipelines, which is standard practice. The improvement is supported by multiple metrics (MMD, Discr., Pred., GC-FPR, Graph-FPR), not just graph metrics.

- **Missing related works / formatting / reproducibility nitpicks**: Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface observations that fundamentally reframe or extend the paper's contributions.

## Suggestions

1. Report the specific ρ and p thresholds used for all experiments, and include a sensitivity analysis showing how GC-FPR and Graph-FPR vary across threshold values (especially on the Henon dataset with known ground truth).
2. Apply a consistent graph extraction methodology across all generative models (e.g., fit a VAR model to each method's outputs and extract graphs via the same percentile procedure) to disentangle generative quality from extraction method.
3. Add a brief description of the denoising network architecture (layers, types, dimensionalities) for reproducibility.
4. Include simple significance tests (e.g., paired t-tests) for the key comparisons in Table 1.
