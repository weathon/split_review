Now I have all the information needed. Let me carefully construct the review.

## Summary

This paper tackles scalability bottlenecks in the Banded Matrix Factorization (BandMF) mechanism for differentially private ML. It contributes: (1) an implicit strategy optimization algorithm reducing complexity from O(n³)/O(n²) to O(n²·b)/O(n·b) for general banded strategies and O(n·b)/O(n) for banded Toeplitz strategies—enabling optimization beyond n=10⁶; (2) a distributed noise generation scheme via coordinate-wise sharding that eliminates the b·d memory bottleneck. The paper demonstrates through RMSE-based evaluation that the scalable BandMF variants retain state-of-the-art performance, with Amplified BandMF achieving up to 2× better RMSE than competing scalable mechanisms at ε=1.

## Strengths

1. **Efficient strategy optimization with proven complexity gains.** The implicit computation (Alg. 3) reduces per-iteration objective evaluation from O(n³) to O(n²·b) time and O(n²) to O(n·b) space. This enables scaling to n≈10⁵ without sacrificing solution quality—Figure 1a confirms convergence to the same solutions as prior work wherever the latter could run. The paper's complexity analysis is clear and the improvement is substantial: a factor of n/b in both time and memory.

2. **Banded Toeplitz strategies scale to n>10⁶ with negligible RMSE loss.** By restricting to banded Toeplitz matrices, the paper achieves O(n·b) time and O(n) space for strategy optimization (Proposition 2). Figure 1a shows this scales beyond n=10⁶ while incurring <2% suboptimality; in the most practical regime (n≥16384, b≤32) suboptimality is ≤0.25%. This is a direct and compelling scalability result.

3. **Distributed noise generation addresses the b·d memory bottleneck.** The paper correctly observes that the per-coordinate independence of Algorithm 1 makes noise generation embarrassingly parallel across machines. Each machine maintains only its shard of the b-1 previous noise vectors, requiring no inter-machine communication until noise addition. The paper provides a concrete analysis: for a 1B-parameter model with 1024 machines and b=256 bands, per-machine overhead drops from 1 TB to 1 GB. The microbenchmark on a 100M-parameter model with 32 accelerators (Figure 4a) validates that noise generation is 1–3 orders of magnitude faster than per-example gradient clipping.

4. **State-of-the-art RMSE across all tested settings.** In comprehensive comparisons (Figure 1b), Amplified BandMF achieves the lowest RMSE among all scalable mechanisms across ε∈[1,8], with improvements of ≈2× over DPSGD and Buffered Toeplitz at ε=1 and 19% at ε=8. Unamplified BandMF also beats Buffered Toeplitz by ~5% across all ε.

5. **Empirical investigation of the RMSE-learning link with honest reporting.** Section 4.3 directly tests whether RMSE predicts learning performance. The finding that RMSE is a reliable proxy for non-adaptive optimizers but not for adaptive ones is an informative contribution that refines the evaluation framework. The paper acknowledges this limitation explicitly in Section 6.

## Weaknesses

### Fatal
None.

### Major

1. **Scalability claim for 10⁹ parameters lacks empirical support.** The abstract states the mechanism can "effectively handle settings with over 10⁶ training iterations and 10⁹ model parameters." While the 10⁶-iteration claim is supported by the Toeplitz optimization experiments (Figure 1a), the 10⁹-parameter claim is not. The distributed noise generation experiment (Figure 4a) uses a 100M-parameter model on 32 TPU v3 cores—two orders of magnitude smaller than the claimed capability. The three examples at the end of Section 3.3 are hypothetical calculations, not experimental evidence. The scaling argument (embarrassingly parallel, per-machine overhead analysis) is logically sound, but the paper presents the claim as an achieved capability rather than an extrapolation. This asymmetry between the framing and the evidence should be corrected.

### Minor

2. **RMSE-learning gap acknowledged but not bridged for the claims that rely on it.** The paper's headline comparative claims (2× better at ε=1, 19% at ε=8) are evaluated solely on RMSE. The paper itself shows (Figure 4b–c) that with adaptive optimizers—which are standard in practice—RMSE is *not* a reliable predictor of learning performance, and strategies with higher RMSE can achieve better cross-entropy. The Limitations section acknowledges this, and Section 4.3 validates RMSE as a proxy for non-adaptive optimizers. Nevertheless, the practical settings where RMSE advantages are claimed most loudly (large models, many iterations) are precisely where adaptive optimizers like Adam are standard. The paper would benefit from either (a) learning experiments confirming the RMSE advantage translates for the specific comparison in Figure 1b, or (b) clearer scope boundaries in the claims.

3. **Buffered Toeplitz comparison lacks stated configuration details.** Figure 1b compares Unamplified BandMF to Buffered Toeplitz and reports ~5% lower RMSE, but the buffer size used for Buffered Toeplitz is not stated. The related work mentions c≈3 as typical (line 306), but the actual experimental parameters are absent. Since Buffered Toeplitz's memory footprint (c·d) and RMSE both depend on the buffer size, the reader cannot assess whether the comparison is on equal resource footing or evaluate the RMSE-vs-memory trade-off. A Pareto plot of RMSE vs. per-iteration memory would be more informative.

4. **Rule of thumb for optimal bands rests on thin evidence.** The paper proposes b_* ≈ ε√n/k based on two plots (n=16384, Figure 3a; n=4096, Figure 3b). The paper frames this as a "good rule of thumb" and "roughly linear," which is appropriately cautious, but the evidence base is narrow. Varying n over a wider range or testing different δ values would strengthen the observation.

5. **Distributed noise generation communication pattern could be clarified.** The paper states "no communication is needed between machines until the noise is added to the clipped + aggregated gradient" (line 171). It is implicit that this assumes data-parallel training with sharded parameters (each machine updates its own parameter shard), but the paper does not state the assumed parallelism strategy. Clarifying this would help readers assess the communication cost.

### Trivial

6. **Proposition 1 (Noise Calibration)** cites prior work but would benefit from a brief intuition connecting ‖C‖₁,₂ ≤ 1 to the privacy guarantee, as this proposition is central to the whole approach.

7. **Column normalization of Toeplitz strategies** is recommended as post-processing, but the paper does not explain how to compute the effect of this step on the objective value, nor report RMSE before vs. after normalization. The evaluation is internally consistent (all strategies column-normalized), so this is a presentation gap rather than a flaw.

8. **Noise generation time experiment** (Figure 4a) would be more informative if it reported absolute time per iteration relative to total step time, and across multiple batch sizes.

## Nice-to-Haves

- A microbenchmark demonstrating distributed noise generation at a larger scale (e.g., a synthetic 1B-parameter workload) would strengthen the scalability claim without requiring full training.
- A learning experiment directly comparing BandMF (amplified and unamplified) with Buffered Toeplitz under a controlled privacy budget would make the state-of-the-art claim more persuasive.
- A simple table reporting wall-clock time and peak memory for the strategy optimization step itself (which is an offline cost) for representative n values would complete the scalability picture.

## Removed Points

- **Criticism about the paper not discussing initialization or convergence of non-convex optimization:** The paper notes the problem is non-convex w.r.t. C (line 101), cites prior work, and reports that L-BFGS converges to the same solution as the convex reformulation (Figure 1a). This is standard practice in the matrix mechanism literature. The criticism is speculative and does not point to an actual failure mode observed in the paper's experiments.

- **Criticism that "the paper does not mention the potential for suboptimal convergence of the non-convex optimization (Section 3.1) for large n":** The paper already demonstrates empirically (Figure 1a) that the implicit method converges to the same solution as prior work for all settings where the latter ran, including n up to ~10⁵. The Toeplitz variant's optimization is convex (linear system solve). No evidence of convergence issues is presented or suggested.

- **The harsh critic's demand that the paper should report the number of bands used for the Toeplitz baseline in the experiment and that the "unfair comparison" criticism is severe:** The missing buffer size is a reporting gap (kept in Minor), but the framing as a fatal flaw is disproportionate—the comparison is RMSE-based, and the paper's contribution includes a mechanism for handling larger memory footprints. The critic's framing that the advantage "may be an artifact of unequal resource allocation" overstates the problem; a Pareto plot would be better but the comparison is not invalid.

- **The remark that "learning experiments with the best Buffered Toeplitz setup" are needed:** This is a reasonable suggestion but belongs in Nice-to-Haves, not as a core weakness, since the paper's primary claim is about RMSE and scalability, not end-to-end learning superiority.

- **Strength Finder's claim that the paper provides "rigorous analysis of optimal bands":** The analysis is based on two configurations (n=16384, n=4096). This is not rigorous in the statistical sense. The strength is retained in spirit as a practical guideline, but "rigorous" is dropped.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no oversight that changes the interpretation of the paper's results. The most useful observation—that the RMSE-learning gap is more pronounced for adaptive optimizers—is already present in the paper itself.

## Suggestions

1. Replace the abstract's "enabling it to effectively handle settings with... 10⁹ model parameters" with a more precise claim (e.g., "our distributed noise generation analysis shows the mechanism can scale to models with over 10⁹ parameters under typical distributed training configurations") unless experimental evidence at that scale is added.

2. State the buffer size used for Buffered Toeplitz in the Figure 1b experimental setup, and consider adding a supplementary Pareto plot of RMSE vs. per-iteration memory across methods.

3. Add a brief sentence clarifying the parallelism assumption in Section 3.3: "In standard data-parallel training with sharded parameters (e.g., FSDP), each machine updates only its parameter shard and can add its noise shard locally without communication."

4. Add a short table reporting strategy optimization runtime and peak memory for representative n values (e.g., n=10⁴, 10⁵, 10⁶) to complete the scalability narrative.

## Score and Decision

The paper makes a genuine technical contribution: the complexity reductions for strategy optimization are well-derived and validated, and the distributed noise generation idea is clean and practically motivated. The experiments convincingly show that the scalable strategies reach the same RMSE as prior work while extending n by orders of magnitude. The main weakness is a gap between the stated claim of handling 10⁹ parameters and the actual experimental evidence (100M parameters). This is addressable without structural changes. The RMSE-learning proxy is acknowledged and partially investigated. I assess this as a solid paper with a clear contribution that should be accepted.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>