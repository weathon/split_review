Now I have a solid calibration picture. Let me synthesize the final review.

**Calibration Summary:**

Round 1 bracket: 4.5–6.0. Lower-band anchors (EMS 4.60, LSH-E 3.83) have weaker evaluation or novelty; upper-band anchors (MatryoshkaKV 6.00, Not All Heads Matter 6.50) are cleaner contributions with fewer overclaiming issues.

Round 2 narrowing: Don't Discard/MiKV (5.00) is the closest peer — similar evaluation breadth and a genuinely useful core idea, but both are held back by limited novelty relative to claims. ChunkKV (5.25) and KV-Dict (5.25) are also comparable in structure (interesting idea + solid experiments + rejected). QubitCache's core idea (relationship preservation over token selection) is more novel than any of these, but the quantum overclaiming is a larger flaw. The paper sits between these anchors — novel idea but weakened by inflated claims — placing it at 5.0.

---

Now let me produce the final review.

## Summary
2-3 sentence summary.

## Strengths

1. **Attention-relationship preservation (not just token selection) is a genuinely novel framing for KV-cache compression.** The ablation study (Table 4) convincingly shows that attention-based critical token selection drives performance (20.4% drop when removed) while position-based heuristics contribute almost nothing (<1% drop each), and random selection collapses to 68% of full performance. This validates the core insight that preserving attention *relationships* is more important than which specific tokens are kept.

2. **Empirically measured 7× compression with 92–97% performance retention across 5 models and 7 benchmarks (Table 1).** The evaluation is reasonably broad — Llama-8B, Mistral-7B, Qwen2-7B, Phi-4-mini, DeepSeek-Coder — and the compression ratios are measured empirically (0.55 GB vs 3.91 GB in Table 3), not just claimed asymptotically. The performance retention numbers are competitive with or better than token-eviction methods (H2O, ScissorHand, StreamingLLM) and the quantization baseline (GEAR).

3. **Scaling demonstration to 70B-parameter models (Table 2).** QubitCache retains 96.9% of uncompressed F1 on Llama-70B NarrativeQA, outperforming all baselines. This addresses the key use case where KV-cache memory is most painful.

## Weaknesses

### Major

1. **The paper overclaims "logarithmic compression beyond classical information-theoretic limits" for a method running entirely as a classical simulation.** The abstract, introduction, and contributions all state this as a core achievement. In the classical simulation, each 9-qubit "quantum state" requires storing all 512 complex amplitudes (a 512-element probability distribution) per segment. The memory complexity in Table 3 lists `O(log N)` for the quantum component, but the total stored information per segment is linear in the segment size (512 numbers), not logarithmic. The paper acknowledges the implementation is a simulation (Section 3.2.2, "the current implementation operates as a classical simulation"), but the marketing language throughout the paper does not match this reality. The 7× compression empirically measured is real, but it comes primarily from retaining only 15% of KV pairs classically — not from any logarithmic quantum advantage. This is a significant gap between the paper's framing and its actual contribution.

2. **The quantum amplitude encoding contributes at most 3.9% of the method's performance (Table 4), while the attention-based token selection is the true driver.** The ablation shows: Full QubitCache = 0.491, No Quantum = 0.472 (3.9% drop), No Critical = 0.391 (20.4% drop), Random + Quantum = 0.335. The paper does not compare against a simple classical baseline that would achieve the same effect: (a) select 15% critical tokens via attention scores, (b) for the remaining 85%, compute a *single weighted average* of their value vectors using the same attention distribution that the quantum measurement provides. Such a baseline would store one aggregated vector per segment instead of 512 probabilities, would match or exceed the "No Quantum" variant's performance, and would make clear that the quantum encoding is not the source of the compression. The absence of this baseline makes it impossible to attribute any meaningful part of the gains to the quantum-inspired component.

3. **The "15-25% higher F1 on multi-hop reasoning" claim in the abstract, introduction, and contribution list is selectively supported.** Verifying against Table 1's HotpotQA results:
   - Mistral-7B: 0.459 vs H2O 0.420 = 9.3% relative improvement
   - Qwen2-7B: 0.604 vs H2O 0.487 = 24.0%, but vs GEAR 0.545 = 10.8%, vs ScissorHand 0.555 = 8.8%
   - Llama-8B: 0.510 vs H2O 0.502 = 1.6%, vs ScissorHand 0.420 = 21.4%
   The 15–25% range only appears against the weakest baselines (H2O, StreamingLLM) and is not uniform. The paper states "compared to existing methods" without specifying which, giving a misleading impression of the consistency of the advantage.

### Minor

4. **The value reconstruction in Equation (6) uses inverse distance weighting (IDW) from neighboring preserved tokens rather than any information from the quantum state's attention distribution.** The quantum state encodes attention probabilities, but the actual *values* for the reconstructed tokens come from interpolating nearby preserved tokens' value vectors. This means the quantum encoding determines *which* tokens get influence (through probabilities p_j), but the *content* of that influence comes entirely from classical interpolation. The paper does not discuss why this design choice was made or how the attention probabilities and interpolated values interact, making the role of the quantum encoding even more unclear.

5. **Circuit depth analysis (Figure 3b) lacks quantification of approximation error.** The paper asserts a depth-15 circuit suffices for amplitude encoding and that performance "plateaus" at depth 15, but does not report the fidelity of the prepared quantum state relative to the target distribution. Without measuring approximation error, it is unclear whether the depth-15 circuit is genuinely adequate or whether saturation occurs because the measurement process or some other bottleneck masks poor state preparation.

6. **No latency or throughput measurements are reported despite significant simulation overhead.** Each inference step requires simulating 9-qubit circuits per segment (up to 16,384 circuit simulations per token for a 32-layer, 32-head model on an 8K sequence). The paper mentions "gate fusion, parallel segment encoding, and adaptive shot allocation" optimizations but provides no wall-clock time, tokens-per-second, or end-to-end latency comparison against baselines. This is a critical omission for a compression method targeting practical deployment.

### Trivial

7. Some baselines perform anomalously poorly on specific model×dataset combinations (e.g., ScissorHand at 0.018 PG19 F1 on DeepSeek-Coder, H2O at 0.200 Contract Acc on Phi-4-mini). These outliers are not remarked upon or explained.

## Nice-to-Haves

- Reporting results with variance/confidence intervals would strengthen the comparisons, especially where the gap between methods is small (e.g., QubitCache vs Full KV on GovReport: 0.820 vs 0.835).
- An ablation showing sensitivity to the retention ratio (beyond the fixed 15%) and segment size (beyond 512) would improve understanding of the method's robustness.
- Adding long-context tasks beyond 8K (e.g., 32K or 64K retrieval tasks) would better match the paper's claimed focus on long-context reasoning.

## Removed Points

The following points from the inputs were removed with justification:

- *Harsh critic: "The key equation (2) introduces a hybrid attention mechanism, but the interpolation of value vectors for compressed tokens uses inverse distance weighting rather than the actual attention weights from the quantum state."* → Kept as Minor weakness #4 above (it's a valid design observation).
- *Harsh critic: "The circuit depth should be O(2^n) in general... the validity of the amplitude encoding step is suspect."* → Toned down. The paper does describe a hierarchical binary tree scheme; the concern about missing approximation error quantification is valid and kept as Minor #5, but the claim that it's "suspect" without evidence of failure is too strong.
- *Harsh critic: "Statistical significance: No standard errors or confidence intervals."* → Moved to Nice-to-Haves. Single-run evaluation on standard benchmarks is the norm in LLM compression papers.
- *Harsh critic: "The use of LAMBADA, PG19, and PIQA as 'long-context' benchmarks: These datasets do not require long contexts."* → Removed. The paper explicitly labels PG19 and PIQA as "Short" tasks in Table 1 (not long-context claims).
- *Harsh critic: "Missing related works"* → Removed per policy.
- *Strength Finder: "Amplitude encoding achieves logarithmic compression (Section 3.2.1)"* → Removed. This statement restates the paper's claim without critical examination; the claim is addressed in Weakness #1.
- *Strength Finder: "Theoretical guarantee of bounded reconstruction error"* → Removed. The proof is in the stripped appendix; its existence cannot be confirmed or evaluated from the visible text.

## Novel Insights

A genuinely novel observation emerges from the interplay of critical and non-critical token treatment. The ablation shows that removing "critical" tokens (selected by attention concentration) causes a 20.4% F1 collapse, while removing "anchor" or "recent" tokens (position-based heuristics) causes <1% drop. This suggests that for KV-cache compression, *which* information to keep matters far more than position-based heuristics — the attention distribution itself is the bottleneck. The paper's framing of this as "relationship preservation" is insightful, even if the quantum encoding does not carry the weight the paper claims. The practical takeaway is that a simple attention-weighted reconstruction (store the attention distribution, softmax-weight the values) may achieve most of the benefit without any quantum machinery.

## Suggestions

1. **Reframe the paper honestly as a classical method with quantum-inspired design principles.** Drop the "beyond classical information-theoretic limits" claim, since the simulation stores 512-amplitude vectors. The core contribution (attention-relationship preservation via probabilistic reconstruction) stands on its own without the quantum hype.
2. **Add the baseline that isolates the quantum component's contribution:** attention-based 15% token selection + a single weighted-average value vector per segment (which is what the quantum measurement produces). If this baseline matches QubitCache, the quantum encoding is indeed ornamental; if it does not, that is an interesting finding worth reporting.
3. **Provide latency/throughput measurements.** Without these, the practical impact of the method for real deployment is unknown, and the simulation overhead may dominate any memory savings.
4. **Quantify the amplitude encoding circuit's approximation error** (state fidelity vs. target distribution) rather than relying solely on downstream task performance saturation.
5. **Be precise about the 15-25% multi-hop claim** — specify which baseline(s) and models yield which improvements, and do not present the range as universal.

## Score and Decision

**Score:** 5.0

**Decision:** Reject

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>