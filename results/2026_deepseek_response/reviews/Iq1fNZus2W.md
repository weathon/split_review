Now let me write the final consolidated review.

## Summary

The paper introduces Patch-wise and Keyword-Aware Attention (PKA), a framework that decomposes the expensive full-attention in multi-condition Diffusion Transformers into two specialized efficient modules: Position-Aligned Attention (PAA) for pixel-aligned spatial conditions (one-to-one attention between aligned patches) and Keyword-Scoped Attention (KSA) for subject conditions (masked attention confined to keyword-relevant regions via a lightweight relevance map). An early-timestep sampling strategy for faster fine-tuning is also proposed. Experiments on FLUX.1 demonstrate up to 10× inference speedup and 5.12× VRAM reduction while maintaining or improving generation quality across multi-condition tasks.

## Strengths

1. **Large, clearly demonstrated efficiency gains**: Figures 7 and 8 show PKA scaling near-flat with condition count while baseline methods grow quadratically, achieving up to 10× speedup and 5.12× VRAM reduction at 16 conditions. These claims are well-supported by quantitative plots with explicit measurements.

2. **Strong empirical motivation for the architectural design**: Figures 2 and 3 provide concrete evidence that spatial-condition attention is concentrated along the diagonal and subject-condition attention is localized to keyword-relevant regions. This directly motivates PAA and KSA before introducing them, making the design rationale transparent.

3. **Generative quality maintained or improved despite efficiency gains**: Table 1 reports that PKA achieves the best FID (52.99 vs. 61.03/72.03), SSIM, CLIP-I, and DINOv2 on Subject-Canny and Subject-Depth tasks, outperforming both OminiControl2 and UniCombine. This demonstrates that the large efficiency gains do not come at a quality cost.

4. **PAA reduces complexity from O(N²) to O(N)**: The design is clearly formalized in Eq. 2 and validated in Figure 9, where PAA (13.63s, 237MB) outperforms full attention (15.38s, 308MB) and all sliding-window variants in both speed and memory.

## Weaknesses

### Major

1. **Baseline comparison fairness is not adequately documented.** The paper states "To ensure a fair comparison, we fine-tune the FLUX.1 model using LoRA" (line 197), but does not clarify whether OminiControl2 and UniCombine were also fine-tuned under identical conditions (same training data, LoRA rank, iterations, optimizer) or whether their pre-trained checkpoints were used as-is. If the baselines were not retrained on the same data, the quality differences in Table 1 could partly reflect differences in training procedure rather than architectural advantage. This is a significant documentation gap for a central claim.

2. **Missing quantitative ablations for PAA and KSA.** Figures 9 and 10 provide only qualitative image comparisons with latency/VRAM numbers. No FID, SSIM, CLIP-I, or DINOv2 scores are reported for the ablation variants. For PAA, this makes it impossible to assess whether the one-to-one attention degrades image quality relative to full attention or SWA. For KSA, the efficiency-fidelity trade-off across different ε values is shown only qualitatively. This weakens the rigor of the ablation story.

3. **Early-timestep sampling claim is under-supported.** The paper claims this strategy "accelerates convergence and enhances control fidelity" (line 302) but provides only a single qualitative example (Figure 11) with no FID, CLIP-I, or any benchmark metric on the main evaluation tasks. The perturbation analysis in Figure 5 plausibly motivates the idea but does not demonstrate that the shifted logit-normal distribution produces a measurably better or faster-trained model. This claimed contribution lacks sufficient quantitative support.

### Minor

1. **KSA mask temporal consistency assumption is unexamined.** The paper reuses mask M_t at timestep t+1 based on "temporal consistency" (Section 3.2.2) but provides no analysis of how often the mask remains valid across consecutive denoising steps. At early steps when the image is very noisy, subject locations could shift, potentially propagating errors. A simple IoU analysis over timesteps would validate this design choice.

2. **Dataset and keyword extraction details are underspecified.** The paper uses "a subset from the Subject200K dataset" without stating its size or composition. KSA relies on "textual keyword" tokens (line 124), but how these are extracted (automatically or manually annotated) is not described, affecting reproducibility.

3. **"w/o KSA, equivalent to ε=0" claim is slightly misleading** (Section 4.3.2, line 296). In Figure 10, "w/o KSA" has 16.99s/368MB while ε=0.2 has 15.33s/280MB. The large gap (368→280 MB going from ε=0 to ε=0.2) suggests w/o KSA reverts to full attention (a structurally different mechanism), not just KSA with threshold 0. This should be clarified.

### Trivial

None.

## Nice-to-Haves

- Provide confidence intervals or variance estimates for the main metrics in Table 1.
- Add a quantitative analysis of KSA mask IoU over consecutive denoising steps.
- Clarify what "condition overhead" refers to in the evaluation setup.
- Acknowledge that PAA is designed for pixel-aligned conditions and may not directly apply to non-aligned conditions (e.g., layout boxes, keypoints).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticisms about missing appendix content / references**: Removed per instructions — the parser strips these sections; they exist in the original submission.
- **Formatting nitpicks, typos, punctuation, parser artifacts**: Removed per instructions — these are parser errors, not author errors.
- **"This method may not generalize to other frameworks"**: Removed — speculative; the paper targets the specific use case it evaluates and does not claim universal applicability beyond its scope.
- **Strength Finder generic strengths** (e.g., "this paper addresses an important problem"): Removed — too generic to be informative as a specific strength.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- **Clarify the baseline training setup**: Explicitly state whether OminiControl2 and UniCombine were fine-tuned on the same data with identical LoRA hyperparameters, or whether their released checkpoints were used directly. If the latter, add a caveat about the comparison.
- **Add quantitative metrics for ablations**: Report FID, SSIM, CLIP-I, and DINOv2 scores for the PAA and KSA ablation variants in Figures 9 and 10.
- **Either validate early-timestep sampling quantitatively** on the benchmark tasks from Table 1, or soften the claim and downgrade it from a core contribution.
- **Describe the dataset subset size** and the keyword extraction process for reproducibility.

## Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/2o58Mbqkd2.md | 3.25 | 1 (weak) | Superposition of Diffusion Models — less related topic, weak anchor |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/Jt1gGIumJo.md | 3.00 | 1 (weak) | Highlight Diffusion — training-free acceleration, very modest speedup (1.52×), weaker evaluation |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/PiHGrTTnvb.md | 3.00 | 1 (weak) | Not comparable topic |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/rnTb9dm9zx.md | 3.00 | 1 (weak) | Not comparable topic |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/kALZASidYe.md | 3.75 | 1 (mid) | Controllability of DMs — less relevant topic |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/uJqKf24HGN.md | 7.00 | 1 (mid) | UniCon — similar DiT control topic, well-documented experiments, clean ablation studies. PKA has larger efficiency gains but weaker documentation. **PKA is slightly weaker than this anchor.** |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/lWGXftRS5h.md | 5.00 | 1 (mid) | Inductive biases in DiTs — less comparable methodology |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/D2as3jDmRA.md | 6.25 | 1 (mid) | LinFusion — linear attention for efficient DiT, similar efficiency motivation, comprehensive experiments. **PKA is roughly comparable but with cleaner motivation.** |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/fV0t65OBUu.md | 8.00 | 1 (strong) | Probabilistic diffusion models — strong theoretical paper, not comparable |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/gU58d5QeGv.md | 8.00 | 1 (strong) | Würstchen — major architecture work, not comparable |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/OvoCm1gGhN.md | 8.00 | 1 (strong) | Differential Transformer — not comparable topic |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/zMoNrajk2X.md | 8.00 | 1 (strong) | CADS — not comparable topic |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/taHwqSrbrb.md | 5.50 | 2 (narrow) | DyDiT — dynamic DiT computation, 1.73× speedup. PKA has larger gains (10×), cleaner motivation (attention sparsity analysis), but weaker documentation. **PKA is slightly stronger than DyDiT.** |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/vNZIePda08.md | 4.75 | 2 (narrow) | Sparse-to-sparse training — less comparable |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/leBbjaUxut.md | 5.00 | 2 (narrow) | Multi-scale DiT — speedup through architecture, less comparable |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/lTrrnNdkOX.md | 6.40 | 2 (narrow) | Qihoo-T2X / PT-DiT — proxy-tokenized DiT, similar efficiency theme. Stronger evaluation (multiple tasks, multiple resolutions) but addresses a different problem (general DiT efficiency vs. multi-condition control). **PKA is slightly weaker than this anchor due to documentation gaps.** |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/MbM1BqGpZu.md | 6.75 | 2 (narrow) | Not comparable (theory paper) |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/qmXedvwrT1.md | 6.67 | 2 (narrow) | LEGO bricks — not comparable |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/qae04YACHs.md | 6.33 | 2 (narrow) | Not comparable (time series) |

**Round 1 bracket:** The paper sits clearly above the weak anchors (3.0–3.75) and below the strong 8.0 anchors, placing it between roughly 4 and 7.

**Round 2 narrowing:** Compared to DyDiT (5.50), PKA has a cleaner motivation story (attention sparsity analysis → specialized modules), larger efficiency gains (10× vs 1.73×), and maintains quality on a practical multi-condition task — but DyDiT's evaluation is more rigorous with thorough ablations. Compared to PT-DiT / Qihoo-T2X (6.40), PKA solves a more specific underexplored problem (multi-condition control efficiency rather than general DiT redundancy) with a more targeted design, but PT-DiT's evaluation is broader and better-documented. **PKA sits between DyDiT and PT-DiT, closer to PT-DiT, at approximately 6.0.**

**Score rationale (6.0):** The paper has a genuinely useful, well-motivated core contribution (PKA), large efficiency gains convincingly demonstrated, and quality maintained on benchmark tasks. However, three significant gaps prevent it from reaching a higher score: (1) insufficient documentation of baseline training conditions for the main quality comparison, (2) missing quantitative metrics in the ablation studies, and (3) the early-timestep sampling claim lacks quantitative validation. These are addressable with additional experiments and clarifications, not fundamental invalidations.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>