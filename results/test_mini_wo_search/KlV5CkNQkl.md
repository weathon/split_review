Here is my consolidated final review.

---

## Summary

This paper proposes HD-Explain, a post-hoc example-based prediction explanation method that uses Kernelized Stein Discrepancy (KSD) to define a model-dependent kernel between data points. Instead of relying on parameter perturbations or latent representations as prior methods do, the method derives a closed-form kernel function conditioned on the trained model, enabling efficient identification of training samples that provide predictive support to a test point. The authors support their claims of fine-grained precision, consistency, and computational efficiency with qualitative examples and quantitative metrics (Hit Rate, Coverage, Run Time) on CIFAR-10, SVHN, Brain Tumor, and Ovarian Cancer datasets, showing >80% hit rate against <10% for baselines.

---

## Strengths

1. **Novel application of KSD to example-based explanation that bypasses costly Hessian inversion.** The paper derives a closed-form kernel $\kappa_\theta$ (Equation 3) that encodes model-dependent data correlation without requiring inverse Hessian approximation or storing per-sample gradients over model parameters. This is the foundational technical novelty — it explains the memory/complexity advantage shown in Table 1, where HD-Explain's cache is bounded by data dimension $(m+k)$ rather than model parameter size, which is practically significant for modern overparameterized networks.

2. **Dramatic quantitative improvements in retrieval-based evaluation.** Under the proposed Hit Rate metric, HD-Explain achieves >80% retrieval of the ground-truth training sample (both the full-model variant and the last-layer variant HD-Explain*) while all three baselines (Influence Function, RPS, TracIn) stay below 10% across four datasets (CIFAR-10, SVHN, Brain Tumor, Ovarian Cancer). This gap is large and consistent, providing strong evidence that HD-Explain produces substantially more fine-grained instance-level explanations than prior methods.

3. **Introduction of objective, reproducible evaluation metrics for a field that relied on qualitative inspection.** The paper defines Hit Rate, Coverage, and Run Time and evaluates them across >300,000 independent runs. While these metrics have limitations (discussed below), they represent a methodological contribution by enabling quantitative comparison in a space that previously relied primarily on visual inspection.

4. **Detection of low-confidence predictions via explanation mismatch.** In misclassification cases (Figure 2c described in Section 4.1), HD-Explain returns top explanations whose class labels do not match the predicted label, reflecting low prediction confidence. This behavior is qualitatively demonstrated and contrasted with baselines that produce explanations consistent with the (incorrect) predicted label — a practically useful property for model debugging.

5. **Systematic kernel ablation across multiple datasets.** Figure 7 compares Linear, RBF, and IMQ kernels on hit rate, coverage, and execution time. Results show that even the linear kernel (fastest) outperforms all baselines in hit rate, and IMQ provides further gains under the challenging horizontal-flip augmentation. This provides practical guidance for deployment.

---

## Weaknesses

### Fatal
None.

### Major

1. **The theoretical grounding relies on two acknowledged approximations that are not rigorously justified.** To adapt KSD (designed for continuous joint distributions) to predictive classifiers $P_\theta(y|x)$, the paper (a) sets $P_\theta(\mathbf{x}) \equiv P_D(\mathbf{x})$ with $P_D(\mathbf{x})$ uniform over training points, and (b) treats the discrete label $y$ as a continuous variable concatenated with $\mathbf{x}$ in the kernel space. The paper explicitly acknowledges both as relaxations ("appears hasty," "can be viewed as an approximation," lines 135, 149) but provides no theoretical analysis or controlled experiment showing that these approximations are innocuous in the explanation setting. Since the kernel $\kappa_\theta$ is defined on the concatenated $(x,y)$ space, the validity of the whole method depends on these choices. The empirical results are promising, but the paper would be significantly stronger with a formal argument or ablation that isolates the effect of each approximation.

2. **The evaluation metrics (Hit Rate, Coverage) are not validated against standard explanation-quality criteria, so the claim of "better" explanations rests on task-specific measures.** The Hit Rate task (retrieve an augmented training sample's original from the training set) tests a form of fine-grained retrieval, which is a reasonable proxy — but it has not been shown to correlate with faithfulness (e.g., leave-one-out prediction change), utility for debugging, or alignment with human judgment. The Coverage metric measures diversity of top-$k$ explanations across test points; the paper treats high coverage as desirable (instance-level granularity), but low coverage from baselines could reflect meaningful class-level prototypes rather than a deficiency. Without additional evaluation (e.g., measuring prediction change when removing top-$k$ influential training points, or a user study), the central claim that HD-Explain offers "better" explanations is supported primarily by a single retrieval task.

### Minor

3. **Missing k-NN baseline.** A simple $k$-nearest neighbor baseline on the same input representation (raw features or last-layer features) would clarify whether HD-Explain's KSD kernel adds value beyond feature similarity, or whether the high hit rate is largely driven by the distance component of the kernel. The paper discusses $k$-NN in related work (line 55) but does not include it as a baseline, making it difficult to isolate the contribution of the Stein operator modulation.

4. **The comparison with baselines is asymmetric.** Influence Function and TracIn are limited to the *last layer* due to scalability (line 199), while HD-Explain is evaluated both on the full model and on the last layer (HD-Explain*). The headline results often feature the full HD-Explain, which is not directly comparable. The paper does include HD-Explain* (last-layer) which also dramatically outperforms baselines, partially mitigating this concern. However, the asymmetry in what the methods measure (gradients w.r.t. parameters vs. KSD kernel on features) means the comparison is not apples-to-apples in terms of the information used.

5. **Evaluation is limited to image classification.** All four datasets are image classification tasks. While the method's formalism is general, the paper provides no experiments on tabular, text, or other data modalities, leaving its generality unaddressed.

### Trivial

6. **Table 1's "size of data dimension" bound.** The bound is accurate for raw features but less precise for last-layer representations, where the dimension could still be large (e.g., 512). The paper roughly acknowledges this (line 154).

---

## Nice-to-Haves

- A faithfulness evaluation where top-$k$ training points are removed (or their influence is negated) and prediction change is measured, which would complement the retrieval-based Hit Rate.
- Explicit discussion of sensitivity to the choice of layer at which the kernel is computed, beyond the brief observation in the horizontal flip experiment (line 341).
- An ablation isolating the contribution of the gradient (Stein operator) terms from the base kernel $k(a,b)$, to quantify how much the model-dependent modulation adds over a simple distance kernel.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Equation 6 gradient w.r.t. y is not standard; the paper seems to treat it as the log-probability vector itself."** — Factually incorrect. The derivation $\nabla_{\mathbf{y}} \mathbf{y}^\top \log f_\theta(\mathbf{x}) = \log f_\theta(\mathbf{x})$ is mathematically standard and correct. The critic misread the derivation.

- **"Figure 6 (medical datasets) is mentioned but not provided."** — The paper references `Figure~\ref{fig:medical_qualitative}` (line 333). This figure was stripped by the PDF parser, not omitted by the authors. Per the formatting note, parser-stripped content should not be treated as a paper weakness.

- **"Table 1 should be more precise about data dimension bound."** — The paper's bound is adequately described and qualified ("whenever the size of model parameters is far larger than the data dimension," line 154). This is a minor precision nitpick that does not affect the paper's claims.

- **"Figure 3 strongly suggests the method is doing little more than distance-weighted nearest neighbors."** — This is speculation not grounded in specific evidence from the paper. The KSD kernel includes gradient modulation terms beyond simple distance. The figure alone cannot support this strong claim; a k-NN comparison (which is separately suggested as a missing baseline) would test it.

- **"HD-Explain's kernel includes an RBF distance on the raw (x,y) concatenation which naturally favors close raw-feature neighbors; its high hit rate is expected."** — This oversimplifies the KSD kernel, which involves four terms (Equation 3) including cross-gradient terms, not just an RBF on concatenated features. Moreover, HD-Explain* (last-layer) also achieves high hit rates, and the horizontal-flip experiment shows that when raw-feature similarity is destroyed, the full HD-Explain method's performance drops while HD-Explain* remains robust — directly contradicting the claim that performance is simply driven by raw-feature distance.

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface observations that transcend what the paper itself says.

---

## Suggestions

1. Add a $k$-NN baseline on the same feature space to isolate the contribution of the KSD-specific components over simple feature similarity. This would directly address the most common anticipated criticism.
2. Add a faithfulness experiment: for a subset of test points, remove the top-$k$ explained training points, approximately retrain (or use influence estimates), and measure prediction change. Compare this to the same procedure using baseline explanations.
3. Provide a more rigorous justification or empirical analysis of the two key approximations (uniform $P_D(\mathbf{x})$ over training points, continuous treatment of discrete labels) — e.g., show that varying these assumptions does not materially change the top-$k$ explanations.
4. Acknowledge the limitations of the evaluation metrics more explicitly in the paper and discuss what additional evidence would complement them.

---

## Score and Decision

The paper makes a genuinely novel contribution by introducing KSD to example-based explanation, which yields real practical advantages (no Hessian inversion, $O(m+k)$ per-sample cache, strong empirical performance). The main weaknesses are that the theoretical grounding relies on approximations that are acknowledged but not rigorously justified, and the evaluation metrics, while reasonable, are not validated against standard faithfulness criteria. These are significant but not fatal — the empirical evidence is extensive and the performance gap over baselines is large and consistent. With reasonable revisions (adding a k-NN baseline and a faithfulness experiment), this would be a strong paper.

**Score**: 7.0  
**Decision**: Accept

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>