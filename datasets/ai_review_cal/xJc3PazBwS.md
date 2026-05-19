- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 6, 3
Now I have a thorough understanding of everything. Let me produce the final consolidated review.

## Summary

This paper proposes a two-stage Variational Information Bottleneck (VIB) framework for disentangling speech representations into textual and acoustic components. In stage 1, a VIB encoder is trained with CTC loss to extract textual latents that preserve only transcription-relevant information. In stage 2, a second VIB encoder is trained on a downstream task (emotion recognition or speaker identification), conditioned on the frozen textual latents, to capture complementary acoustic features. Experiments on Wav2Vec2 and HuBERT models (various sizes, pre-trained and fine-tuned) show that the compressed latents maintain or improve task performance. Sanity-check probing on Common Voice demonstrates near-perfect separation, and the framework is further used for layerwise analysis and preliminary attribution.

## Strengths

- **Quantitative validation of disentanglement via sanity-check probing (Figure ~2, Section 5.1):** Textual latent representations achieve random performance (WER ≈ 100, with a minor typo noted below) when probed for acoustic features (pitch, intensity, gender, speaker ID), while acoustic latent representations score at random baseline for transcription. This directly validates that the VIB training achieves meaningful separation rather than merely producing two different representations.

- **Task performance preserved under strong compression (Table 1):** VIB with d=128 achieves accuracy competitive with or exceeding probing on full hidden states across multiple settings — e.g., emotion recognition on HuBERT-Large: 66.1% vs 57.3%; speaker identification on HuBERT-Large: 98.4% vs 92.3%. This demonstrates that aggressive compression via VIB does not sacrifice downstream utility.

- **Layerwise analysis reveals model specialization during fine-tuning (Section 6, Figure 3 right):** The framework reveals that for Wav2Vec2-FT, the acoustic contribution to emotion recognition drops sharply in final layers while textual contribution increases, consistent with ASR fine-tuning sacrificing acoustic information. This illustrates the framework's value as an analytical tool for understanding how different layers encode different information types.

- **Disentangled attribution shows interpretable patterns (Section 7, Figure 4):** Despite being preliminary, the attribution analysis shows that acoustic attention scores correlate more strongly with intensity/pitch peaks than textual attention, while textual attention correlates more with word-level sentiment polarity. This demonstrates the framework's potential as a disentangled attribution method.

## Weaknesses

### Fatal
None.

### Major

- **Disentanglement sanity-check not performed on IEMOCAP (the emotion recognition dataset).** The sanity-check probing (Section 5.1) is conducted entirely on Common Voice data, while the main emotion recognition results (Table 1) are on IEMOCAP. The paper does not verify that the IEMOCAP textual latents are clean of acoustic information, or that the acoustic latents for IEMOCAP are complementary to the textual ones. The t-SNE visualization (Section 5.2) uses RAVDESS, which has a different distribution. This gap is consequential because the claim that "stage 2 captures acoustic features not already in the textual component" assumes the textual latents are domain-robust. Without sanity probes on IEMOCAP, the emotion recognition results could — in the worst case — partly reflect acoustic latents compensating for domain-shifted textual latents. This is an addressable issue but limits the strength of the central claim.

### Minor

- **No comparison to other disentanglement methods.** The paper compares VIB to probing on original hidden states (a strong baseline), but does not benchmark against any alternative explicit disentanglement technique — e.g., adversarial feature removal, β-VAE, or methods from the voice conversion literature repurposed for the same protocol. While the paper's contribution is the framework itself (not state-of-the-art performance claims), the absence of any comparison makes it hard to assess what the VIB approach adds beyond its intuitive design.

- **Missing data-split specification for IEMOCAP.** The paper reports 4,064 utterances from 5 dyadic sessions with 10 speakers but does not describe the train/test split. Standard practice for IEMOCAP is leave-one-session-out cross-validation to avoid speaker overlap. If a random utterance-level split is used instead, results could be inflated by speaker identity leakage. The speaker identification experiments on Common Voice are also not described in sufficient split detail (only "4,000 training and 1,000 test"). This undermines reproducibility.

- **HuBERT-FT Large shows large WER degradation under VIB (25.6 vs. 6.9 probing, Table 1).** The paper does not discuss why fine-tuned models (which already optimize for ASR) cause VIB to lose so much textual fidelity. This is worth addressing because it may indicate that the VIB bottleneck is too aggressive for fine-tuned representations, or that CTC is not the ideal task loss for the VIB objective on those models.

- **No error bars or standard deviations in Table 1.** The paper states "Scores are averaged over three runs with different random seeds" but reports only point estimates without variance. Given the modest (1–4%) differences between some conditions (e.g., Wav2Vec2-Base emotion: 61.4 probing vs. 58.9 VIB), it is unclear which differences are significant.

- **Layerwise analysis interpretation confound (Section 6).** The decline in acoustic contribution in fine-tuned models' final layers is measured by probing the acoustic latents, which are task-specific. It is not clear whether this reflects less acoustic information in the original hidden states, or simply that the VIB encoder learns to ignore it because it is not needed for emotion. The paper's interpretation favors the former but does not disentangle these possibilities.

### Trivial

- **Typo: "WER=1" instead of "WER=100" for the random baseline (line 194).** The figure caption correctly says WER=100. The body text has a typo.

## Nice-to-Haves

- Performing sanity-check probing on IEMOCAP itself (probing textual latents for acoustic features and acoustic latents for transcription) would directly address the domain mismatch concern and substantially strengthen the paper.
- Including at least one alternative disentanglement method (e.g., an adversarial baseline) would help calibrate the contribution.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Conditioning" mechanism criticized as heuristic / not rigorous.** The paper's stage 2 uses concatenation of z_textual with z_acoustic before the classifier head, with KL penalty on z_acoustic. Concatenation is a standard conditioning mechanism, and the KL penalty combined with frozen z_textual creates valid disentanglement pressure. The paper describes the approach accurately and does not claim a formal theoretical derivation beyond the standard VIB framework. This criticism is overly strict.

- **Data description inconsistency (5,000 samples vs. hours).** The numbers are consistent: 5,000 from each of two corpora = 10,000 total; 1,000 test from each = 2,000 test, 8,000 train; 17.4 training hours / 8,000 ≈ 7.8 sec average, 3.2 test hours / 2,000 ≈ 5.8 sec average. These are reasonable.

- **Acoustic latents not capturing all acoustic features.** The paper explicitly addresses this (Section 5.1): "not all those acoustic features encoded in the hidden representations are crucial for recognizing emotion, thus, not all of those features were retained in stage 2." The framing is appropriate as-is.

- **t-SNE uses RAVDESS not IEMOCAP.** The paper motivates this choice explicitly: RAVDESS has constant linguistic content across emotions, making it ideal for visualizing disentanglement. This is a deliberate, well-reasoned methodological choice.

- **Attribution section too preliminary.** The paper transparently states: "While a comprehensive evaluation of disentangled attribution is beyond the scope of this work, we do conduct a preliminary investigation." Criticizing it for being preliminary is scope creep.

- **WER=1 typo removed** — it's kept above as a Trivial weakness, not fully removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Probe textual and acoustic latents on IEMOCAP.** The single highest-leverage addition would be to run the same sanity-check probing (for both textual and acoustic information) on the IEMOCAP utterances used in the emotion experiments, confirming that the disentanglement holds in that domain.

2. **Report standard deviations for Table 1.** Since three seeds are run, reporting variance would greatly improve the reader's ability to assess which differences are meaningful.

3. **Specify the IEMOCAP data split procedure clearly.** State whether leave-one-session-out or another speaker-independent protocol was used; if a random split was used, discuss potential speaker overlap.

4. **Discuss the HuBERT-FT Large WER degradation.** The gap (25.6 vs. 6.9 probing) deserves explanation — is it due to the VIB bottleneck being too aggressive for fine-tuned representations, or a mismatch between CTC and VIB on that model?

5. **Consider including a simple disentanglement baseline** (e.g., an adversarial approach that penalizes text predictability from acoustic latents) to help contextualize the VIB framework's contribution.
