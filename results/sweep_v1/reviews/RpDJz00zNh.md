## Summary

This paper proposes ConciseHint, a framework that continuously injects concise hints (either manually designed text like "make answer concise!" or learned continuous embeddings) *during* the token-generation process of large reasoning models (LRMs). Unlike prior methods that operate before reasoning (prompting, SFT, RL), ConciseHint guides the model toward shorter outputs while it is actively generating. It features a complexity-adaptive injection interval (longer intervals for harder queries), a dynamic injection position that moves from head toward tail to balance accuracy and prefilling cost, and a learnable hint variant (ConciseHint-T) trained via prompt-tuning on concise data. Experiments across GSM8K, AIME24, and GPQA-Diamond with Qwen3-4B/8B and DeepSeek-R1-14B show consistent token reductions of 10–65% while maintaining accuracy, and the method integrates as a plugin on top of existing baselines (BeConcise, Prompt, Deer, NoWait).

## Strengths

- **Genuinely novel paradigm of in-reasoning hint injection.** The paper introduces a fundamentally different approach from the dominant before-reasoning paradigms (prompting, SFT, RL). While early-exit (Deer) and token-filtering (NoWait) methods operate during generation, ConciseHint's mechanism of *injecting hints that actively influence subsequent generation* is clearly distinct and novel. This is evidenced by Figure 1 and the contrast drawn in Sections 1 and 2.2.

- **Well-designed adaptive injection mechanism (Eq. 1) with strong empirical backing.** The adaptive interval $\tau_k = \alpha + \beta \cdot l_k$ automatically reduces hint intensity as reasoning lengthens, preventing over-hinting on complex queries. Table 3 provides concrete evidence: on AIME24 with Qwen3-4B, a fixed interval of 64 collapses accuracy from 67.00% to 45.33%, while the adaptive method maintains 67.00%. On GSM8K, the same fixed interval causes only minor loss, confirming that adaptation to query complexity is necessary.

- **Dynamic injection position (Eq. 3) convincingly demonstrated.** Table 4 shows that injecting at the tail drops accuracy from 55.56% to 42.93% (Qwen3-8B, GPQA-Diamond), while head-injection incurs 100% prefilling cost. The dynamic strategy achieves the best accuracy with a gradually increasing prefilling ratio, avoiding both failure modes.

- **Consistent plugin-style integration across diverse baselines.** Table 1 shows that ConciseHint reduces token usage when combined with each of four baselines (BeConcise, Prompt, Deer, NoWait) across three model families, with accuracy essentially preserved. For example, on GSM8K with Qwen3-4B, Ours(Prompt) uses 839 tokens vs. 1263 for Prompt alone (65% reduction), and Ours(NoWait) uses 857 vs. 1289 (33% reduction).

- **Controllability via interpolation (Eq. 4) is practically useful.** Figure 3 cleanly demonstrates that adjusting $\gamma$ provides a continuous accuracy-efficiency trade-off curve, which is valuable for deployment scenarios with varying computational budgets.

## Weaknesses

### Fatal
None.

### Major

- **Training-based variant (ConciseHint-T) evaluated only on the smallest model.** Table 2 tests ConciseHint-T exclusively on Qwen3-1.7B (the smallest model). Claims that "the learned embeddings generalize well to out-of-domain data" rely on this single small model. Results on AIME24 and GPQA-Diamond at $\gamma=0.7$ already show accuracy degradation (e.g., 42.67%→39.00% on AIME24), and further degradation at $\gamma=1.0$. Without experiments on Qwen3-4B/8B or DeepSeek-R1-14B, the effectiveness and generalization of the training component are unsubstantiated.

- **Efficiency evaluation is limited to token count without any wall-clock time or cost analysis.** The paper measures efficiency solely as average token usage. While token count is the standard metric in this literature and the primary driver of computation, Algorithm 1's loop structure (multiple `client.completions.create` calls per reasoning pass) could introduce additional overhead beyond what token count captures. The paper would be strengthened by reporting latency measurements or at minimum discussing this implementation choice. As written, readers cannot assess whether the token savings translate to actual wall-clock speedups under realistic deployment conditions.

### Minor

- **Framing of "in-reasoning intervention" as a fully blank space is slightly overbroad.** The paper claims prior work "mainly adheres to before-reasoning paradigms" and "does not dynamically intervene in the model during the token generation." Deer (early exit during generation) and NoWait (token suppression during generation) are acknowledged as baselines but their existence weakens the strong dichotomy. The *specific mechanism* of hint injection is novel, but the broader paradigm claim is overstated. This affects the abstract and introduction framing, not the technical contribution.

- **Statistical significance not reported.** Accuracy and token usage are averaged over 5–10 runs but no confidence intervals, standard deviations, or hypothesis tests are given. For AIME24 (30 problems) and GPQA-Diamond (198 problems), small differences of a few percentage points could reflect sampling noise. The paper would be stronger with error bars.

- **The constant 1024 in Eq. 3 (position selection) appears heuristic.** The position formula $p = \tau_k \cdot \min((\tau_k - \alpha)/1024, 0.8)$ uses 1024 without clear justification. While the appendix (removed by parser) may contain analysis, the main text would benefit from explaining why 1024 was chosen and how sensitive results are to this value.

- **Ablation of $\alpha$ and $\beta$ sensitivity is deferred to appendix.** The paper states these are "not sensitive" but only one configuration ($\alpha=128, \beta=0.2$) is tested in the main paper. Table 3 shows fixed intervals of 64 vs. 128 produce very different outcomes on AIME24 (45.33% vs. 63.33% for Qwen3-4B), suggesting the parameters may matter more than claimed.

### Trivial
None.

## Nice-to-Haves

- A wall-clock time comparison between ConciseHint and baselines on a representative subset of queries, to directly confirm that token reduction translates to latency reduction.
- A comparison of ConciseHint-T against direct SFT on the same concise dataset (not only hint tuning), to measure the benefit of the embedding-tuning approach over full model fine-tuning.
- Reporting standard deviations or confidence intervals for the main results.
- Analyzing the number of generation-loop iterations per query and their correlation with token savings.

## Removed Points

- **"Efficiency metric is incomplete (API call overhead) — Fatal" (from Harsh Critic):** Removed as a fatal claim. Token count is the standard efficiency metric in this literature. The loop structure in Algorithm 1 is a pseudocode abstraction; in practice, incremental generation can be implemented as a single streaming call. The reviewer's concern is speculative about implementation overhead and does not invalidate the core efficiency claim. Downgraded to a Major weakness above.
- **"Novelty is invalid because Deer and NoWait also intervene during generation — Structural" (from Harsh Critic):** Partially removed. Deer (early exit) and NoWait (token filtering) use fundamentally different mechanisms that do not actively inject guidance into generation. The paper's core technical novelty (hint injection during generation) stands. However, the framing overclaim is real and kept as a Minor weakness.
- **"The 1024 constant in Eq. 3 is unexplained" (from Harsh Critic):** The appendix (removed by parser) likely contains the explanation. Kept as a minor concern because the main text should still offer intuition for this design choice.
- **"ConciseHint-T training is standard prompt tuning — straightforward extension" (from Harsh Critic):** The training procedure is described as "like Prompt Tuning" and is a reasonable approach for learning hint embeddings. Being standard does not make it a weakness of the paper.

## Novel Insights

The harsh critic raises a legitimate concern about the overhead of looped generation calls, but this is an implementation detail that would affect all comparable methods (e.g., Deer also terminates generation at a non-deterministic point). The more interesting observation that emerges from cross-referencing the two reviews is that ConciseHint's *adaptive* components (interval and position) are what make it work — the ablation study (Table 3) reveals that a naive fixed-interval version actually *loses* accuracy substantially on hard problems (AIME24 accuracy falls from 67% to 45% with fixed interval 64). This suggests that the core challenge in in-reasoning intervention is not just *whether* to intervene, but *how much and where* — and the paper's specific engineering of these adaptivity rules is the genuine contribution, beyond the simple idea of injecting hints.

## Suggestions

1. **Add wall-clock latency measurements** for at least one model-benchmark pair to validate that token reduction translates to real speedup.
2. **Run ConciseHint-T on at least one additional model** (Qwen3-4B or DeepSeek-R1-14B) to substantiate the generalization claim of the learned embeddings.
3. **Add error bars or standard deviations** to the main results tables.
4. **Tone down the "blank space" framing** in the introduction to acknowledge that Deer and NoWait also operate during generation, while clarifying that hint injection is the specific novel mechanism.
5. **Provide intuition or an ablation for the 1024 constant** in Eq. 3 in the main text.

## Score and Decision

**Calibration anchors (all from the same review corpus):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| FlexPrefill (OfjIlbelrT) | 8.00 | Stronger — cleaner framing, more thorough efficiency evaluation including latency. |
| Inference Optimal VLMs (6VhDQP7WGX) | 5.80 | Weaker — methods section less novel, fewer ablations. ConciseHint has clearer technical contributions. |
| Rational Metareasoning (jRZ1ZeenZ6) | 5.00 | Comparable overall quality but ConciseHint has more clearly novel methodology. |
| FRAPPE (MjR5LcAGXJ) | 3.80 | Much weaker — heuristic pipeline with limited novelty. ConciseHint's technical contribution is more grounded. |
| Demonstration Distillation (Y8DClN5ODu) | 3.40 | Much weaker — lacks novelty, strong baseline issues. |
| IntelLLM (4QWPCTLq20) | 3.00 | Much weaker — insufficient baselines and unclear novelty over prior KV-cache methods. |

The paper presents a genuinely novel approach with thorough experiments and well-designed ablations. The core contribution (in-reasoning hint injection with adaptive control) is clearly demonstrated and practically useful. The main shortcomings are the limited evaluation of the training variant (ConciseHint-T) and the lack of latency measurements. These are addressable and do not undermine the paper's primary claims.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>