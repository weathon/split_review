Now I have all the information I need. Let me write the final consolidated review.

**Round 1 bracket:** Based on the first calibration search, the paper clearly belongs in the middle band (3.5–7.5). The weak-band papers (3.0–3.33) are about token pruning for VLMs and were rejected for having limited novelty or fundamental flaws — CLIP-Map is substantially more novel and more thoroughly evaluated. The strong-band papers (8.0) are about entirely different topics (Text-to-3D, embodied navigation) and are not comparable.

**Round 2 narrowing:** I examined anchors at 4.00 (Reject), 5.00 (Reject), 5.60 (Accept Poster), 6.00 (Accept Poster) and 6.00 (Accept Poster). CLIP-Map is clearly stronger than the 4.00–5.00 papers — those were rejected for having questionable theoretical justification, limited novelty, or narrow scope. It is at least as strong as the 6.00 papers and, in my assessment, slightly stronger due to the genuine paradigm novelty (mapping vs. selection) and the thoroughness of evaluation across multiple compression ratios and tasks. The harsh critic's main criticism (ablation not comparing against importance-based pruning) is factually incorrect — "Manual Drop (0 epoch)" values exactly match TinyCLIP's numbers, showing it IS the importance-based pruning baseline.

**Final score: 6.5**

---

## Summary

This paper proposes CLIP-Map, a mapping-based compression framework for CLIP models that replaces conventional select-based pruning with learned linear transformations of pretrained weights. The core technical contributions are: (1) a Kronecker-factorized full-mapping strategy that compresses width and depth dimensions efficiently, and (2) a diagonal inheritance initialization scheme that enables stable optimization. The method is evaluated in a two-stage mapping-retraining pipeline (mapping → knowledge distillation) across retrieval and classification benchmarks at 1.0%, 10.0%, and 50.0% compression ratios, showing consistent improvements over TinyCLIP and other baselines.

## Strengths

1. **Novel paradigm shift from select-based to mapping-based compression.** Unlike prior CLIP compression work that prunes parameters via hard selection (e.g., importance-based masks), CLIP-Map formulates compression as learning linear transformations that combine original weights. This is qualitatively different and well-motivated by the information-loss limitations of hard pruning. The Kronecker factorization (Equations 3–4) makes this tractable, reducing mapping parameters from O(D₁²D₂²) to O(D₁D₂).

2. **Diagonal Inheritance Initialization is clearly validated as essential.** Table 5 shows the initialization is not merely helpful but absolutely critical: diagonal init achieves 28.9% IN-1K accuracy vs. the next-best 4.9% (Xavier). The paper provides a clean mathematical derivation (Equations 5–8) of why standard initializations cause multiplicative variance explosion in Kronecker-structured mappings, making the proposed solution principled rather than heuristic.

3. **Substantial gains at high compression ratios.** At 1.0% compression (Table 1), CLIP-Mapₜᵢₙᵧ achieves TR@1=15.8 vs. progressive TinyCLIP's 12.5 on MSCOCO — a 26% relative improvement. At 10.0%, CLIP-Mapₛₘₐₗₗ achieves TR@1=38.4 vs. 36.2. These improvements are consistent across both retrieval datasets and across 18/21 zero-shot classification datasets (Table 2), with the same total training epochs or fewer.

4. **Generalization to different CLIP variants and encoders.** The method is validated on OpenCLIP, Meta-CLIP, and ResNet-50 vision encoder (Table 1), demonstrating that the mapping framework is architecture-agnostic rather than tied to a specific CLIP variant.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **No variability/error bars reported.** The paper does not mention whether results come from a single run or multiple seeds. Given the potential training instability at extreme compression ratios (1.0%), reporting standard deviations or multiple-run averages would strengthen confidence in the reported improvements.

2. **The ablation on initialization (Table 4) is not explicitly labeled as TinyCLIP-equivalent.** The row "Manual Drop (0 epoch)" produces numbers identical to TinyCLIP at 10.0% compression (TR@1=33.8, IR@1=20.2), confirming it is the importance-based pruning baseline and not random pruning. However, the paper does not explicitly state this equivalence, which could confuse readers. The paper would benefit from a short clarifying sentence.

3. **Computational overhead of the mapping stage is not quantified.** The paper notes the mapping stage is only 5 epochs, but the mapping matrices themselves are additional learned parameters with update costs during those 5 epochs. A brief comparison of total training FLOPs/memory vs. TinyCLIP's progressive scheme would help readers assess the true training cost.

### Trivial

- The caption text for Figure 2 appears garbled due to parser artifacts in this version; the original figure description should be verified.
- Some table formatting (e.g., duplicated column headers) appears to be a parser artifact.

## Nice-to-Haves

- A direct visual comparison of the learned mapping matrices (evolution from diagonal to uniform distribution) in the main paper would strengthen intuition. (Currently deferred to Appendix A.7.)
- An analysis of which layers benefit most from mapping vs. which could be handled by simpler selection would deepen understanding of the method's behavior.

## Removed Points

These points were flagged by the input reviewers but are removed after verification against the paper:

1. **"The ablation compares mapping against a weak random-pruning baseline, not importance-based pruning" (from Harsh Critic).** REMOVED. The "Manual Drop (0 epoch)" row in Table 4 produces values that are numerically identical to TinyCLIP at 10.0% compression (TR@1=33.8, IR@1=20.2, identical across all six retrieval metrics). This confirms it IS the importance-based pruning baseline, not random pruning. The system-level comparison (Table 1) further confirms that CLIP-Map outperforms progressive TinyCLIP even with fewer total training epochs (25 vs. 50). The critic's concern is based on a misreading.

2. **"Missing details about target dimension selection" (from Harsh Critic).** REMOVED. The paper explicitly directs this to Appendix A.3, which the parser strips. This is standard practice at ICLR and not a flaw in the submission.

3. **"Visualization of learned mappings should be in main paper" (from Harsh Critic).** DEMOTED to Nice-to-Have. The visualization exists in Appendix A.7; deferring it to the appendix is reasonable for a 9-page paper.

4. **Generic strengths about "addressing an important problem" from Strength Finder.** REMOVED. These are superficial and apply to any paper in this area (CLIP compression is well-known to be important).

## Novel Insights

The most striking finding that emerges from the review process is that the proposed Diagonal Inheritance Initialization is not merely helpful but is essentially enabling — without it, the method collapses (28.9% vs. 4.9% IN-1K). This suggests that the primary practical difficulty in mapping-based compression is not the mapping architecture itself but the optimization landscape created by Kronecker-structured transformations. The variance derivation (Equations 5–8) provides a principled explanation that goes beyond the typical empirical ablation, and this analysis could inform other Kronecker-based techniques beyond compression.

## Suggestions

1. Add standard deviations or multiple-seed runs for the main results (at least for the high-compression settings where variability is largest).
2. Explicitly note in Table 4 that "Manual Drop" corresponds to the initialized weights from the pruning procedure (i.e., TinyCLIP-equivalent initialization without progressive training).
3. Provide a brief quantification of the mapping stage's computational overhead (e.g., extra parameters and FLOPs during the 5 mapping epochs) relative to the retraining stage, to allow direct comparison with TinyCLIP's multi-stage progressive scheme.

## Score and Decision

**Calibration Anchors Used (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 2TK9CLwMGA (PREP token pruning) | 3.33 | R1 | Rejected. Token pruning for VLMs; narrower scope. CLIP-Map is stronger in novelty and evaluation. |
| 5Y8PMEeAkv (ZSPAPrune) | 3.33 | R1 | Rejected. Similar token pruning category. CLIP-Map addresses weight compression, a harder problem with clearer practical impact. |
| jmQKr47S77 (MLLM-Pruner) | 3.00 | R1 | Withdrawn/Reject. Activation-aware pruning for MLLMs; limited novelty. CLIP-Map is substantially more original. |
| AqCG1RUbyO (Posterior-guided token pruning) | 3.00 | R1 | Withdrawn/Reject. CLIP-Map has stronger technical depth and better empirical results. |
| Fxz0aaGSNY (APM dataset distillation) | 4.80 | R1 | Reject. Questionable theoretical justification (InfoNCE→least-squares simplification). CLIP-Map's theoretical motivation is sounder. |
| bl3drImevi (Prototype-guided distillation) | 5.60 | R1,R2 | Accept Poster. Learning-free approach with good results, but narrow evaluation (retrieval only). CLIP-Map evaluates more thoroughly across tasks and compression ratios. |
| Wa9Bg9b50B (CompoDistill) | 6.00 | R2 | Accept Poster. Attention distillation for MLLMs. CLIP-Map addresses model compression rather than distillation alone and has a more novel core idea. |
| 6ycBM1nsS3 (CoDA dataset distillation) | 4.50 | R1 | Accept Poster (4,4,4,6). Marginal SOTA gains (0.1%). CLIP-Map's improvements are larger and more consistent. |
| UGCgt3cvcC (AMP MLP pruning) | 4.00 | R2 | Reject. Targets only MLP modules; high search cost. CLIP-Map's method is more general and better motivated. |
| YDRoTtmXu1 (CoTAM MLLM codec) | 6.00 | R2 | Accept Poster (4,8,6,6). Mixed reviews. Strong analysis but narrow task focus. CLIP-Map has cleaner experiments across more settings. |
| 46LbXtFgBm (IVC-Prune) | 6.00 | R2 | Accept Poster (6,4,8,6). Training-free token pruning with good insight but hyperparameter sensitivity. CLIP-Map addresses a harder problem (weight compression) with stronger technical contributions. |
| 073WQjmWKU (Visual Compositional Tuning) | 5.67 | R2 | Accept Poster. Data recipe for VIT. Different area, comparable score band. |
| ZGJJF1e2u0 (MPS-Tuning) | 6.00 | R2 | Accept Poster. Manifold-aligned fine-tuning. Strong paper but different problem scope. |

**Round 1 bracket:** [3.5, 7.5] — CLIP-Map clearly exceeds the weak-band papers (3.0–3.33) and is far below the strong-band papers (8.0, different topics).

**Round 2 narrowing:** The paper sits above the 4.0–5.0 anchors and is comparable to or slightly above the 5.6–6.0 anchors. The most comparable anchor is the 6.00 IVC-Prune paper (accepted poster): CLIP-Map has a more novel paradigm, stronger theoretical grounding for its initialization, and broader evaluation, placing it slightly higher.

**Final score: 6.5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>