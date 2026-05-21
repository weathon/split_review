Now I have all the information needed to write the consolidated review.

## Summary

MOCHA presents a curated resource of 10 multi-subject spatially resolved transcriptomics (SRT) datasets, each claimed to include gene expression, spatial coordinates, H&E images, and expert pathologist domain annotations. The paper enumerates the cohorts in Table 1 and describes standard preprocessing and batch correction pipelines. The intended contribution is to fill a gap in publicly available multi-sample SRT benchmarks with expert annotations.

## Strengths

- **Curated catalog of 10 diverse multi-subject SRT cohorts**: Table 1 enumerates cohorts spanning human and mouse tissues (breast, colorectal, kidney, lung cancer; DLPFC; MOB), two technology platforms (10x Visium, ST), and sample sizes from 3 to 94 subjects. This provides a useful reference for practitioners seeking multi-subject SRT datasets and documents the scope of available public cohorts in one place.

## Weaknesses

### Fatal

- **The dataset is not accessible.** The paper states that "MOCHA is released in formats readily usable with Python and R" but provides no URL, DOI, data availability statement, or description of file formats/directory structure. For a dataset paper, the resource itself *is* the contribution. Without any way to access the data, the contribution cannot be evaluated, reproduced, or used. This alone is sufficient grounds for rejection.

### Major

- **The central claim of expert pathologist annotations is stated but entirely unsubstantiated.** The paper's key differentiating feature (cited in the Abstract, Section 1, and Section 2) is that "each sample is accompanied by spatial domain labels produced by an expert pathologist." However, the paper provides: (a) no description of the annotation protocol (number of pathologists, annotation guidelines, inter-annotator agreement); (b) no figure showing example annotations overlaid on tissue; (c) no discussion of whether annotations were sourced from the original publications or created de novo for MOCHA; (d) no quantification of annotation granularity, quality, or confidence. Section 4 mentions four broad categories (immune, stroma, tumor, normal) but defers details to Supplementary Material. As presented, a reader cannot assess whether these annotations exist, are of usable quality, or add value beyond what is already published with the original studies.

- **No validation of the resource's utility.** A dataset paper should demonstrate that the resource enables something useful. MOCHA provides no benchmark experiments using multi-sample clustering methods (BASS, STAGATE, BayeSMART) on the curated data, no batch effect analyses showing the value of the harmonized resource, and no comparison demonstrating that MOCHA enables analyses that would be difficult with existing repositories. The only analysis is Figure 1, which shows basic descriptive statistics (spot counts, gene counts, sparsity) across cohorts — this does not establish utility. Without a validation use case, the paper is a list of datasets rather than a demonstrated resource.

### Minor

- **No explicit comparison to existing repositories.** The paper cites SORC, Aquila, SODB, STOmicsDB, and SpatialDB, and asserts that "multi-subject datasets with expert-generated spatial annotations remain limited," but never systematically compares what these repositories already offer versus what MOCHA adds. A comparison table would clarify the value proposition.

- **Empty/incomplete sections.** The Author Contributions and Acknowledgments sections are blank placeholders, suggesting incomplete preparation.

- **Annotation category details relegated to missing Supplementary.** The harmonization of four annotation categories (immune, stroma, tumor, normal) across cohorts is described as being "in the Supplementary Material" — this information is central to the paper's claims and should appear in the main text.

### Trivial

None. (Formatting issues noted by the harsh critic are parser artifacts, not author errors.)

## Nice-to-Haves

- Running even a simple benchmark (e.g., using the claimed annotations as ground truth to evaluate ARI of BASS or STAGATE across cohorts) would substantially strengthen the paper.
- A table comparing MOCHA to SORC, Aquila, SODB, STOmicsDB, and SpatialDB across dimensions like multi-subject coverage, annotation availability, and file formats would clarify the contribution.

## Removed Points

These points from the reviewers are removed because they are parser artifacts, factually incorrect, or violate the filtering rules:

1. **"Figure 1 axis labels are garbled"** (RCC_TL8_10x instead of RCC.TLS_10x, DLPC_10x instead of DLPFC_10x): The rendered "TL8" is a PDF font-rendering artifact (S→8). The table in the paper uses correct names (RCC.TLS_10x, DLPFC_10x). Removed per formatting-artifact rule.

2. **"Inconsistent naming conventions"** (BC.HER2+_10x vs BC.TNBC.ST vs MOB.ST): The naming convention is actually systematic — the technology suffix (_10x for Visium, .ST for ST) consistently indicates the platform. Removed as factually incorrect nitpick.

3. **"AA standard pipeline"** (Section 3, last line): This is a PDF parser rendering artifact ("A" duplicated). Removed per formatting-artifact rule.

4. **"Figure caption repeats itself for Figure 2"**: PDF parsing artifact (image placeholder caption extracted alongside text caption). Removed.

5. **Strength about "expert pathologist annotations for every sample"**: This conflicts with a verified weakness (annotations are claimed but not substantiated). Per the rule "when a strength and weakness disagree, the weakness wins," this strength is removed.

6. **Strength about "standardized data organization and format compatibility"**: Claimed but not demonstrated (no data access, no format specification). Removed as unsubstantiated.

7. **Strength about "explicit preprocessing and batch-effect correction pipeline"**: Section 3 describes a generic textbook summary of standard SRT preprocessing (TMM normalization, HVG selection, Harmony batch correction), not a MOCHA-specific contribution. Removed as not a distinctive strength.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the fundamental observation that the paper describes a plan rather than a completed resource — its core claims about annotations and data access are unverifiable from the submitted manuscript.

## Suggestions

1. **Provide data access.** Include a URL or DOI in the paper and describe the directory structure, file formats, and how to load the data in Python and R. Without this, the paper is an abstract proposal.
2. **Demonstrate the annotations.** Show example annotations overlaid on H&E images for at least one sample per cohort. Describe the annotation protocol (who produced them, guidelines used, inter-rater reliability). State clearly whether these are new annotations or repurposed from original publications.
3. **Run a benchmark use case.** Apply a multi-sample clustering method (BASS, STAGATE, or BayeSMART) to several cohorts, report ARI/NMI using the annotations as ground truth, and show that the resource enables meaningful evaluation.
4. **Differentiate from existing repositories.** Create a comparison table showing what MOCHA adds beyond SORC, Aquila, SODB, STOmicsDB, and SpatialDB.

## Score and Decision

**Round 1 (Bracketing):** I queried for similar-quality dataset/benchmark papers across three bands. The strongest comparables from the low band were *ivrit.ai* (avg 2.50, pure dataset paper with data available but missing baselines) and *Explainable Medical Image Clustering* (avg 2.50, dataset + method but poor clarity and no data access). From the low-middle band, *Mineral Fertilizer Dataset* (avg 3.75, dataset with baselines but limited novelty) and *TAROT* (avg 4.33, dataset + method with novel algorithm). MOCHA is substantially weaker than even the 2.50 anchors because it provides no data access and no evidence for its central claim.

**Initial bracket:** 2.0 – 3.0.

**Round 2 (Narrowing):** I pulled additional low-band anchors including *LST-Bench* (avg 2.50, benchmark with experiments but limited novelty) and *DataSciBench* (avg 3.20, benchmark with some evaluation). Even the weakest of these anchors — the *ivrit.ai* dataset (2.50) — had the actual data available under a permissive license and described its collection pipeline. MOCHA fails to provide data access and fails to substantiate its primary selling point (expert annotations), making it strictly weaker.

**Final score: 2.5.** The paper has one genuine factual contribution (the curated cohort list in Table 1), but as a dataset resource submission it is fundamentally incomplete — the data is inaccessible, the main claimed feature (annotations) is unsubstantiated, and utility is not demonstrated. This score positions it below the weakest accepted pure-dataset anchors (typically 5+) and below even the rejected dataset papers that at minimum provided data access and some validation.

MY FINAL SCORE: <score>2.5</score>
MY FINAL DECISION: <decision>Reject</decision>