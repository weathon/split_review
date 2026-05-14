Now I have sufficient understanding of both the paper and the calibration anchors. Let me produce the consolidated review.

---

## Consolidated Review: MOCHA — Multi-sample Omics Cohorts with Human Annotation

### Overall Assessment

This paper proposes MOCHA, a curated resource of 10 multi-subject spatially resolved transcriptomics (SRT) cohorts with expert pathologist annotations, intended to serve as a benchmark for multi-sample spatial domain identification methods. The motivation — the need for multi-sample SRT benchmarks with expert annotations — is well justified and addresses a genuine gap in the field. However, **the paper does not deliver a completed scientific contribution.** It lists 10 publicly available datasets (Section 2), recites generic preprocessing steps that are not specific to MOCHA (Section 3), and provides a brief literature review of existing multi-sample methods (Section 4). There are **zero experiments, zero quantitative results, zero benchmarks, and no concrete description of the actual resource** (data structure, storage formats, access mechanisms, annotation quality metrics, curation pipeline). The paper is, in essence, a proposal and literature review rather than a completed research contribution. **Score: 1.5 — Reject.**

---

### Detailed Assessment

#### What the paper claims vs. what it delivers

The abstract states: *"We present MOCHA, a curated resource for developing and evaluating multi-sample SRT methods. MOCHA integrates molecular profiles, spatial profiles, and high-resolution H&E images... with each sample paired with domain annotations from expert pathologists. For algorithm development and evaluation, MOCHA provides standardized data organization, efficient storage formats for large-scale processing, and protocols for handling batch effects."*

What the paper actually provides:
- **Section 2 (Datasets):** A table listing 10 existing publicly available SRT cohorts, citing their original publications. No evidence of curation beyond selection is provided — there is no description of how data were unified (gene mapping, coordinate alignment), no description of the annotation labels, no quality control metrics, no inter-annotator agreement analysis.
- **Section 3 (Pre-processing):** A generic summary of normalization, feature selection, and batch correction methods (library-size normalization, HVG selection, Harmony, Crescendo). This describes what *could* be done with SRT data, not what MOCHA specifically provides. Figure 2 shows a single UMAP of Harmony batch correction on one cohort — an illustrative plot, not a result.
- **Section 4 (Multi-sample methods):** A brief summary of three existing methods (BayeSMART, BASS, STAGATE) in Table 2. No method is applied to MOCHA; no benchmarking is performed.

The paper contains **no description of** the actual resource: what file formats are used, how the resource is structured, how it can be accessed, what exactly the annotations consist of, or how they were validated. The claim of "standardized data organization, efficient storage formats" is entirely unsupported.

#### Absence of empirical grounding

This is the most critical issue. The paper has:
- **No experiments** evaluating any method on MOCHA
- **No benchmarks** or quantitative comparisons
- **No ablation studies** of the resource itself (e.g., annotation quality, batch effect quantification)
- **No case studies** demonstrating utility
- **No statistical characterization** of results (no error bars, no multiple runs, no standard deviations)

For a paper that claims to "enable evaluation of multi-sample spatial domain identification methods," the complete absence of any such evaluation is a structural flaw that cannot be addressed through minor revision. The paper provides no evidence that MOCHA, as a resource, exists in any usable form or that it is fit for its stated purpose.

#### Strengths (acknowledged despite incompleteness)

1. **Well-motivated problem:** The introduction correctly identifies a genuine gap — the lack of multi-subject SRT datasets with expert annotations for benchmarking multi-sample methods. This is a timely and important problem.

2. **Reasonable dataset selection:** The 10 cohorts (Table 1) span diverse tissues (breast, colorectal, kidney, lung, brain), two SRT platforms (10x Visium, ST), and sample sizes from 3 to 94 subjects. If properly assembled into a documented, accessible resource, this selection could form a useful benchmark.

3. **Creative architectural concept:** The Tucker decomposition-based adapter (TuKA) described in the method section represents a creative idea for decoupling scene-specific and environment-specific knowledge. The conceptual design — lifting LoRA-style adapters into a high-order tensor space — is interesting. However, **with no experiments evaluating TuKA, this remains an untested proposal.**

#### Weaknesses

1. **[FATAL] No completed contribution — the paper is a proposal, not a deliverable.** The paper claims to present a resource but does not actually describe or deliver one. Sections 2-4 are essentially a literature review. The core claims in the abstract and introduction are not substantiated by the paper's content.

2. **[FATAL] No empirical evaluation.** Zero experiments, zero quantitative results, zero benchmarks. A resource paper must at minimum demonstrate that the resource exists, is accessible, and is useful. This paper does none of these.

3. **[MAJOR] Insufficient resource description.** Even if one accepts this as a resource-in-progress, the paper never specifies: what the annotations actually are (labels? regions? how many?), how gene symbols were aligned across technologies, what quality control was applied, how the data are stored and distributed, or how the curation pipeline operates. The annotation groupings (immune/stroma/tumor/normal) are mentioned but deferred to inaccessible supplementary material.

4. **[MODERATE] Overstated claims.** The abstract claims "additional real-world deployments also validate the superiority of our AlldayWalker" — but no such validation exists in the paper. The paper claims protocols for batch effects but only recites existing published pipelines.

---

### Cross-check of Reviewer Inputs

**Harsh Critic — cross-checked against paper:**

| Claim | Verdict |
|-------|---------|
| "No contribution — it is a proposal, not a completed work" | **VERIFIED.** The paper has no concrete resource description, no experiments. |
| "No evaluation or empirical grounding exists" | **VERIFIED.** Zero experiments, zero quantitative results. |
| "Resource description too vague to be considered a dataset contribution" | **VERIFIED.** No file formats, access mechanisms, annotation details, or quality metrics. |
| "Formatting artifacts (strikethrough)" | **Parser issue** — not a paper problem. Noted and dismissed. |
| "Single random ordering, no multiple runs" | **Moot** — there are no experiments to run multiple seeds on. |

**Strength Finder — cross-checked against paper:**

| Claim | Verdict |
|-------|---------|
| "Curated multi-subject cohorts with expert annotation" | The cohorts are listed (Table 1), but no curation beyond selection is demonstrated. Annotations are from original papers' pathologists, not newly generated. **Thin strength, but acknowledged.** |
| "Standardized preprocessing and batch-correction protocol" | Section 3 describes *generic* pipelines, not MOCHA-specific protocols. This is a literature summary, not a contribution. **REMOVED as a strength.** |
| "Broad cohort diversity across tissues, technologies, scales" | True but superficial — dataset selection alone doesn't constitute a paper. **Kept as minor supporting point.** |
| "Inclusion of co-registered histology images" | This is a property of the original datasets (all Visium/ST data include H&E images), not a MOCHA contribution. **REMOVED.** |
| "Consistent higher-level annotation groupings" | Briefly mentioned but deferred to inaccessible supplementary material. **REMOVED.** |

---

### Calibration Against Accepted/Rejected Papers

- **STAMP (score 6.5, Accept):** Built SpaVis-6M (1,982 slices), proposed a novel framework, validated across 6 datasets and 4 tasks. MOCHA has none of this empirical depth.
- **HEIST (score 5.0, Accept):** Proposed a graph transformer, pretrained on 22.3M cells, downstream evaluations across multiple tasks. Substantially more complete.
- **Aptamer Benchmark (score 3.5, Reject):** Integrated 8 sources into 6,413 pairs, established baselines with multiple models and splitting protocols. Even this rejected paper had concrete benchmarks.
- **IL3D (score 2.0, Reject):** Actually constructed 27,816 layouts, ran SFT experiments on LLMs, included ablation studies. Despite being criticized for limited technical contribution, it was far more complete than MOCHA.
- **PED-X-Bench (score 2.0, Reject):** Had 737 classified records, expert validation (κ=0.72), baseline benchmarks with multiple models. Again, far more concrete than MOCHA.

MOCHA is substantially less complete than even the lowest-scoring comparables. It lacks the minimum components expected of a resource/benchmark paper: description of the resource, demonstration of access, and empirical validation of utility.

---

### Recommendation

**Reject.** The paper does not constitute a completed scientific work. The core claims ("we present MOCHA, a curated resource") are not supported by the content delivered. To become a viable submission, the paper would need to be rebuilt from the ground up with: (1) a concrete, detailed description of the actual curated resource including annotation quality metrics, data formats, and access mechanisms; (2) benchmarks of at least two multi-sample methods on the resource; (3) a demonstration that the resource enables evaluation that was not previously possible. This exceeds what can be addressed in a rebuttal. I encourage the authors to complete this work and resubmit, as the underlying motivation remains valuable to the community.