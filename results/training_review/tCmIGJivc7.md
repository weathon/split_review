Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper proposes Topic-XICL, a demonstration selection method for cross-lingual in-context learning. The method first clusters English training data into topics using Sentence-BERT embeddings and K-means, then fine-tunes topic token embeddings on a compact LLM (BLOOMZ-1.7B) to learn per-topic representations. For a test input, it assigns a topic via Sentence-BERT nearest-neighbor search and selects top-k demonstrations from that topic ranked by the learned topic-token probability. Experiments across three multilingual tasks (XNLI, XCOPA, TyDiQA-GoldP) and three LLMs (BLOOM, Qwen1.5, Llama3.1) show consistent improvements over random, semantic-similarity, and cluster-random baselines by 1.77%–3.32%.

## Strengths

- **Consistent multi-model, multi-task empirical gains**. The method outperforms all baselines on all three datasets across all three LLMs (Table 1). The improvements are not aggregated illusions — per-language breakdowns (Figure 3) show gains in most languages, including substantial improvements on low-resource and unseen languages (e.g., +10.9% on Vietnamese XCOPA with BLOOM, +10.3% on Bengali TyDiQA).

- **Extension to non-classification tasks with verified results**. Prior topic-based demonstration selection (Wang et al., 2023) was limited to classification. This paper validates the approach on reasoning (XCOPA) and reading comprehension (TyDiQA-GoldP), where gains are larger (2.47% and 3.32%) than on classification (1.77%), suggesting the method is particularly useful beyond classification.

- **Lightweight training with cross-model transfer**. Training only the topic token embeddings on BLOOMZ-1.7B takes 15–30 minutes, and the resulting topic representations transfer to different model families (BLOOM, Qwen1.5, Llama3.1), demonstrating that the learned topic information generalizes across architectures.

- **Cross-source-language experiments (Section 5.4)** . Testing with Chinese and Italian as source languages (in addition to English) provides useful evidence about the method's robustness to source language choice, which is uncommon in XICL papers.

## Weaknesses

### Fatal
None.

### Major

1. **Topic inference for test inputs does not use the learned topic model (structural disconnect).** The paper is titled "Demonstration Selection with Topic Inference," and its claimed novelty centers on "topic inference." Yet the critical step of assigning a topic to a target-language test input (Section 3.3) is performed by a separate Sentence-BERT k-NN procedure — the fine-tuned LLM with learned topic tokens plays no role in this step. The fine-tuned model is only used to rank candidate demonstrations *within* a topic that was already assigned by an external similarity measure. Until we see a version where topics are inferred by feeding the test input to the fine-tuned LLM (e.g., checking which topic token gives the highest conditional probability), the phrase "topic inference" overstates what the learned model actually does. The ablation in Figure 5 compares alternative topic-assignment heuristics (top-1, k-means predict) but does not test whether the learned topic model itself could perform this assignment.

2. **The ablation does not isolate the contribution of the fine-tuned topic tokens.** The comparison between Topic-XICL and the ICL cluster baseline shows a combined effect of (a) topic-token fine-tuning and (b) probability-based ranking within topics versus random selection within topics. But no ablation separates (a) from (b). A cleaner test would compare the full method against a variant that keeps the same clustering and topic assignment but replaces the probability-based ranking with random selection (i.e., removing the topic model's contribution while keeping everything else identical). Without this, we cannot determine whether the gains come from the learned topic tokens or simply from the cluster-based diversity combined with the Sentence-BERT matching already present in the pipeline.

### Minor

3. **Missing BM25 baseline.** The paper mentions BM25 as a standard off-the-shelf retriever in the introduction but does not include it as a baseline. Since BM25 is easy to implement and commonly used in retrieval-augmented settings, its absence is a gap. That said, BM25 is a purely lexical method unlikely to outperform Sentence-BERT on cross-lingual tasks, so this does not threaten the paper's conclusions.

4. **Bayesian framing is decorative rather than operational.** Sections 3.1–3.3 present an elaborate Bayesian derivation (Eqs. 1–5), but the actual algorithm reduces to: cluster → train topic tokens → rank by P(θ̂|X,Y) → pick top-k. There is no Bayesian update across demonstrations, no inference about θ from multiple examples jointly, and no verification that the selected demonstrations induce a posterior near 1 (the optimality condition in Eq. 5). The derivation does motivate the choice of P(θ̂|X,Y) as a ranking criterion, but the paper would benefit from either tightening the connection (e.g., showing that the selection procedure actually approximates the described objective) or simplifying the exposition to match what is implemented.

5. **Hyperparameter selection without a clearly held-out validation set.** The hyperparameters n (number of topics) and c (number of topic tokens) are chosen separately per dataset (p. 7), but the paper does not describe a held-out validation procedure. The authors reference Appendix A for guidelines, which the parsed text does not contain (and which likely exists in the original submission). If hyperparameters were selected based on performance on the same test languages reported in the main results, the reported gains could be inflated. This should be clarified in the appendix or by adding a validation-split description.

6. **The claim of being "first to apply it to non-classification tasks on XICL" is overstated.** Wang et al. (2023) applied topic-based selection to classification, and the current paper's key change is clustering data into topics (vs. treating each class as a topic) plus adding a cross-lingual topic-assignment step. This is an incremental but nontrivial extension; the "first" framing is accurate in a narrow sense but risks overclaiming.

7. **No statistical significance testing per language.** The improvements in Figure 3 are reported as raw percentage differences. Given the known variability of ICL and the modest margins (often 2–4%), it is unclear which per-language gains are statistically reliable. Reporting significance (e.g., bootstrap tests or confidence intervals) would strengthen the claims, especially for languages where the improvement is small.

### Trivial
None.

## Nice-to-Haves
- Test a topic-assignment method that uses the fine-tuned LLM directly (e.g., feed the test input with each topic token and pick the topic maximizing P(θ̂^a|X_test)). This would close the gap between the "topic inference" framing and the actual pipeline.
- Report variance across languages (not just across seeds), to give a sense of language-level robustness.
- Include a systematic analysis of what topics capture (e.g., topic-wise label distribution or performance breakdown), beyond the brief case study in Section 5.2.

## Removed Points

These points were flagged by reviewers but are removed or weakened in the final review. Treat them with caution:

- **Complaint about missing XICL baselines (Winata et al., Li et al., Tanwar et al., Shi et al.)** — Removed. These methods either require LLM parameter access (task-specific retrievers), use substantially different experimental setups, or are not standard enough to demand inclusion. The paper's baseline set (random, semantic similarity, cluster-random) covers the primary lightweight, off-the-shelf alternatives. Requesting exhaustive comparison against every cited related method is scope creep.
- **Criticism that "no sensitivity analysis is provided for alternative priors" (uniform prior assumption)** — Removed. This is a generic, one-size-fits-all request that does not harm the paper's core empirical claims.
- **Concern that XCOPA output formatting ("1" or "2") is a "task-specific hack"** — Removed. This is standard practice for XCOPA evaluation and was applied uniformly to all methods including baselines.
- **Criticism that "standard deviations are very small...suggesting either extremely stable tasks or insufficiently diverse seeds"** — Removed. Three seeds with consistent K-means initialization is a reasonable experimental design; small stds more likely reflect task stability than a flaw in the setup.
- **Strength #4 from Strength Finder ("Ablation confirms the necessity of the topic model")** — Removed because it conflicts with verified Weakness #2: the ablation tests topic-assignment methods, not the topic model's ranking, so the strength is not supported.
- **Request for "per-language breakdown with statistical significance"** — Moved to Minor weakness (kept but downgraded from Harsh Critic's stronger framing to a reasonable suggestion).

## Novel Insights

None beyond the paper's own contributions. The key finding — that learning topic-token embeddings on a compact LLM and using them to rank demonstrations within clusters yields modest but consistent improvements across models, tasks, and languages — is well-supported by the experiments and constitutes the paper's main empirical contribution. The per-language analysis showing larger gains on low-resource and unseen languages is noteworthy and deserves deeper investigation in future work.

## Suggestions

1. **Clarify the role of the topic model in the pipeline.** Either rename "topic inference" to something more precise (e.g., "two-stage topic-aware selection"), or modify the pipeline to use the fine-tuned model for test-input topic assignment as well (e.g., by checking P(θ̂^a|X_test) across topics). The latter would make the method self-contained and directly test the claim that learned topic tokens capture information beyond Sentence-BERT similarity.

2. **Add a cleaner ablation.** Compare Topic-XICL (full) against a variant that keeps the same clustering and Sentence-BERT-based topic assignment but replaces the probability-based ranking with random selection within the assigned topic. This isolates the contribution of the learned topic tokens.

3. **Acknowledge the limited role of the Bayesian framework.** Either provide evidence that the selection procedure actually approximates a Bayesian posterior (e.g., measure P(θ|demos) for chosen sets) or simplify the theoretical framing to match what is implemented: a two-stage cluster-then-rank procedure motivated by a topic perspective.

4. **Clarify the hyperparameter selection procedure** in the main text (whether n and c were selected on a held-out validation set or on the test languages themselves), and if the latter, add a validation split analysis to quantify sensitivity.

5. **Add BM25 as a baseline** for completeness, since it is mentioned in the paper's own introduction as a standard approach.

## Score and Decision

This paper presents a method with genuine empirical value: the proposed Topic-XICL consistently outperforms reasonable baselines across three LLMs, three task types (including non-classification), and many languages, with lightweight training. The cross-model transfer of learned topic tokens is a practically useful finding. However, the paper has two significant weaknesses: (1) the "topic inference" framing is partially misaligned with the actual pipeline (test-input topics are assigned by Sentence-BERT, not the learned model), and (2) the ablation does not isolate the topic model's contribution from the cluster-based design. These are addressable concerns — they do not invalidate the empirical results, but they do mean the paper's claimed novelty is narrower than advertised. The missing BM25 baseline and decorative Bayesian framing are minor issues.

Overall, this is a solid empirical paper with a moderate contribution. The weaknesses are real but not fatal.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>