Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper introduces SQL-GEN, a framework for generating high-quality synthetic Text-to-SQL training data for any SQL dialect by using dialect-specific tutorials to guide an LLM in expanding seed templates and generating question-SQL pairs. The paper also proposes a Mixture-of-Experts (MoE) initialization method that merges dialect-specific fine-tuned LLMs by initializing expert MLP layers from expert models, using SLERP to merge self-attention layers, and initializing routers with dialect-specific keyword hidden states. Experiments across SQLite, PostgreSQL, and BigQuery with three model families (CodeLlama 7B, CodeGemma 7B, Codestral 22B) show that SQL-GEN synthetic data substantially outperforms existing synthetic datasets (Gretel, SQL Create Context) and narrows the gap with human-annotated BIRD data, while the MoE model achieves the best overall accuracy across dialects.

## Strengths

- **SQL-GEN synthetic data yields large and consistent gains over existing synthetic datasets across all three dialects and model sizes.** On SQLite (BIRD dev, CodeLlama 7B), SQL-GEN achieves 38.33% EX vs. Gretel 26.01% and SQL Create Context 18.31%. Similar patterns hold for BigQuery (33.53% vs. 26.73% and 10.84%) and PostgreSQL (39.22% vs. 28.05% and 13.35%). These gains are consistent across CodeLlama 7B, CodeGemma 7B, and Codestral 22B (Tables 3–5).

- **SQL-GEN narrows the gap with human-annotated data to under 2 percentage points.** On SQLite BIRD dev with CodeLlama 7B, SQL-GEN (38.33%) trails the BIRD train set (40.22%) by only 1.89pp. On PostgreSQL BIRD, the gap is 5.15pp (39.22% vs. 44.37%), and on BigQuery BIRD, it is 4.51pp (33.53% vs. 38.04%).

- **Data augmentation with SQL-GEN yields up to 5.6% improvement over the BIRD train set alone**, with controlled epoch budgets (1 epoch for combined 20K, 2 epochs for BIRD-only 10K). This is substantially larger than previous augmentation results (1.5% from prior work on the same model) (Table 5).

- **The proposed MoE initialization produces a unified multi-dialect model achieving the best overall accuracy (35.44%),** outperforming individual experts (best: 32.71%), SLERP merging (33.77%), TIES (31.1%), DARE (29.94%), and a generalist MoE trained on 40K samples (33.43%) (Table 6).

- **Database adaptation with zero human annotation** — generating 10K synthetic samples on BIRD dev databases yields 38.78% EX, only 1.44% below the 10K human-annotated BIRD train set. In-context learning with 10 synthetic examples improves accuracy by +10.12% over zero-shot (Table 4).

## Weaknesses

### Fatal
None.

### Major

- **The MoE initialization is not properly ablated, so its individual contribution cannot be isolated.** There is no comparison where a randomly initialized MoE of the same architecture is fine-tuned on the same 20K/1-epoch data; the generalist MoE baseline is trained on 40K samples and initialized from the base CodeLlama 7B rather than from the proposed keyword-based initialization. Without this control, the 2.01pp improvement of the fine-tuned MoE (35.44%) over the generalist MoE (33.43%) — which had *double* the training data — cannot be confidently attributed to the initialization method versus other architectural advantages. This is the paper's main methodological gap.

- **Several key training and generation details are missing, impeding reproducibility.** The LLM used for the main generation pipeline (M1 for template expansion and sample generation, M2 for quality checking) is not specified — Gemini-1.5-pro is only mentioned for the Database Adaptation experiment. LoRA rank, learning rate, batch size, and optimizer are not reported. The template expansion thresholds θ and β are never specified. Training epochs for the main SQLite/PostgreSQL/BigQuery experiments (Tables 3, 4, BigQuery table) are not stated. While the data augmentation experiment controls for epochs, the core comparisons do not. These details are needed for reproducibility and for proper interpretation of the magnitude of reported gains.

### Minor

- **The abstract's phrasing "over existing methods" for the 20% improvement is imprecise.** The ΔEX column in the tables is explicitly measured relative to zero-shot (the paper states "calculate the performance gains for each method relative to zero-shot"), and the paper would benefit from clarifying what the comparison baseline is. While the 20% number is verifiable against SQL Create Context (18.31% → 38.33%), the phrasing risks misleading readers into thinking the comparison is against the strongest existing method rather than the weakest baseline.

- **No native BigQuery benchmark is used for evaluation.** Unlike PostgreSQL (which includes the Pagila dataset — real PostgreSQL-specific queries), the BigQuery experiments only evaluate on BIRD queries transpiled to BigQuery. This weakens the claim of dialect-specific evaluation for BigQuery.

- **No variance or statistical significance is reported.** None of the tables report multiple runs or confidence intervals. Given the known variance in LoRA fine-tuning, this limits confidence in the magnitude of reported improvements.

- **No dedicated limitations section.** The paper discusses failure cases of transpilation (20% error rate for BigQuery→SQLGlot) but does not discuss failure modes of the synthetic data pipeline itself — e.g., tutorials being incorrect/outdated, LLM hallucinations of unsupported functions, or the cost of the two-LLM quality check.

- **The keyword diversity analysis (Figure 2/3) is a proxy metric.** While it shows SQL-GEN queries have more dialect-specific keywords than baselines, diversity does not guarantee correctness or training usefulness. The primary evidence (execution accuracy) is stronger; the diversity analysis is a minor supporting observation.

### Trivial

- The "MoE 3×7B (ours)" row in Table 6 (no fine-tuning, 32.56%) underperforms SLERP merging (33.77%), which the paper acknowledges but could be stated more prominently. The contribution depends on the full fine-tuned pipeline.

## Nice-to-Haves

- **A randomly-initialized MoE ablation** trained on the same 20K/1-epoch data would cleanly isolate the initialization contribution.
- **A native BigQuery benchmark** (analogous to Pagila for PostgreSQL) would strengthen the dialect-specific claims for BigQuery.
- **A cost analysis** would be useful — generating 20K samples with an LLM API has non-trivial cost, and a comparison to human annotation cost (which the paper qualitatively mentions for the Database Adaptation experiment) would strengthen the practical motivation.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. "The BigQuery results table (Table 2) is garbled and uninterpretable" — Removed per parser-artifact rule. The garbled rows (lines 233–237) are a PDF extraction artifact; the structured rows (lines 227–231) show valid data.

2. "The 7.3% claimed improvement in the introduction is actually over zero-shot, not MoE vs. experts" — Factually wrong. Verified: the 7.3% corresponds to the MoE fine-tuned model (32.25) vs. the SQLite expert (25) on BigQuery BIRD. Zero-shot CodeLlama 7B on BigQuery BIRD is 16.57, giving +15.68, not +7.3.

3. "The MoE comparison is unfair because the proposed method uses 20K samples vs. generalist MoE's 40K" — Removed per hard rule: the asymmetry favors the baseline (generalist MoE has more data), not the proposed method. The proposed method achieving higher accuracy with less data *strengthens* the claim.

4. "Missing related works" — Per instructions, I cannot verify the existence of missing related works and must not mention these.

5. "The synthetic vs. human comparison is unfair because synthetic has 20K vs. human's 10K" — The paper is transparent about dataset sizes. If anything, the synthetic data having more data but still slightly underperforming human data (38.33% vs. 40.22%) is an honest result. The framing as "narrowing the gap" is accurate.

6. Requests to add citations for the motivation statement about users managing multi-dialect databases — This is a standard motivating observation, not a research claim requiring a citation.

## Novel Insights

The review surfaces one genuinely novel observation beyond the paper's own contributions: the SQL-GEN data generation pipeline's design — using LLMs to expand seed templates guided by dialect-specific tutorials, then populating them with database values — is an elegant solution to the cold-start problem for under-resourced SQL dialects. The paper's core contribution (synthetic data quality) is well-supported. The MoE initialization method is interesting but under-evidenced; the most novel aspect is the keyword-based router initialization, but the ablation gap means its value remains suggestive rather than proven.

## Suggestions

1. Add an ablation with a randomly initialized MoE (same architecture) trained on the same 20K samples to isolate the initialization contribution.
2. Clarify the abstract's comparison baseline — replace "over existing methods" with the specific comparison (e.g., "over prior synthetic datasets" or specify the strongest baseline outperformed).
3. Specify the LLM(s) used for the main generation pipeline (M1, M2), the training hyperparameters (LoRA rank, learning rate, batch size, optimizer, epochs), and the numerical values of thresholds θ and β.
4. Add a native BigQuery evaluation dataset, even a small curated set, to match the rigor of the PostgreSQL evaluation (Pagila).
5. Add a limitations section discussing failure modes of the synthetic data pipeline.
6. Report variance across multiple runs (at least 2–3 seeds) for key results.

## Score and Decision

The paper's core contribution — the SQL-GEN synthetic data generation pipeline — is well-motivated, methodologically sound, and convincingly demonstrated across three dialects, three model families, and multiple benchmarks. The data quality results are the strongest part of the paper. The MoE initialization method is a secondary contribution that is interesting but incompletely evaluated — the missing ablation prevents attributing gains to the initialization specifically. The reproducibility gaps (unspecified generation LLM, unstated hyperparameters, missing thresholds) are addressable. The overall paper makes a solid empirical contribution to multi-dialect Text-to-SQL and deserves acceptance after addressing the major reproducibility concerns.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>