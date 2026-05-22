## Summary

This paper proposes QubitCache, a KV-cache compression method for LLMs that combines classical token retention (15% of tokens) with quantum-inspired amplitude encoding to preserve attention distributions for the remaining 85% of tokens. The core idea is to encode the attention distribution over non-critical tokens into a 9-qubit quantum state, replacing binary eviction decisions with soft, probability-weighted attention at generation time. The method achieves 7× compression with 92-97% of uncompressed performance across several models and benchmarks.

## Strengths

- **Genuinely novel paradigm.** QubitCache reframes KV-cache compression as *attention distribution preservation* rather than token selection. This is a conceptually different approach from H2O, ScissorHand, and quantization methods like GEAR, and the ablation study (Table 4) convincingly shows that attention-selected tokens matter far more than position-based or random retention (20.4% drop when critical tokens are removed vs. 0.6% for anchors/recent tokens).

- **Strong empirical breadth.** Evaluated across five models (4B-70B) and seven benchmarks, including long-context, multi-hop reasoning, and code tasks. The scaling results on Llama-70B and Qwen-30B (Table 2) demonstrate viability at production scale — QubitCache retains 96.9% of uncompressed F1 on Llama-70B, outperforming all compression baselines.

- **Measured 7× compression (0.55 GB vs. 3.91 GB for full KV).** The memory consumption numbers in Table 3 are specific and reproducible, showing QubitCache uses less memory than GEAR (0.59 GB) while achieving competitive or better performance.

- **Ablation study validates the design.** The 3.9% gain from the quantum encoding component (Full QubitCache 0.491 vs. No Quantum 0.472) confirms that preserving attention distributions provides a measurable, non-trivial benefit beyond the token retention policy itself.

## Weaknesses

### Major

- **Overclaimed quantum advantage.** The paper claims "logarithmic compression beyond classical information-theoretic limits" (abstract) and lists memory complexity as `O(L × H × 0.15S × D + log N)` in Table 3. On classical hardware (where the evaluation is conducted), simulating a 9-qubit state requires storing 2⁹ = 512 complex amplitudes — that is O(N), not O(log N). The paper acknowledges classical simulation in Section 3.2.2 but continues to present the logarithmic claim as a realized compression benefit in the abstract, introduction, and Table 3. The primary compression comes from retaining only 15% of tokens classically, not from the quantum encoding.

- **Baseline comparisons at different compression ratios are uninformative for the key claimed advantage.** QubitCache operates at 7× compression (15% retention). The token-selection baselines (H2O, ScissorHand, StreamingLLM) are evaluated at 2× (50% retention). The paper's headline claim of "15-25% higher F1 scores on multi-hop reasoning" compares against methods using 3.3× *more* memory. GEAR at 6.7× is the only method at a comparable compression ratio, and on that comparison QubitCache's advantages are modest (e.g., Mistral-7B on HotpotQA: 0.459 vs. 0.434). The paper should either push baselines to matched compression ratios or evaluate QubitCache at 2× for a fair head-to-head.

- **No statistical significance or variance reported.** All results (Tables 1, 2) are single numbers with no error bars, confidence intervals, or multiple-run statistics. Autoregressive decoding has non-trivial variance; differences of 0.01-0.03 F1 (many of the claims of superiority over GEAR) could plausibly lie within noise. This undermines confidence in all comparisons.

- **Missing promised results (LAMBADA).** LAMBADA is listed as a benchmark in Section 4.1.2 but does not appear anywhere in Table 1 or elsewhere in the results. The abstract says "five models and six benchmarks" while the experiments section lists "five benchmark datasets" but Table 1 uses seven columns — these inconsistencies suggest incomplete or sloppy reporting.

- **Ablation table lacks task/model context.** Table 4 reports raw F1 scores with no indication of which model, task, or compression ratio was used. The "No Quantum" variant's memory consumption is not reported, making it impossible to assess whether the comparison is at equal memory budget. Without this context the ablation's quantitative claims are unverifiable.

### Minor

- **Attention averaging across layers and heads (Eq. 3–5) destroys head-specific information.** It is well established that different attention heads serve different linguistic functions (Clark et al., 2019). Averaging all heads/layers into a single importance score per token may lose information that is critical for certain tasks. This design choice is not motivated or ablated.

- **The quantum encoding's marginal benefit is modest relative to the complexity it introduces.** The ablation shows a 3.9% gain from the quantum component (0.491 vs. 0.472). Given the significant increase in conceptual and implementation complexity — including the need to simulate quantum circuits on classical hardware — the practical cost-benefit trade-off is questionable. The paper should discuss whether a simpler interpolation scheme (e.g., distance-weighted averaging without the quantum formalism) could match this gain.

- **Computational overhead is not quantified.** The paper mentions hierarchical amplitude encoding and claims O(log n) per-token update cost, but provides no wall-clock time measurements, circuit execution counts, or end-to-end latency comparisons. Without this data, it is impossible to assess practical deployment feasibility.

### Trivial

- The abstract says "six benchmarks" while Section 4.1.2 lists five benchmark datasets, and Table 1 shows seven columns. This counting inconsistency is confusing.
- Figure 3a shows F1 vs. qubit count but does not show the full-model baseline, making it impossible to determine at what qubit count performance saturates relative to uncompressed.

## Nice-to-Haves

- Reporting results at matched compression ratios (e.g., all methods at 7× and at 2×) would make the comparisons directly interpretable.
- Error bars (mean ± std over 3+ runs) for the key comparisons, especially those where QubitCache's advantage over GEAR is small (≤0.03 F1).
- Wall-clock latency measurements showing the overhead of state preparation and measurement extraction during inference.
- An ablation where the quantum encoding is replaced by a simple classical storage of the attention distribution (same 512 floats) to isolate whether the quantum formalism provides any benefit over direct storage.
- Reporting which task/model the ablation in Table 4 was performed on.

## Removed Points

These points from the input reviews were removed during consolidation:

- **"The method does not preserve attention patterns — it replaces them with static importance weights"** — This claim is overstated. The method *does* preserve the attention distribution (computed from the initial forward pass) for the 85% of compressed tokens. The weights are static, but they are still attention-derived probability distributions, not arbitrary importance scores. For the 15% preserved tokens, dynamic attention is used. This is a necessary trade-off in any compression scheme that does not store keys — one cannot compute query-key dot products for keys that are not stored. The paper is transparent about how the weights are obtained, and calling this a "structural flaw" that "requires a fundamental reconceptualization" is excessive.

- **"Baselines may not have been configured optimally"** — The reviewer speculates about H2O and ScissorHand settings without evidence. The paper states "consistent protocols" were used. Without specific knowledge of misconfiguration, this is speculative.

- **"Missing related works"** — Removed per instructions; I cannot verify whether missing works exist.

- **"Quantum circuit depth circuit count not provided"** — The paper provides Figure 3b with F1 vs. circuit depth and states that depth-15 is optimal within NISQ constraints. While wall-clock time is missing (noted as a Minor weakness above), the circuit depth analysis itself is provided.

- **"The λ hyperparameter is not ablated"** — This is a valid point but belongs in Nice-to-Haves rather than as a real weakness; no method ablates every hyperparameter.

- **"The interpolation assumes locality of value vectors"** — This is standard practice in distance-based interpolation and is motivated by known attention locality; it is not a weakness unique to this method.

## Novel Insights

The key insight that survives scrutiny is that *preserving the attention distribution over tokens* — even as a static, precomputed distribution — is far more effective at maintaining model performance than binary token selection at the same retention rate. The ablation study (Table 4) cleanly demonstrates this: attention-selected tokens at 15% retention dramatically outperform random selection at ~50% retention. This suggests that the field's focus on "which tokens to keep" may be partially misplaced — the more important question may be "how much of the attention distribution to preserve." The quantum encoding provides a concrete mechanism for this, but the core insight (distribution preservation > token selection) is independent of the quantum formalism and stands as the paper's most durable contribution.

## Suggestions

1. **Reframe the paper honestly.** Strip the "beyond classical information-theoretic limits" language and present QubitCache as an attention-distribution-preserving compression method, not a quantum breakthrough. The quantum encoding is a principled way to store and reconstruct a probability distribution — this is interesting enough without overclaiming.
2. **Report results at matched compression ratios.** Either push baselines to 7× or evaluate QubitCache at 2×, so readers can make direct comparisons.
3. **Add error bars** for at least the key comparisons (Tables 1-2) using 3 runs.
4. **Report context for the ablation** (which model, task, and memory budget) and add memory consumption for the ablation variants.
5. **Add wall-clock latency** for the quantum encoding/decoding steps to enable practical deployment assessment.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Initial bracket of (4, 6) based on comparison with three search bands:
- Low band (<3.5): IntelLLM (3.0, reject), PrefixQuant (3.0, reject) — QubitCache is clearly stronger (more novel idea, broader evaluation).
- Middle band (3.5–7.5): KVTQ (4.40, reject), KV-Distill (4.00, reject), KV-Dict (5.25, reject), MiKV (5.00, reject) — QubitCache is comparable to these in scope and novelty.
- High band (>7.5): QTDA (8.0, accept), CBQ (7.60, accept) — QubitCache is not in this league (missing rigor, overclaiming).

**Round 2 (Narrowing):** Read 6 anchors in full from the (4.5, 6.5) band:
- **ChunkKV (5.25, reject)** — Similar scope, comparable novelty. QubitCache has a more novel paradigm but worse comparison fairness.
- **KV-Dict (5.25, reject)** — Novel dictionary approach, decent experiments. QubitCache is comparable in novelty but has more overclaiming issues.
- **MiKV (5.00, reject)** — Mixed-precision approach, straightforward. QubitCache is more novel but less rigorous.
- **Identify Critical KV (5.75, reject)** — Stronger theoretical foundation than QubitCache, but also rejected.
- **SqueezeAttention (5.50, accept)** — Layer-wise allocation, well-executed but modest novelty. The only accepted paper in this band; QubitCache has more novelty but more significant issues (overclaiming, no error bars, unfair comparisons).
- **KV-Distill (4.00, reject)** — Weaker than QubitCache in both execution and novelty.

**Final placement:** QubitCache sits near the lower end of this band. Its core idea is genuinely novel and the experimental breadth is decent, but the quantum overclaiming, unfair baseline comparisons, missing error bars, and incomplete reporting (missing LAMBADA, context-free ablation) are significant issues that the accepted paper in this range (SqueezeAttention at 5.50) does not have. Score: **5.0** — a paper with a novel paradigm that requires substantial honesty and rigor improvements before it can be competitive.

**Anchor papers used (all rounds):**
| Anchor ID | Score | Round | Comparison |
|-----------|-------|-------|------------|
| 4QWPCTLq20 | 3.00 | R1 | Weaker — less novel, smaller scope |
| vw0NurJ7UX | 3.00 | R1 | Weaker — different subproblem |
| 0T8vCKa7yu | 3.00 | R1 | Weaker — different domain (weight quantization) |
| 2DD4AXOAZ8 | 2.00 | R1 | Weaker — architecture modification, not compression |
| eZAlb8fX5y | 4.40 | R1/R2 | Comparable but cleaner execution |
| p7vJ3wsm34 | 4.00 | R1/R2 | Slightly weaker — less clear motivation |
| FkXYvV7nEB | 5.25 | R1/R2 | Comparable in novelty, cleaner presentation |
| CRQ8JuQDEd | 5.00 | R1/R2 | Comparable — similar issues with limited novelty |
| dLrhRIMVmB | 8.00 | R1 | Much stronger — different tier |
| vrBVFXwAmi | 8.00 | R1 | Much stronger — different tier |
| CxXGvKRDnL | 8.00 | R1 | Much stronger — different tier |
| eW4yh6HKz4 | 7.60 | R1 | Much stronger — better execution |
| 8sglLco8Ti | 5.25 | R2 | Comparable in scope, similar weaknesses |
| jZVNmDiU86 | 5.60 | R2 | Slightly stronger — better motivated |
| lRTDMGYCpy | 5.75 | R2 | Stronger in theory, weaker in breadth |
| 9HK2rHNAhd | 5.50 | R2 | Stronger — accepted with cleaner claims |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>