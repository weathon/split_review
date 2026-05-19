- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 5, 6
Now I have all the evidence I need. Let me produce the final consolidated review.

## Summary

The paper proposes **Concept Influence for Fairness (CIF)**, a framework that generalizes influence functions for model fairness from simple removal/reweighting of training samples to counterfactually changing samples along "concepts" (sensitive attribute *A*, label *Y*, or features *X*). The core idea is to compute how fairness would change if a training sample's concept were overridden (e.g., "what if this applicant were from a different demographic group?"), providing both an explanation tool and a data-repair mechanism. The paper evaluates CIF on four datasets (synthetic, COMPAS, Adult, CelebA) across three fairness metrics, and demonstrates mitigation, mislabeling detection, poisoning defense, and resampling applications.

## Strengths

1. **Conceptually novel generalization of fairness influence beyond removal/reweighting.** Section 2.2–2.3 formalizes the idea of "concepts" (A, Y, X, removal) and derives CIF in Proposition 2. Prior work (Wang et al. 2022a, Li & Liu 2022) only considered removal or reweighting; CIF extends this to counterfactual changes along any concept, enabling a richer set of "what if" questions about fairness causes. This is a genuine conceptual advance.

2. **Empirical mitigation results across multiple datasets and fairness metrics.** Figures 2–4 show that applying CIF's recommendations (replacing high-influence samples with counterfactuals) consistently reduces Demographic Parity, Equality of Opportunity, and Equality of Odds gaps on synthetic, COMPAS, Adult, and CelebA data. The comparison against "random" and "removal" baselines supports that concept-specific overrides add value beyond mere sample deletion.

3. **Practical counterfactual generation for non-identifiable settings.** Section 3.1 provides a W-GAN-based method for generating counterfactual samples when the causal graph is not identifiable, with an ℓ₂ cost to keep generated samples close to original. The framework is designed to accept better counterfactual generators as they become available, making it forward-compatible.

4. **Additional applications demonstrating the framework's versatility.** Section 4.2 shows CIF can detect mislabeled samples, identify backdoor-poisoned samples, and recommend rebalancing of imbalanced representations. These go beyond pure mitigation and illustrate the broader utility of the CIF concept.

## Weaknesses

### Fatal
None.

### Major

1. **Counterfactual generation quality is not validated.** The entire pipeline depends on the quality of counterfactual samples produced by the W-GAN (for overriding *A* and *X*), yet the paper provides **no direct evaluation** of counterfactual quality — no distributional distance metrics, no visual examples (even for CelebA), no assessment of whether generated feature vectors are realistic. The paper states (line 116) that "the effectiveness of our solution depends on finding a proper transform" but never verifies that the specific W-GAN transform used is adequate. Without this, fairness improvements from overriding could stem from artifacts in the generated samples rather than meaningful concept changes. This is a methodological gap that undercuts confidence in the pipeline.

2. **Influence approximation accuracy is validated on only one dataset (COMPAS) with one metric (DP).** Figure 6 shows the CIF estimate correlates with actual fairness change only for COMPAS + Demographic Parity. The paper provides no similar validation for COMPAS with EOP/EO, or for Adult, synthetic, or CelebA datasets. This matters because the paper acknowledges (line 185) that the convexity assumption required for the Hessian approximation "is often violated" and convergence "would suffer." For deep models on CelebA, the approximation may be substantially less reliable. The claim that "our influence value can estimate the fairness change reasonably well" (line 216) is only supported for a single (tabular, logistic-model) setting.

3. **The paper does not deliver on its title's promise of "understanding unfairness."** The abstract and introduction emphasize *understanding* the causes of unfairness through explanation. However, the experiments are overwhelmingly about *mitigation* (fixing unfairness). The only explanatory content is a brief mention of the "distribution of CIF" (presumably in the appendix). There is no qualitative analysis of what high-CIF samples look like, no case studies connecting influential samples to domain knowledge, and no analysis of whether the explanations align with known sources of bias. The detection applications (mislabeling, poisoning) provide some diagnostic utility, but the paper does not substantiate its central framing as an *understanding* tool.

### Minor

1. **Additional applications lack meaningful baselines.** For mislabeling detection, the paper compares only to "randomly flagging the same percentage" (line 233). For poisoning defense and resampling, no detection/reweighting baselines are mentioned in the main text. Without comparisons to standard methods (e.g., influence on accuracy, training loss percentile, spectral signatures for poisoning), it is unclear whether CIF adds value for these tasks or merely reflects generic properties of high-loss samples.

2. **No comparison to the exact methods of prior influence-based fairness works.** The paper claims (line 14) to "generalize" Wang et al. 2022a and Li & Liu 2022, but the only baseline related to these works is "removal" — a CIF concept, not a direct re-implementation of those methods. This is partially mitigated because removal is the core operation in Wang et al. 2022a, but Li & Liu 2022's reweighting approach is not compared at all. A direct comparison would more convincingly demonstrate the claimed advantage.

3. **Fairness-utility tradeoff compared to only one in-processing method.** Figure 5 compares CIF-based mitigation to Agarwal et al. 2018 on COMPAS alone. Other pre-processing or in-processing methods (e.g., Kamiran & Calders 2012 reweighing, fair generative oversampling) would provide a more complete picture of where CIF stands relative to the broader fairness toolbox.

4. **No analysis of the number of overridden samples (a key hyperparameter).** The mitigation results depend on how many high-CIF samples are replaced, but the paper does not report this number or perform sensitivity analysis. Error bars in Figures 2–4 sometimes overlap between CIF and baselines, and no statistical significance testing is reported.

### Trivial
None.

## Nice-to-Haves
- A sensitivity analysis of the ℓ₂ cost weight in the W-GAN objective (Section 3.1), exploring the trade-off between counterfactual conservatism and meaningful change.
- A brief discussion of the computational cost of training per-concept W-GANs and computing Hessian-vector products for deep networks, which would help practitioners assess feasibility.
- Statistical significance tests (e.g., paired t-tests across retraining runs) to quantify whether CIF improvements over baselines are reliable given overlapping error bars.

## Removed Points

These points from the inputs were excluded or moved here with justification:

- **"No discussion of scalability for image datasets"** (Harsh Critic): This is a nice-to-have but does not threaten any core claim. Moved to Nice-to-Haves.
- **"Section 2: fairness loss surrogate uses logit g instead of hard predictions"** (Harsh Critic): Using a differentiable surrogate is standard practice in this literature (the paper cites Wang et al. 2022a and Sattigeri et al. 2022 for the same approach). This is a known engineering choice, not a weakness.
- **"Section 2.2: reweighting not explicitly discussed as a concept"** (Harsh Critic): Trivial observation; reweighting is a continuous-weight variant of removal, and the paper's framework (which includes removal) can readily accommodate it. This does not weaken the paper.
- **"Section 2.3: empirical approximation creates risk"** (Harsh Critic): The paper explicitly acknowledges this (lines 90–92, 116) and states that better methods can be plugged in. Repeating the acknowledgment as a weakness is redundant.
- **"Section 3.2: convexity assumption violated"** (Harsh Critic): The paper acknowledges this (line 185) and refers to the literature on this well-known limitation. The point is already self-contained in the paper.
- **Strength Finder's generic strengths** ("this paper addressed an important problem," "the problem is important"): Removed as generic/superficial — every paper claims its problem is important. Only concrete, evidence-grounded strengths are retained.

## Novel Insights

The reviews do not surface any genuinely novel observation beyond the paper's own contribution. The main value of the reviews is in identifying the gap between the paper's framing ("understanding unfairness") and its experimental emphasis (mitigation), and in highlighting specific missing validation pieces (counterfactual quality, broader influence accuracy checks). These are useful for revision but do not constitute a new analytical insight about the method itself.

## Suggestions

1. **Validate counterfactual quality directly.** Report distributional distances (e.g., Wasserstein distance, MMD) between generated and real samples for each concept override. Show visual examples of counterfactual images for CelebA. Demonstrate that overriding with random (untrained) counterfactuals produces worse results, establishing that the specific W-GAN transform matters.

2. **Broaden influence accuracy validation.** Show the correlation between estimated and actual fairness change (as in Figure 6) for all datasets and all three fairness metrics. Report R² or Pearson correlation coefficients.

3. **Add a qualitative understanding case study.** For one dataset (e.g., COMPAS), analyze the top-CIF samples: what are their characteristics? Why are they influential? Do the identified samples align with domain knowledge about where bias originates? This would directly support the paper's title and framing.

4. **Include direct comparisons to prior influence-based fairness methods.** Implement the removal-based method from Wang et al. 2022a and the reweighting-based method from Li & Liu 2022 on the same datasets and metrics, and show whether CIF's concept-level overrides yield better mitigation or detection.

5. **Add baselines for the three additional applications.** For mislabeling detection, compare to influence on accuracy (Koh & Liang 2017) and training loss percentile. For poisoning defense, compare to spectral signatures or activation clustering. For resampling, compare to naive random oversampling/undersampling.
