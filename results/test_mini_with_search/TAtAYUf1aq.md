Now I have everything I need. Let me synthesize the final review.

**Round-1 bracket:** After reading the first calibration results, I determined the paper sits between 4 and 7 — clearly stronger than the rejected bio-inspired papers (2.50) and much weaker than top-tier papers (8.00), but in the range of comparable memory-augmented Transformer papers.

**Round-2 narrowing:** I read Hippoformer (5.00, accepted), RMAAT (5.60, accepted), MeSH (4.50, accepted), Elastic Memory (4.50, rejected), and Artificial Hippocampus Networks (2.50, rejected) in full. Memoria is slightly weaker than Hippoformer (which had better ablation/analysis) and RMAAT (which had ablation on retention factor), comparable to MeSH and Pretraining with Hierarchical Memories (4.80), but stronger than Artificial Hippocampus Networks and Language Models Need Sleep (2.50).

**Final score: 4.5**

---

## Summary

This paper proposes Memoria, a memory module for Transformers inspired by Hebbian theory and the Multi-Store model of human memory (working, short-term, long-term stores). Memoria stores information as "engrams" connected in a directed graph updated by co-activation counts (Hebbian "fire together, wire together"), retrieves relevant engrams via correlation-based selection and graph traversal (DFS), and forgets via lifespan decay. The module is architecture-agnostic and is evaluated on sorting, language modeling (WikiText-103, PG-19, enwik8), and long-document classification (Hyperpartisan). Memoria achieves consistent improvements over Transformer-XL, Compressive Transformer, and ∞-former across all tasks, with the most pronounced gains on the sorting task and statistically significant improvements on classification.

## Strengths

- **Consistent improvements across three language modeling benchmarks**: Memoria Transformer achieves the best perplexity/BPC on WikiText-103 (20.17 vs 20.35 for ∞-former, 20.46 for Transformer-XL), PG-19, and enwik8 (Table 1). The improvement is small but consistent across all three datasets, supporting robustness.

- **Clear gains on the sorting task with increasing sequence length**: Memoria shows substantially less performance degradation than Transformer-XL, Compressive Transformer, and ∞-former as input length grows from 1K to 32K tokens across all segment lengths (Figure 4). This provides the strongest visual evidence that the memory architecture preserves long-range frequency information.

- **Evidence of genuine long-term retrieval via average age analysis**: The average age of reminded LTM engrams increases steadily over steps (Figure 5), demonstrating that Memoria retrieves old engrams rather than only recent ones — a non-trivial validation that the mechanism works as designed.

- **Statistically significant gains on long-document classification**: Memoria RoBERTa achieves the highest macro F1 (0.93) and accuracy (0.93) on Hyperpartisan, with a one-tailed t-test showing significance over Longformer (p=0.045) and BigBird (p=0.005) across five runs (Table 3). This provides rigorous statistical evidence in the encoder-based setting.

- **Architecture-agnostic design**: Memoria is successfully integrated with both decoder-only (GPT-family, Section 4.2) and encoder-based (BERT/RoBERTa, Section 4.3) Transformers, with positive results in both causal and bidirectional settings, supporting the claim of generality.

- **Validation under challenging short-segment conditions**: When segment length is reduced to 50 tokens (Table 2), Memoria shows a larger perplexity gap over baselines, demonstrating effectiveness when many segments must be linked.

## Weaknesses

### Fatal
None.

### Major

- **No ablation studies isolate any component's contribution**: The paper presents a multi-component system (three memory stores, graph-based retrieval via DFS, correlation-based selection, lifespan updates, Hebbian co-occurrence counting) but performs zero ablation experiments. The improvements over baselines could plausibly come from the generic addition of extra memory tokens with cross-attention, the abstractor encoder, or the lifespan mechanism — none of which is distinctively Hebbian. Without ablations comparing, e.g., a simple FIFO queue with similarity-based retrieval against the full Memoria, or removing the graph traversal, the paper's central claim — that Hebbian theory and the three-level architecture produce the gains — is unsupported. This is the most consequential weakness: the evaluation cannot attribute results to the proposed mechanism.

- **Missing comparison to closely related memory-augmented Transformers cited in the paper**: The related work section (line 27–28) discusses Recurrent Memory Transformer (Bulatov et al., 2022) and Memorizing Transformers (Wu et al., 2022), which are directly comparable and have been evaluated on the same benchmarks (e.g., WikiText-103). Neither appears in the results tables. If Memoria outperforms these, the case is strengthened; if it does not, the contribution is weaker than implied. The current baseline set (Transformer-XL, Compressive Transformer, ∞-former) is necessary but not sufficient to establish relative merit against the closest contemporaries.

- **Language modeling results lack variance or significance testing**: On WikiText-103, Memoria's perplexity of 20.17 versus 20.35 for ∞-former and 20.46 for Transformer-XL represents ~1–2% relative improvement. No confidence intervals, standard errors, or multi-run statistics are reported for any language modeling result (Tables 1 and 2). The classification experiments report five-run averages with t-tests and p-values — the LM experiments should follow the same standard. Without such reporting, it is impossible to determine whether the claimed improvements are statistically reliable or could arise from random seed variation.

### Minor

- **Classification comparison is not apples-to-apples**: The comparison between Memoria BERT/RoBERTa and Longformer/BigBird (Table 3) is acknowledged by the authors as not direct: the latter are pretrained with long-document objectives, while BERT and RoBERTa are not. The p-values against Longformer (0.045) and BigBird (0.005) are reported, but it is unclear whether the same hyperparameter search was conducted for all baselines. A cleaner comparison would be Memoria RoBERTa versus RoBERTa + Longformer-style sparse attention.

- **Average age of reminded engrams does not measure retrieval correctness**: Figure 5 shows that the average age of reminded LTM engrams increases over time, which confirms the mechanism is retrieving old engrams. However, it does not demonstrate that those engrams are semantically relevant or useful — only that they are old. An analysis of retrieval quality (e.g., precision-recall on a diagnostic task) would strengthen the claim.

- **Computational overhead and scaling not discussed**: The paper does not report training time, memory usage, or wall-clock speed relative to baselines. Maintaining and traversing a dynamically growing directed graph (DFS with pairwise count updates O(N²) per step) has non-trivial cost as the number of LTM engrams grows unboundedly. This is a practical concern for deployment on long sequences.

- **Co-occurrence-based edge weights may introduce noise**: Edge weights are defined as empirical conditional probabilities based on co-reminding counts, incremented for *all* pairs in the activated set each step regardless of semantic relatedness. Two engrams that co-occur repeatedly by accident will be strongly connected. The paper does not discuss whether this introduces noise, nor does it compare against a simpler similarity-based retrieval.

- **DFS traversal may produce narrow retrieval paths**: The traversal follows highest-weight edges deterministically (Section 3.2, step 5), which could lead to a narrow, path-dependent retrieval. The paper does not justify why depth-first rather than breadth-first or weighted sampling is the appropriate choice.

### Trivial
- The paper claims trace decay theory for forgetting but implements a uniform global decrement on lifespan, which is a simplified interpretation. This is a minor mismatch worth clarifying.

## Nice-to-Haves
- Reporting computational overhead (training time, memory) relative to baselines.
- Adding variance or confidence intervals for all language modeling results.
- A qualitative analysis or precision-recall measure showing that the retrieved engrams are semantically relevant, not just old.
- Ablation of the graph traversal strategy (DFS vs. BFS vs. weighted sampling vs. no graph).

## Removed Points
- **Criticism about segment length being too short (150 tokens):** The paper already addresses this by showing even larger gaps at segment length 50 (Table 2). The comparison is against the same baselines under identical conditions, so the setting is fair.
- **Criticism about missing reproducibility details (abstractor sizes, cross-attention specifics):** The paper provides the abstractor definition (Equation in Section 4.1) with Q, Wk, Wv parameters and describes the cross-attention mechanism. For a conference paper, these are adequately specified.
- **Criticism about missing appendix content:** The parser strips appendices; they exist in the original submission.
- **Generic concerns about "could the metric be measuring a proxy" without specific evidence:** Removed as speculative.
- **Several formatting/style nitpicks:** Removed as parser artifacts or non-substantive.

## Novel Insights

A genuinely novel observation emerging from combining the reviews is that while Memoria's design is the most comprehensive implementation of cognitive memory theory (Hebbian plasticity, three-store model, trace decay, displacement) among recent memory-augmented architectures, this very comprehensiveness creates an attribution problem: the more components a system has, the more essential controlled ablations become to isolate the functional contribution of each. The paper's strongest empirical result — the sorting task — actually provides the most credible evidence for the approach, yet it is also the task where the advantage of graph-based associative retrieval over simpler alternatives is least surprising. The paper would substantially benefit from identifying which of its many design choices is the critical one, rather than presenting the entire system as an indivisible whole.

## Suggestions

1. **Add ablation studies as the top priority.** Compare full Memoria against at least: (a) Memoria without the memory graph (FIFO queue + similarity-based retrieval), (b) Memoria without lifespan decay (infinite lifespan), (c) a version using random retrieval instead of DFS, (d) a version using BFS or sampling instead of DFS. This would isolate whether the Hebbian graph and its traversal actually drive the gains.
2. **Add Memorizing Transformers and Recurrent Memory Transformer to the LM baselines** on at least one dataset (e.g., WikiText-103) to establish where Memoria sits relative to its closest contemporaries.
3. **Report multi-run statistics (mean ± std over at least 3 seeds) for all language modeling results**, matching the rigor shown in the classification experiments.
4. **Discuss computational complexity explicitly** — report training time, inference speed, and memory overhead relative to baselines, especially since the graph maintenance has non-trivial cost.

## Score and Decision

**Calibration Anchors Used (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| UUW0DHqs4f (Artificial Hippocampus) | 2.50 | R1 | Weaker — less evidence, narrower eval |
| iiZy6xyVVE (Sleep) | 2.50 | R1 | Weaker — no functional method details |
| slNz3N216N (Hierarchical Bio) | 1.00 | R1 | Much weaker — withdrawn, pseudo-science |
| WMeIXD8r81 (Learn to Remember) | 3.00 | R1 | Slightly weaker — narrower scope |
| XOu5z16cbY (Pretrain Hier Memories) | 4.80 | R1 | Comparable — similar quality, accepted poster |
| eZ5jtFuk3e (Meta-Tokens) | 5.60 | R1 | Slightly stronger — better analysis |
| 15KpLriUTU (PUM-Net) | 4.00 | R1 | Slightly weaker — less comprehensive |
| Iskm1kYo70 (Elastic Memory) | 4.50 | R1 | Comparable — rejected but similar issues |
| hxwV5EubAw (Hippoformer) | 5.00 | R2 | Slightly stronger — better ablations/analysis |
| sTkJdbVxsI (RMAAT) | 5.60 | R2 | Slightly stronger — ablation on retention factor |
| IhTrFvY7p3 (MeSH) | 4.50 | R2 | Comparable — similar evidence level, accepted |
| gZyEJ2kMow (Attentional Bias) | 4.50 | R2 | Comparable — similar scope |

Round-1 bracket: [4, 7]. Round-2 narrowing placed the paper near the lower end of this bracket, comparable to MeSH (4.50) and Elastic Memory (4.50) but below Hippoformer (5.00) and RMAAT (5.60). Final score: 4.5.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>