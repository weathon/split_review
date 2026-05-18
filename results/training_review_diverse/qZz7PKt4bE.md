Now I have all the information I need. Let me write the consolidated final review.

## Summary

This paper proposes an autotuning framework that combines Low-Rank Adaptation (LoRA) with Limited Discrepancy Search (LDS) to automatically find good hyperparameter configurations for fine-tuning pre-trained time series transformers (specifically Chronos T5 Mini) on target domain datasets. The approach uses Ray Tune for parallelization, evaluates 10 trials per dataset with two discrepancy settings, and is demonstrated on 10 out-of-domain benchmark datasets from the Monash repository. The main findings are that autotuning achieves a 5.21% average MASE improvement over zero-shot, with a notable 20.59% improvement on the exchange-rate dataset, and that the autotuned Mini model (20M params) can match or exceed larger zero-shot models (up to 710M params) on several datasets.

## Strengths

- **First systematic application of LoRA-based autotuning to time series transformers.** The paper addresses a genuinely practical gap: pre-trained time series foundation models exist, but their hyperparameter sensitivity for fine-tuning is underexplored. The combination of LoRA (parameter-efficient fine-tuning) with an automated search strategy for time series is novel, and the work opens a useful direction for the community.

- **Demonstration that a small autotuned model can outperform much larger zero-shot models.** Table 4 and Figure 5 show that the autotuned Chronos Mini (20M) beats zero-shot Small (46M) on 6/10 datasets, zero-shot Base (200M) on 4/10, and zero-shot Large (710M) on 3/10. This finding has practical importance: it suggests that efficient fine-tuning can substitute for scaling up model size, reducing both training and inference cost.

- **Practical resource footprint.** The entire pipeline runs 10 trials per dataset on a single MacBook Pro M3 Max, making the approach accessible to researchers without large GPU clusters. The choice of LDS as a search strategy is motivated by keeping the trial budget small, which is a realistic constraint for many practitioners.

- **Diverse, out-of-domain evaluation setup.** The 10 datasets span energy, transport, retail, finance, weather, and web traffic domains, all held out from Chronos pre-training. This provides reasonably strong evidence that the approach generalizes across different forecasting problems rather than fitting to a narrow distribution.

## Weaknesses

### Major

- **No comparison to alternative search strategies.** The paper's second stated contribution is "the adoption of LDS for exploring the LoRA hyper-parameter search space in autotuning to minimize computational overhead," yet LDS is never compared to any baseline search strategy — not random search, grid search, Bayesian optimization, or even simple greedy search. The only variable within LDS that is varied is `max_discrepancy` (4 vs. 8). Because the paper does not isolate the contribution of LDS, it is impossible to tell whether the observed improvements come from the search strategy itself or simply from trying 10 different LoRA configurations (which random search could also do). This is a structural gap: the paper's central methodological claim about LDS is entirely unevaluated. Adding a random-search or grid-search baseline with the same budget would directly address this.

- **No measures of variability or statistical significance.** All MASE scores in Tables 3 and 4 are reported as single values averaged over 5 runs, with no standard deviations, confidence intervals, or individual trial outcomes. Many reported differences are very small (e.g., 0.063 vs. 0.062 for ERCOT Load, 0.030 vs. 0.029 for M5) and could easily fall within noise. Without error bars, the reader cannot assess which improvements are meaningful. This directly affects confidence in the headline 5.21% average improvement claim.

- **LDS application to the hyperparameter space is underspecified, affecting reproducibility.** The search space (Table 2) includes both categorical variables (`apply_to_attention`, `apply_to_mlp`) and numerical/ordinal variables (`rank` 4–32, `alpha` 8–32, `dropout` 0.0–0.5, `learning_rate`, `warmup_ratio`). LDS was originally designed for discrete constraint satisfaction problems. The paper never explains how discrepancies are defined for numerical variables — whether they are discretized (and at what granularity), how distance is measured for continuous values, or how the initial configuration is selected. Algorithm 1 is referenced but its pseudocode appears only in an extracted image that provides no textual detail. This makes the method impossible to reproduce without guessing these critical design choices.

### Minor

- **Only one model size (Chronos T5 Mini) is autotuned.** The paper evaluates zero-shot performance of larger models but never runs the autotune pipeline on Chronos Small (46M), Base (200M), or any other size. While the paper justifies this as a resource choice, the claim that "our approach can be easily extended to other time series foundation models" remains unvalidated. Showing results for at least one additional model size (e.g., Small) would significantly strengthen the claim of generality.

- **Full fine-tuning baseline details are sparse.** The full fine-tuning is described only by a citation to Ansari et al. (2024), with no information about the optimization protocol used (learning rate schedule, number of epochs, early stopping, compute budget allocated). If the full fine-tuning baseline was not itself tuned or given a reasonable budget, the comparison may be unfair. Since the paper's autotune method is compared against full fine-tuning, baseline fidelity matters.

- **Computational efficiency claims lack quantitative support.** The paper motivates the approach by "minimizing computational overhead" but reports no wall-clock time, GPU-hours, or number of trainable parameters for the autotune pipeline vs. full fine-tuning. Providing these numbers — even approximate ones — would ground the efficiency claims.

- **Overclaiming novelty (minor).** The abstract's claim that this is "the first paper to explore the potential of autotuning time series transformer models" is broader than what the paper actually demonstrates (autotuning one specific model with one specific PEFT method and one specific search strategy). There is substantial prior work on HPO for time series models cited in the paper's own AutoML section. The contribution is more accurately described as the first application of LoRA + LDS autotuning to time series transformers, which is already a worthwhile contribution without the stronger framing.

### Trivial

- Figure 4 (relative performance plot) uses bars that extend beyond the reference line for worse methods. A critical-difference diagram or radar plot might be more conventional, but this is a presentation preference, not a substantive flaw.
- The paper uses "mean absolute squared error" as the definition of MASE in the implementation section, which appears to be a minor terminological inconsistency — MASE is the mean absolute scaled error, not mean absolute squared error.

## Nice-to-Haves

- An ablation isolating the contribution of LDS vs. LoRA: full fine-tuning vs. LoRA with fixed (default) hyperparameters vs. LoRA + random search vs. LoRA + LDS. This would separate the benefit of PEFT from the benefit of tuning PEFT hyperparameters.
- Analysis of which hyperparameter values were selected across datasets (e.g., do out-of-domain datasets favor different rank/alpha settings than in-domain ones?). This could provide practical insights for practitioners.
- A note on whether MASE was computed robustly for any edge cases where in-sample MAE approaches zero, as MASE can be undefined in such settings.

## Removed Points

The following reviewer criticisms were evaluated against the paper and removed:

- **"All datasets are univariate; should include multivariate."** Chronos is pre-trained for univariate forecasting. Demanding multivariate evaluation would require a fundamentally different experimental design and is clearly scoped as future work by the authors. This is scope creep.
- **"Figure 4 is confusing; use radar/critical-difference diagram instead."** This is a presentation preference, not a weakness.
- **"Missing related work."** Insufficient external basis to verify; also the paper does cite relevant AutoML and HPO literature.
- **Several formatting/presentation nitpicks** that are parser artifacts, not author errors.

## Novel Insights

Beyond the paper's own contributions, the most interesting synthesis from the reviews is that the paper's value may lie less in the specific search strategy (LDS) and more in the overall demonstration that systematic LoRA hyperparameter tuning for time series transformers yields significant practical gains. The finding that a 20M-parameter autotuned model beats a 710M-parameter zero-shot model on some datasets is the paper's strongest practical result, and it raises a broader question: how much of the benefit attributed to "larger foundation models" could instead be captured by smaller, well-tuned PEFT models? This is a direction worth exploring further and is the paper's most impactful insight, regardless of whether LDS is the optimal search strategy or merely a sufficient one.

## Suggestions

1. **Add a search-strategy baseline.** Compare LDS against random search with the same 10-trial budget. If LDS matches or exceeds random search, the LDS claim is supported. If not, reframe the contribution as "autotuning with LoRA works" and treat LDS as a design choice rather than a core contribution.
2. **Report standard deviations or empirical 95% intervals** for every MASE score. Even a simple "mean ± std" over 5 runs would dramatically increase confidence in the results.
3. **Clarify how LDS handles numerical hyperparameters.** Specify the discretization scheme (if any), the initial configuration selection method, and how discrepancies are computed for each hyperparameter type.
4. **Run autotune on at least one additional Chronos model size** (e.g., Small: 46M) to show the method is not specific to Mini.
5. **Report wall-clock time or parameter counts** for the autotune pipeline vs. full fine-tuning to quantitatively support the efficiency claim.
6. **Tone down the novelty claim** from "first paper to explore autotuning time series transformer models" to something more precise (e.g., "first to combine LoRA with LDS for autotuning time series transformers").

## Score and Decision

The paper addresses a genuine practical problem and produces interesting results, particularly the finding that a well-tuned small model can match larger zero-shot models. However, the evaluation has two structural gaps — the absence of any search-strategy baseline and the lack of variability measures — that prevent the reader from trusting the central claims about LDS and the precise magnitude of improvement. These are addressable with additional experiments. The paper would be strengthened considerably by a major revision incorporating the suggestions above.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>