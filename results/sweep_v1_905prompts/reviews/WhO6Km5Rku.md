Now I have all the information I need to synthesize the final review.

---

## Summary

This paper proposes QubitCache, a KV-cache compression method that combines classical token storage (15% of tokens: anchor, recent, and attention-critical tokens) with quantum-inspired amplitude encoding of attention patterns for the remaining 85% of tokens. During inference, the compressed tokens' attention weights are reconstructed via quantum measurement probabilities, producing a hybrid hard+soft attention mechanism. Experiments across five models and seven benchmarks show 7× compression with 92–97% of full-KV performance, and ablation studies isolate a 3.9% improvement from the quantum encoding component.

## Strengths

- **Novel conceptual framing**: The paper correctly identifies that existing eviction methods irreversibly discard relational information between tokens, and proposes an alternative that preserves attention distributions rather than making binary keep/drop decisions. This reframing of KV-cache compression as a relational-structure preservation problem is genuinely creative and distinguishes the work from the large body of incremental eviction-strategy papers.

- **Comprehensive empirical evaluation across five models and seven benchmarks**: Table 1 evaluates on models from 4B to 8B parameters (Llama-3-8B, Mistral-7B, Phi-4-mini, Qwen2-7B, DeepSeek-Coder-7B) across diverse tasks including language modeling, multi-hop reasoning, summarization, and commonsense reasoning. The consistent trend — QubitCache outperforms H2O, ScissorHands, StreamingLLM, and GEAR at higher compression ratios — provides genuine evidence that the overall system works.

- **Component ablation isolating the quantum contribution (Table 4)**: The controlled comparison between "Full QubitCache" (0.491), "No Quantum" (0.472), and random selection baselines (0.334–0.335) cleanly separates three effects: (1) attention-based token selection is the dominant driver (20.4% gap vs. No Critical), (2) the quantum encoding provides a measurable 3.9% benefit over classical-only reconstruction, and (3) random selection fails entirely. This allows the reader to assess each component.

- **Practical NISQ feasibility analysis**: Figure 3 demonstrates that the 9-qubit, depth-15 circuit operates within T₂ coherence times (~100 μs) of current quantum processors, with execution time ≈750 ns per segment. This grounds the approach in hardware constraints rather than treating quantum computing as a purely abstract tool.

## Weaknesses

### Major

- **The soft attention over compressed tokens is query-independent, and this limitation is not discussed.** The measurement probabilities pⱼ(ψ) in Equation (7) are precomputed from aggregated historical attention scores (Equations 3–5) and do not depend on the current query during generation. Only the hard-attention term over preserved tokens (≈15%) is query-dependent. For the 85% of tokens processed through the quantum branch, their relational influence is frozen at compression time. This is a genuine departure from standard transformer attention that the paper should acknowledge as a limitation — some tasks where token importance shifts dynamically per query may suffer. The paper's claim of "preserving relational structure" is only partially accurate, since the reconstruction is query-agnostic.

- **The framing substantially overclaims relative to the ablation evidence.** The paper presents a "paradigm shift from token selection to relational preservation," but Table 4 shows that the dominant component is an attention-based token selection strategy (the "No Critical" ablation causes a 20.4% drop), while the quantum encoding contributes a modest 3.9% improvement. This 3.9% is non-negligible but does not support the narrative of a fundamental paradigm shift. If the paper were reframed as "attention-based critical token selection with quantum-informed soft reconstruction of non-critical tokens," the claims would be better aligned with the evidence. The 3.9% quantum contribution should be contextualized against simpler alternatives (e.g., storing a sparse histogram of attention weights classically).

- **The claim of "logarithmic compression beyond classical information-theoretic limits" is misleading for the implemented system.** In the classical simulation actually evaluated, the 9-qubit quantum state is stored as a vector of 2⁹ = 512 complex amplitudes — exactly the same classical cost as storing the original attention weights. The memory savings come entirely from retaining only 15% of KV entries classically. The quantum encoding neither reduces memory below what is classically achievable at the same token retention, nor does the current implementation realize the claimed information-theoretic advantage. The paper should distinguish between the theoretical potential of quantum storage (which could be logarithmic on real quantum hardware) and the empirical memory consumption of the simulated system.

### Minor

- **No statistical significance or variance reported.** Given that quantum measurement is fundamentally probabilistic and the method's name centers on "probabilistic" reconstruction, the absence of standard deviations or confidence intervals for any result is a notable omission. Single-run evaluations leave open the question of result stability.

- **Controlled comparison at matched compression ratios is missing.** QubitCache (15% token retention) is compared against H2O/ScissorHands/StreamingLLM (50% retention). While the system-level comparison is informative (better performance at higher compression), it does not isolate whether the advantage comes from the quantum encoding or from a superior token selection strategy. A controlled experiment where all methods are evaluated at the same retention ratio (e.g., 15%) would strengthen the case for the quantum component specifically. (The ablation in Table 4 partially addresses this but uses its own internal variant "No Quantum" rather than external baselines.)

- **The mixing weight λ = √(|ℐₚ|/N) is presented without empirical validation.** No ablation or sensitivity analysis on λ is provided. For 15% retention, λ ≈ 0.387 — meaning the 15% of preserved tokens get ≈39% weight and the 85% of reconstructed tokens get ≈61% weight. This choice may be reasonable but should be validated or at least discussed.

- **No actual runtime/latency measurements.** The paper states "minimal latency overhead" but reports no wall-clock time, throughput, or FLOP comparisons. Given that quantum circuit simulation via Qiskit adds non-trivial overhead, the practical cost of the method is unclear.

### Trivial

- The critical-token selection threshold sₘᵢₙ is mentioned in Section 3.4 but its value is not specified; a sensitivity analysis would be helpful.
- The claim "15–25% higher F1 scores on multi-hop reasoning" varies significantly across models (e.g., Llama-8B shows 1.6% improvement over H2O on HotpotQA while Phi-4-mini shows 41.8%), so the range should be qualified more precisely.

## Nice-to-Haves

- Compare against a classical baseline that stores a sparse histogram or low-rank approximation of attention weights for the compressed tokens, to directly test whether the quantum formalism provides any benefit over a purely classical mechanism with the same reconstruction philosophy.
- Report results with standard deviations (multiple runs) to assess stability of the probabilistic reconstruction.
- Provide wall-clock inference time comparisons to quantify the overhead of quantum circuit simulation.

## Removed Points

- **Theoretical proof (rank-r preservation) missing from main text**: Removed because the parser strips appendices from all papers; the proof exists in the original submission per the hard rules.
- **"Reconstructed attention is not query-dependent — this breaks the core premise" labeled as fatal/structural**: Downgraded to Major. The method is intentionally hybrid (query-dependent for preserved tokens, query-independent for compressed tokens). This is a real limitation that should be discussed, but it does not invalidate the approach — it is a design trade-off, not a broken premise.
- **Comparison at different retention ratios is unfair**: Partially removed. The system-level comparison is valid — QubitCache achieves better results at higher compression. The request for controlled experiments at matched ratios is kept as a Minor weakness.
- **Formatting/style nitpicks and grammar issues**: Removed as parser artifacts.
- **Missing related work**: Removed per hard rules (cannot verify external references).
- **"The paper does not mention that the quantum encoding is not truly 'probabilistic'"**: Removed. The paper describes Born-rule measurement probabilities; in classical simulation exact probabilities are computed, but on quantum hardware measurements would be probabilistic. This is standard practice and acknowledged.
- **Strength Finder's generic strengths**: Removed generic statements about the problem being important or interesting; kept only concrete, evidence-anchored strengths.

## Novel Insights

The most interesting observation — which no single reviewer fully articulated — is that QubitCache's design exposes a fundamental tension in KV-cache compression that the field has not grappled with directly: the trade-off between query-dependence and memory. Standard attention is fully query-dependent (O(N) per step); token eviction preserves query-dependent attention for a subset (O(k) per step); QubitCache's quantum encoding preserves all tokens' influence but sacrifices query-dependence for the compressed majority. This reveals a three-way design space (memory × coverage × query-sensitivity) that is worth articulating explicitly. The paper's results suggest that for many tasks, query-independent relational information (precomputed attention distributions) retains surprising value — a finding that deserves broader discussion even if the quantum mechanism is replaced by a classical alternative.

## Suggestions

1. **Acknowledge and analyze the query-independence trade-off explicitly.** Measure the gap between QubitCache's query-independent reconstruction and a version that uses the true query-dependent attention for all tokens (at higher memory cost). This would quantify what is lost by freezing the compressed-branch weights.
2. **Replace the "paradigm shift" framing with a more precise characterization** of what the method achieves: attention-based critical token selection + quantum-informed soft reconstruction for non-critical tokens.
3. **Add a controlled comparison** where all methods use the same retention ratio (15%) to isolate the reconstruction mechanism from the selection strategy.
4. **Clarify the memory accounting**: separate the memory cost of classically stored KV entries (15% × full KV) from the cost of the simulated quantum state (2ⁿ complex amplitudes) to avoid misleading readers about logarithmic compression in the current implementation.
5. **Run a classical-only variant** that replaces the quantum amplitude encoding with a sparse histogram or low-rank matrix of the same attention weights, to test whether the quantum formalism provides any benefit beyond its mathematical description.

## Score and Decision

**Round 1 bracket**: I queried three bands — weak anchors (<3.5) for general KV cache compression papers (avg scores 2.0–3.0), middle anchors (3.5–7.5) for quantum-inspired ML papers (avg scores 4.75–6.33), and strong anchors (>7.5) for top ML papers (avg scores 8.0–8.5). This placed the plausible range between 4 and 6.

**Round 2 narrowing**: I queried two narrower bands within the bracket. For KV cache compression papers scoring 3.5–6.0, the anchors averaged 3.83–5.75 (rejected: LSH-E at 3.83, Identify Critical KV at 5.75, ChunkKV at 5.25). For quantum-inspired ML papers scoring 5.0–7.5, the anchors averaged 5.0–7.0 (QNF-Net 5.0, QPA 6.0, EQGNN 6.0, Trainability of VQLMs 7.0).

Calibrating against these anchors:
- **Identify Critical KV Cache** (5.75, reject): Stronger theoretical grounding (formal proof in main text) but less novel idea. QubitCache is more novel conceptually but has weaker validation and a significant unaddressed limitation. QubitCache is slightly weaker → below 5.75.
- **ChunkKV** (5.25, reject): Incremental chunk-level eviction idea. QubitCache has more novelty → above 5.25.
- **QPA - Quantum Circuit-Based Compression** (6.00, accept): Clean quantum-classical hybrid with good execution. QubitCache is more ambitious but has larger methodological concerns → below 6.00.
- **QNF-Net** (5.00, reject with split reviews): Had similar issues (quantum contribution unclear, heavy reliance on classical component). QubitCache has similar weaknesses but stronger empirical evaluation → roughly comparable.

Final position: between ChunkKV (5.25) and QNF-Net (5.00), slightly below Identify Critical KV Cache (5.75). The paper has genuine novelty and solid breadth of evaluation, but the disconnect between the ambitious framing and the modest 3.9% quantum contribution, combined with the unaddressed query-independence limitation and several missing experimental controls, places it below the acceptance bar.

**Final score: 5.0. Decision: Reject.**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>