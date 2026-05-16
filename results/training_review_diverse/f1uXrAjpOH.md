Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me write this up now.

---

## Summary

This paper introduces Open-vocabulary Multimodal Emotion Recognition (OV-MER), a new task paradigm that removes the fixed label-space limitation of traditional emotion recognition, allowing prediction of arbitrary numbers and categories of emotional labels. To support this paradigm, the authors construct OV-MERD (a dataset with 248 emotion categories — a dramatic expansion over existing ≤10-category datasets), propose set-based evaluation metrics with semantic grouping, and provide a comprehensive benchmark evaluating 15 MLLMs plus oracle pipeline variants. The human-LLM collaborative annotation strategy is shown to produce richer descriptions and more diverse labels than human-only annotation.

## Strengths

1. **Novel and well-motivated task paradigm**: The paper clearly defines and justifies OV-MER as a logical extension beyond one-hot and multi-label MER, arguing convincingly that fixed label spaces cannot capture the full range of human emotions (~34,000 according to Plutchik). The task comparison diagram and quantitative label comparison (248 categories vs. ≤10 in prior datasets, Table 20) make a strong case for the paradigm shift.

2. **Human-LLM collaborative annotation pipeline**: The dataset construction strategy (Section 3) — combining LLM pre-annotation (GPT-4V for video, SALMONN for audio) with two rounds of human checks (different annotators per round), cross-lingual label merging, and final manual verification — is a creative approach to generating rich open-vocabulary labels at scale. Figure 20 provides quantitative evidence that this strategy produces longer descriptions, more diverse emotions, and more labels per sample than human-only annotation.

3. **Set-based metrics with semantically grounded grouping**: The paper proposes a thoughtful solution to the evaluation challenge in OV-MER — grouping semantically similar emotions before computing precision/recall/F₁. Two complementary grouping strategies are offered: a direct GPT-based method and a psychologically grounded Emotion Wheel-based method. The thorough analysis (Table 4) showing high Pearson correlation (0.942 M-avg) between GPT-based and EW-based rankings demonstrates that the inexpensive, reproducible EW-based metrics can serve as a practical substitute.

4. **Comprehensive benchmark and actionable analysis**: 15 MLLMs are evaluated, revealing that even the best MLLM (GPT-4V, Fₛ=55.51) falls far short of the human-LLM pipeline (Fₛ=80.05), clearly establishing the difficulty of OV-MER as an open challenge. The ablation on MLLM prompting strategies (S0/S1/S2, Figure 6) showing that a two-step decomposition (separate MLLM extraction + LLM fusion, S2) consistently outperforms joint input (S1) provides a practical architectural insight.

## Weaknesses

### Fatal
None.

### Major

1. **Ground-truth labels lack direct human validation**: The OV-MERD ground truth is extracted by GPT-3.5 from CLUE-Multi descriptions. While two rounds of human checks are performed on the *clues* (descriptive content such as facial expressions, tone of voice), and cross-lingual merging with manual checks is applied, the final emotion *labels* themselves are never validated against a purely human-annotated gold standard. It is not demonstrated that the LLM-extracted labels reflect genuine emotional nuance rather than GPT-3.5's particular annotation biases. This is a structural concern for a dataset that will serve as a benchmark — users cannot be certain whether model failures reflect genuine emotion recognition limitations or misalignment with an LLM-derived ground truth. The paper does not report inter-annotator agreement statistics for the human checks, nor the total number of annotators involved, which further limits confidence in the annotation quality.

### Minor

2. **Dataset size and basic statistics are not reported**: The paper states that OV-MERD is a sub-sample of MER2023, gives the number of categories (248) and label range per sample (1–9), but never reports the total number of samples. The limitations section merely says it is "currently small in scale." For a dataset contribution, this is a basic missing fact that prevents assessment of statistical power, diversity, and coverage.

3. **The benchmark table groups oracle pipelines with automatic baselines without clear labeling**: In Table 1, CLUE-Multi (which uses human-checked clues) achieves 80.05 Fₛ, far above any fully-automatic MLLM (~55 max). While the table visually separates the "CLUE-M/A/T/V" section and the text notes it uses manually checked clues, this critical distinction should be made more explicit — e.g., labeling the oracle methods as "Human-in-the-Loop Upper Bound" or presenting them in a separate table. A casual reader could misinterpret the gap as indicating a solvable algorithmic deficiency rather than an inherent advantage from human input.

4. **Metric circularity concern not fully addressed**: The GPT-based grouping (used in the main results) relies on GPT-3.5 — the same model used to extract ground-truth labels. This creates a potential circular dependency where metrics reward models that happen to align with GPT-3.5's notion of emotion similarity rather than capturing genuine emotional variation. The EW-based grouping is proposed as a remedy, but the synonym/word-form expansions (EW-S, EW-SF) within the EW pipeline also depend on GPT-3.5. Only the core EW structure (the five emotion wheels) is truly GPT-independent. The correlation analysis relies on Pearson (linear correlation); rank-order correlation (Spearman) would be more informative for establishing whether rankings are stable across grouping strategies.

5. **Similarity score methodology for cross-lingual labels is unspecified**: The paper reports a similarity score of 0.82 between Y_EE and Y_CE (English labels vs. translated-from-Chinese labels) but does not specify how similarity was computed (e.g., Jaccard, cosine, F₁?). This omission hinders reproducibility of the cross-lingual validation step.

### Trivial

6. **Random baseline description is underspecified**: The paper says "randomly select a label from basic emotions" but does not enumerate which basic emotions are used. From context (Section 1 lists six: anger, disgust, fear, happiness, sadness, surprise), it seems to be these six, but this should be explicit. (This does not harm the evaluation since the Random baseline is presented as a lower bound.)

7. **The ensembling finding is predictable**: Table 2 shows that combining audio and video MLLMs improves performance, sometimes surpassing GPT-4V. This is a predictable ensembling effect; the result is not particularly surprising or novel.

8. **Three-frame sampling for GPT-4V is not justified beyond "relatively short duration"**: The paper samples only three frames per video for GPT-4V pre-annotation without specifying video durations or providing evidence that three frames are sufficient to capture temporal emotion cues. This is acknowledged as a limitation but the analysis is thin.

9. **LLM bias is not discussed in limitations**: The limitations section (Section 7) discusses small scale and incomplete model coverage, but does not address the potential bias introduced by using LLMs at multiple points in the annotation and evaluation pipeline.

## Nice-to-Haves
- A human validation experiment on a subset of OV-MERD (independent annotators assigning open-vocabulary labels) would substantially strengthen confidence in the ground truth.
- Reporting Spearman rank correlation in addition to Pearson for the GPT vs. EW metric comparison would more directly address ranking stability.
- A brief ethics statement covering annotator training, data sensitivity, and potential harmful content would be welcome for a dataset paper.
- Cost analysis for the full dataset construction pipeline (not just GPT-based grouping) would aid reproducibility planning.

## Removed Points
The following points from the harsh critic are removed or downgraded per verification against the paper:

- **"Paper does not compare against prompting MLLMs directly to output emotion labels"**: The ablation study (S0/S1/S2, Figure 6) does compare scenarios where MLLMs receive joint video+text input (S1), which is functionally equivalent to direct prompting. The critic appears to have overlooked this section.
- **"Data availability not stated"**: Removed per hard rule — criticism about release status/availability of cited resources.
- **"Standard precision/recall/F1 without grouping not reported"**: These metrics are not meaningful for open-vocabulary prediction with an unbounded label space, making this an expectation mismatch with the paper's class.
- **"Ensembling conclusion is a non-finding"**: While predictable, the combination experiments serve as a useful ablation demonstrating modality complementarity, not a core claimed contribution. Downgraded to trivial.
- **"CLUE-Multi presentation is deceptive"**: The table visually separates oracle pipelines and the text explicitly notes the difference. Recharacterized as a presentational clarity issue (minor) rather than a misleading comparison.
- **"Ground-truth validity is fundamentally questionable"**: The human-LLM collaborative pipeline includes two rounds of human checks with non-overlapping expert annotators, cross-lingual merging, and manual verification. The concern is real but overstated as "fundamental" — reduced to Major from the critic's implied Fatal framing.

## Novel Insights
None beyond the paper's own contributions. The reviews surface a genuine tension in LLM-derived datasets and metrics that is characteristic of the current era: as LLMs are increasingly used to create benchmarks, the risk of circular evaluation grows. The paper's explicit attempt to provide an LLM-independent evaluation alternative (EW-based grouping grounded in psychological theory) is a principled response, though imperfectly executed (EW-S/EW-SF still depend on GPT). This dynamic — using theory-driven structures to break free of LLM circularity while still needing LLMs for coverage — is worth watching as a methodological pattern across NLP/vision communities.

## Suggestions
1. **Report dataset size** (number of samples) and basic statistics such as train/val/test splits. This is essential for any benchmark paper.
2. **Run a human validation study** on a subset: have independent annotators directly assign open-vocabulary emotion labels to ~100–200 samples, and compute agreement between human labels and the OV-MERD ground truth. This would directly address the central validity concern.
3. **Add Spearman rank correlation** to Table 4 alongside Pearson to demonstrate ranking stability between GPT-based and EW-based metrics. This is stronger evidence that EW can "replace" GPT.
4. **Separate oracle baselines more explicitly** — either put CLUE-M/A/T/V in a separate table clearly labeled "Human-in-the-Loop Upper Bounds," or add a prominent footnote to Table 1.
5. **Specify the similarity metric** used for cross-lingual label comparison (Section 3.2) explicitly.
6. **Add inter-annotator agreement statistics** (e.g., Cohen's κ or percentage agreement) for the two rounds of human checks on clues.
7. **Discuss LLM bias explicitly** in the limitations section.

## Score and Decision

This paper introduces a genuinely novel task paradigm and provides the necessary initial infrastructure (dataset, metrics, baselines). The core contribution is real: OV-MER addresses a meaningful limitation of current fixed-label emotion recognition, and the groundwork laid here enables future research in this direction. The weaknesses — particularly the lack of direct human validation of ground-truth labels and the missing dataset size — are real and need attention, but they do not invalidate the contribution. The paper understands its limitations and the proposed EW-based metrics represent a good-faith effort to address the circularity concern.

The paper is above the acceptance threshold: the strengths of the paradigm contribution, the thoughtful dataset construction methodology, and the comprehensive benchmarking outweigh the presentational and validation gaps. I recommend acceptance with expectation that the authors address the major concerns (validation, statistics) in a revision.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>