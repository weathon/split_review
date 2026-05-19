- Decision: Reject
- Avg Score: 3.25
- Scores: 6, 1, 3, 3
Now I have a thorough understanding of the paper and can verify reviewer claims against the actual text. Let me produce the final consolidated review.

## Summary

This paper proposes LeBD (and a claimed variant CA-LeBD), a run-time backdoor defense for YOLOv5 that uses LayerCAM to locate triggers. The pipeline is: (1) run YOLOv5 on the input, (2) for each detected object, compute a LayerCAM saliency map, (3) occlude the high-attribution region, (4) re-infer and check if the classification changes — if so, a trigger is detected. The main claimed contributions are: diagnosing why YOLOv5's anchor-based design causes deep-layer saliency maps to focus on bounding-box centers, and using LayerCAM in shallower layers to avoid this; a low-overhead real-time defense (LeBD); and a counterfactual-attribution variant (CA-LeBD) said to improve localization.

## Strengths

1. **Insightful analysis of YOLOv5-specific saliency map behavior** (Section 3.2, Figure 2). The paper provides a reasoned explanation for why deep-layer GradCAM/LayerCAM in YOLOv5 consistently highlights bounding-box centers: anchor-based training only computes positive loss for grids near the object center, and NMS retains only the center-grid prediction. The paper further traces the effect of the SPPF module's maximum-pooling layers on expanding the receptive field and causing diffuse hot regions post-SPPF, motivating the choice of shallower (pre-SPPF) layers for LayerCAM. This analysis is concrete and specific to the YOLOv5 architecture.

2. **Lower runtime overhead than the closest comparable baseline (NEO)** (Section 5.4, Table 5). LeBD is reported to incur ~10× the base inference time (~200ms per image) versus NEO's >100× overhead (~2600ms). Given the baseline YOLOv5 runs at ~50 FPS, this is a meaningful improvement in deployability over the only other scanning-based defense considered.

3. **Systematic hyper-parameter exploration** (Sections 5.2–5.3, Tables 2–4). The paper examines the effect of occlusion size constraint, CAM threshold, layer choice, and filtering schemes (mean, median, Gaussian, none). Mean filtering is shown to improve TP rate by >10% in the digital world and >20% in the physical world. This ablation gives useful insight into the method's sensitivity.

## Weaknesses

### Fatal
None.

### Major

1. **CA-LeBD is never defined or explained.** The paper names CA-LeBD in the abstract, contributions list ("We integrate counterfactual attribution into the calculation of saliency maps"), and reports its results in Tables 1–4. However, Section 4 (Method) describes only LeBD in full (Algorithm 1). There is no equation, algorithm, or procedural description of what counterfactual attribution means in this context, how it differs from standard LayerCAM, or how it is computed. The only hint is a remark in Section 5.4 about randomizing "the order of classes to perform CA LayerCAM," which is insufficient. A claimed central contribution — one that the paper asserts yields 5–10%+ improvement — is absent from the method section. This gap prevents evaluation, reproduction, or meaningful comparison of CA-LeBD.

2. **No dataset is named for digital-world experiments.** The paper evaluates on "images in the digital world" but never states which dataset was used (e.g., COCO, VOC, or a custom collection). Without this information, the reader cannot assess the difficulty of the task, the generalizability of the results, or the appropriateness of the attack configuration. This is a fundamental reporting gap for any empirical paper.

3. **Backdoored model's own performance is not reported.** The paper never reports the attack success rate (ASR), benign accuracy, or clean mean average precision (mAP) of the backdoored YOLOv5 model. Without these baselines, the reader has no way to assess whether the attack is actually effective (a weak attack makes any defense look good) or whether the defense degrades performance on benign samples. A defense paper must establish that a meaningful threat exists.

4. **Physical-world evaluation setup is underspecified.** The paper reports results on "video streams in the physical world" with >90% TP rate, but provides no details about: camera model and resolution, lighting conditions, recording distance, trigger material and placement, number of video frames / test samples, or how triggers were rendered in the physical environment. The entire physical-world experiment is a black box, making it impossible to assess, reproduce, or trust the claimed >90% detection rate.

### Minor

5. **NEO adaptation from classification to object detection is not described.** NEO (Udeshi et al., 2022) was designed for image classification. The paper uses it as a baseline for object detection but does not specify how it was adapted (e.g., whether scanning is per-bounding-box or per-image, how the trigger blocker size was chosen). This makes the NEO comparison difficult to interpret.

6. **No explicit "correction" metric.** The paper claims to "correct the misclassification caused by backdoor" (contribution bullet 4 and Section 1), but the reported metrics are detection TP/FP rate and IOU with the trigger. Occluding the trigger and re-inferring naturally yields correction when the classification changes (which is what TP measures), but a direct "correction rate" — what fraction of detected triggers result in correct reclassification to the source class — would strengthen the evidence for the stated claim.

7. **Real-time claim is overstated for the most demanding settings.** LeBD is reported at ~200ms (5 FPS), which the paper calls "completely acceptable in a real-time OD system." For many real-time applications (autonomous driving at highway speeds, fast video surveillance), 5 FPS is below the required threshold. The paper should acknowledge this limitation and discuss the trade-off between detection rate and speed more candidly.

### Trivial

- None beyond the organizational gaps already covered above — the paper is generally well-structured and readable.

## Nice-to-Haves

- **Discussion of adaptive attacks.** An attacker aware of the defense could attempt to distribute trigger features to reduce LayerCAM saliency, or design triggers that are less salient to CAM-based methods. The paper does not discuss this limitation.
- **Comparison with adapted STRIP or Februus for OD.** While these methods have higher overhead, a comparison (even at non-real-time speeds) would provide a ceiling for detection accuracy.
- **Sharpen the "first work" claim.** The paper states "first work on backdoor defense in the physical world" but there are physical-world defenses for other tasks (face recognition, lane detection). Narrowing to "first real-time defense for object detection in the physical world" would be more precise and defensible.

## Removed Points

- **GradCAM baseline is a straw man.** The harsh critic claimed GradCAM should be compared at the same layer as LayerCAM. However, the paper's analysis (Section 3.2) shows GradCAM has inherent problems at ALL layers in YOLOv5 — shallow layers are noisy, deep layers are center-focused due to the anchor-based architecture. This is not a cherry-picked comparison; it is a genuine architectural limitation of GradCAM for this task, which LayerCAM was designed to address. Removed as a misunderstanding of the paper's contribution.

- **Tables are unavailable for review.** The extracted text renders tables as images, which is a PDF-parsing artifact. In the actual submission, the tables are present and readable. Removed per rules.

- **Missing code / reproducibility.** This is a standard limitation for most paper submissions and not a specific flaw of this paper. Removed per rules.

- **Missing related works.** Per instructions, I cannot include this as I lack external sources to verify.

- **Algorithm implementation details missing (connect graph, size constraint).** The paper describes these at a level typical for a conference paper (Algorithm 1, Lines 5–7). While more detail would be helpful, this is not a gap that undermines the contribution.

- **Typos and formatting.** Removed per rules as parser artifacts.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface observations that add significant perspective beyond what the paper provides about its own method and limitations. The harsh critic's diagnosis of the CA-LeBD gap is accurate but follows directly from reading the method section, and the empirical gaps (no dataset name, no ASR, no physical setup) are straightforward observations about missing content.

## Suggestions

1. **Define CA-LeBD.** Provide the counterfactual attribution procedure — a clear equation, algorithm, or at minimum a paragraph explaining how CA LayerCAM differs from standard LayerCAM, why it improves localization, and what the computational cost is. Without this, the paper is missing a claimed contribution.

2. **Name the dataset and describe the experimental setup.** State which dataset was used for digital-world experiments (e.g., a subset of COCO). Describe the physical-world setup: camera, environment, trigger appearance, number of test frames, and how ground truth was established.

3. **Report the backdoored model's ASR and benign mAP.** This is essential context for interpreting any defense result.

4. **Add a correction rate metric.** Report the fraction of detected triggers where the occluded object is correctly reclassified to the source class, not just that the prediction changed.

5. **Add confidence intervals or multiple-run statistics.** The reported improvements of 5–20 percentage points should be accompanied by standard deviations across seeds or data splits.
