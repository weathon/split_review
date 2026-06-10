Here is my final consolidated review:

---

## Summary
QUOKA is a training-free, hardware-agnostic sparse attention algorithm for accelerating chunked prefill in LLM inference. It identifies the most geometrically distant queries from the mean query via cosine dissimilarity, scores keys against those queries using cosine similarity, and aggregates scores (max over queries, mean over GQA heads) to select a reduced KV set. Evaluated across 6 model families, 4 benchmarks, and 3 hardware platforms, QUOKA consistently outperforms baselines by 10–20% on RULER and achieves near-dense accuracy on LongBench, with 5× attention speedup and 3× TTFT reduction on A100.

## Strengths
- **Clean, well-motivated empirical observation about query geometry:** The core insight—that queries with low cosine similarity to the mean query interact more strongly with keys—is supported by a PCA visualization (Figure 2b), a correlation of 0.737 between S_q and max_k(A) (Figure 2c), and a heavy-tailed distribution of query-level deviations (Figure 3). This multi-pronged validation makes the design choice principled rather than ad hoc.
- **Consistently strong accuracy across benchmarks, models, and sparsity levels:** On RULER with B_SA=1024 (Table 1), QUOKA outperforms all baselines by 10–20% absolute across all five models and all sequence lengths. On LongBench (Table 3), QUOKA achieves 0.945 normalized accuracy at B_SA=512 for Llama3.2-3B-Instruct versus 0.738 for the best baseline (SampleAttn). Table 2 shows at 25% compression, accuracy loss remains ~1–3 points even at 32k tokens across six models.
- **Demonstrated hardware portability with substantial latency gains:** QUOKA achieves 5× attention speedup and 3× TTFT reduction on NVIDIA A100 (Figures 5a, 5b), ~5–6× on Intel Xeon CPU (Figure 5c), and ~5–6× on NVIDIA RTX 2080 (Figure 5d). Unlike kernel-level sparse attention methods requiring custom CUDA, QUOKA is built on standard linear algebra operations, and the portability claim is substantiated by multi-hardware measurements.
- **Addresses multi-query prefill where prior methods fail:** Table 3 demonstrates that generation-oriented sparse attention methods degrade severely under multi-query prefill—LessIsMore drops to 0.461 and Loki to 0.589 on Qwen2.5-3B at B_SA=512, while QUOKA achieves 0.869. The query-subselection step (Algorithm 1, lines 1–5) is the key differentiator.
- **Broad cross-architecture validation on 6 decoder-only LLM families** spanning standard dense attention (Llama3.2-3B, Qwen2.5-3B), MoE-based (Qwen3-30B-A3B), NoPE variants (SmolLM3), and a larger model (GPT-OSS-20B).

## Weaknesses

### Fatal
None

### Major
None

### Minor
1. **Misleading sub-quadratic complexity claim (Section 3.4, line 131):** The paper states "QUOKA reduces prefill cost from O(T²) to a sub-quadratic complexity." Per chunk i, the scoring step computes S = Q̄K^T where Q̄ has N_Q rows and K has up to (i+1)·B_CP rows, costing O(N_Q · (i+1)·B_CP · d). Over N_B = T/B_CP chunks, the total scoring cost is O(N_Q · T² · d / B_CP)—still quadratic in T. The attention computation per chunk drops to O(N_Q · B_SA · d), yielding O(N_Q · B_SA · T / B_CP) total—linear in T at fixed B_SA—but the scoring dominates asymptotically. The claim should be qualified: the attention computation is reduced to linear in T, but the scoring step remains quadratic with a reduced constant factor (N_Q/B_CP ≈ 1/8). This matters because "sub-quadratic" is a prominent theoretical claim used in the abstract and introduction.

2. **Theorem 1 has an undefined variable q* and a loose bound (Section 3.1, lines 143–149):** The theorem introduces q_0 as "a fixed query" but then uses q* in the bound (Equation 5) and in the score S_q = -CosSim(M_Q, q*) without defining q*. From context it appears q* = q_0, but this must be stated explicitly. More substantively, the bound CosSim(M_Q, q*) ≤ 1 - 0.5(α_q - β_q)² shows the cosine similarity is at most some value less than 1, but does not establish that it is *negative*, which is what the subselection procedure (selecting queries with most negative CosSim to M_Q) requires. An upper bound that is positive does not guarantee the query would be selected. The proof in Appendix D may address this, but the stated theorem in the main text has this gap.

3. **Missing Table 1 entry for GPT-OSS-20B at 32K with QUOKA (line 213):** The last cell in the QUOKA row for GPT-OSS-20B at 32k context length is empty. This should be filled in.

### Trivial
1. No confidence intervals or variance reported for latency measurements (Section 4.6), despite averaging over 100 trials per data point.

## Nice-to-Haves
- The >1.0 normalized LongBench scores for SmolM3 (1.03 at B_SA=1024, 1.028 at B_SA=2048 in Table 3) indicate sparse attention can sometimes *outperform* dense attention. This is noteworthy and worth discussing—even a brief hypothesis about attention sink effects or regularization would be valuable.
- Math500 results are described only by reference to Table 8 in the appendix (Section 4.4). Since Math500 is listed as a main contribution, a brief summary or representative result in the main text would improve self-containment.

## Removed Points
These points are flagged to be removed, treat them with caution.
- Coverage unevenness (GPT-OSS not in LongBench/Math500): This is an experimental design choice given different models suit different benchmarks, not a flaw.
- "88% fewer KV pairs" not tied to specific configuration: The abstract presents a headline number which is standard for a summary claim.
- Full baseline discussion in NIAH: Figure 4 already shows Full with chunked prefill, providing this reference implicitly.
- "Near-mean queries concentrate on a small shared group of keys" not directly demonstrated: Figure 2a visually supports this claim.

## Novel Insights
The paper's core geometric observation—that queries with low cosine similarity to the mean query attend most broadly to keys—provides a principled, lightweight proxy for query importance that is both theoretically motivated and empirically validated with correlation of 0.737. The key insight from analyzing the complexity is that at fixed selective budget B_SA, the actual attention computation becomes linear in T while the scoring step remains quadratic with a small constant factor—making the constant-factor reduction (N_Q/B_CP) the driver of practical speedups rather than asymptotic improvement.

## Suggestions
- Qualify the complexity claim: state that attention cost per chunk drops from O(B_CP · T) to O(N_Q · B_SA), making total attention cost linear in T at fixed B_SA, while scoring remains quadratic with reduced constant N_Q/B_CP.
- Define q* explicitly as q_0 in Theorem 1, and either tighten the bound to establish negativity or reframe the theorem as providing a necessary condition for high-scoring queries.
- Fill in the missing GPT-OSS-20B 32K QUOKA entry in Table 1.
- Discuss the >1.0 LongBench scores for SmolM3 briefly—this finding about potential beneficial regularization effects is worth highlighting.

## Scoring Report

**Round 1 bracket:** 6.5–8.0. QUOKA is clearly above the 5.5–6.8 range of comparable accepted papers (Cascading KV Cache at 6.00, HeadKV at 6.50, Radar at 6.60, Selective Attention at 6.75, HShare at 6.80) and comparable to FlexPrefill (8.00).

**Round 2 narrowing:** QUOKA demonstrates stronger evaluation breadth (6 models, 4 benchmarks, 3 hardware platforms) than all papers in the 6.5–6.8 range, with cleaner methodological framing and stronger accuracy margins. Compared to FlexPrefill (8.00), QUOKA has comparable experimental rigor and better multi-hardware validation, with minor theoretical framing weaknesses (complexity claim, Theorem 1) that FlexPrefill doesn't have in the same form. The paper lands at 7.5—clearly above the 6.5–6.8 anchors and near FlexPrefill's 8.0, with a small gap due to the theoretical framing issues.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>