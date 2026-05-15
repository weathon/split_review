Here is my consolidated final review.

---

## Summary

This paper introduces LAION-Comp, a large-scale dataset (540K image–scene graph pairs) built by annotating LAION-Aesthetics V2 with GPT-4o-generated scene graphs encoding objects, attributes, and inter-object relations. The authors also propose CompSGen Bench, a dedicated evaluation benchmark of 20,838 complex scenes, and fine-tune four diffusion/flow-matching backbones (SD1.5, SDXL, SD3.5, FLUX) augmented with a GNN-based scene graph encoder. Experiments show that SG2IM models trained on LAION-Comp outperform both prompt-only T2I baselines and prior SG2IM methods trained on COCO-Stuff or Visual Genome, demonstrating that high-quality structural annotations at scale improve compositional generation.

## Strengths

- **Large-scale, high-quality scene graph dataset with broad coverage.** LAION-Comp contains 540K image–SG pairs—an order of magnitude larger than existing SG datasets such as COCO-Stuff (~118K) and Visual Genome (~108K). The annotation pipeline uses GPT-4o with partial human verification, achieving reported accuracies of 98.8% (objects), 97.5% (attributes), and 95.7% (relations). The dataset captures 77.48% non-spatial relations (vs. 41.98% in VG), moving beyond predominantly spatial annotations to include abstract, functional semantics (Sec. 3.2, Fig. 4).

- **Consistent gains across diverse backbones and held-out datasets.** SDXL-SG, SD3.5-SG, and FLUX-SG all outperform their SG2IM counterparts (SGDiff, SG-Adapter) trained on the same backbone when trained on LAION-Comp vs. COCO or VG (Table 2). The fact that gains replicate across diffusion (SD1.5, SDXL) and flow-matching (SD3.5, FLUX) architectures—and on cross-dataset evaluation (COCO test, VG test)—provides reasonable evidence that the dataset itself drives improvement, not just the conditioning modality. For instance, SGDiff achieves SG-IoU 0.435 on COCO but 0.531 on LAION-Comp, and SDXL-SG achieves SG-IoU 0.497 on COCO vs. 0.558 on LAION-Comp (Table 2).

- **CompSGen Bench fills a gap for SG-based evaluation.** Existing compositional benchmarks (T2I-CompBench, HRS-Bench, GenEval) focus on text prompts. CompSGen Bench provides 20,838 complex scenes with structured SG annotations and metrics (SG-IoU, Entity-IoU, Relation-IoU) that directly measure compositional fidelity, filling a genuine gap in the evaluation ecosystem.

- **Ablation confirming data scaling benefits.** The proportion-based ablation (10% → 100% of LAION-Comp, fixed iterations) shows monotonic improvement: SDXL-SG SG-IoU rises from 0.530 to 0.558 and FID drops from 27.3 to 20.1 (Table 4). The 10% subset (~48K samples) is smaller than VG (~108K) yet yields competitive or better scores than VG-trained models, suggesting annotation quality contributes beyond sheer volume.

## Weaknesses

### Major

1. **Primary benchmark (CompSGen Bench) is derived from the same data distribution as training.** CompSGen Bench is curated from the 50,000-image test set of LAION-Comp itself (Sec. 3.3). Models trained on LAION-Comp are therefore evaluated on images from the same source and with annotations produced by the same GPT-4o pipeline. While Table 2 provides cross-dataset evaluation on COCO and VG test sets, and the paper mentions T2I-CompBench results in the appendix, the headline quantitative results in Table 3 (which directly support the claim that LAION-Comp-trained models set a new state of the art) are primarily on CompSGen Bench. The community would benefit from an out-of-distribution evaluation on a fully human-annotated SG benchmark or a held-out dataset annotated by an independent pipeline to confirm that the gains are not partly due to distributional overlap or annotation-style bias.

2. **The central comparison against prompt-only T2I models conflates conditioning modality with dataset quality.** The paper contrasts SDXL, SD3.5, FLUX (text prompts only) with SDXL-SG, SD3.5-SG, FLUX-SG (structured scene graphs) and attributes the gap to the dataset (Sec. 5.1, Table 2). However, the advantage may come entirely from the richer input modality, not from LAION-Comp specifically. This comparison is valid for demonstrating that structured conditioning helps, but it does not isolate the dataset's contribution. Fortunately, this does not invalidate the paper's core claim: the SG2IM comparisons (SGDiff/SG-Adapter/SDXL-SG on COCO vs. VG vs. LAION-Comp) do hold the conditioning modality constant and show a clear dataset-level advantage. The paper should more clearly separate these two arguments.

3. **Annotation quality metrics are largely self-referential.** The reported accuracies (98.8%/97.5%/95.7%) and the SG-IoU+/Ent-IoU+/Rel-IoU+ metrics in Table 1 and Figure 3 are computed against GPT-4o's own outputs as "ground truth." While the paper mentions partial human verification (Sec. 3.1), the proportion of samples verified, the exact protocol, and how accuracy is measured (exact match vs. relaxed) are not specified in the main text. Any systematic bias in the GPT-4o annotations (e.g., missed objects, hallucinated relations, format errors) will be invisible in self-consistency checks and will propagate to both training and evaluation. Including a quantified human-annotation subset for evaluation would substantially strengthen the paper.

### Minor

1. **No text-only fine-tuning control on the same data.** A natural control experiment would be to fine-tune SDXL on LAION-Comp's *original text captions* (without scene graphs) for the same number of steps, then evaluate on CompSGen Bench. This would disentangle whether the SG2IM gains come from the structural annotations or simply from additional fine-tuning on higher-quality images. While the SG2IM cross-dataset comparison (Table 2) partially addresses this, the control is missing.

2. **FID is used as a quality metric despite acknowledged degradation.** The paper states that "fine-tuning pre-trained T2I models inevitably increases FID scores" (Sec. 5.1), yet FID is reported as a quality metric in both Table 2 and Table 3. In Table 2, SDXL achieves FID 19.3 while SDXL-SG achieves 20.1; similar patterns hold for SD3.5 and FLUX. The FID and the accuracy metrics thus pull in opposite directions. The paper should either adopt a quality metric that does not penalize fine-tuning (e.g., CLIP score, which is included in Table 3) or explicitly justify why FID is still meaningful in this fine-tuning context.

3. **The ablation on data proportion does not fully distinguish quality from quantity.** The proportion ablation (Table 4) shows that more data helps, but the 10% condition uses ~48K samples—still larger than several existing SG datasets. A matched-size comparison (e.g., subsample LAION-Comp to exactly match COCO's 118K or VG's 108K) would more cleanly attribute gains to annotation quality rather than scale. The paper does note that 10% of LAION-Comp outperforms VG on several metrics, which is suggestive, but a precise head-to-head at identical sample sizes would be more convincing.

### Trivial

- None beyond typical formatting artifacts introduced by the PDF extraction process.

## Nice-to-Haves

- Evaluate LAION-Comp-trained models on a fully human-annotated SG benchmark (e.g., test split of Visual Genome with human SGs) to eliminate self-referential evaluation concerns.
- Compare against one or two layout-based conditioning methods (e.g., GLIGEN, BoxDiff) using the same backbone and training data, to contextualize SG conditioning within the broader controllable generation landscape—though this is outside the paper's core scope.
- Include a failure case analysis showing systematic errors of LAION-Comp-trained models (e.g., attribute binding failures, missing objects) rather than only successes.

## Removed Points

These points are flagged to be removed from the main weakness list; treat them with caution:

1. **"No comparison against layout- or region-conditioned baselines"** — Removed as scope creep. The paper focuses on SG-based generation; the related work section mentions layout methods as alternative approaches, not as required baselines. A comprehensive comparison across conditioning modalities is a different paper.

2. **"FID trends contradict the conclusion of better quality"** — Removed because the paper transparently acknowledges that fine-tuning increases FID (Sec. 5.1: "Fine-tuning pre-trained T2I models inevitably increases FID scores") and relies primarily on SG-IoU/Entity-IoU/Relation-IoU for its core claims. The FID reporting is standard practice in the literature.

3. **"Ablation does not compare datasets at the same scale"** — Removed because the paper does address this: "in the 10% LAION-Comp ablation, where the data volume is smaller than that of VG, the model's FID and Entity-IoU scores still outperform the results trained on VG" (Sec. 5.2). A precise matched-size experiment would strengthen the paper but the existing analysis is reasonable.

4. **Missing related works** — Removed per policy, as I cannot verify what related works exist or do not exist without access to the full literature.

5. **Missing appendix content** — Removed per policy (the appendix was stripped by the parser, it exists in the original submission).

## Novel Insights

Beyond the paper's own contributions, the most interesting finding from the review is the tension between modality-conditioning and data-quality effects. The harsh critic correctly notes that T2I vs. SG2IM comparisons conflate these factors, but a careful reading of Table 2 reveals that the *within-modality* comparisons (SG2IM models trained on different datasets) actually provide cleaner evidence for the dataset's value. This suggests the paper would benefit from reframing its narrative to foreground the within-SG2IM comparisons and relegate the T2I comparison to a secondary demonstration of structured conditioning's benefits. The reviewer's "circular evaluation" concern, while partially valid, overlooks the cross-dataset evaluations in Table 2. The net effect is that the paper's core claims are supportable but overstated, and the presentation conflates independent arguments.

## Suggestions

1. **Separate the two narratives clearly.** Distinguish between (a) "structured conditioning (SGs) helps over text-only prompts" and (b) "LAION-Comp's annotation quality and scale improve over existing SG datasets." The former should cite the T2I comparison as supporting but secondary; the latter should be the main claim backed by the within-SG2IM comparisons.

2. **Add a text-only fine-tuning control.** Fine-tune SDXL on LAION-Comp's original captions (no SGs) for the same steps and evaluate on CompSGen Bench. This small experiment would cleanly isolate whether the SG gains come from the structural format or from other properties of the LAION-Comp image selection.

3. **Clarify the evaluation reference distributions.** The paper should explicitly state for Table 2 which test set each model is evaluated on, since FID values differ across datasets and the current table caption is ambiguous.

4. **Add a human-annotated evaluation subset.** Even 200–300 human-annotated samples from the CompSGen Bench would provide an anchor for the automated metrics and address the self-referential annotation concern.

## Calibration Anchors

| Path | Avg Human Score | Comparison to This Paper |
|---|---|---|
| `EwdWR6lfvW.md` (Generate Any Scene) | 5.00 | Similar topic (SG-driven data for generative models). That paper's data engine is synthetic, while LAION-Comp provides real image–SG pairs. This paper has more extensive backbone evaluation but similar evaluation-design concerns about distribution overlap. Slightly weaker due to evaluation issues. |
| `iqAFhWistW.md` (T2I-CoReBench) | 6.00 | Stronger paper—comprehensive evaluation framework with 12 dimensions, 28 models, clean benchmarking methodology. This paper has a valuable dataset contribution but less rigorous evaluation design. |
| `nrZW60mzeW.md` (CompGen Curriculum) | 4.00 | Also uses scene graphs for compositional T2I. That paper was withdrawn/rejected due to unclear method and weak baselines. This paper is stronger—clearer contribution (dataset + baselines) and more thorough evaluation. |
| `ddFN3lWpIr.md` (SpatialGenEval) | 5.00 | Similar structure (benchmark + fine-tuning dataset). Accepted poster with cleaner evaluation. This paper's dataset is larger but the evaluation has more confounds. |
| `DealNNlz94.md` (Object-Centric Repr.) | 3.00 | Rejected—claims not fully supported by evidence, narrow scope. This paper is stronger in scope and practical contribution. |
| `Omo8RAEqSS.md` (TESA) | 2.00 | Rejected/withdrawn—weak methodology, oracle conditioning, poor reproducibility. This paper is substantially stronger. |
| `wAb8vtEZfM.md` (Size Doesn't Matter) | 1.20 | Clear reject—incoherent presentation, unsupported claims. Not comparable; this paper is far above this level. |

## Score and Decision

The paper provides a genuinely useful resource (LAION-Comp dataset with 540K SG annotations, CompSGen Bench) and demonstrates that SG2IM models benefit from larger, higher-quality structural annotations. The main empirical evidence is partially confounded by evaluation on a same-distribution benchmark and by conflating conditioning modality with dataset quality in some comparisons. However, the within-SG2IM cross-dataset comparisons (Table 2) partially address these concerns, and the dataset itself is a contribution that the community can build on regardless of evaluation quibbles. The paper is meaningfully stronger than the typical 3–4 range reject papers in the calibration set but falls short of the rigor expected for a strong accept (6+). Positioned relative to the anchored reviews, a score of **4.0** reflects a paper with real contributions that are somewhat undermined by evaluative confounds that should be addressed.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>