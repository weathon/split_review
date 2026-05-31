## Summary

The paper proposes an unsupervised 3D shape matching framework that combines a dual-layer attention mechanism for feature extraction, a hybrid spectral space (LBO eigenfunctions plus elastic eigenmodes), and a Sinkhorn optimal transport post-processing step to compute point-to-point correspondences. Experiments are conducted on near-isometric (FAUST, SCAPE, SHREC‘19), non-isometric (SMAL), and topologically noisy (TOPKIDS) datasets.

## Strengths

- The design choice of integrating both Laplacian and elastic modal representations into a hybrid functional map is well motivated by the need to handle both global isometric alignment and local high-frequency details.
- The ablation study on the SMAL dataset provides evidence that each proposed component (hybrid space, dual attention, optimal transport) contributes to the overall performance under the controlled setting.
- Code is publicly available, which supports reproducibility.

## Weaknesses

### Fatal
None.

### Major

- **The quantitative results do not support the claimed state-of-the-art performance.** In Table 1, on several key settings the proposed method performs substantially worse than many baselines. For example, when trained on SCAPE and tested on FAUST, the method achieves an average geodesic error of 10.0, while many other unsupervised methods (e.g., Hybridmap 2.2, EOT 1.6, AttentiveFMaps 1.9) are far better. Similarly, on FAUST→SCAPE the method gets 8.5 vs. Hybridmap 4.2 and EOT 3.4. The method only shows marginal improvement on a few settings (e.g., FAUST→FAUST: 1.4 vs. 1.5). The paper’s narrative of “substantial improvements” and “outperforms state-of-the-art” is not consistent with the reported numbers.

- **The method exhibits poor cross-dataset generalization.** The large performance drop on SCAPE→FAUST (10.0) compared to other methods indicates that the approach is not robust to changes in training distribution, undermining its practical value.

- **Lack of clarity in the loss function and training procedure.** The loss in Eq. (7) is vaguely defined: the components $\mathcal{L}_{\text{LBO}}$ and $\mathcal{L}_{\text{Elas}}$ are not specified, nor is the annealing schedule for $\alpha$. It is unclear whether the method is truly unsupervised or uses some form of self-supervision that may require ground-truth correspondences (the main text claims “unsupervised” but the functional map loss often involves comparing to ground-truth maps). This ambiguity makes it difficult to assess the technical soundness.

### Minor

- The dual-attention module is essentially a combination of existing components (DiffusionNet backbone, channel attention with structural guidance from Laplacian statistics, and cross-attention from Predator). While the combination is new, the architectural novelty is limited.
- The hybrid spectral space is directly adopted from Bastian et al. (2024) without theoretical or practical extension.
- Figures 2, 3, and 5 contain repeated caption text and formatting issues that reduce readability, though these are likely parser artifacts.

### Trivial

- The SMAL dataset description says “five categories are used as training and the remaining three as test” but does not specify which categories.
- Table 1 has inconsistent bolding: some numbers are bolded that are not the best in their column (e.g., Ours 1.4 on FAUST is best, but 8.5 on SCAPE is not bolded, correctly). However, the claim of superiority is not supported by the table.

## Nice-to-Haves

- A detailed description of the loss functions $\mathcal{L}_{\text{LBO}}$ and $\mathcal{L}_{\text{Elas}}$ would strengthen the paper.
- Additional analysis on why the method fails on cross-dataset settings (SCAPE→FAUST) would be valuable.

## Novel Insights

None beyond the paper’s own contributions: the combination of attention-based features, hybrid spectral bases, and Sinkhorn post-processing is a straightforward integration of recent ideas. The paper does not uncover any unexpected behavior or new theoretical understanding of shape matching.

## Suggestions

- The authors should honestly discuss the failure cases and limitations, especially the poor cross-dataset performance. If the method only works well when training and test distributions are similar, this should be clearly stated.
- Clarify the unsupervised nature of the loss: specify exactly what supervision (if any) is used, and how the functional map is trained without ground-truth correspondences.
- Provide a fairer comparison: either retrain all baselines under the same protocol or explain the discrepancies (e.g., the SCAPE→FAUST results for Ours appear to be an outlier; could there be an implementation bug?).

## Score and Decision

**Score:** 3 (reject)

The paper proposes a reasonable combination of existing ideas, but the experimental evidence directly contradicts the claim of state-of-the-art performance. The method underperforms many baselines in several critical settings, and the paper glosses over these failures. The contribution is therefore not validated.

MY FINAL SCORE: 3 <score>3</score>
MY FINAL DECISION: Reject