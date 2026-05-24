Now I have a clear picture. Let me finalize the review.

## Summary
MOCHA proposes a curated resource of 10 multi-subject spatially resolved transcriptomics (SRT) cohorts, each paired with expert pathologist-derived spatial domain annotations. The paper aims to fill a gap in multi-sample SRT method development by providing standardized data and annotations for benchmarking. However, the manuscript as written never delivers the promised resource: it provides no empirical validation, no annotation methodology, no comparison to existing databases, and substitutes generic survey material for concrete contribution. The paper reads as a preliminary proposal rather than a completed resource contribution.

## Strengths
- **Addresses a genuine need**: Multi-subject SRT datasets with expert spatial annotations are indeed scarce, and the paper correctly identifies this as a bottleneck for multi-sample integration research. The motivation is well-founded.
- **Reasonable cohort selection**: The 10 cohorts in Table 1 span diverse tissue types, disease contexts, and platforms (10x Visium, ST), with sample sizes ranging from 3 to 94 subjects. Figure 1 documents meaningful variability in spot counts, gene counts, and sparsity across cohorts.

## Weaknesses

### Fatal
- **No empirical validation whatsoever**: The paper claims to provide a resource for developing and evaluating multi-sample SRT methods, yet it contains zero benchmarking experiments, zero case studies, and zero demonstrations that MOCHA enables any computational workflow. For a resource/dataset paper, the complete absence of experimental evidence that the resource is useful is disqualifying. The paper's core contribution is entirely unsubstantiated.
- **The submission is critically incomplete**: The AUTHOR CONTRIBUTIONS and ACKNOWLEDGMENTS sections are empty. The manuscript ends abruptly after Section 4 with no Results section, no Usage Example, no Data Access statement, no Limitations discussion, and no conclusion. Even accounting for a stripped appendix, the core narrative never delivers what the abstract promises. This is not a finished submission — it is a 4-page outline.

### Major
- **Annotation methodology is not described**: The paper's central value proposition rests on "expert pathologist" annotations, yet it provides no information about which pathologists performed the annotations, what guidelines they followed, how disagreements were resolved, or any measure of inter-rater reliability. The selection criteria (line 31-32) state that included studies must "provide... cellular annotations delineated by a pathologist," suggesting these are existing annotations from the original publications. But this is never clarified, and no assessment of annotation quality or consistency across studies is provided. Without this, the reader cannot evaluate whether the annotations are trustworthy or comparable across cohorts.
- **Sections 3 and 4 are generic literature surveys, not MOCHA contributions**: Section 3 (Pre-processing and Batch Effect Correction) catalogs standard tools (scater, scran, Seurat, scanpy, Harmony, Crescendo) without describing any MOCHA-specific protocol, software, or integration. Section 4 (Multi-Sample Spatial Clustering Methods) briefly summarizes three published methods (BayeSMART, BASS, STAGATE). Neither section advances a contribution specific to MOCHA. Together they occupy roughly half the paper's body without adding any original content.
- **No comparison to existing resources**: The introduction mentions SORC, Aquila, SODB, STOmicsDB, and SpatialDB but never explains how MOCHA differs from or improves upon them in measurable terms. The claim that MOCHA fills a gap is asserted (line 19-20) but never demonstrated through a side-by-side comparison of features, annotation types, cohort counts, or formats.
- **Ambiguous scope**: Throughout the manuscript, MOCHA is described alternately as a "database," a "resource," and a provider of "protocols for handling batch effects." It is unclear whether MOCHA is a new database, a benchmark suite, a preprocessing package, or a repackaging of existing public data with added annotations. This ambiguity makes it impossible to evaluate the paper against an appropriate standard for its claimed contribution type.

### Minor
- **Annotation grouping mentioned but not explored**: The one sentence (line 147) noting that pathologist annotations can be collapsed into four categories (immune, stroma, tumor, normal) is the paper's only hint of concrete annotation work. But it is never illustrated with examples, validated across cohorts, or connected to downstream method evaluation. This is a missed opportunity to demonstrate even minimal annotation substance.

### Trivial
- None.

## Nice-to-Haves
- Releasing the data with a permanent identifier (DOI) and clear documentation of file formats (AnnData, h5ad, Zarr, etc.) would make the resource concretely usable.
- Running benchmarking experiments with published multi-sample methods (BayeSMART, BASS, STAGATE) on MOCHA versus existing resources would demonstrate utility.
- Providing even a small-scale illustration of the annotation scheme (e.g., one annotated H&E image per cohort) would substantiate the annotation claims.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **Strength Finder: "Standardized preprocessing and batch-correction protocols"** — REMOVED. Section 3 is a generic literature review of existing methods (scater, Harmony, etc.), not MOCHA-specific protocols. The paper claims to provide "protocols" but delivers a survey.
- **Strength Finder: "Consistent annotation categories across cancer studies"** — REMOVED. This is mentioned in a single sentence (line 147) with no elaboration, examples, or validation. Too thin to count as a demonstrated strength.
- **Strength Finder: "Accessible data formats"** — REMOVED. The abstract claims Python- and R-friendly formats, but no format specification (AnnData? h5ad? Zarr? CSV?) is provided anywhere in the paper.
- **Strength Finder: "Concise summary of existing multi-sample methods"** — REMOVED. Table 2 is a 3-row summary of published methods. This is background, not a contribution of MOCHA.

## Novel Insights
None beyond the paper's own contributions. The observation that expert-annotated multi-subject SRT cohorts are needed is reasonable but not novel — the paper itself cites several existing database efforts and acknowledges that the gap is already recognized in the literature.

## Suggestions
- The single highest-leverage improvement would be to complete the resource before submitting: release the curated data with documentation, provide annotation methodology (pathologist qualifications, guidelines, inter-rater agreement), and run at least one benchmarking experiment demonstrating that the annotations improve multi-sample SRT method evaluation.
- Remove or drastically condense Sections 3 and 4 (the generic surveys) and replace them with material specific to MOCHA: annotation scheme description, data format specification, usage examples, and limitations.
- Add a structured comparison table against existing SRT databases (SORC, Aquila, SODB, etc.) showing what MOCHA uniquely provides.

## Score and Decision

### Calibration anchor comparison (all rounds):

**Round 1 (bracketing):**
- Le823SjZEc.md (3.00) — method paper with experiments. More complete than MOCHA.
- nUpM7egYFd.md (3.40) — LLM+single-cell study with experiments. More complete than MOCHA.
- JQbqaQjV7D.md (3.00) — benchmark with 99K records, experiments with 9+ LLMs. Much more complete.
- 44IKUSdbUD.md (3.00) — method paper with experiments. More complete than MOCHA.
- Uc3kog3O45.md (5.75) — SRT method paper with full experiments. Much stronger.
- VdX9tL3VXH.md (4.50) — foundation model paper with zero-shot evaluation. Much stronger.
- ja4rpheN2n.md (8.00) — strong accept. Not comparable.
- YrycTjllL0.md (9.00) — strong accept, BigCodeBench. Not comparable.

**Initial bracket: 2.0–3.5** — the paper is clearly weaker than all middle-band anchors which have actual experiments.

**Round 2 (narrowing within 1.5–3.5):**
- 44IKUSdbUD.md (3.00) — has experiments with Transformer model. Stronger than MOCHA.
- 2wwPG1wpsu.md (2.50) — LST-Bench: has experiments with 11 models on 14 datasets. Much more complete than MOCHA, yet scored only 2.50.
- nUpM7egYFd.md (3.40) — has experimental investigation. Much stronger.
- aOPTDchLBz.md (2.50) — ivrit.ai Hebrew speech dataset: describes data but has no baselines. Similar in being a resource paper without experiments, but at least provides concrete details about the data (10K hours, speaker diversity, data formats). MOCHA is weaker even than this.
- BltaWJZMeR.md (3.20) — DataSciBench: comprehensive benchmark with pipeline. Much stronger.
- gNoqEdT2wO.md (2.33) — MCIL benchmark: has experiments with baselines. More complete than MOCHA.
- ly10tMV6cD.md (3.25) — Structure-Rich Text benchmark: 2512 QA pairs, experiments with 4 LLMs. Much more complete.

**Narrowed range: 1.5–2.5.** MOCHA is objectively less complete than ivrit.ai (2.50) which at least provides concrete data descriptions and format details, and substantially less complete than LST-Bench (2.50) which has extensive experiments. It is comparable to or slightly weaker than the MCIL benchmark (2.33), which has actual baseline experiments.

MOCHA provides a problem motivation, a list of 10 cohorts, and two sections of generic background — but no experiments, no annotation methodology, no data format specification, no comparison to competitors, and no evidence the resource exists in usable form. The incompleteness is structural. I assign a score of **2.0**.

MY FINAL SCORE: <score>2.0</score>
MY FINAL DECISION: <decision>Reject</decision>