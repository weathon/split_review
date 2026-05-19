- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 3, 6, 5
Now I have a thorough understanding of the paper. Let me construct the final review.

---

## Summary

This paper proposes a two-stage framework (FLP) for predicting the downstream task performance of large language models: first model FLOPs→pre-training loss via a power law, then model pre-training loss→downstream performance via linear regression. The key insight is that using intermediate checkpoints generates dense data points after the emergent threshold, avoiding the need to train models all the way to convergence. The paper then extends this to a data-mixing setting (FLPMix) where domain-specific losses are predicted from FLOPs across multiple data sources using a product power law, and a small neural network maps per-domain losses to performance. Experiments with sampling models up to 3B predict 7B and 13B target performance within 5-10% error, and FLPMix predicts performance across data mixtures within 10% error for most benchmarks.

## Strengths

1. **Two-stage framework effectively addresses the emergence problem.** By routing through pre-training loss as an intermediate variable, the method circumvents the scarcity of emerged data points that plagues direct FLOPs→Performance prediction. The paper shows this concretely: direct FP (FLOPs→Performance) has only ~3 usable data points per task due to the emergent threshold, whereas FLP uses dense intermediate-checkpoint data and achieves 5-10% relative error for 7B and 13B targets (Section 4.4, Figs. 1-2 in the paper).

2. **Domain-specific loss with a neural network mapping provides a principled extension to data mixtures.** FLPMix replaces average validation loss with per-domain losses, which is well-motivated: different data mixtures can change domain-specific capabilities in ways that average loss masks. The ablation study (Section 7.2, Fig. 8, Table 2) systematically compares FLOPs-only, average-loss-linear, domain-loss-linear, and domain-loss-neural approaches, confirming that domain-specific neural network mapping yields the best predictions.

3. **Thorough ablation study of analytical forms for FLOPs→Domain Loss.** The paper evaluates four candidate functions (M1–M4) for modeling FLOPs→domain loss (Section 7.2, Figs. 6-7) and shows that the chosen form (M4, product of three power-law terms) achieves the lowest average relative error while remaining within 2.5% error across most domains. Simpler forms like total-FLOPs-only (M1) produce high domain errors, making this a well-justified design choice.

4. **Efficient use of intermediate checkpoints for data collection.** Rather than training each sampling model to convergence for a single data point, the method collects (loss, performance) pairs from up to ~30 intermediate checkpoints per run, filtering only by above-random performance. This significantly reduces the compute needed to fit the Loss→Performance curve (Section 3.2, Section 4.3).

## Weaknesses

### Fatal

None.

### Major

1. **Limited evaluation scope for the core claims.** The FLP framework is tested on only two target sizes (7B, 13B). The FLPMix extension is tested on 3B targets across multiple mixing ratios but on only **one** 7B target at a single mixing ratio (0.3, the same ratio used for the 3B sampling model). The data mixture optimization study (Section 8.1) is conducted entirely at the 1B scale, not at the target scales the method is designed for. This narrow evaluation means we cannot assess generalization to larger models, different mixing ratios at scale, or whether the optimization findings transfer. The paper's title claims "scaling laws" and the abstract promises a method that "effectively forecast[s] the performance of 3B and 7B LLMs across various data mixtures," but the 7B evidence for FLPMix is a single data point at one mixture ratio.

2. **No quantitative comparison to the most relevant existing methods.** The paper acknowledges that Hu et al. (2023) (PassUntil) and Schaeffer et al. (2024) (answer loss) address the same core problem — predicting downstream performance despite emergent abilities — and even discusses their limitations (Section 2). Yet the experimental comparison is limited to trivial baselines: direct FLOPs→Performance (FP) for FLP, and average-loss FLP for FLPMix. Without comparing to PassUntil or answer-loss-based alternatives on the same evaluation setup, the claimed advantages ("operates independently from and complements existing approaches," line 94) are unsubstantiated. The paper also mentions comparisons with GPT-4 and Llama-3 technical report approaches in deferred sections, but these are less targeted than the closest academic prior work.

### Minor

1. **The key premise (loss→performance correlation) is not directly evidenced in the main text.** The entire FLP framework depends on a predictable relationship between pre-training loss and downstream performance after the emergent threshold. The paper asserts this correlation citing Du et al. (2024) and Huang et al. (2024), and says scatter plots appear in a deferred section (`sec:linear_rel`). No visual evidence — scatter plots, R² values, or residual analyses — is shown in the main paper. While the end-to-end prediction results serve as indirect validation, the reader cannot independently assess the linearity assumption that motivates Equation (2). The paper would benefit from presenting this evidence prominently.

2. **Checkpoint non-independence is unaddressed.** The method uses up to ~30 intermediate checkpoints from each training run as independently sampled data points for fitting the Loss→Performance curve (Section 4.3). These checkpoints are auto-correlated along the training trajectory — they share the same model family, training distribution, and optimizer state. The paper does not discuss this, nor does it employ any correction (e.g., clustering standard errors, hierarchical modeling, or cross-validation across independent model runs). This could lead to overconfident parameter estimates and optimistic error margins.

3. **TriviaQA failure signals brittleness in sparsely sampled regimes.** The paper reports 20–30% relative error on TriviaQA for FLPMix (Section 6.4) and attributes this to insufficient sampling LMs between 1B and 3B parameters. This is an honest admission, but it reveals a structural limitation: the method requires dense coverage of the parameter range, and performance degrades substantially when the sampling LM set does not densely cover accelerated improvement phases. Users of the method would need to know how to choose sampling LM sizes to avoid this failure mode.

4. **Data mixture optimization is demonstrated only at the sampling-model scale.** Section 8.1 validates optimal mixing ratios found by FLPMix scaling laws by training models at the same scale (1B) used for the sampling LMs. While this shows the method can identify optimal ratios, it does not demonstrate the claimed practical value of optimizing mixtures for target models larger than the sampling set. This is a weaker claim than what the conclusion implies.

5. **Training details for the LMs are not reported.** The paper does not specify optimizer, learning rate schedule, batch size, tokenization, or hardware for the trained sampling and target LMs. Given that the method relies on training 12+ models, these details are important for reproducibility and for understanding potential confounders in the scaling trends.

### Trivial

None.

## Nice-to-Haves
- Reporting confidence intervals or bootstrap-estimated error ranges for predictions, especially given the small number of target evaluations (one per size/ratio).
- An analysis of how sensitive the fits are to the checkpoint filtering criteria (loss improvement threshold, >random+5 performance threshold).
- A rough FLOPs budget comparison showing that training the sampling models + evaluating checkpoints is cheaper than training a single target LLM to convergence.

## Removed Points

The following points from the reviewer inputs were removed (with brief justification):

- **"Method's main advantage rests on a correlation neither established nor tested"** (from Harsh Critic): Overstated. The paper cites external evidence for the correlation (Du et al. 2024, Huang et al. 2024) and provides end-to-end prediction results that serve as validation. The scatter plots are referenced in a deferred section (likely an appendix that was stripped by the parser). The remaining valid core (that this evidence should be in the main text) is retained as a Minor weakness.

- **"FP baseline is a straw man"** (from Harsh Critic): The FP baseline is not a straw man — it is a natural direct alternative. The fact that it predictably fails on emergent tasks is precisely the motivation for the two-stage approach. The comparison is valid for illustrating the problem.

- **"Crucial insight about intermediate checkpoints is presented as new, while it's standard"** (from Harsh Critic): In the scaling-law literature (Kaplan et al. 2020, Hoffmann et al. 2022), models are typically evaluated at convergence only (one data point per model). Using intermediate checkpoints for performance prediction as done here is genuinely novel in this context.

- **"Missing related works (inverse scaling prize, etc.)"** (from Harsh Critic): Removed per instruction — I cannot independently verify the existence or relevance of works not cited in the paper.

- **"Pure formatting/style nitpicks"** and **"Reproducibility nitpicks about undisclosed hyperparameters"**: Partially removed or weakened. The training details concern (optimizer, LR schedule, batch size) is not a trivial nitpick for a paper that trains many models, so it is retained as a Minor weakness. Other nitpicks (appendix content, proof locations) are removed since the parser strips those sections.

- **Strength Finder strength #3 ("practical application of scaling laws for data-mixture optimization")**: Weakened — the demonstration is at 1B scale only. The core fact that the method can identify optimal ratios is real, so the strength remains but is qualified by the limitation already stated in Weaknesses.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a new observation about the work that the paper itself does not already articulate.

## Suggestions

1. **Broaden the evaluation.** Add at least one more target size (e.g., 1B or 3B as a target, not just a sampling model) and, for FLPMix, test the 7B target at a different mixing ratio (not 0.3). This would significantly strengthen the generalization claims.

2. **Implement at least one existing baseline.** Compare FLP to PassUntil (Hu et al. 2023) or answer-loss prediction (Schaeffer et al. 2024) on the same benchmarks to substantiate the claim of complementarity/improvement.

3. **Move direct evidence for the loss→performance relationship into the main paper.** Show scatter plots with regression lines and R² values for each benchmark. This is the core premise of the method and merits front-and-center presentation.

4. **Address checkpoint non-independence.** Either adopt a hierarchical model that accounts for run-level grouping, or show that results are unchanged when using only one checkpoint per model (e.g., the best or last) or when cross-validating across runs.

5. **Report training configurations.** Specify optimizer, learning rate schedule, batch size, tokenization, and hardware for all trained models to support reproducibility.

6. **Discuss the sampling-density requirement.** The TriviaQA failure is informative. The paper should explicitly guide practitioners on how to choose sampling model sizes to avoid the gap that caused this failure.
