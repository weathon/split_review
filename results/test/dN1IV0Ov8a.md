Now I have a thorough understanding of the paper. Let me compile the final consolidated review.

---

## Summary

This paper proposes a method for bankruptcy prediction using the full text of annual account annexes, which frequently exceed BERT's 512-token limit. The approach segments long documents into overlapping chunks, processes them through parallel BERT instances (bert-base-multilingual-cased), and integrates the segment representations via either LSTM or concatenation+dense layers. Evaluated on 20,000 multilingual annexes from the Luxembourg Business Registry (81% French, ~20% risky class), the best configuration achieves 73.30% precision on the risky class. The paper also provides a practical analysis showing that LSTM-based integration works better for shorter documents while concatenation-based models handle very long documents more effectively.

## Strengths

1. **Practical architecture for long-document bankruptcy prediction from unstructured text**: The paper addresses a genuine limitation of standard BERT (512-token cap) by segmenting documents into overlapping chunks, processing them in parallel BERT instances, and integrating via LSTM or dense layers (Section 4.2–4.4, Figure 1). This enables processing entire annexes (often multi-page) rather than just short excerpts, going beyond prior work like Mai et al. (2019) that relied on the structured "risk factor" section of 10-K filings.

2. **Real-world, multilingual, SME-heavy dataset**: The dataset of 20,000 annexes from the Luxembourg Business Registry covers 16 industries, three languages (~81% French, 11% English, 8% German), and includes many small and medium enterprises (Section 3). This is a meaningful extension beyond prior work focused on U.S. public corporations, and the multilingual setting tests the robustness of the approach.

3. **Concrete evidence of risk information in text**: The best configuration (model m4 with φ=80) achieves 73.30% precision on the minority "risky" class (Table 3, Figure 4) on an imbalanced dataset (~80/20). This provides empirical evidence that unstructured annex text contains signal about financial distress, even when risk is not explicitly stated.

4. **Systematic comparison of integration strategies and document-length interaction**: The paper tests six architectural variants (m1–m6) combining different BERT-output reduction choices, LSTM hidden sizes ([30,50,80,120,200]), and integration approaches (Table 2, Table 3). It further varies the maximum segment count κ from 5 to 20 (Table 4, Figure 5) and demonstrates a meaningful interaction: LSTM-based models perform better on shorter documents (κ ≤ 10), while concatenation-based models maintain or improve precision on very long documents (up to 20 segments). This is a practical finding for deployment.

## Weaknesses

### Fatal

None.

### Major

1. **No baselines against simpler alternatives**: The paper presents no baselines of any kind — not a bag-of-words + logistic regression, not a BERT model limited to the first 512 tokens, not the numerical financial-ratio models mentioned in Section 2 (75–87% AUC on the same registry data). Without any baseline, it is impossible to determine whether the proposed segmentation-and-integration architecture adds value beyond a trivial approach, or even whether the text signal is meaningful at all. The paper's central claim — that this architecture can extract bankruptcy risk from long text — remains unsupported.

2. **Incomplete evaluation and selective metric reporting**: The paper states (Section 5.1, line 153) that "we are going to show the Accuracy, F1 score, precision, and recall" and that metrics are computed using sklearn's weighted methods. However, Tables 3 and 4 report *only* "Risk Precision." On an 80/20 imbalanced dataset, a trivial majority-class classifier achieves 80% accuracy and ~0.89 weighted F1. Without recall and F1 for the minority class, the reader cannot assess whether the 73% precision comes at the cost of extremely low recall (e.g., high precision on a tiny fraction of risky cases). No standard errors, confidence intervals, or significance tests are provided for any result.

3. **Ambiguous temporal relationship in labeling**: The paper labels documents "based on the status of the company of the last filled report or published court order" (Section 3, line 56). For a task framed as *bankruptcy prediction*, the label must be forward-looking relative to the annual account date. The paper does not clarify the time lag between the annual account filing date and the determination of the label, nor does it specify which legal events constitute "risky" (e.g., bankruptcy filing, liquidation order, court-ordered restructuring). If the label is concurrent with the filing rather than predictive, the task is misaligned with its stated goal.

4. **Critical preprocessing parameter δ is unspecified and unanalyzed**: The overlap parameter δ (number of tokens copied between adjacent segments to preserve context) is introduced in Equation 1 (Section 4.1, line 89–92) but never given a concrete value. Nor is its impact on model performance explored. Since δ directly affects how much context is preserved (and how many segments are generated), leaving it unspecified means the core preprocessing pipeline is a black box. Additionally, trimming the *first part* of documents that exceed κ=10 segments (line 99) is an unusual choice that could introduce systematic bias (e.g., losing early context that may be informative), and this bias is not analyzed.

### Minor

1. **Limited hyperparameter exploration**: The LSTM hidden size φ is varied over five values, but all other hyperparameters (learning rate = 1e-5, epochs = 4, batch size = 5, 10/12 frozen BERT layers) are fixed without justification. Four epochs is notably few for fine-tuning BERT on a domain-specific classification task. The dense layer sizes are set by ad-hoc formulas (Section 5, lines 131–133) rather than tuned.

2. **No analysis of language-specific performance**: The dataset is 81% French, 11% English, 8% German, and the model uses bert-base-multilingual-cased (Section 4.1, line 87). The paper does not analyze whether performance differs by language, nor whether French tokenization (which may produce more tokens per word due to subword segmentation) systematically affects the number of segments generated or the quality of representations.

3. **No held-out test set distinction**: The paper reports "validation precision" throughout but does not clarify whether a held-out test set exists or whether results come from validation alone (abstract mentions "train and validate," line 4). This raises concerns about potential overfitting from evaluating multiple configurations on the same data.

### Trivial

- Figure 4/Figure 5 axis labels exhibit formatting artifacts (garbled text in extracted PDF — likely parser issues, not author errors).

## Nice-to-Haves

- A comparison against a simple numerical baseline (e.g., logistic regression on financial ratios from the same LBR data, which the paper itself cites as achieving 75% AUC in Section 2) would provide context for whether the text signal is complementary or redundant.
- A sensitivity analysis of the overlap parameter δ and an analysis of how many tokens/documents are trimmed at the beginning would make the preprocessing choices transparent.
- Language-stratified results (French vs. English vs. German) would strengthen the analysis of the multilingual setting.
- Reporting recall and F1 for the minority class specifically (not just weighted averages) would enable proper assessment on the imbalanced dataset.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The task framing conflates 'processing long text' with 'segmenting and padding' — the paper does not cite or compare against Longformer, BigBird, hierarchical BERT."** This is a request to expand the paper's scope to cover the entire long-document classification literature. The paper's contribution is a straightforward segment-and-integrate architecture for a specific application (bankruptcy prediction), not a claim of advancing long-context modeling. The missing comparison against a first-512-tokens BERT baseline is valid and already captured in Major weakness #1 above; the demand to compare against every alternative long-context architecture is scope creep. Moved from Major.

- **"The statement that 'by default, a BERT instance cannot be fed with long textual information' is too strong."** The paper is clearly referring to the specific BERT architecture they use (Devlin et al., 2018), which has a 512-token limit. This is a standard, uncontroversial statement and not a weakness of the paper. Removed.

- **"Figure 4 and Figure 5 values do not correspond precisely to those in Tables 3 and 4."** The tables and figures cannot be cross-verified from the extracted text (figures are images). Even if there is a minor presentation mismatch, this does not affect the paper's core claims. Removed as a formatting/presentation nitpick.

- **"The hyperparameter search is minimal" framed as a major issue.** The paper does vary the key architectural parameter (LSTM hidden size φ) over five values and tests six model variants. While more tuning would be better, this is a common limitation in academic work and does not invalidate the results. Downgraded from the critic's framing to Minor.

- **"No attention mask discussion for [PAD] tokens."** The paper describes padding (line 101) and BERT's standard handling of [PAD] tokens via attention masks is a well-known implementation detail. This is a trivial implementation point with no effect on the paper's contribution. Removed.

## Novel Insights

The paper's most useful finding is the interaction between document length and integration architecture: LSTM-based integration outperforms on shorter documents (≤10 segments) while concatenation-based models maintain or improve precision on very long documents (up to 20 segments). This is a practical insight for deploying BERT-based models on real-world document collections with variable lengths, where a single fixed architecture may not be optimal. Additionally, the demonstration that unstructured, multilingual annex text from SMEs (not just U.S. public companies) contains bankruptcy-relevant signal is a meaningful empirical finding for the financial NLP community. Beyond these, the paper does not produce insights that go beyond its own results.

## Suggestions

1. Add at least two baselines: (a) a BERT model using only the first 512 tokens of each annex, and (b) a simple text classifier (e.g., TF-IDF + logistic regression or XGBoost). If possible, also report the performance of numerical financial-ratio models on the same dataset to contextualize the text model's contribution.

2. Report full classification metrics (precision, recall, F1 for the minority class, AUROC or precision-recall AUC) for the best model(s) on a clearly defined held-out test set, with error estimates (e.g., bootstrapped confidence intervals).

3. Clarify the labeling methodology: specify the time offset between the annual account date and the label determination, list the legal events that define "risky," and discuss whether the labels are forward-looking or concurrent.

4. Specify the overlap parameter δ (in Equation 1) and report its chosen value. Analyze how different δ values affect the number of segments, token loss from trimming, and model performance.

5. Report the fraction of documents trimmed at the beginning (due to the κ=10 cap) and analyze whether these long documents differ systematically from shorter ones in terms of label distribution or content.

## Score and Decision

**Originality**: The architecture is a straightforward combination of existing techniques (BERT segmentation + LSTM/dense integration), but the application to multilingual SME annexes for bankruptcy prediction fills a gap in the literature.

**Importance of Research Question**: Predicting bankruptcy from financial text is practically important, especially for SMEs that lack analyst coverage. The question is valid.

**Claims Support**: The central claim that the architecture extracts risk information from long text is **not adequately supported** due to the absence of baselines, incomplete metrics, and ambiguous labeling.

**Soundness**: The experimental design has significant gaps (no baselines, no test set distinction, unspecified δ, no error bars). The architectural ablation is the strongest component.

**Clarity**: The writing is adequate but could be more precise, particularly regarding the labeling scheme and preprocessing parameters.

**Value to Community**: If the evaluation gaps were addressed, the dataset and the document-length analysis would be useful. In its current form, the contribution is difficult to assess.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>