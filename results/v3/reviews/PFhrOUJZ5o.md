## Summary

This paper introduces LAION-Comp, a large-scale dataset of 540K+ aesthetic images annotated with scene graphs (objects, attributes, relations) built on LAION-Aesthetics V2 (6.5+). The authors also introduce CompSGen Bench, a 20,838-sample benchmark for complex scene generation, and train several T2I backbones (SDXL, SD3.5, FLUX) with a GNN-based scene graph encoder. The core thesis is that the bottleneck for compositional generation is data quality/scale rather than architecture. The dataset is a potentially valuable community resource, and the annotation pipeline (GPT-4o with structured prompts + partial human verification yielding 98.8%/97.5%/95.7% accuracy) is well-designed. However, the evaluation that is meant to validate the dataset's superiority suffers from significant reporting gaps and missing baselines.

## Strengths

1. **Large-scale, high-quality scene graph dataset.** LAION-Comp provides 540K scene-graph–image pairs on carefully curated aesthetic images, roughly 40× larger than prior SG datasets (COCO-Stuff, Visual Genome). The annotation pipeline enforces well-motivated design choices (abstract adjectives for attributes, concrete verbs for relations, unique IDs for distinct objects) and achieves high human-verified accuracy (98.8% objects, 97.5% attributes, 95.7% relations). This is the paper's primary contribution and a genuine community resource.

2. **CompSGen Bench enables targeted evaluation of complex scenes.** The benchmark filters 20,838 test samples requiring ≥4 relations, filling a gap in compositional evaluation. On this benchmark (Table 3), the proposed models (SDXL-SG, SD3.5-SG, FLUX-SG) consistently outperform T2I (SD1.5, SDXL) and SG2IM (SGDiff, SG-Adapter) baselines on SG-IoU, Entity-IoU, and Relation-IoU, demonstrating the benefit of SG conditioning when the comparison is controlled.

3. **Ablation shows data quality matters more than scale.** Table 4 demonstrates that even 10% of LAION-Comp (≈48K samples) yields Entity-IoU scores (0.874) exceeding the full Visual Genome model (0.813), while SG-IoU is comparable (0.530 vs 0.546). This provides concrete evidence for the paper's central claim that annotation quality is a critical factor.

4. **GNN-based encoder is backbone-agnostic.** The SG encoder produces consistent gains across diffusion (SDXL, SD3.5) and flow-matching (FLUX) backbones, showing the approach is not tied to a single architecture.

5. **Rich non-spatial relation coverage.** LAION-Comp contains 77.48% non-spatial relations vs 41.98% in Visual Genome, capturing more functional/interaction-based semantics and making the dataset more challenging and realistic for compositional generation.

## Weaknesses

### Major

1. **Test set for cross-dataset comparison (Table 2) is never explicitly stated.** Table 2 compares models trained on COCO, Visual Genome, and LAION-Comp, with a "Dataset" column that indicates training data. The paper does not state what test set these models are evaluated on. The ablation section (Sec. 5.2) cross-references Table 2's VG-trained results, implying all models in Table 2 share a common test set (likely the LAION-Comp 50K-image test set). But this must be inferred rather than read. If instead each row uses its own dataset's test set, the central claim that "results trained on LAION-Comp consistently outperformed those trained on COCO and VG" would be invalid because different test sets have different difficulty and reference annotations. Every quantitative experiment in the paper should explicitly state the evaluation set. This is the single most important revision needed.

2. **Missing T2I baselines for strongest backbones on CompSGen Bench (Table 3).** Table 3 evaluates models on the CompSGen Bench but only includes T2I baselines SD1.5 and SDXL. The original, unmodified SD3.5-Medium and FLUX.1-Dev are **not** evaluated on this benchmark, despite being the backbones for SD3.5-SG and FLUX-SG. Without this comparison, the paper cannot support the claim that SG conditioning improves over text-only conditioning for the strongest models on this benchmark — the advantage might come entirely from the stronger backbone. This omission weakens one of the paper's central claims.

3. **Internal inconsistency about FID.** The paper states "Fine-tuning pre-trained T2I models inevitably increases FID scores" (Sec. 5.1). Yet in Table 2, SD3.5-SG (20.8) has *lower* FID than SD3.5-Medium (24.6), and FLUX-SG (24.7) has *lower* FID than FLUX.1-Dev (26.2). If test sets are the same (as the controlled interpretation requires), this directly contradicts the claim. If test sets differ, the comparison is incoherent. Either way, the paper should clarify and discuss this.

### Minor

4. **Table 1 statistics based on only 300 samples out of 540K.** While labeled, this is too small a sample for drawing population-level conclusions about annotation length and accuracy characteristics. The paper should either provide dataset-wide statistics or acknowledge the limitation.

5. **Human verification sample size not reported in main text.** The paper states 98.8%/97.5%/95.7% accuracy (Sec. 3.1) and references Sec. A.5, but the main text does not state how many samples were verified. This makes it difficult to assess the reliability of these numbers.

6. **Scene graph predictor accuracy for SG-IoU/Entity-IoU/Relation-IoU metrics not discussed.** These metrics (from Shen et al., 2024) rely on a scene graph predictor whose accuracy is never reported. If the predictor is weak or biased toward certain relation types, the metrics become unreliable. The paper should at least cite the predictor's performance and discuss potential biases.

### Trivial

7. "Dataset" column heading in Table 2 is ambiguous — it could mean training dataset, evaluation dataset, or both.

## Nice-to-Haves

- Including SD3.5-Medium and FLUX.1-Dev as T2I baselines in Table 3 would directly demonstrate the benefit of SG conditioning for the strongest backbones.
- Reporting human verification sample size in the main text.
- Computing Table 1 statistics on a larger subset or the full dataset.
- Brief discussion of GPT-4o annotation biases (e.g., preference for certain object types, omission of rare relationships).

## Removed Points

These points were flagged for removal. Treat them with caution.

- **Harsh critic: "The paper's central contribution rests on an unverifiable comparison."** — Overstated. Table 3 provides controlled evidence on CompSGen Bench, and the ablation section's cross-references strongly imply a common test set for Table 2. The issue is under-specification, not invalidity. The comparison is verifiable once the test set is clarified. (Moved from Fatal to Major weakness #1, re-framed as an ambiguity that needs clarification.)

- **Harsh critic: "If the evaluation sets differ, this further highlights the lack of controlled comparison" (re: FID).** — Combined into Major weakness #3 (FID inconsistency).

- **Harsh critic: "CompSGen Bench selects only those test samples with over four relations... However, the metrics SG-IoU, Entity-IoU, and Relation-IoU depend on a scene-graph predictor whose accuracy is never reported."** — Moved to Minor weakness #6.

- **Harsh critic: "The paper should compute these statistics over the entire dataset or at least a much larger random subset."** — Moved to Minor weakness #4.

- **Strength Finder: "Models trained on LAION-Comp consistently outperform corresponding models trained on previous SG datasets on SG-IoU, Entity-IoU, and Relation-IoU (Table 2). This directly validates the claim that high-quality structural annotations are crucial."** — The evidence depends on the test set being controlled; weakened to note the ambiguity.

- **Strength Finder: "Human-verified annotation accuracy provides a reliable foundation."** — Kept as Strength #1 but sample size issue noted in Minor weaknesses.

- **Strength Finder: "Ablation experiments demonstrate that dataset quality is more important than sheer scale."** — Kept as Strength #3. However, the cross-comparison with VG in the text depends on the common test set assumption, noted in Major weakness #1.

## Novel Insights

None beyond the paper's own contributions. The primary insight — that large-scale, high-quality structural annotations improve compositional generation — is demonstrated by the data but the central comparison is undermined by reporting gaps.

## Suggestions

1. **Explicitly state the test set for every experiment.** For Table 2, specify whether all rows are evaluated on the LAION-Comp test set (or CompSGen Bench, or each dataset's own test set). If all models share the LAION-Comp test set, state this clearly.

2. **Add SD3.5-Medium and FLUX.1-Dev as T2I baselines in Table 3** to directly demonstrate the benefit of SG conditioning over text-only conditioning for the strongest backbones.

3. **Correct or clarify the "inevitably increases FID" statement** — acknowledge that fine-tuning on a large, in-distribution dataset can decrease FID on that distribution.

4. **Report human verification sample size** in the main text.

5. **Compute dataset statistics (object counts, accuracy metrics) on a larger sample** or the full 540K dataset.

6. **Add a brief discussion of the scene graph predictor's accuracy** (used for SG-IoU etc.) and potential limitations of the SG-IoU metrics.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Round / Query | Comparison |
|------|-----------|---------------|------------|
| V73W8MXnNW | 3.00 | R1-topic-low | Unrelated paper; paper under review is clearly stronger |
| TCSaLeANpN | 3.00 | R1-topic-low | Unrelated paper; paper under review is clearly stronger |
| KCYDpqSpqg (SG-Adapter) | 5.50 | R1-topic-mid | Directly comparable SG2IM paper with small dataset (309 images). This paper has larger dataset but evaluation clarity issues SG-Adapter didn't have. Moderately worse overall due to reporting gaps. |
| haJHr4UsQX | 6.67 | R1-topic-mid | Stronger paper with cleaner evaluation. This paper is weaker. |
| 3i13Gev2hV | 8.00 | R1-topic-high | Much stronger paper. Not comparable. |
| LDu822E45Q (EEVEE) | 4.25 | R1-weakness-ambiguous-eval | Paper with unclear evaluation protocol, scored low (4.25). This paper shares this failure mode. |
| Im2neAMlre | 7.33 | R1-weakness-evaluation | Strong T2I evaluation paper. Not comparable. |
| QVBeBPsmy0 (Mitigating Comp.) | 4.50 | R2 | Rejected paper about compositional T2I with limited comparisons. Comparable weakness profile. |
| ITq4ZRUT4a (Davidsonian SG) | 6.00 | R2 | Accepted, cleaner evaluation. This paper is weaker. |
| 0YXckVo7Kw (MMCOMPOSITION) | 5.50 | R2 | Rejected, similar topic area but different focus. |

**Round 1 bracket:** 3.5–5.5.

**What the low-band anchors failed at:** Papers in the low band (3.0) offered no significant dataset or performance contribution. The paper under review does not share this failure — LAION-Comp is a genuinely large-scale resource.

**What the weakness-anchored queries showed:** Papers with unclear evaluation protocols or missing baselines (e.g., EEVEE at 4.25, Mitigating Compositional Issues at 4.5) consistently scored in the 4–5 range. The paper under review shares these specific failure modes.

**Final score position:** The paper sits between SG-Adapter (5.5) and the weaker ambiguity/omission papers (4.25–4.5). It has a larger dataset than SG-Adapter but worse evaluation reporting. The missing SD3.5/FLUX baselines and test set ambiguity are the deciding factors that prevent a higher score. The dataset contribution is valuable but the evaluation evidence for the central claim is currently incomplete.

**Score:** 4.5  
**Decision:** Reject

The paper has a meaningful dataset contribution, but the evaluation is insufficiently specified to support the central claims. The test set for Table 2 is ambiguous, the strongest backbones lack text-only baselines on CompSGen Bench, and the FID statement is internally inconsistent. These issues are fixable in major revision.

<score>4.5</score>
<decision>Reject</decision>