## Summary

The paper proposes a primal-dual framework for continual learning that explicitly solves the constrained optimization problem (minimize loss on the current task subject to no-forgetting constraints on past tasks) using Lagrangian duality. Dual variables are interpreted as sensitivity indicators with respect to constraint perturbations and are used for (a) buffer partition across tasks, allocating more memory to harder tasks, and (b) per-sample buffer selection, storing only impactful samples. Theoretical sub-optimality bounds (Theorem 4.2) connect empirical dual variables to ideal statistical quantities. Experiments span four benchmarks across image, speech, and medical domains.

## Strengths

- **Explicitly solves the constrained CL problem via Lagrangian duality rather than heuristics.** The paper formulates continual learning as a constrained optimization problem (Eq. P_t, Section 2) and solves it directly via the empirical dual saddle-point problem (Eq. D̂_t, Section 3), contrasting with prior work (GEM, A-GEM) that uses gradient projections or manually-tuned loss-augmentation hyperparameters. This is a principled and well-motivated direction.

- **Theorem 4.2 provides rigorous sub-optimality bounds connecting empirical and statistical dual variables.** The bound shows \(\|\hat{\lambda}_p^\star - \lambda_u^\star\|_2^2\) in terms of model capacity (\(\nu\)), sample size (\(\tilde{n}\)), and dual variable norms, establishing that empirical dual variables converge to the statistical quantities as capacity and sample sizes grow.

- **Proposition 5.1 gives a principled basis for per-sample buffer selection.** It establishes \(-\lambda_t^\star(x,y) \in \partial P_t^\star(\epsilon(x,y))\), meaning the magnitude of per-sample dual variables directly quantifies how much that sample's constraint perturbation affects the optimal value — analogous to support vectors in SVMs.

- **Honest and thorough discussion of limitations (Section 7).** The paper openly addresses dual variable underestimation, scaling issues with many constraints, and the difficulty of distinguishing informative samples from outliers — transparency that strengthens trust in the analysis.

## Weaknesses

### Fatal
None.

### Major

- **Empirical claims are unsupported by numerical results in the text.** The abstract claims to "empirically corroborate our theoretical results," yet Section 6 contains no quantitative results whatsoever — no accuracy percentages, no forgetting scores, no standard deviations. The text describes results only qualitatively: "leads to comparatively low forgetting in almost all buffer sizes and benchmarks" (line 218). While figures exist in the original PDF, the textual description alone provides no way to assess the magnitude of any claimed improvement. This makes the empirical contribution unverifiable from the manuscript.

- **On the hardest benchmark, the method offers no benefit over random Reservoir sampling.** The paper honestly reports (line 218) that "in settings such as CIL Tiny Imagenet, no method outperforms Reservoir by a significant margin." This directly undercuts the paper's central claim that "it is both possible and beneficial to undertake the constrained learning problem directly" — at minimum, the "beneficial" part is unsupported on the most challenging setting, and the paper offers no analysis of *why* the method fails there.

### Minor

- **Theory-practice gap acknowledged but not bridged.** The theoretical results (Theorem 4.2, Proposition 4.1) rely on Assumption 2.2 (convex loss and functional space) and Assumption 2.3 (near-universality), which do not hold for the deep neural networks used experimentally. The paper acknowledges this (line 101: "the inner minimization, however, is generally non-convex") but makes no attempt to empirically measure the gap — e.g., checking whether the dual function is approximately strongly concave on actual models.

- **Sample-level dual variable underestimation acknowledged but unresolved.** The paper identifies (Section 7) that a task may appear easy initially (low \(\lambda\)) but become difficult later, and already-discarded samples cannot be recovered. The proposed fix (augmented samples or current-task samples) is stated without any experimental validation, leaving a gap in the practical reliability of the sample-selection method.

- **Forgetting tolerance ablation conducted only on Seq-MNIST** (Section 6.1, Figure 5). MNIST is a trivial dataset where almost any method works. An ablation on a harder benchmark (e.g., SpeechCommands or Tiny-ImageNet) would be far more informative about the method's sensitivity to this critical hyperparameter.

- **No analysis of computational overhead.** The sample-level variant maintains O(N) per-sample dual variables and performs dual updates each iteration, yet no wall-clock time or per-iteration cost comparison against baselines is provided.

- **Dual learning rates differ by 10× across settings with no justification.** The paper reports \(\eta_d = 0.05\) for most datasets and \(\eta_d = 0.5\) for Tiny-ImageNet (line 214), with no sensitivity analysis or tuning rationale given.

- **Baseline set is limited.** Four replay methods from Mammoth (Reservoir, X-DER, GSS, iCARL) are included. The selection criteria are not explained, and several more recent replay-based methods are absent.

### Trivial
None.

## Nice-to-Haves

- Reporting a summary table with mean ± std accuracy and forgetting for all benchmarks, both CIL and TIL settings, would transform the evidential strength of the paper from qualitative to quantitative.
- Analyzing *why* the method fails to beat random Reservoir on Tiny-ImageNet CIL (task similarity violation? constraint scaling? tolerance mismatch?) would be more valuable than the current negative report.
- Empirically measuring the strong concavity constant of the dual function on actual neural network models would help bridge the theory-practice gap.

## Removed Points

The following points from the inputs were removed with justification:

- **"Algorithm 1 full description missing"**: Parser artifact — appendix/supplementary material stripped from all papers. The algorithm exists in the original submission.
- **"Theorem 3.2 not stated in text"** / **"Section 4.1 missing"**: Parser artifacts — LaTeX theorem environments and subsections may not survive extraction.
- **"Missing related works"**: Not permissible to flag; I cannot verify existence of works not already known.
- **Reproducibility nitpicks about hyperparameters** (dual learning rate selection, training details): The paper provides architectures, learning rates, and references to Mammoth implementations; this is adequate for a conference submission.
- **Criticisms inflated from Minor to Fatal or Major**: The harsh critic's framing of the theory-practice gap as "structural" was demoted to Minor because the paper acknowledges it; the sample-selection tension was demoted from "fundamental" to Minor because the paper identifies it as a limitation.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a results table with mean accuracy, forgetting, and standard deviations for all four benchmarks and both CIL/TIL settings — this is the single most impactful improvement.
2. Include a dedicated analysis of the Tiny-ImageNet CIL result: is the failure due to violated task similarity, constraint scaling, tolerance misconfiguration, or something else?
3. Benchmark and report wall-clock time overhead, especially for the sample-level variant where dual variables scale with buffer size.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>