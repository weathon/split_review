Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper proposes HGDE (Hybrid Granularity Distribution Estimation), a method that fuses coarse-grained category-level statistics with fine-grained instance-level statistics to estimate distributions for novel categories in few-shot learning. The approach generates additional training samples for the support set by linearly interpolating means and averaging covariances from both levels, with added covariance refinement via eigendecomposition and a distance-based generation constraint. The method is evaluated on Mini-ImageNet, Tiered-ImageNet, CUB, and CIFAR-FS, and is shown to improve accuracy when applied on top of LRDC, Meta-Baseline, and SMKT.

## Strengths

1. **Well-designed ablation studies that systematically isolate each component**: The paper evaluates the individual contribution of weighted mean estimation (Figure 3), covariance refinement (Figure 4), distribution fusion (Table 1 / Figure 5), and generation constraint (Figure 6). Each component is shown to provide measurable improvements, with the fused distribution yielding over 3% improvement above baseline on Mini-ImageNet in both 1-shot and 5-shot settings. This kind of thorough component-level analysis is rare and valuable.

2. **Simple and broadly integrable method**: HGDE operates on frozen features and can be added to existing few-shot learners (LRDC, Meta-Baseline, SMKT) with minimal changes. The ablation in Table 1 (Section 4.2.3) provides direct evidence that the hybrid estimation outperforms either single granularity alone: category-level alone gives ~2.5% improvement, instance-level alone gives ~2.7%, and fusion gives >3.3%.

3. **Consistent improvements across multiple benchmarks and backbones**: Tables 3 and 4 show that applying HGDE to LRDC, Meta-Baseline, and SMKT yields higher accuracy on Mini-ImageNet, Tiered-ImageNet, CUB, and CIFAR-FS under both 1-shot and 5-shot settings. For example, on CUB with ViT-S, HGDE improves LRDC by 1.8% (1-shot) and 0.97% (5-shot). The method works with WRN, ResNet, and ViT feature extractors.

4. **Covariance refinement via eigendecomposition is a technically sound addition**: Figure 4 shows that reconstructing estimated covariances by retaining only top-L principal components yields clear accuracy improvements for both category-level and instance-level estimation, addressing a genuine concern about noise in estimated covariances.

5. **Weighted mean estimation improves over simple averaging**: Figure 3 demonstrates that the similarity-based weighting scheme (Equations 6 and 10) consistently outperforms non-weighted averaging across different selection sizes for both category-level and instance-level estimation.

## Weaknesses

### Fatal

None.

### Major

1. **Hyperparameters tuned exclusively on Mini-ImageNet validation, with no cross-dataset sensitivity analysis**: The selection parameters — k=2 for category-level, k=1000 for instance-level, α=0.2, L=110/160, ε=8 — are all determined on the Mini-ImageNet validation set (Section 4.2: "we evaluate the effectiveness of various modules of HGDE using the validation set from Mini-ImageNet") and then applied unchanged to Tiered-ImageNet, CUB, and CIFAR-FS. These datasets differ substantially in scale (number of base categories ranges from 64 to 351), feature dimension, and domain (general objects vs. fine-grained birds). The paper provides no analysis of how performance varies with these parameters across datasets, nor any evidence that the chosen values are reasonable elsewhere. While single-dataset tuning is common practice, the absence of any sensitivity experiments weakens the claim of general effectiveness, especially because some parameters interact (e.g., k for category-level selection is 2, which means the entire category-level estimate relies on just two prototypes — this choice could be domain-dependent).

2. **No confidence intervals or statistical significance reported**: In Tables 3 and 4, accuracy is reported as point estimates without error bars, confidence intervals, or significance tests. Given that results are averaged over 600 tasks, standard deviations in few-shot benchmarks are typically 0.3–0.5%. Some reported improvements are as small as 0.2–0.5% (e.g., on CIFAR-FS 5-shot with LRDC), making it impossible to assess whether these gains are statistically meaningful. Without this information, the claim of "consistent improvement" is not fully rigorous.

### Minor

1. **The "diversity vs. representativeness" framing is asserted but never formally quantified**: The paper argues that category-level estimation provides "diversity" and instance-level provides "representativeness," and Tables 5 and 6 (likely in the appendix) provide some empirical grounding. However, these concepts are never formally defined or measured in the main paper. No metrics are introduced to quantify whether the fused distribution indeed produces samples that are both more diverse and more representative than either level alone. The core motivation of the paper rests on this distinction, yet it remains a conceptual intuition rather than a measured property.

2. **Instance-level estimation alone is nearly competitive with fusion in the 5-shot setting**: In Figure 5, for 5-shot, instance-level alone (α=0) achieves accuracy very close to the best fusion (α=0.2). The improvement from adding category-level statistics is <0.5% in this setting. This suggests that the category-level contribution is marginal when more support samples are available, which limits the practical significance of the hybrid design in higher-shot scenarios.

3. **No comparison of generated sample quality against baseline DE methods**: Table 2 shows KL divergence, mean similarity, and variance similarity between HGDE-generated samples and ground truth data. However, there is no comparison against samples generated by a baseline DE method (e.g., LRDC without instance-level estimation). Without this anchor, it is impossible to determine whether HGDE improves distribution fidelity relative to existing approaches, or merely produces different samples.

### Trivial

1. The weighting functions in Equations 6 and 10 (reciprocal square root of distance, and similarity raised to a power) are introduced without justification for their specific functional forms. They are reasonable heuristics, but the paper does not discuss why these forms were chosen over alternatives (e.g., softmax weighting, Gaussian kernels).

## Nice-to-Haves

- A cross-dataset sensitivity analysis for key hyperparameters (especially k, α, L) would substantially strengthen the generality claims.
- t-SNE or similar visualizations of generated samples from category-level, instance-level, and fused distributions alongside real support/query samples would provide intuitive validation of the "diversity vs. representativeness" narrative.
- Reporting results with confidence intervals or standard deviations over the 600 tasks would bring the evaluation in line with standard practice.

## Removed Points

*The reviewer's criticism about uncontrolled baseline comparisons (Weakness 2 in the Harsh Critic) is removed.* The paper's table captions explicitly state "† denotes our implementation." For methods like LRDC, Meta-Baseline, and SMKT, both the baseline and HGDE-augmented results carry this annotation, meaning they come from the same implementation with the same feature extractors, training protocols, and data splits. The concern that "only the HGDE-augmented version uses their implementation" is speculation that contradicts the paper's own annotation.

*The reviewer's concern about k=2 being "extreme" and "fragile" is weakened to trivial status.* The paper provides empirical evidence (Figure 3) that k=2 works best and larger k degrades performance, which is attributed to noise from additional categories. This is a reasonable empirical finding. While stability analysis across tasks would be nice-to-have, the method is evaluated over 600 tasks and produces consistent results, so fragility is not demonstrated.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a useful perspective: the key insight of the paper — that instance-level statistics can complement category-level statistics in distribution estimation — is well-supported by ablation but is partially undercut by the observation that improvement from fusion over instance-level alone is modest in the 5-shot setting. This suggests the paper's main practical value may be in the 1-shot regime where the instance-level signal is noisier.

## Suggestions

1. **Run the ablation studies (Figures 3–6) on at least one additional dataset** (e.g., CUB or CIFAR-FS) to demonstrate that the chosen hyperparameters are not Mini-ImageNet-specific. Even a single sensitivity figure showing accuracy with varying α on CUB would substantially improve confidence in the method's generality.
2. **Add standard deviations or 95% confidence intervals to Tables 3 and 4**, computed over the 600 evaluation tasks. This is a straightforward addition (standard practice in FSL) and would make the claimed improvements interpretable.
3. **Quantify "diversity" and "representativeness"** with simple metrics (e.g., intra-class variance for diversity, distance to support prototype for representativeness) and measure them for category-level, instance-level, and fused distributions. This would turn the paper's central conceptual framing from an intuition into a testable claim.
4. **Compare sample quality against a baseline DE method** (e.g., LRDC) in the style of Table 2, so readers can evaluate whether HGDE improves distribution fidelity beyond existing approaches.

**Calibration anchors** (all from the human-review corpus):

| Anchor | Path | Avg Human Score | Comparison |
|--------|------|-----------------|------------|
| Distribution Calibration for FSL by Bayesian Relation Inference | 8oZf2SlXEY.md | 4.33 (Reject) | Similar topic (DE for FSL). Our paper has much broader experiments (4 datasets vs. 1) and better ablations, making it clearly stronger. |
| Dist Loss (imbalanced regression) | YeSxbRrDRl.md | 6.67 (Accept) | Different domain. Similar incremental contribution level but stronger empirical validation. Our paper is weaker. |
| Context-Aware Meta-Learning | lJYAkDVnRU.md | 5.50 (Accept) | Similar acceptance level with comparable flaws (missing ablation was a criticism there too) and similar level of incremental contribution. Our paper's ablations are better, but hyperparameter concern is more serious. |
| BECLR (unsupervised FSL) | k9SVcrmXL8.md | 6.67 (Accept) | Stronger paper with more novelty, accepted. Our paper is more incremental. |
| MOKD (cross-domain FSL) | bzO7cusxBl.md | 6.25 (Reject) | Stronger theoretical contributions but was rejected due to limited novelty over prior work. Similar level of incremental contribution. |
| Projected Subnetworks | WM5G2NWSYC.md | 2.00 (Reject) | Very weak paper with fundamental methodological flaws. Our paper is substantially stronger. |

## Score and Decision

The paper makes a sensible incremental contribution to distribution estimation for few-shot learning. The ablation studies are thorough, the method is simple and integrable, and the empirical evaluation spans four benchmarks with multiple backbones. However, the contribution is modest (fusion over instance-level alone provides small gains, especially in 5-shot), and two issues prevent a stronger assessment: (1) all hyperparameters are tuned on a single dataset with no cross-dataset sensitivity analysis, leaving generality unproven, and (2) the main results lack confidence intervals, making it impossible to assess whether small reported gains are statistically significant. The paper would be strengthened by addressing these concerns, but in its current form it provides sufficient evidence of a useful, if incremental, improvement.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>