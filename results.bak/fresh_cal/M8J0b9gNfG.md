Now I have all the evidence I need. Let me produce the final consolidated review.

## Summary
This paper presents the first sentence-level multilingual Visual Speech Recognition system using a single model. The core innovation is the **visual speech unit** — a quantized 10-bit discrete token obtained from a multilingual self-supervised AV-HuBERT (mAV-HuBERT) — which compresses a video frame to 0.016% of its original size and enables a fast unit-to-text pre-training stage. A curriculum-learning strategy (audio-visual → visual-only inputs) complements the sparse visual signal, and finetuning on continuous features recovers quantization loss. On five languages, the single model achieves state-of-the-art results among multilingual methods and is best or second-best among all methods (including language-specific) on all five languages.

## Strengths
1. **First sentence-level multilingual VSR with a single model** — The paper explicitly identifies this as a novel contribution, and no prior work exists for this setting. (Abstract, Section 1)
2. **Dramatic data-size reduction validated quantitatively** — A video frame (88×88 grayscale, 61,952 bits) is compressed to a 10‑bit unit — a reduction to 0.016% of the original — which directly supports the efficiency motivation. (Section 3.1)
3. **Strong multilingual VSR results** — Table 7 shows the single proposed model outperforms language-specific state-of-the-art methods on 3/5 languages (Es, It, Fr) and achieves second-best on En and Pt. The paper transparently discusses the English gap (24.4% vs. 20.5% WER) as a consequence of the "curse of multilinguality." (Section 4.3.5)
4. **Curriculum learning is shown to be critical** — Table 5 ablations show that removing curriculum dramatically degrades performance, often below the no-pretraining baseline. (Section 4.3.4)
5. **mAV-HuBERT clearly benefits multilingual VSR** — Table 2 shows that mAV-HuBERT (multilingual pretraining) outperforms English-only AV-HuBERT by >10% WER on non-English languages, validating the need for multilingual visual speech features. (Section 4.3.1)
6. **Analysis validates the design rationale** — Figure 2 shows qualitative alignment between visual speech units and viseme families; Table 4 shows speaker verification EER drops from 2.38% (raw audio) to 32.74% (visual speech unit), confirming that quantization suppresses speaker information while preserving linguistic content. (Section 4.3.3)
7. **Efficiency gains quantified on the same hardware** — Table 3 reports a 12× speedup in pre-training time (6.6 h vs. 52.5 h) with 6× larger batch size, measured on identical GPU hardware. (Section 4.3.2)
8. **Systematic ablation study** — Table 5 tests removal of each proposed component (unit pretraining, curriculum learning, finetuning), showing that all contribute positively. (Section 4.3.4)

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Comparison with monolingual baselines lacks data-size context.** The paper claims "comparable performances" to language-specific models (Table 7), which is a reasonable characterization, but it does not report the training data sizes of the cited monolingual baselines. Since those baselines are trained on language-specific datasets of unknown size, readers cannot fully calibrate the performance trade-off between multilingual coverage and per-language accuracy. The paper's own discussion of the "curse of multilinguality" partially mitigates this, but transparency about the baseline data budgets would strengthen the comparison. (Section 4.3.5, Table 7)

- **Efficiency comparison (Table 3) is ambiguous about what "Previous VSR" entails.** The paper compares the proposed pre-training (6.6 h) against a "standard VSR method" (52.5 h) but does not specify which architecture, training configuration, or data setup the baseline uses. Moreover, the efficiency claim focuses on the unit-to-text stage and does not account for the one-time cost of training mAV-HuBERT (350k steps, 64 GPUs). While this one-time cost is standard for self-supervised feature extractors and would be amortized across many downstream tasks, the paper should clarify the scope of the comparison to avoid misleading readers. (Section 4.3.2, Table 3)

- **The `–Unit Pretraining` ablation conflates pretraining with architecture differences.** Removing unit pretraining means directly finetuning mAV-HuBERT (an encoder-only model) on video-text with an unspecified prediction head, whereas the full method uses unit-to-text pre-training followed by finetuning of an encoder-decoder. The observed WER gap could partly reflect this architecture mismatch rather than purely the value of discrete pretraining. The paper's other comparisons (e.g., Table 6 vs. AV-HuBERT) also support the method's effectiveness, so this does not threaten the core claim, but the ablation itself is confounded. (Section 4.3.4, Table 5)

- **Language identification accuracy with Whisper is not reported.** The paper uses Whisper for language identification on VoxCeleb2 and AVSpeech to filter the mAV-HuBERT training data (9 languages). No accuracy or error analysis of this step is provided, making it difficult to assess potential data-quality issues from misidentified utterances. (Section 3.1)

- **Automatic label quality is not discussed.** A substantial portion of the 4,545-hour VSR training set uses automatically generated transcripts from Ma et al. (2023) and Yeo et al. (2023c). The expected noise level (e.g., WER of the labeler on a held-out gold subset) is not reported, which would help readers understand the robustness of the method and the reliability of the reported results. (Section 3.2, Table 1)

- **No statistical significance or variance reporting.** The key comparison tables (Tables 6, 7) report single WER values. Without multiple runs or bootstrap confidence intervals, it is unclear whether the observed differences (especially 1–2% gaps) are significant. (Section 4.3)

- **Phoneme/viseme mapping analysis is qualitative only.** The visualization of 200 out of 1,000 units (Fig. 2) is suggestive but lacks a quantitative metric (e.g., purity, NMI, or accuracy of unit-to-phoneme alignment) to support the claim that units align with visemes. (Section 4.3.3, Fig. 2)

### Trivial
- The architecture used for the AV-HuBERT multilingual VSR baseline (Table 2) — i.e., how the encoder-only AV-HuBERT is adapted for sequence-to-sequence VSR — is not specified, making the comparison less precise.
- "Previous VSR" in Table 3 would benefit from a specific citation or model name.

## Nice-to-Haves
- Testing alternative masking schedules for the curriculum learning (e.g., exponential, step-wise) would strengthen the claim about the specific schedule choice, though the "with vs. without" ablation already validates the basic idea.
- Adding a quantitative metric for unit-to-phoneme alignment would strengthen the analysis in Section 4.3.3.
- An evaluation on a genuinely low-resource language (e.g., Greek or Arabic from the mAV-HuBERT set) would showcase the method's value for languages with very limited paired data.
- A brief analysis of the training loss curves during pre-training (unit-to-text accuracy on a held-out set) would help illustrate the dynamics of curriculum learning.

## Removed Points
These points were raised in the reviews but are excluded from the main weaknesses above for the following reasons:

- **Critical Issue 4 (curriculum schedule alternatives)** — The paper's ablation tests "with curriculum" vs. "without curriculum," which is the standard and sufficient test for establishing that a component is helpful. Requesting tests of alternative schedules is scope creep beyond what is needed to validate the core claim.
- **Abstract claim about quantization vs. feature extraction** — The harsh critic argued that the abstract should specify that quantization, not feature extraction, suppresses speaker info. However, the paper already clearly states (Section 4.3.3, line 156) that "the quantization process averages out the speaker effects." The abstract's phrasing is accurate.
- **Speaker verification numbers (32.74% vs. 19.42% EER)** — The critic noted that speaker info is still partially present in units. This is true, but the paper never claims it is *completely* removed; the numbers actually support the claim that suppression occurs (EER rises from 19.42% → 32.74% after quantization). This is not a weakness.

## Novel Insights
The two reviewer inputs largely converge on the assessment that the paper is solid but has presentation and clarity gaps. The most interesting tension is between the harsh critic's claim that the efficiency comparison is "misleading" (because it omits mAV-HuBERT training) and the paper's implicit framing that mAV-HuBERT is a one-time self-supervised pretraining cost — analogous to how all VSR methods using AV-HuBERT would pay a similar upfront cost. Neither reviewer fully engaged with the question of *whether the total pipeline amortizes well*: if mAV-HuBERT is reused for many downstream tasks (VSR, AVSR, speaker recognition, etc.), the per-task cost decreases substantially. This framing could have been made more explicit in the paper to preempt the criticism. Beyond this, no fundamentally novel insight emerges beyond the paper's own contributions.

## Suggestions
1. **Clarify the scope of the efficiency comparison.** Specify the architecture and configuration of the "Previous VSR" baseline in Table 3, and explicitly state that the mAV-HuBERT training cost is excluded because it is a one-time amortizable cost (analogous to any self-supervised pretrained feature extractor). Optionally report total pipeline GPU-hours with and without mAV-HuBERT amortization.
2. **Disentangle the `–Unit Pretraining` ablation.** Train an encoder-decoder from scratch on continuous features (no discrete pretraining) and compare to the full pipeline. This would isolate the contribution of unit pretraining from the architecture choice.
3. **Report data sizes for the monolingual baselines in Table 7** to enable fairer calibration of the "comparable" claim. A brief discussion of how data availability and model capacity trade off against multilinguality would strengthen the framing.
4. **Add statistical reporting.** Report variance across multiple runs or bootstrap confidence intervals for key comparison tables, especially where gaps are small (1–2% WER).
5. **Briefly analyze label quality.** A short paragraph reporting the WER of the automatic labelers (Ma et al. and Yeo et al.) on a held-out subset would help readers assess data reliability.
6. **Report Whisper language-ID accuracy** on a known-language set to validate the mAV-HuBERT data filtering step.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>