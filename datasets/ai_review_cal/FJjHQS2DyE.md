- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6
Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper proposes Conditional Adversarial Support Alignment (CASA) for unsupervised domain adaptation under label shift. The key idea is to align the supports of class-conditional feature distributions (via a novel Conditional Symmetric Support Divergence) rather than marginal feature distributions as done in prior work (ASA). The paper provides a theoretical target risk bound (Theorem 1) that justifies conditional over marginal support alignment, and implements the approach via an adversarial training scheme that uses a joint representation (feature × classifier output) and pseudo-labels. Experiments on USPS→MNIST, STL→CIFAR, and VisDA-2017 under five levels of Dirichlet-sampled label shift show CASA outperforming baselines on 11/15 transfer tasks.

## Strengths

1. **Novel conditional support divergence and associated target risk bound.** Theorem 1 and Lemma 1 provide an upper bound on target risk that uses per-class localized hypothesis spaces and conditional symmetric support divergence (CSSD) rather than marginal SSD. Remark comparing CSSD vs. SSD (lines 156–167) correctly identifies the trade-off: per-class sup-norm terms are tighter even though the conditional distance terms can be larger. This is a genuine theoretical contribution that goes beyond the existing ASA framework.

2. **Consistent empirical gains across multiple datasets and shift levels.** The paper reports average per-class accuracy on USPS→MNIST, STL→CIFAR, and VisDA-2017 under five Dirichlet α levels. CASA outperforms baselines on 11/15 transfer tasks and achieves the highest average accuracy across all three datasets (e.g., 4.1% above second-best on USPS→MNIST, 1.8% on STL→CIFAR, 1.0% on VisDA-2017). It specifically exceeds ASA and IWCDAN, the most directly related label-shift methods.

3. **Visualization of feature embeddings corroborates the core claim.** Figure 2 shows that on a 3-class subset with severe label shift, CASA achieves 99% accuracy with CSSD=0.02 versus ASA's 93% with CSSD=0.05 and CDAN's 85% with CSSD=0.13, visually demonstrating that conditional support alignment produces better-separated class clusters than marginal alignment.

4. **Theoretical justification for the joint-distribution proxy.** Proposition 1 proves that zero CSSD is equivalent to zero joint support divergence between P^S_{Z,Ŷ} and P^T_{Z,Ŷ}, providing a principled basis for minimizing CSSD via the joint discriminator without requiring target labels.

5. **Ablation study validates all loss components.** Table (referenced as Table 1) shows that removing L_align, L_ce, or L_v reduces accuracy across all shift levels on USPS→MNIST, confirming that all three terms derived from the bound are necessary.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The distance function `d` in the alignment loss L_align is underspecified.** Equation (loss:ssd) defines L_align using `d(r(s(x_i^S)), {r(s(x_j^T))})` but does not specify the form of `d` (e.g., distance to nearest neighbor, mean distance, or a specific metric). The paper states "d is a proper distance" (Definition 1) and "a well-defined distance" (before Definition 2), but the exact distance used in the implementation is never stated. While the approach follows the ASA framework (Tong et al. 2022) and the discriminator outputs are scalars in [0,1] where several natural choices coincide, the paper should specify the metric for reproducibility.

2. **Pseudo-label error is mentioned but not analyzed.** The paper employs pseudo-labels to approximate the conditional distributions and mentions entropy conditioning (Long et al. 2018) to mitigate error accumulation (line 205), but provides no analysis of pseudo-label accuracy during training, how error propagates under severe shift (α=0.5), or how effectively entropy conditioning addresses the issue. Given that Proposition 1 relies on the assumption that P^S(Ŷ=y)>0 and P^T(Ŷ=y)>0, some analysis of whether this holds during training would strengthen the paper.

3. **Gap between the theoretical bound and the practical training objective is acknowledged but not bridged.** Theorem 1 includes terms (Σ q_k δ_k + p_k γ_k and the ideal joint risk) that are "assumed to be small" in the optimization (Remark after Theorem 1). The bound also depends on per-class localization parameters r^1_k, r^2_k that are not explicitly set in the algorithm. The paper is transparent about these assumptions, but the chain of relaxations from the bound to the loss is not analyzed. This is standard practice for theory-motivated DA papers, but a simplified bound that maps more directly to the loss terms would strengthen the presentation.

4. **No discussion of hyperparameter sensitivity.** The loss uses four weighting parameters (λ_align, λ_y, λ_ce, λ_v) with no sensitivity analysis. While this is common in multi-objective DA methods, a brief discussion of stability or a reference to the setting procedure would improve the paper.

### Trivial

- The paper does not specify how the outer product `f(x) ⊗ g(x)` is flattened/vectorized for the discriminator (though this follows CDAN, Long et al. 2018, which is cited).

## Nice-to-Haves

- Report pseudo-label accuracy during training (or on source as a sanity check) to quantify the robustness of the conditional support proxy.
- Add a simplified version of the bound that directly connects to the loss terms being optimized (e.g., L_T(g) ≤ L_S(g) + E_T[H(g)] + D^c_supp(...) + constants under appropriate conditions).
- Include runtime/model size comparison with ASA since the joint outer product increases dimensionality.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Harsh Critic's claim about outer product flattening being unspecified**: The paper explicitly says this follows Long et al. 2018 (CDAN), so this implementation detail is a reference to existing work, not a missing piece. Removed.
- **Harsh Critic's criticism about tables not being visible**: The tables are included via `\input`, which is standard LaTeX. The paper text summarizes the results clearly. The reviewer acknowledges this is a weakness of the review process, not the paper. Removed as per instructions about missing appendix content.
- **Strength Finder's claim that "Complete training algorithm directly derived from the bound"**: This overstates the connection; the authors acknowledge assumptions and gaps between the bound and the loss. Weakened into weakness #3 above.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's own narrative: the novel conditional support divergence is well-motivated, the bound is a genuine contribution, and the experiments are solid. The main observations from the reviews are about presentation gaps (distance definition, pseudo-label analysis) rather than fundamental flaws.

## Suggestions

1. **Specify the distance metric `d` explicitly.** A single sentence clarifying whether L_align uses nearest-neighbor distance, mean distance to the k nearest neighbors, or the specific form from ASA (Tong et al. 2022) in the discriminator output space would resolve the reproducibility concern.
2. **Add pseudo-label accuracy curves or error analysis.** Even a simple plot of pseudo-label accuracy during training (or a comparison with/without entropy conditioning) would address the concern about error amplification under severe shift.
3. **Include hyperparameter sensitivity results** for the four loss weights, either as a table or a brief remark about how they were selected (e.g., grid search on a validation set).
4. **Simplify the bound presentation.** Consider presenting a simplified corollary of Theorem 1 that drops the per-class localization parameters (assuming full hypothesis space) to directly connect to the loss: L_T(g) ≤ L_S(g) + E_T[H(g)] + D^c_supp(...) + constant. This would make the bound immediately actionable for readers.
