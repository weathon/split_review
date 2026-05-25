Now I have all the information needed to produce the final consolidated review.

---

## Summary

This paper introduces the task of Free-Form HOI Generation — producing diverse, non-grasping hand-object interactions (pushing, tipping, rotating) from fine-grained textual prompts and object geometry. It contributes (a) WildO2, a 4.4k-sample 3D dataset automatically reconstructed from Internet video with multi-level annotations (92 intents, 610 object categories, 17-part hand segmentation), and (b) TOUCH, a three-stage framework combining contact-map prediction, a multi-level conditioned diffusion model, and physical refinement. The task definition and dataset are genuine contributions, and the method is technically sound. However, the evaluation has significant gaps that prevent full confidence in the claimed advantages.

## Strengths

1. **New task definition with demonstrated feasibility beyond grasping.** The paper formalizes "Free-Form HOI generation" — breaking the dominant grasp-centric paradigm — and provides concrete evidence (Table 1, Figs. 5, 8) that TOUCH generates non-grasping interactions (e.g., pushing with an index finger, tipping, rolling) that prior methods (ContactGen, Text2HOI) cannot produce. Table 1 shows TOUCH outperforms baselines in contact accuracy (P-IoU 0.776 vs. 0.711) and semantic consistency (P-FID 4.13 vs. 15.72).

2. **WildO2 dataset is a valuable resource.** The O2HOI frame-pairing pipeline (Section 3) addresses a genuine bottleneck: it scalably produces 3D HOI samples from 2D video without manual completion or template fitting. The 4.4k samples with 92 intents, 610 object categories, 17-part hand segmentation, and multi-level text annotations fill a real gap — existing datasets are predominantly lab-based and grasp-only.

3. **Architecture validated by thorough ablations.** Table 2 quantifies the contribution of each component: removing contact prediction (hoc.) drops P-IoU from 0.728→0.492, removing the multi-level structure (mul.) to 0.525, and removing the refiner to 0.513. These degradations are substantial and consistent, confirming that the three-stage design is synergistic and necessary.

## Weaknesses

### Major

1. **Baseline adaptation is insufficiently specified.** The comparison against ContactGen and Text2HOI (Section 5.2) is the main evidence for the method's superiority, but the adaptation details are critically thin. Text2HOI adaptation is described only as "remove its temporal axis and adapt it for our setting" with no specifics about architecture changes, loss functions, or training protocols. The "optimization-based post-processing module to correct hand poses" added to both baselines is completely unspecified — what objective does it optimize? Was it tuned equally for each baseline? How much of the reported baseline performance is carried by this add-on? Without this information, the reader cannot assess whether the comparison is fair, and the central quantitative claim is undermined.

2. **Semantic controllability — the paper's defining contribution — is evaluated with insufficient rigor.** The paper claims fine-grained control as its core advance, yet the evidence comprises:
   - Hand-picked qualitative examples (Figs. 5, 7, 8).
   - A "VLM assisted evaluation" metric in Table 1 that is entirely undefined in the main text — no model name, prompt, evaluation protocol, or scale is provided. The reader sees "VLM↑" with values (4.8, 6.5, 7.1) and has no basis to interpret them.
   - A perceptual score from only 10 users (Table 1).
   - A correlational force-level analysis (Fig. 9).

   For a paper whose central claim is enabling *controlled* generation beyond grasping, the absence of a quantitative metric for part-level contact accuracy against the text-specified hand region, and the reliance on a 10-person study, leaves the main contribution under-evidenced.

### Minor

3. **Inconsistent treatment of PD/PV metrics.** Section 5.3 correctly warns that penetration depth/volume can be "deceptively low" when contact is weak (exemplified by the ✗ refiner variant with P-IoU 0.513). Yet Table 1 reports PD and PV as "Physical Plausibility" evidence without caveat. While all methods in Table 1 do establish nontrivial contact (P-IoU ≥ 0.62), the paper's own argument creates confusion about what these numbers mean. This inconsistency should be resolved by explicitly stating in Section 5.1 that PD/PV are informative only when contact is established, and that contact metrics are the primary plausibility measure.

4. **Dataset construction bias is acknowledged but not discussed.** Figure 3 reports a 55% success rate and 31% "Pore Estimation Failure." The paper does not analyze whether the 45% of discarded clips are systematically different from the successes (e.g., specific poses, object categories, or interaction types that are harder for MANO reconstruction). If so, the training distribution is narrower than the "daily HOI" framing suggests.

5. **VLM metric undefined in main text.** Despite appearing as a numbered column in the primary comparison table, the VLM-assisted evaluation receives zero description in the visible main text — no prompt template, no model, no scale, no methodology. Readers cannot assess what this metric measures.

### Trivial

None.

## Nice-to-Haves

- Report variance or confidence intervals for the quantitative metrics in Tables 1 and 2 to assess significance.
- Provide inference-time / computational cost analysis for the three-stage pipeline (CVAE + Diffusion + TTA refinement).
- Include a failure-mode analysis of the generation model (what types of prompts/objects cause implausible outputs).

## Removed Points

- **"PD/PV makes Table 1 untrustworthy"** — Removed because this overstates the issue. The paper's warning about deceptive PD/PV applies to the ✗ refiner ablation (P-IoU 0.513), where the hand drifts away from the object. In Table 1, all compared methods establish nontrivial contact (P-IoU ≥ 0.62), so the PD/PV comparison is not in the deceptive regime. The criticism is valid only as a presentation inconsistency (kept as Minor #3 above).
- **"OOD verbs are in-distribution"** — Removed. WildO2's 92 intents are a subset of Something-Something V2's 174 classes, so "Pinch" and "Press" can be in SSv2 yet outside WildO2's selected intents. The main text does not list the 92 intents, so this cannot be verified either way.
- **"Missing related works"** — Removed per policy (cannot verify external references).
- **Various formatting/style nitpicks and requests for appendix content** — Removed per policy.
- **"Dataset bias from 45% failure rate"** — Demoted from potential major to minor (#4) because the paper does show the breakdown; the issue is that implications are not discussed rather than that the information is hidden.

## Novel Insights

None beyond the paper's own contributions. The most striking observation in the reviews — that the paper's own ablations reveal PD/PV can be deceptive — is already stated in Section 5.3.

## Suggestions

1. **Specify all baseline adaptation details.** Describe the exact architecture changes, loss functions, training protocol, and the optimization-based post-processing module (objective, hyperparameters, tuning procedure) for both ContactGen and Text2HOI. Release reference implementations.
2. **Define the VLM evaluation.** State the VLM model, prompt template, scoring scale, and evaluation protocol. Report inter-prompt variance.
3. **Add a part-level contact accuracy metric.** Measure whether the generated hand-part contact matches the hand part specified in the DSC text (e.g., "index pad" should be in contact).
4. **Expand the human evaluation.** Increase the rater pool and add a forced-choice semantic compliance test (does the generated interaction match the intended verb?).

## Calibration Analysis

**Round-1 bracket:** 4.5 – 6.0 (based on topic-anchored and weakness-anchored queries).

**Anchor comparison:**

| Path | Score | Round / Query | Comparison to Paper |
|------|-------|---------------|-------------------|
| HOI-Diff (ZYwLfi50GI) | 5.25 | R1-mid, R2, R2-q2 | Most comparable (text-driven 3D HOI). Rejected for evaluation gaps. Paper slightly stronger (dataset contribution, hand-level detail) |
| IHDiff (nTNElfN4O5) | 5.50 | R1-mid, R2, R2-q2 | Two-hand diffusion. Rejected for limited novelty. Comparable quality |
| InterDance (KfkmwYQXWh) | 5.60 | R2 | Dance generation. Rejected. Comparable quality |
| Interactive-Action Img (OWIk5E4lJs) | 5.20 | R1-mid | 2D images. Rejected for limited scope. Paper stronger in dataset contribution |
| ViTaM-D (J4D5WVoc5g) | 4.50 | R1-mid, R2 | HOI reconstruction, not generation. Less comparable |
| Adversarial Instance Attacks (zQXX3ZV2HE) | 3.00 | R1-low | Much weaker in all dimensions |

**What low-band anchors failed at:** Poor motivation, unclear contributions, trivial methods, or no evaluation. TOUCH does not share those failures — its task definition, dataset, and architecture are genuine contributions.

**What the most comparable mid-band anchors (HOI-Diff, IHDiff) failed at:** Evaluation gaps, missing/weak baselines, insufficient verification of core claims. TOUCH *shares* these failures: baseline adaptation is opaque, semantic controllability is under-evaluated, and key metrics are undefined or inconsistently handled. This places it in the same 5–6 range as those papers, slightly above HOI-Diff (5.25) due to its stronger dataset contribution, but not above the rejection threshold for a top venue.

## Score and Decision

**MY FINAL SCORE:** <score>5.5</score>
**MY FINAL DECISION:** <decision>Reject</decision>