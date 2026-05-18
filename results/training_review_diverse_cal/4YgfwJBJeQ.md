Now I have a thorough understanding of the paper. Let me synthesize the final review after careful cross-verification of all claims.

## Summary

This paper proposes StructChart, a two-stage pipeline for chart understanding that separates perception (extracting chart data into text) from reasoning (answering questions, summarization, redrawing). The main contributions are: (1) Structured Triplet Representations (STR), which reformat linearized CSV into (row-header, column-header, value) triplets to better bridge perception and reasoning; (2) Structuring Chart-oriented Representation Metric (SCRM), a tolerance-aware evaluation metric for chart perception; and (3) SimChart9K, a synthetic chart dataset generated via LLM-based self-inspection to reduce reliance on real annotated data. Experiments show that STR improves downstream QA over standard LCT, and SimChart9K enables competitive perception performance with only 20% real data.

## Strengths

- **STR improves downstream reasoning over LCT.** Table 4 shows that STR + GPT-3.5 outperforms LCT + GPT-3.5 on ChartQA (both human and augmented sets), directly demonstrating that the triplet format helps an LLM reason over extracted chart data. This is the paper's cleanest result.

- **SimChart9K demonstrably boosts perception under low-data regimes.** Tables 5 and 6 show that combining SimChart9K with only 10–20% real data matches (and in some cases exceeds) the perception performance of training on 100% real data. The scaling experiment in Table 3 (0.1K → 9K) further confirms that more synthetic data consistently improves CIE performance.

- **Competitive QA results achieved without proprietary training data.** Table 4 shows StructChart+GPT-3.5 surpasses VL-T5-OCR and Deplot on ChartQA and approaches Matcha, which was trained on a closed-source dataset. This demonstrates the STR + simulation pipeline can match methods with access to large proprietary data.

- **Generalizability across multiple datasets and tasks.** The perception experiments cover ChartQA, PlotQA, and Chart2Text (Tables 2, 6), and the framework handles QA, summarization, and redrawing, showing broader applicability than methods focused solely on QA.

- **The two-stage design enhances interpretability and reusability.** As stated in Section 3.1, the explicit text-level representations (STR/LCT) can serve as pre-training corpus for LLMs and VLMs, a capability end-to-end approaches lack.

## Weaknesses

### Fatal
None.

### Major

- **No external baselines for the chart perception stage (CIE).** The paper introduces CIE as a core component ("Transformer-based Chart-oriented Information Extractor") and the introduction explicitly frames chart perception as a challenge. Yet the perception experiments (Tables 2, 3, 5, 6) only compare different configurations of the proposed method — varying dataset composition, data amounts, etc. — with no comparison against existing perception methods such as ChartOCR (Luo et al., 2021), ChartReader (Rane et al., 2021), or any other chart-data extraction system. ChartOCR and ChartReader are cited in Related Work (Section 2, lines 29–30), establishing their relevance, but they never appear in experimental comparison. This makes it impossible to assess whether CIE advances the state of the art in perception or merely provides an adequate front-end for the STR pipeline. Since the paper's framing identifies "chart perception" as half the contribution, this omission is significant.

### Minor

- **SCRM's claimed necessity is not empirically validated.** The paper argues that existing metrics are inadequate (Section 1, challenge (2)) and proposes SCRM as a solution, but provides no evidence that SCRM captures something meaningful that simpler alternatives (e.g., exact-match accuracy, mean relative error, F1 for entity strings) would miss. The tolerance thresholds (edit distance ≤ 2 vs. 5, relative error ≤ 0.05 vs. 0.1) are stated without justification. The metric design is reasonable, but the claim that it addresses a real evaluation gap remains unsupported. A diagnostic experiment comparing SCRM rankings with downstream QA performance — and showing simpler metrics fail to capture the same signal — would substantiate this contribution.

- **STR is a deterministic reformatting, not a learned transformation.** As described in Section 3.2, the perception stage outputs LCT, and STR is obtained by a fixed rule-based restructuring (each CSV cell → row-header, column-header, value triplet). The novelty lies in the *format choice* for downstream reasoning, not in a new modeling capability. The paper's framing as "alleviating the task gap" (Section 1) suggests deeper integration than the actual implementation. This is a valid engineering insight but should be calibrated accordingly.

- **Architecture details for CIE are underspecified.** Section 3.1 mentions a ViT-based encoder-decoder with variable-resolution patch handling and 2D positional embeddings but does not state the ViT variant, number of layers, patch size, sequence length, or training hyperparameters (learning rate, batch size, optimizer, epochs). These are standard specifications for reproducibility.

- **Dataset preparation is not described.** The paper uses ChartQA, PlotQA, and Chart2Text for perception training, which come with different annotation formats. No description is given of how these were converted to the LCT format used for training and evaluation, or whether any filtering/re-sampling was applied.

- **No error bars or multiple-run analysis for GPT-3.5 results.** The QA evaluation uses GPT-3.5 in a one-shot setting (line 184), but GPT-3.5 outputs are non-deterministic. Single-run results without variance estimates weaken the reliability of the comparisons in Table 4.

- **Summarization and redrawing results are purely qualitative.** The paper acknowledges this limitation (line 196: "due to the lack of public datasets and annotations, it is difficult to provide quantitative results"), which is fair, but the qualitative demonstrations are too limited to serve as convincing evidence for these claimed capabilities.

- **The self-inspection loop's cost and reliability are unreported.** Section 3.3 describes a mechanism that iteratively skips non-executable code until success, but no statistics are given on how many attempts are typically needed or how often generation fails outright.

### Trivial

- The section title "Achieving 100% Performance by Only 20% Real Data" could be misread as claiming perfect perception, whereas the text correctly clarifies it means matching the performance of full-set *training* (line 171). The title is catchy but ambiguous.

## Nice-to-Haves

- A diagnostic experiment showing that SCRM rankings of perception models correlate with downstream QA performance, and that simpler metrics (e.g., mean relative error) fail to capture that correlation, would turn the SCRM contribution from plausible to empirically grounded.

- Training the perception model to output STR directly (instead of LCT + rule-based conversion) and measuring whether that improves perception accuracy or downstream QA would provide a stronger test of the STR representation's value.

## Removed Points

None. All criticized points were verified against the paper and found to be substantively correct. No points were removed as factually wrong, strawman arguments, parser artifacts, or scope-creep demands.

## Novel Insights

A genuinely interesting finding that emerges across both the strengths and weaknesses is the asymmetry in the paper's empirical strategy: the perception module (CIE) is evaluated only through internal ablations, yet the downstream reasoning results (which depend on CIE's output) outperform external baselines when paired with STR. This suggests that the STR representation itself may compensate for potential weaknesses in the perception module — the format choice matters at least as much as the extraction accuracy. If validated further (e.g., by feeding ground-truth tables vs. CIE-extracted STR into the same LLM), this could point to the broader insight that for chart understanding, *how* extracted data is presented to a reasoner (structured triplets vs. flat CSV) may be more impactful than marginal gains in perception accuracy. The paper hints at this but never isolates the effect.

## Suggestions

1. **Add perception baselines.** The single highest-leverage improvement is to compare CIE against ChartOCR, ChartReader, or Deplot's internal perception on a standard extraction task (e.g., reconstructing the underlying data table from chart images). This directly validates the perception contribution and makes the downstream results more interpretable.

2. **Disambiguate SCRM reporting.** Clarify which SCRM indicator (Precision@fixed IoU threshold vs. mPrecision) is used in each table, and state the chosen IoU_thr and tolerance settings. Currently the text alternates between "SCRM" and "mPrecision" without explaining whether these refer to the same or different indicators.

3. **Provide architectural specifications.** Report the ViT variant, number of layers, patch size, sequence length, and training hyperparameters (learning rate, batch size, optimizer, epochs) for reproducibility.

## Score and Decision

The paper tackles a well-motivated problem and provides several useful components (STR, SimChart9K, SCRM) with internal evidence supporting their individual value. The STR → improved reasoning result (Table 4) and the SimChart9K → reduced data dependence (Tables 5, 6) are credible contributions. However, the absence of external baselines for the perception stage is a significant gap that prevents assessment of whether CIE advances the state of the art — a gap that matters because chart perception is presented as half the paper's contribution. Combined with the unvalidated necessity of SCRM and underspecified architectural details, the paper is not yet ready for acceptance, but has a clear and achievable revision path.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>