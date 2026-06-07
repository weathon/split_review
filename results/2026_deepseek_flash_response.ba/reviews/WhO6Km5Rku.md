## Summary

QubitCache proposes a KV-cache compression method that combines attention-guided token selection (retaining ~15% of tokens classically) with a quantum-inspired amplitude encoding of attention patterns for non-critical tokens, which are reconstructed probabilistically during inference. The system achieves 7× compression and shows competitive performance across 5 models and 7 benchmarks compared to prior compression methods operating at lower (2×) compression ratios.

## Strengths

- **Comprehensive evaluation across diverse models and tasks.** Table 1 reports results across 5 models (Llama-8B, Mistral-7B, Qwen2-7B, Phi-4-mini, DeepSeek-Coder-7B) and 7 benchmarks spanning reasoning, summarization, QA, and language modeling. This breadth exceeds most prior KV-cache compression papers and provides a solid empirical basis for assessing the method.

- **Informative ablation isolating attention-based token selection (Table 4).** Removing attention-selected critical tokens causes a 20.4% F1 drop (0.491→0.391), while removing anchor/recent tokens causes only 0.6% drops each. Random token selection with quantum encoding achieves only 68.2% of QubitCache's performance (0.335 vs 0.491). This cleanly validates that attention-guided token selection, not position heuristics, drives the core performance.

- **Transparent scoping of quantum implementation.** The paper explicitly states (line 100) that "the current implementation operates as a classical simulation," avoiding overclaiming a hardware quantum advantage.

## Weaknesses

### Major

1. **Headline performance retention claim is factually contradicted by the paper's own data.** The abstract, introduction, and conclusion repeatedly state QubitCache "maintains 92-97% of baseline performance" (abstract, §1, line 178, §5). Computing FullKV-to-QubitCache ratios from Table 1 reveals multiple entries well below this range: DeepSeek-Coder HotpotQA (75.5%), DeepSeek-Coder SummScreen (75.9%), Mistral-7B HotpotQA (81.1%), DeepSeek-Coder PG19 (80.8%), Phi-4-mini SummScreen (82.4%), Llama-8B TriviaQA (84.9%), Phi-4-mini PIQA (90.9%), and others. This is not a minor imprecision — the paper asserts a narrow 92-97% range that does not hold for roughly a third of the individual model–benchmark entries. A central quantitative claim repeated four times is demonstrably false.

2. **PG19 benchmark uses an undefined, non-standard metric.** PG19 is a language modeling benchmark where the accepted metric is perplexity. Table 1 reports "PG19 F1(↑)" without any definition of what this F1 score measures (token-level exact match? some generative metric?). The paper's dramatic comparisons (e.g., "retaining 97.6% performance on PG19... compared to ScissorHand's 37.1%") cannot be evaluated without knowing the metric. This makes the PG19 results uninterpretable and potentially invalid.

3. **No inference latency or throughput measurements.** The paper claims "minimal latency overhead" (line 216) but provides zero runtime data. For a KV-cache compression method that replaces simple attention lookup with Qiskit circuit simulation, controlled-RY gate sequences, and per-token value interpolation via inverse distance weighting, inference speed is a first-order concern. A method that halves memory but multiplies latency is not practically useful. The complete absence of timing data is a serious omission for a paper claiming practical feasibility.

4. **Unresolved inconsistency in the qubit-count ablation (Figure 3a).** Figure 3a shows F1 monotonically increasing from 4 qubits (encoding 2^4=16 tokens) to 15 qubits (encoding 2^15=32,768 tokens). However, the paper's segment size is fixed at 512 tokens, which requires exactly 9 qubits. How a 15-qubit encoding maps onto a segment of 512 tokens is unexplained. If segment size varies with qubit count, the comparison is confounded; if not, the experiment is incoherent. The claim that the 9-qubit configuration "retains 94% of the 15-qubit performance" lacks a clear basis.

5. **Memory complexity claim for the quantum component is misleading.** The paper claims O(log N) memory for the quantum encoding (line 60, Table 3: "+ log N"). In the classical simulation that is actually run, each 9-qubit state stores or computes 2^9=512 complex amplitudes. With N/512 segments, the total is O(N) amplitudes, not O(log N). While the practical 7× compression comes from the 15% classical token retention (the O(0.15S) term is the dominant term), the O(log N) claim as stated is incorrect for the implemented system.

### Minor

1. **No statistical variance reported.** All results in Tables 1, 2, and 4 are single point estimates with no standard errors or confidence intervals. For a method involving probabilistic sampling from a measurement distribution, run-to-run variance could be non-negligible.

2. **Adaptive shot allocation is unspecified.** The paper mentions "adaptive shot allocation" as an optimization (line 132) but gives no details on how many measurements are needed per quantum segment or what the computational cost is.

3. **Initial full-attention cost is unaccounted for.** Identifying critical tokens via accumulated attention scores (§3.1) requires computing attention over the full sequence first (O(N²) cost). The paper discusses the amortized O(log n) per-token update cost during generation but does not account for this initial encoding overhead.

4. **Attention averaging across all heads discards head-specific patterns.** Equation 4 averages attention scores across all L×H heads. Individual attention heads capture functionally distinct patterns (Clark et al., 2019; Michel et al., 2019); this design choice is not ablated.

### Trivial

None.

## Nice-to-Haves

- Comparing baselines (H2O, ScissorHands) at the same 15% retention ratio would more cleanly isolate the contribution of the quantum encoding versus the pure selection + interpolation scheme.

## Removed Points

These points were removed after verification against the paper text. Treat them with caution:

- **"Quantum encoding provides no compression advantage (Holevo bound, measurement overhead)"** — The critic's quantum information analysis applies to a hypothetical hardware implementation, not the classical simulation the paper actually runs. The paper transparently states it uses classical simulation. The practical compression benefit is from the 15% token retention, which is valid irrespective of quantum information theory.
- **"Evaluation compares at different compression ratios making it uninformative"** — This criticism is directionally reversed: QubitCache operates at a higher (more aggressive) compression ratio (7× vs 2×). Outperforming baselines while using less memory is a stronger result, not a weaker one.
- **"Missing baselines (KIVI, KVT, attention-sink-only)"** — Scope creep; the paper includes 5 baselines covering the main sparsity-based and quantization-based approaches.
- **"Circuit depth: 'never addresses' O(2^n) gate requirement"** — Factually wrong: the paper acknowledges this in §2 (line 40: "arbitrary state preparation requires O(2^n) gates in the general case").
- **"GovReport is insensitive to compression"** — Speculation without evidence.
- **"Value interpolation is standard / unrelated to quantum"** — Not a weakness; IDW is part of the hybrid pipeline.
- **"Rank r theorem proof deferred to appendix"** — The appendix was stripped by the parser; cannot be evaluated.
- **"Missing related works"** — Cannot be verified without external sources.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Correct the performance retention claim** to honestly reflect the per-task range in Table 1 (roughly 75–99% depending on model and task, not 92–97%).
2. **Define the PG19 metric** (what does "F1" measure in this context?) or replace with standard perplexity.
3. **Report wall-clock latency or tokens-per-second** for at least one representative model and sequence length.
4. **Explain the qubit-count ablation (Figure 3a):** specify what segment size corresponds to each qubit count, or clarify why 15 qubits is meaningful with 512-token segments.
5. **Correct the memory complexity claim** to honestly characterize the classical simulation's storage requirements.
6. **Add variance estimates** (standard errors or confidence intervals) across multiple runs.

## Score and Decision

### Calibration Anchor Report

| Paper | Path | Avg Score | Round | Comparison to this paper |
|-------|------|-----------|-------|-------------------------|
| IntelLLM (KV cache, 3.0) | 4QWPCTLq20.md | 3.00 | R1 | Weaker evaluation (2 models × LongBench only) but no factual errors in claims. This paper has broader experiments but more serious integrity issues. |
| MixAttention (KV cache, 2.0) | 2DD4AXOAZ8.md | 2.00 | R1 | Much weaker overall. |
| PrefixQuant (KV cache, 3.0) | vw0NurJ7UX.md | 3.00 | R1 | Different approach (quantization). Comparable score level. |
| Quantum Circuit Compression (6.0) | bB0OKNpznp.md | 6.00 | R1 | Significantly stronger: cleaner claims, accepted at top venue. This paper is well below this level. |
| Quantum Entanglement Attention (4.5) | 3jRzJVf3OQ.md | 4.50 | R1 | Cleaner small-scale study without factual errors. This paper is worse due to integrity issues. |
| LSH-E (KV cache, 3.83) | 0ZcQhdyI3n.md | 3.83 | R2 | Similar scope, also missing latency data. LSH-E has weaker baselines but no factual errors in central claims. This paper is slightly worse. |
| KV-Distill (KV cache, 4.0) | p7vJ3wsm34.md | 4.00 | R2 | Training-based approach with clean claims. This paper is worse. |

### Score Rationale

The paper has genuine empirical breadth (5 models × 7 benchmarks) and an informative ablation study confirming the importance of attention-guided token selection. These are non-trivial contributions. However, three issues combine to prevent acceptance at a top venue: (a) the central 92–97% performance retention claim is factually contradicted by the paper's own Table 1 (some entries are as low as 75%), repeated four times across abstract, introduction, results, and conclusion; (b) the PG19 metric is undefined, making a significant portion of results uninterpretable; and (c) no latency measurements are provided despite the method involving Qiskit circuit simulation. The O(log N) memory complexity claim is also misleading for the classical simulation actually performed. The score of 3.5 places this paper below typical acceptance thresholds (which at ICLR require at least 5–6) and below comparable rejected papers in the calibration set that do not have factual errors in their central claims.

**Round-1 bracket:** 2.0–6.0 (after comparing weak anchors at 3.0 and mid anchors at 4.5–6.0).

**Round-2 narrowing:** Reading LSH-E (3.83) and KV-Distill (4.0) confirmed this paper belongs below both due to the factual error in the central performance claim and undefined PG19 metric, which are more serious integrity issues than the missing baselines/missing timing common to these anchor papers.

**Final score:** 3.5.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>