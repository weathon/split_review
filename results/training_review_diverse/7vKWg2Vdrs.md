Now I have a thorough understanding of the paper. Let me synthesize the consolidated review.

---

## Summary

This paper proposes LeBD and CA-LeBD, runtime defenses against backdoor attacks in YOLOv5 object detection. The core idea is to use LayerCAM to locate suspicious regions in detected objects, occlude them, and compare predictions before/after occlusion to identify triggers. The method is evaluated on digital images and physical-world video streams. A key contribution is the analysis of CAM behavior across YOLOv5 layers, identifying that deep-layer saliency maps concentrate on bounding-box centers due to YOLO's anchor-based training, motivating the use of shallower layers for trigger localization.

## Strengths

- **Novel application of LayerCAM to runtime backdoor defense for object detection in the physical world.** The paper tackles an underexplored and practically important setting. It evaluates on physical-world video streams and reports >90% true-positive detection rates (Table 1), which is a meaningful advance over prior defenses that either focus on image classification or digital-only scenarios.

- **In-depth analysis of CAM behavior in YOLOv5 layers (Section 3.2).** The paper identifies that high-layer GradCAM/LayerCAM saliency maps concentrate on bounding-box centers due to YOLOv5's anchor-based training and NMS, and explains why the SPPF module causes hot-region expansion. This diagnosis is non-trivial, provides a principled justification for choosing shallower layers, and is a generally useful finding beyond this paper.

- **Well-motivated threat model and practical assumptions.** The defender does not modify the model, has no access to poisoned training data, and has no prior knowledge of the trigger. This matches real-world deployment constraints.

- **Ablation study on mean filtering (Table 4) demonstrates a simple and effective post-occlusion enhancement.** The paper compares mean, median, Gaussian, and no filtering, showing mean filtering boosts TP by 10–20%. The explanation (mean filtering aggressively disrupts residual trigger signal at occlusion boundaries) is plausible and grounded.

## Weaknesses

### Major

- **CA-LeBD is not described.** The paper lists CA-LeBD as a core contribution ("We integrate counterfactual attribution into the calculation of saliency maps") and reports its results in all tables, but never explains what counterfactual attribution means computationally. How does CA-LeBD differ from LeBD? What does "CA LayerCAM" compute differently? The only clue is in the runtime analysis (Section 5.4), which contrasts "CA LayerCAM on all 80 classes" versus "only one class," suggesting it involves computing CAM for multiple classes — but this is never stated, let alone formalized. A reader cannot understand what was actually implemented or evaluate whether the claimed improvements are methodologically sound.

- **Experimental setup is critically underspecified.** The paper reports detection rates, false positive rates, and IOUs in multiple tables, but omits essential details: (a) what dataset(s) are used for digital-world experiments? (b) what exact triggers (size, pattern, placement strategy), poisoning fraction, and training recipe are used for the backdoored YOLOv5 model? (c) what are the physical-world capture conditions (camera, resolution, lighting, number of frames, trigger objects)? (d) how many total poisoned and benign samples are tested? (e) are results averaged over multiple runs with standard deviations? Without these, the numerical results in Tables 1–4 are ungrounded and non-reproducible.

- **No evaluation on clean (non-backdoored) models.** The reported FP rate (~8%) for LeBD is presumably measured on poisoned images where the model is backdoored. It is unclear what happens when LeBD is applied to benign objects in a clean deployment scenario (no backdoor at all). Would the method produce false alarms on benign objects whose salient features happen to change classification when occluded? This is a critical missing baseline for a defense that must not degrade normal operation.

### Minor

- **The "real-time" claim is overstated.** LeBD adds ~200 ms overhead (Table 5), yielding ~4.5 FPS total. The paper calls this "completely acceptable in a real-time OD system," but typical real-time object detection applications (autonomous driving, surveillance) require 30 FPS. The paper does not specify what real-time threshold it is targeting, and the comparison to NEO (which is much slower) does not make 5 FPS real-time. The mention of parallel analysis of multiple objects is not backed by experimental results.

- **"Connect graph" is never defined.** Line 5 of the algorithm description refers to calculating the "connect graph" to determine the crucial region from the saliency map. This operation is central to the pipeline but is never explained. A reader cannot know what this step does (connected components? a graph over high-activation pixels?).

- **"First work on backdoor defense in the physical world" is overclaimed without rigorous justification.** The paper itself cites STRIP, NEO, and Februus as defenses that could theoretically be applied to physical-world images. While these methods may not be optimized for real-time object detection, the claim of "first" requires a more precise delimitation (e.g., "first run-time defense for YOLO with physical-world video evaluation") rather than a blanket assertion. The paper acknowledges that prior defenses "can theoretically be adopted in the physical world" but "can hardly meet the real-time requirements," which partially addresses this — however, the phrasing in the contributions section ("first work on backdoor defense in the physical world") is still too broad.

- **Missing comparison with Februus.** Februrus (Doan et al., 2020) also uses GradCAM for trigger localization and reconstruction. It is cited in related work but not compared against experimentally. While Februrus targets classification, adapting a reasonable version to YOLO would strengthen the evaluation and clarify what LeBD adds beyond prior CAM-based defenses.

### Trivial

- The paper defers key implementation details to Algorithm 1 and figures that are not fully readable in the parsed text. The algorithm reference (Line 1, Line 4, etc.) in the prose is helpful, but the pseudocode itself would aid clarity.

## Nice-to-Haves

- A sensitivity analysis or principled guidance for setting hyperparameters (occluded region size constraint, CAM threshold) beyond observed trends.
- Evaluation on non-anchor-based detectors (e.g., FCOS, DETR) to validate the explanation that the center-bias is caused by anchor-based training.
- Discussion of adaptive attacks: an adversary aware of the defense could craft triggers that produce diffuse CAM responses or exploit the occlusion/mean-filtering threshold.

## Removed Points

- *"The algorithm text is not included in the main body"* — The paper provides a detailed prose description of LeBD with line references to Algorithm 1. The algorithm pseudocode likely exists in a format stripped by the parser. However, the core issue (CA-LeBD being undescribed) is retained in Major above.
- *"The paper does not explain why mean filtering works better than median/Gaussian"* — The paper does provide this: Table 4 compares all three, and Section 5.3 explains that mean filtering has "the most pronounced impact on pixel values, especially at the edge of the occluded region... The destruction of the pixel value inhibits the attack ability of the residual trigger." This is a sufficient explanation for an empirical observation.
- *"The center-bias validation requires experiments on non-anchor-based detectors"* — The paper's explanation in Section 3.2 is well-reasoned and grounded in YOLOv5's training objective (only grids closest to object center compute positive-sample loss) and NMS behavior. While extra validation would strengthen the paper, this is an analysis/diagnosis, not an unsubstantiated claim. Moved to Nice-to-Haves.
- *"GradCAM and NEO results are uninterpretable without knowing runtime specifics"* — The runtime analysis (Table 5) clearly reports time per image. While the paper does not achieve conventional 30 FPS real-time, the measurement itself is clear. The real-time claim is addressed in Minor above.

## Novel Insights

The most striking observation from the reviews is that the paper's strongest contribution may not be LeBD/CA-LeBD itself but rather the systematic analysis of LayerCAM behavior across YOLOv5 layers (Section 3.2). The finding that deep-layer saliency maps consistently focus on bounding-box centers due to YOLO's anchor-based training — and that this can be traced to the positive-sample assignment rule — is a genuinely useful diagnostic that extends beyond the backdoor defense context. This analysis could inform any downstream task using CAM-based interpretability on one-stage detectors. The paper would benefit from framing this as a standalone finding rather than burying it in Preliminaries.

## Suggestions

1. **Provide a complete, self-contained description of CA-LeBD in the main text.** What is the counterfactual attribution objective? How does it modify the LayerCAM computation? Which classes are compared, and how does this help localize triggers?

2. **Add a table summarizing experimental conditions:** dataset, trigger specifications, poisoning rate, physical-world capture setup (camera, environment, number of frames/samples), and sample counts for all experiments.

3. **Report means and variances across multiple runs or seeds** to establish reliability of the reported numbers.

4. **Evaluate LeBD on a clean (non-backdoored) model** to measure false positive rates in benign conditions.

5. **Replace the "first work on backdoor defense in the physical world" claim** with a precise statement such as "first runtime defense for object detection evaluated on physical-world video streams at <measured FPS>."

6. **Define "connect graph"** — is this a connected-components algorithm on the thresholded saliency map? A graph cut? Clarify the operation.

7. **Discuss real-time feasibility honestly.** State the measured FPS, specify the target application's FPS requirement, and suggest optimizations (e.g., running CAM every N frames, on suspicious objects only, or using hardware acceleration).

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>