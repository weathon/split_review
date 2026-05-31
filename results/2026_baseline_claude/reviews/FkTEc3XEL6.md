## Summary

MOCHA (Multi-sample Omics Cohorts with Human Annotation) is a curated resource of 10 spatially resolved transcriptomics (SRT) cohorts spanning cancer and non-cancer tissues, assembled to support development and evaluation of multi-sample SRT methods. The resource pairs gene expression matrices, spatial coordinates, and co-registered H&E images with expert pathologist annotations, and standardizes storage formats compatible with Python and R. The paper also reviews standard preprocessing/batch-effect-correction pipelines and catalogs existing multi-sample spatial clustering methods.

---

## Strengths

- **Addresses a genuine gap.** Multi-subject SRT datasets with expert pathologist annotations are notably scarce in the literature, and the motivation is clearly supported by the review of existing repositories (SORC, Aquila, SODB, STOmicsDB, SpatialDB) that do not provide per-sample domain labels.
- **Scale and diversity.** The 10 cohorts span human and mouse tissues, two sequencing platforms (10x Visium, ST), multiple cancer indications and a neurological region (DLPFC), with sample counts ranging from 3 (KC.TLS) to 94 (BC.TNBC), offering method developers a variety of test scenarios.
- **Practical metadata and preprocessing guidance.** Table 1 summarizes cohort-level statistics; Figure 1 characterizes spot counts, gene counts, and sparsity; and Section 3 concisely covers normalization, HVG selection, and both Harmony- and Crescendo-based batch correction pipelines.

---

## Weaknesses

### Fatal

- **No benchmark results.** A dataset/benchmark paper's primary obligation is to demonstrate the dataset's utility by evaluating methods on it. Section 4 names three methods (BayeSMART, BASS, STAGATE) and describes them in Table 2, but **no quantitative results are reported on any MOCHA cohort**. There is no accuracy, ARI, NMI, or any other metric comparing methods across samples. Without this, the paper cannot fulfill its stated purpose of providing an "evaluation resource."

### Major

- **All data is repackaged from existing public sources.** Every cohort in Table 1 is drawn from prior publications (Andersson et al. 2021; Coutant et al. 2023; Wu et al. 2021; etc.). The paper does not describe any new data collection, any new annotation effort, or any new pathologist labeling beyond grouping pre-existing annotations into the four broad categories (immune, stroma, tumor, normal). This severely limits the novelty of the contribution.
- **Annotation origin and quality are unclear.** It is ambiguous whether the pathologist annotations came directly from each original study or were generated fresh for MOCHA. No inter-annotator agreement, annotation protocol, or quality-control metrics are provided, making it impossible to assess annotation reliability.
- **Coarse harmonization loses information.** Collapsing diverse, study-specific annotations into only four categories (immune, stroma, tumor, normal) discards the fine-grained spatial structure that would make the benchmark genuinely challenging. The paper does not justify this choice or examine how it affects method evaluation.
- **Dataset accessibility is not demonstrated.** No repository URL, DOI, license, or download mechanism is provided in the paper. For a dataset contribution, reproducibility fundamentally requires knowing where and how to access the data.

### Minor

- The cohort size is very uneven and skewed toward small samples; cohorts with 3–5 samples (KC.TLS, LC.TLS) offer limited power for evaluating multi-sample methods.
- The differentiation from existing repositories (especially STImage-1K4M, which the paper itself cites as a prior art) is stated but not rigorously argued with direct comparison of what MOCHA uniquely provides.

### Trivial

None worth recording.

---

## Nice-to-Haves

- A held-out test split with standardized evaluation metrics (ARI, NMI, clustering accuracy) using the included methods would make MOCHA immediately usable as a benchmark rather than just a data repository.
- Per-sample annotation histograms (number of spots per domain, domain imbalance ratio) would help practitioners understand the difficulty of each cohort.

---

## Novel Insights

None beyond the paper's own contributions. The paper does not generate new scientific insights about tissue biology or methodology; it is purely an organizational resource whose value depends on the benchmarking experiments that are absent.

---

## Suggestions

- Run BayeSMART, BASS, and STAGATE (already listed in Table 2) on all MOCHA cohorts and report ARI/NMI against the pathologist labels; this single experiment would substantially validate the benchmark's utility.
- Clarify whether pathologist annotations are newly generated or inherited from source studies, and describe the annotation protocol and any inter-rater reliability metrics.
- Provide an explicit data access URL and license so the community can reproduce the work.
- Consider retaining fine-grained per-cohort annotations rather than (or alongside) the four-category harmonization, to support harder evaluation tasks.

---

## Score and Decision

MOCHA addresses a real and important gap in the SRT computational ecosystem. However, as submitted, the paper lacks the benchmark experiments that would constitute its core contribution; repackages entirely public data with coarse, unexplained label harmonization; omits annotation provenance and quality metrics; and provides no data access information. The result is a position statement for a resource rather than a validated resource paper. These are fundamental deficiencies, not presentation issues.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>