- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 5, 6
Now I have a thorough understanding of the paper content. Let me write the consolidated review.

## Summary

This paper proposes RotPruner, a training-based framework that learns orthonormal rotation matrices to transform weight matrices and activations in LLM linear layers *before* applying existing pruning methods (e.g., magnitude, Wanda). The rotation is optimized via Cayley SGD to minimize the pruned network's loss, with the insight that the rotated space can be more amenable to pruning (e.g., by increasing weight outliers). Experiments on OPT, LLaMA-2, and LLaMA-3 (up to 8B) across unstructured, 2:4 semi-structured, and structured sparsity show that RotPruner consistently improves perplexity and zero-shot accuracy over baselines including SparseGPT, Wanda, and SliceGPT.

## Strengths

- **Controlled experiment isolates the effect of learned rotation (Table 1)**: The paper directly compares pruning (Wanda) in three spaces — original, random rotation, and learned rotation — on OPT-1.3B at 50% sparsity. The learned rotation achieves substantially lower perplexity than both the original space and the random rotation, proving that the improvement is due to the *optimized* rotation and not just any transformation or additional compute. This is the single strongest piece of evidence for the paper's central claim.

- **Consistent gains across model families, sparsity patterns, and base methods**: Table 2 shows RotPruner (with Wanda/magnitude as the base) beating SparseGPT, Wanda, and SliceGPT on OPT-1.3B/2.7B/6.7B, LLaMA-2-7B, and LLaMA-3-8B under unstructured, 2:4 semi-structured, and structured sparsity. Table 9 further shows that RotPruner improves *all* tested base pruning methods (magnitude, Wanda, SparseGPT mask), demonstrating it is a general-purpose augmentation rather than being tied to a specific pruning metric.

- **Thorough ablation studies verify every design choice**: Tables 5–9 systematically ablate the loss function (auto-regression + cosine is best), straight-through estimator variants (SR-STE > STE > none), optimizer (Cayley SGD > Cayley Adam), calibration set size, number of shared rotation matrices, and base pruning method. This level of scrutiny makes the method's design choices well-supported.

- **Inference overhead is measured and shown to be small**: Table 4 reports that the residual rotation multiplications cause only a 1.006× slowdown (and as low as 1.003× with parameter sharing), confirming that the framework does not negate the speed benefits of pruning in practice.

- **Toy example motivates the core idea clearly**: Section 3.1 provides a concrete 2×2 example where pruning in the original space always produces a wrong result, but after a carefully chosen rotation the pruning becomes lossless. This directly validates the premise that the original space is not optimal.

## Weaknesses

### Fatal
None.

### Major

- **The paper's framing overclaims relative to what the experiments directly compare.** RotPruner trains rotation matrices for 5 epochs, while the primary baselines (SparseGPT, Wanda, SliceGPT) are one-shot methods with no training. The abstract and introduction position RotPruner as a "state-of-the-art" pruning method competing with these baselines without adequately caveating the training overhead. This is not a fatal flaw — the paper is transparent about the training (setup: "We train for 5 epochs," "1.5 hour" on an L40S) and the controlled experiment (Table 1) isolates the rotation's effect. However, a reader could come away thinking RotPruner is a drop-in replacement for one-shot methods, when it is more accurately a training-based *augmentation* that wraps existing methods. The paper would be significantly strengthened by: (i) framing RotPruner primarily as an augmentation technique that improves any base pruning method, (ii) centering the apples-to-apples comparison (RotPruner + Wanda vs. plain Wanda; RotPruner + SparseGPT mask vs. plain SparseGPT mask) in the main results rather than the ablation, and (iii) explicitly discussing the cost-benefit trade-off.

### Minor

- **The mask update schedule is underspecified for reproducibility.** Algorithm 1 and the text (Section 3.4, line 147) state that masks are obtained "in every training epoch" and then "after several iterations, update the masks." The phrase "after several iterations" is ambiguous — it is unclear whether masks are updated every epoch, every few iterations within an epoch, or according to some other schedule. This matters because mask recomputation adds cost and affects convergence.

- **No comparison against other training-based pruning methods that also use calibration data.** The related work discusses ADMM-Pruner and FISTAPruner (which update weights) and AST (which uses more data), but none appear in the experimental comparison. While RotPruner differs in not updating the original weights, these methods are natural competitors given that they also involve a training phase over calibration data.

- **Model scale is limited to 8B parameters.** The largest models evaluated are LLaMA-3-8B and OPT-6.7B. For LLM pruning papers, it is common to include 13B, 30B, or 70B models to demonstrate scalability. The paper's "suggest[ion] to use less number of Qs to save memory" for larger models is not backed by experimental evidence.

- **No confidence intervals or standard deviations reported.** For perplexity and zero-shot accuracy, the paper reports single-run point estimates. Given that the method involves training (even on fixed Qs), variance across different calibration subsets or random seeds is expected.

- **The SparseGPT-Mask baseline in the ablation (Table 9) disables weight reconstruction.** The paper acknowledges this ("To shorten the training time, we use SparseGPT without weight reconstruction"), but this means the "SparseGPT mask" baseline is a weakened version of the actual SparseGPT method. While this doesn't invalidate the result (RotPruner improves the mask itself), it should be noted that the improvement shown does not apply to the full SparseGPT algorithm.

- **The theoretical connection between the training objective (pruned loss minimization) and the "outlier creation" intuition is not formally established.** The paper provides a toy example and distribution plots (Figure 2) suggesting that learned rotation creates more weight outliers. However, there is no analysis proving that the loss-minimizing rotation *causally* works through the outlier mechanism rather than through some other effect (e.g., redistributing weight importance more favorably). This is not a fatal gap — the empirical evidence stands on its own — but the claimed explanatory mechanism is only suggestive.

### Trivial
- The paper lacks a "Limitations" section that could transparently discuss training overhead, calibration set sensitivity (partially shown in Figure 5 but not discussed), potential overfitting, and memory cost of the rotation matrices.

## Nice-to-Haves
- Report the wall-clock time for each baseline in addition to RotPruner's 1.5-hour figure, to give readers a concrete cost-benefit comparison.
- Quantify the memory overhead of the extra rotation parameters (e.g., for a 7B model, ~0.5B additional parameters as estimated by the reviewer) and discuss whether they can be freed after training or fused.
- Show a per-task breakdown for the zero-shot results (Table 3) rather than only averages.
- Provide a convergence curve (perplexity vs. training epochs) to justify that 5 epochs is sufficient and not overfit to the small calibration set.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Random rotation demonstrates catastrophic performance" (Harsh Critic's characterization of this as a minor point should be removed)**: The Harsh Critic notes this as a finding, not a weakness. The Strength Finder correctly lists it as evidence. Not a weakness at all; removed.

- **Criticism that missing related works are a problem**: I cannot verify what related works are missing; this is speculation. Removed per instructions.

- **"The L1-minimization discussion (Candès et al., 2006) is misleading"**: The paper explicitly says "This problem can be approximately converted to minimize ∥AW∥₁ (Candès et al., 2006)" — this is a standard framing done approximately and the paper immediately qualifies it by noting that activation distribution also matters. The criticism overstates the issue.

- **"The paper's presentation overclaims by stating 'state-of-the-art' without caveats about training overhead" (framed by the harsh critic as fatal/structural)**: Down-graded to Major above. The paper does disclose the training; the issue is framing, not deception.

- **"Inference speed experiment is valuable" / other strengths from Strength Finder that are generic or conflict with verified weaknesses**: Kept the concrete strengths; any generic or sycophantic praise removed.

- **"The method may be sensitive to initialization — no experiments explore this"**: This is speculative. The paper initializes to identity (unstructured) or SliceGPT's PCA (structured), which are natural choices. Without evidence that other initializations would produce different results, this is not a concrete weakness.

- **"Gains diminish for larger models — this deserves discussion"**: The paper shows consistent improvements at all sizes tested (125M to 8B). The claim of "diminishing" is not verified from the numbers available in the text (Table 2 is an image).

## Novel Insights

The reviews surface an important nuance: RotPruner's contribution is best understood not as a new pruning algorithm but as a *space-transformation layer* that can wrap existing pruning methods. The strongest evidence comes from Table 1 (same method, different spaces) and Table 9 (same method with/without rotation across multiple base methods). The paper's framing as "state-of-the-art versus SparseGPT" distracts from what is actually the cleaner scientific claim: that the representation space in which pruning operates matters, and that a lightweight learned rotation can substantially improve any base pruning method. An interesting observation from cross-referencing the reviews is that the method's 1.006× inference overhead is remarkably small given that it adds O(L·d²) parameters — this is worth highlighting more prominently in the paper as evidence of practicality.

## Suggestions

- **Reframe the contribution**: Position RotPruner as an *augmentation* technique ("RotPruner improves any base pruning method by learning a rotation before pruning") rather than as a stand-alone method competing with one-shot baselines. Move the apples-to-apples comparisons (RotPruner+Wanda vs. Wanda; RotPruner+SparseGPT-mask vs. SparseGPT-mask) from the ablation (Table 9) to the main results table.

- **Specify the mask update schedule**: Replace "after several iterations" with the exact schedule (e.g., "masks are recomputed at the beginning of each epoch" or "every k iterations").

- **Add comparison against at least one training-based method** (e.g., ADMM-pruner or FISTAPruner) to give readers a reference point for the training overhead trade-off.

- **Include a larger model experiment** (e.g., LLaMA-2-13B or LLaMA-3-70B) or at minimum an explicit discussion of the scaling behavior and memory constraints.

- **Add confidence intervals** for at least one experimental setting to demonstrate that the improvements are statistically significant given the training variance.

- **Quantify the memory overhead** of the rotation matrices explicitly, and clarify whether they can be freed or fused post-training.
