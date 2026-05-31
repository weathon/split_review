## Summary

The paper proposes FedTransTEE, a federated learning framework for Individual Treatment Effect (ITE) estimation that handles heterogeneous covariates, treatments, and outcome spaces across multiple sites. It uses a transformer-based covariate encoder, a treatment encoder (optionally incorporating textual descriptions), and a cross-attention module to produce patient-treatment representations; each site retains a local predictor for personalization. The authors claim this is the first work to address federated ITE estimation under such full heterogeneity and demonstrate results on semi-synthetic benchmarks (IHDP, ACIC-16, Twins) and two real-world clinical trial collections (ICH, CPAD), including zero-shot predictions and attention-based interpretability.

## Strengths

- **Important practical problem.** The setting—federated causal inference with non-identical covariates *and* treatments across sites—is realistic and underexplored. The paper explicitly acknowledges data silos and privacy constraints that arise in healthcare.
- **Architecture tailored to heterogeneity.** The covariate encoder that processes each feature as a (name, value) token is a sensible way to handle varying feature sets across sites, and the use of cross-attention to model treatment–covariate interactions is appropriate.
- **Interpretability attempt.** Analyzing attention weights to link model focus to clinically meaningful variables (e.g., GCS, NIHSS) is a nice addition that goes beyond pure performance reporting.

## Weaknesses

### Fatal

- **Baseline performances on semi-synthetic datasets are implausible, invalidating the claimed improvements.** On the IHDP dataset, the centralized baselines (S-Learner, T-Learner, TARNet, FlexTENet) report ATE errors of 3.6–3.9, which is an order of magnitude larger than standard results in the literature (typically 0.2–0.5). Similarly, on ACIC-16, the ATE errors for these baselines (~3.5) are far above the 0.3–1.0 range commonly reported. These unrealistic numbers suggest a bug in the evaluation code, a mismatched metric definition, or a flawed experimental setup (e.g., different outcome scaling, improper data splits). If the baselines are not correctly implemented, the performance gains claimed by FedTransTEE are unsupported.

### Major

- **Insufficient comparison with relevant methods that can handle heterogeneous features.** The paper compares only with FedCI and iFedTree (both assume identical covariate spaces) and with standard ITE methods trained centrally or locally. No comparison is made with personalized federated learning approaches that can handle heterogeneous feature spaces—for example, using a shared feature extractor with local heads (e.g., FedPer, LG-FedAvg, pFedMe), or with tabular-transformer methods that already handle varying feature sets (e.g., TabTransformer, FT-Transformer) in a non-federated or federated setting. This makes it unclear whether the architectural choices are necessary or if simpler alternatives would perform as well.
- **Zero-shot evaluation is narrow and lacks baselines.** The experiment with two ICH treatments demonstrates feasibility, but no comparison is provided against alternative ways to leverage treatment descriptions (e.g., using the same treatment encoder within a non-federated ITE model). Without baselines, it is difficult to assess whether the zero-shot capability is an intrinsic advantage of FedTransTEE or simply a property of using pre-trained treatment embeddings.
- **Mixed results on the CPAD dataset are glossed over.** On CPAD, FedTransTEE achieves the best RMSE-F but the worst ATT error (10.2 vs. 8.1 for FlexTENet). The paper does not discuss this trade-off or explain why ATT is worse, which weakens the claim of “superior performance.”
- **Interpretability claims are qualitative and not validated against alternative methods.** The attention analysis shows that certain heads attend to clinically plausible variables, but this is a post-hoc observation without quantitative evaluation (e.g., feature importance correlation, or comparison with SHAP/LIME). The phrase “validated by domain expertise” is vague and does not constitute a rigorous claim.

### Minor

- **The problem formulation conflates within-institution silos and cross-institution FL.** The paper describes both scenarios, but the experimental setup only evaluates the FL scenario. The claim that the same framework works for internal silos is not empirically tested.
- **The federated aggregation strategy is standard weighted averaging of shared parameters.** The paper does not discuss or compare any advanced FL aggregation (e.g., FedProx, adaptive weighting) that might improve convergence under heterogeneous data.

### Trivial

- The paper uses 5 repetitions, but some standard deviations are suspiciously small (e.g., 0.01 on PEHE for FedTransTEE on IHDP). The authors should confirm that these reflect genuine low variance and not a mistake in the reporting.

## Nice-to-Haves

- It would be valuable to include an ablation study that isolates the contribution of the cross-attention module, the treatment encoder, and the personalized predictor. For example, does a simple concatenation of covariate and treatment embeddings work as well?
- The zero-shot experiment could be strengthened by including multiple held-out treatments and by comparing with a simple baseline (e.g., replacing the treatment encoder with random embeddings or with a one-hot encoding of a “new treatment” token).

## Novel Insights

None beyond the paper’s own contributions. The combination of transformer-based heterogeneous feature encoding with personalized federated learning for ITE is a plausible recipe, but it does not reveal a fundamentally new principle.

## Suggestions

- **Fix baseline evaluation.** Re-run centralized baselines with proper hyperparameter tuning and verify that the metric computation (especially ATE error) matches the standard definition. Report the results honestly, even if FedTransTEE no longer outperforms.
- **Add comparisons with heterogeneous FL methods.** At minimum, compare against a baseline that uses a shared (fixed-size) representation learned via a common feature mapping (e.g., one-hot concatenation of all possible features) and a local predictor. This will help isolate the benefit of the token-based encoder.
- **Provide a more thorough zero-shot evaluation.** Include more held-out treatments, report results on multiple datasets, and compare against a model that uses treatment descriptions but is trained in a non-federated local setup.
- **Discuss the trade-off on CPAD ATT error.** Explain why ATT degrades and whether this is a limitation of the method.

## Score and Decision

The paper addresses a relevant and timely problem, but the experimental validation is critically flawed—the baseline performances on standard semi-synthetic datasets are not credible, which undermines the central claim of superior performance. Without a reliable comparison, the contribution of the framework cannot be properly assessed. The paper also lacks comparisons with relevant personalized FL methods and provides only a narrow evaluation of the zero-shot capability. Therefore, I recommend rejection.

MY FINAL SCORE: 3.0</score>
MY FINAL DECISION: Reject</decision>