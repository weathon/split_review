Now I have strong calibration. Let me finalize my review.

**Round-1 bracket:** The paper is clearly above the weak band (3.0-4.8, e.g., MambaVC at 4.80 which was rejected for having limited compression-specific novelty and weak baselines). CMIC has genuine compression-specific innovations (CTP, GPP), compares against 15 SOTA baselines, and has strong ablation/ERF analysis. It is below the strong band (7.5-8.0 diffusion/weather models). So the bracket is roughly **5.5–7.0**.

**Round-2 narrowing:** FTIC (6.00, Accept) — frequency-aware transformer block for LIC, accepted, similar contribution type. CMIC has more thorough ablations (Tables 2,4–6), more baselines (15 vs fewer), better efficiency analysis, and compelling ERF visualizations. Spatial-Mamba (7.00, Accept) — general-purpose Mamba backbone, slightly broader impact. CMIC is stronger than FTIC but not as broadly applicable as Spatial-Mamba. **Final score: 6.5.**

Now let me produce the final consolidated review.

Here are my filtering decisions:

**Harsh Critic Filtering:**
- Point 1 (non-causality framing): The paper consistently uses "mitigates" and "relaxes," not "solves." The mechanism is clearly presented in Section 3.4 with Eq. O_i = (C+P_i)h_i + Dx_i. The ERF visualizations confirm the effect. This is a minor communication nitpick at most — REMOVE from weaknesses (doesn't rise to any tier).
- Point 2 (MS-SSIM underreported): Valid. The paper mentions MS-SSIM gains against only 2 baselines without a full table. KEEP as minor weakness.
- Point 3 (baseline training data not controlled): Valid but standard practice in LIC. KEEP as minor weakness.
- Training hyperparameters: Valid minor point. KEEP as minor.
- No error bars: Standard practice. Move to nice-to-have.
- BD-PSNR mentioned in text: Minor, but doesn't really hurt the paper.

**Strength Finder Filtering:**
- All listed strengths are concrete and evidence-backed. KEEP all.

Let me write the final review.## Summary

This paper introduces Content-Aware Mamba (CAM) for learned image compression, addressing two limitations of standard Mamba SSMs: content-agnostic fixed scans and strict causality. CAM proposes (1) Content-Adaptive Token Permutation (CTP) — reordering tokens by feature-space proximity via codebook-based clustering — and (2) Global-Prior Prompting (GPP) — injecting sample-specific global priors into the SSM output matrix to relax causality without multi-directional scanning. The full CMIC model achieves strong BD-rate savings over VTM-21.0 (15.91%, 21.34%, 17.58% on Kodak, Tecnick, CLIC) with favorable complexity (69M params, 2.39 TFLOPs, 4.44 GB peak memory).

## Strengths

- **Content-adaptive token permutation demonstrably improves over fixed-scan Mamba baselines.** Table 2 shows CTP alone yields 2.0–2.4% BD-rate improvement. Fig. 9(d/e) provides direct visual evidence that CTP breaks the raster-scan pattern, spreading activation over semantically related locations rather than spatial neighbors. This is a compression-specific innovation that goes beyond straightforward application of Mamba.

- **Global-prior prompting relaxes strict causality without the 4× computational overhead of multi-directional scanning.** GPP achieves non-causal behavior (confirmed by Fig. 9(c) showing non-zero activations beyond the causal boundary) while keeping memory at 4.44 GB vs. MambaIC's 20.32 GB on 2K images, and FLOPs at 2.39T vs. MambaIC's 5.56T.

- **State-of-the-art RD performance with thorough baseline comparison.** Table 1 covers 15 baselines. CMIC leads on Tecnick (−21.34%) and CLIC (−17.58%), and is near the top on Kodak (−15.91%, competitive with MLICv2 at −16.16% and DCAE at −15.40%). Against prior Mamba-based models (MambaVC, MambaIC), gains are substantial (2.2–10.1% BD-rate).

- **Favorable complexity-performance trade-off.** CMIC (69.11M params, 2.39 TFLOPs) outperforms the much larger MLIC++ (116.48M params) and substantially reduces FLOPs (−36%), latency (−25%), and peak memory (−43%) vs. TCM-L. Throughput overhead from CTP+GPP is minimal (23.19 → 22.05 samples/s, ~5%).

- **ERF visualizations provide unusually strong interpretability evidence.** Figs. 7–9 systematically isolate the individual and joint effects of CTP and GPP, showing progression from strict raster-scan causality to global, content-adaptive coverage. This is a higher bar of evidence than most LIC papers meet. Cluster visualizations (Fig. 10) confirm semantically meaningful groupings.

- **Clean ablation study design.** Table 2 isolates CTP (~2% BD-rate) and GPP (~1%) contributions with additive gains. Table 4 compares CAM against Conv, 2D Mamba, Attention-only, and CAM-only variants. Table 5–6 analyze clustering behavior (mean 23.27 of 64 centroids active, varying per image) and K sensitivity.

## Weaknesses

### Major
None.

### Minor

1. **MS-SSIM evaluation is underreported.** The paper states λ values {3,5,8,16,32,64} for MS-SSIM optimization and claims gains of −7.34% (vs. TCM-L) and −3.87% (vs. FTIC), but provides no full BD-rate table comparable to Table 1 for the MS-SSIM-trained model. Table 1 is MSE-only. Without a complete MS-SSIM comparison, the claim of SOTA across metrics is not fully verifiable from the main paper. The paper acknowledges that MambaVC and MambaIC are MSE-only, but other baselines (ELIC, TCM, MLIC++, FTIC) commonly report MS-SSIM in their original papers.

2. **Baseline training data is not controlled.** CMIC is trained on Flickr2W (20K images), while baseline numbers are taken from published papers that use varying training data (e.g., ImageNet subsets, DIV2K). This standard but unacknowledged practice introduces uncertainty into absolute BD-rate comparisons — some fraction of the reported advantage could stem from training data differences rather than architectural innovation. The ablation and ERF experiments partially compensate by confirming component-level benefits, but the absolute comparisons are affected.

3. **Training hyperparameters are incomplete for full reproducibility.** The paper reports initial learning rate (10⁻⁴), optimizer (Adam), λ schedules, and architecture details (channel dimensions, block counts, K=64, window size 8), but omits batch size, total training steps/epochs, and learning rate schedule.

### Trivial
None.

## Nice-to-Haves

- A full MS-SSIM BD-rate table comparable to Table 1 would close the evaluation gap.
- Bootstrap-based error bars or multi-seed variance for BD-rate numbers, though not standard in LIC, would strengthen the quantitative claims.
- One or two failure-case cluster visualizations (where centroids poorly match feature distribution) would demonstrate awareness of the method's limitations.

## Removed Points

- **"Non-causality" framing imprecision (Harsh Critic Point 1).** The paper consistently uses "mitigates" and "relaxes" (not "solves") regarding causality. Section 3.4 clearly presents the mechanism (adding prompt P to matrix C in the output equation, not modifying the recurrence). The ERF in Fig. 9 confirms the intended effect. Removed: the criticism is accurate in detail but does not reflect an actual flaw in the paper — the paper's language is precise enough given the mechanism description.

- **No error bars on RD results.** Standard practice across LIC literature; requesting this for the main table exceeds the field's norms. Moved to nice-to-have.

- **BD-PSNR mentioned in text only.** Minor presentation preference; does not obscure the results since BD-rate is the primary metric.

- **λ schedule justification for MS-SSIM.** These values are consistent with prior LIC work. Removed as not a genuine weakness.

- All generic/formulaic strengths from Strength Finder that lacked concrete evidence anchors were filtered. Kept only evidence-backed strengths.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a full MS-SSIM BD-rate table (comparable to Table 1) in the main paper or appendix, covering at least the strongest MSE-trained baselines that also report MS-SSIM. This is the single most actionable improvement.
2. Explicitly acknowledge the training data discrepancy when comparing against baselines trained on different datasets, and discuss the potential impact of this factor.
3. Report batch size, total training steps, and learning rate schedule for reproducibility.

## Score and Decision

**Calibration anchors used (all rounds):**

| Path | Avg Score | Round | Comparison to CMIC |
|------|-----------|-------|-------------------|
| RmmrHEH6Nx (GroupMamba) | 3.00 | 1 (weak) | Much weaker — limited novelty, copied SE block, unfair distillation comparison. CMIC has genuine novel contributions. |
| VtP7CamOR5 (Mamba Neural Operator) | 3.00 | 1 (weak) | Much weaker — typos, weak baselines, unclear significance. |
| KgJwbsfN7G (MambaVC) | 4.80 | 1 (weak), 2 (narrow) | Weaker — limited compression-specific novelty (just applied VSS blocks), weak baselines (only ConvVC/SwinVC), no MS-SSIM evaluation. CMIC has two compression-specific innovations and 15 SOTA baselines. |
| XKQ2qzajbU (GlobalMamba) | 5.00 | 2 (narrow) | Weaker — global image serialization via DCT with moderate results. CMIC has stronger empirical results and more thorough analysis. |
| PQpvhUrA1C (Autoregressive Pretraining Mamba) | 5.75 | 2 (narrow) | Comparable lower bound — different domain (ImageNet classification pretraining). CMIC's compression-specific contributions are more tailored. |
| HKGQDDTuvZ (FTIC / Frequency-Aware Transformer) | 6.00 | 2 (narrow) | Comparable — both propose novel blocks for LIC with SOTA results. CMIC has more thorough ablations (Tables 2,4–6), more baselines (15 vs fewer), better efficiency analysis, and ERF visualizations. CMIC is slightly stronger. |
| iDe1mtxqK5 (Spatial-Mamba) | 7.00 | 1 (middle) | Stronger upper bound — general-purpose vision Mamba backbone with broader applicability. CMIC is comparable in paper quality but narrower in scope. |

**Round 1 bracket:** [5.5, 7.0] — clearly above MambaVC (4.80) due to genuine compression-specific innovations, strong baselines, and thorough analysis; below general-purpose vision Mamba papers like Spatial-Mamba (7.00) which have broader impact.

**Round 2 narrowing:** CMIC is somewhat stronger than FTIC (6.00) — better ablations, more baselines, stronger ERF analysis. It is not as broadly impactful as Spatial-Mamba (7.00). Score of 6.5 reflects this placement.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>