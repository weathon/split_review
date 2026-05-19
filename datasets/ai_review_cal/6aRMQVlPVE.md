- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes TDLRT, a training-time compression method for convolutional layers that parameterizes each convolutional kernel in Tucker tensor format and adaptively adjusts the Tucker ranks during training. The algorithm leverages dynamical low-rank approximation theory, introducing a change of variables ($K_i = U_i S_i$) to eliminate stiff terms that arise from the high curvature of the low-rank Tucker manifold. Theoretical guarantees (loss descent and approximation bounds) are provided under exact ODE integration. Experiments on CIFAR-10 (AlexNet, VGG16, ResNet18) and MNIST/LeNet5 demonstrate high compression rates (>95% for VGG16) with accuracy comparable to or exceeding the full baseline.

## Strengths

1. **First rank-adaptive training algorithm for convolutional layers in Tucker format.** Algorithm 1 automatically adjusts Tucker ranks during training via a basis-augmentation step (lines 5–6) and a rank-adjustment step (lines 10–12). The paper explicitly claims this as a first and the algorithm is a genuine contribution to the low-rank training literature, where prior work (e.g., Schotthöfer et al., 2022) only handled matrix-valued layers.

2. **Theoretical guarantees of loss descent and approximation independent of ill-conditioning.** Theorems 2 and 3 prove that the method ensures loss descent (Theorem 2) and that the low-Tucker-rank filter approximates the full filter with error bounds that do not depend on higher-order singular values (Theorem 3). This directly addresses a known failure mode of prior low-rank methods (stiffness from equation 7, slow convergence cited in Section 1).

3. **Efficient handling of convolutional layers without matricization via the $K_i$ construction.** Theorem 1 uses a QR decomposition of $\mathrm{Mat}_i(C)^\top$ to construct $K_i$, which avoids the $O(n_i \prod_{j\neq i} r_j^2)$ computational cost that "would render the resulting training method impractical" (Section 3). This is a nontrivial improvement over a naive extension of matrix DLRT to tensors.

4. **Strong compression-accuracy results across multiple architectures.** Table 1 and Figure 1 show TDLRT achieves the best compression rates on CIFAR-10 for AlexNet (90.1% c.r.), VGG16 (95.3% c.r., matching/exceeding baseline accuracy), and ResNet18 (93.9% c.r.), outperforming competing factorization and pruning baselines.

5. **Empirical robustness to ill-conditioned ranks.** The MNIST experiment (Figure 2, right panel) demonstrates that TDLRT converges faster and more robustly than standard Tucker and CP training when ranks are overestimated with exponentially decaying singular values, validating the theoretical claim that the method does not suffer from ill-conditioning.

## Weaknesses

### Fatal
None.

### Major

1. **Training wall-clock time is not measured, leaving the "reduces training costs" claim partially unsupported.** The abstract claims the method "drastically reduces the training costs." However, Section 4.2 only reports *inference* time and memory footprint. The paper does not report wall-clock time per epoch, total training time to target accuracy, or peak GPU memory *during training* for the full pipeline (including QR decompositions, SVD truncation, and rank-adaptation overhead). Parameter count reduction during training is demonstrated (and is genuine), but whether the method's overhead offsets these savings in wall-clock time remains unknown. This is the most consequential gap in the empirical evaluation.

2. **The algorithm's computational overhead is not quantified.** The rank-adaptation steps (line 6: basis augmentation doubling the rank each iteration; line 11: truncated Tucker decomposition of a $2r$-sized core tensor) add non-trivial per-iteration cost. The paper does not measure how much overhead these operations introduce relative to a standard forward/backward pass. The discussion acknowledges that "alternative techniques... may lead to a boost in computational performance" but provides no measurement of the current implementation's overhead.

### Minor

1. **Gap between theoretical guarantees (exact ODE integration) and practical implementation (SGD with momentum).** Theorems 2 and 3 assume "the one-step integration from 0 to λ is done exactly," but the implementation uses SGD with momentum on mini-batches. The paper cites Scieur et al. (2017) to justify the connection, but the cited reference addresses deterministic accelerated methods under full-gradient assumptions, not stochastic mini-batch settings. The paper does not discuss how stochasticity and discretization error affect the theoretical guarantees. While this type of gap is common in ML theory papers, it should be acknowledged more explicitly.

2. **No rank evolution plots during training.** The paper claims rank-adaptivity as a key property, yet never shows how the Tucker ranks of individual layers evolve over training epochs. This is a straightforward and informative addition that would directly support the claimed contribution.

3. **Hyperparameter details for fixed-rank baselines are incomplete.** The rank of fixed-rank baselines is set as $\hat{r} = \kappa r_{\mathrm{max}}$, but the actual values of $\kappa$ used in the experiments are not reported. Similarly, momentum=0.1 is unusually low and no ablation or tuning discussion is provided.

4. **No sensitivity analysis for the tolerance parameter $\tau$.** The paper states that "larger values of $\tau$ yield smaller Tucker ranks and thus higher parameter reduction" but does not systematically study how accuracy varies with $\tau$ across datasets (Figure 1 shows some variation but a dedicated table or ablation would strengthen the paper).

### Trivial

- The abstract and Section 1.1 use slightly different fonts for "training costs" vs "training compression rates," making the central claim appear broader than what is measured.
- The text in Section 4.2 says "computational performance in inference and training" but then only evaluates inference time and memory footprint.
- Algorithm 1 pseudocode uses a mix of mathematical notation and informal descriptions (e.g., "descent step; direction $\nabla_{K_i}\mathcal{L}(\dots)$") that could be more precise.

## Nice-to-Haves

- A comparison of TDLRT against matrix DLRT applied to matricized convolutions on the MNIST robustness experiment, to isolate the benefit of the tensor format over an already rank-adaptive matrix method.
- Studying convergence speed (epochs to a given validation loss or accuracy) as an additional metric.
- An empirical investigation of the "low-rank winning ticket" assumption (e.g., comparing SVD of trained full kernels to obtained Tucker ranks).

## Removed Points

These points from the harsh critic were checked against the paper and removed with justification:

1. **"Inconsistent claim about VGG16 accuracy — Table 1 shows both at 93.6%."** The paper's text clearly states TDLRT "exceeds the baseline on average for τ = 0.03" at 95.3% compression. The surrounding text describes the full baseline accuracy as lower. The harsh critic likely misread the image-embedded table. REMOVED (factually incorrect).

2. **"The paper should remove or separate pruning baselines."** The paper acknowledges the distinction ("methods based on factorizations yield an analogous compression rate during the entire training process") and including pruning baselines for a comprehensive compression comparison is standard practice. The comparison is not misleading — it reports post-training compression rates for all methods side-by-side. DEMOTED from the review (scope creep / not a genuine flaw).

3. **"The paper does not discuss how to choose τ."** The paper does discuss that τ controls compression (Section 3.1: "larger values of τ yield smaller Tucker ranks and thus higher parameter reduction") and Figure 1 shows results for different τ regimes. More systematic sensitivity analysis would be nice but the paper is not silent on this. DEMOTED to a minor point above, which is fair.

4. **"The ε-close assumption is phrased informally."** The paper connects this to the "winning ticket" hypothesis and the informal phrasing is typical for theoretical assumptions in this literature. This is a standard type of assumption, not an error. REMOVED (standard practice).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Most impactful: measure and report wall-clock training time** (epoch time or total time to target accuracy) and peak GPU memory during training for the CIFAR-10 benchmarks, compared against both the full baseline and the fixed-rank Tucker/CP baselines. This directly addresses the main empirical gap and would support the central claim.
2. Add rank evolution plots (per-layer Tucker ranks vs. epochs) to directly illustrate the claimed rank-adaptivity.
3. Acknowledge the theory-practice gap (exact ODE vs. SGD) more explicitly, perhaps adding a remark that the theorems are a conceptual/motivational justification rather than a guarantee of the SGD-based implementation.
