Now I have a thorough understanding of the paper and can verify the reviewer's claims against the actual content. Let me produce the consolidated review.

## Summary

The paper proposes Polyak Parameter Ensemble (PPE), a technique that maintains a running weighted average of model parameters obtained at each epoch interval during training. The method is applied to Knowledge Graph Embedding models (DistMult, ComplEx, QMult) and tested on link prediction, multi-hop query answering, and image classification tasks across 11 benchmark datasets. The key idea is that parameter averaging (with exponential epoch weights) improves generalization at no additional test-time cost.

## Strengths

- **Consistent generalization improvement across diverse models, datasets, and tasks**: Tables 4–7 report that PPE improves link prediction MRR and Hits@N for DistMult, ComplEx, and QMult on all seven benchmark datasets for link prediction, and Table 7 shows improved multi-hop query answering. This breadth of positive results supports the paper's main claim that parameter averaging helps generalization.

- **Simple, cost-effective method with principled foundation**: The paper provides a formal derivation (Section 3) showing how parameter averaging at epoch intervals relates to Polyak averaging and can mitigate the "circling" behavior around a minimum caused by noisy mini-batch gradients. The method requires no additional test-time memory or inference cost.

- **Parameter-scaling analysis reveals boundary conditions**: Table 8 systematically varies embedding dimension d ∈ {4, 8, 16, 32, 128, 256} and shows that PPE's benefits become more tangible as d grows, while dissipating for d ≤ 4. This provides practical guidance on when the method is most useful.

## Weaknesses

### Fatal
None.

### Major

- **Missing comparison to SWA as a baseline**: The paper cites Izmailov et al. (2018) (SWA) in the related work but does not include SWA as an experimental baseline. PPE with uniform epoch weights is closely related to SWA (which averages parameters along the trajectory, typically using uniform weights). Without a direct comparison, it is difficult to assess whether the exponential weighting scheme provides meaningful improvements over the existing state of the art. The paper does compare uniform (λ=1.0) vs. exponential (λ=1.1) weights in Table 8, and finds only marginal differences ("Using the 1.1 growth rate leads to a slight improvement over no growth rate"), which further underscores the need for a clear comparison to prior parameter-averaging methods.

- **Ambiguity around the j=200 choice and risk of degenerate ensembles**: Section 4.1 states that the ensemble-start epoch j is fixed at 200 for all datasets, while the number of training epochs N is chosen from {200, 250}. If any dataset uses N=200, setting j=200 would mean α_{0:200}=0 and α_{201:200} is empty, reducing the ensemble to the final model weights — completely invalidating the claimed benefit from parameter averaging on those datasets. The paper does not specify which N value is used for which dataset, making this impossible to verify. This is a critical experimental design flaw that the authors must address.

- **No statistical significance or variance reporting**: All tables report single numbers with no standard deviations, confidence intervals, or multiple-seed results. Many improvements are small (e.g., Table 4: MRR from 0.010 → 0.011 on YAGO3-10 for QMult; 0.003 → 0.003 for DistMult). Without uncertainty estimates, it is impossible to determine whether these improvements are real or within run-to-run noise. This is the single most important fix needed.

### Minor

- **The dynamic α determination method is proposed but never evaluated**: Section 3.1 proposes determining α dynamically by tracking validation loss (akin to early stopping). However, Section 4.1 explicitly states this approach was not used ("we did not dynamically determined α by tracking the validation loss"). The paper claims this as a contribution but provides no experimental evidence for its effectiveness.

- **Unsubstantiated claims about computational cost**: The paper claims "virtually no additional computational cost" and "we did not detect any runtime overhead of using PPE," but reports no actual runtime measurements, peak memory usage, or FLOPs comparisons. While a running average plausibly has low overhead, the claim is presented as an empirical finding without supporting data. Additionally, the paper describes PPE as a "running weighted average" (which requires only one extra copy of parameters), but the formal definition in Eq. 3 as a sum over all Θ_i could be read as requiring storage of all epoch checkpoints. This implementation detail needs clarification.

- **Ambiguity about which λ is used in main experiments**: The paper reports λ ∈ {1.0, 1.1} as hyperparameters but does not clearly state which value produced the results in Tables 4–7. Table 8 clarifies that PPE with λ=1.1 is denoted PPE† and that "using the 1.1 growth rate leads to a slight improvement over no growth rate," but the main results tables lack this distinction.

- **Modest effect sizes**: The reported improvements are often very small (e.g., 0.001–0.003 in MRR on several datasets). While consistent across datasets, the practical significance of such small gains is unclear, especially without variance estimates.

### Trivial

- The notation is slightly inconsistent — Θ and w are used interchangeably for parameter vectors (e.g., Eq. 3 vs. Eq. 7 and surrounding text).

## Nice-to-Haves

- A comparison of PPE to prediction averaging (training K independent models) would help quantify the cost-benefit trade-off, even if prediction averaging is computationally expensive.
- Analysis of the effect of varying j (e.g., for N=250, test j ∈ {200, 225, 240, 249}) would strengthen the understanding of this key hyperparameter.
- Training loss curves showing the claimed "less zigzagging" behavior would substantiate the intuition in Figure 2.

## Removed Points

1. **Claim that FB15K-237 and YAGO3-10 specifically use N=200**: The paper states "N ∈ {200, 250}" as hyperparameter configurations but does NOT specify which N is used for which dataset. This claim by the reviewer is factually unsupported. *(The general concern about j=200 with N=200 is retained in Major weaknesses above.)*

2. **Claim that PPE requires storing all Θ_i (N× model size)**: The paper explicitly describes PPE as a "running weighted average" that is "updated at each epoch interval," implying an online update rather than storage of all checkpoints. The reviewer's specific claim of N× memory is contradicted by the paper's text. *(The need for implementation clarification is retained in Minor weaknesses.)*

3. **Claim that "no comparison to standard Polyak averaging (uniform epoch weights) is reported"**: The paper DOES compare uniform (λ=1.0) vs. exponential (λ=1.1) weights in Table 8 and mentions uniform weights in Figure 1. The reviewer's claim that no such comparison exists is incorrect. *(The lack of clarity about which λ produced the main results is retained in Minor weaknesses.)*

4. **Pure formatting/style nitpicks and claims about missing appendix content**: The parser strips these sections; they exist in the original submission.

5. **Generic criticisms that demand scope-creep experiments** (e.g., requiring comparison to prediction averaging as a baseline — retained in Nice-to-Haves).

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the reviews is that the combination of (a) the j=200 = N concern and (b) the consistently positive but tiny improvements across all datasets raises a genuine question: could the reported improvements be artifacts of the experimental setup (e.g., implicit regularization from the running average updating procedure, or differences in effective learning rate schedule) rather than evidence that parameter averaging fundamentally improves generalization? The paper's discussion does not consider alternative explanations for the observed improvements, which would strengthen the overall argument.

## Suggestions

1. **Run all experiments with ≥5 random seeds and report means ± std. dev.** This is the highest-priority fix. Without it, the small improvements are uninterpretable.

2. **Clarify which N (200 or 250) is used for each dataset and ensure j < N for all experiments.** If any dataset uses N=200 and j=200, those results must be re-run with j < N or acknowledged as not using the ensemble.

3. **Include SWA as a baseline** (uniform parameter averaging over the last 5–10 epochs, as in Izmailov et al., 2018) to establish the marginal benefit of exponential weighting.

4. **Report actual training-time memory and runtime measurements** to substantiate the "no additional cost" claim, and clarify whether the running weighted average is implemented as an online update.

5. **Specify which λ value is used in Tables 4–7** and consider adding a column showing both variants.

## Score and Decision

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>