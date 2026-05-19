- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 5, 6, 5
Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper proposes a weakly supervised virus capsid detection method that uses only binary image-level labels (virus present/absent) to produce bounding boxes in electron microscopy images. The key innovation is an optimization procedure that starts with a large Gaussian mask covering the full image and progressively shrinks its standard deviation (inspired by score-based generative models), enabling gradient-based refinement of a particle's position directly from a pretrained classifier. A user study quantifies annotation time savings of binary labels (~42% less than bounding boxes), and experiments across five virus types show that a detector trained on the resulting pseudo-labels (Ours(OD)) outperforms fully supervised and other weakly supervised methods under the same annotation time budget.

## Strengths

1. **Gaussian masking with shrinking standard deviation enables direct bounding-box regression from a classifier, removing the need for ROI proposal networks.** Section 3.2 and Figure 2 describe how initializing with large σ and decreasing it during optimization propagates gradients over the full image and converges to precise locations. This is a clean, well-motivated algorithmic contribution that draws a novel connection to score-based generative models.

2. **User study quantitatively validates that image-level labels are faster and less error-prone than point or box annotations.** Section 4.2 reports annotation times and F₁ scores from six experts (Latin square design, counterbalanced). Binary labels require ~11h vs. ~19h for bounding boxes on Herpes and achieve higher inter-annotator agreement. This directly supports the paper's motivation and provides empirical grounding for the equal-time experiments.

3. **Outperforms fully supervised object detection under equal annotation time budget on the Herpes dataset, with consistent trends across four additional viruses.** Figure 5 shows Ours(OD) achieving higher mAP₅₀ than bounding-box-supervised models at every tested budget (5%–100%) on Herpes, with Ours(Opt) surpassing full supervision below 25% time. Table 1 extends this to four other viruses, with Ours(OD) leading in 4/5 cases.

4. **Validated across five virus types spanning different sizes (30nm–165nm) and imaging modalities (room-temperature TEM, negative-stain TEM).** Table 1 reports mAP₅₀ for Herpes, Adeno, Noro, Papilloma, and Rota viruses. The method achieves top performance on all except Adeno, demonstrating meaningful generalization beyond a single organism.

5. **Stable where zero-shot segmentation methods (SAM, CutLER) degrade.** Section 4.4 documents that SAM struggles with small viruses (Noro, Papilloma) and CutLER underperforms on negative-stain TEM, while the proposed approach maintains consistent performance. This demonstrates the value of domain-specific design for low-SNR EM data.

## Weaknesses

### Fatal

None.

### Major

1. **Annotation time ratios measured on a single virus type (Herpes) are applied to all five viruses without justification.** The user study (Section 4.2) measures annotation times only for Herpes. Table 1 uses these Herpes-derived times to compute how many images each supervision type can annotate within a fixed budget for *all* viruses (Adeno, Noro, Papilloma, Rota). Viruses differ substantially in size (30nm–165nm), particle density, and imaging conditions (room-temperature TEM vs. negative-stain TEM). It is plausible that bounding-box annotation for a 30nm Noro particle takes a different amount of time relative to a binary decision than for a 165nm Herpes particle. If the time ratios shift, the budget allocation changes, and the headline comparison in Table 1 rests on uncertain footing. The paper neither acknowledges this limitation nor provides a sensitivity analysis bounding how much the ratios would need to shift to alter the conclusions. The strongest evidence for the equal-time claim remains Figure 5 (Herpes only), which is cleanly supported. This is an **evidential gap** for the cross-virus generalization of the central claim.

### Minor

2. **Stopping criterion threshold is ambiguously specified and could be problematic.** Section 3.4 states: "The value of *t* is chosen based on the smallest threshold used for computing the Mean Average Precision (mAP) metric." The mAP metric (mAP₅₀, as specified in Section 4.3) uses an IoU threshold of 0.5—a geometric overlap criterion, not a classifier confidence threshold. Using an IoU value as a classifier score threshold is conceptually mismatched and the rationale is unclear. If the authors instead meant a confidence-score threshold from the evaluation pipeline, that would be circular. Either way, the description needs clarification and the choice of *t* should be justified from a validation set independent of test-set evaluation.

3. **The paper never reports the binary classification accuracy of the pretrained classifier**, which is the foundation of the entire pipeline (all pseudo-labels derive from it). A simple table showing classification accuracy or AUC per virus would help the reader assess whether the downstream detection failures are due to poor classifier quality or issues in the optimization procedure.

4. **The description of how "the knowledge about the virus size" is incorporated into the baseline methods is vague.** Section 4.3 says "we also include the knowledge about the virus size in the compared approaches" without specifying the mechanism for each baseline (CAM thresholding? size filtering of connected components? NMS box-size constraints?). This makes the baseline setup harder to reproduce.

5. **Computation/running time is not reported.** The paper carefully reports annotation time but ignores the computational cost of the iterative optimization (gradient descent per particle, repeated classifier forward passes). For practical deployment, wall-clock time matters and should be documented.

### Trivial

None.

## Nice-to-Haves

- A sensitivity analysis showing how much the Herpes-derived annotation time ratios would need to change to alter the conclusions of Table 1. This would address the main weakness without requiring additional user studies.
- An ablation study on the σ decay schedule (e.g., linear vs. exponential vs. stepwise) to demonstrate that the proposed schedule is necessary and that results are not highly sensitive to this hyperparameter.
- Failure analysis examples (false positives, missed viruses) to build intuition about the method's limitations at low budgets.
- Statistical significance testing (e.g., paired bootstrap) for the low-budget comparisons in Figure 5, where the gap between Ours(Opt) and other methods is most critical.

## Removed Points

These points were flagged by one or both of the input reviews but are removed per the filtering rules. Treat them with caution—they may be based on reviewer misunderstanding or are not verifiable from the paper.

- **Underspecified hyperparameters (σ_schedule values, learning rate, number of optimization steps).** Per filtering rules, these are standard implementation details that would reside in the appendix (stripped by the parser). The main paper provides the algorithmic structure; numeric values are a reproducibility detail, not a methodological gap.
- **Request for missing related works.** Per filtering rules, the reviewer cannot confirm which works exist; the paper's cited coverage of WSOD and EM-specific detection is thorough.
- **Concern about zero-shot methods not being an equal-time comparison.** The paper presents this as a separate experimental axis (pre-trained models with no annotation), not as an equal-time comparison, so this is an observation, not a flaw.
- **Request for significance tests on all comparisons.** The paper follows standard practice (mean and std over 3 runs). This is a nice-to-have, not a weakness.
- **Formatting/parser-artifact complaints.** All formatting issues in the extracted text are parser artifacts, not author errors.

## Novel Insights

The input reviews surface an interesting tension: the paper's central methodological innovation (shrinking Gaussian mask for direct box regression) is technically sound and novel, but its headline evaluative claim (outperforming fully supervised detection under equal time) depends on an unvalidated assumption about annotation-time ratio portability across virus types. This is a common pattern in annotation-cost-aware papers—the cost model is carefully measured for one domain but assumed constant. The deeper insight is that the *relative* ranking of methods (Ours(OD) > BB > Loc) is likely robust because binary labels are fundamentally cheaper, but the *magnitude* of the advantage is dataset-dependent and should be reported with confidence intervals that reflect uncertainty in the cost model, not just the detection model. The reviews also converge on the point that the stopping criterion's reference to mAP thresholds needs clarification—this is a specific, fixable issue that could affect reproducibility.

## Suggestions

1. **Address the annotation-time generalization concern.** The cleanest fix is to acknowledge it explicitly as a limitation and provide a sensitivity analysis: e.g., "binary labels would need to be X% slower relative to bounding boxes to change the ranking in Table 1." Even a brief bounding calculation would significantly strengthen the paper's credibility.
2. **Clarify the stopping criterion threshold (Section 3.4).** Explain what "the smallest threshold used for computing the mAP metric" means. If it refers to the IoU=0.5 threshold used in mAP₅₀, state that explicitly and justify why this value is appropriate as a classifier confidence threshold. If it refers to something else, provide the correct definition and a validation-based justification.
3. **Report classifier accuracy/AUC per virus** in a supplementary table. This is a simple addition that would let readers assess the quality of the foundation the method builds on.
4. **Specify how virus size information is used in each baseline.** A brief sentence per baseline (e.g., "For CAM-based methods, we filter detected connected components to keep only those with bounding box dimensions within ±20% of the known virus radius") would improve reproducibility.
