Now I have all the information I need. Let me write the consolidated review.

---

## Summary

This paper addresses the challenging problem of hyper-parameter optimization and model selection for unsupervised anomaly detection (UAD), where no labeled anomalies are available for validation. It proposes three surrogate metrics—RTM, EAG, and NPD—that estimate expected test performance without ground-truth labels. The primary contribution is NPD (Normalized Pseudo Discrepancy), which measures the discrepancy between anomaly scores on a held-out validation subset of the training data and a synthetically generated Gaussian dataset. NPD is integrated with Bayesian optimization to guide hyper-parameter search. Experiments on 38 datasets with four UAD methods (OCSVM, AE, DeepSVDD, DPAD) show that NPD-guided optimization consistently achieves higher mean AUC/F1 than Default, Random, and existing internal metrics (EM/MV, MC, HITS), with statistical significance.

## Strengths

1. **Novel and well-motivated approach.** The idea of using a synthetic Gaussian validation set as a surrogate for unseen test data in UAD model selection is creative. The paper provides clear motivation for why a Gaussian (maximum entropy among same-variance distributions) is a reasonable choice, and the geometric intuition of covering the "rest of the hypersphere" space for potential anomalies is compelling.

2. **Extensive empirical evaluation.** The experiments cover 38 real-world benchmark datasets and four UAD methods spanning shallow (OCSVM) and deep (AE, DeepSVDD, DPAD) architectures. Table 1 shows mean AUC improvements for NPD over the Random baseline (e.g., AUC 0.833 vs. 0.807 for OCSVM, 0.729 vs. 0.676 for AE, 0.832 vs. 0.792 for DPAD), all with p < 0.05. Table 2 further validates NPD in the UOMS (grid search model selection) setting, outperforming consensus-based methods MC and HITS.

3. **Clear problem framing.** The paper cleanly delineates the inductive UAD setting (pure normal training, detect new test anomalies) from the transductive outlier detection setting, and explains why methods that assume anomalies in the training set fail in this regime (Section 2). This contextualizes the contribution relative to existing work.

4. **Demonstrated monotonic correlation.** Figures 5–6 show that higher NPD values consistently correspond to higher AUC and F1 across BO iterations, with reported Spearman rank coefficient of 1, validating its use as a surrogate for Bayesian optimization.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **"Isotropic Gaussian" is a technical misnomer that undermines the geometric interpretation.** The paper generates data from `N(μ_trn, diag(σ²_trn))` and repeatedly calls it "isotropic Gaussian" (abstract, Definition 6, Figure 3 caption, Section 3.3). A diagonal covariance with potentially different entries is *not* isotropic — isotropic requires all diagonal entries to be equal (σ²I). The geometric interpretation that "the outline of χ_gen is a hypersphere" (Section 3.3) is therefore incorrect; the level sets of a diagonal Gaussian with unequal variances are axis-aligned ellipsoids, not spheres. This does not invalidate the method's empirical performance, but it is a factual error and the geometric motivation (Figure 4) as presented is misleading.

2. **The "hyper-parameter-free" claim for NPD is overstated.** The abstract and introduction state NPD is "simple and hyper-parameter-free" and "without additional hyper-parameters." However, NPD requires choosing the validation split size M (and M samples for the generated set). The specific value of M used in the experiments is never reported, and no ablation or sensitivity analysis is provided. While M might be robust across reasonable choices, the paper does not demonstrate this, making the "hyper-parameter-free" characterization inaccurate.

3. **Missing ablation on the split proportion M.** Related to the above, the paper provides no analysis of how the validation split size M/N affects NPD's effectiveness. This is a critical design choice — if the split is too small, the validation set may not be representative; if too large, the model training is under-powered. Without such analysis, the robustness of the method is uncharacterized.

4. **Table 1 reports means and p-values but does not show per-dataset variability.** The paper states experiments use 5 random splits and "report the results with mean and standard deviation," but Table 1's caption and content present only mean AUC/F1 across 38 datasets and p-values. Without standard deviations (across splits or across datasets), the reader cannot assess whether the observed improvements are consistent or driven by a few favorable datasets. The p-values from a paired t-test partially address this, but error bars or per-dataset scatter plots would substantially strengthen confidence.

5. **Theoretical analysis provides motivation but not rigorous guarantees for the surrogate claim.** Theorems 1–3 present interesting structural properties of NPD (entropy comparison, translation/scale invariance, KL-divergence bounds), but none directly establish that NPD is a monotonic surrogate for *unseen test AUC/F1* (Equation 3). Theorem 2's bound assumes a perfect partition of validation/generated points into normal and anomalous, which is unavailable in practice (validation points are unlabeled). Theorem 3's constants make the bound uninformative. The theoretical section is honest about these limitations, but the paper's claim of "theoretical guarantee" (Section 1, contributions) overstates what is actually provided. Reframing these as heuristics or structural motivations would be more accurate.

### Trivial

- Figure 5 shows BO iteration trends but does not name the specific datasets plotted, making it impossible to verify the claim qualitatively.
- No runtime analysis is provided; the paper claims "scalable to larger datasets" (Section 4) without evidence.

## Nice-to-Haves

- A per-dataset scatter plot or bar chart comparing NPD-guided AUC vs. Random/baseline AUC across all 38 datasets, to show consistency of improvement.
- An ablation study varying M/N (e.g., 20%, 40%, 60%) to demonstrate robustness.
- A brief discussion of computational cost (e.g., number of BO iterations × model training time) for the deep methods.
- Correction to the geometric interpretation: "ellipsoid" instead of "hypersphere," or clarification that the method standardizes features first (making the covariance identity) if that is the actual practice.

## Removed Points

The following criticisms from the reviewers were removed or downgraded with justification:

- **"Baseline comparisons are weak and incomplete"** — The reviewer suggested adding method-specific baselines (reconstruction error for AE, hypersphere radius for DeepSVDD). These are model-specific heuristics that would not generalize across all four UAD methods tested (OCSVM, AE, DeepSVDD, DPAD). The paper's baselines (MC, HITS, EM/MV, Default, Random, Max) are defensible choices from the UAD model selection literature. The paper also acknowledges that MC/HITS are consensus-based and not designed for iterative BO, yet still includes them for completeness.

- **"Inconsistency between the UAD definition and experimental setup"** — Definition 1 includes a scenario with anomalies in training (N₀ ≫ N₁), but Remark 3.1 explicitly notes N₁ may be 0. The paper clearly states it focuses on the inductive setting (Section 2: "train a model on a 'normal' dataset to detect the newly incoming anomalies"). Theorem 2's partition into normal/anomalous subsets is a theoretical construct for analysis, not a practical requirement. The paper is consistent.

- **"MC and HITS are not natural competitors"** — The paper explicitly acknowledges this limitation (Section 4: "The consensus-based metrics are not adaptable for BO because they are designed to select the most reliable model from a set of models"). They are included as existing baselines from the literature and are evaluated in the UOMS setting (Table 2) where they are appropriate. No misrepresentation.

- **The "5 repetitions is low" concern** — For hyper-parameter optimization across 38 datasets with multiple deep models, 5 splits is a standard practice consistent with prior work (Shenkar & Wolf, 2022, which the paper cites). This is not unusually low.

- **Criticisms about missing appendix content** — The parser strips appendix sections from all papers; these exist in the original submission.

## Novel Insights

The cross-review analysis reveals a pattern worth noting: the paper's theoretical apparatus (Theorems 1–3) and its empirical evaluation pull in somewhat different directions. The theory analyzes the *structure* of NPD (entropy, invariance, KL bounds) without directly addressing the core operational question of whether NPD ranks models in the same order as test AUC. The empirical evaluation (Figure 6, Spearman ρ = 1) is actually the strongest evidence for this claim, but it is presented as a supporting figure rather than a central result. The paper would be stronger if it acknowledged this asymmetry and framed the theory as intuition-building rather than guarantee-providing. Conversely, the empirical demonstration of strict monotonicity (ρ = 1) across BO iterations is quite striking and deserves more prominence.

## Suggestions

1. **Correct the "isotropic" terminology.** Replace "isotropic Gaussian" with "diagonal Gaussian" or "axis-aligned Gaussian" throughout. Adjust the geometric interpretation (Figure 4) from "hypersphere" to "ellipsoid" unless the data is standardized to have unit variance in all dimensions. If standardization *is* performed (Section 4 mentions standardizing with training set mean and std), clarify that the generated Gaussian is then *approximately* isotropic and the geometric interpretation holds after standardization.

2. **Report the value of M used in all experiments** and add a brief sensitivity study (e.g., supplement) showing that NPD's ranking of models is stable across M ∈ {20%, 40%, 60%} of the training set. Alternatively, adopt a fixed rule (e.g., M = min(500, 0.2N)) and state it explicitly.

3. **Add standard deviations or confidence intervals to Table 1**, or provide a per-dataset comparison table/figure in the supplementary material. This would allow readers to assess consistency.

4. **Tone down the "theoretical guarantee" claim.** Rephrase as "theoretical motivation" or "structural analysis," since the theorems do not directly prove surrogate monotonicity with respect to test AUC. Theorem 3 in particular adds little and could be moved to an appendix or removed.

5. **Add a runtime/compute-cost table or note**, even brief, for the full AutoUAD pipeline (BO iterations × model training time) to support the scalability claim.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>