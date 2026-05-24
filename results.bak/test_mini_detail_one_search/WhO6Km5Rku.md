Now I have all the calibration data I need. Let me write the final consolidated review.

## Summary

QubitCache proposes a hybrid KV-cache compression framework that moves beyond token-level eviction by encoding attention patterns of non-critical tokens into amplitude-based quantum states. The system keeps ~15% of tokens in classical storage (anchor, recent, critical) while encoding the remaining 85% via 9-qubit amplitude encoding, then reconstructs attention weights probabilistically during inference. Evaluated across 5 models and 6 benchmarks, it achieves 7× compression with 92–97% of full-KV performance and demonstrates particular strength on multi-hop reasoning tasks.

## Strengths

1. **Novel framing of cache compression as relational preservation rather than token selection.** The paper makes a well-motivated case that attention patterns (relationships between tokens) carry more essential information than the tokens themselves. This is a genuine conceptual shift from prior eviction-based methods (H2O, ScissorHands, StreamingLLM) and is supported by references to sparsity analyses in the attention literature.

2. **Consistent empirical advantage on multi-hop reasoning.** On HotpotQA, QubitCache clearly outperforms all baselines across model sizes — e.g., Qwen2-7B: 0.604 F1 vs H2O 0.487 (+24%) and GEAR 0.545 (+11%) (Table 1). This advantage holds despite using *more aggressive compression* (7×) than the baselines (2×), making the comparison asymmetric in the baselines' favor.

3. **Strong ablation isolating the real driver of performance.** Table 4 shows that removing attention-selected critical tokens causes a 20.4% F1 drop (0.491→0.391), while removing positional heuristics causes only ~0.6% drops. Random token selection achieves only 68.2% of the full system's performance. This cleanly validates that attention-pattern preservation (not token-count retention) drives the compression quality.

4. **Comprehensive evaluation across 5 models and 6 benchmarks.** The paper tests on Llama-3-8B, Mistral-7B, Phi-4-mini, Qwen2-7B, and DeepSeek-Coder-7B across diverse tasks including PG19, HotpotQA, GovReport, and PIQA, showing consistent trends.

## Weaknesses

### Major

- **Overclaimed "logarithmic compression" for a classically simulated system.** The abstract and introduction claim "logarithmic compression beyond classical information-theoretic limits" and the memory complexity in Table 3 lists "+ log N" as though the quantum representation is compact. However, the paper transparently states (§3.2.2) that "the current implementation operates as a classical simulation." In classical simulation, each 9-qubit segment requires storing 512 complex amplitudes (the full statevector) — which is *linear* in the segment size, not logarithmic. While the practical overhead is modest (~32 MB across all layers and heads for an 8K sequence), the framing of "beyond classical limits" is misleading without clearly qualifying that the logarithmic bound applies only to a real quantum computer. This is the paper's most significant weakness.

- **The quantum encoding contributes only marginally (3.9% from Table 4).** The ablation shows Full QubitCache at 0.491 F1 vs. No Quantum at 0.472 — a difference of 0.019. No statistical significance is reported, and this is the only direct evidence that the quantum encoding itself provides value. The paper frames quantum amplitude encoding as the core innovation, but the data suggests that the attention-based critical token selection + inverse-distance interpolation accounts for ~96% of the performance, with the quantum machinery adding a small increment. This undermines the central narrative.

- **No statistical significance or variance reporting.** All results appear to be single-run point estimates. No confidence intervals, standard deviations, or significance tests are reported anywhere. Given the small absolute differences in several comparisons (e.g., Table 2: QubitCache 0.216 vs ScissorHand 0.209 on Llama-70B, a 0.007 gap), it is impossible to assess whether these differences are meaningful.

- **The autoregressive update mechanism (§3.4) is described but never evaluated.** The paper describes a strategy for updating the cache when new tokens are generated, but all experiments use fixed-input tasks where the cache is compressed once. No experiment tests generation beyond the precomputed encoding, so the practical feasibility of dynamic cache updating under real autoregressive conditions is unvalidated.

### Minor

- **Theoretical guarantee is claimed but not presented in the main text.** The abstract and introduction state: "We prove QubitCache preserves rank r attention structure with bounded reconstruction error." The proof is deferred to the appendix (stripped by the parser). Without the proof in the main paper, this claim is unverifiable.

- **Table 3's memory complexity notation is imprecise.** The column lists "O(L × H × 0.15S × D + log N)" for QubitCache. The "+ log N" term ideally captures the quantum encoding but is misleading for the classical simulation (where it should be O(#segments × 2^9) per layer-head). A more accurate accounting of the simulation overhead would strengthen the paper.

- **The 92–97% vs. 75–85% comparison in §5 compares different compression ratios.** The paper claims "92-97% performance retention at 7× compression compared to 75-85% for classical methods." The classical methods' 75-85% figure is measured at 2× compression, so this cross-ratio comparison is methodologically loose (though QubitCache still wins at a stricter ratio).

### Trivial

- The PG19 F1 metric choice is unusual for language modeling (perplexity is standard). This does not invalidate the results but makes comparison with the literature harder.

## Nice-to-Haves

- A fair comparison at matched compression ratios (e.g., running H2O/ScissorHands at 7× as well) would cleanly separate the benefit of the compression approach from the compression ratio.
- An experiment measuring performance degradation over multiple generation steps beyond the initial prompt would validate the §3.4 update strategy.

## Removed Points

These points were flagged by reviewers but are removed or downgraded:

1. **"Unfair baseline comparisons at different compression ratios" (critic's #3)** — Removed. The asymmetry favors the baselines (they use 2× compression with more memory), yet QubitCache (7×) still outperforms them. This strengthens, not weakens, the paper's claims.

2. **"Quantum encoding provides no actual compression benefit" (critic's #1 in strongest form)** — Downgraded to Major. The critic asserted "zero benefit" and that the method is "misleading wrapper." In reality, the quantum encoding provides a measurable 3.9% improvement (Table 4), and the paper is transparent about using classical simulation. The overclaim about logarithmic compression is real, but the "zero benefit" framing is too harsh.

3. **Various section-by-section nitpicks** (e.g., "no justification for λ, inverse distance weighting is classical") — Removed. These are implementation details appropriately scoped for a systems paper and do not threaten the core claims. The heuristic λ = √(|I_p|/N) is a reasonable design choice.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely agree on what the paper does well and where it falls short — the primary novel observation from synthesis is that the paper's strongest result (outperforming baselines at 7× vs. 2× compression) is actually *underemphasized* by the harsh critic's complaint about unfair comparisons, since the asymmetry cuts in QubitCache's favor.

## Suggestions

- Reframe the quantum claims carefully: make explicit that "logarithmic compression" refers to the qubit requirement on real quantum hardware, and add a clear memory accounting for the classical simulation's statevector overhead.
- Either report the bounded-reconstruction-error proof in the main text or downgrade the claim from "we prove" to "we conjecture / provide in appendix."
- Add error bars or multiple-run statistics to all experimental tables.
- Include at least one experiment that evaluates dynamic cache updating during generation (e.g., summarization where new tokens must attend to compressed context).
- Consider presenting the "No Quantum" configuration (attention-based token selection + interpolation) as the primary baseline and contribution, with the quantum encoding as an optional enhancement.

## Score and Decision

**Calibration anchors (all from the DeepReview corpus):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `E4Fk3YuG56` (Cut Cross-Entropy) | 8.50 | Far stronger: clean engineering contribution with rigorous evaluation |
| `OfjIlbelrT` (FlexPrefill) | 8.00 | Much stronger: well-executed sparse attention with thorough analysis |
| `eW4yh6HKz4` (CBQ) | 7.60 | Stronger: careful quantization with complete evaluation |
| `s1kyHkdTmi` (Evolved Universal Transformer Memory) | 7.00 | Stronger: learned memory management with better execution |
| `FJFVmeXusW` (HeadKV) | 6.50 | Stronger: cleaner execution in same KV compression area, accepted |
| `bB0OKNpznp` (QPA) | 6.00 | Stronger: honest quantum framing with measured claims, accepted |
| `FkXYvV7nEB` (KV-Dict) | 5.25 | Comparable: similar novelty but fewer overclaim issues |
| `CRQ8JuQDEd` (MiKV) | 5.00 | Comparable: similar evaluation quality, slightly less novelty |
| `p7vJ3wsm34` (KV-Distill) | 4.00 | Weaker: less compelling results |
| `4QWPCTLq20` (IntelLLM) | 3.00 | Weaker: limited novelty, poor execution |
| `0T8vCKa7yu` (CVXQ) | 3.00 | Weaker: incomplete evaluation |

The paper has a genuinely novel conceptual contribution (relational preservation over token selection) and strong empirical results on multi-hop reasoning. However, the quantum framing is significantly overclaimed for a classically simulated system, the quantum encoding's own contribution is marginal (3.9%), there is no statistical validation, and the dynamic update mechanism is unevaluated. The paper sits between the mid-range rejected papers (~5.0) and the accepted papers (6.0+) in this space — closer to MiKV (5.00) in overall quality than to HeadKV (6.50, accepted) or QPA (6.00, accepted). A carefully revised version that rectifies the overclaiming and adds missing evaluations could be competitive.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>