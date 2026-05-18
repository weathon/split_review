Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes a weakly supervised object detection method for virus capsids in electron microscopy (EM) images. The key idea is to take a classifier trained on binary (present/absent) image-level labels and distill it into a detector via iterative gradient-based optimization with a shrinking Gaussian mask. The mask starts with a large standard deviation (covering the whole image) and decays exponentially, allowing gradients to pull the initial position toward a virus from far away and then refine it locally. After each detection, the found particle is masked out; the process repeats until a stopping criterion triggers. The method is evaluated on five virus types and compared against WSOL baselines (GradCAM, LayerCAM, TS-CAM, Reattention), zero-shot models (SAM, CutLER), location labels, and full bounding-box supervision. A user study with six experts confirms that binary labels are faster and less error-prone than location or bounding-box annotations.

## Strengths

- **Novel shrinking-Gaussian optimization that directly regresses bounding boxes from a classifier without ROI proposals or specialized architectures.** The method uses a Gaussian mask whose standard deviation decreases during optimization (Section 3.2), enabling gradient propagation from distant positions early and fine localization later. This is a clean, principled advance over prior WSOD approaches that rely on selective search or MIL.
- **Consistent outperformance of both weakly and fully supervised methods under equal annotation time across five virus types.** Table 1 shows that Ours(OD) (a Faster-RCNN trained on pseudo-labels from the optimization) achieves higher mAP₅₀ than location labels, bounding-box labels, and all WSOL baselines when annotation time is fixed. On the Herpes dataset with limited budgets (5%–100%), Ours(Opt) even exceeds fully supervised detectors (Figure 5), directly supporting the paper's main claim.
- **User study provides concrete empirical justification for the weak-supervision setup.** A six-expert study (Section 4.2) measures annotation time and F₁ error rates for binary, location, and bounding-box labels. It shows binary labels are significantly faster (11 h vs. 17–19 h for Herpes) and less error-prone (F₁ ≈ 0.98 vs. ≈ 0.95 for location and ≈ 0.90 for bounding boxes), grounding the time-budget comparisons in real annotation cost.
- **Systematic comparison with zero-shot models (SAM, CutLER) highlights domain-specific advantages.** Section 4.4 shows that SAM and CutLER perform well on stainTEM but struggle with small viruses and are sensitive to noise levels and preparation methods, whereas the proposed method gives stable results across all datasets — demonstrating the value of incorporating domain knowledge.

## Weaknesses

### Fatal
None.

### Major

- **No sensitivity analysis for the assumed virus radius — the method's key domain-specific parameter.** The method takes the virus radius *r* as input and uses it in three places: the magnification-dependent σ schedule for the Gaussian mask, the circular mask for removing detected particles, and the final bounding box construction. The paper uses literature values for each virus (Section 4.1) but never studies how results degrade when *r* is off by 10–20 %. EM preparation variability means actual sizes can differ from literature averages. Without this analysis, the method's robustness in practical deployment is unknown, and the paper's claim of exploiting "known virus size" is incompletely validated. The conclusion even acknowledges this as future work ("analyze the applicability of our method to the localization of objects that vary in size"), confirming the gap.

### Minor

- **No runtime characterization of the detection pipeline.** The paper acknowledges "computational overhead" and introduces GradCAM initialization to reduce it (Section 3.1, contribution list), but never reports wall-clock time per image or per particle. Comparisons against other methods (GradCAM, LayerCAM, TS-CAM, SAM, CutLER) are reported only on mAP₅₀, so the practical trade-off between detection accuracy and compute cost remains unclear. This is not fatal — the paper's core claim is about annotation-time efficiency, not inference speed — but it would strengthen the practical case.
- **Stopping criterion threshold *t* is under-specified.** Section 3.4 states: "The value of *t* is chosen based on the smallest threshold used for computing the Mean Average Precision (mAP) metric." This is ambiguous — mAP is a summary metric computed over a range of thresholds, not a single threshold. It is unclear whether *t* is fixed across datasets, tuned per dataset, or how sensitive the number of detections is to its choice. This hurts reproducibility.
- **Only mAP₅₀ is reported.** While this is standard in detection, the method produces fixed-size bounding boxes (matching the known virus size) by construction, which could give it an advantage at IoU=0.5 over methods predicting variable-size boxes. Reporting additional IoU thresholds (e.g., 0.3, 0.75) or mAP₅₀:₉₅ would provide a more complete picture of localization quality.
- **The non-overlap assumption (used to justify NMS) is stated but not verified on the datasets.** Section 3.5 says the method can "exploit the fact that virus particles do not overlap in the image plane" to justify NMS, but no evidence or quantification is provided. If particles can be closer than the virus radius, the virus-removal mask may partially or fully remove an undetected particle before it is found, causing missed detections. A discussion of this failure mode is absent.
- **The paper does not specify whether the WSOL baselines (GradCAM, LayerCAM, etc.) used the same trained classifier as the proposed method.** Section 4.3 describes that the proposed method uses a ResNet-101 binary classifier, and that GradCAM/LayerCAM are compared with ResNet-101 and ViT-B/16 backbones, but it does not explicitly state whether the baselines' saliency maps were computed from the *same* binary classifier or from separately trained ones. Since the proposed optimization directly consumes the same classifier it uses for detection, this matters for fairness.

### Trivial
None.

## Nice-to-Haves

- An analysis of how the method behaves on images that contain no viruses (e.g., how the stopping criteria handle classifier false positives on empty patches), though this is partially covered by the stopping criteria.
- Convergence statistics: average number of optimization steps per particle, and how GradCAM initialization reduces steps compared to a random baseline.

## Removed Points

The following points from the reviewer inputs were removed or downgraded because they were speculative, reflected reviewer preferences rather than paper flaws, or were not supported by the paper text:

- **"Criterion 1 (CAM min = max) seems brittle — CAM maps in negative-stain TEM can be nearly uniform even when viruses remain."** — Speculative. The paper's check (min = max) is a reasonable test for a degenerate CAM with no spatial information. No evidence is provided that this scenario occurs in the datasets.
- **"Criterion 3 could easily trigger false-positive acceptances."** — Also speculative; no evidence or analysis is provided to support this claim.
- **"User study F₁ differences are relatively small / modest effect size."** — Subjective judgment. The paper reports statistically significant differences, and the effect sizes (≈0.98 vs. ≈0.95 vs. ≈0.90) are meaningful in an annotation-quality context.
- **"The paper's method may be computationally expensive / orders of magnitude slower."** — The actual runtime is unreported (which is a valid weakness), but the reviewer's speculation about *orders of magnitude* is not grounded in any data. The weakness is about missing runtime numbers, not about the method being presumptively slow.

## Novel Insights

The iterative shrinking-Gaussian optimization described in this paper is effectively a coarse-to-fine gradient-based search that bears a striking structural similarity to score-based generative model sampling — an intellectual bridge that the authors explicitly acknowledge. One subtle but important observation is that the method's reliance on a fixed virus size is simultaneously its greatest strength and its most brittle assumption: it regularizes the detection to produce physically plausible bounding boxes (which helps on low-SNR EM data where standard WSOL methods fail), but it also means the method cannot handle size-variant objects or polydisperse particle mixtures without modification. The consistent outperformance over location labels (which are more expensive to collect) is also noteworthy — it suggests that for roughly circular objects of known size, image-level supervision plus geometric priors can be more annotation-efficient than point annotations, which is not an obvious outcome.

## Suggestions

1. **Add a sensitivity analysis for the virus radius *r*.** Vary *r* by ±10–20 % for at least one dataset (e.g., Herpes or Adeno) and report mAP₅₀ and the number of detections. This directly addresses the paper's central design assumption and is orthogonal to adding more datasets or baselines.
2. **Report per-image or per-dataset wall-clock runtime** (single-threaded, on a standard GPU) for the proposed pipeline and at least one baseline (e.g., GradCAM). Even a single table row would resolve the current opacity about computational cost.
3. **Clarify the stopping criterion threshold *t*.** Specify whether *t* is a classification-score threshold, how it is derived from mAP thresholds, and whether it is tuned per dataset or fixed. A precision/recall analysis of the stopping decision would further strengthen this.
4. **Consider reporting mAP at a second IoU threshold** (e.g., 0.3 or 0.75) to characterize localization quality beyond the size-aligned IoU=0.5.
5. **Explicitly state whether the WSOL baselines used the same trained classifier** as the proposed method, or whether separate classifiers were trained per method.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>