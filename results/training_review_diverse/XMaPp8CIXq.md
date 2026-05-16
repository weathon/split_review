Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper introduces Guided Stochastic Exploration (GSE), an always-sparse dynamic sparse training (DST) algorithm. The key idea is to sample a subset of inactive connections at each grow/prune step, compute gradients only for those sampled connections, and grow the ones with the largest gradient magnitude. This avoids the dense gradient computation required by RigL while maintaining (often exceeding) its accuracy. Experiments on CIFAR-10/100 and ImageNet with ResNet, VGG, and ViT models show GSE outperforms prior always-sparse methods and matches or beats RigL at high sparsities (90-98%).

## Strengths

1. **Novel and effective algorithm design**: GSE's hybrid exploration strategy — randomly sampling a subset of inactive connections followed by gradient-guided selection from that subset — is a clean, well-motivated idea that bridges SET (pure random) and RigL (pure greedy). The empirical validation (Table 1) consistently shows GSE outperforming both at 98% sparsity across architectures (e.g., CIFAR-100 ResNet-56: 69.71% vs. RigL 68.76% and SET 68.41%).

2. **Always-sparse computation is genuinely maintained**: Unlike RigL, which periodically computes dense gradients (O(n²) time), GSE never materializes the dense weight matrix or computes dense gradients. The method samples O(n) connections, computes gradients only for those, and selects top-k in O(n) time via introselect. The FLOPs comparison in Figure 4 quantifies this advantage: at 99% sparsity GSE uses 11.8% fewer FLOPs than RigL, and at brain-like sparsities the gap widens to 131×.

3. **Thorough ablation on design choices**: Section 4.2 systematically varies the subset sampling ratio γ (0.25 to 2) and compares three distributions (uniform, GraBo, GraEst). The finding that uniform sampling with γ ≈ 1 matches or exceeds RigL is non-trivial and well-supported. The paper also tests the hypothesis that γ→∞ converges to RigL behavior, confirming the expected trend.

4. **Comprehensive evaluation**: GSE is compared against 9 baselines (Lottery, Gradual, SNIP, GraSP, SynFlow, SET, RigL, Top-KAST, DSR, SNFS) across two datasets, three architectures, and three sparsity levels. The consistent outperformance — especially at extreme sparsity where differences are most meaningful — provides solid evidence for the method's effectiveness.

## Weaknesses

### Fatal
None.

### Major

1. **The method description does not explain how it applies to convolutional layers, yet experiments rely heavily on them.** Section 3.1 describes subset sampling via independent draws over "input units" and "output units" (a_i ∼ f^{[l]}, b_i ∼ g^{[l]}), and states this is discussed "in the case of fully-connected layers" (line 53). For conv layers, filter weights connect channels with spatial structure, activations and gradients are 4D tensors, and the gradient of a weight involves a sum over spatial locations. The paper does not specify: (a) what constitutes a "unit" for conv layers (channels? spatial positions? a combination?), (b) how the vector-valued distributions f and g are derived from tensor-valued activations and gradients, or (c) how the gradient magnitude of a sampled inactive conv filter weight is computed efficiently. While the experiments clearly work — and the adaptation likely follows standard DST practice (treating channels as units, aggregating over spatial dimensions) — the paper does not provide the specification, making the method description incomplete for the architectures actually evaluated. This is a significant presentation gap that must be addressed for the paper to be reproducible.

2. **ImageNet comparison uses literature-reported baseline numbers rather than controlled reproduction.** Table 2 compares GSE against baselines whose results are "obtained from prior publications" (line 144). Training protocols (epochs, learning rate schedule, label smoothing, weight decay) can differ substantially across papers. While this is common practice for large-scale benchmarks, it weakens the evidence that GSE outperforms competing methods on ImageNet — the GSE result was obtained under one set of conditions, while baselines were obtained under potentially different conditions. The paper should at minimum report the variance across GSE runs and acknowledge the limitation more explicitly.

### Minor

1. **Statistical reporting uses the 95th percentile rather than standard deviation.** The paper reports the mean and "plot the 95th percentile" (line 102) across 3 runs. Standard deviation or confidence intervals would be more conventional and informative. The choice of 95th percentile (which shows the best-case performance among runs) is not justified.

2. **The complexity analysis is spread across the paper rather than presented as a unified derivation.** The O(n) claim is stated in the abstract and supported by component-level reasoning (|A| = O(n) from Erdős–Rényi in line 81; O(n) sampling in line 60; O(n) top-k selection in line 89), but these pieces are not assembled into a coherent end-to-end derivation. A single paragraph connecting the pieces would significantly clarify the claim.

3. **The interaction between subset size γ and pruning fraction α is not explored.** The ablation varies γ at fixed α (cosine-annealed from 0.2 to 0.0), but the optimal γ may depend on α. Since the paper commits to a specific cosine annealing schedule without testing alternatives or interaction effects, it is unclear how robust the γ=1 recommendation is to the choice of schedule.

4. **The FLOPs comparison (Figure 4) only compares against RigL, not SET or Top-KAST.** GSE is always-sparse like SET but the FLOPs comparison does not include it. The comparison against RigL is the most informative for the paper's core claim (vs. dense-gradient methods), but including SET would provide a fuller picture.

### Trivial
- None.

## Nice-to-Haves
- An analysis of how the method handles batch normalization and bias parameters in the complexity accounting (the paper states they are kept dense but does not quantify their overhead).
- Controlled ImageNet experiments re-running the most important baselines (RigL, SET) under the same pipeline, even if at reduced scale (e.g., 90 epochs).

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"The complexity claim has no derivation or proof in the main paper"** — The paper does provide component-level reasoning (lines 81, 60, 89) that collectively supports the O(n) claim, though it is spread across sections. The critic overstates the absence. The weakness is downgraded to Minor (item 2 above).

2. **"The paper does not report whether method-specific hyperparameters (α, T) were re-tuned for each baseline"** — The paper states "All experiments use the same optimization settings" and specifies that all DST methods use "the same update schedule" (line 106). Using a common setting is standard practice for fair comparison. Different hyperparameters per baseline would introduce confounding. This is not a weakness.

3. **"Sparsity initialization for conv layers is ambiguous"** — The Erdős–Rényi formula ⌈ε(n^{[l-1]}+n^{[l]})⌉ where n^{[l]} are "the number of units" follows the same convention as RigL and SET. For conv layers, n^{[l]} refers to the number of channels (feature maps), consistent with the DST literature. The paper could be clearer, but the practice is standard.

4. **"No discussion of how the method handles batch normalization"** — The paper explicitly states at line 102: "The bias and normalization parameters are kept dense since they only contribute marginally to the size and cost of a model." This is addressed.

5. **"LTH inclusion does not strengthen the case for GSE"** — The LTH baseline is included for completeness as a common sparsification method. All relevant DST baselines (SET, RigL, Top-KAST) are also included. The critic's point about LTH underperforming at high sparsity is well-known and does not weaken the paper.

6. **"ViT experiment is tangential"** — The ViT experiment is part of the model scaling study (Section 4.5), which supports the paper's claim about scaling to larger models. It is relevant.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Provide a complete specification of how GSE applies to convolutional layers.** Map each component to conv operations: define "units" as channels, explain how tensor-valued activations/gradients are aggregated over spatial dimensions to produce the vector distributions f and g, describe how gradient magnitudes are computed for sampled inactive filter weights (including the spatial sum), and discuss how the complexity analysis accounts for spatial dimensions and kernel sizes. This is the single most impactful revision.

2. **Present the complexity analysis as a unified end-to-end derivation** in Section 3 — from Erdős–Rényi initialization (|A| = O(n)), through subset sampling (O(n) draws using alias method), set difference (O(n) via hash tables), gradient computation (O(n) for sampled connections), to top-k selection (O(n) via introselect). Clarify how this extends to conv layers (whether kernel size and spatial dimensions affect the complexity).

3. **Replace the 95th percentile with standard deviation or confidence intervals** for the 3-run experiments, or at minimum justify the choice of 95th percentile.

## Score and Decision

The paper proposes a genuinely useful algorithm backed by solid experiments and a clear ablation study. The core idea — sampling a subset of inactive connections, computing their gradients, and growing the top-k — is simple, well-motivated, and empirically effective. The CIFAR results provide strong evidence that GSE outperforms existing always-sparse methods and matches or exceeds RigL at high sparsities.

However, the paper has a significant presentation gap: the method description explicitly covers only fully-connected layers, while all key experiments use convolutional networks. The adaptation to conv layers is not specified, leaving the experimental results partially ungrounded in the described method. This is a major weakness that must be addressed in revision, but it does not invalidate the contribution — it is a documentation gap rather than a structural flaw, as the experiments clearly work and the adaptation follows standard DST conventions.

Given the paper's genuine contributions balanced against this presentation gap, I recommend **acceptance** conditioned on the authors providing a clear specification of the conv-layer adaptation.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>