Now I have a thorough understanding of the paper and can verify all reviewer claims against the actual content. Let me write the consolidated review.

## Summary

This paper introduces Multi-Field Adaptive Retrieval (mFAR), a framework that decomposes structured documents into constituent fields (e.g., title, abstract, authors), scores each field independently using both lexical (BM25) and dense (Contriever) scorers, and learns a query-conditioned weighting mechanism to combine these scores adaptively. On the STaRK benchmark (three datasets: Amazon, MAG, Prime), mFAR achieves state-of-the-art results, outperforming prior methods including strong lexical/dense baselines, LLM-based rerankers, and agent-based approaches.

## Strengths

- **State-of-the-art results on structured retrieval.** Table 1 shows mFAR variants (especially mFAR₁₊ₙ) substantially outperform all prior methods on STaRK across three datasets, with average H@1 of 0.478 vs. the next best non-mFAR (Contriever-FT at 0.360) and even surpassing the GPT-4 reranker (0.347) and the agent-based AvaTaR (0.376). This directly validates the central claim.

- **Query-conditioned adaptation is clearly necessary for performance.** Table 2 provides a clean ablation: removing query-conditioned weighting from mFAR_Hybrid causes large drops across all metrics (e.g., H@1 drops 22.6% on STaRK average, 41.1% on Prime). This is strong evidence that the adaptive weighting mechanism is not superfluous.

- **Hybrid lexical–dense scoring consistently outperforms single-scorer variants.** In both multi-field (mFAR_Hybrid vs. mFAR_Dense/mFAR_Lexical) and single-field settings (mFAR_Single vs. BM25/Contriever-FT), using both scorers yields better results than either alone across virtually all metrics and datasets. Scorer masking (Table 3) confirms that both scorer types contribute nontrivially.

- **Interpretable and controllable via post-hoc field/scorer masking.** The framework's design enables principled ablation of individual fields and scorers after training (Tables 3–4), revealing dataset-specific behaviors (e.g., MAG relies more on lexical scores, Amazon on dense scores) and providing insight beyond raw accuracy.

- **Practical efficiency: outperforms LLM-based methods without large models or pretraining.** mFAR finetunes a standard Contriever encoder (512-token window) and still outperforms methods using larger context windows (ada-002 with 2K tokens) and expensive LLM rerankers (Claude3, GPT-4), making the contribution practically relevant.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by the evidence presented. The issues below are addressable without altering the fundamental conclusions.

### Minor

- **No variance or statistical significance reported.** All tables report point estimates from a single run per configuration. Some comparisons between mFAR variants involve close scores (e.g., mFAR_Single vs. mFAR₁₊ₙ on Amazon: H@1 0.574 vs. 0.565; average H@1: 0.435 vs. 0.478), and the reader cannot assess whether differences are reliable. While single-run evaluation is common in large-scale retrieval benchmarks, reporting means and standard deviations over 3–5 seeds would significantly strengthen the paper's rigor and is standard practice in top-tier venues.

- **Inference approximation is unanalyzed.** The paper uses an inexact inference procedure (Section 2, Inference): retrieve top-k per field-scorer, then compute full scores for the union. The potential for missing relevant documents that are not individually captured by any single field-scorer is acknowledged but never quantified. A simple comparison of exact vs. approximate ranking on a subset of queries would establish whether this introduces systematic bias. Without it, the reported numbers reflect the approximation, not the true model.

- **Interpretability claim is partially supported but not directly verified.** The paper asserts that field weights are "naturally interpretable and controllable," but the analysis (Section 5.2) only demonstrates interpretability through ablation (masking out entire fields/scorers globally). The paper does not inspect actual learned weight values per query to verify, for example, that queries about "authors" produce higher weights on the authors field. While the ablation evidence is useful, it falls short of directly validating the interpretability claim at the per-query level. (The qualitative examples in Figure 2 illustrate behavioral advantages but do not examine weights directly.)

- **Missing hyperparameter details for best models.** The paper reports a grid search over learning rates and whether to use normalization, but does not disclose which configurations were selected for each dataset's best model. This would aid reproducibility.

- **Computational cost of the multi-field inference pipeline is not discussed.** For practitioners, understanding how mFAR's retrieval time (with the approximate shortlist) compares to standard dense retrieval would be valuable, especially given that mFAR involves scoring each field-scorer pair separately.

### Trivial

- Adaptive weighting is limited to query-embedding-based field selection; the model cannot dynamically adjust weights based on whether query terms actually appear in a specific field. This design choice (which the paper does not acknowledge as a limitation) means the model can only learn globally query-type-correlated field importance, not instance-level decisions. This is worth noting but not a flaw.

## Nice-to-Haves

- Adding a simple fixed-weight hybrid baseline (e.g., sum of normalized BM25 + Contriever-FT scores with a single tuned weight on dev) would cleanly isolate whether learned adaptive weighting adds value over a tuned static fusion. The existing "No QC" ablation (which still uses multi-field decomposition with learned *global* weights) partially addresses this, and mFAR_Single (both scorers, single-field) further shows hybrid > single-scorer, so this is not a gap — but it would tighten the argument.
- A direct analysis of the inference approximation error (Recall@k of approximation vs. exact ranking) on a query subset.
- Disclosing how the learned field embeddings $\mathbf{a}_f^m$ are initialized (random? based on field-name embeddings?) and whether this affects convergence speed or final weight interpretability.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Best model does not align with central motivation" (Harsh Issue 4).** The paper *acknowledges at length* (Section 4) that multi-field lexical scoring sometimes underperforms single-field BM25, and *explicitly motivates* mFAR₁₊ₙ as a synthesis of findings (multi-field dense is good, single-field lexical is good, hybrid is best). The paper's contribution is the framework, not a prescription that every component must be multi-field. This is an honest finding, not a contradiction. **Removed** because the paper already addresses this.

- **Missing related works (ColBERT, SPLADE, etc.).** Per rules, I cannot verify whether these are missing or whether the paper's scope justification is adequate. **Removed** per instructions.

- **"Multi-field lexical hurts" as a weakness.** The paper is transparent about this finding and offers a plausible explanation (BM25 length normalization). A finding that a component of a framework does not always help is not a weakness of the paper — it is a nuanced result.

- **Strength Finder's potential generic/superficial strengths.** All listed strengths have specific citations to tables or figures and do not conflict with verified weaknesses. No removal needed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface useful but incremental suggestions (variance reporting, inference analysis, weight inspection) that would strengthen the paper; they do not reveal a fundamentally different interpretation of the work.

## Suggestions

- **Run 3–5 random seeds** for each mFAR variant and report means and standard deviations in Tables 1–4. This single change would address the most significant rigor gap.
- **Analyze the inference approximation** on a held-out query subset: compare exact full-scoring rankings against the approximate shortlist method and report Recall@k of the approximation.
- **Add a qualitative weight inspection** for a handful of queries where the relevant field is unambiguous (e.g., a query mentioning "authors"). Show that the learned weights meaningfully shift toward the relevant field and scorer.
- **Report the selected hyperparameters** (learning rate, normalization setting) for each dataset's best mFAR configuration.
- **Add a brief discussion of computational cost** — approximate per-query latency vs. standard dense retrieval.

## Score and Decision

This is a solid paper with a clear, well-motivated contribution. The mFAR framework is novel, achieves substantially better results than prior work on a challenging benchmark, and the ablations convincingly validate the key design choices (query conditioning, hybrid scoring). The weaknesses are all addressable in a minor revision and do not undermine the core claims. The paper would benefit from multiple seeds and a few additional analyses, but in its current form it already makes a compelling empirical contribution.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>