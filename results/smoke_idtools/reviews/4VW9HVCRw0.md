Now I will produce the final consolidated review.

---

## Summary

This paper introduces **Free-Form HOI Generation**, a new task that extends hand-object interaction synthesis beyond the grasp-centric paradigm to include non-grasping actions (pushing, poking, rotating, etc.). To support this, the authors construct **WildO2**, a 4.4k-sample 3D HOI dataset from internet videos via an automated O2HOI frame-pairing pipeline. They propose **TOUCH**, a three-stage framework combining (1) contact map prediction via CVAEs, (2) a multi-level diffusion model with coarse-to-fine text/geometry conditioning, and (3) a self-supervised cycle-consistency refinement. Experiments show TOUCH outperforms adapted baselines on contact accuracy, physical plausibility, diversity, and semantic consistency.

## Strengths

1. **Novel and well-motivated task formulation.** The paper clearly identifies that existing HOI generation is dominated by grasp-centric priors and proposes free-form HOI generation as a meaningful extension. The argument that contact, not penetration metrics, should be primary for this task (since a hand that drifts away trivially avoids penetration but fails the interaction) is well-reasoned and specific to the problem.

2. **O2HOI frame-pairing pipeline is a genuine technical contribution.** The strategy of pairing object-only frames (I_ref) with interaction frames (I_hoi) from video, transferring object masks via dense matching (avoiding diffusion-inpainting inconsistencies), and then using differentiable rendering for camera alignment is clever, scalable, and produces 4,414 high-quality 3D samples. The 55% success rate with documented failure modes is honestly reported (Fig. 3a).

3. **Multi-level conditioning architecture is thoughtfully designed.** Injecting coarse semantic cues (SSCs, global geometry) in early diffusion blocks and fine-grained cues (DSCs, local contact features) in later blocks is a principled alignment with the problem structure. The 10% random drop of global conditions during training prevents over-reliance. Ablations (Table 2) confirm each component contributes meaningfully — e.g., removing the multi-level structure (✗mul.) drops P-IoU from 0.728 to 0.525.

4. **Clear quantitative advantage over adapted baselines on multiple metric families.** In Table 1, TOUCH outperforms both ContactGen and Text2HOI on contact accuracy (P-IoU 0.776 vs. 0.711/0.620), physical plausibility (MPVPE 2.97 vs. 4.69/5.46), penetration depth (0.932 vs. 1.239/1.296), diversity (Entropy 2.93 vs. 2.85/2.85), and semantic consistency (P-FID 4.13 vs. 15.72/6.08). The advantage is not confined to the contact-focused metrics where TOUCH has a structural advantage.

5. **Cycle-consistency loss for refinement is novel and ablated.** Equation 7's bidirectional contact-mapping consistency loss is a clean idea. The ablation (Table 2, ✗L_cycle → P-IoU drops 0.728→0.702, P-FID 4.84→5.79) confirms its contribution.

## Weaknesses

### Fatal
None.

### Major

1. **Baseline comparison is informative but limited.** Only two baselines are compared (ContactGen and a temporally-ablated Text2HOI), and both were originally designed for different settings (grasp generation and video-sequence HOI). The paper's justification — that no existing method handles free-form fine-grained controlled HOI — is reasonable, but the evaluation would be significantly stronger with at least one more recent text-conditioned HOI method adapted (e.g., the works cited as Zhang et al. 2025a;b). This limits the reader's ability to calibrate how much of the gain is from the dataset vs. the method architecture vs. the task redefinition itself.

2. **No error bars, standard deviations, or statistical significance reported for any metric.** Tables 1 and 2 present single-point estimates. Given the modest test set size (677 samples), this omission makes it impossible to assess whether differences are meaningful or within noise. This is a standard expectation in the field and should be addressed.

3. **Semantic controllability evaluation is thin relative to the central claims.** The paper's headline claim is fine-grained semantic control (hand parts, object parts, force nuance), yet the quantitative support relies on: (a) P-FID — referenced but computation details are sparse; (b) VLM-assisted evaluation — no prompt, model choice, or agreement analysis given; (c) Perceptual Score from 10 users — too small to draw reliable conclusions. The ablation removing T_DSC (fine-grained text) shows only a ~0.03 P-IoU drop (0.728→0.698), which is modest for the claimed level of control. A direct test — e.g., generating with varying hand-part specifications for a fixed object and measuring whether the specified parts are indeed the contacting ones — would substantially strengthen the evidence.

4. **Dataset size and source diversity limit the "in-the-wild" claim.** WildO2 draws from a single source (Something-Something V2, which contains staged interactions in controlled settings) and yields only 4.4k samples after a 55% reconstruction success rate. The term "in-the-wild" is somewhat overstated for this provenance. The method's generalization beyond Something-Something-like scenarios is demonstrated only qualitatively on a handful of Objaverse examples (Fig. 7). Computing quantitative metrics on a held-out set of novel objects with human-verified ground truth would substantiate the generalization claim.

### Minor

1. **Contact maps are computed via a heuristic, not true ground truth.** The paper acknowledges using "relative and absolute distance thresholds with bidirectional nearest-neighbor filtering" to identify contacts. Errors from this step propagate into both training and evaluation. While this is a practical necessity, the impact of contact-map noise is not analyzed.

2. **Auxiliary loss weights (λ_global, λ_dmap, λ_cycle, β in Eq. 3) are not reported.** These are important for reproducibility. The paper should specify them at least in the appendix.

3. **Entropy and cluster size (diversity metrics) are mentioned but never defined.** The features used and computation procedure are absent, making these numbers uninterpretable.

4. **The refiner is trained with frozen diffusion parameters, but the rationale for not finetuning jointly is not discussed.** The paper should justify this design choice or at least ablate it.

### Trivial

- The caption symbols in Table 2 (✗hoc., ✗L_eye, etc.) are not all defined inline, making the table hard to parse without cross-referencing the text. "L_eye" in the table refers to the cycle-consistency loss L_cycle (parser corruption) — this should be corrected.
- "Pore Estimation Failure" in Figure 3a is a likely parser corruption of "Pose Estimation Failure" — should be fixed.

## Nice-to-Haves

- A systematic taxonomy or quantitative breakdown of what fraction of generated outputs are non-grasping (e.g., pushes, pokes, rotations) vs. grasping, and how this compares across methods, would strengthen the "free-form" claim.
- A comparison of three text variants: (i) only SSC, (ii) only DSC, (iii) both, would directly isolate the additive value of the two text levels beyond the current ablation.
- Failure case analysis (e.g., where contact prediction is wrong, where the hand penetrates, where geometry is violated) would help readers understand the method's remaining limitations.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Criticism about "Pore Estimation Failure" being unexplained.* This is a parser artifact — the original paper almost certainly says "Pose Estimation Failure." The 31% figure is documented in the pipeline breakdown, and it is reasonable to accept that hand-pose estimation fails on a fraction of in-the-wild frames. **Removed: parser artifact.**
- *Criticism about the "L eye" notation being a clarity problem.* This is a parser corruption of "L_cycle" (cycle-consistency loss), which is defined in Section 4.3 and Equation 7. **Removed: parser artifact.**
- *Complaint about 10 users being too small for perceptual score.* While the sample is small, this is a common practice in HOI generation papers for supplemental qualitative validation. The metric is ancillary to the main quantitative evaluation. **Removed: field-standard practice.**
- *Demand to release the WildO2 dataset.* Questions about release status or availability of any cited entity must be removed per hard rules. **Removed: hard rule.**
- *Criticism about not comparing with more baselines from Zhang et al. 2025a;b.* The paper cites these as concurrent work with different goals (LLM-based grasping). The paper's claim that no existing method handles this specific task is plausible and the baselines chosen are representative of the closest prior work. However, the limitation on the number of baselines is kept as a Major weakness (weakness #1) because more adaptation effort would strengthen the evaluation. **Partially removed from its harsh framing; kept in weakened form as Major weakness #1.**
- *Complaint about P-FID not being standard for HOI generation.* P-FID is a point-cloud adaptation of FID (Nichol et al., 2022), a standard metric for generative quality. Its use is reasonable. **Removed: not a genuine weakness.**
- *Strength Finder's generic claims about "important problem" and "timely task."* These are generic and lack specific evidence. **Removed.**
- *Strength Finder's claim about the method being "superior" — the evidence is Table 1, which is already covered.* **Merged with strength #4 above.**

## Novel Insights

None beyond the paper's own contributions. The key insight that the harsh and strength reviews converge on is: the paper's main strengths are its novel task framing and dataset pipeline, which are genuine contributions, but the evaluation — particularly around semantic controllability and baseline breadth — does not yet match the ambition of the claims. The method's three-stage design is reasonable and the ablations are helpful, but the lack of error bars and thin semantic evaluation are the chief evidential gaps.

## Suggestions

1. **Add at least one more adapted baseline** from recent text-conditioned HOI work (e.g., Zhang et al. 2025a;b or Yang et al. 2024a;b, if publicly available) to strengthen the comparison.
2. **Report standard deviations** over at least 3 runs for all metrics in Tables 1 and 2.
3. **Provide a direct semantic controllability benchmark:** fixed object + coarse action, varying only the hand-part specification in the DSC, and measure hand-part contact accuracy against the instruction.
4. **Describe the P-FID computation, VLM prompt, and user-study protocol** with sufficient detail for reproducibility.
5. **Compute quantitative metrics on a held-out Objaverse set** with human-verified ground truth to substantiate the out-of-domain generalization claim.

## Score and Decision

### Calibration anchors considered

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| HOI-Diff (ZYwLfi50GI) | 5.25 | Similar topic (text-driven HOI synthesis), but TOUCH is stronger — has a novel dataset, more comprehensive evaluation, and clearly better results. |
| IHDiff (nTNElfN4O5) | 5.50 | Both use diffusion for hand-related generation. TOUCH has broader task scope and stronger dataset contribution. |
| Interactive-Action (OWIk5E4lJs) | 5.20 | Addresses interaction generation in a different domain (2D images). TOUCH has stronger technical contributions. |
| EgoHOI (M8gXSFGkn2) | 7.00 | Different task (HOI understanding vs. generation). Comparable in evaluation thoroughness but EgoHOI has a cleaner evaluation setup. |
| CyberHost (vaEPihQsAA) | 7.60 | Generation paper in a different domain. TOUCH is less polished in evaluation but has a novel dataset contribution. |
| IC-Light (u1cQYxRI1H) | 10.00 | Exceptional paper with extremely strong results. TOUCH does not reach this level. |
| FHA-Kitchens (otoggKnn0A) | 4.00 | Hand action dataset paper. TOUCH is significantly stronger in method and evaluation. |
| 3D Hand Pose (96jZFqM5E0) | 6.67 | Hand pose estimation pre-training. TOUCH has stronger architectural novelty. |

TOUCH is clearly stronger than HOI-Diff (5.25) and IHDiff (5.50), comparable to or slightly below EgoHOI (7.00) in evaluation rigor, and substantially below exceptional papers like IC-Light (10.00). The paper's genuine contributions (new task, dataset pipeline, multi-level conditioning) are offset by evidential gaps in the evaluation (limited baselines, no error bars, thin semantic controllability evidence).

**Score:** 6.5  
**Decision:** Accept

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>