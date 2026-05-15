Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

The paper proposes FARV, a unit-based vocoder for Video-to-Speech (V2S) synthesis that integrates facial embeddings (from FaRL) with acoustic units to improve speaker identity preservation while maintaining the domain-gap resilience of unit-based vocoders. It claims FARV achieves leading intelligibility and a favorable balance between speaker preservation and acoustic quality.

## Strengths

1. **Clear motivation and elegant architecture design.** The idea of using a frozen facial encoder (FaRL) to inject speaker identity information into a unit-based vocoder is well-motivated and conceptually sound. The paper identifies a real limitation of unit-based vocoders in V2S (loss of speaker characteristics, as noted in ReVISE) and proposes a plausible solution that requires no extra audio or text supervision at inference time.

2. **FARV achieves strong intelligibility among visual-only V2S methods.** Table 1 shows that FARV consistently ranks in the top two across ESTOI, MCD, LSE-C, LSE-D, and WER on both LRS3-TED and LRS2-BBC when compared to prior visual-only V2S systems, and even outperforms several methods that use additional supervision (speaker embeddings, text). This is a genuinely competitive result.

3. **Quantitative evidence of improved speaker-relevant information in the embedding.** Table 6 shows that FARV's unit embedding achieves 100% gender classification accuracy (vs. 78.1% for unit-HiFiGAN) and substantially better emotion classification. While this experiment has limitations (discussed below), it provides direct evidence that the facial fusion injects speaker-relevant information into the embedding space.

4. **Thorough investigation of adaptation scenarios.** The paper systematically evaluates vocoder behavior across dataset adaptation (zero-shot vs. finetuned, Table 3/Figure 2), frontend adaptation (Table 4), and mel vocoder finetuning (Table 5), providing useful characterization of practical deployment challenges.

## Weaknesses

### Fatal
None.

### Major

1. **Missing controlled ablation: Same training data without facial embeddings.** The paper never compares FARV against unit-HiFiGAN trained on the *exact same multi-speaker datasets* (LRS3-TED + LRS2-BBC) *without* facial embeddings. FARV is trained on LRS3/LRS2 (multi-speaker, audio-visual), while the primary comparison baseline (unit-HiFiGAN) is trained only on LJSpeech (single-speaker). This confound is present across Tables 2, 3, and 4. Although Table 3 does finetune both models on the same target dataset (e.g., VoxCeleb2), FARV has already been additionally trained on LRS3, so the comparison remains asymmetric. Without a unit-HiFiGAN trained on the same multi-speaker data as FARV (minus facial input), the reported gains in SECS, EER, and embedding quality cannot be conclusively attributed to the facial embedding mechanism rather than to larger/more diverse training data.

2. **Missing ablation: Audio-based speaker embedding baseline.** The paper does not compare FARV against a unit-HiFiGAN augmented with an audio-based speaker embedding (e.g., d-vector from a pretrained speaker encoder). Such a comparison would quantify whether the *visual* modality offers unique benefits over an acoustic speaker embedding that could be derived from the same V2S frontend. Without this, it is unclear if the improvement is from additional speaker information generally or from facial information specifically.

3. **Contribution 3 oversells a known property.** Contribution 3 states that "mel-based vocoders require finetuning... FARV is more resilient." The significantly better resilience of unit-based vocoders over mel-based ones in V2S was already demonstrated by ReVISE (Hsu et al. 2023). The paper's experiments in Sections 4.3.2–4.3.3 largely re-verify this known property for unit-based vocoders in general, without isolating whether the *facial embedding* contributes to this resilience. The claim should be reframed accordingly.

### Minor

1. **The embedding capability experiment (Section 4.4) is not a controlled comparison.** The linear classifier uses FARV's unit embedding *after* facial fusion vs. unit-HiFiGAN's embedding (trained on different data). This shows that FARV's embedding carries more speaker information, which is expected given the design. A cleaner test would compare FARV's unit embedding *before vs. after* facial fusion, or compare FARV vs. unit-HiFiGAN when both are trained on the same multi-speaker data.

2. **The "zero-shot" terminology is inconsistently applied.** FARV is initialized from unit-HiFiGAN's LJSpeech checkpoint and then trained on LRS3/LRS2. When evaluated on LRS2 or VoxCeleb2 without further finetuning, it has already seen data from these domains (via its training on LRS3, which is multi-speaker audio-visual data). This is not "zero-shot" in the same sense as unit-HiFiGAN, which was trained only on LJSpeech and tested on unseen datasets. The paper acknowledges this asymmetry (line 183) but the terminology could mislead readers.

3. **Reproducibility gaps.** The paper does not specify the FaRL model variant used, the unit vocabulary size, the clustering algorithm for HuBERT units, or the exact AV-HuBERT checkpoint. These details are needed to reproduce the work.

### Trivial
None.

## Nice-to-Haves

- An ablation comparing simple additive fusion vs. concatenation, cross-attention, or gating for the facial embedding would strengthen the architectural justification.
- Analysis of failure cases (e.g., out-of-distribution facial poses, occlusions) and their effect on speaker preservation would improve practical understanding.
- Qualitative spectrogram comparisons or audio samples would help visually verify the claimed improvements in speaker characteristics.

## Removed Points

- **"Circular validation" of Section 4.4 (from Harsh Critic):** Removed as overblown. The experiment compares FARV's embedding (with facial info) against unit-HiFiGAN's embedding (without). This is not circular — it tests whether the fused embedding carries more speaker-relevant information, which is a legitimate sanity check. However, it is weakened by the training data confound, which I have already captured in Weaknesses Minor-1.
- **"Metric bias" concern (Section 4.1.2):** The critic speculates that SECS/EER may be biased toward methods using the same speaker encoder. If the same metric is applied to all methods uniformly, this is not a bias. Removed as speculative.
- **Pure formatting/style nitpicks:** Removed per instructions.
- **Missing related works / missing appendix / missing proofs:** Removed per instructions.
- **Strength Finder claims about "strong domain adaptation":** The strength that "FARV exhibits strong domain adaptation" is partially confounded by the training data issue. I have kept a version of this in the Strengths section (point 4) but reframed it as "thorough investigation" rather than conclusive proof of FARV's superiority.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a well-known structural concern in cross-modal V2S evaluation (training data confounds between proposed method and baselines), but this is a standard experimental design issue rather than a novel observation about the paper's subject matter.

## Suggestions

1. **Essential: Train a unit-HiFiGAN baseline on the same LRS3-TED + LRS2-BBC data without facial embeddings.** This is the single most important experiment needed to isolate the contribution of the facial embedding. Without it, the paper's central claim remains unsubstantiated.

2. **Add an audio-based speaker embedding baseline.** Augment unit-HiFiGAN with a d-vector or similar speaker embedding trained on the same data, to test whether the visual modality offers unique value.

3. **Reframe Contribution 3.** Acknowledge that the zero-shot resilience of unit-based vocoders over mel-based vocoders is a known property (ReVISE), and clarify that FARV's contribution is maintaining this property while improving speaker preservation through facial embeddings.

4. **Clarify the "zero-shot" terminology.** Provide an explicit table showing what data each model was trained on to avoid confusion.

## Score and Decision

The paper addresses a well-motivated problem and proposes a reasonable solution. However, the experimental evaluation contains a significant confound (training data disparity between FARV and baselines) that weakens the central claims about facial embeddings improving speaker identity preservation. The missing controlled ablation prevents strong conclusions. The work is promising but requires substantial re-evaluation with proper controls before the contributions can be fully assessed.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>