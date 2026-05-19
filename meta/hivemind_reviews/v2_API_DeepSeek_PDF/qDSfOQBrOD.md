## Summary
This paper presents VChangeCodec, a neural speech codec with a built-in voice changer for real-time communication (RTC). The key idea is to integrate a lightweight causal projection network (Converter) between the encoder and decoder of a speech codec, enabling timbre adaptation at the token level without additional end-to-end latency. The system supports seamless switching between original voice mode and customized voice-change mode. Using scalar quantization instead of residual vector quantization, VChangeCodec achieves 0.97M parameters and 40 ms end-to-end latency. Experiments compare the codec quality against OPUS, EVS, Lyra2, Encodec, and DAC, and the VC capability against VQMIVC, Diff-VC, QuickVC, DDDM-VC, and FACodec.

**Core Contributions (C1-C3):**
- **C1**: A lightweight (0.97M param) speech codec with integrated VC, achieving 70x parameter reduction vs DAC with comparable objective quality.
- **C2**: A causal projection network (Converter) that performs token-level timbre adaptation, enabling seamless mode switching and compatibility with other encoder-quantizer-decoder architectures.
- **C3**: 40 ms ultra-low-latency integrated VC-codec pipeline that addresses the gap between cascaded VC-codec systems and RTC latency requirements.

**Note on Novelty Verification:** External literature search was unavailable in this run. Novelty and comparative positioning conclusions are marked as *deferred manual verification* throughout this report. All judgments below are grounded in manuscript evidence and internal consistency audits.

## Strengths
1. **Novel integration of VC into speech codec**: Placing the voice changer module inside the codec's encoder path (rather than as a cascaded pre-processor) is a clean architectural idea that eliminates redundant coding-decoding cycles and reduces cumulative latency. The Converter operates on quantized tokens, which is conceptually efficient.

2. **Impressive parameter efficiency**: At 0.97M parameters, VChangeCodec is remarkably lightweight compared to typical neural codecs (DAC: 76M, Encodec: ~14M). This makes the system practical for edge deployment on smartphones and embedded devices, which is a genuine engineering achievement.

3. **Ultra-low latency**: The reported 40 ms end-to-end latency (architecture + inference on iPhone X) is competitive for RTC applications, where the typical budget is 60-100 ms one-way. The streaming causal design is appropriate for this domain.

4. **Comprehensive ablation study**: Section 4.4 systematically ablates metadata inclusion, Converter dimensions, commitment loss weight, and encoder fine-tuning. This helps isolate which design choices matter for VC quality. The ablation confirming that encoder fine-tuning is unnecessary is a useful practical finding.

5. **Retrained baseline comparison**: Going beyond pre-trained model evaluation by retraining selected VC baselines on the target timbre dataset (Table 4) demonstrates methodological rigor, even if the retraining conditions were not perfectly matched.

6. **Privacy-aware design**: The operator-controlled deployment model (pre-defined timbre embeddings, user-inaccessible configurations) is a thoughtful approach to mitigating voice deepfake risks in RTC services.

## Weaknesses
1. **Limited VC evaluation scope (Major)**: Only 2 target timbres (1 male, 1 female) with near-parallel data from RVC. This does not demonstrate general-purpose VC capability. The "one model per timbre" paradigm contrasts sharply with zero-shot VC systems, and the trade-offs are not explicitly discussed in the main paper.

2. **Metric-task mismatch for VC evaluation (Major)**: DNSMOS is used as a primary VC naturalness metric despite being designed and validated for noise suppression evaluation, not voice conversion. DNSMOS scores showing converted speech outperforming ground truth (OVRL 3.11 vs 3.06) suggest the metric is not capturing VC-specific quality dimensions.

3. **Unfair codec baseline comparison (Major)**: Baseline codecs (DAC, Encodec) are evaluated after downsampling from higher native sampling rates (24-48 kHz) to 16 kHz, which disadvantages them by discarding frequency content they were trained to reproduce. This artificially inflates VChangeCodec's relative scores.

4. **Formula error in token commitment loss (Major)**: Eq. (3) has a typographical error (extra parenthesis), undefined variable ($\hat{x}$), and omits the metadata input to the Converter network, making the loss function incompletely specified.

5. **Incomplete retrained baseline comparison (Major)**: Retrained baselines use different training protocols (from-scratch vs fine-tune, different steps), with VQMIVC showing complete quality collapse (WER 118.96%), undermining the conclusiveness of the comparison.

6. **Related Work deferred to appendix (Moderate)**: The main text Related Work section is one brief paragraph. Key comparisons with StreamVC and StreamVoice are relegated to Appendix A.8, weakening the paper's novelty positioning in the main body.

7. **Overclaiming and promotional language (Moderate)**: Terms like "paradigm shift," "superiority," and "innovative methodology" are used without commensurate evidence. The abstract claims "excels" in timbre adaptation but evaluation covers only 2 target timbres.

8. **No statistical significance testing (Moderate)**: None of the reported metrics (POLQA, ViSQOL, MCD, speaker similarity) include confidence intervals or significance tests. Many metric differences are small (e.g., POLQA 4.10 vs 4.06), making it unclear whether improvements are statistically reliable.

9. **Latency profiling detail (Minor)**: The 40 ms latency claim is based on "2 ms per 20 ms chunk on iPhone X CPU core" but no breakdown into encoder/converter/decoder components is provided, and no comparison runtime on other devices is reported.

10. **Reproducibility gaps (Minor)**: Code is not released; training data mixtures (English + Mandarin ratios, noise mixing details) are underspecified; the RVC data generation pipeline is not documented.

## Key Issues
### Ranked Error Board (Top-5 Core Defects)

| Rank | Issue | Severity | Validity Risk | Fixability | Confidence |
|------|-------|----------|---------------|------------|------------|
| 1 | Limited VC evaluation scope (2 target timbres, near-parallel RVC data) | Major | High — undermines generality of claimed VC capability | Fixable — add 3-5 more target timbres | High |
| 2 | Metric-task mismatch (DNSMOS for VC naturalness) | Major | Medium — DNSMOS not validated for VC artifacts | Fixable — de-emphasize DNSMOS, use VC-specific metrics | High |
| 3 | Unfair codec comparison (downsampled higher-rate codecs) | Major | Medium — may inflate VChangeCodec's relative scores | Fixable — add native 16kHz baseline comparisons | High |
| 4 | Formula error in Eq. (3) — token commitment loss incomplete | Major | Medium — impedes reproducibility | Fixable — correct notation, add metadata input | High |
| 5 | No statistical significance testing | Moderate | Medium — small metric differences may not be reliable | Fixable — add confidence intervals, multi-seed runs | High |

### Core Research-Value Assessment

The paper's primary value lies in demonstrating that a lightweight VC module can be integrated into the encoding path of a neural speech codec without breaking streaming or adding significant latency. This architectural insight is practically useful for operator-deployed RTC systems. However, the current experimental validation is too narrow (2 timbres, RVC-synthetic data, downsampled baselines) to fully establish the robustness and generality of the approach. The main research gap is whether the approach scales to more diverse target timbres and non-parallel conditions, and whether the observed quality advantages hold under properly matched evaluation protocols.

## Actionable Suggestions
### S1: Expand VC Evaluation to More Target Timbres (Must, P0)
**Problem:** Only 2 target timbres evaluated; cannot assess generalization.
**Action:** Train and evaluate on at least 5 target timbres (3 male, 2 female, or balanced) with diverse voice characteristics. Report per-timbre metrics and aggregate statistics.
**Acceptance criteria:** Table showing MCD, speaker similarity, and N-MOS per target timbre with mean ± std across timbres.
**Expected impact:** Conclusively demonstrates whether the approach generalizes across voices.

### S2: Correct Token Commitment Loss Formulation (Must, P0)
**Problem:** Eq. (3) has typo, undefined variable, and missing metadata input.
**Action:** Revise to: $L_T(x_{\text{src}}, x_{\text{tgt}}) = \|\hat{z}_{\text{enc}}(x_{\text{tgt}}) - C(\hat{z}_{\text{enc}}(x_{\text{src}}); u_2)\|_2^2$, where $C(\cdot; u_2)$ is the Converter with metadata. Define all variables explicitly.
**Expected impact:** Enables reproducibility and correct implementation.

### S3: Use VC-Appropriate Evaluation Metrics (Must, P0)
**Problem:** DNSMOS used for VC naturalness despite domain mismatch.
**Action:** (a) De-emphasize DNSMOS in the main paper; report it only as supplementary. (b) Add VC-specific metrics: MCD with DTW alignment, F0 RMSE, speaker embedding cosine similarity (already done via Resemblyzer), and subjective N-MOS as the primary naturalness metric. (c) Add confidence intervals (bootstrap or multi-rater) for subjective scores.
**Expected impact:** Ensures evaluation is valid for the VC task.

### S4: Add Native-Rate Codec Comparisons (Must, P1)
**Problem:** Higher-rate codecs downsampled to 16 kHz may be disadvantaged.
**Action:** Add a comparison at the native rates of each codec: Encodec at 24 kHz, DAC at 44.1 kHz (using a separate test set at those rates, then downsampling the reference for POLQA). Alternatively, retrain/configure DAC at 16 kHz for a fair comparison.
**Expected impact:** Clarifies whether VChangeCodec's quality advantage is real or an artifact of downsampling.

### S5: Add Statistical Significance (Must, P1)
**Problem:** No confidence intervals or significance tests anywhere.
**Action:** Run codec evaluation with at least 3 seeds and report mean ± std for all metrics. For subjective tests, report 95% confidence intervals. For Table 1 comparisons, add paired significance tests vs strongest baseline.
**Expected impact:** Enables readers to assess whether differences are meaningful.

### S6: Expand Related Work in Main Text (Nice-to-have, P1)
**Problem:** Key comparisons with StreamVC and StreamVoice deferred to appendix.
**Action:** Move at least one paragraph from Appendix A.8 into Section 2, explicitly comparing latency, architecture, and mode-switching capability. Add a small comparison table.
**Expected impact:** Strengthens novelty positioning in main paper.

### S7: Revise Promotional Language (Nice-to-have, P2)
**Problem:** "Paradigm shift," "superiority," "innovative methodology," "excels" are overclaims.
**Action:** Replace with factual, bounded statements throughout. For example: "Our framework differs from cascaded VC-codec systems by integrating compression and timbre adaptation within a single streaming pipeline" (instead of "paradigm shift").
**Expected impact:** Improves scientific credibility.

### S8: Provide Detailed Converter Latency Breakdown (Nice-to-have, P2)
**Problem:** Latency profiling lacks component-level breakdown.
**Action:** Report per-component latency (encoder/converter/decoder) on iPhone X CPU, plus comparison on 1-2 additional devices (e.g., Pixel 6, MacBook). Clarify that "no additional latency" should read "negligible additional latency."
**Expected impact:** Strengthens deployment feasibility claims.

## Storyline Options + Writing Outlines
### Current Storyline Diagnosis

The current introduction follows this structure:
- P1: Speech coding background -> user demand for VC -> prior VC architectures (list) -> non-streamable limitation.
- P2: Streaming VC approaches -> cascaded VC-codec latency problem -> proposed integrated solution -> operator privacy framing.
- P3: Proposed VChangeCodec overview (SQ, Converter, commitment loss).
- P4: Contribution bullet list.

**Issues with current storyline:** (1) P1 reads as a literature survey rather than a motivated narrative. (2) The jump from "prior VC architectures" to "streaming VC" is abrupt. (3) The research gap ("no integrated VC-codec exists") is stated only implicitly. (4) The latency comparison example uses AC-VC (2021) rather than the most relevant streaming VC baselines. (5) The operator-oriented privacy discussion, while important, interrupts the technical narrative flow.

### Recommended Storyline: "Problem-Solution-Evidence"

A cleaner narrative arc is:

**P1 (Big Picture + Gap):** "Speech coding is essential for RTC. Neural speech codecs now deliver high quality at low bitrates. Separately, voice conversion (VC) technology has advanced, but applying VC in RTC requires cascading a VC front-end before a codec. This cascaded design introduces cumulative latency (often >100 ms) that exceeds RTC budgets, and requires modifying both sender and receiver pipelines. What is missing is a unified architecture that performs compression and timbre adaptation jointly within a single streaming module."

**P2 (Solution intuition):** "We observe that the encoding stage of a neural codec already extracts a compact latent token that captures speech content. If we can 'recolor' this token to match a target speaker's timbre before decoding, we achieve VC without additional latency or separate processing stages. We propose VChangeCodec, which inserts a lightweight causal projection network (Converter) between encoder and decoder. The Converter takes the source quantized token plus target speaker metadata and produces an adapted token. The decoder then reconstructs the target-timbre speech directly."

**P3 (Key contributions + Results preview):** "This design yields three benefits: (1) 40 ms end-to-end latency, far below cascaded alternatives; (2) seamless switching between original and voice-change modes by bypassing or activating the Converter; (3) a lightweight model (0.97M parameters) suitable for smartphone deployment. Evaluations show competitive codec quality and timbre adaptation performance versus selected baselines."

**P4 (Operator-oriented note):** Keep as a concise final paragraph before contributions, focusing on the privacy-preserving deployment model.

### Abstract Outline (4 sentences)

**S1 (Problem):** "Neural speech codecs enable high-quality real-time communication, but modifying voice timbre still requires separate, high-latency voice conversion systems."
**S2 (Gap):** "Cascading VC with a speech codec introduces cumulative latency that exceeds RTC budgets and complicates the communication pipeline."
**S3 (Solution):** "We propose VChangeCodec, which integrates a lightweight causal projection network into the speech codec encoder, enabling token-level timbre adaptation within the same streaming pipeline."
**S4 (Result):** "VChangeCodec achieves 40 ms end-to-end latency with 0.97M parameters. Evaluated on two target timbres with near-parallel data, it demonstrates competitive timbre adaptation quality compared to selected VC methods, with the highest speaker similarity among tested systems."

### Introduction Outline (4 paragraphs)

**P1 — Problem Setup (Sentence-level):**
- S1: "Speech coding is essential for real-time communication (RTC), compressing waveforms for efficient transmission."
- S2: "Neural speech codecs (NSCs) now deliver high-quality reconstruction even at low bitrates."
- S3: "Beyond faithful transmission, users in live streaming and online meetings increasingly want to customize their voice timbre."
- S4: "Voice conversion (VC) research has addressed this, but prior methods -- both non-streamable (Transformers, GANs, diffusion) and streamable (HuBERT/PPG-based) -- are designed as separate front-end modules."
- S5: "Cascading VC before a standard codec incurs cumulative latency (often >100 ms) that exceeds the ~60 ms one-way RTC budget."

**P2 — Proposed Solution:**
- S1: "We instead propose integrating VC directly into the codec's encoding stage."
- S2: "In VChangeCodec, a causal projection network (Converter) transforms the encoder's quantized tokens to match a target speaker's timbre before decoding."
- S3: "This eliminates the cascaded overhead because VC occurs inside the codec, not before it."
- S4: "The system supports seamless switching between original and voice-change modes by activating or bypassing the Converter."

**P3 — Technical Highlights + Results Preview:**
- S1: "VChangeCodec uses scalar quantization to keep the model lightweight (0.97M parameters)."
- S2: "The full streaming pipeline achieves 40 ms end-to-end latency on a smartphone CPU."
- S3: "In experiments, VChangeCodec shows competitive codec quality vs OPUS, EVS, Lyra2, Encodec, and DAC, while its VC capability achieves the highest speaker similarity among evaluated methods."

**P4 — Contribution list:**
(List the 4 contributions concisely, removing promotional language.)

## Priority Revision Plan
```text
ASCII Diagram — Revision Strategy Roadmap

[P0: Must-fix before acceptance]
  ├── S1: Expand VC evaluation to >=5 target timbres (add metrics table)
  ├── S2: Correct Eq. (3) token commitment loss (fix notation, add metadata)
  ├── S3: Use VC-appropriate metrics (de-emphasize DNSMOS, add CIs)
  └── S5: Add statistical significance (multi-seed, confidence intervals)

[P1: Strongly recommended for next revision]
  ├── S4: Add native-rate codec comparisons (fair baselines at 16kHz)
  ├── S6: Expand Related Work in main text (move from appendix)
  ├── Fix unfair downsampling comparison (acknowledge as limitation)
  └── Add 1-2 more target timbres to strengthen generalization evidence

[P2: Quality improvements]
  ├── S7: Revise promotional language throughout
  ├── S8: Provide converter latency breakdown
  ├── Add limitations subsection to Conclusion
  └── Release inference code and RVC data pipeline documentation
```

### Stage 1 (Immediate — before next submission)
1. **Correct Eq. (3)** with proper notation and metadata input.
2. **Remove DNSMOS as primary VC metric**; use MCD, speaker similarity, N-MOS as main axes.
3. **Add confidence intervals** to all table metrics (at least 3 seeds).
4. **Rephrase promotional claims** ("paradigm shift" -> "differs from", "superiority" -> "competitive", "excels" -> "demonstrates competitive quality").
5. **Expand Related Work section** with one substantive paragraph comparing StreamVC and StreamVoice.

### Stage 2 (Before major resubmission)
6. **Evaluate on at least 5 target timbres** (not 2) with per-timbre breakdown.
7. **Add fair codec comparisons** by evaluating all baselines at 16 kHz native configuration.
8. **Report component-level latency** breakdown for Converter.
9. **Add limitations paragraph** to Conclusion.

### Stage 3 (Extended work)
10. **Scale to more timbres** and analyze data-per-timbre requirements.
11. **Investigate zero-shot or few-shot Converter adaptation** to reduce "one model per timbre" cost.
12. **Release full implementation** (code + pre-trained models + RVC pipeline) upon resolving legal concerns.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|---------------------------------------|---------|--------------|-----------------|-------------------|
| E1 | Codec quality (Table 1) | 68 test utterances (EN+ZH), 16kHz. Baselines: OPUS, EVS, Lyra2, Encodec, DAC | POLQA, ViSQOL, STOI | VChangeCodec > Encodec/Lyra2 at similar bitrates; comparable to DAC | C1 (lightweight codec quality) | Baselines evaluated at downsampled rates (unfair); no CIs |
| E2 | Codec subjective (Fig 3) | 8 ZH utterances, 24 listeners, DCR method | DCR-MOS | VChangeCodec comparable to OPUS@16kbps | C1 (subjective quality) | Only 8 ZH utterances; no EN test |
| E3 | VC objective (Table 2, male) | 42 unseen utterances from 42 speakers, 1 male target. Baselines: Diff-VC, VQMIVC, QuickVC, DDDM-VC, FACodec | DNSMOS, MCD, WER/CER, Resemblyzer | Best speaker similarity (88.07%), lowest MCD (5.76) | C2 (Converter timbre adaptation) | DNSMOS not VC-appropriate; only 1 male timbre |
| E4 | VC subjective (Table 3, male) | 2 male + 3 female sources -> 1 male target = 5 pairs x 6 systems = 30 utterances | N-MOS, S-MOS | Highest S-MOS (3.98), 2nd best N-MOS (3.55) | C2 (subjective timbre adaptation) | Only 1 male target; 5 conversion pairs only |
| E5 | Retrained baselines (Table 4) | Male target. Baselines retrained on target data: VQMIVC (500ep), QuickVC (ft 3200k), DDDM-VC (200k) | DNSMOS, MCD, WER/CER, Resemblyzer | VChangeCodec comparable/better after retraining | C2 (robustness to fairer comparison) | Retraining not matched; VQMIVC collapsed (118% WER) |
| E6 | Ablation (Table 5) | Metadata, Converter dims, λT, encoder tuning | Same as E3 | Metadata + dim256 + λT=50 + frozen encoder optimal | C2 (design choices) | Single seed; no statistical test |
| E7 | RTF (Table 6) | MacBook Pro M1 Pro single thread | RTF (encoder/decoder/converter) | Encoder 0.007, Decoder 0.007, Converter 0.003 | C3 (low latency) | Only MacBook; no smartphone or GPU comparison |

### Research-Theme Gap Diagnosis

**New Knowledge:** The paper's core new knowledge claim is that a lightweight causal projection network inserted into a neural codec encoder can perform effective timbre adaptation. This is a valid architectural insight, but its generality is not yet established due to the narrow evaluation (2 timbres).

**Reproducibility/Reusability:** Several gaps prevent independent reproduction: (1) Eq. (3) has a notation error; (2) RVC data generation pipeline not documented; (3) code not released; (4) training data mixture ratios unspecified.

**Impact on Practice/Understanding:** If validated across more timbres and under fair baselines, VChangeCodec could influence how RTC providers deploy voice changer features. The operator-controlled privacy model is a practical contribution. However, the "one model per timbre" constraint limits practical deployment scalability.

### Proposed Research Experiments (P0/P1/P2)

```text
ASCII Diagram — Experiment Upgrade Plan

P0 (Before acceptance):
  ├── E8: Multi-timbre VC evaluation (5+ targets)
  │   └── Claim: C2 scales across voices
  ├── E9: Multi-seed codec evaluation (≥3 seeds)
  │   └── Claim: C1 statistical reliability
  └── E10: Native-rate codec comparison (16kHz configs)
      └── Claim: C1 fair comparison

P1 (Next revision):
  ├── E11: Non-parallel VC evaluation (remove RVC dependency)
  │   └── Claim: C2 works without synthetic parallel data
  ├── E12: Converter generalization (swap encoder-decoder)
  │   └── Claim: C2 plug-and-play with other codecs
  └── E13: Latency profiling on mobile device
      └── Claim: C3 verified on target hardware

P2 (Extended work):
  ├── E14: Any-to-many extension (multiple stored embeddings)
  └── E15: Ablation on RVC data quality vs manual parallel data
```

| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost/Time | Expected Gain |
|-------------|------------|---------------|-------------------|---------|------------------|---------------|---------------|
| C2 generalization | VC quality is consistent across ≥5 target timbres | Train on 3 male + 3 female targets. Test 42 utterances per target | Same baselines as Table 2 | MCD, Resemblyzer, N-MOS | Mean similarity within 5% of current 88.07% across timbres | ~3 GPU-days | Conclusively demonstrates generalization |
| C1 statistical reliability | Reported POLQA gains are statistically significant | Run 3 seeds of VChangeCodec and top-2 baselines | Same baselines | POLQA mean±std, paired t-test | p<0.05 for VChangeCodec vs Encodec | ~2 GPU-days | Adds credibility to all codec claims |
| C1 fair comparison | VChangeCodec quality at 16kHz vs baselines at 16kHz native | Configure DAC at 16kHz (if available) or compare at native rates with downsampled references | DAC@16kHz, Encodec@16kHz | POLQA, ViSQOL | Report both native and downsampled; acknowledge any differences | ~2 GPU-days | Clarifies whether quality advantage is real |
| C2 non-parallel | Converter works without RVC near-parallel data | Train on non-parallel VCTK, evaluate same protocol | RVC-parallel vs non-parallel | MCD, Resemblyzer | Similarity within 3% of RVC-parallel model | ~2 GPU-days | Demonstrates practical utility outside synthetic data

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5 / 10**

*Rationale:* The paper presents a genuinely useful architectural innovation -- integrating VC into the codec encoder path -- and demonstrates engineering efficiency (0.97M parameters, 40 ms latency). However, the experimental validation has significant scope and fairness limitations: evaluation on only 2 target timbres, use of DNSMOS (a metric not designed for VC quality assessment), downsampled baseline comparisons that may disadvantage competitors, a formula error in the key loss equation, and no statistical significance testing. These issues reduce confidence in the claimed superiority and generality of the approach. The novelty claim (integrated VC-codec) is promising but requires broader validation.

**Post-Revision Target: [6.5, 7.5] / 10**

If the authors address the P0 issues (expand to ≥5 target timbres, correct Eq. (3), use VC-appropriate metrics, add statistical significance, and fix the unfair codec comparisons), the paper would be a solid contribution to the speech/audio processing community. The P1 improvements (native-rate comparisons, expanded related work) could raise confidence further. The fundamental architecture is sound; the main work needed is in strengthening the evidence base and properly bounding the claims.

*Scoring emphasis:* Research value + novelty (60%), validity/soundness (25%), reproducibility (15%).