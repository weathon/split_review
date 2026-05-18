Now I have enough information to produce the consolidated review. Let me carefully construct it.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves
## Removed Points
## Novel Insights
## Suggestions
## Score and Decision

Let me write the final review now.

---

Here is my consolidated final review:

## Summary

This paper tackles hyper-parameter optimization and model selection for unsupervised anomaly detection (UAD) without any labeled anomalies. It proposes three surrogate metrics — RTM, EAG, and NPD — that approximate expected test performance from the unlabeled training set alone. NPD, the main contribution, compares anomaly scores on a validation split from the training data against scores on data generated from an isotropic Gaussian fitted to the training data. The metrics are integrated with Bayesian optimization (TPE) to search for optimal hyper-parameters. Experiments on 38 datasets with four UAD methods (OCSVM, AE, DeepSVDD, DPAD) show NPD consistently outperforms existing unsupervised model-selection heuristics (MV/EM, MC, HITS) and baselines (Default, Random).

## Strengths

1. **Creative and principled surrogate metric (NPD).** The idea of using Gaussian-generated data as a reference set for evaluating UAD models without labels is novel and intuitively appealing. NPD's formulation (Definition 6) — measuring the mean-difference-to-variance ratio between validation scores and Gaussian-generated scores — is simple, has a clean geometric interpretation (Figure 4), and is grounded in the intuition that a good UAD model should assign higher scores to out-of-distribution synthetic points than to real validation points.

2. **Strong empirical results across diverse settings.** On 38 benchmark datasets with four different UAD methods (shallow and deep), NPD-guided BO achieves the highest mean AUC and F1 scores in 3 out of 4 methods (Table 1), with statistical significance reported (p-values). The UOMS grid-search study (Table 2) similarly shows NPD/RTM outperform consensus-based methods (MC, HITS). The Spearman rank correlation of 1 between NPD and AUC/F1 (Figure 6) provides direct evidence of monotonicity, which is exactly the property demanded by the surrogate formulation (Equation 3).

3. **Clear problem framing and scope.** The paper carefully distinguishes the UAD setting (inductive learning from normal-only training data) from the transductive outlier detection setting where training data contains anomalies (Section 2). It also clearly defines the AutoUAD problem (Definition 2) with two explicit goals: optimizing hyper-parameters per method and selecting the best method. This precise framing clarifies the contribution and avoids confusion with prior work that assumes different settings.

4. **Validation in both BO and UOMS settings.** Unlike many papers that only show one usage scenario, this work evaluates the metrics in two distinct settings: Bayesian optimization for hyper-parameter search (Goal 1) and grid-search model pool selection (Goal 2, UOMS). The NPD metric performs well in both, demonstrating robustness across usage paradigms.

## Weaknesses

### Fatal
None.

### Major

1. **The validation split ratio $M$ is never specified or ablated, despite NPD being called "hyper-parameter-free."** Definition 6 splits training data into $\mathcal{X}_{\text{trn}}$ (size $N-M$) and $\mathcal{X}_{\text{val}}$ (size $M$), with $M$ also being the size of the generated Gaussian set. However, the paper never states what $M$ is (e.g., 10%/20%/50% of training data), provides no ablation showing sensitivity to this choice, and offers no principled rule for setting it. Calling NPD "hyper-parameter-free" while $M$ is a free design choice is misleading. This matters because if the metric is sensitive to $M$, results could be cherry-picked; if it is robust, that should be demonstrated.

2. **BO implementation details are underspecified for reproducibility.** The paper states "We utilize BO with Tree-structured Parzen Estimator (TPE)" (Section 3.4) but does not report: the number of BO iterations, the number of initial random trials, TPE kernel/estimator parameters, or whether the search is repeated independently per data split or conducted once and evaluated across splits. The search spaces for each UAD method's hyper-parameters are referenced only by example (e.g., "the search space for $\gamma$ is $(0,\infty)$" — which is impractical as stated) and deferred to a Table 4 that is not in the main paper. While some details may be in the (parser-stripped) appendix, the main paper should provide a summary sufficient for understanding and replication.

### Minor

3. **Theorem 2's practical grounding is limited.** The theorem bounds NPD by the score gap between normal and anomalous data, but the bound depends on an unknown decomposition of $\mathcal{X}_{\text{val}}$ and $\mathcal{X}_{\text{gen}}$ into normal and anomalous subsets. Since this decomposition is unavailable in practice (the whole point is that labels are absent), the theorem does not provide an actionable guarantee that maximizing NPD widens the true normal-anomaly gap. The paper's interpretation ("When maximizing NPD, the gap also becomes larger") is suggestive but not rigorously justified by the theorem as presented. This does not invalidate the empirical results but weakens the claimed theoretical support.

4. **RTM and EAG are presented as co-equal contributions but are acknowledged to be inferior.** The abstract and introduction list all three metrics as contributions, yet the paper states that RTM and EAG "do not always work well," "could overfit the training data when implemented on a complex UAD model," and "both have an additional hyper-parameter to determine." The experiments confirm they are consistently outperformed by NPD. The paper would be stronger and more coherent if it positioned RTM/EAG as failed attempts or ablative baselines, and focused the contribution narrative on NPD.

5. **The Gaussian reference set's effectiveness is not systematically analyzed.** The paper provides intuitive justification (max-entropy, Theorem 1, qualitative examples in Figures 3/4) and validates empirically on 38 datasets, but does not analyze *when* the Gaussian proxy works well versus poorly. The paper itself notes "the highest NPD did not always correspond to the best model performance" (Conclusion). Understanding the failure cases — e.g., is NPD weak on datasets with highly multimodal or correlated features? — would significantly strengthen the contribution. A simple simulation with known ground truth would help validate the mechanism.

### Trivial

6. The paired t-test p-values are reported (Table 1) but the pairing structure is not explained — are tests paired across datasets? Across splits? What are the degrees of freedom?

7. The paper states "search space for $\gamma$ is $(0,\infty)$" (Remark 3.2) which is obviously impractical for any search algorithm; presumably practical ranges were used in experiments, but this is not mentioned.

## Nice-to-Haves

- An ablation study on the split ratio $M$ to justify the (implicit) default value and demonstrate robustness.
- A controlled simulation study (e.g., Gaussian mixture with known normal/anomaly components) to directly verify that NPD is monotonically related to AUC when the Gaussian reference distribution is appropriately constructed.
- A comparison of NPD's Gaussian-based generation against other reference distributions (e.g., uniform over the data range, bootstrap resampling, or a fitted Gaussian mixture) to justify the Gaussian choice beyond the entropy argument.
- Timing/scalability analysis to support the claim that the method is "scalable to larger datasets."

## Removed Points

The following points from the inputs were removed with justification:

- **Meta-learning baselines omitted**: Removed. The paper explicitly scopes itself to fully unsupervised methods without historical labeled data. Meta-learning methods (Zhao et al., 2021; 2022; Zhao & Akoglu, 2024; Ding et al., 2024) require labeled historical datasets, which is a fundamentally different setting. The Max oracle is an upper bound, not a competing method — criticizing it as "using supervision" misses its purpose.
- **"Gaussian assumption is strong and untested" / "no systematic analysis across datasets"**: Demoted to Minor #5. The paper empirically tests the method on 38 datasets with positive results; the concern is about mechanistic understanding, not empirical validity.
- **"The paper never shows that RTM, EAG, or NPD satisfy monotonicity"**: Partially inaccurate — Figure 6 shows Spearman rank correlation = 1 for NPD on the displayed datasets. Limited scope, but not absent. Kept as part of Minor #3 (theoretical grounding).
- **Missing appendix/proof content**: Removed. The parser strips appendices; they exist in the original submission.
- **"Exclusion of datasets >50k is arbitrary"**: Removed. This is a pragmatic time/resource constraint acknowledged by the authors.
- **Code not provided**: Removed. Reproducibility requirements for a conference submission do not typically include complete codebases. Hyper-parameter search spaces (likely in stripped Table 4) and experimental details are the relevant concern, addressed in Major #2.
- **Figure 7 (t-SNE) criticism**: Removed. t-SNE visualizations are standard qualitative illustrations; requesting them to be quantitative misunderstands their purpose.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Specify the split ratio $M$ in the NPD definition (or at least the default used in experiments) and include an ablation showing AUC/F1 as a function of $M$. This is the single most actionable fix to strengthen the main claim that NPD is "hyper-parameter-free."
2. Summarize the BO configuration (iterations, initial random trials, search space ranges) in the main paper's experimental section, even if full details remain in the appendix.
3. Reframe the contribution to clearly highlight NPD as the primary contribution, with RTM/EAG treated as preliminary attempts or additional baselines rather than co-equal contributions.
4. Add a brief failure analysis section or paragraph discussing datasets/conditions where NPD underperforms relative to Random or other baselines.

## Score and Decision

**Originality** (7/10): The NPD metric is genuinely novel. Using Gaussian-generated reference data as a surrogate for unseen anomalies is creative and well-motivated.

**Importance of research question** (8/10): Hyper-parameter tuning for UAD without labels is a practically important and under-studied problem.

**Claims well-supported** (6/10): The empirical evidence is strong (38 datasets, 4 methods), but the underspecified split ratio and lack of mechanism validation weaken the support for the core claim.

**Soundness of experiments** (6/10): Reasonably thorough but missing ablation on M and BO details limit reproducibility assessment.

**Clarity of writing** (7/10): Generally clear, with precise definitions. The narrative around RTM/EAG vs NPD could be cleaner.

**Value to community** (7/10): If the split ratio issue is resolved, this would be a useful contribution for practitioners deploying UAD.

The paper presents a creative and well-evaluated approach to a real problem, with the main empirical claim (NPD outperforms existing unsupervised heuristics) supported by evidence on 38 datasets. The core weakness is the unstated and unablated split ratio $M$, combined with insufficient BO detail for reproducibility. Neither issue invalidates the contribution, but both should be addressed. Overall, this is a solid paper that makes a meaningful contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>