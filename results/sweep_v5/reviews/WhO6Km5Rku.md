Now I have sufficient calibration context. Let me write the consolidated review.

---

## Summary

QubitCache proposes a hybrid quantum-classical KV cache compression method that preserves 15% of tokens in classical storage while encoding the attention patterns of the remaining 85% into 9-qubit quantum states via amplitude encoding. During inference, these states are measured to produce probabilistic "soft attention" weights for the compressed tokens, combined with exact attention over preserved tokens. The paper evaluates across 5 models and 7 benchmarks, reporting competitive performance against compression baselines.

## Strengths

- **Attention-based token selection is convincingly shown to be the main driver of performance.** Table 4's ablation is the strongest result in the paper: removing attention-selected critical tokens drops F1 by 20.4% (0.491 → 0.391), while replacing selection with random tokens drops it to 0.335. This cleanly demonstrates that *which* tokens are preserved matters far more than the quantum encoding itself — a useful empirical finding independent of the quantum framing.

- **Competitive memory footprint with generally strong retention of uncompressed performance.** Table 3 reports 7.0× compression (0.55 GB for 8K tokens) vs 2.0× for token-selection methods and 6.7× for GEAR. On PG19 language modeling (Table 1), QubitCache retains 97.6% of FullKV F1 (0.121 vs 0.124), while ScissorHand collapses to 37.1%. This suggests the hybrid strategy preserves more useful information than pure eviction.

- **Thorough multi-model evaluation across a reasonable range of architectures.** The paper tests 5 models (Mistral-7B, Qwen2-7B, Phi-4-mini, DeepSeek-Coder-7B, Llama-8B) plus scaling experiments on Llama-70B and Qwen-30B. This breadth supports the generalizability of the core findings.

## Weaknesses

### Major

- **The headline performance claim ("15-25% higher F1 on multi-hop reasoning") is not supported by the reported data.** On HotpotQA (the main multi-hop benchmark), the improvement over the best compression baseline at comparable retention rates is 1.6–10.8%, not 15–25% as stated in the abstract and contributions. For instance, Mistral-7B: 0.459 vs GEAR 0.434 (+5.8%); Llama-8B: 0.510 vs H2O 0.502 (+1.6%). Only if one selectively compares against the weakest baselines on specific models (e.g., Phi-4-mini vs H2O's 0.390) does the number approach 15%. The abstract's phrasing is misleading and should be corrected to precise delta ranges.

- **The "logarithmic compression beyond classical information-theoretic limits" framing is overstated for the actual implementation.** The paper's own Table 3 makes clear that the memory complexity is dominated by the O(L×H×0.15S×D) term from preserved tokens; the quantum log N term is negligible. Moreover, for the *classical simulation* that is actually evaluated, each 9-qubit state is stored as 2⁹ = 512 complex amplitudes — the same O(N) cost as directly storing the attention vector. The logarithmic claim only strictly holds if the method runs on actual quantum hardware, which the paper does not do. This does not invalidate the method but makes the "beyond classical limits" framing inaccurate for what is actually evaluated.

- **Dynamic query-dependent attention for compressed tokens is not addressed.** The quantum states are constructed from attention scores computed during the initial forward pass (Equations 3–5). During autoregressive decoding, the query vector changes at each step, yet the probability distributions pⱼ(ψ) for already-compressed segments remain fixed (Equation 7). Section 3.4 describes updating quantum states when tokens shift categories but never discusses recomputing existing states in response to new queries. While this limitation is shared with other eviction-based methods (H2O, ScissorHand also make irrevocable decisions), the paper's claim of enabling "dynamic attention" and "relational preservation" is undercut by this static behavior. The paper should either acknowledge this limitation explicitly or provide evidence that the fixed prior does not materially harm performance on tasks requiring query-dependent re-weighting.

### Minor

- **Evaluation is limited to 2K–8K token sequences.** For a KV-cache compression method, this is relatively short. The method's purported advantages (graceful degradation, long-context coherence) would be more convincingly demonstrated on 32K+ or 100K+ sequences, especially since theoretical scaling differences from eviction methods become more apparent at extreme lengths.

- **The quantum circuit construction is under-specified.** The claim that a depth-15 hierarchical Ry rotation pattern can prepare a target 512-dimensional amplitude vector with fidelity sufficient for the reported results is not supported by any mathematical construction or analysis. Arbitrary 9-qubit state preparation generally requires O(2⁹) gates in the worst case, so some structural assumption or approximation must be at play — but none is described. A circuit that operates at depth 15 with 9 qubits can implement at most a very restricted class of states; the paper should specify the expressiveness of this family and ground it theoretically.

- **The "relational preservation" claimed is actually marginal importance weights.** The quantum state encodes αᵢ = a̅ᵢ / Σⱼ a̅ⱼ, where a̅ᵢ is token i's average attention weight aggregated over layers, heads, and positions. This is a per-token marginal distribution, not a pairwise relational encoding. Calling it "relational structure preservation" overstates what is stored, which is closer to importance-weighted retrieval than pairwise attention reconstruction.

- **The quantum component's contribution is modest.** Removing the quantum encoding entirely (Table 4: "No Quantum" → 0.472) only drops F1 by 3.9% relative to Full QubitCache (0.491). The primary driver of performance is clearly the attention-based token selection policy (20.4% drop when removed). The paper over-interprets the quantum contribution as "validating our core hypothesis" when it is the selection mechanism that does the heavy lifting.

### Trivial

- Table 1 formatting is dense and the column grouping ("Short" vs "Long") is not immediately clear.
- The paper repeatedly cites "15-25% improvement" without a specific breakdown of which baseline × model combinations produce those numbers.

## Nice-to-Haves

- Matched-budget comparison: evaluating H2O, ScissorHand, and StreamingLLM at 15% token retention would cleanly separate the benefit of the method from the benefit of operating at a different compression ratio. (The comparison against GEAR at 6.7× partially mitigates this concern, since GEAR operates at a similar compression ratio.)
- A per-step analysis showing how the attention weights pⱼ(ψ) for compressed tokens compare to the true query-dependent weights during decoding.
- Memory breakdown plot showing the fraction consumed by classical tokens vs. quantum state overhead vs. interpolation data.

## Removed Points

- **"The method does not actually compress the KV cache via quantum encoding"** (Harsh Critic Issue 1, first sentence): Removed because the paper is explicit about being a hybrid method where 15% of tokens are stored classically. The quantum encoding *does* compress attention patterns in the theoretical sense the paper describes. The misrepresentation is about the *extent* of the quantum contribution, not its existence. This is addressed adequately under the "logarithmic compression" weakness above.
- **"The 15–25% F1 improvement on multi-hop reasoning is unsupported"** (Harsh Critic Issue 3b with the claim "None of these approach 15%"): The critic calculated against GEAR only. Against 50%-retention methods, some models do show 15%+ improvement (Llama-8B: +21.4% vs ScissorHand; Phi-4-mini: +17.2% vs ScissorHand). However, the claim as stated in the abstract is still too broad, so a revised version of this criticism is kept in Major weaknesses.
- **"The ablation shows the quantum part is marginal"** → kept in Minor weaknesses as stated.
- **"The paper should be reframed as token-eviction with interpolation"** → this is a framing suggestion, not a weakness.
- **"The graph-theoretic argument is cited but never connected to the method"** → this is a writing observation, not a substantive weakness.
- **"Storing attention weights classically would cost O(N)"** → for the *classical simulation* the paper actually runs, this is true, but it's acknowledged as a classical simulation. The reviewer's framing ignores the stated hardware target.
- **Generic strengths from Strength Finder about "important problem" or similar** → removed as not specific enough.

## Novel Insights

Beyond the paper's own contributions, the crossover observation from the reviews is that the ablation study (Table 4) implicitly provides a clear ranking of what matters in this hybrid approach: attention-based token selection contributes ~20% performance, the quantum encoding contributes ~4%, and positional heuristics (anchor/recent tokens) contribute <1%. This suggests the most valuable direction might be improving *token selection policy* rather than the quantum encoding itself — a finding the paper's framing inverts by foregrounding the quantum component. The reviewers also collectively surface a disconnect between the paper's language ("relational preservation," "logarithmic compression") and what is actually implemented (marginal importance weights, classical simulation). This is a recurring pattern in quantum-inspired ML papers and should be treated as a lesson for future work in this space.

## Suggestions

1. **Correct the overclaiming.** Replace "15-25% higher F1 on multi-hop reasoning" with precise ranges tied to specific baselines. Either remove or carefully qualify the "logarithmic compression beyond classical limits" language given that the evaluation is classical.
2. **Add matched-budget baselines.** Run eviction methods at 15% retention and show QubitCache's advantage persists.
3. **Address the dynamic-attention limitation directly.** Either (a) explain how quantum states are updated during decoding for already-compressed segments, or (b) acknowledge the fixed-prior limitation and provide evidence (e.g., per-step attention alignment scores) that it does not significantly harm performance on multi-hop reasoning compared to the ideal full-attention baseline.
4. **Specify the quantum circuit construction mathematically.** Provide the explicit mapping from the target attention distribution to the rotation angles in the hierarchical Ry circuit. Analyze the expressiveness of the depth-15, 9-qubit circuit family and bound the approximation error.
5. **Run long-context experiments (≥32K tokens)** on benchmarks like LongBench's long-document subsets or RULER to demonstrate the method's scaling behavior.

## Score and Decision

**Calibration anchors** (all retrieved in single batch):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| LSH-E (KV cache, LSH eviction) — /home/wg25r/split_review/datasets/deepreview_13k_calibration/0ZcQhdyI3n.md | 3.83 | Weaker evaluation (limited baselines, datasets), less novel framing. QubitCache has better ablation and broader model coverage. |
| ChunkKV (KV cache, chunk eviction) — /home/wg25r/split_review/datasets/deepreview_13k_calibration/8sglLco8Ti.md | 5.25 | Comparable evaluation breadth but ChunkKV is less novel (chunking + layer reuse). QubitCache's quantum idea is more creative but its empirical claims are less reliable. |
| PyramidKV (KV cache, layer-aware eviction) — /home/wg25r/split_review/datasets/deepreview_13k_calibration/jZVNmDiU86.md | 5.60 | More thorough evaluation at extreme compression ratios, less overclaiming. QubitCache's idea is more novel but its evaluation is less complete for the claimed benefits. |
| FreqKV (KV cache, frequency compression) — /home/wg25r/split_review/datasets/deepreview_13k_calibration/KscheKSYrh.md | 5.80 | Similar level of overclaim vs. actual compression benefits. FreqKV has clearer technical specification. QubitCache has better ablation. |
| Extreme composite compression (LLM compression) — /home/wg25r/split_review/datasets/deepreview_13k_calibration/zno7tZVG8T.md | 4.25 | Both overclaim and have limited evaluation scope. QubitCache is more novel but its central claim is less supported. |
| HeadKV (KV cache, head-level) — /home/wg25r/split_review/datasets/deepreview_13k_calibration/FJFVmeXusW.md | 6.50 | Stronger evaluation, more convincing empirical support, accepted. QubitCache has more novelty in framing but weaker empirical verification. |
| Cut Your Losses (LLM optimization) — /home/wg25r/split_review/datasets/deepreview_13k_calibration/E4Fk3YuG56.md | 8.50 | Extremely clean contribution with thorough evaluation. QubitCache is not in the same tier empirically. |

Relative to these anchors: QubitCache is stronger than LSH-E (3.83) in evaluation breadth and novelty, comparable to ChunkKV (5.25) and FreqKV (5.80) in overall quality but weaker than HeadKV (6.50) in empirical rigor. The paper's central overclaim and the gap between its stated novelty and actual implementation limit its score.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>