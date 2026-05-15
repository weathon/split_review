Now I have thoroughly analyzed the paper and all reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper introduces UniTS, a hybrid time-series forecasting model combining global (linear/MLP-based) and local (CNN-based) feature extractors with instance normalization (IN) and data patching. It also addresses the issue of inconsistent lookback window lengths across prior work by systematically evaluating models under multiple lookback settings. The paper claims state-of-the-art performance across eight long-term forecasting benchmarks and uses ablations to assess the contribution of each module.

## Strengths

- **Systematic standardization of lookback window evaluation (well supported, Section 4.1)**: The paper identifies a concrete methodological problem — prior work uses different lookback window lengths, making cross-model comparisons unreliable — and addresses it by designing two evaluation settings (finetuned lookback and fixed lookback). Figure 2 empirically demonstrates that lookback length strongly affects performance, which is a useful practical insight for the field. This standardization contribution stands on its own regardless of the model's performance.

- **Clean, thorough ablation isolating the contribution of each module (Table 2, Section 4.5)**: The paper provides a systematic ablation that quantifies the effect of removing individual components (GFE, LFE, IN, attention, position encoding, layer normalization) across three datasets. The finding that Instance Normalization is far more impactful than any architectural component is an honest and useful result, and the ablation methodology is sound.

- **Consistent state-of-the-art claims across eight benchmarks (Table 1)**: UniTS is reported to achieve the best MSE/MAE results across all datasets and prediction horizons, outperforming strong baselines including PatchTST, DLinear, TimesNet, and FEDformer. While the actual numbers are in an image table that cannot be rendered here, the claim is clear and the breadth of evaluation (8 datasets, multiple prediction horizons) is substantial.

## Weaknesses

### Fatal
None.

### Major

- **The hybrid contribution is empirically very small, undermining the paper's central narrative (Section 4.5, line 154).** Removing the Local Feature Extraction (LFE / CNN) module increases MSE by only 2.19% on average, while removing the Global Feature Extraction (GFE / linear) module increases MSE by 28.04%. The paper is titled "Hybrid Modeling" and its core motivation is combining global and local modeling to overcome single-model limitations, but the evidence shows the global linear component is doing nearly all the work. The local CNN branch provides a marginal, not structural, improvement. This does not invalidate the model (UniTS as a whole still achieves SOTA), but it means the paper's framing substantially oversells the importance of the hybrid design.

- **The claim that "attention is not essential for time series forecasting" overreaches from an insufficient experiment (Section 4.4, line 145).** The paper tests whether adding attention, position encoding, and layer normalization to UniTS's *linear global extractor* degrades performance, and concludes "the attention layer is not essential for temporal modeling." This experiment tests a specific, ad-hoc addition of attention mechanisms without the full Transformer design (residual connections, proper tuning, multi-head attention with matched hyperparameters). It does not constitute a valid test of whether canonical Transformer architectures (e.g., PatchTST) are effective — the paper's own claim that PatchTST is a strong baseline contradicts this conclusion. The result shows only that attention does not help *this particular linear layer in this particular architecture*, not that attention is generally unnecessary for time series forecasting. This overclaim is significant and needs correction.

### Minor

- **The "best-of-six" lookback selection inflates baseline results and is not a standard reproducible configuration (Section 4.1, line 103).** For setting (i), baselines are evaluated with six different lookback lengths and the *best* result is reported. This reports an upper envelope of performance rather than a principled, reproducible configuration. While the paper applies this uniformly to all models, the methodology inflates absolute performance and is itself a deviation from the "fair comparison" standard the paper claims to establish. A more standard approach would be to pick a single reasonable lookback or tune it on a validation set.

- **Lack of reproducibility details for the CNN-based local feature extractor (Section 3.2.3, line 80).** The paper states the local extractor uses "several convolutional kernels of different scales" but provides no specific numbers (how many kernels, what kernel sizes, strides, number of layers). The global extractor is clearly described (linear layer following DLinear), but the CNN branch — which is half of the claimed hybrid contribution — is underspecified.

- **No computational cost comparison (parameters, inference time, training time) is reported.** The hybrid model adds CNN kernels to a linear backbone, but the paper never reports whether this increases parameter count or runtime relative to baselines. Given the modest 2.19% gain from the LFE module, a cost-benefit analysis is needed to assess whether the added complexity is justified.

- **The paper overstates the novelty of hybridizing linear and convolutional branches (Section 1, lines 10–14).** Combining linear/MLP layers with CNN layers for time series is a well-explored design pattern (e.g., TCN+linear hybrids, N-BEATS, and various multi-branch architectures). The paper does not clearly articulate what is architecturally new about UniTS beyond the particular implementation choices.

### Trivial
- The writing contains some awkward phrasing and grammatical issues, but these do not impede understanding.

## Nice-to-Haves

- Reporting standard deviations or confidence intervals for the main results would help assess whether the 2.19% improvement from LFE is statistically reliable.
- An analysis of what the CNN branch actually learns (e.g., visualizing feature maps or frequency responses) would help justify retaining it despite the small marginal gain.
- Testing UniTS on a domain where local patterns are known to dominate (e.g., high-frequency financial data, sensor logs with transients) would provide a more convincing demonstration of the hybrid design's value.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **Criticism that Table 1 has a "missing figure placeholder" and text provides no concrete MSE/MAE values.** REMOVED: The table is an image that was stripped by the PDF-to-text parser; it exists in the original submission. The paper clearly references Table 1 and its results.

2. **Strength Finder claim #2: "Empirical demonstration that attention layers are not essential for time series forecasting ... providing strong evidence against the necessity of Transformer-style modeling."** REMOVED (moved from Strengths): This strength conflicts with the verified weakness showing that the experiment is an insufficient test of Transformer architectures. The paper's experiment only tests attention within its own linear layer, not a proper Transformer, so calling it "strong evidence" overstates the finding.

3. **Criticism about the hyperparameter search section (Section 4.5) not validating the proposed model.** REMOVED: This is a standard supplementary experiment that demonstrates the importance of hyperparameter tuning in the field generally; it is not required to validate the specific model.

4. **Criticism about missing comparison with PatchTST under identical preprocessing.** REMOVED: The paper does run PatchTST as a baseline under the same evaluation framework (Section 4.1), which constitutes a reasonable comparison. The reviewer's request for an even stricter control is a nice-to-have, not a required experiment.

5. **Criticism that the paper does not test UniTS without IN but with the hybrid design still outperforming DLinear.** REMOVED: The paper's ablation already shows that IN is the dominant factor. Requesting an additional deconfounding experiment is a reasonable suggestion for future work, not a weakness of the current paper.

## Novel Insights

The most interesting observation from this review process is the tension between the paper's two main contributions. On one hand, the paper provides a valuable methodological contribution by systematically studying how lookback window length affects model performance and standardizing evaluation protocols — this is a genuine service to the field. On the other hand, the paper's architectural contribution (hybrid global+local modeling) turns out to be much more modest than the narrative suggests: the local CNN branch contributes only ~2% to performance. This asymmetry creates a mismatch between the paper's framing ("hybrid modeling overcomes single-model limitations") and its evidence ("the global linear component does almost everything, with a tiny additive benefit from local features"). The paper would be stronger if it honestly centered its contribution on the evaluation standardization and the finding that IN and lookback tuning matter far more than architectural innovations — rather than centering it on the hybrid architecture itself.

## Suggestions

1. **Reframe the paper's contribution honestly.** The most impactful findings are (a) that lookback window length standardization is critical for fair comparison, and (b) that instance normalization and global features dominate performance, with local features providing a small but consistent benefit. The title and framing should reflect this rather than overselling hybrid modeling.

2. **Tone down the conclusion about attention/Transformers.** Replace "the attention layer is not essential for temporal modeling" with the more precise claim: "Adding attention to a linear layer within the UniTS framework does not improve performance." Qualify the broader implications.

3. **Add a cost-benefit analysis.** Report parameter counts and training/inference times for UniTS and key baselines (especially DLinear + IN) to help readers assess whether the 2.19% improvement from the CNN branch is practically worthwhile.

4. **Provide specific CNN architecture details** in the main text or appendix: number of kernels, kernel sizes, strides, number of layers, and how scales are selected.

5. **Report standard deviations or use multiple seeds** for the main experimental results, particularly for the ablation comparison between UniTS and UniTS without LFE, to establish that the 2.19% gain is statistically reliable.

## Score and Decision

The paper has real, useful contributions — particularly the systematic study of lookback window effects and the clean ablation evidence that IN and global features dominate performance. However, the central narrative about the value of hybrid modeling is not well supported by the evidence (2.19% gain from the novel component), and the paper overclaims in its conclusions about Transformers. The evaluation protocol (best-of-six lookback selection) is itself a methodological concern. These issues do not invalidate the paper but mean it requires substantial reframing and additional experiments to meet the claims made.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>