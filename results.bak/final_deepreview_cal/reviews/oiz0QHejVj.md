## Summary

This paper proposes CLIP-Map, a mapping-based CLIP compression framework that replaces the conventional select-based pruning (e.g., importance masking) with learnable linear mappings. The approach uses Kronecker-factorized matrices to map each layer's weights to a smaller size (width compression) and a depth-combination matrix (depth compression). A Diagonal Inheritance Initialization scheme is introduced to stabilize optimization of the mapping matrices. In a two-stage pipeline (mapping → retraining via knowledge distillation), CLIP-Map consistently outperforms TinyCLIP at high compression ratios (e.g., 1% and 10% of original size) across multiple retrieval and classification benchmarks, and achieves these results with fewer training samples.

## Strengths

- **Strong performance at extreme compression ratios that directly validates the core idea.** At 1% compression (0.84M total parameters), CLIP-Map achieves 15.8 TR@1 on MSCOCO vs. TinyCLIP's 10.5 — a 50% relative improvement. At 10% compression (8+3M), gains are consistent across all retrieval metrics (e.g., 38.4 vs. 33.8 TR@1). These results are spread across MSCOCO, Flickr30K, and 21 classification datasets (Tables 1–2).

- **Diagonal Inheritance Initialization is convincingly shown to be critical.** Table 5 demonstrates that Random/Kaiming/Xavier initialization yields near-chance results (0.1–4.9% IN-1K) after the mapping stage, while Diagonal Init achieves 28.9%. The paper provides a clean theoretical analysis (Eq. 6–8) showing that independent Kronecker factors multiplicatively amplify variance under standard initialization, and the diagonal scheme eliminates this issue.

- **Fewer training samples required than select-based methods.** In Table 3, CLIP-Map_tiny reaches 19.0% zero-shot IN-1K with 0.45B seen samples, while TinyCLIP-8M/16 requires 1.125B samples to reach 16.6%. This directly supports the claim that mapping-based initialization provides a better starting point for subsequent distillation.

- **Parameter-efficient mapping via Kronecker factorization is technically sound and well-motivated.** The parameter count for each mapping is reduced from O(D₁²D₂²) to O(D₁D₂) (Eq. 3–4), making full-mapping practical. The ablation in Table 4 traces the effect of mapping duration, showing a clear improvement trajectory.

## Weaknesses

### Major

- **Depth compression is described as part of the method but never evaluated.** Section 3.2 and Eq. 2 introduce a learnable depth operator L_depth that combines layers linearly, and the paper claims a "unified end-to-end pipeline" for width and depth compression. However, all experiments (Tables 1–5) involve only width compression (hidden-dimension reduction). The number of layers is never stated for any compressed model, and no ablation measures depth compression's effectiveness or validates that the linear-combination formulation (Eq. 2) works in practice. This makes the paper feel overclaimed relative to what is demonstrated.

- **The controlled ablation isolating the mapping initialization is only run at 10% compression, not at 1% or 50%.** Table 4 provides a "Manual Drop (0 epoch)" baseline at 10% — exactly the control needed to separate the mapping initialization from the retraining pipeline — and the mapping approach improves over it (e.g., 38.3 vs. 33.8 TR@1, a 4.5-point gain, and 42.1 vs. 41.1 IN-1K). However, the largest gains are at 1% compression (15.8 vs. 10.5 TR@1), and no Manual Drop baseline is provided for this regime. Without it, we cannot fully attribute the 1% gains to the mapping itself versus other pipeline differences.

### Minor

- **Table 1 contains a labeling inconsistency.** The 1% compression row is labeled "CLIP-Map_base (Ours)" with 0.84M params, but according to Table 3 and Section 4.1, the 0.84M model is CLIP-Map_tiny. Similarly, the 10% row (8+3M params) is labeled "CLIP-Map_base" but should be CLIP-Map_small. The 50% row (39+19M) is correctly labeled. The text at line 366 correctly refers to CLIP-Map_tiny and CLIP-Map_small for the 1% and 10% rows, so this is a table formatting error. It does not affect the correctness of the results (the parameter counts and performance numbers are correct), but it must be fixed.

- **No error bars or confidence intervals are reported.** Given that the 50% comparison (CLIP-Map_base 55.1 vs. TinyCLIP 54.9 TR@1) is within 0.2 points, a few random seeds would clarify whether improvements are reliable.

### Trivial

- **Section 3.2.4 on retraining is essentially standard CLIP knowledge distillation.** The paper would benefit from explicitly stating that the retraining stage is not a novel contribution.

## Nice-to-Haves

- A controlled ablation (Manual Drop baseline) at 1% compression would strengthen the claim that mapping initialization drives the large gains in that regime.
- An experiment demonstrating depth compression — even a small one, e.g., reducing 12 layers to 10 — would validate the claimed unified pipeline.
- A brief discussion of how the Kronecker factor structure limits expressiveness and why it is sufficient for CLIP layers would address a likely reviewer question.

## Removed Points

These points were raised in the input reviews but are removed after verification against the paper:

- **"Core claim not directly tested" (Harsh Critic point 2)** — The paper DOES have a direct controlled test: Table 4's "Manual Drop (0 epoch)" is exactly the sub-network extraction baseline the critic asks for at 10% compression. It shows clear gains. The critic's claim that improvement is "only ~1 point" selectively cites IN-1K while ignoring the 4.5-point gain on MSCOCO TR@1. The missing baselines at 1% and 50% are a valid limitation (retained in Major), but the claim that the core claim is "not directly tested" is false for the 10% regime.

- **"Table 3 mixing methods" (Harsh Critic point 4)** — The table includes controlled comparisons (CLIP-Map_tiny vs. TinyCLIP-8M/16 on same data, CLIP-Map_base vs. TinyCLIP-39M/16 on same data). Other rows (MoPE-CLIP, MobileCLIP, ViT-T/16) are context comparisons, which is standard practice. The paper notes MobileCLIP's different data. This is not a weakness.

- **"Comparison to non-pruning compression methods (quantization)"** — This demands coverage of methods outside the paper's stated scope (pruning-based CLIP compression). Quantization is an orthogonal technique and not necessary for the paper's framing.

- **"Code is not mentioned"** — Hard rule: reproducibility nitpicks about non-essential artifacts are removed. The training recipe (32 H800 GPUs, YFCC-15M) is provided.

- **"Formal analysis of Kronecker mapping expressiveness"** — A nice-to-have, not a weakness. The paper provides a clear argument for why Kronecker factorization is sufficient (it operates independently on input and output dimensions).

- **"Weakness about missing related works"** — Hard rule: cannot include.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the paper's strengths and weaknesses without revealing a perspective that the paper itself does not articulate.

## Suggestions

1. **Fix Table 1 labels:** Rename "CLIP-Map_base" in the 1% and 10% rows to "CLIP-Map_tiny" and "CLIP-Map_small," respectively, consistent with the naming in Table 3 and Section 4.1.
2. **Add a Manual Drop baseline at 1% compression** to verify that the 5.3-point gain over TinyCLIP at 1% is attributable to the mapping initialization rather than other pipeline differences.
3. **Either include a depth-compression experiment or explicitly scope the paper to width-only compression.** The current framing overclaims.
4. **Add error bars** (at least 2–3 seeds) for key comparisons, especially the 50% regime where improvements are marginal.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
| Anchor | Score | vs. CLIP-Map |
|--------|-------|-------------|
| FwkYeLovHk (weak-to-strong CLIP) | 3.33 | Much weaker; different problem |
| HfJxXbXlYJ (LLM2CLIP) | 3.00 | Much weaker; different problem |
| a4nSE2kpoq (HyperCLIP) | 4.00 | Weaker; unclear motivation, limited experiments |
| GSUNPIw7Ad (Bridging Compressed Image Latents) | 6.00 | Similar strength; less novelty but no omissions |
| imT03YXlG2 (Sparse autoencoders for CLIP) | 6.50 | Different contribution type; stronger theory |
| kbjJ9ZOakb (neuron invariance manifolds) | 8.00 | Different topic; much stronger theory |
| **Round 1 bracket: 5.0–6.5** | | |

**Round 2 (Narrowing):**
| Anchor | Score | vs. CLIP-Map |
|--------|-------|-------------|
| pAVJKp3Dvn (Differentiable Structured Matrices) | 5.67 | Similar topic (structured matrices); comparable contribution, weaker empirical validation |
| 1RrOtCmuKr (Network Memory Footprint Compression) | 6.33 | Different method (codebook); stronger variance in reviews |
| VMV8gefvq8 (MCNC) | 6.00 | Model compression; similar contribution level |
| I5S1a1NKxo (SIDCLIP data-scarce distillation) | 5.00 | Related (CLIP distillation); weaker novelty |
| W2Wkp9MQsF (Model Folding) | 5.75 | Data-free compression; comparable empirical depth |

**Final score rationale:** The paper is stronger than the 5.0–5.75 range (better technical novelty and empirical grounding than SIDCLIP, Differentiable Structured Matrices, or Model Folding). It is comparable to the 6.0 anchor (Bridging Compressed Image Latents) — both have clear practical value with some limitations. I set the score at 6.0 rather than higher because the depth-compression overclaim and the missing controlled ablation at 1% are real issues that prevent this from being a clean strong accept. The core width-compression contribution is well-supported and the Diagonal Inheritance analysis is theoretically grounded, but the paper claims more than it demonstrates.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>