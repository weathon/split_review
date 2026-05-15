Now I have a thorough understanding of the paper and can verify the reviewer claims against the actual paper content. Let me compile the final review.

---

## Summary

CardBench is a benchmark for learned cardinality estimation containing 19–20 real-world databases, thousands of SQL queries (single-table filters and binary joins) with pre-computed true cardinalities, and open-source infrastructure for statistics calculation and query generation. The paper evaluates GNN and graph transformer models under three regimes—instance-based, zero-shot, and fine-tuned—finding that zero-shot CE is challenging (especially for joins) but that fine-tuning with as few as 500 samples recovers accuracy comparable to instance-based models.

## Strengths

- **Large-scale, multi-dataset benchmark that advances beyond prior work.** CardBench spans 19–20 real-world databases across diverse domains, far exceeding prior benchmarks that relied on 1–2 datasets (JOB, STATS, SE/IMDB). This diversity is essential for training and evaluating pre-trained/zero-shot CE models. The open release of the infrastructure and pre-computed training data (requiring 7 CPU-years of query execution) significantly lowers the entry barrier for the community.

- **Systematic investigation of zero-shot and fine-tuned transfer for CE.** The paper studies three distinct configurations (instance-based, zero-shot, fine-tuned) using two architectures (GNN, graph transformer), providing a clear picture of where pre-training helps and where it fails. The finding that fine-tuned models achieve comparable accuracy to instance-based models with roughly half the training data (Figures 3–4) is practically valuable and well-supported by the sample-efficiency analysis.

- **Careful feature design for transferability.** The models use only dataset-agnostic statistics (row counts, percentiles, null fractions, correlations) and exclude dataset-specific identifiers (table/column names). This design choice, validated by the experiments, is critical for zero-shot generalization and is a thoughtful contribution to the literature on transferable learned CE.

## Weaknesses

### Fatal
None.

### Major

- **No comparison against any existing learned cardinality estimator.** The paper evaluates only two custom models (GNN, graph transformer) and a heuristic baseline. To substantiate the claim that CardBench "enables systematic evaluation" of CE methods and "track[s] progress," the benchmark must be validated by benchmarking at least one prior published learned estimator (e.g., MSCN, DeepDB, NeuroCard, or a representative from those cited in Section 2). Without this, the paper's experimental contribution is isolated to the authors' own architecture choices and the benchmark's discriminative power remains unproven.

- **Baseline description overstates how well it represents modern DBMS.** The paper claims (Section 5.2) that the independence/uniformity baseline "represents heuristics employed in conventional DBMS such as PostgreSQL." Modern PostgreSQL uses histograms, most-common-value lists, multi-column statistics, and extended statistics — considerably more sophisticated than the paper's simple independence assumption. While this does **not** invalidate the paper's core findings (which primarily compare model configurations against each other, not against the baseline), the overstatement should be corrected and a more realistic traditional baseline would strengthen the work.

### Minor

- **Query complexity is limited.** CardBench includes only single-table filter queries and binary joins. Real-world CE involves multi-way joins, subqueries, OR/NOT predicates, and aggregates. The paper acknowledges that "[binary] joins are harder" (Section 3) but the benchmark's scope excludes these challenges. While not a fatal flaw—the benchmark can be extended—this narrow query space reduces the relevance of the zero-shot and fine-tuned findings for realistic workloads.

- **Inconsistent dataset count.** The abstract, introduction, and experiments consistently refer to "20 distinct databases," but Table 1 lists only 19 datasets. This discrepancy (whether a counting error or a missing entry) must be resolved before publication.

- **No statistical significance or variance reporting.** Results are aggregated across datasets with box plots but no confidence intervals or paired significance tests. Given that only a single run per configuration is reported, the variance across random seeds or dataset splits is unknown, which limits the strength of comparative claims (e.g., "fine-tuned models outperform instance-based with 500 samples").

### Trivial

- **Hyperparameter and optimization details are sparse.** The model descriptions (Section 4) lack architectural specifics (number of layers, hidden dimensions, learning rate, optimizer, dropout, convergence criteria), making reproduction more difficult than necessary.

- **The "Broader Impact" section appears empty** (line 363), followed by "Conclusion and Broader Impact" which contains the actual discussion. Likely a formatting artifact but should be cleaned up.

## Nice-to-Haves

- Include a modern DBMS estimator (PostgreSQL EXPLAIN cardinalities with default statistics) as a secondary baseline to ground the comparison to production systems.
- Add per-dataset results (table or heatmap of P50/P95 q-errors) to show which datasets are hardest and whether fine-tuning helps uniformly.
- Perform an ablation of input features to identify which statistics drive zero-shot performance.
- Provide training curves to support the claim about zero-shot overfitting (Section 5.1).

## Removed Points

*These points were flagged by reviewers but are removed for the reasons stated below. Treat them with caution.*

- *"The baseline is a straw man that makes traditional CE appear far worse than it is in practice — the experimental foundation is unsound"* — **Removed as overreach.** The baseline comparison is a supporting experiment, not the paper's core claim. The paper's main findings (benchmark release, fine-tuning sample efficiency, zero-shot difficulty) are independent of this baseline. The baseline overstatement is still a genuine concern and is retained in the Major Weaknesses section above, but characterizing it as a fatal structural flaw that "invalidates the experimental foundation" is incorrect.
- *"The paper understates benchmarks like STATS"* — **Removed.** The paper's characterization (Section 2) that existing benchmarks contain "one or two different datasets, which is clearly not sufficient for testing pre-trained models" is factually correct and not a weakness.
- *"The query generator description is too brief"* — **Removed as trivial.** The generator produces queries with 1–4 single-table predicates and 1–3 per-table join predicates, and the filtering process (duplicates, zero results, timeouts) is explained. More detail would be nice but the description is adequate.
- *"Results show only visual inspection, no numerical comparisons for sample efficiency"* — **Partially removed.** The paper does provide numerical comparisons (lines 358–359: "average P50 and P95 Q-errors across 20 datasets are: 1.57 & 280 for instance-based... 1.32 & 120 for fine-tuned"). The claim about "twice the data" is based on the figures, which could be made more explicit, but it is supported.
- *"Strength #7: Compares against a heuristic baseline that mimics conventional DBMS assumptions"* — **Removed (conflicts with verified weakness).** The strength claims the baseline "quantitatively shows the limitations of traditional estimators," but the weakness that the baseline is oversimplified and not representative of modern DBMS is a verified concern. Per the instructions, when a strength and a verified weakness disagree, the weakness wins.

## Novel Insights

None beyond the paper's own contributions. The reviewers' comments are constructive but do not uncover a novel interpretation or framing that the paper itself does not provide.

## Suggestions

1. **Add at least one existing learned CE method as a baseline** (e.g., a simple data-driven model like MSCN or a representative workload-driven model). This is the single most important addition to validate the benchmark's utility for method comparison.
2. **Replace or augment the heuristic baseline** with PostgreSQL EXPLAIN cardinalities (using default statistics) or another production-grade traditional estimator. If this is infeasible, temper the claim that the baseline "represents heuristics employed in conventional DBMS such as PostgreSQL."
3. **Resolve the 19 vs. 20 dataset discrepancy** — either add the missing dataset to the table or correct the text.
4. **Report hyperparameters and model selection details** (learning rate, hidden dimensions, number of layers, optimizer, convergence criteria) in the main text or appendix for reproducibility.
5. **Add a small set of multi-way join queries** (3–4 tables) to demonstrate the benchmark's extensibility and to test whether the zero-shot and fine-tuned findings hold for harder queries.

## Score and Decision

The paper's core contribution — a diverse, open-source benchmark with pre-computed training data for learned cardinality estimation — is timely and valuable to the community. The experimental findings on fine-tuning sample efficiency are interesting and well-supported. However, the experimental validation is incomplete in two significant ways: no comparison against existing learned CE methods, and an overstated baseline description. These gaps do not invalidate the benchmark contribution but do limit the strength of the paper's empirical claims.

The paper makes a real contribution that merits publication, contingent on addressing the most critical gaps (particularly adding baseline comparisons to existing learned methods and correcting the dataset count). I recommend **acceptance with major revisions**.

**Originality**: Good — CardBench fills a clear gap (lack of multi-dataset CE benchmarks for pre-trained models).

**Importance of research question**: High — accurate CE is critical for query optimization, and pre-trained models are a promising direction.

**Claims well supported**: Partially — the fine-tuning finding is well-supported, but the lack of existing learned CE baselines weakens claims about the benchmark's utility.

**Soundness of experiments**: Adequate but incomplete — the comparisons between model configurations are sound, but missing baselines and the over-simplified heuristic baseline are weaknesses.

**Clarity of writing**: Good — clear structure, well-motivated.

**Value to research community**: High — the benchmark release and pre-computed data will enable broader participation in CE research.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>