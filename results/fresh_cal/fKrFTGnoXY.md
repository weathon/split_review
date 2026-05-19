Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper proposes SD-VICL, a training-free method for visual in-context learning (V-ICL) that repurposes an off-the-shelf Stable Diffusion model. The core idea is to modify self-attention computation at inference time so that the query's features attend to the prompt image's keys and the prompt ground-truth's values (Eq. 7), explicitly injecting context between query and prompts. The method is evaluated on six diverse tasks (segmentation, detection, keypoint detection, edge detection, colorization), consistently outperforming Visual Prompting and IMProv by substantial margins — for example, 8.9% mIoU improvement on foreground segmentation and 6× reduction in MSE on keypoint detection. A second contribution is implicitly-weighted prompt ensembling (IWPE), which concatenates keys/values from multiple prompts to enable attention-weighted aggregation, outperforming uniform feature ensembling on multi-class tasks.

## Strengths

1. **Training-free repurposing of SD outperforms trained baselines across multiple tasks.** Tables 1 and 2 show the proposed method, without any fine-tuning, achieves absolute mIoU improvements of 8.9% (foreground segmentation) and 5.3% (single object detection) over Visual Prompting, and 3.2% and 7.1% over IMProv on Pascal-5i. On keypoint detection (DeepFashion), MSE is reduced by 6× and PCK improved by 7×. These are large, consistent gains across six diverse tasks, directly supporting the claim that an off-the-shelf SD model can be repurposed for V-ICL.

2. **Implicitly-weighted prompt ensembling (IWPE) provides significant gains over uniform feature ensembling.** On semantic segmentation (Cityscapes, Table 4), IWPE improves mIoU by 4.9% and accuracy by 6.8% over the single-prompt case, whereas uniform feature ensembling (SegGPT-style) yields only 0.9% and 0.9% gains. This validates that the concatenation-based attention formulation (Eq. 11) effectively weights prompts by their correspondence to the query.

3. **Extensive ablation study validates the attention formulation design.** Table 3 compares multiple Q/K/V variants ({Q_D, K_B, V_B}, {Q_C, K_B, V_B}, {Q_D, K_A, V_B}) and demonstrates that the proposed {Q_C, K_A, V_B} formulation yields the best mIoU. Figure 5 provides qualitative evidence that alternatives fail to preserve semantic correlations (e.g., focusing on color similarity instead of task structure).

4. **Practical trade-off analysis between denoising steps, prompt count, and performance.** Figure 6b shows that with five prompts, the method achieves higher mIoU at 30 denoising steps (159 sec) than the single-prompt case at 70 steps (231 sec), providing a practical insight into efficiency.

## Weaknesses

### Fatal

None.

### Major

- **Ambiguity about whether baselines used the same prompt selection protocol.** The paper states: "For all these tasks, we use the unsupervised prompt retrieval (Zhang et al., 2023) to select the candidates for the prompt images" (line 138), which chooses CLIP-based nearest neighbors of the query. It then says "For a fair comparison, we use Visual Prompting and IMProv as baselines" (line 140). However, the paper never explicitly states whether the *baselines* also used this same CLIP-based retrieval or whether they were evaluated with their default (likely random) prompt selection. If the baselines used random prompts while the proposed method used targeted CLIP-based retrieval, the reported gains could partly reflect prompt quality rather than the attention modification itself. *Why it matters: This is the single largest confound in the experimental setup. The paper's core claim that the attention re-computation drives the improvements hinges on a level playing field for prompt selection. The authors should either (a) confirm that baselines used identical prompts, (b) re-run baselines with the same retrieval, or (c) show that the method still wins with random prompts.*

### Minor

- **No justification for modifying only the upsample self-attention layers.** The method modifies self-attention in "the upsample layers of the denoising U-Net" (line 70) but does not explain why downsampling or all layers were excluded. An ablation on which layer groups are modified would strengthen the paper and reveal whether this design choice is critical. *Why it matters: A reader cannot tell if the choice is principled or heuristic.*

- **Cross-attention handling is not fully described.** The paper states it "focuses only on the self-attention computations" (line 60) and that cross-attention layers are left default, but it does not clarify what text input (null prompt? empty? unconditional embedding?) is used for the cross-attention layers that remain active. *Why it matters: For reproducibility, the full inference setup must be specified.*

- **The description of "off-the-shelf" slightly oversimplifies the pipeline's complexity.** The paper describes using an "off-the-shelf Stable Diffusion model" with "no additional training," which is technically true, but the full pipeline also requires an off-the-shelf inversion model (Huberman-Spiegelglas et al., 2024), CLIP-based prompt retrieval, and three inference-time techniques adapted from prior work (attention contrasting, swap-guidance, AdaIN). The paper transparently describes all these components, so this is not a flaw in the science, but the framing could give an overly simplistic impression of the deployment complexity. *Why it matters: Modest, but calibrating expectations helps readers assess practical applicability.*

### Trivial

None.

## Nice-to-Haves

- **Ablation of the inversion model:** The method uses a specific off-the-shelf inversion model (Huberman-Spiegelglas et al., 2024). Results with a simpler alternative (e.g., naive DDIM inversion) would clarify whether performance depends on high-quality inversion.
- **Inference time comparison to baselines:** While Fig. 6 reports the method's own timing, comparing wall-clock time to Visual Prompting (feed-forward) and IMProv would help calibrate the practical cost of the diffusion-based approach.
- **Failure case analysis:** The paper could strengthen its honesty by showing examples where the method struggles (e.g., classes absent from the prompt, resolution limits, ambiguous keypoints).

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Lack of comparison to more recent V-ICL methods" (Harsh Critic Point 3).** *Removed per hard rules: "DO NOT mention missing related works, as you do not have external sources to confirm their existence and could be making things up."* The paper compares against the two relevant methods that do not use curated/annotated data. Criticizing the absence of hypothetical newer works that the reviewer cannot name is not a valid weakness.

2. **"Missing reproducibility details (denoising steps, SD checkpoint, hyperparameters)."** *Removed per hard rules: "REMOVE weaknesses about missing appendix...The parser strips those sections from all papers."* The paper explicitly says "Please refer to the supplementary for details on datasets, evaluation metrics, and sensitivity analysis" (line 140-141) and "one set of hyperparameters that provided optimal performance" (line 141). These details live in the appendix, which was stripped during parsing.

3. **"Unsupervised prompt retrieval not described" and "CLIP model and retrieval procedure not described."** *Removed.* The paper provides a clear summary: "chooses the nearest neighbours of the query image as prompt candidates" based on "cosine similarity of CLIP's vision encoder embeddings" (lines 138-139). This is sufficient for a main paper; full details would reside in the supplementary.

4. **"FID and LPIPS may be inappropriate for colorization/edge detection."** *Removed.* The paper uses metrics standard for these tasks (FID for colorization, LPIPS for edge detection). The reviewer's suggestion of additional per-pixel metrics is a nice-to-have, not a weakness.

## Novel Insights

None beyond the paper's own contributions. The two reviews operated at different levels (the harsh critic correctly flagged the prompt-selection confound but inflated several minor issues into major concerns; the strength finder correctly identified the paper's well-supported claims). No genuinely novel synthesis emerges from combining them beyond confirming that the core contribution is strong while one experimental clarity issue needs resolution.

## Suggestions

1. **Clarify the prompt selection protocol for baselines.** In a revision or rebuttal, explicitly state: "For all methods (proposed and baselines), we use the same set of prompts retrieved via CLIP-based nearest neighbors (Zhang et al., 2023)." If this was already done, a one-sentence clarification resolves the concern. If not, re-running the baselines with the same prompts is necessary to validate the comparison.

2. **Add a brief justification for modifying only the upsample self-attention layers**, or include a small ablation showing the effect of modifying different layer groups.

3. **Specify the cross-attention text conditioning** (null prompt, empty string, unconditional embedding) used during inference, for reproducibility.

## Score and Decision

**Originality:** The paper introduces a genuinely novel approach — the first training-free V-ICL method that repurposes SD via in-place attention re-computation. The implicitly-weighted prompt ensembling is also novel. **Importance of research question:** Training-free adaptation to out-of-domain visual tasks is an important and timely problem. **Claims supported:** The core quantitative claims are strongly supported across six tasks, though one experimental ambiguity (prompt selection fairness) needs resolution. **Soundness of experiments:** Evaluation is broad (6 tasks, multiple datasets, ablations) and well-designed, except for the prompt-selection clarity issue. **Clarity of writing:** The method is clearly explained with helpful equations and figures. The motivation (Fig. 1) is effective. **Value to community:** The paper opens a new direction for training-free V-ICL and will likely inspire follow-up work.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>