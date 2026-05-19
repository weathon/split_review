- Decision: Reject
- Avg Score: 5.40
- Scores: 5, 5, 6, 5, 6
Now I have all the information needed to write a comprehensive, verified review.

## Summary

This paper presents a large-scale empirical study evaluating 20 sample selection strategies across 5 few-shot learning approaches (Prototypical Networks, MAML, Fine-Tuning, Mistral-7B, Zephyr-7B) on 8 image and 6 text datasets, and proposes ACSESS — a method for automatically combining selection strategies by first identifying relevant strategies (via forward/backward/datamodels selection) then weighting them. The key empirical findings are: (1) learnability properties (Cartography, Forgetting) are more impactful than informativeness or representativeness, (2) the benefit of selection diminishes with shot count and disappears after ~30-40 shots, and (3) the proposed combination method consistently outperforms individual strategies and the LENS baseline.

## Strengths

- **Comprehensive and well-designed evaluation.** The study covers 20 selection strategies × 5 few-shot approaches × 14 datasets (image + text) with 10 seeds and 5 splits — a scope that substantially exceeds prior single-paradigm studies. This breadth allows the paper to draw robust conclusions about modality and approach dependence.

- **ACSESS consistently improves over all individual strategies.** Table 1 shows ACSESS_Uniform achieves +1.12 to +2.30 pp across settings vs. classic selection, outperforming every single strategy. The comparison against LENS (the closest ICL-specific method) is statistically significant (p=0.0002, Wilcoxon), with ACSESS_Weighted achieving +2.55 pp on Mistral vs. LENS's +1.73 pp.

- **Identification of diminishing returns with shot count (Figure 3) is a practically valuable finding.** The observation that selection impact peaks at low shots and regresses to random at 30-40 shots, and that ICL performance actually *decreases* beyond 20-25 shots due to context limits, provides actionable guidance for practitioners deciding whether to invest in selection.

- **Evidence that learnability dominates other properties.** Cartography (Easy) yields +1.17 pp on MAML image tasks, Forgetting yields +1.27 pp on Mistral, while representativeness strategies often hurt (Herding: -2.36 pp on MAML image). This ranking of property types is a clean takeaway from the study.

- **ACSESS shows lower seed sensitivity than individual strategies.** Figure 4 shows ACSESS_Uniform's standard deviation across runs (~0.5 pp) is consistently smaller than similarity-based selection (>1 pp) or active learning strategies, supporting the claim that combination stabilizes selection.

## Weaknesses

### Fatal
None.

### Major

- **Strategy selection phase does not specify what data is used for evaluation.** The paper describes forward/backward selection as evaluating "the increase in performance the strategy would yield" (line 96) and the datamodels variant as training LASSO on "difference in performance to the baseline" (line 100), but never states whether these evaluations use a held-out validation set or the test set itself. If test-set performance guides strategy selection, the reported gains would reflect test-set overfitting. This is the most critical gap in the method description — it must be clarified for the core claim to be credible. (*Note: this is a specification gap, not a demonstrated flaw; the authors may have used proper validation but omitted the detail.*)

- **The candidate pool for computing strategy scores is underspecified.** Strategies like Forgetting, Cartography, GraNd, and Herding require training dynamics or full-dataset statistics to assign per-sample scores. The paper never states: (a) how many candidate samples per class are available for selection, (b) whether a separate training set is used to precompute these scores, or (c) how metrics like forgetting events are meaningfully computed on small pools (e.g., 5-way 5-shot). This ambiguity makes it difficult to assess whether the setting is realistic or whether the results apply to standard few-shot regimes.

### Minor

- **Absolute accuracy is never reported.** Table 1 shows only *differences* from the classic selection baseline. Without absolute performance numbers, readers cannot judge whether a +1 pp gain is on top of 50% or 90% accuracy, limiting practical interpretation. The differences alone could mask floor/ceiling effects.

- **The conversion of categorical strategy outputs (Cartography: easy/ambiguous/hard) to numeric scores is not described.** The paper normalizes all scores to [0,1] and takes weighted averages (line 103), but does not explain how Cartography's discrete categories (lines 77, 155-158) are mapped to numerical scores — binarization, rank-based encoding, or some other scheme? This affects reproducibility.

- **Computational cost is discussed qualitatively but never quantified.** The paper notes that uniform weighting "represents a good trade-off between the performance increase and the computation costs" (line 194), but provides no wall-clock time, number of model trainings required per selection run, or GPU-hour estimates. Forward/backward selection with 20 strategies could require dozens of model trainings per dataset per approach; quantifying this would help practitioners assess practicality.

- **Comparison against learned selection methods is limited to LENS.** The paper correctly identifies LENS as the closest related method and compares against it. However, other learned approaches exist (trained retrievers, reinforcement-learning-based selection) that are not discussed or compared. This should be acknowledged as a scope limitation rather than a gap.

### Trivial
None.

## Nice-to-Haves
- Adding significance tests (paired t-test or Wilcoxon) for ACSESS vs. each individual strategy across datasets would strengthen the headline claim beyond the single LENS comparison.
- Including a small table of absolute accuracy (not just deltas) in the appendix for readers to assess practical significance.
- A brief description of how Cartography categories are derived from training dynamics would improve self-containedness (though the information is available in cited works).

## Removed Points

*These points were raised by reviewers but are removed after cross-checking:*

- **"A 95% CI would include values close to zero" for ACSESS_Uniform on Image/ProtoNet (+1.12 ± 0.80).** This is factually wrong: with 8 image datasets, SEM ≈ 0.28, so the 95% CI is approximately [0.46, 1.78] — it excludes zero. The specific example used to claim weak statistical support is incorrect.

- **"The paper does not compare against any learned selection method" beyond LENS.** This overstates the gap: the paper acknowledges LENS as "a work closest to ours" (line 41) and compares against it. Expanding to all possible learned methods is outside the paper's stated scope of evaluating heuristic single-property strategies vs. a combination method. Kept as a weakened minor point.

- **"Forward/backward selection might have circularity in the uniform weighting scheme."** This is not a flaw — forward selection evaluates combinations using uniform weighting and then uses uniform weighting for the final combination. This is consistent by design, not circular. The Datamodels weighting is indeed a genuinely different scheme, as the paper already describes.

- **"Cartography variants not explained."** The paper cites the original works and lists the categories (easy, ambiguous, hard, easy+ambiguous) in Table 1. Expecting readers to consult cited works for full definitions is standard practice.

- **"Herding performs poorly on all image datasets but Cartography works well across all"** — this was listed as a strength but is simply a restatement of the paper's findings rather than a contribution assessment. Moved here as it does not add independent evaluative weight.

## Novel Insights

The key insight that emerges across the three sources, but is more explicit in synthesis than in any single one, is that the paper's value is asymmetrically distributed: the *empirical findings* (the ranking of property types, the shot-count analysis, the modality/approach dependence) are robust, well-supported, and likely to be cited regardless of the ACSESS method. The ACSESS method itself is simple — uniform weighting of selected strategies — and its main contribution is to demonstrate that combination beats selection, not to propose a novel algorithmic technique. The reviews collectively surface that the paper would be strengthened by explicitly separating these two contributions and acknowledging that the empirical taxonomy may outlast the method in impact.

## Suggestions

1. **Clarify the validation protocol for strategy selection.** Add a sentence stating explicitly that strategy selection was performed using a held-out validation set (or cross-validation) and that final reported numbers are from a separate test set. This is the single most important fix.
2. **Define the candidate pool.** Specify how many labeled samples per class were available to the selection strategies, and briefly describe how training-dynamics-based strategies (Forgetting, Cartography) are computed with this pool size.
3. **Report absolute accuracies.** Add a supplementary table with the raw accuracy values alongside the deltas, or include them in the appendix.
4. **Describe Cartography score conversion.** Add a sentence explaining how the categorical labels (easy/ambiguous/hard) are turned into numeric scores used in the weighted combination.
5. **Add a computational cost note.** A single sentence with approximate GPU-hours per ACSESS run (e.g., "forward selection required ~X model trainings per dataset") would help readers gauge practicality.
