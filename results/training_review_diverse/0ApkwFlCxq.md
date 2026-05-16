Now I have thorough understanding of the paper and the reviews. Let me compile my final review.

---

## Summary

ComputAgeBench proposes the first systematic, open-access benchmark for evaluating blood-based epigenetic aging clocks. It collects and harmonizes 66 public DNA methylation datasets covering 19 aging-accelerating conditions across 9 disease classes, defines four standardized evaluation tasks (AA2, AA1, chronological age accuracy, prediction bias) plus a cumulative score, and tests 13 published clock models. The paper is a benchmark contribution — it does not propose a new method, and its value lies in the quality of its dataset harmonization, evaluation methodology, and fairness of comparisons.

## Strengths

1. **First systematic, large-scale benchmark for epigenetic aging clocks.** The paper fills a genuine gap: "no systematic open access benchmark… has been proposed to date" (Section 2.2). ComputAgeBench's collection of 66 datasets across 19 conditions (Section 3.3) is far more comprehensive than prior single-disease or small-scale comparisons (e.g., Porter et al. 2021; Ying et al. 2024).

2. **Principled, evidence-based criteria for selecting aging-accelerating conditions.** The three AAC criteria (decreased life expectancy, chronic, systemic; Section 3.1) are clearly defined and go beyond ad-hoc selection in prior work. Population-based evidence for each condition is cited (Table A3), ensuring reproducibility and clinical relevance.

3. **Composite benchmarking score that addresses known pitfalls.** The cumulative score (Section 3.6, Eq. 2) explicitly penalizes the AA1 task score by the magnitude of positive prediction bias (Med(Δ) on HC). This mitigates the known issue that first-generation clocks with high chronological age accuracy may fail to detect acceleration while second-generation clocks may appear strong in AA1 due to systemic bias — a problem prior ad-hoc comparisons did not address.

4. **Comprehensive evaluation with 13 diverse clock models across four tasks.** The benchmark tests both first-generation (HorvathV1, Hannum, etc.) and second-generation clocks (PhenoAge, GrimAge) using tasks that measure relative acceleration (AA2), absolute acceleration (AA1), age prediction accuracy, and systematic bias (Section 3.5, Table 1).

5. **Open-access and harmonized data with clear reproducibility commitment.** All datasets are from GEO with open access, no data access requests required (Section 3.2). The paper provides a Google Colab notebook and promises code/dataset repositories after review (Section 7), with metadata harmonization described (Section 3.3).

## Weaknesses

### Fatal
None.

### Major

1. **Unsubstantiated claim of no data leakage between clock training sets and benchmark datasets.** Section 3.4 states "we also ensured that no data in the benchmark was used to train any of the selected clocks," but provides no verification methodology, no list of GEO IDs used in each clock's original training, and no analysis of overlap. This is critical because several evaluated clocks (especially Horvath's multi-tissue clock and its variants) were trained on large compilations of public GEO data spanning many years. If overlap exists, performance results could be inflated and comparisons unreliable. The paper should either: (a) provide a direct verification (e.g., listing the GEO series or sample IDs used in each clock's training and confirming no overlap), or (b) acknowledge that overlap cannot be fully ruled out and discuss how this might affect the results. Without this, the core benchmarking results (Table 1, Figure 3E-F) rest on an assumption that may be false.

2. **AAC assumption not critically examined.** The three criteria (decreased LE, chronic, systemic) are reasonable, but the paper treats all 19 included conditions as equally valid proxies for accelerated *biological aging*. Some conditions (e.g., HIV) increase mortality through immunodeficiency and comorbidities, and evidence that they accelerate the intrinsic aging process per se is mixed. The benchmark's logic depends on the assumption that failing to detect a clock difference (or detecting one) can be interpreted as a property of the clock. If some conditions do not accelerate aging in the biologically relevant sense, interpreting clock successes/failures becomes ambiguous. The paper should discuss this limitation and consider a sensitivity analysis excluding conditions with weaker evidence for aging acceleration to test whether rankings are robust.

### Minor

1. **Known-groups validity vs. property validation framing could be more precise.** The paper defines four properties of biological age (Section 1), then claims to "validate the 1st and the 2nd properties in epigenetic aging clocks" (line 32). What the benchmark actually does is test whether *specific clock predictions* can distinguish AAC from HC cohorts — i.e., known-groups validity of the clocks, not direct validation of the latent BA construct. A clock could fail this test due to measurement noise or tissue specificity even if BA is truly accelerated; conversely, it could pass due to confounding. The paper's framing is not wrong (it does test whether clocks satisfy property 2), but it risks overstatement. Explicitly framing the benchmark as testing *known-groups validity* using AACs as proxies would align claims more precisely with the evidence.

2. **AA1 batch-effect sensitivity not fully mitigated.** The AA1 task (one-sample test that Δ > 0 in AAC cohorts) lacks within-study controls. The paper acknowledges AA1 is less rigorous (Section 3.5) and penalizes global positive bias in the cumulative score, but this global bias measure may not capture dataset-specific technical offsets. AA1 scores could be inflated by batch effects that happen to align with the test's direction in particular datasets. The paper should discuss this limitation more explicitly and consider reporting results with and without per-dataset normalization.

3. **No confidence intervals or variance reported for benchmark metrics.** Table 1 presents Med(|Δ|), Med(Δ), AA2, AA1, and cumulative score as point estimates without confidence intervals or measures of variance across datasets. Since the number of datasets per condition varies, scores may be sensitive to condition class balance. Reporting variability (e.g., bootstrap confidence intervals for the cumulative score, or per-dataset effect sizes) would strengthen the reliability of model comparisons.

4. **"Some datasets were evaluated incorrectly by all models" — unquantified.** The paper mentions this observation (Section 5) and offers plausible explanations, but does not quantify how many datasets, which conditions, or the magnitude of failure. This would strengthen the claim and enable comparisons with future benchmarks.

5. **Missing CpG imputation impact not reported.** The paper imputes missing beta values using gold-standard means from SeSAMe (Section 3.4), but does not report how many CpGs per clock were missing across datasets, or how imputation affects predictions. This is relevant because different clocks use different CpG sets, and some may not be covered by all microarray platforms.

### Trivial
- The sample-size thresholds (10 per dataset, 5 AAC per dataset) are stated without power analysis justification.
- The AAC condition table with evidence is in the appendix; having it in the main text would improve readability, but citing the appendix is standard practice.

## Nice-to-Haves
- Per-dataset bias distributions (boxplot across HC samples) would make the heterogeneity visible that the cumulative score averages over.
- A sensitivity analysis excluding conditions with weaker evidence for aging acceleration (e.g., HIV, specific metabolic conditions) would test robustness of the rankings.
- Reporting AA2 and AA1 with effect sizes (not just significance flags) would allow readers to assess the magnitude of acceleration detection, not just binary pass/fail.

## Removed Points

These points were removed per guidelines; treat with caution:

- **Conflation between BA properties and known-groups validity (original Critical Issue 1)**: The paper's statement is more careful than the reviewer implies. Section 3.5 describes testing "aging clock ability to distinguish AAC from healthy control samples" and the abstract says "reliable aging clocks must be able to distinguish between healthy individuals and those with aging-accelerating conditions." The paper tests whether clocks satisfy property 2, which is precisely what a benchmark for clocks should do. The reviewer's philosophical distinction (validating properties of BA vs. known-groups validity of clocks) overstates the problem. The remaining framing suggestion is kept as a Minor weakness above.
- **"comprehensive benchmarking...can resolve the controversy" is overconfident**: The paper says "comprehensive benchmarking of aging clocks can resolve the controversy regarding their robustness and utility" — this is a reasonable statement about what a benchmark *can* contribute, not a claim of single-handed resolution.
- **Missing related works**: Not included per policy — no external sources to confirm existence.
- **Formatting/presentation nitpicks**: Removed per policy (parser artifacts).
- **Appendix content requests framed as missing**: The paper references appendix content explicitly; the appendix exists in the original submission.

## Novel Insights

Beyond the paper's own contributions, the key novel insight from the reviews is the asymmetry between the paper's *claim* of being a benchmark for validating properties of biological age versus its actual methodology of known-groups validation. This tension is present in many biomarker papers but is particularly acute here because the benchmark explicitly discusses BA's latent, unmeasurable nature. The suggestion to frame the contribution more precisely around known-groups validity would not weaken the paper — it would strengthen it by aligning claims more tightly with the evidence, making the benchmark harder to dismiss on philosophical grounds. Additionally, the data leakage concern highlights a systemic vulnerability in retrospective benchmarking of widely-used models: the community should establish norms for verifying training/benchmark separation when the training data are public but their exact composition is poorly documented.

## Suggestions

1. **Highest priority**: Provide explicit verification of no data leakage — list the training data sources for each evaluated clock (or at least the major ones like Horvath's multi-tissue clock) and confirm none of the 66 benchmark datasets overlap. If verification is impossible for some clocks, transparently acknowledge the limitation and discuss the directional impact on results.
2. Rephrase the benchmark's purpose from "validating properties of BA" to "evaluating known-groups validity of clocks using a pre-specified AAC panel" to align claims with methodology.
3. Add a sensitivity analysis excluding conditions with the weakest evidence for aging acceleration to test ranking robustness.
4. Report confidence intervals or bootstrap estimates for the cumulative score and key per-dataset effect sizes.
5. Quantify the "some datasets evaluated incorrectly by all models" claim with specific counts and conditions.

## Score and Decision

The paper makes a significant and timely contribution — a systematic, large-scale benchmark for epigenetic aging clocks has been clearly missing from the field, and the dataset harmonization, AAC criteria, and cumulative score are well-conceived. The weaknesses identified are real but addressable: the data leakage concern is the most serious and must be verified, but it is an evidential gap rather than a structural flaw. The other issues (framing precision, batch effects, variance reporting) are standard matters of rigor that strengthen the paper without requiring redefinition of the contribution. The paper is a solid contribution that, with the suggested revisions, would be a valuable resource for the aging clock community.

**Score**: 7.0 / 10

**Decision**: Accept

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>