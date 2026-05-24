Now I have a thorough understanding of the paper and the calibration landscape. Let me produce the final review.

---

## Summary

TNT introduces a two-stage training framework for deep memory modules (RNNs with test-time memorization like Titans). Stage 1 employs a hierarchical memory architecture—a sequential global module with large chunks plus parallel local modules that periodically reset their states to a learned initial value—which breaks sequential dependencies and enables massive context parallelism. A Q-K projection resolves a compression-retrieval domain mismatch. Stage 2 fine-tunes only the local modules with smaller chunk sizes to optimize inference. On Titans at 150M scale, TNT achieves up to 17× faster time-to-target-loss than the best Titans baseline while improving perplexity (23.13 vs. 25.07) and reasoning accuracy (41.0% vs. 39.0%).

## Strengths

- **Novel periodic-reset mechanism for context parallelism in non-linear memories.** The key innovation is elegantly simple: resetting local memory states to a learned initial value at regular intervals ($S_L$) breaks the token-to-token sequential dependency that prevents parallelization of deep memory modules. This is a genuinely useful solution to a real bottleneck (Section 4.1.1, Eq. 6) and is what enables the throughput gains.

- **Clean ablation study validating each component.** Table 3 directly quantifies contributions: removing global memory hurts severely (PPL 21.04→25.60), removing Q-K projection hurts substantially (21.04→22.01), and adding local modules monotonically improves performance (23.53→20.15 with four). This is strong evidence that the hierarchical design is responsible for both the speedup and the quality.

- **Convincing demonstration of chunk-size sensitivity (Challenge 3).** Figure 2 shows that a model pre-trained with chunk size 64 achieves near-optimal perplexity only at that exact chunk size, with sharp degradation at both smaller and larger sizes. This clean observation motivates Stage 2 and is a genuine insight about deep memory modules.

- **Strong time-to-quality gains without sacrificing accuracy.** Table 1 shows TNT reaches target loss 3.20 up to 17.37× faster than the best Titans configuration, while Table 2 shows TNT Stage 1 models simultaneously achieve better perplexity (23.13 vs. 25.07) and reasoning accuracy (41.0% vs. 39.0%). This combination rebuts the usual efficiency–accuracy trade-off for the setting studied.

## Weaknesses

### Major

None.

### Minor

- **Headline speedup conflates architectural quality and parallelism gains.** The 17× speedup in Table 1 measures *time to reach a target loss*, which combines (a) how many tokens the model needs (sample efficiency) and (b) how fast each token is processed (throughput). Because TNT changes the architecture (hierarchical memory, Q-K projection) beyond just enabling parallelism, part of the speedup may come from the model being better per token rather than from parallelization. The paper provides separate runtime data (Figure 4) and quality data (Table 2), so the issue is not a missing analysis, but the headline claim is ambiguous. Reporting tokens-per-second and tokens-to-target-loss separately would cleanly resolve this. This is a presentation gap, not a fatal flaw, but it should be addressed.

- **Runtime scaling of Figure 4 is misdescribed.** The paper states "TNT's runtime grows linearly with sequence length" (Section 5.2). The actual data shows that TNT (C_L=16) is flat at ~400ms across 2k–32k, and TNT (C_L=128) grows from ~400ms to ~550ms—far slower than linear and arguably near-constant. This description is factually inaccurate. The constant/flat runtime is actually a *stronger* result than linear scaling (it follows because total tokens per batch is fixed, so the number of parallel local windows is constant), and should be described correctly and celebrated.

- **Stage 2 improvement is modest relative to the two-stage framing.** The paper's title and narrative position Stage 2 as a key part of the "decoupling" of efficiency from performance. The empirical gain from Stage 2 on top of the best Stage 1 model is small: PPL 23.13 → 23.09 and accuracy 40.6% → 40.9% (Table 2). While Stage 2 does enable using very small inference chunks (C_L'=1) which is practically useful for autoregressive decoding, the quality improvement is marginal and the current framing somewhat overstates its importance.

- **Q-K Projection overhead not quantified.** The $d \times d$ projection matrix per head per local module is described as "constant-size state" without numerical context. For typical dimensions (e.g., $d=512$, multi-head), this is a non-trivial auxiliary state. The paper would benefit from acknowledging this cost and discussing scaling to wider models. (Parameter count is held constant vs. baselines, so this is a cost that trades off against other parameters.)

### Trivial

- The phrase "grows linearly" in Section 5.2 contradicts Figure 4's flat data for C_L=16 (see Minor above).

## Nice-to-Haves

- **Scale beyond 150M.** All primary experiments use 150M-parameter models. Showing viability at 350M or 1B+ would significantly strengthen the scalability claims.
- **Sensitivity study of $S_L$ (local window size).** The degree of parallelism and long-range context captured by local memories depends entirely on $S_L$. A sweep (e.g., 512, 1024, 2048, 4096) for both quality and throughput would be informative.
- **Q-K projection alternatives.** Ablating against simpler query-conditioning mechanisms (e.g., concatenating $q_t$ with a key aggregate) would clarify whether the specific projection form matters or whether any alignment mechanism suffices.
- **Roofline or FLOPs-utilization analysis.** The paper claims TNT makes training compute-bound; profiling evidence would strongly support this.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. *Harsh critic's claim that Challenge 2 lacks rigorous justification.* The paper provides a clean ablation (Table 3: removing Q-K projection raises PPL from 21.04 to 22.01), which is standard empirical validation for this type of architectural claim. The request for a "proof of a gradient vanishing problem" is unrealistic for an empirical systems paper.
2. *Harsh critic's "factual contradiction" framing of the scaling analysis.* While the description "linear" is indeed inaccurate (it is actually flat/constant or very weakly growing), the data supports a *stronger* claim than what the paper makes. Calling this a "factual contradiction" or suggesting "the authors do not fully understand what their own experiment is measuring" is disproportionate. The error is in the text description, not in the data or the method.
3. *Harsh critic's suggestion that the paper is a "specific architecture" rather than a "training paradigm."* The periodic reset and hierarchical memory are architectural changes, but they are applied to an existing class of architectures (deep memory modules) and the paper tests on multiple bases (Titans, with TTT as baseline). The "training paradigm" framing is reasonable.
4. *Strength Finder's claim that "TNT is also validated on TTT models."* The abstract states "Evaluated on Titans and TTT models" — TTT appears only as a baseline (Table 2), not as an architecture to which TNT is applied. This is a factual error in the strength description (not in the paper itself, since the appendix, which is stripped from the parser output, may contain TNT-on-TTT results).
5. *Criticism about missing hyperparameter details (e.g., exact parameter distribution).* These are standard implementation details; the hard rules require removing nitpicks about trivial implementation details.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Disentangle the speedup.** Add columns to Table 1 reporting (a) tokens-per-second and (b) tokens-to-target-loss for TNT vs. baseline Titans at matched chunk sizes. This separates the parallelism contribution from the architectural quality contribution and makes the headline claim fully interpretable.

2. **Correct the Figure 4 description.** Replace "grows linearly" with a description that matches the data: e.g., "TNT's per-step runtime is approximately constant (or grows very mildly) with sequence length because total tokens per batch is fixed, so the number of parallel local windows is constant. This near-constant runtime is a consequence of the periodic-reset parallelism and is even stronger than O(L) scaling."

3. **Recalibrate the Stage 2 narrative.** Acknowledge that the quality improvement from Stage 2 is modest in absolute terms (≈0.04 PPL, ≈0.3% accuracy) while the primary practical value is enabling small-chunk inference (C_L'=1) for autoregressive decoding. Present Stage 2 as a lightweight adaptation step rather than a co-equal pillar of the contribution.

4. **Provide a brief numerical note on Q-K Projection overhead.** For example: "For a model with d=512 and 4 local memory heads, the running sum Σ k_τ k_τ^⊤ requires storing 4 × 512 × 512 = ~1M parameters worth of state, which is modest relative to the 150M total parameters."

---

## Score and Decision

My final score is determined through comparative calibration. 

**Round 1 (bracketing):** I queried three bands. The low band (avg < 3.5) returned papers on general RNN training scoring 2.33–3.00 — TNT is clearly stronger. The middle band (3.5–7.5) returned hierarchical-memory and efficient-sequence-modeling papers scoring 5.00–6.50, with the most relevant being MELODI (6.25, hierarchical memory compression). The high band (7.5+) returned papers on unrelated topics (context-parametric inversion, associative memories) scoring 7.60–8.00 — TNT is not at this level. Initial bracket: **5.0–6.5**.

**Round 2 (narrowing):** I queried inside the bracket and beyond, retrieving:

| Anchor | Avg Score | How it compares to TNT |
|--------|-----------|------------------------|
| "Parallelizing non-linear sequential models..." (E34AlVLN0v) | 6.00 (Accept) | Same problem class; TNT has stronger empirical validation (multiple benchmarks, ablations) but more framing issues. Comparable. |
| Ultra-Sparse Memory Network (zjeHLSiNv1) | 6.00 (Accept) | Different problem (inference memory access); TNT has similar evaluation thoroughness. Comparable. |
| MELODI (TvGPP8i18S) | 6.25 (Accept) | Similar hierarchical memory idea; MELODI is cleaner in framing but TNT addresses a harder parallelism bottleneck. TNT is slightly weaker. |
| Think Before You Act (FhbZ1PQCaG) | 5.75 (Reject) | Memory for RL decision transformers; TNT has stronger technical novelty and evaluation. TNT is clearly better. |
| HiP (PTcMzQgKmn) | 6.25 (Accept) | Training-free attention pruning for Transformers; different setting, similar rigor. TNT is comparable. |

**Final score:** The paper is consistently near the 6.0 anchors. It has stronger empirical contributions than the 5.75 rejected paper and comparable rigor to the 6.00 accepted papers. The framing issues (conflated metric, runtime misdescription) prevent it from reaching the 6.25 level of MELODI or HiP. I place it at **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>