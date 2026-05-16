Now I have all the information needed. Let me construct the final consolidated review, carefully cross-checking each claim.

## Summary

This paper proposes a weakly supervised object detection method for virus capsids in electron microscopy (EM) images, using only image-level binary labels (virus present/absent). The method trains a binary classifier, then uses a gradient-based optimization with a shrinking Gaussian mask (inspired by score-based generative models) to localize particles from the classifier, producing pseudo-labels to train a Faster-RCNN. Evaluated on five virus types (Herpes, Adeno, Noro, Papilloma, Rota) spanning different sizes and imaging modalities, the method outperforms other weakly supervised approaches and, under equal annotation time budgets, can exceed fully supervised methods. A user study with six experts confirms that binary labels are faster and less error-prone than center-point or bounding-box annotations.

## Strengths

- **Novel optimization-based localization with shrinking Gaussian mask**: The gradient-based localization (Section 3.2) uses a Gaussian mask whose standard deviation decays exponentially during optimization. This design allows gradients to propagate over the full image initially and then focus on fine details, enabling direct bounding-box regression from an image-level classifier without region proposals or specialized architectures. Figure 2 visualizes how this scheme pulls distant positions toward virus particles and refines nearby ones.

- **User study validates the annotation-time motivation**: The study (Section 4.2) measures annotation time and accuracy for six experts on three label types (binary, center location, bounding box) across 85 patches of Herpes TEM images. Binary annotations take less time per patch, are less sensitive to particle count (Figure 3), and achieve higher F₁ scores (Figure 4). This directly supports the paper's practical motivation that binary labels reduce annotation cost and human error.

- **Outperforms alternatives under equal annotation time budgets**: When total annotation time is equated to the time needed for binary labels (Table 1, Figures 5–6), the proposed method achieves higher mAP₅₀ than location labels, bounding-box labels, and several weakly-supervised baselines (GradCAM, LayerCAM, TS-CAM, Reattention) across all five viruses. On Herpes, Ours(Opt) also outperforms all other methods when the annotation time budget is below 25% (Figure 5), showing a clear advantage when expert time is limited.

- **Generalization across diverse virus types and imaging conditions**: The method is evaluated on five viruses ranging from Noro (30 nm) to Herpes (165 nm), including both cryo-EM and negative-stain TEM images (Table 1). It obtains competitive or superior results consistently, indicating robustness to different particle sizes, contrast levels, and preparation methods.

- **Comparison against modern zero-shot models (SAM, CutLER)** provides useful context: these methods perform well on some viruses (e.g., Adeno) but are less stable, especially for small viruses like Noro, whereas the proposed method is more reliable across all datasets.

- **Ablation-style experiments on annotation time and dataset size** (Figures 5–6) add practical nuance: Ours(Opt) outperforms Ours(OD) when data are scarce (< 25% annotation time), and Ours(OD) matches/exceeds supervised methods with abundant data.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Missing classifier training details hinder full reproducibility.** The paper states that a ResNet-101 is used for the classifier (§4.3) and that it is pre-trained on image-level labels, but provides no details on optimizer, learning rate schedule, number of epochs, data augmentation, or whether it is fine-tuned from ImageNet pretraining. Since the downstream localization (§3.2) depends on the classifier's gradient behavior and the quality of pseudo-labels determines detector performance, these omissions make it harder for others to reproduce or adapt the method. This is a common gap in many papers but should be rectified (a brief paragraph in §4.3 or the appendix would suffice).

- **No statistical significance assessment for the main comparisons.** Table 1 reports mean and standard deviation over three runs, which is good practice, but the key claim that Ours(OD) significantly outperforms the best alternative is not backed by confidence intervals, effect sizes, or any significance test. Given only three runs and potentially overlapping standard deviations, the reader cannot judge the reliability of the reported ordering. The authors should either add basic statistical measures or explicitly acknowledge this limitation.

- **User study is limited to one virus type and six experts.** The study (Section 4.2) is well-designed (balanced Latin square, randomization) but involves only six experts annotating 85 patches from a single virus (Herpes). While this is sufficient to motivate the use of binary labels in the paper's domain, the results should not be overgeneralized. The paper largely avoids overclaiming here, but the scope limitation should be stated explicitly.

- **Stopping criteria threshold is underspecified.** The stopping criterion in §3.4 uses a threshold *t* chosen "based on the smallest threshold used for computing the Mean Average Precision (mAP) metric." This is unclear—mAP thresholds are IoU thresholds (e.g., 0.5 for mAP₅₀), while the classifier outputs a score/probability. How the IoU threshold translates to a classifier score threshold is not explained, and it is unclear whether this choice is circular (using evaluation metric thresholds to set detection hyperparameters). The authors should clarify the mapping or specify how *t* is selected on a validation set.

- **Terminology: "infinite annotation time" (Section 4.4) is confusing.** It means "all available labels," not literally infinite time. This phrasing could mislead readers.

### Trivial

- None beyond the minor points above; the paper is generally well-written with no significant presentation flaws.

## Nice-to-Haves

- **Ablation of the optimization components** — removing GradCAM initialization, fixing σ to a constant, or replacing exponential σ decay with linear decay would strengthen the claim that the shrinking Gaussian mask is driving localization improvement.

- **Sensitivity analysis for the assumed virus radius** — reporting how performance changes when the radius is off by 10–20% would be practically valuable.

- **Failure case analysis**, especially for the Adeno virus where the method underperforms, would help users understand when the method might struggle.

- **Computational cost reporting** — number of gradient steps per particle and total runtime versus training Faster-RCNN from scratch would help practitioners assess practicality.

## Removed Points

These points were identified by the reviewers but are removed or downgraded per the consolidation guidelines. Treat them with caution.

1. **Central claim framing (Critic Issue 1):** The critic argued the abstract could be misread as "weak labels are better than strong labels regardless of data quantity." However, the abstract already qualifies the claim: "in cases where the time to obtain the annotation is limited." The qualifier is present and sufficient. This is not a weakness.

2. **Connection to score-based generative models not developed:** The critic noted the inspiration from Song & Ermon (2019) is "not developed beyond a similarity in scheduling." The paper uses this as a design inspiration, which is appropriate. No further development is needed.

3. **SAM/CutLER description too brief:** The critic said it is "unclear whether these zero-shot models are used off-the-shelf or fine-tuned." The paper explicitly states "forward these through the pre-trained models," clearly indicating off-the-shelf use. The description is adequate for a comparison baseline.

4. **Qualitative results request:** The critic suggested showing example detections. The paper already includes figures (Figure 2 visualizes gradients; Figure 9 is referenced as showing classifier bias). This is a wishlist item, not a weakness.

5. **Dedicated limitations section:** The critic requested this, but the paper discusses limitations in Section 4.4 and mentions future work on varying object sizes in the conclusion. The existing discussion is adequate for a conference paper.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a paragraph in §4.3 (or an appendix) specifying the classifier training details: optimizer, learning rate, epochs, data augmentation, and whether ImageNet pretraining is used.
2. Clarify the stopping criterion threshold *t*: explain how the mAP IoU threshold maps to a classifier score threshold, or state that *t* is selected on the validation set.
3. Add a brief note acknowledging that statistical comparisons are based on three runs without formal significance testing.
4. Replace "infinite annotation time" with a clearer phrase such as "full dataset annotation."

## Score and Decision

The paper makes a genuine contribution: a novel, domain-appropriate method for weakly supervised virus detection in EM, with thorough evaluation across five viruses, a user study supporting its motivation, and practical results showing advantages under realistic annotation budgets. The weaknesses are all minor and addressable — none threaten the core claims. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>