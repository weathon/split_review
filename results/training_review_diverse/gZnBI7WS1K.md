Now I have all the information I need to verify the claims. Let me produce the consolidated review.

## Summary

This paper proposes PruMerge, a training-free token reduction method for Large Multimodal Models (LMMs) that prunes and merges visual tokens by exploiting sparsity in the CLS-token attention of the visual encoder (CLIP-ViT). The method uses Interquartile Range (IQR) outlier detection to adaptively select important visual tokens, and supplements them by clustering pruned tokens with selected ones via key-similarity merging. Applied to LLaVA-1.5 and Video-LLaVA, PruMerge achieves 4–14× compression ratios. A variant, PruMerge+, adds spatial-uniform token sampling to reduce performance degradation at 4× compression.

## Strengths

- **Adaptive token selection via IQR on CLS-attention sparsity is well-motivated and empirically effective.** The paper identifies that CLS-token attention scores to visual tokens are highly sparse (Figure 2a) and uses IQR to automatically select the appropriate number of important tokens per image. The ablation (Table 4, left) shows adaptive IQR-based sampling (40 tokens = 54.00 on TextVQA) substantially outperforms both sequential (42.72) and spatial (46.85–47.42) sampling at equal token counts. This is strong evidence that the selection criterion captures genuinely informative regions.

- **Token Supplement via key-similarity clustering recovers information from pruned tokens.** The ablation (Table 3 right panel) shows that adding Token Supplement (TS) to Adaptive Important Token Selection (AITS) improves performance across all four benchmarks (e.g., MME 1221.6 → 1350.3, a +10.5% improvement), confirming that the merging step enriches representations beyond pruning alone.

- **PruMerge+ achieves a favorable compression/accuracy trade-off at 4× compression (25% tokens).** On LLaVA-1.5 (Vicuna-7B), PruMerge+ holds VQAv2 within 2.2% relative (78.5 → 76.8), improves ScienceQA (66.8 → 68.3), improves MMBench (64.3 → 64.9), and keeps MME within 3.2% relative (1510.7 → 1462.4). This level of degradation is practically interesting for deployment scenarios where throughput is critical.

- **Training-free inference on video LMMs demonstrates cross-modality generality.** Applying PruMerge directly to Video-LLaVA (no retraining) improves ActivityNet-QA accuracy (45.3 → 48.3) and MSVD-QA (70.7 → 71.1), while reducing visual tokens from 2048 to ~256. This suggests substantial redundancy in video tokens and demonstrates the method's plug-and-play versatility.

- **Comprehensive efficiency model shows orthogonal benefits to quantization.** Table 2 quantifies FLOPs, prefill time, and activation memory reductions, and shows that PruMerge's savings stack with INT4 quantization (e.g., Vicuna-7B FP16: 9.3 TB → 0.91 TB; INT4: 2.3 TB → 0.28 TB).

## Weaknesses

### Fatal
None.

### Major

- **The claim of "comparable performance" is materially misleading for the high-compression (PruMerge, ~5.5% tokens) regime.** The abstract states PruMerge "can compress the visual tokens by 14 times on average, and achieve comparable performance." This claim (repeated in the introduction and conclusion) is at odds with the data in Table 1. PruMerge at 5.5% tokens drops VQAv2 by 8.3% (78.5→72.0), MME by 10.6% (1510.7→1350.3), and POPE by 11.2% (85.9→76.3). These are not "comparable" by any reasonable standard — the degradation is substantial on several core benchmarks. The paper's framing systematically conflates the two regimes: PruMerge+ (25% tokens, moderate degradation) is a genuinely useful result, but PruMerge (5.5% tokens, substantial degradation) is not well described by "comparable." The authors should present these as two points on a Pareto frontier and let readers judge the trade-off, rather than using "comparable" as a blanket characterization. This is the most impactful weakness because it affects how the entire paper is perceived.

- **The Algorithm 1 description of PruMerge+ does not transparently map to the reported token counts.** Algorithm 1 shows PruMerge using IQR to select *m* tokens (Step 202), then PruMerge+ optionally sampling another *m* spatially uniform tokens (Steps 203–205), for a total of 2*m* tokens. However, the reported average token counts are ~32 tokens (5.5%) for PruMerge and ~144 tokens (25.0%) for PruMerge+. A doubling from 32 to 64 does not explain 144. The relationship between the IQR-selected token count and the final PruMerge+ token count is not clearly specified, and the algorithm as written does not match the reported compression ratios. This needs clarification.

### Minor

- **Evaluation is limited to a single visual encoder (CLIP-ViT).** The method's core mechanism — CLS-token attention sparsity in the penultimate layer — is specific to ViT architectures with a CLS token. Many LMMs use other backbones (ConvNeXt, SigLIP, EVA-CLIP, or Q-Former without a global token) where this sparsity pattern may not hold. The paper's claim that it provides a general token reduction strategy would be strengthened by testing at least one alternative encoder. As it stands, the scope is narrower than claimed.

- **Video results raise unanswered questions.** PruMerge improves ActivityNet-QA by +3.0 and MSVD-QA by +0.4 while *reducing* tokens from 2048 to ~256, but MSRVTT-QA accuracy drops (−0.8). No variance or significance measures are reported. The improvements are surprisingly large for a training-free compression method — if removing 87.5% of tokens consistently *helps*, this warrants deeper analysis (e.g., is the original Video-LLaVA suboptimal with 2048 tokens, or is there an evaluation artifact?). The current discussion attributes it to "redundancy removal" without ruling out simpler explanations (noise, overfitting to the token distribution). Additionally, the video text has an apparent inconsistency ("256 (12.5% on average) and 256 (25.0% on average)" — 256/2048 = 12.5%, so the 25.0% figure appears to be a typo or unclear).

- **The number of neighbors *k* in the key-similarity merging step is never specified or ablated.** The method relies on *k*-nearest neighbor clustering (Algorithm 1, Step 208), but the paper does not state the value of *k* or study its impact on performance. This is a meaningful hyperparameter: too few neighbors would under-utilize pruned tokens, too many could dilute informative tokens with noise.

- **Efficiency analysis uses roofline estimates, not wall-clock measurements.** The paper is transparent about this (the caption states "time estimated by the roofline model represents the theoretical performance"), but the main text later calls the results "significant, as demonstrated in Table 2" without noting that real latencies may differ substantially due to memory bandwidth, kernel launch overhead, and implementation efficiency. A simple wall-clock speedup on actual hardware would be more persuasive.

- **The choice of the penultimate layer (over the last layer) for CLS attention is asserted but not justified.** The paper uses the penultimate layer for IQR selection (line 161) and the final layer's keys for merging (line 175). The rationale for this specific layer choice is not discussed or ablated.

- **IQR is justified only qualitatively.** The paper shows a log-scale plot of attention score distribution (Figure 3a) and asserts that IQR outlier detection is appropriate, but provides no quantitative analysis (e.g., what fraction of tokens are selected by IQR vs. a fixed top-*k* approach, or how the 1.5× IQR threshold was chosen).

### Trivial

- **Inconsistency between abstract (5.5%) and conclusion (6.9%) for token count.** The abstract reports 5.5% as the average across 6 tasks; the conclusion and ablation report 6.9% (40 tokens, a fixed setting). These are compatible (different aggregation methods) but the presentation is confusing without explanation.

## Nice-to-Haves

- A simple top-*k* baseline based on CLS attention (i.e., select top *k* tokens by attention without IQR or merging) would help isolate the benefit of the IQR heuristic.
- Wall-clock latency measurements on the same GPU would strengthen the efficiency claims.
- Ablation on layer choice (penultimate vs. last vs. earlier layers) would strengthen the design justification.
- Reporting variance or confidence intervals, especially for the video results where improvements are small and mixed, would help assess significance.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Missing related works on token reduction for LMMs (from Harsh Critic).** Removed per meta-reviewer instructions: missing-related-work criticisms cannot be verified without external sources.
- **Baselines being "older models" (BLIP-2, InstructBLIP).** Removed: these are contextual baselines; the paper's key comparison is LLaVA-1.5 vs. LLaVA-1.5+PruMerge, which is properly controlled.
- **"The last layer also has a CLS token" layer-choice criticism.** Kept in Minor in modified form — the criticism is about the lack of justification for penultimate vs. last layer, which is valid. But the claim that the last layer "also has a CLS token" is not actually a weakness (the authors use penultimate for selection and final for keys, which is a specific design choice that could be right or wrong).
- **Formatting/style nitpicks from the Harsh Critic.** Removed per instructions.

## Novel Insights

The key insight — that the sparsity pattern of CLS-token attention in CLIP-ViT's penultimate layer can serve as a reliable signal for token importance in LMMs — is clean and practically useful. The IQR-based adaptive selection is a clever choice because it avoids a fixed token budget, letting simpler images use fewer tokens and complex images (e.g., dense text) use more. The observation that token reduction can actually *improve* video LMM performance (though it needs verification) suggests that current video LMMs may over-provision tokens to the point of introducing noise. However, the paper's most important contribution is the careful ablation showing that merging pruned tokens back via key-similarity clustering recovers a meaningful amount of the information lost by pruning alone.

## Suggestions

1. **Reframe the claims precisely.** Distinguish clearly between the PruMerge regime (5.5% tokens, substantial degradation) and PruMerge+ regime (25% tokens, moderate degradation). Present them as operating points on a trade-off curve rather than using "comparable" as a blanket claim.
2. **Clarify Algorithm 1's PruMerge+ token count.** Explain how the 2*m* tokens from the algorithm relate to the reported 25% ratio, or correct the algorithm to match the actual selection process.
3. **Add a simple baseline: top-*k* by CLS attention at matched token counts.** This is the most natural ablation and would directly show the value of the IQR heuristic and the merging step.
4. **Specify and ablate *k* (number of neighbors in merging).** This is a parameter the reader cannot evaluate or reproduce without knowing its value.
5. **Test on at least one non-CLIP-ViT backbone** (or clearly scope the paper's claims to CLIP-ViT-based LMMs if generalization is not yet established).

## Score and Decision

The paper proposes a clean, practical token reduction method with useful empirical results. The method itself is sound and the ablation study convincingly shows the contribution of each component. However, the paper is let down by (a) a materially misleading framing of "comparable performance" for the 14× compression regime, (b) an algorithmic ambiguity that prevents full reproducibility of PruMerge+, and (c) evaluation scope limited to one visual encoder. These are fixable issues — the core contribution is real — but in their current form they weaken the paper's claims more than the authors acknowledge.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>