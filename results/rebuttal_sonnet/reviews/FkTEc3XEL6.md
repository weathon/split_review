## Summary

MOCHA is a curated database of ten publicly available spatially resolved transcriptomics (SRT) datasets reformatted into a unified organization with Python/R compatibility, paired with spatial domain labels from pathologist annotations. The resource aims to enable multi-sample SRT method development and evaluation by providing standardized data organization, preprocessing/batch correction protocols, and a catalogue of three existing multi-sample spatial clustering methods (BASS, BayeSMART, STAGATE). The paper is approximately 4–5 pages long and contains no quantitative experimental results.

---

## Rebuttal Assessment

**Weakness: Annotation provenance is entirely unaddressed**
- **Author's response:** Partially address
- **Assessment:** Partially convincing, but overstated. The rebuttal correctly notes that Section 4 describes a four-category harmonization (immune, stroma, tumor, normal) and that this mapping "is annotation curation work beyond passthrough reproduction." Verified: Section 4 does contain the sentence "the detailed pathologist annotations can be grouped into four broad categories: immune, stroma, tumor, and normal. These groupings, described in the Supplementary Material…" This is genuine curation. However, the mapping logic itself is entirely in the supplementary (unavailable in the main paper as submitted), no per-cohort provenance is stated, and no example of how original labels map to the four categories appears anywhere in the main paper. The rebuttal's promise of a "dedicated provenance column to Table 1 in the revision" is a future fix, not current evidence. The rebuttal overstates how much the existing paper addresses the reviewer's concern.
- **Score impact:** Weakness downgraded (from "annotations may be wholly inherited/re-used verbatim" to "annotations are at minimum harmonized into a four-category taxonomy, but provenance remains opaque in the main body")

---

**Weakness: No experimental demonstration of utility**
- **Author's response:** Partially address
- **Assessment:** Partially convincing, but insufficient. The rebuttal claims Figure 2 provides "a proof-of-concept application of Section 3's methodology to MOCHA data." Verified: the paper's Figure 2 caption explicitly reads "A standard pipeline for feature selection with HVGs and batch effect correction using Harmony, illustrated with the KC\_TLS\_10x cohort (Dawo et al., 2023)." The Harmony scatter plots show before/after batch integration on real MOCHA data. This is a genuine, if modest, demonstration that the preprocessing pipeline can be applied. However, Figure 2 shows only qualitative batch alignment plots — there is no evaluation against pathologist labels, no ARI/NMI, and no comparison of methods. It does not demonstrate that the resource enables *method evaluation*, only that the pipeline can be mechanically applied. The rebuttal's proposed addition of an ARI benchmark in revision is a future fix that does not count. The core weakness (no quantitative evaluation of domain identification against expert labels) stands entirely.
- **Score impact:** Weakness downgraded trivially (Figure 2 partially mitigates the "Section 3 is textbook with no MOCHA data" sub-point, but the major concern — no evaluation against pathologist labels — is unchanged)

---

**Weakness: MOB.ST conflates biological and technical replication without comment**
- **Author's response:** Acknowledge
- **Assessment:** Unconvincing as mitigation. The author correctly identifies that MOB.ST has 1 subject and 12 samples and acknowledges the reviewer's concern is valid. The promised fix (a provenance/replication-type column in Table 1) is future work. The current paper offers no qualification distinguishing MOB.ST from multi-subject cohorts.
- **Score impact:** Weakness unchanged

---

**Weakness: Four-category annotation taxonomy deferred entirely to supplementary**
- **Author's response:** Partially address
- **Assessment:** Partially convincing as diagnosis, unconvincing as rebuttal. The rebuttal agrees the mapping logic should appear in the main body and promises to move "a representative mapping table (e.g., for BC.HER2+)" into the main paper in revision. This confirms the reviewer was correct. No fix is present in the current submission.
- **Score impact:** Weakness unchanged

---

**Weakness: Section 3 is a textbook survey without validation on MOCHA data**
- **Author's response:** Partially address
- **Assessment:** Partially convincing. The rebuttal correctly points out that Figure 2 anchors Section 3 to real MOCHA data (KC\_TLS\_10x). This is verified: the figure caption and content confirm a real application of HVG + Harmony. However, the original review's stronger sub-point — no comparative validation of which preprocessing choices perform best, no quantitative metrics — remains entirely unaddressed. The demonstration is qualitative only.
- **Score impact:** Weakness downgraded trivially (Section 3 is not purely textbook; Figure 2 grounds it in real data, but no comparative validation exists)

---

## Strengths

- **Aggregation of 10 diverse SRT cohorts in a standardized format**: Table 1 documents cohorts spanning breast, colorectal, kidney, lung, and brain tissues across both 10x Visium and the original ST platform, ranging from 3 to 94 subjects. Formatting these into common, usable formats is a practical community contribution.
- **Multimodal data alignment per sample**: The paper ensures each sample includes co-registered gene expression, spatial coordinates, and high-resolution H&E image (Section 1 and Figure 2). This benefits methods that integrate histology, such as BayeSMART (Table 2).
- **Concrete preprocessing demonstration on real MOCHA data**: Figure 2 applies HVG selection and Harmony batch correction to the KC\_TLS\_10x cohort with a before/after visualization, confirming the pipeline is applied to actual data rather than being purely hypothetical.

---

## Weaknesses

### Fatal
None — no incorrect proofs or fabricated results.

### Major

- **No quantitative evaluation of domain identification against expert labels.** The paper's central claim is to enable evaluation of multi-sample SRT methods using pathologist annotations. Yet no method (BASS, BayeSMART, or STAGATE) is applied to any MOCHA cohort, and no quantitative metric (ARI, NMI, clustering accuracy) is reported anywhere. Figure 2 shows qualitative batch integration but provides no evaluation against the pathologist labels that are MOCHA's claimed differentiator. A resource paper's obligation is to demonstrate that the resource enables evaluation; this paper does not. The rebuttal acknowledges this as "the paper's most significant limitation" and promises a future benchmark, which does not count.

- **Annotation provenance remains opaque in the main paper.** The paper's name and abstract foreground "human annotation" as the differentiating feature, yet the main body never states which annotations are inherited verbatim from original publications, which are re-mapped, or which (if any) are newly commissioned. The four-category taxonomy exists in the supplementary but no worked example appears in the main paper. Section 2's selection-criteria language is consistent with annotations being entirely inherited from original publications. The rebuttal acknowledges this and promises a provenance column in revision — a future fix that does not resolve the current paper.

### Minor

- **MOB.ST conflates biological and technical replication without comment.** Table 1 shows MOB.ST has 1 subject with 12 samples. These are spatial/technical replicates, not multi-subject biological variation. No qualification distinguishes this from multi-subject cohorts like BC.TNBC.ST (94 subjects). Acknowledged by authors; unfixed in the current submission.

- **Four-category annotation taxonomy entirely deferred to supplementary.** The cross-cohort mapping logic — central to MOCHA's claimed consistent reference structure — does not appear in the main paper. The rebuttal acknowledges this is a problem and promises a worked example in revision.

### Trivial

- Section 3 surveys standard preprocessing choices (TMM/RLE, HVG, Harmony, Crescendo) with only a qualitative Figure 2 as grounding; no comparative validation of which choices perform best for which cohort types is provided.

---

## Nice-to-Haves

- Run at least one method (BASS or STAGATE) on one cohort and report ARI/NMI against pathologist labels — this is the minimum bar for the resource paper's utility claim.
- Add a per-cohort annotation provenance table: which annotations are taken from source publications, which are re-mapped, and which (if any) are newly commissioned.
- Add a column or footnote in Table 1 distinguishing multi-subject cohorts from multi-section technical replicates.
- Move at least one worked mapping example from the supplementary into the main body to illustrate the four-category taxonomy.

---

## Novel Insights

The rebuttal partially clarifies that the annotation contribution is harmonization-and-curation rather than production of new annotations — the four-category mapping across heterogeneous per-cohort label vocabularies is a real but modest curation step. The reviewer's original concern that the annotation claim might be "potentially illusory" is modestly overstated; there is genuine cross-cohort harmonization work. However, this does not change the paper's fundamental problem: the resource's utility as an *evaluation* database — its primary claim — is demonstrated only by a qualitative preprocessing figure, not by any comparison of method predictions against expert domain labels.

---

## Suggestions

1. Add a one-paragraph or table-based annotation provenance statement for each cohort in the main paper, specifying which labels are from source publications and which were re-mapped into MOCHA's four-category taxonomy.
2. Run STAGATE (Python-accessible, no H&E requirement) on one 10x Visium cohort and report ARI against the expert-derived domain labels — this is the minimum demonstration needed for a resource paper.
3. Add a column to Table 1 distinguishing multi-subject from multi-section/technical-replicate cohorts.
4. Move one worked label-mapping example into the main body.

---

## Score and Decision

The rebuttal is largely an acknowledgement of the original weaknesses with promises of future revision. The two major weaknesses are both explicitly acknowledged by the authors and both remain unaddressed in the current submission:

1. No quantitative benchmarking against expert labels — authors say they "plan to address" this in revision.
2. Annotation provenance opaque in the main paper — authors say they "will add" a provenance column in revision.

The one genuinely new information that modestly mitigates the original review is that Figure 2 does apply the preprocessing pipeline to real MOCHA data (KC\_TLS\_10x), which the original review's "textbook survey" characterization partially underweighted. However, this is a qualitative demonstration with no evaluation against the pathologist labels, and it was already present in the paper the reviewer read. The two minor weaknesses (MOB.ST labelling, taxonomy deferral) are acknowledged and unfixed. No promises of revision count.

The original score of 2.5 is appropriate. The rebuttal does not reveal that the original review was unfairly harsh; it confirms the weaknesses. The trivial mitigation of Figure 2 being a real (if qualitative) MOCHA application does not move the needle on a paper that lacks all quantitative evidence of its claimed evaluation utility.

MY FINAL SCORE: <score>2.5</score>
MY FINAL DECISION: <decision>Reject</decision>