Now I have enough calibration data. Let me write the final review.

**Round 1 Bracket: 3.5–6.0**. The paper's comprehensive evaluation (5 models, 7 benchmarks, 70B scaling, memory measurements) places it above weak anchors like LSH-E (3.83) and KV-Distill (4.00), but the significant quantum overclaiming issues place it below cleaner contributions like MatryoshkaKV (6.00, accepted).

**Round 2 Anchors:**
- KV-Dict (5.25, rejected): Novel dictionary approach, limited comparisons. QubitCache has better evaluation but worse framing.
- ChunkKV (5.25, rejected): Chunk-based selection. QubitCache has broader eval but more serious overclaiming.
- PyramidKV (5.60, rejected): Dynamic allocation across layers. QubitCache has comparable eval breadth.
- Critical KV (5.75, rejected): Output perturbation theory. QubitCache has better evaluation coverage but weaker theoretical contribution.
- MatryoshkaKV (6.00, accepted): Clean orthogonal projection contribution. QubitCache has comparable eval but more framing issues.

QubitCache's evaluation is broader than most 5.0–5.75 anchors (5 models, 7 benchmarks, 70B scaling), which pushes it up. But the quantum overclaiming — claiming "logarithmic compression beyond classical limits" when the ablation shows the quantum component contributes only 3.9% and the implementation is admitted to be classical — is more misleading than any framing issue in the anchors. This pushes it down.

**Final score: 5.0.** The paper has genuine practical value and strong evaluation breadth, but the overclaimed quantum framing pervades the abstract, introduction, and significance claims, and the paper's own ablation undermines its central narrative.

## Summary
QubitCache proposes a KV-cache compression framework that retains the top 15% of attention-critical tokens in classical storage, encodes remaining tokens' aggregated attention distributions into quantum-inspired amplitude states (classically simulated as normalized probability distributions), and reconstructs value vectors via inverse-distance weighting. The paper reports 7× memory reduction with 92–97% performance retention across 5 models and 7 benchmarks, with scaling validation to 70B-parameter models.

## Strengths
- **Comprehensive evaluation across 5 diverse models and 7 benchmarks**: Table 1 presents results for Llama-3-8B, Mistral-7B, Phi-4-mini, Qwen2-7B, and DeepSeek-Coder-7B across PG19, PIQA, HotpotQA, TriviaQA, GovReport, Contract, and SummScreen. QubitCache consistently outperforms all baselines on the majority of model-benchmark combinations.
- **Clean ablation study isolating component contributions**: Table 4 demonstrates that removing critical (attention-selected) tokens causes a 20.4% F1 drop (0.491→0.391), while removing anchor or recent tokens causes only 0.6% drops each. Random selection with quantum achieves only 0.335 vs. QubitCache's 0.491, empirically validating that attention-based selection drives effectiveness.
- **Practical memory measurements with scaling validation**: Table 3 reports empirical GPU memory of 0.55 GB (7× compression) vs. 3.91 GB for FullKV. Table 2 extends evaluation to Llama-70B and Qwen-30B, showing the method scales to production-relevant model sizes with 96.9% and 89.0% baseline retention respectively.
- **Multiple compression baselines compared**: The paper compares against FullKV, ScissorHand, H2O, StreamingLLM, and GEAR — a reasonable set of contemporary baselines covering eviction, quantization, and streaming approaches.

## Weaknesses

### Fatal
None.

### Major
- **Quantum framing is misleading — the implementation is classical and the quantum component is marginal**: The paper claims "logarithmic compression beyond classical information-theoretic limits" (line 9) and presents the quantum amplitude encoding as the central contribution. However, line 100 admits "the current implementation operates as a classical simulation." On classical hardware, simulating a 9-qubit state stores 2⁹=512 amplitudes — O(S) across segments, not O(log N) as claimed in Table 3. More importantly, the paper's own ablation (Table 4) shows the quantum encoding contributes only 3.9% improvement (0.491 vs. 0.472), while attention-based token selection is responsible for 20.4% of performance. The real contribution — attention-based token selection + IDW interpolation + soft attention weighting — is obscured by quantum framing that the ablation shows is empirically marginal.

- **"15–25% improvement on multi-hop reasoning" is selectively reported**: The abstract and line 34 claim "15-25% higher F1 scores on multi-hop reasoning tasks." From Table 1 HotpotQA vs H2O: 9.3% (Mistral), 24.0% (Qwen2), 41.8% (Phi-4), 9.4% (DeepSeek), 1.6% (Llama-8B). Many values fall well below 15%. Additionally, QubitCache still substantially underperforms FullKV on HotpotQA for several models (e.g., Mistral-7B: 0.459 vs. 0.566, a 19% gap; DeepSeek: 0.256 vs. 0.339, a 24.5% gap), which is not foregrounded.

- **No latency analysis despite memory being only one dimension of practical benefit**: The paper reports memory savings but never measures inference latency. Classical simulation of quantum circuit encoding, measurement operations, and IDW interpolation all add computation. Table 3 claims "minimal latency overhead" without measurements. If the computational overhead of the quantum simulation offsets the memory savings in practice, the contribution is substantially weakened.

### Minor
- **Averaging attention across all layers and heads discards structurally important information**: Equation 4 computes mean attention as (1/LH) Σ_l Σ_h a_i^(l,h), collapsing per-layer, per-head attention patterns. Different layers encode different relationship types, and this averaging means the method cannot distinguish between tokens important for different semantic functions.
- **"No Quantum" ablation is underspecified**: Table 4 reports "No Quantum" achieves 0.472 F1 but does not describe what weighting scheme replaces the quantum-derived probabilities for non-critical tokens. Without knowing whether this baseline uses uniform weights, zero vectors, or some other scheme, the ablation is incomplete.
- **Sensitivity of λ = √(|I_p|/N) is not analyzed in the main text**: With 15% retention, λ ≈ 0.39, giving reconstructed tokens ~61% of attention weight. This is a significant design decision that should be analyzed in the main paper rather than deferred to appendix.
- **"First framework" claim overstates novelty**: The abstract claims QubitCache is "the first framework recognizing that attention patterns between tokens constitute the primary information carrier." H2O and ScissorHand are both attention-score-based methods that explicitly use attention patterns for token retention decisions.

### Trivial
None.

## Nice-to-Haves
- Pareto-frontier comparisons with baselines evaluated at multiple retention ratios (e.g., 15%, 30%, 50%).
- Ablation of IDW vs. alternative interpolation strategies (zero vectors, nearest-neighbor, learned interpolation).
- Per-task failure mode analysis showing when 15% retention with IDW breaks down.
- Proof of bounded reconstruction error sketched in the main paper (claimed in abstract).

## Removed Points
These points are flagged to be removed, treat them with caution:
- The harsh critic's claim that comparison is unfair to baselines because they use only 50% retention — this comparison actually favors the baselines (lower compression) and QubitCache still wins, making it an asymmetric comparison that strengthens the paper's case, not weakens it.
- The harsh critic's comparison of IDW to StreamingLLM's assumptions — IDW interpolates missing values while StreamingLLM discards them entirely; the methods are qualitatively different, and the paper cites locality bias literature to justify IDW.
- The harsh critic's claim that "the proof of bounded reconstruction error is missing" — the appendix was stripped by the parser; the proof likely exists in the original submission.
- Strength Finder's framing of the 3.9% quantum improvement as a "meaningful additional benefit" — while the gain is real, presenting it as a strength conflicts with the documented major weakness that the quantum framing overclaims relative to its actual contribution.

## Novel Insights
The paper's most valuable contribution is empirical rather than quantum-theoretical: the ablation study provides clean evidence that attention-based token selection is the dominant factor in KV-cache compression, and that aggressive 15% retention combined with IDW-based value interpolation achieves strong results at 7× compression. This empirical finding, however, is obscured by quantum framing that the paper's own experiments show is secondary.

## Suggestions
1. Reframe the paper honestly around the classical contribution: attention-based token selection + IDW interpolation + soft attention weighting. Either drop the quantum claims or clearly scope them as a minor enhancement.
2. Report inference latency measurements alongside memory in Table 3.
3. Provide Pareto-frontier comparisons where baselines are evaluated at multiple retention ratios.
4. Fully specify the "No Quantum" ablation and add IDW vs. alternatives ablation.
5. Analyze λ sensitivity in the main text.
6. Correct the memory complexity claim from O(log N) to O(S) for the classical simulation, or explicitly note the O(log N) applies only to hypothetical quantum hardware.

---

**Retrieved Anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 4QWPCTLq20 (IntelLLM) | 3.00 | 1 | Weaker — similar KV cache problem, less comprehensive evaluation |
| 2DD4AXOAZ8 (MixAttention) | 2.00 | 1 | Much weaker — simpler sliding window approach |
| vw0NurJ7UX (PrefixQuant) | 3.00 | 1 | Weaker — quantization focus, less broad evaluation |
| E4Fk3YuG56 (Cut Cross-Entropy) | 2.67 | 1 | Different topic (loss computation), not directly comparable |
| 0ZcQhdyI3n (LSH-E) | 3.83 | 1 | Weaker — LSH-based approach with limited evaluation |
| 8sglLco8Ti (ChunkKV) | 5.25 | 1 | Similar — chunk-based selection, comparable evaluation scope, QubitCache has broader eval but worse framing |
| lRTDMGYCpy (Critical KV) | 5.75 | 1 | Similar — output perturbation theory, QubitCache has better eval but weaker theoretical grounding |
| CRQ8JuQDEd (Don't Discard) | 5.00 | 1 | Similar — adaptive precision, comparable quality |
| OfjIlbelrT (FlexPrefill) | 8.00 | 1 | Stronger — accepted, clean sparse attention contribution |
| wg1PCg3CUP (Scaling Laws for Precision) | 8.00 | 1 | Stronger — accepted, strong theoretical contribution |
| t7P5BUKcYv (MoE++) | 8.00 | 1 | Stronger — different topic, clean method |
| EytBpUGB1Z (Retrieval Head) | 8.00 | 1 | Stronger — accepted, mechanistic analysis |
| eZAlb8fX5y (KVTQ) | 4.40 | 2 | Weaker — ternary quantization, less comprehensive |
| p7vJ3wsm34 (KV-Distill) | 4.00 | 2 | Weaker — distillation framework, limited eval |
| QlvL6eEOC6 (KV Prediction) | 4.50 | 2 | Weaker — TTFT optimization, different focus |
| FkXYvV7nEB (KV-Dict) | 5.25 | 2 | Similar — dictionary learning, limited comparisons |
| jZVNmDiU86 (PyramidKV) | 5.60 | 2 | Similar — dynamic layer allocation, comparable quality |
| BQwsRy1h3U (MatryoshkaKV) | 6.00 | 2 | Slightly stronger — cleaner contribution, accepted at 6.0 |

**Round 1 bracket: 3.5–6.0.** Round 2 narrowed to 4.5–5.5. QubitCache has better evaluation breadth than most 5.0–5.75 anchors but more serious framing issues. Final score: 5.0 — a paper with genuine practical contributions and strong evaluation, offset by overclaimed quantum framing that the paper's own ablation undermines.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>