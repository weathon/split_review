Now let me write the final consolidated review.

## Summary

This paper tackles the computational bottleneck of multi-condition control in Diffusion Transformers (DiTs). The authors first analyze attention patterns in existing multi-condition DiTs and find that spatial-condition attention is near-diagonal while subject-condition attention is localized. Building on this insight, they propose **Patch-wise and Keyword-Aware Attention (PKA)**, which decomposes full attention into **Position-Aligned Attention (PAA)** (O(N) one-to-one attention between aligned spatial tokens) and **Keyword-Scoped Attention (KSA)** (attention confined to keyword-relevant regions). A condition KV cache and an early-timestep sampling schedule further improve efficiency. Experiments on FLUX.1 with LoRA fine-tuning report up to 10× inference speedup and 5.12× attention VRAM reduction over full-attention baselines.

## Strengths

- **Empirically grounded motivation from attention pattern analysis**: Figures 2 and 3 directly visualize the structured sparsity in multi-condition DiT attention (near-diagonal for spatial conditions, localized for subject conditions), providing clear evidence that full attention is wasteful. This analysis drives the entire PKA design and distinguishes it from ad-hoc pruning.

- **Impressive and well-measured efficiency gains**: Figure 7 demonstrates 3.90×–10× inference speedup as conditions grow from 4 to 16, and Figure 8 shows 2.46×–5.12× VRAM reduction for the attention module relative to full attention. These are direct quantitative confirmations of the paper's central efficiency claim. The gains scale with condition count, which is precisely where the bottleneck is worst.

- **Clean architectural decomposition**: PAA (Eq. 2) reduces spatial attention from O(N²) to O(N) via a principled one-to-one alignment, and KSA (Eqs. 3–4) uses a lightweight relevance mask to prune subject-image interactions. The condition KV cache (Figure 4a) is a natural consequence of the decomposed structure. These design choices are internally coherent and well-justified.

- **Competitive quality on 2-condition tasks**: Table 1 shows PKA achieves the best FID, SSIM, CLIP-I, and DINOv2 scores across Subject-Canny, Subject-Depth, and Canny-Depth tasks, and improves on most controllability metrics. The efficiency gains do not come at the cost of worse generation on these settings.

## Weaknesses

### Major

- **Quality evaluation only at 2 conditions, while headline efficiency claims go to 16 conditions.** Table 1 and Figure 6 evaluate generation quality on three tasks, each using exactly two visual conditions (e.g., Subject+Canny). The efficiency curves in Figures 7–8 show the largest gains at 8 and 16 conditions. The paper's central claim is that PKA "maintains or improves generative quality" — but no quantitative or qualitative evaluation is offered at 4+, 8+, or 16-condition settings. It is plausible that quality degrades as more conditions compete (e.g., PAA's one-to-one alignment cannot capture inter-condition interactions between multiple spatial maps, or KSA masks from multiple subject conditions overlap). Without evidence, the core claim is only substantiated for the simplest case. This is the most critical gap.

- **Unclear whether baselines received equivalent fine-tuning.** The paper states: "We employ OminiControl2 and UniCombine as baselines for our comparative analysis" (Line 293) and separately describes fine-tuning FLUX.1 with LoRA on a Subject200K subset (Lines 288–291). It does **not** specify whether OminiControl2 and UniCombine were also fine-tuned on the same data or used as released. If the baselines were not similarly fine-tuned, the quality gap in Table 1 could reflect an additional 20k LoRA iterations rather than a benefit of PKA. Both baselines are designed for multi-condition control and would likely benefit from task-specific fine-tuning. The comparison is not controlled for training protocol.

- **Subject-Canny F1 gap is substantial and downplayed.** In Table 1, PKA achieves F1=0.414 on Subject-Canny vs. UniCombine's 0.551 — a 25% relative drop. The paper dismisses this as a "minor exception on a narrow margin" (Line 259), but 0.414 vs. 0.551 is neither minor nor narrow. This matters because PAA's one-to-one alignment may be too rigid for edge-based conditions (canny edges that fall near patch boundaries). The paper neither analyzes why this gap occurs nor discusses what types of spatial conditions PAA handles well or poorly, which weakens the claim that PAA is a general replacement for spatial attention.

### Minor

- **Early-timestep sampling is only qualitatively validated.** The perturbation analysis in Figure 5 is insightful, but the proposed logit-normal shift (μ=0.5, δ=1.5) is only demonstrated through visual comparisons in Figure 11. No quantitative metric (e.g., FID, CLIP score vs. iteration count) is reported for different (μ, δ) configurations. This secondary contribution remains suggestive rather than rigorously validated.

- **Training data subset size and composition unspecified.** The paper says "We curate a subset from the Subject200K dataset" (Line 288) without giving the size or class distribution of this subset. This omission hurts reproducibility.

- **KSA mask refresh frequency is not studied.** The mask is computed at step t and reused at step t+1, appealing to "temporal consistency" (Line 140). The paper does not study how often the mask should be refreshed or what happens when the subject shifts significantly between timesteps (common in early denoising).

### Trivial

- None.

## Nice-to-Haves

- A quantitative plot of CLIP-I/Latency across ε values for KSA would strengthen the trade-off analysis beyond the two visual examples in Figure 10.
- Ablating PAA with per-position dot-product (rather than sliding-window attention) would provide a cleaner baseline for the O(N) comparison.
- A controlled diagnostic experiment on Subject-Canny (e.g., F1 vs. canny edge density, or PAA with a small local window) would clarify whether the gap is fundamental or an artifact.

## Removed Points

- Critic's claim that "SWA-1 may not be a faithful implementation" is speculative and not verifiable from the paper. Removed.
- Critic's suggestion that the paper should add "more models" or "larger dataset" — the current model zoo and dataset size are adequate for the claims being made. Removed as scope creep.
- Strength Finder's generic strengths about "the problem being important" or "addressing a real bottleneck" — these are not specific to this paper's contribution. Removed.
- Critic's formatting/style nitpicks. Removed per instructions.
- Critic's complaint about missing appendix content — the parser strips appendices. Removed.

## Novel Insights

None beyond the paper's own contributions. The core observation — that spatial-condition attention in DiTs is near-diagonal and subject-condition attention is localized — is the paper's own contribution, not a meta-level insight from the reviews. The synthesis of these two patterns into a single efficient attention framework (PAA + KSA) is the paper's primary novel insight.

## Suggestions

1. **Evaluate quality at 4+ and 8+ conditions.** Even a single multi-condition task (e.g., Subject + Depth + Canny + Sketch) with quantitative metrics (FID, controllability scores) would dramatically strengthen the paper's central claim. This is the single most impactful addition.
2. **Clarify the baseline training protocol** explicitly. If OminiControl2 and UniCombine were fine-tuned on the same data, state this clearly. If not, either fine-tune them or restrict quality comparisons to within-family ablations (PAA vs. full attention with the same training).
3. **Address the Subject-Canny F1 gap** with analysis, not dismissal. Add a diagnostic experiment or at minimum a discussion of why this gap occurs and when practitioners should be cautious.
4. **Quantify the early-timestep sampling benefit** with FID or CLIP scores for several (μ, δ) configurations across iterations.
5. **Specify the training subset size** and composition for reproducibility.

## Score and Decision

### Anchor calibration

**Round 1 bracket**: 4.5 – 6.0

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Highlight Diffusion | Jt1gGIumJo | 3.00 | R1 | Weak paper with 1.52× speedup, limited evaluation — this paper is substantially stronger |
| UniCon | uJqKf24HGN | 7.00 | R1 | Clean evaluation, clear training protocol, accepted — this paper has stronger motivation but weaker validation |
| LinFusion | D2as3jDmRA | 6.25 | R1 | Linear attention for diffusion, comprehensive experiments — this paper has more impressive efficiency but less complete evaluation |
| DyDiT | taHwqSrbrb | 5.50 | R1/R2 | Dynamic computation for DiT efficiency, accepted — comparable topic, DyDiT has more thorough evaluation but smaller gains |

**Round 2 narrowing**: Retrieved anchors inside the bracket

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| DyDiT | taHwqSrbrb | 5.50 | R2 | Comprehensive evaluation across datasets, 1.73× speedup, accepted — this paper has larger gains but bigger evaluation gaps |
| SeerAttention | HmwneoGoy9 | 5.25 | R2 | Learned sparse attention for LLMs — similar spirit, this paper is roughly comparable in quality |
| Sparse-to-Sparse | vNZIePda08 | 4.75 | R2 | Sparse diffusion training from scratch — this paper has stronger motivation and clearer results |

**Final score determination**: The paper sits between DyDiT (5.50, accepted) and Sparse-to-Sparse (4.75, rejected). It has a stronger conceptual motivation and larger efficiency gains than either, but the evaluation gaps (quality only at 2 conditions, unclear baseline training, unaddressed F1 gap) prevent it from reaching the acceptance level of DyDiT. Compared to SeerAttention (5.25, rejected), the paper has more impressive quantitative results but less complete validation. A score of 5.0 reflects a paper with a genuinely interesting contribution and impressive efficiency numbers, held back by evaluation gaps that a major revision could plausibly address.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>