Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes Topic-XICL, a demonstration selection method for cross-lingual in-context learning (XICL) that trains a latent topic model on a compact LLM (BLOOMZ-1.7B) and selects demonstrations via topic inference. The method first clusters English training data into topics using K-means on multilingual Sentence-BERT embeddings, then learns topic-specific token embeddings by fine-tuning a small LLM. For each test instance, its topic is inferred via semantic similarity, and the top-\(k\) candidates (ranked by topic-model probability) within that topic serve as demonstrations. Experiments on XNLI, XCOPA, and TyDiQA-GoldP across three LLMs (BLOOM, Qwen1.5, Llama3.1) report average gains of 1.77–3.32% over clustering-based and semantic-similarity baselines.

---

## Strengths

1. **Novel application area.** The paper extends Bayesian-inference-based demonstration selection (previously limited to monolingual classification) to cross-lingual settings and non-classification tasks (reasoning, QA). This is a genuine extension of prior work by Wang et al. (2023).

2. **Consistent empirical trends across tasks and models.** Table 1 reports that Topic-XICL outperforms the strongest baseline (ICL cluster) on average across three LLMs on TyDiQA-GoldP (+3.32%), XCOPA (+2.47%), and XNLI (+1.77%). Per-language results in Figure 3 show meaningful gains on several low-resource and unseen languages (e.g., +10.3% on Bengali for BLOOM in TyDiQA, +10.9% on Vietnamese for BLOOM in XCOPA).

3. **Practical efficiency.** The topic model trains on BLOOMZ-1.7B in 15–30 minutes (Section 5.3), and the learned topic tokens transfer to different target LLMs (BLOOM, Qwen1.5, Llama3.1) without retraining. Even with BLOOMZ-560M, the method maintains gains on two of three tasks.

4. **Ablation study provides partial validation.** Figure 5 shows that the full Topic-XICL method outperforms variants with simpler test-instance topic classification (top-1 topic, k-means predict), confirming that the topic-inference-based classification step contributes positively.

5. **Generalizability to non-English source languages.** Experiments with Chinese and Italian as source languages (Section 5.4, Figures 8–9) show that Topic-XICL consistently outperforms baselines, and Italian even surpasses the English-based baseline on Llama3.1.

---

## Weaknesses

### Fatal
None.

### Major

1. **The contribution of the learned topic tokens is not fully isolated from within-cluster ranking.**  
   The key baseline, ICL cluster, uses the same K-means clustering and the same test-instance topic classification as Topic-XICL but *randomly* samples \(k\) demonstrations per cluster. Topic-XICL ranks candidates within each topic using the topic-token probabilities and selects top-\(k\). The improvement over ICL cluster could therefore come from *any* sensible within-cluster ranking, not specifically from what the topic tokens capture. The paper does not include a control where within-cluster ranking is done by a simpler method (e.g., Sentence-BERT similarity to the cluster centroid). Without this, the central claim that the topic model "learns additional features automatically through the Topic variables" (Section 4.4) is not fully substantiated — the ranking mechanism itself, rather than the specific learned representation, may be responsible for the gains. The ablation study (Figure 5) only varies how test instances are assigned to topics, not how candidates are selected within a topic.

2. **Baseline set is limited and does not include stronger off-the-shelf retrievers.**  
   The paper compares only against random selection, Sentence-BERT semantic similarity, and cluster+random. While these are reasonable starting points, the field has competitive off-the-shelf cross-lingual retrievers (e.g., LaBSE, XLM-R-based retrieval) that could set a higher bar. The paper argues against task-specific retrievers (which are expensive), but does not compare against lightweight multilingual retrievers that are directly relevant. Without these comparisons, the claimed improvements sit in a weaker reference frame than necessary.

### Minor

3. **Inconsistent gains and selective reporting.** The paper's overall averages (1.77% on XNLI) can mask per-model failures. The text acknowledges that on XNLI, "apart from BLOOM's performance on the unseen language Turkish (tr), where it did not surpass the strongest baseline" — but does not disclose whether Topic-XICL underperforms ICL cluster on BLOOM for XNLI overall (the critic's reported numbers suggest this may be the case). Per-model breakdowns are not provided in the main results table, making it difficult to assess where the method truly helps versus where it hurts. Given overlapping standard deviations in some settings, this is a reporting gap.

4. **No statistical significance testing.** Given the variance across languages and seeds, paired bootstrap tests or signed tests per language would clarify whether the improvements are reliable. The paper reports standard deviations but does not test significance.

5. **The Bayesian theoretical framing has a loose connection to the algorithm.** The paper derives its method from the Bayesian ICL framework of Wang et al. (2023), but the practical instantiation — K-means clusters on Sentence-BERT embeddings treated as "topics," with learned token embeddings — does not clearly correspond to the latent variable \(\theta\) in the theoretical model. The gap between theory and practice is substantial; the algorithm could be described and evaluated without the Bayesian framing. This does not invalidate the method but weakens the claimed theoretical contribution.

6. **Brittleness on simpler tasks with a smaller topic model.** When trained on BLOOMZ-560M, the method fails on XNLI (classification), with most languages falling below the strongest baseline (Section 5.3). The paper briefly notes this ("more clarity clustering information may be necessary") but does not analyze why the method degrades specifically on classification versus reasoning/QA. This inconsistency raises questions about robustness.

### Trivial

- The paper reports that BLOOMZ-560m and BLOOMZ-1b7 have "approximately the same" training time (15-30 minutes), but the sentence in Section 5.3 appears to be cut off/grammatically incomplete.
- Some figure references in the text (e.g., "Table 9" on line 227) seem to point to figures that are not clearly labeled in the provided text.

---

## Nice-to-Haves

- **Within-cluster ranking ablation:** Compare Topic-XICL's probability-based within-cluster ranking against ranking by semantic similarity to the cluster centroid (or to the test instance). This would isolate whether the learned topic tokens add value beyond simple ranking within clusters.
- **Stronger baselines:** Add at least one additional off-the-shelf cross-lingual retriever (e.g., LaBSE) to calibrate the reference frame.
- **Statistical testing:** Report paired bootstrap tests or per-language signed tests for the main comparisons.
- **Sensitivity analysis:** Vary the number of topics \(n\) and topic tokens \(c\) on at least one dataset to show how robust performance is to these hyperparameters.
- **Per-model breakdown:** Include a table or figure showing results separately for each model on each dataset, not just grand averages.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism that Figure 1 caption does not clarify "sem":** The caption explicitly states "'sem' refers to semantic-based selection, while 'random' refers to random selection." This claim is factually incorrect and is removed.
- **Criticism about not testing target LLM as topic model:** The paper's design choice (training on BLOOMZ, testing on other LLMs) is intentional to demonstrate transferability. Testing the target LLM as the topic model would test a different research question. Moved to Nice-to-Haves.
- **"Section 5.4 is inconclusive":** The paper explicitly acknowledges this ("no clear conclusion as to which source language's demonstrations provide more benefit") and frames it as an exploratory analysis. Criticizing it for being inconclusive misreads the section's purpose.
- **Strength Finder's claim of "statistically significant" improvements:** The paper does not report significance tests, so this claim overstates what is supported. The strength is kept but reworded to remove "statistically significant."

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine methodological gap (the missing within-cluster ranking ablation) that the paper's own analysis does not address, but do not reveal a fundamentally new perspective on the work.

---

## Suggestions

1. **Add a within-cluster ranking ablation.** This is the single most impactful addition: compare Topic-XICL (rank by topic-token probability) against within-cluster ranking by Sentence-BERT similarity to the cluster centroid. If Topic-XICL still wins, the learned topic tokens are doing meaningful work. If not, the contribution reduces to "any reasonable within-cluster ranking beats random."
2. **Provide per-model per-dataset breakdowns** in the main paper, not just grand averages. This allows readers to see where the method succeeds and fails.
3. **Add at least one stronger baseline** from off-the-shelf multilingual retrievers (e.g., LaBSE) to strengthen the evidential bar.

---

## Score and Decision

The paper proposes a clearly motivated approach with a plausible mechanism and provides broad empirical validation across three tasks and three LLMs. The main weakness — that the contribution of the learned topic tokens is not fully isolated from simple within-cluster ranking — is addressable but does not invalidate the overall finding that the method outperforms baselines. The baseline set, while not exhaustive, includes the most natural comparisons (random, semantic, cluster-random). The work is a solid applied contribution to cross-lingual demonstration selection, with a practical efficiency profile that makes it usable in resource-constrained settings. The weaknesses are not fatal and can be addressed with additional analysis.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>