- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 6, 8, 8
Now I have a thorough understanding of the paper and have verified the reviewer claims against the text. Let me compose the final consolidated review.

## Summary

This paper proposes fVLM, a fine-grained vision-language pre-training method for CT that aligns individual anatomical regions with corresponding report descriptions via an explicit anatomy-level matching strategy. To handle the proliferation of false negatives that this fine-grained framing introduces (from both normal anatomies and similar abnormal samples), the authors propose a dual false-negative reduction module combining impression-based normal-sample identification with a co-teaching training strategy. The method is trained on MedVL-CT69K (272K scans, 69K patients) and evaluated on zero-shot diagnosis (54 diseases across 15 anatomies), report generation, and two public benchmarks (CT-RATE, Rad-ChestCT), achieving substantial reported gains.

## Strengths

1. **Explicit anatomy-level alignment is well-motivated and ablated.** The core idea—moving beyond global image-report contrast to anatomy-specific matching—is clearly grounded in the clinical reality of how radiologists write reports. Table 4 (cited in the text) shows fine-grained alignment alone yields a +3.8 AUC gain over the CLIP baseline, providing direct evidence that the central methodological choice drives performance.

2. **Dual false-negative reduction addresses a genuine challenge of fine-grained contrastive learning.** The observation that fine-grained alignment introduces many more normal samples and increases inter-sample similarity among abnormal samples is insightful. The proposed combination of impression-based normal identification and co-teaching is shown (Table 4) to add another +4.0 AUC beyond the alignment gain, giving readers a clear picture of each component's contribution.

3. **Strong results on public benchmarks against fair comparisons.** On CT-RATE and Rad-ChestCT, fVLM is compared against CT-CLIP—a method designed for 3D CT—and reports absolute AUC gains of 7.4% and 4.8%. These gains are more straightforward to interpret than the in-house dataset results because both methods operate on the same 3D CT modality and data splits, and even surpass supervised fine-tuned variants of CT-CLIP.

4. **Large-scale dataset and extensive evaluation.** MedVL-CT69K at 69K patients is a substantial resource, and evaluating across 54 diseases in 15 anatomies provides a comprehensive view of model capability. The scaling-law analysis (Figure 5) showing consistent improvement across data sizes adds useful evidence of data efficiency.

## Weaknesses

### Fatal
None.

### Major
1. **Baseline adaptation procedures for LoVT, MGCA, and Merlin are not described, compromising comparison fairness.** The paper compares against LoVT and MGCA—methods originally designed for 2D chest X-rays with implicit cross-attention alignment—and against Merlin, which was designed with structured EHR data as additional supervision. The paper does not explain how these methods were adapted to operate on 3D CT volumes (e.g., whether 3D volumes were sliced/projected to 2D slides, or how the implicit local attention was scaled). For Merlin, it is unclear whether the comparison uses the same input data as fVLM or whether Merlin additionally received EHR. The large margins over these baselines (e.g., +9.4 AUC over Merlin, Table 1) cannot be confidently attributed to fVLM's design rather than to differences in adaptation quality or available supervision. This is a structural gap that weakens the central evidence from the in-house dataset.

2. **Report decomposition pipeline is critically underspecified for reproducibility.** The method depends on Qwen 2.5 to extract anatomy-level descriptions from reports, supplemented by a string-matching strategy (Section 3.1). No prompt template, context window, or any example of the LLM call is provided. The string-matching rules are illustrated with one example ("jejunum" → "small intestine") but the completeness and generation process of this rule set are not described. The decomposition quality is not evaluated (no precision/recall against expert annotations, no error analysis). Since the entire pipeline rests on this decomposition step, the lack of detail makes it impossible to assess the robustness of the downstream alignment or to reproduce the work.

### Minor
1. **Missing statistical precision for key results.** All AUC, ACC, and F1 scores are reported as point estimates without confidence intervals, standard deviations, or significance tests across the 54 diseases. Given the 54-disease aggregation and the large claimed gains, this omission makes it difficult to assess the reliability or variability of the results. (Verified: no CIs, stds, or p-values found in the paper text.)

2. **Co-teaching strategy lacks implementation detail.** The alternation between the two models is described only as "trained alternately" with different initializations, data orders, and augmentations to maintain diversity (Section 3.3). It is not specified whether alternation occurs per batch, per epoch, or at some other interval. The momentum baseline compared in Table 4 is not described (e.g., momentum coefficient). The parameter α=0.5 is used without sensitivity analysis.

3. **Visual encoding details are underspecified.** The method "update[s the query token] via a self-attention layer" (Section 3.2) without specifying the number of layers, attention heads, or whether this is applied per-anatomy independently or jointly across anatomies.

4. **Reader study results are not presented in the main text.** The paper states "we conduct a reader study to compare our method with three board-certified radiologists" (line 120) but provides no results, tables, or summary in the accessible main body. A cross-reference to supplementary material does not help the reader evaluate this evidence within the paper.

5. **No ablation of the anatomy grouping granularity.** The 104 TotalSegmentator regions are grouped into 15 categories, justified by a verbal trade-off argument (Section 3.1), but no experiment explores intermediate grouping levels (e.g., 10, 15, 25 categories) to validate the chosen granularity.

6. **Zero-shot prompting strategy is not described.** The paper does not specify how class vectors are constructed for the zero-shot evaluation of any method (CLIP, Merlin, LoVT, MGCA, or fVLM). Differences in prompting strategies could confound the comparisons.

7. **Impression-based normal labeling heuristic is not validated.** The method labels anatomies not mentioned in the impression section as normal (Section 3.3), but the accuracy (false positive/negative rates) of this heuristic is not reported despite its role in correcting contrastive labels.

8. **Per-anatomy or per-disease results not shown.** The 54-disease average AUC masks potential variation—gains could be concentrated in a few anatomies. Reporting per-anatomy breakdowns would strengthen the analysis.

### Trivial
- Line 112: "LOVT" should be "LoVT" (capitalization inconsistency).

## Nice-to-Haves
- The suggestion that the downstream task should be anatomy-level generation rather than whole-report generation goes against the stated scope of the paper. The authors acknowledge this "granularity mismatch" and flag it as future work. This is a natural extension, not a flaw.
- Inter-rater reliability for the expert radiologist annotations on MedVL-CT69K would strengthen dataset documentation but is not essential for evaluating the method.

## Removed Points
- *Criticism about Table 3 not being visible in extracted text*: This is a PDF parsing artifact; the table exists in the original submission. Removed per hard rules about formatting artifacts.
- *Criticism that the "exceedingly intractable" claim for implicit local alignment in CT is "asserted rather than demonstrated"*: The paper provides supporting evidence (LoVT and MGCA perform similarly to CLIP in Table 1) and includes a structural argument in Section 2.2. This is an interpretation difference, not a factual weakness.
- *Criticism about missing confidence intervals being "standard practice" in a way that should trigger major revision*: Acknowledged as missing but demoted from the reviewer's framing because the ablation study and consistent gains across multiple benchmarks mitigate this concern. Kept as a minor weakness instead.
- *Criticism about "unfair comparison with baselines"* in the sense that the reviewer asserted the asymmetry favors baselines: This is already addressed in the retained Major weakness about adaptation procedures, which is the precise form of this concern.
- *Suggestion that data availability of MedVL-CT69K should be clarified*: Privacy constraints are standard for medical data. The paper states the CT-RATE decomposed descriptions will be released. This is not a weakness.

## Novel Insights
None beyond the paper's own contributions. The reviews largely converge on the paper's stated contributions (fine-grained alignment, dual FNR, large dataset) and surface standard concerns about evaluation rigor that do not introduce novel perspectives about the work.

## Suggestions
1. **Specify baseline adaptations clearly.** Provide a brief paragraph for each adapted baseline (LoVT, MGCA, Merlin) describing the adaptation to 3D CT, ideally with the same input format. For Merlin, clarify whether EHR data was used. Even a short supplementary section would substantially raise confidence.
2. **Provide the LLM prompt template and validate decomposition quality.** Release the prompt used with Qwen 2.5 and report precision/recall of anatomy extraction against a manually annotated subset of ~100 reports, including failure examples.
3. **Add per-disease or per-anatomy result breakdowns** for the main zero-shot comparison (Table 1) to show whether gains are uniform or concentrated.
4. **Add confidence intervals or standard deviations** for the 54-disease average AUCs (e.g., via bootstrapping), especially for the main zero-shot results.
5. **Specify alternation frequency and diversity mechanisms** for the co-teaching strategy, and include a brief sensitivity analysis for α.
