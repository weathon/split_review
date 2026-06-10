## Summary

The paper proposes POLCA (Projection Oriented Loss Change Allocation), a method to decompose changes in training loss along an arbitrary basis of the low-rank training subspace derived from Hessian eigenvectors. By clustering POLCA trajectories for individual tokens, the paper aims to reveal "hidden breakthroughs" — conceptual skills acquired at specific training times that are obscured in the aggregate loss curve. Validation is performed on a synthetic 3-digit addition task and a case study on Wikipedia text.

## Strengths

- **Novel problem framing with a well-motivated approach.** The observation that aggregate loss smooths over per-example learning dynamics is genuine and important. The idea of decomposing loss along multiple directional axes (Hessian eigenvectors), not just per-parameter or per-example, is a non-trivial extension of Loss Change Allocation that addresses a real limitation of single-axis analysis.

- **Second-order correction is methodologically sound (Equations 5–6).** The paper correctly identifies that first-order LCA is insufficient when the basis consists of Hessian eigenvectors with large eigenvalues, and provides a tractable approximation for the second-order term using per-datapoint Hessian-vector products. This is a genuine technical contribution over standard LCA.

- **Empirical discovery of temporally ordered skill acquisition (Section 4.3, Figure 2).** The paper shows that as the POLCA vector index increases (corresponding to later checkpoints and smaller eigenvalues), the sharp increase in POLCA values for the carry cluster occurs at progressively later training iterations, and later basis vectors capture finer-grained skill compositions. This non-trivial finding about the hierarchical structure of skill acquisition is genuinely invisible in the aggregate loss curve.

- **Cross-setting validation.** The method is applied to both synthetic arithmetic (3-digit addition with ground-truth skills) and real Wikipedia text, demonstrating the approach is not tailored to a single synthetic setting. In arithmetic, POLCA recovers homogeneous carry clusters for all output tokens, while loss-only clustering succeeds for only one token type (Table 1).

- **Principled, computationally feasible basis construction (Algorithm 1).** The iterative approach of projecting the Hessian onto the nullspace of collected vectors and using Hessian-vector products to avoid constructing the full Hessian ensures each new direction is orthogonal to earlier ones, addressing the concern that directions of interest change over training.

## Weaknesses

### Fatal
None.

### Major

1. **The core POLCA approximation is not directly validated.** The paper introduces a chain of approximations (replacing the per-datapoint Hessian eigenvalue with a scaled version of the aggregate eigenvalue via Equation 5) and acknowledges the strong condition required ("If the aggregate Hessian eigenvector b is close to the span of the top eigenvectors of the datapoint-specific Hessian for x"), but never directly tests whether POLCA values track actual per-direction loss changes. There is no ablation or sanity check that isolates the approximation's accuracy — e.g., comparing POLCA-attributed loss changes against brute-force finite-difference measurements along individual basis directions in the synthetic setting where ground truth is available. Without this, the reader cannot distinguish between genuine signal and artifacts of the heuristic. This is not a speculative concern: the paper's central claim is that POLCA reveals hidden structure, but the mechanism by which it does so rests on an unverified approximation.

2. **The natural language validation is substantially too thin to support the paper's generalizability claims.** The NL experiment (Section 5) examines only two output tokens (`< and>` and `<,>`) with:
   - Manual labeling of contexts by the authors, introducing subjective bias.
   - An ad hoc labeling criterion: "over 85% of the top 10% of trajectories closest to the centroid."
   - No quantitative cluster quality metrics (silhouette, adjusted Rand index, etc.).
   - No comparison against any baseline other than loss-only clustering (which yields one homogeneous cluster for one of the two tokens).
   The paper's conclusion that POLCA "recovers interpretable conceptual skills in the natural language setting" (line 285) substantially outpaces the evidence from this single case study.

3. **The comparison between POLCA and loss-only clustering is asymmetrically reported.** Table 1 reports whether "at least one" POLCA vector (out of 30) produces a homogeneous carry cluster per token, while loss-only clustering gets a single trajectory. The paper does not report how many of the 30 POLCA vectors succeed per token, what their individual carry-fraction values are, or how a combined representation would compare. Loss clustering is reported via a "maximum fraction" metric, while POLCA is reported via a binary threshold ("at least 90% carry instances") — these are different comparison standards. While the asymmetry is partially inherent to POLCA producing richer output, the lack of these details makes it difficult to assess how robustly the method recovers each skill versus capitalizing on multiplicity.

### Minor

1. **Limited experimental scope.** Only one model architecture (2-layer, 512-dim transformer), one synthetic task (3-digit addition), and one natural language dataset (Wikipedia) are tested. The paper acknowledges this limitation (line 327) but does not provide evidence that the method generalizes across model sizes or data modalities.

2. **No sensitivity analysis.** Critical parameters — number of basis vectors (30), HDBSCAN minimum cluster size (20%), checkpoint frequency (every 5 or 100 iterations), eigenvalue computation parameters — are fixed without sensitivity analysis. The paper states that "we did not observe significantly different results from adding more basis vectors in our preliminary experiments" but does not report these experiments.

3. **No comparison against simpler alternatives.** The paper compares POLCA against loss-only clustering but not against other decomposition approaches such as random projections, PCA of parameter trajectories, or standard per-example loss-curve clustering with different distance metrics. This makes it unclear whether the Hessian eigenvector basis is uniquely effective or whether any dimensionality reduction of the trajectory space would yield similar results.

4. **The "breakthrough" framing is asserted more strongly than demonstrated.** The paper claims to find "abrupt breakthroughs" (abstract, line 10) but the evidence consists of clustered average trajectories with inflection points — consistent with gradual separation that becomes visible through clustering. No per-instance analysis is provided showing that individual examples within a cluster exhibit synchronized discrete jumps at specific training iterations. The evidence supports the claim that skills are learned along specific directions at different times, but does not establish that the transitions are discrete "breakthroughs" rather than periods of more rapid but continuous learning.

### Trivial
None.

## Nice-to-Haves

- Direct validation of the POLCA approximation against ground-truth loss changes in the synthetic setting.
- Larger-scale natural language evaluation with automated skill detection and quantitative cluster-quality metrics.
- Reporting the proportion of POLCA vectors (out of 30) that yield homogeneous carry clusters per token, and reporting both methods using the same metric.
- Sensitivity analysis over clustering parameters and basis vector count.
- Comparison against random-basis or PCA-based baselines.

## Removed Points

These points were considered and removed after verification against the paper — treat them with caution:

- **"Circularity concern about Equation 6"** (Harsh Critic): The critic claimed h̃'s dependence on the aggregate loss change creates circularity. This is a misunderstanding — the ratio in Equation 5 normalizes per-example curvature relative to the aggregate, a standard approach in decomposition. Not a genuine weakness.
- **"Missing appendix / proofs"**: Excluded per instructions — parser strips these from all papers.
- **"Reproducibility concerns about undisclosed hyperparameters"**: Excluded per instructions — standard artifacts impractical to include.
- **"Formatting/style nitpicks"**: Excluded per instructions — parser artifacts, not author errors.
- **"Missing related work"**: Excluded per instructions — cannot verify without external sources.
- **Generic strength about "addressing an important problem"** (Strength Finder): Dropped — superficial and applies to many papers.
- **"Cross-domain validation" as a pure strength** (Strength Finder): Weakened and placed as a strength with caveats given the thin NL evidence, not removed outright.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Validate the POLCA approximation directly.** In the synthetic arithmetic setting, take a single basis direction, compute the true loss change via finite-difference steps, and compare against the POLCA-attributed value. Report error distributions across examples and training steps. This is essential for the method to be credible as a tool for analyzing training dynamics.

2. **Expand the natural language evaluation.** Analyze more token types, use automated context labeling (e.g., grammar-based rules), and report quantitative cluster-quality metrics (adjusted Rand index against skill labels, silhouette scores). Compare against loss-only clustering with matched evaluation standards.

3. **Report the comparison more informatively.** For each output token in Table 1, report: (a) how many of the 30 POLCA vectors yield a homogeneous carry cluster, (b) the range of carry fractions across all vectors, and (c) the carry fraction from loss-only clustering using the same threshold rather than a different metric.

4. **Add a simpler baseline.** Test whether random projections or PCA of the trajectory space produce similar clustering results. This would establish whether the Hessian eigenvector basis is specifically valuable.

5. **Substantiate the "breakthrough" claim.** Show per-instance POLCA trajectories for individual examples within a cluster, demonstrating that they exhibit synchronized, discrete jumps at specific training iterations rather than just gradual separation of cluster means.

## Score and Decision

**MY FINAL SCORE: <score>4.5</score>**
**MY FINAL DECISION: <decision>Reject</decision>**