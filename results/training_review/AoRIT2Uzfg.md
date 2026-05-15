Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the consolidated review.

## Summary

This paper proposes DRMGuard, the first backdoor defense framework specifically designed for deep regression models (DRMs) in the image domain. It identifies a novel feature-space signature of backdoored DRMs — the ratio of angle variance (RAV) being significantly smaller than 0.1 — and formulates a reverse-engineering optimization that jointly minimizes output variance, L1 input perturbation, and feature-space angle variance. Experiments on gaze and head pose estimation across four datasets and four backdoor attacks show strong identification (95% on MPIIFaceGaze) and mitigation performance, substantially outperforming four adapted classifier defenses.

## Strengths

- **Novel identification of a DRM-specific feature-space backdoor signature.** The paper discovers and empirically demonstrates (Table 1, Figures 1b/c) that for backdoored DRMs, the angle between feature vectors and the output-layer weight matrix has dramatically reduced variance (RAV ≪ 0.1) compared to benign inputs, across all four examined attacks and two datasets. This observation is theoretically grounded in the structure of DRMs (no argmax, continuous output, all neurons active) and fundamentally distinguishes DRM backdoors from DCM backdoors — it is the paper's core intellectual contribution.

- **Principled optimization framework that circumvents the infinite-target-space problem.** Equation (4) replaces the impossible enumeration of continuous target vectors with an output-variance minimization objective, coupled with a feature-space regularization term derived from the RAV observation. The ablation study (Table 7, w/o FSRT: all models misclassified as backdoored) proves that this feature term is not merely helpful but *necessary* for DRM detection — a clean empirical validation of the theory.

- **Comprehensive and honest evaluation scope.** The experiments cover two regression tasks (gaze estimation, head pose estimation), four datasets (MPIIFaceGaze, ColumbiaGaze, Biwi Kinect, Pandora), four backdoor attacks spanning input-independent (BadNets, Clean Label) and input-aware (WaNet, IA) categories, ablation on hyperparameters λ₁, λ₂ and benign dataset size, an adaptive attack, and a multi-backdoor scenario. The paper also adapts four classifier defenses and reports their failure — which, while not flattering, honestly documents the domain gap.

- **Effective backdoor mitigation that outperforms adapted approaches.** After fine-tuning on reversed poisoned data, DRMGuard raises AE from ~1.3 to ~15.4 and lowers DAE from ~15.9 to ~3.3 for WaNet on MPIIFaceGaze (Table 5), significantly exceeding Fine-pruning and ANP (Table 6), which are fundamentally mismatched to DRMs.

- **Clear explanation of why classifier defenses fail on DRMs.** The paper correctly identifies two structural causes: (1) continuous outputs preclude target enumeration, and (2) the absence of argmax means all neurons contribute to backdoor behavior, unlike DCMs where only a few neurons matter. This analysis is well-motivated and consistent with experimental observations.

## Weaknesses

### Fatal
None.

### Major

1. **Architecture validation is limited to a single backbone with a linear output head, yet the Discussion claims generality to "different architectures."** All experiments use ResNet18 (without its dense layer) as $F$ and a single linear dense layer (no activation) as $H$. While the theory in Equation (1) includes an activation function $\Omega$, it is set to identity in practice. Real-world DRMs often use non-linear output heads (MLPs with ReLU, multiple layers, residual connections) where the direct relationship between angle variance and output variance may break. The paper states in the Discussion (line 441) that DRMGuard "can be generalized to different architectures," but no experiment with a different backbone or output head is provided. This overclaims the scope of validation.

2. **The Momentum Reverse Trigger (MTR) mechanism is critically underspecified.** The MTR is described in one high-level sentence (line 189): it "assigns different weights to different regions to balance the attention of the DRM on the image." The detailed description of gradient-based attention map generation is present only as a LaTeX comment (%, not rendered in the PDF). The ablation study (Table 7) shows that removing MTR causes complete failure on benign models (10 FPs), making MTR a *necessary* component, yet no algorithm, pseudocode, or formal description of how the weights are computed or updated is given. This is a reproducibility concern.

3. **Limitation section is inadequate.** The paper devotes a single sentence to limitations (line 443: "our method requires a small benign dataset"), neglecting to acknowledge the architecture dependency noted above, threshold ($\epsilon=0.03$) sensitivity, the computational cost of training a generative model per DRM under test, the small evaluation scale, or the dataset-dependent performance variability (70% on ColumbiaGaze vs. 100% on Biwi Kinect with no analysis of why).

### Minor

1. **Small evaluation scale and perfect ROC-AUC scores.** Each condition evaluates 10 backdoored + 10 benign models. While this is not atypical for defense papers, the ROC-AUC of 1.000 across all four attacks on MPIIFaceGaze should be interpreted cautiously. On datasets where performance drops (ColumbiaGaze: 70% accuracy), the method's limitations are more visible. The paper would benefit from either confidence intervals or a larger model count to establish stability.

2. **Adapted baseline defenses may not be optimally tuned.** The paper generalizes Neural Cleanse and FeatureRE by "taking the potential target vector $y_t$ as the optimization variable" (Section 4.1). While NC achieves a reasonable 0.940 AUC on WaNet (suggesting the adaptation has some validity), its 0.005 AUC on Clean Label is so low that it raises the question of whether the adaptation itself requires better tuning rather than reflecting a fundamental limitation of NC. Given that DRMGuard is the paper's primary comparison point, a more thorough effort to make baselines competitive would strengthen the comparison.

3. **Performance variability across datasets is unexplained.** Accuracy ranges from 70% (ColumbiaGaze) to 100% (Biwi Kinect), yet the paper offers no analysis of why. The FP/FN patterns differ substantially (ColumbiaGaze: 4 FPs, 2 FNs; Pandora: 0 FPs, 3 FNs), suggesting dataset-specific factors (image size, pose distribution, background diversity) affect the perturbation threshold or the RAV observation, but this is not discussed.

4. **Threshold $\epsilon=0.03$ sensitivity is not analyzed.** The ablation on benign dataset size shows that FP counts change from 2 to 0 as $p$ varies (Table 7), indicating the identification threshold interacts with data availability. A sensitivity analysis showing how $\epsilon$ affects TP/FP rates across datasets would help assess robustness.

### Trivial
None.

## Nice-to-Haves

- **Test the RAV observation on diverse architectures** (e.g., VGG, ViT, or ResNet with a non-linear MLP head) to support the claim of generality.
- **Provide full algorithm details for MTR** (attention map computation, weighting scheme, update rule) either in the main paper or an appendix.
- **Report per-dataset analysis** explaining why ColumbiaGaze and Pandora underperform MPIIFaceGaze and Biwi Kinect, particularly whether dataset diversity, image resolution, or output dimensionality are factors.
- **Include a threshold sensitivity analysis** for $\epsilon$ across datasets.
- **Report approximate runtime** for the reverse-engineering stage (training $G_\theta$) to help gauge practical deployability.

## Removed Points

The following points from the reviewer inputs are flagged to be removed; treat them with caution:

- **Criticism about Section 4.1 text reading "as if main experiments are scoped to one attack":** This is a misreading. The sentence "{We consider gaze estimation task with MPIIFaceGaze dataset and the state-of-the-art input-aware attack WaNet}" (line 228) describes the *default setting* for defense hyperparameters; the experimental section then evaluates all four attacks and four datasets. REMOVED (factually wrong / misread).
- **Criticism that "first defense" claim is overstated given Li et al. (2021):** The paper explicitly qualifies "in the image domain" and acknowledges Li et al., whose work considered five-dimensional vector inputs. The claim is precise and accurate. REMOVED (misread).
- **Criticism demanding validation that adapted NC/FeatureRE work on classification problems:** This asks the paper to solve a proxy problem outside its stated scope. DRMGuard's goal is to defend DRMs; the baselines are adapted in a reasonable (though improvable) way. REMOVED (scope creep).
- **Demands for confidence intervals and 50+ models per condition:** While not unreasonable, many single-run defense papers use 10 models per condition; this is a field convention issue. WEAKENED from a severe criticism to a minor note.
- **Complaint that the Discussion section claims generalization to "different architectures" is unsupported:** This criticism is KEPT (it is accurate), but it appears under Major Weaknesses, not removed.

## Novel Insights

The most striking finding in this review is the tension between the paper's clean theoretical contribution and the fragility implied by the ablation studies. The RAV metric is elegant: it captures a structural necessity of DRM backdoors (that all neurons must agree on a single output, forcing angle concentration). Yet the MTR ablation shows that without region-aware weighting, the method collapses on *benign* models (10/10 FPs). This suggests the framework is balancing on a knife's edge: the feature-space term prevents false negatives, while MTR prevents false positives. Neither alone works. This delicate interdependence is a double-edged sword — it makes each component indispensable (good science, well-ablated) but also suggests the method may be brittle if the attention maps or weighting schemes are not carefully tuned for each dataset. The ColumbiaGaze results (70% accuracy) may reflect this brittleness. The paper does not discuss this trade-off, but the data points to it.

## Suggestions

1. Verify the RAV observation on at least one additional backbone (e.g., a ResNet with a 2-layer MLP head with ReLU) and one additional architecture (e.g., a ViT-based regressor). If RAV ≪ 0.1 holds, the generality claim is strongly supported; if it fails, the scope should be explicitly bounded.
2. Provide the full MTR algorithm — the gradient-based attention map computation and the momentum-weighted update rule — either in the main paper or as pseudocode in an appendix. This is necessary for reproducibility.
3. Expand the limitation section to honestly discuss architecture scope, threshold sensitivity, computational cost, and the dataset-dependent performance variation observed in the experiments.
4. Add a brief analysis of why ColumbiaGaze and Pandora underperform: is it image resolution, pose diversity, or something else? This would strengthen the paper's scientific value.
5. Include a sensitivity analysis for $\epsilon$ across at least two datasets to demonstrate whether a fixed threshold is reasonable or if per-dataset calibration is needed.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>