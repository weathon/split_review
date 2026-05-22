Now I have a thorough understanding of the paper and the calibration landscape. Let me write the final consolidated review.

---

## Summary

This paper proposes USR 2.0, improving the USR semi-supervised framework for unified ASR/VSR/AVSR. The key idea is **CTC-driven teacher forcing**: instead of costly autoregressive decoding to generate attention-based pseudo-labels, the teacher's greedily-decoded CTC outputs are fed into the decoder to generate attention targets in a single forward pass. This removes the AR bottleneck and, because both PL types are now length-aligned, the student can predict both simultaneously—coupling the two branches and improving OOD robustness. A **mixed sampling** strategy (50% CTC-driven mode, 50% standard AR mode) mitigates the resulting exposure bias. USR 2.0 achieves ~2× training speedup, state-of-the-art WER on LRS3 (VSR 17.6%, ASR 0.9%, AVSR 0.8% with a Huge model), and substantially improved robustness on long utterances, noisy audio, and cross-dataset shifts.

## Strengths

1. **Novel, well-motivated core idea with clear reasoning.** The observation that "global coherence is irrelevant in pseudo-labelling because teacher and student share the same conditioning" is insightful and directly supports the CTC-driven teacher forcing design. The paper provides a concise theoretical justification (Section 4.1) that distinguishes the proposed approach from standard teacher forcing.

2. **~2× training speedup with equal or better accuracy** (Figure 5, Section 6). The speedup is driven by two factors: faster per-step PL generation (CTC-driven teacher forcing vs. AR decoding) and faster convergence (50 vs. 75 epochs). This is a practically important result for scaling semi-supervised training.

3. **Dramatically improved OOD robustness** (Section 5). USR 2.0's WER stays flat (~35%) on long VoxCeleb2 utterances up to 600 frames, while USR's rises to ~100% under greedy decoding (Figure 3a). Large margins are also shown on LibriSpeech (15.4% vs. 25.3%), WildVSR (73.7% vs. 80.0%), and across noise levels (Table 1). These results directly validate the claim that coupled CTC-attention supervision improves robustness.

4. **State-of-the-art in-distribution results with a single unified model** (Table 2, Section 6). USR 2.0 matches or outperforms modality-specific methods (AV-HuBERT, BRAVEn, etc.) across VSR, ASR, and AVSR in both low- and high-resource settings. The Huge model sets new SOTA on LRS3 while using a single set of parameters—a meaningful practical advance.

5. **Informative ablations** (Table 4, Figure 4). Table 4 cleanly isolates the contribution of each PL type to ID and OOD performance. Figure 4 reveals the accuracy–robustness–efficiency trade-off controlled by the AR-mode sampling probability, giving practitioners a principled tuning knob. The ablation analysis is well-designed and directly supports the design choices.

## Weaknesses

### Fatal
None.

### Major
- **No variance or confidence-interval reporting.** None of the main tables (Tables 1–4) report error bars, standard deviations, or multiple-run statistics. Several comparisons are close (e.g., USR vs. USR 2.0 at Base level on LRS3: VSR 36.0% vs. 36.2%, ASR 3.2% vs. 3.0%, AVSR 3.0% vs. 2.9%). Without variance estimates, the reader cannot determine whether these differences are systematic or noise. This is standard practice to address in this community and would significantly strengthen the paper's claims.

### Minor

- **Whisper as an oracle for OOD evaluation.** The VoxCeleb2 (Figure 3) and AVSpeech evaluations use Whisper-generated transcripts as pseudo-ground-truth. The paper acknowledges this ("automatically transcribed," "treating Whisper...as an oracle"), and relative comparisons across methods remain valid since the same transcripts are used. However, if Whisper's errors correlate with utterance length or domain (e.g., higher WER on long or accented speech), the absolute WER numbers could be biased. A brief qualitative analysis (e.g., manually inspecting a sample of Whisper transcripts on this data) would increase confidence in the absolute numbers.

- **Encoder initialization not fully specified in the main text.** Section 4.3 states "Our implementation follows USR" and references Appendix A for full details. In the original USR paper, the encoder was initialized from an AV-HuBERT checkpoint. This is an important detail for fair comparison with self-supervised baselines and should be stated explicitly in the main text rather than deferred to an appendix.

- **Convergence speed claim not directly shown.** The paper claims faster convergence (50 vs. 75 epochs, Appendix C.5) but Figure 5 only shows wall-clock time. A plot of WER vs. training step/epoch would cleanly separate whether the speedup comes from faster steps, fewer steps, or both.

### Trivial
None.

## Nice-to-Haves

- **ASR- and VSR-specific ablations of mixed sampling.** Figure 4 shows only AVSR. Since Table 2 shows larger VSR gains than ASR gains from USR 2.0, it would be informative to see whether a different sampling probability is optimal for each modality.

- **Qualitative analysis of long-utterance outputs.** For the VoxCeleb2 evaluation, showing example transcripts from USR vs. USR 2.0 on a long sample (e.g., 400+ frames) would illuminate whether the flat 35% WER arises from complete-but-errorful transcripts or truncated/trivial outputs.

- **Analysis of the student decoder's learned conditioning.** The paper argues that the student learns a mapping from CTC prefix to next-token prediction. Reporting perplexity of the student decoder under AR decoding (without CTC scoring) on a held-out set would provide supportive evidence.

## Removed Points
- *"Missing appendix reference"* (harsh critic): The parser strips appendix content from all papers. This is a PDF extraction artifact, not a submission error. Removed per hard rule.
- *"Training schedule details not in main text"* (harsh critic): These are deferred to Appendix A (standard practice). Removed per hard rules about appendix content.
- *"Missing related work"* (strength finder, not raised; generic related-work gaps): Per hard rules, I cannot verify the existence of missing references. Removed.
- *"AB clearly stronger than USR in base model LRS3 VSR"* (strength finder's interpretation of Table 2 where USR 2.0 VSR is 36.2% vs USR's 36.0%): This is actually slightly worse, not better. Misreading by the strength finder. Removed.
- Various formatting/style nitpicks and speculative "could be" concerns. Removed per filtering rules.

## Novel Insights

The harsh critic identifies the core insight well: the paper's key conceptual contribution is that **within a self-training loop, the global coherence of teacher-generated sequences is irrelevant** because teacher and student are conditioned on the same input. What matters is the local next-token mapping under the shared prefix. This reframing—borrowing teacher forcing from supervised learning but substituting CTC outputs for ground-truth tokens—is transferable beyond speech to any seq2seq setting with monotonic alignment and large unlabelled corpora. The paper's empirical demonstration that this substitution actually *improves* OOD robustness (rather than merely trading off accuracy for speed) is a non-obvious result with practical significance.

## Suggestions

1. **Report standard deviations or confidence intervals** for the main results (at minimum Tables 1–2) over 3 random seeds. If compute is limited, bootstrap confidence intervals on the test sets would also help.
2. **Explicitly state the encoder initialization** (AV-HuBERT or otherwise) in Section 4.3.
3. **Include a WER-vs-epoch plot** to separate the contributions of faster steps vs. faster convergence to the overall speedup.
4. **Add a brief qualitative check** of Whisper transcription quality on a sample of VoxCeleb2 utterances, to bound the oracle confound.

## Score and Decision

**Round-1 bracket: [6, 8]**

Anchors from round 1:
- UFwefiypla (3.00, weak) — DM-Codec speech tokenization. Much weaker paper with unclear contribution.
- 4lOWCkhr4g (5.25, middle-low) — Cross-lingual pseudo-labeling for ASR. Narrower scope, limited novelty.
- CIs9x2ZRgh (6.75, middle) — CR-CTC for improved ASR. Simple method, modest gains, reproducibility concerns.
- tyEyYT267x (8.00, strong) — Interpolating AR and diffusion LMs. Unanimous accept, different domain.

**Round-2 anchors:** Narrowed to (6.0, 8.0):

- CIs9x2ZRgh (6.75) — CR-CTC. This paper clearly surpasses it in method novelty, evaluation breadth, and result significance.
- fUGhVYPVRM (7.00) — Align With Purpose. Well-written CTC paper with solid latency results. This paper has stronger empirical results and a more novel method.
- WEQL5ksDnB (6.75) — CAV2vec. Similar domain (AVSR robustness). This paper's method is more novel; CAV2vec had concerns about being an incremental extension of AV-HuBERT/data2vec.
- TtKN1TpvUu (6.25) — T2V2. Unified ASR+TTS with limited novelty and non-SOTA ASR. This paper is clearly stronger.
- M8J0b9gNfG (6.20) — Multilingual VSR. Limited novelty over AV-HuBERT. This paper has a more novel method.

**Comparison:** The paper under review is stronger than all round-2 anchors in terms of method novelty, empirical thoroughness, and result quality. The weaknesses (no variance reporting, Whisper oracle) are real but addressable and do not threaten the core claims. The paper comfortably sits above the strongest round-2 anchor (AWP at 7.00).

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>