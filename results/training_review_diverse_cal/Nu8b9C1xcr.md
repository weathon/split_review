Now I have thoroughly verified all claims. Let me produce the final consolidated review.

---

## Summary

This paper releases CardBench, a benchmark for learned cardinality estimation containing 20 real-world databases, thousands of annotated single-table and binary-join queries with pre-computed true cardinalities (costing ~7 CPU-years to compute), and open-source scripts for generating further queries and statistics. The authors also train GNN and graph transformer models under instance-based, zero-shot, and fine-tuned setups to demonstrate the benchmark's utility. The primary contribution is the benchmark itself—it fills a clear gap (existing CE benchmarks use only 1–2 datasets, making them unsuitable for pre-trained / zero-shot research) and the release of pre-computed labels dramatically lowers the entry barrier for ML researchers.

## Strengths

1. **Large-scale, diverse benchmark for pre-trained CE**: CardBench provides 20 real-world datasets with thousands of queries each, directly enabling systematic training and evaluation of zero-shot and fine-tuned CE models—something prior benchmarks (JOB with 1 dataset, CEBench with 2 datasets) cannot support for pre-training approaches. This is the paper's central contribution and it is genuinely valuable.

2. **Open-source release with pre-computed true cardinalities**: The authors release scripts for statistics calculation, SQL query generation, annotated query graph creation, and—critically—the pre-computed training data with true cardinalities. Given that executing the queries cost ~7 CPU-years on BigQuery, this release saves future researchers enormous compute. This meaningfully lowers the barrier to entry.

3. **Principled transferable feature design for zero-shot generalization**: Features are deliberately restricted to dataset-agnostic signals (table row counts, column histograms, correlation values, etc.) and exclude dataset-specific identifiers like table/column names (Section 4.1, Table 2). This design choice is methodologically sound for enabling zero-shot and fine-tuning experiments.

4. **Systematic evaluation across two query complexities and three setups**: Both single-table and binary-join workloads are evaluated with GNN and graph transformer models under instance-based, zero-shot, and fine-tuned configurations (Sections 5.2–5.3). This provides a useful baseline map of where learned CE stands and where it struggles (e.g., zero-shot on joins).

5. **Demonstrated sample-efficiency of fine-tuning**: Fine-tuned models with ~500 samples achieve accuracy comparable to instance-based models trained on ~1000 samples, with training time dropping from ~1.3hr to ~11min for the GNN (Section 5.3). This finding, while awaiting tighter statistical confirmation, points toward a practical path for reducing deployment overhead.

## Weaknesses

### Fatal
None. The core benchmark contribution is real, timely, and valuable. No identified weakness invalidates the paper's central claim of releasing a useful multi-dataset CE benchmark.

### Major

1. **Baseline comparison is overclaimed and uninformative.** The paper frames its baseline as "heuristics employed in conventional DBMS such as PostgreSQL" (Section 4.2), but the baseline is a simplistic independence-assumption model that computes predicate selectivity via multiplication and assumes join cardinality from the larger table's scan output. This is substantially weaker than what PostgreSQL actually uses (one-dimensional histograms, MCV lists, multi-column statistics). The paper then claims "learning-based models significantly outperform the baseline" (Section 5.2.2). Any reader familiar with DBMS internals will recognize the baseline as a straw man rather than a meaningful comparison. While the paper's contribution is the benchmark (not beating PostgreSQL), this overclaim and the absence of even a single histogram-based production CE baseline weaken the experimental showcase. *Why it matters:* The experimental section is meant to demonstrate the benchmark in action, but the comparison against an artificially weak baseline makes the demonstration far less informative than it should be.

2. **Lack of statistical rigor in experimental evaluation.** Every accuracy number comes from a single training run per configuration per dataset (Section 5.2: "We run a single experiment on each of the 20 test datasets"). There are no confidence intervals, no multiple seeds, and no repeated trials reported. The box plots show variance *across datasets* but hide run-to-run variance. The sample-size experiments in particular (Figures 3 and 4) use a single random draw per training subset size—with sample sizes as small as 250, this is highly sensitive to which queries happen to be selected. *Why it matters:* For a benchmark paper intended to serve as a reference point for future work, trusting single-run numbers is insufficient. Without error bars, readers cannot assess whether the reported improvements (e.g., fine-tuning vs. instance-based) are statistically meaningful or within the noise floor.

### Minor

1. **Generated queries lack characterization.** The paper provides almost no analysis of whether the generated queries reflect realistic CE challenges. Key properties—filter selectivity distributions, number of predicates, join selectivity ratios, degree of cross-column correlation—are unreported. There is no comparison against established query workloads like JOB. The benchmark is still useful without this characterization, but it makes it harder for users to understand what kind of difficulty the queries pose and whether the benchmark stresses CE models in ways that transfer to real deployments.

2. **Dataset count discrepancy.** The paper consistently states there are 20 datasets (abstract, introduction, experimental setup), but Table 1 lists only 19 entries. A 20th dataset is referenced in the zero-shot setup ("the remaining 20th dataset") but is missing from the table. This is a minor but distracting inconsistency.

### Trivial

1. **Empty "Broader Impact" section header.** An isolated `\section{Broader Impact}` (line 363) appears before `\section{Conclusion and Broader Impact}` (line 369) with no content between them—likely a LaTeX artifact that should be removed.

## Nice-to-Haves

- **Add PostgreSQL's actual CE estimates** (via `EXPLAIN`) as an additional baseline. This would address the most significant concern about the experimental section and would make the results directly relevant to practitioners.
- **Repeat experiments with 3–5 random seeds** and report median q-errors with error bars. For expensive zero-shot transformer training (11.8hr), even 2–3 runs would provide meaningful stability signals.
- **Characterize generated query properties** such as selectivity distributions, predicate counts, and correlation patterns, ideally with a comparison to JOB or real query logs.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Fine-tuning details are missing (learning rate, frozen layers, etc.)"** — The paper mentions max training epochs (20 for zero-shot, 100 otherwise) and training times. Finer hyperparameter details (learning rate, optimizer, batch size, layer freezing strategy) are standard for an appendix section, which the parser may have stripped. Based on the hard rules, missing appendix content that may exist in the original submission should not be counted as a weakness.
- **"Model architecture specifics too sparse (number of layers, hidden dims, attention heads)"** — The GNN references the prior work [carsten] for detailed design, and the Transformer references Graphormer [ying2021transformers]. Architecture dimensions are appropriate for an appendix, which may have been stripped by the parser.
- **"The baseline comparison is too weak (overall assessment that it's fatal)"** — While the baseline overclaim is a real issue (kept as a Major weakness above), the reviewer's assertion that this makes the experimental section "uninformative" and that the paper cannot serve as a reference is too harsh given that the benchmark itself (not the experimental showcase) is the primary contribution. The baseline weakness is significant but does not invalidate the benchmark.

## Novel Insights

None beyond the paper's own contributions. The reviews surface important methodological gaps (baseline overclaim, statistical rigor) but do not contribute new technical insights beyond what careful reading of the paper would reveal.

## Suggestions

- Replace or supplement the baseline with PostgreSQL's actual cardinality estimates (via `EXPLAIN`) to make the comparison meaningful and remove the overclaim that the current baseline "represents ... PostgreSQL."
- Correct the dataset count in Table 1 (reconcile 19 vs. 20) and ensure consistency throughout.
- Add error bars by repeating key experiments (at minimum the instance-based and fine-tuned setups, where training is cheaper) with multiple random seeds.
- Add a brief characterization of generated queries (selectivity distributions, join ratios) to help users calibrate benchmark difficulty.
- Remove the stray empty "Broader Impact" section header.

## Score and Decision

The paper's core contribution—a diverse, multi-dataset benchmark with pre-computed cardinalities and open infrastructure—is timely, well-motivated, and fills a genuine gap in the learned CE landscape. However, the experimental section that showcases the benchmark suffers from two significant weaknesses: a baseline that is overclaimed and uninformative, and a single-run methodology without statistical confidence measures. The benchmark itself remains valuable, and both issues are addressable. The paper should be accepted conditional on correcting the baseline overclaim (and ideally adding a stronger baseline) and on providing evidence of experimental stability.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>