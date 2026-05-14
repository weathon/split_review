Now I have all the information I need. Let me compile the final review.

---

## Summary
This paper proposes QubitCache, a KV-cache compression method for LLM inference that frames compression as preserving attention-relationship patterns rather than retaining individual tokens. The method keeps ~15% of tokens classically (anchor, recent, and attention-based critical tokens) and encodes the attention distribution of the remaining 85% into a 9-qubit amplitude-encoded quantum state. During inference, soft attention weights derived from quantum state measurements are applied to interpolated neighbor value vectors. The paper evaluates on 5 models and 7 benchmarks, reporting 7× compression with 92–97% of full-cache performance.

## Strengths
- **Novel conceptual framing:** The shift from "which tokens to keep" to "how to preserve relational structure" is well-motivated by attention sparsity literature and provides a fresh perspective on KV-cache compression. The idea that soft attention over evicted tokens is better than binary discard is intuitively appealing and empirically sensible.

- **Comprehensive model coverage:** Evaluation across five models (Llama-3-8B, Mistral-7B, Phi-4-mini, Qwen2-7B, DeepSeek-Coder-7B) and scaling to Llama-70B/Qwen-30B demonstrates that the method works across diverse architectures, not just a single model.

- **Informative ablation study (Table 4):** The ablation cleanly isolates contributions: removing attention-based critical token selection causes a 20.4% drop, while removing the quantum encoding causes only a 3.9% drop. The random-selection baselines (with and without quantum encoding) convincingly show that attention-guided selection — not the quantum component — is the primary driver of performance. This is an honest and useful analysis.

- **Qualitative error analysis (Table 9, Appendix A.5):** The side-by-side generation examples with error-type categorization provide a concrete sense of how the method differs from baselines in practice, showing QubitCache avoids the catastrophic hallucinations that plague StreamingLLM and H2O on the shown examples.

## Weaknesses

### Major
- **Unsubstantiated proof claim in the abstract:** The abstract states "We prove QubitCache preserves rank r attention structure with bounded reconstruction error." The main body (and available appendix material) contains no theorem statement, proof sketch, or formal analysis of this claim. A claim of theoretical guarantees in the abstract that is never delivered in the paper is a serious credibility issue.

- **Compression ratios not matched across methods (Table 1–3):** QubitCache is evaluated at 7× compression (15% retention), while H2O, ScissorHand, and StreamingLLM are configured at 2× compression (50% retention). The paper's headline claim of "15–25% higher F1 scores … despite using 3.3× more aggressive compression" therefore rests on an asymmetric comparison. The baselines could plausibly be pushed to 7×, and their performance would degrade — but without that comparison, the claimed superiority at matched budgets is unsupported. The paper would need either matched-compression-ratio comparisons or compression-vs-performance curves for all methods to substantiate this claim. GEAR at 6.7× is closer but still not matched, and GEAR's own paper reports 2.39× as its primary result, raising questions about the 6.7× configuration.

- **Quantum framing is largely cosmetic relative to the actual contribution:** The core mechanism — store a probability distribution over evicted token indices, use it as soft attention weights on interpolated neighbor values — is entirely classical in both concept and implementation (the paper acknowledges classical simulation in Section 3.2). The "logarithmic compression beyond classical information-theoretic limits" claim in the abstract is misleading: the information encoded (attention weights) is classical, and a classical system could store the same distribution with at most 512 floats or a low-precision vector. The quantum formalism provides a mathematical framework but does not deliver a genuine quantum advantage in the presented system. The paper would be stronger — and more honest — if it presented the method as an attention-pattern-preserving compression framework and relegated the quantum encoding to an interesting theoretical connection rather than the central contribution.

### Minor
- **Table 4 lacks dataset/model specification:** The ablation study reports a baseline F1 of 0.491 for Full QubitCache without stating which model, dataset, or task this score comes from. Without this context, it is unclear whether the 3.9% quantum contribution generalizes or is task-specific.

- **No latency or throughput measurements:** The paper reports memory consumption (Table 3) but provides no timing results for the classical simulation of quantum circuits. Since the method uses Qiskit statevector simulation, the per-token inference overhead of computing quantum state measurements could be substantial and is relevant for practical deployment.

- **The "No Quantum" ablation needs more detail:** The 3.9% drop when removing quantum encoding (Table 4) is the best evidence that the quantum component adds value beyond the classical token-selection heuristic. However, the paper does not describe what "No Quantum" replaces the quantum encoding with — e.g., uniform weights, zero weights, or a classical probability vector. Clarifying this would strengthen the ablation's interpretability.

### Trivial
- The abstract's claim of "logarithmic compression beyond classical information-theoretic limits" is technically inaccurate: amplitude encoding maps N values to log₂(N) qubits, but the information content of the distribution is unchanged. The phrasing should be softened or removed.

## Nice-to-Haves
- It would strengthen the paper considerably to include a purely classical baseline that stores the attention distribution explicitly (e.g., a 512-float probability vector or a top-k sparse version) with the same interpolation scheme, to isolate whether the quantum formalism adds anything beyond the soft-attention idea itself.
- Compression-vs-performance curves for all methods would make the comparison fair and informative across the full range of memory budgets.

## Removed Points
These points are flagged to be removed — treat them with caution.

- **Harsh Critic — "The paper does not include evaluation of any method at the same compression ratio, nor does it present compression‑vs‑performance curves"**: KEPT in modified form as a Major weakness. The core concern is valid, but the paper does include GEAR at 6.7× compression, so it's not true that *no* method is evaluated at comparable compression. The issue is that the primary baselines (H2O, ScissorHand, StreamingLLM) are at 2×, and this is the correct critique to emphasize.

- **Harsh Critic — "NISQ compatibility serves no practical purpose"**: REMOVED. The paper explicitly states the implementation is a classical simulation and discusses NISQ as a future direction, not as a present contribution.

- **Harsh Critic — "Figure 3 / quantum parameter discussion is irrelevant"**: REMOVED. This analysis shows how qubit count and circuit depth affect performance, which is informative for understanding the encoding's behavior. It's not irrelevant, just forward-looking.

- **Harsh Critic — "The information content of that distribution is exactly the normalized attention weights" and the compression claim is false**: PARTIALLY KEPT as a Major weakness but reframed. The core insight that the quantum formalism doesn't provide a genuine compression advantage is valid and important. However, the paper does acknowledge classical simulation, so the issue is about overclaiming rather than false claims.

- **Strength Finder — "Theoretical guarantee of bounded reconstruction error"**: REMOVED. This is not a strength because the proof does not appear anywhere in the paper.

- **Strength Finder — "Practical quantum-circuit design validated for current NISQ constraints"**: REMOVED. The implementation is entirely classically simulated; NISQ compatibility is aspirational, not demonstrated.

- **Strength Finder — "Detailed qualitative error analysis showing robustness"**: WEAKENED. The error analysis covers only 3 examples (Table 9) — insufficient to draw reliable conclusions about hallucination rates, but the examples are illustrative and useful.

- **Strength Finder — "Seamless integration into autoregressive generation with efficient update strategies"**: REMOVED as a standalone strength. This is a design description, not an empirically validated strength.

- **Strength Finder — "Paradigm shift" language**: REMOVED. The conceptual framing is interesting but calling it a "paradigm shift" is marketing, not a strength.

## Novel Insights
None beyond the paper's own contributions. The reviews did not surface a genuinely new observation about KV-cache compression or quantum-inspired methods that the paper itself does not already contain.

## Suggestions
- Reframe the paper around "soft attention preservation for KV-cache compression" rather than quantum-inspired encoding. The core idea is strong and does not need quantum terminology to be interesting. Present the amplitude encoding as one possible implementation of storing attention distributions compactly, and compare against classical alternatives (sparse top-k, low-precision vector, etc.).
- Either provide the proof of the rank-r preservation claim (at minimum a sketch in the main body) or remove the claim from the abstract and introduction entirely.
- Re-run baseline comparisons with matched compression ratios, or present full compression-vs-performance curves for all methods. This is the single most impactful improvement to the paper's empirical credibility.
- Add latency/throughput measurements for the classical simulation to give readers a realistic sense of deployment feasibility.

## Score and Decision

**Anchor comparisons:**

| Anchor | Avg Score | Decision | Comparison to paper under review |
|---|---|---|---|
| KVTC (`aNVKROYpLB`) | 5.50 | Accept (Poster) | KVTC has honest claims, thorough matched evaluation, clear practical value. This paper's idea is comparably interesting but the evaluation is weaker (unmatched compression ratios) and the framing overclaims. |
| Sublinear Time Quantum Algorithm (`0zIcPe4CtY`) | 5.50 | Accept (Poster) | Rigorous theoretical quantum algorithm with full proofs. This paper claims a proof it never delivers; substantially weaker on theoretical rigor. |
| Pitfalls of KV Cache Compression (`dDgoYv2f7Q`) | 4.00 | Withdrawn/Reject | Similar tier: identifies an important problem with useful experiments but has methodological limitations. This paper has more comprehensive experiments across more models/benchmarks. |
| CompressKV (`Eed6XsFNJ5`) | 3.50 | Withdrawn/Reject | Both have interesting ideas with evaluation gaps. CompressKV has better-matched comparisons; this paper has wider model coverage but more overclaiming. |
| VQKV (`YyxvRDh4d4`) | 2.50 | Withdrawn/Reject | VQKV has limited novelty and no efficiency evaluation. This paper has a clearer novel idea (soft attention vs binary eviction) and more comprehensive experiments. |
| Quantum Attention (`i75XGv8oqj`) | 2.00 | Withdrawn/Reject | Quantum Attention is a shallow theoretical exercise with no experiments. This paper has substantial empirical work and a practical method, even if the quantum framing is overclaimed. |

The paper sits between the 3.50–4.00 range. The core idea (soft attention over evicted tokens) is genuinely interesting and well-motivated. The experimental coverage across 5 models and 7 benchmarks is impressive. However, three issues prevent a higher score: (1) the abstract claims a proof that is nowhere in the paper, (2) the headline empirical comparison uses unmatched compression ratios, and (3) the quantum framing overclaims relative to the actual contribution. These are addressable but substantial issues. The paper is better than the 2.0–3.0 tier (shallow quantum papers, limited novelty) but falls short of the 5.0+ tier (rigorous evaluation, honest claims, clear practical value).

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>