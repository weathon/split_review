Now I have all the information I need. Let me compose the consolidated review.

## Summary

This paper proposes STREAM, a video evaluation metric that separately assesses spatial quality (STREAM-S, decomposed into fidelity STREAM-F and diversity STREAM-D) and temporal naturalness (STREAM-T). It uses a per-frame image embedding network (DINO) to extract frame features, applies FFT along the temporal axis, uses the DC component (mean amplitude) for spatial evaluation via improved Precision & Recall, and models the AC components via power-law distributions whose skewness histograms are compared between real and generated datasets. Experiments on CATER, UCF-101, and Kinetics-600 with both synthetic distortions and real generative models (MoCoGAN-HD, DIGAN, TATS, VideoGPT, MeBT, PVDM) demonstrate that STREAM responds selectively to its intended degradation type while FVD conflates spatial and temporal factors.

## Strengths

- **Independent evaluation of spatial and temporal video quality.** The controlled experiments (Figures 2–4, 5–6) convincingly show that STREAM-T remains flat across visual noise while STREAM-S decreases monotonically, and vice versa for temporal distortions. This directly supports the paper's core claim and is the metric's primary differentiating value.

- **Length-agnostic and bounded evaluation.** By using a per-frame image embedding network, STREAM handles any number of frames without architectural modification — demonstrated on both 16-frame (Table 1) and 128-frame (Table 2) videos — whereas FVD requires a sliding-window adaptation. STREAM's bounded [0,1] range is a practical advantage over FVD's unbounded scores.

- **Actionable diagnostic insights.** STREAM reveals that TATS achieves high fidelity (STREAM-F=0.912) but very low diversity (STREAM-D=0.085), while VideoGPT has more balanced but lower fidelity — insights not available from a single FVD score. The paper reports Spearman correlations of 0.9 (realism) and 0.6 (temporal coherence) against human judgments (details deferred to appendix).

- **Rigorous controlled-experiment design.** The paper tests visual noise (luminance, Gaussian, salt-and-pepper, color jitter), temporal swaps (local/global), random translation, and stop scenes on both CATER (controlled) and UCF-101/Kinetics-600 (real-world) datasets, providing a comprehensive validation suite that goes well beyond what prior metric papers typically offer.

- **Explicit demonstration of FVD's limitations.** Figures 2–6 quantitatively show that FVD is more sensitive to spatial than temporal degradation (e.g., FVD reaching ~822 under random translation but responding less to stop scenes), and that FVD's response varies unpredictably with noise type — strengthening the case for STREAM as a more principled alternative.

## Weaknesses

### Fatal
None.

### Major

- **Ceiling effect concern for short-video evaluation (16-frame setting).** In Table 1, all six generative models obtain STREAM-T scores between 0.9616 and 0.9843 — a narrow range near the maximum. The paper attributes this to all models "maintain[ing] reasonable consideration for temporal flow in generating short videos," and the toy experiments (Figures 3–4) do show that STREAM-T can detect graded temporal distortions (frame swaps, stop scenes). However, without a deliberately poor temporal baseline (e.g., randomly shuffled frames or a still-frame generator) tested under the same short-video protocol, it is difficult to determine whether the metric's narrow range reflects genuine similarity among models or a ceiling effect that limits discriminative power for realistic short-video artifacts. This directly affects the metric's practical utility for the most common evaluation setting.

### Minor

- **Methodological justification for skewness is incomplete.** The paper explains that mean/variance of Fourier amplitudes are biased by the 1/f phenomenon, motivating the use of skewness instead. However, it does not compare against simpler alternatives such as directly comparing the fitted power-law exponent α (which directly captures temporal dynamics), nor does it ablate the choice of skewness versus other higher-order statistics. The skewness definition on line 69 states γ = E[(X-μ)³]/Σ³ where "Σ is the variance" — standard skewness is μ₃/σ³ = μ₃/(variance)^(3/2), not μ₃/(variance)³. While the actual computed formula in Equation 71 may resolve this (derivation deferred to the MGF appendix), the notation as presented is potentially inconsistent and confusing without the appendix.

- **Missing standard deviations in long-video evaluation (Table 2).** Table 1 includes standard deviations from five repeated measurements, but Table 2 (128-frame videos) reports only point estimates. Variability information is needed to assess whether the dramatic drops in STREAM-T (e.g., TATS from 0.9832→0.0302) are statistically robust.

- **Incomplete specification of sliding-window baselines (sFVD, sVIS).** The paper states these are measured "for every 16 frames using a sliding window" but does not specify the stride. This omission hinders exact reproduction of the comparison.

### Trivial
None.

## Nice-to-Haves

- A deliberately poor temporal baseline (e.g., frame-shuffled videos or a static-frame generator) for 16-frame evaluation would fully address the ceiling-effect concern.
- An ablation comparing STREAM-T's skewness-based approach against simpler alternatives (e.g., comparing α directly, or a KS test on the amplitude spectrum) would strengthen the methodological grounding.
- Runtime comparison with FVD would help practitioners assess the practical overhead of the power-law fitting per feature dimension.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticism about human evaluation details being absent from the main text (Critic's Point 2).** The paper states "see \Aref{sec:human_judgement_study} for further details" — the appendix exists in the original submission and was stripped by the parser. Per guidelines, absence of appendix content is not a valid weakness.
- **Criticism about related works being thin (Critic's Section 4 note).** Per guidelines, missing-related-works criticisms cannot be verified and should not be included.
- **Criticism questioning whether the DINO embedding captures motion patterns.** The paper explicitly justifies using an image embedding network to avoid the spatio-temporal mixing of video encoders and to enable length-agnostic evaluation — this is a deliberate design choice, not an oversight.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a deliberately low-quality temporal baseline (shuffled frames, static video) to Table 1 to demonstrate that STREAM-T does not saturate for short videos. Show that the metric can distinguish real videos from a trivially bad temporal baseline even at 16 frames.
2. Clarify the skewness definition: either correct the denominator notation (Σ³ → Σ^(3/2) or equivalently σ³) or show explicitly how the MGF derivation yields the standard skewness formula.
3. Add standard deviations to Table 2, and specify the stride used for the sFVD/sVIS sliding window.
4. Consider including an ablation that compares the skewness-based approach to directly comparing the power-law exponent α across real and generated distributions, to justify the additional complexity.

## Score and Decision

The paper proposes a conceptually clean and practically useful video evaluation framework that demonstrably separates spatial and temporal quality — a genuine gap in current metrics. The controlled experiments are thoughtfully designed and generally support the claims. The main weakness is the narrow STREAM-T range on short videos, which raises appropriate questions about the metric's discriminative power in the standard 16-frame setting, though the toy experiments partially mitigate this concern. This is addressable with a simple additional baseline experiment and does not invalidate the core contribution, particularly since the metric's value for long-video evaluation (where it shows dramatically wider dynamic range) is clearly demonstrated.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>