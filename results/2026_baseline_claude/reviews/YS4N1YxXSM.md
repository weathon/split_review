## Summary
QUOKA is a training-free, hardware-agnostic sparse attention method for accelerating LLM prefill via chunked prefill. The key observation is that queries with low cosine similarity to the mean query attend broadly to most keys, while near-mean queries concentrate on a small shared group. QUOKA exploits this to (1) subselect informative queries via cosine dissimilarity, (2) score keys via cosine similarity, and (3) aggregate scores via GQA-aware max/mean pooling—all using standard linear algebra, making it compatible with any dense attention kernel (e.g., FlashAttention).

---

## Strengths

- **Novel geometric observation with supporting evidence.** The claim that queries far from the mean attend to broader sets of keys is backed both by Theorem 1 and by clear empirical evidence—Figure 2c shows a 0.737 correlation between $S_q$ and $\log(\max_k A)$, and Figure 2b provides geometric intuition via PCA. This is not a trivial observation and motivates the design directly.

- **Substantially outperforms all baselines across every benchmark.** On RULER (Table 1, $B_{SA}=1024$), QUOKA exceeds the next-best competitor (SampleAttention) by 10–25 points across all models and lengths. On LongBench (Table 3, $B_{SA}=512$), the gap is 20+ percentage points on some models—a large and consistent margin, not a narrow win. At $B_{SA}=25\%$ of sequence length (Table 2), accuracy drops are under 2% on most model-length combinations.

- **Hardware portability is genuinely demonstrated.** Speedups are shown on three hardware platforms: NVIDIA A100 (enterprise), NVIDIA RTX 2080 (consumer), and Intel Xeon CPU. The $5\times$ attention module speedup on A100 and nearly $7\times$ on CPU are supported by actual timing experiments averaged over 100 trials.

- **Broad model coverage.** Evaluation spans six model families (Llama 3.2-3B, Qwen 2.5-3B, Qwen3-4B, Qwen3-30B-A3B MoE, SmolLM3, GPT-OSS-20B), covering GQA, MoE, NoPE, and standard architectures. This robustness is directly relevant to practitioners.

- **Principled design choices supported by ablations.** The choice of max (not mean) across queries and mean (not max) across GQA groups is motivated by Figure 3 (heavy-tailed query deviation vs. concentrated head deviation) and validated by Tables 9–10. Ablations on $B_{CP}$, $B_{SA}$, and $N_Q$ (Tables 3, 5, 6, 11, 12) show graceful accuracy degradation.

---

## Weaknesses

### Fatal
None.

### Major

1. **Theorem 1 does not directly prove the paper's core motivating claim.** The core claim is "queries with lower cosine similarity to the mean query attend to more keys." Theorem 1 establishes an *upper bound* on $\text{CosSim}(M_Q, q^*)$ given that $q^*$ aligns with key $k$ and $M_Q$ is anti-aligned with $k$ ($\alpha_q < 0$). However: (a) the precondition $\alpha_q < 0$ is assumed rather than established as common in practice; (b) the bound being small only shows the query *can* have low cosine similarity to $M_Q$, not that it necessarily does; and (c) the theorem says nothing about attending to *many* keys versus one. The theorem supports the intuition partially, but the logical gap between it and the full claim is not closed in the paper.

2. **No formal approximation error analysis.** The paper provides no bound on $\|\text{Softmax}(QK^\top/\sqrt{d})V - \text{Softmax}(Q\hat{K}^\top/\sqrt{d})\hat{V}\|$ in terms of QUOKA's hyperparameters. While the empirical results are compelling, the absence of any formal characterization of approximation quality (e.g., under mild distributional assumptions) weakens the theoretical contribution.

3. **A single shared key set serves all queries in a chunk.** QUOKA selects one set of $B_{SA}$ keys for the entire chunk using max-aggregation over the $N_Q$ representative queries. Queries that were *not* selected (the remaining $B_{CP} - N_Q$ queries) attend to the same key set, regardless of their own preferences. The correctness argument—that near-mean queries attend to common keys and are thus well-served by this selection—is only empirically supported. Cases where this assumption breaks (e.g., documents with many independent topics in one chunk) are not analyzed.

### Minor

1. **Scores exceeding 1.0 in Table 3 for SmolLM3** (1.03 and 1.028) are not explained. While this could be noise or a regularization effect from sparsification, the paper claims QUOKA "in some cases surpasses the accuracy of dense attention" as a positive but offers no causal analysis. This could indicate a subtle evaluation issue or an interesting phenomenon worth investigating.

2. **Full-attention baseline absent from Table 1.** RULER results in Table 1 compare only sparse methods against each other; the dense attention baseline is shown separately in Table 2 only at 25% budget, making it hard to directly quantify how much accuracy QUOKA sacrifices relative to full attention in the fixed-budget $B_{SA}=1024$ setting.

3. **Selection overhead crossover point not characterized.** Figure 5 begins at 5K tokens, implying QUOKA may not be beneficial for shorter sequences. The paper does not indicate where the crossover is or provide guidance for practitioners choosing sequence length thresholds.

### Trivial

- Algorithm 2 (full chunked prefill integration) is referenced in the main text but resides in the removed appendix, creating a minor forward-reference gap.

---

## Nice-to-Haves

- An analysis of QUOKA's failure modes or the distribution of cases where the shared-key-set assumption breaks down would increase confidence in the method.
- A brief theoretical discussion of when cosine similarity is and is not a good proxy for softmax attention weights would strengthen Section 3.2.

---

## Novel Insights

The observation that cosine *dissimilarity* from the mean query predicts which queries will have broad key interactions is a concrete, novel geometric insight about LLM attention that goes beyond prior work on key geometry (Park et al., 2025). The pre-aggregation trick—averaging normalized queries across GQA groups *before* computing $\bar{Q}K^\top$—is an elegant efficiency gain that reduces complexity by a factor equal to the number of KV groups, exploiting the linearity of the mean in a way that prior GQA-aware methods have not explicitly formulated. Together these form a principled, composable design rather than an ad hoc combination of heuristics.

---

## Suggestions

- Add a sentence in Section 3.1 explicitly stating the assumption under which Theorem 1 supports the full motivating claim (e.g., that $\text{CosSim}(M_Q, k) < 0$ is empirically common) and provide statistics from actual models to close the gap.
- Include the dense-attention baseline in Table 1 to allow direct accuracy comparison at fixed $B_{SA}=1024$.
- Briefly characterize the sequence length threshold below which QUOKA adds overhead rather than saves latency.
- Investigate and explain the >1.0 LongBench scores for SmolLM3.

---

## Score and Decision

QUOKA is a practically impactful, well-evaluated sparse attention method. Its core observation is novel and supported by both theory and data. The empirical margins over baselines are large and consistent across benchmarks, model families, and hardware platforms—this is the kind of applied systems result that directly benefits practitioners. The main shortcomings are a theoretical gap between Theorem 1 and the full motivating claim, and the lack of approximation error analysis. These are meaningful limitations but do not undermine the overall contribution given the strength of the empirical evidence.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>