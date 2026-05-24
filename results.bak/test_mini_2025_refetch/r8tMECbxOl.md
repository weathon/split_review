## Summary

This paper proposes TDTransformer, a transformer-based framework for tabular data that addresses two core challenges: heterogeneity of column types and numerical reasoning. The framework uses distinct embedding processes for categorical, numerical, and binary columns with alignment layers to map them to a common space, adapts piecewise linear encoding (PLE) for numerical values without requiring labels, and introduces column-type-aware corruption and positional encoding for pretraining. The method is evaluated on OpenML benchmark datasets and achieves average accuracy gains over tree-based baselines (+1.67% over CatBoost on binary; +3.62% over XGBoost on multiclass).

## Strengths

1. **Strong multiclass results on a large benchmark.** TDTransformer (with CTA positional encoding) achieves 80.51% average accuracy and 0.70 F1 across the multiclass evaluation, substantially outperforming XGBoost (76.45% / 0.66) and CatBoost (76.61% / 0.65). The improvement is consistent across most dataset subsets. (Table 3)

2. **Well-motivated architectural design.** The paper identifies two real obstacles to transformer performance on tabular data — heterogeneity and numerical reasoning — and designs explicit mechanisms for each: per-column-type embeddings with alignment layers, and label-free PLE for numericals. This is more principled than ad-hoc serialization approaches.

3. **Label-free adaptation of PLE.** The original PLE (Gorishniy et al., 2022) requires labels to fit decision trees for binning. The paper's quantile-based adaptation removes this requirement while maintaining a fixed sequence length and a codomain $[-1, 1]$ that aligns with layer normalization. This is a concrete, useful modification. (Section 3.1, Table 1)

4. **Honest discussion of failure cases.** The paper explicitly identifies the Au4-2500 table (non-semantic column names and categorical values) as a case where XGBoost outperforms TDTransformer, and notes that XGBoost remains best on datasets with $|\mathcal{D}| \geq 2000$ in multiclass. This transparency strengthens credibility. (Section 4.2)

5. **Ablation of pretraining strategy.** The comparison of SSCL vs. SCL (Figure 3) shows across four metrics that self-supervised contrastive learning outperforms supervised contrastive learning for tabular data, which is a non-obvious finding worth reporting.

## Weaknesses

### Fatal
None.

### Major

1. **Missing FT-Transformer baseline.** FT-Transformer (Gorishniy et al., 2021) is the most directly comparable transformer-based tabular model — it also uses feature tokenization and a transformer encoder — and is cited in the paper's introduction. However, it is not included as a baseline. Without this comparison, the improvements cannot be cleanly attributed to the proposed innovations (separate embeddings, PLE, CTA encoding) as opposed to simply using a reasonably tuned transformer architecture. The paper includes TransTab, but FT-Transformer is the standard transformer baseline in the tabular deep learning literature and its absence is a significant gap.

2. **Missing component-level ablations.** The paper lists three main contributions (separate column-type embeddings, PLE adaptation, column-type-aware corruption and CTA positional encoding), but the ablation study only covers (a) SSCL vs. SCL pretraining and (b) positional encoding variants. There is no ablation that isolates:
   - Separate embeddings per column type vs. a unified embedding approach.
   - PLE vs. standard tokenization for numerical values.
   - The Hadamard product with column-name embeddings vs. a simpler additive or concat scheme.
   - Column-type-dependent corruption vs. standard random corruption.
   
   Without these, the observed gains cannot be conclusively tied to the specific design choices touted as contributions.

3. **Dataset count inconsistency.** The abstract and table captions state "76 real-world tabular classification datasets," but Section 4.1 (Datasets) states "56 real-world tabular classification datasets." This internal contradiction (76 vs. 56) is unexplained and undermines confidence in the experimental reporting.

### Minor

4. **No variance or significance reporting.** All results in Tables 2, 3, and the ablation tables are reported as point estimates. Figure 2 shows error bars but the caption does not specify what they represent (standard deviation? standard error? over what? across seeds? datasets?). Without any measure of variance or statistical significance test, modest gains (e.g., +1.67% accuracy in binary) cannot be assessed for reliability.

5. **Marginal contribution of CTA positional encoding.** Table 4 shows that on multiclass, the gain of CTA positional encoding over standard positional encoding is only +0.28% accuracy (80.51 vs. 80.23). On binary, CTA actually performs slightly worse (87.48 vs. 87.79). The large jump is from "no positional encoding" to "any positional encoding" (74.78→80.23). This weakens the claim that CTA encoding is a meaningful innovation — it is essentially on par with standard positional encoding.

6. **Title and framing overstate the "language model" connection.** The main experimental results use a randomly initialized gated transformer (Wang & Sun, 2022) as the backbone, not a pretrained language model. While BERT tokenizer weights are used, the core transformer is trained from scratch. RoBERTa backbone results are relegated to the appendix. The title "Language Models are Good Tabular Learners" implies a stronger connection to pretrained LMs than the experiments deliver.

7. **Undefined `max_len` in Eq. (2).** The variable `max_len` is used in the definition of $k_{\text{cat}}$ but is never defined in the paper. This affects reproducibility of the categorical embedding procedure.

8. **No regression experiments.** The evaluation covers only binary and multiclass classification. Adding even a small set of regression datasets would strengthen claims about general tabular learning capability.

### Trivial
None.

## Nice-to-Haves
- Reporting results with standard deviations over at least 3 random seeds.
- Defining `max_len` and clarifying the chunking procedure for categorical embeddings.
- Adding regression experiments to demonstrate generality beyond classification.

## Removed Points

The following points from the harsh critic were evaluated against the paper text and removed:

- **"No cross-validation or multiple seeds"** — The paper uses fixed 72/8/20 splits with a single A40 GPU. This is a minor concern that is subsumed by Weakness #4 (variance reporting). Single-seed evaluation is common in large-benchmark tabular papers.
- **"Table 4 shows similar performance between standard and CTA encoding"** — Kept as Weakness #5 (CTA marginal). The critic's framing has been adjusted to match what the table actually shows (some difference exists but is very small).
- **"The method's strength is dataset-specific"** — The paper openly acknowledges this (Au4-2500, large datasets). This is framed as a strength (honesty), not a weakness.
- **"No justification for Hadamard product"** — Subsumed by Weakness #2 (missing ablations). Could be a design choice without theoretical justification, which is common in empirical papers.
- **"Permutation invariance claim contradicted"** — The paper's argument (columns are permutable, categorical token sequences are not, hence CTA positional encoding only for categoricals) is logically coherent. The critic misread this.
- **"RoBERTa results should be in the main paper"** — The parser strips appendices; these likely exist in the original submission. Removed per hard rules.
- **"Dataset list belongs in main paper"** — Removed per hard rules (parser strips appendices).
- **"Code repository not verifiable"** — Removed per hard rules (cited references are assumed to exist).
- **"No comparison to original PLE"** — The paper's PLE adaptation is compared in Table 1 on three axes (codomain, label requirement, fixed sequence length). This is sufficient for a methods comparison.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no contradiction or unrecognized pattern that the paper itself does not already discuss.

## Suggestions

1. **Add FT-Transformer as a baseline.** This is the single most important addition. Without it, the paper's central claim ("significantly improves SOTA") is under-supported.
2. **Add four targeted ablations** that isolate (a) separate vs. unified embeddings, (b) PLE vs. tokenization, (c) Hadamard vs. additive column-name combination, and (d) column-type-dependent vs. uniform corruption.
3. **Resolve the 56 vs. 76 dataset count discrepancy** and clarify which OpenML benchmark variant is used.
4. **Add variance estimates** (e.g., 3 random seeds) for the main results, or at minimum clarify what the Figure 2 error bars represent.
5. **Retitle** to something like "Tabular Domain Transformer: Addressing Heterogeneity and Numerical Reasoning in Tabular Data" to better reflect what is actually evaluated.

---

## Score and Decision

### Calibration Protocol

**Round 1 — Bracketing:**
- Weak anchors (score < 3.5): TabKANet (3.0, `3qDhqj6qfu`) — tabular transformer with numerical embedding, rejected. TDTransformer is clearly stronger (76 datasets vs. few, much larger performance gains over tree-based methods).
- Middle anchors (3.5–7.5): MotherNet (5.75, `6H4jRWKFc3`) — tabular hypernetwork accepted as poster despite missing comparisons and limited novelty concerns. UniPredict (5.20, `20L7txbIa8`) — LLM-for-tabular, rejected with missing-baseline concerns similar to TDTransformer. Tabular Dataset Distillation (5.50, `Thnk4ez3wN`) — rejected.
- Strong anchors (7.5+): PTaRL (8.0, `G32oY4Vnm8`) — prototype-based tabular learning, accepted spotlight. Significantly stronger in experimental rigor and completeness.

**Round 1 bracket: [4.5, 6.5]** — below PTaRL-level rigor, above TabKANet-level weakness.

**Round 2 — Narrowing within bracket:**
- Searched (5.0, 6.2) for tabular transformer+contrastive learning papers. Retrieved: MotherNet (5.75, poster), Tabular Dataset Distillation (5.50, reject), UniPredict (5.20, reject).
- Comparison to MotherNet (5.75): MotherNet had a creative approach but limited datasets and missing comparisons analogous to TDTransformer's missing FT-Transformer. MotherNet was accepted as poster. TDTransformer has more extensive evaluation but worse dataset-count inconsistency. **Comparable, maybe slightly lower.**
- Comparison to UniPredict (5.20): UniPredict was rejected due to concerns about whether gains came from the method or the large backbone, plus missing details. TDTransformer has better architectural justification and is more reproducible. **Slightly stronger than UniPredict.**
- Comparison to Tabular Dataset Distillation (5.50): Well-executed but a less central contribution. **Comparable.**

**Final score: 5.5**

### All Anchors Considered

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `3qDhqj6qfu` (TabKANet) | 3.00 | R1 | Weaker — fewer datasets, marginal gains |
| `2L1OxhQCwS` (LSTM vs Transformer) | 3.33 | R1 | Less relevant topic, weaker |
| `i28ZjVxl81` (OOD tabular) | 2.50 | R1 | Less relevant, weaker |
| `2wwPG1wpsu` (Time-series benchmark) | 2.50 | R1 | Different domain |
| `pE0UM18TQh` (ICL Tabular) | 4.33 | R1 | Similar missing-baseline issues, smaller scale |
| `6H4jRWKFc3` (MotherNet) | 5.75 | R1/R2 | Comparable — accepted poster despite eval gaps |
| `IbCvnpJ4py` (Molecular FT) | 5.25 | R1 | Less relevant domain |
| `53gU1BASrd` (Financial TS) | 4.50 | R1 | Different domain |
| `G32oY4Vnm8` (PTaRL) | 8.00 | R1 | Much stronger — comprehensive evaluation |
| `PdaPky8MUn` (Long-seq priors) | 8.00 | R1 | Different domain, much stronger |
| `1CLzLXSFNn` (TimeMixer++) | 8.00 | R1 | Different domain, much stronger |
| `bWcnvZ3qMb` (FITS) | 8.00 | R1 | Different domain, much stronger |
| `20L7txbIa8` (UniPredict) | 5.20 | R1/R2 | Slightly weaker — worse reproducibility issues |
| `CiiLchbRe3` (Seq decision transformer) | 5.25 | R2 | Less relevant topic |
| `Thnk4ez3wN` (Tabular distillation) | 5.50 | R2 | Comparable — well-executed but limited scope |
| `7VkHffT5X2` (AnoLLM) | 6.75 | R2 | Stronger — more focused evaluation |
| `rmXXKxQpOR` (Provable pretraining) | 7.00 | R2 | Different topic (theory), stronger |
| `EIPLdFy3vp` (Time-series contrastive) | 6.60 | R2 | Different topic |
| `4Ay23yeuz0` (TabSyn) | 6.75 | R2 | Stronger — more rigorous evaluation |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>