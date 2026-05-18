Now I have a thorough understanding of the paper and all reviewer claims. Let me construct the final review.

## Summary

SeedLM is a novel post-training weight compression method that encodes each block of LLM weights as a seed for a Linear Feedback Shift Register (LFSR) pseudo-random generator plus a small set of quantized linear coefficients. During inference, weights are reconstructed on-the-fly from the stored seed and coefficients using lightweight LFSR hardware, trading increased compute for reduced memory access. The method is entirely data-free and achieves strong results: on Llama 3 70B at 4-bit, SeedLM retains ~98% of FP16 accuracy (78.06 vs. 79.51 baseline), significantly outperforming AWQ (72.34). An FPGA prototype demonstrates near-4× speedup on matrix-vector multiply.

## Strengths

1. **Novel and well-motivated compression paradigm.** The idea of encoding weight blocks into LFSR seeds and reconstructing them via pseudo-random projections at inference time is genuinely novel. The hardware motivation — trading cheap compute cycles for expensive DRAM accesses — is sound and directly addresses a real bottleneck in LLM inference (memory-bound autoregressive generation). The paper is the first to demonstrate this approach in practice.

2. **Strong empirical results on the model that matters most for the claimed advantage.** On Llama 3 70B — explicitly noted as "particularly challenging to compress" — SeedLM at 4-bit achieves a mean zero-shot accuracy of 78.06 vs. AWQ's 72.34 (Table 2), a nearly 6-point improvement, all without any calibration data. At 3-bit on the same model, SeedLM (74.68) massively outperforms AWQ (61.35). These results directly support the paper's central claim that data-free compression can beat calibration-based methods on hard-to-compress models.

3. **FPGA implementation validates the hardware thesis.** The prototype achieves a measured 3.98× speedup on a 2048×2048 matrix-vector multiply (34,331 cycles vs. 136,559 for FP16, Table 5). The resource overhead (128 DSPs, added LUTs/FFs) is well within a Virtex7-class device (Table 4). This is the first actual hardware demonstration of LFSR-based weight reconstruction for LLM inference and confirms that the memory-bandwidth savings materialize in practice despite the decompression overhead.

4. **Principled design-space exploration tied to bit budgets.** Section 3.4 derives the exact bit-per-element formula \( M = (K+4+4P)/C \) and solves the constrained optimization numerically via grid search over block size \(C\), latent dimension \(P\), and LFSR length \(K\). This provides a reproducible rationale for hyperparameter selection rather than ad-hoc tuning.

5. **Consistently strong perplexity results.** In Table 1 (WikiText-2), SeedLM achieves the best perplexity among all 4-bit methods across nearly every model, including Llama 2 7B (5.7 vs. AWQ 5.8, OmniQuant 6.1), Llama 2 70B (3.5, tying AWQ and beating OmniQuant 3.7), and Llama 3 70B (3.8 vs. AWQ 4.7, OmniQuant inf). At 3-bit, SeedLM often dominates by wide margins. This consistency across a different metric (perplexity) strengthens confidence.

## Weaknesses

### Fatal
None.

### Major

1. **Compression cost is not reported or acknowledged as a limitation, and is plausibly very large.** The algorithm enumerates all \(2^K-1 = 65{,}535\) seeds per weight block. For each seed, a \(P \times C\) matrix-vector multiply (\(\mathbf{t}_j = \mathbf{U}(s_j)^\dagger \mathbf{w}\)) is performed. For a 70B model with block size \(C=8\), there are ~8.75 billion blocks, yielding ~\(5.7 \times 10^{14}\) such operations. While the pseudo-inverse precomputation (once per seed, ~6.3 MB) and block-level parallelism help, the total compute is immense. The paper states "to enhance computational efficiency, we precompute and cache the pseudo-inverse matrices … and perform steps 2–5 in parallel across all blocks" but never quantifies the wall-clock compression time or resource requirements for any model size. This is an offline/one-time cost, so it does not invalidate the method — but for a paper proposing a practical compression method, omitting this information makes it impossible to assess practical feasibility. A 70B model could take thousands of GPU-hours to compress, which would be a significant practical barrier even if one-time. **The authors should report compression time for at least one model size and discuss any heuristics (e.g., seed sampling, early stopping) that could reduce cost.**

2. **The OmniQuant comparison is suspect and undermines the "state-of-the-art" claim.** The paper states: "For QuIP# and OmniQuant, we ensure a fair comparison with SeedLM and AWQ by not performing fine-tuning on the quantized models." OmniQuant's core method *is* learning weight clipping/transformation parameters via gradient descent on calibration data — disabling what the paper calls "fine-tuning" may strip OmniQuant of its essential mechanism. The results are catastrophically bad on Llama 3 70B (OmniQuant 4-bit mean: 33.45 vs. baseline 79.51), suggesting a misconfiguration or that the method was run without its core learning step. The paper does not specify exactly which components of OmniQuant were disabled or cite a specific configuration from the OmniQuant repository. Because the "outperforms state-of-the-art" narrative relies heavily on these OmniQuant numbers, this needs clarification. **That said** — even setting OmniQuant entirely aside, SeedLM still convincingly beats AWQ on Llama 3 70B (78.06 vs. 72.34 at 4-bit), so the paper's core contribution does not collapse. But the OmniQuant comparison as presented is not credible and should be corrected or removed.

### Minor

3. **Hyperparameter selection is validated only on Gaussian synthetic data, not on real model weights.** The design-space exploration in Section 3.4 minimizes reconstruction error for a standard normal random vector \(\mathbf{w}\), then fixes the resulting \((C, P, K)\) for all LLM experiments. The paper acknowledges the limitation ("while assuming a Gaussian distribution may have its limitations") but claims it "has proven effective within our design space and aligns well with real-world benchmarks" without providing supporting evidence — no ablation varying \(C, P, K\) on actual model weights, and no comparison with alternative configurations at the same bit budget. Real LLM weight distributions are far from i.i.d. Gaussian, so the optimal configuration on synthetic data may not be optimal in practice. A simple ablation on a single model layer would have been straightforward and would substantially strengthen confidence in the hyperparameter choice.

4. **Accuracy improvements are model-dependent, but some claims overgeneralize.** The abstract states that "SeedLM achieves significantly better zero-shot accuracy retention at 4- and 3-bit than state-of-the-art techniques." This is strongly supported on Llama 3 70B but not uniformly true: on Llama 2 70B at 4-bit, SeedLM (75.90) is slightly *worse* than AWQ (76.27); at 3-bit it is essentially tied (73.83 vs. 73.91). The body text (line 390) more fairly says "performs on par with or better than state-of-the-art methods." The paper would benefit from explicitly acknowledging that SeedLM's largest advantage appears on models that are hard to compress (like Llama 3), while it is competitive but not uniformly superior on others (like Llama 2). The current framing risks overselling.

5. **No comparison against a simple data-free baseline (e.g., round-to-nearest quantization).** Since SeedLM's unique selling point is being data-free, comparing against RTN (the trivial data-free baseline) at the same bit widths would directly quantify the benefit of the LFSR-based approach over naive compression. The paper only compares against calibration-data methods, which shows that SeedLM is competitive with (and often beats) methods that use *more* information — a strong result — but it does not isolate how much of the gain comes from the LFSR mechanism vs. simply being a well-tuned compression scheme. An RTN row in Tables 1 and 2 would contextualize the contribution and would require no additional data.

6. **Sensitivity of results to LFSR length \(K\) is not explored.** The paper fixes \(K=16\) for both 3-bit and 4-bit configurations. Since increasing \(K\) grows the seed-search space exponentially (\(\log_2\) scale) while consuming bits from the budget, a sweep over \(K\) for a fixed bit budget would clarify whether the chosen \(K\) is near-optimal or if the configuration is robust to this choice.

### Trivial

7. **No discussion of the degeneracy problem beyond excluding the all-zero state.** The paper correctly excludes the all-zero LFSR state. But some seeds could produce nearly linearly dependent columns in \(\mathbf{U}(s)\), inflating reconstruction error. The paper does not examine whether this occurs in practice or whether it matters given the exhaustive search over all seeds (which naturally avoids bad seeds via the minimization).

## Nice-to-Haves

- An RTN baseline row in Tables 1 and 2 would cleanly quantify the advantage of the LFSR+coefficient approach over the simplest data-free alternative.
- An ablation on a single model layer comparing reconstruction error for several \((C, P, K)\) combinations at the same bit budget would replace the Gaussian-proxy argument with direct evidence.
- Reporting compression time for one model (e.g., Llama 2 7B) with the current exhaustive algorithm, potentially with a note on how it scales to 70B, would address the main feasibility concern.

## Removed Points

- **"FPGA speedup ~4× is expected from first principles"** — Removed. While the theoretical limit is indeed 4× from 16-bit to 4-bit, the practical achievement requires handling LFSR decompression, fixed-to-float conversion, and pipelining without stalling. The fact that the prototype achieves 3.98× is a non-trivial validation that the overhead does not eat into the theoretical gain. The reviewer's framing undersells this contribution.
- **Strength Finder's claim of "consistent superiority over calibration-based methods at 3-bit"** — Downgraded from a strength to a more nuanced statement. On Llama 2 70B at 3-bit, SeedLM (73.83) is slightly below AWQ (73.91). The raw numbers support competitiveness, not universal superiority.
- **OmniQuant criticism re: "the paper's claim relies heavily on these OmniQuant numbers" (overstated version)** — Kept the substantive concern but removed the overstatement. SeedLM still beats AWQ on Llama 3 70B by a large margin regardless of OmniQuant's status, so the paper does not depend solely on OmniQuant.

## Novel Insights

The reviews reveal an interesting tension: the paper's data-free approach outperforms calibration-based methods precisely on the model (Llama 3 70B) where one would expect calibration data to be most helpful — because the model's training distribution is richer and harder to compress. This suggests a counterintuitive trade-off: methods that learn fixed quantization grids from calibration data may overfit to the calibration distribution and perform poorly when the weight distribution itself (not the activation distribution) is the limiting factor. SeedLM's exhaustive search over many random projections finds good reconstruction subspaces without assuming any particular weight structure, which may give it an advantage precisely when weights are "hard" (high-entropy, as in Llama 3). Conversely, on models where weight distributions are more compressible (Llama 2), the advantage of exhaustive search is smaller, and simpler methods like AWQ match it. This insight — that data-free exhaustive-subspace search and data-driven quantization may have complementary strengths depending on model hardness — is worth exploring explicitly in future work.

## Suggestions

1. Report the wall-clock compression time for at least one model (e.g., Llama 2 7B) on the hardware used. If the cost is high, discuss practical heuristics: random seed subsampling, early stopping when reconstruction error drops below a threshold, or warm-starting from adjacent blocks' seeds.
2. Clarify the OmniQuant configuration: specify which components were disabled, cite the exact version/commit used, or reproduce results consistent with published OmniQuant numbers. If the numbers are unreproducible, remove OmniQuant from the comparison.
3. Add an ablation on real model weights (at least one layer each from Llama 2 7B and Llama 3 8B) showing reconstruction error for multiple \((C, P, K)\) combinations at the same bit budget, to validate the Gaussian-based hyperparameter selection.
4. Add an RTN (round-to-nearest) row to the accuracy and perplexity tables. This requires no data and cleanly quantifies the benefit of the LFSR+coefficient approach over naive compression.
5. Tone down the "significantly better" language for Llama 2 models where SeedLM is competitive but not uniformly superior. The abstract can focus on the Llama 3 70B result (where the advantage is clear), and the body can explicitly note model-dependent behavior.

## Score and Decision

This is a solid paper with a genuinely novel idea, strong results on the flagship model, and a real hardware demonstration. The main issues (missing compression cost, questionable OmniQuant comparison, hyperparameter validation on synthetic data only) are fixable and do not threaten the core contribution. The paper would benefit from addressing these before acceptance.

**MY FINAL SCORE: <pineapple>6.5</pineapple>**
**MY FINAL DECISION: <orange>Accept</orange>**