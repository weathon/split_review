Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces Sparse Labels Node Classification (SLNC), a semi-supervised node classification setting where only a handful of randomly selected labels (not selected per-class) are available, and proposes the ELI framework. ELI uses unsupervised clustering (AGC) to estimate pseudo-label distributions, then incorporates them as additional Laplacian regularizers into label propagation and simplified graph convolution (SGC). Experiments on 7 benchmark datasets show 10–20% absolute accuracy gains over LP, SGC, DGI, GMI, and CGPN when only 1–2 labels per class are available.

## Strengths

- **Novel and practically motivated problem definition.** Section 3 (Definition 3.1) formally defines SLNC, which relaxes two hard requirements of standard SSNC: the need for substantial labels and the need for per-class label selection. This directly addresses a real-world constraint where annotators cannot cherry-pick labels per class.

- **Consistent 10–20% accuracy improvement under extreme label sparsity.** Across all 7 datasets (Cora, Citeseer, Pubmed, Wiki, Computers, Photos, Cs), both LP-ELI and SGC-ELI consistently outperform all baselines. For example, on Cora with 1 label/class, SGC-ELI achieves 63.8% vs. SGC's 47.0% (Tables 3–4, Figure 1). The improvement holds across different label counts (1–4 per class) and is visible in every dataset tested.

- **Practical computational efficiency.** The paper reports (Section 5.6) that CGPN takes >48 seconds per run on Citeseer and fails to complete on larger datasets within 45 minutes, while LP-ELI and SGC-ELI complete in 0.27 and 2.18 seconds respectively. This is a meaningful advantage for a method targeting practical sparse-label deployment.

- **Honest discussion of the key limitation.** Section 6 explicitly acknowledges that ELI requires knowing the number of classes \(c\) in advance, which is often unavailable in real applications. This candor strengthens scientific integrity and provides a clear direction for follow-up work.

## Weaknesses

### Major

- **Described pipeline vs. evaluated method are misaligned.** Section 4.2 describes "key nodes selection" as the second step of the ELI framework — selecting labeled nodes based on clustering confidence. However, the evaluation protocol (Section 5.2) states that labels are "randomly selected" for all methods. The paper never clarifies whether ELI's reported results use key nodes selection, random selection, or some hybrid, and there is no experiment that tests whether the key-node selection step improves or harms performance. This leaves the reader unable to determine what the method actually does in the claimed setting. The core contribution (pseudo-label regularization) is still demonstrated and valid, but the framework description oversells a component that is never evaluated, making the paper less coherent than it should be.

- **Overclaimed generalization to "any GNN."** Section 4.5 claims the framework generalizes to "any other GNN framework" but only tests SGC (a simplified linear model) and LP (which is not a GNN at all). Testing on a standard GCN or GAT would be necessary to substantiate this claim. As written, the evidence supports generalization to SGC, not to arbitrary GNNs.

### Minor

- **No experiments on heterophilic graphs.** The method relies on Laplacian smoothness regularization, which is known to perform poorly on heterophilic graphs where neighbors tend to have different labels. The paper mentions heterophily in the related work (Section 2) as a known challenge but does not test on any heterophilic dataset (e.g., Texas, Wisconsin, Chameleon). Including even one such dataset would define the method's boundary of applicability.

- **Limited GNN architecture scope.** Only two base architectures (LP and SGC) are tested with ELI. While the paper claims to generalize to any GNN, the practical demonstration is limited to the simplest possible instantiations. Testing on a deeper or attention-based GNN would strengthen the empirical contribution.

### Trivial

- None that survive filtering (formatting issues are parser artifacts, not author errors).

## Nice-to-Haves

- An ablation that isolates the contribution of each Laplacian term in \(L_A = \frac{1}{3}(L_{sym} + L_{\mathcal{G}_H} + L_{\mathcal{G}_Y})\) would help attribute the improvement to the pseudo-label regularization vs. the extra Laplacian structure alone. (Note: if this ablation already exists in the stripped appendix, the authors should move it to the main paper.)
- Reporting confidence intervals or effect sizes for the main comparisons (e.g., LP-ELI vs. LP at 1 label/class) would strengthen the statistical grounding, though the reported mean/std over 10 runs is within community norms.

## Removed Points

- **"MLP vs. logistic regression for pre-trained baselines"** — The paper explicitly states (Section 5.5.2) that MLP was used because it "performed much better" than logistic regression. This gives the pre-training baselines a *stronger* downstream model, making the comparison harder for the proposed method. Per the rules, criticisms about asymmetry that favors baselines are removed.
- **"Missing appendix/ablation/sensitivity studies"** — The paper references Appendices C, C.1, and D.1 for ablation and sensitivity studies. These sections exist in the original submission but were stripped by the PDF extraction process. Per the rules, such criticisms are removed.
- **"Statistical significance not reported"** — Mean and std over 10 runs are reported. This is standard practice; demanding confidence intervals or p-values goes beyond the norms for this type of empirical paper.
- **"Varying number of labels not shown beyond 2 per class"** — Factually incorrect. The paper states #num varied from 1–4, and Figure 1 shows accuracy curves across this range.
- **"Parameter settings not justified"** — The paper cites Section D.1 in the appendix for sensitivity analysis on the KNN parameter. This exists in the original submission.
- **"CGPN excluded from large datasets"** — The paper acknowledges this with a legitimate practical reason (runtime >45 min). This is not a weakness of the proposed method.
- **"Key nodes selection step should be removed" (framed as fatal)** — While the misalignment is a real problem requiring clarification, it does not invalidate the core contribution (pseudo-label regularization), which is tested and works. This is demoted from "fatal" to "major" above because the core empirical contribution survives the removal of the untested component.
- Several generic strengths from the Strength Finder (e.g., "comprehensive evaluation setup") were dropped because they overstate the evaluation's completeness given the above-noted gaps, or because they conflict with verified weaknesses.

## Novel Insights

The reviews do not surface an insight that goes substantially beyond what the paper itself contributes. The interaction between the two reviews is largely complementary: the harsh critic identifies a structural inconsistency (key nodes selection unevaluated) and overclaimed generalization, while the strength finder correctly identifies the problem definition and consistent empirical gains as the paper's genuine contributions. The main synthetic observation is that the paper's *actual* contribution (pseudo-label regularization improves sparse-label propagation) is narrower than its *claimed* contribution (a four-step framework including active node selection), and the paper would be significantly strengthened by aligning the two.

## Suggestions

1. **Align the pipeline description with the evaluation.** Either remove Section 4.2 (key nodes selection) from the framework description if it is not used, or explicitly state that it is optional and test it in an ablation. This single change would resolve the most serious source of confusion.
2. **Temper the generalization claim.** Change "any GNN framework" to "linear GNNs such as SGC" or add experiments with GCN/GAT.
3. **Add at least one heterophilic dataset** (e.g., Texas, Wisconsin, or Chameleon) to demonstrate the method's boundaries.
4. **Move the ablation study** (pseudo-label Laplacian vs. graph Laplacian vs. key-label Laplacian) from the appendix into the main paper, as it is central to understanding what drives the improvement.

**Score and Decision**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>