Now I have sufficient calibration data. Let me write the consolidated review.

---

## Summary

MOCHA presents a curated collection of 10 publicly available spatial transcriptomics cohorts (spanning breast cancer, colorectal cancer, kidney/lung/renal cancer, DLPFC, and mouse olfactory bulb) that the authors claim are each paired with expert pathologist-generated spatial domain annotations. The paper also discusses preprocessing pipelines (normalization, batch correction via Harmony) and lists three existing multi-sample spatial clustering methods. The stated purpose is to enable development and evaluation of multi-sample SRT integration methods.

## Strengths

- **Diverse multi-cohort collection.** Table 1 enumerates 10 cohorts spanning multiple tissues (breast, CRC, kidney, lung, DLPFC, MOB), two technology platforms (10x Visium and ST), and two species (human, mouse), with subject counts ranging from 3 to 94. This breadth is appropriate for studying multi-sample integration across biological contexts. Figure 1 provides molecular summary statistics (spots, genes, sparsity) that help characterize each cohort.

- **Clear gap identification.** The paper correctly identifies that existing SRT repositories (SORC, Aquila, SODB, STOmicsDB, SpatialDB) are not specifically designed to provide multi-subject data with expert spatial annotations, which is a real bottleneck for multi-sample method development.

- **Pathologist annotations per sample.** If the claimed annotations are genuine and of high quality, the resource would fill a genuine need — each sample in every cohort is described as having domain labels from an expert pathologist, a feature that existing repositories do not systematically provide for multi-subject collections.

## Weaknesses

### Major

1. **No experimental validation of the resource.** The paper provides zero experiments demonstrating that MOCHA is usable for its intended purpose. There are no benchmark results from any multi-sample clustering method, no agreement metrics comparing predicted domains against the pathologist annotations, no case study showing the resource in use, and no analysis of whether batch correction protocols actually work on these cohorts. A dataset paper must provide evidence that the resource *works* — without it, the paper describes a plan rather than a completed contribution. (Compare to similar dataset papers at ICLR such as ReefNet [2.50 avg], which at minimum included within/cross-source benchmarks.)

2. **Annotation methodology is entirely unspecified.** The paper repeatedly states that samples have "domain annotations from expert pathologists" but provides no information about: number of pathologists per cohort, their qualifications, the annotation protocol (guidelines, software, resolution), inter-annotator agreement, or even the detailed label taxonomy. The only concrete detail is a single sentence in Section 4 about four broad groupings (immune, stroma, tumor, normal), with further details deferred to supplementary material. For a resource whose primary value-add is human annotation, omitting all annotation methodology is a fundamental gap that prevents evaluation of label quality.

3. **No data access, format, or availability information.** The paper claims "standardized data organization, efficient storage formats" and that MOCHA is "released in formats readily usable with Python and R," yet provides no file format specification (e.g., .h5ad, .rds), no repository URL, no DOI, no download instructions, no data dictionary, and no statement on whether data are provided as raw counts or preprocessed. For a resource paper, this makes the contribution impossible to evaluate or use. No code or data availability statement appears anywhere in the paper.

4. **The claimed gap versus existing repositories is asserted, not demonstrated.** The paper mentions SORC, Aquila, SODB, STOmicsDB, and SpatialDB and claims that "multi-subject datasets with expert-generated spatial annotations remain limited" in these resources, but provides no systematic comparison. Are any MOCHA cohorts already present in these repositories? Do they already have annotations? Without a concrete analysis (e.g., a comparison table showing what each existing resource offers and where MOCHA adds value), the claimed novelty is unsubstantiated.

### Minor

- **The MOB cohort is single-subject in a "multi-subject" resource.** MOB (mouse olfactory bulb) has 1 subject and 12 sections. The paper frames itself as a "multi-subject" resource throughout, yet includes a single-subject dataset. This inconsistency should be noted and the paper should clarify how single-subject multi-section data fits into the resource's purpose.

- **Cancer-heavy coverage not discussed as a limitation.** Eight of ten cohorts are cancer-related, with only one normal human tissue (DLPFC) and one mouse brain. The paper does not discuss how this bias might limit method development for non-cancer applications or general tissue types.

- **Sections 3 and 4 read as general tutorials rather than MOCHA-specific content.** Section 3 describes standard preprocessing tools (scran, Seurat, Harmony) without specifying which pipeline MOCHA actually employs or provides. Section 4 lists three existing methods (BayeSMART, BASS, STAGATE) in a single paragraph. These sections do not demonstrate MOCHA-specific protocols or analyses and could be substantially condensed.

### Trivial

- Author Contributions and Acknowledgments sections appear as empty placeholders (only line numbers).

- Figure 2 caption has a typo ("AA standard pipeline").

## Nice-to-Haves

- A comparison table showing what existing repositories (SORC, Aquila, SODB, STOmicsDB, SpatialDB) provide and how MOCHA differs would significantly strengthen the gap argument.
- Even a simple label-distribution summary across cohorts would help establish annotation quality and utility.
- A limitations section discussing coverage (cancer dominance, only two platform types) would improve scientific rigor.

## Removed Points

*These points from the reviewers were removed or demoted per the filtering rules. They are listed here for completeness but should not be considered in the overall evaluation.*

- **"The dataset selection and coverage are not justified"** — The paper states its search strategy and selection criteria (Section 2). The MOB critique is noted above as a Minor weakness, but the broader claim that coverage is "not justified" overstates the issue; the paper documents its curation process.
- **"Section 4 is too brief"** — While brief, Section 4 lists three multi-sample methods and notes the four-category grouping. This is descriptive rather than analytical, but brevity is not a structural flaw per se.
- **"Figure 2 uses simulated data and is not specific to MOCHA"** — The figure caption says it is "illustrated with the KC_TLS_10x cohort." The pipeline is a general illustration of preprocessing, not a claim of novelty, so this is within scope.
- **Various formatting/style nitpicks** from the harsh critic's section-by-section notes and several minor reproducibility concerns — removed per the filtering rules.

## Novel Insights

None beyond the paper's own contributions. The reviews raise structural critiques about validation, documentation, and comparison to existing resources, but do not identify emergent insights about multi-sample SRT analysis that transcend what the paper itself attempts to claim.

## Suggestions

1. **Add at least one benchmark experiment.** Run 2–3 multi-sample clustering methods (e.g., BASS, BayeSMART, STAGATE) on a representative subset of MOCHA cohorts and report quantitative metrics against the pathologist annotations (ARI, NMI, F1 per domain). This would simultaneously validate annotation quality, demonstrate the resource's utility, and identify concrete challenges.

2. **Fully describe the annotation process:** number of pathologists, qualifications, annotation tool/software, label taxonomy, quality control, and inter-annotator agreement statistics for at least one cohort.

3. **Provide concrete data access information:** file format (e.g., .h5ad with spatial coordinates, annotations, and raw counts), hosting platform and DOI, data dictionary, and versioning.

4. **Add a comparison table** mapping existing SRT repositories against the features MOCHA claims to provide (multi-subject cohorts, pathologist annotations, H&E images, etc.) and clarifying overlap.

5. **Remove or substantially condense Sections 3–4** into MOCHA-specific content (e.g., "which preprocessing pipeline does MOCHA provide, and for which cohorts?"), and fill in the placeholder sections.

## Score and Decision

**Calibration Anchors** (all rounds):

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| ReefNet (aY6RcnTH4v) | 2.50 | R2 | Had within/cross-source benchmarks, data release plan, expert verification. MOCHA is weaker. |
| PED-X-Bench (s1H22o72kx) | 2.00 | R2 | Had expert adjudication (κ=0.72), benchmarking experiments, data release. MOCHA is comparable or slightly weaker. |
| RNA Benchmark (OVXvHt9zqG) | 2.50 | R2 | Had 7 tasks, baselines, code, standardized pipeline. MOCHA is weaker. |
| TabPalooza (TJWhvS5JXg) | 1.20 | R2 | Fundamentally broken paper. MOCHA is better structured. |
| GPattern-Bench (WDNmAe2v6O) | 4.00 | R2 | Had benchmarks, baseline results, a method. MOCHA is much weaker. |
| Lead-Lag Benchmark (6tPcQE98ZA) | 3.50 | R2 | Had large-scale datasets, verification, comprehensive benchmarks. MOCHA is much weaker. |
| STAGE (ZGzKckA29U) | 3.00 | R1 | Proposed a method with experiments. MOCHA is weaker. |

**Round 1 Bracket**: 1.5–2.5 (MOCHA falls far below papers with any experimental validation)
**Round 2 Narrowing**: MOCHA is clearly weaker than ReefNet (2.50) and RNA Benchmark (2.50), comparable to PED-X-Bench (2.00), and better structured than the 1.2-level papers. The absence of any validation, any data-access information, and any annotation methodology pushes it to the lower end of the bracket.

**Score: 2.0**
**Decision: Reject**

The idea behind MOCHA — a curated multi-subject SRT resource with expert annotations — is timely and potentially valuable. However, the paper as submitted does not demonstrate that such a resource actually exists in a usable, validated form. It provides no experimental validation, no annotation methodology, no data access information, and no systematic comparison with existing repositories. These are not stylistic shortcomings; they are structural omissions that prevent evaluation of the claimed contribution. A substantially revised version with validation experiments, full annotation documentation, and concrete data availability could be a viable submission.

MY FINAL SCORE: <score>2.0</score>
MY FINAL DECISION: <decision>Reject</decision>