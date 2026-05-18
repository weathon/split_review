Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

## Summary

This paper proposes a weakly supervised object detection method for virus capsids in electron microscopy (EM) images that requires only image-level binary labels (virus present/absent). The core technical innovation is a gradient-based optimization with a progressively shrinking Gaussian mask that directly regresses bounding box positions from a pre-trained classifier. The method is evaluated on five virus types, with a user study confirming that binary labels are faster and less error-prone than location or bounding box annotations.

## Strengths

- **Novel optimization with shrinking Gaussian receptive field enables direct bounding box regression from image-level labels.** The method starts with a large Gaussian mask standard deviation covering the full image and progressively reduces it, allowing gradients to guide the position from far away to precise convergence (Section 3.2, Figure 2). This is a clean, well-motivated technical innovation that distinguishes the method from prior CAM-based or selective-search approaches and directly enables the reported detection results across five virus types (Table 1).

- **User study with domain experts provides empirical evidence that binary labels are faster and more robust.** The controlled experiment with six experts annotating 85 patches under three conditions (binary, location, bounding box) uses a balanced Latin square design and measures both annotation time and F1 score (Figures 3, 4). Results show binary annotations are significantly faster (e.g., 11 hours vs. 19 hours for bounding boxes on the Herpes dataset) and less error-prone, directly supporting the core motivation.

- **Competitive results across multiple virus types under limited annotation budgets.** The detector trained on pseudo-labels (Ours(OD)) consistently performs well across Herpes, Adeno, Noro, Papilloma, and Rota viruses (Table 1). On the Herpes dataset, the method shows particular strength when annotation time is constrained (Figure 5), demonstrating practical utility in realistic scenarios.

- **Domain-aware design choices address specific EM challenges.** The GradCAM-based initialization (Section 3.1) reduces computational overhead, iterative virus removal with known radius (Section 3.3) handles multiple instances per image, and incorporating the known virus size mitigates the low signal-to-noise ratio problem inherent in EM images.

## Weaknesses

### Fatal
None.

### Major

- **The annotation-time comparisons in Table 1 generalize from a single-virus user study to all five virus types without validation.** The user study (Section 4.2) measures annotation times only on Herpes virus images (165 nm particles). These time estimates are then used (Section 4.4) to set time budgets for *all* viruses in Table 1, including Norovirus (30 nm). The relative cost of binary vs. bounding box annotations could differ substantially for smaller, harder-to-see particles — if binary labels are relatively more expensive for small viruses, the claimed advantage would be overstated. The Reduced Annotation Time experiment (Figure 5) is only run on Herpes, leaving the cross-virus generalization of time budgets unvalidated. This directly affects the central claim that the method "outperforms fully supervised methods given the same annotation time."

### Minor

- **No sensitivity analysis for the assumed virus radius.** The method requires the virus radius *r* as input and uses it throughout: mask design, virus removal, and final bounding box creation (Sections 3.2, 3.3, 3.5). While the literature-reported values are reasonable, no experiment tests how performance degrades when the true virus size deviates from the given value. For Herpes the paper validates that the literature value matches the dataset average, but for other viruses this is only assumed. A robustness analysis (e.g., ±20 % radius variation) would clarify the method's practical brittleness.

- **Limited statistical rigor in comparisons.** All results report means and standard deviations over only three runs (Section 4.3), with no statistical significance tests. Several comparisons in Table 1 show overlapping error bars (e.g., Ours(OD) vs. BB for Adeno), and the paper itself acknowledges that Adeno is an exception where the method does not achieve the best results (Section 4.4). With only three runs, it is difficult for readers to assess which reported advantages are reliable.

- **No comparison against MIL-based WSOD methods.** The paper compares against WSOL methods (GradCAM, LayerCAM, TS-CAM, Reattention) adapted to detection but omits MIL-based weakly supervised object detection methods (e.g., Bilen & Vedaldi 2016; Zeng et al. 2019) because they rely on selective search, argued to be ill-suited for EM. While this choice is understandable, a limited experiment on a dataset where selective search could plausibly work (e.g., Herpes with large particles) would strengthen the claim that the proposed method outperforms "other weakly supervised methods."

- **Key optimization hyperparameters are not reported.** The optimization procedure (Section 3.2) describes the shrinking-σ strategy qualitatively but omits specific values for learning rate, number of optimization steps per particle, σ_min, σ_max, and the exponential decay schedule. This harms reproducibility.

### Trivial
- **The stopping threshold *t* description is unclear.** Section 3.4 states the threshold is "chosen based on the smallest threshold used for computing the Mean Average Precision (mAP) metric." This mixes classifier-score thresholds (for stopping) with IoU thresholds (for evaluation). While likely not circular in practice, the wording is confusing and should be clarified.

## Nice-to-Haves
- A component ablation study (e.g., replacing GradCAM init with random positioning, or fixing σ to σ_max or σ_min) would clarify which parts of the pipeline are essential.
- Per-virus annotation time estimates from a small sample of a second virus type (e.g., Noro) would strengthen the cross-virus time-budget experiments.
- Reporting recall and precision of the pseudo-labels (Ours(Opt) boxes) before training the Faster-RCNN would make the pipeline's bottleneck explicit.
- A brief discussion of overlapping/clustered particles as a known limitation would be helpful (the paper currently assumes non-overlapping particles via NMS).

## Removed Points
- The critic's claim that the stopping threshold *t* creates a "circular dependency" that "inflates mAP" is inaccurate — the stopping threshold is on the classifier output score, while mAP uses IoU thresholds. These are different quantities, so no circularity exists. The presentation is unclear but the technical concern is not valid.
- The critic's observation about zero-shot baselines (SAM, CutLER) "adding little information" is noted but the comparison provides useful context for the reader and is not a weakness.
- The critic's suggestion about Figure 2 showing "actual optimization trajectories on real EM images" is a wishlist item, not a weakness.

## Novel Insights
The reviewer cross-examination reveals that the paper's most original contribution is not simply another weakly supervised detector, but a fundamentally different paradigm for converting a weak binary classifier into a spatial detector: using a parametrized mask with controlled annealing of its spatial extent to guide gradient-based optimization toward convergence. This is distinct from both CAM-thresholding and MIL-based WSOD, and especially well-suited to EM where objects have known sizes and roughly circular shapes. The key insight is that mask annealing mimics coarse-to-fine search in a differentiable way. However, the evaluation over-relies on a single time-estimate calibration (Herpes) while treating virus size as a known parameter rather than testing sensitivity to it — both gaps that undercut the generalizability claims.

## Suggestions
1. **Validate or qualify the cross-virus time-budget comparisons.** Either (a) collect small-sample annotation time estimates for at least one other virus type to confirm the time ratios hold, or (b) explicitly discuss this as a limitation and characterize how much the time ratios would need to shift to change the conclusions (sensitivity analysis on the time ratios themselves).
2. **Add a sensitivity analysis for the virus radius parameter** on at least one dataset, testing performance at ±10 % and ±20 % of the reported radius.
3. **Report optimization hyperparameters** (learning rate, number of steps, σ_min, σ_max, decay schedule) to improve reproducibility.
4. **Clarify the stopping threshold selection** in Section 3.4 — explain how *t* is chosen in practice (e.g., fixed at 0.5, or calibrated on a validation set) without reference to mAP thresholds.
5. **Qualify statistical claims** — acknowledge where comparisons have overlapping error bars and note the limited number of runs.

## Score and Decision

This paper presents a genuinely novel and well-motivated method for weakly supervised virus detection in EM. The core technical idea (shrinking Gaussian mask optimization) is clean and domain-appropriate. The user study is a valuable contribution in itself. However, the strongest claims about outperforming fully supervised methods under equal annotation time rest on time estimates derived from a single virus type and extrapolated across all five viruses without validation — a gap that meaningfully weakens the evidence for those claims. The remaining weaknesses (no size-sensitivity analysis, limited statistical rigor, incomplete hyperparameter reporting) are addressable but non-trivial. The paper has real value but requires substantial strengthening of the evaluation.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>