- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3
Now I have a thorough understanding of the paper and the reviews. Let me produce the final consolidated review.

## Summary

This paper proposes a method to enforce topological constraints — specifically contact ratio (heart chambers) and minimum distance (spine vertebrae) — in multi-part 3D reconstruction using implicit signed distance functions. The approach refines latent vectors of DeepSDF models by sampling points, identifying topologically meaningful regions, and minimizing compatibility losses that push surfaces toward or away from these points. Results on heart and spine reconstruction show reduced penetration and improved constraint satisfaction compared to independent SDF fitting.

## Strengths

- **Novel differentiable formulation of contact ratio via Monte Carlo sampling (Eq. 2).** The paper derives a sampled approximation of the contact ratio as a function of signed distances, enabling gradient-based optimization through latent vectors. This is the key technical contribution and is clearly explained in Section 3.2.1.

- **Quantitative improvements on out-of-distribution heart data (Table 1).** The method reduces Chamfer distance (e.g., LV from 1.50 to 0.50) and penetration ratio (e.g., M-LV-LV from 8.25% to 0.15%) compared to independent SDF fitting, while achieving contact-ratio accuracy close to the prior. The qualitative results (Fig. 3) corroborate the numbers.

- **Ablation study validates each loss component (Table 3).** Removing any of ℒ_intersecting, ℒ_contact, or ℒ_non-contact substantially increases topological errors, confirming that the joint loss design is necessary and correctly motivated.

- **Unified framework handles two fundamentally different constraints.** Sections 3.2 and 3.3 show that the same sampling-and-loss pattern enforces both a precise contact ratio (heart) and a minimum-distance gap (spine) with only a change in the definition of topologically meaningful points and loss function. Successful results on both use cases (Tables 1–2) demonstrate generality.

## Weaknesses

### Fatal
None.

### Major

- **Underspecified ground-truth source for the OOD heart evaluation.** The paper reports "average absolute difference contact ratio (%) from the ground-truth" on the in-house OOD dataset (Table 1), but never explicitly states whether manual segmentations exist for these 10 images or how they were obtained. The dataset is described only as "obtained from a nearby hospital's radiology department" (line 194) with no annotation protocol. While it is reasonable to assume ground truth exists (otherwise Chamfer distance and contact-ratio error could not be computed), the omission is a significant reporting gap that undermines reader confidence in the paper's central quantitative claim. This must be clarified in the final version.

### Minor

- **Key hyperparameter values not reported.** The paper introduces ε (a threshold for contact proximity, Eq. 2) and λ₁–λ₄ (loss weights, Eq. 8) but never specifies their numerical values. Without these, the method cannot be reproduced and the sensitivity of results to these choices cannot be assessed. The paper does report that 300K points are used with updates every 10 iterations (line 161), so some details are present — the missing values are a non-trivial gap.

- **No variance or statistical significance on quantitative results.** All tables report single aggregate numbers without standard deviations, confidence intervals, or error bars. The heart ID test set has only 5 samples and OOD has 10. Without variance information, it is impossible to judge whether reported improvements are meaningful or could arise from random variation. This is standard to expect even for modest-sized medical test sets.

- **Ablation study conducted on only one pair (LV and myocardium) in the OOD set.** While the ablation usefully validates each loss term, the paper does not discuss whether the findings generalize to other component pairs (e.g., LV-RA, LA-RV) or the spine case, where the constraints differ. This limits the strength of the ablation conclusions.

- **Constant-denominator assumption stated but unvalidated.** The paper assumes the denominator in Eq. 2 (reflecting combined surface areas) "tends to remain relatively constant during optimization" (line 111). This is a plausible claim, but no empirical evidence (e.g., a plot of the denominator over iterations) is provided to support it. A simple verification would strengthen the paper.

### Trivial
None.

## Nice-to-Haves

- A sensitivity analysis for ε and λ weights (e.g., varying one at a time) would demonstrate robustness.
- A convergence plot showing loss and topological metrics over optimization iterations.
- A discussion of whether the contact-ratio priors (computed from training data) remain valid for pathological or severely deformed anatomies, since the paper currently limits the spine experiment to healthy subjects but does not discuss this for the heart case.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Contact ratio prior may not hold for OOD cases" (Harsh Critic #2):** The paper explicitly states that contact ratios are "known *a priori* from centuries of medical practice" (line 22) and that such ratios are "consistent across all annotated instances" (line 65). The claim that priors might not generalize to OOD data is a speculative concern not grounded in the paper's own description of the domain. The paper does pre-compute priors from training data (line 192), but the anatomical claim stands independently. **Removed as a strawman.**

- **"nn-UNet trained on only 15 images — test scenario is quite specific" (Harsh Critic, section-by-section):** This is an intentional experimental design choice to demonstrate the method's value when training data is scarce (the paper notes "only images of 20 cases are publicly available," line 192). Criticizing this as a weakness misreads the experimental setup. **Removed.**

- **"No comparison to alternative constraint-enforcement approaches" (Harsh Critic, Missing Parts):** The paper provides a mesh-refinement baseline as an alternative (lines 215–217). Requesting comparisons to Lagrange multipliers or occupancy networks is scope creep beyond what the paper sets out to demonstrate. **Removed.**

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation about the interaction between the contact loss and intersection loss (points inside one object and outside the other being pushed toward the same location) is a genuine subtlety, but the paper already includes a separate intersection loss that addresses this case, and the ablation confirms the joint design works. No genuinely new synthesis emerges from the reviews that the paper itself does not articulate.

## Suggestions

1. **Clarify the OOD ground truth explicitly** — state whether the in-house dataset was manually annotated, by whom, and the annotation protocol. If the "ground-truth" contact ratios are computed from the nn-UNet segmentations themselves (which would make the metric circular), this must be acknowledged and the evaluation reframed.
2. **Report ε and λ values** in a table or the main text so readers can reproduce the method.
3. **Add error bars or standard deviations** to all quantitative tables, especially given small test-set sizes.
4. **Plot the Monte Carlo denominator** over optimization iterations to validate the constant-denominator assumption, and discuss what happens if it changes.
5. **Extend the ablation** to at least one additional component pair or discuss the limitation explicitly.
