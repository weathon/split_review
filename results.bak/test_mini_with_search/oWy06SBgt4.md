Now I have all the information I need. Let me write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me produce the final review.

Let me first state my bracket reasoning:

**Round 1 bracket**: Based on the initial calibration, low-score anchors (2-3) were on very different/weaker papers, high-score anchors (8) were on unrelated topics. The paper clearly sits in the middle band (4-7).

**Round 2 narrowing**: I compared against anchors at 4.67 (BitNet Distillation - Reject), 5.0 (Robust Training - Accept Poster), 5.33 (Beyond Outliers - Accept Poster), and 6.0 (Compute-Optimal QAT - Accept Poster). The paper under review has genuine contributions comparable to the 5.0-5.33 range. It's stronger than the 4.67 rejected paper (which had overclaimed contributions and missing baselines). It's not as experimentally thorough as the 6.0 paper. I place it at 5.0.

Now let me produce the review.## Summary

This paper makes the first attempt at 1-bit Fully Quantized Training (FQT), pushing gradient quantization from the prior 4-bit frontier down to an average of 1 bit per element. The contributions are threefold: (1) a theoretical analysis showing that SGD's convergence depends on gradient variance quadratically while Adam's depends linearly, explaining Adam's superior performance at low bitwidths; (2) Activation Gradient Pruning (AGP), which prunes low-range gradient groups and reallocates bits to high-range groups to reduce quantizer variance; and (3) Sample-Channel joint Quantization (SCQ) that enables practical acceleration of both weight-gradient and activation-gradient computations on low-bitwidth hardware. Experiments on transfer learning tasks with binary-pretrained models show consistent improvements over 1-bit per-sample quantization and real speedups up to 5.13× on CPU/edge devices.

## Strengths

- **First 1-bit FQT with theoretical grounding.** The paper provides regret bounds (Theorems 1 and 2) linking gradient variance to convergence for both SGD ($O(\sigma^2)$ dependence) and Adam ($O(\sigma)$ dependence), offering a principled explanation for why Adam succeeds where SGD fails at 1-bit precision. This theory directly motivates the variance-reduction design of AGP.

- **AGP demonstrably reduces quantizer variance and improves accuracy.** Equation (24) derives a variance bound proportional to $\sum_{i=1}^{N/b} R_i^2$ versus 1-bit PSQ's $\sum_{i=1}^N R_i^2$, and Table 1 confirms this transfers to practice: AGP with $b=4$ improves average accuracy over 1-bit PSQ by 6.52% (ResNet-18) and 5.73% (VGGNet-16) across six datasets. Figure 11 directly plots the variance reduction per dataset, causally linking lower variance to smaller accuracy gaps.

- **SCQ reformulation enables real hardware acceleration.** The paper identifies that naive per-sample quantization (PSQ) cannot accelerate weight-gradient computation, and solves this via a dual quantization strategy (PSQ for activation gradients, PCQ for weight gradients). Table 3 validates the approach: the full pipeline achieves up to 5.13× speedup over FP32 PyTorch on Hygon and 2.49× on Raspberry Pi 5, while the PSQ-only baseline achieves only 0.07×.

- **Thorough evaluation of the $b$ hyperparameter trade-off.** Table 1 systematically explores $b \in \{2,4,8\}$ across six datasets and two architectures, finding $b=4$ consistently optimal. This provides clear practical guidance and demonstrates understanding of the variance-information-loss trade-off.

- **Cross-architecture and cross-task validation.** Table 2 extends results beyond CNNs to Faster R-CNN (detection), MLP-Mixer (all-MLP), and BERT (NLP), showing the method's potential generality.

## Weaknesses

### Fatal
None.

### Major

1. **Missing ablation study isolating AGP and SCQ individually.** The paper presents AGP+SCQ as a combined method, but never ablates AGP alone (without SCQ, using full-precision on the other path) or SCQ alone (without AGP). Without these ablations, it is impossible to determine how much each component contributes to the final results. For example, the accuracy improvements in Table 1 could be driven primarily by AGP's variance reduction, with SCQ providing only the acceleration benefit, but the paper does not provide evidence to separate these effects.

2. **Channel-wise AGP for PCQ is underspecified.** The sample-wise AGP receives a detailed description with probability formulas ($p_i = NR_i/(bR_{total})$) and mask construction. However, for the channel dimension, the paper states only "pruning operations also need to be performed along the channel dimension" (line 267) without specifying how pruning probabilities are computed for channels, how many channels are retained, or whether the same $b$ is shared. This makes the algorithm partially irreproducible.

### Minor

3. **Limited 1-bit baseline comparisons.** The paper compares only to 1-bit PSQ (per-sample quantization). While the paper claims "existing work has not tried 1-bit FQT," it is straightforward to implement per-tensor quantization (PTQ) or per-channel quantization (PCQ) at 1-bit as additional baselines. Adding these would isolate the benefit of AGP's adaptive pruning over simpler per-group strategies and strengthen the claim that AGP is the key enabler.

4. **The analysis is scoped to transfer learning only.** The paper explicitly acknowledges that training from scratch remains an open problem (even 3-bit FQT from scratch is unsolved), which is honest. However, the title "Pushing the Limit of Fully Quantized Training to 1-bit" and the abstract's broad framing could give the impression of a more general capability than is demonstrated. The paper would benefit from qualifying this scope earlier.

5. **Pruning/metadata overhead is not quantified.** The paper does not report the computational overhead of range computation, probability calculation, random mask generation, and metadata management at each iteration. These operations occur in floating-point and could offset some of the speedup, especially for small layers or low batch sizes where the 1-bit GEMM is very fast.

### Trivial

6. The y-axis labels and scales in Figure 11 (quantizer variance plot) are difficult to read in the PDF, making it hard to verify the variance numbers visually.

## Nice-to-Haves

- An optimized 8-bit PSQ baseline (e.g., using `torch.int8` GEMM) would make the speedup comparison even cleaner, though the current comparison already uses unoptimized implementations on both sides (Ours-Basic vs PSQ-Basic).
- Exploring $b$ values beyond $\{2,4,8\}$ (e.g., $b=1,3,6$) could more precisely characterize the trade-off landscape.
- Extending the theoretical analysis to non-convex settings (while challenging) would strengthen the theory's relevance to deep networks.

## Removed Points

- **"Speedup comparison to 8-bit PSQ is misleading" (Harsh Critic #1):** Removed because it is factually incorrect. I verified that the speedup ratios 32.28× and 45.28× are computed from Ours-Basic vs PSQ-Basic — *both* of which are labeled "unoptimized" implementations in Table 3. The paper's own caption states: "Basic and Basic represent unoptimized FQT and unoptimized FP32 training." The comparison is therefore between unoptimized 1-bit and unoptimized 8-bit (same implementation baseline), not between optimized and unoptimized as the critic claimed. For VGGNet-16: Ours-Basic (3.17×) / PSQ-Basic (0.07×) = 45.29× ≈ 45.28×. For ResNet-18: Ours-Basic (2.26×) / PSQ-Basic (0.07×) = 32.29× ≈ 32.28×. The claim is fully supported by the data as presented.

- **Generic formatting/style nitpicks** from both reviewers removed per filtering rules.

- **Generic strengths** from the Strength Finder that were superficial or sycophantic (e.g., generic praise of the importance of the problem) removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add an ablation study: (a) AGP-only (with full-precision SCQ path), (b) SCQ-only (with PSQ instead of AGP), and (c) full AGP+SCQ. This will cleanly isolate the contribution of each component.
2. Add at least one additional 1-bit baseline — per-channel quantization (PCQ) at 1-bit — to Table 1 to show AGP's advantage over simpler per-group strategies.
3. Provide a complete specification of channel-wise pruning probabilities and mask computation for the PCQ path in SCQ, either in the main text or appendix.
4. Report the overhead of the pruning/metadata operations (range computation, mask generation, bit decomposition) in cycles or microseconds to help practitioners assess the net speedup.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|------------------------|
| LUopdQeiz1.md (quantized training LLM) | 2.50 | R1 | Much weaker; limited experimental scope |
| 6P8AEfsw86.md (saliency-guided quantization) | 3.00 | R1 | Weaker; narrower contribution |
| OEXOAMvsc6.md (FP4 training) | 2.00 | R1 | Weaker; rejected for insufficient novelty |
| kBRXrAkqR2.md (SplitQuant DiT) | 2.50 | R1 | Weaker; PTQ not FQT |
| e6nZrzSccj.md (Robust Training arbitrary precision) | 5.00 | R1/R2 | Similar quality; accepted poster; more general framework but less hardware validation |
| mjmDFmGue5.md (SURGE BNN) | 4.00 | R2 | Similar scope but weaker empirical validation |
| Urt7MPg1u0.md (Rethinking 1-bit optimization) | 4.00 | R1 | Weaker; rejected for unfair comparisons |
| jxtCMoZIu8.md (BEP binary training) | 5.33 | R1 | Similar quality; accepted poster; narrow experimental setup |
| hsgl5Owiio.md (BitNet Distillation) | 4.67 | R2 | Weaker; rejected for overclaimed contributions |
| 0qVu2WsDle.md (Bit-efficient dataset condensation) | 4.50 | R2 | Weaker; different task |
| QpbtT95S95.md (Compute-Optimal QAT) | 6.00 | R2 | Stronger; more thorough empirical methodology |
| IEGwgxe13Y.md (WiniQ QAT) | 5.00 | R2 | Similar score but rejected; weaker methodology |
| mVldAuDAn5.md (Beyond Outliers optimizer study) | 5.33 | R2 | Similar quality; accepted poster; well-executed study |

**Bracketing:** Round 1 placed the paper in the 4–7 range. Round 2 narrowed to 4.5–6.0 based on comparisons to accepted poster papers (Robust Training at 5.0, Beyond Outliers at 5.33, BEP at 5.33) and a rejected but similar-scope paper (BitNet Distillation at 4.67).

**Final position:** The paper compares favorably to the 4.67 and 5.0 anchors — it has genuine algorithmic novelty (first 1-bit FQT), real hardware measurements, and a clean theoretical motivation. It is not as experimentally thorough as the 6.0 anchor (Compute-Optimal QAT, which ran hundreds of experiments to fit scaling laws). The missing ablations and incomplete SCQ specification prevent it from reaching that tier. The paper sits between the 5.0 and 5.33 anchors.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>