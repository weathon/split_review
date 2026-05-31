Now I have all the information needed to produce the consolidated review.

## Summary

This paper proposes Topic-XICL, a demonstration selection method for cross-lingual in-context learning (XICL). The method clusters English training data using multilingual Sentence-BERT, learns topic-specific token embeddings by fine-tuning BLOOMZ-1b7 (freezing all other parameters), and selects the most topic-informative demonstrations for each test input via Bayesian-inspired probability scoring. Experiments on XNLI, XCOPA, and TyDiQA-GoldP across three 7-8B LLMs (BLOOM, Qwen1.5, Llama3.1) show consistent improvements over random, semantic-similarity, and cluster-based baselines, with average gains of 1.77–3.32%.

## Strengths

- **Consistent improvements across three tasks and three LLMs**: Table 1 shows Topic-XICL exceeds the strongest baseline (ICL cluster) on TyDiQA-GoldP (+3.32%), XCOPA (+2.47%), and XNLI (+1.77%) averaged over BLOOM, Qwen1.5, and Llama3.1. Per-language gains in low-resource languages reach 10.9% (Vietnamese on XCOPA) and 10.3% (Bengali on TyDiQA). The trend holds across k=2,3,4 shots and for larger k (6,8,12) in XCOPA (Figure 4).

- **Lightweight and LLM-agnostic**: The topic model is trained only once on BLOOMZ-1b7 (15–30 minutes) and then applies to any black-box LLM without requiring parameter access, output distributions, or per-model retraining. This is a practical strength compared to task-specific retrievers that need LLM feedback.

- **Ablation validates modular design**: Section 4.5 (Figure 5) decomposes the approach into topic assignment method and selection strategy, showing the full Topic-XICL outperforms ablated variants (top-1 topic, k-means predict, random-within-cluster), confirming that both the topic inference module and the probability-based selection are necessary.

- **Works with smaller topic model on complex tasks**: Section 5.3 shows BLOOMZ-560m still beats baselines on XCOPA and TyDiQA-GoldP (e.g., +13.4% EM on Arabic for Qwen1.5), demonstrating the approach does not require a large topic-modeling LLM for harder tasks.

- **Non-English source languages also work**: Section 5.4 shows Topic-XICL using Chinese or Italian as the source language consistently outperforms baselines on BLOOM and Llama3.1, indicating the method is not tied to English-centric topic structures.

## Weaknesses

### Fatal
None.

### Major
None. The weaknesses below are all addressable in revision.

### Minor

1. **Theoretical framing is somewhat overstated relative to the practical algorithm.** The paper presents Sections 3.1–3.3 as a Bayesian inference framework (extending Wang et al. 2023), but the cross-lingual bridge is a purely semantic-similarity heuristic (top-10 Sentence-BERT cosine similarity). No language variable appears in the core equations (Eq. 7–8), and the assumption that topics are cross-lingually invariant is never empirically verified. The method works, but the narrative implies a tighter theory-to-practice connection than is demonstrated. **Suggested fix**: temper the Bayesian justification to match what is implemented, or provide evidence (e.g., that test-topic assignments from semantic similarity correlate with actual topic-model posterior estimates computed cross-lingually).

2. **Missing baseline that would isolate the topic model's contribution.** The ICL cluster baseline (random within cluster) controls for clustering but not for learned reranking. A natural comparison is a within-cluster retriever trained without LLM feedback (e.g., a logistic regression or small bi-encoder trained on cluster labels using the same multilingual embeddings). Since such a retriever does not require LLM access, it would be directly comparable in resource usage and would clarify whether the advantage comes from the topic model's learned structure or simply from having *any* learned reranker over clusters. The paper mentions task-specific retrievers (line 12) and bi-encoders (line 35) but does not include one as a baseline.

3. **No statistical significance testing.** The average gains are modest (1.77–3.32%). Standard deviations are reported across seeds but not across languages. A paired permutation test or bootstrap across languages would strengthen confidence that the improvements are not due to chance on a few outlier languages.

4. **Hyperparameter sensitivity is underexplored.** The number of topics n (5 or 20) and tokens per topic c (10 or 15) vary per task with no sensitivity analysis in the main paper (the paper references "Appendix A" for guidelines, which was stripped). For a method claiming generalizability, practitioners need principled guidance on how to choose n and c rather than manual tuning per task. The BLOOMZ-560m failure on XNLI (Section 5.3) is acknowledged with a post-hoc explanation ("simpler classification tasks may need clearer clustering information") but not analyzed.

5. **Ablation does not isolate all design choices.** Section 4.5 compares Topic-XICL to top-1 topic, k-means predict, and random-within-cluster. However, it does not test "improved topic assignment (top-10) + random selection within the assigned topic." This would isolate whether the topic model's selection or the improved assignment drives the gains. The critic's identification of this gap is correct.

6. **Case study does not support all claimed topic characteristics.** The paper claims topics capture "syntactic structure" and "task structure" (line 17), but the case study (Section 5.2) only shows domain-level information (biology, sports, short passages). The stronger claims about syntax and task structure are unsupported by examples.

7. **Cross-lingual topic assignment accuracy is not analyzed.** The method assigns topics to target-language test inputs via top-10 semantic similarity with English candidates. If multilingual Sentence-BERT alignment is noisy for low-resource languages, the assigned topic may be inaccurate. The paper does not verify this bottleneck (e.g., by checking whether topic assignments correlate with task difficulty or by evaluating assignment accuracy on a held-out set).

### Trivial

- **Clarify probability estimation for generation tasks.** Section 3.3 could specify how $\hat{P}_{M'}^a(\hat{\theta}^a|X_i^a,Y_i^a)$ is computed for free-form outputs (TyDiQA) versus classification. The paper mentions evaluating with regular matching (max output length 16) but the topic-model loss uses the full gold answer — this is reasonable but should be stated explicitly.

- **Token order for topic tokens.** Section 3.2 appends c topic tokens as a fixed prefix (e.g., "<t1.1><t1.2>...<t1.c> X") but does not discuss whether token order matters.

## Nice-to-Haves

- Report inference overhead (topic assignment + probability scoring per candidate) in addition to the 15–30 minute training time already stated.
- Provide a qualitative comparison of demonstrations selected by Topic-XICL vs. baselines to illustrate the advantage concretely.
- Test the method on a more diverse set of source languages (beyond English, Chinese, Italian) or on culturally specific topics where cross-lingual alignment may break.
- Consider an ablation where the topic model is replaced with a logistic regression on Sentence-BERT features (as suggested by the harsh critic) to further isolate the fine-tuning step's value.

## Removed Points

These points from the inputs are removed with brief justification:

1. *Criticism that "the theoretical development assumes topics are cross-lingually invariant, but no language variable appears in the equations"* — The paper does introduce the language variable l in line 60 ($P_M^{a,l}$). The cross-lingual claim is a design choice (semantic similarity), not a mathematical omission. The underlying point about overstated framing is kept (see Minor #1), but the specific claim of a missing formal variable is incorrect.

2. *Criticism that "Strengthening the Paper on Its Own Terms" point 1 about measuring what the topic model captures should be an expectation* — This is an interesting research question but goes beyond what is standard for a conference paper. Moved to Nice-to-Haves implicitly.

3. *Strength Finder's claim about being "first demonstration of Bayesian-theoretic demonstration selection for non-classification XICL tasks"* — This is stated by the paper and supported. KEPT as Strength #1, though the connection to Bayesian theory is imperfect (noted in Minor #1).

4. *Strength Finder's claim about the case study demonstrating topics capture "structural/domain information beyond semantic similarity"* — Partially valid: the case study shows domain-level information (biology, sports) but not syntactic or task structure. KEPT but the overclaiming is flagged in Minor #6.

5. *Complaint that the paper lacks "discussion of computational cost beyond 'moderate'"* — The paper states 15–30 minutes training time (lines 223–224). This is adequate for a practitioner-oriented paper. Removed.

6. *Criticism that the method "is only tested with English as source (except Section 5.4)"* — Section 5.4 explicitly tests Chinese and Italian. The critic acknowledges this exception, making the criticism redundant. Removed.

7. *Section-by-section note about "Introduction and Figure 1: the paper does not verify that the topics learned actually capture the diversity that random selection provides"* — The paper never makes this specific claim; it claims topics capture factors *beyond* similarity. This is a strawman. Removed.

## Novel Insights

None beyond the paper's own contributions. The harsh critic identified several well-calibrated gaps (overclaimed Bayesian connection, missing baseline, hyperparameter sensitivity) but synthesized them as fixable weaknesses rather than fundamental flaws. The strength finder's claims are largely duplicative of the paper's own stated contributions. The most useful synthesized insight is that the cross-lingual topic assignment bottleneck (semantic similarity for topic inference) is conceptually separable from the topic model's selection mechanism, and the paper could be strengthened by analyzing these two stages independently and by adding a trained-but-non-LLM baseline.

## Suggestions

1. **Temper the Bayesian framing in Sections 3.1 and 3.3** to align with what is actually demonstrated. Present it as a *practical algorithm inspired by* Bayesian inference rather than as an extension of the theory. Specifically, acknowledge that the cross-lingual transfer relies on a semantic similarity heuristic rather than a learned cross-lingual topic posterior.
2. **Add a simple trained baseline**: e.g., fine-tune Sentence-BERT (same size as BLOOMZ-1b7) on the cluster labels via contrastive learning, then use its similarity scores to select demonstrations within each cluster. This would isolate whether the topic-model fine-tuning step contributes beyond a straightforward learned reranker.
3. **Add a statistical significance test** (paired bootstrap or permutation test across languages) to support the claim that the modest average improvements are reliable.
4. **Report a sensitivity sweep** for the number of topics n (e.g., {5, 10, 20, 50}) on at least one task, and provide a heuristic for practitioners to set n and c.
5. **Add the missing ablation**: top-10 topic assignment + random selection within the assigned topic, to isolate the contribution of the topic model's probability-based selection from the improved assignment.
6. **Analyze cross-lingual topic assignment accuracy**: for a subset of languages, manually or via held-out data, check whether the top-10 semantic similarity heuristic assigns test inputs to the correct cluster.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>