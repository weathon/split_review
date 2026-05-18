Now I have a thorough understanding of the paper and can verify the reviewer's claims. Let me produce the final consolidated review.

---

## Summary

Topic-XICL proposes a demonstration-selection method for cross-lingual in-context learning (XICL) that clusters English candidate examples via K-means (on Sentence-BERT embeddings) to define "topics," learns topic-specific token embeddings on a small LLM (BLOOMZ-1b7), then selects the most representative demonstrations per topic by the LLM's estimated topic probability. Target-language inputs are assigned to a topic via a Sentence-BERT similarity heuristic, and the corresponding topic demonstrations are used as context for any downstream LLM. The method is evaluated on three tasks (XNLI, XCOPA, TyDiQA-GoldP) across three 7–8B parameter LLMs (BLOOM, Qwen1.5, Llama3.1), consistently outperforming random selection, Sentence-BERT similarity, and within-cluster random sampling baselines by 1.77%–3.32% absolute on average.

## Strengths

- **Consistent empirical improvements across tasks, models, and languages**: Topic-XICL outperforms all baselines on all three tasks and all three LLMs. The gains are especially notable for low-resource and unseen languages (e.g., +10.9% for Vietnamese on XCOPA with BLOOM, +10.3% for Bengali on TyDiQA-GoldP with BLOOM). The ablation (Figure 5) confirms that each component of the pipeline contributes to the gains.

- **Lightweight, model-agnostic topic model that transfers across LLMs**: The topic model is trained on a compact 1.7B-parameter LLM (BLOOMZ-1b7) in 15–30 minutes by fine-tuning only the added topic token embeddings (all other parameters frozen). Once trained, it selects demonstrations for any downstream LLM without additional training or parameter access. Even a 560M-parameter topic model still outperforms baselines on XCOPA and TyDiQA (Figure 7).

- **Thorough analysis validating the learned topics**: The t-SNE visualization (Figure 6) shows that learned topic token embeddings form coherent regions, and the case study (Section 5.2) confirms that topics capture structural and domain-level information (e.g., biology, sports, passage length) beyond surface-level semantic similarity.

- **Demonstrated generalization to non-English source languages**: When using Chinese or Italian (translated from English XCOPA) as the source language, Topic-XICL still outperforms baselines, and Italian even surpasses English on Llama3.1 (Figure 9), showing the method is not tied to English.

## Weaknesses

### Fatal
None.

### Major

1. **The claimed Bayesian theoretical grounding is not sound as presented.** The paper grounds its method in the Bayesian ICL framework of Xie et al. (2022) and Wang et al. (2023), claiming to "extend Bayesian inference theory to practical applications in cross-lingual ICL." However, there is a logical gap between the theory and the implementation. The derivation (Eq. 7–8) assumes that clusters produced by K-means on Sentence-BERT input embeddings correspond to coherent latent topic variables θ^a that causally influence Y given X — an assumption that is never justified. In Wang et al. (2023), each topic corresponded directly to a class label, which is a natural latent variable. Here, K-means clusters are defined purely on input embeddings; nothing guarantees that examples in the same cluster share a common causal structure relating input to output. The factorization in Eq. 8 further assumes conditional independence of demonstrations given θ^a without discussion. The paper's own case study (Section 5.2) shows clusters capturing domain-level information (sports, biology), but domain ≠ a latent variable that causally influences the *output* given the *input* in the sense required by the theory. **This does not invalidate the empirical results** — the method works on its own merits — but the paper's framing substantially overclaims what the theory justifies. The paper should either substantially revise the theoretical claims, presenting the method as a practical heuristic inspired by (rather than instantiating) Bayesian inference, or provide rigorous justification for why K-means clusters satisfy the Bayesian assumptions.

### Minor

2. **The target-language topic assignment is disconnected from the trained topic model.** For target inputs, the topic is determined by: (a) Sentence-BERT similarity to all source candidates, (b) taking the top-10 most similar, (c) taking the most frequent topic among those 10. This means the fine-tuned topic model (which required training a 1.7B LLM) is used only for intra-cluster *ranking* of demonstrations, while the actual topic *assignment* relies entirely on Sentence-BERT + K-means — a completely different representation. The ablation (Figure 5) tests simpler alternatives (top-1 topic, K-means prediction) and shows the top-10 heuristic works best, which partially addresses this concern. But the paper does not explore the more principled alternative of using the fine-tuned topic model directly for target input classification (e.g., appending all topic token sequences and taking argmax over P(topic|X)). Including and discussing this alternative would make the method more coherent.

3. **The "first to apply Bayesian theory to non-classification XICL" claim is overstated.** The method for TyDiQA-GoldP (QA) uses the same pipeline as for classification — the Bayesian derivation does not depend on the nature of Y. The real contribution is that the method *works empirically* for QA and causal reasoning tasks, not that it extends the theory. The paper should reframe this claim accordingly.

4. **Missing cost-benefit discussion.** The paper reports training takes "only 15-30 minutes" but does not report GPU type, GPU-hours, or peak memory usage. Since the method requires training a 1.7B-parameter model (vs. zero-training baselines), practitioners need concrete resource figures to assess whether the 1.77%–3.32% average gains justify the cost. This is especially relevant since for the simpler classification task (XNLI), the gains are the smallest (1.77%).

### Trivial

5. **The explanation for the smaller model's failure on XNLI is vague.** The paper notes that BLOOMZ-560m works for XCOPA and TyDiQA but fails on XNLI, offering the explanation that "simpler classification tasks may need more clarity clustering information." Since XNLI is a classification task (the simplest of the three), this non-explanation is self-contradictory and deserves a more principled diagnosis.

## Nice-to-Haves

- Add a cross-lingual adaptation of Wang et al. (2023) as a baseline for XNLI (treating each class label as a topic). This would directly isolate the value of the clustering-based topic discovery.
- Add a controlled experiment comparing the topic model's ranking of candidate demonstrations against Sentence-BERT similarity ranking, using the target LLM's own perplexity on (X,Y) pairs as the ground truth. This would validate that the topic model captures signal the target LLM actually cares about.
- Provide hyperparameter sensitivity analysis for n (number of topics) and c (tokens per topic). Currently only one configuration per dataset is reported, and the guidelines mentioned in Appendix A are absent in this extract.

## Removed Points

- **"Baseline comparison incomplete — need fine-tuning without topic tokens"**: This suggestion has face validity but the concern is substantially addressed by the existing ablations (Figure 5), which show that simpler topic assignment methods are weaker than the full method, and by the ICL cluster baseline, which uses the same clustering with random selection. Additionally, a fair comparison would need a parameter-efficient fine-tuning approach comparable to the paper's frozen-parameters setup. Moved here because the underlying concern (is it fine-tuning or topic structure?) is real but already partially addressed by the paper's experiments, and the reviewer's specific proposed baseline is not standard in the demonstration-selection literature.
- **"Missing Wang et al. (2023) cross-lingual baseline"**: A reasonable suggestion for the classification task (XNLI), but only one of three tasks; moved to Nice-to-Haves.
- **"Cross-model transfer under-explained"**: The paper provides t-SNE analysis and empirical results. More analysis would strengthen the paper but its absence is not a weakness. Moved here as a suggestion.
- **"Missing limitations section"**: The paper does not have one, but this is a presentation choice many papers make. Not a substantive weakness.

## Novel Insights

The most interesting observation that emerges across the reviews is the implicit finding that **a model trained on one LLM (BLOOMZ-1b7) to estimate topic probabilities can successfully select demonstrations for other, larger LLMs (BLOOM 7B, Qwen1.5 7B, Llama3.1 8B) without any adaptation**. This cross-model transfer is non-trivial and suggests that the topic model captures properties of the *task data* (input-output structure) rather than model-specific preferences. The visualization (Figure 6) partially supports this by showing that the learned topic tokens form coherent regions. The paper would benefit from explicitly highlighting this transfer finding as a main contribution rather than burying it in the results.

## Suggestions

1. **Substantially revise the theoretical framing.** Remove or qualify the claim of "extending Bayesian inference theory." Present the Bayesian derivation as *motivation/inspiration* rather than as a valid instantiation of the theory. The method's value is empirical; let it stand on that.

2. **Add an experiment using the fine-tuned topic model for direct topic inference on target inputs** (computing P(topic|X) by appending each topic's tokens and taking the argmax). Report whether this works, and if it fails, discuss what the failure tells us about what the topic model learns.

3. **Report concrete compute requirements** (GPU type, hours, peak memory) and discuss the practical cost-benefit tradeoff.

4. **Diagnose why BLOOMZ-560m fails on XNLI.** Analyze whether the issue is the number of topics (n=20 for XNLI vs. n=5 for XCOPA), the task complexity, or model capacity.

5. **Tone down the "first to apply Bayesian theory to non-classification" claim** — the real novelty is empirical.

## Score and Decision

The paper makes a solid empirical contribution: a practical demonstration-selection method that consistently improves XICL across tasks, models, and languages, supported by thorough ablations and analysis. The main weakness is a significant overclaim in the theoretical framing, but this does not invalidate the empirical results. The remaining issues (disconnected target topic assignment, missing resource reporting, a vague explanation) are addressable with moderate revisions.

**Score**: 6.5

**Decision**: Accept

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>