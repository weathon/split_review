Now I'll produce the final consolidated review.

---

## Summary

This paper proposes SVD-Space Alignment (SSA), a local training framework that decomposes each layer's weight matrix into its SVD components (U, S, V^T) before training and uses Direct Feedback Alignment (DFA) with a custom composite loss to update them locally. A dynamic rank reduction strategy progressively reduces model size during training. The paper reports accuracy within ~0.2% of backpropagation on CIFAR-10 (VGG-13) with substantial memory and compute savings, and shows SSA can train convolutional layers where standard DFA struggles.

## Strengths

- **Competitive accuracy with BP on CIFAR-10 using local updates**: The paper states SSA achieves accuracy within 0.2% of backpropagation on CIFAR-10 with VGG-13 (Section 5.1, Table 2). Given that DFA-based methods have historically struggled to match BP accuracy on deeper networks, this is a notable result. Results are reported as mean ± std over 5 runs (Table 1).

- **50% memory and 40% compute reduction documented**: Section 3.5 provides a formal complexity analysis showing SSA's per-layer cost transitions from O(m×n) (BP) to O(m×r + r + r×n), and Figure 2 shows per-layer memory/compute savings for ResNet-32, MobileNetV1, and VGG-13.

- **SSA trains convolutional layers where DFA cannot**: Section 6.1 and Tables 4/5 show SSA outperforming DFA variants (uSF, brSF) on CIFAR-10 and ImageNet. Section 3.1 provides a spatial decomposition technique for convolution kernels that preserves spatial structure, directly addressing a known DFA limitation.

- **Ablation study validates each loss component**: Table 3 (Section 5.3) systematically removes each of the five loss terms and reports the impact on accuracy and efficiency, providing empirical evidence that each term serves a distinct role.

- **Dynamic rank reduction combining epoch-based scheduling with energy threshold**: Section 3.4 introduces a two-phase strategy that mitigates overly-aggressive late-stage reduction, a practical concern often overlooked in low-rank training.

## Weaknesses

### Major

- **Unsustained theoretical convergence claims**: The abstract states "With strong theoretical convergence guarantees," the contribution list says "We provide theoretical convergence guarantees" (line 26), and the conclusion asserts "Theoretical analysis guarantees convergence of our loss objectives" (line 274). However, the main text contains **no theorem, lemma, proof sketch, or convergence analysis of any kind**. The only use of "theoretical analysis" in the body (line 177) refers to hyperparameter selection via ablation studies. This is a central claimed contribution that is entirely unsubstantiated in the presented text. If the proof was relegated to the appendix (which is inaccessible), the paper would still need at least a theorem statement in the main body. The authors should either provide the analysis or remove the claims.

### Minor

- **Rank reduction mechanics are underspecified**: Section 3.4 gives a formula for r_k (Eq. 8) and mentions the Hoyer regularizer "sparsifies" singular values, but never explains what happens to the parameter tensors when rank drops. If U ∈ ℝ^{m×r} and rank reduces to r' < r, are columns of U/V^T truncated? What happens to optimizer states and gradient buffers after truncation? Does training continue smoothly through the discontinuity? Without these details, the method is not fully reproducible and the claimed memory/compute savings cannot be independently verified.

- **Misleading notation L_CE(θ_i)**: The loss is written as L_CE(θ_i) where θ_i = (U_i, S_i, V_i^T) — the SVD components of layer i. But lines 82–84 clarify that this is the *global* cross-entropy loss: "This loss is the model cross entropy loss" and "The feedback error comes from the derivative of the entire model's cross entropy loss." The notation therefore implies the CE loss is a function of a single layer's parameters, which is incorrect. This muddies the algorithm description unnecessarily.

- **Cosine similarity loss dimensionality for convolutional layers not addressed**: Equation (5) defines a cosine similarity between layer_output = layer_input·(USV^T) and the feedback signal (B_U B_S B_V^T)^T·e. For convolutional layers, layer_output is a 4D feature map (batch × channels × height × width), while the feedback signal after projection has a different structure. The paper does not specify how these are reshaped or tensor-contracted to make cosine similarity well-defined, nor how the spatial structure is preserved in this comparison.

- **Convergence comparison only on a 3-layer MLP**: Figure 3 compares convergence rates using a minimal MLP (3 layers) rather than the convolutional architectures where the method's core claims are evaluated. The paper acknowledges this (line 252: "To ensure uniformity in comparisons, the plotted results focus on MLPs") because DFA variants cannot be applied to convolutions, but this means the convergence behavior of SSA on the architectures that matter most (VGG-13, ResNet-32) is uncharacterized.

- **No wall-clock training time comparison**: The paper reports FLOPs reductions (Figure 2) but provides no actual runtime comparison. SVD-based computations involve multiple small matrix multiplications that may not translate to proportional wall-clock speedups on GPU hardware due to kernel launch overhead and reduced arithmetic intensity. A runtime comparison would strengthen the practical efficiency claims.

### Trivial

None.

## Nice-to-Haves

- A simple runtime table (hours/epoch or total training time) comparing SSA against BP and SVD-BP on the same hardware would meaningfully strengthen the efficiency claims.
- The one-time SVD initialization cost per layer (O(min(mn², m²n))) should be acknowledged and quantified, especially for large layers.

## Removed Points

The following points from the inputs were removed with brief justification:
- **Tables as images / unreadable numbers**: Parser artifact — the original submission has proper tables.
- **SVD-BP comparison fairness**: The paper includes SVD-BP as a baseline (Section 4); numerical values are in image tables (parser artifact).
- **DFA loss ambiguity (whether local vs global CE)**: The paper clearly states L_CE is the global CE loss (lines 82–84). Remaining notation imprecision is kept as Minor above.
- **Unfair comparison (low-rank vs full-rank)**: The comparison is between training methods, not architectures. SSA's ability to achieve BP-level accuracy at lower rank is the claimed contribution, not a flaw.
- **Update-locking**: DFA inherently avoids update-locking, and SSA inherits this property — no evidence it's violated.
- **Overstatement about prior conv-layer local methods**: Not verifiable from paper alone; the critic's counter-claim is unsupported by specific evidence.
- **Quasi-convexity claim**: A passing remark in the hyperparameter section; not central to the paper's claims.
- **Limitations about linear separability**: Already acknowledged as a limitation in Section 6.2 by the authors.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's stated findings and surface the same concerns about overclaimed theory and underspecified mechanics.

## Suggestions

1. Remove or substantially moderate the convergence guarantee claims, or add a theorem statement (even a basic one) to the main text.
2. Explicitly describe the rank-truncation procedure: when r_k drops at epoch boundaries, specify exactly how U, S, V^T tensors are resized, what happens to optimizer state, and whether training continuity is preserved.
3. Correct the notation L_CE(θ_i) to clarify that the cross-entropy error signal is global and shared across layers, not a per-layer function of layer i's parameters.
4. For the cosine similarity loss on convolutional layers, specify the reshaping/vectorization procedure that makes the cosine similarity well-defined between feature maps and feedback signals.
5. Add a wall-clock runtime comparison to validate that the FLOPs reductions translate to actual speedups.

## Score and Decision

The paper addresses a real and underexplored problem — combining SVD decomposition with DFA for local training — and presents suggestive empirical results. The core algorithmic idea has merit, and the experiments offer preliminary evidence that the approach works. However, the paper is held back by two significant issues: (1) it repeatedly claims "strong theoretical convergence guarantees" without providing any theory whatsoever, even a theorem statement; (2) the rank reduction mechanics are not fully specified, affecting reproducibility. These are fixable with revisions, but in its current form the paper does not meet the ICLR bar.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>