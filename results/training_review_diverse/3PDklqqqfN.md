Now I have all the information I need. Let me construct the final consolidated review.

## Summary

This paper introduces Multi-Field Adaptive Retrieval (mFAR), a framework for retrieving structured documents by decomposing them into fields, scoring each field independently with dense and/or lexical scorers, and combining scores via learned query-conditioned weights. On the STaRK benchmark (Amazon, MAG, Prime), mFAR achieves state-of-the-art results, with the best hybrid variant (single-field lexical + multi-field dense) obtaining 0.478 H@1 and 0.686 R@20 on average, outperforming prior methods including AvaTaR, GPT-4 reranking, and fine-tuned Contriever.

## Strengths

1. **State-of-the-art results on multi-field structured retrieval.** mFAR achieves the best average scores across all three STaRK datasets, outperforming strong baselines including BM25, fine-tuned Contriever, and the agent-based AvaTaR (Table 4). The best model (mFAR\_1+n) surpasses the prior best method (AvaTaR) by 0.102 H@1 and 0.184 R@20 on average — a substantial margin.

2. **Clear empirical demonstration that query-conditioned weighting is essential.** The ablation in Table 5 (lines 248–268) shows that removing query conditioning (i.e., using global per-field weights only) causes large drops across all datasets: up to 41.1% loss in H@1 on Prime and 22.6% average H@1 loss. This directly validates the paper's central claim about adaptive weighting.

3. **Thorough analysis of field and scorer contributions.** Section 6.2 provides fine-grained field-level ablation (Table 7), showing which fields contribute via lexical vs. dense channels and revealing interactions (e.g., masking one scorer type for a field may show no effect, yet masking both hurts — suggesting redundancy across scorers for that field). This is practically useful for understanding the model's behavior and for future work on structured retrieval.

4. **Sound experimental design.** All dense scorers use the same base encoder (Contriever) as the dense baseline, ensuring fair comparisons. The paper tests multiple configurations (multi-field dense, multi-field lexical, multi-field hybrid, single-field hybrid, and the hybrid 1+n variant), providing a clear picture of where each component helps.

## Weaknesses

### Fatal
None.

### Major

1. **Inference shortlist k is unspecified and unanalyzed.** The paper states (lines 122–125) that at test time it forms a top-*k* shortlist per (field, scorer) and scores only the union of those shortlists to produce the final ranking. This is a lossy approximation — a relevant document that does not appear in *any* single field's top-*k* is permanently missed. The paper never states what *k* is used, nor provides any analysis of recall degradation vs. exact scoring. Without this, readers cannot assess whether the reported results reflect the method itself or a particular (possibly aggressive) approximation. The authors should report *k* and provide a sensitivity analysis on a development set demonstrating that approximation loss is negligible at the chosen *k*.

### Minor

2. **Framing oversells "multi-field" when the best variant partially abandons it.** The title, abstract, and contributions emphasize multi-field decomposition, yet the overall best model (mFAR\_1+n) uses a *single-field* lexical scorer combined with multi-field dense scorers. The paper acknowledges this candidly (lines 224–234, "Multi-field vs. Single-field"), but the narrative still centers "multi-field" as the core contribution. The main advantage is actually the ability to combine *both* a hybrid mixture and per-field scoring, with optimal use being dataset- and scorer-dependent. Recalibrating the framing around the mFAR\_1+n configuration and explaining *why* single-field lexical works better (e.g., BM25's length normalization is inappropriate for per-field scoring) would make the contribution sharper.

3. **No analysis of what the query-conditioned weights actually learn.** The ablation (Table 5) convincingly shows query conditioning matters, but the mechanism remains a black box. Since the weight predictor is a softmax over dot products between learned embeddings `a_f^m` and the query embedding `q` (which also feeds the dense scorer), the conditioning could be picking up on query length, token frequencies, or other shallow correlates rather than genuine field semantics. A small analysis — e.g., computing average learned weights for "authors" when the query contains a person name, or for "enzyme" when biomedical terms appear — would strengthen the claim that the model learns query-field semantics, not just correlations.

4. **No discussion of computational cost.** Indexing each field separately multiplies storage by the number of fields (22× on Prime). At query time, the dense scorer computes dot products against each field embedding for all shortlisted documents. The paper should acknowledge this trade-off and ideally provide latency or storage numbers to help assess practical viability.

### Trivial

5. **Some hyperparameter details missing.** The embedding dimension of `a_f^m` (the field-scorer embedding used in the query conditioning mechanism) and whether it is trained from scratch or initialized are not stated.

6. **Full field listing not provided.** The paper gives field counts and names a few examples in tables/figures, but a complete list of fields for each dataset (ideally in an appendix) would aid reproducibility.

## Nice-to-Haves

- **Weight interpretability analysis:** Compute average learned weights per field across queries, and separately for queries whose content likely targets a specific field. This would directly validate that the model "learns" field semantics.
- **"Late fusion" baseline:** Compare mFAR to a baseline that retrieves from each field independently with BM25 and Contriever, then merges ranks with a learned global per-field weight (no query conditioning). This would isolate the value of the adaptive component.
- **Proactive controllability demonstration:** Show a case where manually overriding a learned field weight (e.g., setting "authors" weight to zero for a query known to need only "title") produces an expected effect — this would strengthen the "controllability" claim in the introduction.

## Removed Points

These points were raised by reviewers but are removed or downgraded per the rules:

- **"Controllability not demonstrated":** The paper *does* demonstrate controllability via the masking analysis in Section 6.2, where specific field/scorer weights are zeroed at test-time to measure their contribution (lines 273–312). This is a legitimate form of test-time control. Removed.
- **"Qualitative analysis is anecdotal / not systematically sampled":** Two examples in Figure 3 are standard practice for retrieval papers; the paper's core claims are supported by quantitative results and ablations. The qualitative examples are illustrative, which is appropriate. Downgraded to removed point.
- **"Loss(%) column difficult to interpret":** The paper already shows raw scores alongside loss percentages (Table 5). This criticism was addressed. Removed.
- **"adaptive vs. query-conditioned terminology":** A pure style preference. The paper uses both terms consistently. Removed.
- **"Related work is well-organized":** Generic strength without specific evidence. Removed per instructions.

## Novel Insights

The most interesting finding emerging from the reviews — beyond what the paper explicitly foregrounds — is the asymmetry between lexical and dense scorers regarding multi-field benefits: multi-field decomposition *helps* dense retrieval (mFAR_Dense outperforms Contriever-FT on all datasets) but can *hurt* lexical retrieval (BM25 alone outperforms mFAR_Lexical on Amazon and MAG). The paper attributes this to BM25's length normalization being ill-suited to per-field scoring (citing Robertson et al., 2004), but this asymmetry has deeper implications: it suggests that dense embeddings naturally benefit from the "separation of concerns" that fields provide (each field's embedding focuses on a sub-aspect), while BM25 relies on cross-field term frequency signals that are lost when fields are split. This could guide future work toward different field-aggregation strategies for different scorer types.

## Suggestions

1. **Specify the inference shortlist *k* and evaluate its impact** on recall vs. exact scoring using a development set. This is the most critical missing detail and must be addressed for the results to be reproducible and trustworthy.

2. **Recalibrate the paper's framing** to center the mFAR\_1+n variant as the main contribution, explaining *why* a single-field lexical scorer + multi-field dense scorers works best. This would make the paper's narrative match its strongest empirical finding.

3. **Add a weight analysis** showing average learned field weights across queries, ideally broken down by query properties (e.g., queries containing named entities vs. not), to demonstrate that the query-conditioning mechanism learns meaningful field semantics.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>