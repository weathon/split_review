Now I have enough context. Let me draft the review before calibration.Good. Now let me run the bracketing calibration search.Let me read the most relevant anchors to form an initial bracket.Based on Round 1, my initial bracket is **5.0–6.5**. CORE-3D is comparable to OpenNeRF (6.0, accepted) in scope but with weaker ablation methodology. Now narrowing within that range.Now I have enough to calibrate. My **Round 1 bracket was 5.0–6.5**, and Round 2 narrows this to **5.0–6.0**:

- **PointSeg** (5.25, Rejected) — training-free 3D segmentation pipeline, similar spirit to CORE-3D but broader evaluation across multiple large datasets. Rejected for writing clarity and limited novelty. CORE-3D is written better and adds a retrieval component, but has comparable methodological concerns.
- **View-Independent** (5.25, Rejected) — CLIP-based 3D feature distillation, rejected for unclear pipeline and limited real-world evaluation.
- **OpenNeRF** (6.0, Accepted) — more technically rigorous, training-based, better-ablated. CORE-3D's undisclosed weights and backbone disparity put it below this anchor.
- **CORE-3D** sits slightly above PointSeg (5.25) due to better presentation, a broader set of contributions (retrieval task is novel), and convincing SR3D+ gains — but the backbone disparity and undisclosed weights keep it below OpenNeRF (6.0).

**Final score: 5.5, Reject.**

---

## Summary
CORE-3D is a training-free pipeline for open-vocabulary 3D scene understanding that combines: (1) progressive multi-granularity SemanticSAM mask generation to reduce fragmentation; (2) a context-aware CLIP embedding strategy aggregating five complementary crops per mask (including a negatively-weighted surroundings crop); and (3) a VLM/LLM-based structured retrieval framework for language-grounded object localization. Evaluated on Replica, ScanNet, and SR3D+, it reports state-of-the-art results across both semantic segmentation and retrieval tasks without any 3D supervision.

---

## Strengths

- **Progressive granularity refinement demonstrably reduces fragmentation**: Table 3 shows that the progressive strategy achieves mIoU 0.29 (Replica) and 0.36 (ScanNet), versus vanilla SAM at 0.22/0.27 and the best single-granularity level (Level 2) at 0.25/0.32. The multi-level accumulation outperforms every fixed-granularity variant, substantiating the paper's core motivation.

- **Substantial and credible retrieval gains**: On SR3D+ (661 queries), CORE-3D achieves 41.8% A@0.1 vs. BBQ's 34.2% and 35.6% A@0.25 vs. BBQ's 22.7% (Table 2). The 7–13 point margins across all difficulty subsets (Easy, Hard, View-Dependent, View-Independent) are large enough to be statistically credible at this evaluation scale and represent a genuine contribution to zero-shot language-grounded 3D retrieval.

- **Principled symmetric-balanced IoV merging criterion**: The three-condition merge criterion (Section 3.3) — both IoV(a,b) > γ, IoV(b,a) > γ, and |IoV(a,b) − IoV(b,a)| < δ — explicitly prevents degenerate containment merges (e.g., cushion on sofa), a known failure mode of naive IoU-based merging. This is a specific, verifiable design improvement.

- **Multi-crop CLIP aggregation with contrastive context**: The five-crop design (Section 3.2, Eq. 4), including a negatively-weighted surroundings crop, is a well-motivated technique that addresses CLIP's known sensitivity to isolated object crops. Table 4 shows a dramatic performance gap over OvSeg (mIoU 0.29 vs. 0.11 on Replica, 0.36 vs. 0.16 on ScanNet), though this comparison conflates the method design with the stronger backbone (see Weaknesses).

---

## Weaknesses

### Fatal
None.

### Major

- **Undisclosed embedding weights in Eq. 4 with no sensitivity analysis — risks test-set tuning**: The five crop weights {w_mask, w_bbox, w_large, w_huge, w_sur} are described only as "empirically tuned" (Section 3.2, line 119) and their values are never stated anywhere in the paper. Since the Replica and ScanNet benchmarks used for evaluation are small (8 scenes each), it is possible these weights were selected by observing performance on those very scenes. The ablation in Table 4 compares the full tuned system against OvSeg — a different fine-tuned model — rather than against a single-crop or equal-weight version of the same approach. Without (a) disclosed weight values, (b) a sensitivity analysis, and (c) a held-out validation procedure, the reader cannot determine whether gains come from the multi-crop design or from weight optimization against the evaluation sets. This is the core technical contribution of the paper and it is not adequately isolated.

- **CLIP backbone disparity conflates backbone strength with methodological contribution**: Section 4.1 discloses that CORE-3D uses Eva02-L CLIP while the zero-shot baselines (ConceptFusion, ConceptGraphs, BBQ-CLIP) use standard CLIP ViT-L/14. The paper mentions parameter-count parity with OvSeg (line 271) but does not provide a version of CORE-3D using the same CLIP backbone as the comparison baselines. Consequently, the segmentation improvements reported in Table 1 over those baselines cannot be cleanly attributed to the proposed multi-crop strategy rather than the stronger backbone.

### Minor

- **LLM and VLM model identities unspecified**: Section 4 (line 185) states the VLM and LLM components are "accessed through external APIs" without naming the specific models or versions used. Retrieval performance on SR3D+ (Table 2) depends heavily on the capability of these external models, making the results non-reproducible as reported.

- **Re-encoding step after 3D merging is underspecified**: Section 3.3 (lines 141–147) states that after averaging merged embeddings the pipeline will "re-apply our multi-crop CLIP embedding procedure." The multi-crop procedure in Section 3.2 requires 2D image crops tied to original frames. It is not explained which frame(s) are used when re-encoding a merged 3D cluster, or how this interacts with multi-view averaging. This is an implementationally critical ambiguity.

- **8-scene evaluation with no variance reporting**: Both segmentation benchmarks evaluate exactly 8 scenes (line 197). Reported margins of 2–5 mIoU units are plausible but, at this scale and given run-to-run variation in external API calls, their significance cannot be assessed without at least a standard deviation. The SR3D+ evaluation (661 queries) is substantially less fragile.

### Trivial
None.

---

## Nice-to-Haves

- Add a same-backbone ablation: CORE-3D with standard CLIP ViT-L/14 to disentangle backbone strength from the multi-crop aggregation design.
- Add a single-crop baseline (bounding-box only) using Eva02-L to isolate the contribution of multi-crop aggregation vs. the stronger backbone alone.
- Add a retrieval component ablation on SR3D+: removing VLM verification vs. removing orientation grounding independently to attribute the improvement over BBQ.
- Report the actual weight values for Eq. 4 and include a simple sensitivity table (e.g., ±50% perturbation on each weight).

---

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **Granularity Level=6 catastrophic failure used as a criticism of the progressive approach**: The reviewer noted Level=6 achieves near-zero mIoU (0.09–0.11) and argued the progressive strategy's value is "simply avoiding the over-segmented regime." However, the progressive method outperforms every single-granularity variant including the best one. The catastrophic Level=6 failure is evidence motivating progressive accumulation, not evidence against it. **Removed as strawman.**

- **Table 3 ablation conflates mask and embedding contributions**: The critic speculatively states "it is not clear whether the ablation uses the same CLIP embedding strategy throughout." There is no textual evidence that this is not the case; the ablation reports full-system numbers across granularity conditions, which is standard practice. **Removed as speculative.**

- **Table 5 extension ratio ablation is "secondary"**: Called a "secondary design choice" by the critic. It is a supporting ablation, not a weakness. **Removed as not a weakness.**

- **Missing related works**: Not raised, but any such criticism would be removed per Hard Rules since related works cannot be verified.

---

## Novel Insights

The contrastive surroundings crop — a negatively-weighted embedding of the background context — is a genuinely interesting inference-time technique that exploits CLIP's contrastive pretraining objective at the level of feature aggregation, without any fine-tuning. Unlike prior works that simply widen the crop window or average multiple scales, this design explicitly pushes the final embedding away from the background distribution, achieving what amounts to background suppression at the representation level rather than the pixel level. The failure mode at Granularity Level=6 (near-zero mIoU across both datasets) also provides concrete, quantitative evidence for where SemanticSAM's fine-granularity regime becomes pathological in indoor 3D mapping, which could inform future work on adaptive granularity selection.

---

## Suggestions

1. **Disclose the Eq. 4 weights and add sensitivity analysis** — even if the weights are tuning artifacts, revealing them enables reproduction and the sensitivity analysis resolves ambiguity about robustness.
2. **Add a same-backbone ablation (CORE-3D with ViT-L/14)** — this single experiment would cleanly separate backbone contribution from method contribution and substantially strengthen the evaluation.
3. **Name the external LLM and VLM models** — required for reproducibility of retrieval results.
4. **Clarify the 3D merge re-encoding step** — which frame is selected for re-encoding the merged cluster, and how is the CLIP crop extracted from a merged 3D cluster?
5. **Expand ScanNet evaluation or report variance** — even running on 5 additional scenes and reporting standard deviation would greatly strengthen the segmentation claims.

---

## Score and Decision

**Calibration Anchors:**

| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| PSzDG612AC (Zero-shot domain adaptation) | 3.00 | R1, low | Clearly weaker than CORE-3D; rejected |
| MqvQUP7ZuZ (DC3DO diffusion 3D) | 3.00 | R1, low | Unrelated domain; much weaker |
| 0jUeqlQxMi (Open Vocab Panoptic) | 4.00 | R1, mid | Weaker scope than CORE-3D; rejected |
| SgjAojPKb3 (OpenNeRF) | 6.00 | R1, mid | Accepted; training-based, similar task, but cleaner ablation; CORE-3D is weaker on methodology |
| ENv1CeTwxc (Segment Any 3D Object) | 6.50 | R1, mid | Accepted; learning-based with stronger evaluation; CORE-3D is below this anchor |
| CRmiX0v16e (Open-YOLO 3D) | 7.80 | R1, mid | Strong accepted paper; significantly stronger than CORE-3D |
| P4o9akekdf (No Pose 3D Gaussians) | 8.00 | R1, high | Different task; much stronger |
| 7RVJxmtzTj (PointSeg) | 5.25 | R2 | Rejected training-free 3D segmentation; similar spirit to CORE-3D; CORE-3D is better-presented and adds retrieval but has comparable methodological issues |
| izzYucQBji (View-Independent CLIP) | 5.25 | R2 | Rejected CLIP 3D distillation; somewhat comparable weaknesses |
| ORUiqcLpV6 (CoT3DRef) | 6.00 | R2 | Accepted 3D visual grounding; different approach (supervised); CORE-3D is weaker |
| 7nOl5W6xU4 (CityAnchor) | 6.50 | R2 | Accepted 3D grounding with LLMs; stronger evaluation and clearer ablations |

**Round 1 bracket:** 5.0–6.5  
**Round 2 narrowing:** PointSeg (5.25, Rejected) and View-Independent (5.25, Rejected) represent papers with similar training-free philosophy and similar or more thorough evaluation that were still rejected. CORE-3D is better than these anchors (cleaner paper, novel retrieval pipeline, convincing SR3D+ gains) but the backbone disparity and undisclosed weights are substantive unresolved issues that would concern reviewers, placing it below OpenNeRF (6.0) or CoT3DRef (6.0).

**Final calibrated score: 5.5** — above the rejected training-free segmentation anchors at 5.25 due to better presentation and the additional retrieval contribution, but below the accepted 6.0 papers due to the undisclosed tuning procedure for the central contribution and the backbone disparity that prevents clean attribution of results.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>