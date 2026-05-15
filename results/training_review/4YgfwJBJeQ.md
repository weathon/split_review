Now I have all the information needed. Let me synthesize the final consolidated review.

---

## Summary

The paper proposes StructChart, a two-stage pipeline for chart understanding: (1) a Chart-oriented Information Extractor (CIE) converts chart images into text via a ViT-based encoder-decoder, and (2) a reasoning stage feeds the extracted text to GPT-3.5 for downstream tasks (question answering, summarization, redrawing). Three contributions are highlighted: **Structured Triplet Representations (STR)** that replace linearized CSV as an intermediate format to better capture row-column-value relations, **SCRM** (a multi-tolerance metric for evaluating chart perception), and an **LLM-based self-inspection data production scheme** that generates a synthetic dataset (SimChart9K) to reduce reliance on real annotated data.

## Strengths

- **STR improves reasoning accuracy over LCT.** Table 4 shows that feeding STR (vs. linearized CSV) to GPT-3.5 improves exact-match accuracy on ChartQA (augmented split: 43.5 vs. 38.5; human split: 43.0 vs. 38.1), and surpasses Pix2Struct and Matcha on the augmented set. This is direct evidence that the structured format helps LLM-based reasoning.

- **Label efficiency via LLM-based data augmentation is convincingly demonstrated.** Table 5 shows that training on only 20% of ChartQA real data + SimChart9K achieves perception performance (mPrecision high: 59.1) comparable to training on 100% real data (58.6). Table 6 extends this finding to PlotQA (10% real + SimChart9K) and Chart2Text (20% real + SimChart9K). This is the paper's strongest result.

- **SCRM provides a structured, multi-level perception metric** that goes beyond simple string matching by evaluating both entity text (edit distance) and numerical values (relative error) at three tolerance levels. The metric is used consistently across all experiments (Tables 2, 3, 5, 6), offering finer granularity than prior evaluation approaches.

- **t-SNE analysis provides visual evidence of distribution alignment** between SimChart9K features and real datasets (ChartQA, PlotQA, Chart2Text), supporting the claim that the synthetic charts resemble real data distributions.

## Weaknesses

### Fatal
None.

### Major

- **No baseline comparison for the perception stage.** Table 2 reports only StructChart's own performance under different training conditions (single-set, real merging, real+sim merging). Without comparisons against existing perception methods (ChartOCR, ChartReader, Pix2Struct, etc.) on a common task using a common metric, it is impossible to assess whether the CIE component advances the state of the art in chart perception. The paper's claim of a "unified perception-reasoning paradigm" is weakened because the perception half is unvalidated against alternatives.

- **Incomplete quantitative evaluation of claimed reasoning tasks.** The paper motivates its "unified" approach by listing three reasoning tasks: question answering, summarization, and redrawing. Yet only QA receives quantitative evaluation (Tables 4, 7). Summarization and redrawing are shown only as qualitative examples, with the paper stating "due to the lack of public datasets and annotations, it is difficult to provide quantitative results" (line 196). This directly contradicts the paper's own description of Chart2Text as "a dataset for automatic summarization of statistical charts ... with annotations" (line 149). If Chart2Text provides chart-summary pairs, quantitative summarization evaluation (e.g., ROUGE, BLEU) should be feasible. The absence of such results means the "unified" claim is only partially supported.

### Minor

- **SCRM tolerance thresholds are presented without justification.** The three tolerance levels (strict: edit distance 0 + relative error 0; slight: edit distance 2 + 0.05; high: edit distance 5 + 0.1) are stated as fact (lines 106-108) with no ablation or sensitivity analysis explaining why these specific thresholds were chosen or how sensitive results are to them.

- **Data augmentation compared only against "no simulation."** Table 3 shows that adding SimChart9K improves performance over no augmentation, but the paper does not compare against simpler, cheaper alternatives (e.g., matplotlib with randomized parameters, standard image augmentations, or CSV row/column permutation). The claim that "the LLM-based method enhances diversity" lacks a controlled experiment isolating the LLM's contribution from other forms of augmentation.

- **Benefits of STR demonstrated only on QA.** While Table 4 shows STR outperforms LCT on ChartQA, the paper does not quantify whether STR's advantage extends to summarization or redrawing. Given that STR is presented as a general bridge between perception and all reasoning tasks, evaluating its benefit on at least summarization (via Chart2Text) would meaningfully strengthen the claim.

- **Architecture similarity to Pix2Struct is not discussed.** Section 3.1 describes a ViT with variable-resolution patching and 2D positional embeddings that closely resembles the Pix2Struct approach (Lee et al., 2022). While Pix2Struct is cited in related work, the paper does not acknowledge or differentiate its architectural design from Pix2Struct's. A brief discussion of differences or design choices would help position the contribution.

- **STR assumes row/column header structure, which does not generalize to all chart types.** The triplet representation (Entity_row, Entity_col, Value) inherently assumes charts have row and column headers. The paper does not discuss how pie charts, scatter plots without explicit legends, or single-series line charts would be represented. The data generation pipeline (line 132) mentions pie charts as a generated type, so this is a real coverage gap.

### Trivial

- **Ethics statement about "chart image plagiarism"** (line 205) is tangential and somewhat misplaced. The space would be better used discussing more material ethical considerations (e.g., bias in synthetic data, hallucination in LLM-generated chart code).

## Nice-to-Haves

- **Correlation analysis between SCRM scores and downstream QA accuracy.** Without showing that improving SCRM translates to better reasoning, the metric's practical utility as a proxy for downstream performance is asserted but not validated.
- **Analysis of STR error patterns vs. LCT.** The paper could analyze whether STR's gains come from better handling of specific failure modes (e.g., row-column misalignment, missing headers).
- **Comparison of LLM-based simulation to simpler augmentation methods** (e.g., matplotlib + random parameters) controlled for dataset size.
- **Ablation showing STR's impact on summarization** using Chart2Text with standard NLG metrics.

## Removed Points

The following points from the reviews are excluded or modified from the main review:

- **"Reproducibility concern about GPT-3.5 prompts not being provided"** — The paper states that SimChart9K and checkpoints will be released, which addresses the primary reproducibility concern. The exact prompts are a secondary implementation detail.
- **"Missing related works"** — Cannot be confirmed without external knowledge; per instructions this is not included.
- **Strength: "Extensive evaluation across four downstream tasks"** — Conflicts with the verified weakness that two of the four tasks lack quantitative evaluation. Dropped as overstated.
- **"Table 1 provides no quantitative comparison"** — Table 1 is a *task-level summary* table, not an experimental results table. This is by design; the quantitative comparison appears in Tables 2-7.
- **"One-size-fits-all suggestion to evaluate on more chart types"** — While relevant, the paper makes reasonable progress on the types it does evaluate. Scaled to a minor weakness above.
- **"The 'generalizability study' only shows more data helps"** — This ignores that jointly training on multiple datasets (ChartQA+PlotQA+Chart2Text) and measuring cross-domain transfer is indeed a meaningful generalizability test.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a consistent tension: the paper pursues an ambitious unified framework covering perception, QA, summarization, and redrawing, but the experimental validation is uneven, heavily favoring perception (via SCRM) and QA, while leaving key claims about summarization/redrawing and perception competitiveness against baselines unsubstantiated. The most interesting empirical finding — that 20% real data + synthetic data matches 100% real data — is well-supported and deserves attention, but it is not enough to carry the full scope of claims made.

## Suggestions

1. **Add perception baselines.** Compare the CIE component against ChartOCR, ChartReader, and/or Pix2Struct on a standard perception task (e.g., extracting table values from ChartQA or PlotQA images) using a shared metric such as relative numerical error or cell-value exact match.
2. **Quantitatively evaluate summarization.** Use Chart2Text's existing annotations with standard NLG metrics (ROUGE-L, BLEU, BERTScore) to demonstrate STR's benefit for summarization, supporting the unified paradigm claim.
3. **Justify or ablate SCRM thresholds.** Provide sensitivity analysis showing how results change across a range of threshold values, or cite prior work motivating the chosen values.

---

## Score and Decision

Originality: The STR formulation and the LLM-based self-inspection data pipeline are creative. SCRM is a reasonable but incremental contribution.

Importance: Reducing annotation cost for chart understanding is practically important. The 20% real data finding is impactful if it holds across more settings.

Claims support: Partially. The label-efficiency claim is well-supported. The unified paradigm claim and perception advance claim are under-supported due to missing baselines and incomplete evaluation.

Soundness: The experiments that are present are properly designed, but the gaps (no perception baselines, no quantitative summarization) limit the overall picture.

Clarity: The paper is generally well-written, though the contradiction about Chart2Text's availability is confusing.

Value: The STR representation and the SimChart9K dataset are useful resources, but the current validation is insufficient to fully establish the claimed contributions.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>