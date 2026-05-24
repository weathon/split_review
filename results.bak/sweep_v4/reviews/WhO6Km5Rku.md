Now I have all the information needed to produce the final consolidated review.

---

## Summary

QubitCache proposes a paradigm shift for KV-cache compression: instead of binary token eviction, it preserves attention *relationships* by encoding non-critical token attention patterns into quantum amplitude states (9-qubit circuits per 512-token segment). Critical tokens (~15%) remain in classical storage, while non-critical tokens (~85%) are reconstructed probabilistically via quantum measurement and their values interpolated by inverse distance weighting. Experiments across 5 models and 6 benchmarks show 7× compression while retaining ~92-97% of Full-KV performance on many settings, with particular gains on multi-hop reasoning.

## Strengths

1. **Genuinely novel paradigm — relational preservation rather than token eviction.** The core insight that attention patterns carry essential information beyond token identity is well-motivated by prior work on attention sparsity. The ablation study (Table 4) cleanly demonstrates that attention-based critical-token selection is far more important than position-based heuristics: removing critical tokens drops F1 by 20.4%, while removing anchor or recent tokens degrades by only 0.6%.

2. **Broad and consistent evaluation.** Results span 5 model families (Llama-8B/70B, Mistral-7B, Qwen2-7B/30B, Phi-4-mini, DeepSeek-Coder-7B) and 6 benchmarks covering language modeling, reasoning, summarization, and code. Scaling results on 70B models further support general applicability.

3. **Detailed quantum circuit design with NISQ feasibility analysis.** The paper provides concrete circuit schematics (9 qubits, depth 15, ~750ns execution well within ~100μs coherence limits) and analyzes qubit count/ depth trade-offs. This provides a tangible pathway for future quantum hardware acceleration.

4. **Ablation study isolates each component's contribution.** Table 4 cleanly separates the contribution of attention-based selection (dominant), quantum encoding (modest but positive), and position-based heuristics (negligible) — enabling readers to understand what drives performance.

## Weaknesses

### Major

1. **Framing disconnect: the "beyond classical" compression claim is misleading.** The paper claims "logarithmic compression beyond classical information-theoretic limits" (abstract) and lists memory complexity as $O(0.15S \times D + \log N)$ (Table 3). In practice, the classical simulation stores 512 amplitude floats per 512-token segment — an $O(S)$ overhead, not $O(\log N)$. The actual 7× compression comes from retaining only 15% of KV pairs classically, which is a classical token-selection strategy. The quantum encoding merely reconstructs soft attention weights for the discarded 85%, adding only 3.9% relative F1 improvement (0.491 vs 0.472, Table 4). The rhetorical framing of a "quantum advantage" over classical methods is not supported by the implementation, which is entirely a classical simulation of a quantum circuit.

2. **Value reconstruction via inverse-distance weighting is unvalidated.** Non-critical token values are reconstructed by Eq. (6) using IDW between nearest preserved tokens. This assumes positional locality in *value space*, which is not justified — attention locality applies to attention *weights*, not value vectors. The paper provides no ablation on alternative interpolation schemes (nearest-neighbor copy, linear interpolation, learned projection), no reconstruction error analysis, and no evidence that this choice does not dominate the approximation error. Since this mechanism handles 85% of tokens, it could be the dominant source of information loss.

3. **No controlled compression-ratio comparison.** Baselines (H2O, ScissorHands) are evaluated at 2× compression while QubitCache operates at 7× compression (Table 1). The paper attributes QubitCache's higher absolute performance to better compression methodology, but the comparison is confounded: QubitCache retains a *different* set of tokens (attention-selected ~15% vs H2O's ~50%) and reports absolute F1, not per-compression-ratio curves. Without running H2O at matching 7× retention (15%) or reporting QubitCache at 2× retention (50%), the claimed advantage is unsubstantiated.

### Minor

4. **The "92-97% retention" claim does not hold universally.** For example, DeepSeek-Coder on PG19 achieves 0.156 vs Full KV's 0.193 (80.8% retention). The claim appears to be drawn from a subset of favorable model-benchmark combinations.

5. **Figure 3 uses an unspecified benchmark with inconsistent F1 values.** Panel (b) reports F1 scores around 0.83-0.84, which do not correspond to any benchmark in Table 1 (HotpotQA max 0.655). The axis labels are missing and the paper does not state which dataset or subset was used. This raises concerns about selective reporting.

6. **No statistical significance or variance reported.** All results in Tables 1 and 2 are point estimates without error bars, confidence intervals, or significance tests. Given the modest absolute differences in some comparisons (e.g., 0.510 vs 0.502 on Llama-8B HotpotQA), this matters.

### Trivial

7. **The "No Quantum" baseline in Table 4 is underspecified.** The paper states it "removes the quantum encoding" but does not specify what replaces it (discarding non-critical tokens entirely? uniform distribution?). Without this detail, the 3.9% quantum gain cannot be properly interpreted.

8. **Per-layer/head averaging** (Eq. 4) averages attention across all layers and heads into a single distribution used for all head computations. This is acknowledged but not analyzed. Given known variation in attention patterns across heads (Clark et al., 2019), an analysis of information loss would strengthen the paper.

## Nice-to-Haves

- Replace the quantum framing with a simpler classical probability vector (softmax over attention scores) to isolate whether the quantum formalism adds any value beyond the mathematical structure.
- Run reconstruction error analysis (e.g., cosine similarity between true and interpolated value vectors) to validate the IDW choice.
- Include a case study or attention heatmap comparing Full KV, H2O, and QubitCache attention patterns for the same input.

## Removed Points

- **"Structural: The quantum mechanism contributes negligibly"** — Retained and reframed as a major weakness above (Point 1), but softened: the original critic claimed "the quantum mechanism contributes negligibly" which overstates the case. The 3.9% gain is modest but not zero, and the critic's framing of "core gains come from attention-based token selection" is correct but the paper's paradigm claim is about *relational preservation*, not the quantum specifically. The weakness is that the *quantum* component is marginal, not that relational preservation itself is marginal. The ablation actually validates that attention-based selection (relational) is the key insight — the quantum encoding is just one specific instantiation of that insight.

- **"Strawman: missing related works"** — Removed per instructions (no external knowledge to confirm).

- **"Theoretical guarantee of bounded reconstruction error"** — Removed from strengths since the proof is deferred to the appendix (removed by parser). Neither confirmed nor denied.

- **"Formatting/style nitpicks"** from the harsh critic — Removed per hard rules.

- **Some strength finder generic strengths** ("addressed an important problem") — Removed as generic/superficial.

## Novel Insights

The reviews surface a tension that the paper does not fully resolve: the paradigm it proposes (relational preservation over token selection) is independently validated by its own ablation (attention-based selection is critical), but the specific quantum mechanism for achieving it contributes only 3.9%. This suggests the paper's genuine contribution is more about *what to compress* (attention relationships) than *how to compress* (quantum encoding). A useful path forward would be to disentangle these: a classical version that stores attention probability distributions explicitly (which requires O(segment size) memory, not O(log N)) could test whether the quantum formalism provides any practical benefit beyond mathematical convenience. The reviewers' shared concern about the value interpolation scheme (IDW without validation) identifies the most likely weak link in the pipeline.

## Suggestions

1. **Conduct controlled compression-ratio experiments.** Run H2O, ScissorHands, and StreamingLLM at the same 7× compression (15% retention) as QubitCache. Without this, performance advantages are confounded with different retention strategies.

2. **Ablate the value interpolation scheme.** Compare IDW against nearest-neighbor copy, linear interpolation, and a learned projection to validate the choice. Report reconstruction error (cosine similarity / MSE) between true and interpolated value vectors.

3. **Replace the quantum encoding with a classical probability vector** (softmax over attention scores for each segment) and compare. This would isolate whether the quantum formalism provides any practical advantage over storing attention probabilities directly.

4. **Specify what the "No Quantum" ablation actually does.** Describe what replaces the quantum encoding (e.g., uniform attention distribution over non-critical tokens? discarding them?) and justify the comparison.

5. **Report all results with variance** (at least 3 runs) and clearly label which benchmark Figure 3's ablation refers to.

6. **Tone down the "beyond classical limits" framing.** The paper's actual contribution — attention-driven token selection with soft reconstruction — is interesting on its own merits and does not require quantum hyperbole.

## Score and Decision

### Calibration Anchors

| Anchor Paper | Avg Score | Comparison |
|---|---|---|
| `IntelLLM` (4QWPCTLq20) | 3.00 | Much weaker evaluation (2 models, no ablation on components), unclear contribution. QubitCache has more novelty and broader evaluation, placing it above this. |
| `Don't Discard/MiKV` (CRQ8JuQDEd) | 5.00 | Cleaner execution (mixed-precision quantization) but incremental contribution. QubitCache is more novel but less rigorous. |
| `KV-Dict` (FkXYvV7nEB) | 5.25 | Solid dictionary-learning approach with thorough experiments. QubitCache comparable breadth but has more unsupported claims. |
| `Identify Critical KV` (lRTDMGYCpy) | 5.75 | Well-motivated theory with perturbation analysis. QubitCache has a more ambitious paradigm shift but weaker verification of core claims. |
| `FlexPrefill` (OfjIlbelrT) | 8.00 | Clean, well-evaluated sparse attention mechanism with clear contributions. QubitCache substantially less rigorous. |

**Decision Rationale:** QubitCache introduces a genuinely novel paradigm shift (relational preservation > token selection), and the broad evaluation across models/benchmarks and detailed circuit design are strengths. However, the paper overclaims its quantum advantage — the compression comes from keeping 15% of tokens, not from quantum encoding, and the quantum component contributes only 3.9% F1 improvement. The value interpolation mechanism (covering 85% of tokens) is unvalidated. The experimental comparison is confounded by unmatched compression ratios. These issues collectively prevent acceptance at ICLR, though the core insight has merit and could form the basis of a stronger submission with more rigorous evaluation.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>