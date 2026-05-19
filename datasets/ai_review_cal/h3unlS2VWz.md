- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5
Now I have all the information I need. Let me construct the consolidated review.

## Summary

This paper quantifies the vision capabilities of four multimodal foundation models (GPT-4o, Gemini 1.5 Pro, Claude 3.5 Sonnet, Qwen2-VL) on six standard computer vision tasks (classification, detection, segmentation, grouping, depth, surface normals) using established datasets (ImageNet, COCO, Hypersim). It introduces prompt-chaining techniques to translate dense visual prediction tasks into text-promptable sub-tasks, enabling direct comparison with specialist vision models under API constraints. The central findings are that MFMs are respectable generalists (GPT-4o tops 5/6 tasks) but lag behind specialists on every task, especially on geometric (depth, normals) vs. semantic tasks.

## Strengths

1. **Prompt chaining enables direct, metric-compatible comparison with vision specialists.** The paper decomposes dense tasks (detection, segmentation, depth, normals) into text-solvable sub-tasks (e.g., recursive grid zooming for boxes, superpixel pairwise ranking for depth) and reports standard metrics (AP, mIoU, RMSE, Spearman ρ) in Tables 2–7. This allows apples-to-apples comparison with specialist models, a step beyond prior VQA-style benchmarks.

2. **Comprehensive control baselines isolate algorithmic constraints from model capability.** The inclusion of *Oracle+Chain*, *Vision Specialist+Chain*, and *Blind Guess* baselines (Section 4, Tables 2–7) is a methodological strength. For example, Table 2 shows DETR+Chain achieves AP75 of 20.3 vs. DETR's 52.5, quantifying how much of the gap is due to the grid-zoom algorithm rather than MFM perception. This calibration is absent from prior MFM vision evaluations.

3. **Multi-model, multi-task evaluation reveals a clear semantic vs. geometric performance divide.** Evaluating four MFMs on six diverse tasks, the paper finds (and Tables 1–7 support) that all MFMs perform notably better on semantic tasks (classification, segmentation) than on geometric ones (depth, surface normals). GPT-4o leads in 5/6 tasks with a consistent margin. This finding goes beyond single-task analyses in prior work.

## Weaknesses

### Fatal

None.

### Major

1. **Small evaluation subsets with no uncertainty quantification weaken the evidence for comparative claims.** Depth and surface normal evaluations use only 100 Hypersim images; semantic segmentation uses 500 COCO images; grouping uses 100 images (lines 67–68). The paper draws comparative conclusions ("GPT-4o performs the best, getting the top position in 5 out of 6 tasks," Abstract) and characterizes performance gaps between MFMs and specialists, yet no confidence intervals, standard deviations, or any measure of uncertainty are reported anywhere in the tables. For the geometric tasks where model scores cluster closer together, it is impossible to assess whether observed differences are statistically reliable. The cost-efficiency rationale is understandable, but the absence of any error quantification is a genuine evidential gap.

2. **Object detection evaluation uses a simplified, single-instance subset with limited generalizability.** The paper filters COCO val to images containing only a single instance of each present class (1.7K examples, line 66). This removes cluttered scenes, occlusions, and overlapping objects — conditions central to the standard COCO detection challenge. The resulting numbers (Table 2) do not reflect performance on the full detection task, and the gap between MFMs and specialists could differ under more realistic conditions. The filtering is mentioned only in a parenthetical and its implications for the paper's claims about detection ability are not discussed.

### Minor

3. **Surface normal evaluation reveals systematic directional biases that are not diagnosed.** Table 7 shows all MFMs fail to achieve positive correlation on the left-right (x-axis), with the blind guess baseline also showing this bias (line 167–174). The paper acknowledges this but does not investigate whether the root cause is a genuine lack of geometric understanding or a prompt-design confound (e.g., ambiguity in the "which superpixel is more aligned with the right direction?" phrasing). Without a control experiment (e.g., synthetic rendered shapes with known normals), the claim that "MFMs have poor 3D visual understanding" on this task is less conclusive than stated — the measuring instrument itself may be flawed.

4. **Prompt sensitivity analysis is claimed but no quantitative results are presented.** Section 4.1 states "We evaluate the MFMs across various prompts to assess their sensitivity to word choice and prompt structure" (line 180) and the abstract claims "better models exhibit less sensitivity to prompt variations," but no numerical data, ablation tables, or systematic comparison across prompts are shown. The paper only states that the best prompt was selected on a validation set.

5. **In-the-wild evaluations lack quantitative results.** Section 4.1 mentions evaluating on recently posted online images to address data contamination, but only qualitative examples in Figure 7 are provided with no systematic quantitative evaluation (line 186). This is a missed opportunity to substantiate the claim of good generalization.

6. **Cost analysis section is empty.** Line 188 reads simply "Cost analysis." with no content — a truncated section. Given that cost is cited as the reason for using small subsets (line 67–68), this is a notable omission.

7. **Grouping task evaluation metric is not defined in the main text.** The paper describes the algorithm (lines 40–41) and reports results in Table 5, but does not state the evaluation metric or how ground-truth groups are obtained in the main body. The reader must infer from context, which harms reproducibility.

8. **Number of pairwise comparisons sampled for depth and normals is not reported.** Lines 47 and 49 describe sampling random pairs of superpixels for depth and normal ranking, but the sample size per image is not stated, making it impossible to assess the risk of under-sampling or the computational cost.

### Trivial

None.

## Nice-to-Haves

- A brief justification for the choice of the Zoran et al. (2015) globalization algorithm over alternatives.
- An explicit discussion of the detection filtering limitation in the Limitations section (Section 5).
- Reporting the superpixel algorithm and its parameters for reproducibility.
- Adding a synthetic test for surface normals to disentangle prompt ambiguity from model inability.

## Removed Points

These points from the inputs were flagged for removal and should be treated with caution:

- **"The abstract's tone is too confident given the limitations"** — The abstract summarizes the paper's findings. The body acknowledges limitations (Section 5). This is a stylistic judgment, not a substantive weakness.
- **"Model Soups ViT-G is not absolute SOTA"** — The paper calls it a "vision specialist," not SOTA, and it is a reasonable strong baseline for 2024 standards. The comparison still fairly shows the gap.
- **"Why direct regression not used for GPT-4o/Claude"** — The paper already addresses this: "our initial attempts showed that many MFMs fail at predicting the coordinates directly" (line 38). The information is present.
- **"Code release not available"** — The paper states code will be open-sourced (line 20). Per policy, questions about release status of cited/promised artifacts are removed.
- **Strength Finder: "Prompt sensitivity analysis correlates model quality with robustness"** — The paper merely mentions testing prompts but provides no results or data to back this claim. Since a verified weakness (#3 above) points out the absence of evidence, this claimed strength conflicts and is removed.
- **Strength Finder: "In-the-wild evaluation mitigates data contamination concerns"** — Only qualitative examples are shown, no quantitative evaluation. The claim of "good generalization" is unsubstantiated in the paper as presented.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge with the paper's self-assessment: the prompt-chaining methodology is sound and useful, the control baselines are well-designed, and the semantic-vs-geometric finding is the most informative result. The critical feedback (small samples, missing uncertainty, surface normal confound) identifies areas where the paper's evidence is weaker than its conclusions, but these observations align with the paper's own acknowledged limitations.

## Suggestions

1. **Add uncertainty quantification to all main tables.** Bootstrapped 95% confidence intervals or standard deviations over multiple evaluation runs would allow readers to assess whether observed model rankings are statistically significant. This is the single most impactful improvement.

2. **Expand the evaluation scale for geometric tasks.** Even 300 images (up from 100) for depth and normals would provide more stable estimates. The completed cost analysis (currently empty) should guide this decision.

3. **Diagnose the surface normal failure mode with a controlled experiment.** Replace the natural images with rendered 3D shapes with known ground-truth normals to distinguish whether the x-axis failure is a genuine geometric limitation or a prompt interpretation issue. Ablating "right/up/forward" language with "positive x/y/z direction" would also help.

4. **Present the prompt sensitivity analysis quantitatively.** Even a small table showing performance variance across prompt variants would substantiate the claim that "better models exhibit less sensitivity."

5. **Either complete the cost analysis section or remove it.** The cost analysis section is currently empty (line 188) — either provide concrete cost-per-task numbers or delete the placeholder.

6. **Include a frank discussion of the detection simplification** in the Limitations section, explaining how filtering to single-instance images affects the conclusions about detection capability.

7. **Define the grouping evaluation metric in the main text.** State what metric is used and how ground-truth groups are constructed.
