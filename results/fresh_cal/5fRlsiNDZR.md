Now I have all the information needed. Let me construct the final consolidated review.

## Summary

FARV is a unit-based vocoder for Video-to-Speech (V2S) synthesis that fuses facial embeddings from a frozen FaRL image encoder with acoustic units to improve speaker identity preservation while inheriting the domain-gap robustness of shared unit vocabularies. The paper evaluates FARV on intelligibility, speaker matching, and adaptation capability across LRS3, LRS2, VoxCeleb2, and RAVDESS datasets.

## Strengths

- **Leading intelligibility among visual-only V2S methods.** Table 1 shows FARV's V2S pipeline consistently ranks top-2 across ESTOI, MCD, LSE-C, LSE-D, and WER on both LRS3-TED and LRS2-BBC, outperforming methods that use additional audio/text supervision. This is a system-level result that stands on its own.

- **Demonstrates zero-shot robustness of unit-based vocoders to V2S frontend output.** Table 4 shows that when applied to V2S frontend encoder predictions without finetuning, FARV's NISQA-MOS drops modestly (2.523 → 2.299 on LRS2-BBC), whereas the mel-based HiFiGAN collapses catastrophically (3.501 → 0.689). This clearly confirms the domain-gap advantage of shared unit vocabularies in V2S pipelines.

- **Systematically validates that mel-based vocoders require finetuning on frontend outputs.** Table 5 shows HiFiGAN finetuned on frontend-generated Mel spectrograms recovers from near-zero quality (0.689) to competitive levels (2.916), confirming the practical limitation of mel-based approaches for V2S.

- **Clean, principled architectural design.** The integration of a frozen FaRL image embedding via simple additive fusion (Equation 3) to the unit embedding is lightweight and well-motivated by the observation (Section 2.3) that unit-based vocoders lack speaker identity information.

## Weaknesses

### Fatal
None. The paper's system-level claims (intelligibility, domain-gap analysis) are supported by evidence. The main structural issue described below is major but addressable.

### Major

- **The core claim that facial embeddings improve speaker characteristics is confounded by unequal training data.** Unit-HiFiGAN (the baseline for speaker-related comparisons) is trained on single-speaker LJSpeech, while FARV is trained on multi-speaker LRS3-TED/LRS2-BBC "resuming from the checkpoint of the unit-HiFiGAN trained on LJSpeech" (line 151). The paper explicitly acknowledges this: "FARV is further trained on the LRS3-TED dataset... while other zero-shot vocoders are trained on the LJSpeech dataset" (line 183). The observed improvements in SECS, EER, gender/emotion classification (Tables 2, 3, 6) could therefore be driven by exposure to hundreds of additional speakers during LRS3/LRS2 training rather than by the facial embedding itself. The paper never provides the necessary control: a unit-HiFiGAN (or a version of FARV without facial input) trained on the *same* multi-speaker data. Without this ablation, the paper's central contribution is unvalidated. A proper control would be: train a unit-HiFiGAN on LRS3 (without facial input) and compare it to FARV trained on LRS3 (with facial input). If FARV still wins on SECS/EER, the facial embedding's role is confirmed.

### Minor

- **The embedding capability experiment (Table 6) compares embeddings at different levels of the processing pipeline.** FARV's "unit embedding" is actually the fused representation \(p_{AV} = e_I \oplus e_U\) (line 93), which directly contains the FaRL facial features. A linear classifier on this representation has direct access to facial information (e.g., for gender classification). The comparison against unit-HiFiGAN's unit embedding (which contains no facial information) primarily confirms that facial features are *present* in the FARV fused embedding, rather than demonstrating that the vocoder has learned to integrate facial cues into its internal representations in a non-trivial way. The paper would be strengthened by ablating the facial branch during inference (e.g., zeroing out \(e_I\)) and showing a significant drop in SECS/EER while intelligibility remains stable.

- **The facial embedding broadcasting mechanism is underspecified.** The paper states "the image embedding is broadcasted to match the length of acoustic units" (line 88) without clarifying whether the same facial vector is replicated identically to every time step or whether any temporal alignment is used. Replicating a static image embedding to every frame discards temporal facial dynamics (e.g., changing expressions), which the paper does not discuss as a limitation or design choice. This is a minor clarity issue affecting reproducibility.

### Trivial
None significant.

## Nice-to-Haves

- **Add more baselines for speaker characteristics (Table 2).** Currently only ReVISE is compared. Including other V2S methods (e.g., SVTS, DiffV2S) on SECS/EER would provide a more complete picture.
- **Human listening evaluation.** The paper relies entirely on automated metrics (NISQA-MOS, SECS, EER). A small-scale listening test for naturalness and speaker similarity would strengthen claims of practical suitability.
- **Discussion of failure cases.** When does the facial embedding hurt? E.g., if the speaker's face image is blurry or occluded, does FARV degrade gracefully?
- **Table 1 attribution.** The intelligibility results (Table 1) compare full V2S pipelines, so the contribution of the facial embedding specifically cannot be isolated there either. Adding an ablation of FARV without facial input in the pipeline would clarify attribution.

## Removed Points

- **"Human evaluation missing"** — Removed. NISQA-MOS is a standard automated quality metric; human evaluation is a nice-to-have, not a required weakness for this type of empirical paper.
- **"Discussion of failure cases"** — Removed from weaknesses; moved to Nice-to-Haves.
- **"More baselines for Table 2"** — Removed from weaknesses; moved to Nice-to-Haves.
- **"Table 1 results also confounded"** — Removed as a standalone weakness. Table 1 compares full V2S pipelines (frontend + vocoder) at the system level; different methods use different frontends, architectures, and data. The claim "FARV achieves leading intelligibility" is an empirical system-level result that does not depend on isolating the facial embedding's contribution. The confound criticism properly applies only to claims that attribute improvements *specifically* to the facial embedding, not to system-level benchmark results.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation that the training-data confound undermines attribution of the facial embedding's benefit is the key structural insight, but this is a criticism of the paper's experimental design rather than a novel synthesis.

## Suggestions

1. **Provide the critical ablation experiment:** Train a unit-HiFiGAN (without facial input) on the same LRS3-TED multi-speaker data that FARV uses, starting from the same LJSpeech checkpoint. Compare this against FARV (trained on LRS3-TED with facial input) on SECS, EER, and intelligibility. This directly tests whether the facial embedding adds value beyond multi-speaker training.

2. **Add a facial-ablation inference experiment:** Evaluate FARV with the facial embedding zeroed out / replaced with a random vector during inference. Show that SECS/EER degrades significantly while intelligibility holds steady. This provides causal evidence for the facial embedding's role.

3. **Clarify the broadcasting mechanism:** Specify whether the facial embedding is replicated identically to all time steps, and discuss the implications of using a static (frame-independent) facial vector.

4. **Clarify what is being classified in Table 6:** Clearly state whether the linear classifier operates on \(e_U\) (pre-fusion) or \(p_{AV}\) (post-fusion) for FARV, to avoid ambiguity about whether facial information is directly visible.

## Score and Decision

The paper tackles a real problem (speaker identity loss in unit-based V2S vocoders) with a well-motivated architectural idea (injecting FaRL facial embeddings). The system-level results for intelligibility and domain-gap robustness are empirically sound and constitute a useful contribution. However, the paper's central novelty claim — that facial embeddings *cause* the observed improvement in speaker characteristics — is not adequately supported because the baseline unit-HiFiGAN is trained on single-speaker LJSpeech while FARV is trained on multi-speaker LRS3/LRS2. This confound is acknowledged but never controlled for, and it undermines the paper's primary claim.

The paper would be significantly strengthened by the controlled ablation described above. In its current form, the evidence for the core contribution is insufficient for acceptance at a competitive venue.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>