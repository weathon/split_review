Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the consolidated review.

## Summary

This paper proposes FARV, a unit-based vocoder for Video-to-Speech (V2S) synthesis that fuses facial embeddings (from the pretrained FaRL encoder) with acoustic units (from HuBERT) in a unit-HiFiGAN framework. The core idea is two-fold: (1) sharing the unit vocabulary between the frontend encoder and vocoder bridges the domain gap that plagues mel-based vocoders, and (2) injecting visual speaker information via FaRL preserves speaker identity that standard unit-based vocoders lose. Experiments compare FARV against mel-based HiFiGAN and unit-based ReVISE on LRS2-BBC, LRS3-TED, and VoxCeleb2.

## Strengths

1. **Novel and well-motivated architecture**: FARV is the first V2S vocoder to explicitly incorporate a pretrained facial representation extractor (FaRL) into the unit-HiFiGAN framework, directly addressing the known limitation that unit-based vocoders discard speaker-specific information (Sec. 3.3). The additive fusion of broadcasted visual embeddings with unit embeddings is simple but effective.

2. **Demonstrably better speaker preservation than unit-HiFiGAN on same-training-data comparisons**: In the dataset adaptation experiments (Table 3, Sec. 4.3.1), where both FARV and vanilla unit-HiFiGAN are finetuned on the same multi-speaker datasets (LRS2, VoxCeleb2), FARV consistently outperforms unit-HiFiGAN on speaker matching metrics. This is the cleanest evidence that the facial embedding contributes beyond simply training on more speakers.

3. **Superior zero-shot adaptation to the V2S frontend without finetuning**: Table 4 and Figure 3 show that when vocoders are applied to frontend encoder predictions without any finetuning, FARV's performance drop is far smaller than that of mel-based HiFiGAN across nearly all metrics (e.g., WER drop ~10% vs. >100% for HiFiGAN on LRS3-TED). This resilience stems from the shared unit vocabulary and is a practically meaningful result.

4. **Top-2 intelligibility among visual-only methods despite competing against supervised baselines**: In Table 1, FARV ranks among the top two across all evaluated metrics (ESTOI, MCD, LSE-C, LSE-D) on both LRS3-TED and LRS2-BBC, outperforming several methods that rely on additional speaker embeddings or textual information. This is notable because FARV uses only visual input.

5. **Empirical verification of the embedding's speaker-relevant content**: The linear probe experiments (Table 6) show that FARV's fused embedding achieves 100% gender classification accuracy vs. ~76% for unit-HiFiGAN, and significantly higher emotion accuracy. This confirms that the visual component enriches the latent representation with speaker-related cues.

## Weaknesses

### Fatal
None. The paper's core claims are plausible and partially supported. The issues below are major but addressable.

### Major

1. **Training data confound in the main V2S synthesis comparison (Table 2) undermines the central speaker-preservation claim**. In the V2S synthesis evaluation, FARV is trained on multi-speaker datasets (LRS2-BBC, LRS3-TED) *with* facial embeddings, while the unit-HiFiGAN baseline is evaluated only in its LJSpeech-trained form (single-speaker) without finetuning. The paper explicitly avoids finetuning unit-HiFiGAN on the multi-speaker data (line 158), arguing that finetuning hurts quality. But this choice conflates two variables: the facial embedding *and* the multi-speaker training data. The paper *does* provide a cleaner comparison in the dataset adaptation experiments (Table 3, where both models are finetuned on the same data with ground-truth inputs), but the V2S synthesis results in Table 2 — the most direct evidence for the paper's main claim — remain confounded. A controlled experiment (unit-HiFiGAN finetuned on LRS2/LRS3 without facial embeddings, evaluated in the V2S pipeline) is needed to attribute the SECS/EER improvements to the visual modality. *Why it matters*: Without this control, the central contribution (facial embeddings improve speaker preservation) is unsubstantiated for the paper's primary evaluation setting.

2. **Incomplete comparison with speaker-conditioned mel vocoders**. The paper argues that FARV strikes a better balance than mel-based vocoders between speaker preservation and domain adaptability. But the mel vocoder used for comparison (plain HiFiGAN) has no speaker conditioning whatsoever, while FARV benefits from FaRL's speaker-relevant features. A mel-based vocoder augmented with the same facial embedding (or another speaker embedding) would be the proper ablation to test whether FARV's advantage is due to the acoustic representation (units vs. mel) or the added conditioning. Without this, the claim that unit-based approaches are superior for this trade-off is not properly isolated. *Why it matters*: The paper frames part of its contribution as addressing mel vocoders' limitations, but the comparison is asymmetric.

### Minor

1. **No ablation on the choice of facial encoder**. The paper uses FaRL exclusively and does not test alternatives (e.g., ArcFace, a simple face recognition embedding). Given that FaRL is a large vision-language model, a lighter face embedding might work as well or better at lower cost. The 100% gender accuracy (Table 6) raises the question of whether the embedding captures coarse cues rather than nuanced speaker identity. This does not invalidate the approach but limits insight into *why* the facial embedding helps.

2. **The "leading intelligibility" claim is slightly too strong for the evidence presented**. The paper states "leading performance in acoustic intelligibility" (abstract) and "consistently ranks among the top two across all evaluated metrics" (Section 4.2.1). "Top-2" is specific and supportable, but "leading" implies first place across the board. Given that half the baselines use additional supervision (speaker embeddings, text), the framing could be more precise. A minor wording revision would suffice.

3. **100% gender classification accuracy in the embedding probe (Table 6) is unexplained**. Perfect accuracy on a multi-class (8 emotions, presumably balanced) dataset raises reasonable questions about potential speaker overlap between FARV's training set and the RAVDESS probe set, or whether the embedding simply memorizes a very coarse visual cue. The paper should clarify the speaker split and discuss whether this result generalizes.

4. **Visual frame selection is underspecified**. Section 3.3 says "a visual frame cropped from the input video" is used, but it is not described how this frame is selected (random, first frame, centered on face?), whether the crop is the face region or mouth region, or whether the embedding is averaged across multiple frames. This level of detail matters for reproducibility.

5. **Mel-based frontend uses a different training objective (L1 regression on Mel spectrograms) than the unit-based frontend (cross-entropy on units)**, as described in Section 3.2. The comparison between mel and unit pipelines is therefore coupled with a difference in the frontend's learning problem. The paper acknowledges this setup explicitly, but it remains a factor that should be noted when interpreting the mel vs. unit vocoder comparison in V2S adaptation.

### Trivial
- "characterisitcs" (typo, line 4) → "characteristics"
- "evalutate" (typo, line 145) → "evaluate"
- "comparsion" (typo, line 81) → "comparison"
- "interfers" (typo, line 35) → "interferes"

## Nice-to-Haves
- Testing on more diverse conditions (different languages, recording environments) beyond LRS2/LRS3 for V2S synthesis. The VoxCeleb2 experiments are a good start but focus on EER, not intelligibility.
- A brief discussion of computational cost/latency introduced by the FaRL encoder, since this is relevant for practical deployment.
- An ablation comparing additive fusion (used in the paper) with concatenation or cross-attention between unit embeddings and visual features.

## Removed Points

These points from the input reviews have been removed or downgraded. They are listed here for transparency but should not be weighted in evaluation:

- **"Zero-shot terminology is misleading"** (Harsh Critic Point 2): *Removed* — The paper explicitly defines two types of adaptation in Section 4.3 ("dataset adaptation" = cross-dataset zero-shot; "V2S adaptation" = no-finetuning on frontend outputs). The term "zero-shot" for V2S adaptation means "without finetuning on frontend predictions," which is a standard and valid usage. The vocoder has not seen the specific error distribution of the frontend, even if training data comes from the same dataset. The paper's definitions are clear.
- **"The paper should note that sync metrics could be affected by both stages"** (Harsh Critic "Other Observations"): *Removed* — This is self-evident for any two-stage pipeline and is not a meaningful gap.
- **"The comparison with mel-based vocoders is incomplete because the mel vocoder is not given speaker conditioning, while FARV is"**: *Kept as Major* (modified from the harsh critic's framing) — This is a valid point, but the harsh critic's phrasing implied the entire mel comparison is invalid. The paper's adaptation claim (shared vocabulary helps domain gap) is independently supported even with unconditioned mel vocoders. The conditioning concern specifically affects the *speaker preservation vs. quality* comparison, not the adaptation claim. Kept as Major weakness #2.
- **Strength Finder's claim that FARV achieves "leading" intelligibility**: *Downgraded* — The paper says "top-2 across all metrics," which is specific and supportable. "Leading" is a minor wording issue (see Minor weakness #2).

## Novel Insights

Beyond the paper's own contributions, a genuinely interesting observation emerges from the combination of Table 4 and Table 5: while mel vocoders (HiFiGAN) catastrophically degrade when applied zero-shot to V2S frontend outputs (NISQA-MOS dropping to near zero), they recover fully after only 20k finetuning steps on frontend-generated Mel spectrograms. This suggests the domain gap for mel vocoders is large in *distribution* but shallow in *complexity* — a small amount of adaptation data suffices. This raises the question of whether a lightweight adaptor between the mel frontend and vocoder could match the unit-based approach without requiring a shared vocabulary, which is left unexplored.

## Suggestions

1. **Run the controlled experiment**: Finetune unit-HiFiGAN on LRS2/LRS3 (without facial embeddings) and evaluate its SECS/EER in the V2S pipeline alongside FARV. Report the acoustic quality as well — even if quality degrades, the trade-off illuminates what the facial embedding contributes. This single experiment would resolve the most damaging confound.

2. **Add a speaker-conditioned mel baseline**: Augment HiFiGAN with FaRL (or any speaker embedding) and compare on the V2S frontend adaptation experiments. This isolates whether FARV's advantage is due to units or the added conditioning.

3. **Clarify the visual frame processing**: Specify how the input frame is selected, cropped, and whether the embedding is averaged across frames. Also clarify speaker overlap between FARV training splits and the RAVDESS probe set to address the 100% gender accuracy question.

4. **Tone down the "leading" language**: Replace "leading performance" with "competitive performance, ranking among the top two across all metrics despite using only visual input."

## Score and Decision

The paper addresses a real problem and proposes a sensible, novel approach. The core architectural idea (facial embeddings as speaker conditioning for unit-based V2S vocoders) is well-motivated and has practical potential. The paper's strengths include clear evidence that unit-based vocoders outperform mel-based ones for V2S frontend adaptation (Table 4), and that FARV beats vanilla unit-HiFiGAN when both are trained on the same data (Table 3). However, the main V2S synthesis comparison (Table 2) — which is supposed to demonstrate that facial embeddings improve speaker preservation — is confounded by training data differences. The mel vocoder comparison is also asymmetric. These weaknesses are major but not fatal; they require additional controlled experiments to resolve. In its current form, the central claim is insufficiently supported.

**Score**: 4.5 / 10 (major revisions needed)

**Decision**: Reject (but encouragement to resubmit with controlled experiments)

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>