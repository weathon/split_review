Now I have a thorough understanding of the paper and all review claims. Let me write the consolidated review.

## Summary

This paper proposes a weakly supervised method for virus capsid detection in electron microscopy images using only image-level (binary presence/absence) labels. The core technical contribution is a gradient-based optimization with a shrinking Gaussian mask that enables direct bounding-box regression from a pre-trained classifier, without requiring region proposals or architecture modifications. The method iteratively detects multiple virus particles, and the resulting pseudo-labels are used to train a standard object detector (Faster-RCNN). Experiments across five virus types compare against fully supervised, location-supervised, and zero-shot baselines under both equal-annotation-time and equal-data conditions.

## Strengths

- **Novel shrinking-Gaussian optimization for direct bounding-box regression.** The idea of progressively reducing the Gaussian mask's standard deviation (inspired by score-based generative models) to enable gradient-based localization from a classifier is genuinely creative and well-motivated. It avoids the need for selective search or ROI proposal networks, which is a meaningful advance for the EM domain (Section 3.2, Figure 2).

- **User study provides quantitative evidence that binary labels are faster and more robust.** Six experts annotated 85 Herpes patches with three label types. Binary annotations had the highest F₁ (fewest errors) and the lowest average time per image (~1–2 seconds vs. 10+ seconds for bounding boxes). This directly supports the practical motivation for the approach (Section 4.2, Figures 3–4).

- **Comprehensive evaluation across diverse virus types.** Experiments span five viruses (Herpes, Adeno, Noro, Papilloma, Rota) with different sizes (30–165 nm), dataset sizes (31–359 images), and EM modalities, demonstrating the method's applicability beyond a single setting (Table 1, Section 4.4).

- **Iterative detection with multiple stopping criteria handles multi-instance images.** The method detects several particles per image (up to 8) via iterative initialization, optimization, and virus removal — a practical improvement over the single-object limitation of the most closely related work (Lu et al. 2020) (Sections 3.3–3.4).

## Weaknesses

### Fatal
None.

### Major

- **The annotation-time comparison conflates data quantity with label quality, overstating the method's inherent advantage.** The main experimental design (Table 1) fixes the annotation budget to the time needed for binary labels, which naturally gives the weak supervision pipeline more training images than the fully supervised baseline (which spends time annotating each bounding box). The paper's framing — "outperforms fully supervised methods" — is technically correct under this budget-constrained protocol, but the confound means the comparison does not isolate the method's ability to extract more information per label. The paper partially addresses this with the "Infinite Annotation Time" experiment (Figure 6), which controls for number of images and shows that supervised methods match or outperform the weak method when data is abundant and annotation budget is not a constraint. However, the main results table is presented without this caveat, and the abstract's claim ("even ground truth labels") inflates what is demonstrated. The central practical claim — that cheaper labels enable better detectors under a fixed budget — is valid, but the paper should more carefully distinguish this from a claim about the optimization method itself being superior to supervised learning.

- **The method requires domain knowledge of virus radius and assumes fixed-size particles, with no sensitivity analysis.** The expected virus radius \( r \) is a critical hyperparameter that must be known in advance from the literature. The paper does not analyze how performance degrades when the assumed radius is off by 20% or 50%. Since EM virus size varies within and across strains, and the paper's future work acknowledges variable-size particles as a limitation, an empirical sensitivity study is needed to establish the method's practical robustness (Section 3, Section 5).

### Minor

- **The patch labeling protocol for classifier training is underspecified.** The paper states "we work on image patches with a resolution of 224×224 pixels... To generate the patches we use a sliding window with no overlap" (Section 4.1). It does not explicitly state how these patches inherit image-level binary labels during classifier training. The standard approach — assigning the full-image label to every constituent patch — is standard in WSOD literature and accepted under a multiple-instance learning assumption, but it should be stated. Without this clarification, a reader cannot fully assess whether the weak-supervision setup is implemented correctly.

- **The user study measures annotation times only on Herpes virus, but these times are extrapolated to estimate budgets for all five virus types.** Six experts annotated 85 patches of a single virus (Herpes, 165 nm). The annotation time ratios (binary vs. location vs. bounding box) are then applied to Adeno, Noro, Papilloma, and Rota, which differ substantially in size, contrast, and shape. While the ratio is likely similar across viruses, the paper provides no evidence for this generalization (Section 4.2, Section 4.4).

- **Missing implementation details for the optimization procedure.** The paper does not specify the learning rate, number of gradient steps, exact convergence criterion for the position optimization, or the precise schedule of standard deviation decay (beyond "exponential decay performed the best"). These details are necessary for reproducibility (Section 3.2).

- **The SAM and CutLER comparison adds limited value.** These zero-shot models are designed for natural images and their poor performance on EM data is expected. A more informative baseline would be a WSOD method adapted to EM (e.g., MIL-based approaches retrained on this domain) (Section 4.4).

- **Iterative detection may fail on closely packed particles.** The virus removal step masks a circular region of radius \( r \), which could hinder detection of a second virus if two particles are closer than \( 2r \). The paper notes that "virus particles do not overlap in the image plane" (Section 3.5), but they can be adjacent. This potential issue is not discussed (Section 3.3).

### Trivial

- Section 4.4 opens with "our method is able to outperform location and bounding box labels for all viruses" and later states "best results on all viruses except for the Adeno." These statements refer to different comparisons (vs. loc/BB labels vs. vs. zero-shot methods), but the juxtaposition could confuse readers. Clarifying the referent would help.

## Nice-to-Haves

- An ablation study comparing GradCAM initialization vs. random initialization vs. grid search to quantify the benefit of the CAM-guided starting point.
- A sensitivity analysis on the assumed virus radius to assess robustness.
- A visualization showing failure cases and the intermediate masks during the optimization process.

## Removed Points

The following criticisms from the harsh reviewer were removed after verification against the paper:

1. **"The entire method pipeline is unfounded" (Critical Issue 2).** The reviewer argued that without a clear patch-labeling protocol the method is unfounded. However, assigning full-image labels to patches is standard practice in WSOD/MIL literature. The paper could be clearer, but the pipeline is not unfounded. This is a clarity issue, not a structural flaw. Moved to Minor.

2. **Claimed inconsistency in Section 4.4 ("outperform... for all viruses" vs. "except for the Adeno").** The paper's first statement refers to comparison against location and bounding-box labels; the second refers to comparison against zero-shot methods (SAM, CutLER). These are not contradictory. Removed.

3. **Criticism about gradient propagation to \( p_t \) not being explained.** The paper explicitly states: "mask the input image with a Gaussian mask \( M \) centered at \( p_t \), before optimizing \( p_t \) to maximize the classifier score \( C(I \cdot M(p_t)) \)." The mask is a differentiable function of \( p_t \), so gradient flow is clear. Removed.

4. **Claim about "less interesting claim" / "does not require the proposed optimization method."** This is a subjective characterization, not a technical weakness. Any method using binary labels would benefit from more data, but the paper's specific contribution is the optimization that enables turning those binary labels into accurate bounding boxes. Removed.

5. **Criticism about whether annotation types are "actually more costly for a specific virus type."** The paper's own user study directly addresses this by measuring annotation times. Removed.

## Novel Insights

The most interesting observation from the cross-review is that the paper's two key experiments (fixed-budget in Table 1 vs. fixed-data in Figure 6) reveal different regimes of applicability: the weak method's advantage concentrates in the *low-data / low-budget* regime, while supervised methods catch up when data is abundant. This suggests that the practical value of the approach is best understood as a tool for rapid deployment when annotation resources are scarce, rather than as a general replacement for supervised detection. The paper could strengthen its framing by leaning into this characterization rather than claiming to outperform supervised methods broadly.

## Suggestions

1. **Reframe the main claim.** Position the method's advantage as: "Under a fixed annotation budget, our weak-supervision pipeline achieves higher detection accuracy than fully supervised methods trained on fewer images" — which is precisely what the experiment shows. Avoid the unqualified "outperforms fully supervised methods" framing.

2. **Clarify the patch labeling protocol in Section 4.1.** State explicitly how patches inherit image-level labels during classifier training.

3. **Add a sensitivity analysis on the assumed virus radius.** Show mAP50 when \( r \) is varied by ±20%, ±50% to establish practical robustness.

4. **Report optimization hyperparameters.** Specify learning rate, number of gradient steps, convergence criterion, and the exponential decay schedule for \( \sigma_t \).

5. **Include an ablation on initialization strategy.** Compare GradCAM-guided initialization against random and grid-based initialization to quantify the benefit of the CAM prior.

6. **Discuss the closely-packed-particles case.** Acknowledge the limitation when particles are adjacent and mention any planned mitigation.

## Score and Decision

**Originality:** The shrinking-Gaussian optimization for direct box regression from a classifier is novel, though the connection to score-based generative models is acknowledged.

**Importance of research question:** The annotation bottleneck in EM virus detection is a real and significant problem. Reducing it to image-level labels is practically valuable.

**Claims support:** The core practical claim (better detection under equal annotation time) is supported, but the framing overstates the method's superiority. The patch labeling protocol needs clarification for full support.

**Soundness of experiments:** Generally sound with comprehensive comparisons across five viruses. The main confound (data quantity vs. label quality) is partially addressed by the Infinite Annotation Time experiment but should be more prominently discussed.

**Clarity of writing:** Mostly clear. The method description is good; the results section could better distinguish between different comparison types.

**Value to community:** Useful contribution for EM practitioners. The optimization approach could inspire similar work in other scientific imaging domains where bounding-box annotation is expensive.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>