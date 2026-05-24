Now I have all the evidence I need. Let me write the consolidated review.

---

## Summary

QUOKA proposes a training-free, hardware-agnostic sparse attention method for chunked LLM prefill. The key insight is that queries with low cosine similarity to the mean query interact with more keys and dominate attention; QUOKA first subselects these representative queries, then uses cosine similarity between the reduced query set and all keys to pick the most relevant KV pairs. The method delivers strong results: near-baseline accuracy on LongBench (0.94–1.0 relative accuracy at B_SA=512 across models), 10–20% gains over competing sparse methods on RULER, up to 5× attention speedup on A100 GPUs and 7× on CPUs, and generalization across RoPE, NoPE, and MoE model families.

## Strengths

1. **Novel geometric observation with empirical backing.** The paper identifies and visualizes (Figure 2) that queries with low cosine similarity to the mean query attend more broadly across keys, with a measured correlation of 0.737 between S_q and max attention weight. This is a non-trivial insight into LLM attention geometry that is not leveraged in prior query-dependent sparse attention work.

2. **Consistent and large-margin empirical superiority.** On RULER (Table 1, B_SA=1024), QUOKA scores 86.71 vs. the best baseline (SparQ) at 79.36 on Llama3.2-3B at 4k, and the gap widens to 57.01 vs. 31.14 at 32k — a 10–25% advantage that holds across all five model families. On LongBench (Table 3), QUOKA at B_SA=512 achieves 0.945 relative accuracy on Llama3.2-3B where SampleAttention (uniform query sampling) drops to 0.738, a 28% relative gap. These margins are large enough that baseline tuning asymmetries are unlikely to be the sole explanation.

3. **Broad and rigorous evaluation scope.** The paper evaluates across 6 model families (Llama3, Qwen2.5, Qwen3, SmollM3/NoPE, Qwen3-30B-A3B/MoE, GPT-OSS-20B), 4 benchmarks (NIAH, RULER, LongBench, Math500), and 3 hardware platforms (A100 GPU, RTX 2080 GPU, Intel Xeon CPU). This breadth convincingly demonstrates generality and hardware portability — properties rare in kernel-dependent sparse attention methods.

4. **Training-free and hardware-portable design.** QUOKA uses only standard linear algebra operations (cosine similarity, top-k, gather), requiring no custom CUDA kernels. This is a practical strength: it can be dropped into any framework supporting chunked prefill, and the measured speedups (5× on A100, 5–6× on RTX 2080, 7× on CPU) validate that the approach works across very different hardware profiles.

## Weaknesses

### Major

1. **The query subselection criterion is not directly validated against alternatives.** The paper's central claim is that low-cosine-similarity queries are the most informative. However, the only comparison that isolates query selection is against SampleAttention (which uniformly samples queries). This shows QUOKA outperforms uniform sampling, but it does not test the *direction* of the heuristic — e.g., selecting the *most* similar queries to the mean (the opposite criterion), or selecting queries by random subselection within the same overall framework (same cosine scoring + max aggregation, differing only in which queries are kept). The ablations on N_Q (Tables 11, 12) show that fewer queries hurt performance, but they do not test *which* queries matter. The paper's motivating claim rests on a plausible but unverified hypothesis: that the specific geometric ranking (low similarity → high informativeness) is what drives the gains. This is the paper's primary evidentiary gap.

2. **Theorem 1 is unclear and appears garbled.** The theorem statement (page 4) reads: "Consider tokens a fixed query q_0 and key k... Then CosSim(M_Q, q^*) ≤ 1 + α_q β_q - 0.5α_q^2 - 0.5β_q^2." The variable q^* appears without definition. The quantities α_q and β_q are defined for q_0 and k, but the inequality's left side involves a different variable q^*. The connection to the selection score S_q = -CosSim(M_Q, q) is not made explicit, and the proof is in the stripped appendix. As presented, this theorem does not provide a convincing theoretical foundation — it reads as incomplete or mis-specified. Given the issue, the paper would be better served by removing the theorem or clearly rewriting it.

3. **Anomalous >1.0 normalized accuracy results are not explained.** In Table 3 (LongBench), SmollM3 at B_SA=1024 and 2048 achieves normalized accuracy of 1.03 and 1.028 — meaning QUOKA *beats* the dense-attention baseline on the normalized metric. The paper also reports surpassing dense attention on Math500 (Section 4.4). Since the dense baseline uses the same chunked prefill (B_CP=128), the most plausible explanation is that chunking itself degrades dense attention (due to the hard causal boundary across chunks), and QUOKA's sparsification inadvertently mitigates this. This is not discussed. Without a non-chunked full-attention baseline clarifying whether the >1.0 result is a "regularization" artifact or a genuine advance, the reader cannot interpret these numbers correctly. The paper should either report a non-chunked full-attention baseline or explain why this is not a concern.

### Minor

4. **Baselines designed for generation may be at a disadvantage in the prefill setting.** The paper acknowledges (Section 4) that LessIsMore, SparQ, and Loki were designed for generation, and their parameter settings (e.g., down-projecting to 64 dimensions) may not be optimal for prefill. QUOKA consistently beats them by 10–20%, and the gap on LongBench (e.g., 0.945 vs. 0.738 vs. SampleAttention) is large enough that some tuning asymmetry is unlikely to flip the ranking. Nevertheless, the paper would be stronger with a sensitivity analysis showing whether baseline performance changes meaningfully under alternative hyperparameter choices for the prefill setting.

5. **The 88% reduction number is stated without derivation.** The abstract claims "88% fewer key-value pairs," but with B_SA=1024 and a 30k-token cache the reduction is 96.6%. The 88% figure likely averages across sequence lengths, but the text does not explain how it is computed. This is a small clarity issue.

### Trivial

6. **Theorem 1's prose uses "subsection selection" where "subselection" is intended.** Minor typo that should be fixed.

## Nice-to-Haves

- Running a non-chunked full-attention baseline on LongBench and Math500 to clarify whether the >1.0 results are an artifact of chunking or a genuine improvement.
- An ablation that replaces QUOKA's cosine-dissimilarity query ranking with (a) random selection and (b) selection of the most similar queries, holding all other components fixed, to directly validate the geometric hypothesis.
- A brief intuitive explanation of how the compression ratio varies with context length, to clarify where the 88% figure comes from.

## Removed Points

These points were raised by reviewers but are removed as invalid or unverifiable:

- **"Ablation tables 5, 6, 11, 12 are in the appendix"** — The appendix is stripped by the PDF parser; the original submission contained these tables. This is a format artifact, not a content gap.
- **"The paper may not release code"** — The paper cites models, benchmarks, and methods that are publicly available. Reproducibility statements and code release are separate from the paper's scientific validity.
- **"The 88% number is not recalculated"** — The number is stated as an aggregate average, which is standard practice. Recalculating it per configuration is a formatting preference, not a substantive error.
- **"Cosine similarity only shows 10% improvement over dot product"** — 10% on RULER is a substantial improvement, and the reviewer's framing ("only") is misleading.
- **"The paper never considers combining QUOKA with eviction"** — The paper explicitly states this is future work (Section 5: "Eviction is complementary to our approach and could be integrated with QUOKA in chunked prefill; we leave this to future work"). This is not a weakness.
- **Strength claimed about Theorem 1 being a strength** — Since Theorem 1 is garbled/incomplete as presented, it does not constitute a valid strength. The empirical evidence (Figure 2) is the actual support for the geometric insight.
- **Strength about "gradual degradation"** — This claim is supported by the paper's text in Section 4.5 referencing ablation tables that are not visible due to appendix stripping, but the claim itself ("less than a 3% drop...") is stated clearly.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix Theorem 1.** Either rewrite it so that all variables are defined and the connection to S_q is clear, or remove it entirely and rely on the strong empirical evidence (Figure 2 correlation, ablations).
2. **Add a direct ablation of the query ranking criterion.** Compare: (a) QUOKA's cosine-dissimilarity ranking, (b) random query selection with the same N_Q, and (c) cosine-similarity ranking (selecting the most similar queries). If (a) outperforms (b) and (c) by a clear margin, the core claim is directly validated.
3. **Address the >1.0 results.** Run a non-chunked full-attention baseline on LongBench (at least for SmollM3) and Math500 to establish whether QUOKA is genuinely surpassing the ideal or whether the effect is an artifact of chunked prefill degradation.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
| anchor_id | avg_score | round | comparison |
|---|---|---|---|
| Y5kgP4x20k (SparseSkeleton) | 2.67 | R1 | Much weaker — method not validated, poor accuracy. |
| GiI6tPrPAG (ILRe) | 2.00 | R1 | Much weaker — limited evaluation scope. |
| kMLfUshPwo (TAKE) | 4.00 | R1 | Weaker — narrower evaluation, no RULER results, lower accuracy retention. |
| yTeDQeuKKz (SALE) | 4.00 | R1 | Weaker — comparable approach but marginal accuracy gains over baselines. |
| CEpNboUJyw (CSAttention) | 4.00 | R1 | Weaker — high prefill overhead, unfixed-size index undermines claims. |
| iHqdSQk6qc (Hierarchical Sparse Attn) | 5.50 | R1 | Different contribution (architecture training, not training-free KV selection). |

Initial bracket: [5.0, 7.0]

**Round 2 (Narrowing):**
| anchor_id | avg_score | round | comparison |
|---|---|---|---|
| RVLMGPXt2i (LookaheadKV) | 5.00 | R2 | Weaker — KV eviction, not sparse attention for prefill. |
| qCaq3jGb0S (TRIM-KV) | 5.50 | R2 | Slightly weaker — training-based method vs. QUOKA's training-free. |
| FnSgecCEwg (FASA) | 6.00 | R2 | Comparable — similar accuracy retention, but FASA is RoPE-dependent while QUOKA generalizes to NoPE/MoE. |
| m3HXHQYmZu (ProxyAttn) | 6.50 | R2 | Comparable — higher speedups (10.3×) but evaluated on fewer model families. |
| PsB6Lynznk (ASEntmax) | 6.50 | R2 | Different contribution (attention activation function, not KV selection). |

### Final Assessment

QUOKA's main contributions — the geometric query-subselection insight, the combination of query and key selection for prefill, and the broad empirical validation — are real and practically valuable. The paper is stronger than the ~4.0 cluster of sparse attention papers (TAKE, CSAttention, SALE) and sits in the same band as FASA (6.0) and ProxyAttn (6.5). However, it falls short of those peers in one respect: the central claim about the query selection criterion is not as rigorously validated as FASA's frequency-chunk analysis or ProxyAttn's head-similarity study. Theorem 1, intended as theoretical support, is garbled and does not help. The >1.0 anomaly also raises an unanswered question about the fairness of the dense baseline.

A score of 6.0 reflects a solid paper with a real contribution and strong evidence, held back from a higher score by the unvalidated query-selection mechanism and the garbled theorem — both fixable in revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>