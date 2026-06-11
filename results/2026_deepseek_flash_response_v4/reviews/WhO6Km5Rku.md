Now I have a clear picture. Let me compile the final review with calibration.

**Round 1 bracket**: Based on the calibration anchors, the plausible score range was 3.5 to 5.5. The paper is clearly above IntelLLM (3.0) and LSH-E (3.83) due to better empirical evaluation and more novel framing, but below MiKV (5.0) and KV-Dict (5.25) because those papers make honest claims while QubitCache has misleading framing.

**Round 2 narrowing**: KVTQ (4.40) provides the closest analog — both have misleading terminology and lack latency numbers, but KVTQ's misleading claim ("ternary" when it's actually multi-channel) is less central than QubitCache's misrepresented O(log N) memory claim. QNF-Net (5.0) is a quantum-inspired paper with similar "does the quantum part do anything" concerns but stronger theoretical grounding.

**Final score**: 4.0 — slightly below KVTQ (4.40), well above IntelLLM (3.0), but significantly below MiKV (5.0) and KV-Dict (5.25).

**Decision**: Reject — the paper's core contribution (soft attention for non-critical tokens via value interpolation) has empirical merit, but the quantum framing introduces misleading claims about O(log N) compression and "beyond classical information-theoretic limits" that are not supported, and the practical viability (latency/throughput) is unevaluated.

---

## Summary

QubitCache proposes a hybrid KV-cache compression method that stores 15% of tokens (selected by attention scores) in classical storage and encodes attention patterns of the remaining 85% into quantum-inspired amplitude-encoded states (simulated classically). Measurement probabilities from these states serve as soft attention weights for interpolated value vectors. On multi-hop reasoning tasks, QubitCache achieves notably higher F1 than token-eviction baselines despite operating at higher compression ratios.

## Strengths

1. **Reframes KV-cache compression from token selection to relational-structure preservation, with supporting ablation evidence.** Table 4 shows that removing attention-selected critical tokens causes a 20.4% F1 drop (0.491→0.391), while removing position-based heuristics (anchor/recent) causes only 0.6% drops. Random token selection with quantum encoding achieves only 0.335 — confirming that attention-based selection, not token count, drives performance. This is a genuine conceptual shift from the binary keep/drop framing of prior work (H2O, ScissorHand, StreamingLLM, GEAR).

2. **Demonstrates 15–25% higher F1 on multi-hop reasoning than baselines despite more aggressive compression.** On HotpotQA with Qwen2-7B (Table 1), QubitCache achieves 0.604 F1 vs. H2O's 0.487 (+24.0%) and ScissorHand's 0.555 (+8.8%). Results are consistent across Mistral-7B, Phi-4-mini, DeepSeek-Coder, and Llama-8B. The evaluation covers 5 models × 7 benchmarks — reasonably thorough for a new compression method.

3. **Ablation reveals the actual mechanism of improvement.** The comparison of Full QubitCache (0.491) vs. No Quantum (0.472) vs. No Critical (0.391) empirically isolates which design choices matter. The 20.4% drop from removing attention-selected tokens versus the 3.9% drop from removing the quantum encoding honestly discloses the relative contribution of each component.

## Weaknesses

### Major

1. **The O(log N) memory claim is not realized as stated.** Table 3 reports QubitCache memory as O(L × H × 0.15S × D + log N). The "log N" term is meant to represent the quantum encoding, but the actual storage required depends on implementation: (a) on a classical simulator, the state vector has 2ⁿ = 512 elements per segment — O(N) per segment, not O(log N); (b) on quantum hardware, the rotation angles encoding the 512 amplitudes must be stored somewhere, also O(N). The paper never clarifies where the logarithmic savings materialize, nor does it provide a memory accounting that includes the encoding parameters. The associated claim "achieving logarithmic compression beyond classical information-theoretic limits" (abstract, line 9) has no supporting information-theoretic analysis — no comparison with Shannon limits, no consideration of the Holevo bound, no demonstration that the total bit budget is lower than classical alternatives.

2. **No latency or throughput measurements are reported.** The paper claims "minimal latency overhead" (line 216) but provides zero wall-clock time, tokens-per-second, or latency comparisons against any baseline. For a method that requires simulating quantum circuits for every segment/layer/head during each forward pass, this is a fundamental omission. Without these numbers, the claim of "practical feasibility" (line 25) is unsubstantiated.

### Minor

3. **The "No Quantum" ablation baseline is underspecified.** Table 4 shows a 3.9% drop from Full QubitCache (0.491) to "No Quantum" (0.472), but the paper does not state what happens in this configuration — are non-critical tokens simply dropped? Replaced with uniform weights? The interpretation of the quantum component's contribution depends critically on this specification. The 3.9% gap is not necessarily trivial, but without knowing the baseline, it is uninterpretable.

4. **Static attention weights may drift from query-dependent attention during generation.** The quantum state encodes attention weights computed at prefill time (Equation 3: column-summed attention to each token), but attention in transformers is query-dependent (softmax(QKᵀ/√d)). The paper describes sliding-window updates (Section 3.4) as partial mitigation but provides no analysis of how much attention distributions drift as new tokens are generated, or how the approximation holds over long generations.

5. **No equal-compression-ratio comparison with baselines.** Baselines operate at ~2× compression (50% retention) while QubitCache operates at ~7× (15% retention). This makes it difficult to isolate whether the advantage comes from the soft-attention mechanism or simply from having a more aggressive (and differently designed) retention policy. An experiment where all methods are evaluated at the same compression ratio would strengthen the claim.

### Trivial

6. Memory figures in Table 3 do not account for the classical simulation cost of the quantum encoding — the 0.55 GB figure includes only the 15% preserved KV pairs plus the abstract "log N" term, not the actual state vectors or rotation parameters.

## Nice-to-Haves

- Analysis of attention drift between encoding time and generation time.
- Equal-compression-ratio experiments (all methods at 7×).
- A rigorous information-theoretic accounting if the "beyond classical limits" claim is to be maintained.

## Removed Points

**From Harsh Critic — removed or downgraded:**

1. *"The quantum amplitude encoding does not provide compression — it is a computationally expensive round-trip"*: Removed as overstated. The encoding compresses representation of non-critical KV pairs into quantum amplitudes, which is a form of compression even if the parameters scale with N. The valid core of this criticism (O(log N) not being realized) is preserved in Major Weakness #1.

2. *"Ablation shows the quantum component contributes almost nothing"*: Removed. A 3.9% improvement is measurable and non-trivial. The criticism is downgraded to Minor Weakness #3 because the baseline is underspecified, not because the effect is negligible.

3. *"The computational cost would be prohibitive" with specific count of 16,384 simulations*: The paper states that optimizations (gate fusion, parallel segment encoding, adaptive shot allocation) are used, and without latency measurements the cost is speculative. Absorbed into Major Weakness #2.

4. *Claims about Holevo bound and Shannon limits fundamentally invalidating the method*: These are legitimate concerns about the "beyond classical limits" claim but do not invalidate the empirical results. The concern is preserved in Major Weakness #1's discussion of missing information-theoretic analysis.

**From Strength Finder — removed as unsupported:**

5. *"Efficient cache update with O(log n) amortized cost"*: This is asserted (Section 3.4) but not empirically validated with any measurements. No update overhead numbers are provided.

## Novel Insights

The harsh critic's analysis correctly identifies a tension: the quantum encoding is presented as the central innovation, but the ablation data shows that attention-based token selection (a known mechanism) accounts for ~20% of performance while the quantum encoding accounts for only ~4%. The strength finder correctly notes that the empirical multi-hop results are genuinely strong. The honest contribution of this paper is likely that a soft-attention / value-interpolation scheme over non-critical tokens (using static attention weights) improves upon hard-eviction baselines. The quantum framing adds conceptual novelty but also introduces misleading memory claims and unquantified computational overhead. The paper would be more convincing if it stripped the quantum framing and presented the method as a simple hybrid of attention-based selection + value interpolation with static weights — but that would also reduce its headline novelty.

## Suggestions

1. Provide a corrected memory accounting that honestly reports the storage needed for the quantum encoding parameters or simulator state vectors. Remove the "O(log N)" claim unless it can be rigorously justified.

2. Report latency and throughput measurements (tokens/s, time per generation step) comparing against all baselines. Without these, the method's practical viability is unknown.

3. Remove or substantially qualify the "beyond classical information-theoretic limits" claim — it is not supported by any analysis in the paper.

4. Specify the "No Quantum" ablation: what exactly is done with non-critical tokens?

5. Add equal-compression-ratio experiments (every method at 7×) to isolate the soft-attention benefit.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- IntelLLM (3.0) — KV cache eviction with weak baselines and missing ablations. QubitCache is clearly stronger (better evaluation, more novel framing).
- LSH-E (3.83) — LSH-based KV eviction, missing baselines and timing. QubitCache is stronger (more models, better benchmarks, stronger multi-hop results).
- MiKV (5.0) — Mixed-precision KV compression, honest claims but limited novelty. QubitCache has more novelty but more severe misleading claims.
- KV-Dict (5.25) — Dictionary-based compression, missing throughput measurements. QubitCache has similar profile but more central misleading claims.

**Round 2 (Narrowing):**
- KVTQ (4.40) — Ternary quantization with misleading terminology and no latency numbers. QubitCache is similarly positioned but has more central misleading claims (O(log N) vs. terminology choice).
- QNF-Net (5.0) — Quantum neural field with similar "does quantum help?" concerns. QubitCache has weaker theoretical grounding for its quantum component.
- ChunkKV (5.25) — Chunk-based KV cache compression. QubitCache has more novel framing but less honest claims.

**Final position**: QubitCache sits slightly below KVTQ (4.40) due to the centrality of its unsupported O(log N) and "beyond classical limits" claims, but well above the 3-range papers (IntelLLM, LSH-E) due to stronger empirical validation and more novel conceptual framing.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>