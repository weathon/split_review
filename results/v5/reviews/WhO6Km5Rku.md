Now I have sufficient calibration context. Let me write the final consolidated review.

**Calibration anchors considered:**

| Anchor | Avg Score | Round | Query Bucket | Comparison |
|--------|-----------|-------|--------------|------------|
| LSH-E (0ZcQhdyI3n) | 3.83 | R1-topic-mid | KV cache compression | Similar issues (missing runtime, missing baselines at same ratios) but QubitCache has broader experiments AND more severe overclaiming |
| ChunkKV (8sglLco8Ti) | 5.25 | R1-topic-mid | KV cache compression | More thorough evaluation, fewer problematic claims. QubitCache is weaker |
| Identify Critical KV (lRTDMGYCpy) | 5.75 | R1-topic-mid | KV cache compression | Stronger theoretical grounding. QubitCache is significantly weaker |
| MiKV (CRQ8JuQDEd) | 5.00 | R2 | limited baselines missing runtime | Similar mixed-preservation idea but better executed. QubitCache has more issues |
| KVTQ (eZAlb8fX5y) | 4.40 | R2 | KV cache quantization | Fewer issues than QubitCache but still rejected for missing runtime/novelty concerns |
| DynamicKV (uHkfU4TaPh) | 4.40 | R2 | limited baselines | Better executed within scope. QubitCache is weaker |
| LSH weak (2DD4AXOAZ8) | 2.00 | R1-topic-low | KV cache | MixAttention paper, not as relevant |
| IntelLLM (4QWPCTLq20) | 3.00 | R1-topic-low | KV cache | More limited evaluation. QubitCache is better in breadth |

**Round 1 bracket:** 3.5–5.5 (between LSH-E and ChunkKV levels)

**Round 2 narrowing:** Within (2.5, 5.5), found KVTQ (4.40), MiKV (5.00), DynamicKV (4.40). QubitCache has more major issues than these papers, placing it below KVTQ at ~4.0.

**What the low-band anchors (≤4.0) failed at:** Missing runtime measurements, limited baseline comparisons, missing ablation studies, insufficient benchmark coverage, unclear contributions. QubitCache shares the missing runtime and comparison issues, and adds quantum overclaiming and ablation-contradiction problems.

## Final Review

## Summary

This paper proposes QubitCache, a KV-cache compression method that retains 15% of tokens in classical storage while encoding the attention distributions of the remaining 85% into quantum-inspired amplitude representations (9 qubits per 512-token segment). The encoded distributions are used during inference to weight interpolated value vectors for a "soft attention" reconstruction of compressed tokens. The paper claims 7× compression with 92–97% performance retention and 15–25% higher F1 on multi-hop reasoning tasks.

## Strengths

1. **Empirical validation that attention-based token selection is crucial.** The ablation study (Table 4) convincingly demonstrates that removing tokens selected by accumulated attention scores causes a catastrophic 20.4% F1 drop, while removing position-based tokens (anchor/recent) costs only 0.6%. The random-selection baselines further confirm the importance of attention-aware selection. This is the paper's most solid empirical finding.

2. **Broad evaluation across models and benchmarks.** The paper evaluates five models (Mistral-7B, Qwen2-7B, Phi-4-mini, DeepSeek-Coder, Llama-8B) on seven benchmarks, plus a scaling study on Llama-70B and Qwen-30B. This breadth is commendable and exceeds what many KV-cache compression papers provide.

3. **Competitive performance against GEAR at similar compression.** Against GEAR (6.7×), QubitCache (7×) shows modest but consistent improvements (e.g., 5–14% relative F1 improvement on HotpotQA across models). This suggests the underlying approach of attention-guided soft reconstruction has genuine merit.

4. **The hybrid preservation idea is worth exploring.** Separating the problem into (a) selecting which tokens to retain and (b) preserving the attention distribution of discarded tokens is a reasonable conceptual framing that could be pursued with or without the quantum formalism.

## Weaknesses

### Major

1. **Headline performance claims are based on an apples-to-oranges comparison.** The paper's central claim of "15–25% higher F1 scores on multi-hop reasoning tasks" compares QubitCache at 7× compression (15% token retention) against H2O, ScissorHand, and StreamingLLM at 2× compression (50% retention). Against GEAR, the only baseline at a comparable compression ratio (6.7×), the advantage shrinks to 2–14% relative across models. The paper is transparent about the different ratios, but the headline framing is misleading nonetheless. A proper evaluation would compare all methods at multiple matched compression ratios (2×, 4×, 7×). The current presentation inflates the method's apparent advantage.

2. **Quantum encoding provides no practical compression benefit in the classical simulation, yet it is framed as the core innovation.** The paper implements QubitCache as a classical simulation. Storing the amplitudes of a 9-qubit state requires 2⁹ = 512 floating-point numbers — exactly the same memory as storing the normalized attention distribution directly as a classical probability vector. The "logarithmic compression beyond classical information-theoretic limits" claimed in the abstract is only realizable on actual quantum hardware. In the present implementation, the quantum formalism adds state-preparation and measurement-simulation overhead with zero compression benefit. The paper would be equivalent — and more honest — if it simply stored normalized attention weights.

3. **The ablation study contradicts the paper's narrative that quantum encoding is the paradigm shift.** Table 4 shows that Full QubitCache achieves 0.491 F1 while "No Quantum" (simply discarding non-critical tokens without attention-pattern preservation) achieves 0.472 — a 3.9% relative improvement. Meanwhile, removing attention-selected critical tokens ("No Critical") causes a 20.4% drop. The dominant factor is attention-based token selection, a heuristic well-explored in prior work (H2O's heavy-hitters, ScissorHand's pivotal tokens). The quantum component adds a small, not transformative, benefit. The paper's abstract, introduction, and conclusion nevertheless frame quantum encoding as the central contribution. This mismatch between evidence and narrative is significant.

4. **No runtime or throughput measurements.** The paper claims "minimal latency overhead" but provides zero empirical measurements of wall-clock time, tokens-per-second, or end-to-end latency. For a compression method that adds per-segment amplitude encoding, measurement simulation, and value interpolation, the computational cost is not obvious. The amortized O(log n) update cost is claimed but never verified. Without any runtime data, the practical applicability of the method is unsubstantiated.

### Minor

1. **No error bars or statistical significance.** All results in Tables 1, 2, and 4 are point estimates. Given that results vary across models and random seeds, confidence intervals or standard deviations would help assess reliability.

2. **No discussion of FlashAttention compatibility.** QubitCache needs the raw attention weight matrix (A = softmax(QK^T/√d)) to construct the quantum state. FlashAttention and related I/O-aware kernels do not materialize this matrix; they compute attention outputs without storing the full N×N attention weights. This creates a practical tension the paper does not address.

3. **Computational overhead of encoding is not quantified.** Constructing the amplitude-encoded quantum state requires controlled-RY rotations applied hierarchically. The paper states this cost amortizes to O(log n) per token, but the constant factors and actual GPU time for the Qiskit-based simulation are never reported. For 2K–8K sequences this may be tolerable; for the 100K-token use cases that motivate the work, the overhead could be prohibitive.

4. **Value interpolation assumption may fail for long-range dependencies.** Equation (6) uses inverse-distance weighting based on two nearest preserved neighbors. This assumes locality of semantic influence, which is reasonable for local context but questionable for the long-range cross-token dependencies that multi-hop reasoning tasks depend on. No analysis is provided for when this interpolation breaks down.

5. **"First to recognize attention patterns as primary information carrier" is overstated.** The paper cites Abnar & Zuidema (2020), Michel et al. (2019), and others who have previously argued that attention structure encodes essential information. The novelty lies in a specific encoding mechanism, not the recognition itself.

6. **NISQ feasibility claim is speculative.** The paper states the 9-qubit circuit operates "within coherence constraints of current NISQ devices" (Section 4.5.2), yet all experiments are classical simulations without noise models. While not requiring actual hardware experiments, the claim should be caveated as theoretical.

## Removed Points

- **Point about O(N²) computation being "the very bottleneck the paper purports to avoid":** The paper frames *memory* growth (122GB for 70B at 100K tokens), not O(N²) compute, as the bottleneck. Computing the attention matrix during prefill is standard in all transformers, not an additional cost unique to QubitCache. However, the paper should still quantify encoding overhead — kept as Minor weakness #3 instead.

- **Point about "no experiments on actual quantum hardware or with realistic noise models":** Requiring quantum hardware execution is an impractical standard for a methods paper. The classical simulation and theoretical coherence analysis are reasonable for this venue. Removed as too stringent.

- **Point about missing appendix content:** The parser strips appendix sections from all papers; these exist in the original submission. Removed per policy.

## Nice-to-Haves

- Compare all baselines at matched compression ratios (2×, 4×, 7×) to cleanly assess whether QubitCache's soft reconstruction adds value at any given ratio.
- Include a control that stores the normalized attention distribution as a classical probability vector (no quantum simulation) to demonstrate whether the quantum formalism provides any benefit beyond what a simple array achieves.
- Report latency and throughput measurements for all methods.
- Test on longer sequences (e.g., 16K–32K from LongBench) to demonstrate scalability.
- Provide error bars (standard deviation over multiple seeds) for all experimental results.
- Analyze failure cases where the inverse-distance value interpolation assumption is violated.

## Novel Insights

None beyond the paper's own contributions. The finding that attention-based token selection dominates performance (from the ablation) is consistent with existing KV-cache compression literature.

## Suggestions

1. **Foreground the attention-selection mechanism, not the quantum encoding.** The paper's strongest evidence is that attention-guided token selection works. Reframe the contribution around the hybrid selection-plus-reconstruction pipeline, with the quantum encoding presented as a possible future hardware pathway rather than the current innovation.
2. **Report runtime at multiple sequence lengths** to establish the practical tradeoff between memory savings and compute overhead.
3. **Add a classical-probability-vector baseline** ("No Quantum, Store Attention Distribution") to the ablation. If it matches QubitCache's performance, the quantum simulation is unnecessary; if it doesn't, explain why amplitude encoding matters.
4. **Test all baselines at 2×, 4×, and 7× compression** and present results side-by-side. This single change would resolve the most damaging criticism.

## Score and Decision

Based on the calibration evidence: this paper sits between LSH-E (3.83) and KVTQ (4.40) in the quality landscape — papers with similarly significant evaluation gaps that were rejected. Three major weaknesses (comparison framing, decorative quantum encoding, ablation-narrative mismatch) collectively undermine the core claim, and per the fundamental-issues rule, the score cannot exceed 4.5. The paper has genuine empirical breadth and an interesting conceptual seed, but the evaluation as structured does not support the claimed contributions, and the quantum framing misrepresents where the actual performance gains come from.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>