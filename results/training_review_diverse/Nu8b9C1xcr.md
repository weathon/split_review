Now I have a complete picture. Let me construct the final meta-review.

## Summary

This paper presents CardBench, a benchmark for learned cardinality estimation (CE) in relational databases. It releases 20 diverse real-world databases with thousands of single-table and binary-join queries and their true cardinalities (obtained at the cost of 7 CPU-years of query execution), along with open-source infrastructure for statistics computation, query generation, and annotated query graph creation. The paper illustrates the benchmark's utility by training GNN and transformer models under instance-based, zero-shot, and fine-tuned configurations, showing that zero-shot CE is challenging for joins but fine-tuning with few samples achieves comparable accuracy to instance-based models with much lower training overhead.

## Strengths

- **Large-scale, diverse benchmark for pre-trained CE models.** CardBench provides 20 real-world databases (genomics, e-commerce, transportation, geospatial, etc.) with thousands of queries each, far exceeding prior benchmarks that used only 1–2 datasets (Section 2, Table 1). This diversity is necessary for training and evaluating zero-shot models, which the paper correctly identifies as a critical gap in existing benchmarks.

- **High-cost training data released to lower the entry barrier.** The paper states that executing queries required "7 cpu time years" (Section 3) and releases the queries with true cardinalities. This pre-computed resource saves enormous computation for future researchers and directly supports the stated goal of fostering ML research on CE.

- **Empirical demonstration of fine-tuning efficiency.** Experiments show that fine-tuning a pre-trained model on 500 samples achieves accuracy comparable to instance-based models trained on 1000 samples (Figures 5–6). For binary joins with 500 samples, fine-tuned GNN achieves P50 q-error 1.32 and P95 120 vs. 1.57 and 280 for instance-based GNN (Section 5.3). This quantitatively validates the claim that pre-trained models with fine-tuning reduce training overhead.

- **Systematic evaluation across three configurations.** The paper presents uniform experiments across all 20 datasets using the same test sets for instance-based, zero-shot, and fine-tuned configurations with two model families (GNN and transformer), establishing baselines for future work (Figures 3–8).

- **Open-source infrastructure for extensibility.** Scripts for statistics calculation, query generation, and annotated query graph creation are released (Section 3, Figure 1), allowing others to add datasets and query shapes, which supports the aim of "foster further research … from the ML community."

- **Dataset-agnostic feature design.** The models exclude table/column names and rely on transferable statistics (row counts, histograms, correlations — Table 1/2), a principled design choice for zero-shot generalization that is clearly documented.

## Weaknesses

### Fatal
None.

### Major
None. The core contribution (the benchmark itself) is solid, and no verified weakness undermines it.

### Minor

- **Single-run experiments without variance reporting.** The paper explicitly states (Section 5.2, line 328) that "We run a single experiment on each of the 20 test datasets per model configuration." Because the experiments involve neural networks with stochastic elements (random initialization, train/validation splits), a single run per dataset per configuration cannot distinguish systematic improvement from random variation. The box plots aggregate over 20 datasets (showing cross-dataset variation) but leave within-dataset variance invisible. For a paper drawing conclusions about relative performance of instance-based vs. zero-shot vs. fine-tuned models, this weakens the reliability of the quantitative comparisons. (Note: 20 datasets do provide some evidence of robustness across datasets, and for a benchmark-focused paper this is a limitation rather than a fatal flaw, but it should be addressed with multi-seed runs for the key comparisons.)

- **The `estimated_selectivity` feature conflates model learning with a traditional estimator.** The models receive `estimated_selectivity` as a predicate-node input feature (Table 1, line 211), which is computed using traditional selectivity estimation methods (Section 3.3, line 251). This means the model effectively learns a correction on top of a traditional estimator rather than learning selectivity from raw statistics alone. The paper does not ablate this feature, making it unclear whether the model's accuracy comes from learning data distributions or from tuning the baseline estimator. An ablation study removing `estimated_selectivity` would clarify what the model is actually learning. (The paper is transparent about using this feature, but the lack of ablation is a methodological gap.)

- **The baseline comparison is simplified relative to modern DBMS estimators.** The baseline assumes column independence and uniformity (Section 5.2, line 307–312) and for joins assumes PK/FK simplification. While the paper states this "represents heuristics employed in conventional DBMS such as PostgreSQL," PostgreSQL's actual estimator uses histograms, MCV lists, and correlation statistics that are more sophisticated. The single-table results show the baseline achieving median q-error < 1.5 and GNN achieving 1.1 — a modest improvement. The paper's claim that "learning-based models significantly outperform the baseline" is well-supported for binary joins (baseline median q-error 55.54 vs. GNN 1.16) but is more modest for single-table queries, which the paper does acknowledge. This does not undermine the benchmark contribution but weakens the strength of the quantitative claims about learned models over traditional methods.

- **The method for selecting fine-tuning training samples is underspecified.** The paper uses sample sizes of 250, 500, and 1000 for fine-tuning (Section 5.3) and states that 4500 queries are "randomly selected" for training (Section 5.2, line 328), but does not state how the fine-tuning subsets of 250/500/1000 are selected from the available pool (random? stratified by predicate complexity?). This is a minor reproducibility gap.

- **Filtering out zero-cardinality queries is not ablated.** The preprocessing step removes queries with zero cardinality or zero predicates (Section 4.1, line 267), with the rationale that they are "relatively rare" and "could introduce noise." While this rationale is reasonable, zero-cardinality queries are common and challenging in practice; the paper does not examine how this filtering affects reported accuracy or model behavior.

### Trivial

- The "Broader Impact" subsection header (Section 7) appears without content — this may be a parser artifact, but should be checked in the original.
- The box-plot captions (Figures 3–6) could clarify that whiskers show min/max across datasets (not across repeated runs).

## Nice-to-Haves

- **Multi-join query workloads.** The benchmark currently covers only single-table and binary-join queries (Section 3). The paper acknowledges this limitation and provides an extensible generator. Adding even a small set of 3+-table join queries would demonstrate extensibility and increase the benchmark's value for zero-shot CE research on realistic workloads.
- **Model code and pre-trained checkpoints.** The paper releases scripts for statistics and query generation, but releasing model code and pre-trained weights would make CardBench a turn-key resource for future researchers and improve reproducibility.
- **Ablation of `estimated_selectivity`** (as noted in Minor weaknesses) would strengthen the paper's methodological clarity.
- **Comparison of fine-tuned vs. zero-shot (without fine-tuning) at the same sample sizes** would clarify how much of the gain comes from pre-training vs. from the additional training data.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Abstract overclaims benchmark utility"** — Removed. The abstract says the benchmark "can be used for training and testing learned models systematically," which is literally true. Not an overclaim.
2. **"Table 1 feature labeling is confusing"** — Removed. The table caption (lines 171–178) clearly explains that ♢ denotes features for query generation and ♡ denotes features used by models.
3. **"4500 query selection not explained"** — Removed. The paper (line 328) states: "4500 queries are randomly selected per dataset."
4. **"Baseline PK assumption is a weakness"** — Removed. The paper acknowledges this assumption (line 311–312): "makes the simplifying assumption... (an assumption commonly made by database systems)."
5. **"GNN design not justified"** — Removed. The design follows prior work (Carsten) with a brief justification.
6. **"Limited query complexity is a 'serious structural limitation'"** — Moved to Nice-to-Have. The paper explicitly scopes itself to single-table and binary-join queries, provides an extensible generator (Section 3), and the experiments show even binary joins are very challenging for zero-shot models. Demanding multi-join workloads is scope creep; the paper's contribution stands on its own terms.
7. **"Broader Impact section empty"** — Removed. This is a parser artifact; the PDF-extraction pipeline likely stripped the content.
8. **Various formatting/style nitpicks** — Removed per instructions.

## Novel Insights

The reviews highlight a substantive tension not fully explored in the paper: the `estimated_selectivity` input feature ties the learned models to a traditional estimator, meaning the "zero-shot" results may actually reflect the model's ability to correct residual errors in a classical estimator rather than learning selectivity patterns from raw statistics. This is important because it affects how we interpret the zero-shot finding (that it "drops" for joins) — the drop may be as much about the quality of the input selectivity estimate for joins as about the model's own generalization. An ablation study would resolve this and could be a useful contribution in itself.

Beyond this, no genuinely novel insight emerges beyond the paper's own contributions.

## Suggestions

1. Run the key comparisons (instance-based vs. zero-shot vs. fine-tuned for both query types) with 3–5 random seeds and report mean ± std or show within-dataset variance alongside cross-dataset box plots.
2. Add an ablation experiment removing `estimated_selectivity` from the input features. Report whether performance changes meaningfully — either outcome is informative.
3. Specify exactly how fine-tuning subsets (250/500/1000) are sampled (random, stratified, etc.).
4. Release model code and pre-trained checkpoints alongside the benchmark data to improve reproducibility.
5. Add a small set of 3-table join queries to demonstrate extensibility (even if just as a proof-of-concept in an appendix).

## Score and Decision

The paper makes a genuine and timely contribution: a diverse, multi-dataset benchmark with pre-computed query cardinalities and open-source infrastructure that can meaningfully advance research on pre-trained cardinality estimation models. The benchmark fills a real gap — existing CE benchmarks use only 1–2 datasets and cannot support zero-shot model training. The experiments, while illustrative, demonstrate the benchmark's utility and yield a non-trivial finding (fine-tuning efficiency).

The verified weaknesses (variance reporting, estimated_selectivity feature, simplified baseline comparison) are real but minor relative to the paper's primary contribution. None threaten the core value of the released benchmark. The paper should be accepted with a request to address the minor experimental gaps during revision.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>