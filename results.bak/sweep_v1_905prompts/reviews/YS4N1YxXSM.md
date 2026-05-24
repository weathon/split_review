Now I have a thorough understanding of the paper and all the reviewer claims. Let me write the consolidated review.

## Summary

QUOKA proposes a training-free, hardware-agnostic sparse attention method designed specifically for chunked prefill in LLM inference. The core idea is to identify "informative" queries (those with low cosine similarity to the mean query) and then select keys via cosine similarity to those representative queries, reducing the effective KV cache to ~12% of tokens. The paper evaluates on NIAH, RULER, LongBench, and Math500 across 5+ model families, showing near-baseline accuracy while achieving up to 5× attention speedups on A100 GPUs and 7× on CPUs.

## Strengths

- **Consistent and large-margin improvements over all baselines across diverse settings**: On RULER (Table 1), QUOKA outperforms the best baseline (SampleAttn) by 10–25+ absolute points across 5 models and 4 sequence lengths (e.g., 57.01 vs. 31.73 on Llama3.2-3B at 32k). On LongBench (Table 3), QUOKA maintains normalized accuracy ≥0.945 even at B_SA=512, while baselines drop to 0.7–0.8. No sparse attention baseline beats QUOKA on any model/sequence-length/budget combination reported.

- **Large latency reductions verified across heterogeneous hardware**: Figure 5 reports attention speedups of ~5× on A100, ~7× on Intel Xeon CPU, and ~5–6× on RTX 2080, all with B_CP=128. TTFT improves 3× at 50k tokens. These are concrete, multi-platform measurements, not just FLOP counts.

- **Strong generalization across diverse model families**: Evaluated on 6 models (Llama3.2-3B, Qwen2.5-3B, Qwen3-4B, Qwen3-30B-A3B MoE, SmollM3, GPT-OSS-20B), covering RoPE, NoPE, MoE, and various scales (3B–30B). QUOKA is the top performer on every model at every sequence length in RULER.

- **Well-motivated, simple, and portable design**: The algorithm uses only standard linear algebra (mean, cosine similarity, top-k), requires no training, and is compatible with any dense attention kernel (e.g., FlashAttention). The core intuition—queries with low cosine similarity to the mean query attend to more keys—is supported by empirical evidence (Figure 2).

## Weaknesses

### Major

- **NIAH results show QUOKA outperforming Full attention without explanation**: Figure 4 reports that on the NIAH benchmark, QUOKA with B_SA=2048 achieves higher accuracy than the Full (dense) attention baseline under the same chunked prefill setup. Since full attention should be the mathematical upper bound, this is surprising. While sparsity can theoretically act as a denoising mechanism in NIAH (a known phenomenon in the literature), the paper presents the figure without any discussion of why this occurs. This is not a fatal error—it does not invalidate the method—but the omission undermines confidence in the evaluation chain and should be addressed.

### Minor

- **Theorem 1 is poorly stated and its connection to the algorithm is unclear**: The theorem uses an undefined variable `q*` (appears to be a typo for `q_0`), and the inequality (Eq. 5) does not straightforwardly connect to the selection criterion `S_q = -CosSim(M_Q, q*)`. The proof is deferred to an appendix that is not visible in the extracted text. The empirical evidence in Figure 2 is already a sufficient motivation; the theorem in its current form adds confusion rather than rigor. The authors should either correct it into a clean, verifiable statement with a clear link to the algorithm, or remove it.

- **The core geometric motivation (Figure 2) is shown for only one layer/head of one model**: The central claim—that queries with low cosine similarity to the mean query attend to more keys—is demonstrated on Llama 3.2-3B layer 0 head 11. The paper would benefit from showing this pattern generalizes across layers and heads of multiple models, even if only as supplementary material.

- **No confidence intervals or variance estimates for accuracy results**: Several results (e.g., Math500 where QUOKA "in some cases even surpasses the accuracy of dense attention"; LongBench where SmollM3 scores 1.03 normalized accuracy) would benefit from confidence intervals to distinguish signal from noise.

- **No random KV selection baseline**: The paper compares against learned/structured sparse attention methods but does not include a random selection baseline at the same budget B_SA. Without it, it is harder to attribute the accuracy preservation to the specific selection strategy versus the fact that B_SA=1024 is large enough to contain relevant information by chance.

### Trivial

- The notation `q*` in Theorem 1 is undefined (appears to be a typo for `q_0` or some other query variable). This should be corrected.

## Nice-to-Haves

- A breakdown of the time spent in the selection mechanism versus the attention computation itself would help practitioners understand the tradeoffs.
- A discussion of why QUOKA occasionally exceeds dense accuracy on Math500 and LongBench (e.g., sparsity as a regularizer in generation) would strengthen the paper.

## Removed Points

- **Criticism about Loki/SparQ being designed for generation (unfair comparison)**: Removed. The paper's thesis is precisely that existing methods fail under chunked prefill; demonstrating this is valid. The paper mentions this asymmetry (Section 2.4).
- **Criticism about limited task variety (lack of summarization, code completion)**: Removed. The paper already evaluates on NIAH, RULER (6 tasks), LongBench (multi-task), and Math500, which is extensive.
- **Claims about missing code, missing appendix content, reproducibility concerns about undisclosed hyperparameters**: Removed per hard rules (parser strips appendices; hyperparameters are documented).
- **Criticism that the Full baseline in Figure 4 is subject to B_SA=2048**: Removed. The caption states experimental conditions; Full attention uses all KVs without budget constraint. The real issue (unexplained Full < QUOKA) is retained above.
- **Strength Finder claims about novelty of query subselection being "novel"**: Weakened. The approach is well-motivated but incremental over existing observations about query/key geometry.

## Novel Insights

None beyond the paper's own contributions. The core observation about query geometry (low cosine similarity to mean query → broad key attention) and the GQA pre-aggregation trick are the paper's genuine contributions; no additional insight emerged from the reviews.

## Suggestions

1. **Explain the NIAH Figure 4 discrepancy**: Add a brief discussion (1–2 sentences) in Section 4.1 acknowledging that Full attention sometimes underperforms QUOKA on NIAH, with a plausible explanation (e.g., sparsity as a denoising mechanism for retrieval, or position bias in the dense baseline).

2. **Fix or remove Theorem 1**: Either correct the undefined `q*`, provide a clean proof sketch connecting the inequality to the selection criterion, and state the theorem's actual implication; or remove it entirely—the empirical evidence is sufficient.

3. **Add a random-selection baseline**: Include a simple baseline that selects B_SA random KVs per chunk for at least one model/benchmark to isolate the effect of the QUOKA selection strategy.

4. **Show the geometric pattern across more layers/heads**: Provide a small table or additional PCA plots for other layers (e.g., early, middle, late) of Llama 3.2-3B and one other model (e.g., Qwen3-4B) to demonstrate that the core observation generalizes.

## Score and Decision

**Calibration Anchors (all rounds):**
| Path | Score | Round | Comparison to QUOKA |
|------|-------|-------|---------------------|
| 4QWPCTLq20 (IntelLLM) | 3.00 | R1 weak | Weaker: less comprehensive eval, Rejected |
| 2DD4AXOAZ8 (MixAttention) | 2.00 | R1 weak | Weaker: limited scope, Rejected |
| vw0NurJ7UX (PrefixQuant) | 3.00 | R1 weak | Different topic (quantization), lower score |
| uHkfU4TaPh (DynamicKV) | 4.40 | R1 mid | Weaker: one model, one benchmark, Rejected |
| pG820nmDvy (Running Huge Context) | 4.67 | R1 mid | Weaker: less convincing latency analysis, Rejected |
| TrKRpaOk8y (A Little Goes a Long Way) | 6.40 | R1 mid | Comparable: QUOKA is training-free vs. this paper's training requirement, similar evaluation breadth |
| dSneEp59yX (Cascading KV Cache) | 6.00 | R2 mid | Weaker approach overall; QUOKA more comprehensive |
| ulaUJFd96G (Hierarchical Context Merging) | 6.25 | R2 mid | Similar tier: training-free context extension |
| gkUyYcY1W9 (SharedContextBench) | 6.50 | R2 mid | Different focus (benchmark paper), but similar quality level |
| ZTpWOwMrzQ (Radar) | 6.60 | R2 narrow | Similar tier: training-free sparse attention. QUOKA has stronger empirical breadth (more models, hardware). Radar has better theoretical grounding. Roughly comparable. |
| j9VVzueEbG (ZETA) | 7.00 | R2 narrow | Stronger theory but only 125M models. QUOKA has more practical validation. |
| Tb5PY5vwp6 (HShare) | 6.80 | R2 narrow | Similar KV-sharing approach but different focus |
| HE6pJoNnFp (Sparse RAG) | 6.60 | R2 narrow | Different application (RAG), similar contribution level |
| OfjIlbelrT (FlexPrefill) | 8.00 | R1 strong | Stronger: more adaptive, dynamically adjusts sparse patterns. QUOKA is simpler and more portable but less adaptive. |

**Round 1 bracket:** 5.5–7.5. **Round 2 narrowing** placed QUOKA between Radar (6.60) and ZETA (7.00), most comparable to A Little Goes a Long Way (6.40) and Radar (6.60). QUOKA has stronger empirical breadth than both but lacks the theoretical rigor of Radar and the novelty of ZETA. The minor-but-numerous weaknesses (unexplained NIAH figure, unclear Theorem 1, missing analyses) prevent it from reaching the 7+ tier.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>