## Summary

This paper introduces **grounding-IQA**, a new IQA task paradigm that integrates multimodal referring and grounding (i.e., bounding box coordinates) into image quality assessment. The paradigm comprises two subtasks: GIQA-DES (quality descriptions with spatial localization) and GIQA-VQA (quality QA with location information). To realize this, the authors construct **GIQA-160K** (167K instruction-tuning samples from 43K images via an automated four-stage pipeline using Llama3, Grounding DINO, and a Q-Instruct-based IQA-Filter), and establish **GIQA-Bench** (100 images, 250 test samples with multi-expert annotation). Four MLLMs (LLaVA-1.5/1.6, mPLUG-Owl2) fine-tuned on GIQA-160K are evaluated against general MLLMs, grounding models (Shikra, Kosmos-2, Ferret, GroundingGPT), and IQA models (Q-Instruct, DepictQA), showing that the proposed method achieves competitive description quality (LLM-Score 60–63) and grounding precision (mIoU 0.55–0.66) simultaneously, whereas prior models excel at only one or the other.

## Strengths

- **Novel task formulation that bridges two active research areas.** Combining spatial grounding with IQA is a natural and well-motivated extension of the progression from score-based → description-based → grounded quality assessment. The two subtasks (GIQA-DES, GIQA-VQA) cleanly operationalize how spatial information can interact with quality perception (referring: position in; grounding: position out). This fills a clear gap: prior IQA models cannot localize quality-relevant regions, and prior grounding models cannot assess quality.

- **Systematic dataset construction pipeline with quality controls.** The four-stage pipeline (object tag extraction via Llama3 with CoT-style quality-effect classification → Grounding DINO detection → IQA-Filter + Box-Merge refinement → discretized coordinate transformation) is well-structured. The ablation in Table 2a validates that refinement (IQA-Filter + Box-Merge) improves mIoU from 0.5624 → 0.5851 and BLEU@4 from 20.97 → 23.67, and the box area distribution analysis (Fig. 6) shows refinement brings automatically generated boxes closer to human annotations.

- **Comprehensive baseline comparison across four model families.** Table 5 compares 4 general MLLMs, 4 grounding MLLMs, 4 IQA models (Q-Instruct on 3 backbones + DepictQA), and 4 fine-tuned variants across 9 metrics. This is thorough and clearly demonstrates the complementary failure modes of prior work: grounding models achieve mIoU 0.34–0.68 but LLM-Scores of only 27.00–43.75 on quality description, while IQA models achieve LLM-Scores of 56.50–62.00 but produce N/A grounding metrics. The proposed method bridges this gap, achieving both reasonable grounding (mIoU 0.55–0.66) and competitive quality assessment (LLM-Score 60–63).

- **Data compatibility demonstrated across diverse backbones.** Table 4 shows consistent grounding-IQA improvement when fine-tuning LLaVA-1.5-7B/13B, LLaVA-1.6-7B, and mPLUG-Owl2-7B on GIQA-160K, with GIQA-VQA mIoU increasing from N/A to 0.52–0.74 across models, suggesting the dataset is not architecture-specific.

## Weaknesses

### Fatal
None.

### Major

- **The benchmark is too small to support fine-grained conclusions.** GIQA-Bench contains only 100 images and 250 test samples, split into 100 GIQA-DES, 90 GIQA-VQA Yes/No, and 60 GIQA-VQA What/Which/How. Many reported metric differences correspond to 1–2 samples (e.g., Acc(W) differences of 0.025 on 60 samples). No confidence intervals or significance tests are reported. While small expert-annotated benchmarks are common in IQA, the 60-sample open-ended VQA split in particular has insufficient statistical power for the paper's comparative claims. The authors mention supplementary experiments on traditional score-based IQA tasks, but these are deferred to the supplementary material and do not appear in the main paper's 9-page body.

- **The evaluation framework measures description quality and grounding precision separately, not their synergy.** Description quality (BLEU@4, LLM-Score) is computed "excluding coordinates," meaning it evaluates text quality independent of spatial information. VQA accuracy measures answer correctness without evaluating whether spatial references matter. The paper's central claim that grounding enables "more fine-grained quality assessment" would be strengthened by an experiment showing that grounded descriptions are more useful or informative than ungrounded ones—for example, via a human evaluation comparing text+bounding-box descriptions against text-only descriptions on informativeness, precision, or utility for downstream tasks like image editing. Without this, the contribution is demonstrated as "models can do both tasks" rather than "grounding improves quality assessment."

- **The automated pipeline's dependence on Q-Instruct for filtering creates a weak circularity concern.** Q-Instruct is used in the IQA-Filter (Stage 3) to verify whether a box patch matches a quality attribute (Tq) inferred by Llama3, and Q-Instruct itself is then a baseline comparison method in Table 5. While this is mitigated by the fact that (a) Q-Instruct is only a binary filter, not a label generator—the actual quality descriptions come from human annotations—and (b) the ablation shows refinement improves over raw boxes, the concern remains that the filtering may embed Q-Instruct's specific failure patterns into the training data. The paper would benefit from an analysis of the filter's accuracy (e.g., human evaluation of a sample of filtered vs. rejected boxes) to quantify this risk.

### Minor

- **Selective reporting in the box representation ablation.** Table 2b shows that Norm-Coord achieves higher mIoU (0.6046) than Disc-Coord (0.5851), but the paper's claim ("Disc-Coord enhances description quality and grounding accuracy") only highlights Tag-Recall (0.5497 vs. 0.5490) and text metrics while omitting the mIoU degradation. The full picture—a trade-off between coordinate precision (mIoU) and text learning ease (BLEU@4, LLM-Score)—should be stated explicitly.

- **Multi-task training shows mixed evidence for grounding improvement.** Table 3 shows that GIQA-160K (joint DES+VQA training) achieves GIQA-DES mIoU of 0.5474, which is *lower* than Only-DES (0.5497). While the difference is tiny (0.0023) and likely noise, the paper's statement that "joint training enhances performance on both" overstates what the data support for the DES grounding metric. Similarly, the claim that GIQA-VQA "exhibits limited grounding information compared to GIQA-DES" (for Only-VQA mIoU of 0.4872 on DES) is expected since VQA-only models haven't seen DES data.

- **The Q-Instruct-filtered ablation improvements could reflect multiple factors.** The refinement step (IQA-Filter + Box-Merge) improves metrics, but it's unclear how much each sub-component contributes independently. The IQA-Filter's binary quality verification uses Q-Instruct on cropped patches—a distribution shift from Q-Instruct's training data—and the reliability of this process on small patches is unexamined.

### Trivial

- None that survive filtering (parser artifacts and format nitpicks removed).

## Nice-to-Haves

- A human evaluation study comparing grounded vs. ungrounded quality descriptions on informativeness and precision.
- Confidence intervals or bootstrap estimates for the GIQA-Bench metrics to clarify which differences are reliable.
- Error analysis of the automated pipeline: what fraction of automatically generated boxes are correct, and what failure modes does the IQA-Filter miss?

## Removed Points

- **Criticism about "circular dependency" being structural/fatal** — removed because Q-Instruct is used only as a binary filter in the pipeline, not as a label generator. The actual quality descriptions come from human-annotated datasets (Q-Pathway, DQ-495K), breaking the circularity. The ablation in Table 2a also validates that refinement (not just Q-Instruct's biases) improves results.

- **Criticism that N/A for baseline grounding metrics avoids showing their capability** — removed because the paper explicitly includes a "Ground" model category (Shikra, Kosmos-2, Ferret, GroundingGPT) that does output bounding boxes and is evaluated on all metrics. N/A for general and IQA models is appropriate since they are not designed to produce box outputs.

- **Criticism about "tautological task definition"** — removed as a philosophical nitpick. Task-relevant regions are defined by human annotation, which is standard practice in vision tasks.

- **Criticism about data statistics inconsistency (50,484 + 50,484 = 100,968)** — removed because the numbers are consistent: the paper reports that after random filtering to balance types, the total remains 100,968. This is clear and not contradictory.

- **Criticism about grid discretization not being ablated** — weakened to nice-to-have; a grid-size ablation (different n,m values) would strengthen the paper but its absence is not a core flaw.

- **Criticism about BLEU@4 correlating poorly with human judgment** — weakened; this is a known limitation of BLEU@4, but the paper also uses LLM-Score as a complementary metric, partially mitigating this concern.

- **Claim that "multi-task training hurts GIQA-DES grounding" (0.5497→0.5474)** — preserved above as a minor weakness since the paper's claim ("enhances both") slightly overstates, but the difference is within noise range.

- **Generic strengths from Strength Finder** (e.g., "comprehensive benchmark with multi-faceted evaluation") — narrowed to specific verifiable achievements above.

## Novel Insights

None beyond the paper's own contributions. The key observation—that prior grounding models fail on quality perception (LLM-Score 27–43) and prior IQA models lack any grounding capability (N/A on all grounding metrics)—is well demonstrated by the paper's comparative evaluation and cleanly motivates the contribution.

## Suggestions

1. Expand GIQA-Bench to at least 300–500 images with more balanced splits, or provide bootstrap confidence intervals for all metrics to enable readers to assess which differences are significant.
2. Add a human evaluation study where raters compare grounded (text+boxes) vs. ungrounded (text-only) quality descriptions on informativeness, precision, and usefulness—this would directly validate the "more fine-grained" claim.
3. Report the ablation tables with both mIoU and Tag-Recall trade-offs explicitly discussed (e.g., Norm-Coord vs. Disc-Coord), rather than selectively highlighting only the metrics that favor the chosen design.
4. Provide an analysis of the IQA-Filter's accuracy on a random sample of filtered vs. rejected boxes, to quantify any Q-Instruct bias introduced during dataset construction.
5. Include the supplementary experiments on traditional score-based IQA in the main paper, as they help validate that grounding-IQA does not degrade standard IQA performance.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/9syH2SseOy.md` (IQA-Octopus) | 4.00 (Reject) | Very similar scope (grounding+reasoning for IQA). Current paper is stronger: larger dataset (160K vs 33K), more systematic pipeline, better ablations. Current paper scores higher. |
| `/home/wg25r/review_agent/human_reviews_2026/raBRIPsdVb.md` (LLM-IQA) | 2.50 (Reject) | Training-free IQA with methodological contradictions. Current paper is substantially stronger in both clarity and contribution. |
| `/home/wg25r/review_agent/human_reviews_2026/zO8LrT9Sy9.md` (Exploring Instruction Data Quality) | 4.50 (Reject) | IQA instruction data selection. Novelty concerns. Current paper has a clearer contribution (new task) and is comparably thorough. |
| `/home/wg25r/review_agent/human_reviews_2026/INOi0YqI8p.md` (EvoQuality) | 5.00 (Accept Poster) | Self-supervised IQA. Different contribution type but similar overall quality. EvoQuality has stronger cross-dataset eval; current paper has a more novel task formulation. Comparable. |
| `/home/wg25r/review_agent/human_reviews_2026/azj53PLJRL.md` (Embodied-IQA) | 7.00 (Accept Poster) | Dataset-centric paper with clearly defined new problem, 30K images, 5M annotations. Current paper is below this anchor's scale and thoroughness. |

**Score rationale:** The paper makes a genuinely novel contribution by introducing spatial grounding into IQA as a formal task paradigm, constructing a substantial dataset via a systematic pipeline, and benchmarking extensively across four model families. Its main weaknesses are (1) a small benchmark that limits statistical power for fine-grained comparisons, (2) an evaluation framework that measures description quality and grounding separately rather than testing their synergistic benefit, and (3) minor selectivity in the reporting of ablation results. These are addressable limitations rather than fatal flaws. Relative to the calibration anchors, the paper is clearly stronger than IQA-Octopus (avg 4.00) and comparable in quality to EvoQuality (avg 5.00, accepted). It does not reach the level of Embodied-IQA (avg 7.00).

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>