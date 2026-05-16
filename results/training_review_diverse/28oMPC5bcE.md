Now I have thorough verification. Let me compose the final consolidated review.

## Summary

UNComp proposes using matrix entropy (effective rank) to measure "uncertainty" across layers and heads in LLMs, then uses this signal to adaptively compress both hidden states (during prefilling) and the KV cache (during decoding) without training. The method groups layers and heads by their effective rank, assigning different token budgets per group. On LongBench, UNComp outperforms prior eviction and head-pruning methods (H2O, SnapKV, PyramidKV, CHAI) at the same compression rate, achieves up to 1.58× prefilling speedup, 6.4× throughput gain, and on the needle-in-a-haystack task for Llama2-4k it matches/exceeds the full-size KV cache at 9.38% of its original size.

## Strengths

1. **First work to compress hidden states during prefilling for speedup** (not just KV cache after generation). The paper explicitly identifies this gap in prior work (Section 2.1) and demonstrates a clear prefilling speedup (Table 3: 48.78s vs 77.34s for FullKV on A100). This is a substantive, concrete advancement over the existing literature.

2. **Training-free adaptive grouping consistently outperforms trained head-pruning (CHAI) and all eviction baselines.** On Llama2-13B with 9.38% KV size, UNComp achieves 33.42 average score versus CHAI's 30.37 (Table 1). The advantage holds across all four model families tested (Llama2-7B, Llama2-13B, Llama3-8B, Mistral-7B), showing the entropy-based grouping is robust.

3. **Strong performance under extreme compression.** With only 12 tokens retained per low-entropy head, UNComp scores 26.08 on six LongBench tasks versus PyramidKV's 22.06 (Table 2), and even deleting 2 full heads per layer incurs only a 1.58-point drop from FullKV. This validates that effective-rank-based head importance ranking captures genuine structure.

4. **Empirical analysis of entropy trends motivates design choices.** The paper systematically investigates which matrix (Q/K/V) best captures compression patterns (Figure 2), shows eigenvalue distributions vary across heads but are stable across datasets (Figure 3), and validates H/R ratio selection via Pearson correlation (Figure 6). Each step of the method has empirical grounding.

5. **Meaningful throughput improvement without catastrophic accuracy loss.** At 4.74% KV size on Llama3-8B, UNComp increases throughput 6.4× (batch size 32 vs 6) over FullKV while losing only 1.41% average accuracy — a practical trade-off for deployment scenarios.

## Weaknesses

### Fatal
None.

### Major

1. **Method is significantly underspecified, hindering reproducibility.** Several critical parameters and procedures are not disclosed: the threshold ε in Eq. (3) for determining compression stages C; the values of S_max and S_min that initialize token budgets (beyond the specific 512/256 values in the main experiment); the number of head groups m (which apparently varies across experiments without explanation); the step size Δs_h for inter-head compression; the concrete algorithm for selecting the "elbow point" for truncated entropy (only mentioned by name with a citation); the sample size from Wikitext2 used during the preparation stage; and how the H/R ratio is deterministically selected from the correlation analysis. Without these details, the method cannot be independently reproduced, and it is unclear how much performance depends on specific parameter choices versus the core idea.

2. **No statistical significance or variance reported anywhere.** The paper's sole mention of repeated experiments is one sentence: "confirmed by averaging multiple repeated experiments." No error bars, confidence intervals, or run-by-run statistics appear. Given the small margins between methods in Table 1 (e.g., 31.98 vs 31.81 vs 31.94 on Llama2-7B), it is impossible to assess whether the reported advantages are meaningful or within noise. This is a significant gap for an empirical systems paper.

3. **Justification for the different compression direction between layers and heads is underdeveloped.** The paper maps higher effective rank to *more* compression for layers (tokens share information across layers) but *less* compression for heads (higher-entropy heads are more informative so keep more tokens). While this mapping is internally consistent given the paper's own definition of "compression rate" (compressed/original, per line 26), the justification that "tokens of the same head in different layers gradually share information... while tokens of different heads do not share information" is asserted without empirical or theoretical support. This is a conceptually interesting claim but needs substantiation — for example, an analysis of cross-layer versus cross-head token similarity. The paper's core thesis rests on the validity of this distinction.

4. **The abstract and needle-in-a-haystack claim are overstated relative to the evidence.** The abstract states "in needle-in-a-haystack tasks, UNComp outperforms the full-size KV cache" without qualification. Table 4 shows this holds for Llama2-4k (98.80 vs 98.70) but *not* for Llama3-8k (83.73 vs 84.99 for Ours-group-stage; 84.13 vs 84.99 for Ours-group). Similarly, the abstract presents "compressing the KV cache to 4.74% of its original size" as the method's headline achievement, but this is the Llama3-8B result only — the Llama2 models operate at 9.38% compression. These over-generalizations need to be scoped to specific model/compression configurations.

### Minor

5. **The link between matrix entropy of the covariance matrix and downstream task compressibility is asserted rather than established.** The paper defines matrix entropy on the token-sequence covariance matrix and calls it "uncertainty," but does not prove or convincingly argue why this measure should correlate with a head's compressibility for task performance. Some empirical validation (e.g., an ablation showing entropy-based grouping outperforms random grouping at the same budget) would strengthen the chain.

6. **No analysis of the computation overhead of the preparation stage.** Computing eigendecompositions of covariance matrices for every head and layer requires nontrivial computation even on a small calibration set. The time and memory cost of this stage is not reported, which is a practical concern for real-world deployment.

7. **H/R ratio selection may leak information from the evaluation set.** The Pearson correlation between compressed and full-erank trends (Figure 6) is measured on LongBench data — the same datasets used for the final evaluation. The paper should use a separate calibration set or clarify whether this step is truly performed on held-out data.

8. **No discussion of failure cases or limitations.** The Mistral-7B results show smaller margins over baselines compared to Llama models (Table 1). Which tasks does the method struggle on? The paper would benefit from acknowledging where the entropy-based compression assumption breaks down.

9. **Metric averaging across heterogeneous tasks.** The paper averages scores across 16 LongBench tasks that use fundamentally different metrics (F1, ROUGE-L, accuracy, specialized counts). While this is standard practice in LongBench papers, the paper does not acknowledge the limitation or provide any per-task breakdown beyond the dense table.

### Trivial
None that survive filtering (the table formatting complaints are standard for dense ML tables).

## Nice-to-Haves

- An ablation comparing entropy-guided grouping against uniform grouping at the same total token budget would directly validate the core thesis.
- A sensitivity analysis of the key free parameters (ε, S_max/S_min, m) would address the reproducibility concern while also illuminating which design choices matter most.
- Clarifying whether the preparation stage grouping is stable across different calibration samples would strengthen the "training-free" claim.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Inconsistent reasoning about matrix entropy and compression direction"** (Harsh Critic's first Critical Issue): After verifying against the paper, the reasoning is internally consistent. The paper defines "compression rate" as compressed/original (line 26). Both line 91 (the bold paragraph) and line 156 map higher erank to *more* compression for layers and *less* compression for heads — the same mapping. The reviewer appears to have misread "compression rate" in the opposite direction. However, the *justification* for this mapping is underdeveloped (retained as Major weakness #3 above).

- **"4.74% as a universal result"**: The reviewer claims the paper presents 4.74% as universal. The abstract does present it as the method's headline without model-specific qualification — this is retained as part of Major weakness #4 above (overclaimed needle/haystack + unqualified numbers), not as a separate point.

- **"No comparison to quantization-based methods"**: The paper explicitly scopes itself to eviction/merging and head pruning (Section 2.1, 2.2). Quantization is a different family of techniques. This is scope creep.

- **"Table 3 memory usage of H2O is lower than Ours-group-stage"**: The table shows H2O at 22908 MB vs Ours-group-stage at 22964 MB — a 56 MB difference (0.24%). The paper's claim about memory efficiency is about the overall method's advantage versus FullKV (25900 MB), not about beating H2O on this specific metric.

- **"Pure formatting/style nitpicks"** about table density, rotated headers, etc. These are aesthetic judgments about a dense but functional table.

## Novel Insights

The reviews surface a genuine tension not articulated by the paper itself: the core claim that matrix entropy provides a *coherent* signal for compression depends on a non-trivial assumption about information sharing across layers (redundancy) versus across heads (diversity). The paper's most interesting finding — that compressed models can *exceed* full-cache performance on retrieval tasks — suggests that entropy-based pruning acts as a denoising mechanism that removes low-information heads. This is a potentially deeper insight than the paper itself develops, and could motivate future work on information-theoretic analyses of attention head specialization.

## Suggestions

1. Fully specify all algorithm parameters (ε, S_max/S_min, m, Δs_h, elbow detection method, Wikitext2 sample size) either in the main text or a clearly marked appendix.
2. Add error bars or at minimum a per-task win-count analysis (sign test) to the main results.
3. Qualify the abstract's claims to specify which numbers apply to which model/compression configuration.
4. Add an ablation: entropy-guided grouping vs. uniform grouping at the same total token budget to directly validate the core premise.
5. Strengthen the justification for the layer-vs-head compression reversal with quantitative evidence (e.g., cross-layer vs. cross-head token similarity analysis).
6. Report the computation cost of the preparation stage (time and memory for eigendecompositions per head/layer).
7. Use a held-out calibration set for H/R ratio selection to avoid information leakage concerns.

## Score and Decision

The paper presents a genuinely novel idea (matrix entropy for adaptive compression) with a demonstrated practical advantage (hidden state compression during prefilling). The empirical results are strong: UNComp consistently outperforms competitive baselines across four model families. However, the method is significantly underspecified, no variance is reported, and the central claim about the direction of compression is insufficiently justified. These are real but addressable weaknesses — the core contribution is solid.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>