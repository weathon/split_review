Now I have a complete picture of the paper and can produce the consolidated review.

## Summary

This paper presents a benchmark for fairness-aware graph learning, evaluating ten representative methods (FairWalk, CrossWalk, FairGNN, NIFTY, EDITS, FairEdit, FairVGNN, InFoRM, REDRESS, GUIDE) across seven real-world attributed graph datasets (including two newly constructed large-scale datasets, AMiner-S and AMiner-L). The study examines group fairness, individual fairness, trade-offs between fairness criteria, and computational efficiency, providing analysis and a practitioner guide.

## Strengths

- **Comprehensive method and dataset coverage.** The benchmark spans ten methods covering both group and individual fairness approaches and both shallow-embedding and GNN-based architectures, evaluated on seven datasets including two new large-scale ones (AMiner-S: 39K nodes, AMiner-L: 130K nodes). This breadth goes well beyond prior benchmarks that covered only two methods.

- **Multi-dimensional analysis across four research questions.** The paper systematically investigates group fairness (Δ_SP, Δ_EO, Δ_Utility), individual fairness (B_Lipschitz, NDCG@k, GDIF), trade-offs between fairness criteria, and computational efficiency. Each dimension yields concrete, actionable findings (e.g., shallow embedding methods like FairWalk/CrossWalk generally outperform GNN-based ones on group fairness metrics but sacrifice utility; GUIDE is the most versatile on individual fairness).

- **Practical guidance anchored to empirical patterns.** Section 5 translates the benchmarking results into a decision guide for practitioners, recommending specific methods based on priority (group fairness vs. utility-fairness balance vs. individual fairness). This adds practical value beyond a simple performance ranking.

- **Two new large-scale, anonymized datasets.** The AMiner-S and AMiner-L datasets, designed specifically for fairness research with continent-based sensitive attributes and a research-field prediction task, are a reusable contribution to the community.

## Weaknesses

### Major

- **Evaluation protocol is underspecified given that "Experimental Protocol Design" is listed as a primary contribution (line 20).** The protocol description (lines 86–87) consists of roughly two sentences covering hyperparameter selection ("lowest loss values on the validation node set via grid search"), three runs with standard deviation, and GCN backbones. Critical details missing for a benchmark that claims protocol design as a contribution include: (1) how training/validation/test splits are constructed for each dataset and whether they are stratified by sensitive attribute; (2) whether and how sensitive attributes are provided to methods that use them explicitly vs. those that do not; (3) the hyperparameter grid ranges searched; (4) whether the GCN backbone is used uniformly for methods originally proposed with different architectures (e.g., FairGNN, NIFTY, EDITS, FairVGNN) and what justification exists for this choice. For a benchmark paper whose value rests on fair and reproducible comparison, this level of specification is insufficient.

- **The newly constructed AMiner datasets raise unresolved questions about their compatibility with the paper's stated experimental setup.** The paper declares binary node classification throughout ("we conduct benchmarking experiments on the popular graph learning task of binary node classification (i.e., c=2)", line 27), but the AMiner task is "predict the primary research field of each researcher" (line 305). The paper does not clarify how this is reduced to binary classification, how many research fields exist, or whether the binary sensitive attribute framework (S ∈ {0,1}, as assumed by Δ_SP and Δ_EO) applies to "continent of affiliation" which is inherently multi-valued. These details are essential for interpreting results on these datasets.

### Minor

- **No dedicated limitations section.** The conclusion briefly acknowledges that "evaluations on other graph learning tasks remain a future direction" (line 213), but the paper would benefit from explicitly scoping its choices (binary node classification only, GCN backbones, the ten specific methods) and acknowledging potential limitations (e.g., backbone choice may disadvantage methods designed for other architectures).

- **Code release not mentioned.** For a benchmark intended to "facilitate broader applications" and serve as a reusable resource, the paper would be strengthened by indicating where code and datasets will be made available.

### Trivial

- Table 1 (dataset statistics) is referenced in the text but appears as a parser-stripped image. While this is a parser artifact (the original submission contains the table), the paper would benefit from ensuring dataset statistics (node/edge counts, attribute dimensions, sensitive attribute distributions) are also presented in accessible textual form where possible.

## Nice-to-Haves

- **Statistical significance analysis.** The paper reports standard deviations from three runs but does not conduct pairwise significance tests or critical difference diagrams (Demšar, 2006) to support claims like "method A outperforms method B." This would strengthen comparative conclusions.

- **Dataset-specific breakdown by graph properties.** The current analysis treats datasets largely interchangeably. Breaking down results by graph characteristics (density, homophily level, sensitive attribute prevalence) could yield deeper insights into when each method is preferable.

- **Sensitive attribute distribution statistics.** For a fairness benchmark, reporting the distribution of sensitive attributes across datasets (proportion of each subgroup) would help readers assess how imbalanced the data is and contextualize the fairness results.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **"Benchmark results are absent from the main paper"** — Removed because the tables and figures (Table 1, Table 3, Figure 4, Figure 5) exist in the original submission but were rendered as image placeholders by the parser. The paper shows these referencing anchors; the parser stripped the visual content. This is a parser artifact, not an author omission.

- **"Analysis relies on text summaries of unreferenced numbers"** — Removed because the findings (Finding 2, 3, 4) reference specific tables and figures (Table 3, Figure 4, Figure 5) that contain the quantitative evidence. The text summaries are intended to draw conclusions from those presented numbers. The absence of visible numbers in the parsed output is a parser artifact.

- **"Missing baseline for individual fairness"** — Removed because the text explicitly discusses vanilla GNN performance (line 97: "The vanilla GNN generally achieves the best utility across most datasets"), confirming that a standard baseline is included and discussed.

- **"OOM handling unspecified"** — Removed because Table 3's caption states "OOM denotes out-of-memory" (line 106), and the RQ3 discussion mentions "datasets free from OOM" (line 104), showing OOM is tracked. Specific per-method/per-dataset OOM information would appear in the tables (which are parser-stripped images).

- **"Practitioner guide feels arbitrary"** — Removed because the guide is intended to be grounded in the quantitative results presented in the tables/figures. The recommendations would be properly evidenced in the full submission.

- **"Unfair comparison via GCN backbone"** — Removed as a standalone point and folded into the protocol underspecification weakness above. The reviewer correctly notes this needs justification, but it is a description gap rather than an unfair comparison (the uniform backbone actually favors the baseline, not the author's method — consistent with the rule that asymmetric comparisons favoring baselines are permissible).

- **"Results should be in the main paper not appendix"** — Removed because Section 4.1 (RQ1) and the tables/figures are part of the main paper in the original submission; the parser stripped Section 4.1 entirely and converted tables to image placeholders.

- **"Missing discussion of sensitive attribute distribution for fairness datasets"** — This is a valid point in spirit, but Table 1 (which reports dataset statistics) would normally include such information. Since Table 1 is a parser-stripped image, we cannot verify whether this information is already present. Moved to Nice-to-Haves.

- **"No discussion of data split construction"** — Folded into the protocol underspecification weakness above.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any novel perspective on the paper that the paper itself does not already articulate.

## Suggestions

- **Expand the experimental protocol description (Section 3.1) to at least a full page.** Specify: data split construction per dataset (including whether stratified by sensitive attribute), exact hyperparameter ranges searched for each method, how sensitive attributes are handled across methods (especially for methods that use them explicitly vs. those that don't), and the rationale for uniform backbone adoption (GCN) for methods originally designed with other architectures.

- **Clarify the AMiner dataset setup.** State explicitly how many research fields exist, how the prediction task is reduced to binary classification, and how the inherently multi-valued "continent of affiliation" sensitive attribute is binarized (or whether multi-group fairness metrics are used instead). Report the distribution of researchers across continents and across research fields.

- **Add a dedicated limitations paragraph** scoping the benchmark's coverage (binary node classification only, GCN backbones, the ten specific methods selected) and acknowledging the potential impact of these choices on generalizability.

- **Include a reproducibility statement** indicating where code, data, and configuration files will be made available.

## Score and Decision

This paper addresses a genuine gap — a comprehensive quantitative benchmark for fairness-aware graph learning — and the underlying compilation of methods, datasets, and analysis appears solid. However, the paper currently lists "Experimental Protocol Design" as a primary contribution while describing the protocol in only two sentences, omitting critical details about data splits, hyperparameter ranges, and sensitive attribute handling that are essential for a benchmark's credibility and reproducibility. Additionally, the new AMiner datasets raise unresolved questions about their compatibility with the stated binary-classification, binary-sensitive-attribute experimental framework. These are substantive gaps in a paper whose central value proposition is systematic comparison. The paper needs a major revision — primarily expanding Section 3.1 substantially and clarifying the AMiner setup — before it can deliver on its claimed contributions.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>