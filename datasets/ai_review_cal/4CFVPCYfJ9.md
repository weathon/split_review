- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 8, 5, 6
Now I have a thorough understanding of the paper. Let me verify the key claims against what's actually in the paper and synthesize the review.

**Verification of Critic Points Against Paper:**

1. **Error bars**: Tables 1, 2, 3 all show single numbers. The paper's Section 5.6 heading says "ROBUSTNESS TO NOISE, ERROR-BAR..." and references appendices, but the main tables lack variance info. ✓ Verifiable from main text.

2. **MLP-only control**: Table 5 ablates SVQ components (SVQ with/without MAE loss) but never tests SimVP + MLP without the codebook matrix. The method description confirms SVQ = MLP(En(X)) → W (dim N) → Q = W @ M → output. Removing M would require an alternate projection. ✓ Verifiable gap.

3. **Theorem 4.1 quality**: Lines 151-189 show unclear notation (ΔΩ^β undefined, T(β,δ) loosely defined), missing algebraic steps, and no connection to the one-step ISTA approximation used in practice. ✓ Verifiable.

4. **Table 4 VQ hyperparameters**: The paper states SVQ codebook sizes (line 200) but does not give codebook sizes or tuning details for the comparison VQ methods in Table 4. ✓ Verifiable.

---

## Summary

This paper proposes **Differentiable Sparse Soft-Vector Quantization (SVQ)** , a plug-in module for spatio-temporal forecasting that replaces hard VQ with a differentiable soft assignment. SVQ approximates one step of sparse regression via a two-layer MLP that generates combination weights over a large codebook, enabling end-to-end gradient flow. Empirically, SVQ is tested across five benchmark datasets and 11 backbone architectures, yielding consistent improvements (e.g., 7.9% MSE reduction on WeatherBench-S, 9.4% average MAE reduction on video prediction). An interesting finding is that a frozen random codebook performs nearly as well as a learned one when the codebook is large.

## Strengths

1. **First VQ method shown to improve spatio-temporal forecasting**: The paper demonstrates experimentally (Table 4, Figure 1) that prior VQ methods (VQ-VAE, Residual VQ, Grouped Residual VQ) degrade forecasting performance, while SVQ consistently improves it. On WeatherBench-S, SVQ reduces MSE from 1.105 to 1.018 (7.9% improvement over the best baseline).

2. **Fully differentiable quantization via MLP-approximated sparse regression**: The derivation from one-step ISTA to a two-layer MLP (Section 3.1, Eqs. 2–4) provides a principled basis for the method. The differentiability avoids the training instability and codebook collapse that plague standard VQ (Figure 6 shows VQ's MSE exceeding 10 while SVQ remains stable).

3. **Consistent improvement as a plug-in across 11 backbone architectures**: Table 3 shows SVQ improves every MetaFormer tested (CNN-based, Transformer-based, MLP-based), with average MSE reduction of 4.8% and MAE reduction of 6.0%. The effect is largest for MLP-based models (10.7% MSE reduction), indicating architecture-agnostic benefit.

4. **Robustness to codebook size and the finding that large random codebooks work well**: Figure 5 shows SVQ's performance is stable over a wide range of codebook sizes (unlike GRVQ, which degrades at large sizes). Table 7 shows that with a codebook of size 10,000, a randomly initialized frozen codebook performs nearly identically to a learned one (1.023 vs. 1.018 MSE, only 0.5% difference), a practically useful property.

## Weaknesses

### Fatal

None.

### Major

1. **Missing variance information in main results (Tables 1, 2, 3)**: All reported results are single numbers with no standard deviations, confidence intervals, or number of random seeds stated. The paper mentions "error-bar" in the Section 5.6 heading and refers to an appendix, but the main tables present no reliability statistics. Some improvements are small in absolute terms (e.g., MAE on WeatherBench-M from 0.201 to 0.194), making it impossible to assess statistical significance from the main paper alone. While the extensive consistency across datasets and backbones partially mitigates this, it is a clear omission.

2. **Missing ablation control for the MLP alone without the codebook**: SVQ consists of (i) a two-layer MLP that produces regression weights, (ii) a dot product with the codebook matrix, and (iii) an MAE loss for sparsity. The ablation in Table 5 compares SimVP only (1.105) with SimVP+SVQ (1.018) but never tests SimVP + the same two-layer MLP with the codebook removed (replaced by a linear projection from N back to C'). Without this control, it is not possible to confirm that the quantization mechanism itself drives the improvement rather than the added nonlinear capacity. Adding other VQ methods (Table 4) does provide indirect evidence that "more capacity alone" is insufficient (since those methods also add parameters but hurt performance), but a direct control is needed.

### Minor

3. **Theorem 4.1 is poorly presented and insufficiently connected to the method**: The theorem and its proof sketch (lines 151–189) use unclear notation (e.g., "ΔΩ^β" is not defined, "T(β,δ)" is introduced without clear definitions of β). The algebraic steps are gapped and do not logically flow. More importantly, the theorem's relationship to the specific one-step ISTA approximation used in SVQ is not established. The paper's contribution is primarily empirical, and this theoretical section does not add credible support. It should either be substantially rewritten or removed.

4. **Hyperparameters for comparison VQ methods in Table 4 not specified**: The paper notes that GRVQ's performance depends on codebook size (Figure 5) and that codebook tuning is important for clustering-based VQ, but does not report the codebook sizes, learning rates, or training configurations used for the VQ methods compared in Table 4. Without this information, the fairness of the comparison is not fully verifiable.

5. **Claim of being "the first approach that demonstrates a boosting effect" is overly assertive**: While the paper convincingly shows that prior VQ methods hurt performance and SVQ helps, the claim of "first" is difficult to verify definitively. This is a minor overclaim.

### Trivial

- Figure 1's "MSE improvement percentage" is not explicitly defined in the caption or surrounding text.
- Table 4 would benefit from including the baseline SimVP MSE value for direct comparison.

## Nice-to-Haves

- A computational cost comparison (parameters, runtime) between SVQ and the baseline SimVP (Figure 3 currently only compares SVQ vs. SVQ-raw).
- Clarification of how ISTA hyperparameters η and λ are handled in practice (absorbed into learned weights?).
- Codebook sizes used for comparison VQ methods in Table 4.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Reproducibility nitpick about hyperparameters not in main text (learning rate, optimizer, scheduler, epochs)**: Per guidelines, the paper references appendices for training details, and minor implementation details not in the main text are not a valid weakness. Removed.

- **General formatting/presentation style criticisms**: Any stylistic nitpicks that don't affect the substance are removed per guidelines.

- **Criticisms about the appendix content being missing**: The parser strips appendices; they exist in the original submission. Removed per hard rule.

## Novel Insights

The synthesis of the reviews surfaces one insight beyond the paper's own framing: the missing MLP-only ablation is the single most actionable gap. If the authors can show that an MLP of equal size without the codebook yields substantially smaller gains (or no gains), the paper's core narrative — that the sparse quantization mechanism, not just added capacity, is responsible — would be decisively supported. Conversely, if the MLP alone recovers most of the improvement, the paper would need to reframe its contribution around the differentiable soft-VQ formulation's training stability benefits rather than representational advantages per se.

## Suggestions

1. **Add error bars to all main tables.** Report results over at least 3 random seeds. This is the single most impactful improvement for the paper's credibility.
2. **Add the missing ablation**: SimVP + MLP (same architecture as SVQ's weight-generating MLP) with a linear projection replacing the codebook, matched in parameter count.
3. **Substantially rewrite or remove Theorem 4.1.** In its current form it is not coherent enough to support any claim. A clean empirical justification (which the paper already largely has) is preferable to a garbled theoretical one.
4. **Report codebook sizes and tuning details** for the VQ methods compared in Table 4.
