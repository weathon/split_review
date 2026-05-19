- Decision: Reject
- Avg Score: 4.20
- Scores: 6, 6, 1, 3, 5
Now I have verified all claims against the paper. Let me construct the final consolidated review.

---

## Summary

This paper proposes a two-stage controllable TTS system using a masked-autoencoder-learned discrete style representation as an intermediary. In the first stage, an autoregressive transformer generates style tokens conditioned on phonemes and discrete control labels (age, gender, pitch, emotion, SNR, C50). In the second stage, a separate acoustic LM generates codec tokens from phonemes and the predicted style tokens. The key insight is that the style generation stage can be trained on large, lower-quality corpora (GigaSpeech-xl, 10k hours) without requiring high-quality paired data, addressing the data scarcity issue that plagues natural-language-controlled TTS. Classifier-free guidance is applied to the style LM to improve fine-grained control accuracy.

---

## Strengths

- **Two-stage design that decouples data-quality requirements**: The paper clearly identifies and exploits an asymmetry — style generation can use large, noisy data (10k hours of GigaSpeech) while acoustic generation only needs a few hundred hours of clean data. Section 3.3 explicitly motivates this separation, and the experiments (Figure 3, 4) show the two-stage system maintains stable WER and UTMOS across CFG scales while the one-stage LibriTTS-trained baseline degrades. This is a practical contribution that directly addresses a known bottleneck in controllable TTS.

- **MAE-learned style representation captures rich prosodic and acoustic information beyond speaker identity**: Reconstruction results (Table 2) show that speech synthesized from phonemes + ground-truth style tokens achieves significantly lower MCD than zero-shot TTS systems (YourTTS, XTTS-V2), while maintaining comparable UTMOS and speaker similarity. This demonstrates the style tokens encode fine-grained prosody and acoustic environment, not just speaker timbre.

- **Classifier-free guidance is shown to substantially boost fine-grained control**: Figure 4 shows that for attributes with ambiguous category boundaries (e.g., pitch std, age), applying CFG at scale 3–7 increases control accuracy from near-chance levels to >80%. The paper also notes the practically important finding that applying CFG to speaker embeddings degrades quality, and therefore restricts it to discrete labels (line 117).

- **Correlation analysis and conflict-resolution proposal**: Section 4.4 provides a thoughtful analysis of attribute correlations (e.g., gender↔pitch mean r=0.50, arousal↔pitch std r=0.58) and proposes both statistical and learning-based methods to resolve conflicting control signals. This demonstrates awareness of real-world deployment challenges and provides a principled path forward.

- **Transparent limitations section**: Section 6 candidly acknowledges labeling tool errors, uneven attribute distributions, and marginal label combinations that cause degraded performance.

---

## Weaknesses

### Fatal
None.

### Major

- **Data-scale confound undermines the headline one-stage vs two-stage comparison**: The one-stage baseline is trained only on LibriTTS (≈585 hours, clean), while the style LM for the two-stage system is trained on GigaSpeech-xl (≈10,000 hours, varied quality). The paper attributes the two-stage model's superior robustness and control accuracy to its architecture ("two-stage design...enhances the robustness"), but the comparison does not control for data scale. A one-stage model trained on GigaSpeech (or a style LM trained on LibriTTS only) would be needed to isolate whether the improvement stems from the architecture or simply from having ~17× more training data. The paper is transparent about the data asymmetry, but the central claim is not properly supported without this ablation.

- **Control accuracy metric is validated only against the same noisy automatic annotations used for training**: The reported control accuracies (70–90% with one-bin relaxation) measure agreement between annotation-tool outputs on generated speech and annotation-tool outputs on ground-truth speech. There is no human perceptual grounding — no listening test asking human judges to identify the intended attribute level. Without knowing how the annotation tools' errors affect the metric, the reported numbers are uninterpretable as evidence of perceptual control. The paper's limitations section acknowledges "errors in the attribute annotations of the training data" but does not address the circularity in evaluation. A small-scale human validation on a subset of attribute contrasts would materially strengthen the claims.

- **No experimental comparison to any natural-language-based controllable TTS system**: The paper's Introduction and Related Work are built around the contrast between discrete attribute labels and natural language prompts, arguing that natural language is "coarse-grained" and "difficult to precisely control specific attributes" (line 12). Yet the experiments contain zero comparisons to PromptTTS, InstructTTS, TextrolSpeech, or any other natural-language-controlled system — even on a shared attribute such as emotion or pitch. The paper's motivating claim that discrete labels provide finer-grained control is therefore entirely untested. This is a significant gap given that the paper positions itself against this line of work.

### Minor

- **Evidence for content-disentangled style representation is incomplete**: The paper supports the claim that style tokens are content-disentangled through (1) the MAE architecture that explicitly separates content and style encoders, and (2) the observation that swapping phonemes and style tokens across samples "fails to generate meaningful speech" (line 152). The latter is a negative result — failure to cross-generate could simply mean the model cannot handle mismatched training-free concatenation, not that the style token is free of content. A stronger test would involve transferring style tokens between utterances and measuring whether content (WER) stays low while style properties transfer. The reconstruction quality and low MCD results (Table 2) provide partial support, but the disentanglement claim is slightly overextended relative to the evidence.

- **No ablation of the MAE auxiliary loss components**: The MAE combines reconstruction, contrastive, pitch classification, and energy classification losses (Section 3.2). The contribution of each individual loss to disentanglement and reconstruction quality is not evaluated. Given that the contrastive and classification losses are inherited from Prosody-TTS (Huang et al., 2023), an ablation would clarify whether all are needed in this setting.

- **No analysis of RVQ codebook count or size**: The choice of 3 codebooks for RVQ tokenization (line 69) is stated but not motivated or ablated. Since this affects the granularity of the style representation and the sequence length for both LMs, a brief ablation would be informative.

### Trivial
None.

---

## Nice-to-Haves

- **Ablation: data scale controlled.** Train the style LM on LibriTTS only (same data as the one-stage baseline) to isolate the architectural benefit from the data scale benefit. Alternatively, if feasible, train a one-stage model on a large subset of GigaSpeech to see if the two-stage advantage persists.

- **Human listening test for control accuracy.** A small-scale test (e.g., 20 attribute contrasts × 10 listeners) asking humans to identify the intended attribute level (low vs high pitch, happy vs sad emotion) would directly validate the control metric.

- **Comparison to a natural-language-based controllable TTS.** Even one attribute (e.g., emotion on a shared test set) would contextualize the claimed advantage of discrete labels.

- **Computational cost comparison.** The two-stage system uses two autoregressive transformers plus a codec decoder. Reporting inference speed or model size relative to the one-stage baseline would help practitioners assess the practical trade-off.

---

## Removed Points

- **"Table 1 is only an image placeholder; actual data sizes and splits not readable"** — This is a PDF extraction artifact. The text provides data sizes and splits verbally (line 126–128).

- **"Missing numerical values in tables"** — PDF extraction artifact. The tables are present in the original submission.

- **"No discussion of why GigaSpeech not used for CT LM or one-stage baseline"** — The paper addresses this: Section 3.3 states "several hundred hours of data are sufficient for the model to learn to reconstruct speech of decent quality" for the acoustic LM; the one-stage baseline similarly generates codec tokens directly and requires cleaner data.

- **Criticisms about formatting, typos, or presentation** — Not assessable from the raw extraction; these are parsing artifacts, not author errors.

- **"The paper could be stronger by showing each loss improves disentanglement"** — Valid as a suggestion but converted to a Minor weakness (ablation missing) rather than a central criticism.

---

## Novel Insights

The reviewers' strongest converging insight is that the paper's central comparison (one-stage vs two-stage) is confounded by data scale, which the authors explicitly acknowledge yet do not control for. What is genuinely useful about the review process is the observation that this confound could be resolved by a single additional experiment (style LM trained on LibriTTS only), and that the paper's own framing implicitly treats this as a feature rather than a bug — the two-stage design is valuable *specifically because* it allows using larger, lower-quality data. The disconnect is between claims about architectural superiority and evidence that actually reflects data scaling. The second useful observation is the circularity of the control metric: the paper evaluates against the same noisy annotation pipeline that produces its training labels, which is a subtle validity threat that the Limitations section acknowledges in spirit but does not fully address.

---

## Suggestions

1. Add an ablation where the style LM is trained on LibriTTS only (matching the one-stage baseline's data) and compare to the full GigaSpeech-trained version. This cleanly separates architecture from data scale.
2. Conduct a small human listening test for attribute discrimination (e.g., low vs high pitch, happy vs sad emotion) on at least one test set to validate that the reported control accuracy corresponds to perceptible differences.
3. Add at least one comparison to a natural-language-based controllable TTS system (e.g., TextrolSpeech) on a shared attribute and test set to substantiate the paper's motivating contrast.
4. Report the WER for the ground-truth style token reconstruction (Table 2) explicitly in the text, to quantify content preservation when style representation is used.

---
