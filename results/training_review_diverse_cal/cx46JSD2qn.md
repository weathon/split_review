Now I have all the information needed to write a thorough, verified review.

## Summary

This paper presents ChiPBench, a benchmark for evaluating AI-based chip placement algorithms using end-to-end PPA (performance, power, area) metrics rather than intermediate surrogate metrics like MacroHPWL. The benchmark includes 20 circuits from diverse domains, compiled from Verilog through a full OpenROAD flow, and provides the necessary physical implementation kits for end-to-end evaluation. The authors evaluate six state-of-the-art AI placement algorithms spanning BBO, analytical, and RL methods, finding that strong intermediate metrics do not reliably translate to strong final PPA outcomes.

## Strengths

- **Full end-to-end evaluation pipeline using a completely open-source toolchain**: The paper constructs a reproducible workflow from Verilog through placement, CTS, and routing using OpenROAD (Sections 4.2, 6.2). This enables measurement of actual PPA metrics (WNS, TNS, power, area) rather than just surrogate metrics, directly supporting the paper's central claim about misalignment. The choice of fully open-source tools is a practical asset for the AI community.

- **Quantitative correlation analysis between intermediate and final metrics**: Section 7.2 computes Pearson correlations among MacroHPWL, HPWL, Wirelength, WNS, TNS, and other metrics (Figure 4). The finding that MacroHPWL has only weak correlation with Wirelength and other PPA metrics, while HPWL correlates strongly with actual Wirelength, provides concrete evidence that optimizing intermediate surrogates does not guarantee end-to-end improvement.

- **Diverse and realistic dataset enabling meaningful evaluation**: The benchmark includes 20 circuits from CPU, GPU, network interfaces, and microcontrollers, with cell counts from hundreds to nearly one million (Table 1, lines 169–189). Unlike prior datasets (ISPD2005, ICCAD2015) that lack necessary files for full EDA flow execution, ChiPBench preserves timing constraints, library files, and LEF files (Table comparison, lines 72–86).

- **Detailed case study illustrating root causes of misalignment**: Section 8.3 analyzes the ariane133 design (Table 4, lines 459–479), showing that AutoDMP reduces wirelength and area but worsens timing significantly because fewer buffers are added during timing repair. This concrete example supports why intermediate optimization can trade off one PPA dimension for another.

- **Comprehensive evaluation spanning multiple algorithmic families**: Six placement algorithms from three categories (BBO, analytical, RL) are assessed under a unified framework (Section 5), strengthening the conclusion that the misalignment issue is pervasive rather than method-specific.

## Weaknesses

### Fatal
None.

### Major

- **No repeated runs or error metrics reported for any experiment.** Every result in Tables 1, 2, and 3 is presented as a single scalar value with no standard deviation, confidence interval, or seed information. Several evaluated algorithms (SA, MaskPlace, ChiPFormer) are stochastic by design. A single run cannot distinguish systematic advantage from sampling noise, especially when many reported differences are on the order of 1–5% (e.g., Power values near 1.01–1.02, Area near 0.98–1.01). For a benchmark that aims to establish reliable findings about the relationship between intermediate metrics and final PPA, the absence of any variance reporting weakens the evidentiary foundation of the central empirical claims.

### Minor

- **Overstated claim about PPA results.** The paper states that "even if intermediate metric of a single-point algorithm is dominant, while the final PPA results are unsatisfactory" (Abstract, line 11). However, Table 1 shows counterexamples: MaskPlace achieves TNS of 0.978 and NVP of 0.903 (both *better* than OpenROAD's 1.000), and ChiPFormer achieves Area of 0.981. These are meaningful PPA improvements achieved despite (or in MaskPlace's case, even with poor) intermediate metrics. The paper would be more credible if it acknowledged these exceptions and discussed under what conditions intermediate metrics do or do not align with final PPA.

- **LEF/DEF ↔ Bookshelf conversion is not validated.** Section 6.3 (lines 321–324) describes converting LEF/DEF files to Bookshelf format for AI placement algorithms and back to DEF afterward, but provides no validation that this round-trip preserves placement equivalence. Conversion could introduce errors (loss of pin geometry, layer information, or technology constraints) that systematically disadvantage AI methods relative to the native OpenROAD flow (which operates directly on LEF/DEF). Without validation, the benchmark tests the combination of the placement algorithm *plus* the conversion pipeline, not the placement algorithm alone.

- **Correlation analysis lacks explicit statistics.** Section 7.2 reports that "MacroHPWL only has a weak correlation with the Wirelength" and that "HPWL shows a very strong positive correlation with actual Wirelength," but the actual Pearson *r* values and p-values are not reported in the text or figure caption. The reader cannot evaluate how weak "weak" is. Additionally, many designs in the dataset have zero macros (Table 1), substantially reducing the usable sample for MacroHPWL-based correlations. Reporting explicit coefficients with significance levels would strengthen the analysis.

- **Hyperparameter tuning is not addressed.** The paper treats each AI method as a black box without stating whether hyperparameters were tuned on a held-out design or whether default settings were used (Section 6.3, line 320). A poorly tuned method may underperform for reasons unrelated to macro placement quality. A brief discussion of the tuning protocol (or the lack thereof) is needed for fairness.

### Trivial

- **Normalization in Tables 1 and 2 hides absolute scale.** All metrics are normalized to OpenROAD = 1.000, making it impossible to assess whether a 2% regression is practically significant. Table 3 (the ariane133 case study) partially addresses this by providing absolute values, but the main tables lack this context.

- **Licensing/distribution status of dataset components is not stated.** While the paper claims the dataset is "fully open source" (line 44), it does not specify whether all design kits (Liberty files, LEF files) are distributable or whether some were generated with non-redistributable tools. A brief statement on licensing would strengthen reusability.

## Nice-to-Haves

- Report Pearson and Spearman correlation coefficients (with p-values) for MacroHPWL vs. each PPA metric across macro-containing designs.
- Add a simple random macro placement baseline to calibrate how much of the PPA gap reflects optimization quality vs. fundamental limitations of AI methods' objectives.
- Report computational cost (GPU hours, total flow time) for each algorithm — relevant for a benchmark aiming to bridge to industry.
- Add a validation experiment for the LEF/DEF ↔ Bookshelf conversion: run OpenROAD's native macro placer, convert output to Bookshelf and back, then measure whether PPA changes.

## Removed Points

These points are flagged to be removed; treat them with caution:

- "The OpenROAD default flow may have been co-designed with its own macro placer, creating an unfair advantage" — This is speculative; the paper's purpose is to compare AI methods against a standard baseline, and the OpenROAD flow is the natural baseline for an open-source benchmark. There is no evidence of intentional "co-design" advantage beyond normal tool integration.
- "Runtime analysis not reported" — Moved to Nice-to-Haves as it is a reasonable addition but not a core flaw for a benchmark paper focused on PPA.
- "Random macro placement baseline not included" — Moved to Nice-to-Haves as it would be informative but is not required for the paper's validity.
- "Supplemental table with absolute values" — Moved to Nice-to-Haves; the case study (Table 3) partially addresses this.

## Novel Insights

None beyond the paper's own contributions. The Harsh Critic's observation that some AI methods (MaskPlace on TNS/NVP, ChiPFormer on Area) actually improve PPA is a genuine tension with the paper's framing, but the paper's data itself reveals this — it is a discrepancy between the paper's rhetoric and its own evidence, not a novel insight beyond what the paper already contains.

## Suggestions

1. **Run every algorithm at least 5 times with different random seeds and report mean ± std for all metrics.** This is the single highest-leverage improvement. Without it, the benchmark cannot serve as a fully trustworthy reference for the relationship between intermediate and final metrics.
2. **Validate the LEF/DEF ↔ Bookshelf conversion.** Run the OpenROAD native macro placer, convert the output to Bookshelf and back, and measure whether PPA changes. If conversion noise exists, report it as a floor for interpreting AI methods' results.
3. **Acknowledge exceptions to the "unsatisfactory PPA" narrative.** Discuss cases where AI methods did improve PPA (MaskPlace on TNS/NVP, ChiPFormer on Area) and what those methods did differently. This strengthens analytical depth and provides constructive guidance.
4. **Report explicit correlation coefficients** (Pearson and Spearman) with p-values for the correlation analysis, and state the sample size used for each pairwise correlation.
5. **State the hyperparameter configuration** used for each AI method — whether defaults were used, and if any tuning was performed.

## Score and Decision

The paper addresses an important and timely problem — the gap between intermediate surrogate metrics used by the AI community and the final PPA metrics that matter in practice. The benchmark design (dataset with full physical implementation kits + end-to-end evaluation pipeline via OpenROAD) is a genuine contribution that could benefit the field. The strengths of the dataset scope, open-source reproducibility, and comprehensive algorithmic coverage are real.

However, the experimental evidence has a significant methodological gap: the complete absence of repeated runs and error metrics. For a benchmark paper whose core empirical claims involve ranking methods and assessing correlations, this is a major limitation. The lack of conversion validation and the overstatement of the "unsatisfactory PPA" claim are additional concerns, though addressable.

The paper is a solid benchmark contribution in a well-scoped direction — it does not need to be a different paper to be valuable. Its core contribution (the dataset and evaluation framework) does not hinge on the exact numerical results, but those results would be much more useful with proper statistical grounding.

**Decision: Accept** — The benchmark contribution is real and useful, and the major weakness (no repeated runs) is addressable. The paper should be accepted with the understanding that the authors will address the methodological gaps in the final version. The review recommends a score reflecting a solid but not exceptional contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>