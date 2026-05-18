Now I have all the evidence I need. Let me write the final consolidated review.

---

## Summary

This paper introduces Multi-Field Adaptive Retrieval (mFAR), a framework for retrieval over structured multi-field documents. It decomposes each document into fields, scores each field independently using lexical (BM25) and/or dense (Contriever) scorers, and learns a query-conditioned weighting mechanism to adaptively combine these per-field scores. On the STaRK benchmark (Amazon, MAG, Prime datasets), mFAR variants achieve substantial gains over prior methods including LLM-based reranking and agent-based approaches, with the best variant (mFAR₁₊ₙ) reaching 0.478 average H@1 (+0.118 over the prior best non-agent baseline).

## Strengths

- **Novel framework for adaptive multi-field retrieval.** mFAR is the first approach to combine per-field decomposition, hybrid lexical+dense scoring, and learnable query-conditioned field weighting in a single end-to-end framework. The design is principled and flexible (any number of fields, any scoring methods). Equations (3)–(4) and (1)–(2) formally define the framework, and the SOTA results validate the design.

- **State-of-the-art results on STaRK.** mFAR₁₊ₙ achieves 0.478 H@1, 0.686 R@20, 0.585 MRR (average across three datasets), substantially outperforming prior methods including GPT-4 reranking (0.347 H@1), AvaTaR agent (0.376 H@1), and the next-best finetuned baseline Contriever-FT (0.360 H@1). These gains hold across all three datasets and metrics. Evidence: Table 1.

- **Query-conditioned weighting is demonstrated to be essential.** The ablation removing query conditioning (Table 4, "No QC") shows large drops across all metrics (e.g., −22.6% H@1 on average, −41.1% H@1 on Prime). This proves the adaptive mechanism is a genuine innovation rather than a byproduct of extra parameters. Evidence: Table 4, §5.1.

- **Interpretability via controllable field/scorer masking.** The framework allows post-hoc analysis by masking arbitrary field×scorer combinations at test time, revealing dataset-specific behavior (e.g., MAG relies more on lexical scores, Prime on dense scores). Evidence: Tables 3 and 5, §5.2.

## Weaknesses

### Major

- **The inference approximation is unexamined.** At test time, the paper uses a top-*k* shortlist per (field, scorer) pair and scores only the union to avoid scoring the full corpus. This is a practical necessity, but the paper never reports the value of *k*, analyzes what fraction of relevant documents the union captures, or provides sensitivity analysis. Without this, the reported metrics may not reflect the true ranking produced by the learned scoring function (though any error likely understates, not inflates, performance). This is the single most consequential omission because it directly affects whether the reported numbers are faithful to the method. [Verified: lines 124–125 describe the approximation but give no *k*, recall analysis, or sensitivity.]

- **The comparison of multi-field vs. single-field dense retrieval is confounded.** mFARDense (multi-field dense) is compared directly to Contriever-FT (single-field dense), and the improvement is attributed to the multi-field decomposition. However, mFARDense introduces additional learned parameters (field-specific attention embeddings **a**ₓᵐ, batch-normalization parameters) that Contriever-FT lacks. The improvement could partly stem from these extra parameters rather than from the multi-field decomposition itself. The paper acknowledges this implicitly in §5.3 (qualitative analysis), which partially mitigates the concern, but a clean quantitative disconfounding is absent. [Verified: Table 1 compares mFARDense to Contriever-FT; the qualitative analysis in §5.3 provides some structural evidence but no controlled experiment.]

- **The best-performing model, mFAR₁₊ₙ, is under-analyzed.** This configuration (single-field lexical + multi-field dense) achieves the highest average scores but is introduced post-hoc ("Based on the initial results," line 176) with only a brief rationale (BM25 can be harmed by field decomposition; dense benefits from it). There is no dedicated ablation study comparable to what is done for mFARHybrid (§5.1, §5.2). The paper does not analyze how the adaptive weighting mechanism balances scores from fundamentally different representations (one global lexical score vs. many field-level dense scores), nor does it ablate query conditioning or field importance for this specific variant. Given that this configuration sets the new state of the art, it deserves at least the same depth of analysis as the other variants. [Verified: lines 176, 234; no ablation for mFAR₁₊ₙ in §5.]

### Minor

- **The softmax in the adaptive weighting function is underspecified.** The paper defines *G*(*q*,*f*,*m*) = softmax({**a**ₓᵐ⊤**q**}) but never states what the softmax is taken over (it is implicitly over all (*f*,*m*) pairs so weights sum to 1 per query). This is a small ambiguity that forces the reader to infer the intended normalization. The "No QC" baseline uses global learned scalars *w*ₓᵐ without any normalization constraint, which is a meaningfully different design. Clarification would help. [Verified: line 113.]

- **Qualitative analysis relies on single examples.** Figure 3 provides concrete illustrations, but the claim that mFARSingle is "possibly confused by negation" is speculative. While illustrative examples are useful, the paper would benefit from a more systematic error analysis (e.g., categorizing failure modes over a sample of queries). [Verified: Figure 3 and §5.3.]

### Trivial

- The "STaRK Avg." column averages across three datasets of very different sizes and domains. The paper does report per-dataset results alongside the average, so this is not misleading, but brief discussion of per-dataset variance would strengthen the presentation.

## Nice-to-Haves

- **Computational cost discussion.** The paper describes the adaptive weighting component as "lightweight" (line 20), which is accurate. But the multi-field approach stores separate indexes per field (multiplying storage), and the inference approximation is needed precisely because the full scoring is expensive. A brief discussion of storage and query-time overhead versus single-field methods would help practitioners evaluate the trade-off.

- **Visualization of learned adaptive weights.** The paper shows that query conditioning is necessary (Table 4) but does not show what the learned weights look like. A few examples of which fields get high/low weight for specific queries would directly illustrate the adaptive behavior and support the interpretability claims.

- **Brief discussion of relationship to late-interaction methods (e.g., ColBERT).** These also decompose scoring into per-token interactions but at a different granularity. Not required, but would better situate the contribution.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Missing Contriever-FT fine-tuning details (learning rate, epochs)* — removed as a reproducibility nitpick. The paper describes the shared experimental setup and grid search, which is standard for this setting.
- *Comparison to ColBERT-style late interaction* — removed as scope creep. The paper's scope is multi-field structured retrieval, not late-interaction methods.
- *Computational cost as a core weakness* — downgraded to Nice-to-Haves. The paper's main claims are about accuracy, and the cost discussion is a secondary concern.

## Novel Insights

The reviewer critiques converge on a pattern: the paper's core contributions (multi-field decomposition, adaptive weighting, SOTA results) are solid, but the depth of analysis does not match the ambition. The three major weaknesses — unexamined inference approximation, confounded comparison, and under-analyzed best model — all point to the same gap: the paper convincingly shows *what* works (mFAR outperforms baselines) but provides limited insight into *why* each design choice matters for the best-performing variant. This is a paper strong in results but slightly thin in scientific interrogation of its own findings. The most important takeaway is that none of the weaknesses are structural or fatal — they are all addressable in a camera-ready revision.

## Suggestions

1. **Report the value of *k* used for the inference shortlist and provide a recall analysis.** At minimum, show recall@*k* of the union of per-field shortlists with respect to the gold documents. A sensitivity analysis over *k* would be even stronger.

2. **Acknowledge the parameter-count confound in the multi-field vs. single-field dense comparison explicitly.** Add a brief discussion of why the multi-field structure (rather than extra parameters) is the likely source of improvement, referencing the qualitative evidence from §5.3.

3. **Add an ablation study for mFAR₁₊ₙ**, comparable to the one done for mFARHybrid (query conditioning, field importance, scorer masking). This is the best configuration and its design deserves scrutiny.

4. **Clarify the softmax normalization** in the adaptive weighting equation: explicitly state that the softmax is over all (*f*,*m*) pairs.

5. **Consider adding a brief visualization** of learned query-conditioned weights for a few example queries, to make the adaptive behavior concrete and interpretable.

## Score and Decision

**MY FINAL SCORE:** <pineapple>7.0</pineapple>

**MY FINAL DECISION:** <orange>Accept</orange>