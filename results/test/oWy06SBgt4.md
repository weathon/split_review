I now have a complete picture of the paper. Let me produce the consolidated review.

## Summary

This paper pushes fully quantized training (FQT) to the 1-bit regime for the first time, in the setting of transfer learning / fine-tuning of pretrained binary models. The authors propose two complementary techniques: Activation Gradient Pruning (AGP), which probabilistically prunes low-range gradient groups to reduce quantizer variance while maintaining unbiasedness, and Sample-Channel joint Quantization (SCQ), which assigns sample-wise quantization for activation gradients and channel-wise quantization for weight gradients so both matrix multiplications in backpropagation can use 1-bit integer operations. They provide a theoretical regret analysis suggesting Adam is more robust to gradient variance than SGD (O(σ) vs O(σ²)), motivating their design. Empirically, their method achieves consistent gains over naive 1-bit per-sample quantization across 6 visual classification datasets, object detection (Faster R-CNN), MLP-Mixer, and BERT, with measured speedups up to 5.13× over FP32 PyTorch on CPU hardware.

## Strengths

1. **First successful 1-bit FQT with a principled variance-reduction mechanism.** Prior FQT work stopped at 4 bits. The paper identifies that the core difficulty at 1-bit is the exploding quantizer variance, and proposes AGP — a clean, theoretically motivated approach that prunes low-range gradient groups and reallocates bits to high-range groups, provably reducing variance from O(N) to O(N/b) (Eq. 24). Empirical variance measurements (Fig. 11) confirm lower variance across all 6 datasets, directly supporting why their method converges where naive 1-bit PSQ struggles.

2. **SCQ resolves a real practical bottleneck.** Prior FQT quantizers (e.g., PSQ) enabled 1-bit acceleration for activation gradient MMs but left weight gradient computation requiring a dequantization step, negating much of the benefit. SCQ assigns per-channel quantization for weight gradients, so both MMs in Eq. 21 can use 1-bit binary operations. This design choice is validated by the substantial speedup over PSQ-Basic and SCQ-Basic in Table 3.

3. **Validation across diverse architectures and tasks beyond convnets.** The method is evaluated on ResNet-18, VGGNet-16, Faster R-CNN, MLP-Mixer, and BERT (Tables 1, 2). The 1.66% mAP drop on detection and reasonable NLP results on GLUE suggest the approach generalizes beyond the primary image classification setting.

4. **Honest limitations and clear scope.** The paper explicitly acknowledges in the conclusion (line 456) that the method is restricted to transfer learning and that "even 3-bit FQT from scratch is still an open problem." This candor is rare and helps readers calibrate expectations.

5. **Ablation study on the critical hyperparameter b.** Table 1 systematically varies b ∈ {2,4,8}, identifying b=4 as the optimal trade-off between variance reduction and information loss. This provides actionable guidance for practitioners.

6. **End-to-end hardware implementation with measured speedups.** The binop library translates the algorithmic contributions into real (not simulated) speedups on Hygon CPU and Raspberry Pi 5, bridging the gap between theory and practice.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Speedup claims presented at two incomparable levels without clear separation.** The paper's central speedup claim (5.13× from "Ours" vs FP32 PyTorch) is legitimate. However, the subsequent claim that "the speedup is well above a hundredfold" and "over 50× on edge devices" is computed by comparing Ours-Basic (unoptimized 1-bit) against Basic (unoptimized FP32) — a ratio of two artificially slow implementations. While the paper does state this context ("to assess the acceleration potential... under the condition without optimization"), the juxtaposition of the 5.13× figure with hundredfold numbers without a clearer explanation risks misleading a casual reader into thinking the practical speedup is far larger than it actually is. The hundredfold comparison is better framed as a theoretical upper bound or removed to avoid confusion.

2. **No experimental comparison to existing low-bit (4-bit) FQT methods.** The paper compares against QAT (full-precision gradients) and PSQ (1-bit naive), but never against state-of-the-art 4-bit FQT methods (Sun et al. 2020, Chmiel et al. 2021, Xi et al. 2023). While the paper's setting (fine-tuning binary models) differs from those works (training full-precision models from scratch), a comparison would contextualize the accuracy loss from going from 4-bit to 1-bit and help readers judge the practical trade-off. Even reporting cited accuracy numbers from those papers on comparable tasks (e.g., CIFAR-10 with a standard architecture) would be informative.

3. **Theoretical analysis is suggestive but not tightly coupled to the proposed method.** The regret bounds (Theorems 1 and 2) show Adam's regret scales as O(σ) vs SGD's O(σ²), motivating variance reduction. However: (a) the bounds assume convex losses, which do not hold for DNNs; (b) the comparison ignores problem-dependent constants (D, D_∞, G, β₁, λ) that differ between the bounds; (c) the variance parameter σ bounds the quantized gradient variance, but the link from AGP's range-based pruning to σ in the regret bound is indirect. The theory serves well as motivation but is not a proof that AGP is optimal. The paper would benefit from stating this limitation explicitly rather than presenting the O(σ) vs O(σ²) comparison as dispositive.

4. **Overhead of AGP (pruning, masking, bit-slicing) is not measured.** The paper reports end-to-end training time but does not break down the cost of computing probabilities, generating Bernoulli masks, and performing the b-bit decomposition. These operations could be nontrivial on edge devices. A simple profiling table showing the fraction of total runtime consumed by AGP overhead vs. the 1-bit MMs would strengthen the practical claims.

5. **Training hyperparameters are not specified in the main text.** Key experimental details such as learning rate schedule, batch size, number of fine-tuning epochs, Adam hyperparameters (β₁, β₂, λ), and how the pretrained binary models were obtained are absent from the main text. These are critical for reproducibility.

6. **Accuracy gap to upper bound is substantial.** Compared to QAT (full-precision gradients), the method loses ~5-6% average accuracy on CIFAR-10/100, Cars, CUB and ~10%+ on harder datasets like CIFAR-100 with ResNet-18. On BERT, the degradation is 8.39%. The paper frames this as "acceptable," but the practical viability of 1-bit FQT depends on whether users are willing to accept these losses for the speedups shown (which are 2-5×, not order-of-magnitude for realistic optimized baselines). The discussion should engage more directly with this trade-off.

### Trivial
- The sentence "The proof is given" (line 236) cuts off mid-sentence, and the associated derivation is deferred (presumably to an appendix stripped by the PDF parser). This is a formatting artifact of the review process, not an author error.
- The "8-bit PSQ" baseline in Table 1 uses 8-bit weights and activations (training a full-precision model with 8-bit everything), not a binary model. This is apples-to-oranges compared to the binary-model setting of QAT and Ours. While the paper uses this comparison only for speedup (not accuracy), the table could be clearer about the different training regimes.

## Nice-to-Haves
- A discussion of when 1-bit FQT is most valuable (extreme resource constraints, fixed-function binary accelerators) vs. when higher-bit methods are preferable.
- Sensitivity analysis of the pruning probability design: does the linear proportionality p_i ∝ R_i always hold, or could other functions (e.g., softmax over ranges) work better?
- Empirical comparison of the b=4 choice vs. simply using 2-bit gradients without pruning (a direct "equal-bitwidth" baseline).

## Removed Points
- **Criticism about proofs being deferred to appendix** — removed per instruction: the parser strips appendix content from all papers; proofs exist in the original submission.
- **"Contribution is narrowly scoped... not acknowledged with sufficient weight"** — removed: the paper explicitly states in the introduction (line 39) that it examines "transfer learning tasks" and in the limitations (line 456) that it does not address training-from-scratch. The scope is appropriately acknowledged.
- **Criticism about the theory being too detached to be useful** — downgraded to minor: the theory is used as motivation, which is standard practice; the reviewer's phrasing overstates the weakness.
- **"Missing comparison to 4-bit FQT methods as a baseline"** reframed: the 4-bit methods train full-precision (non-binary) models from scratch, making a direct comparison in the same table apples-to-oranges. Kept as a minor suggestion for additional context rather than a missing baseline.
- **"The value of b is not explained in terms of computational cost"** — the paper has Table 5 showing runtime for "average 1-bit" vs "1-bit" which directly addresses this; the concern about larger models is valid but unsubstantiated given the reported 5.13× speedup already incorporates the b-slice cost. Removed as the paper adequately addresses this.

## Novel Insights

None beyond the paper's own contributions — the reviews surface useful presentation critiques but do not add novel analytical insights.

## Suggestions
1. Reframe the "hundredfold" and "50×" speedup numbers explicitly as "theoretical upper bounds from comparing unoptimized implementations" rather than presenting them as speedups, to avoid any appearance of overclaiming.
2. Add a small table (potentially in the main text or existing appendix) comparing against accuracy numbers reported by 4-bit FQT papers on a common task (e.g., CIFAR-10 with ResNet-18/VGGNet) to contextualize the accuracy-speed trade-off.
3. Include a profiling breakdown showing the fraction of training time spent on AGP overhead (mask generation, bit-slicing) vs. the 1-bit MMs.
4. State the key training hyperparameters (learning rate, schedule, epochs, batch size, optimizer settings) explicitly in the main experimental section.
5. Tighten the presentation of the theory: acknowledge that the O(σ) vs O(σ²) comparison omits problem-dependent constants, and emphasize that the main takeaway is qualitative (Adam is more robust to variance) rather than quantitative.

## Score and Decision

This paper makes a genuine first attempt at 1-bit FQT, proposes a well-motivated algorithm (AGP + SCQ), validates it across multiple architectures and tasks, and provides an honest assessment of its limitations. The weaknesses are minor — presentation issues and missing ablations — none of which threaten the core contribution. The paper would be notably strengthened by the suggestions above, particularly clarifying the speedup claims and adding training details for reproducibility.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>