Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper introduces ComputAgeBench, the first systematic open-access benchmark for validating blood-based epigenetic aging clocks. It harmonizes 66 public DNA methylation datasets covering 19 aging-accelerating conditions across nine disease classes, defines evidence-based criteria for condition and dataset selection, proposes four benchmarking tasks (relative acceleration, absolute acceleration, age prediction accuracy, bias), and evaluates 13 published clock models with a cumulative score that penalizes positive prediction bias. The benchmark reveals that second-generation clocks (PhenoAgeV2, GrimAge variants) outperform first-generation ones, and that no clock reliably detects acceleration in cardiovascular/metabolic conditions.

## Strengths

- **Large-scale, principled dataset harmonization**: The paper aggregates 66 datasets from over 50 studies across nine disease-class categories (Section 3.3, Fig. 2E). This is, to my knowledge, the largest open-access panel assembled specifically for clock benchmarking, directly addressing the lack of standardized validation sets noted in prior work (Section 2.2).

- **Evidence-based criteria for AAC selection**: Three explicit, reproducible criteria (decreased life expectancy, chronic nature, systemic manifestation) are defined for selecting aging-accelerating conditions (Section 3.1, Fig. 2B). This grounds the benchmark in biology rather than ad hoc condition selection, making the methodology reusable and defensible.

- **Multi-task evaluation framework with bias-aware cumulative score**: The four tasks (AA2, AA1, age prediction accuracy, bias) and the cumulative score (Eq. 2) explicitly address the biomarkers paradox — the fact that high chronological age prediction accuracy can mask poor biological age estimation. The bias penalty demonstrably corrects inflated AA1 scores (e.g., GrimAgeV2, Table 1), and the framework differentiates first- from second-generation clocks in interpretable ways.

- **Demonstrated utility through evaluation of 13 published clocks**: The benchmark produces concrete, actionable findings: second-generation clocks (PhenoAgeV2, GrimAge variants) lead on the cumulative score; all clocks fail to detect acceleration in cardiovascular/metabolic diseases (Fig. 3E); and most clocks perform best on immune-mediated conditions, likely reflecting biases in their training data (Section 4). These results generalize prior smaller-scale findings and expose previously unquantified limitations.

- **Reproducibility and open access**: The pipeline is available as a Google Colab notebook, and all data sources are public GEO datasets (Section 7). No data in the benchmark was used to train any of the evaluated clocks (Section 3.4), ensuring no data leakage.

## Weaknesses

### Fatal
None.

### Major

1. **The global bias measure may mask dataset-specific covariate shifts.** The bias task (fourth task) computes a single median Δ across *all* HC samples in the panel. A clock could have opposing positive and negative biases across different datasets that cancel out, yet the AA1 scores for individual datasets could still be misleading. The paper acknowledges covariate shift as a potential confound (Section 5) but does not analyze how much per-dataset bias varies across the panel. The AA1 task is the less rigorous of the two acceleration tasks (the paper says so), but because it is explicitly used to expand coverage to datasets lacking HC samples — exactly the setting where one *cannot* control for dataset-specific bias — this gap is nontrivial. The authors should at minimum report the distribution of per-dataset Med(Δ) for HC samples and discuss whether global bias is a reasonable summary.

2. **Per-dataset results for the AA1 and AA2 tasks are not shown in the main paper.** Figure 3 aggregates scores by condition class, and Table 1 gives cumulative numbers, but the reader cannot see which specific datasets each clock gets right or wrong, or whether a high class-level score is driven by a few datasets. The paper mentions that "some datasets were evaluated incorrectly by all models" (Section 5), but does not name them or analyze why. For a benchmark paper, making per-dataset scores available (at least in supplementary material) is important for transparency, replication, and understanding failure modes. Without this, the claim that most clocks perform best on immune-related conditions remains a qualitative statement.

### Minor

3. **The asymmetric bias penalty in the cumulative score is principled but under-justified.** The formula `max(0, Med(Δ)) / Med(|Δ|)` penalizes only positive bias. This is actually well-motivated: the AA1 task tests H_A: Δ_AAC > 0 (one-sided), so positive bias inflates the score (creating false-positive risk), while negative bias deflates it (already a natural penalty). The critic's concern that negative bias "could produce spurious positive results" is incorrect — negative bias makes positive detection *harder*, not easier. However, the paper does not explicitly argue this rationale, leaving the asymmetry open to interpretation. A brief justification or acknowledgment that a symmetric penalty is a design choice would improve clarity.

4. **No confidence intervals or uncertainty estimates for scores in Table 1.** Given the modest number of datasets per condition class (ranging from ~3 to ~12), the leading ranks could shift with the addition or removal of a few datasets. Bootstrap intervals or similar would help calibrate how much trust to place in the ranking.

5. **The third AAC criterion (systemic manifestation) is operationalized only qualitatively.** The paper provides examples of excluded conditions (bone fractures, some malignancies — Section 3.1) but does not give a systematic procedure. A more explicit decision rule or acknowledgment of the inherent uncertainty would strengthen the methodology.

6. **The single saliva dataset is treated identically to blood datasets without discussion of tissue-specific covariate shifts.** Given that all other datasets are blood-based, combining tissues could introduce additional batch effects. A brief note on why this is reasonable or what checks were performed would help.

### Trivial
None.

## Nice-to-Haves

- Provide per-dataset AA1 and AA2 results (with p-values before and after FDR correction) in a supplementary table, along with dataset characteristics (sample size, condition, platform). This would make the benchmark transparently reusable and enable readers to identify failure patterns.
- Report the distribution of per-dataset median Δ for HC samples to empirically assess whether the global bias measure is adequate or whether dataset-specific bias varies enough to distort AA1 scores.
- Add a brief power analysis showing how sample size per dataset affects the sensitivity of the two-sample and one-sample tests, to help calibrate expectations for small datasets.
- Name and analyze the specific datasets that "all models" get wrong (Section 5) — this could yield concrete insights about whether failures are due to small sample size, strong batch effects, or genuine lack of an aging signal for that condition.

## Removed Points

The following points from the harsh critic were removed after verification against the paper:

- **"The authors do not state reasons for excluding kidney/liver datasets"** — *Removed because the paper explicitly states: "All five dataset selection criteria were met by none of the found kidney- and liver-related AAC datasets" (Section 3.3). The reason is stated: they did not meet the five dataset-selection criteria.*
- **"No mention of train/validation split or data leakage"** — *Removed because the paper states: "we also ensured that no data in the benchmark was used to train any of the selected clocks" (Section 3.4).*
- **"Negative bias could produce spurious positive AA1 results"** — *Removed because this is factually incorrect. The AA1 test is H_A: Δ_AAC > 0. Negative bias (systematic underprediction) makes Δ smaller, reducing statistical power to detect positive acceleration — it cannot produce spurious positives. The asymmetry in the penalty is actually principled.*
- **"AA2 one-sided test should be two-sided"** — *WEAKENED and moved to Minor. The one-sided test is justified because the benchmark is constructed around AACs (aging-accelerating conditions). The alternative hypothesis is directional by design.*
- **Reproducibility concern based on missing implementation details** — *Not applicable; the paper provides a Colab notebook and cites all public data sources.*

## Novel Insights

The two reviewer inputs, read together, reveal a subtle tension in the paper's methodology that is worth articulating: the benchmark is explicitly designed to compensate for the absence of mortality data (which would be the gold standard), but its core innovation — the AA1 task as a means to expand dataset coverage — introduces a reliance on a global bias correction that may be insufficient precisely in the settings where AA1 is most needed (datasets without HC samples where per-dataset covariate shifts cannot be directly measured). This is not a fatal flaw, but it means the AA1 results should be interpreted as the more speculative half of the benchmark, and the paper would benefit from making this caveat more prominent. Conversely, the AA2 task, which is more rigorous because it controls per-dataset shifts via a within-dataset control group, is the more trustworthy signal in the evaluation, and it is encouraging that the cumulative score's ranking aligns with the AA2 ranking (both place PhenoAgeV2 first), lending convergent validity to the overall conclusions.

## Suggestions

1. Provide a supplementary table of per-dataset results (AA1 hits/misses, AA2 hits/misses, per-dataset HC bias, p-values) to improve transparency and reusability.
2. Add a figure or table showing the distribution of per-dataset Med(Δ) for HC samples to empirically justify (or revise) the global bias correction.
3. Explicitly justify the asymmetry of the bias penalty in the main text (i.e., that negative bias naturally penalizes the AA1 score via the one-sided test, while positive bias does not).
4. Add bootstrap confidence intervals for the cumulative scores in Table 1.

## Score and Decision

**Originality**: 7/10 — The benchmark methodology itself is novel in its systematic, evidence-based approach, though individual tasks (AA1, AA2) build on prior work (Porter et al., 2021; Ying et al., 2024).

**Importance**: 8/10 — Addresses a real gap: the absence of standardized validation for epigenetic clocks, which has direct relevance for clinical trial design.

**Claims support**: 7/10 — The main claims are supported, but the lack of per-dataset transparency and the unexamined dataset-specific bias weaken the evidentiary floor for the AA1-based conclusions.

**Soundness**: 7/10 — The experimental design is generally sound. The cumulative score is clever, the AA2 task is rigorous, and the dataset harmonization is careful. The gaps (global bias assumption, no per-dataset results) are fixable but real.

**Clarity**: 8/10 — Well-structured, clear motivation, good figures.

**Value**: 8/10 — The benchmark panel and methodology are likely to be reused by the community.

This is a solid benchmark paper with real contributions. The weaknesses are real but not fatal — they concern transparency and the strength of one component of the methodology, not the overall soundness of the contribution. The paper would benefit from more detailed reporting but does not need a methodological overhaul. I recommend acceptance with the expectation that the authors provide per-dataset results and analyze dataset-specific bias variation in the final version.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>