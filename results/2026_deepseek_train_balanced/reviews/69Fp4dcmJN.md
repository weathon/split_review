## Summary

This paper proposes scalability improvements to the Banded Matrix Factorization (BandMF) mechanism for differentially private ML. The contributions are: (1) an implicit strategy optimization that reduces per-iteration cost from O(n³) to O(n²·b) for general banded strategies, (2) a Toeplitz-restricted variant that reduces this further to O(n·b), and (3) a distributed noise generation scheme that shards the b×d state across machines. Together these extend BandMF from ~10⁴ iterations / 10⁷ parameters to beyond 10⁶ iterations / 10⁹ parameter-scale models with ≤2% RMSE degradation.

## Strengths

- **Genuine asymptotic complexity improvements.** The implicit objective evaluation (Algorithm 3) avoids materializing n×n matrices, cutting per-iteration strategy optimization from O(n³)/O(n²) to O(n²·b)/O(n·b). The Toeplitz variant (Proposition 2) drops this further to O(n·b)/O(n). These are clean, well-explained algorithmic innovations that directly address the known bottleneck in BandMF.

- **Quantified approximation quality of the Toeplitz restriction.** The paper measures suboptimality of the Toeplitz variant and shows it is ≤2% in expected error, and ≤0.25% in the practical regime (n≥16384, b≤32). This is a concrete, bounded trade-off — notably better than the concurrent BandSqrt baseline (up to 25% suboptimality, line 216).

- **Distributed noise generation with measured overhead.** The sharding strategy (Section 3.3) is embarrassingly parallel and requires zero communication between machines until noise addition. Experimental evidence on 32 TPU v3 cores with a 100M-parameter BertBase model shows noise generation time is 1–3 orders of magnitude less than per-example gradient clipping (Figure 3a, lines 257–261).

- **Head-to-head RMSE comparison against concurrent scalable mechanisms.** Figure 1b compares Amplified BandMF against DPSGD, Tree Aggregation, Stamping, FHU, and the concurrent Buffered Toeplitz. Amplified BandMF achieves ~2× better RMSE than DPSGD and Buffered Toeplitz at ε=1, and 19% better at ε=8. This is the first such comparison showing a scalable BandMF variant dominating alternatives across the full ε range.

## Weaknesses

### Major

- **Gradient computation for the implicit optimization is not specified, leaving the O(n²·b) complexity claim for each L-BFGS iteration incomplete.** The paper states (lines 112, 140) that L-BFGS requires gradient evaluations and that gradient computation "can be more time and memory intensive than the loss calculation," but no gradient algorithm is provided, and its complexity is not analyzed. The forward pass (Algorithm 3) is O(n²·b), but without the gradient complexity the practical per-iteration cost is unsubstantiated. The same concern applies to the Toeplitz variant. While empirical convergence results (line 215) suggest tractability, a complexity claim without the corresponding gradient analysis is a methodological gap.

### Minor

- **Headline scaling claims (10⁶ iterations, 10⁹ parameters) are supported by complexity analysis and component-level experiments, not end-to-end training at those scales.** The abstract states BandMF can "effectively handle settings with over 10⁶ training iterations and 10⁹ model parameters." The strategy optimization demonstrably scales to n > 10⁶ (line 214), and distributed noise generation is validated on a 100M-parameter model (Figure 3a). However, no end-to-end training experiment is run at anything close to 10⁹ parameters or 10⁶ iterations. The paper's illustrative examples (lines 175–185) and the billion-parameter framing are aspirations, not demonstrations. This gap between the abstract's claim and the empirical evidence is significant enough to warrant recalibration.

- **The paper's own experiments show RMSE is an imperfect proxy for learning performance with adaptive optimizers (Section 3.4), which weakens the force of the RMSE-based SOTA claims.** For adaptive optimizers, strategies with fewer bands yield better learning performance at the same RMSE (line 291). This means the RMSE advantages of larger b reported in Figures 1a–b and 2a–b may not translate proportionally to actual training utility. The paper acknowledges this limitation (lines 284, 318) but does not quantify how much the headline comparisons overstate the practical benefit of many-band strategies. While this does not invalidate the scalability contributions, it means the RMSE-based claims should be interpreted with significant caveats beyond what the current framing conveys.

- **The data partitioning requirement (Algorithm 2, line 49–51) may interact poorly with realistic data pipelines.** Training requires pre-partitioning the dataset into b fixed subsets with cyclic assignment, which is a non-standard constraint. The paper does not discuss how this interacts with sharded data loading, shuffling, or distributed training frameworks. This is a practical concern for adoption.

### Trivial

- **Indexing in Algorithm 3 (line 130) is hard to verify from the text.** The mapping between the parameterization Θ and the forward-substitution recurrence is not explained clearly enough to confirm correctness without re-deriving from scratch. The paper's reported convergence to the same solutions as prior work (line 215) suggests the implementation is correct, but the exposition could be clearer.

## Nice-to-Haves

- Reporting wall-clock time and peak memory for strategy optimization at n=10⁵ and n=10⁶ (not just that it "ran") would strengthen the scalability claims substantially.
- A derivation or quantitative bound on suboptimality for the b* ≈ ε√n / k rule of thumb (line 254) would make it more useful to practitioners.
- An end-to-end training experiment at a scale meaningfully larger than 4M parameters (even a single run at 100M+ parameters with the scalable mechanism) would bridge the gap between the component-level validation and the headline claims.

## Removed Points

These points from the inputs were removed with brief justification:

- **"RMSE is a systematically misleading proxy that overstates the significance of scaling to many bands" (Harsh Critic, Critical Issue 1, fatal framing):** The paper explicitly acknowledges this limitation in both Section 3.4 (lines 284, 291) and the Limitations section (line 318). The core claim is about enabling scaling with minimal RMSE degradation, not that RMSE perfectly predicts learning performance. The paper's own finding is a secondary insight, not evidence against the primary contribution. This is retained as a minor weakness (above), not a fatal issue.

- **"The b* ≈ ε√n / k rule of thumb needs derivation" (Harsh Critic, under Missing Parts):** This is presented as an empirical heuristic ("a good rule of thumb," line 254) derived from systematic ablations. While a derivation would strengthen it, expecting formal error analysis for a heuristic in an empirical paper is scope creep. Moved to Nice-to-Haves.

- **Several formatting/style nitpicks and "strengthening on its own terms" points:** These are generic or speculative, not concrete weaknesses. Moved to Nice-to-Haves or removed.

- **Strength Finder's claims about "important problem" framing:** Generic praise removed per instructions. Only concrete, evidence-grounded strengths retained.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Specify the gradient computation for the implicit optimization** — provide the algorithm and analyze its complexity. At minimum, state whether gradients are computed analytically (e.g., via automatic differentiation through the forward-substitution steps) or numerically, and report the measured per-iteration time for the optimization at various (n, b) settings.
2. **Recalibrate the scaling claims in the abstract.** "Effectively handle" 10⁹ parameters is defensible as a capability claim backed by the distributed noise generation analysis, but it would strengthen the paper to explicitly distinguish between what is empirically demonstrated and what follows from complexity analysis and scaling arguments.
3. **Address the RMSE proxy gap more directly.** The paper finds that RMSE overestimates the benefit of large b for adaptive optimizers. A short discussion quantifying how this affects the headline comparisons (e.g., "if the proxy gap reduces the effective advantage of b=64 over b=8 by X%, the SOTA margin over DPSGD shrinks from 2× to Y×") would be more informative than the current standalone acknowledgment.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>