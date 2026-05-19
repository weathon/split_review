- Decision: Reject
- Avg Score: 3.00
- Scores: 5, 3, 1
Here is the consolidated review.

## Summary

This paper proposes an autotuning framework for time-series transformers that combines Low-Rank Adaptation (LoRA) with Limited Discrepancy Search (LDS) to automate the selection of LoRA hyperparameters for domain-specific fine-tuning. Experiments on 10 Monash benchmark datasets using Chronos T5 Mini show that the autotuned model achieves an average 5.21% MASE improvement over zero-shot baselines, and a small autotuned model can match or exceed larger zero-shot models on several datasets.

## Strengths

- **Novel integration of LoRA with automated search for time-series transformer fine-tuning.** The paper is among the first to apply LoRA-based PEFT specifically to time-series transformers (Chronos) and to couple it with a search procedure for hyperparameter selection. The architecture diagram (Figure 1) and the defined search space (Table 2) make the approach concrete.

- **Smaller autotuned models outperform larger zero-shot models.** Table 4 and Figure 5 show that the autotuned Chronos Mini (20M parameters) beats the zero-shot Small model (46M) on 6/10 datasets and the zero-shot Large model (710M) on 3/10 datasets. This is a practically meaningful result: a tuned small model can reduce compute requirements while achieving competitive accuracy.

- **Evaluation across diverse out-of-domain datasets.** The 10 datasets span energy, transport, retail, weather, and finance (Table 1), and the paper distinguishes between domains seen vs. unseen during Chronos pretraining. The strongest gains (e.g., 20.59% on exchange rate) occur on genuinely out-of-domain data, which is where the approach's value proposition is clearest.

## Weaknesses

### Fatal

None.

### Major

- **Full fine-tuning baseline is underspecified, undermining the comparison.** The paper states "we also perform full fine-tuning of the Chronos mini model described in Ansari et al. (2024)" but provides no details about the fine-tuning protocol: learning rate, number of epochs, optimizer, learning rate schedule, warmup, or early stopping. Without knowing whether the full fine-tuning hyperparameters were themselves tuned (or at minimum followed the recommended procedure from the original Chronos paper), the claim that autotune "outperforms full fine-tuning specifically for out-of-domain datasets" (Section 6) rests on an uncontrolled comparison. A properly tuned full fine-tuning baseline could change the results substantially.

- **The contribution of LDS over simpler search strategies is not validated.** The paper lists "the adoption of LDS for exploring the LoRA hyper-parameter search space in autotuning to minimize computational overhead" as a key contribution, yet never compares LDS to any alternative — not random search, grid search, or Bayesian optimization. With only 10 trials across an 8-hyperparameter search space, the distinction between LDS and random sampling is not obvious, and no evidence is provided that LDS finds better configurations per trial. Without this ablation, the LDS component is decorative rather than demonstrated.

- **LDS methodology is critically underspecified for reproducibility.** The paper defines LDS only conceptually ("depth-first search that iteratively increases the number of discrepancies," where a discrepancy is the number of variables differing from an initial configuration). However, the initial configuration itself is never specified. The paper does not define how the discrepancy metric is computed over the mixed categorical/numerical hyperparameter space in Table 2 (e.g., how is "target modules" — a categorical with 10+ values — handled under discrepancy counting?). Tie-breaking among configurations with identical discrepancy is not discussed, and the procedure for generating the next candidate given a discrepancy budget is not described. Algorithm 1 is referenced but its content appears in a figure that cannot be extracted. These gaps make the method irreproducible as presented.

- **No variance reporting for key results.** Table 3 reports MASE "averaged across 5 runs" but no standard deviations or confidence intervals are provided anywhere. This is especially concerning because: (a) the claimed improvements are modest (5.21% average, 4.76% for out-of-domain), (b) the protocol reports the *best* of 10 trials per dataset, which introduces selection bias and inflates the reported performance relative to what a practitioner would expect in a single run, and (c) the "5 runs" are not clearly defined — does each run repeat the entire 10-trial search, or are they 5 evaluations of the same best configuration? Without variance, the reader cannot assess whether the differences are statistically reliable.

### Minor

- **No analysis of the two maximum discrepancy values.** The paper experiments with max discrepancy 4 vs. 8 but never compares their results or justifies the choice. The selection (4 or 8) is called out in Section 4 but absent from the results.

- **Only one base model (Chronos Mini) is tested.** The paper acknowledges this implicitly as a resource constraint, but claims of generalizability ("can be easily extended to other time series foundation models") would be strengthened by testing at least one additional model or model size.

### Trivial

None.

## Nice-to-Haves

- Report the MASE of the *average* trial (not just the best-of-10) to give a realistic sense of expected performance, along with standard deviations.
- Compare LDS against random search over the same 10-trial budget to justify its inclusion.
- Specify the full fine-tuning protocol used (learning rate, epochs, optimizer, schedule) or use the recommended settings from Ansari et al. (2024).
- Provide a complete, executable specification of the LDS algorithm for this search space, including the initial configuration and the discrepancy function for mixed-type hyperparameters.
- Include a computational cost analysis (total wall time per dataset, epochs per trial).

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism that the "first paper to explore autotuning time series transformers" claim is narrow.** This is speculative on the reviewer's part and cannot be verified without a complete literature survey. The claim is qualified as "to the best of our knowledge" and the paper's scope is clearly defined.
- **Missing related work on HPO for time-series fine-tuning.** This is scope creep; the paper's contribution is a specific combined method (LoRA + LDS) for a specific model family, not a general HPO survey.
- **Strength: "clear and reproducible methodology."** Dropped because it conflicts with the verified weakness that LDS is underspecified for reproducibility.
- **Strength that the paper addresses an important problem.** Generic and lacking specific evidence anchor.
- **Section-by-section notes about the abstract/introduction framing and related work being "adequate but shallow."** These are generic editorial opinions without concrete defects.

## Novel Insights

The Strength Finder's identification of the smaller-autotuned-model-beats-larger-zero-shot result (Table 4) is the paper's most compelling empirical finding and is worth elevating beyond the paper's own emphasis. The fact that a 20M-parameter model with LoRA fine-tuning can outperform a 710M-parameter zero-shot model on 3/10 datasets — and a 46M-parameter model on 6/10 — is a practical point that speaks to the value of targeted fine-tuning over simply scaling up model size. The paper somewhat buries this insight in the text; it is stronger evidence for the approach than the full-fine-tuning comparison that the authors foreground.

None beyond the paper's own contributions.

## Suggestions

1. **Fix the full fine-tuning baseline.** Either tune the full fine-tuning hyperparameters with the same budget (10 trials) or document the protocol used and cite Ansari et al. (2024)'s recommended settings. Without this, the central comparison is not interpretable.
2. **Validate LDS experimentally.** Add a random search baseline over the same 10-trial budget. If LDS does not consistently outperform random search, remove the LDS framing and present the contribution as "LoRA + search" rather than "LoRA + LDS."
3. **Specify the LDS algorithm completely.** Provide: the initial configuration, the discrepancy function definition (with handling of categorical variables), the tie-breaking rule, and the candidate generation procedure. A fully specified algorithm in the main text (not a figure) is essential.
4. **Report error bars.** Add standard deviations or confidence intervals for all reported MASE values. Also consider reporting the median or mean performance across search trials, not just the best.
