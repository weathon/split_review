Now I have a thorough understanding of the paper and all claims. Let me produce the final consolidated review.

## Summary

This paper introduces SQL-GEN, a framework for generating high-quality synthetic Text-to-SQL training data for any SQL dialect (focusing on SQLite, PostgreSQL, and BigQuery) by using LLMs to expand seed templates guided by dialect-specific tutorials. The framework includes template expansion, sample generation, and quality checking. Empirically, models fine-tuned on SQL-GEN data substantially outperform those trained on existing synthetic datasets (Gretel, SQL Create Context) and narrow the gap with models trained on human-annotated BIRD data. The paper also proposes an MoE initialization method that merges dialect-specific expert models using SLERP-based self-attention merging and keyword-based router initialization. The MoE component shows modest but consistent improvements over model merging baselines.

## Strengths

- **SQL-GEN synthetic data yields large, consistent execution accuracy gains over existing synthetic datasets across all three dialects and multiple model sizes (7B–22B).** On SQLite BIRD dev set with CodeLlama 7B, SQL-GEN achieves 38.33% vs. Gretel's 26.01% and SQL Create Context's 18.31% (Table 3). On PostgreSQL BIRD, SQL-GEN reaches 39.22% vs. Gretel's 28.05% (Table 1). The gains hold across CodeGemma 7B and Codestral 22B, confirming robustness.

- **The template expansion approach using dialect-specific tutorials demonstrably yields higher dialect-specific keyword diversity than existing synthetic datasets.** Figure 2 (keyword distribution analysis) shows SQL-GEN queries contain substantially more dialect-specific keywords (e.g., BigQuery's STRUCT, PostgreSQL's ARRAY) than Gretel or SQL Create Context. The paper also identifies that SQL Create Context, intended for SQLite, erroneously contains BigQuery-specific keywords — highlighting a quality issue in prior data that SQL-GEN avoids.

- **SQL-GEN enables database adaptation without human annotation, performing close to the full BIRD train set.** Generating 10K synthetic samples on BIRD dev databases achieves 38.78% execution accuracy (CodeLlama 7B, Table 4), only 1.44% below training on 10K human-annotated BIRD samples (40.22%). This demonstrates practical utility for low-resource database scenarios.

- **Data augmentation with SQL-GEN synthetic data gives consistent improvements (up to +5.6% absolute) across all tested models.** Adding 10K synthetic samples to the BIRD train set boosts CodeLlama 7B from 40.22% to 45.82%, CodeGemma 7B from 45.63% to 51.10%, and Codestral 22B from 53.12% to 56.45% (Table 5). This significantly exceeds prior augmentation gains (~1.5%, Yang et al. 2024).

- **The MoE initialization approach (SLERP self-attention merging + keyword-based routing) outperforms all model merging baselines (SLERP, TIES, DARE) and the generalist MoE baseline.** The fine-tuned MoE 3×7B achieves 35.44% overall accuracy vs. the best baseline SLERP at 33.77% and the generalist MoE at 33.43% (Table 6). The "before fine-tuning" MoE (32.56%) also surpasses TIES (31.1%) and DARE (29.94%), validating the initialization itself.

## Weaknesses

### Fatal
None.

### Major

- **The BigQuery evaluation relies entirely on transpiled BIRD queries, which cannot verify whether SQL-GEN truly captures BigQuery-specific dialect features.** The paper argues that SQL-GEN teaches dialect-specific syntax, but the BigQuery test set consists of BIRD queries transpiled from SQLite (line 165 confirms that "for dialects other than SQLite, all queries from the baselines are transpiled"). Transpiled queries are inherently constrained by what the original SQLite query could express, so they do not require BigQuery-specific constructs like `STRUCT`, `ARRAY`, or `REGEX`. While the keyword analysis (Figure 2) provides indirect evidence that SQL-GEN's training data contains more dialect-specific keywords, this analysis is separated from task performance evaluation. The paper convincingly shows dialect-specific learning only for PostgreSQL (via the native Pagila benchmark). To fully support the claim of "bridging the dialect gap" for BigQuery, the authors need either a native BigQuery test set or a targeted evaluation on queries requiring BigQuery-only constructs. Alternatively, this limitation should be explicitly acknowledged and caveated.

### Minor

- **The "up to 20% improvement" claim in the abstract is ambiguous between absolute percentage-point gains and relative improvement, and imprecise in its scope.** The paper does not specify which interpretation is intended. From the data, the largest absolute gain over the best synthetic baseline (Gretel) is ~12% (SQLite CodeLlama 7B), while the largest absolute gain over SQL Create Context is ~23% (BigQuery CodeLlama 7B). Relative gains are far larger (40%+). Meanwhile the introduction separately states "4% to 27%" (line 28), which appears to use a different reference point. The paper should consistently state whether gains are absolute or relative and specify the comparison condition.

- **The claim that SQL-GEN "narrows the gap with models trained on large-scale human-annotated data" has variable support across dialects.** On SQLite dev set, the gap is narrow (SQL-GEN 38.33% vs. BIRD train 40.22% = 1.89 points). On PostgreSQL BIRD, the gap is larger (39.22% vs. 44.37% = 5.15 points, Table 1). The paper reports the former prominently but the latter with less emphasis. The claim should be qualified with the specific dialect and benchmark.

- **The MoE improvement over SLERP merging is small (35.44% vs. 33.77% = +1.67 absolute points) and no variance or significance measures are reported.** Given the small evaluation sets (e.g., Pagila likely has ~23 queries based on the reported percentages) and the single-run experimental design, the difference could be within the noise range. However, this is a secondary contribution and the main data generation results are not affected.

### Trivial
None.

## Nice-to-Haves

- A native BigQuery test set (even a small hand-curated one) would substantially strengthen the dialect-specificity claims.
- Reporting the number of API calls or tokens consumed by the SQL-GEN pipeline would help practitioners assess cost.
- For the MoE section, a routing analysis (e.g., what fraction of dialect-specific tokens are routed to the corresponding expert) would directly validate the design. The paper references such an analysis in the appendix (\Cref{MoE_token_routing}); if it already exists, summarizing key results in the main text would be beneficial.

## Removed Points

These points were identified by reviewers but are either factually incorrect, misunderstand the paper, or reflect inappropriate expectations. They are recorded here for transparency in case they prove useful, but they should **not** be considered valid criticisms.

- **"The MoE model has ~21B active parameters while baselines are 7B, so improvement may reflect capacity, not initialization."** → REMOVED (factually wrong). The paper explicitly states (line 122) that "only a subset of experts is activated for each token" and that MoE increases "modeling expressiveness without significantly increasing the compute budget." Furthermore, the paper includes a generalist MoE 3×7B baseline (same architecture, random initialization) that scores 33.43%, isolating the initialization effect to ~2%. The reviewer's claim of ~21B active parameters misunderstands how MoE routing works.

- **"Missing routing analysis for MoE"** → REMOVED (parser artifact). The paper references \Cref{MoE_token_routing} (line 356) for detailed analysis. This section was in the appendix, which was stripped during PDF parsing.

- **"Request for human evaluation of 100 generated pairs"** → REMOVED (scope creep). The paper already uses an LLM-as-judge quality check with a separate model to avoid bias, and references a quality-check ablation. Requiring human annotation for a synthetic data generation paper is not standard practice for this venue.

- **"Comparison to larger dense model (13B/34B) in MoE section"** → REMOVED (infeasible ask). Training and serving a CodeLlama 13B/34B dense model as a "compute-matched" baseline requires substantial resources beyond what's typical for academic submissions. The existing controls (generalist MoE 3×7B, generalist dense 7B, SLERP/TIES/DARE) are adequate.

- **"Computational cost of SQL-GEN not discussed"** → Moved to Nice-to-Haves. This is useful practical information but not a substantive weakness of the paper's scientific contribution.

## Novel Insights

The most interesting observation from the synthetic data experiments is that SQL-GEN's data — despite being entirely LLM-generated — generalizes more robustly across benchmarks than the human-annotated BIRD train set. On Pagila (a native PostgreSQL benchmark), the BIRD-tuned model drops to 19.56% (CodeLlama 7B) while the SQL-GEN-tuned model achieves 39.13%. This suggests that the template expansion process (which draws on diverse dialect tutorials rather than a fixed corpus) yields broader coverage of query patterns, mitigating the overfitting to benchmark-specific distributions that plagues human-annotated datasets. This has implications beyond multi-dialect settings: synthetic data generated via structured template expansion may produce more robust models than human-annotated data in any setting where the annotation process follows a narrow schema.

## Suggestions

1. Clarify the "up to 20%" claim: explicitly state whether this refers to absolute or relative improvement, and specify which dataset/baseline comparison yields this figure.
2. Either construct a small native BigQuery test set (e.g., hand-writing ~50 queries that use BigQuery-specific constructs like STRUCT, ARRAY, REGEX) or clearly acknowledge as a limitation that the BigQuery task evaluation relies on transpiled queries and therefore only the keyword analysis (Figure 2) supports dialect-specific learning for BigQuery.
3. Add a brief summary of the MoE routing analysis from the appendix to the main text to strengthen the MoE contribution.
4. Report the gap with human-annotated data separately per dialect rather than as a single undifferentiated claim.

## Score and Decision

**Originality:** The SQL-GEN pipeline is novel in its use of dialect-specific tutorials for template expansion, and the keyword-based MoE router initialization is a clean idea. Both contributions are clearly differentiated from prior work.

**Importance:** Multi-dialect Text-to-SQL is an underexplored but practically important problem. The paper demonstrates that SQL-GEN data can substantially reduce reliance on expensive human annotations for under-resourced dialects.

**Soundness:** The SQL-GEN data generation evaluation is thorough across three dialects, three model families, and multiple benchmarks. The MoE evaluation is less rigorous (no variance reporting, small gains) but is a secondary contribution.

**Clarity:** Generally well-written, though some quantitative claims (e.g., "up to 20%") are ambiguous.

**Value:** The SQL-GEN framework is a practical contribution that should be useful to practitioners working with non-SQLite databases. The data augmentation results (+5.6%) are practically meaningful.

The primary contribution (SQL-GEN data generation) is well-supported. The main concern — BigQuery evaluation relying on transpiled queries — is significant but fixable with either a native benchmark or an explicit caveat. The ambiguous "up to 20%" claim is a clarity issue, not a validity issue. The MoE contribution is modest but does not undermine the paper.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>