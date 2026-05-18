Now I have a thorough understanding of the paper and the reviews. Let me produce the final consolidated review.

## Summary

This paper proposes STREAM, a video evaluation metric that separately assesses spatial quality (fidelity and diversity via STREAM-F/STREAM-D) and temporal naturalness (STREAM-T). The spatial component adapts improved Precision & Recall using the per-frame mean FFT amplitude (frequency zero) as a video-level representation. The temporal component applies FFT along the temporal axis of per-frame image embeddings, fits a power-law distribution to the frequency amplitudes per feature dimension, computes the skewness of that distribution, and compares histograms of these skewness values across dimensions between real and fake videos. The paper validates STREAM on synthetic (CATER) and real (UCF-101, Kinetics-600) data, demonstrating that STREAM-T and STREAM-S respond independently to spatial vs. temporal distortions, that STREAM provides diagnostic insights beyond FVD's single score, and that it handles videos of arbitrary length.

## Strengths

- **First metric to separately assess spatial and temporal video quality in a unified framework**: The paper provides clear experimental evidence that STREAM-T and STREAM-S respond independently to spatial vs. temporal degradation. In Figure 2 (visual noise), STREAM-T remains stable near 1.0 while STREAM-S decreases proportionally. In Figure 3 (temporal swap), STREAM-T detects both local and global swaps while STREAM-S only responds to global swap (which affects diversity). This separation is validated across controlled toy data (CATER) and real datasets (UCF-101, Kinetics-600) — a rigorous empirical foundation.

- **Bounded, length-agnostic scores**: STREAM values are constrained to [0,1] and interpretable regardless of video length. The paper demonstrates evaluation on 128-frame videos (Table 2) without architectural modification, unlike FVD which requires a sliding-window adaptation (sFVD). This directly supports the universal applicability claim.

- **Diagnostic insights beyond FVD**: Table 1 reveals that TATS has high STREAM-F (0.9120) but low STREAM-D (0.0850), indicating high per-frame fidelity but poor diversity — a granular diagnosis not provided by FVD's single score (693.27). This is reinforced by reported Spearman correlations against human judgment (0.9 for realism, 0.6 for temporal naturalness), supporting the claim that STREAM offers actionable diagnostic information.

- **Rigorous experimental design with controlled toy data**: The paper uses the CATER synthetic dataset for controlled experiments where ground-truth degradation is known, systematically testing four types of spatial noise and three types of temporal distortion. This "calibration" approach — testing whether the metric behaves as expected when the type of degradation is known — is a strength that most video metric papers lack.

## Weaknesses

### Fatal

None.

### Major

- **The skewness formula in the main text is presented unclearly and appears inconsistent with standard definitions**: In §3.3 (lines 69–72), the paper defines skewness as $\gamma = E[(X-\mu)^3]/\Sigma^3$ where "$\Sigma$ is the variance," which would make the denominator $(\sigma^2)^3 = \sigma^6$ — inconsistent with the standard definition $\gamma = E[(X-\mu)^3]/\sigma^3$. The resulting formula $\frac{\sqrt{K}\sum_\zeta \zeta^{(3-\alpha)}}{\sqrt{C\sum_\zeta \zeta^{(2-\alpha)}}}$ does not obviously follow from either the definition or standard skewness of a discrete distribution, and mixes raw moments with normalization constants in a way that is not transparent. **However**, the paper explicitly states that the full derivation uses Moment Generating Functions and is provided in the appendix (\Aref{sec:moment_generating_function}), which is stripped by the parser. This is therefore a **presentation gap in the main text** rather than necessarily a mathematical error — but it means the core mathematical foundation of STREAM-T cannot be assessed from the main paper alone. The authors must either correct the formula or add enough derivation steps in the main text for the reader to verify it.

- **The claim that FVD "predominantly focuses on spatial attributes" is incompletely supported**: The paper argues FVD is biased toward spatial quality because experiments show larger absolute FVD changes for spatial distortions (e.g., 3-pixel random translation) than for temporal ones (80% stop scenes). But FVD is an unbounded Wasserstein distance — its absolute values are not directly comparable across different types of distortion. The larger response to translation could simply reflect that I3D features are highly sensitive to pixel shifts (even perceptually minor ones), not that FVD "focuses on" spatial quality. The paper does not control for the scale of feature-space response across perturbation types. This weakens the motivation for why a new metric was necessary, though the separable evaluation paradigm remains independently valuable.

### Minor

- **No sensitivity analysis for the k-NN parameter in STREAM-S**: The spatial component uses $k=5$ (line 140) without reporting how STREAM-F and STREAM-D vary with $k$. For image P&R, the choice of $k$ is known to affect results. A simple ablation on at least one controlled experiment would substantially strengthen the spatial component's robustness.

- **No baseline comparison with simpler temporal metrics**: The paper does not compare STREAM-T to simple baselines like average frame-to-frame cosine similarity, LPIPS, or SSIM over time, or mean frame difference statistics. Such comparisons would clarify whether the FFT + power-law + skewness pipeline adds value over straightforward autocorrelation-type measures for temporal evaluation.

- **Image embedding dependency not ablated**: The paper uses Caron et al. (2020) as the image embedding network but does not test alternative image embeddings (e.g., CLIP, ResNet-50, DINO) or compare with video embeddings adapted for the STREAM framework. The choice matters because image-level features' sensitivity to motion (vs. appearance change) is unknown, especially for natural videos with camera motion and partial occlusions.

- **Long-video scores lack a real-video reference baseline**: Table 2 shows dramatic STREAM-T drops for TATS (0.9832→0.0302) and MoCoGAN (0.9683→0.3274) at 128 frames. But the paper does not report STREAM-T on real long videos (e.g., 128-frame Kinetics clips), making these scores difficult to calibrate. A real-video baseline would clarify whether STREAM-T appropriately penalizes long generated videos or whether it becomes overly strict for long sequences in general.

- **"First" claim should be more carefully scoped**: The paper states "STREAM is the first evaluation metric that can separately assess the temporal and spatial aspects of videos." While the claim is qualified ("to the best of our knowledge" in the abstract), it invites unnecessary skepticism. Framing the contribution around what STREAM *enables* (bounded, length-agnostic, decomposed scores) rather than an exclusivity claim would better reflect the paper's actual value without risking debate about prior art.

### Trivial

- The skewness definition in §3.3 uses notation "Var(ζ)³" where the exponent on variance is ambiguous — standard notation would use $\sigma^3$ or $\text{Var}(\zeta)^{3/2}$.

## Nice-to-Haves

- A small controlled experiment showing that STREAM-T's skewness-distribution comparison captures temporal naturalness specifically (e.g., comparing real videos, temporally shuffled videos, and videos with swapped frames) to demonstrate that the statistic tracks temporal coherence rather than any distributional difference.
- Ablation of DINO vs. SwAV vs. CLIP vs. ResNet as embedding networks to test sensitivity.
- Real long-video STREAM-T scores for calibration of Table 2 results.

## Removed Points

- **"The histogram-correlation method lacks a principled justification" (Harsh Critic, 1b)**: This is not a genuine weakness. Computing a per-sample statistic (skewness of frequency spectrum), building histograms of that statistic across samples, and comparing distributions via correlation is a standard approach (analogous to how FVD compares feature distributions, or how P&R compares manifold support). The statistic itself — skewness of the Fourier amplitude distribution — is specifically designed to capture temporal frequency structure. The claim that the method could "respond to other properties" applies to any distributional comparison metric and is not a specific failure of STREAM-T. The paper's logic is clear: temporal structure → frequency spectrum → skewness of spectrum → compare skewness distributions → temporal similarity score.

- **"The boundedness is not a decisive advantage" (Harsh Critic, Other)**: This is an opinion, not a weakness of the paper. Boundedness is a practical benefit for interpretability that the paper legitimately lists as an advantage.

- **"The human correlation study is referenced to the appendix" (Harsh Critic, Missing Parts)**: The main text (line 207) already reports the key numbers (0.9 for realism, 0.6 for temporal naturalness) and references the appendix for details. The rules prohibit penalizing papers for appendix-deferred content. The method and key results are stated in the main paper.

- **Criticism that the paper uses "DINO" specifically**: The paper actually cites Caron et al. (2020) — this is SwAV, not DINO (which is Caron et al. 2021). However, the broader concern about image embedding dependency is valid and kept as Minor.

- **Any formatting/style/typo complaints**: Removed per rules.

## Novel Insights

The reviews surface an interesting tension: the harsh critic demands a full mathematical derivation in the main text for the temporal metric, while the empirical validation (toy data controls + real data + human correlation) is actually quite thorough. This reflects a broader question in metric papers: should the mathematical derivation of a Perceptual metric be airtight before experimentation, or is empirical calibration (the metric "behaves as expected" across multiple controlled distortions) sufficient validation? The paper leans heavily on the latter approach, which is defensible — many widely used metrics (e.g., FID, IS, P&R) were validated primarily through empirical correlation with human judgment rather than a priori derivation from a model of "naturalness." The paper could strengthen its position by explicitly arguing for this empirical-validation epistemology.

## Suggestions

1. **Clean up the skewness presentation in §3.3**: Either provide enough derivation steps in the main text to make the formula follow clearly, or explicitly state that the formula is a simplified/approximate version and direct readers to the appendix. Use standard skewness notation ($\gamma = E[(X-\mu)^3]/\sigma^3$ where $\sigma$ is standard deviation) and show how the power-law distribution's parameters lead to the expression.

2. **Add a simple temporal baseline**: Compare STREAM-T to frame-wise cosine similarity or LPIPS-over-time on at least the swap/toy experiments. This would directly show the value of the FFT-based approach.

3. **Add k-NN sensitivity analysis**: Report STREAM-F/D for several $k$ values (e.g., 3, 5, 7, 10) on the noise degradation experiment or GAN comparison.

4. **Add real long-video baseline**: Report STREAM-T for real 128-frame videos (from Kinetics-600 or similar) to calibrate the long-video results in Table 2.

5. **Soften the "first" claim or better scope it**: The contribution stands on its own without the exclusivity framing, which only invites unnecessary debate.

6. **Reconsider the FVD bias argument**: Either add evidence that controls for the scale of feature-space response across perturbation types, or reframe the motivation around what STREAM *offers* (decomposable scores, boundedness, length-agnostic evaluation) rather than what FVD *fails* at.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>