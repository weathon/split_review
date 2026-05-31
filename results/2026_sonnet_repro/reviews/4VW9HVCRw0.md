Now let me do calibration searches to determine the appropriate score range.Round 1 bracket: **5.5 to 7.5**. TOUCH contributes both a new dataset and a method, outperforming comparable HOI papers. Let me narrow with round 2.Based on my reading of the full paper and calibration analysis, I can now write the consolidated review.

---

## Summary

TOUCH introduces the **Free-Form HOI Generation** task, aiming to break the grasp-centric paradigm in hand-object interaction generation. The authors construct WildO2, the first large-scale in-the-wild 3D dataset (4.4k samples from internet videos spanning 92 intents and 610 object categories), and propose a three-stage framework: a dual-branch CVAE for contact map prediction, a coarse-to-fine multi-level conditioned diffusion model for hand pose synthesis, and a cycle-consistency refinement module. TOUCH consistently outperforms two adapted baselines across contact accuracy, physical plausibility, diversity, and semantic consistency metrics.

---

## Strengths

1. **WildO2 fills a genuine community need**: The dataset explicitly includes non-grasping motions (pushing, poking, rotating) absent from lab-based datasets. The multi-level annotation system—SSC + DSC + contact maps + 17-part hand segmentation (including dorsal contact)—goes beyond coarse part divisions used in prior work (Section 3.3, Fig. 3b, 3c). The automated O2HOI pipeline's mask-transfer strategy via dense matching avoids inpainting artifacts, enabling scale.

2. **Contact-guided generation markedly improves results**: Removing both contact branch modules (✗ hoc.) drops P-IoU from 0.728 to 0.492 and P-FID from 4.84 to 5.41 (Table 2). The multi-level conditioning ablation (✗ mul.) is even more impactful: P-IoU falls to 0.525, confirming the coarse-to-fine design is central to the method's success.

3. **Cycle-consistency refinement robustly corrects pose drift**: The refiner recovers contact accuracy from 0.513 (✗ refiner) to 0.728 (Table 2), addressing the high-DOF drift problem specific to free-form, non-grasping interactions. Fig. 6 provides a clear stepwise visualization. The paper's clarification that low PD/PV without a refiner reflects hand drifting away—not physical quality—is an insightful and honest methodological point.

4. **Force-semantics mapping is concretely quantified**: The model learns to associate "firm" vs. "gentle" prompts with 22–25% larger contact areas without explicit force modeling (Section 5.4.3, Fig. 9), a non-obvious emergent behavior validated with quantitative analysis.

5. **Comprehensive ablations isolate all major design choices**: Removal of DSC/SSC text levels, different text encoders (CLIP, BERT, MPNet vs. Qwen-7B), and the cycle-consistency loss are all ablated, confirming each contributes meaningfully (Table 2).

---

## Weaknesses

### Fatal
None.

### Major

- **No per-action-type evaluation of the defining capability**: The paper's core claim is generation of diverse *non-grasping* interactions (push, press, rotate, poke). Yet Table 1 reports only aggregate metrics (P-IoU, P-FID, VLM, PS) that do not distinguish between action categories. A model that generates excellent grasps for every prompt could score well on these aggregates if the dataset skews toward grasping-adjacent behaviors after the 45% attrition through reconstruction. Without a per-intent or per-contact-type breakdown, the quantitative evidence does not directly validate the paper's central differentiating claim. This is the most important gap given what the paper promises.

- **Pipeline selection bias remains uncharacterized**: The 31% hand pose estimation failure rate (Fig. 3a) is not random—fast motions, unusual viewpoints, and heavy occlusion (characteristics of harder non-grasping interactions) are more likely to fail. The paper does not analyze whether interaction types have differential survival rates through the pipeline. If pushing, poking, or rotating fail at higher rates, the surviving 4.4k samples may underrepresent the very interactions the paper claims to model, creating a circularity between training data, model capability, and evaluation. A breakdown of reconstruction success rates by action category would directly address this.

### Minor

- **Perceptual study has only 10 annotators**: Section 5.1 specifies PS is collected from 10 users. This is too small to draw statistically reliable conclusions about perceived naturalness, particularly for the 8.8 vs. 7.5 vs. 6.3 differences in Table 1. The PS score is the most ecologically valid metric—a study with ≥50 participants would substantially strengthen this evidence.

- **VLM evaluation protocol is underspecified in the main text**: Section 5.1 mentions "VLM assisted evaluation" but does not specify which VLM, the exact prompt, or how numeric scores are computed from its outputs. Without this, the VLM column in Table 1 cannot be reproduced or verified.

- **Coarse-to-fine split location is not ablated**: The split at transformer block 4-of-8 (Eqs. 4–5) is presented as a design decision but is not ablated against alternatives (e.g., blocks 2 or 6). Since the multi-level injection design is a central contribution, ablating the split boundary would strengthen the design justification.

- **Hand-part mask initialization mechanism from DSC text is not explained**: Section 4.1 states that the hand-part mask for the CVAE input is "initialized from the fine-grained text T_DSC" without describing how contact part names in the DSC are parsed and mapped to the 17-part segmentation. This is a reproducibility gap.

### Trivial

- The out-of-domain generalization claim (Section 5.4.2) is supported by 4 qualitative examples only (Fig. 7). This is presented as evidence of "strong generalization capability," which overstates a suggestive finding.

---

## Nice-to-Haves

- **Per-action-type evaluation**: Grouping test samples by action category (push, lift, tip, rotate, press) and reporting contact accuracy and semantic consistency per group would transform the paper's central claim from plausible to demonstrated.
- **Dataset coverage analysis**: Reporting the fraction of WildO2 samples with dorsal-contact or fingertip-only interactions—cross-tabulated with action type—would characterize how well the dataset covers non-grasping modes beyond what Fig. 3c provides.
- **Quantitative generalization evaluation**: Even 50 Objaverse objects scored by VLM would substantially support the out-of-domain claim.
- **TTA contribution isolated**: An ablation disabling only TTA (while keeping the refiner) is in Table 2 as "Ours (✗ TTA)," but it would be useful to see whether the refiner itself (without TTA) already recovers most of the contact improvement, to clarify the marginal value of TTA iterations.

---

## Removed Points

*These points are flagged as removed; treat them with caution.*

- **"Baselines receive weaker post-processing"** (Harsh Critic, §Baseline comparison): Section 5.2 explicitly states: "we also augment them with an optimization-based post-processing module to correct hand poses." This is stated for both baselines. The critic's concern that the post-processing differs in tuning is speculative—the paper does not confirm this asymmetry—so it does not qualify as a verified weakness at Major severity. Downgraded to acknowledged ambiguity noted in context.

- **Distance map loss justification** (Harsh Critic, §4.2): The critic asks for justification of the distance map auxiliary loss (Eq. 6). The paper provides a rationale ("ensures precise contact by supervising the distance map from 21 hand joints to the object surface"), and this is a standard auxiliary design choice. Not a flaw.

- **Objaverse results described as "far from systematic evidence"**: Correct but this is in scope of a nice-to-have, not a major weakness. The paper explicitly frames this as a generalization example, not a systematic study.

- **Camera alignment underdetermination concern** (Harsh Critic, §3.2): The critic flags the joint optimization of K, R, t in Eq. 1 as potentially underdetermined. The paper uses a multi-phase procedure (mask IoU → Sinkhorn → edge penalty → depth + RGB) that progressively constrains the problem; this is a reasonable engineering approach and the concern is speculative without evidence of degenerate solutions in practice.

- **DSC VLM generation biases** (Harsh Critic, §3.3): Concern about VLM-generated DSCs having generic language for unusual interactions. Plausible but speculative; no concrete evidence from the paper.

- **Refiner re-training concerns** (Harsh Critic, §5.2 note about baselines not re-optimized for WildO2): This is a valid methodological note but not a flaw the authors can easily resolve without extensive re-tuning.

---

## Novel Insights

The paper's most non-obvious insight is that the CVAE contact prediction can serve as a regularizer for the high-DOF free-form interaction space: by first fixing contact regions on both hand and object surfaces, the diffusion model navigates a substantially reduced and physically constrained configuration space. This separation of "where to contact" from "how to configure the hand" is architecturally elegant and the ablation showing P-IoU drops from 0.728 to 0.492 without it provides concrete validation. A second genuine finding is the emergent force-semantic grounding—the model learns to map "firmly/gently" to contact area size purely from data, without any explicit force modeling, suggesting that contact geometry in WildO2 is sufficiently correlated with force language in the DSCs to enable this transfer.

---

## Suggestions

1. Add a per-action-category breakdown table (even on a representative subset) to directly validate the non-grasping generation claim.
2. Specify the VLM evaluation protocol (model, prompt, scoring) in the main text.
3. Expand the user study to ≥50 annotators and report confidence intervals.
4. Report reconstruction success rates broken down by action category (from Something-Something V2 category labels) to characterize pipeline selection bias.
5. Add one ablation row for an alternative coarse-to-fine split boundary to justify the block-4 design choice.

---

## Calibration Anchors

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| ZYwLfi50GI.md (HOI-Diff) | 5.25 | R1 | Text-driven HOI with diffusion; no dataset contribution, weaker baselines — TOUCH is clearly stronger |
| nTNElfN4O5.md (IHDiff) | 5.50 | R1 | Two-hand interaction prior via diffusion; no new dataset, narrower scope — TOUCH is broader |
| J4D5WVoc5g.md (ViTaM-D) | 4.50 | R1 | Dynamic HOI reconstruction with tactile; comparable complexity but less evaluation — TOUCH is stronger |
| OeH6Fdhv7q.md (TapMo) | 6.50 | R2 | Text-driven animation for skeleton-free characters; similar scale of contribution and evaluation quality — TOUCH is roughly comparable |
| kPC83HK4br.md (CHAMP) | 6.50 | R2 | Multi-hypothesis 3D pose with conformal prediction; strong technical contribution — TOUCH has similar scope |
| 1CIUkpoata.md (6D pose from internet videos) | 6.00 | R2 | Internet-video-based 3D reconstruction; comparable effort and rigor — close peer |
| YOpa6dTrpt.md (PMR dataset) | 7.00 | R2 | Large-scale benchmark with mixed reality; dataset is larger/more controlled — TOUCH's dataset is smaller but task is more novel |

**Round 1 bracket**: 5.5–7.5  
**Round 2 narrowing**: The paper sits above the rejected HOI work (5.25–5.5) due to the clear dataset contribution and comprehensive ablations. It is roughly comparable to 6.0–6.5 accepted papers. Its major gaps (no per-action evaluation, small user study) prevent it from reaching the upper end. The missing per-action breakdown is a concrete evidence gap for the paper's central claim, pulling it below TapMo/CHAMP (6.5). I set the score at **6.0** — clearly publishable, dataset and method contributions are real, but the evaluation does not fully substantiate the free-form non-grasping claim it headlines.

---

**Originality**: Moderate-to-high. Free-form HOI beyond grasping is a genuine new framing; the O2HOI pipeline and multi-level conditioning are non-trivial contributions.  
**Importance**: High. The absence of in-the-wild 3D HOI data is a recognized community bottleneck; WildO2 directly addresses it.  
**Claim support**: Moderate. Aggregate metrics show improvement, but per-action evidence is absent.  
**Experimental soundness**: Moderate. Ablations are thorough; baselines are limited and comparisons have ambiguities; user study is undersized.  
**Clarity**: Good. The pipeline and method are clearly described; the VLM evaluation protocol is the main clarity gap.  
**Community value**: High. Dataset alone is a contribution; method provides a concrete baseline.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>