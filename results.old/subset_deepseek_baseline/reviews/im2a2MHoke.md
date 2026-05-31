## Summary

This paper proposes RisoTTo, a non-autoregressive (NAR) zero-shot TTS model that aims to close the performance gap with autoregressive (AR) models. The key contributions are: (1) **Soft Alignment Generation (SAG)** – a flow-matching network that generates soft attention-like alignments between text and mel-spectrograms without requiring autoregressive decoding; (2) **Invertible Encoder (IE)** – a normalizing-flow-based module that disentangles residual acoustic information from the semantic context vector, allowing sampling of missing acoustic details at inference; (3) **Prompt-Aware Lightweight Convolution (PAL)** – a speaker-adaptive convolution that dynamically adjusts kernel weights from a speech prompt. Experiments on VCTK and Seed-TTS test sets show that RisoTTo achieves competitive MOS, speaker similarity (SECS), and WER against several strong zero-shot TTS baselines while using far fewer parameters (33M) and lower latency (0.89s for 10s speech).

## Strengths

- **Novel combination of techniques for NAR TTS:** The paper identifies two fundamental limitations of NAR TTS (lack of soft alignment and missing acoustic context) and proposes principled solutions (SAG and IE) that are well-motivated by the success of AR attention mechanisms. The use of flow matching for alignment generation and normalizing flow for residual disentanglement is creative and technically sound.
- **Strong empirical results with high efficiency:** RisoTTo achieves the highest SECS among all compared models on both VCTK (0.668) and Seed-TTS (0.651), and its MOS/WER are competitive with much larger models (e.g., MaskGCT with 1048M parameters). The model is extremely lightweight (33M parameters) and fast (0.89s latency), which is a significant practical advantage.
- **Thorough ablation study:** The ablation in Table 5 clearly isolates the contribution of each proposed module. The results show that SAG improves MOS, IE improves WER (intelligibility), and PAL improves SECS (speaker similarity), confirming that each component serves a distinct and valuable role.
- **Clear theoretical grounding:** The paper provides a solid theoretical justification for the invertible encoder, linking the KL divergence minimization to mutual information reduction (Eq. 5) and explaining why the deterministic nature of normalizing flow avoids posterior collapse compared to VAE (Table 2). The MMD analysis in Table 2 convincingly demonstrates better disentanglement.

## Weaknesses

### Fatal
None.

### Major
- **Evaluation relies on NISQA-MOS instead of human listening:** The paper uses a pre-trained NISQA model to estimate MOS rather than conducting human evaluation. While NISQA is a reasonable proxy, the claim of “comparable performance to existing autoregressive models” would be significantly strengthened by human perceptual evaluation, especially since MOS differences in Table 4 are small and confidence intervals overlap in several cases.
- **Comparison with baselines is not fully controlled:** For VALL-E, T5-TTS, and NaturalSpeech2, the paper uses audio samples from official demo pages rather than running the models under identical conditions. This introduces potential mismatches in test sets, prompt selection, and evaluation pipeline. The paper acknowledges this but does not discuss how these differences might affect the comparison. For a fairer assessment, the authors should either re-implement these baselines or use only models with publicly available code (as done for Spark-TTS, F5-TTS, MaskGCT).
- **The claim “beyond autoregressive models” is overstated:** In Table 4, T5-TTS (AR) and MaskGCT (non-AR but much larger) achieve higher MOS and lower WER than RisoTTo on VCTK. RisoTTo only surpasses them in SECS. The title and abstract suggest a general superiority over AR models, but the evidence shows competitiveness rather than clear outperformance. The paper should temper this claim and more precisely state that RisoTTo achieves comparable quality with dramatically higher efficiency.

### Minor
- **Ablation result for IE on SECS is puzzling:** In Table 5, removing IE (RisoTTo w/o IE) actually increases SECS from 0.673 to 0.681, while WER degrades. The paper attributes IE’s impact to speech quality (WER) but does not explain why speaker similarity slightly improves without it. This deserves a brief discussion.
- **Limited test set size for some evaluations:** The ablation study in Table 1 uses only 6 unseen speakers and 5 utterances per speaker (30 samples total). The VCTK evaluation in Table 5 uses 50 samples. While these are common in TTS papers, the small sample size increases variance and reduces statistical reliability. The paper should report confidence intervals for all metrics or use larger evaluation sets.
- **Missing details on training of SAG and IE:** The paper does not specify the number of flow matching steps used during SAG training, the architecture of the duration predictor, or the exact training schedule for the invertible encoder (e.g., whether it is trained jointly or separately). These details are important for reproducibility.

### Trivial
None.

## Nice-to-Haves
- A human listening test (e.g., MUSHRA or AB preference) comparing RisoTTo against T5-TTS and MaskGCT on a common set of prompts would greatly strengthen the perceptual claims.
- Analysis of the generated soft alignments (e.g., visualization of A_soft) to qualitatively show that SAG produces meaningful alignments similar to AR attention.
- Discussion of failure cases or limitations, such as when the Gaussian prior sampling fails to provide adequate acoustic context.

## Novel Insights

Beyond the paper’s own contributions, a key insight is that the performance gap between NAR and AR TTS can be largely attributed to two specific missing components—soft alignment and residual acoustic context—rather than an inherent limitation of parallel generation. By explicitly modeling these components with flow matching and normalizing flow, the paper demonstrates that NAR models can approach AR quality while retaining their efficiency advantages. This suggests that future NAR TTS research should focus on “what information is missing” rather than “how to mimic AR decoding,” opening a new direction for lightweight, high-quality TTS.

## Suggestions
- Conduct a human evaluation (e.g., MOS or preference test) on a subset of the VCTK and Seed-TTS test sets to validate the NISQA-based results.
- Reproduce the comparison with VALL-E, T5-TTS, and NaturalSpeech2 using their official code (if available) or at least under a controlled prompt and test-set setting to eliminate confounding factors.
- Clarify the claim in the title and abstract: replace “beyond autoregressive models” with “competitive with autoregressive models” or “achieving autoregressive-level quality with non-autoregressive efficiency.”
- Add a brief discussion of the SECS increase when removing IE in the ablation study.

## Score and Decision

**Score:** 7.5  
**Decision:** Accept  

The paper presents a well-motivated, technically sound, and empirically strong contribution to zero-shot non-autoregressive TTS. The proposed modules (SAG, IE, PAL) are novel and clearly beneficial. The efficiency gains (33M parameters, 0.89s latency) are impressive and practically important. The main weaknesses are the reliance on automated MOS instead of human evaluation and the slightly overclaimed title, but these do not invalidate the core contribution. With minor revisions to temper the claims and add a human evaluation, the paper would be a solid addition to ICLR.

MY FINAL SCORE: <score>7.5</score>  
MY FINAL DECISION: <decision>Accept</decision>