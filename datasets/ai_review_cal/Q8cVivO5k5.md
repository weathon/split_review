- Decision: Reject
- Avg Score: 5.50
- Scores: 3, 6, 5, 8
## Summary

This paper proposes LBN-MOBO, a Bayesian optimization framework for multi-objective problems where batch sizes are extremely large (thousands to tens of thousands) and the goal is iteration efficiency. The core idea is a novel 2M-dimensional acquisition function that performs non-dominated sorting over both the predicted objectives and their epistemic uncertainties, using NSGA-II. The paper demonstrates that existing acquisition functions (qEHVI, qNEHVI, qParEGO) fail at batch sizes beyond ~200–500 on the ZDT3 benchmark, while LBN-MOBO scales to batch sizes of 20,000 on real-world airfoil design and 3D printer color gamut problems. The approach is gradient-free and embarrassingly parallelizable.

## Strengths

- **Novel and well-motivated acquisition function**: The 2M-dimensional Pareto sorting that jointly optimizes performance objectives and their epistemic uncertainties (Eq. 7) is a clean and intuitive idea. It addresses a genuine gap — existing acquisition functions become computationally prohibitive at large batch sizes, and the paper systematically demonstrates this failure in Section 3 (Fig. 1) for qEHVI, qNEHVI, and ParEGO on ZDT3.

- **Demonstrated scalability to very large batch sizes**: Section 5.1 shows that LBN-MOBO with Deep Ensembles or MC Dropout completes ZDT3 optimization for batch sizes up to 1000, while Fig. 1 shows existing methods fail at 200–500. The real-world problems (Section 5.3) operate at batch sizes of 15,000–20,000 — a regime where no standard BO acquisition function can operate — and produce reasonable Pareto fronts.

- **Gradient-free and embarrassingly parallel acquisition**: The acquisition function uses NSGA-II for non-dominated sorting and is explicitly designed to be parallelized (line 240: "performance remains unhampered even when batch size increases"). This is a structural advantage over differentiable acquisition functions like qEHVI/qNEHVI, and shifts the bottleneck from the algorithm to the evaluation infrastructure.

- **Systematic surrogate comparison**: Section 5.1 compares Deep Ensembles, MC Dropout, HMC, SGHMC, DKL, and IBNN on ZDT3 using the 2MD acquisition function, providing a useful benchmark of neural surrogate scalability.

## Weaknesses

### Fatal
None.

### Major

1. **No external baseline comparison on real-world problems.** The real-world evaluation (Section 5.3) compares only LBN-MOBO with MC Dropout vs. LBN-MOBO with Deep Ensembles. No existing BO method (qNEHVI, qParEGO, etc.) is evaluated on these problems. The abstract claims "superiority of our method by comparing it with state-of-the-art multi-objective optimizations" (line 12), and line 299 claims to "establish the superiority of our method over a few other algorithms," but neither claim is supported by evidence in the paper. Without comparing to even a simple baseline like random sampling at the same large batch size, the reader cannot assess whether the acquisition function adds value over brute-force parallelization. This is the single most significant gap — the paper's central claim does not follow from the evidence presented.

2. **Missing contribution: regret analysis.** The introduction (line 53) lists "A novel algorithm for regret analysis of large batch, multi-objective evaluations (Section \ref{sec:regret})" as a contribution and states "Through a series of experiments, we demonstrate that the regret for LBN-MOBO consistently outperforms the counterpart optimizers." This section is entirely absent from the main paper. A contribution advertised in both the abstract and introduction that is not present is a significant omission.

3. **"Order of magnitude less iterations" claim is unsupported.** The abstract (line 8 in context) and introduction (line 40) claim the Pareto front can be obtained with "an order of magnitude less iterations." No experiment in the paper establishes this — there is no comparison showing how many iterations existing methods would need on these problems, nor any measurement of iteration counts for LBN-MOBO vs. an alternative.

### Minor

4. **Acquisition function implementation is underspecified.** The acquisition function uses NSGA-II for non-dominated sorting and mentions "parallel independent acquisitions (different NSGA-II seeds) with smaller batch sizes" (line 239). However, critical details are missing: candidate set size, population initialization, number of generations, crossover/mutation parameters, and how the smaller batches are recombined into the full batch. These are necessary for reproducibility. The method description currently reads as a high-level sketch rather than a specifiable algorithm.

5. **Uncertainty ablation is qualitative only.** Section 5.4 (Fig. 4) shows convex hulls of candidate distributions with and without epistemic uncertainty, but reports no hypervolume values, Pareto front quality metrics, or other quantitative comparison. The paper argues that uncertainty improves exploration, which is visually plausible, but the magnitude of the effect cannot be assessed. Given that this is a central component of the method, quantitative evidence is needed.

6. **No statistical rigor.** No experiments are repeated with different random seeds. The method has multiple stochastic components (initial random sampling, NSGA-II seeds, neural network training), yet all results appear to be single runs. Confidence intervals, variance bars, or repeated trial information are absent throughout.

7. **Claim about diverse activation functions is unsupported.** Line 225 states "providing a diverse set of activation functions across K members of the ensemble significantly helps with obtaining higher quality uncertainty," but no experiment or ablation supports this claim.

### Trivial

8. **Hypervolume reference point is not specified** for the real-world problems, making the metric difficult to interpret or reproduce.

9. **The noise handling section (Section 5.5)** requires manual tuning of hyperparameters α and β, and is demonstrated on a simplified (2-variable) version of the printer problem. The paper acknowledges this is a proof of concept, which is fine, but it does not contribute to the core claim.

## Nice-to-Haves

- Comparing LBN-MOBO to existing methods (qNEHVI, qParEGO) at a moderate batch size (e.g., 100–500) where both can run, to establish competitiveness on common ground.
- Comparing LBN-MOBO to random batch sampling at the same large batch size on real-world problems, to directly test whether the acquisition function adds value.
- Reporting how surrogate retraining time scales with cumulative data size across iterations (cumulative dataset can reach ~200K points after 10 iterations).
- Explicitly reporting the number of iterations Q used for each real-world experiment (though it appears to be 10 from the figures).

## Removed Points

The following points from the harsh critic were considered but are removed for the stated reasons:

- *"Section 5.5 feels like a separate contribution that is not well integrated"* — The noise handling is listed as one of four contributions and extends the acquisition function to handle aleatoric uncertainty. It is reasonably scoped and the paper acknowledges its limitations. This is a judgment call about presentation, not a concrete weakness.
- *"The paper does not specify whether the surrogate is retrained from scratch each iteration"* — Algorithm 1 (line 187) clearly states `f_{BNN}^i ← train dataset`, and the text (line 153) says "train the BNN for the next generation." Retraining from scratch on the accumulated dataset is the natural reading.
- *"The inset figure (schematic of 4D acquisition) is not explained in the caption"* — The figure is explained in the surrounding text (lines 247–250). A more detailed caption would be nice but is a formatting nitpick.
- *"The paper should not be accepted in its current form"* — This is an overall assessment, not a specific weakness.
- *"The active learning comment is a non sequitur"* — This is a subjective judgment about a single sentence in the conclusion and has no bearing on the paper's technical validity.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the evaluation gap but do not identify new technical observations about the method itself.

## Suggestions

1. **Add baseline comparisons on the real-world problems.** At minimum, compare against random sampling at the same large batch size (15,000–20,000) and report hypervolume. If possible, also compare against qNEHVI at a reduced batch size where it can run.

2. **Either include the regret analysis in the main paper or remove it from the contribution list.** The current state is misleading.

3. **Specify the acquisition function implementation details** — NSGA-II population size, number of generations, candidate generation strategy, recombination mechanism for parallel runs — to enable reproducibility.

4. **Provide quantitative uncertainty ablation results** — hypervolume at each iteration with and without epistemic uncertainty for both real-world problems.

5. **Report results with multiple random seeds** and include confidence intervals or variance bars, at least for the ZDT3 benchmark and the real-world comparisons.
