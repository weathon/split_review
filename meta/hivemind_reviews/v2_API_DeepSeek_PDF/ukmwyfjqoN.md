## Summary
# Final Review Report

## Summary

This paper presents ReBotNet (Recurrent Bottleneck Mixer Network), an efficient architecture for real-time video enhancement targeting live video calls and streaming applications. The method employs a dual-branch encoder: one branch tokenizes stacked input frames into spatio-temporal tubelets via a ConvNext encoder followed by an MLP-Mixer bottleneck, while the second branch extracts per-frame image tokens and processes them through another Mixer to learn temporal correspondences. A shared decoder fuses both branches, and a frame-recurrent training scheme uses the previous predicted frame as additional input. Two new multi-degradation datasets (PortraitVideo, FullVideo) are introduced to emulate real-world video call scenarios. Experiments show ReBotNet achieves competitive or better PSNR/SSIM compared to strong baselines (RVRT, VRT, BasicVSR++, FastDVDNet) while reducing latency by ~2.4× and peak memory usage, supporting real-time 30+ FPS inference on an A100 GPU.

The paper addresses a practically important problem and proposes a thoughtfully designed architecture that combines ConvNext efficiency with MLP-Mixer bottlenecks. However, several concerns affect the overall assessment: (1) a critical data anomaly where ReBotNet-S and ReBotNet-M report identical FullVideo PSNR despite 4× FLOP difference, (2) unsupported or overclaimed statements ("state of the art", "from our experiments we found"), (3) missing statistical variance across all metrics, (4) incomplete dataset curation documentation, and (5) absence of limitations discussion. With major revisions to address data integrity, claim bounding, and experimental rigor, the paper could make a valuable contribution to efficient video enhancement.

## Strengths
1. **Practical problem and clear motivation.** The paper targets real-time video enhancement for live video calls and streaming, a timely and practically significant problem. The emphasis on latency (real-time 30 FPS) and computational efficiency sets a clear design goal that distinguishes this work from purely quality-driven video restoration methods.

2. **Thoughtful architecture design.** The dual-branch design combining ConvNext encoders (for efficient low-level feature extraction) with MLP-Mixer bottlenecks (for token-mixing without quadratic attention complexity) is well-motivated and technically sound. The ablation study (Table 4) convincingly demonstrates that each component contributes to overall performance, particularly the recurrent setup which adds +0.26 dB PSNR with zero additional FLOPs or latency.

3. **Strong empirical efficiency results.** ReBotNet achieves substantial latency reductions (~2.4× faster than RVRT in medium FLOP regime, 15.02 ms vs 35.93 ms) while maintaining competitive PSNR/SSIM. The peak memory advantage (Figure 4c) further supports deployment feasibility. These efficiency gains are the paper's strongest contribution.

4. **New datasets for the community.** The curated PortraitVideo and FullVideo datasets address a genuine gap: existing video restoration datasets focus on single degradations, while video conferencing scenarios involve mixed degradations and talking-head content. Making these datasets available (with proper documentation) could stimulate further research in application-focused video enhancement.

5. **Comprehensive user study.** The perceptual evaluation with human raters provides evidence beyond PSNR/SSIM that ReBotNet's quality is competitive with SOTA methods. The near-equivalence with RVRT (mean preference +0.08) while being substantially faster is a practically meaningful finding.

6. **Validation on public benchmarks.** Appendix Table 13 confirms that ReBotNet generalizes beyond the proposed datasets, achieving results competitive with RVRT on DVD/GoPro deblurring benchmarks (34.30 vs 34.30 PSNR on DVD).

## Weaknesses
1. **Critical data integrity concern (F1 Numerical consistency failure).** ReBotNet-S and ReBotNet-M report identical FullVideo PSNR (33.45) despite a 4.3× FLOP difference (13.02 vs 56.06 GFLOPs) and substantially different embedding dimensions. This strongly suggests insufficient numerical precision in reporting or a data processing error. Without resolution, all quantitative claims are called into question.

2. **Unsupported motivating claims (F6 citation-backed factuality).** The paper states "from our experiments we found that they are computationally complex and have a high inference time" (Page 1) without citing or describing those experiments. Similarly, "achieves state of the art results" (Page 1) is asserted without scope boundaries or standardized benchmark verification for the primary setting.

3. **No statistical variance reporting.** All PSNR/SSIM results in Tables 1, 3, 4, and 13 are reported as point estimates without standard deviations, confidence intervals, or significance tests. Given that performance differences between methods are often within 0.2-0.3 dB (well within typical run-to-run variance), the reported rankings may not be statistically reliable.

4. **Missing matched-capacity ablation controls.** The ablation study (Table 4) adds components cumulatively, increasing capacity at each step. The +0.18 dB gain from adding the bottleneck mixer (31.41 → 31.59) could partially reflect increased parameter count rather than the mixer mechanism itself. A capacity-matched control (e.g., replacing the mixer with equally-sized ConvNext block) is needed.

5. **Incomplete dataset documentation.** The degradation pipeline's composition logic is underspecified (how many degradations per frame? per-frame or per-video consistency?). Manual filtering criteria for both datasets are not quantified, introducing selection bias risk. FullVideo content composition (human vs. non-human) is not clarified.

6. **Absence of limitations section.** The paper does not discuss any failure modes, generalization boundaries, or practical deployment constraints. This omission is significant for a paper claiming real-world applicability.

7. **Related Work is a chronological list.** The section organizes prior work sequentially without explicit comparison axes (e.g., temporal modeling strategy, efficiency profile, attention vs. mixer backbone), making it difficult for readers to identify where ReBotNet fits relative to existing methods.

## Key Issues
### Issue 1 (Critical): Data Anomaly — ReBotNet-S and ReBotNet-M report identical FullVideo PSNR
- **Location:** Page 7, Table 1
- **Evidence:** ReBotNet-S (13.02 GFLOPs) and ReBotNet-M (56.06 GFLOPs) both report PSNR = 33.45 on FullVideo. SSIM differs (0.9113 vs 0.9168), but PSNR being identical to 2 decimal places for models with 4× FLOP difference is statistically implausible. This suggests a data processing bug, rounding artifact, or reporting error.
- **Risk:** If the numbers are unreliable, all quantitative conclusions are compromised.

### Issue 2 (Major): Unsupported evidence for core motivation
- **Location:** Page 1, Introduction Paragraph 2
- **Evidence:** The claim "from our experiments we found that they are computationally complex and have a high inference time and are not suitable for real-time applications" is presented as fact without citing any experiment. This claim drives the paper's motivation.
- **Risk:** Reviewers cannot verify the motivating premise. If the claim is inaccurate, the paper's raison d'être weakens.

### Issue 3 (Major): Missing statistical significance across all experiments
- **Location:** Tables 1, 3, 4, 13
- **Evidence:** No standard deviations, confidence intervals, or multi-seed experiments reported. PSNR differences between methods are often within 0.2 dB, which could be within run-to-run noise for deep learning models.
- **Risk:** Readers cannot assess whether reported improvements are statistically significant or due to random variation.

### Issue 4 (Major): Conclusion lacks limitations and overclaims
- **Location:** Page 9, Section 6
- **Evidence:** The conclusion states "outperformed state-of-the-art methods" despite RVRT(L) achieving higher PSNR on FullVideo (33.79 vs 33.65). No limitations are discussed. Future work is generic.
- **Risk:** Hurts credibility with reviewers and misleads readers about the scope of validation.

### Issue 5 (Major): Dataset documentation gaps
- **Location:** Pages 5-6, Section 4.1; Appendix E
- **Evidence:** The degradation pipeline's randomness composition is not specified (number of degradations per frame, per-frame vs per-video consistency). Manual filtering criteria for "low quality" and "high quality" are not quantified. Number of excluded videos not reported.
- **Risk:** Irreproducible dataset construction and potential selection bias.

### Issue 6 (Major): Related Work lacks comparative structure
- **Location:** Pages 2-3, Section 2
- **Evidence:** Methods are described chronologically without explicit comparison axes. The paper's differentiation from optical-flow methods and transformer methods is implied but never systematically stated.
- **Risk:** Readers cannot quickly understand the paper's novel position relative to prior art.

## Actionable Suggestions
### S1 (Must): Verify and correct Table 1 data anomaly
- Re-run both ReBotNet-S and ReBotNet-M on FullVideo with 3 random seeds each. Report PSNR and SSIM as mean ± std. If the PSNR values are indeed identical, provide an explanation (e.g., the S model saturates on FullVideo's content distribution, or a rounding artifact). If the discrepancy is due to a data processing error, correct it immediately.
- Increase numerical precision to 3 decimal places for all metrics.

### S2 (Must): Add multi-seed variance to all experiments
- Re-run all models (ReBotNet S/M/L, all baselines) with at least 3 different random seeds on both PortraitVideo and FullVideo.
- Report PSNR and SSIM as mean ± std in Tables 1, 3, 4, and 13.
- Add a paired significance test (e.g., Wilcoxon signed-rank) for the key ReBotNet vs RVRT comparison.

### S3 (Must): Support or remove "from our experiments we found" claim
- Either add a supplementary section documenting the preliminary latency benchmarks that motivated this claim (which methods, which resolution, which hardware, measured latency), or replace the claim with a literature-grounded statement about known computational costs of transformer-based video restoration.

### S4 (Must): Bound all "state of the art" and "outperforms" claims
- Replace "achieves state of the art results" (Page 1) with: "achieves competitive results with lower computational cost."
- In the conclusion, replace "outperformed state-of-the-art methods" with "achieved competitive or better PSNR/SSIM on our proposed datasets while being 2.4× faster."
- In the abstract, replace "outperforms existing approaches" with specific, scoped wording.

### S5 (Must): Add a dedicated Limitations section
- Include at minimum: (a) synthetic vs. real-world degradation gap, (b) only 2-frame processing, (c) no long-sequence drift analysis, (d) fixed 384×384 resolution, (e) single loss function (Charbonnier) without perceptual or adversarial losses.

### S6 (Must): Document dataset curation fully
- Specify: (a) number of videos excluded during filtering, (b) exclusion criteria with examples, (c) degradation composition algorithm (how many per frame, per-frame vs per-video consistency), (d) human vs non-human content breakdown for FullVideo.

### S7 (Must): Add matched-capacity ablation control
- Replace the bottleneck mixer with a ConvNext block of matched parameter count/FLOPs in the ablation study to verify that the mixer mechanism (not just added capacity) drives the +0.18 dB gain.

### S8 (Nice-to-have): Restructure Related Work
- Organize by comparison axes: (i) temporal modeling (sliding window vs. recurrent vs. flow-based), (ii) backbone (CNN vs. transformer vs. mixer), (iii) efficiency focus. Include a paragraph explicitly comparing ReBotNet with the closest methods along these axes.

### S9 (Nice-to-have): Improve Abstract with bounded claims
- Revise to specify "on our proposed PortraitVideo and FullVideo datasets" and "under comparable FLOP budgets", and remove "outperforms existing approaches" in favor of specific numbers.

### S10 (Nice-to-have): Clarify "flipped" → "transposed" in mixer description
- Page 5, Section 3.3: Replace "flipped along the C axis" with "transposed (shape [N, C] → [C, N])" to match the original MLP-Mixer formulation.

## Storyline Options + Writing Outlines
### Abstract Outline (Recommended)

**S1 (Problem + Gap):** "Real-time video enhancement under mixed degradations (noise, blur, compression) remains challenging because existing video restoration networks are either too slow for live 30 FPS deployment or target only single degradations, limiting their practical usefulness for video calls and streaming."

**S2 (Prior Work Insufficiency):** "Transformer-based restoration methods such as RVRT and VRT achieve high quality but incur prohibitive latency (>35 ms per frame) due to quadratic self-attention complexity, while pure MLP-Mixer approaches suffer quality regression at full resolution."

**S3 (Proposed Method):** "We propose Recurrent Bottleneck Mixer Network (ReBotNet), which combines a ConvNext encoder with MLP-Mixer bottlenecks in a dual-branch design: spatio-temporal tubelet tokens capture joint motion cues while per-frame image tokens enhance temporal consistency, all fused by a shared decoder. A frame-recurrent training scheme leverages the previous prediction at zero extra FLOPs."

**S4 (Key Result — Bounded):** "On two newly curated multi-degradation datasets (PortraitVideo, FullVideo) and public benchmarks (DVD, GoPro), ReBotNet achieves competitive PSNR/SSIM with state-of-the-art methods while reducing latency by 2.4× and peak memory, enabling real-time inference at >50 FPS on an A100 GPU."

**S5 (Implication):** "These results demonstrate that carefully designed mixer-based architectures can bridge the gap between quality and speed for practical video enhancement."

### Introduction Outline (Recommended)

**Current Storyline Diagnosis:** The current introduction (Paragraphs 1-4) progresses as: Broad use-cases → Restoration vs enhancement → Method overview → Dataset introduction → Contribution bullets. The main weakness is that Paragraph 1 dissipates reader attention across many applications before focusing on video calls, and Paragraph 2's "from our experiments we found" is unsupported.

**Recommended Storyline (Big Picture → Gap → Solution → Evidence):**

**P1 — Practical Stakes and Concrete Gap (replace current P1):**
"Real-time video enhancement — improving video quality on-the-fly under mixed degradations — is critical for live video calls, remote healthcare, and streaming. Despite advances in video restoration, existing methods either target single degradations (denoising, deblurring, super-resolution) or are too computationally expensive for real-time deployment. In particular, state-of-the-art transformer-based methods exceed the 33 ms per-frame budget needed for 30 FPS video, while requiring multiple future frames that introduce lookahead latency incompatible with live streaming. An efficient method that handles mixed degradations in real-time with competitive quality has not yet been established."

**P2 — Existing Approaches and Their Limitations (replace current P2):**
"Video restoration methods can be categorized by their temporal modeling strategy. Sliding-window CNN methods (FastDVDNet) are fast but quality-limited. Recurrent flow-based approaches (BasicVSR++) improve quality but incur optical flow overhead. Transformer-based methods (VRT, RVRT) achieve the best quality but suffer from high FLOPs and latency. A common thread is that all top-performing methods exceed 30 ms inference time on standard hardware at 384×384 resolution, making them unsuitable for live deployment."

**P3 — Proposed Method Intuition (adapted from current P3):**
"To address this gap, we propose ReBotNet, an architecture designed for efficiency from first principles. Rather than using quadratic-complexity self-attention, we adopt MLP-Mixers at the bottleneck, applied on compact spatio-temporal tubelet tokens extracted by a ConvNext encoder. A second branch processes per-frame image tokens through another Mixer to learn temporal correspondences without expensive flow computation. A frame-recurrent scheme uses the previous prediction as additional input, carrying temporal information forward at zero extra inference cost."

**P4 — Key Evidence Preview (new):**
"On two new multi-degradation datasets (PortraitVideo, FullVideo) and public benchmarks, ReBotNet achieves PSNR competitive with RVRT (within 0.14 dB) while being 2.4× faster (15.0 ms vs 35.9 ms in medium FLOP regime). A user study confirms perceptual near-equivalence with RVRT. These results establish ReBotNet as a practical solution for real-time video enhancement."

**P5 — Contributions (restated with technical specificity):**
"1) A dual-branch architecture combining ConvNext spatio-temporal encoders with MLP-Mixer bottlenecks, avoiding quadratic attention complexity. 2) A frame-recurrent training scheme that improves quality (+0.26 dB) with zero added FLOPs or latency. 3) Two new multi-degradation video datasets (PortraitVideo, FullVideo) for real-world video enhancement research."

### Storyline Options

**Option A (Selected Above): Efficiency-First Narrative.** Frame the paper around the unmet need for real-time video enhancement. Emphasize that ReBotNet is not trying to beat transformer quality at all costs, but to achieve "good enough" quality at real-time speed. This is honest, defensible, and aligns with the experimental evidence.

**Option B: Bottleneck Design Narrative.** Highlight the methodological contribution: using ConvNext for efficient low-level feature extraction and MLP-Mixers for bottleneck processing is a principled way to combine the strengths of convolutions and MLPs while avoiding attention complexity. This framing targets a more architecture-focused audience.

**Option C: Dataset + Application Narrative.** Center the paper on the practical video-call scenario, emphasizing the new datasets and the application-driven design (talking-head content, mixed degradations, real-time constraint). This framing targets the application-oriented community.

## Priority Revision Plan
### P0 — Must fix before resubmission (publication-critical)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|----------------|--------|
| P0.1 | Data anomaly: ReBotNet-S/M identical FullVideo PSNR (33.45) | Re-run with 3 seeds, report mean±std, add decimal precision | Restores trust in all quantitative results | 2-3 GPU-days |
| P0.2 | No statistical variance reported | Add std over 3+ seeds to all tables | Enables significance assessment | 3-5 GPU-days |
| P0.3 | Unsupported "from our experiments" claim | Add preliminary benchmark appendix or replace with lit-grounded statement | Fixes motivation credibility | 0.5 day |
| P0.4 | Overclaimed "state of the art" / "outperforms" | Bound all strong claims to specific datasets/regimes | Aligns claims with evidence | 1 day |
| P0.5 | Missing Limitations section | Add dedicated paragraph covering 4-5 concrete limitations | Demonstrates scientific maturity | 0.5 day |
| P0.6 | Dataset curation gaps | Document exclusion counts, degradation composition logic | Enables reproducibility | 1-2 days |

### P1 — High priority (strongly recommended)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|----------------|--------|
| P1.1 | Matched-capacity ablation | Add ConvNext control for mixer comparison | Strengthens causal claims | 1-2 GPU-days |
| P1.2 | User study: report N participants | Add number of raters, blinding procedure | Improves methodological rigor | 0.5 day |
| P1.3 | Related Work as list | Restructure by comparison axes | Clarifies positioning | 1 day |
| P1.4 | Conclusion unbounded/overclaiming | Replace with validated-findings + limitations + specific future work | Aligns with evidence | 0.5 day |

### P2 — Nice-to-have (quality improvement)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|----------------|--------|
| P2.1 | Missing implementation details | Add batch size, AMP status, training time | Reproducibility | 0.5 day |
| P2.2 | "Flipped" → "transposed" in mixer | Fix terminology | Clarity | 0.1 day |
| P2.3 | Abstract lacks bounded claims | Rewrite per recommended outline | First impression | 0.5 day |
| P2.4 | Public benchmarks in appendix → main | Move Table 13 or summary to main paper | Strengthens generalizability claim | 0.5 day |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Compare ReBotNet vs baselines across FLOP regimes (S/M/L) | PortraitVideo, FullVideo; PSNR/SSIM; 2-frame input; same training protocol | PSNR, SSIM, GFLOPs, Latency (ms) | ReBotNet achieves competitive/better PSNR/SSIM with 2.4× lower latency vs RVRT | C1 (architecture efficiency) | No variance reported; data anomaly in FullVideo S/M PSNR |
| E2 | User study — perceptual quality comparison | M-config models on PortraitVideo; expert raters; pairwise preference {-2,+2} | Mean preference score, 95% CI | ReBotNet preferred over FastDVDNet/VRT/BasicVSR++; near-equivalence with RVRT (+0.08) | C1 (quality-efficiency tradeoff) | N participants not reported; side-by-side bias not discussed |
| E3 | Ablation: component contribution | PortraitVideo; Tubelet, Image, Mixer, Recurrent ablation | PSNR, SSIM, GFLOPs, Latency | Each component adds improvement; Recurrent: +0.26 dB at zero FLOPs | C1 (design validity) | No capacity-matched control for mixer |
| E4 | Analysis: embedding dim, depth, frames | PortraitVideo; varied mixer dim/depth/frame count | PSNR, SSIM, GFLOPs, Latency | Dim 512 optimal; depth 6 best; 2+ frames beneficial | C1 (hyperparameter sensitivity) | Single dataset; no interaction effects tested |
| E5 | Public benchmark evaluation (Appendix) | DVD, GoPro deblurring; compare with VRT, RVRT, etc. | PSNR, SSIM | ReBotNet matches RVRT (34.30 DVD), slightly below (34.90 vs 34.92 GoPro) | C1 (generalizability) | No latency/FLOPs reported for public benchmarks |
| E6 | Temporal consistency analysis (Appendix) | PortraitVideo; mean SSIM diff between consecutive frames | SSIM difference | With temporal branch: 0.124 (vs 0.158 without, vs 0.104 GT) | C2 (temporal consistency) | Only SSIM diff; no standard temporal consistency metrics |
| E7 | Pure mixer experiment (Appendix) | VRT with mixers replacing transformers; DVD dataset | PSNR, SSIM, GFLOPs, FPS | Quality drop (34.24→32.14 PSNR); still high GFLOPs (1495) | Motivates bottleneck design | Only tested on DVD; one configuration |

### Research-Theme Gap Diagnosis

- **New Knowledge:** The paper's primary contribution is architectural (ConvNext + MLP-Mixer for real-time enhancement). This is moderately novel but the individual components (ConvNext, MLP-Mixer, frame-recurrent training) are all established. The *combination* and *application to video enhancement* is the main novelty. Without external literature verification, definitive novelty assessment is deferred.
- **Reproducibility:** Currently insufficient. Missing: batch size, AMP status, gradient clipping, training time, dataset exclusion counts, degradation composition algorithm, and multi-seed variance.
- **Impact on Practice:** Potentially high if the efficiency gains hold across diverse hardware. The 2.4× speedup at competitive quality could enable real-time enhancement on consumer GPUs. However, deployment viability depends on verification on edge hardware (not tested).
- **Unresolved Core Claims:** (a) Whether the mixer mechanism specifically (vs. capacity increase) drives gains, (b) whether results are statistically significant given no variance reporting, (c) whether datasets generalize to authentic in-the-wild degradation.

### Proposed Research Experiments (P0/P1/P2)

| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost/Time | Expected Paper-Quality Gain |
|-------------|-----------|---------------|-------------------|---------|------------------|----------------|---------------------------|
| **P0.1** Data integrity | ReBotNet-S/M PSNR differs with proper precision | Re-run S/M config on FullVideo with 3 seeds, report to 3 decimals | Same training config | PSNR (3 decimals), std | S and M PSNR differ by >0.05 dB or explanation provided | 2 GPU-days | Resolves critical validity concern |
| **P0.2** Statistical significance | ReBotNet gains are statistically significant | Re-run top-3 methods (ReBotNet, RVRT, BasicVSR++) × 3 seeds on both datasets | Matched seed, training protocol | PSNR±std, paired t-test | Gains > 2× pooled std or p<0.05 | 4 GPU-days | Enables valid comparison claims |
| **P1.1** Causal attribution of mixer | Mixer mechanism (not capacity) drives gain | Replace mixer with ConvNext block (matched params) in bottleneck | Same training config | PSNR, SSIM | Mixer > ConvNext by >0.05 dB | 1 GPU-day | Strengthens architectural claim |
| **P1.2** Temporal drift analysis | Recurrent setup does not cause quality drift over long sequences | Evaluate on full 150-frame videos; compute PSNR per frame index | Single-frame baseline | PSNR vs frame index slope | Slope not significantly < 0 | 1 GPU-day | Addresses limitation gap |
| **P2.1** Edge-device deployment | Efficiency advantage holds on lower-end GPUs | Measure latency on T4/V100 GPU; report FPS | A100 baseline | FPS, peak memory | Maintain >30 FPS on T4 | 1 GPU-day | Strengthens practical impact claim |
| **P2.2** Real-world generalization | Performance holds on authentic degradations | Evaluate on RealVSR or in-the-wild video call recordings | Synthetic degradation baseline | PSNR, user study | No significant quality drop vs synthetic | 2 GPU-days | Validates real-world applicability |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5 / 10**

The score reflects the paper's genuine practical contribution (efficient real-time video enhancement architecture, new datasets) tempered by critical concerns about data integrity (identical PSNR across 4× FLOP difference), missing statistical validation, unsupported motivating claims, and incomplete documentation. The research value is meaningful — a 2.4× speedup at competitive quality is practically useful — but the current evidentiary standards are insufficient for publication without major revision.

**Score rationale:**
- **Research Value (priority dimension):** 6/10 — The efficiency-focused approach to video enhancement is timely and potentially impactful, but novelty of the architectural combination (ConvNext + MLP-Mixer + recurrent) is moderate given that all components are established.
- **Validity/Soundness:** 4/10 — The data anomaly and absence of statistical variance are significant concerns that must be resolved.
- **Novelty:** 5/10 — Dual-branch design with tubelet+image tokens is a reasonable contribution, but without external literature verification (retrieval disabled), novelty judgment is partially deferred.
- **Reproducibility:** 4/10 — Missing critical implementation details and dataset curation documentation.
- **Clarity:** 6/10 — Generally well-written but introduction is diffuse, Related Work is list-like, and overclaims reduce precision.

**Post-Revision Target: [6.5, 7.5] / 10**

If all P0 and P1 items are addressed (data anomaly resolved, variance reported, claims bounded, limitations added, dataset documented, matched-capacity ablation added), the paper could reach 6.5-7.5/10, making it a solid conference publication. The key upgrade comes from restoring trust in the quantitative results and bounding claims to match evidence. The architecture itself is sound and the efficiency results are compelling when properly contextualized.

**Note:** This score is based solely on manuscript evidence (Retrieval-Disabled Mode active; external literature verification deferred). A full novelty assessment requires manual literature comparison before final acceptance decision.