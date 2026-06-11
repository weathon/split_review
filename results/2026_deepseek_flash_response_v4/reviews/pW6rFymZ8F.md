## Summary

EmbodiedMAE proposes a multi-modal masked autoencoder that jointly learns representations across RGB, depth, and point cloud for robot manipulation. It introduces DROID-3D, a processed version of the DROID dataset with temporally consistent depth and point clouds from ZED SDK (76K trajectories, 350 hours). The model is pre-trained at ViT-Giant scale on DROID-3D and distilled to smaller variants. Evaluations span 70 simulation tasks (LIBERO, MetaWorld) and 20 real-world tasks on two robot platforms (SO100, xArm).

## Strengths

- **DROID-3D dataset is a genuine resource contribution.** The paper processes all 76K trajectories of DROID using ZED SDK with temporal fusion and AI-augmented enhancement, in contrast to prior work (SPA) that processed ~1/15 of the dataset with CrocoV2-Stereo depth estimation known to lack temporal consistency. This is explicitly documented in Section 2.1 and represents a substantial engineering effort.

- **Re-coloring diagnostic reveals emergent semantic understanding without segmentation supervision.** Section 3.2 (Figure 3, column 12) shows that when an altered RGB patch is injected during depth-to-RGB reconstruction, only the corresponding object (table) adopts the modified color while surrounding elements (background, robot, cup) remain unchanged. This provides direct qualitative evidence of implicit object-level semantic understanding from the multi-modal MAE objective.

- **Modality-shared decoder reducing computational cost by ~3×.** The decoder design (Section 2.3) shares transformer components across modalities via cross-attention for explicit fusion, reducing computational cost by approximately a factor of three compared to separate per-modality decoders—a concrete architectural contribution.

- **Comprehensive evaluation breadth.** The paper evaluates across 70 simulation tasks (40 LIBERO + 30 MetaWorld) and 20 real-world tasks on two distinct robot platforms (SO100 low-cost, xArm high-performance), using two different policy architectures (RDT and ACT). Tables 2-3 show EmbodiedMAE representations transfer to ACT with consistent improvements (83.7 vs 76.3 on LIBERO-Goal RGB, 90.8 vs 82.2 for RGBD), demonstrating generalization beyond a single policy class.

## Weaknesses

### Major

- **The distillation ablation undermines the claimed contribution of the MAE reconstruction loss.** Section 3.5 reports that masking ratios ≥ 100% (i.e., using *only* the feature alignment loss, eliminating the MAE reconstruction loss entirely) perform better than any configuration that includes the MAE loss. The paper claims "mask autoencoding provides additional benefits," but the data shows the opposite—the best configuration removes the MAE loss. If pure distillation from the Giant model outperforms any mixture with MAE reconstruction, it is unclear what the multi-modal MAE pre-training contributes beyond a simpler distillation pipeline. This weakness directly undercuts a central claim of the method.

- **Multi-modal comparisons are structurally unfair, conflating architecture benefit with pre-training benefit.** The multi-modal results (Finding 3, Section 3.3) compare EmbodiedMAE—a model designed and pre-trained specifically for multi-modal input—against DINOv2-RGBD, which is DINOv2 with an ad-hoc trainable depth branch that was never pre-trained on multi-modal data. The paper presents DINOv2-RGBD's degradation as evidence for EmbodiedMAE's multi-modal superiority. However, this conflates the benefit of having a multi-modal architecture with the benefit of EmbodiedMAE's specific pre-training design. MultiMAE (Bachmann et al., 2022), which the paper cites but never evaluates as a baseline, would be a natural comparator. Without it, the claim that "EmbodiedMAE promotes policy learning from 3D input" (Finding 3) cannot be attributed to the proposed method's specific design choices.

- **No ablation of the pre-training itself.** The paper does not ablate the pre-training phase—no RGB-only MAE on DROID-3D, no random initialization baseline, no comparison with a different pre-training objective. Section 3.5 attributes this to the prohibitive cost of ViT-Giant pre-training. This means the central claim about the value of multi-modal pre-training is not directly supported by any controlled experiment; it relies entirely on comparing the full pipeline against baselines that lack any DROID-3D pre-training at all. The contribution of the DROID-3D data, the multi-modal objective, and the architecture cannot be disentangled.

### Minor

- **Initialization contradiction.** Section 2.2 states "This design choice allows us to initialize the ViT directly from DINOv2 pre-trained weights," while Section 2.4 says "we first train a ViT-Giant EmbodiedMAE model **from scratch** on the DROID-3D dataset." These are incompatible. If DINOv2 initialization is used, the reported gains over DINOv2 could partly reflect additional in-domain training on DROID-3D rather than the multi-modal MAE objective. This needs clarification.

- **No error bars or variance reporting.** Despite noting 150 trials per LIBERO task (Figure 6 caption) and 10 trials per real-world task (Figure 8 caption), no standard deviations or confidence intervals are reported for any result. The modest RGB-only gains on MetaWorld (EmbodiedMAE 73.0% vs DINOv2 70.7%—a 2.3 point difference, and a tie with SPA at 73.0%) could fall within evaluation noise.

- **No quantitative evaluation of DROID-3D depth quality.** Figure 2 shows only qualitative comparisons. No metrics (e.g., absolute relative error, RMSE, temporal consistency) against alternatives like CrocoV2-Stereo (used by SPA) are provided.

- **Abstract oversells RGB-only results.** On MetaWorld (Table 1), EmbodiedMAE RGB (73.0%) ties with SPA (73.0%) and is 2.3 points ahead of DINOv2 (70.7%). The abstract's "consistently outperforms state-of-the-art vision foundation models" language is overstated for the RGB-only setting where margins are small and a strong baseline is matched rather than outperformed.

### Trivial

- The "scaled-down RDT" policy used for evaluation is not clearly specified beyond "approximately 40M parameters"; architectural details relative to the full RDT are not given in the main text.

## Nice-to-Haves

- Including a proper multi-modal pre-trained baseline (e.g., MultiMAE or an RGBD variant of the same architecture trained with an alternative objective) would substantially strengthen the multi-modal comparisons.
- Quantitative depth quality metrics for DROID-3D vs. alternatives would strengthen the dataset contribution.
- A controlled pre-training ablation at a smaller scale (e.g., Base or Large) comparing RGB-only MAE on DROID-3D vs. multi-modal MAE on DROID-3D would directly test the core claim.

## Removed Points

- **Weakness about missing related works**: Not included per instruction (cannot verify externally).
- **Weakness about "no quantitative evaluation of DROID depth quality"** being presented as fatal: Demoted to minor. It's a useful addition but not central to the paper's claims.
- **Strength about "controlled comparison showing naive depth fusion degrades"** (from Strength Finder #4): Removed. The comparison is structurally unfair and the strength overstates what it demonstrates—it shows that DINOv2 with an ad-hoc depth adapter performs worse, which is expected, not that EmbodiedMAE's multi-modal design is validated.
- **Various formatting nitpicks and speculation** (e.g., "the appendix may specify X but…"): Removed as speculative or parser artifacts.
- **Pure formatting/style nitpicks**: Removed per instruction.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the MAE ablation contradiction**: If the MAE loss does not help during distillation (as the 100% masking result suggests), the paper should either (a) revise its claims about the method's contribution or (b) provide evidence that the MAE loss is important at the Giant pre-training stage (which distillation alone doesn't test).
2. **Add a multi-modal pre-trained baseline**: At minimum compare against MultiMAE, or train an RGBD variant of the same architecture with an alternative pre-training objective, to support the claim of multi-modal superiority.
3. **Report confidence intervals or standard deviations** across evaluation trials, especially given the modest margins in some settings.
4. **Clarify the initialization**: Is the Giant model initialized from DINOv2-g weights or trained from random initialization? If the former, rephrase "from scratch" and add an ablation controlling for additional in-domain training on DROID-3D.
5. **Add at least one controlled pre-training ablation** at a smaller model scale (Base or Large) comparing multi-modal vs. single-modal MAE on DROID-3D.
6. **Tone down the abstract's claims** to accurately reflect the RGB-only results, where gains over strong baselines like DINOv2 and SPA are modest.

## Calibration Anchors

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/FMsmo01TaI.md (M3L) | 4.33 | R2 | Weaker: only 3 simulated tasks, no real-world, no dataset contribution |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/NxoFmGgWC9.md (GR-1) | 5.50 | R1/R2 | Comparable: GR-1 had stronger relative gains but narrower evaluation; EmbodiedMAE has broader evaluation but weaker support for core claims |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/IsGsv8qEHp.md (Human-oriented Rep) | 5.00 | R1/R2 | Comparable: both have representation learning for robotics; EmbodiedMAE has more comprehensive evaluation but also more significant methodological weaknesses |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/VYOe2eBQeh.md (LAPA) | 5.83 | R2 | Stronger: clearer contribution, more rigorous evaluation, despite having data consistency concerns |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/9GKMCecZ7c.md (Generalist Policy) | 3.40 | R1 | Weaker: simulation only, narrower scope |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/sXF5P4N7e8.md | 3.00 | R1 | Weaker: different topic (goal-conditioned masking) |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/1CIUkpoata.md | 6.00 | R1 | Different topic (6D pose tracking) |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/k5VHHgsRbi.md (MME-RealWorld) | 6.80 | R2 | Different topic (MLLM evaluation) |

**Round 1 bracket:** [4.5, 5.5] — determined by comparing against weak anchors (~3.0), middle anchors (3.5–6.5), and strong anchors (>6.5).

**Round 2 narrowing:** After reading M3L (4.33), GR-1 (5.50), Human-oriented Rep (5.00), and LAPA (5.83) in full, the paper's evaluation issues (MAE ablation undermines the core claim, unfair multi-modal comparisons) place it below GR-1 (5.50). It is comparable to the Human-oriented paper (5.00) which had similar strengths and weaknesses. Score set at 5.0.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>