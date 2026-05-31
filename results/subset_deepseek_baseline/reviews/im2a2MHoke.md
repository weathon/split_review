## Summary
This paper proposes RisoTTo, a non-autoregressive zero-shot TTS system that aims to close the performance gap with autoregressive models through three key innovations: (1) Soft Alignment Generation (SAG) using flow matching to distill attention-like soft alignments into NAR models, (2) an Invertible Encoder based on normalizing flow to disentangle residual acoustic information from semantic representations, and (3) Prompt-Aware Lightweight Convolution (PAL) for speaker-adaptive feature extraction. The model achieves competitive performance with autoregressive baselines while maintaining significantly lower latency and parameter count.

## Strengths
- **Novel combination of techniques**: The paper creatively combines flow matching for alignment generation, normalizing flows for residual modeling, and adaptive convolution for speaker adaptation—each addressing a specific limitation of NAR TTS. The theoretical motivation for using mutual information minimization to disentangle residual information is well-grounded.
- **Strong empirical results with practical advantages**: RisoTTo achieves competitive MOS, SECS, and WER scores against strong baselines including autoregressive models (VALL-E, T5-TTS) while using only 33M parameters (7-30x smaller than competitors) and achieving 0.89s latency for 10-second speech (4-7x faster). This practical efficiency is a genuine contribution.
- **Comprehensive ablation studies**: The paper systematically evaluates each proposed component (SAG, IE, PAL) and provides clear evidence of their individual contributions. The MMD analysis for the invertible encoder versus VAE is particularly insightful, demonstrating better disentanglement and avoidance of posterior collapse.

## Weaknesses

### Major
- **Limited evaluation scope and potential cherry-picking**: The main comparison (Table 4) mixes results from official demo pages (VALL-E, T5-TTS, NaturalSpeech2) with locally-run models (Spark-TTS, MaskGCT, F5-TTS). This introduces uncontrolled variables—different test conditions, vocoders, and preprocessing pipelines. The paper only evaluates on VCTK and Seed-TTS test sets, which is relatively narrow for claiming general superiority. Additionally, the ablation study (Table 5) uses only 50 samples from 10 speakers, which is too small for reliable conclusions.

- **Missing critical baselines and comparisons**: The paper does not compare against several important recent NAR zero-shot TTS systems like Voicebox, NaturalSpeech 3, or CosyVoice. The comparison with F5-TTS (a flow-matching NAR model) is valuable, but the paper doesn't discuss why RisoTTo's approach is preferable to F5-TTS's simpler DiT-based architecture. The claim "outperforms all models except T5-TTS and MaskGCT" is misleading—RisoTTo is actually outperformed on MOS and WER by both T5-TTS and MaskGCT on VCTK.

- **Insufficient detail on training and reproducibility**: The paper mentions training on 580+292+24 hours of data but doesn't specify the exact training split, number of training steps, or computational budget. The SAG network architecture is described as a "Conv2D-based U-Net" with channel reduction by factor 8, but critical architectural details (number of layers, kernel sizes, downsampling factors) are omitted. The inference procedure for SAG (number of sampling steps N_SAG) is not specified.

### Minor
- **The invertible encoder's role during inference is unclear**: The paper states that during inference, "residual information can be sampled directly from the prior distribution" (Gaussian noise). However, it's not explained how this sampled noise is used—is it simply added to the context vector? The architecture diagram (Figure 2) shows z being fed into the invertible encoder during inference, but the text says the encoder is "not required" during inference. This contradiction needs resolution.

- **Limited analysis of failure cases**: The paper doesn't discuss scenarios where RisoTTo might fail (e.g., extreme speaker variation, very short prompts, out-of-domain text). The WER of 5.51 on VCTK versus ground truth 3.81 indicates room for improvement, but no analysis of error patterns is provided.

### Trivial
- The paper uses NISQA-MOS instead of human evaluation, which is acceptable but should be noted as a limitation. The confidence intervals are relatively wide for some metrics.

## Nice-to-Haves
- A comparison with the SAG network using different numbers of flow matching sampling steps would help understand the speed-quality trade-off.
- Analysis of how the 3-second prompt length affects performance would be valuable for practical deployment.
- Visualizing the learned soft alignments (A_soft) compared to attention-based alignments would strengthen the claim that SAG captures similar patterns.

## Novel Insights
The key insight is that the performance gap between AR and NAR TTS can be systematically addressed by decomposing the problem into two complementary challenges: (1) generating soft alignments without autoregressive decoding (via flow matching distillation), and (2) modeling the residual acoustic information that soft alignments cannot capture (via normalizing flow-based disentanglement). The mutual information minimization perspective provides a principled way to ensure the residual representation is truly complementary to the semantic context. This two-pronged approach is more principled than simply scaling up NAR models or using more complex upsampling schemes.

## Suggestions
1. Clarify the inference procedure for the invertible encoder—specifically, how Gaussian noise is converted to residual information and combined with the context vector.
2. Add comparisons with more recent NAR zero-shot TTS systems (Voicebox, NaturalSpeech 3) and ensure all comparisons use identical evaluation conditions.
3. Increase the sample size for ablation studies and report statistical significance tests.
4. Provide more architectural details for the SAG U-Net and specify the number of sampling steps used during inference.

## Score and Decision
The paper presents a well-motivated and technically sound approach to improving NAR zero-shot TTS, with clear theoretical grounding and practical advantages in efficiency. However, the evaluation has significant limitations—mixing results from different sources, missing important baselines, and small sample sizes for ablation studies. The claims of "comparable performance to autoregressive models" are partially supported but overstated given that T5-TTS and MaskGCT outperform RisoTTo on key metrics. The practical benefits (33M parameters, 0.89s latency) are genuine and valuable. The paper would benefit from more rigorous and comprehensive evaluation before acceptance.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>