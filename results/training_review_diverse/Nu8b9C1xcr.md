Now I have a thorough understanding of the paper. Let me synthesize the final review by carefully cross-checking each reviewer claim against the actual paper content.

---

## Summary

This paper releases **CardBench**, a benchmark for learned cardinality estimation (CE) consisting of 20 diverse real-world databases, a query generator producing single-table and binary-join queries, pre-computed true cardinalities (requiring 7 CPU years of execution), and open-source infrastructure for computing statistics, generating queries, and creating training data. The paper evaluates GNN and transformer-based models in three setups (instance-based, zero-shot, fine-tuned), finding that zero-shot CE struggles significantly with joins but pre-trained models can achieve instance-comparable accuracy with modest fine-tuning.

## Strengths

1. **Largest and most diverse benchmark for learned CE.** CardBench includes 20 distinct real-world databases with thousands of queries each, far exceeding prior benchmarks (JOB: 1 dataset, STATS: 1, CEB: 2). This diversity is essential for training and evaluating zero-shot/generalizable CE models — a direction of growing importance. The paper explicitly contrasts with prior benchmarks in Section 2 and documents dataset/query counts in Table 1.

2. **Release of expensive pre-computed training data and open-source infrastructure.** The benchmark provides pre-computed query graphs with true cardinalities that cost 7 CPU years to generate (line 103). By releasing both the training data and the full pipeline (statistics calculation, query generation, graph construction), the paper dramatically lowers the barrier to entry for ML and DB researchers working on learned CE (as stated in the Abstract and Section 3).

3. **Demonstration of sample-efficient fine-tuning.** The experiments show that fine-tuning a pre-trained model with as few as 500 samples achieves accuracy comparable to instance-based models trained on 1000 samples (Section 5.4, Figures 5–6). For binary joins, the fine-tuned GNN achieves P50 q-error 1.32 vs. instance-based 1.57 at 500 samples — a concrete quantitative demonstration of pre-training's practical benefit.

4. **Systematic evaluation across multiple configurations.** The paper evaluates GNN and transformer architectures under three well-defined setups (instance-based, zero-shot, fine-tuned) with consistent methodology, enabling direct comparison and providing actionable guidance for future research (Section 5.1).

5. **Dataset-agnostic feature design.** By excluding dataset-specific identifiers (table/column names) and using only transferable features (rows, null_frac, percentiles, correlations, etc.), the benchmark is explicitly designed to support generalizable zero-shot models (Table 2, Section 4.1). This design choice is validated by the experiments.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Baseline characterization is somewhat imprecise for binary joins.** The paper states the baseline "represents heuristics employed in conventional DBMS such as PostgreSQL" (line 307). For single-table queries, the independence-assumption baseline is reasonable. However, for binary joins, the baseline assumes PK-FK semantics and simply uses the larger table's scan cardinality (line 311). Modern DBMS like PostgreSQL use histograms on join columns and MCV lists for join selectivity, which is more sophisticated than this baseline. **However, this does not undermine the paper's main claims**: the baseline's binary-join P50 q-error is already 55.54 and P95 is 4.4×10^6 — so poor that even a more realistic PostgreSQL baseline would still be dramatically outperformed by learned models. The imprecision is in the *description* of the baseline, not the conclusions drawn from it.

2. **Per-dataset results would strengthen the analysis.** The experiments report aggregate box plots across 20 datasets (Figures 3–6), but individual dataset results are not shown. The high variance visible in the box plots (especially for zero-shot models on binary joins) raises the question of which datasets drive the failures. Reporting per-dataset P50/P95 q-errors in a table would make the benchmark more useful for diagnosing model weaknesses and guiding future improvements.

### Trivial

- The binary-join baseline formula (described inline in Section 5.1) could be accompanied by a citation or a more formal mathematical statement for clarity.

## Nice-to-Haves

- **Multi-join queries (three or more tables) as future work.** The paper explicitly acknowledges this as a future extension: "we hope that the benchmark itself will be extended with new datasets and more complex queries using the tools and code we provide" (line 376). The current binary-join results already demonstrate that joins are substantially harder for zero-shot models than single-table queries, making multi-join queries a natural next step. This is not a weakness of the current paper — the benchmark infrastructure supports extension, and the paper is transparent about its scope — but adding multi-join queries would increase the benchmark's impact.

- **A comparison table with existing CE benchmarks** (JOB, STATS, CEB, etc.) systematically contrasting number of datasets, number of queries, query complexity, and domain coverage would strengthen the positioning of CardBench relative to prior work. The paper makes these comparisons textually in Section 2 but a summary table would be helpful.

- **Broader reporting of dataset characteristics** (e.g., row counts per table, number of columns, data types, correlation strengths) would help users interpret benchmark difficulty and select appropriate datasets for their experiments.

- **Clarification on query filtering.** The paper states that duplicate, zero-result, and timeout queries were filtered (line 140) but does not report the fraction filtered per dataset. Reporting these fractions would aid reproducibility.

## Removed Points

These points were raised by reviewers but are removed or downgraded after verification against the paper:

- **"Limited query complexity undermines the benchmark's stated generality"** — REMOVED. The paper is transparent about its scope throughout. The title "A Benchmark for Learned Cardinality Estimation in Relational Databases" is appropriate for a benchmark covering single-table and binary-join queries across 20 databases. The abstract, introduction, and Section 3 all clearly state that the benchmark includes these two query types. The paper explicitly notes that the infrastructure can be extended to more complex queries (line 41) and calls for "more research... on more complex queries" (line 80). This is an honest scope choice, not an overclaim.

- **"The estimated_selectivity feature limits learned models"** — REMOVED. The paper shows that learned models *dramatically* outperform the baseline (which uses the same per-predicate selectivities with the independence assumption). The feature is one of many inputs; the model can learn to correct the heuristic's errors. The empirical results contradict this concern.

- **"The baseline is a strawman; claim that learned models are better is unreliable"** — DOWNGRADED to Minor (see above). The baseline's P50 q-error of 55.54 and P95 of 4.4×10^6 for binary joins is so poor that even a more sophisticated PostgreSQL baseline would not change the qualitative conclusion that learned models dramatically outperform traditional heuristics on this workload.

- **"Missing statistical significance / confidence intervals"** — REMOVED. Single-run evaluation at this scale is standard practice for CE benchmarks; the box plots with 20 data points per configuration already convey variability.

- **"Paper does not clarify how duplicate queries or zero-result queries are handled"** — The paper states this at line 140. The fraction filtered is a minor detail that can be added.

- **Graph transformer punctuation artifact ("}:")** — REMOVED. This is a parser artifact, not an author error.

- **"7 CPU years breakdown"** — REMOVED. This is a minor clarification, not a weakness affecting the paper's contributions.

## Novel Insights

None beyond the paper's own contributions. The review does surface one structural observation worth noting: the paper's core value proposition is the *infrastructure and pre-computed data* for learned CE research, yet the baseline criticism focuses on a component (the traditional baseline) that is peripheral to the benchmark's primary purpose. The benchmark's enduring value is in providing 20 datasets × thousands of queries × true cardinalities and an extensible pipeline — not in its baseline comparison, which is a sanity-check experiment.

## Suggestions

1. In the baseline description, replace "represents heuristics employed in conventional DBMS such as PostgreSQL" with a more precise statement: describe what the baseline actually does and note that it is a simplified heuristic (not a full reproduction of any specific DBMS). Or, if feasible, replace the binary-join baseline with actual PostgreSQL estimates (via EXPLAIN) to make the comparison more directly relevant to practitioners.

2. Add a supplementary table with per-dataset P50 and P95 q-errors for each model configuration. This would substantially increase the benchmark's diagnostic utility without requiring new experiments.

3. Include a systematic comparison table with existing benchmarks (JOB, STATS, CEB, etc.) covering number of datasets, domains, query types, and whether they support zero-shot evaluation.

## Score and Decision

**Originality:** Good. CardBench is the first large-scale, multi-dataset benchmark specifically designed for pre-trained/zero-shot CE. The combination of 20 databases, diverse query workloads, and pre-computed training data is novel relative to prior benchmarks (JOB, STATS, CEB) that cover 1–2 datasets.

**Importance of research question:** High. Cardinality estimation is a long-standing bottleneck in query optimization. The recent direction toward pre-trained/generalizable CE models requires exactly the kind of benchmark infrastructure CardBench provides.

**Claims well-supported:** Yes. The main claims — that the benchmark provides diverse training data, that zero-shot CE is challenging (especially for joins), and that fine-tuning is sample-efficient — are all supported by the experimental results.

**Soundness of experiments:** The experimental design is systematic and well-structured. The main limitation is the baseline characterization (minor, see above). The experiments compare multiple model architectures and training configurations in a consistent framework.

**Clarity of writing:** The paper is clearly written and well-organized. The scope is transparently stated.

**Value to community:** High. The pre-computed training data saves enormous compute, the open-source infrastructure enables extension, and the 20-dataset benchmark enables a new class of experiments on generalizable CE.

**Overall:** This paper makes a genuine and substantial contribution to the CE research community. The weaknesses are minor and do not undermine the core contributions. The benchmark fills a clear gap — no existing benchmark provides enough datasets for training and evaluating zero-shot CE models.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>