Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper introduces HyResPINNs, a novel PINN architecture that combines DNN and RBF components within hybrid residual blocks using learnable convex combination weights (α). The architecture also employs adaptive skip connections (β) between blocks and compactly supported Wendland C⁴ kernels for computational efficiency. The central claim is that HyResPINNs achieve "orders of magnitude greater accuracy" than standard PINNs and several strong baselines (ExpertPINNs, ResPINNs, PirateNets, StackedPINNs) on Allen-Cahn and Darcy-Flow problems.

## Strengths

1. **Novel hybrid architecture with dynamic DNN/RBF balancing**: The paper introduces a genuinely underexplored idea — combining a standard DNN with an RBF network inside residual blocks via a sigmoid-gated convex combination parameter α per block (Eq. 6, Section 3.1). This is a clear architectural innovation over prior work like PirateNets (which use adaptive residuals but lack an RBF branch) and stacked PINNs. The motivation — leveraging smooth (neural) and non-smooth (RBF) approximators for different solution features — is well-grounded and addresses a known PINN limitation.

2. **Adaptive skip connections (β) for flexible information flow**: Beyond the intra-block α parameters, the paper incorporates inter-block adaptive connection weights β^(l) (Section 3.1), extending the PirateNets-style adaptive residual concept to a hybrid DNN-RBF setting. This provides an additional mechanism for controlling layer-wise information flow.

3. **Compactly supported Wendland C⁴ kernels for sparsity and efficiency**: The use of Wendland C⁴ kernels (Section 3.2) — which are compactly supported and yield sparse kernel matrices — is a principled engineering choice that addresses the scalability challenge of RBF networks while preserving their ability to capture sharp local features. Each τᵢ is trainable, giving the model flexibility to learn appropriate length scales.

4. **Principled regularization of α**: The L₂ penalty on α (Eq. 2, Section 3.1) explicitly prevents over-reliance on the RBF component, promoting smoother solutions and stable training. This goes beyond simple architecture design by providing learnable control over function regularity.

5. **Qualitative evidence of improved sharp-feature capture**: Figure 4 (wrapfigure) shows a visual comparison on the 2D Allen-Cahn equation, where the HyResPINN solution visibly tracks sharp transitions better than the standard PINN, which smooths over them. This provides some visual support for the core claim even without the (parser-omitted) quantitative table.

## Weaknesses

### Fatal
None. The core idea is novel and sound, the method is clearly described, and no fundamental methodological flaw invalidates the approach.

### Major

- **Missing architectural specifications for the RBF component**: The paper does not specify how many RBF centers are used per residual block, how they are initialized, or whether centers are shared across blocks or independently trained. The method section (Section 3) describes the RBF kernel form and that centers are trainable, but the number N_c per block is never stated. These details are crucial for reproducibility and for understanding the model's capacity. Even accounting for content potentially in the parser-removed experiment subsections, the core method section should specify this.

- **Global α per block limits spatial adaptivity**: The combination parameter α is a single scalar per residual block, meaning the same DNN-vs-RBF trade-off applies uniformly across the entire input domain for that block. This partially contradicts the paper's motivation that RBFs capture "localized, discontinuous or sharp features" (line 54) while DNNs capture "continuous, global behaviors" (line 53). A spatially varying α (e.g., α as a function of input) would be more naturally aligned with this motivation. While different blocks can learn different α values, the paper does not discuss this limitation or justify why a block-global α is sufficient.

### Minor

- **No ablation isolating the adaptive α/β mechanism**: The paper claims benefits from adaptive α and β, but there are no reported experiments where these are fixed (e.g., α=0.5 constant, β=1 constant). Without such ablations, it is unclear whether the improvement comes from the hybrid block structure itself or specifically from the adaptivity. The missing experiment subsections (`\input{...}`) may contain some ablations, but this should be explicitly reported.

- **No analysis of how α evolves during training**: The paper claims α adaptively balances DNN/RBF contributions, but provides no plots of α values over training for any problem. Such visualization would substantially strengthen the narrative that the model learns the intended behavior (e.g., α → higher values near sharp features).

- **Experimental hyperparameters incompletely reported**: While the paper states that all methods use "exactly the same hyper-parameter settings" (line 252) and follows experimental procedures from prior works (line 256), it does not report specific values for: number of residual blocks, layer widths per block, learning rate schedules, number of training iterations, mini-batch sizes, regularization strength λₚ for the α-penalty, or collocation point selection strategies. These are standard reporting expectations for empirical PINNs papers. Some of these may appear in the missing experiment subsections, but given their importance, they should be stated in the main experimental setup.

- **The regularization on α encourages DNN, not RBF, usage — this is presented as a feature but could limit the model's ability to exploit RBFs**: The L₂ penalty on α penalizes large α values (Eq. 2), which "encourages smoother solutions" (line 177). This is by design and not a contradiction, but the paper does not discuss how λₚ is chosen or what happens when sharp features require large α. If λₚ is too large, the regularization could suppress exactly the RBF behavior the architecture is designed to provide.

### Trivial

- The architecture diagram (referenced via `\input{resblock_diagram_vert}` and `\input{fullarchitecture_diagram}`) is not visible in the extracted text. While this is a parser artifact, the paper would benefit from ensuring these diagrams are embedded as actual figure includes rather than LaTeX `\input{}` commands for robustness.

## Nice-to-Haves

- **Comparison with a simple ensemble baseline**: An RBF network and DNN whose outputs are averaged (non-residual, non-adaptive) would isolate the contribution of the residual block structure itself.
- **Application to problems with genuine discontinuities** (e.g., Burgers' equation with shock, advection with jump): The Allen-Cahn and Darcy-Flow examples are challenging but not dominated by sharp interfaces where PINNs are known to catastrophically fail.
- **Scatter plot of final RBF center positions overlaid on the solution**: Figure 3 shows some learned RBF values, but a plot showing where centers concentrate (ideally near sharp features) would strengthen the spatial-adaptivity argument.

## Removed Points

The following points from the reviewer inputs were removed per policy:

1. **Missing empirical evidence / Table 1 / experiment subsections absent**: The `\input{results_overview}`, `\input{06-AC_experiments}`, `\input{06-DF-smooth_experiments}`, and `\input{06-DF-rough_experiments}` commands are parser artifacts — the original compiled PDF would have contained this content. Per Hard Rules, parser artifacts are not author errors.

2. **Architecture diagram missing (via `\input{}`)**: Same parser artifact issue as above.

3. **The regularization "contradicts" the goal of using RBF**: The L₂ penalty on α is explicitly described as encouraging smoother solutions (lines 177–178, 187). This is by design, not a contradiction. The paper consistently presents this as a feature for stable training.

4. **Criticism about missing appendix or proofs**: Removed per Hard Rules — parser strips these sections.

5. **Generic formatting/style nitpicks**: Removed per Hard Rules.

## Novel Insights

The key insight that emerges from the reviews — beyond the paper's own contributions — is that the global-per-block α design creates a tension between the spatial-localization motivation (RBF captures sharp features locally) and the architectural implementation (α applies uniformly across the block's domain). This suggests a natural extension: allowing α to vary as a function of the input coordinates (e.g., via a small learned network or spatial grid), which would permit the model to dynamically decide *where* to rely on RBF versus DNN components within a single block. Such an extension would more faithfully realize the paper's stated motivation and could yield further improvements on problems with spatially heterogeneous smoothness.

## Suggestions

1. **Specify the number of RBF centers per block and their initialization strategy** in Section 3.2 — this is essential for reproducibility.
2. **Add ablations with fixed α (e.g., α=0.5 constant) and fixed β (β=1 constant)** to isolate the benefit of adaptivity from the benefit of the hybrid structure itself.
3. **Report and discuss the choice of λₚ** (regularization strength on α) and include a sensitivity study.
4. **Show how α evolves during training** for at least one problem — this would directly support the claim that α adaptively balances components.
5. **If possible, include a baseline that simply averages a DNN and RBF network output** (non-residual) to further isolate the contribution of the residual architecture.

## Score and Decision

The paper presents a genuinely novel architecture with a clear motivation. The method is well-described algebraically. The core weakness is incomplete experimental transparency (unspecified architectural details, missing ablations, no α-evolution analysis), but none of these are fatal — they are addressable in a revision. The global α limitation is real but does not invalidate the contribution; it is more a design choice with trade-offs than a flaw.

I rate this as a solid paper whose contribution is meaningful, with room for improvement in experimental rigor and reporting.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>