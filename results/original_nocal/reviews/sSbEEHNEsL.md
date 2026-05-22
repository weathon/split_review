Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper proposes USR 2.0, an improvement to the USR framework for unified audio-visual speech recognition. The core idea is CTC-driven teacher forcing: instead of slow autoregressive decoding to generate attention-based pseudo-labels, the teacher's greedily-decoded CTC outputs are fed into the decoder to generate attention targets in parallel. This is coupled with a mixed sampling strategy that alternates between CTC-driven and autoregressive modes to mitigate exposure bias. The method achieves ~2× faster training, substantially improved robustness to out-of-distribution inputs (long utterances, noise, unseen domains), and state-of-the-art in-distribution results on LRS3, LRS2, and WildVSR across ASR, VSR, and AVSR with a single unified model.

## Strengths

1. **Nearly 2× faster training with clear evidence**: Figure 5 shows across multiple model scales and pre-training datasets that USR 2.0 reaches lower WER in roughly half the wall-clock training time of USR. The paper explicitly attributes this to both faster per-step decoding (CTC-driven teacher forcing) and faster convergence (50 epochs vs. 75), providing a concrete and practically meaningful efficiency gain.

2. **Consistent and substantial out-of-distribution robustness**: Table 1 (noise at multiple SNRs), Figure 3a–b (long utterances up to 600 frames), and Table 3 (three unseen OOD datasets: LibriSpeech, WildVSR, AVSpeech) all show USR 2.0 outperforming USR and strong self-supervised baselines (AV-HuBERT, BRAVEn) by wide margins under distribution shift. The result is particularly striking because the gap grows precisely where CTC's monotonic alignment helps (long sequences, noisy conditions).

3. **State-of-the-art in-distribution performance with a single unified model**: Table 2 reports that USR 2.0 achieves the best or second-best WER across low- and high-resource settings on LRS3 for all three tasks (VSR, ASR, AVSR) while using a single shared-parameter model, surpassing even methods that train separate per-modality models. Scaling to a Huge model yields 0.8% AVSR WER.

4. **Well-structured ablation study**: Table 4 systematically ablates pseudo-label targets in both CTC-driven and AR modes, showing that both CTC and attention targets contribute to ID and OOD performance. Figure 4 carefully characterizes the trade-off between ID accuracy, OOD robustness, and training time as a function of the mixed-sampling probability, providing practical guidance.

5. **Scalability demonstrated without degradation**: Section 6 shows that scaling USR 2.0 to a Huge model on ~2500 hours of unlabelled data yields strong results (0.8% AVSR), demonstrating the method does not degrade at larger capacity.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **OOD evaluations rely on Whisper as oracle without validation on human-transcribed samples.** The OOD results in Figure 3 (VoxCeleb2) and Table 3 (AVSpeech, LibriSpeech) use Whisper transcriptions as ground truth. The paper explicitly acknowledges this ("treating Whisper... as an oracle"), and *relative* comparisons between methods remain valid. However, Whisper has known biases on accented or noisy speech that could differentially affect reported WER magnitudes. A small-scale validation with human transcriptions on a subsample would strengthen confidence in the absolute WER figures, especially for the strongest claim about OOD robustness (e.g., the gap between USR and USR 2.0 on LibriSpeech in Table 3: 25.3% vs. 15.4%).

2. **Mechanism of robustness improvement is not fully isolated from multi-task learning.** In CTC-driven mode (Table 4, row 1), the decoder predicts both CTC PLs and attention PLs simultaneously. Removing CTC PL supervision from the decoder (row 2) drastically increases OOD WER from 24.2% to 35.1%, showing that direct CTC target prediction is a major contributor to OOD gains. The paper attributes the robustness primarily to CTC-driven teacher forcing, but it is possible that the same multi-task loss (predicting CTC targets in the decoder) applied alongside AR-generated attention PLs would also improve robustness. This control is infeasible in its pure form (AR-mode PLs have different lengths), but the mechanistic interpretation is therefore underdetermined by the presented evidence. The empirical benefit of the overall method is clear; the *reason* for it is less precisely pinned down.

3. **The "self-reinforcing error" claim motivating the method is not directly measured.** Section 3 states that decoupled supervision causes "errors [to be] reinforced in the training loop" and that "noisy AR PLs supervise the student, which can then degrade the teacher via EMA updates." While this is a plausible motivation and consistent with the overall results (USR 2.0 outperforms USR on OOD), no experiment tracks pseudo-label quality over training (e.g., per-step WER of teacher-generated PLs on a held-out set) to directly demonstrate this effect or quantify its magnitude for USR vs. USR 2.0.

### Trivial
None.

## Nice-to-Haves

- **Human-transcribed validation of OOD data**: A small subsample (100–200 utterances) of VoxCeleb2 or AVSpeech with human transcriptions would validate that Whisper oracle bias does not drive the main OOD conclusions.
- **Training time breakdown**: A decomposition of per-step time into encoder forward, CTC decoding, decoder forward (CTC-driven vs. AR), and loss computation would clarify how much of the ~2× speedup comes from faster teacher passes vs. fewer iterations.
- **Example outputs**: A few qualitative examples of CTC-driven vs. AR attention PLs on OOD samples would help readers assess the "global incoherence" claim concretely.

## Removed Points

These points from the Harsh Critic/Strength Finder are flagged for removal; treat them with caution:

1. **"Incremental novelty" assessment**: The critic's characterization of the method as "a clever tweak, not a breakthrough" is a subjective framing rather than a specific, verifiable weakness. The paper's contribution — replacing AR pseudo-label generation with CTC-conditioned teacher forcing — is clearly defined, non-obvious, and produces significant empirical gains.
2. **Concern about baseline comparison fairness (self-supervised vs. semi-supervised paradigms)**: The critic noted that AV-HuBERT/BRAVEn use a different training paradigm (pre-training + fine-tuning) than USR. The paper compares them within the same low-resource labelled-data setting (30h LRS3), which is standard. The critic concluded this comparison is fair. No weakness remains.
3. **Concern about training time not being "controlled" for overheads**: The critic suggested the speedup could partly reflect a suboptimal USR schedule. The paper provides actual wall-clock training time comparisons (Figure 5) showing ~2× improvement across multiple model scales, which is the most practically relevant metric. This is not a weakness.
4. **Strength Finder's framing of "addressed an important problem" / generic motivation praise**: Removed as generic/superficial. Only strengths with concrete empirical anchors were retained.

## Novel Insights

The most interesting observation to emerge from cross-referencing the reviews against the paper is the unresolved tension between the paper's mechanistic claim and the ablation evidence. The paper argues that CTC-driven teacher forcing transfers robustness to the decoder, but Table 4 row 2 reveals that removing the *CTC target* from the decoder's loss (while keeping CTC-conditioned input) causes OOD WER to jump from 24.2% to 35.1%. This suggests that the robustness gain may be substantially driven by multi-task learning (predicting CTC targets in the decoder) rather than (or in addition to) the conditioning itself. The ideal control — training the decoder with CTC targets alongside AR-generated (not CTC-driven) attention PLs — is structurally infeasible because AR PLs have different lengths, which the paper correctly notes. This limitation is inherent to the design space but should be acknowledged more explicitly when interpreting *why* the method works. The empirical bottom line (USR 2.0 is faster and more robust) is secure regardless of this ambiguity.

## Suggestions

1. Add a small-scale human-transcribed OOD validation set (100–200 utterances from VoxCeleb2 or AVSpeech) and report whether the relative ranking and approximate magnitudes of WER differences hold.
2. Acknowledge the multi-task learning confound more explicitly: state that the decoder benefits both from being conditioned on CTC outputs and from being supervised with CTC targets, and that the ablation cannot fully separate these two effects because AR-mode attention PLs have incompatible lengths.
3. Track and report pseudo-label WER over training for USR vs. USR 2.0 on a held-out unlabelled set to validate the "self-reinforcing error" motivation directly.
4. Break down the training time speedup into per-step improvement vs. fewer epochs in the main paper to strengthen the efficiency claims.

## Score and Decision

The paper's contribution is substantial and well-supported: it introduces a simple, theoretically-motivated modification to pseudo-labelling that simultaneously improves training speed, OOD robustness, and in-distribution accuracy. The experimental evaluation is thorough across noise, utterance length, and domain shift, and the ablations are informative. The two main limitations — reliance on Whisper as an oracle without human validation, and ambiguity about whether robustness gains come from CTC conditioning or multi-task learning — are real but do not undermine the paper's core empirical findings or practical value. This is a strong paper that clearly surpasses the acceptance bar.

MY FINAL SCORE: <score>8.5</score>
MY FINAL DECISION: <decision>Accept</decision>