## Summary
MOCHA is a dataset resource paper presenting a curated collection of 10 publicly available spatially resolved transcriptomics (SRT) datasets, reformatted to a common schema with standardized storage formats for Python/R. The stated differentiating feature is that each sample is paired with expert pathologist spatial domain annotations. The paper also describes standard preprocessing pipelines (normalization, HVG selection, Harmony, Crescendo) and tabulates three existing multi-sample spatial clustering methods.

---

## Strengths

- **Multi-cohort breadth and diversity**: Table 1 documents 10 distinct cohorts spanning breast, colorectal, kidney, lung, brain, and mouse olfactory bulb tissues, two sequencing technologies (10x Visium and ST), and sample counts ranging from 3 to 94, providing a broad surface for evaluating multi-sample SRT methods.
- **Multimodal alignment per sample**: The paper states (Introduction, Section 2) that every sample includes a gene expression matrix, spatial coordinates, and a co-registered H&E image, which is necessary for methods such as BayeSMART that integrate histological information.
- **Standardized data organization**: The resource is released in formats compatible with Python and R, lowering the barrier to adoption.

---

## Weaknesses

### Fatal
*None that are unambiguously fatal from the page as written.*

### Major

- **Annotation provenance is completely absent, undermining the paper's central novelty claim.** The resource is named for "Human Annotation" and the abstract explicitly positions pathologist-derived spatial domain labels as the key differentiator. Yet the paper provides zero information about annotation origin. The selection criteria in Section 2 state: *"our selection criteria required each study to provide… cellular annotations delineated by a pathologist using the corresponding H&E images,"* which strongly implies the annotations originate from the source publications (e.g., Maynard et al. 2021 for DLPFC already provides layer-level expert annotations; Andersson et al. 2021 for BC.HER2+ already includes spatial deconvolution annotations). If MOCHA is re-packaging annotations that already existed in the original papers, the contribution is data harmonization—a legitimate but weaker claim than novel expert annotation. The paper never disambiguates these cases for any of the ten cohorts, making its headline differentiator unverifiable and potentially overstated. There is no mention of annotation protocol, annotator credentials, inter-annotator agreement, or mapping decisions.

- **No experimental results of any kind.** Section 4 tabulates three multi-sample spatial clustering methods (BASS, BayeSMART, STAGATE) but runs none of them. The paper presents zero quantitative outcomes: no ARI, no clustering performance, no domain identification accuracy, no cross-cohort evaluation. A resource paper's essential burden is demonstrating that the resource enables something—even a single-cohort baseline experiment scoring the three listed methods against the expert labels would constitute evidence of evaluation utility. The paper asserts that MOCHA "enables evaluation of multi-sample spatial domain identification methods" (Section 2) but provides nothing to support that assertion.

### Minor

- **MOB.ST conflates technical and biological replication without comment.** Table 1 lists MOB.ST with 1 subject and 12 samples. Twelve samples from a single mouse are spatial or technical replicates, not independent subjects. MOCHA is explicitly motivated by the challenges of *multi-subject* integration (cross-subject variability, batch effects); including a single-subject dataset in that context without any caveat is confusing and could mislead users about which cohorts are appropriate for evaluating inter-subject generalization.

- **Annotation category schema deferred entirely to Supplementary Material.** Section 4 states that the four-category grouping (immune, stroma, tumor, normal) is "described in the Supplementary Material." Given that consistent cross-cohort labels are a core utility of the resource, the body of the paper should at minimum describe how fine-grained per-cohort labels were mapped to these four categories, and whether any mapping is ambiguous or forced for a given cohort.

### Trivial

- **No summary statistics on the annotations themselves.** The paper gives molecular statistics (spots, genes, sparsity) in Figure 1 but provides no per-cohort statistics on spatial domain annotations: number of domain classes, class imbalance, annotation granularity per sample. This information is practically necessary for users selecting cohorts for their experiments.

---

## Nice-to-Haves
- Even a single-cohort, two-method benchmark would strongly demonstrate the resource's evaluation value and should be included in any revision.
- A clear table distinguishing cohorts by their multi-subject biological variability suitability (e.g., flagging MOB.ST as technical replication) would help users make appropriate selections.
- The preprocessing section (Section 3) reads as a textbook overview of general tools; it would be more useful if it indicated which pipeline choices were applied to which MOCHA cohorts and what practical guidance emerged.

---

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic — "Crescendo not validated on MOCHA data"**: The paper describes Crescendo as an alternative batch correction pipeline (Section 3) and mentions that it "can extend" BayesCafe to multi-sample settings. There is no explicit claim that Crescendo was applied to MOCHA in Section 3. However, since the paper doesn't claim to validate any pipeline on MOCHA, this is no worse than the Harmony pipeline description—there is no evidence Harmony was applied beyond the Figure 2 illustration. This point is partially valid but merges into the broader "no experimental results" weakness already captured; raising it separately would inflate the weakness count.

- **Strength Finder — "Standardized evaluation categories for cross-cohort comparison"**: Partially valid, but because the annotation mapping schema is entirely in the Supplementary Material and the provenance of those annotations is unclear, this strength conflicts with a verified Major weakness and is demoted.

- **Harsh Critic — general claim that the field-gap motivation is "asserted rather than demonstrated"**: This is generic scope-creep critique. A resource paper is not required to quantitatively map the entire landscape of existing annotation coverage. Removed as too speculative.

- **Harsh Critic — BC.HER2+ described as including "deconvolution-based spatial annotations"**: The original Andersson et al. paper uses spatial deconvolution and pathologist annotation. The characterization is broadly consistent with what those papers contain. This claim is sufficiently close to accurate that it does not rise to a factual error; however, the broader point about annotation provenance is retained.

---

## Novel Insights
The paper is a data aggregation exercise. Neither reviewer surfaces a genuinely novel methodological observation. The implicit insight—that the field lacks a uniformly formatted, multi-subject SRT resource with paired H&E images and pathologist annotations—is real and likely correct, but it is the paper's own stated motivation, not a reviewer synthesis. The most practically important gap identified in this review is that the annotation provenance question is not merely cosmetic: if the labels come directly from source papers, the MOCHA contribution is format harmonization; if new annotations were commissioned, the contribution is substantially stronger but entirely undemonstrated in the paper. Resolving this would materially change how the community would use and cite the resource.

---

## Suggestions
1. **Add an annotation provenance table**: For each of the 10 cohorts, state explicitly whether annotations are (a) used as-is from the original publication, (b) adapted/re-labeled from original annotations, or (c) newly generated by the MOCHA team. If (c), describe the annotation protocol and include an inter-annotator agreement assessment.
2. **Add a minimal benchmark section**: Run at least two of the three listed methods (e.g., BASS and STAGATE) on two cohorts of different scales, scoring against the expert labels. This directly validates the resource's evaluation use case.
3. **Clarify MOB.ST's role**: Either remove it or add explicit framing distinguishing technical replication cohorts from biological multi-subject cohorts, so users understand what evaluation settings each cohort supports.
4. **Move the annotation category schema to the main paper**: The immune/stroma/tumor/normal grouping—and the per-cohort mapping rationale—belongs in Section 4 or a supplementary table referenced from the main text with enough detail to assess consistency.

---

## Assessment by Axis

- **Originality**: Low-to-moderate. The combination of multi-subject SRT datasets with H&E images is useful, but the datasets themselves are not new, and the annotation novelty is unverified.
- **Importance of Research Question**: Moderate. Multi-sample SRT benchmarking is a genuine need.
- **Claims Well Supported**: Weak. The paper's central claim—expert human annotation—is asserted but not described or evidenced.
- **Soundness of Experiments**: None. No experiments are presented.
- **Clarity of Writing**: Adequate for what is written; but what is written is very sparse.
- **Value to Research Community**: Potentially meaningful if annotation provenance is clarified and the resource is properly characterized, but undemonstrated in this submission.

---

MY FINAL SCORE: <score>2.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>2</originality>
<importance>3</importance>
<claims_supported>1</claims_supported>
<soundness>1</soundness>
<clarity>2</clarity>
<community_value>2</community_value>
</subscores>