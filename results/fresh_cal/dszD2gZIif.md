Now I have all the information needed to write the review.

## Summary
This paper proposes Swin4TS, which adapts Swin Transformer's window-based attention and hierarchical representation for long-term time series forecasting. Two variants are presented — Swin4TS/CI (channel-independent) and Swin4TS/CD (channel-dependent) — enabling flexibility across datasets with different numbers of channels. The method achieves linear O(ML) complexity and is evaluated on 32 prediction tasks across 8 benchmark datasets.

## Strengths
- **Linear computational complexity well-supported**: Section 5 explicitly derives O(ML) complexity for both variants by fixing window and patch sizes. Table 4 confirms this empirically with inference time and memory measurements on the Electricity dataset, showing better speed/memory trade-offs than all other Transformer-based models listed. This is a concrete, verifiable advantage.
- **Flexible adaptation to both CI and CD strategies**: Section 3.2 clearly describes two architectural variants. The CI variant handles channels independently (efficient for large-channel datasets like Traffic, Electricity), while the CD variant extends window attention to the 2D (channel × time) grid to capture cross-channel correlations. This flexibility contrasts with methods that only support one strategy (e.g., PatchTST uses CI only, Crossformer uses CD only).
- **Strong empirical results on controlled subsets**: On the ILI dataset, where all models use the same look-back window (L=108), Swin4TS/CD achieves a 15.8% improvement over the previous best (1.967→1.657 MSE). On ETT datasets, Swin4TS/CD achieves approximately 10% average improvement over CD-strategy baselines. These controlled comparisons provide genuine evidence of effectiveness.
- **Complexity/efficiency table (Table 4)**: Provides a clean comparison of time and memory complexity across Transformer-based models, demonstrating that Swin4TS is the first Transformer-based model with linear complexity in both L and M.

## Weaknesses

### Fatal
None.

### Major
- **Uncontrolled comparison via mismatched look-back windows**: Swin4TS uses L=512 for most datasets (L=108 for ILI), while several baselines (Autoformer, FEDformer, Crossformer, TimesNet, N-HiTS, MICN) are evaluated at L=96. The authors acknowledge this in a footnote ("different models require suited L to achieve their best performance") and state they "compare with the strongest results of each baseline algorithm." However, they do not re-run these baselines with matched look-back windows. Because longer historical context almost always improves forecasting accuracy, the reported advantage on several datasets could be partly attributable to the longer input rather than the architectural design. The central claim of state-of-the-art performance is therefore not fully supported by the evidence presented. This is the most significant weakness — fixable, but critical to the paper's main contribution.

### Minor
- **Ablation study is limited**: Table 3 covers only two datasets (ETTm1, ETTm2) with only the CD variant. The reported degradation from removing shift or scale is modest (~3% MSE increase), and no standard deviations or multiple-seed results are provided. Without ablations on additional datasets (e.g., Weather, ILI, Traffic) or on the CI variant, the claimed importance of the two key design choices is not rigorously validated. The paper would benefit from a broader ablation with variance estimates.
- **Qualitative attention analysis only**: Figures 5 and 6 show attention maps that are interesting but anecdotal. The paper claims these demonstrate "correlations across channel and time" and "hierarchical information," but no quantitative measure (e.g., correlation between attention weights and ground-truth channel correlations) is provided to substantiate these interpretations.

### Trivial
- **Brief mention of TNT4TS**: The conclusion mentions designing "TNT4TS" as further evidence of generalizability but provides no architecture details, results, or analysis. This should either be expanded (even a single table or paragraph) or removed to avoid distracting from the main contribution.

## Nice-to-Haves
- Present per-horizon results in the main text (rather than only as averages over four horizons) to give readers a clearer picture of performance across different forecast lengths.
- Include "Other Results" findings (randomness test, effect of channel order, varying historical length) in the main text, or at least summarize key takeaways from them in a short paragraph, to make the paper more self-contained.

## Removed Points
These points are flagged to be removed; treat them with caution:
- **Missing hyperparameter specifications (window size, patch length, #stages, etc.)**: Per the hard rules, nitpicks about undisclosed hyperparameters are removed. These details would be important for full reproduction but are typically expected in an appendix or code release, and their omission does not invalidate the paper's claims.
- **Unfinished sentence / garbled text in CD strategy section**: This is a PDF parsing artifact, not an author error.
- **Missing appendix content ("Other Results" refer to absent appendix)**: Per the hard rules, weaknesses about missing appendix content that was stripped by the parser are removed.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Control the look-back window**: Re-run all baselines at L=512 (and L=108 for ILI), or run Swin4TS at L=96 and demonstrate it still outperforms the baselines. This single experiment would resolve the most damaging criticism.
2. **Expand the ablation study**: Include at least 2 additional datasets (e.g., Weather and ILI) and both CI/CD variants. Report results over multiple random seeds with standard deviations.
3. **Provide hyperparameter specifications**: A table with window size, patch length, number of stages, hidden dimension, number of heads, and training details (learning rate, batch size, epochs) should be included, either in the main text or an appendix.

## Calibration Anchors
All anchors from calibration_search (one batch), compared to the paper under review:
- **TimeMixer++** (8.00, `/home/wg25r/split_review/datasets/deepreview_13k_calibration/1CLzLXSFNn.md`): Much more thorough evaluation across 8 tasks with stronger ablations; current paper is substantially weaker.
- **FITS** (8.00, `/home/wg25r/split_review/datasets/deepreview_13k_calibration/bWcnvZ3qMb.md`): Ultra-lightweight model with cleaner evaluation and comprehensive ablation; current paper has more significant evaluation concerns.
- **ModernTCN** (8.00, `/home/wg25r/split_review/datasets/deepreview_13k_calibration/vpJMJerXHU.md`): Consistent SOTA across 5 tasks with thorough analysis; current paper is less thorough in validation.
- **Simple Baseline MTS** (6.75, `/home/wg25r/split_review/datasets/deepreview_13k_calibration/oANkBaVci5.md`): Similar-level issues (baseline discrepancy, missing hyperparameters) but with more extensive baselines (15 models); current paper is slightly weaker due to the more central look-back window concern.
- **Generative TS Learning** (5.60, `/home/wg25r/split_review/datasets/deepreview_13k_calibration/rGdEM131Ht.md`): Energy-based approach with decent idea but limited evaluation; current paper has stronger empirical support.
- **Retrieval Augmented TS** (4.67, `/home/wg25r/split_review/datasets/deepreview_13k_calibration/GYwH71ugtC.md`): Interesting idea with mixed results; current paper has clearer methodology and stronger results.
- **Frequency Collapse** (4.33, `/home/wg25r/split_review/datasets/deepreview_13k_calibration/SwIkknEqmt.md`): Interesting phenomenon but weaker evaluation and theoretical gaps; current paper is stronger in method clarity and empirical scope.
- **TF-score** (3.00, `/home/wg25r/split_review/datasets/deepreview_13k_calibration/RDLvnUJ5JZ.md`): Significant mathematical issues and limited innovation; current paper is substantially stronger in all dimensions.
- **VIPER** (3.00, `/home/wg25r/split_review/datasets/deepreview_13k_calibration/0Q1mBvUgmt.md`): Weak evaluation overall; current paper is clearly stronger.
- **FIA-Net** (2.50, `/home/wg25r/split_review/datasets/deepreview_13k_calibration/WFlLqUmb9v.md`): Confusing presentation and weak results; current paper is better on all fronts.

## Score and Decision
The paper proposes a clean, well-motivated adaptation of Swin Transformer to time series. The linear complexity analysis and CI/CD flexibility are genuine strengths. However, the core SOTA claim is undermined by mismatched look-back windows between Swin4TS (L=512) and several baselines (L=96) without controlled re-evaluation. The ablation study is also too narrow to fully validate the design choices. These issues are fixable but central; in its current form, the paper does not provide sufficient evidence for its main empirical claim. I position this paper below the Simple Baseline MTS (6.75) anchor and above the Frequency Collapse (4.33) anchor.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>