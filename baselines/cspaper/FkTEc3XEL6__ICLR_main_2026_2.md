---
job_id: 6039005a-9d0e-4ee6-82cf-58e7a43769aa
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: FkTEc3XEL6.pdf
paper: MOCHA: Multi-sample Omics Cohorts with Human Annotation
main_score_norm: 0.2
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is centered on datasets/benchmarks and software-oriented infrastructure for spatial transcriptomics, which is within ICLR scope, especially under datasets, benchmarks, and ML applications in biology/healthcare.

## Minimum Quality
Pass ✅. The submission is complete enough to review as a dataset/resource paper, with abstract, introduction, dataset description, workflow discussion, figures/tables, and references. That said, it falls well short of ICLR quality for acceptance because the contribution is mostly curation with limited empirical validation, weak benchmarking, and insufficient detail on several important aspects.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, manipulative instructions, or suspicious text targeting automated review systems in the provided paper content.

# Expected Review Outcome:
## Summary
This paper presents MOCHA, a curated multi-sample spatial transcriptomics resource intended for developing and evaluating methods for cohort-level spatial domain identification. The resource aggregates 10 publicly available cohorts spanning multiple tissues, species, and platforms, and standardizes access to gene expression matrices, spatial coordinates, H\&E images, and expert pathologist annotations. The paper also outlines a preprocessing and batch-correction workflow, and briefly summarizes several existing multi-sample spatial clustering methods that could be applied to the resource.

## Strengths
The paper tackles a real bottleneck. Multi-sample spatial transcriptomics is becoming increasingly important, and datasets with both cross-subject coverage and expert annotations are indeed scarce. A curated resource that puts expression, coordinates, pathology images, and labels in one place could be useful for method development and reproducible evaluation.

The inclusion criteria are reasonably strict and practically meaningful. Requiring, for each study, a count matrix, spatial coordinates, H\&E, and pathologist annotations is more valuable than simply listing available SRT datasets. This gives MOCHA a clearer intended use case than broader repositories that emphasize storage or browsing.

Table 1 is a useful overview of the cohort diversity. It makes clear that the resource spans different biological settings, including cancer and non-cancer tissues, different scales of cohort size, and multiple platforms. This heterogeneity could be a strength for testing robustness of multi-sample methods.

Figure 1 is one of the more informative elements in the paper. The boxplots summarizing number of spots, number of genes, and sparsity across cohorts help the reader quickly understand the breadth and heterogeneity of the curated data. In particular, the figure supports the paper’s claim that these cohorts vary substantially in scale and sparsity, which is exactly the kind of variation that makes multi-sample integration challenging and potentially interesting from an ML perspective.

Figure 2 is also useful at a didactic level. Even though it is not a benchmark, it gives a concrete illustration of the intended preprocessing pipeline, from pathology image and annotations to HVG selection and Harmony-based integration. For readers outside spatial transcriptomics, this makes the paper easier to follow.

The paper is generally readable at a high level. The motivation, namely that cohort-level SRT method development lacks standardized annotated resources, is understandable and well aligned with an important practical need.

## Weaknesses
The biggest issue is that the paper does not actually demonstrate the value of MOCHA through benchmarking. The central claim is that MOCHA is a resource for “developing and evaluating” multi-sample SRT methods, yet the paper contains no quantitative benchmark using the curated cohorts. There is no comparison of methods such as BASS, BayeSMART, or STAGATE on any subset of MOCHA, no evaluation protocol, no train/validation/test split logic for benchmark use, and no reported performance against pathologist labels. As a result, the submission remains a description of a dataset collection rather than a convincing benchmark paper. For ICLR, that gap matters a lot, because the community needs evidence that the resource enables meaningful, reproducible method comparison rather than simply packaging existing data.

Relatedly, the paper lacks a results section in substance, even if it contains descriptive figures and tables. Table 1 is a dataset inventory, Table 2 is a method summary, Figure 1 shows dataset statistics, and Figure 2 shows a workflow illustration, but none of these provide experimental evidence that MOCHA improves reproducibility, supports method ranking, or reveals failure modes of existing methods. The paper repeatedly motivates evaluation, but it never performs one. This weakens both soundness and contribution.

The paper is underspecified about the annotation harmonization process, which is arguably the scientific core of the resource. On Page 4, the authors state that in a majority of cancer studies, detailed pathologist annotations can be grouped into four broad categories, immune, stroma, tumor, and normal, with details deferred to supplementary material. But in the main paper there is no precise mapping protocol, no statement of which cohorts use which original labels, no discussion of inter-cohort incompatibilities, and no evidence that the mappings are biologically coherent or consistent across studies. This matters because the usefulness of MOCHA as a benchmark depends heavily on whether the “ground truth” labels are comparable across cohorts. If the labels come from different pathologists with different annotation criteria and are then coarsened post hoc, downstream method evaluation could be noisy or even misleading.

The paper’s positioning against existing resources is too shallow. The introduction names repositories such as SORC, Aquila, SODB, STOmicsDB, and SpatialDB, but the paper does not clearly articulate what MOCHA uniquely adds beyond collecting a smaller subset with labels. Is the main novelty the pathologist annotations, the multi-sample orientation, the standardized file format, the harmonized categories, or the preprocessing recommendations? Right now it reads as “we assembled useful datasets and provide them in convenient formats,” which is helpful but modest. For a main-track ICLR paper, the authors need a sharper argument about what is scientifically new.

Table 2 is too limited to support the broader methodological framing. The paper presents this as “a summary of the existing multi-sample spatial clustering methods,” but includes only BayeSMART, BASS, and STAGATE. Even within the paper’s own narrative, this feels incomplete and undercuts the claim that MOCHA is intended as a broad development/evaluation platform. A benchmark resource paper should usually connect more systematically to the evaluation ecosystem, including methods, metrics, and practical setup. As written, Table 2 functions more like a short reading list than a serious benchmark framing device.

The discussion of preprocessing and batch correction in Section 3 is generic and not sufficiently tied to MOCHA itself. The section mostly surveys standard normalization methods, HVG/SVG selection, dimensionality reduction, Harmony, and Crescendo. That is not wrong, but it reads like a tutorial paragraph rather than a carefully justified protocol. The paper does not specify which choices are recommended defaults for MOCHA, what exact preprocessing is distributed with the resource versus left to users, or how methodological comparisons should control for preprocessing variance. For a benchmark-oriented contribution, those details are critical.

Figure 2, while visually helpful, also exposes this problem. The figure demonstrates an HVG + Harmony workflow on the KC\_TLS cohort, but the paper does not explain whether this pipeline is merely illustrative or part of the standardized benchmark setup. If the latter, key parameters are missing, including how HVGs are selected, how many genes are retained, whether selection is per sample or pooled, how Harmony is configured, and whether the pathologist labels are used anywhere during tuning. If the former, then the figure risks implying a level of standardization that the paper does not actually define.

There is little technical detail about the actual deliverable. The abstract states that MOCHA provides “standardized data organization, efficient storage formats for large-scale processing, and protocols for handling batch effects in multi-sample integration,” but the main paper does not specify the schema, metadata fields, file conventions, APIs, package structure, loaders, or compatibility details in a meaningful way. For a data/infrastructure submission, this is not a minor omission. The value of such a resource depends on concrete usability, and the paper remains frustratingly abstract about what exactly users receive.

The paper does not address dataset split design or benchmark governance. A multi-cohort benchmark should define how methods should be compared: per-cohort evaluation, leave-one-subject-out, cross-cohort transfer, pooled training with held-out samples, or some other protocol. Without this, the risk is that every user evaluates differently and MOCHA fails to create a standardized comparison framework. This is especially important because sample counts in Table 1 are highly imbalanced, for example 94 samples for BC\_TNBC\_ST versus only 3 samples for KC\_TLS. Those imbalances could dominate pooled metrics or encourage questionable evaluation choices if not explicitly handled.

The paper’s evidence for cross-sample variability and batch effects is asserted rather than demonstrated. Figure 1 shows descriptive heterogeneity in spots, genes, and sparsity, which is useful, but this is not the same as showing batch structure or integration difficulty. Likewise, the Harmony illustration in Figure 2 visually suggests alignment, but there is no quantitative before/after metric, no domain conservation measure, and no assessment of whether biological structure is preserved. For a paper that emphasizes batch correction as part of the contribution, the support is too thin.

There are also presentation issues that reduce credibility. On Page 4, the caption begins “AA standard pipeline,” which looks like an editing oversight. The paper includes two image insertions after Figure 2, corresponding to the HVG panel and Harmony panel, but they are not introduced as separate figures in the text. This makes the figure structure confusing. The manuscript also lacks a proper conclusion/discussion section to synthesize limitations, scope, and intended benchmark use.

A more subtle but important concern is that the paper mixes several claims without fully committing to any one of them: dataset paper, benchmark paper, workflow/tutorial paper, and mini-survey of methods. That makes the contribution feel diffuse. If this is a benchmark/resource paper, the benchmark should be front and center with metrics and baselines. If it is a survey/resource note, that is a different standard and likely a weaker fit for ICLR main track.

Finally, the ML contribution is limited. There is no new model, no new evaluation metric, no new theoretical result, and no empirical study showing new scientific findings enabled by the resource. Dataset papers can still be strong at ICLR, but then the benchmark design, rigor, and impact need to be unusually well executed. Here, the execution does not yet reach that bar.

## Questions
1. Can the authors provide a concrete benchmark in the rebuttal, even on a subset of MOCHA, using the methods listed in Table 2 or similarly standard baselines? What I would want to see is at least one quantitative comparison against the provided pathologist labels, with a clearly defined metric and protocol. This would substantially increase my confidence that MOCHA is more than a curated collection.

2. Please spell out, in the main paper, the exact harmonization procedure for expert annotations. For each cohort, what were the original labels, how were they mapped into shared categories, who performed the mapping, and how were ambiguous cases handled? If some cohorts are excluded from harmonized evaluation, say so explicitly.

3. What exactly is distributed with MOCHA? I am looking for specifics: data schema, storage format, metadata tables, image-coordinate registration information, standard loaders, and whether preprocessing outputs are included or only raw data references.

4. What benchmark protocol do the authors recommend? For example, are methods supposed to cluster separately per sample and then align across samples, jointly cluster all samples, or use one cohort for training and another for transfer? The paper should define at least one standard protocol if it aims to support fair method comparison.

5. For the workflow in Figure 2, please clarify whether HVG selection and Harmony are normative parts of the benchmark or just an example. If they are intended as defaults, what are the exact hyperparameters and implementation details? If they are not defaults, the paper should make that distinction explicit.

6. Have the authors assessed label consistency or expert disagreement in any way? Even a limited audit of annotation reliability would help readers judge how much confidence to place in these labels as evaluation targets.

7. Why were the specific methods in Table 2 chosen, and do the authors intend MOCHA to support evaluation of methods beyond clustering, for example integration quality, transfer learning, or histology-guided representation learning? A stronger articulation of the intended task scope would improve the paper.

## Flag For Ethics Review
- Yes, Responsible research practice (e.g., human subjects, data release)

## Details Of Ethics Concerns
The paper aggregates human tissue datasets with pathology images and expert annotations across multiple public studies. I do not see an obvious ethical violation in the submission itself, and these appear to be public datasets, but the paper should more explicitly document data provenance, licensing/terms of use, and any restrictions on redistribution of H\&E images and annotations. For a resource paper, transparent reporting of dataset permissions and redistribution policy is part of responsible research practice.

## Soundness Rating
2: fair. The paper’s descriptive claims about the collected cohorts are plausible, but the central claims about enabling evaluation and reproducible method development are only weakly supported because the submission lacks actual benchmark experiments and leaves important curation details underspecified.

## Presentation Rating
2: fair. The motivation is understandable and some visual elements, especially Figure 1 and Table 1, are helpful, but the manuscript is thin, omits key implementation and benchmark details, and has several structural/presentation issues that make the contribution feel incomplete.

## Contribution Rating
1: poor. The resource may be practically useful, but in its current form the contribution is mostly curation and packaging of existing datasets without the level of benchmark design, validation, or methodological depth typically needed for a strong ICLR main-track paper.

## Overall Rating
2: Reject, not good enough. The problem is worthwhile, and a well-executed multi-sample annotated SRT benchmark could be valuable. But this submission does not yet provide the empirical benchmarking, annotation harmonization detail, benchmark protocol, or concrete resource specification needed to justify acceptance at ICLR.

## Reviewer Confidence
4: confident. I am confident in this assessment, though it remains possible that some implementation details or harmonization procedures exist outside the main paper. My evaluation is based on what is actually presented in the submission, and on that basis the paper is not yet strong enough.