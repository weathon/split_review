## Summary

The paper proposes Swin4TS, an adaptation of the Swin Transformer to long-term time series forecasting. It adopts window-based attention (achieving linear complexity O(ML)) and hierarchical representation from the Swin Transformer, and supports both channel-dependence (CD) and channel-independence (CI) strategies. Experiments on 8 benchmark datasets report strong performance.

## Strengths

- **Linear computational complexity in both time length and channel count**: The complexity analysis (Section 5) and empirical efficiency numbers on Electricity (Table 4) demonstrate that Swin4TS/CI achieves O(ML) complexity and competitive inference cost (0.18s, 1,174 MB) compared to PatchTST (0.28s, 1,432 MB) and Crossformer (1.76s, 4,375 MB). This is a concrete architectural advantage over prior quadratic-complexity Transformers.

- **Flexible compatibility with both CD and CI strategies**: The paper designs Swin4TS to work with both channel-dependence and channel-independence paradigms within the same framework. The results show that the preferred variant is dataset-dependent (e.g., CD excels on ILI and ETTh1, CI excels on Traffic and ETTm2), and the paper acknowledges this complementarity rather than forcing a single strategy.

- **Attention map visualizations support the multi-scale and cross-channel modeling claims**: Figures 5 and 6 provide qualitative evidence that the CD variant attends to patches across channels and that different hierarchical stages capture different temporal scales (local periodicity vs. global trends), lending interpretability to the architecture's design.

- **Conceptually clear motivation**: The paper articulates a clean analogy between time series patches and image patches, motivating why ViT/Swin architectures can transfer to time series. The adaptation is presented in a straightforward manner.

## Weaknesses

### Fatal
None.

### Major

- **Input length asymmetry weakens the SOTA claims**: Swin4TS uses L=512 (L=108 for ILI) for evaluation, while most baselines (FEDformer, Autoformer, TimesNet, N-HiTS, MICN, Crossformer) are evaluated at L=96. The paper acknowledges this ("different models require suited L") but provides no matched-length experiments — neither baselines at L=512 nor Swin4TS at L=96. While PatchTST and DLinear do use comparable lengths (336/512), the remaining six baselines see 5× less history. Without controlled experiments, the reported improvements (e.g., 15.8% on ILI, 10.3% on Traffic) cannot be confidently attributed to architectural merit rather than the advantage of longer input context. This is a significant gap in the main evidence for SOTA claims.

- **"Other Results" section contains unsupported claims**: Section 4.3 lists seven experimental findings (randomness test, channel order, varying hierarchical design, varying historical length, dynamic covariate, transferability) as single-sentence bullets with zero supporting tables, figures, or numerical values. These are presented as evidence for claims but cannot be evaluated. This is not a formatting issue — the substantive empirical content is absent. Either these results should be accompanied by data or the section removed.

### Minor

- **Ablation study is narrow**: The ablation (Table 3) only evaluates ETTm1 and ETTm2 (2 of 8 datasets). Removing both shift-window attention and hierarchical design degrades MSE by only 3.2% and 2.7% — modest for removing the paper's two claimed innovations. No ablation isolates the contribution of window-based attention versus full attention with comparable parameter count, making it difficult to assess whether the windowing itself or other aspects of the architecture drive performance.

- **Univariate evaluation is selective**: Univariate forecasting is reported only on the 4 ETT datasets, not on the other 4 (Weather, Traffic, Electricity, ILI). This makes the univariate SOTA claim appear incomplete.

- **Garbled/incomplete text in methodology**: Line 107 reads "Channel-dependence strategy The of Swin4TS with the CI strategy." — an incomplete sentence that disrupts the CD variant description. The downscaling operation in hierarchical representation is described as "unfold and reshape operations followed by a linear layer" without kernel size, stride, or dimension details, harming reproducibility.

- **Dangling reference to TNT4TS**: The conclusion mentions having designed a TNT4TS architecture but provides no results, comparison, or analysis. This adds no value.

### Trivial

- **Inconsistent baseline count**: The text says "compare with 7 the most recent and popular models" but then lists 8 models (counting 4 Transformer-based + 4 non-Transformer-based).
- Minor issue: Line 141 has a stray ".3)" reference that appears to be a broken citation or footnote tag.

## Nice-to-Haves

- Running controlled experiments with matched input lengths (baselines at L=512, Swin4TS at L=96) would substantially strengthen the SOTA claim.
- Expanding the ablation to more datasets and including a comparison against global attention with matched parameter count would better isolate the contribution of windowing.
- Providing per-horizon breakdowns in an appendix would allow readers to inspect consistency across prediction lengths.
- Adding a limitations discussion acknowledging contexts where Swin4TS might underperform (e.g., highly non-stationary series, very low data regimes) would improve credibility.

## Removed Points

- **"Incomplete experimental reporting (per-horizon breakdowns, confidence intervals)"**: Removed because reporting averages across horizons is standard practice in the LTSF field (e.g., PatchTST, iTransformer, TimesNet all do this), and confidence intervals are not standard in this sub-area. Not requiring confidence intervals does not mean the evaluation is "insufficient to be compelling."
- **"Complexity analysis is sketchy"**: Removed. The derivation is standard — fixed window size → constant complexity per window → O(L) total — and is accompanied by empirical measurements in Table 4, which is adequate for a conference paper.
- **"Missing code release / hyperparameters"**: Removed per instructions — trivial reproducibility nitpicks about undisclosed hyperparameters should not surface in evaluation.
- **"Missing related work"**: Removed per instructions — the reviewer cannot confirm whether works are missing without full knowledge of the field.
- **"No statistical significance tests"**: Removed per instructions about demanding practices not standard in this community.
- **"No limitations section"**: Removed per instructions about scope creep.
- **Strength Finder's "SOTA performance" strength was kept but qualified** in the weaknesses section.
- **Strength Finder's generic/superficial praise** about "problem importance" was filtered out.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a pattern common in cross-domain transfer papers: the conceptual adaptation is clean and well-motivated, but the experimental evidence is compromised by an asymmetric evaluation setup that prevents clean attribution of gains. This is worth noting as a general caution: when transferring architecture from one domain (vision) to another (time series), care must be taken to control for input-length advantages that are unrelated to the architectural transfer itself.

## Suggestions

1. **Run controlled experiments**: Evaluate all baselines at L=512 (where feasible) and Swin4TS at L=96. Report these results alongside the current asymmetric setup so readers can assess the role of input length.
2. **Substantiate or remove the "Other Results" section**: Each of the seven claims should have at minimum one table or figure with concrete numbers. If space is limited, move the substantiated versions to an appendix and reference them.
3. **Expand ablation**: Include at least the 4 ETT datasets plus one large-channel dataset (Traffic or Electricity). Add a variant replacing window attention with global attention (same parameter count) to isolate the contribution of windowing.
4. **Fix the garbled text around line 107** and clarify the downscaling operation with concrete dimensions or pseudocode.
5. **Add per-horizon results** to an appendix table for reproducibility and transparency.

## Score and Decision

**Anchors used (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 0Q1mBvUgmt.md (VIPER) | 3.00 | R1 | Much weaker — limited empirical evaluation, unclear contribution |
| WFlLqUmb9v.md (FIA-Net) | 2.50 | R1 | Much weaker — poorly supported claims |
| Y89o3LAEHX.md (Hybrid Loss) | 2.00 | R1 | Much weaker — limited contribution |
| MACKSU3xed.md (PeriodNet) | 2.50 | R1 | Much weaker — lightweight model with limited scope |
| T97kxctihq.md (Revisiting LTSF) | 5.00 | R1/R2 | Similar — both have clear ideas undermined by experimental gaps; this paper has a stronger architectural contribution |
| 9VRFPC29nb.md (Simplified Mamba) | 4.50 | R1/R2 | Similar — both have baseline fairness concerns and insufficient experiments |
| QhXisLeIqR.md (WinNet) | 5.00 | R1/R2 | Similar — both have reasonable core ideas but experimental gaps |
| zW1tyw3UFu.md (Dozerformer) | 4.50 | R1 | Similar — both propose attention modifications with incomplete validation |
| BSsyY29bcl.md (TwinsFormer) | 5.80 | R2 | Slightly stronger — more rigorous experiments (13 datasets), clearer writing, but marginal improvements over baselines |
| PdaPky8MUn.md (Never Train from Scratch) | 8.00 | R1 | Clearly stronger — thorough evaluation, clean experimental design, novel findings |
| 1CLzLXSFNn.md (TimeMixer++) | 8.00 | R1 | Clearly stronger — comprehensive evaluation across multiple tasks |
| bWcnvZ3qMb.md (FITS) | 8.00 | R1 | Clearly stronger — rigorous experiments, convincing ablations, strong results with minimal parameters |
| xriGRsoAza.md (Inherently Interpretable TSC) | 8.00 | R1 | Stronger in a different sub-area, but higher evaluation rigor |
| 9EBSEkFSje.md (GIFT-Eval) | 5.25 | R2 | Benchmark paper, different genre — similar evaluation rigor |
| 3rBu7dR7rm.md (Unified LTSF Benchmark) | 4.33 | R2 | Benchmark paper, different genre |
| 53gU1BASrd.md (Financial TSF) | 4.50 | R2 | Different domain but similar evaluation issues |
| X8aFMdXk3N.md (Fair Comparisons in TSF) | 4.25 | R2 | Focuses on data quality issues, not directly comparable |

**Round-1 bracket**: Placed the paper between 4 and 6 based on weak anchors at 2-3 and strong anchors at 8.

**Round-2 narrowing**: Compared against TwinsFormer (5.8), WinNet (5.0), Revisiting LTSF (5.0), Simplified Mamba (4.5), and GIFT-Eval (5.25). The Swin4TS paper has a clearer architectural contribution than Revisiting LTSF (which is primarily an analysis paper) and comparable scope to WinNet. However, the input-length asymmetry and unsupported "Other Results" section make it slightly weaker than TwinsFormer (5.8), which had more rigorous experiments. The paper is most comparable to WinNet (5.0) and Simplified Mamba (4.5) — papers with reasonable ideas but significant experimental gaps that prevent their claims from being fully supported.

**Final score**: 5.0

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>