Now I have a thorough understanding of the paper and can verify each claim against the actual text. Let me compile the final review.

## Summary

2-3 sentence summary of the paper's contribution.

---

**Final review:**

## Summary

The paper introduces SQL-GEN, a framework for generating high-quality synthetic Text-to-SQL training data tailored to specific SQL dialects (SQLite, PostgreSQL, BigQuery) using seed templates, dialect-specific tutorials, and LLM-based generation with quality checks. It also proposes a Mixture-of-Experts (MoE) initialization method that merges dialect-specific expert models into a single multi-dialect model via SLERP-based self-attention merging and keyword-initialized routers. Extensive experiments across three model sizes (7B–22B) and multiple benchmarks show that SQL-GEN substantially outperforms existing synthetic datasets and that the proposed MoE model surpasses both individual experts and standard merging heuristics.

## Strengths

1. **SQL-GEN consistently and substantially outperforms existing synthetic datasets across dialects and model sizes.** On PostgreSQL BIRD with CodeLlama 7B, SQL-GEN achieves 39.22% execution accuracy vs. 28.05% for Gretel and 13.35% for SQL Create Context (Table 1). On SQLite BIRD dev set, it reaches 38.33% vs. 26.01% for Gretel (Table 3). These patterns hold across CodeGemma 7B and Codestral 22B and across all three dialects, demonstrating robustness.

2. **The proposed MoE initialization yields a multi-dialect model that outperforms single-dialect experts and all three standard merging baselines.** The fine-tuned MoE 3×7B model achieves 35.44% overall accuracy across SQLite, PostgreSQL, and BigQuery benchmarks, exceeding the best single-dialect expert (32.71%), SLERP (33.77%), TIES (31.1%), and DARE (29.94%) (Table 8). Notably, the proposed MoE achieves this despite being trained on only 20K samples (vs. 40K for the generalist MoE baseline), making the result more impressive, not less.

3. **Data augmentation with SQL-GEN yields gains (+5.6%) that far exceed prior work (+1.5%).** Adding 10K SQL-GEN synthetic samples to the BIRD training set improves CodeLlama 7B from 40.22% to 45.82%, and CodeGemma 7B from 45.63% to 51.10% (Table 7). The paper explicitly contrasts this with the +1.5% reported by Yang et al. (2024), demonstrating a clear and substantial advantage.

4. **Database adaptation shows SQL-GEN nearly matches human-annotated data without manual annotation.** Fine-tuning on 10K synthetic samples generated for BIRD development databases yields 38.78% on the BIRD dev set — only 1.44% below the model trained on 10K human-annotated BIRD samples (40.22%) (Table 5). ICL with synthetic demonstrations also yields +10.12% improvement on a held-out database without any weight update.

5. **Keyword diversity analysis quantifies a concrete advantage.** Figure 3 shows SQL-GEN queries contain more unique SQL keywords and substantially more dialect-specific keywords (e.g., STRUCT() for BigQuery) than Gretel or SQL Create Context, directly supporting the claim that SQL-GEN captures dialect-specific syntax better.

## Weaknesses

### Fatal
None.

### Major

1. **The LLMs used in the main SQL-GEN pipeline (M₁ and M₂ for template expansion, sample generation, and quality checking) are never identified.** The paper repeatedly refers to "an LLM" and "a different LLM" without specifying any model name, size, provider, or access method (Sections 3.1, Algorithm 1). The only named model is Gemini-1.5-pro, which is used exclusively for the Database Adaptation experiments (line 289), not the main pipeline. Since the quality and characteristics of the synthetic data depend entirely on the LLM choice, this omission is a structural reproducibility failure. Without this information, readers cannot reproduce the pipeline, compare it to alternatives, or assess whether the reported gains are tied to a specific model or generalize across LLMs. **The authors must explicitly name M₁ and M₂ (exact model, size, checkpoint, provider/open-source link) for the paper to be reproducible.**

### Minor

1. **No confidence intervals, error bars, or significance tests are reported for the MoE and merging results.** The absolute gains of the proposed MoE over baselines are 2–3 percentage points overall (Table 8). Without multiple seeds or statistical testing, it is unclear whether these differences are robust or within noise. This is common practice to add in revision and does not invalidate the results, but it weakens the precision of the claims.

2. **The "up to 20%" claim in the abstract, while technically accurate, over-represents gains against very weak baselines.** The largest improvements (e.g., +22.69 points vs. SQL Create Context on BigQuery) come from comparing against an extremely weak baseline (10.84% EX) that was never designed for BigQuery. Against stronger baselines like Gretel, the gains are smaller (6.8–12.3 points). The "up to" qualifier makes the claim formally correct, but it gives an imprecise impression of typical improvement magnitudes.

### Trivial
None.

## Nice-to-Haves

- Report the concrete hyperparameters of the generation pipeline: θ (template count threshold), β (pair count threshold), K (rows in quality check), temperature/sampling settings, and the top-K keyword count for routing initialization.
- Disclose whether the synthetic data, trained models, and code will be released to maximize community impact.
- A routing analysis visualization (currently deferred to the appendix, which was stripped by the parser) would be helpful to include in the main paper.

## Removed Points

- **Criticism about MoE comparison being unfair (40K vs 20K training samples):** The asymmetry favors the baseline (more data for the generalist MoE, less for the proposed MoE), which makes the proposed method's superior result *stronger* rather than weaker. Per evaluation rules, this is an intentional asymmetry that proves a stronger point. **Removed.**

- **Criticism about BigQuery table corruption (lines 233–237):** This is a PDF extraction artifact — the original submission does not have this issue. **Removed (parser artifact).**

- **Criticism about lack of overfitting evidence:** The paper explicitly provides evidence: the BIRD train set drops from 44.37% on PostgreSQL BIRD to 19.56% on Pagila, while SQL-GEN synthetic data maintains 39.13% on both (Table 1, rows for BIRD train set vs. Our synthetic dataset on Pagila). This is direct evidence of distribution mismatch/overfitting. **Removed (factually incorrect — evidence is present).**

- **Criticism about missing MoE routing analysis:** The paper references \Cref{MoE_token_routing} for detailed analysis. This content exists in the appendix, which was stripped by the parser. **Removed (appendix issue).**

- **Criticism about database adaptation table formatting:** A formatting/layout nitpick. **Removed.**

- **Criticism about missing related work:** Insufficient grounds to evaluate without external sources. **Removed.**

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Disclose the identities of both LLMs (M₁ and M₂) used in the SQL-GEN pipeline** — exact model name, size, checkpoint, and access method. This is the single most important revision for reproducibility.
2. **Add error bars or multi-seed runs** for the MoE and merging experiments (Table 8) to establish whether the observed 2–3 point gains are statistically significant.
3. **Calibrate the "up to 20%" claim** in the abstract to more precisely reflect the typical gain against stronger baselines (e.g., Gretel), or retain the statement but contextualize the comparison.
4. **Include a brief routing behavior analysis** in the main paper (or ensure it is in the appendix) to justify why keyword-based hidden state initialization is an effective signal for dialect routing.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>