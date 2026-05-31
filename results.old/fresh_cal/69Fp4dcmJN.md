Now I have all the information I need. Let me write the final consolidated review.

---

## Summary

This paper presents techniques to scale the Banded Matrix Factorization (BandMF) mechanism for differentially private ML training. It addresses two key bottlenecks: (1) strategy optimization, which previously required O(n³) time and O(n²) memory, is reduced to O(n²·b) time and O(n·b) memory via implicit computation (general banded) or O(n·b) time and O(n) memory (banded Toeplitz); (2) the b·d training-time memory overhead is mitigated through a distributed noise generation scheme that shards the correlated-noise state across machines. The resulting scalable BandMF achieves lower expected error (RMSE on the prefix workload) than competing scalable mechanisms (DPSGD, Tree Aggregation, Stamping, FHU, Buffered Toeplitz) across a range of privacy budgets.

## Strengths

1. **Efficient strategy optimization that demonstrably extends the reach of BandMF.** Section 3.1 (Algorithm 3) and Section 3.2 (Proposition 2) provide clean, mathematically sound reductions in the complexity of strategy optimization. Figure 1a validates that the implicit optimization matches prior work (Choquette-Choo et al., 2024) where that prior work can run, and that Toeplitz strategies are within 0–2% suboptimal (≤0.25% for the regime of most interest). This is the paper's strongest evidence: it shows the core algorithmic contribution works as advertised.

2. **Distributed noise generation with documented training-time overhead.** Section 3.3 proposes a straightforward sharding scheme for the b×d noise-generation state. Figure 3a (noise generation time) provides concrete wall-clock measurements on a 100M-parameter BertBase model with 32 TPU v3 cores, showing correlated noise generation is 1–3 orders of magnitude cheaper than per-example gradient clipping even with b=128 bands. This addresses a practical concern that could otherwise prevent adoption.

3. **Consistent RMSE advantage over scalable baselines.** Figure 1b compares Amplified BandMF against DPSGD, Tree Aggregation, Stamping, FHU, and Buffered Toeplitz across ε ∈ [0.5, 8] (n=16384, k=8). Amplified BandMF achieves the lowest RMSE in every setting, with roughly 2× improvement over DPSGD at ε=1 and still 19% better than the best competitor at ε=8. The comparison is fair: it includes both amplified (DPSGD) and non-amplified (Buffered Toeplitz, etc.) baselines, and the paper distinguishes between Amplified and Unamplified BandMF.

4. **Honest characterization of the RMSE-to-learning-performance relationship.** Section 4.3 (Figures 3b–3c) directly studies the gap between RMSE and evaluation cross-entropy. The finding that adaptive optimizers cause fewer-band strategies to outperform higher-band strategies at the same RMSE is useful guidance for practitioners and reflects good scientific practice.

## Weaknesses

### Fatal
None.

### Major
1. **The headline claim of "state-of-the-art performance" rests on RMSE, and the paper's own evidence shows RMSE is an imperfect proxy for training utility when band counts differ.** The paper states in the Conclusion that it offers "better expected error than any other DPMF-family-style mechanism across a wide variety of settings" and claims in Section 4.1 that "Amplified BandMF is better than all other mechanism across all settings evaluated." Both statements are anchored to RMSE on the prefix workload. However, Section 4.3 demonstrates that for adaptive optimizers, RMSE is not a consistent predictor of learning performance across strategies with different numbers of bands — strategies with fewer bands achieve strictly better cross-entropy at fixed RMSE. Since the comparison in Figure 1b includes mechanisms with different effective band counts (e.g., DPSGD with b=1 vs. Amplified BandMF with some b>1), it is not clear whether the RMSE advantages translate proportionally into training utility. The Limitation section (Section 6) acknowledges this proxy issue, but the paper continues to treat RMSE as the primary performance metric without bridging the gap. An end-to-end comparison of top-1 accuracy or evaluation loss at fixed (ε, δ) across mechanisms would substantiate (or refute) the practical significance of the reported RMSE gains.

2. **No wall-clock or memory measurements for strategy optimization at the largest claimed scales.** The paper states that Toeplitz optimization scales to n > 10⁶ and that implicit optimization scales to n > 10⁵, but the only runtime data reported is for noise generation during training (Figure 3a). Strategy optimization is done "on an NVIDIA V100 Tensor Core GPU for up to 10K iterations" (Section 4), but no actual wall-clock times, peak memory usage, or iteration counts are reported for the large-n regime. A practitioner considering n = 10⁶ needs to know whether optimization takes minutes, hours, or days. This is a concrete data gap for the paper's central scalability claim.

### Minor
3. **The learning-performance validation is done at a scale far below the paper's motivating regime.** Section 4.3 uses a 4M-parameter BertTiny model trained on StackOverflow, while the paper's Introduction motivates the work with "billions of parameters trained for hundreds of thousands of iterations." The distributed noise generation experiment uses a 100M-parameter BertBase model. While the algorithmic arguments for scaling are sound (the approach is embarrassingly parallel), the empirical evidence stops an order of magnitude short of the claimed regime. Showing the noise generation overhead at 1B+ scale (even with a microbenchmark or simulation) would strengthen the paper substantially.

4. **The rule of thumb b* ≈ ε√n/k is presented without direct validation.** Section 4.2 introduces this heuristic as "a good rule of thumb" for near-optimal band selection, but no scatter plot, table, or quantitative comparison against brute-force optimal bands is provided. Given that the paper frames this as practical guidance, validation against the optimization results would increase confidence.

### Trivial
None.

## Nice-to-Haves

- **Strategy optimization wall-clock times:** A small table or figure reporting optimization time vs. n (e.g., for n = 10³, 10⁴, 10⁵, 10⁶) would directly address the main data gap.
- **BT comparison caveat:** The paper already notes (line 306) that BT is a good alternative in federated settings — this could be surfaced more prominently in the main text rather than deferred to Related Work.

## Removed Points

These points from the reviewer inputs were removed with justification:

- **"Comparison against BT is unfair because BT uses less memory and doesn't need distributed noise generation"** — The paper clearly compares *Unamplified* BandMF against BT (both non-amplified), and acknowledges in the text (line 306 and Section 6) that BT is preferable in federated/single-machine settings. The claim about "all settings evaluated" refers to the specific experimental setup (centralized, multi-machine), not literally every conceivable setting. The paper does not claim dominance in all possible deployment scenarios.
- **"No error bars/confidence intervals in Figure 1b"** — RMSE computations from Proposition 1 are deterministic given (C, ε, δ, n, k); error bars are not applicable.
- **"Missing citation for the claim that prior BandMF is limited to n≈10⁴"** — This follows directly from the O(n³) time / O(n²) space complexity analysis stated in Section 2 (line 101), not from an external empirical claim.
- **"Distributed noise generation requires agreement on random seed"** — This is a standard implementation detail common to all distributed RNG; not a weakness of the paper.
- **"Missing end-to-end training comparison across all mechanisms at fixed privacy budget"** — The paper's contribution is about scaling BandMF and evaluating its RMSE; the paper explicitly scopes out full end-to-end mechanism comparison (Section 4.3, line 284: "Our goal is not to compare different mechanisms across different privacy budgets"). The paper includes learning-performance experiments but for a different purpose (studying the RMSE proxy). This is a reasonable scope choice.
- **"Missing discussion about how the Toeplitz approach differs from Henzinger et al."** — The paper discusses this in Related Work (Section 5, line 300), noting that prior Toeplitz approaches use full (non-banded) Toeplitz matrices and do not address the training-time memory overhead.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the same trade-offs the paper itself acknowledges (RMSE proxy limitation, need for distributed noise generation).

## Suggestions

1. Report wall-clock time and peak GPU memory for strategy optimization at n = 10³, 10⁴, 10⁵, 10⁶ (general banded and Toeplitz variants) in a single table or figure.
2. Validate the rule of thumb b* ≈ ε√n/k by plotting predicted vs. brute-force optimal bands across a sweep of (ε, k, n) values.
3. Add a brief end-to-end experiment comparing training loss/accuracy at a fixed (ε, δ) between DPSGD, Unamplified BandMF, Amplified BandMF, and Buffered Toeplitz on a moderately sized model (e.g., GPT-2 124M) to bridge the RMSE-to-utility gap for at least one setting.

## Score and Decision

This paper presents well-motivated algorithmic contributions with clean complexity analysis and solid RMSE-based evaluation. The scaling techniques are real and address a genuine practical bottleneck. The main weaknesses — the RMSE proxy gap and missing runtime data at the largest scales — are addressable and do not invalidate the core contributions. The paper honestly acknowledges its own limitations, which strengthens its credibility.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>