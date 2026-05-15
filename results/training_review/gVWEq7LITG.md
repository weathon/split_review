I now have a thorough understanding of the paper and all the claims. Here is my consolidated review.

---

## Summary

The paper proposes TF-HOT (Training-Free Hand-Object Tracking), a pipeline that optimizes hand and object pose trajectories from monocular video using differentiable rendering combined with priors from pre-trained 2D foundation perception models. The approach avoids costly 3D annotations by leveraging 2D hand joints, masks, and 3D point clouds as optimization constraints. The paper also demonstrates an application in imitation learning (Pose Trajectory Following, PTF) where pose trajectories extracted by TF-HOT are used as dense reward signals to train dexterous manipulation policies, outperforming standard RL and IL baselines.

## Strengths

- **Well-motivated and conceptually clean approach**: The core idea of combining differentiable rendering with pre-trained 2D foundation models in a training-free optimization loop directly addresses the annotation bottleneck and generalization challenges that plague learning-based hand-object trackers. The use of rich 2D perception priors (joints, masks) to guide 3D optimization is a sensible design choice. (Section 1)

- **Efficient per-video processing**: The paper claims the entire pose optimization can be completed within 1 minute per video with no model training required. If validated, this efficiency is a real advantage for generating demonstration data at scale for downstream tasks like imitation learning. (Section 1, Abstract)

- **Ablation study demonstrates contribution of each loss term**: The ablation study on the DexYCB can category (Section 4.3, Table 2) systematically removes each loss component. The qualitative results in Figure 6 are informative: the visible-aware 3D surface loss handles occlusion, the penetration loss prevents interpenetration, the attraction loss produces realistic grasps, and the regularization loss stabilizes against depth noise. This shows the design is principled.

- **Application to imitation learning is a natural downstream use case**: Demonstrating that TF-HOT trajectories enable PTF to outperform PPO (sparse/dense reward) and SOIL on dexterous pickup tasks (Figure 7c) provides a compelling argument that the extracted trajectories are practically useful. (Section 4.4)

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The PTF application experiment does not isolate the quality of TF-HOT's trajectories from the advantage of the trajectory-following paradigm.** PTF uses pose trajectories as dense rewards, while PPO receives only task-level rewards. This comparison shows that using trajectory information helps, but it does not demonstrate whether TF-HOT's specific trajectory quality drives the improvement. A cleaner ablation would compare PTF using TF-HOT trajectories vs. PTF using ground-truth poses or trajectories from a different (e.g., learning-based) tracker. Without this, the experiment primarily validates the trajectory-following approach itself rather than TF-HOT's specific contribution.

- **The ablation study is limited to a single object category (can) on DexYCB.** While the qualitative results are illustrative, the quantitative ablation (Table 2) is restricted to one category, which limits confidence in the generalizability of the loss-term analysis to other objects and interaction types.

- **No numerical success rates at convergence reported for PTF.** The results are presented as learning curves in Figure 7c without reporting final numerical success rates, making it difficult to assess the precise magnitude and statistical significance of the improvement over baselines.

- **Several experimental details are deferred to supplementary material.** The precise noise magnitudes, reward formulations for baselines, and the baseline methods used for the DexYCB comparison are noted as being in the supplementary material. While this is standard practice, it makes it harder to fully assess experimental rigor from the main paper alone.

### Trivial

- Table 2 is embedded as an image in the extracted text, making the exact MPJPE values unreadable in this version (this is a parser artifact, not an author error).

## Nice-to-Haves

- A comparison of PTF using TF-HOT trajectories against PTF using ground-truth or alternative pose trajectories would strengthen the claim that TF-HOT produces high-quality pose data.
- Runtime profiling across diverse video lengths and conditions would substantiate the "1 minute per video" efficiency claim.
- Ablating the choice of the pre-trained 2D models (e.g., different hand keypoint detectors or segmentation models) would test the method's robustness to its upstream components.
- An analysis of failure cases (e.g., severe depth noise, transparent objects, fast motion) would provide a more balanced assessment.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"The paper is structurally incomplete — Sections 2 and 3 are missing."** The extracted paper is only 66 lines long and jumps from Section 1 to Section 4.3, but this is a PDF parsing/extraction failure, not an author error. The original submission would have contained these sections. Per instructions, formatting/extraction artifacts should not be counted against the paper.

2. **"Quantitative results are absent or unreadable (Table 2 is an image)."** The table is embedded as an unextractable image — a parser artifact. The original paper presented this table in a readable format.

3. **"The main evaluation against baselines on DexYCB is not shown."** The paper claims state-of-the-art performance on DexYCB, and this comparison table almost certainly existed in the original submission's full Section 4 (which was not extracted). The extracted text references "superior performance... compared to baseline methods" but the actual table is in the missing sections. This is a parser artifact.

4. **"The application experiment is unfairly configured — PTF has privileged information."** The comparison is explicitly designed to show that using pose trajectories as dense rewards (PTF) outperforms methods that do not use such information (PPO, SOIL). This is the intended experimental design, not an unfair configuration. Criticizing it as "unfair" misunderstands the paper's claim: the paper shows that trajectories extracted by TF-HOT are useful for policy learning, not that TF-HOT's trajectories are better than an equally-privileged alternative.

5. **"Missing related works"** — cannot be verified without external sources.

6. **Criticisms about missing appendix content, proof details, or hyperparameters** — these are standard supplementary material items, not missing core content.

## Novel Insights

None beyond the paper's own contributions. The review process did not generate any observations that were not already present in the paper.

## Suggestions

1. In the PTF application experiment, add a condition where the same trajectory-following formulation is applied using ground-truth poses (or poses from a competing tracker). This would isolate whether TF-HOT's trajectory quality specifically contributes to downstream performance, beyond the general advantage of the trajectory-following paradigm.

2. Expand the ablation study to at least 2–3 object categories with different shapes and sizes to demonstrate that the loss term analysis generalizes beyond the "can" category.

3. Report final numerical success rates alongside the learning curves for the PTF experiment, with confidence intervals, to allow precise comparison.

## Score and Decision

The paper presents a well-motivated, cleanly designed approach to a practical problem. The core contribution — training-free hand-object pose tracking via differentiable rendering guided by 2D foundation model priors — is sound and addresses a genuine need. The ablation study provides evidence that each loss term serves a distinct purpose, and the imitation learning application demonstrates downstream utility. The primary limitations visible in the extracted text are (a) the PTF experiment does not fully isolate the quality of TF-HOT's trajectories from the trajectory-following paradigm, and (b) the ablation is limited in scope. These are addressable weaknesses, not fatal flaws. The paper makes a reasonable contribution to the field.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>