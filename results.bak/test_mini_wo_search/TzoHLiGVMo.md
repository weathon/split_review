Now let me produce the final consolidated review.

## Summary

The paper introduces ODEFormer, the first transformer-based method for inferring symbolic, multidimensional ODE systems from a single noisy, irregularly sampled solution trajectory. The model is pre-trained on large-scale synthetic ODE data via sequence-to-sequence translation, avoiding finite-difference derivative estimation. The authors also release ODEBench, a curated benchmark of 63 dynamical systems (1D–4D). On both the Strogatz dataset and ODEBench, ODEFormer achieves higher reconstruction accuracy than eight established baselines (GP, SINDy, ProGED) under noise and subsampling, while running orders of magnitude faster than most competitors.

## Strengths

1. **State-of-the-art benchmark performance.** On both the Strogatz dataset and the newly introduced ODEBench, ODEFormer achieves the highest average reconstruction accuracy across multiple noise levels and subsampling ratios (Fig. 4). The paper honestly reports that on clean data PySR occasionally wins, but "as noise and subsampling kick in, ODEFormer gains an increasingly large advantage over all other methods."

2. **Substantially faster inference.** ODEFormer runs "on the order of seconds, versus minutes for all other methods except SINDy" (Fig. 4, rightmost panels). This is a concrete, measured advantage over prior dynamical SR approaches that require per-system optimization.

3. **Systematic robustness ablation.** The ablation study on synthetic data (Fig. 3) varies system dimension, operator count, noise, subsampling, and trajectory length across 10,000 examples, showing graceful degradation. The result that performance is "surprisingly insensitive to the number of points in the trajectory" is a controlled demonstration of robustness that goes beyond the benchmark comparisons.

4. **Introduction of a curated multi-dimensional benchmark.** ODEBench (63 ODEs, dimensions 1–4, including chaotic systems) is a significant resource for the field, addressing the limitations of the prior Strogatz dataset (only 7 systems, all 2D, imprecise integration). The benchmark is publicly released with descriptions and sources.

## Weaknesses

### Fatal
None.

### Major

1. **Limited training operator vocabulary restricts the scope of symbolic discovery.** The training data generator samples binary operators from {+, ×} only and unary operators from {sin, x↦x⁻¹, x↦x²} only (lines 148, 154). The paper does not analyze the operator composition of either Strogatz or ODEBench in the main text, nor does it quantify what fraction of test ODEs fall outside this vocabulary. If a substantial fraction of test systems use operators like cos, exp, log, or tanh (which are routine in dynamical modeling), then ODEFormer cannot recover the correct symbolic form — at best it finds a surrogate expression that fits the trajectory. This limitation does not invalidate the contribution (the method still provides a fast, robust functional approximation), but it undermines the framing of "inferring dynamical laws in symbolic form" as a universal capability. The authors should characterize the operator coverage of ODEBench, and report symbolic-equivalence rates (or structural similarity) for test cases within the trained vocabulary.

2. **Evaluation relies on trajectory R² rather than symbolic correctness.** The primary metric is reconstruction R² thresholded at 0.9. While the paper justifies numerical evaluation over symbolic comparison (lines 253–258 — citing expression ambiguity and non-deterministic simplification), the central claim of "symbolic form" inference demands evidence that the predicted expressions are symbolically correct, not just that they fit one or two trajectories. The paper's own generalization experiment shows that "half the correctly reconstructed ODEs do not match the ground truth symbolically" (line 378), confirming the gap. Reporting at least a secondary metric — e.g., the fraction of predictions that are symbolically equivalent to the ground truth (after simplification) for in-vocabulary test cases — would close this gap and substantiate the "symbolic discovery" claim.

### Minor

1. **Rescaling procedure has an unaddressed edge case.** The inference-time rescaling divides by xᵢ(t₀) to normalize initial values (line 233). This fails when any component of the initial condition is zero (e.g., a harmonic oscillator starting at the equilibrium). The paper does not discuss handling of this case.

2. **Ablation study lacks variability estimates.** The synthetic ablation (Fig. 3) averages over 10,000 examples per setting but does not report error bars or confidence intervals. Since the ablation is the primary controlled evidence for robustness, showing variation across independent data draws would strengthen confidence.

3. **Baseline hyperparameter optimization protocol could overfit.** The paper states that for each baseline, "we perform a separate hyperparameter optimization for each run to ensure maximal fairness" (line 341). Optimizing per noise realisation and test ODE risks overfitting to the specific run; a held-out validation split per run would clarify the protocol.

### Trivial

- The example tokenization in Section 4 illustrates `cos(2.4242 x)` (line 224), but cos is not in the training vocabulary. This could confuse readers about what operators the model actually supports.

## Nice-to-Haves

- **Failure analysis.** A per-ODE breakdown of ODEFormer's failures (e.g., concentrated on systems with operators outside the vocabulary, high-dimensional, or chaotic systems) would help users understand the method's limitations and guide improvements.
- **Ablation of the rescaling scheme.** Showing what happens without time/initial-condition rescaling at inference would quantify its importance.
- **Additional metrics.** Reporting median/average R² (not just thresholded accuracy) would give a fuller picture of typical performance.

## Removed Points

These points from the reviewers were evaluated and removed:

1. **"Unfair advantage in noise regime" / "No baseline uses integration-based fitness."** The paper includes ProGED (Table 1, line 333), which uses "MC on probabilistic context free grammars" and does NOT require finite differences (column "f.d.: no" at line 333, confirmed at line 342). The claim that no baseline avoids finite-difference amplification is factually incorrect. **Removed.**

2. **"Missing appendix analysis of operator composition."** The parser strips the appendix from all papers; the operator analysis for ODEBench may appear there. Cannot verify its absence from the original submission. **Removed** per hard rules.

3. **"R² threshold at 0.9 is arbitrary and not justified."** The paper explicitly justifies this choice (line 276): "Since R² is unbounded from below, average R²-scores across multiple predictions may be severely biased by even a single particularly poor outlier." The paper also notes that distribution plots are in the appendix. **Removed** — the paper already addresses this.

4. **Generic strength about "addressing an important problem."** The Strength Finder's generic statements about problem importance were removed per filtering rules.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface concerns about the scope of the method's operator coverage and the gap between trajectory-fit evaluation and symbolic-correctness evaluation — issues the paper partially acknowledges but does not fully resolve. No reviewer identified a fundamentally new perspective on the method or its broader implications.

## Suggestions

1. **Add operator-coverage analysis.** List all operators appearing in ODEBench's 63 equations, indicate which are in the training vocabulary, and report results separately for in-vocabulary vs. out-of-vocabulary test cases. This would clarify the method's true symbolic discovery capability.

2. **Report symbolic accuracy as a secondary metric.** For test ODEs whose true operators are within the training vocabulary, report the fraction of predictions that are symbolically equivalent (after simplification, with a defined tolerance for constant variation). This would directly substantiate the "symbolic form" claim.

3. **Tone down scope claims.** Given the limited operator vocabulary, reframe claims from "inferring dynamical laws" (which implies universal discovery) to "inferring symbolic ODEs within a fixed operator library" or similar, unless the above analyses show that ODEBench's ODEs are largely covered.

4. **Address the xᵢ(t₀) = 0 edge case** for the rescaling procedure (e.g., add a small epsilon before division, or note that trajectories with zero-valued initial components are excluded).

**Score and Decision**

The paper presents a well-executed engineering contribution with strong empirical results, a useful new benchmark, and clear practical advantages (speed, robustness to noise/subsampling). The two major weaknesses — limited training vocabulary and the reliance on trajectory R² rather than symbolic correctness — are real but do not invalidate the core contribution. They primarily demand better characterization of the method's scope and toned-down claims. The paper should be accepted contingent on addressing the operator-coverage analysis and symbolic accuracy reporting.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>