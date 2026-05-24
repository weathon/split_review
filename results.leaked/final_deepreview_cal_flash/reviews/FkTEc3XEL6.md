Now I have a thorough understanding of the paper and can assess all claims against the text. Let me write the final consolidated review.

---

## Summary

MOCHA presents a curated collection of 10 publicly available spatial transcriptomics cohorts (spanning breast cancer, colorectal cancer, kidney cancer, lung cancer, DLPFC, and mouse olfactory bulb) with the stated goal of creating a resource for multi-sample SRT method development and evaluation. Each sample is claimed to be paired with expert pathologist spatial domain annotations. The paper provides a summary table of the cohorts, basic molecular profile visualizations, and two survey-style sections on preprocessing pipelines and multi-sample clustering methods.

## Strengths

- **Unique combination of multi-subject SRT data with expert annotations.** The curation targets a genuine gap: existing repositories (SORC, Aquila, SODB, etc.) do not systematically pair multi-subject spatial transcriptomics data with expert pathologist domain labels. Table 1 lists 10 cohorts spanning diverse tissues and technologies, ranging from 3 to 94 subjects, providing a heterogeneous testbed that is not available from any single existing resource.

- **Broad tissue and platform coverage.** The collection includes both human cancers (breast, colorectal, kidney, lung, renal cell carcinoma) and normal tissues (DLPFC, mouse olfactory bulb), profiled on both 10x Visium and ST platforms. Figure 1 quantifies cross-cohort variability in spots, genes, and sparsity, which helps characterize the resource's heterogeneity.

## Weaknesses

### Fatal

- **The dataset is not described with sufficient specificity to be used or evaluated, and its utility is not demonstrated.** For a dataset paper, the core requirement is a well-specified, accessible resource whose value is evident. This paper meets none of those criteria.

  - **No data access information.** The paper contains no repository URL, DOI, data availability statement, or license. Throughout the paper, the dataset is described in future or vague terms ("MOCHA is released in formats readily usable with Python and R and distributed for integration into existing pipelines" — line 27-28), but no actual access mechanism is provided.
  - **No format specification.** The paper never states whether the data is stored as AnnData, Seurat objects, HDF5, CSV files, or any other concrete format. "Efficient storage formats" (line 13) is named but never specified.
  - **No annotation protocol details.** The paper's primary selling point is expert pathologist annotations, yet it gives zero information about the annotation process: how many pathologists, what consensus method, what label categories, inter-rater reliability, or whether annotations are newly produced or simply compiled from the original publications. The selection criteria (line 31-33) required studies with "cellular annotations delineated by a pathologist," suggesting the annotations are pre-existing, but this is never clarified.
  - **No experimental validation.** The paper claims MOCHA supports "developing and evaluating multi-sample SRT methods" (line 13), but it contains zero experiments, baselines, performance metrics, or comparisons. No method is run on the dataset, no ARI/NMI is reported, and no comparison against existing repositories is provided. The reader is given no evidence that the resource functions as claimed.

  These omissions are not refinements—they are the primary content of a dataset paper. Without them, the contribution cannot be assessed, reproduced, or used. This is a fundamental failure to deliver the claimed resource.

### Major

- **Sections 3 (Pre-processing) and 4 (Multi-sample Spatial Clustering Methods) are generic surveys disconnected from MOCHA.** These sections describe standard normalization pipelines (library-size scaling, Harmony batch correction) and list three existing methods (BayeSMART, BASS, STAGATE). They never state which, if any, preprocessing steps were applied to MOCHA, how the listed methods perform on MOCHA, or how MOCHA enables their evaluation. Figure 2 illustrates a pipeline applied to one cohort, but it is presented as a generic workflow rather than a characterization of the resource itself. These sections occupy nearly half the paper's content without advancing the dataset description.

- **Ambiguity about the core contribution.** It is unclear whether MOCHA provides newly produced expert annotations or merely aggregates datasets whose original publications already included pathologist labels. The selection criteria (line 31-33) required "cellular annotations delineated by a pathologist" from the original studies, which implies compilation rather than new annotation. If the latter, the added value is the organization and standardization—but these are neither detailed nor demonstrated. The paper never articulates what work was done to create the resource beyond listing cohort names and sample counts.

- **No comparison with existing repositories.** The introduction mentions SORC, Aquila, SODB, STOmicsDB, and SpatialDB as existing resources but provides no quantitative comparison (e.g., a table showing coverage of multi-subject data, annotation types, sample sizes, or tissue diversity across MOCHA and each existing repository). Such comparison is essential to substantiate the claimed gap.

### Minor

- **Quality control and cohort selection are not explained.** The paper does not discuss whether any samples or spots were excluded during curation, what quality metrics were applied, or whether the reported cohort sizes represent all samples from the original studies or a subset. Figure 1 shows sparsity exceeding 90 % for some cohorts, which could affect downstream method evaluation, but this is not discussed.

- **Batch structure is unspecified.** For cohort-level method development, information about which samples come from the same subject vs. independent subjects, and known batch groupings (sequencing run, slide), is critical. The paper provides only "Subjects" and "Samples" counts in Table 1 without clarifying this structure.

- **The four-category annotation grouping ("immune, stroma, tumor, normal") is mentioned but not applied.** Line 147 states these groupings are "described in the Supplementary Material," but they are not presented or validated in the main text, and it is unclear whether they have been harmonized across cohorts.

### Trivial

- Some cohort names in Figure 1 contain apparent rendering artifacts (e.g., "DLPC_10x" vs. "DLPFC_10x" in Table 1).

## Nice-to-Haves

- A single baseline experiment (e.g., running BASS or STAGATE on the dataset and reporting ARI against expert labels) would have substantially demonstrated the resource's utility and is standard for dataset papers.
- Including a data card or datasheet (per Gebru et al.) covering intended uses, composition, collection process, and limitations would align with community best practices for dataset releases.

## Removed Points

These points were raised by the reviewers but are excluded from the main weaknesses above for the reasons stated:

- **Empty Author Contributions and Acknowledgments (lines 216-218).** The paper is under double-blind review; empty author lists in these sections are standard practice, not a weakness.
- **"The term 'integrates' is ambiguous."** This is a minor phrasing preference that does not affect the paper's substantive evaluation.
- **"No companion software tool described."** The paper claims Python and R compatibility without specifying tools; this is already covered under "no format specification" above.
- **Strength Finder claims about "standardized preprocessing pipeline" and "accessible formats."** These overstated what the paper actually provides. Section 3 describes general pipelines, not MOCHA-specific ones; the formats claim is vague and unsubstantiated.
- **Criticism about missing appendix or proofs.** The parser strips supplementary materials; these may exist in the original submission.
- **Questions about whether cited models/repositories exist.** All cited resources (SORC, Aquila, SODB, etc.) are published and indexed; the hard rules forbid questioning their existence.

## Novel Insights

None beyond the paper's own contribution description. The paper inventories 10 cohorts with basic metadata but offers no analysis, meta-analysis, or biological insight derived from the assembled data.

## Suggestions

1. **Provide data access.** Add a repository URL, DOI, and data availability statement. Specify the exact file format(s) and include a minimal code snippet to load the data.
2. **Clarify the annotation provenance.** State explicitly whether annotations are newly produced or compiled. If compiled, describe any harmonization or standardization performed (e.g., label name mapping). If newly produced, report the annotation protocol, number of pathologists, and inter-rater reliability.
3. **Add at least one baseline evaluation.** Run a standard multi-sample method (BASS, STAGATE, or BayeSMART) on the dataset and report domain identification metrics (ARI, NMI) against the expert labels. This single addition would demonstrate that the resource is functional and useful.
4. **Cut or relocate Sections 3 and 4.** Replace the generic survey content with a detailed description of the dataset: format, access, quality control, batch structure, and a comparison table against existing resources.
5. **Add a limitations section** discussing annotation resolution, technology differences across cohorts, possible annotation errors, and the intended scope of the resource.

## Score and Decision

### Calibration

**Round 1 — Bracketing.** Three calibration queries on SRT dataset/topic papers:
- Low band (<3.5): anchors at 2.50–3.40 (rejected papers with incomplete methodology or missing validation). MOCHA is weaker than these because they at least contain methodological contributions or experiments.
- Middle band (3.5–7.5): anchors at 3.67–6.67. Papers like *BoneMet* (6.00, Accept) provide actual data access, baseline experiments, and detailed descriptions. MOCHA has none of these.
- High band (>7.5): anchors at 8.00 (strong accepted papers). Not comparable.

**Round 1 bracket:** 1.5–3.0.

**Round 2 — Narrowing.** Additional queries in (1.5–4.0) and (4.0–6.5):
- *A Guide to Misinformation Detection Datasets* (3.50): a curation paper that provides baseline experiments, data URLs, and analysis. MOCHA is substantially weaker.
- *Mineral Fertilizer Dataset* (3.75): provides actual data, segmentation masks, and baseline model results. MOCHA lacks all three.
- *COMET* (5.75): includes extensive benchmarking experiments across 17 tasks. MOCHA contains zero experiments.

**Round 2 conclusion:** MOCHA is clearly weaker than all anchors at 3.0+. It is most comparable to the weakest rejected papers (2.5–3.0) but lacks even the core content those papers provide (methods, experiments, or data). The paper is an incomplete proposal for a resource rather than a finished contribution.

**Anchors considered:**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Le823SjZEc (QCA, SRT prediction) | 3.00 | R1 | Has method + experiments; MOCHA has neither |
| 44IKUSdbUD (Gene interaction sampling) | 3.00 | R1 | Has method + experiments; MOCHA has neither |
| YH4M1Tbxfz (BoneMet dataset) | 6.00 | R2 | Full dataset release + baselines; MOCHA has neither |
| C81bqFCmMf (COMET benchmark) | 5.75 | R2 | Extensive benchmarking; MOCHA has zero experiments |
| Jztt1nrjAM (Misinformation datasets) | 3.50 | R2 | Curation + baselines + data URLs; MOCHA has none |
| 6nnWnLK8If (Mineral Fertilizer Dataset) | 3.75 | R2 | Actual data + segmentation + baselines; MOCHA has none |
| nUpM7egYFd (scMPT) | 3.40 | R1 | Method + experiments; more complete than MOCHA |

### Final Assessment

**Originality:** The concept of a curated multi-sample SRT resource with expert annotations addresses a genuine need. However, the paper does not establish that MOCHA adds value beyond the original, independently published datasets it aggregates.

**Importance of the research question:** Facilitating multi-sample SRT method evaluation is important. The paper identifies a real gap.

**Claims well-supported:** No. The central claim — that MOCHA is a useful resource for developing and evaluating methods — is unsupported by any evidence.

**Soundness of experiments:** Not applicable; there are no experiments.

**Clarity of writing:** The paper is clearly written but allocates space poorly, using two sections for generic surveys that do not advance the dataset description.

**Value to the community:** Potentially high if the resource were properly released and validated, but in current form the paper provides no usable artifact.

**Score:** 2.0 — a fundamentally incomplete paper that describes an intention rather than delivering a functional resource. The curation work (cohort identification, Table 1, Figure 1) represents some effort, but the absence of data access, format specification, annotation protocol, and any experimental validation means the paper does not meet the bar for a published dataset contribution.

**Decision:** Reject

MY FINAL SCORE: <score>2.0</score>
MY FINAL DECISION: <decision>Reject</decision>