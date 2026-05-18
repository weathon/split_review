Now I have a thorough understanding of the paper and the reviews. Let me write the consolidated review.

## Summary

This paper proposes NEPENTHE, an iterative unstructured pruning method that uses neuron-level entropy to guide pruning toward eliminating entire layers in rectifier-activated neural networks. The core idea is to concentrate pruning on low-entropy layers (where neurons are already nearly always ON or OFF) so they become linearizable and can be removed. Experiments on ResNet-18, MobileNet-V2, and Swin-T across multiple datasets show that NEPENTHE can remove several layers with little or no accuracy loss.

## Strengths

- **Empirically demonstrated layer removal across diverse architectures and activations**: NEPENTHE successfully removes 3/17 layers from ResNet-18 on CIFAR-10 (Table 1) while improving top-1 accuracy (92.55% vs. 91.66% dense). The method is validated on CNNs (ResNet-18, MobileNet-V2) and a Transformer (Swin-T), and across five activation functions (Table 4: ReLU, SiLU, PReLU, LeakyReLU, GELU), showing genuine architecture-agnostic operation.

- **Well-designed ablation study isolating each component's contribution**: Table 3 sequentially ablates the entropy-weighted budget, the "don't care" state handling, and the neuron-selection mechanism. Each addition improves accuracy (from 92.18% to 92.55%) while maintaining the same 3/17 removed layers, providing clean evidence that all three design choices contribute to NEPENTHE's effectiveness.

- **Honest discussion of limitations**: Section 4.4 acknowledges that the method struggles with already parameter-efficient or underfitting architectures (e.g., ResNet-18 on ImageNet), scoping the contribution to over-parameterized regimes where it is genuinely useful.

- **Conceptually novel framing**: Using unstructured pruning to drive *layer-level* linearization (rather than just weight-level sparsity) is a creative and non-obvious application of entropy-based budget allocation, distinct from prior width-focused pruning and from explicit depth-reduction methods like Layer Folding.

## Weaknesses

### Fatal
None.

### Major

- **The theoretical derivation in Section 3.2 is mathematically flawed.** The paper models the pre-activation $Z$ as a *single product* of one weight and one input ($Z = W \cdot X$), deriving its distribution using the product-of-Gaussians result (Bessel function, Eq. 6). In reality, a neuron's pre-activation is $z = \sum_{j=1}^N w_j x_j$ — a *sum* of $N$ such products. In the "large $N$ limit" the paper itself invokes, this sum converges to a Gaussian by the Central Limit Theorem, *not* to the Bessel-function distribution shown. The subsequent derivation of $p[Z>0]$ and entropy as a function of threshold $t$ (Eqs. 7–9, Fig. 3c) is therefore built on an incorrect starting point. **Why this matters:** The paper lists this as a contribution ("we suggest from a theoretical perspective that unstructured pruning... reduces the layer's entropy"). An incorrect proof cannot support this claim. Fortunately, the empirical observation (Table 1) — that pruning reduces entropy — stands independently, and the NEPENTHE method does not depend on the flawed derivation. The theory section should be removed or completely rewritten. This is a Major issue because it undermines the paper's claimed theoretical contribution, but not Fatal because the method and empirical results remain valid.

- **The paper does not demonstrate actual computational benefits from the claimed depth reduction.** The abstract and introduction motivate NEPENTHE by the need to reduce computational burden, and the conclusion claims "practical impact even in computation on parallel architectures... as it inherently reduces the critical path." Yet the experiments report only top-1 accuracy, layer entropy, and the count of "removed layers." No FLOPs reduction, inference latency, or model size after layer folding is provided. Furthermore, the paper never specifies *how* a zero-entropy layer is physically removed from the computational graph — Algorithm 1 only prunes weights and returns weights; it never executes layer removal or folding. The evaluation counts layers with $\widehat{\mathcal{H}}_l = 0$ as "removed" without verifying that they can be excised without modifying the forward pass or measuring the resulting speedup. **Why this matters:** The paper's core applied claim is that NEPENTHE reduces a network's depth in a practically meaningful way. Without reporting computational metrics or implementing actual removal, this claim is unsubstantiated.

- **The role of the "removed layers" claim vs. actual implementation is unclear.** The paper says a layer with $\widehat{\mathcal{H}}_l = 0$ "can be removed entirely" and "absorbed by the following layer" (Sec. 3.1, line 179 ff.), and that neurons always OFF "can be simply pruned" while neurons always ON "can in principle be absorbed by the following layer." But Algorithm 1 never performs removal — it only prunes weights, retrains, and checks accuracy. The paper conflates "has zero entropy" with "is removed," leaving the reader uncertain whether the layers were actually excised or merely identified as removable. This needs clarification and, ideally, a demonstration of post-removal forward-pass correctness.

### Minor

- **No error bars or multiple runs reported.** All results appear to be from single runs. While this is common in pruning papers, the lack of statistical variability makes it impossible to assess whether the observed number of removed layers is consistent or coincidental.

- **GELU is not a rectifier activation function.** The paper repeatedly calls GELU a "rectifier activation function" (line 33, line 401). GELU is smooth, not rectified. This is a minor terminology inaccuracy — the method empirically works with GELU, so it does not affect the results, but the framing should be corrected.

- **Cost of entropy computation not discussed.** Computing $\widehat{\mathcal{H}}_l$ requires evaluating neuron states over the entire training set at each pruning iteration (Algorithm 1, line 259). For large models and datasets (e.g., Swin-T), this overhead could be substantial. The paper should at least acknowledge this cost.

### Trivial
None.

## Nice-to-Haves

- **Control experiment with uniform pruning allocation:** An ablation that prunes the same total number of weights per iteration but allocates them uniformly across layers (or proportional to layer size) would isolate whether the entropy-guided budget, rather than iterative retraining alone, drives layer-level linearization.
- **Comparison with a simple thresholding baseline:** For example, removing layers where the fraction of always-ON or always-OFF neurons exceeds a threshold would help contextualize NEPENTHE's advantage.

## Removed Points

- The harsh critic's claim that "the reference to 'the large use of rectifier activation functions such as ReLU, GELU, and Leaky-ReLU' is inaccurate" regarding GELU — this is kept as a Minor weakness because it is a genuine terminology error, though minor. *(Actually kept, not removed.)*
- The harsh critic's criticism about missing tables (`\input{sections/main_table}`, `\ref{tab:results_cifar-10}`) — **Removed.** These are LaTeX includes stripped by the parser; they exist in the original submission.
- The harsh critic's criticism about typos (`\corr`, `\|\mathcal{D}\|_0`) — **Removed.** These are parser artifacts from LaTeX rendering, not author errors.
- The Strength Finder's strength #1 ("Theoretical grounding linking unstructured pruning to entropy reduction") — **Removed.** Conflicts with the verified weakness that the theoretical derivation is mathematically flawed.
- The Strength Finder's strength #5 ("Practical impact on computational efficiency in parallel hardware") — **Downgraded.** The paper claims this but provides no measurements, so it is a claim rather than a demonstrated strength.
- The harsh critic's sub-criticism #3 about Eq. 8 notation ("$\frac{1}{\|\boldsymbol{w}_{l,i}\|_0}|w_{l,i}|$ is ambiguous") — **Removed.** The notation is standard for per-neuron weight vectors and is clear in context.
- The harsh critic's sub-criticism that zero-entropy layers remain in $L$ and affect $\sum \mathcal{I}_j$ — **Removed.** When $\mathcal{I}_l = 0$, $\mathcal{R}_l = 0$, so $\exp(0)=1$ in the softmax gives negligible budget. This is a trivial inefficiency, not a structural flaw.
- The harsh critic's suggestion to "Replace the flawed theory with an empirical justification" — kept as implicit in the Major weakness; the specific suggestion is redundant.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the key tension: the empirical phenomenon (pruning reduces entropy) is real and well-demonstrated, but the attempted mathematical explanation is incorrect. This suggests the phenomenon may have a different underlying mechanism than the one postulated.

## Suggestions

1. **Remove or completely rewrite Section 3.2.** The empirical observation (Table 1) that pruning reduces neuron entropy is sufficient motivation for the method. An incorrect derivation weakens rather than strengthens the paper.
2. **Measure and report computational impact.** After identifying zero-entropy layers, physically fold them into adjacent layers (or implement the forward pass without them) and report FLOPs, inference latency, and/or model size. Without this, the practical claim is unsupported.
3. **Clarify the algorithm's handling of zero-entropy layers.** Specify whether layers are removed from the computational graph during or after training, and how always-ON neurons are "absorbed" by the following layer.
4. **Add error bars or multiple seeds** to key results, at least for the main CIFAR-10 experiment, to establish consistency.
5. **Correct the terminology** regarding GELU not being a rectifier.

## Score and Decision

The paper proposes a genuinely novel and empirically validated approach to depth reduction via entropy-guided pruning. However, it contains a mathematically flawed theoretical derivation presented as a contribution, and it fails to measure the computational benefits that motivate its own framing. These are significant but fixable issues. The core empirical contribution (NEPENTHE method + validation) is solid and could be publishable after revision. In its current form, the paper is borderline and requires major revision.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>