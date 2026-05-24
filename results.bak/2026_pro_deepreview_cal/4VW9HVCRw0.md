Now I have a thorough understanding of the paper and the calibration anchors. Let me compile the final review.

After cross-checking all reviewer claims against the actual paper, here is my assessment:

**Round 1 Bracket:** The paper is clearly stronger than HOI-Diff (5.25) and IHDiff (5.50) — it has a new dataset, more comprehensive framework, and broader scope. It sits below the 7.5+ tier (Co³Gesture, InstructScene) which have more polished evaluation. Initial bracket: **6.0 – 7.5**.

**Round 2 Narrowing:** Compared against Phidias (6.20) and TapMo (6.50): the paper under review has broader evaluation than Phidias but shares some experimental design concerns. It is comparable to TapMo in contribution quality — a novel task with a well-designed method and reasonable experiments — though TapMo's evaluation is cleaner in some respects while narrower in others.

**Final score anchored at 6.5**, positioned above Phidias (6.20, experimental robustness concerns) and at TapMo level (6.50, novel capability with some evaluation gaps), but below the 7.5 tier due to the split design concern and metric under-specification.

---

## Summary

This paper introduces the task of **Free-Form HOI Generation** — generating diverse hand-object interactions beyond grasping, conditioned on fine-grained text and object geometry. The authors contribute (1) **WildO2**, a large-scale in-the-wild 3D HOI dataset (4.4k samples, 92 intents, 610 object categories) built via an automated O2HOI reconstruction pipeline from internet videos, and (2) **TOUCH**, a three-stage framework combining contact-map prediction CVAEs, a multi-level conditioned diffusion model with coarse-to-fine semantic/geometric control, and a cycle-consistency refinement module. Comprehensive ablations and out-of-domain generalization on Objaverse demonstrate the method's effectiveness.

## Strengths

- **Novel task and dataset fill a genuine gap.** The paper moves HOI generation beyond the grasp-centric paradigm that dominates prior work. WildO2 is the first large-scale, in-the-wild 3D HOI dataset covering non-grasping actions (pushing, poking, rotating), with 17-part hand segmentation and VLM-generated descriptive captions (DSCs). The O2HOI frame-pairing strategy and three-stage reconstruction pipeline (Sec. 3.1–3.2) are technically sound and enable scalable dataset construction.

- **Well-designed three-stage framework with strong empirical validation.** The contact-map prediction CVAEs (Sec. 4.1) explicitly model hand and object contact surfaces, providing spatial priors beyond grasp heuristics. The multi-level conditioned diffusion (Sec. 4.2) with coarse-to-fine FiLM/cross-attention injection yields P-IoU of 0.776, substantially outperforming ContactGen (0.620) and Text2HOI (0.711). The cycle-consistency refinement (Sec. 4.3) is validated by ablation: removing the refiner drops P-IoU from 0.728 to 0.513 (Table 2).

- **Thorough ablation study.** Every design choice is tested: hand-object contact features (hoc.), multi-level structure (mul.), DSC/SSC text, cycle loss, text encoder (Qwen-7B vs. CLIP/BERT/MPNet), and refiner/TTA. The ablations coherently justify the architecture (Table 2, Sec. 5.3–5.4).

- **Out-of-domain generalization evidence.** Figure 7 shows plausible interactions on four Objaverse CAD models not seen during training, using LLM-generated DSC-format captions. This qualitatively supports the claim that TOUCH learns transferable contact and semantic priors rather than memorizing training objects.

- **Insightful analysis of force-related semantics.** The model implicitly associates terms like "firmly"/"gently" with contact area size (22–25% larger contact for "firm" prompts, Fig. 9), demonstrating semantic nuance beyond explicit supervision.

## Weaknesses

### Fatal
None.

### Major

- **Dataset split does not isolate object instances, partially weakening generalization claims.** The split is described as "for each hand part contact category, we perform a random 4:1 split" (Sec. 5.1). This is stratified by hand-part label but not by object identity or category. Since WildO2 is built from Something-Something V2 videos where similar objects can appear across clips with different actions, the same object instance or highly similar objects may appear in both train and test. This means the quantitative results in Tables 1–2 may partially reflect familiarity with object geometry rather than pure generalization to novel interaction configurations. The out-of-domain results (Fig. 7) partially mitigate this concern but do not replace controlled quantitative evaluation. An object-category-aware or clip-level split would strengthen the evidence substantially.

- **Core evaluation metrics are insufficiently defined in the main paper.** Diversity is reported as "Ent↑" and "CS↑" (cluster size) with no explanation of what distributions the entropy is computed over, how clusters are formed, or what distance metric is used. The "VLM↑" score (Table 1) has no description of the model, prompt template, or scoring protocol. The perceptual score (PS) from 10 users lacks details on the rating scale, task design, or inter-rater agreement. P-FID (Nichol et al., 2022) is cited but how a point-cloud FID is adapted to evaluate hand poses is not explained. These gaps make it difficult to assess the meaningfulness of the reported improvements and hurt reproducibility.

### Minor

- **Baseline post-processing is not detailed.** Both ContactGen and Text2HOI are augmented with "an optimization-based post-processing module to correct hand poses" (Sec. 5.2). The nature and hyperparameters of this module are not described. It is unclear whether baseline performance without this module is substantially worse, and whether the module is equally effective for both baselines and TOUCH. Since TOUCH has its own refiner (Sec. 4.3), the fairness of the comparison depends on whether the post-processing is comparable across methods. This does not threaten the core claims but adds uncertainty to the quantitative comparisons.

- **No quantitative quality assessment of WildO2 reconstructions.** The pipeline yields a 55% success rate after manual inspection (Sec. 3.2, Fig. 3a), but no metrics (e.g., 2D reprojection error, human judgment on reconstruction fidelity) are reported. Since the ground-truth hand poses and contact maps used for training and evaluation are derived from this pipeline, reconstruction noise propagates into all downstream metrics. Reporting even a modest quality assessment would increase confidence in the dataset.

### Trivial

- The tension between generating "static snapshots" and the action-oriented framing (pushing, poking, rotating) is acknowledged only in the conclusion (Sec. 6). Earlier scoping would help readers.

## Nice-to-Haves

- Per-action or per-object-category performance breakdowns would clarify where TOUCH succeeds and struggles (e.g., push vs. lift vs. rotate).
- A failure case panel (e.g., complex multi-contact or heavily occluded scenarios) would strengthen the analysis.
- A simple nearest-neighbor retrieval baseline from the training set would help gauge whether the diffusion model is generating novel poses or recalling training configurations.
- Reporting quantitative reconstruction quality metrics for the WildO2 pipeline (even on a small subset) would improve confidence in the ground truth.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic: "Dataset split invalidates the quantitative evaluation" (claimed as fatal).** While the split design concern is legitimate (retained as Major above), the claim that it "renders the quantitative comparisons uninterpretable" overstates the severity. The dataset has 610 object categories and 4.4k samples — it is not obvious that object leakage is pervasive enough to invalidate all metrics, and the out-of-domain results provide corroborating evidence. Demoted from Fatal to Major.

- **Harsh critic: "Baselines may be weak proxies, and post-processing may not be neutral."** The paper explicitly states that post-processing was added to help the baselines, which if anything makes the comparison harder for TOUCH. The concern that the module may be unfairly tuned is speculative and not supported by evidence from the paper. Retained as Minor (lack of detail).

- **Harsh critic: "P-FID is cited from Nichol et al. but it is not explained how a point-cloud FID is adapted to evaluate hand poses or what the reference distribution is."** Partially valid — metric under-specification is a real issue — but the harsh critic frames this as making results uninterpretable, which is an overstatement. Retained as part of the Major metric-definition weakness.

- **Strength Finder: "The choice of the Qwen-7B text encoder is justified by controlled comparisons."** This is a genuine finding but is a standard ablation, not a core strength. The paper would be expected to justify its text encoder choice. Kept but not listed as a top-line strength.

- **Strength Finder: "The physical refinement module with cycle-consistency loss eliminates pose drift."** The ablation shows substantial improvement but "eliminates" is too strong — the paper shows it reduces but does not claim to eliminate drift. The evidence is good but the framing is corrected.

## Novel Insights

None beyond the paper's own contributions. The review process did not surface insights that the paper itself does not already contain.

## Suggestions

- Redesign the dataset split to separate by object category or use clip-level isolation. At minimum, discuss the potential for object leakage and report per-category metrics to bound its effect.
- Add concise metric definitions to the main paper (even 1–2 sentences each for Ent, CS, VLM, PS, P-FID), moving detailed protocols to the appendix if needed.
- Report quantitative reconstruction quality for WildO2 (e.g., 2D reprojection error on a held-out subset) to establish ground-truth reliability.
- Include per-interaction-type breakdowns and a failure case analysis in the appendix or discussion.

## Score and Decision

**Anchor comparison summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| HOI-Diff (ZYwLfi50GI) | 5.25 | R1 | TOUCH is clearly stronger — has new dataset, better hand contact modeling, more comprehensive evaluation |
| IHDiff (nTNElfN4O5) | 5.50 | R1 | TOUCH has broader scope (HOI vs. two-hand only), new dataset, more technical depth |
| Phidias (TEkoMEjf7E) | 6.20 | R2 | Comparable contribution level; TOUCH has broader evaluation but shares experimental design concerns |
| TapMo (OeH6Fdhv7q) | 6.50 | R2 | Most comparable — novel task + method + good experiments; TapMo has cleaner split but narrower evaluation |
| Co³Gesture (VaowElpVzd) | 7.50 | R2 | Co³Gesture has more comprehensive and better-structured evaluation; TOUCH's metric/split issues prevent reaching this tier |

**Bracket:** Round 1 placed the paper in 6.0–7.5. Round 2 narrowed to 6.0–6.5, anchored against Phidias (6.20) and TapMo (6.50). The paper is comparable to TapMo in contribution quality but has a more concerning evaluation design issue (split). Score: **6.5**.

The paper addresses a genuine gap with a well-motivated task, contributes a resource (WildO2) that will benefit the community, and proposes a technically sound method validated by thorough ablations. The evaluation concerns — primarily the split design and metric under-specification — are significant but addressable, and do not invalidate the core contributions.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>