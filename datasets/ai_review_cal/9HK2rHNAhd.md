- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 3, 5, 8
Now I have a thorough understanding of the paper and all the reviewer claims. Let me write the final consolidated review.

## Summary

This paper proposes SqueezeAttention, a 2D KV-cache compression algorithm that jointly optimizes cache budgets across both the sequence dimension (existing token-eviction methods) and the layer dimension (novel contribution). The key idea is to measure each layer's importance via the cosine similarity of hidden states before and after self-attention, cluster layers into groups by importance, and reallocate the KV-cache budget — giving less budget to "unimportant" layers and more to important ones. Experiments on 7 LLMs (6.7B–70B) with 3 sequence-wise compressors (H2O, Sliding Window, StreamingLLM) across 5 datasets show that SqueezeAttention achieves better accuracy with 20–30% cache budget versus 30–60% for baselines, saving 30–70% memory and improving throughput up to 2.2× over Full Cache.

## Strengths

- **Novel and well-motivated layer-wise compression framework.** The paper identifies that existing KV-cache compression treats all layers equally, missing a clear optimization opportunity. The 2D view (sequence × layer) is a natural extension that has been underexplored. Algorithm 1 provides a concrete, reproducible instantiation of this idea, showing how cosine similarity scores from the prefilling phase are used to cluster layers and redistribute budgets on-the-fly.

- **Consistent accuracy improvements across a broad experimental scope.** The results span 7 LLMs (Mistral-7B, Llama2-7B/70B, Falcon-7B, OPT-6.7B, GPT-NeoX-20B, Mixtral-8×7B), 5 datasets (CNN/DM, XSUM, SAMSUM, NarrativeQA, TriviaQA), and 3 sequence-wise baselines (H2O, Sliding Window, StreamingLLM). Figure 3 shows that SqueezeAttention consistently improves or matches the best baseline's accuracy across budget levels ranging from 10–100%. The memory budget comparison (Table 2) is directly evidence: SqueezeAttention achieves the same accuracy as baselines with roughly half the KV-cache budget (e.g., 20% vs 60% for GPT-NeoX-20B on XSUM).

- **Orthogonality to existing methods.** SqueezeAttention is designed as a drop-in layer on top of any sequence-wise eviction policy. The paper demonstrates successful integration with three distinct algorithms (H2O, Sliding Window, StreamingLLM) across multiple architectures, showing that the layer-wise reallocation works independently of the token-selection strategy.

- **Low overhead.** The additional computation (cosine similarity + KMeans clustering) occurs only during the one-time prefilling phase, adding only 6.3% overhead to prefilling time (Table 5). This overhead amortizes over the full decode phase, making the method practically efficient.

## Weaknesses

### Fatal
None.

### Major

- **The end-to-end accuracy gains in Figure 3 are modest for some tasks, and practical relevance is not discussed.** For tasks like XSUM, the absolute improvement is approximately 0.03–0.04 ROUGE-2 (roughly a 33–50% relative improvement from a low base of ~0.08), while for TriviaQA the improvement is much larger (roughly 10–15 F1 points). The paper reports these results without discussing which types of tasks benefit more from layer-wise reallocation or what the practical significance of these gains is. This makes it harder for readers to gauge when the method is worth deploying.

### Minor

- **Cosine similarity as an importance metric is plausible but not directly ablated.** The paper's intuition — that layers with high cosine similarity (embedding changes little) are less important — is reasonable, but no ablation compares the metric against alternatives (e.g., random budget allocation, inverse-similarity assignment, or an entropy-based metric). End-to-end results demonstrate the method works, but they do not isolate whether the specific metric drives the gains or whether a simpler heuristic would suffice. Adding even one ablation (e.g., random allocation at fixed total budget) would substantially strengthen the evidence for the metric's causal role.

- **The main paper defers the throughput comparison against sequence-wise baselines to the appendix.** Table 3 compares SqueezeAttention only against Full Cache. While the appendix (referenced in the caption) contains the head-to-head comparison, readers of the main body cannot determine how much additional throughput SqueezeAttention provides on top of H2O/Sliding Window/StreamingLLM alone. Since the paper positions itself as improving upon these baselines, having this comparison prominently in the main body would better support the contribution claims.

- **Prompt-level variance in layer importance is not discussed.** The cosine similarity scores are averaged over 200 prompts per model (Section 3), but no analysis shows how stable the layer importance rankings are across individual prompts. If importance is highly variable per prompt, the on-the-fly clustering is essential; if stable, static precomputed budgets might suffice. A few sentences addressing this would help clarify the necessity of the per-prompt clustering step.

- **Hyperparameter choices (p=0.3–0.4, 3 KMeans groups) have reasonable motivation but no sensitivity analysis in the main text.** The paper explains why 3 groups are natural (Section 4.2) and notes that p=0.3–0.4 works well empirically, but defers sensitivity to the appendix. While this is not a fatal gap (the choices work empirically across 7 models), including even a single sensitivity figure in the main paper would strengthen confidence in generalizability.

- **Minor algorithmic edge cases are not addressed.** Algorithm 1 does not specify what happens when a layer's allocated budget exceeds the current sequence length (common for early tokens). The budgets should be implicitly capped, but this is not stated. Similarly, the algorithm only reduces budgets below b_init — it never increases them, even though redistributing saved budget could allow some important layers to exceed the initial unified budget.

- **Table 2 column headers could be clearer.** The labels "w/ \sys" and "w/o \sys" under the "Performance / Used KV Budget" header are ambiguous on first read. Renaming to "Baseline + SqueezeAttention" and "Baseline alone" would improve clarity.

### Trivial
None that warrant independent listing beyond the minor points above.

## Nice-to-Haves
- **Error bars or variance estimates.** No statistical uncertainty is reported for any metric. Given the modest per-task sample sizes (200 for NarrativeQA, SAMSUM, and TriviaQA), reporting variance across runs or bootstrapped confidence intervals would improve reproducibility assessment. This is noted as a nice-to-have because single-run evaluation without error bars is standard practice in the LLM compression literature.
- **Experimental comparison with FastGen.** FastGen selects per-head eviction strategies but uses a unified budget for layers sharing the same strategy, making it a natural point of comparison. The paper discusses FastGen as complementary but does not benchmark against it directly. An ablation showing that SqueezeAttention's budget reallocation adds value on top of FastGen's strategy selection would strengthen the positioning.

## Removed Points
- *"Throughput claims lack direct comparison against baseline methods"* (from Harsh Critic): The paper is clear that Table 3 compares against Full Cache (caption: "with \sys and Full Cache"). The comparison against sequence-wise baselines exists in the appendix (referenced as `\ref{throughput comparison between best baseline and squeezeattention}`), which is present in the full submission. The rule requiring removal of criticisms about missing appendix content applies, and the claim as stated misreads the table's clearly stated comparison target. A softened version (about main-body evidence distribution) is retained as a Minor weakness.
- *"KMeans on 1D data is overkill"*: Pure implementation-style nitpick with no bearing on the paper's validity or contribution.
- *"Statistical significance / no error bars"*: Moved to Nice-to-Haves per the soft rule about field-standard practices. Single-run evaluation is the norm in this area.
- *"Strength: Novel layer-wise importance metric validated across models"* from Strength Finder: Retained (it is specific and supported by the heatmaps). However, the strength is accurate — the metric IS validated by showing consistent cross-model patterns and by the method's empirical success.
- *"Missing related works"*: Not included per the rule about not mentioning missing related works without external verification.

## Novel Insights
None beyond the paper's own contributions. The key insight — that layer-wise cosine similarity patterns correlate with optimal budget allocation — is the paper's own discovery, and the reviews do not surface a fundamentally different lens on the work.
