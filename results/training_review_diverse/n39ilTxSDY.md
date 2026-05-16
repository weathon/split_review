Now I have all the information needed. Let me produce the consolidated review.

## Summary

Ditto presents a framework for quantization-aware secure Transformer inference over MPC, combining static dyadic quantization, novel upcast/downcast type-conversion primitives for converting shares between rings (ℤ₂³² ↔ ℤ₂⁶⁴), and compiler-level dynamic ring dispatch. The paper reports speedups of 1.44–2.35× over PUMA and 3.14–4.40× over MPCFormer across Bert and GPT2 models with modest utility degradation.

## Strengths

- **Novel MPC type-conversion primitives for quantization-aware inference.** The upcast protocol (Algorithm 1) is a genuine technical contribution — it converts RSS shares from a smaller ring to a larger ring with concrete communication complexity of 3ℓ + ℓ′ bits in 3 rounds. No prior MPC framework for Transformers supports these conversions, which are essential for variable-precision quantization. The downcast protocol is locally computable (right-shift + modulo), which is cleanly designed.

- **Consistent and substantial empirical speedups across four Transformer models.** Ditto achieves 1.44–2.35× over PUMA and 3.14–4.40× over MPCFormer (Figure 2, Table 4). The speedups are consistent across Bert-base, Bert-large, GPT2-base, and GPT2-medium, and hold across varying input sequence lengths (Table 5). The communication reductions (2–3× over PUMA) directly explain the runtime improvements, lending credibility to the results.

- **Well-motivated MPC-friendly quantization design.** The paper clearly identifies two cross-domain gaps (Gap 1: dynamic quantization is MPC-expensive; Gap 2: type conversions between rings are non-trivial in MPC) and provides principled solutions: static dyadic quantization with shift-based truncation replaces expensive clip/max operations, and the novel upcast/downcast primitives enable ring conversion. The toy example (Figure 1) concretely illustrates why naive quantization fails in MPC.

- **System-level compiler integration.** Extending the SPU compiler to support dynamic ring dispatch and automatic type-conversion insertion makes the approach practical and easy to deploy from HuggingFace models. This bridges the gap between the protocol design and real-world usability.

## Weaknesses

### Fatal
None.

### Major
None — none of the issues individually or collectively invalidate the core contribution. The upcast protocol's range assumption is transparently presented as a heuristic, the baseline comparisons show large and consistent speedups that cannot be explained by framework differences alone, and the utility numbers are honestly reported in the tables.

### Minor

- **The upcast protocol's range assumption is stated but not verified (Section 4.3.1).** The "positive heuristic trick" assumes input `x ∈ [-2^{ℓ-2}, 2^{ℓ-2}-1]` so that the MSB of the masked value can be used to compute the wrap term. The paper calls this a heuristic and says "supposing" the input satisfies this bound, but never verifies that actual values during quantized Transformer inference respect this bound. For the 32→64-bit upcast path actually used, the bound is [-2³⁰, 2³⁰-1] ≈ ±1 billion — extremely generous given FXP32₈ encoding (with 8-bit fractional precision, actual integer values are ≪ 2²³), so the assumption very likely holds in practice. However, the paper should either provide a formal argument, empirical validation across all models/inputs tested, or a fallback protocol. This is a documentation gap, not a structural flaw.

- **The "negligible utility degradation" claim is overstated for GPT2.** Perplexity increases from 12.25→13.78 (GPT2-base, +12.5% relative) and 10.60→11.35 (GPT2-medium, +7% relative) under Ditto (Quad). While the GLUE results for Bert indeed show minimal degradation (within ~1–2 points on accuracy metrics), the GPT2 perplexity increases are clearly noticeable and should be characterized as a modest trade-off rather than "negligible." The paper should discuss whether this degradation is acceptable for downstream applications.

- **Experimental results do not specify which network setting (LAN vs. WAN) was used for the main efficiency figures.** The experimental setup (line 314) defines both LAN (5 Gbps, 0.4ms RTT) and WAN (400 Mbps, 40ms RTT), but Figure 2 and Table 4 ("Inference efficiency with varying input length") do not state which setting produced the reported numbers. Protocol round count matters more in WAN, so this omission makes it impossible to assess how the speedups would translate to real deployments. The authors should report results for both settings or at minimum state which was used.

- **Cross-framework baseline comparisons are not fully apples-to-apples.** The paper compares against MPCFormer and PUMA running in their own frameworks rather than within the same SPU pipeline. The footnote about MPCFormer being "configured to run on CPU for fair comparisons" is vague. Additionally, the embedding layer difference (one-hot vectors computed in MPC vs. locally by the client) is acknowledged but the potential impact on the GPT2 results (where MPCFormer shows lower communication) is not quantified. Re-implementing baselines within SPU, or providing a detailed per-operation cost breakdown, would substantially strengthen the efficiency claims.

- **Ablation studies are performed only on Bert, not GPT2.** Given the larger utility degradation observed on GPT2, an ablation on GPT2 showing the individual effect of quantization alone vs. quantization + Quad approximation would help readers understand the source of the perplexity increase.

- **Discussion section is empty.** The paper has a `\section{Discussion}` with no content. This is a missed opportunity to address limitations (the upcast heuristic, the GPT2 trade-off, framework differences) and to situate the work.

### Trivial
- Figure 2 is dense; the "red star" marking Ditto is hard to distinguish. A higher-contrast marker or annotation would help.

## Nice-to-Haves
- A breakdown of where time is spent in the Ditto pipeline (linear layers, non-linear functions, type conversions) would help readers understand which components drive the speedup.
- An ablation varying the precision bits (why 8 for linear layers and 18 for non-linear?) would strengthen the empirical contribution.
- A brief security argument for the upcast protocol (why revealing `y = x + r` in the smaller ring does not leak information beyond the ideal functionality) would be useful, though the protocol is plausibly secure under semi-honest assumptions.

## Removed Points

- **Criticism about the "first framework" claim being too broad.** The paper qualifies this with "To the best of our knowledge" (line 57) and properly distinguishes from SecureQ8 which did not extend quantization to ciphertext ring sizes. This is appropriately scoped.
- **Criticism about missing related works.** Cannot be verified without external sources (per instruction).
- **Criticism about undisclosed hyperparameters / reproducibility details beyond what is standard.** The paper states it will open-source code and provides sufficient detail for the protocol contributions.
- **Criticism about the missing GPT2 results for Quad+2ReLU in Table 2.** The dash entries indicate configurations that were not run, which is standard practice; this is not a weakness.
- **Criticism about missing security analysis of the upcast protocol framed as a fatal flaw.** The paper operates in the standard semi-honest model; the protocol's information flow is straightforward and the concern is addressable in a sentence.
- **The claim that the "upcast protocol is structurally flawed."** The paper transparently calls it a heuristic trick; the assumption is very likely satisfied in practice for the actual bitwidths used.

## Novel Insights

The most interesting point emerging from the reviews is the tension between the paper's framing of the upcast "heuristic trick" as a practical optimization and the reviewer's demand for formal guarantees. This reflects a broader methodological gap in the MPC+ML literature: protocols are often designed for worst-case guarantees, while quantization inherently bounds value ranges. The paper would benefit from explicitly bridging this gap by analyzing the value ranges induced by the static dyadic quantization scheme and proving that the heuristic's assumption is always satisfied under the chosen precisions (FXP32₈). Conversely, the concern about cross-framework baseline comparisons is standard for systems papers and the community should develop norms for fair comparison across MPC frameworks.

## Suggestions

1. **Verify or prove the upcast range assumption.** Since FXP32₈ has an 8-bit fractional part, the integer values are bounded by the quantization grid. Show analytically that for the chosen precision allocation (FXP32₈ for linear layers), all values satisfy the [-2³⁰, 2³⁰-1] bound. If possible, also provide empirical verification across all models and inputs.

2. **Re-benchmark with a "vanilla quantized" baseline within the same SPU framework.** Implement a uniform 64-bit fixed-point baseline and a "quantized + no type conversion" baseline inside Ditto's own SPU pipeline to isolate the contribution of reduced bitwidth from framework differences.

3. **Separate LAN and WAN results** for the main efficiency comparisons, or at minimum clearly state which network setting was used for each reported figure/table.

4. **Qualify the GPT2 perplexity degradation** as a modest trade-off rather than "negligible." Consider adding a GPT2 ablation (quantization only vs. quantization + Quad) to Table 6.

5. **Add a brief security note** for the upcast protocol explaining why revealing `y = x + r` in the smaller ring does not leak information (intuitively: `r` is uniform random and masks `x` perfectly in the smaller ring, so `y` is statistically independent of `x`).

## Score and Decision

The paper addresses an important practical problem (accelerating secure Transformer inference) with a novel and well-motivated approach combining static dyadic quantization, type-conversion primitives, and compiler support. The empirical results show meaningful and consistent speedups. None of the identified weaknesses are fatal — they concern verification gaps, presentation issues, and overclaiming rather than invalidating the core contribution. The paper would benefit from addressing these concerns but is acceptable in its current form.

**Score:** 6.0

**Decision:** Accept

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>