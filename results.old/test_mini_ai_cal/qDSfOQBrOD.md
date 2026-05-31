Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes VChangeCodec, a neural speech codec that integrates a voice changer directly into the codec's encoding module via a lightweight causal projection network (Converter). The system uses scalar quantization (replacing RVQ), target-speaker metadata from openSMILE, and a token commitment loss to adapt quantized tokens to a target timbre at the encoder side. The integrated framework achieves 40 ms end-to-end latency with fewer than 1M total parameters. The paper reports strong codec performance (POLQA >4.0 at 6–8 kbps, 70× fewer parameters than DAC) and shows competitive voice conversion quality against SOTA VC models in both objective and subjective evaluations.

## Strengths

- **Strong speech codec performance with ultra-low parameter count.** Table 1 shows VChangeCodec achieves POLQA MOS >4.0 at 6 kbps and 8 kbps, outperforming OPUS, EVS, Lyra2, and EnCodec at comparable bitrates, while using 70× fewer parameters than DAC. This is a genuine engineering achievement for low-bitrate RTC applications.

- **Novel integration of voice conversion into the codec pipeline with verified low latency.** The paper demonstrates that the full pipeline (encoder + converter + decoder) runs in real-time on a smartphone CPU (2 ms per 20 ms chunk), yielding end-to-end latency of ~40 ms (Section 3.2, "Computational latency"). This is clearly lower than the illustrative cascaded latency of 107.5 ms referenced for AC-VC + LPCNet + codec.

- **Lightweight causal projection network with ablation validation.** The Converter (three grouped residual units with causal dilated convolutions) introduces no additional latency. Table 5 systematically ablates metadata input, converter dimension, commitment loss, and encoder freezing, showing each component contributes measurably (e.g., metadata improves speaker similarity by ~2%, commitment loss improves MCD and similarity).

- **Comprehensive evaluation including subjective listening tests.** The paper includes both objective metrics (POLQA, ViSQOL, STOI, DNSMOS, MCD, speaker similarity, ASR word error rate) and subjective tests (N-MOS, S-MOS) for the voice changer mode, alongside DCRMOS subjective tests for the codec mode. The subjective results show VChangeCodec achieving the best S-MOS and second-best N-MOS for a male target timbre (Table 3).

- **Operator-oriented design with explicit privacy considerations.** The ethical statement (Section 6) describes a deployment model where operators manage target timbres and the decoder is immutable, providing a practical framework for mitigating misuse — a consideration rarely addressed in VC research.

## Weaknesses

### Major

- **No cascaded baseline is tested, leaving the central integration advantage unmeasured.** The paper's key claim is that integrating VC into the codec is superior to a separate VC + codec pipeline, yet the experimental comparisons (Tables 2–4) are against *standalone* VC models that operate on raw waveforms without any codec compression step. A fair comparison would require encoding the source with VChangeCodec's encoder, then applying a separate VC model (trained on the same data) to the decoded speech, or evaluating an off-the-shelf VC model followed by a standard codec on the full pipeline. Without this, the paper cannot quantify whether the integration itself — as opposed to the codec's token quality — is responsible for the results. The latency comparison (Section 1, paragraph about AC-VC at 107.5 ms) is illustrative rather than experimental, and the absence of a controlled cascaded baseline undermines the "paradigm shift" framing (line 36).

- **Voice conversion baselines are not compared under equal training conditions.** Table 2 compares VChangeCodec against VC models (Diff-VC, VQMIVC, QuickVC, DDDM-VC, FACodec) that were trained on different datasets (VCTK, LibriTTS, Librilight) with different data quantities, language coverage, and speaker counts. This confounds architectural differences with data effects. The paper partially addresses this by retraining three baselines (Table 4), but the retraining is limited to male timbre data only, uses different training procedures (from scratch vs. finetuning), and only reports three of four metrics for some baselines. While the retrained results still favor VChangeCodec, the lack of a fully controlled comparison weakens the claim of "competitive if not the best performance on all metrics" (Table 2 caption).

### Minor

- **Female timbre subjective evaluation results are not reported in a dedicated table.** The paper states it evaluated six VC systems on two target timbres (one male, one female), but Table 3 shows results only for male timbre. Female timbre subjective scores are mentioned in passing in the text ("in the case of female timbre, our approach has significantly narrowed this gap") but are not presented with the same detail. This is an asymmetric reporting gap.

- **DNSMOS is used as a naturalness metric without validation for the voice conversion task.** DNSMOS was originally trained on noisy speech (speech enhancement) data. While it has been adopted by some VC papers, its applicability to timbre-transformed speech is not established in this paper. The authors do not report correlation between DNSMOS and their subjective N-MOS scores for the VC task, which would help justify this choice. (This is partly mitigated by the inclusion of actual subjective MOS scores, but the paper relies on DNSMOS for many quantitative claims.)

- **Training data for the Converter uses RVC-generated near-parallel data without quality analysis.** The paper generates training pairs using the RVC voice conversion toolkit (Section 4.1). If RVC conversions contain artifacts or incomplete timbre transfer, these would propagate into the training targets. The paper does not analyze the quality of the RVC-generated data, nor does it quantify how the token commitment loss (L_T) behaves when the target speech passes through the same encoder — the encoder may already normalize some speaker information, making the commitment loss easier to satisfy without meaningful timbre adaptation.

- **Only two target timbres are evaluated.** The voice changer is trained and tested on only one male and one female target speaker (1 hour of data each). While the paper frames this as an operator-oriented design with pre-defined timbres, the lack of diversity in target speakers makes it unclear whether the approach generalizes to speakers with different voice characteristics or atypical prosody.

### Trivial

None.

## Nice-to-Haves

- Adding a controlled cascaded baseline (e.g., VChangeCodec's encoder → a lightweight VC predictor → decoder) would directly quantify the benefit of integration.
- Reporting female timbre subjective results in a full table (analogous to Table 3) would close the reporting gap.
- Analyzing RVC-generated data quality (e.g., comparing RVC outputs to ground-truth target speech) would address the training data contamination concern.
- Including confidence intervals or error bars for subjective MOS scores would strengthen the statistical reliability of the N-MOS/S-MOS comparisons.
- Testing the claimed "plug-and-play" compatibility with other codec architectures (e.g., EnCodec, DAC) would substantiate the modularity claim.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The AC-VC latency comparison is cherry-picked"** — REMOVED. The paper uses AC-VC as an *illustrative example* of a lightweight streaming VC model (57.5 ms algorithmic delay per its own paper). The comparison is not presented as a rigorous benchmark but as a motivating example. The harsh critic's counter-suggestions (using QuickVC + EnCodec) are speculative — no specific latency numbers are provided for that combination. This is not a verifiable weakness.

- **"The paper does not clearly differentiate VChangeCodec from StreamVC"** — REMOVED. The paper explicitly lists three key differences in the related work section (lines 59–63): (1) seamless switching between original/VC modes, (2) joint compression and VC by the same codec, (3) lightweight causal projection network between encoder and decoder. The differentiation is present.

- **"MCD correlates poorly with perceptual quality in VC"** — REMOVED (strawman). While MCD has known limitations, it is a standard evaluation metric in the VC literature (used by QuicVC, VQMIVC, FACodec, DDDM-VC, etc.). The paper also includes subjective evaluations and speaker similarity metrics that capture perceptual quality. This is a generic criticism that applies to the entire field, not specifically to this paper.

- **"DNSMOS is not designed for VC"** — DEMOTED to Minor (above). The concern is valid, but the paper mitigates it with subjective tests. It is not a fatal or structural issue.

- **"Metaphor of 'coloring' the source tokens is vague"** — REMOVED (pure style nitpick). The technical description of the Converter (causal convolutions, grouped residual units, concatenation of metadata and tokens) is precise. A metaphorical framing in one sentence does not affect scientific clarity.

- **"Privacy is introduced as a contribution but never technically substantiated"** — REMOVED. The paper's ethical statement (Section 6) describes the deployment model that restricts target timbre configuration to operators. This is a design-level consideration, not a technical guarantee. The paper correctly frames it as an operator-oriented design aspiration rather than a formal security property. Demanding cryptographic proofs for a deployment model described in an ethical statement is scope creep.

- **"The plug-and-play claim is untested"** — DEMOTED to Nice-to-Haves. The paper claims the Converter "can be combined with any end-to-end encoder-quantizer-decoder codec" but only tests it with VChangeCodec. This is a reasonable future-work suggestion, not a weakness that invalidates the paper's core claims.

- **"No comparison of metadata (openSMILE) vs. pre-trained speaker embeddings (ECAPA-TDNN)"** — REMOVED (scope creep). The paper acknowledges this design choice and provides a justification (computational cost). Requesting a full comparison is a nice-to-have.

- **"No noise robustness evaluation for the codec"** — REMOVED. The paper trains on mixed speech (clean + noise) and evaluates on clean speech. Requesting noise robustness evaluation extends beyond the stated scope. The codec is designed for voice communication, not general audio.

- **"No discussion of bitrate vs. VC quality trade-off"** — MOVED to Nice-to-Haves. This is a useful extension but not a required experiment.

- **"No speaker adaptation / few-shot fine-tuning discussion"** — REMOVED. The paper's scope is operator-defined target timbres, not few-shot adaptation. This is scope creep.

- **"No switching latency or audio artifacts during mode changes"** — MOVED to Nice-to-Haves. A practical concern for deployment but not required for a research paper.

- **Strength Finder's generic strengths** — REMOVED. Claims about "addressing an important problem" and "scalable plug-and-play converter design" that are generic or unsupported by evidence are dropped.

- **Strength Finder's "best speaker similarity (91.51%) and lowest MCD (5.76)"** — KEPT (supported by Table 2). But the caveat about different training data is noted in Weaknesses.

- **"Codec is too computationally expensive"** (not actually raised) — N/A.

## Novel Insights

The most valuable synthesis from the reviews is that the paper has two separable contributions — (1) a parameter-efficient speech codec that is genuinely competitive with DAC at 70× fewer parameters, and (2) a token-level VC integration module — but the evaluation conflates them in a way that makes it impossible to disentangle how much the VC result depends on the codec's token quality versus the Converter design. The codec contribution (Table 1) is well-validated and could stand on its own. The VC contribution is promising but would be materially strengthened by a controlled experiment that isolates the integration benefit: compare against a cascaded baseline using exactly the same encoder (without the Converter) feeding a separately trained lightweight VC module. The absence of this experiment is the single most impactful gap.

## Suggestions

1. **Add a cascaded baseline.** Use VChangeCodec's encoder (without Converter) → a lightweight VC predictor (e.g., a small projection network trained on the same data) → decode. This directly isolates the benefit of integration from the benefit of the codec's token quality.

2. **Retrain all VC baselines on the same parallel data** used for VChangeCodec (RVC-generated VCTK/AISHELL-3 pairs), with matched training steps and resources, and report all metrics for both male and female timbre.

3. **Report female timbre subjective results** in a dedicated table comparable to Table 3, with sample sizes and confidence intervals.

4. **Analyze the RVC-generated training data** quality — e.g., measure speaker similarity and MCD between RVC outputs and ground-truth target speech — to verify that the training targets are not degraded.

5. **Include confidence intervals** for all subjective MOS scores and for key objective metrics where run-to-run variance is expected.

6. **Temper the "paradigm shift" framing** (line 36) and the "competitive if not the best" claim to accurately reflect the limitations of the baseline comparison.

---

**Round 1 (bracketing) anchors:**

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|------------------------|
| /home/wg25r/split_review/datasets/ai_review_cal/pWdkM9NNCA.md | 3.00 | R1 (weak) | Much weaker — evaluation fundamentally flawed |
| /home/wg25r/split_review/datasets/ai_review_cal/2JXe3RprGS.md | 3.00 | R1 (weak) | Much weaker — different domain (driving navigation) |
| /home/wg25r/split_review/datasets/ai_review_cal/m4mwbPjOwb.md | 3.00 | R1 (weak) | Weaker — Simple-TTS lacks rigorous evaluation vs. strong baselines |
| /home/wg25r/split_review/datasets/ai_review_cal/JOBokGDcX0.md | 2.50 | R1 (weak) | Much weaker — different domain (chunk overlap) |
| /home/wg25r/split_review/datasets/ai_review_cal/KCVv3tICvp.md | 5.00 | R1 (middle) | **Comparable** — both have clean core contributions but evaluation gaps (no external TTS comparison vs. unfair VC baselines) |
| /home/wg25r/split_review/datasets/ai_review_cal/anQDiQZhDP.md | 5.50 | R1 (middle) | Stronger — Vevo has cleaner VC experimental design with controlled data |
| /home/wg25r/split_review/datasets/ai_review_cal/TJNCnkDRkY.md | 5.25 | R1 (middle) | Slightly stronger — GPST has fair VALL-E comparison but missing ablations |
| /home/wg25r/split_review/datasets/ai_review_cal/3sfOGsBh85.md | 4.75 | R1 (middle) | Comparable — CerebroVoice has genuine dataset contribution but multiple evaluation gaps |
| /home/wg25r/split_review/datasets/ai_review_cal/bWcnvZ3qMb.md | 8.00 | R1 (strong) | Much stronger — FITS is a clean, well-evaluated contribution |
| /home/wg25r/split_review/datasets/ai_review_cal/xXTkbTBmqq.md | 8.67 | R1 (strong) | Much stronger — OLMoE is a full open-source release with extensive ablations |
| /home/wg25r/split_review/datasets/ai_review_cal/vf5aUZT0Fz.md | 8.00 | R1 (strong) | Much stronger — DEPT has clean experiments across multiple settings |
| /home/wg25r/split_review/datasets/ai_review_cal/xoXn62FzD0.md | 8.00 | R1 (strong) | Much stronger — different domain (SMC for LLM generation) |

**Round 2 (narrowing) anchors:**

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|------------------------|
| /home/wg25r/split_review/datasets/ai_review_cal/BomQa84efw.md | 5.40 | R2 | Stronger — dMel has cleaner experiments but narrower scope |
| /home/wg25r/split_review/datasets/ai_review_cal/anQDiQZhDP.md | 5.50 | R2 | Stronger — Vevo has cleaner VC comparisons with controlled data |

**Bracket determination:** Round 1 placed the paper clearly in the middle band (3.5–7.5), with strong anchors at ~8.0 being clearly better, weak anchors at ~3.0 being clearly worse. The most relevant middle-band anchors (4.75–5.50) all have evaluation gaps but cleaner experimental designs on narrower scope.

**Final positioning:** This paper is comparable to the Codec-LM co-design paper (5.00) but slightly weaker than GPST (5.25), dMel (5.40), and Vevo (5.50) due to the significant confounds in the VC baseline comparisons and the absence of a cascaded baseline. The codec contribution (Table 1) is strong, but the VC evaluation does not meet the same standard of rigor. Score set at 4.5.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>