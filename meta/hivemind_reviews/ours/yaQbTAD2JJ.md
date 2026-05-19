## Summary
The paper presents Cube-LLM, a multi-modal LLM trained on a large unified 2D+3D dataset (LV3D) to perform 3D-grounded reasoning from images without any 3D-specific architectural changes. The approach combines data scaling (compiling 15 datasets into 40.9M QA pairs), task decomposition (breaking 3D labels into easier sub-tasks), and visual chain-of-thought (VCoT) prompting. Experiments show strong gains on outdoor benchmarks (Talk2Car, DriveLM) and competitive results on indoor 3D and standard 2D MLLM benchmarks.

## Strengths
1. **Large-scale unified 2D+3D pretraining dataset (LV3D)**: The paper compiles 15 datasets (9.6M images, 40.9M QA pairs) into a standardized format with consistent camera intrinsics and 2D→3D coordinate relationships (Table 1). This is a substantial engineering contribution that enables future work on 3D-capable MLLMs.

2. **Clean Talk2Car results show genuine 3D grounding**: Cube-LLM (camera-only) achieves 46.3 BEV AP_A and 34.7 3D AP_A on Talk2Car, and with CenterPoint proposals reaches 71.4 BEV AP_A — outperforming the prior SOTA MSSG (50.1) by 21.3 points (Table 2). Critically, Talk2Car is **not** in the LV3D pretraining mixture (verified from Table 1), so these gains are not attributable to data contamination. This is the paper's strongest result.

3. **Controlled ablation on DriveLM shows 2D data alone transfers**: Table 3 shows Cube-LLM with LV3D (2D only, no nuScenes) reaches 50.5 BEV AP_A vs. LLaVA-1.5's 33.2 — a clean 17.3-point improvement from 2D pretraining alone, demonstrating genuine cross-task transfer.

4. **Visual chain-of-thought improves 3D reasoning**: Table 7 provides a clean within-model ablation showing VCoT improves BEV AP_A from 43.6 to 46.3 on Talk2Car (+2.7) and 3D AP_A from 32.7 to 34.7 (+2.0). This validates the claimed emergent LLM-like property.

5. **3D capability does not degrade 2D performance**: Cube-LLM achieves SOTA 87.0 average on refCOCO/+/g among 7B generalist models (Table 5) and competitive scores on VQAv2, GQA, SQA, POPE (Table 8). This supports the claim that 3D reasoning is an expansion, not a trade-off.

6. **Specialist prompting is flexible and effective**: The model can incorporate external detector proposals (e.g., CenterPoint) at inference without retraining, achieving dramatic gains (+25.1 BEV AP_A on Talk2Car). This is a practical advantage.

## Weaknesses
### Fatal

None.

### Major

- **DriveLM-Grounding results partially confounded by pretraining data overlap**: The LV3D pretraining mixture includes nuScenes (Table 1), and DriveLM-Grounding is constructed by associating DriveLM 2D boxes with nuScenes 3D boxes (lines 264–266). The full-LV3D model therefore sees nuScenes images and 3D labels during pretraining and again during DriveLM fine-tuning. The jump from LV3D (2D) at 50.5 to full LV3D at 66.0 (Table 3) is the most impressive part of the DriveLM results, but it conflates the effect of pretraining on generic 3D data with direct exposure to the same scene-level 3D distribution. The 2D-only baseline (50.5) is clean and already strong, but without an ablation that pretrains on non-nuScenes 3D data, the marginal benefit of "3D pretraining" for DriveLM cannot be cleanly attributed to general 3D understanding vs. dataset familiarity.

### Minor

- **Missing DINOv2 vs. CLIP ablation**: The paper replaces CLIP with DINOv2, claiming "minimal degradation in the standard visual language model benchmarks while significantly improving 3D-related tasks" (line 194). No direct comparison is shown. Since DINOv2 is not text-aligned, its impact on VLM benchmarks is non-obvious. A simple ablation (Cube-LLM with CLIP vs. DINOv2 on the same recipe for Talk2Car and VQAv2) would cleanly substantiate this claim.

- **"Pure data scaling" claim overstates the method**: The paper titles itself around "pure data scaling" enabling 3D understanding, but the actual method includes substantial task engineering: (a) label decomposition into sub-tasks (Sec. 3.2), (b) visual chain-of-thought prompting (Sec. 3.3), and (c) multi-stage training (low-res then high-res). These are all deliberate design choices beyond simply "adding data." The paper would benefit from acknowledging this tension and clarifying which components are essential vs. incidental.

- **refCOCO SOTA claim lacks context on training data overlap**: Cube-LLM achieves 87.0 average on refCOCO/+/g (Table 5) — SOTA among 7B models. However, refCOCO is in the LV3D pretraining mixture (Table 1). While most competing generalist models (Shikra, Ferret, Qwen-VL) also train on refCOCO, the paper does not clarify which competitors' training protocols include refCOCO data and at what stage. This makes the "state-of-the-art" claim harder to contextualize fairly.

### Trivial

- The caption for Table 4 refers to "Inodoor" (typo).

## Suggestions
1. **Address the DriveLM/nuScenes overlap directly**: Pretrain Cube-LLM on a variant of LV3D that excludes nuScenes (and any other dataset whose test distribution overlaps with evaluation benchmarks), then fine-tune on DriveLM-Grounding. Show the degradation from the full-LV3D setting. If this is infeasible, explicitly quantify the overlap and discuss its impact.

2. **Add a DINOv2 vs. CLIP ablation**: Train Cube-LLM with CLIP on the same recipe and report results on at least Talk2Car (3D) and VQAv2 (2D). This cleanly validates the visual encoder choice.

3. **Clarify the "data scaling" thesis**: Acknowledge that task decomposition and VCoT are deliberate engineering choices that go beyond "pure data scaling." Report results from a variant without task decomposition to show how much these design decisions contribute.

4. **For refCOCO, add a footnote**: State which competitors used refCOCO data and during which training stage (pretraining vs. fine-tuning), so the SOTA claim can be properly contextualized.

## Score and Decision

The paper makes a solid empirical contribution (LV3D dataset, strong Talk2Car results, VCoT, specialist prompting) with a clean evaluation on its primary benchmark. The main concern — partial data overlap for DriveLM-Grounding — is partially mitigated by the 2D-only control. The missing DINOv2 ablation and overstated "pure data scaling" framing are addressable in revision. The paper is above the acceptance threshold.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

## Questions


## Decision
Accept
