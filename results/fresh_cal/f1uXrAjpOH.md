Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

---

## Summary

This paper introduces Open-vocabulary Multimodal Emotion Recognition (OV-MER), a paradigm that removes constraints on the label space, allowing models to predict an arbitrary number and categories of emotion labels. To support this new task, the authors construct OV-MERD (a dataset with 248 emotion categories derived from MER2023 via human-LLM collaborative annotation), propose set-based evaluation metrics with two grouping strategies (GPT-based and emotion-wheel-based), and benchmark 16 MLLMs alongside CLUE variants. The work provides foundational resources for transitioning from basic-emotion recognition to richer, open-vocabulary emotion understanding.

## Strengths

- **Substantially larger label space than any prior MER dataset.** Table 1 shows OV-MERD has 248 emotion categories and supports 1–9 labels per sample (most 2–4), whereas all 12 listed existing MER datasets have at most 10 categories and only a single label per sample. This is a genuine, concrete expansion that directly supports the paper's core contribution.

- **Human-LLM collaborative annotation demonstrably enriches label quality.** Figure 20 compares human-only (H) vs. human-LLM (H+L) annotation along three dimensions: description length, label count distribution, and word cloud diversity. The H+L descriptions are longer, produce more labels per sample, and exhibit a broader set of emotion terms, providing quantitative evidence that the proposed annotation method outperforms human-only approaches.

- **Comprehensive benchmark establishing a clear performance gap.** Table 1 evaluates 16 MLLMs plus CLUE variants under a consistent protocol. The best MLLM (GPT-4V) achieves F_s = 55.51, while the human-LLM pipeline (CLUE-Multi) reaches 80.05 — a 24.5-point gap that quantifies how far current models are from adequate OV-MER performance and validates the task's difficulty.

- **Informative ablation study on CLUE-MLLM generation strategies.** Figures 5–6 compare three strategies (S0: no text; S1: joint text+video input; S2: two-stage — extract descriptions first, then combine with text). S2 consistently outperforms S1 across all tested MLLMs, providing clear, evidence-based guidance for future practitioners.

- **Validation that emotion-wheel-based metrics can substitute for GPT-based grouping.** Table 4 reports Pearson correlation coefficients between the EW-based M-avg and GPT-based metric as high as 0.942, showing that a cheaper, reproducible alternative can maintain ranking consistency with the more expensive GPT-based grouping.

## Weaknesses

### Fatal
None.

### Major

- **Tension between the open-vocabulary premise and the grouping-based metric.** The paper motivates OV-MER by arguing that human emotions span ~34,000 distinct states and that fixed label spaces miss nuance. Yet the evaluation metric groups emotions into coarse categories (e.g., mapping "angry" and "frustrated" to the same L1 group in an emotion wheel). After grouping, predicting any emotion in the correct group earns full credit regardless of fine-grained specificity — a model that outputs "angry" scores the same as one that outputs "frustrated" when both fall under "mad" (L1 in W1). The paper acknowledges the need to handle synonyms (lines 139–142), but the grouping goes well beyond synonym handling to coarse psychological categories (e.g., "offended" and "humiliated" grouped together). This does not invalidate the contribution — the dataset and task framing remain valuable — but it means the metric measures *group-level* accuracy, not fine-grained open-vocabulary fidelity. The paper should more clearly delimit what the metric captures and discuss this gap.

- **Heavy reliance on GPT-3.5 across multiple pipeline stages without quantifying downstream effects.** GPT-3.5 is used to: (a) extract ground-truth emotion labels from CLUE-Multi descriptions (line 95), (b) define the GPT-based grouping that the evaluation metric depends on (line 146), and (c) serve as the LLM that combines MLLM outputs with text in the CLUE-MLLM baselines (line 216). While the ground-truth labels are human-validated, the validation *follows* GPT-3.5 extraction and is thus bounded by what GPT-3.5 produced. The paper does not report how often annotators *added* labels that GPT-3.5 missed versus removing erroneous ones. Without this quantification, it is unclear whether the reported gap between CLUE-MLLM baselines and CLUE-Multi partly reflects vocabulary alignment with GPT-3.5 rather than genuine multimodal emotion understanding.

### Minor

- **The exact number of samples in OV-MERD is not stated.** The paper says it "evenly selects samples with further annotations" from MER2023 (line 131) but gives no count. Knowing the test-set size is essential for assessing statistical power and generalizability.

- **Annotation quality metrics are not reported.** The paper describes having "experts in affective computing" conduct two rounds of manual checks with non-overlapping annotators (line 83), but provides no inter-annotator agreement statistics, number of annotators, or breakdown of labels added vs. removed during human validation.

- **The Random baseline is not a valid lower bound for the open-vocabulary setting.** It selects one label from basic emotions (6 categories) rather than from the full 248-category space (line 292). A baseline restricted to 6 categories has an artificially high chance of hitting a group, achieving ~17% F_s. A random draw from the full label distribution would produce a lower and more meaningful baseline.

- **Only two experimental runs per baseline.** The paper conducts each experiment twice (line 284). Two runs are insufficient to characterize variance reliably, and many baselines show overlapping error bars (e.g., Video-ChatGPT and LLaMA-VID in English, Table 1). Three to five runs would be more credible.

- **The similarity metric used to compute the 0.82 score between Y_EE and Y_CE is unspecified.** The paper reports "the similarity score between Y_EE and Y_CE is 0.82" (line 98) without defining what similarity metric was used (e.g., Jaccard, cosine, set overlap). This makes the claim difficult to interpret or reproduce.

### Trivial

- **Implementation statement inconsistent with GPT-4V baseline.** The paper states "all models are implemented in PyTorch, and all inference processes are carried out using a 32G NVIDIA Tesla V100 GPU" (line 216) in the context of CLUE-MLLM baselines, which include GPT-4V — a cloud API that cannot run locally on a V100 GPU. The phrasing should clarify that this applies only to local models.

## Nice-to-Haves

- Include a human judgment study validating that the emotion groupings (both GPT-based and EW-based) align with perceived emotion equivalence in this task, or replace group-based metrics with a continuous semantic similarity measure (e.g., cosine distance in an emotion embedding space).
- Report a random baseline sampled from the full 248-category label distribution.
- Compare the OV-MER metric against embedding-based semantic similarity metrics (e.g., cosine similarity between label embeddings) alongside the lexical-overlap metrics already evaluated.

## Removed Points

- **"Paper implies prior work is strictly limited to Ekman's six"**: The paper says "researchers *typically* limit the label space to these basic emotions" (line 18) and Table 1 correctly shows IEMOCAP (10 categories). The characterization is accurate, not overstated. **Removed** (factually incorrect criticism).
- **"The metric, test set, and baselines all rely on the same LLM creating circularity"**: The critic frames this as "circular," but the pipeline is sequential, not circular. Ground truth is human-validated, grouping is a separate post-hoc process, and baselines use diverse MLLMs (only the final text-combination step uses GPT-3.5). The overlap is a legitimate concern about vocabulary alignment, but "circularity" is too strong a characterization. **Re-framed** as the GPT-3.5-reliance weakness above.
- **"GPT-based and EW-based grouping use different notions of similarity — the paper does not discuss this discrepancy"**: The paper *does* discuss this by comparing both approaches via PCC (Table 4) and explicitly notes that GPT-based grouping uses "same meaning" while EW uses psychological relatedness. The discrepancy is acknowledged and empirically evaluated. **Removed** (paper already addresses this).
- **"Correlation between GPT-based and M-avg does not imply they capture the same construct"**: A standard methodological observation that could be applied to any correlation analysis. Without specific evidence that the correlation is misleading, this is generic speculation. **Removed**.
- **"The paper should have compared against semantic similarity metrics"**: This is a suggestion for improvement, not a weakness. **Moved to Nice-to-Haves**.
- **Strength Finder's generic strengths**: Removed strengths framed as "this paper addresses an important problem" or similar generic praise. **Removed** per filtering rules.

## Novel Insights

None beyond the paper's own contributions. The reviews surface legitimate methodological concerns (metric-grouping tension, GPT-3.5 reliance) but do not offer novel scientific insights that the paper itself does not provide.

## Suggestions

1. **Report the exact dataset size** (number of samples) in OV-MERD alongside the number of emotion categories already given.
2. **Validate the grouping** with a human study showing that grouped emotions are indeed considered equivalent for the task, or supplement with a fine-grained continuous similarity metric.
3. **Quantify the human contribution** to ground-truth labels: report how many labels were added by human annotators vs. retained/removed from GPT-3.5's extraction.
4. **Replace the Random baseline** with sampling from the full 248-category distribution to establish a meaningful lower bound.
5. **Increase experimental runs** to at least 3–5 for reliable variance estimation.
6. **Specify the similarity metric** used for the cross-language label comparison (0.82 value on line 98).
7. **Add inter-annotator agreement statistics** (e.g., Cohen's kappa) for the manual check rounds.
8. **Clarify the infrastructure statement** to distinguish between locally-run models and cloud APIs (GPT-4V).

## Score and Decision

This paper makes a genuinely novel contribution by defining the OV-MER task and providing foundational resources (dataset, metrics, baselines). The label space expansion (248 vs. ≤10 categories) is a meaningful step forward, and the benchmark provides a useful reference for future work. The weaknesses are real but not fatal — they concern the metric's ability to fully deliver on the "open-vocabulary" promise and the heavy GPT-3.5 footprint — and are addressable in revision. The paper warrants acceptance at a venue that values new task/dataset contributions over tight evaluation, provided the authors acknowledge and discuss these limitations.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>