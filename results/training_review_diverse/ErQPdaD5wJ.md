Now I have all the information needed to produce the consolidated review. Let me carefully verify each claim against the paper.

---

## Summary

This paper tackles hyperparameter optimization and model selection for unsupervised anomaly detection (UAD), where labeled validation data is unavailable. It proposes three surrogate metrics—RTM, EAG, and NPD—to approximate expected test performance without labeled anomalies. NPD, the main contribution, measures the discrepancy between anomaly scores on a held-out validation partition of the training data versus scores on data generated from an isotropic Gaussian with matched first/second moments. The metrics are integrated with Bayesian optimization (TPE) and evaluated on 38 benchmark datasets across four UAD methods (OCSVM, AE, DeepSVDD, DPAD). NPD consistently outperforms existing heuristics, including consensus-based methods (MC, HITS) and EM/MV, on both BO-based HPO and unsupervised model selection tasks.

## Strengths

1. **Simple, well-motivated metric (NPD) with practical appeal.** The idea of comparing anomaly scores on real vs. Gaussian-generated data is intuitive and requires no labeled anomalies or prior knowledge of the anomaly ratio. The metric is hyperparameter-free by design (modulo the validation split, see Weaknesses), translation- and scale-invariant (Theorem 2b), and does not overfit because it is computed on held-out data independent of training. This contrasts favorably with prior work that requires meta-learning across labeled historical datasets or assumes knowledge of the anomaly ratio.

2. **Strong empirical results across a large benchmark.** In Table 1, NPD-guided BO achieves the highest mean AUC and F1 among all methods for OCSVM (AUC 0.832), AE (AUC 0.779), and DPAD (AUC 0.697). NPD consistently outperforms the Random baseline (expected grid search value) with statistically significant p-values across 38 datasets. The UOMS study (Table 2) further shows NPD and RTM outperform consensus-based selectors (MC, HITS) on a model pool of up to 2,667 configurations.

3. **Clear problem formulation and thorough motivation.** Definitions 1 and 2 formalize the UAD and AutoUAD problems with precision. Figure 1 vividly demonstrates the sensitivity of UAD methods to hyperparameters and the diversity of performance landscapes across datasets, providing concrete motivation for automated tuning.

4. **NPD avoids overfitting issues of internal metrics.** The paper shows (Figure 6) that NPD yields a Spearman rank coefficient of 1.0 with test AUC across configurations, while RTM and EAG exhibit non-monotonic relationships on some methods (e.g., DPAD). This is a genuine advantage of the semi-internal design.

## Weaknesses

### Fatal
None.

### Major

1. **Missing critical experimental details that compromise reproducibility.** Two parameters central to the experimental design are not reported:
   - **M (validation split size) in NPD (Definition 6):** The paper never states what fraction of training data is held out as $\mathcal{X}_{\text{val}}$  (size $M$) versus used for training (size $N-M$). Since $M$ determines both the validation quality and the size of the generated set $\mathcal{X}_{\text{gen}}$, this is a free design parameter of NPD. The paper claims NPD is "hyper-parameter-free," which is strictly true only if $M$ is treated as a fixed preset rather than a tunable choice, but the value is never disclosed.
   - **Number of BO iterations:** The paper uses Bayesian optimization with TPE but never states how many function evaluations are performed per dataset per method. Without this, readers cannot assess whether the search budget was sufficient, whether comparisons across methods on a given budget were fair, or whether the results are reproducible.

   These omissions go beyond presentation polish—they prevent independent verification and limit the paper's scientific value. *Recommendation: specify $M$ (or the split ratio $M/N$), report the number of BO iterations, and ideally show robustness to the choice of $M$.*

2. **Lack of ablation studies for NPD's design choices.** The paper does not ablate:
   - Varying $M$ (e.g., 10%, 20%, 50% of training data)
   - Replacing the isotropic Gaussian with a uniform distribution, a shuffled version of the training data, or another reference distribution
   
   An ablation would substantially strengthen the claim that the specific choices in NPD—the Gaussian, the particular split—are important. Without it, one cannot rule out that other reasonable choices would work as well or better.

### Minor

3. **Surrogate validation is indirect; direct correlation analysis would be stronger.** The paper validates that RTM, EAG, and NPD are good surrogates by showing that BO guided by these metrics finds hyperparameters that outperform Random and baselines. This is a valid but indirect approach. A direct analysis—computing Spearman or Kendall correlation between each metric and test AUC across all hyperparameter configurations for each dataset and method—would more cleanly establish the surrogate claim. Figure 5 shows trends for "different datasets" (plural) and Figure 6 is illustrative, but neither constitutes a systematic correlation study across all 38 datasets. The results are not inconsistent with the surrogate claim, but the evidence could be more direct.

4. **Theoretical results (Theorems 2 and 3) have limited practical utility.** Theorem 2 bounds NPD in terms of the unknown partition of $\mathcal{X}_{\text{val}}$  and $\mathcal{X}_{\text{gen}}$ into normal and anomalous points—quantities never observed in practice. Theorem 3 assumes a Gaussian mixture approximation with bounds on eigenvalues, component norms, and approximation error $\varepsilon$, which are unlikely to hold on real-world datasets. While the translation/scale-invariance property (Theorem 2b) and the entropy result (Theorem 1) are useful, the more complex bounds offer no actionable guidance. They give an appearance of theoretical rigor without providing guarantees that inform practice.

5. **EM/MV baseline usage could be clearer.** The paper states EM/MV is compared "with BO" in Table 1, but does not fully describe how EM/MV is computed and used as the acquisition objective. For reproducibility, the paper should specify the exact implementation (e.g., the Goix 2016 formulation used, hyperparameters of the metric itself). The "Random" baseline is, however, clearly defined as "the expected value of the grid search" (Table 1 caption), so this specific concern raised by the reviewer is unfounded.

6. **Notable that NPD does not outperform Random on DeepSVDD.** In Table 1, NPD's AUC (0.737) is close to Random (0.730) on DeepSVDD, with the p-value indicating marginal or no statistical significance. The paper does not discuss this negative result, which would provide useful context about when NPD may fail.

### Trivial

- Figure 6's dataset is not identified in the text (line 205 says "taking Figure 6 as an example").
- The double p-value notation in Table 1 ($p$ and $p^*$) is explained but could be clearer.

## Nice-to-Haves

- A direct correlation analysis (Spearman rank) between each metric and test AUC across all configurations, datasets, and methods.
- An ablation of NPD varying the split ratio $M$ and the reference distribution.
- A brief discussion of the DeepSVDD case where NPD does not significantly outperform Random.

## Removed Points

These points are factually wrong or reflect misreading of the paper. They are noted here for completeness but should not factor into the evaluation:

- **"Figure 5 shows that for one dataset (unlabeled)."** Removed because the Figure 5 caption explicitly says "on different datasets" (plural). The reviewer misread the figure.
- **"Random baseline could mean the expected performance of a single random draw."** Removed because the paper clearly states "Random is the expected value of the grid search" (Table 1 caption), which is standard terminology meaning the average over all grid configurations.
- **"The paper says 'the same number of iterations for all methods'" (from Strength Finder).** This claim from the Strength Finder is not verifiable in the paper text and is removed from consideration.
- **"Confusion over whether EM/MV is used with the same BO procedure."** The paper states at line 203: "We compare the performance using BO to search for the best model of RTM, EAG, and NPD with Max, Default, Random, and EM/MV in Table 1." While the implementation details of EM/MV could be clearer, the paper does state it is used with BO.

## Novel Insights

The harsh reviewer correctly identifies that the UOMS study (Table 2)—where NPD selects from a known pool of models—is cleaner evidence than the BO experiments. The reviewer's suggestion to add a direct correlation analysis across all configurations and datasets is the single most impactful improvement the authors could make. The reviewer's observation about the theorems' limited practical utility is also fair, though it does not invalidate the paper: many ML papers include theory that is more about establishing basic properties (here, scale/translation invariance and the entropy result in Theorem 1) than about providing actionable bounds.

The Strength Finder overstates the theoretical contribution by treating Theorems 2-3 as "theoretically grounded" in a practical sense, but understates the paper's genuine strength: NPD's simplicity and strong empirical performance across a diverse 38-dataset benchmark are the real contributions.

## Suggestions

1. **Specify all missing experimental parameters:** report the value of $M$ (or the ratio $M/N$) used for NPD, and the number of BO iterations per dataset/method.
2. **Add a direct correlation analysis:** compute Spearman rank correlation between each metric (RTM, EAG, NPD, EM/MV) and test AUC/F1 across the full hyperparameter grid for each dataset and method. Report the distribution (mean, variance, fraction of datasets with significant positive correlation).
3. **Add ablations:** vary $M$ (e.g., 10%, 20%, 50%), compare Gaussian vs. uniform vs. shuffled training data as the reference distribution for $\mathcal{X}_{\text{gen}}$.
4. **Discuss the DeepSVDD negative result** where NPD does not significantly outperform Random.
5. **Consider whether Theorems 2 and 3 add enough value to justify their complexity.** The translation/scale-invariance and entropy results are useful; the more elaborate bounds may mislead readers about the strength of the theoretical foundation.

## Score and Decision

The paper tackles an important and underexplored problem with a simple, intuitive metric (NPD) and provides solid (though imperfect) empirical validation across a large benchmark. The core weakness is the omission of key experimental details (M, BO iterations) and the lack of ablations and direct correlation analysis, which prevent the paper from being a fully convincing contribution. However, the positive results are consistent and the core idea is sound. The paper would be significantly strengthened by the suggested additions, and the missing details are fixable in revision.

**Overall assessment:** The paper's contribution is meaningful—a practical, hyperparameter-free surrogate metric for UAD that works well in practice—but the experimental reporting gaps and missing validations lower confidence in the current form.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>