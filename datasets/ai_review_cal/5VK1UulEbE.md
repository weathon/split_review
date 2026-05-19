- Decision: Reject
- Avg Score: 4.20
- Scores: 3, 5, 3, 5, 5
Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary
The paper proposes FredNormer, a frequency-domain normalization module for non-stationary time series forecasting. It uses a coefficient-of-variation-based stability metric (computed across training samples) to weight frequency components, combined with a learnable linear projection to adjust those weights per sample. Experiments across seven datasets with three backbones (DLinear, PatchTST, iTransformer) show consistent improvements over RevIN and SAN, the leading time-domain normalization methods.

## Strengths

- **Novel formulation of normalization in the frequency domain.** This is the first work to explicitly design a normalization module that operates in the frequency domain for time series forecasting. Using cross-sample frequency stability as an inductive bias for reweighting the spectrum is a sensible and underexplored direction.

- **Consistent empirical improvements across backbones and datasets.** Against RevIN and SAN, FredNormer (without stacking SAN) achieves 8 out of 14 top-1 MSE results (Table 2, "Count" row for Ours alone on MSE). These gains hold across both MLP-based (DLinear) and Transformer-based (iTransformer) architectures, indicating method-agnosticity.

- **Computational efficiency.** Per-epoch runtime (Figure 4, labeled `fig:Cost_result`) is consistently lower than SAN, with the paper reporting speed improvements of 60–70% in 16 out of 28 settings. This is a practical advantage for a normalization module that must be fast enough to not bottleneck the backbone.

- **Complementarity with existing normalization.** The "Ours*" results (FredNormer stacked on top of SAN) often achieve the best or second-best results (e.g., ETTh1 iTransformer at H=96: 0.380 vs 0.389 for Ours alone), showing that frequency-domain weighting can add value beyond what time-domain normalization already provides.

## Weaknesses

### Fatal
None.

### Major

- **Headline improvements are against the bare backbone, not the relevant competitors.** The abstract and introduction advertise "33.3% and 55.3%" improvements on ETTm2. These compare FredNormer to an *un-normalized* backbone (Table 1, "Ori" columns). Against SAN—the claimed state-of-the-art normalization—the improvements are substantially more modest (e.g., iTransformer on ETTm2: 0.283 vs 0.287, ~1.4% relative; Weather: 0.246 vs 0.247). The paper *does* report the SAN comparison in Table 2, but the prominence given to the bare-backbone numbers in the abstract and introduction creates an inflated impression. A practitioner evaluating whether to replace SAN with FredNormer needs the SAN-relative numbers front and center.

- **Theoretical analysis is oversold.** Lemma 1 (normalization uniformly scales non-zero frequencies) and Theorem 1 (energy proportion of stable frequencies is preserved) are direct consequences of the linearity of the Fourier transform and the definition of z-score normalization. These are elementary observations, not novel theoretical insights. Presenting them as a "theoretical analysis" and a core contribution overstates their depth. The paper's real novelty lies in the method design and empirical validation, not in these theorems.

### Minor

- **Ablation study does not isolate what drives the improvement.** Table 4 compares FredNormer's stability metric against (a) a low-pass filter and (b) random frequency selection. These are weak baselines; a random filter is expected to perform poorly. The paper does not ablate its own components: (i) stability weighting without the learnable linear projection, (ii) learnable weights without stability precomputation (i.e., treating them as free parameters), or (iii) the CV-based metric vs. using mean amplitude alone or inverse variance alone. Without these ablations, it is unclear whether the improvement comes from the stability metric, the learnable projection, or the combination.

- **Unexplained interaction of 1-D differencing with frequency stability.** The method applies 1-D differencing before the DFT (Alg. 2, line 235; Section 3) "to smooth the data." Differencing is a high-pass filter that fundamentally changes the spectrum. Its effect on the stability measure S(k) is not analyzed, and no sensitivity study (e.g., with/without differencing) is provided. This step may be critical or incidental—the paper does not say.

- **Unclear experimental protocol regarding z-score normalization.** The paper states "We combine our module with a z-score normalization-denormalization operation in all experiments" (line 425). Since RevIN *is* an instance-wise z-score normalization, it is ambiguous whether FredNormer receives an extra normalization step that RevIN does not, or whether both operate under the same pipeline. The paper should state explicitly: which preprocessing does each condition receive? Are all methods (FredNormer, RevIN, SAN) applied on top of the same base normalization, or does each replace it?

- **Definition of Stable Frequency Subset (Definition 2) is decorative.** It defines a hard-selected subset of size M, but the method uses continuous weighting throughout, never actually selecting M components. M is never specified or ablated. This definition adds confusion rather than clarity.

- **No discussion of limitations.** The paper concludes without acknowledging any limitations (e.g., what happens when the training distribution is non-representative of the test distribution? Does the stability measure break down with very short input lengths where frequency resolution is poor?).

### Trivial
None.

## Nice-to-Haves

- Include the running time of RevIN alongside SAN in the efficiency comparison (Figure 4) to give a complete picture of overhead.
- Report confidence intervals or perform paired significance tests on the comparisons where gains over SAN are small (e.g., Weather: 0.246 vs 0.247).
- Analyze sensitivity to the differencing step: what happens if it is omitted?

## Removed Points

*These points were raised in the input reviews but are removed here with justification:*

- **Ambiguity in tensor operation notation (S × W_r):** The critic claimed the operation is not well-defined. The algorithm pseudocode (Alg. 2) and the explicit statement of W_r ∈ ℝ^{K×1} together make the intended broadcasting/iteration clear. The notation is standard in deep learning papers. *Removed: overly pedantic; not a real barrier to reproducibility.*

- **Table 1 comparing only bare backbone is "not meaningful":** It is standard to first show the improvement over the un-normalized baseline before comparing against competitors. The meaningful comparison is in Table 2. *Removed: standard presentation practice.*

- **Missing related works / comparison with frequency-domain forecasting models:** The paper is about normalization, not about forecasting model architectures. Comparing against FEDformer/TimesNet would be scope creep. *Removed: outside stated scope.*

- **"Plug-and-play" claim vs. learnable parameters:** The paper explicitly states "Only simple linear projection layers with a few parameters need learning and tuning" (line 78). It does not claim to be parameter-free. *Removed: paper already addresses this.*

- **Pure formatting and style nitpicks** from the reviews: removed per filtering rules.

## Novel Insights

None beyond the paper's own contributions. The cross-sample frequency stability measure as a normalization signal is the core insight, and the reviews do not surface an additional novel lens beyond what the paper already presents.

## Suggestions

1. Rebalance the abstract and introduction: lead with the comparison against RevIN and SAN (18/28 top-1 results), and state the bare-backbone improvements as secondary.
2. Add ablations that isolate the three components: (a) stability metric without learnable weights, (b) learnable weights without stability precomputation, (c) CV-based metric vs. mean-only or variance-only alternatives.
3. Clarify the experimental protocol: does FredNormer add a separate z-score step on top of what RevIN/SAN already do, or do all methods share the same base pipeline? Be explicit.
4. Either remove Definition 2 (Stable Frequency Subset with hard M selection) or explain how it relates to the continuous weighting used in practice.
5. Add a brief limitations paragraph to the conclusion.
