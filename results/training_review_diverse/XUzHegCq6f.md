Now I have thoroughly verified the paper against the reviewer claims. Let me write the consolidated review.

## Summary

This paper proposes Polyak Parameter Ensemble (PPE), a method that constructs a parameter-level ensemble by maintaining a running weighted average of model parameters across epochs, with the key novelty being an exponentially increasing weighting scheme (λ > 1) over uniform weights (λ = 1.0). The method is evaluated primarily on knowledge graph embedding (KGE) models (DistMult, ComplEx, QMult) across multiple link prediction benchmarks, with a brief CIFAR-10 visualization. The core idea is simple and builds on well-known Polyak averaging.

## Strengths

- **Consistent improvements on KGE benchmarks**: Tables 4–6 report that PPE improves Hits@N and MRR for DistMult, ComplEx, and QMult across seven link prediction benchmarks (FB15K-237, YAGO3-10, NELL-995 variants, UMLS, KINSHIP, Mutagenesis, Carcinogenesis). The paper states that "PPE consistently improves the link prediction performance … on all datasets" (Section 5). This breadth across KGE models and datasets is the paper's main empirical contribution.

- **Benefits scale with model capacity**: Table 8 shows that for embedding dimension d ≥ 32, DistMult with PPE achieves higher scores in 81 out of 96 comparisons, while performing worse in only 6. The effect is more pronounced at larger d, which is a nontrivial empirical finding supporting the paper's claim.

- **Zero inference-time overhead**: The method requires no architectural changes, no additional parameters at test time, and no extended training time. The paper confirms "Throughout our experiments, we did not detect any runtime overhead of using PPE" (Section 5). This practical advantage over prediction-level ensembles is genuine and well-motivated.

- **Effectiveness on multi-hop reasoning**: Table 7 shows improvements in average MRR, Hit@1, and Hit@3 across all eight query types on UMLS, extending the method's applicability beyond simple link prediction.

## Weaknesses

### Fatal
None.

### Major

- **The averaging window definition creates a potentially degenerate configuration.** Section 4.1 states j = 200 as the cut-in epoch for averaging, while N ∈ {200, 250}. When N = 200, the averaging window (epochs j+1 to N) is empty, meaning PPE collapses to zero or the final model — i.e., no averaging occurs at all. The paper never specifies which datasets use N = 200 vs. N = 250, nor does it explain the choice. If any dataset uses N = 200, the reported improvements on that dataset cannot come from the proposed method. This is not a nitpick — it is a methodological gap that undermines the experimental design. The authors must clarify this, or re-run experiments with consistent N > j.

- **The claimed generality to image classification is essentially unsupported.** The abstract and introduction claim improvements on "11 benchmark datasets ranging from multi-hop reasoning to image classification," yet the sole non-KGE evidence is Figure 1 — a visualization of CIFAR-10 accuracy curves with no architecture description, no hyperparameters, no tabular results, and no baseline comparisons. This is not a valid experiment; it is an illustration. Either the authors should provide a proper CIFAR-10 evaluation (network architecture, training setup, test accuracies with and without PPE, comparison to SWA/uniform averaging) or withdraw the generality claim and scope the paper to KGE models.

### Minor

- **No variance or statistical significance reported.** All results in Tables 4–8 are single numbers. Given that mini-batch SGD is stochastic, small improvements (e.g., <1 MRR point in some entries of Table 8) cannot be assessed without standard deviations or multiple seeds. While single-run evaluation is common in parts of the KGE literature, the paper should at minimum acknowledge this limitation, and ideally report means over 3–5 runs.

- **The "cost-free" claim overstates the training cost.** The paper calls PPE "a cost-free ensemble technique in training and testing time concerned" (Section 1). While test-time memory is indeed that of a single model, during training PPE must maintain a running weighted average of all parameters, which requires storing a second parameter copy in memory — effectively doubling the training memory. This trade-off should be acknowledged.

- **The dynamic α determination via validation loss is described but never used, creating confusion.** Section 3.1 describes an "early-stopping-like" dynamic weighting scheme, but Section 4.1 states "we did not dynamically determined α by tracking the validation loss." Presenting a variant that is never evaluated and then saying it was not used is confusing. This should be clearly labeled as future work or removed from the method description.

- **The direct comparison of exponential (λ=1.1) vs. uniform (λ=1.0) weighting is limited.** Table 8 provides this comparison only for DistMult on two datasets (UMLS, KINSHIP). The main results tables (4–6) do not separately break out λ=1.0 vs. λ=1.1 for ComplEx and QMult, making it difficult to assess whether the exponential weighting specifically — as opposed to parameter averaging generally — is what drives improvements across all models. The paper's central claim is about exponential weighting, so this comparison should be shown for all model-dataset combinations.

- **Missing comparison to Stochastic Weight Averaging (SWA).** SWA (Izmailov et al., 2018) is cited in related work but never used as a baseline. SWA is the most closely related method (parameter averaging over a trajectory segment, often with a cyclical LR schedule). While the paper does compare λ=1.0 (uniform) vs. λ=1.1 (exponential), adding SWA would strengthen the positioning and demonstrate that the specific weighting scheme, not just any averaging, adds value.

### Trivial
- Figure 1 caption describes "the figure on the right" but the figure appears to contain multiple plots; the relationship between the figure and the caption text is unclear in the extracted text.

## Nice-to-Haves
- An ablation on the cut-in epoch j (e.g., 50%, 80%, 90% of training) to show robustness to this hyperparameter.
- An analysis of why performance degrades for very low embedding dimensions (d ≤ 4 / d < 16) — the paper notes this but does not explain it.
- A discussion of limitations, including that benefits diminish at low model capacity and that the method has not been tested outside KGE and a single CIFAR-10 visualization.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The paper never compares PPE to standard Polyak averaging."** — Factually wrong. The paper has λ ∈ {1.0, 1.1}, and λ = 1.0 is explicitly described as uniform weights / standard Polyak averaging at epoch intervals (Section 3: "Using positive equal ensemble weights α_i = 1/N corresponds to applying the Polyak averaging technique at each epoch interval"). Table 8 directly compares λ = 1.0 vs. λ = 1.1.

2. **"The paper never states how the weights are normalized to sum to 1."** — Factually wrong. Section 3 states "α_i s.t. Σ_i^N α_i = 1" directly in the definition of PPE.

3. **"The derivation with T=2 and N=2 is mathematically trivial and does not add insight."** — Subjective opinion about presentation, not a technical weakness. The derivation is a pedagogical illustration.

4. **Criticisms about the supplementary material / appendix being missing.** — The parser strips these sections; they exist in the original submission.

5. **Formatting/style nitpicks** — These are parser artifacts, not author errors.

6. **"Tables 4–6 are reported as screenshots with small, low-contrast text"** — This is a formatting artifact from PDF extraction, not a content issue with the original submission.

## Novel Insights

None beyond the paper's own contributions. The reviews do not reveal any deeper insight not already present in the paper. The observation about the j/N consistency issue is a methodological critique, not a novel research insight.

## Suggestions

1. **Clarify the j/N relationship immediately.** Report which datasets use N = 200 vs. N = 250 re-run experiments with consistent N > j, or justify why j = 200 is valid for all settings.
2. **Either add a proper CIFAR-10 experiment** (with architecture, hyperparameters, tabular test accuracies, baselines) or remove the image classification claim from the title/abstract and scope the paper to KGE models.
3. **Report variance.** Run each configuration with at least 3 random seeds and report mean ± std.
4. **Expand the λ = 1.0 vs. λ = 1.1 comparison** to all model-dataset combinations (ComplEx, QMult on all datasets), not just DistMult on two datasets.
5. **Add SWA as a baseline** on a subset of datasets to directly benchmark against the most related prior work.
6. **Acknowledge the training memory cost** of maintaining a second parameter copy.

## Score and Decision

The paper proposes a simple, plausible variant of parameter averaging. The core idea is not without merit, and the KGE experiments are reasonably broad in model and dataset coverage. However, the paper has two major problems: (1) the epoch window inconsistency (j = 200 with N ∈ {200, 250}) could render the method degenerate on some datasets, and the paper provides no clarification; (2) the claimed generality beyond KGE is supported only by a figure with no experimental detail — essentially absent evidence. Combined with the lack of variance reporting, limited direct comparison of the key variable (uniform vs. exponential weighting across all models), and overstated "cost-free" claim, the paper in its current form does not meet the bar for acceptance. The weaknesses are correctable with a major revision, but the paper as submitted is not ready.

**Originality**: 3/10 — The idea is a minor variant of existing parameter averaging (Polyak/SWA).
**Importance**: 5/10 — Parameter averaging is a useful technique; exponential weighting is a plausible refinement.
**Claims support**: 3/10 — Central claim is inadequately tested; epoch window issue undermines confidence.
**Soundness**: 3/10 — Methodological gap in evaluation design; no variance; overclaimed generality.
**Clarity**: 5/10 — Generally readable but confusing about dynamic α and the j/N issue.
**Value**: 4/10 — Could be useful for KGE practitioners after proper validation.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>