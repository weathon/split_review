## Summary

This paper introduces WaveFormer, a hierarchical transformer for 3D medical image segmentation that replaces the shifted-window mechanism with multi-level discrete wavelet transform (DWT) decomposition. Features are decomposed via DWT; the high-frequency (detail) coefficients are discarded, and window-based self-attention is applied to the multi-scale low-frequency approximation coefficients. This is intended to capture both local and global context within each layer while reducing computation. The method is evaluated on FLARE2021, AMOS2022, KiTS2019 (claimed), and ImageNet-1K.

## Strengths

- **Quantified computational-accuracy trade-off**: On FLARE2021, WaveFormer achieves 0.941 mean Dice with 326.56G FLOPs — roughly half the compute of 3D UX-Net (639.4G FLOPs) which achieves 0.934, demonstrating that DWT-based multi-resolution attention can improve accuracy while substantially reducing FLOPs (Section 6.1, lines 168–177).

- **Architectural distinction from shifted-window attention**: Figure 1 and the surrounding text (Section 1, lines 13–31) make clear that WaveFormer captures both fine-grained local and coarse global context within each layer via multi-level DWT, whereas Swin requires stacked shifted-window layers to expand the receptive field. This is a genuine structural architectural difference, not just a performance increment.

- **Principled motivation via Parseval's theorem**: The paper formally connects energy compaction in the wavelet domain (Equation 5, line 90) to empirical observations that ViT features concentrate energy in low frequencies, providing a theoretical basis for the design (Section 3.1, lines 79–95). This is stronger than a purely empirical architectural choice.

- **Systematic ablation over decomposition depths**: Four variants (1111, 2211, 3211, 3221) are tested on both FLARE and ImageNet-1K, and DWT is ablated against max pooling, showing that decomposition depth matters and that DWT is not interchangeable with simple downsampling (Section 6.4, lines 199–222).

- **Cross-domain generalization**: WaveFormer achieves competitive ImageNet-1K top-1 accuracy with ~22% fewer FLOPs than Swin Transformer (Section 6.3, line 195), showing the approach transfers beyond medical imaging to natural image classification.

## Weaknesses

### Fatal

None.

### Major

1. **Missing KiTS results despite explicit claims**: The abstract states the model was validated on "three challenging public datasets" including KiTS (line 4), and Contribution 3 (line 45) explicitly claims "superior mean dice scores on the FLARE, AMOS and KiTS test sets." The training setup (Section 5.2, line 152) mentions 5-fold cross-validation on KiTS. Yet the Results section (Section 6) contains no KiTS table, no KiTS Dice scores, and no KiTS analysis whatsoever. The paper therefore does not deliver on one of its stated core contributions. This is a significant empirical gap — either the results were omitted because they were uncompetitive (selective reporting) or the paper is incomplete. Either interpretation undermines the stated claims.

2. **Inconsistent FLARE Dice scores between abstract and results body**: The abstract (line 4) reports WaveFormer achieving "0.938 Dice" on FLARE2021, while the results text (line 177) reports "0.941 in Wavelet" for the same model on the same dataset. Both numbers are attributed to WaveFormer without explanation of the discrepancy. For a paper whose central evidence consists of small-margin improvements (~0.4–2.0 Dice points), exact numbers matter, and this inconsistency erodes trust in the reported results.

3. **No ablation of the discarded high-frequency coefficients**: The paper's core design choice is to discard all high-frequency (detail) coefficients (Figure 2 caption, line 99: "Low-energy-density HFCs are omitted in our network"). For dense prediction tasks like segmentation, where boundaries, edges, and fine anatomical structures are critical, the detail coefficients carry potentially valuable information. The paper provides no ablation comparing the full-DWT variant (including HFCs in some form) against the version that discards them. The future work section (line 231) acknowledges this as open, but without testing it, the claim that "essential" information is preserved is unsupported by evidence.

### Minor

4. **No variance reporting for primary results**: The paper mentions 5-fold cross-validation for FLARE and KiTS (line 152) and titles Table 4 "across all folds," yet no standard deviations, per-fold results, or confidence intervals are reported. The only statistical test is a Wilcoxon signed-rank symbol (p<0.01) in the AMOS table caption with no test statistic reported. Without variance, the reader cannot assess whether the reported small-margin improvements are stable or driven by a single favorable fold.

5. **DWT-vs-pooling ablation uses max pooling, not average pooling**: The ablation (Section 6.4, line 218) compares DWT against max pooling as a downsampling alternative. Since DWT's low-frequency approximation coefficients result from a low-pass (averaging) operation followed by subsampling, the appropriate baseline to isolate DWT-specific frequency-domain properties is average pooling. Max pooling is a non-linear operation that preserves maxima rather than smoothing. As designed, this comparison does not show whether DWT's orthogonality or energy compaction drive the improvement beyond what simple low-pass filtering provides.

6. **Underspecified architectural details**: The variable P in the input specification (line 119: "Random sub-volumes S_i ∈ ℝ^{H×W×D×P}") is never defined. The number of DWT scales m per stage is mentioned but not clearly specified for each stage independent of the variant naming convention. These omissions make precise reproduction harder.

7. **Unsupported claims about prior methods in related work**: Several critiques in Section 2 are asserted without evidence (e.g., "LinFormer sacrifices fine-grained detail," "Performer yields unreliable performance across tasks and modalities"). These weaken the literature positioning.

### Trivial

8. **Broken cross-references**: The text contains "Figure ??" references (lines 177, 184), indicating unresolved cross-references.

## Nice-to-Haves

- Adding average pooling as a DWT alternative in the ablation would strengthen the claim that DWT's specific properties drive improvements beyond standard low-pass filtering.
- Reporting per-organ Dice scores with standard deviations for the main results would substantially improve empirical rigor.
- Including a variant that retains high-frequency coefficients (e.g., via a separate lightweight CNN path) would test the sufficiency of the low-frequency-only design.

## Removed Points

These points are flagged to be removed; treat them with caution.
- **Criticism about missing code/availability**: Removed per hard rules — the paper states code will be available; questioning future artifact existence is not permitted.
- **Criticism about small improvement margins in isolation**: Merged into Weakness #4. Small margins are acceptable when variance is reported; the real problem is missing variance.
- **Criticism about abstract/body comparing different baselines (SwinUNETR vs 3D UX-Net)**: Removed — these are different rows in the table and the abstract and body can reference different comparison points. The genuine inconsistency is the WaveFormer score itself (0.938 vs 0.941), kept as Weakness #2.
- **Criticism about tables being unreadable images**: Removed per hard rules — parser artifacts are not author errors.
- **Generic strength ("this paper addressed an important problem")**: Removed as non-specific.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a tension between the paper's architectural novelty (DWT-based multi-scale attention is legitimately different from shifted-window approaches) and its incomplete empirical backing. The strongest observation is that the method's most distinctive design choice — discarding all high-frequency coefficients — is simultaneously the least tested one, and this gap should be addressed in any revision.

## Suggestions

1. **Add the missing KiTS results** — without them, the paper does not support its stated contributions.
2. **Resolve the FLARE Dice discrepancy** between abstract (0.938) and body (0.941), and clarify which number is correct under which condition.
3. **Ablate the role of high-frequency coefficients** by comparing the current design against a variant that retains HFCs (e.g., via a residual connection or lightweight parallel path).
4. **Replace max pooling with average pooling** in the downsampling ablation, or include both and discuss the comparison.
5. **Report variance** (standard deviations or inter-quartile ranges) across cross-validation folds for all main results.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>