Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper proposes FoRDE (First-order Repulsive Deep Ensemble), which applies particle-based variational inference (ParVI) to diversify neural network ensembles in the space of input gradients (gradients of logits w.r.t. inputs) rather than in weight space or function space. The authors argue that input-gradient space avoids the inefficiency of weight-space repulsion (due to over-parameterization) and the underfitting problem of function-space repulsion on training data. They develop a data-dependent PCA-based kernel for the repulsion term and show that FoRDE-PCA achieves gains in accuracy and calibration under covariate shift (CIFAR-10/100-C, TinyImageNet-C) over standard Deep Ensembles and other repulsive ensemble methods, while FoRDE-Tuned matches or exceeds DE on clean data as well.

## Strengths

- **Consistent and substantial improvement under covariate shift**: FoRDE-PCA achieves +2.4% corrupted accuracy (cA) on CIFAR-10-C (80.5 vs. 78.1 for DE, Table 2) and +1.8% on CIFAR-100-C (56.1 vs. 54.3 for DE, Table 1), with corresponding improvements in cNLL and cECE. These gains hold across three datasets (CIFAR-10, CIFAR-100, TinyImageNet) and are consistent across multiple corruption metrics.

- **Input-gradient repulsion avoids the underfitting problem that plagues function-space repulsion**: The toy experiments (Figure 2: 1D regression, Figure 3: 2D classification) qualitatively demonstrate that FoRDE maintains high predictive uncertainty outside the training data, whereas function-RDE collapses (visible as low-entropy regions in Figure 3). This directly validates a core motivation of the paper.

- **PCA-based kernel with principled motivation**: The connection to the EmpCov prior (Section 3.3) provides theoretical grounding for using inverse eigenvalues as lengthscales. The ablation showing FoRDE-PCA outperforms FoRDE-Identity under corruptions (Tables 1–2) confirms the design choice is empirically beneficial, and the explanation (encouraging reliance on high-variance features) is well-reasoned.

- **FoRDE-Tuned demonstrates no clean-data degradation**: FoRDE-Tuned matches the best clean accuracy on CIFAR-100 (82.1%, Table 1) while still outperforming DE on corrupted data (55.3 cA vs. 54.3), showing the method does not trade off in-distribution performance for robustness when lengthscales are appropriately tuned.

- **Transfer learning validation**: Figure 5 (labeled Fig. 4 in the harsh critic) shows FoRDE outperforms baselines in a transfer learning setting (ViT features on CIFAR-10/100) on both in-distribution and shifted test sets, with higher epistemic uncertainty (functional diversity) than DE and other RDE methods — demonstrating generality beyond the main benchmark setup.

## Weaknesses

### Fatal
None.

### Major

- **Missing standard deviations for corruption metrics (Tables 1–3)**. The paper reports ± error bars for all clean-data metrics (NLL, Accuracy, ECE) but provides only point estimates for cA, cNLL, and cECE. While results are averaged over 5 seeds, without variance information the reader cannot assess whether the reported gains (e.g., +2.4% cA on CIFAR-10-C, +1.3% on CIFAR-100-C) are significant or within the noise of training seeds. This is the most significant weakness because it concerns the paper's central claim (improved corruption robustness). The pattern is consistent across datasets, which is reassuring, but standard deviations should still be reported.

- **Transfer learning results (Figure 5) lack error bars**. The caption states results are "averaged over 5 seeds" but no measure of variance is shown. Given that this is a second experimental setting validating the method's generality, the missing error bars weaken the evidence.

### Minor

- **Overclaimed "guarantee" of functional diversity (Abstract, Introduction)**. The paper states that input-gradient repulsion "guarantees that ensemble members are functionally different" (Abstract) and "each ensemble member is guaranteed to correspond to a different function" (Introduction, item 1). The paper does acknowledge "up to translation" (line 7), but "guarantees" is too strong for two reasons: (a) the repulsion is a soft force in the gradient update, not a hard constraint; (b) two functions could have identical input gradients yet differ by a per-class additive constant, leaving softmax predictions unchanged. The core idea is still valid — the language should be softened to "encourages" or "promotes."

- **Interaction between PCA lengthscales and the median heuristic is unexamined**. The PCA kernel sets inverse squared lengthscales to eigenvalues (Section 3.3), which the paper acknowledges could drive the RBF kernel toward zero for high-variance dimensions (line 187). The median heuristic (Section 3.4) introduces a global bandwidth that mitigates this, but no ablation is provided that disentangles the two effects (e.g., fixed bandwidth vs. median heuristic for each lengthscale variant). While FoRDE-Identity vs. FoRDE-PCA is a controlled comparison, the mechanism by which PCA scaling and median heuristic interact remains unclear.

- **Implementation of second-order derivatives not described**. The update rule (Eq. 3) requires computing ∇_θ k(θ_i, θ_j), which involves Hessian-vector products (gradients of ∇_x f w.r.t. θ). The paper mentions "another backward pass" (line 218) but does not explain how this is implemented (e.g., double backprop, functional API, or JAX/ PyTorch-specific approach). This is a reproducibility concern for researchers wishing to implement the method.

- **EmpCov comparison (Table 3) is not fully controlled**. The EmpCov prior is applied only to first-layer weights, while FoRDE's PCA kernel affects all layers through the gradient path. The paper acknowledges this difference (Section 3.3: "the difference is that while [izmailov2021dangers] incorporates knowledge... into the prior, we embed this knowledge into our approximate posterior via the kernel"), but the comparison remains asymmetric. The results are still informative — FoRDE outperforms EmpCov-augmented baselines — but the framing should more clearly note the different mechanisms at play.

### Trivial

- **The "biased stochastic gradients" issue (line 208) is noted but not analyzed**. The paper states that mini-batching leads to "biased stochastic gradients" and that "in practice, we found no convergence issues." A brief theoretical comment or a small ablation (full-batch vs. mini-batch on a small problem) would address this cleanly. As is, the acknowledgment is reasonable but minimal.

## Nice-to-Haves

- A direct quantitative measure of input-gradient diversity during training (e.g., mean pairwise cosine similarity of normalized gradients) correlated with robustness gains would strengthen the causal link claimed in the paper.
- A sensitivity analysis of the median heuristic bandwidth (e.g., fixed h vs. adaptive) would help clarify the interaction with PCA lengthscales.
- The paper could discuss whether FoRDE's 3× training cost is justified in settings with smaller ensemble sizes or limited data.

## Removed Points

These points are flagged to be removed — treat them with caution:

1. **"Missing baseline: more recent variants of LIT" (Harsh Critic)**: The critic asked for "[methods] more recent variants" of LIT without naming specific works. This is too vague to constitute a valid weakness and is removed per the rule against requesting unbounded additional related work.

2. **"PCA kernel notation inconsistency" (Harsh Critic)**: The critic claimed the notation was ambiguous ("inverse square lengthscales equal to eigenvalues" vs. Eq. 9). On inspection, the notation is consistent: squared lengthscales S = L^{-1}, so the quadratic form uses S^{-1} = L (the eigenvalues), which is exactly what Eq. 9 writes. The notation is correctly reconciled.

3. **"Strength: addressed an important problem" (Strength Finder — implied generic framing)**: The Strength Finder's output was all specific and evidence-backed, so no strengths needed removal under the filtering rules.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a pattern or limitation that the paper itself does not already touch on.

## Suggestions

1. **Most important**: Add standard deviations (or confidence intervals) for all corruption metrics (cA, cNLL, cECE) in Tables 1–3 and Figure 5. This single change would address the most significant weakness.

2. Soften the "guarantee" language in the Abstract and Introduction to "promotes" or "encourages" functional diversity, noting the translation-invariance caveat.

3. Add a brief implementation note on how the second-order gradients (gradients of ∇_x f w.r.t. θ) are computed — a sentence or two describing the software mechanism (e.g., `torch.autograd.grad` with `create_graph=True`).

## Score and Decision

The paper proposes a novel and well-motivated approach (input-gradient-space repulsion for ensembles) that addresses a genuine limitation of existing ParVI ensemble methods (weight-space inefficiency and function-space underfitting). The experimental evidence consistently shows improvements under covariate shift across multiple datasets and metrics. The main weakness — missing standard deviations for corruption metrics — is a reporting gap rather than a methodological flaw, and the pattern of results is consistent enough to be credible even without them. The overclaimed "guarantee" language is a minor rhetorical issue. Overall, the contribution is solid and the paper is ready for acceptance with minor revisions.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>