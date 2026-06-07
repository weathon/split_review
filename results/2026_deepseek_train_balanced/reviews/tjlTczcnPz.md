Now I have all the information needed. Here is my consolidated final review.

---

## Summary

This paper proposes SliM-LLM, a structured mixed-precision post-training quantization (PTQ) framework for LLMs at ultra-low bit-widths (2–3 bits). It introduces two techniques: Salience-Determined Bit Allocation (SBA), which assigns bit-widths to weight groups based on Hessian-derived salience, and Salience-Weighted Quantizer Calibration (SQC), which adjusts the quantizer to better preserve locally salient weights within each group. SliM-LLM integrates as a plug-in into existing PTQ pipelines (GPTQ and OmniQuant) and demonstrates consistent perplexity improvements across LLaMA-1/2/3 model families.

## Strengths

1. **Consistent and large perplexity improvements across many model scales at 2-bit**: Table 1 shows SliM-LLM reduces GPTQ's perplexity on LLaMA-13B from 20.44 to 8.87 (~57% improvement) and on LLaMA-7B from 152.31 to 14.58 (~90% improvement). These gains hold across LLaMA-1 (7B–65B), LLaMA-2 (7B–70B), and LLaMA-3 (8B, 70B) — a broader evaluation across model sizes than many PTQ papers provide.

2. **Theoretical motivation connecting activation outliers to structured salience clustering**: Theorem 1 provides a formal derivation showing how outlier activations propagate through the Hessian to make entire weight columns salient, and ties this to known results about regional clustering of outlier tokens. This gives a principled reason why *structured* (group-wise) mixed-precision is viable, distinguishing the work from purely empirical approaches.

3. **Plug-and-play integration demonstrated on two distinct quantization backbones**: SliM-LLM (with GPTQ's statistic quantizer) and SliM-LLM⁺ (with OmniQuant's learnable quantizer) both outperform their respective backbones (Tables 1 and 2, e.g., 3-bit LLaMA-7B: SliM-LLM⁺ 6.07 vs OmniQuant 6.15 vs AffineQuant 6.14). This cross-framework generality is a distinctive advantage over methods tied to a single quantizer design.

4. **Ablation isolates the benefit of salience-guided allocation over naive mixed-precision**: Fig. 4 compares SBA against random and head-tail (spatial-order) allocation under identical average bit-width. Both naive strategies fail to improve or degrade performance, while SBA consistently reduces perplexity — directly validating that the *salience-determined* aspect of the allocation drives the gains.

5. **Memory-efficiency verified with concrete measurements**: Table 3 confirms that SliM-LLM 2-bit uses ~2.3G weight memory for LLaMA-7B (vs 12.6G FP16), a ~5.5× reduction, with nearly identical memory to uniform GPTQ (2.2G).

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparison against SpQR, a directly relevant mixed-precision PTQ baseline**: The paper cites SpQR in related work (line 56) as a "finer-grained partitioning for grouped quantization with unstructured mixed-precision" method that uses a similar Hessian-based salience concept, but does not include it in any experiment. SpQR is a *post-training* quantization method (not QAT/re-training, which the paper scopes out at line 247), making it directly comparable. The paper's claim of "outperforming other unstructured mixed-precision PTQ methods" (line 42) is weakened without this comparison. (The exclusion of QuIP# and AQLM is more defensible as they involve fine-tuning/re-training, which the paper explicitly scopes out.)

2. **Throughput degradation at 2-bit is significantly understated**: Table 3 shows SliM-LLM at 2-bit is 20–27% slower than GPTQ (e.g., LLaMA-7B: 83.9→61.2 tok/s, LLaMA-13B: 92.6→73.7 tok/s, LLaMA2-7B: 83.6→64.4 tok/s). The paper describes this as "only with a slight decrease in inference speed" (line 385). A 20–27% reduction is not slight and should be honestly characterized. While the paper's claim of "no additional bits and computation overhead" (line 39) is made *relative to unstructured methods* (not GPTQ), the overall efficiency framing in the abstract and introduction gives an unduly optimistic picture. The throughput comparison against GPTQ — the only speed data presented — shows a real cost of mixed-precision alignment that the paper minimizes. The paper should provide throughput comparisons against unstructured methods (SpQR, PB-LLM) to substantiate the claimed efficiency advantage, and transparently discuss the root cause.

### Minor

1. **C4 perplexity and OPT model results are mentioned in the evaluation scope but absent from main tables**: Line 246 states experiments are conducted on "WikiText2 and C4 datasets" across "OPT, LLaMA, LLaMA-2 and LLaMA-3" models. However, the main results tables report only WikiText2 perplexity for LLaMA-family models. No C4 perplexity or OPT perplexity appears in the main body. If these exist in the appendix (which the parser strips), the main text should reference them; if not, the evaluation scope exceeds what is reported.

2. **Abstract's "48% decrease of perplexity" claim is imprecise**: The baseline method and model configuration corresponding to this figure are not specified. Given that SliM-LLM's improvement over GPTQ on LLaMA-7B at 2-bit is ~90%, the 48% figure appears to refer to a different baseline — but the reader cannot determine which. This should be explicitly stated.

3. **SBA's mathematical formalism (Eq. 4) is disproportionate to its actual procedure**: The paper presents SBA as an argmin over group assignments with set constraints (Eq. 4), but the implementation (lines 120–131) is a single-parameter grid search over T (number of groups to upgrade/downgrade) with ~16 iterations. The formal presentation creates the impression of a combinatorial optimization. The method is effective, but the presentation should match the actual procedure.

4. **SQC's 3-σ masking rule lacks sensitivity analysis**: The paper applies a 3-σ threshold to identify salient weights (1–5% of weights per group) and sets λ=0.1, n=50 for the γ search (line 154) without any ablation or sensitivity study. A brief analysis of how performance varies with these choices would add rigor.

### Trivial
None.

## Nice-to-Haves

- Compare against simpler allocation heuristics (e.g., weight-magnitude or activation-magnitude based) in the ablation to further isolate the value of Hessian-based salience computation over cheaper alternatives.
- Report calibration cost (total GPU time or GPU-hours) for quantizing models of different sizes, which is standard practice in PTQ papers.
- Explain the minor memory increase observed at 2-bit (e.g., 2.3G vs 2.2G for LLaMA-7B, Table 3) — likely due to alignment padding for mixed-precision groups.
- Provide a brief sensitivity study for the γ search range and the 3-σ threshold in SQC.

## Removed Points

These points were removed after cross-checking against the paper; treat them with caution:

- **Missing QuIP#/AQLM comparisons**: These methods involve fine-tuning/re-training, which the paper scopes out (line 247). The criticism was over-broad and only SpQR is a pure PTQ method without fine-tuning.
- **Salience definition attribution**: The paper explicitly credits SparseGPT (line 88: "we follow the SparseGPT to define"). This is not a weakness.
- **Theorem 1 as "essentially formalizing what SparseGPT already captures"**: Subjective opinion, not a verifiable flaw. The theorem connects existing salience to spatial clustering, which is the paper's insight.
- **Various speculative criticisms**: Comments about "what if the metric measures a proxy" or "if the normalization were X" are not anchored in specific paper content and were removed per filtering guidelines.
- **Formatting/style nitpicks**: These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add SpQR as a baseline in the main perplexity tables to substantiate the claim of outperforming unstructured mixed-precision PTQ methods.
2. Include a throughput comparison against unstructured methods (SpQR, PB-LLM) rather than only against uniform GPTQ, so readers can evaluate the structured-vs-unstructured efficiency trade-off honestly.
3. Add C4 perplexity results (or reference existing appendix tables) and OPT results to match the evaluation scope claimed in Section 4.
4. Clarify the abstract's "48% decrease" by specifying the baseline method and model.
5. Provide a sensitivity analysis for the 3-σ masking rule and γ hyperparameters in SQC.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>