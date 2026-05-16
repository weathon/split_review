Now I have a thorough understanding of the paper and the reviewer's claims. Let me compose the final consolidated review.

## Summary

This paper benchmarks 13 deep learning models (7 "spatial" FC-graph models and 6 "sequential" BOLD-time-series models) across 34,887 fMRI samples from six public databases (HCP, ADNI, OASIS, PPMI, ABIDE), covering task-fMRI classification, neurodegenerative disease diagnosis, and neuropsychiatric disorder classification. The authors provide domain-informed guidelines for model selection and conduct a preliminary post-hoc interpretability analysis. The public release of preprocessed data is a genuine service to the community.

## Strengths

- **Large-scale, multi-dataset benchmarking across diverse fMRI scenarios**: The study evaluates 13 deep models on 34,887 samples from six public databases, covering task-evoked fMRI, neurodegenerative disease, and neuropsychiatric disorders. This is the most comprehensive benchmark in terms of dataset breadth and model variety for fMRI analysis (Tables 1–4). The paper directly answers its stated first research question about no single model dominating across all settings.

- **Domain-informed guidelines for model selection tied to biological mechanisms**: The paper provides actionable, neuroscience-grounded recommendations — sequential models for task fMRI (supported by individual model rankings showing top sequential models consistently beating top spatial models), spatial models for neurodegenerative disease, and spatial-temporal approaches for neuropsychiatric disorders. These guidelines are connected to biological reasoning (Remarks 1.1, 2.1, 3.1) and are practically useful.

- **Inclusion of recent and diverse model families**: The benchmark covers 13 methods from classical GNNs to Mamba, MLP-Mixer, and SPDNet — several models absent from prior fMRI benchmarks (Section 4). This ensures the comparison reflects the current state of the art.

- **Public release of preprocessed data**: The paper explicitly states that preprocessed data are made publicly available (Conclusions), lowering barriers for future comparative studies and fostering collaborative research between machine learning and neuroscience.

## Weaknesses

### Fatal
None.

### Major

- **Flawed family-level statistical comparison (two-sample t-test on model accuracies)**: The paper performs two-sample t-tests comparing 7 spatial vs. 6 sequential models by treating each model's accuracy as an independent observation (Section 5.2, Figure 3). This is structurally problematic: all models are evaluated on the same data splits, violating the independence assumption of the t-test. With only 6–7 "samples" per group, the test also has extremely low power and the reported p-values (e.g., *p=0.01*, *p<10⁻⁴*) are unreliable indicators of population-level differences. The paper's guidelines (e.g., "sequential models are more effective in task fMRI") are still largely supported by comparing the *best* individual models in each family — e.g., top sequential models clearly outperform top spatial models on HCP tasks by raw accuracy margins visible in Table \ref{hcp}. But the t-test framing as rigorous statistical evidence for *family-level* superiority is not valid. The authors should either: (a) drop the family-level t-test and present per-dataset individual model rankings with confidence intervals, or (b) use appropriate dependent-samples methods (e.g., paired permutation tests across matched configurations) if a family-level claim is essential.

### Minor

- **Under-specified experimental setup for disease datasets**: The paper describes train/validation/test splits for HCP ("Separated Scan" vs. "Mixed Scan") but provides no split procedure for ADNI, OASIS, PPMI, or ABIDE. Standard deviations are reported (± values) for disease tasks without explanation — are these from cross-validation folds, repeated runs with different seeds, or some other procedure? A benchmark paper's primary contribution is its evaluation framework, and these omissions make it harder for readers to assess or reproduce the disease-dataset results.

- **Under-specified interpretability analysis**: The post-hoc analysis (Section 6) extracts importance maps via "logistic regression weights for features derived from different models" and selects the top 40 brain regions. The paper never specifies *how features are extracted from each deep model* — whether from the last hidden layer, attention weights, gradients, or some other mechanism. Without this, the cross-model comparison of attention maps is ambiguous, since different models may produce features with fundamentally different semantics. Furthermore, the evaluation is purely visual — no quantitative metric (overlap with Neurosynth maps, Dice scores, spatial correlation) is provided. The conclusion that "findings are not yet converging" is safe but adds little insight. Since the interpretability analysis is presented as exploratory (not a core contribution), this is a minor gap but one worth addressing.

- **No discussion of computational cost**: A benchmark evaluating 13 models on 34,887 samples should report training time, number of parameters, and/or inference time per model. This information is directly useful for practitioners deciding which model to adopt and is standard in benchmarking papers.

- **No per-task accuracy breakdown for HCP**: The paper reports aggregate accuracy across cognitive tasks but does not show per-task breakdowns. Given that cognitive tasks differ (emotion, motor, language, working memory, etc.), a per-task analysis could reveal whether certain models excel at specific task types (e.g., motor tasks being easier for spatial models), which would strengthen the "guideline" aspect.

- **HCP-WM low absolute performance not discussed**: The best accuracy on HCP-WM Separated is only 61.55% (8-way classification, chance ≈ 12.5%). The paper notes the short scan duration (39 time points) but does not discuss whether this makes the problem ill-posed for spatial models (which require stable FC estimates) or whether the task itself is inherently difficult. This context is important for the guidelines.

### Trivial

- **Inconsistent hypothesis labeling**: The paper introduces H1, H3, H4 in Section 5 (lines 106–109) but then references H2 in the Discussion (line 294: "the answer to (H2) is 'YES'"), suggesting H2 was dropped during editing. This is a minor inconsistency.

- **Unnecessary self-citation density**: The introduction paragraph on contributions (line 35) cites ~15 of the authors' own papers in a single sentence. This does not affect soundness but reads as self-promotional rather than a balanced literature review.

## Nice-to-Haves

- **Cross-validation details for disease datasets**: Clarify whether the reported standard deviations come from k-fold cross-validation, repeated runs, or some other procedure, and specify the train/validation/test split for each disease dataset.
- **Per-task accuracy for HCP**: A breakdown of accuracy by cognitive task (emotion, motor, language, etc.) would make the guidelines more actionable.
- **Computational cost table**: Reporting training time, inference time, and parameter counts per model would significantly increase the paper's practical value.

## Removed Points

- **Criticism that the model selection is arbitrary (e.g., SPDNet only among manifold methods, no TCN/GRU)**: The selection of 13 models spanning multiple architectural families is defensible for a benchmark of this scope. No benchmark can include every variant, and the paper provides a clear rationale for each family (Section 4). This is scope creep, not a valid weakness.

- **Criticism about node embedding sensitivity**: The paper uses degree vectors as node features following optimal settings from Bedel et al. (2023). For a model-comparison benchmark, citing a prior work's established optimal configuration is standard practice, and testing additional node feature types would broaden the paper beyond its stated scope.

- **Criticism about post-hoc biological speculations in Remarks**: The paper uses hedging language ("One possible explanation," "could be attributed to," "We speculate") and clearly distinguishes between observed accuracy differences and biological interpretations. This is appropriate for a discussion/remarks section.

- **Strength Finder's claim of "Rigorous statistical comparison between model categories"**: This conflicts with the verified Major weakness about the flawed t-test analysis. Dropped per the rule that when a strength and verified weakness disagree, the weakness wins.

## Novel Insights

None beyond the paper's own contributions. The main novel finding — that no single architecture family dominates across all fMRI scenarios, and that appropriate model choice depends on the task's biological properties (BOLD dynamics vs. connectivity topology) — is a useful synthesis that the paper documents at an unprecedented scale, but it is not a surprising theoretical insight.

## Suggestions

1. **Replace or remove the family-level t-test comparisons.** Present per-dataset rankings of individual models with bootstrap confidence intervals or Bayesian hierarchical models. If family-level claims are desired, compare the *best* model from each family using paired bootstrap across data subsamples, not a two-sample t-test on 6 vs. 7 model accuracies.

2. **Document the experimental protocol for disease datasets.** Specify the train/validation/test split (e.g., 5-fold cross-validation, stratified splits) and explain the source of reported standard deviations. Add a one-paragraph implementation details summary covering optimizer, learning rate, batch size, and number of runs.

3. **Clarify the feature extraction mechanism for the interpretability analysis.** State explicitly how features are extracted from each model type (e.g., penultimate layer activations, attention weights, or logistic regression on latent representations) so readers can interpret the attention maps meaningfully. Adding a quantitative overlap metric would substantially strengthen this section.

4. **Add a computational cost comparison** (training time, inference time, parameter counts) to help practitioners make informed trade-offs.

## Score and Decision

This paper makes a genuine contribution through its large-scale, multi-dataset benchmarking effort and the release of preprocessed data. The individual model comparisons and domain-informed guidelines are largely supported by the raw accuracy numbers, which are clearly presented in the tables. However, the paper's statistical evidence for family-level comparisons (the t-test analysis) is methodologically flawed and should be removed or replaced. The interpretability analysis and experimental documentation for disease datasets need improvement. These issues are addressable and do not invalidate the core empirical contribution.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>