- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6
Now I have a thorough understanding of the paper and all review inputs. Let me produce the consolidated review.

## Summary

The paper introduces Physics-Informed Gaussians (PIGs), a hybrid PDE solver that combines learnable Gaussian functions (with trainable positions and shapes) with a lightweight MLP. This enables dynamic adaptive mesh-like behavior within the standard PINN optimization framework. The method is evaluated on five challenging PDE benchmarks and achieves competitive or superior accuracy compared to existing methods, often with far fewer parameters.

## Strengths

- **Dynamic adaptation of basis functions is convincingly demonstrated**: The ablation study (Table 4, labeled "ablation-MLPandPosition") shows that learnable Gaussian positions (μ) consistently outperform fixed positions across all five PDEs, e.g., Allen-Cahn error dropping from 1.82e-3 (fixed) to 7.27e-5 (learned). Figure 1 visualizes Gaussians migrating to regions of abrupt solution change during training, directly confirming the claimed adaptive allocation of representational capacity.

- **Competitive accuracy across multiple PDE benchmarks with high parameter efficiency**: Table 1 reports that PIG achieves the best relative L² error among compared methods on 4 of 5 equations (Helmholtz, Nonlinear Diffusion, Flow Mixing, Klein-Gordon). On Allen-Cahn, PIG (5.93e-5 best) is within the same order as PirateNet (2.24e-5) while using roughly 20K parameters versus >250K. The parameter count comparison on Allen-Cahn is explicitly documented and compelling.

- **Robustness to architectural choices**: The hyperparameter analysis (Table 5, labeled "hh_ablation_study") systematically varies MLP width (4–256 hidden units) and input dimension (1–4) for the Helmholtz equation, yielding relative L² errors all within a narrow range (5.21e-3 to 1.22e-2), demonstrating that the method is not brittle to architectural choices.

- **Theoretical grounding**: Section 3.3 provides a universal approximation theorem for PIGs by extending the RBF universal approximation theorem (Park & Sandberg 1991) to include learnable covariance matrices and the lightweight MLP, formally establishing that PIGs are dense in continuous function spaces.

## Weaknesses

### Fatal
None. The core claims (adaptive mesh via learnable Gaussians, competitive accuracy, parameter efficiency) are supported by the experimental evidence. The identified weaknesses are substantive but addressable and do not invalidate the paper's central contributions.

### Major

- **Baseline comparisons rely entirely on published numbers without controlled re-implementation**. The paper reports PIG results with mean±std over three seeds but lists most baselines as single values from prior papers (without error bars). For Helmholtz, the paper compares against PIXEL using L-BFGS — but differences in collocation point distributions, initialization, and stopping criteria can affect results. The paper acknowledges this difficulty (line 229: "the sensitivity of PINN variants to hyperparameters complicates fair comparisons"), but this does not remove the evidential gap. At minimum, re-implementing the most directly comparable baselines (e.g., PIXEL and SPINN) under the same training conditions would substantially strengthen the evaluation. Without this, the numerical superiority claim on 4 of 5 equations has uncontrolled confounds.

- **The efficiency/convergence claim lacks timing or FLOPs evidence**. The paper asserts faster convergence and lower per-iteration cost (line 218: "computational costs per iteration of ours are significantly lower than JAX-PI") but provides no wall-clock timing, FLOPs measurements, or GPU-hour comparisons. The error-versus-iteration curves (Figures 2–5) show iteration-level convergence, which is informative, but per-iteration costs differ across methods — a small MLP with 20K parameters might be cheaper per forward pass, but PIG with 4000 Gaussians requires computing Gaussian evaluations for every collocation point. The paper mentions leveraging locality to reduce computation (line 356) but does not confirm whether this was actually used in the experiments. Without timing data, the stated efficiency advantage is an assertion rather than a demonstrated result.

### Minor

- **The covariance matrix ablation is confounded by differing Gaussian counts**. Table 6 compares dense covariance matrices (50 Gaussians) against diagonal matrices (4000 Gaussians) for Nonlinear Diffusion, and finds similar error levels. The paper acknowledges the difference in Gaussian count (line 334), but this confound makes it impossible to attribute the similar errors to the covariance structure. The comparison does not serve as a clean ablation of covariance type.

- **Non-monotonic behavior in the Gaussian-count sensitivity is not discussed**. Table 2 (sensitivity-gaussian) shows a clear anomaly: for Nonlinear Diffusion, increasing from 800 Gaussians (1.95e-3) to 1000 Gaussians (7.33e-3) causes a sharp accuracy drop, followed by partial recovery at 1200 (3.96e-3). This could indicate training instability or overfitting, but the paper states "Overall, we observe a positive correlation" without noting or explaining this non-monotonic behavior.

- **Several reproducibility details are missing**: the initialization scheme for Gaussian positions (e.g., uniform grid vs. random) is not reported, and the exact number of collocation points per equation is not given. The paper reports which optimizer was used for each equation (Adam vs. L-BFGS) but omits learning rate schedules and stopping criteria; these details are important for a methods paper seeking broad adoption.

### Trivial
None.

## Nice-to-Haves

- A direct comparison or qualitative discussion with adaptive mesh-based PINN methods (e.g., DMIS, MMPDE-Net) would strengthen the positioning of PIG within the adaptive PDE solving literature. These are cited in related work but not compared.
- An experiment testing the overfitting claim (e.g., increasing the number of Gaussians beyond current range while monitoring generalization error) would further motivate the method's design.
- A simple initialization heuristic for the number and placement of Gaussians would aid adoption.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Introduction claim about fixed-grid methods requiring high resolution is stated without citation"** — This is a minor, context-level motivation statement about a well-known limitation of fixed grids; it does not affect the paper's technical contribution.
2. **"Paper does not discuss how to choose the number of Gaussians or initial positions"** — Partially overlapping with reproducibility details. Kept a condensed version under missing reproducibility details; removed the extended version since it asks for material that goes beyond standard expectations for a first methods paper.
3. **"Missing comparison with DMIS, MMPDE-Net"** — Scope creep. The paper is not required to compare against every adaptive method. These are cited in related work.
4. **"Learning rate schedules and stopping criteria not reported"** — Per Hard Rules, hyperparameter-level reproducibility nitpicks of this granularity are removed. The more structural omission (initial Gaussian placement, collocation point counts) is retained in Minor weaknesses.
5. **"PIG uses locality trick mentioned but not confirmed as used in experiments"** — This is noted in the Major weakness about timing data, but the separate framing as a standalone criticism is removed.
6. **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem") — Removed. Only strengths anchored in specific evidence are retained in the Strengths section above.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely agree on the paper's strengths (dynamic adaptation, competitive accuracy, parameter efficiency) and weaknesses (uncontrolled baseline comparisons, lack of timing data). The harsh critic provides a deeper analysis of the evaluation gaps, while the strength finder correctly identifies the ablation study and robustness analysis as concrete evidence. The convergence of both reviews on the central weakness — reliance on published numbers without controlled re-implementation — reinforces that this is the most significant issue facing the paper, but neither review questions the soundness of the proposed architecture or the validity of the core idea.

## Suggestions

1. **Re-implement top-2 baselines (PIXEL and SPINN)** under the same training pipeline (same collocation points, optimizer schedule, seeds) to eliminate the uncontrolled comparison concern. Provide results with error bars.
2. **Report wall-clock training time** (or FLOPs) for PIG and baselines on at least the Allen-Cahn and Helmholtz equations to substantiate the efficiency claim.
3. **Clarify whether locality-based acceleration** (evaluating only nearby Gaussians) was used in the reported experiments, and if so, provide details. If not, note this explicitly and discuss the computational cost implications.
4. **Add a brief discussion** of the non-monotonic behavior in the Gaussian-count sensitivity table to help readers understand potential training instability.
5. **Report the Gaussian initialization scheme** (uniform grid over the domain?) and the number of collocation points used for each equation in the main paper or supplement.
