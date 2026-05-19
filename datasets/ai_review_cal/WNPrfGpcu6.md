- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 5, 8, 6
Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper proposes FourierMamba, a framework that integrates Fourier transforms with Mamba (state space models) for image deraining. The key innovation is designing frequency-ordered scanning strategies (bilateral zigzag and progressive zigzag) for the spatial dimension of the Fourier space, and a direct 1D Mamba scan for the channel dimension, enabling ordered correlation of low-to-high frequencies. The method achieves state-of-the-art or competitive PSNR/SSIM across four benchmark datasets (Rain100H, Rain100L, Test2800, Test1200) with reasonable parameter efficiency (22.56 GFlops).

## Strengths

1. **State-of-the-art empirical performance**: Table 1 shows FourierMamba achieves the highest PSNR/SSIM on Rain100H (31.79/0.913), Rain100L (39.73/0.986), and Test1200 (34.76/0.938), outperforming 13 prior methods including recent Fourier-based (Fourmer) and Mamba-based (FreqMamba, VMambaIR) approaches. The gains on Test1200 (+1.40 PSNR over FreqMamba) and Rain100L (+0.55 PSNR over FreqMamba) are substantial.

2. **Principled adaptation of Mamba to Fourier-space structure**: The paper correctly identifies that frequency ordering differs between the spatial dimension (concentric circular arrangement) and channel dimension (linear along axis), and designs distinct scanning strategies for each. The bilateral zigzag and progressive zigzag scans in Sec. 3.2 are tailored to the central symmetry of the Fourier spectrum and the periodic nature of the transform.

3. **Systematic ablation evidence**: Tables 2-3 (ablation_block and scan tables) isolate each component's contribution. Removing spatial-dimension Fourier drops PSNR from 39.73 to 38.25 on Rain100L; removing the proposed scans in favor of the standard VMamba scan drops PSNR from 39.73 to 38.82. Each removal produces a clear degradation, confirming that all proposed components contribute meaningfully.

## Weaknesses

### Fatal
None.

### Major

1. **Insufficiently precise specification of the core scanning method**: The bilateral zigzag and progressive zigzag scans — which are the paper's central technical contribution — are described only conceptually in Sec. 3.2. The paper states they "start from the vertex of the highest frequency on one side of the spectrum, progressing in a zigzag pattern toward the center's low frequencies; similarly, it then zigzags to the opposite side's highest frequency," and that they scan "half of the spectrum" due to symmetry. However, no pseudocode, coordinate mapping from 2D $(u,v)$ positions to 1D sequence indices, or algorithmic listing is provided. Since Mamba's SSM is inherently 1D and causal, the ordering of tokens is critical to reproducibility. While zigzag coding is a familiar concept from JPEG, the specific adaptation to the Fourier spectrum's concentric and symmetric structure (including how the "bilateral" and "progressive" variants differ in coordinate order) needs a precise specification for the work to be built upon.

### Minor

1. **Imprecise positioning relative to Fourier-attention methods**: The paper claims that "previous Fourier-based methods rarely utilize the correlation of different frequencies" (abstract) and that "the commonly used 1×1 convolutions cannot correlate different frequencies" (Section 1). However, the paper itself cites Fourmer (ICML'23), which applies **self-attention in the Fourier domain** — an operation that explicitly correlates across frequency positions. The paper should acknowledge this and reframe its motivation as arguing for the advantages of *ordered scanning* (linear complexity, natural low-to-high ordering) over *attention-based correlation* (quadratic complexity, no built-in ordering). This does not invalidate the contribution but weakens the motivation as written.

2. **No variance or statistical significance reporting**: All quantitative results in Table 1 are reported as single numbers without standard deviations or confidence intervals. Given that some improvements are small (e.g., Rain100H: 31.79 vs 31.74 for FreqMamba), it is unclear whether these differences are statistically significant.

3. **No quantitative evaluation on real-world rain datasets**: The figures after the conclusion provide qualitative results on RainDS-Real, SPA-Data, and RE-RAIN, but the paper lacks a quantitative evaluation (PSNR/SSIM on real-world test sets with ground truth). This limits the strength of the claim that the method generalizes beyond synthetic benchmarks.

4. **Under-analyzed channel-dimension Fourier component**: The rationale for why channel-dimension Fourier transform is preferable to standard channel attention mechanisms (e.g., SE, ECA) is not provided. The FCE-SSM module (Sec. 3.2.2) is described but not compared against a simple gated-channel-attention baseline with comparable parameters.

5. **Weak argument against the Euclidean-distance baseline**: The paper dismisses the intuitive Euclidean-distance-based approach as "impractical" because it requires recalculating distances for each image size (Sec. 3.2). This is a trivial O(HW) precomputation. The *real* limitation is that Euclidean distance groups points into concentric rings without fully ordering within each ring — the paper should make this argument instead.

6. **Unclear whether baselines are retrained or numbers from original papers**: The comparison table uses results from original papers for some methods. While standard practice in this field, the paper should explicitly state the protocol (which numbers are from original publications vs. retrained under a unified setting) to avoid potential unfairness from different training setups.

7. **Loss weight not ablated**: The Fourier loss weight $\lambda = 0.02$ is set empirically (Sec. 3.3) but no sensitivity analysis is provided.

### Trivial

1. **Typo in Table 1**: The table header reads "PNSR" instead of "PSNR" (once; the rest of the paper uses PSNR correctly).
2. **Grammatical issue in abstract**: "despite there exists dependency" should be restructured.
3. **Minor formatting**: The figures after the conclusion (lines 311–351) appear to be supplementary material placed in the main body, including a figure captioned "Correction of the second picture in Figure 5." These should be moved to a proper supplementary section or integrated earlier.

## Nice-to-Haves

- **Provide pseudocode or a coordinate-mapping algorithm** for the bilateral and progressive zigzag scans. This would directly address the major reproducibility concern.
- **Add a baseline that replaces the Fourier-space Mamba scan with a self-attention layer** (comparable FLOPs) on the Fourier spectrum. This would isolate whether the benefit comes from Mamba's linear complexity, the low-to-high ordering, or the architecture itself, and would directly address the missing comparison with Fourmer.
- **Ablate the FCE-SSM against a standard channel-attention mechanism** (e.g., SENet-style gating) with comparable parameters to demonstrate the specific value of the Fourier channel transform.
- **Ablate the Fourier loss weight $\lambda$** over a small range (e.g., 0.0, 0.01, 0.02, 0.05) to show sensitivity.

## Removed Points

These points are flagged for removal; treat them with caution:

1. **"Figures after conclusion are formatting artifacts"** — The harsh critic notes that multiple minipage figures appear after the conclusion with titles like "Correction of the second picture in Figure 5" and suggests this reflects a disorganized layout. However, this is a parser artifact from PDF extraction; the original submission likely has these in a proper supplementary section. Removed per the rule that formatting artifacts from parsing are not author errors.

2. **"Classic scan is a strawman baseline"** — The harsh critic suggests the "Classic" scan ablation (VMamba scan applied to Fourier features) should be clarified as not a strawman. Looking at the paper, the Classic scan achieves 38.82 PSNR vs the proposed 39.73 — this is a reasonable and informative baseline comparison, not a strawman. The critic's suggestion to add a self-attention baseline is valid but moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The two reviews are consistent in their overall assessment: the method is empirically strong and the core idea is sound, but the scanning description is too vague for reproducibility and the positioning relative to prior Fourier-attention work needs sharpening. A genuinely novel insight that emerges from combining the reviews is that the paper would be substantially strengthened by a simple complexity comparison (inference GFlops) between its scanning-based frequency correlation and Fourmer's attention-based frequency correlation — the paper already reports GFlops for both (22.56 vs 16.75), which would make the efficiency argument concrete if discussed.

## Suggestions

1. **Provide a precise algorithmic specification** of the bilateral and progressive zigzag scans: either pseudocode or a coordinate-to-index mapping formula. This is essential since the scanning strategy is the paper's core technical contribution.
2. **Reframe the motivation** to acknowledge that Fourmer uses self-attention for frequency correlation, then argue why scanning (ordered low-to-high, linear complexity) is preferable — rather than implying prior work does not correlate frequencies at all.
3. **Add variance reporting** (e.g., mean ± std over 3 runs) for at least the main benchmark results.
4. **Add a quantitative real-world evaluation** on available datasets (e.g., RainDS, SPA) with ground truth, or note the absence as a limitation.
5. **Fix the "PNSR" typo** in Table 1 and the grammatical issue in the abstract.
6. **Clarify the training protocol**: explicitly state whether all baselines were retrained under the same protocol or whether numbers are taken from original publications.
