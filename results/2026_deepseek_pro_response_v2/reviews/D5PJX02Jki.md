I now have a complete calibration picture. Let me finalize the review.

**Calibration Summary:**

**Round 1 Anchors (bracketing):**
- `jp4pxKqCRW` (2.50): Long-context extrapolation via periodic extension — Reject, much weaker
- `5dDYhvt6dY` (3.00): Efficient transformer with reinforced PE — Reject, weaker
- `GtvuNrk58a` (6.20): "Round and Round We Go" (RoPE internals) — Accept, deep analysis but single model, mostly perplexity
- `JO7k0SJ5V6` (5.00): "Scaling Laws of RoPE-based Extrapolation" — Accept, good theory but only perplexity eval
- `EytBpUGB1Z` (8.00): "Retrieval Head" — Accept, exceptional across 4 model families, 6 scales
- `OvoCm1gGhN` (8.00): "Differential Transformer" — Accept, more novel architecture

**Round 1 Bracket: 6.0 – 7.5**

**Round 2 Anchors (narrowing):**
- `eoln5WgrPx` (6.50): STRING — Accept, training-free, 70B models but heuristic; RoPE++ has cleaner theory
- `rR03qFesqk` (6.67): FIRE — Accept, learned PE, thorough but ad-hoc and slower; RoPE++ more efficient
- `q2Lnyegkr8` (6.75): Forgetting Transformer — Accept, more novel architecture but similar model scale

RoPE++ compares favorably to STRING (cleaner math, causal experiments) and FIRE (more efficient, cleaner design). It's slightly below Forgetting Transformer in architectural novelty. Score: **6.5**.

---

## Summary
This paper proposes RoPE++, which re-incorporates the imaginary component of the complex-valued attention score from RoPE as an additional group of attention heads. The key technical observation is that the imaginary attention can be computed as standard RoPE applied to query vectors rotated by -π/2, requiring minimal code changes while inheriting RoPE's compatibility with FlashAttention. Two configurations are proposed: RoPE++_EC (doubled heads, equal KV cache) and RoPE++_EH (equal heads, halved KV cache and QKV parameters). Evaluated at 376M and 776M model scales with 50B-token pre-training, RoPE++ variants outperform standard RoPE and other position embeddings on both short-context and long-context benchmarks, with gains widening as context length increases.

## Strengths
- **Clean mathematical derivation linking imaginary and real attention (Section 3.1, Eqs 2-4):** The paper shows that the negative imaginary part of the complex attention can be expressed as standard RoPE applied to a -π/2-rotated query, meaning it inherits all key RoPE properties without architectural changes. This derivation is rigorous and directly enables the practical implementation.
- **Well-designed noise-perturbation causal experiment (Section 5.2):** Adding matched Gaussian noise to imaginary vs. real attention components and measuring RULER-4k degradation provides direct causal evidence that imaginary heads play a dominant role in long-context performance (5-8 point gap at σ=1.0), ruling out the hypothesis that gains come merely from increased capacity.
- **Consistent empirical gains across model sizes, context lengths, and extension methods (Tables 1-3):** RoPE++_EC consistently achieves the best average scores across short-context and long-context benchmarks at both 376M and 776M scales. Gains on long-context tasks grow with context length (e.g., BABILong at 776M: RoPE++_EC 24.1 vs RoPE 22.8 average). The advantage persists when combined with PI and YaRN (Table 3).
- **Practical dual-configuration design with clear efficiency-performance trade-off (Section 3.3, Figure 4):** RoPE++_EH achieves comparable or better performance to standard RoPE with half the KV cache and QKV parameters, with memory/throughput advantages that widen with context length. This is a concrete engineering contribution.
- **Attention-pattern visualizations corroborating the global-vs-local theory (Figure 5):** Imaginary heads consistently attend more to initial/global positions while real heads focus on local context, aligning with the characteristic-curve prediction and the noise-perturbation results, forming a coherent narrative across theory, visualization, and causal intervention.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **"Discarded information" framing is potentially misleading (Section 3.1, Introduction, Abstract):** The paper frames standard RoPE as "discarding" imaginary information. In the real-vector formulation of RoPE (q^T R_Θ k), the rotation is complete and lossless — there is nothing discarded. The imaginary part only exists within the complex-number rewriting. The actual contribution is adding sin-modulated attention heads alongside cos-modulated ones. While the mathematical derivation is correct, the framing overstates the novelty and could confuse readers. The paper would be stronger if it reframed the contribution as "augmenting RoPE with complementary sin-based positional modulation heads."
- **Missing "doubled-heads" baseline for RoPE++_EC:** RoPE++_EC doubles the number of attention heads compared to standard RoPE. A controlled comparison against standard RoPE with the same doubled head count (matching total parameters) would more cleanly isolate whether the sin/cos decomposition itself drives the gains, rather than increased capacity. The noise-perturbation experiment (Section 5.2) partially addresses this by showing imaginary heads play a distinct causal role, but a head-count-controlled baseline would be more direct.
- **Characteristic-curve analysis is theoretical motivation, not proof of mechanism (Section 3.2):** The derivation assumes random isotropic q,k vectors, but trained models learn structured, content-dependent attention patterns. The oscillatory behavior of the Si function (it does not monotonically decay) is not discussed. However, the paper corroborates the long-range claim empirically through attention visualizations and the noise-perturbation experiment, so this is a theoretical limitation rather than an empirical gap.
- **Model scales are modest (376M, 776M):** While the experiments are thorough at these scales and show consistent trends, results on larger models (>1B parameters) would strengthen the generality claims. This is a common limitation in position-embedding papers that train from scratch and does not undermine the presented evidence.

### Trivial
- The paper occasionally references figures by incorrect numbers in the text (e.g., line 111 references "Figure 5f" and "Figure 5h/5j" when discussing Figure 3 content — likely a cross-reference error).

## Nice-to-Haves
- A direct head-count-controlled baseline (standard RoPE with same total heads as RoPE++_EC) would conclusively rule out capacity confounds.
- Analysis of whether the Si function's oscillatory behavior creates systematic suppression at certain distance bands in trained models.
- Results at larger model scales (>1B parameters) would strengthen generality, though the 376M/776M experiments already show consistent trends.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic: "The 'discarded information' framing is conceptually wrong and undermines the paper's motivation (structural)"** — Demoted from Fatal to Minor. The mathematical derivation (Eqs 1-4) is correct regardless of framing. Whether one views the imaginary part as "discarded" or "not computed" is a matter of perspective within the complex-number representation. The underlying method is valid and well-validated. Kept as Minor: the framing inflates novelty but does not invalidate the contribution.
- **Harsh Critic: "The method reduces to adding attention heads with a fixed transformation, and the paper never justifies why this specific transformation should help"** — The paper justifies this through the characteristic curve analysis (Section 3.2), the length extrapolation mechanism (Section 3.4), the noise-perturbation causal experiment (Section 5.2), and the attention pattern visualizations (Figure 5). The doubled-heads baseline concern is kept as Minor, but the claim that the method is unjustified is incorrect.
- **Harsh Critic: "The theoretical argument in Section 3.2 is suggestive but does not establish the claimed mechanism (evidential)"** — The paper treats the characteristic curve as theoretical motivation, not as standalone proof of mechanism. The empirical validation (attention patterns, noise perturbation) corroborates the theory. Demoted to Minor with the oscillatory-behavior observation preserved.
- **Harsh Critic: "Related work section is thin"** — The related work covers the main lines of RoPE improvement (length extrapolation, data-awareness, multi-modal, feature-dimension partitioning) and correctly identifies the gap. Removed as subjective.
- **Harsh Critic: "The claim about length extrapolation... was not reached in my reading"** — The harsh critic acknowledged they couldn't read the experimental sections. The extrapolation claim is supported by Section 3.4 (mechanistic argument) and Tables 2-3 (empirical results at 64k context). Removed.
- **Strength Finder: Generic strengths about problem importance** — Removed. Generic "important problem" statements do not constitute concrete strengths.

## Novel Insights
The key insight — that the imaginary component of the complex attention can be expressed as a simple -π/2 query rotation followed by standard RoPE — is genuinely clever and practically useful, requiring minimal implementation changes while unlocking complementary positional modulation. The length-extrapolation observation (Section 3.4) that RoPE++ exposes q,k dimensions to a wider positional embedding range during training, thereby mitigating OOD issues at longer contexts, is also a crisp mechanistic insight that goes beyond prior work on RoPE extrapolation.

## Suggestions
- Reframe the motivation from "recovering discarded information" to "adding complementary sin-based positional modulation heads alongside the standard cos-based ones." The math and results remain identical, but the framing would be more precise and avoid conceptual confusion.
- Add a head-count-controlled baseline for RoPE++_EC (standard RoPE with doubled heads, matched total parameters) to conclusively isolate the sin/cos decomposition effect from capacity increases.
- Fix the cross-reference errors where Figure 5 is cited when Figure 3 is intended (Section 3.4, line 111).

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>