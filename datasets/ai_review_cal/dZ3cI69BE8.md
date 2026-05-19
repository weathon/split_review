- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 5, 3, 6
Now I have all the information needed. Let me produce the consolidated review.

## Summary

FlexBCQ proposes a method for binary-coding quantization (BCQ) of LLMs that decomposes BCQ's quantization process into the composition of a uniform quantization (UQ) transformation and an inner BCQ. This enables borrowing FlexRound's flexible mapping technique from UQ while retaining BCQ's adaptive non-uniform quantization levels. A Composition Theorem proves the two-step reconstruction can be merged back into a single BCQ operation, eliminating inference overhead. The method also introduces unified initialization, gradient filtering, and periodic remapping optimization techniques. The headline result is a +3.24% absolute accuracy gain on MMLU 5-shot for Llama-3 70B at 3-bit weight-only quantization over prior methods.

## Strengths

1. **Novel and well-motivated formulation.** The decomposition of BCQ into UQ transformation + inner BCQ (Eq. 7) is clever and principled. It directly addresses the core challenge — UQ methods have better optimization techniques but BCQ has better representation power — and combines both. This is not an incremental tweak.

2. **Composition Theorem guarantees no inference overhead (Theorem 1).** The paper proves that the two-step reconstruction (detransformation after BCQ reconstruction) can be merged into a single BCQ reconstruction function, so FlexBCQ adds zero latency or memory cost at inference time vs. standard BCQ. This is a non-trivial and practically important result.

3. **Ablation study cleanly demonstrates the necessity of each component.** Removing gradient filtering collapses MMLU accuracy to ~0% (Table 3), and removing periodic remapping drops accuracy by >4%. This provides strong evidence that the optimization techniques are essential, not decorative.

4. **Strong performance on the largest model at the lowest bit-width.** The 3.24%p gain over FlexRound on Llama-3 70B at 3-bit (MMLU 5-shot) is a practically meaningful result on a challenging setting where gains are hard to achieve. The unified initialization also demonstrably reduces weight reconstruction error across all projection types (Table 4).

5. **Empirical validation of intended mechanism.** Section 4.5 visualizes that FlexBCQ indeed produces quantization levels denser where weights concentrate (Figure 4a) and enables diverse index mappings akin to FlexRound (Figure 4b), confirming the theoretical motivation.

## Weaknesses

### Fatal
None.

### Major

1. **Perplexity results are entirely absent.** The paper evaluates quantized models exclusively on downstream tasks (MMLU, GSM8K) and never reports perplexity on a standard language modeling corpus such as WikiText-2 or C4. Perplexity is the standard metric for assessing whether a weight-only quantization method preserves language modeling quality, and virtually all recent LLM quantization papers (GPTQ, AWQ, OmniQuant, FlexRound, QuIP) report it. Downstream accuracy can be noisy, calibration-set-dependent, and opaque about whether language modeling capability is genuinely retained. The 4-bit results already show FlexBCQ *underperforming* FlexRound by 0.25%p (acknowledged by the paper as possible overfitting), and without perplexity there is no way to decouple fitting-to-benchmark from genuine compression quality. This is the single largest evidential gap.

2. **No error bars, statistical significance, or multiple-run variability reported.** All results appear to be single runs. The headline 3.24%p gain on Llama-3 70B at 3-bit could partially reflect run-to-run noise, and we have no way to assess. This is especially important given that on Mistral 7B and Llama-3 8B the gains are very small or negative in several configurations — the overall picture of "superior" accuracy is less robust without variance estimates.

### Minor

3. **BCQ baselines are weak (Greedy/Alternating from Xu et al. 2018).** These methods were designed for small neural networks, not LLMs, and achieve near-zero accuracy on GSM8K and far-below-UQ accuracy on MMLU. While the paper acknowledges that BCQ research for LLMs is limited, the comparison creates an artificially large gap that FlexBCQ then "closes." The ablation study (Table 3) partially addresses this by comparing against FlexBCQ without flexible mapping, but this comparison is only shown for one model/bit-width. Extending the ablation-style baseline (FlexBCQ without flexible mapping) to all models in the main tables would establish how much of the gain comes from the optimization framework vs. the flexible mapping innovation itself.

4. **The method slightly underperforms FlexRound at 4-bit, and gains are marginal in several configurations.** On Mistral 7B at 3-bit, the improvement over FlexRound is ~0.04% (essentially tied), and at 0-shot Llama-3 8B at 3-bit, results are also near-identical. The 4-bit results are consistently below FlexRound by ~0.25%. The paper attributes this to overfitting but provides no evidence (validation loss, held-out perplexity, distribution gap analysis) to support or refute this claim. The strong claim in the abstract ("3.24%p higher accuracy than existing UQ and BCQ algorithms") highlights the best case without contextualizing the more mixed results.

5. **No calibration cost or wall-clock time reported.** The unified initialization iterates over 50 clipping ratios × 15 quantization level adaptation iterations per group, plus 20 epochs of blockwise reconstruction. For a 70B model this is a non-trivial compute budget. The paper does not report how long calibration takes or whether it is practical relative to baselines.

6. **No empirical verification of inference speed.** The paper repeatedly claims that FlexBCQ incurs no latency or memory overhead (via the Composition Theorem), which is theoretically sound. But no empirical measurement (tokens/sec, wall-clock inference time) is provided to confirm that the merged BCQ reconstruction is indeed as fast as claimed.

7. **The gradient filtering threshold (τ = min(α_(k))) and remapping period (p) are heuristics with no sensitivity analysis.** The ablation shows that removing gradient filtering causes collapse, and there is sensitivity to p (p=1 drops accuracy by ~4%). But no ablation varies τ or p over a range of values to show stability. The period p is 2 for most experiments but 1 for Llama-3 70B with no rationale given.

### Trivial

8. The paper uses "FlexBCQ" and "FLEXBCQ" inconsistently in the text. The abstract and introduction establish "FlexBCQ" but some section headings and equations use "FLEXBCQ."

## Nice-to-Haves

- Adding perplexity results on WikiText-2 and C4 (this is listed as Major above, but I note here that it would be a natural extension that would clearly resolve the biggest gap).
- Including GPTQ and AWQ as additional accuracy reference points, even if inference speed comparisons are not directly apples-to-apples due to different kernels.
- Reporting the exact computation for the merged BCQ parameters Θ_B* (α*, z*) from Θ_U and Θ_B — the Composition Theorem is stated but not operationalized.
- Analyzing why p=1 for Llama-3 70B but p=2 for other models.

## Removed Points

These points were raised by reviewers but are removed (with justification):

- *"The proof of Composition Theorem is relegated to the appendix."* → Removed per hard rule: the parser strips appendix sections from all papers. The proof exists in the original submission (Section E).
- *"BCQ's representation space claim is unclear because after training levels are fixed."* → Removed: the paper's claim about representation space refers to the *capacity* of the quantization scheme, not to a specific trained instance. The critic misunderstands this.
- *"Notation is dense and could be simplified."* → Removed as a style nitpick without specific actionable content.
- *"The number of epochs and learning rate are taken from OmniQuant but it's not clear if the same schedule was used."* → Removed: the paper explicitly states it follows OmniQuant's setup, which is standard practice for controlled comparison.
- *"The ablation collapse without gradient filtering warrants explanation and the paper doesn't provide one."* → Removed: the paper *does* provide an explanation (lines ~224-226: clipped weights violate the STE hypothesis). The explanation may be imperfect but it exists.
- *"Reproducibility concern about merged parameter procedure."* → Removed: the proof in the appendix (Section E) would contain the construction; the procedure exists in the original submission.

## Novel Insights

None beyond the paper's own contributions. The two reviews are largely concordant: the harsh critic correctly identifies evaluation gaps (especially perplexity), and the strength finder correctly identifies the genuine methodological novelty (the composition formulation and theorem). The key insight that synthesizes both is that the paper's contribution is real and well-motivated, but the evaluation needs to meet the field's standard before the paper's claims can be fully trusted.

## Suggestions

1. **Add perplexity on WikiText-2 and C4** for all model/bit-width combinations tested. This is the single highest-impact improvement and directly addresses the most serious weakness.
2. **Add error bars or at least report multiple runs** (ideally 3 seeds) for the key configurations, especially the headline Llama-3 70B 3-bit result. This would substantially increase confidence in the results.
3. **Extend the "FlexBCQ without flexible mapping" ablation** (currently only in Table 3 for one setting) to all models and bit-widths in the main tables, creating a stronger BCQ baseline for comparison.
4. **Report calibration time** (total GPU-hours for 70B model) so readers can assess practicality.
5. **Report empirical inference throughput** (tokens/sec) for FlexBCQ vs. baselines to verify the Composition Theorem's practical claim.
6. **Provide sensitivity analysis** over the remapping period p and gradient filtering threshold τ.
