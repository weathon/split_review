Now I have verified all the relevant content. Let me produce the final consolidated review.

---

## Summary

This paper presents the first sentence-level multilingual Visual Speech Recognition (VSR) system with a single model. Key innovations include: (1) **visual speech units** — discretized representations from a newly proposed multilingual self-supervised model (mAV-HuBERT, trained on 5,512 hours across 9 languages) that reduce input data size to 0.016% of raw video; (2) **curriculum learning** that transitions from audio-visual speech unit inputs to visual-only inputs during pre-training; and (3) leveraging automatic labels to construct 4,545 hours of multilingual video-text paired data. The trained model achieves competitive or better performance compared to prior language-specific SOTA methods across 5 languages (En, Es, It, Fr, Pt) using a single model, with ~12× faster pre-training.

## Strengths

1. **First sentence-level multilingual VSR with a single model.** The paper explicitly and correctly positions itself as the first work to demonstrate that a single model can recognize multiple languages in VSR at the sentence level (Section 1, Contribution 1). This is a genuinely novel framing that addresses a real gap — multilingual audio ASR is common, but VSR has remained language-specific.

2. **Visual speech units enable drastic efficiency gains.** The discretization reduces input data to 0.016% of the original (61,952 bits per frame → 10 bits per unit). Table 3 shows a ~12× training speedup (6.6 hours for 11 epochs of pre-training vs. 52.5 hours for 8 epochs of standard VSR training), a concrete and significant computational improvement.

3. **mAV-HuBERT substantially outperforms English-only AV-HuBERT on non-English languages.** Table 2 shows WER reductions of over 10% absolute on Es, It, Fr, and Pt when using the proposed multilingual encoder, validating the need for language-diverse self-supervised pretraining. The mAV-HuBERT component is soundly motivated and empirically justified.

4. **Curriculum learning from audio-visual to visual inputs is critical.** The ablation in Table 5 demonstrates that removing curriculum learning causes catastrophic degradation (e.g., English WER jumps from 24.4 to 40.7; Spanish from 50.6 to 77.7), confirming the importance of the progressive masking strategy. This ablation cleanly isolates the contribution.

5. **Competitive results against dedicated monolingual systems.** Table 7 shows that the single multilingual model achieves best scores on 3 of 5 languages (Es, It, Fr) and second-best on the remaining 2 (En, Pt) when compared with prior language-specific SOTA methods. This is the strongest evidence for the paper's central claim.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core contributions are sound, and no verified flaw invalidates the main claims.

### Minor

1. **The "state-of-the-art" claim is imprecisely framed.** The paper asserts "new state-of-the-art multilingual VSR performances" (abstract, conclusion), but the only direct multilingual baseline (Table 6) is a self-constructed AV-HuBERT finetuned on the same data — there is no established prior work on this exact task. The meaningful empirical contribution is in Table 7 (competitive with/beating language-specific SOTA using a single model), which is strong enough to stand on its own. The SOTA framing as written invites unnecessary skepticism and should be qualified to reflect what was actually demonstrated: a single multilingual model that is competitive with or surpasses prior language-specific approaches.

2. **The efficiency comparison omits the upfront cost of training mAV-HuBERT.** Table 3 reports 6.6 hours for pre-training vs. 52.5 hours for standard VSR training, but the mAV-HuBERT itself required 350k steps on 64 GPUs (Section 4.2). While mAV-HuBERT is a reusable resource (analogous to a pretrained backbone in other pipelines), the "~10× faster" framing should transparently acknowledge this upfront cost. A fair total-system comparison would include the mAV-HuBERT training cost amortized or stated separately.

3. **The curriculum learning ablation reveals a phenomenon that deserves deeper analysis.** The "−Curriculum" condition (pre-training on visual speech units directly, without progressive masking) produces WERs that are *worse than no pre-training at all* for several languages (Spanish: 77.7 vs. 56.9; French: 65.3 vs. 40.5; Portuguese: 80.6 vs. 63.9). The paper's explanation — "directly performing the visual speech unit to text translation from scratch is challenging" — is plausible but does not address why pre-training on visual units alone actively *hurts* relative to a random initialization. This raises interesting questions about whether the visual speech units are too lossy to bootstrap useful representations without audio guidance. The authors should at minimum discuss this negative transfer phenomenon.

4. **The "curse of multilinguality" explanation is invoked imprecisely.** The paper attributes English performance degradation to the curse of multilinguality (Sections 4.3.1, 4.3.5), but English has by far the most training data (Table 1: 3196 hours vs. ≤500 hours for other languages). The classic curse of multilinguality describes a trade-off with roughly balanced data across languages; here the data is heavily skewed. A more precise explanation would discuss capacity constraints and the specific data distribution, not just the number of languages.

5. **No evaluation on languages outside the 5 training languages.** The mTEDx dataset provides 8 languages, and mAV-HuBERT is trained on 9 languages (including De, Ru, Ar, El). Evaluating the pre-trained model on these unseen languages (even in a zero-shot manner or with minimal adaptation) would substantially strengthen the multilingual generalization claim. Without this, the "multilingual" claim is limited to the 5 seen languages.

### Trivial

- **Unreported Whisper confidence threshold.** The paper does not report the confidence threshold used for Whisper-based language identification when constructing the mAV-HuBERT training data from VoxCeleb2 and AVSpeech (Section 3.1). Reporting this threshold and the resulting language distribution would improve reproducibility.

## Nice-to-Haves

- **Ablation on quantization depth** (e.g., 100, 500, 2000 visual speech units) to test sensitivity to the unit vocabulary size and whether there is a sweet spot between compression and linguistic content.
- **A fixed-p=0 ablation** (always audio-visual units throughout pre-training) to isolate whether the *progressive* nature of the masking schedule matters, or whether any audio-augmented pre-training would suffice.
- **Incremental language addition** to quantify the curse of multilinguality: measuring English WER as languages are added one at a time.
- **Error analysis** (confusion matrices, language confusions, error types) comparing the multilingual model against the monolingual baselines.
- **Testing on unseen mTEDx languages** (De, Ru, Ar, El) to demonstrate cross-lingual zero-shot capability.

## Removed Points

These points were flagged for removal per the review guidelines and should be treated with caution:

- **"Figure 2 is absent from the text, making it impossible to evaluate the claim."** — The figure is clearly referenced in the text (line 130: "Figure 2: Visualization of speech units"). The image was dropped by the PDF parser, not by the authors. This criticism reflects a parser artifact, not an author error.
- **"The paper should compare with a model pre-trained on audio speech units alone (no visual units)."** — This is a reasonable suggestion but framed as a "missed experiment" rather than a genuine weakness. The paper's contribution centers on *visual* speech units; the curriculum already uses audio units as auxiliary input. This is moved to Nice-to-Haves.
- **Generic strength claims from Strength Finder** (e.g., vague statements about addressing important problems without specific evidence) were dropped as they lacked concrete content or citation support.

## Novel Insights

The most striking finding is the *negative* effect of pre-training on visual speech units alone (the −Curriculum ablation in Table 5). The fact that this condition is worse than no pre-training at all for multiple languages suggests that the visual speech units, when presented in isolation, may actually mislead the model — possibly because the discretization discards information needed to disambiguate homophenes (visually similar phonemes), and without the audio signal to break ties during early training, the model converges to poor local minima. The curriculum learning papered over this by letting audio units provide the disambiguating signal initially, effectively letting the model "learn to read" the lossy visual units through the lens of the richer audio modality first. This dynamic is worth explicit study in future work: are visual speech units inherently insufficient for a cold-start, or could a different training objective (e.g., reconstruction rather than translation) make them viable without audio?

## Suggestions

1. **Reframe the SOTA claim.** Replace "new state-of-the-art multilingual VSR performances" with language such as "competitive with or surpassing prior language-specific SOTA methods" to align the claim with what the experiments actually show.
2. **Acknowledge the upfront mAV-HuBERT cost** in the efficiency discussion. A brief sentence stating "mAV-HuBERT training requires 350k steps on 64 GPUs as a one-time cost" would satisfy transparency without weakening the contribution.
3. **Add a paragraph discussing the negative transfer in the −Curriculum ablation.** Even a brief analysis of why visual-unit-only pre-training hurts (e.g., hypothesis about unit lossiness leading to confirmation bias in early representations) would substantially strengthen the analysis section.
4. **Report the Whisper confidence threshold** and language distribution after filtering for reproducibility.
5. **Refine the curse of multilinguality discussion** to reference the heavily imbalanced data distribution rather than attributing English degradation solely to the number of languages.

## Score and Decision

This paper presents a genuinely novel contribution — the first single-model sentence-level multilingual VSR system — supported by a well-designed technical approach (visual speech units, mAV-HuBERT, curriculum learning) and solid empirical results (competitive with dedicated monolingual systems, ~12× training speedup). The weaknesses are primarily framing imprecision and shallow analysis of one ablation phenomenon, none fatal to the core contribution. The paper's strengths clearly outweigh its weaknesses, and the contributions are publishable with moderate revisions.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>