Now I have a thorough understanding of the paper and all the review inputs. Let me write the final consolidated review.

## Summary

The paper presents a large-scale empirical study (1T token pretraining from scratch, 8B model) investigating when and with what characteristics reasoning data should be introduced during LLM training. It tracks models through pretraining → SFT → RL across systematically varied data conditions. The core findings are: (1) front-loading reasoning data into pretraining creates a durable advantage that intensifies through post-training, (2) an asymmetric principle where pretraining benefits most from diversity while SFT benefits most from quality, (3) high-quality pretraining data can have latent effects unlocked by SFT, and (4) naive scaling of SFT data with mixed quality is harmful. The experimental scale and design are ambitious, and the central front-loading finding is well-supported.

## Calibration

### Round 1 bracket: 4.0–6.0

### Round 1 — Topic-anchored queries (low, mid, high bands)

**Low-band (high_score=3.5):** Retrieved anchors scored 2.0–3.2. These papers had fundamental validity issues (e.g., FreeLM avg 2.0, LogicJitter avg 2.5). The paper under review is clearly stronger than these.

**Mid-band (low_score=3.5, high_score=7.5):** Retrieved anchors scored 4.0–6.75. Most relevant:
- GtpubstM1D (Advancing Mathematical Reasoning, avg 5.71, Accept) — similar topic (CPT vs SFT, data quality). Scores ranged from 1 to 8 (highly mixed). Our paper has a similar contribution level but a more significant methodological gap (SFT exposure confound).
- 8uXkyWFVum (Amuro and Char, avg 4.20, Reject) — about pre-training/fine-tuning relationship. Our paper is substantially stronger in scale and findings.
- 1hQKHHUsMx (What Kind of Pretraining Data, avg 6.75, Accept) — stronger paper with well-executed influence function analysis. Our paper has broader scope but weaker methodology in one area.
- nwZHFKrYTB (How to Train Long-Context LMs, avg 5.80, Reject) — similar empirical recipe paper. Our paper has more novel findings but the same type of methodological gaps.

**High-band (low_score=7.5):** Retrieved anchors scored 8.0 (e.g., Combatting Dimensional Collapse, Training on the Test Task). Our paper does not reach this level due to the methodological gap.

### Round 1 — Weakness-anchored queries

**SFT data quality confound (Query 4):** Retrieved anchors scored 3.0–4.4 (e.g., "Disentangling the Roles of Representation and Selection in Data Pruning" avg 3.0, "Rethinking Data Selection at Scale" avg 4.40). These are papers where methodological confounds in training data comparisons led to lower scores.

**Decontamination (Query 5):** Retrieved anchors scored 4.25–6.75. The "Benchmark Inflation" paper (avg 4.25, Reject) had similar concerns about missing contamination analysis.

**Catch-up hypothesis (Query 6):** Retrieved anchors scored 2.5–5.71. The "Supervised Chain of Thought" paper (avg 2.50) had more fundamental issues.

### Round 2 — Narrowing within bracket

Narrowed to 4.5–6.5 range. Retrieved:
- BGnm7Lo8oW (Towards Learning to Reason at PT Scale, avg 5.50, Reject) — similar pretraining-scale reasoning experiments, but weaker experimental validation.
- nwZHFKrYTB (How to Train Long-Context LMs, avg 5.80, Reject) — well-executed empirical recipe paper with similar structure.

### What the low-band anchors and weakness-anchored hits failed at

The low-band topic anchors (avg 2.0–3.2) failed at basic experimental validity (no controlled comparisons, insufficient scale). The weakness-anchored hits (avg 3.0–4.4 for SFT confound query) shared the failure mode of uncontrolled experimental comparisons where confounds undermine specific claims. **The paper under review shares this failure mode**: the SFT experiments comparing D_SHQ and D_LDQ datasets (Table 5) do not clarify how the drastic size mismatch (1.2M vs 268M samples) is handled when both are described as "finetuned on 4.8M reasoning samples." This confound weakens the headline "asymmetric principle" claim that SFT is dominated by data quality.

The paper's central front-loading claim does **not** share these failures — it is supported by clean comparisons (pretraining with controlled token budgets, catch-up experiment with controlled SFT data, RL with controlled SFT). This distinction is critical for scoring.

### Anchor list

| Anchor ID | Avg Score | Round | Query Bucket | Comparison |
|-----------|-----------|-------|-------------|------------|
| SaOxhcDCM3 | 3.20 | R1 | topic-low | Much weaker — self-consuming loop paper |
| qgLyKwXVDs | 2.00 | R1 | topic-low | Much weaker — FreeLM |
| mfTM4UdYnC | 2.50 | R1 | topic-low | Much weaker — logic games for misinformation |
| OdoS6cH8MP | 2.00 | R1 | topic-low | Much weaker — data valuation metrics |
| 506Sxc0Adp | 4.00 | R1 | topic-mid | Weaker — only analyzes diversity coefficient, no training |
| GtpubstM1D | 5.71 | R1 | topic-mid | **Similar** — Advancing Mathematical Reasoning. Comparable contribution; our paper has larger scale but a methodological gap |
| 1hQKHHUsMx | 6.75 | R1 | topic-mid | Stronger — well-executed influence function study |
| kDakBhOaBV | 4.00 | R1 | topic-mid | Weaker — same diversity coefficient paper, duplicate |
| f4gF6AIHRy | 8.00 | R1 | topic-high | Much stronger — Combating Dimensional Collapse |
| jOmk0uS1hl | 8.00 | R1 | topic-high | Much stronger — Training on the Test Task |
| 07yvxWDSla | 8.00 | R1 | topic-high | Much stronger — Synthetic continued pretraining |
| PdaPky8MUn | 8.00 | R1 | topic-high | Much stronger — Never Train from Scratch |
| qUJsX3XMBH | 4.40 | R1 | weakness (SFT confound) | Similar weakness — data selection confounds |
| EOPLy80bBm | 3.00 | R1 | weakness (SFT confound) | Similar weakness — data pruning confounds |
| eVKP64sQBd | 4.00 | R1 | weakness (SFT confound) | Less relevant — multi-modal spurious correlations |
| m2NVG4Htxs | 6.75 | R1 | weakness (decontamination) | Stronger — rigorous contamination analysis |
| rAylWUIKtu | 4.25 | R1 | weakness (decontamination) | Similar gap — Benchmark Inflation, lacks contamination analysis |
| Nk1MegaPuG | 4.25 | R1 | weakness (decontamination) | Similar gap — Evading Contamination Detection |
| Nsms7NeU2x | 6.75 | R1 | weakness (decontamination) | Stronger — contamination analysis |
| 8uXkyWFVum | 4.20 | R1 | weakness (catch-up) | Weaker — Amuro and Char, smaller scale, narrower scope |
| pXIbcRPxWR | 2.50 | R1 | weakness (catch-up) | Much weaker — Supervised Chain of Thought |
| 28gMnEAgl9 | 5.33 | R1 | weakness (catch-up) | Different topic — abstract reasoning benchmark |
| BGnm7Lo8oW | 5.50 | R2 | narrow | Similar — Towards Learning to Reason at PT Scale. Comparable contribution level but different weaknesses |
| nwZHFKrYTB | 5.80 | R2 | narrow | Similar — How to Train Long-Context LMs. Comparable empirical recipe paper |
| FIXk0RP960 | 5.50 | R2 | narrow | Similar — Does RLHF Scale? Similar empirical scaling study |
| MCjVArCAZ1 | 4.50 | R2 | narrow | Weaker — Pre-training vs Meta-Learning comparison |

### Final Score Decision

The paper sits above the 3.0–4.4 anchors that share the uncontrolled-comparison failure mode, because (a) the SFT confound is limited to one specific claim and does not affect the central front-loading finding, and (b) the paper's scale and systematic design across most conditions are genuine strengths. However, it sits below the 5.71 "Advancing Mathematical Reasoning" anchor because that paper's weaknesses (limited novelty for some findings, proprietary data) are less damaging than the methodological gap here. Within the 5.0–6.0 bracket, the paper is closest to the 5.50–5.80 range of similar empirical recipe papers (BGnm7Lo8oW, nwZHFKrYTB), all of which were rejected at their respective venues. The SFT exposure confound is a real issue that requires major revisions to resolve.

---

## Strengths

1. **Controlled large-scale pretraining comparison demonstrates that front-loading reasoning data creates a durable, compounding advantage.** The RL-phase results (Table 3) show an 18.74% gap between M_base (37.92) and M_LMQ (56.66) after identical SFT and RL. The experimental design holds the total reasoning token budget constant (80B tokens across all pretraining conditions) and controls for total training tokens (1T for all models). This finding is the paper's central contribution and is well-supported by the evidence.

2. **Clear evidence for the asymmetric allocation principle within pretraining.** Table 1 shows that diverse pretraining data (M_LDQ: 64.09) dramatically outperforms less diverse high-quality data (M_SHQ: 54.98) by 9.09% absolute, with the largest gains in math (+28.4% over baseline) and code. The reasoning ratio sensitivity experiments (Tables 6, 7) further show monotonic improvement with higher reasoning proportions. The catch-up experiment (Table 4) demonstrates that even 2× SFT epochs on the baseline cannot match the weakest reasoning-pretrained model.

3. **The latent effect discovery is well-supported.** The finding that M_LMQ (which adds high-quality D_SHQ to diverse D_LDQ) shows negligible pretraining advantage over M_LDQ (Table 1: 64.07 vs 64.09) but gains +4.25% after SFT on the same data (Table 4: 50.95 vs 46.70) is a clean result that uses controlled SFT conditions, avoiding the exposure confound.

4. **Demonstration that naive SFT scaling is harmful.** Table 8 compares within the same data family (D_LDQ): doubling mixed-quality data barely changes performance (+0.15) while adding a small fraction (0.4%) of high-quality long-CoT data (D_ALF*) yields consistent improvements. This within-family comparison avoids the cross-dataset exposure confound.

## Weaknesses

### Fatal

None.

### Major

1. **SFT exposure is uncontrolled across datasets, undermining the "quality dominates SFT" claim.** The paper states each model is "finetuned on 4.8M reasoning samples from D_res." The datasets differ enormously in size: D_SHQ has 1.2M unique samples, D_LDQ has 268M. The paper never specifies whether D_SHQ is repeated ~4× to reach 4.8M while D_LDQ is subsampled to 4.8M unique samples. This means the comparison in Table 5 (M_res + SFT_SHQ at 44.99 vs M_res + SFT_LDQ at 31.54) confounds data quality with repetition frequency, unique sample count, and effective training steps. The better performance on D_SHQ could be partly due to repeated exposure to a small set of examples rather than quality per se. This directly affects the headline "asymmetric principle" claim. The issue is partially mitigated by Table 8 (within-family comparison using D_ALF, a subset of D_LDQ) and Table 4 (controlled SFT across pretraining conditions), but the paper's most direct evidence for the quality-over-diversity-in-SFT claim (Table 5) remains confounded.

### Minor

1. **Abstract numbers don't match body numbers.** The abstract claims an "11% average gain" for diversity in pretraining, but the body reports 9.09% (M_LDQ vs M_SHQ, Section 5). The abstract claims "15% average gain with high quality data" for SFT, but the body shows 13.45% (M_res+SFT_SHQ vs M_res+SFT_LDQ, Table 5). These discrepancies likely arise from using different reference points (comparing to M_base vs comparing to M_SHQ), but are not explained, creating unnecessary confusion.

2. **SFT training protocol is underspecified.** Beyond batch size (512) and context length (32k), the paper does not report the number of training steps, epochs, or how "4.8M reasoning samples" is operationalized. This makes it impossible to assess whether comparisons across SFT datasets are fair or to reproduce the experiments.

3. **RL comparison is limited to two model variants.** Only M_base + SFT_SHQ and M_LMQ + SFT_SHQ are taken to the RL stage. While these represent the two extremes and the results are striking, including at least one intermediate pretraining condition (e.g., M_LDQ or M_SHQ) would strengthen the claim that "pretraining strategy dictates final accuracy."

4. **No decontamination analysis.** The reasoning datasets cover tasks similar to evaluation benchmarks (GSM8K, MATH, AIME). The paper does not report whether benchmark tasks were removed from training data or provide any overlap analysis. Given standard practices in the field, this should be addressed.

### Trivial

- Table 2's large drop from Table 1 to Table 2 is explained by adding harder benchmarks (AIME, GPQA) to the SFT evaluation suite, but this is not stated explicitly. A brief explanation would prevent confusion.

## Nice-to-Haves

- Including M_LDQ or M_SHQ in the RL phase would strengthen the claim about pretraining strategy dictating final accuracy.
- Error bars or variance estimates for the reported results would help assess the reliability of observed gaps (especially the +4.25% latent effect).
- The ALF dataset (answer length >4096 tokens) is acknowledged as a proxy for complexity, but the interpretive weight placed on it (Table 8) could be contextualized with qualitative examples of what makes the longer answers higher quality.

## Removed Points

- **Harsh critic's "structural flaw" characterization:** The critic labels the SFT exposure issue as a "structural flaw" that undermines the core claims. While the issue is real and major, it does not invalidate the paper's central front-loading finding (supported by multiple clean comparisons), nor does it affect the latent effect finding (Table 4 uses controlled SFT) or the SFT scaling findings (Table 8 uses within-family comparisons). The "structural flaw" framing overstates the scope of the problem. The weakness is retained but as Major, not Fatal.
- **Criticism that catch-up experiment "starts from a baseline with more general pretraining tokens":** This is factually correct (M_base has 1T general tokens vs ~920B for reasoning models), but this makes the comparison *more* favorable to the baseline, not less. If the baseline still can't catch up despite having more general data, the finding is stronger, not weaker.
- **Strength Finder's generic strengths about "problem importance" and "timely question":** Removed as per filtering rules — these are generic and not specific to the paper's evidence.
- **Strength Finder's claim about "systematic control across both training stages":** Partially weakened by the SFT exposure issue. The pretraining control is genuinely strong; the SFT control is incomplete.
- **Strength Finder's praise of "broad evaluation suite":** Retained implicitly in the review but not as a separate strength, as the evaluation is standard for the field.
- **Harsh critic's complaint about "missing related works":** Removed per filtering rules.
- **Harsh critic's writing/presentation nitpicks:** Removed per filtering rules.

## Novel Insights

The reviews surfaced an important tension: the paper's strongest contribution (front-loading creates a durable, compounding advantage) and its weakest link (SFT quality-dominance claim from a confounded comparison) are presented as part of a unified "asymmetric principle," but they have very different evidentiary support. The front-loading finding survives the confound; the quality-over-diversity-in-SFT claim does not. This suggests the paper would be better served by decoupling these claims and presenting the SFT quality evidence with appropriate caveats. The reviewers did not highlight this decoupling explicitly, but it emerges from cross-referencing the confounded and unconfounded experiments.

## Suggestions

1. **Clarify and control SFT exposure.** Report how many unique samples, repetitions, and total gradient steps were used for each SFT run. If the current setup is confounded, re-run the critical SFT comparisons (especially Table 5) under controlled conditions: either (a) match the number of unique examples across datasets by subsampling D_LDQ to 1.2M, or (b) match total training steps while controlling repetition factor. If the quality advantage persists, it significantly strengthens the claim.

2. **Align abstract numbers with body reports** by explicitly stating the reference comparisons used for each percentage gain. If different baselines are used for different claims, state this clearly.

3. **Add the missing SFT training details** (steps/epochs, how "4.8M samples" is constructed from each dataset) to the experimental setup section.

4. **Expand the RL phase** to include at least one more pretraining condition (e.g., M_LDQ or M_SHQ) to strengthen the claim about compounding gains.

5. **Add a brief decontamination statement** about whether evaluation benchmarks overlap with training data.

6. **Acknowledge the SFT exposure limitation** explicitly in the paper, even if the authors believe it does not affect the conclusions.

## Score and Decision

The paper makes a credible attempt at a timely and important question, with impressive experimental scale. The central finding about front-loading reasoning data is well-supported. However, the SFT exposure confound is a significant methodological gap that undermines one of the paper's headline claims (the "asymmetric principle"). The issue is resolvable with additional experiments or clarification, but as presented, the evidence for the quality-dominance-in-SFT claim is not fully convincing.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>