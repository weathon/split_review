Now I have all the information I need. Here is the final consolidated review.

---

## Summary

This paper introduces the trace neural tangent kernel (trNTK) and its random projection variants (proj-trNTK, proj-pNTK) as computationally efficient approximate empirical NTK kernels for building faithful kernel surrogate models of neural networks. The authors evaluate faithfulness via Kendall-τ rank correlation between the kGLM surrogate and NN softmax outputs — an improvement over prior test-accuracy-based evaluation — and demonstrate that trNTK-based surrogates consistently achieve τ ≥ 0.7 across eight architecture-dataset combinations (Table 1). The projection variants reduce computation from 389h to 1.12h for ResNet18, enabling practical scalability.

## Strengths

1. **Definition and systematic evaluation of trNTK as a novel approximate eNTK.** The paper formally defines the trace NTK (Eq. 3) and its normalized form, and is the first to explicitly investigate its faithfulness properties. In Table 2, trNTK achieves the highest Kendall-τ correlation in both large-scale comparisons (0.776 for ResNet18, 0.809 for Bert-base), supporting the claim that it is a faithful approximate eNTK.

2. **Consistent faithfulness across diverse architectures and datasets.** Using Kendall-τ, the paper demonstrates that trNTK-based surrogate models consistently achieve correlation ≥ 0.7 across eight model-dataset combinations (Table 1), spanning MLP, CNN, ResNet18/34, MobileNetV2, and Bert-base on MNIST, FMNIST, CIFAR10, and COLA datasets. This is a novel systematic demonstration that approximate eNTK surrogates correlate with the original network's per-sample behavior, not just replicate test accuracy.

3. **Introduction of random projection variants with quantified computational savings.** The paper defines proj-trNTK and proj-pNTK (Eqs. 4–5) and provides wall-clock time comparisons (Table 4) showing dramatic speedups (e.g., trNTK: 389h → proj-trNTK: 1.12h for ResNet18; 1200h → 22m for Bert-base). This directly supports the practical usability claim.

4. **Improved faithfulness evaluation methodology.** The paper replaces test-accuracy-based evaluation with Kendall-τ rank correlation, correctly arguing that test accuracy is invariant to per-sample behavior and thus insufficient. Figure 1 validates that high τ implies an approximately invertible monotonic mapping (R²=0.91 for Bert-base), providing a more principled measure than prior work.

5. **Practical demonstration in data poisoning forensics.** Table 3 shows that trNTK and proj-pNTK achieve 99.99% precision and 100% recall in identifying poisoned test examples, demonstrating a concrete security application where faithfulness translates to utility.

## Weaknesses

### Fatal
None.

### Major

1. **The sparsity claim is not quantitatively supported, yet the paper draws a strong conclusion from it.** The paper argues that attribution distributions are not sparse (Figure 2) and concludes that "the assumption of sparsity in explain-by-example strategies is misguided" (Section 5). This is a significant claim with implications for a class of methods (Representer Points, etc.). However, the evidence is limited to a single boxplot (Figure 2) and the statement that "mean lines are always observed to be within the inner quartile range." This is not a formal test of sparsity — attributions can be spread across many points yet still have a heavy tail where a small fraction of points carry disproportionate weight. The paper needs quantitative sparsity measures (e.g., Gini index, fraction of training points needed to reach 50%/80%/95% of total attribution mass) to support this conclusion. Without such quantification, the "sparsity is misguided" claim is an overreach from qualitative visual inspection. The paper's third contribution (comparing explanations across kernels) remains intact, but the strong auxiliary conclusion about representer methods is unsubstantiated.

### Minor

2. **The faithfulness metric suite is internally inconsistent on the question of which kernel is best, and the paper never reconciles disagreements.** The paper uses τ (correct-class softmax rank correlation) as the primary metric and R_Miss (misclassification coincidence rate) as a complementary metric. However, in Table 2 these metrics often conflict about which kernel is most faithful. For Bert-base, trNTK has τ=0.809 (best) but R_Miss=0.67 (worst), while CK has τ=0.52 (worst) but R_Miss=0.91 (best). The paper consistently defaults to τ when claiming trNTK superiority but does not justify why τ dominates R_Miss, nor discusses how practitioners should interpret cases where the rankings diverge. A brief discussion reconciling these metrics or explaining when one takes precedence would significantly strengthen the evaluation.

3. **The abstract and conclusion overclaim "most consistent performer" without qualifying the clean-data / poisoned-data caveat.** The poisoning experiment (Table 3) shows that proj-pNTK (τ=0.665) outperforms trNTK (τ=0.569) on poisoned test data, a reversal the paper acknowledges in the body text. Yet the abstract states trNTK is "the most consistent performer" without caveat, and the conclusion asserts it is "a consistently faithful choice" without qualification. Since a practitioner applying these methods to distribution-shifted or poisoned data might draw a different conclusion, the claims should be appropriately scoped.

4. **No empirical error analysis for projection variants relative to full trNTK.** The Johnson-Lindenstrauss lemma is invoked to justify random projections, but the paper provides no empirical comparison between the full trNTK kernel matrix and its projected variant (e.g., Frobenius norm of the difference, element-wise correlation). Given that the projection dimension K=10240 is fixed across all experiments with no ablation, readers cannot assess how much fidelity is lost at this specific setting, nor how to choose K for new applications. A small-scale comparison (e.g., on a subset or smaller model) would address this gap.

5. **Experimental scope choices could be better justified.** The paper uses 2-class versions of several datasets (MNIST2, CIFAR2, FMNIST2) without discussing why. The embedding kernel is defined as "a sum over the Gram matrices of embedding vectors from various layers" without specifying which layers were used, making reproduction difficult. The kGLM training uses an SGD classifier with minimal detail (log loss, L2=1e-4) and no convergence checks reported. These are addressable in a camera-ready version.

### Trivial
None beyond what is addressed in Nice-to-Haves.

## Nice-to-Haves

- An ablation over projection dimension K (e.g., 512, 2048, 8192, 32768) on a smaller model would reveal the tradeoff between faithfulness and speed, and help guide practitioner choices.
- A comparison of the kGLM surrogate with a non-parametric kernel method (e.g., KNN on the same kernel) would test whether the linearity assumption in kernel space harms faithfulness.
- Implementation details on per-sample Jacobian computation (e.g., vmap, custom backward hooks) would aid reproducibility beyond the cited code repository.

## Removed Points

- *"The code repository is mentioned but not accessible in the review"* — Removed per hard rule: criticisms questioning availability of cited artifacts are not permitted. The paper cites a repository; that suffices.
- *"Computational costs reported in Table 4 (389h for trNTK) make the full trNTK evaluation infeasible for most practitioners"* — Removed: this is precisely the motivation for the projection variants, and the paper's recommendation is to use the practical variants. Not a weakness.
- *Strength Finder point #7 (attribution non-sparsity insight)* — Removed because it conflicts with the verified weakness that the sparsity claim lacks quantitative support.

## Novel Insights

The most interesting finding in the paper is the poisoning experiment reversal: trNTK is most faithful on clean data (τ=0.643) but proj-pNTK becomes most faithful on poisoned data (τ=0.665). This suggests that faithfulness is not kernel-invariant and depends on the structure of the data distribution — a phenomenon that could indicate that under distribution shift, the summed Jacobian of pNTK captures different gradient structure than the per-class trace of trNTK. The paper does not explore this, but it opens a potentially fruitful direction for future work on adaptive kernel selection.

## Suggestions

1. Add quantitative sparsity measures (Gini index, fraction of points to reach 50%/80% attribution mass) to support or soften the "sparsity is misguided" claim. If the data do not support a strong claim, reframe it as an observation rather than a conclusion.
2. Add a brief discussion reconciling the τ and R_Miss metric disagreements: e.g., a sentence on when practitioners should prioritize each metric depending on their use case.
3. Add a small-scale empirical comparison of the full trNTK vs. proj-trNTK kernel matrices (Frobenius norm / element-wise correlation) to ground the JL justification, and include a brief ablation over K on a smaller model.
4. Tone down the abstract/conclusion claims about trNTK being the "most consistent performer" to account for the poisoning reversal, or add explicit qualifiers about clean vs. shifted data.

## Score and Decision

**Originality:** The paper introduces trNTK (previously mentioned only in passing by another work) and is the first to systematically evaluate approximate eNTK faithfulness via rank correlation rather than test accuracy. The projection variants adapt ideas from TRAK but are novel in this context. Modest but solid originality.

**Importance of research question:** Yes — faithful surrogate models for neural networks are important for explainability, and the computational cost of eNTK is a real barrier. The question is well-motivated.

**Claims supported:** The core claim (trNTK-based surrogates consistently correlate with NNs at τ ≥ 0.7) is supported. The secondary sparsity claim is not well-supported.

**Soundness of experiments:** Generally sound. The faithfulness evaluation (Tables 1–2) is well-designed. The poisoning experiment is informative. The sparsity analysis (Figure 2) lacks quantitative rigor.

**Clarity of writing:** Clear and well-structured. Notation is introduced carefully.

**Value to community:** The trNTK and its projection variants, along with the code, are likely to be useful to researchers working on data attribution and explainability. The faithfulness evaluation methodology is also a contribution.

Overall, the paper makes real contributions — defining and evaluating trNTK, demonstrating consistent rank correlation across diverse settings, and providing practical projection variants with dramatic speedups. The weaknesses are addressable: the sparsity claim should be softened or better quantified, the faithfulness metrics should be reconciled, and the claims should be more carefully scoped. None of these issues invalidate the central contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>