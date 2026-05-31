Now I have all the information I need. Let me write the final consolidated review.

---

## Summary

This paper introduces a new task — concurrent two-speaker co-speech 3D gesture generation — along with a large-scale pseudo-labeled dataset (GES-Inter, 70 hours, 7M+ frames) and a method (Co³Gesture) that uses bilateral diffusion branches with a Temporal Interaction Module (TIM) and mutual attention to produce coherent two-person gestures. The task is well-motivated, the dataset fills a clear gap (it is the first large-scale concurrent two-speaker whole-body mesh dataset), and the core architectural design is validated by clean ablations.

## Strengths

1. **First large-scale concurrent co-speech gesture dataset with whole-body mesh.** GES-Inter provides 70 hours / 7M+ frames of two-speaker interactive gestures with multi-modal annotations (facial, mesh, phoneme, text). Table 1 shows it is the only dataset offering concurrent gestures, mesh representation, and all four additional attributes simultaneously, while prior datasets like TWH16.2 lack facial data and BEAT2 lacks concurrent gestures. This is a substantial resource contribution.

2. **Bilateral cooperative diffusion framework validated by clear ablation improvements.** The two-branch design with separated audio conditioning (Section 3.3) is directly motivated by asymmetric body dynamics. Table 4 shows removing bilateral branches degrades FGD from 0.769 to 1.669, and removing audio separation degrades BC from 0.692 to 0.633 — cleanly confirming the design choices are critical for the task.

3. **TIM and Mutual Attention provide measurable, well-ablated gains.** Table 3 shows TIM outperforms an MLP-based fusion (FGD 0.769 vs 1.202) and removing mutual attention hurts (FGD 0.769 vs 0.924), demonstrating these components contribute to interaction coherence.

4. **SOTA quantitative results on the new task.** Table 2 shows Co³Gesture achieves FGD 0.769, BC 0.692, substantially outperforming adapted baselines including InterGen (FGD 1.012, BC 0.670), demonstrating the framework successfully addresses the new task.

## Weaknesses

### Fatal

None.

### Major

- **The foot contact loss ablation result is suspicious and unexplained.** Table 5 shows removing L_foot causes FGD to jump from 0.769 to 1.082 (a 41% degradation). The paper explicitly states (Sec 4.1) that only upper body joints (46 joints: 16 body + 30 hand) are generated, and the lower body is fixed as a T-pose during forward kinematics when computing this loss (Sec 4.2, ablation text). The lower body is also fixed as seated during visualization (Sec 4.3). While root rotation (part of the 16 generated body joints) could propagate through the kinematic chain to affect foot position in world space, a 41% improvement in FGD from this indirect effect alone is implausibly large without a much clearer mechanistic explanation. This result may reflect high variance in the metric (no CIs are reported for FGD, see Minor weakness below) or an artifact of the implementation. Either way, **this result is not reliable as published** and should not be used as evidence until the authors clarify exactly how the loss is computed and why the effect is this large. Importantly, however, this issue is localized to Table 5 and **does not invalidate the paper's core claims**, which are supported by other ablations (Tables 3, 4) that do not involve L_foot.

### Minor

- **Missing confidence intervals for FGD and BC.** The tables report 95% CI only for Diversity. FGD and BC are reported as point estimates without variance. Given the test set size (~2,054 clips from 7.5% of 27,390), the point estimates may have substantial variance. This is especially relevant for the foot contact loss ablation (above), where the reported effect is very large. The paper would be strengthened by reporting standard deviations or CIs across runs or bootstraps.

- **Small user study with no significance testing.** 15 participants each rated 16 videos (240 ratings per metric). The reported margins over InterGen are modest (~0.3 points on a 5-point scale for interaction coherency). No error bars, significance tests, or inter-rater agreement metrics are provided. The results are suggestive but not strongly conclusive.

- **MLP is a weak baseline for TIM ablation.** Table 3 replaces TIM with an MLP layer, producing FGD 1.202 vs 0.769. While this supports TIM's value, a simple temporal cross-attention without the soft-weight blending would be a more informative control. The w/o TIM row (FGD 1.297) is a cleaner ablation.

- **No quantitative validation of pseudo-labeled pose quality.** The dataset uses Pymaf-X estimates without a held-out quantitative quality check (e.g., MPJPE against manual annotations or mocap). The paper acknowledges this as a limitation, but it is worth noting as the dataset is intended to serve as a benchmark.

- **Equation 1 uses a single projection matrix W for Q, K, V**, which is unconventional. This is likely a notation simplification but should be clarified.

### Trivial

None.

## Nice-to-Haves

- A stronger baseline: two independent DiffSHEG or ProbTalk branches (one per speaker, no interaction modeling) would directly test whether the bilateral design and interaction module are necessary beyond independent generation.
- Expanding the user study to 30+ participants with significance tests and error bars would strengthen the qualitative claims.
- Clarifying how the temporal correlation matrix M (Sec 3.3) is computed (dot product? cosine similarity?) and how the motion encoder producing σ works.

## Removed Points

- **Criticism that the foot contact loss issue is "fatal" and the paper "should not be accepted":** Removed from Fatal tier. The foot contact loss is a separate auxiliary loss whose ablation is in Table 5, distinct from the core technical contributions validated in Tables 3 and 4. While the result is suspicious and needs resolution, it does not invalidate the paper's central claims about bilateral branches, TIM, or mutual attention. Downgraded to Major.
- **"No confidence intervals for the two primary metrics" as a critical issue:** The paper does report CIs for Diversity with ± notation, and FGD/BC CIs are missing. This is a valid but standard limitation in this field (many gesture papers report FGD as point estimates). Downgraded from critical to Minor.
- **"The comparison set leans heavily on adapted text2motion methods" as a fairness concern:** This is the standard approach for a new task with no existing baselines. The asymmetry favors baselines (same audio encoder as ours), so this is not a flaw against the paper. Removed.
- **"The user study is too small to support strong conclusions" downgraded from critical:** 15 participants is at the low end of acceptable for this community but not unusually small. Combined with the modest margins, the results are suggestive rather than conclusive. Downgraded from critical to Minor.
- **"Pure formatting/style nitpicks" and "reproducibility nitpicks":** Removed per filtering rules.
- **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem"): Removed per filtering rules; only concrete, evidence-backed strengths retained.

## Novel Insights

None beyond the paper's own contributions. The key insight — that two-speaker concurrent gesture generation benefits from asymmetric bilateral branches with temporal interaction modeling — is clearly articulated by the authors themselves.

## Suggestions

1. **Resolve the foot contact loss issue.** Either remove L_foot from the model and re-run all experiments, or provide a detailed, physically grounded explanation of how it meaningfully affects upper-body-only outputs. If the model generates root translation/rotation that propagates to the T-pose lower body, quantify this mechanism and show that its contribution to FGD is plausible at the reported magnitude. Report the foot contact loss ablation with CIs.
2. **Report CIs or standard deviations for FGD and BC** across multiple sampling runs or bootstrap samples of the test set.
3. **Expand the user study** to include more participants and report significance tests (e.g., paired bootstrap) and inter-rater agreement (e.g., Krippendorff's alpha).
4. **Provide quantitative validation** of the pseudo-labeled pose quality on a small held-out subset with manual annotations or comparison to mocap data.

## Score and Decision

### Calibration Anchors

| Paper (Path) | Avg Score | Round | Comparison |
|---|---|---|---|
| CoCoGesture (g3kK6YBSZ1.md) — Reject | 4.0 | R1 bracket | Same research group, similar topic but weaker novelty and method validation. Current paper is stronger (new task, better ablations). |
| VideoDiT (lvgsPjRtLM.md) — Reject | 2.5 | R1 bracket | Unrelated topic (video generation). Not comparable. |
| DynamicsDiffusion (kKXIYUi8ff.md) — Reject | 3.0 | R1 bracket | Unrelated topic (molecular dynamics). Not comparable. |
| Human Motion Prior (dTpbEdN9kr.md) — Accept (poster) | 6.0 | R1/R2 | Also tackles two-person motion via diffusion; cleaner experiments but weaker dataset contribution. Current paper is slightly weaker due to foot contact loss concern. |
| TANGO (LbEWwJOufy.md) — Accept (oral) | 8.5 | R1 bracket | Higher quality/novelty co-speech work. Current paper is clearly below this tier. |
| DART (XNA3Mnnbvb.md) — Accept (spotlight) | 6.6 | R2 narrow | Strong real-time text-to-motion with clean validation. Current paper is below this level of experimental rigor. |
| NaturalSigner (4JjSJyT15z.md) — Reject | 4.75 | R2 narrow | Sign language generation; also pseudo-labeled data but limited novelty concerns. Current paper is stronger. |

**Round-1 bracket:** [4.0, 7.5] (between CoCoGesture at 4.0 and the oral-level papers at 7.6+).

**Round-2 narrowing:** The closest comparable accepted anchor is Human Motion Prior (6.0). The current paper has a stronger dataset contribution and tackles a genuinely new task, but has weaker experimental rigor (foot contact loss issue, missing CIs). It is clearly stronger than CoCoGesture (4.0) but somewhat weaker than Human Motion Prior (6.0) in terms of trust in the reported results.

**Final placement:** The paper sits between 5.0 and 6.0. At 5.5, it is a borderline paper with a solid core contribution but an unresolved experimental concern (foot contact loss) that prevents full trust in the results. A revised version that resolves this issue could be a strong 6+ paper.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>