Now I have all the information to write the final consolidated review. Let me synthesize everything.

---

## Summary

This paper introduces a Fixed Non-negative Orthogonal (FNO) classifier and analyzes its training dynamics through a proposed variant of neural collapse called "zero-mean neural collapse" (ZNC), where class means center to the origin rather than the global mean. The key theoretical claim is that the FNO classifier induces ZNC and max-margin in an orthogonal layer-peeled model (OLPM). The paper then leverages the resulting Feature Dimension Separation (FDS) — each class uses disjoint feature dimensions — to enhance masked softmax in continual learning and to enable a new interpolation method called arc-mixup for imbalanced learning. Experiments on CIFAR, Tiny-ImageNet, ImageNet-LT, and Places-LT show performance improvements over several baselines.

## Strengths

- **Novel formulation of zero-mean neural collapse for fixed orthogonal classifiers.** Standard neural collapse (Papyan et al., 2020) assumes the classifier converges to a simplex ETF, which fixed orthogonal classifiers cannot achieve due to geometric constraints. The paper's ZNC (Section 4, Table 1) provides a principled alternative by centering class means to the origin, extending collapse theory to a previously unanalyzed setting.

- **Theorem 1 provides a theoretical foundation linking FNO classifiers, global optimality, and ZNC in the OLPM.** The theorem states that under the orthogonal layer-peeled model (Eq. 5), a global minimizer of the FNO classifier induces zero-mean neural collapse while achieving max-margin. This connects the fixed-classifier literature (Hoffer et al., 2018; Pernici et al., 2021a) with neural collapse theory, which prior work had not done.

- **Feature Dimension Separation (FDS) is a geometrically clean concept with practical utility.** The disjoint-support property (Definition 3) arising from non-negativity + orthogonality is intuitive and has demonstrable applications. The experimental results (Tables 2–4) show that FNO + masked softmax frequently improves over standard masked replay in continual learning, and FNO + arc-mixup achieves consistent gains on long-tailed benchmarks including ImageNet-LT and Places-LT.

- **Comprehensive experimental scope.** Experiments span multiple architectures (ResNet18/32/50/152), datasets (CIFAR-10/100, Tiny-ImageNet, ImageNet-LT, Places-LT), and settings (class-IL, task-IL, long-tailed recognition), demonstrating breadth beyond a single-task evaluation.

## Weaknesses

### Major

- **No empirical validation that zero-mean neural collapse actually occurs during training.** The paper's core theoretical contribution is that FNO classifiers induce ZNC. Section 4 states "we analyzed the zero-mean neural collapse in the same environments to neural collapse by conducting comprehensive experiments (Papyan et al.1)" but provides **no measurements whatsoever** — no NC1/NC2/NC3-style metrics, no convergence plots, no class-mean alignment visualizations. For a paper whose central claim depends on a specific collapse phenomenon emerging, the absence of any direct empirical evidence for that phenomenon is a critical gap. The connection between the theory and the downstream applications remains speculative without this verification.

- **Unclear specification of the arc-mixup loss and its integration with the training objective.** Definition 5 gives the arc-mixup loss as ℒ_{cls}(x̂, q̂) = −log(q̂^T ĥ), where q̂ is a mixed class weight vector (D-dimensional). This is not the standard cross-entropy loss (which uses softmax over K classes). The paper refers to "cross-entropy loss" in the experimental setup (Tables 3, 4 caption) but does not clarify whether arc-mixup replaces the standard CE loss entirely, is used as an additional regularization term, or is combined in some other way. If the final loss is not cross-entropy, the connection to neural-collapse theory (derived for cross-entropy loss) is weakened. This ambiguity undermines the imbalanced-learning claims.

- **Missing ablations to isolate the contributions of individual components in imbalanced learning.** Tables 3 and 4 compare FNO+arc-mixup against CE+ B-mixup and other baselines, but no ablation separates the effect of (a) the FNO classifier alone, (b) FNO + standard mixup, (c) FNO + arc-mixup without zero-masking, or (d) arc-mixup with a learnable classifier. Without these, it is impossible to attribute the reported gains to arc-mixup versus the FNO classifier versus zero-masking. "Zero masking" itself is mentioned in a figure caption (Figure 3b) but is never defined in the paper.

### Minor

- **The constraint Σ_{j≠k} h^T q_j* ≥ 0 in the OLPM (Eq. 5) is not justified.** This constraint is added to the LPM formulation but the paper does not explain why it should hold naturally during training, whether it is a necessary condition for the theorem, or whether it is ever checked empirically. The theorem's validity depends on this constraint, but its origin and plausibility are left unaddressed.

- **Mixed continual-learning results undercut the claim of "outperforming."** The paper states FNO "outperforms masked replay excepts few parts in task-incremental learning" (Section 7.1). In the class-IL settings on S-CIFAR-100 and S-TinyImageNet (Table 2), RM+FNO underperforms RM+FC. The paper does not analyze why FNO fails in these cases, which would be informative for understanding the method's limitations.

- **Construction of the non-negative orthogonal classifier is underspecified.** The paper says "we initialize the linear classifier Q as a random fixed non-negative orthogonal matrix by Eq. 8" (Section 5) but Eq. 8 is not visible in the parsed text (likely deferred to an appendix). For reproducibility, the paper should at minimum sketch how such matrices are generated (e.g., permutation of a block matrix), especially for datasets with thousands of classes (ImageNet-LT, Places-LT).

- **The ZNC definition in Section 4 is informal.** Rather than providing formal metrics or characterizing the convergence dynamics, the definition is given as two bullet points ("variability collapse..." and "convergence to non-negative orthogonal matrix"). While Table 1 offers a clean side-by-side comparison with standard NC, the definition itself lacks the precision needed for rigorous downstream analysis.

### Trivial

- The paper mentions "Proof 1." following Theorem 1 with no visible content (line 134). This appears to be a parser artifact.

## Nice-to-Haves

- Adding NC1/NC2/NC3-style measurements (within-class variance, class-mean alignment, self-duality) on CIFAR-10 or CIFAR-100 to demonstrate that ZNC actually emerges in practice.
- Visualizing the FDS effect through per-class feature activation heatmaps to confirm that dimensions are indeed disjoint as claimed.
- Plotting logit evolution during continual learning to quantitatively illustrate how FNO+masked softmax reduces interference compared to FC+masked softmax.

## Removed Points

These points from the reviewers are removed per guidelines:

1. **"Missing proof of Theorem 1"** — Removed: The parser strips appendix/supplementary sections from all papers; the proof exists in the original submission. The hard rule states that criticisms about missing proofs in appendices must be removed.
2. **"No head-to-head comparison with a standard learnable classifier"** — Removed: Table 2 directly compares RM+FC (learnable) vs RM+FNO (fixed) under identical encoder and rehearsal method. The comparison exists.
3. **"Figure 1 is conceptually muddy"** — Removed: Subjective formatting/presentation opinion.
4. **"Theorem 2 is straightforward / not deep"** — Removed: This is a subjective judgment about theoretical depth; the theorem is a valid algebraic consequence that connects orthogonality to the arc-mixup property.
5. **"D ≥ K limitation applies more severely due to FDS"** — Removed: The paper already acknowledges the D ≥ K limitation in the conclusion; FDS requiring distinct dimensions is an inherent property, not an additional unacknowledged limitation.
6. **Generic strengths from Strength Finder** (e.g., "comprehensive experimental setup") — Kept as supporting strengths since they are factually correct.

## Novel Insights

None beyond the paper's own contributions. The reviews did not identify a perspective that the paper itself does not already articulate.

## Suggestions

1. **Show that ZNC actually occurs**: Add a figure (or appendix subsection) with NC1/NC2/NC3 metrics computed for models trained with the FNO classifier on a small-scale dataset (e.g., CIFAR-10). This is essential to bridge the theoretical claim and the downstream applications.
2. **Clarify the arc-mixup loss**: Specify precisely how ℒ_{cls}(x̂, q̂) = −log(q̂^T ĥ) relates to the overall training objective — does it replace standard CE entirely, or is it an additional term? If it replaces CE, explain how the connection to neural-collapse theory (derived for CE) is maintained.
3. **Add ablations for imbalanced learning**: Compare FNO alone, FNO + standard mixup, FNO + arc-mixup, and arc-mixup with a learnable classifier on a single long-tailed benchmark to isolate the source of gains. Define "zero masking" clearly.
4. **Describe the construction of non-negative orthogonal matrices**: Provide the algorithm (even a short description) for generating such matrices, including for large K. Show robustness across different random seeds.
5. **Analyze the failure cases in continual learning**: Discuss why FNO underperforms FC in some class-IL settings (S-CIFAR-100, S-TinyImageNet) — is it a capacity issue due to FDS, a hyperparameter sensitivity, or something else?

The paper addresses an interesting problem and offers a novel geometric perspective, but the lack of empirical verification for its central theoretical claim and the unclear loss specification for arc-mixup are substantive gaps that need to be resolved before the paper can be accepted.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>