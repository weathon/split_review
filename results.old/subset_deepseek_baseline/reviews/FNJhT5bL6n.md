## Summary

The paper proposes a “morphing” framework for time series forecasting with exogenous variables. It argues that transformer models struggle to use exogenous data effectively due to permutation invariance. The solution preprocesses each exogenous series by weighting its values with a rolling statistical similarity (e.g., correlation, mutual information) to the target series, then feeds the morphed series to the model. The authors conduct an ablation study across seven datasets, five transformer models, five saliency metrics, and five window sizes, reporting that 73% of experiments show improvement and that Crossformer benefits particularly strongly.

## Strengths

- **Clear problem motivation:** The paper identifies a real limitation of channel-dependent transformer models — their inability to exploit temporally varying exogenous relevance — and proposes a simple preprocessing remedy. The argument builds on a reasonable hypothesis that statistical saliency detection can be decoupled from modeling.
- **Extensive ablation design:** The experiment covers seven datasets (including ETT, weather, traffic, ECL), five Transformer backbones (Autoformer, Crossformer, PatchTST, TimeXer, iTransformer), five statistical saliency methods, and five window sizes. This breadth provides a thorough empirical sketch of when morphing helps.
- **Illustrative toy example:** Figure 2 provides an intuitive demonstration of the morphing concept and shows a 6% MSE improvement on a synthetic case, which helps convey the core idea.

## Weaknesses

### Fatal

- **No proper baseline against raw exogenous inputs.** The “improvement” percentages in Table 1 are explicitly defined as “the gain compared to a forecast without exogenous information” (Section 4.1). This means the baseline is a univariate model that receives only the target history. Comparing morphed-exogenous + transformer against univariate transformer does **not** test whether morphing improves over using the *same* exogenous data without morphing. The observed gains could be entirely due to the presence of any exogenous information, not to the morphing operation itself. Without a direct comparison (same model, raw exogenous vs. morphed exogenous), the paper’s central claim is unsupported.

### Major

- **Over-optimistic reporting of best-case results.** The authors report the best-performing configuration (saliency method + window size) per dataset-model combination, selected after seeing the test results. This cherry-picking inflates the apparent benefit of morphing. The median effect is stated as “≈0%” (Section 5), which suggests that most configurations do not help — a fact that is buried. A proper evaluation would use a validation set to select hyperparameters, or report distributional statistics (median, quartiles) over configurations.
- **Unclear and potentially unfair comparison in Table 1.** The caption says “compared to a forecast without exogenous information”, yet the table includes entries like PatchTST on ECL with 0.0% improvement. If the baseline truly omits all exogenous channels, then the transformer is trained differently (fewer input dimensions), making the comparison inequitable. The experimental setup (Section 4) describes training “multivariate models with univariate output” – it is ambiguous whether the baseline removes exogenous channels or retains them but disables morphing. Clarity is critically needed.

### Minor

- **Limited novelty.** The core idea — scaling exogenous inputs by a rolling statistical similarity — is simple and appears to be a form of adaptive feature weighting that has been explored in other contexts (e.g., attention mechanisms, instance weighting). The paper does not draw clear connections to or comparisons with existing adaptive weighting schemes.
- **Missing details on evaluation protocol.** The paper states hyperparameters are taken from original papers and will be released “after acceptance.” For reproducibility, these should be fully described now. The Appendix (removed in the extract) is referenced for experiment setup, saliency method definitions, and the CATS framework comparison — all essential for understanding the work.

### Trivial

- Several references are anonymized (e.g., “Auth1 et al.”) which is appropriate for double-blind review but makes it impossible to verify related claims.
- Table 1 contains missing entries (e.g., Crossformer on ECL and TrafficL) due to computational limits, which weakens the completeness of the ablation.

## Nice-to-Haves

- Report results for **all** hyperparameter combinations alongside the best, e.g., via a boxplot of improvements over configurations. This would give a realistic picture of the method’s reliability.
- Provide ablation that separates the effect of adding any exogenous data from the effect of morphing, by including a “raw exogenous” column in Table 1.

## Novel Insights

None beyond the paper’s own contributions.

## Suggestions

- **Fix the baseline:** Compare each morphed experiment against the *same model using the same exogenous channels without morphing*. Report the distribution of improvements across configurations, not just the best.
- **Validate with a held-out selection set:** Choose the best saliency method and window size for each dataset-model pair using a validation sample, then evaluate only the selected configuration on the test set.

## Score and Decision

**Score: 3**  
**Decision: Reject**

MY FINAL SCORE: <score>3</score>  
MY FINAL DECISION: <decision>Reject</decision>