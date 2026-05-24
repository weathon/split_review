I now have a thorough understanding of the paper and the anchored calibration. Let me produce the final review.

## Summary

This paper introduces the task of free-form hand-object interaction (HOI) generation, moving beyond the grasp-centric paradigm that dominates prior work. The authors construct **WildO2**, a dataset of 4.4k 3D hand-object interactions with 92 intents and 610 object categories, built from internet videos via an automated O2HOI reconstruction pipeline. They propose **TOUCH**, a three-stage framework comprising: (1) CVAE-based contact map prediction, (2) a multi-level diffusion transformer with coarse-to-fine text conditioning (SSCs → DSCs), and (3) cycle-consistency-based physical refinement. Experiments on WildO2 show quantitative improvements over adapted baselines (ContactGen, Text2HOI), and ablations validate the contribution of each module.

## Strengths

1. **WildO2 dataset is a genuine contribution.** It is the first large-scale in-the-wild 3D HOI dataset covering non-grasping interactions, with 4.4k samples across 92 intents and 610 object categories, multi-level semantic annotations (SSCs + DSCs), and fine-grained 17-part hand segmentation (Section 3, Fig. 3). The semi-automated O2HOI frame-pairing pipeline provides a scalable alternative to lab-based capture.

2. **Well-motivated three-stage method architecture.** The coarse-to-fine design — contact map prediction → multi-level diffusion with FiLM + cross-attention → cycle-consistency refinement — is sensible and clearly described. The ablation study (Table 2) systematically validates each component: removing contact prediction ("✗ hoc.") drops P-IoU from 0.728→0.492, removing the multi-level structure ("✗ mul.") drops it to 0.525, and removing the refiner ("✗ refiner") causes the hand to drift away from the object.

3. **Thorough ablation study.** Table 2 covers contact prediction, refinement, cycle-consistency loss, multi-level architecture, text-level ablations (✗ T_DSC, ✗ T_SSC), and text encoder variants (CLIP, BERT, MPNet, Qwen-7B). The authors honestly note that penetration metrics can be misleading when the hand drifts away, which shows careful analysis of metric limitations.

4. **Out-of-domain generalization demonstrated.** Fig. 7 shows plausible interactions on novel Objaverse CAD models with verbs outside the primary annotation set, suggesting generalization beyond the training distribution.

5. **Force-related semantic interpretation (Section 5.4.3).** The finding that the model learns to associate "firmly"/"gently" with contact geometry (22-25% contact area difference) provides interesting evidence for semantic controllability beyond simple intent matching.

## Weaknesses

### Major

1. **Uncontrolled input-conditioning asymmetry in the main comparison (Table 1).** The baselines (ContactGen, Text2HOI) receive only coarse SSCs and the object mesh, while TOUCH additionally receives fine-grained DSCs that contain detailed hand-part and object-part contact specifications. The large gaps in Table 1 — especially P-FID (4.13 vs 15.72) and PS (8.8 vs 7.5) — are therefore partly attributable to richer input, not purely to better method design. The paper states it "augment[s] them with an optimization-based post-processing module to correct hand poses" (Section 5.2), but this does not address the input asymmetry. The ablation ✗ T_DSC (Table 2) partially mitigates this concern by showing TOUCH without DSCs still achieves competitive results (e.g., MPVPE 3.02 vs Text2HOI's 4.69), but this comparison has TTA disabled while baselines in Table 1 have post-processing. A controlled experiment where all methods receive only SSCs would be needed to attribute gains fairly. This is the paper's most consequential weakness.

2. **Evaluation ground truth is from the same reconstruction pipeline (Section 3, Section 5.1).** All metrics on WildO2 (P-IoU, P-F1, MPVPE, etc.) are computed against ground truth produced by the same O2HOI pipeline that generated the dataset (55% success rate, manual inspection). The evaluation therefore measures how well the model reproduces the outputs of a particular reconstruction algorithm rather than how well it generates *realistically plausible* interactions. The pipeline's 45% failure rate (31% "Pore Estimation Failure" — likely a parser artifact for pose/point cloud estimation — plus other failures, Fig. 3a) means the surviving 4.4k samples may carry systematic biases that both the pipeline and the model share. The qualitative comparisons to the original 2D frames (Fig. 5, I_hoi column) provide some external reference but are not quantified.

### Minor

3. **Dataset action-type breakdown not quantified.** The paper emphasizes "non-grasping actions like pushing, poking, and rotating" as a key contribution, but Fig. 3 does not quantify the proportion of such actions in the dataset. The Sankey diagram (Fig. 3b) uses broad labels like "writing, sitting, holding" that are ambiguous. The visualizations (Figs. 5, 7, 8, 9) show a mix of grasping and non-grasping interactions, but the overall distribution is unknown. Since the central framing of the paper is moving *beyond* grasping, a quantitative breakdown by action type would substantiate this claim.

4. **Qwen-7B text encoder shows only marginal gains over CLIP.** From Table 2, switching from CLIP to Qwen-7B improves P-IoU from 0.713→0.728 (+0.015) and P-FID from 4.84→4.84 (no change). The 7B-parameter model carries significant compute overhead, and its benefit over a lightweight encoder like CLIP is modest. The paper should either justify the choice or acknowledge the limited gain.

5. **Perceptual score from only 10 users (Section 5.1).** The PS metric uses ratings from 10 users with no reported inter-rater reliability or confidence intervals. Given the small test set (677 samples), this is too few evaluators for a reliable perceptual judgment.

6. **55% reconstruction success rate not analyzed.** The O2HOI pipeline succeeds on only 55% of candidate clips (Fig. 3a). The paper does not analyze what types of interactions systematically fail (e.g., high occlusion, complex object geometry, certain action types). This selection bias affects dataset representativeness and, consequently, the claims about covering "diverse daily interactions."

### Trivial

- The text encoder ablation rows in Table 2 are not clearly separated from the architecture ablation rows, making the table somewhat confusing to parse.
- The phrase "pore estimation failure" in Fig. 3a is not defined in the main text (likely a parser artifact for "pose estimation failure").

## Nice-to-Haves

- A controlled experiment where all methods (including baselines) are evaluated on SSCs-only input would cleanly resolve the comparison fairness concern.
- Human evaluation comparing generated 3D renderings against the original 2D frames for plausibility would strengthen the case that the model generalizes beyond the reconstruction pipeline's distribution.
- Statistical significance tests (e.g., confidence intervals) for Table 1 metrics given the 677-sample test set.

## Removed Points

- **Criticism about "missing related works"**: Removed per instructions — I cannot verify which related works exist or not.
- **Criticism that baselines "cannot be independently verified"**: Removed per Hard Rules — the paper cites ContactGen and Text2HOI as published works; questioning their existence is not appropriate.
- **"The method uses expensive Qwen-7B"**: This was demoted from a weakness; it's noted in Minor #4 but not as a separate weakness about runtime — the paper doesn't claim efficiency and the community norm for this type of work allows large encoders.
- **"The dataset is fragmented with few examples per category"**: This is speculative; the paper notes resampling to address long-tailed distribution, and without category-level statistics it's unclear how severe this is.
- **"Cycle-consistency loss not ablated separately from the refiner"**: The ablation does test "✗ refiner" which removes the entire refinement stage including the cycle-consistency loss. Further decomposition (cycle loss vs. architecture) would be nice-to-have but the current ablation is adequate.
- **Strength about "dataset diversity (92 intents, 610 objects)" being impressive but then noting the dataset is "fragmented"**: These are contradictory claims from different reviewers; I keep the positive assessment as the dominant framing since the paper does provide resampling to handle the long tail.
- **Several generic strengths from the Strength Finder about "addressing an important problem" and "the paper is well-structured"**: These are too generic to include; removed.
- **Criticism about "force semantics analysis uses no statistical test"**: The 22-25% contact area difference is a descriptive statistic from the dataset; a significance test would strengthen the claim but this is a minor point about an already-qualified finding.

## Novel Insights

The most interesting observation from the reviews — not fully articulated by the paper itself — is the tension between the paper's two central claims. Claim A: "TOUCH generates free-form HOI beyond grasping." Claim B: "The quantitative comparison shows TOUCH substantially outperforms grasp-centric baselines." These interact in an important way: if the baselines are fundamentally designed for grasping and the test set contains a substantial proportion of grasping-like interactions, then some of TOUCH's advantage may come from doing better on the same task (grasping) rather than from succeeding at a categorically different task (non-grasping). Conversely, if the test set is heavily skewed toward non-grasping, the baselines might be at a systematic disadvantage. The paper does not provide the per-action-type breakdown needed to disentangle these possibilities. This matters because the paper's framing hinges on a *qualitative* extension of the task scope, but the evaluation conflates task extension with in-task improvement.

## Suggestions

1. **Add a controlled comparison on SSCs only.** Run all methods (ContactGen, Text2HOI, and TOUCH) with only SSCs as text input. This directly addresses the conditioning asymmetry. Present this alongside the full comparison so readers can separate the contribution of the DSC input from the contribution of the method architecture.
2. **Quantify the action-type breakdown in the dataset.** Provide a table or figure showing what proportion of WildO2 samples correspond to grasping vs. non-grasping actions (push, poke, rotate, press, etc.). This substantiates the "free-form" claim.
3. **Analyze reconstruction failures.** Characterize which types of interactions or objects cause the 45% failure rate in the O2HOI pipeline. This is important for understanding dataset bias and the scope of the method's applicability.
4. **Report confidence intervals** for the main metrics in Table 1.

## Score and Decision

**Round 1 (Bracketing):** I queried three bands on topics similar to this paper. Weak anchors (score < 3.5) — e.g., a pose generation paper at 3.00 and a robotic grasping paper at 2.50 — were clearly weaker contributions with thin experiments. Middle anchors (3.5–7.5) included HOI-Diff (5.25, Reject) and 3D Interacting Hands Diffusion (5.50, Reject), both with comparable scope but less thorough evaluation. Strong anchors (7.5+) included TANGO (8.50, Accept) and CyberHost (7.60, Accept), which are polished papers with clean experimental chains. Initial bracket: **4.5–6.5**.

**Round 2 (Narrowing):** I queried the 5.0–6.5 and 6.5–8.0 ranges. HandCLR (6.67, Accept) and Unified Motion Language (7.00, Accept) represent well-executed papers with tightly controlled evaluations. Build-A-Scene (5.75, Accept) had comparable contribution levels but less serious evaluation concerns. HOI-Diff (5.25, Reject) and IHDiff (5.50, Reject) are the most topically similar — both tackle interaction generation with diffusion and both were rejected partly for evaluation concerns. TOUCH has stronger contributions than HOI-Diff/IHDiff (a real dataset, more thorough ablation) but shares the same class of evaluation weakness (uncontrolled comparison).

**Final positioning:** TOUCH is stronger than HOI-Diff (5.25) and IHDiff (5.50) in dataset and ablation quality, but below HandCLR (6.67) and Unified Motion Language (7.00) in evaluation rigor. The comparison fairness issue is consequential but fixable. I place this paper at **5.5**, reflecting real contributions held back by a structural evaluation weakness.

**Score: 5.5 — Decision: Reject**

The paper has genuine contributions (WildO2 dataset, well-motivated method, thorough ablation), but the primary quantitative evidence (Table 1) is confounded by input conditioning asymmetry. The central claim of superiority is not convincingly supported as written. A revision with controlled comparisons and additional external validation could substantially strengthen the paper.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>