Now let me run calibration search and verify the key numerical claims.Now I have enough information to write the consolidated review. Let me verify the key ablation numbers one more time:

From Table 3 (prior_ablation, lines 291-294):
- Method (a) baseline: mAP=16.48
- Method (b) Road Mask only: mAP=16.27, NDS=28.40, Road mIoU=61.18
- Method (c) Box Mask only: mAP=**26.07**, NDS=36.07, Vehicle mIoU=26.27
- Method (d) Box+Road Mask: mAP=**25.10**, NDS=36.24, mAOE=0.72, Road mIoU=61.26, Vehicle mIoU=27.13

The critic's point about (c)→(d) mAP regression (26.07→25.10) is confirmed. The paper text at line 278 does not discuss this regression — it only reports (d) vs. (a).

The critic's point about BEVControl* underperforming published BEVControl is confirmed: 16.48 vs. 19.64 with BEVFormer. The paper explains that BEVControl* uses "identical settings, with the exception of our innovative element: the PerL-based cross-attention mechanism." However, it never explains why removing PerL-CM makes it 3.16 points weaker than the published BEVControl.

---

## Summary

PerLDiff proposes a perspective-layout diffusion model for controllable street view synthesis. The core contribution is a PerL-based cross-attention mechanism (PerL-CM) that adds a binary geometric prior mask — derived from 3D bounding box projections and road maps — as an additive bias to the softmax logits of cross-attention during training. This encourages the model to associate each object's conditioning features with its corresponding image region. Experiments on NuScenes and KITTI show substantial gains over reimplemented baselines in downstream 3D detection and segmentation metrics, and the generated data is shown to be useful for perception model augmentation.

---

## Strengths

- **Clear architectural idea with genuine advantage over inference-time competitors.** The PerL-CM adds a soft spatial mask ($\lambda \cdot \mathcal{M}$) to cross-attention logits during *training*, eliminating the need for inference-time attention manipulation as required by BoxDiff and ZestGuide. This is computationally simpler and avoids disrupting the diffusion denoising process at test time — a meaningful practical distinction (Section 3.2, Eq. 4).

- **Substantial empirical gains over BEVControl* and MagicDrive on NuScenes.** PerLDiff achieves 25.10 mAP / 36.24 NDS with BEVFormer versus BEVControl*'s 16.48 / 28.08 and MagicDrive*'s 15.21 / 28.79 (Table 1). Even compared to the published BEVControl (19.64 mAP) and MagicDrive (12.30 mAP), PerLDiff shows a convincing margin, indicating the gains are not entirely attributable to baseline reimplementation weaknesses.

- **Clean data augmentation results.** Table 3 (augmentation experiment) shows that PerLDiff synthetic data brings BEVFormer to 31.66 mAP on the NuScenes test set (from 28.97 train-only), closing 83% of the gap to real-val augmentation (32.20), and far outperforming BEVControl* synthetic data (29.92). This is a concrete, downstream-validated result that demonstrates practical utility.

- **KITTI cross-dataset transfer demonstrates geometric precision.** The contrast between PerLDiff (11.04 mAP Easy) and BEVControl* (0.33 mAP Easy) on KITTI — where the geometric prior is critical because of limited training data and monocular depth sensitivity — directly illustrates the value of the PerL masking approach in data-scarce regimes (Table 2).

---

## Weaknesses

### Fatal
None.

### Major

- **Unexplained degradation of BEVControl*.** BEVControl* achieves only 16.48 mAP (BEVFormer) versus the published BEVControl's 19.64 mAP — a 3.16-point gap the paper never explains. The paper asserts BEVControl* uses "identical settings, with the exception of our innovative element: the PerL-based cross-attention mechanism," implying the sole difference is the cross-attention. But the performance gap means either (a) there are other unacknowledged implementation differences, or (b) there is some confounding factor. This undermines the baseline comparison, since the marginal gain attributed to PerL-CM is measured against a self-reported degraded version of the prior art. The same issue applies to MagicDrive* (10.27 vs. published 12.30 mAP with BEVFusion). A clear accounting of what differs between BEVControl and BEVControl* — or an experiment verifying that published BEVControl's 19.64 mAP is reproducible — is needed to validate the ablation premise.

- **Unaddressed mAP regression when road mask is added.** Table 3 (ablation) shows Method (c) (Box Mask only) achieves mAP = 26.07, while the full Method (d) (Box + Road Mask) achieves mAP = 25.10 — a −0.97 regression. The paper presents the "+8.62% in mAP" gain as the headline result of the full method, computed against baseline (a), but never discusses the mAP drop induced by adding the road mask (even though (d) outperforms (c) on NDS, mAOE, Road mIoU, and Vehicle mIoU). The claim that combining both masks "optimally regulates elements of the background and foreground" (Section 4.2) is not substantiated for mAP specifically. This inconsistency should be directly addressed.

### Minor

- **Controllability validated only through downstream detection proxy.** The paper's core claim is "precise object-level control," but this is measured entirely through the mAP/NDS of a detector pretrained on real data applied to synthetic images. This conflates two factors: (a) spatial accuracy of generated objects relative to annotations, and (b) domain realism that determines transfer fidelity. A method that generates photorealistic vehicles in slightly incorrect positions could still score high on this proxy. No direct geometric alignment metric (e.g., IoU between generated object pixels and the projected annotation region) is provided. The attention map visualizations in Figure 3 are qualitative only. This is an important gap for a paper whose central contribution is "controllability." It is noted that using downstream detection as a proxy for controllability is standard in this field, so this is minor rather than fatal.

- **PerL mask carries no orientation signal, but impact on mAOE is not isolated.** The paper acknowledges in the Limitation section that PerL masks do not encode yaw orientation. Since mAOE is a primary metric in the autonomous driving context and the paper reports mAOE improvements (0.88 → 0.72), it would be informative to show how much of that improvement comes from other factors (e.g., better overall object localization) versus actual orientation accuracy. This limitation is mentioned but not quantified.

### Trivial

- Line 278 appears to label the full method (d) as "Method (c)" in the prose — a notation inconsistency between table and text. The numbers are internally consistent, but the description is confusing.

---

## Nice-to-Haves

- A direct geometric alignment metric (e.g., pixel-level IoU between generated object regions and projected 3D box footprints) would directly validate the controllability claim rather than relying solely on downstream detection proxies.
- An experiment perturbing annotations (shifting box positions or yaw) and measuring how well PerLDiff follows vs. ignores the perturbation would characterize controllability beyond the realism proxy.
- Making $\lambda_s$ and $\lambda_b$ jointly learnable (as scalars initialized to 5.0) could remove the grid-search hyperparameter and is a natural extension given that $\gamma_s$ and $\gamma_b$ are already learnable.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "PerLDiff is worse on FID"** — The FID difference (13.05 vs. 13.36) is very small and the paper already acknowledges the trade-off in Section 4.1. Not a meaningful criticism.
- **Harsh Critic: BEVControl* near-zero on KITTI (0.33 mAP) makes the comparison "misleading."** The paper explicitly explains this (Section 4.1): the KITTI dataset has only 3,712 training images, making it hard for standard cross-attention methods to learn the annotation-to-image correspondence without the PerL geometric prior. The explanation is reasonable. This is not a structural flaw.
- **Harsh Critic: "The MLP depth/width not specified" (reproducibility nitpick).** This is an implementation detail; the paper provides sufficient architectural information for researchers to implement the method.
- **Harsh Critic: "λ_s = λ_b set isotropically — independent tuning might reveal insights."** This is a valid experimental extension but is a nice-to-have, not a weakness that threatens the paper's claims.
- **Strength Finder: "Significant improvements over BEVControl* in controllability metrics"** — Kept but partially qualified due to the unexplained BEVControl* degradation. The absolute improvement over published BEVControl (25.10 vs. 19.64) is still substantial and real.
- **Strength Finder: "Comprehensive ablation study isolating component contributions"** — Retained in modified form (the ablation does isolate contributions) but weakened by the unaddressed mAP regression from (c)→(d).

---

## Novel Insights

The key insight the paper adds beyond prior work is that injecting a binary spatial prior directly into the cross-attention softmax *during training* (rather than at inference) is an effective and low-overhead way to improve object-level controllability in diffusion models for street view synthesis. Unlike BoxDiff/ZestGuide which modify attention at inference and can disrupt the denoising dynamics, the training-time approach lets the diffusion model internalize geometric correspondence naturally. The ablation (Table 3) quantifies that the box-level prior (PerL box mask) is far more important than the scene-level prior (road mask) for detection metrics — the road mask adds marginal benefit in NDS/segmentation but costs roughly 1 mAP point. This component-level finding, while not fully discussed in the paper, is an informative signal for researchers in this area.

---

## Suggestions

1. **Provide an explicit account of the BEVControl* vs. published BEVControl gap.** Reproduce the published BEVControl numbers (19.64 mAP) with the same detector to confirm reproducibility, or explain which additional differences (e.g., data processing, training schedule) account for the 3.16-point gap. This is critical for validating that PerL-CM is the sole causal factor in the BEVControl* → PerLDiff gain.

2. **Explicitly address the (c)→(d) mAP regression in the ablation discussion.** Show that the aggregate gain (NDS, mAOE, segmentation) justifies accepting a small mAP drop, or investigate whether a small $\lambda_s$ (e.g., $\lambda_s=1, \lambda_b=5$) can preserve mAP while retaining road segmentation gains.

3. **Add at least one direct geometric alignment measurement.** Compute the proportion of generated object pixels that fall within the projected annotation region across the validation set. Even a simple correlation between annotation placement and generated object centroid would directly support the controllability claim.

---

## Score and Decision

**Anchor comparison:**

| Path | Avg Human Score | Comparison to PerLDiff |
|---|---|---|
| `sBQwvucduK.md` (MagicDrive) | 6.00 | Direct predecessor in same domain; PerLDiff shows larger empirical gains on NuScenes but a narrower/simpler contribution; MagicDrive has broader scope (full system, multi-view, video) |
| `Dq9VrVuLzV.md` (SyntheOcc) | 5.00 | Similar evaluation setup on NuScenes; rejected with similar type of proxy-metric concerns; PerLDiff has cleaner ablations but similar unresolved issues |
| `0uFTqvQhML.md` (MagicDrive3D) | 5.00 | More complex contribution (3D generation), rejected; PerLDiff more focused but results are substantive |
| `f92M45YRfh.md` (Satellite-to-Street) | 6.25 | Different task; accepted with somewhat similar precision-alignment contributions |
| `dTGH9vUVdf.md` (FreeVS) | 5.80 | Accepted; similar generative driving synthesis context; more novel framing |
| `G6aJyS0ZV0.md` (3D StreetUnveiler) | 6.25 | Accepted; autonomous driving street scene understanding; higher technical novelty |
| `TBw53TdDgb.md` (SADE) | 3.50 | Low anchor; much weaker contribution, clearly insufficient experiments |
| `skJLOae8ew.md` (Floor Plan Diffusion) | 3.00 | Low anchor; superficial methodology, no compelling empirics |
| `ndRkLsoQ1Q.md` (Noisy Labels) | 3.75 | Low anchor; different topic, limited technical novelty |

**Assessment:** PerLDiff sits between the MagicDrive (6.00, accepted) and SyntheOcc/MagicDrive3D (5.00, rejected) anchors. The contribution is genuinely simpler than MagicDrive but the empirical gains are larger and more clearly isolated. The two major issues (unexplained BEVControl* degradation and unaddressed mAP regression) reduce confidence in the quantitative claims without invalidating the direction. The data augmentation results are the cleanest contribution. Overall, the paper makes a real, implementable contribution with substantive results, but the ablation inconsistency and baseline explanation gap place it below a comfortable accept.

**Originality:** Moderate. The idea of using mask biases in cross-attention is intuitive; the application to perspective-projected 3D annotations for driving is the novelty.  
**Importance:** Moderate-high. Controllable driving synthesis for perception augmentation is practically valuable.  
**Claim support:** Mixed. Gains over published baselines are real, but the ablation premises have issues.  
**Experiment soundness:** Mostly sound with two methodological gaps noted.  
**Clarity:** Good overall; a few notational inconsistencies (method labeling in ablation text).  
**Community value:** Positive; the training-time PerL-CM approach is an improvement over inference-time alternatives.

**Final Score: 5.0 — Borderline Reject**

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>