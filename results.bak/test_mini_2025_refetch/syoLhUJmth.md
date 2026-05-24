Now I have all the information I need. Let me write the consolidated review.

---

## Summary

This paper presents a systematic empirical investigation of different visual encoders (CLIP, DINOv2, MAE, DeiT) and their layer-wise feature distributions in Multi-modal Large Language Models (MLLMs). It finds that shallow CLIP layers benefit fine-grained tasks like grounding, and that DINOv2 — a vision-only model — outperforms CLIP on such tasks when paired with a simple MLP alignment head. Building on these observations, the paper proposes COMM (Combining CLIP and DINO with Multi-level feature Merging), which fuses multi-level features from both encoders via a learnable LLN-Layerscale mechanism. The model is evaluated on REC, REG, POPE, VQA, and captioning benchmarks, showing competitive or state-of-the-art results against published MLLM baselines.

## Strengths

1. **Systematic layer-wise analysis of visual encoders is genuinely useful.** Section 3 (Fig. 2) provides a quantitative comparison of CLIP, DINOv2, and MAE features at different depths on REC, POPE, and REG. The finding that shallow CLIP features (layer ~12) outperform deep features on fine-grained grounding tasks, while deep features excel on object hallucination benchmarks, is clearly demonstrated and practically actionable. This analysis fills a gap — most prior MLLM work simply uses the penultimate layer of CLIP without investigation.

2. **DINOv2, a vision-only model, works surprisingly well as an MLLM visual backbone.** Table 1 shows that DINOv2 with only an MLP alignment layer achieves 54.8 Avg REC vs. CLIP's 47.3 — a 7.5-point gain, despite never being trained on image-text pairs. This is a non-obvious empirical finding that challenges the assumption that CLIP or its variants are necessary for MLLMs.

3. **COMM achieves strong absolute performance on several benchmarks.** Table 2 shows COMM-7B outperforms published results for Shikra-7B and Qwen-VL-7B on all RefCOCO/+/g splits (e.g., 91.73 vs. 87.01 on RefCOCO val). Table 4 shows COMM achieves the best POPE scores on Popular (86.50) and Adversarial (84.50) splits. Table 5 shows strong captioning results (COCO CIDEr 132.7, Flickr30k 88.2). These absolute numbers demonstrate the method works well in practice.

4. **Principled ablation of multi-level feature merging strategies.** Figure 3 systematically evaluates five fusion schemes (Mean, Layerscale, LLN-Layerscale, Conv-Layerscale) for both CLIP and DINOv2, providing empirical justification for the LLN-Layerscale+MLP design used in COMM.

## Weaknesses

### Major

1. **The claimed benefit of fusing CLIP and DINO is not cleanly isolated from multi-level feature merging (MFM).** The paper's central contribution is that combining CLIP + DINO is beneficial. However, Table 1 — the controlled analysis where all models share the same training protocol — shows that COMM (72.8 Avg REC) does *not* outperform DINOv2 w/ MFM alone (73.1) on REC, and ties or barely edges ahead on POPE (83.6 vs 83.3). On COCO captioning, COMM (127.3) improves over CLIP w/ MFM (125.8) by 1.2%, and on MME Cognition the gain is larger (360.4 vs 296.6). But the paper never ablates a version where cross-encoder fusion is removed while keeping MFM for both encoders (e.g., "CLIP w/ MFM + DINO single-layer" or "CLIP w/ MFM + DINO w/ MFM without MLP alignment"). Without this, it is unclear whether the cross-encoder fusion adds value beyond what MFM already provides within each encoder individually. The REC result (where COMM is *worse* than DINOv2 w/ MFM) is particularly concerning for the core claim.

2. **No controlled comparison with a fully-trained single-encoder baseline.** The paper's main results (Tables 2–5) compare COMM's fully trained model to published Shikra and Qwen numbers. But the internal ablation (Table 1) uses only 9,400 iterations. This means there is no apples-to-apples comparison where a single-encoder CLIP or DINOv2 model is trained with the same data, steps, resolution, and LLM finetuning as COMM. The substantial gains over Shikra in Table 2 could partly reflect training differences (e.g., 336 vs 224 resolution, different data mixtures, full LLM finetuning) rather than the encoder fusion itself. A single-encoder CLIP model trained under the same conditions as COMM is needed.

3. **Increased model capacity is not controlled for.** COMM uses two ViT-Large encoders (CLIP + DINOv2) while baselines use one. This roughly doubles the visual parameter count and FLOPs. The paper does not compare against a single-encoder model with comparable total visual capacity (e.g., a single larger ViT or a deeper projection network). Some of the observed gains may reflect additional capacity rather than the specific multi-encoder fusion strategy.

### Minor

4. **No statistical significance or variance reporting.** Differences on several benchmarks are small (e.g., VQAv2 dev: 81.04 vs 79.5 for Qwen; OK-VQA: 59.18 vs 58.6). No confidence intervals or run-to-run variance are reported, making it impossible to assess whether improvements are statistically significant.

5. **Shikra REG baseline numbers appear unusually low.** Table 3 reports Shikra achieving 44.26 CIDEr on RefCOCO test-A and 75.61 on RefCOCO val. The paper states these are reproduced from the official checkpoint, but these numbers are substantially lower than what one might expect from Shikra. The paper does not explain the discrepancy or verify whether the evaluation protocol matches Shikra's original setting.

6. **Incomplete documentation of training data composition.** The claim "less training data than Qwen (3.6M vs 1.4B)" in Section 5.1 is ambiguous about whether this is total training samples or VQA-specific data; Section 5.4 clarifies "we use 0.6M and Qwen with 3.6M" for VQA data specifically. The first-stage dataset is described only as "the reorganized vision-language dataset as (Chen et al., 2023)" without sample counts per source. Full reproducibility would benefit from more precise data specifications.

### Trivial

7. The DINOv2 feature range description in Section 4 appears garbled in the extracted text (features indexed as v_2^{19} through v_2^5), likely a parser artifact. The intended range should be clearly stated.

## Nice-to-Haves

- A computational cost analysis: reporting inference throughput, GPU memory, and visual-parameter counts for COMM vs. single-encoder baselines would contextualize the trade-offs of using two ViT-Large encoders.
- Loss curves or validation performance as a function of training steps for the fully-trained model versus single-encoder counterparts.
- A limitations section discussing when the dual-encoder approach might not help (e.g., when the two encoders disagree, or on tasks where global semantic understanding suffices).

## Removed Points

These points from the input reviews were removed with brief justification:

- **"Contradictory data numbers (3.6M vs 1.4B vs 0.6M vs 3.6M)"** — The paper's two statements refer to different quantities. Section 5.1 compares total training data size (COMM vs Qwen total), while Section 5.4 compares VQA-specific data only (0.6M vs 3.6M). Not contradictory, though clarity could be improved (absorbed into Minor weakness 6).

- **"Missing related work comparisons (InternLM-XComposer, CogAgent, LLaVA-1.5, InstructBLIP)"** — Multiple related-work complaints are combined here. LLaVA and InstructBLIP are already compared in Table 4. Per instructions, missing-related-work criticisms are not included.

- **"CLIP baseline undertrained and comparison is inconsistent"** — The critic claimed inconsistency between the undertrained analysis (Table 1) and the main results (Tables 2–5). But Table 1 is an internal comparison where *all* rows share the same (short) training; the main results compare fully trained COMM to published baselines. This is standard practice. The real issue (which is retained as Major weakness 2) is the *absence* of a fully trained single-encoder control, not an inconsistency.

- **"DINOv2 only uses deep layers — inconsistent with analysis showing shallow layers help"** — The paper explicitly addresses this: Fig. 3(c,d) shows that *Mean(all)* performs worse than *Mean(19–24)* for DINOv2, meaning shallow DINOv2 features lack semantic information. The design choice is empirically motivated.

- **"Formatting/parser issues (v_2^5 garbled)"** — Moved to Trivial (weakness 7).

- **"OFA-L* is an older model"** — This is a missing-related-works type complaint about the comparison set. Per instructions, removed.

- **"COMM may not generalize across tasks with the LLN-Layerscale strategy"** — This is speculative without supporting evidence.

- **"The analysis of the introduction overstates novelty"** — Generic. The core analysis is genuinely useful even if the "first to extensively investigate" claim is debatable.

- **"Missing appendix content"** — The parser strips appendices. Per instructions, removed.

- **"DeiT details in appendix not provided"** — Same as above.

## Novel Insights

None beyond the paper's own contributions. The reviews (harsh critic and strength finder) do not surface an observation about the paper that the paper itself does not already articulate. The main missed opportunity noted across both reviews is that the paper undervalues its own analysis contribution relative to the fusion method — the layer-wise encoder study is arguably the stronger contribution, a point that both the strength finder (which lists it first) and the harsh critic (which recommends reframing around it) independently converge on.

## Suggestions

1. **Reframe the contribution** to foreground the systematic analysis of visual encoders and layer depths. The multi-level feature merging (MFM) can be presented as a natural consequence of this analysis, and the CLIP+DINO fusion as a secondary result.

2. **Provide a fully controlled ablation** where CLIP (single encoder), DINOv2 (single encoder), and COMM are each trained from scratch with the same data, steps, resolution (336), and LLM finetuning. Report whether COMM's gains over DINOv2 w/ MFM alone are consistent across tasks.

3. **Add a capacity-controlled baseline** — e.g., a single ViT-Huge encoder or a deeper projection network with roughly the same visual parameters as CLIP+DINO — to show the fusion is more than a capacity increase.

4. **Report confidence intervals** for the main benchmark results, especially where margins over baselines are small (e.g., OK-VQA: 59.18 vs 58.6).

5. **Clarify the Shikra REG baseline** — explain why the reproduced numbers (e.g., 44.26 on RefCOCO test-A) differ from what Shikra's paper reports, or verify that the evaluation protocol is identical.

6. **Report inference cost** (latency, FLOPs, memory) for COMM vs. single-encoder models to quantify the practical overhead of the dual-encoder design.

## Score and Decision

Calibration anchors used across rounds:

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| Y2RW9EVwhT.md (Eagle) | 7.20 | 1 | Much stronger — more thorough ablations, cleaner design space exploration, accepted Spotlight |
| vqgDq1uycO.md (MERV) | 6.00 | 1,2 | Similar multi-encoder approach, rejected; comparable rigor, current paper has stronger analysis but similar validation gaps |
| Uhj5OxAz7I.md (Matryoshka) | 6.00 | 1 | Cleaner experimental methodology, accepted Poster; current paper is weaker on controlled evaluation |
| bb2Cm6Xn6d.md (Intriguing Properties) | 5.50 | 1 | Analysis paper rejected for loose conclusion-method connection; current paper's findings are more actionable but method validation is weaker |
| 2jEiFTLRwX.md (VisionFuse) | 5.00 | 2 | Similar multi-encoder fusion, withdrawn; comparable in contribution strength |
| QPDbIFumQ8.md (EMMA) | 5.33 | 2 | Modest architectural contribution, rejected; similar level of contribution and rigor |
| DgaY5mDdmT.md (MLLMs Know Where to Look) | 7.00 | 2 | Clean analysis-to-method pipeline, accepted Poster; notably stronger experimental validation |
| KBSHR4h8XV.md (EF-VLA) | 3.33 | 1 | Much weaker — preliminary continual learning setup, not comparable |
| JIlIYIHMuv.md (LVLM-CL) | 2.50 | 1 | Much weaker — withdrawn paper, not comparable |

**Round 1 bracket**: 4.0–6.0. The paper is clearly above weak papers (~2.5–3.4) and below top-tier papers (~7.2+).

**Round 2 narrowing**: The paper sits between VisionFuse (5.00) and MERV (6.00), closer to VisionFuse/EMMA. The analysis contribution is genuinely valuable and raises it above pure fusion papers, but the method validation gaps (no controlled single-encoder baseline, no clean fusion ablation, capacity confound) prevent it from reaching MERV's or Matryoshka's level.

**Final score: 5.0** — The paper has a solid empirical analysis component and achieves strong absolute results, but the core claim about CLIP+DINO fusion is insufficiently isolated from confounds (MFM, model capacity, training differences). Major revisions addressing the ablation and controlled comparison issues could substantially strengthen the paper.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>