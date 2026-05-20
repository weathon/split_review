Now I have sufficient calibration data. Let me write the consolidated review.

**Round 1 bracket:** Based on comparison with anchors, the plausible range for this paper is between 4.0 and 6.0. The paper is clearly stronger than DIMS (2.5) and STARformer (2.75), comparable to TwinS (4.5), FreCoformer (5.0), and TVDN (4.67), but somewhat weaker than TimeMixer (5.67) and SimpleTM (6.75) which were accepted.

**Narrowing within bracket:** After reading full reviews of TFPS (5.4), TVDN (4.67), and TimeMixer (5.67), I place Swin4TS around 5.0 — it has a cleaner contribution and stronger results than TVDN, but weaker experimental rigor than TimeMixer.

---

## Summary

This paper proposes Swin4TS, which adapts two core designs from the Swin Transformer — window-based attention and hierarchical representation — to long-term time series forecasting. The method achieves linear O(ML) complexity and supports both channel-dependence (CD) and channel-independence (CI) strategies. Experiments on 8 benchmark datasets show that Swin4TS variants achieve state-of-the-art or near-SOTA results across all datasets, with particularly strong gains on ILI (15.8% MSE improvement) and Traffic (10.3%).

## Strengths

- **Consistent SOTA performance across 8 benchmark datasets (Table 1):** Swin4TS variants achieve the best or second-best average MSE/MAE on every dataset evaluated. On ILI, Swin4TS/CD reaches 1.657 MSE vs. the previous best of 1.967 (PatchTST); on Traffic, Swin4TS/CI reaches 0.356 vs. 0.397. This is a broad and systematic empirical result.

- **Linear computational complexity O(ML) in both time and channel dimensions (Section 5, Table 4):** The paper formally derives O(ML) complexity for both Swin4TS/CI and Swin4TS/CD and measures 11.3 ms inference time on Electricity vs. 15.4 ms for PatchTST (O(ML²)) and 25.2 ms for Crossformer (O(ML²)). This is a concrete practical advantage.

- **Ablation confirms the contribution of shift-window attention and hierarchical design (Table 3):** Removing either component increases prediction error. On ETTm2, full Swin4TS/CD achieves 0.248 MSE; removing shift-window attention raises it to 0.253, and removing hierarchical design raises it to 0.262. Controlled evidence that both borrowed ViT components are effective.

- **Flexible adaptation to both CD and CI strategies:** The paper cleanly implements both variants and shows they complement each other — CD excels on ILI and ETT datasets, CI on Weather, Traffic, and Electricity. This dual-strategy coverage is a practical advantage over methods supporting only one (e.g., PatchTST is CI-only, Crossformer is CD-only).

## Weaknesses

### Fatal

None.

### Major

- **Lookback length asymmetry between Swin4TS and many baselines is not fully controlled.** Swin4TS uses L=512 (or L=108 for ILI) while several baselines (FEDformer, Autoformer, Crossformer, MICN, TimesNet, N-HiTS) were originally designed and tuned for L=96. The paper evaluates these baselines at L=96, 336, and 512 and selects the best result, which partially mitigates the concern. However, no ablation shows Swin4TS's performance at shorter lookbacks (e.g., L=96). Without this controlled comparison, the reported SOTA advantage cannot be fully attributed to architectural merit rather than input-length advantage. The paper's own appendix section (C.5, "Varying historical series length") indicates longer lookbacks benefit Swin4TS, which reinforces the need for this control. (See Section 4.1, lines 161-163.)

- **No variance or uncertainty reported for main results.** Table 1 reports all results as point estimates with no standard deviations, confidence intervals, or multi-seed runs. Many improvements over strong baselines are small (e.g., Swin4TS/CI 0.220 vs. PatchTST 0.224 on Weather; Swin4TS/CD 0.406 vs. Swin4TS/CI 0.411 on ETTh1). Without variance estimates, the reader cannot assess whether these differences are systematic or noise. The paper mentions a "Randomness test" in Appendix C.1, but the main paper's headline results lack the most basic uncertainty quantification. (See Table 1.)

- **Several strong baselines cited in the references are not included in the comparison.** The references include TSMixer (Ekambaram et al., 2023, cited as [Ekambaram et al., 2023]) and TiDE (Das et al., 2023, cited as [Das et al., 2023]), both of which have shown competitive results on these same benchmarks and are contemporaneous with the baselines that are included. Excluding them — especially TSMixer, which also achieves linear complexity — weakens the "state-of-the-art" claim. (See References, lines 292-293.)

### Minor

- **No ablation comparing BatchNorm vs. LayerNorm within Swin4TS.** The paper uses BatchNorm (Footnote 1, line 113), stating that it outperforms LayerNorm for time series Transformers, citing Zerweas et al. (2020). Most Transformer-based time series models use LayerNorm, yet Swin4TS provides no controlled experiment demonstrating that this choice is beneficial in its specific architecture or discussing potential interactions with window-based attention. An ablation would improve reproducibility confidence.

- **Table 1 contains an inconsistency in the asterisk notation.** The caption states "* suggests the use of CI strategy otherwise the CD strategy," but Swin4TS/CD* in Table 1 is marked with an asterisk despite using the CD strategy. In Table 2, the notation is consistent (Swin4TS/CD has no asterisk), suggesting a formatting error in Table 1. (See Table 1 caption, line 169; Table 1 header, line 171; Table 2 header, line 187.)

### Trivial

- **Complexity analysis (Table 4) does not specify hardware, batch size, or sequence length used for the timing measurements.** While the theoretical complexity derivation is clear, the empirical efficiency numbers lack the context needed for reproduction.

## Nice-to-Haves

- Show Swin4TS results with L=96 (matching the native setting of many baselines) to isolate architectural benefit from input-length advantage.
- Provide standard deviations over multiple random seeds for all main results.
- Compare against TSMixer and TiDE, which are already cited in the references.
- Include an ablation comparing Swin4TS with LayerNorm vs. BatchNorm to validate the normalization choice.
- Include a variant that replaces window attention with full self-attention (comparable parameter count) to isolate the benefit of the windowing mechanism itself.

## Removed Points

- **Criticism about the "Zerweas et al., 2020" reference being unrecognized:** Per review guidelines, questioning the existence of a cited reference is not permitted. The paper cites it; it exists. However, the point about the missing normalization ablation is retained as a Minor weakness.
- **Garbled text "The of Swin4TS with the CI strategy" (line 133):** This is a parser artifact, not an author error.
- **Missing hyperparameter details and appendix content:** The appendix is stripped by the parser; these details exist in the original submission.
- **Attention map visualizations described as "only qualitative":** Attention maps are by convention qualitative; this is not a weakness of the paper.
- **Claim that "the paper does not show whether L=512 is always optimal" for Swin4TS:** The paper explicitly references Appendix C.5 ("Varying historical series length") which addresses this. The appendix is stripped by the parser.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the central tension well: the paper's strongest claim — SOTA on 8 datasets — is supported by a broad and consistent evaluation, but the experimental design does not fully decouple the advantage of longer lookbacks from the advantage of the architecture itself. This is the single issue that would most strengthen the paper if addressed. The remaining criticisms (variance reporting, missing baselines, normalization ablation) are individually minor but collectively reduce confidence in the headline claims.

## Suggestions

1. Run Swin4TS with L=96 on all datasets and report results alongside the L=512 results. If Swin4TS at L=96 still outperforms or matches baselines at their preferred lookback, the architecture's advantage would be cleanly isolated.
2. Report standard deviations over at least 3 random seeds for all main results (Table 1 and Table 2). This is the single most impactful addition for judging the reliability of the reported improvements.
3. Add TSMixer and TiDE to the baseline comparisons. Both are already cited in the references and are widely recognized as competitive methods on these benchmarks.
4. Add a BatchNorm vs. LayerNorm ablation on at least one dataset (e.g., ETTm1 or Weather) to validate the normalization choice.
5. Fix the asterisk notation inconsistency in Table 1.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>