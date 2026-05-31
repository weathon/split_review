## Summary

SpatialBoost proposes a framework to inject 3D spatial knowledge into pre-trained vision encoders by converting geometric information (extracted via off-the-shelf depth/segmentation/3D reconstruction models) into linguistic descriptions and using an LLM to supervise fine-tuning. The method features (1) a multi-turn Chain-of-Thought VQA dataset at pixel→object→scene levels, and (2) a dual-channel attention mechanism to preserve pre-trained knowledge while incorporating spatial information. Experiments span depth estimation, segmentation, 3D scene understanding (Lexicon3D), robot learning (CortexBench), classification, and retrieval across multiple encoders (OpenCLIP, SigLIPv2, DINOv2, DINOv3).

## Strengths

1. **Consistent gains across diverse tasks and backbones.** SpatialBoost improves nearly every evaluated metric across 8+ benchmarks and 4 vision encoders. For example, DINOv3's SQA3D accuracy improves from 51.4% to 54.9%, NYUd depth RMSE from 0.31 to 0.25, CortexBench robot learning average from 72.8 to 80.8, and ImageNet linear probing from 88.4% to 90.2%. This breadth is strong evidence that the method injects useful spatial information without degrading general representations.

2. **Dual-channel attention preserves pre-trained knowledge.** Figure 6 shows that while full fine-tuning drops DINOv2 ImageNet accuracy from 86.3% to 79.5%, dual-channel attention maintains it at 87.6% while improving segmentation (47.7→49.2). This cleanly validates the design choice and addresses a real problem in vision encoder fine-tuning.

3. **Hierarchical multi-turn reasoning is well-designed and ablated.** The pixel→object→scene CoT order (Table 7) outperforms random or reverse order, and combining single-view and multi-view data yields the best results. This systematic ablation supports the paper's core methodological claim.

4. **LLM-based fine-tuning shows clear benefits over pixel-level alternatives.** Table 6 shows that LLM-based supervision improves all four tasks simultaneously, while linear/SAM/VGGT decoders either underperform or degrade some tasks. Though not perfectly controlled, the result directionally supports the language-as-medium thesis.

## Weaknesses

### Fatal
None.

### Major

1. **Potential training/evaluation overlap on ScanNet (Table 3).** The multi-view training data (Section 4.1) includes ScanNet (Dai et al., 2017), and the main 3D-centric evaluation (Table 3) is on the Lexicon3D benchmark built on ScanNet scenes. The paper does not explicitly confirm that training and evaluation scenes are disjoint. This is a serious concern because dramatic gains (e.g., SigLIPv2 3D mIoU from 6.9 to 54.9) could partly reflect scene-specific overfitting rather than general spatial understanding. **However**, this does not invalidate the paper: strong improvements on non-ScanNet benchmarks (NYU depth, KITTI depth, ADE20K segmentation, Pascal VOC, ImageNet, CortexBench) cannot be explained by ScanNet contamination and independently support the method's effectiveness. The authors must clarify the split design in the rebuttal — either confirm disjoint splits or re-run with controlled separation.

### Minor

1. **LLM vs. pixel-level comparison (Table 6) is not fully controlled.** The LLM training uses multi-turn QA with 300K rich samples, while the pixel-level baselines (linear depth, linear seg, SAM decoder, VGGT decoder) use simpler regression/segmentation losses. The paper does not specify whether data sizes, training iterations, or hyperparameters were matched across baselines. While the comparison directionally supports the claim, a cleaner apples-to-apples setup would strengthen confidence.

2. **Upstream model error analysis is absent.** The spatial QA pipeline uses depth estimation, segmentation, and 3D reconstruction models (Bochkovskii et al., 2024; Ravi et al., 2024; Wang et al., 2025a). Errors in these models propagate into the supervision signal. While this is common in data-generation pipelines, a brief analysis of QA correctness (e.g., human evaluation of a sample) would be helpful.

### Trivial
None.

## Nice-to-Haves
- A control experiment where the LLM is fine-tuned on non-spatial caption data of similar format to isolate the spatial contribution from the LLM's general language capabilities.
- Confidence intervals on Table 3 results (most other tables already have them or use standard protocols).
- Real-world robot evaluation beyond CortexBench simulation, though the simulation results are already meaningful.

## Removed Points
- Harsh Critic's claim that the full fine-tuning degradation "suggests the fine-tuning regime may have been too aggressive" — this is speculation about optimization choices not documented in the paper; the paper simply reports results as obtained.
- Harsh Critic's characterization of dual-channel attention as "essentially a parameter-efficient fine-tuning approach similar to existing adapter variants" — this is observationally correct but not a weakness. The paper cites the source (Hong et al., 2023a) and provides a clear rationale.
- Strength Finder's generic strengths about the problem being "important" or "well-motivated" — removed as superficial and not specific to this paper.
- Strength Finder's strength about dataset scalability (Figure 5) — a reasonable observation but a supporting detail rather than a core strength.

## Novel Insights
None beyond the paper's own contributions. The novelty of using language as a medium to inject 3D spatial knowledge into vision encoders, combined with the hierarchical CoT data design and dual-channel attention, is adequately described by the paper itself.

## Suggestions

1. **Clarify the ScanNet split issue.** Explicitly state whether training and evaluation scenes from ScanNet/Lexicon3D are disjoint in the training data. If they are, add a sentence to Section 4.1 or the Table 3 caption. If they are not, either re-run with controlled splits or provide a version of Table 3 evaluated only on scenes not seen during training.
2. **For Table 6, report data sizes and training iterations for each baseline** to make the LLM vs. pixel-level comparison interpretable.
3. **Include a small human evaluation** of the generated spatial QA pairs (e.g., 100 samples rated for correctness) to demonstrate that upstream model errors do not dominate the training signal.

## Calibration Report

**Round 1 — Bracketing:**
- Weak band (avg < 3.5): Visual Encoders for Data-Efficient Imitation Learning (2.50) — SpatialBoost is clearly much stronger.
- Middle band (3.5–7.5): SR² (5.20), GeVLM (4.50), Locality Alignment (6.00), Refining CLIP's Spatial Awareness (6.00) — SpatialBoost is comparable to the upper part of this band.
- Strong band (avg > 7.5): PhysBench (8.00), HyCoCLIP (8.00) — SpatialBoost is clearly below these.
- **→ Initial bracket: 5.5 – 6.5**

**Round 2 — Narrowing:**
- Locality Alignment (avg 6.00, Accept): Similar post-training improvement of spatial understanding in vision encoders. SpatialBoost's evaluation is broader (more tasks, more backbones) but has the ScanNet overlap concern that Locality Alignment lacks. Comparable quality overall.
- Refining CLIP's Spatial Awareness (avg 6.00, Accept): Similar spatial-awareness enhancement. Comparable level of contribution.
- GPT4RoI (avg 5.50, Reject): Lower quality; SpatialBoost is stronger.
- MERV (avg 6.00, Reject): Mixed scores; SpatialBoost is slightly better.

**Final position:** SpatialBoost is comparable to the 6.0 anchors. It has broader experimental scope than most comparable work and a clean ablation, but the ScanNet overlap concern prevents a higher score (6.5+). It is clearly above the 5.0–5.5 papers (SR², GeVLM) which have more marginal improvements.

**Score:** 6.0

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>