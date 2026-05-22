Now I have good calibration. Let me write the final review.

**Round-1 bracket:** Based on the calibration, the paper clearly sits above the weak band (scores 2.5–3.0, all reject) and below the strong band (scores 8.0, all accept). The middle band (3.5–7.5) contains the most relevant comparisons. I initially bracket this paper between 5.0 and 7.0.

**Round-2 narrowing anchors considered:** HandsOnVLM (6.33, Reject), HAMSTER (6.00, Accept), Cross-Embodiment (5.00, Accept), Articulate-Anything (6.20, Accept), VLP (7.00, Accept).

**Comparison to anchors:** UniHM is clearly stronger than Cross-Embodiment (5.00). It is comparable to HAMSTER (6.00) and slightly stronger than HandsOnVLM (6.33, Reject) because UniHM's experiments are cleaner and its technical contributions more substantial. It is weaker than VLP (7.00), which has broader scope and more polished presentation. **Final score: 6.0, leaning Accept.**

---

## Summary

UniHM proposes a unified framework for generating *dynamic*, *language-conditioned* dexterous hand manipulation sequences (not just static grasps). It couples (a) a cross-morphology VQ-VAE codebook that lets different hand types share a common discrete action space, (b) a small VLM (Qwen3-0.6B) with a decoupled perception module and progressive masking curriculum for instruction-conditioned token generation, and (c) a physics-guided refinement that optimizes contact, generative-prior, and smoothness terms per frame. Evaluated on DexYCB and OakInk, UniHM outperforms adapted motion-generation baselines (TM2T, MDM, FlowMDM, MotionGPT3) on MPJPE, FOL, FPL, and FID, and shows promising real-world success rates.

## Strengths

- **First dynamic, language-conditioned dexterous manipulation beyond static grasps.** Prior methods either generate static grasp poses only or work on low-DoF grippers. UniHM produces full manipulation sequences conditioned on open-vocabulary instructions, and the experiments support this advance: e.g., MPJPE 61.40 vs. 74.80 (MotionGPT3) on seen DexYCB (Table 1), with similar margins on OakInk (Table 2).

- **Morphology-agnostic shared codebook with cross-hand distillation.** The paper formalizes a shared VQ-VAE codebook (Eq. 1–2) with a distillation objective (Eq. 3) that aligns encoders across hand morphologies, enabling token reuse across five dexterous hands (Shadow, Allegro, SVH, Leap, Panda). The unified translation formula (Eq. 6) makes cross-morphology transfer direct.

- **Physics-guided dynamic refinement is clearly beneficial.** The energy-based post-processing (Eq. 11–18) with contact, generative-prior, and temporal-smoothness terms improves feasibility. Ablation (Table 4) shows physical refinement degrades MPJPE from 61.40 to 65.78 on seen DexYCB, confirming its contribution.

- **Strong ablation study.** The paper ablates depth input, masked training, and physical refinement (Table 4), showing all components are necessary. The progressive masking curriculum (Eq. 10) alone accounts for a large performance drop when removed (MPJPE 61.40 → 73.41).

- **Real-world validation on diverse task categories.** Table 3 reports success rates for four task types (Grab, Pick&Place, Pull&Push, Open&Close) on both seen and unseen objects, demonstrating practical applicability.

## Weaknesses

### Major

1. **Diversity collapse on DexYCB is not discussed.** In Table 1, the ground-truth Diversity is 125.53; UniHM achieves 39.62 (seen) and 42.70 (unseen) — a ~68% collapse. MotionGPT3 achieves 72.51/75.84, substantially more diverse. The paper claims "closer to GT is better" but does not acknowledge this weakness or analyze its cause (e.g., codebook collapse, mode-seeking from the masking curriculum, or smoothness penalties in refinement). On OakInk the diversity is closer to GT (165.47 vs. 147.40 seen), making the DexYCB gap particularly notable. This omission undermines the claim that the method produces "human-like" and "diverse" sequences across all settings.

2. **Real-world evaluation lacks critical experimental details.** The entire real-world section (Table 3, Fig. 3) provides no: hardware specification (which dexterous hand? Which robot arm?), number of trials per condition, success criteria per task category, failure mode analysis, or breakdown by object. Without this information, the 60% "Grab" success rate for unseen objects cannot be properly interpreted or compared. The ablation study uses only DexYCB, not OakInk, and real-world results lack any breakdown by object category or instruction type.

### Minor

3. **Baseline adaptation method is underspecified.** The paper states that baselines (TM2D, MDM, FlowMDM, MotionGPT3) are post-processed with the physics-guided refinement "to ensure a fair comparison" (Section 4.3), but does not describe how these full-body motion generation models are adapted to the hand-manipulation input format (language + object point cloud + target trajectory) or whether they are fine-tuned on the hand-specific datasets. The real-world table (Table 3) lists "MDM+Dex-Retargeting" and "MotionGPT3+Dex-Retargeting" without the physics refinement, creating an inconsistency with the main tables where refinement is applied. While the paper's overall improvement is likely robust, the comparison is less informative than it could be.

4. **The "first" claim is slightly overstated.** The abstract claims "the first unified framework for dexterous hand manipulation guided by free-form language commands." HOIGPT (Huang et al., 2025) also generates HOI sequences from text. The Related Work section acknowledges HOIGPT and makes the distinction that prior work targets "Digital Hand" rather than dexterous robot hands — this distinction is reasonable but should be clearer in the abstract/introduction.

5. **No direct comparison with or discussion of HOIGPT as a baseline.** Since HOIGPT generates HOI sequences, it would be a natural competitor. The paper acknowledges it in Related Work but does not include it in the experimental comparison, citing that it targets digital hands. Explanation of why HOIGPT cannot be adapted to this setting would strengthen the evaluation.

### Trivial

6. Table 2 footnote style is inconsistent: MPJPE for GT row shows "—" while Diversity shows "147.40". Clarify which GT metrics exist.
7. Some abbreviations (FOL, FPL) are defined only in Section 4.2 but the arrow notation "→" for Diversity is not explicitly explained (it means "closer to GT is better").

## Nice-to-Haves

- **Ablate the shared codebook.** The paper central claim of cross-morphology capability is not directly ablated (e.g., training separate codebooks per hand vs. shared).
- **Sensitivity analysis of CLIPort/Point-SAM errors.** The inference pipeline uses estimated trajectories from CLIPort while training uses ground-truth. An analysis of how perception errors propagate to manipulation quality would be informative.
- **Inference time / optimization cost.** The frame-by-frame Gauss-Newton optimization — reporting total time per sequence would help assess real-time viability.

## Novel Insights

None beyond the paper's own contributions. The combination of a cross-morphology discrete codebook with a small VLM and physics-guided refinement is a design choice with ablative support, but the individual components are standard.

## Suggestions

1. **Discuss the diversity gap on DexYCB explicitly.** Analyze whether the collapse is caused by the VQ codebook size, the masking curriculum, or the refinement smoothness penalty, and if possible, increase diversity (larger codebook, stochastic sampling) or justify why lower diversity is acceptable for the target tasks.
2. **Add real-world experimental details:** hardware setup, number of trials, success criteria per task, failure analysis, and object breakdown. This is essential for the claimed "strong generalization to open-world tasks."
3. **Clarify baseline adaptation** by explicitly stating: (a) whether baselines received text + point cloud + trajectory input or just text + initial pose, and (b) whether they were fine-tuned or used off-the-shelf.

## Removed Points

- **"CLIPort and Point-SAM are not cited/described"** — The references section (which would contain these citations) was stripped by the parser. The paper describes the functional role of both modules ("takes RGB-D and language to infer target trajectories" for CLIPort; "segments the object point cloud" for Point-SAM), which is reasonable granularity for a systems-level description. Per hard rules, absent citation visibility cannot be penalized.
- **"Point-SAM receives no definition"** — The paper explicitly says it is used to "segment the object point cloud P_obj with the corresponding semantics" (Eq. 8). Its function is defined.
- **"Dexterity metrics are ambiguous"** — The paper states "Diversity → closer to GT is better" and the GT values are listed. The calculation direction is clear.
- **"Hyperparameters not given"** — Training hyperparameters (learning rate, batch size, etc.) are standard details that would appear in an appendix (which was stripped). Per hard rules, this is not a valid criticism.
- **"Missing ablation of shared codebook"** — This is a nice-to-have rather than a core weakness, as the ablation study does show the components that directly impact the main metrics.

## Score and Decision

**Calibration anchors used:**

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| xcHIiZr3DT | 2.50 | R1 | Much weaker — simple vision-based grasping, no language or sequence generation |
| q1Cv7Hp52y | 3.00 | R1 | Much weaker — RL skill discovery, unrelated to dexterous manipulation |
| AJQuTFd9es | 6.33 | R1/R2 | Slightly weaker — had missing experimental details and unclear baselines, was rejected |
| h7aQxzKbq6 | 6.00 | R1/R2 | Comparable — hierarchical VLA with similar documentation gaps, accepted |
| 9pKtcJcMP3 | 7.00 | R2 | Stronger — broader scope, more polished presentation, accept |
| Aqfwhna1D7 | 5.20 | R1 | Weaker — simpler problem setting, reject |
| twIPSx9qHn | 5.00 | R2 | Weaker — static grasps only, limited cross-embodiment, accepted |
| s3FTX4Ay55 | 6.20 | R2 | Comparable quality — different domain (articulated objects), accepted |

**Round-1 bracket:** 5.0–7.0  
**Narrowing:** Comparisons to HAMSTER (6.00, accept) and HandsOnVLM (6.33, reject) place UniHM around 6.0. The paper has stronger experiments than HandsOnVLM but similar documentation gaps, putting it in a "borderline accept" territory.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>