Now I have a clear picture. Let me compile the final review.

**Round 1 Bracket:** Based on comparison with LSH-E (3.83), KVMerger (4.33), KV-Dict (5.25), FlexPrefill (8.00), and CBQ (7.60), the paper plausibly sits in the **4.5–6.5** range.

**Round 2 Narrowing:** Compared against Critical KV (5.75, Reject), VL-Cache (6.00, Accept), and PyramidKV (5.60, Reject), QubitCache has more comprehensive experiments than most but the quantum overselling and underspecified ablation pull it below the accept line. I place it at **5.0**.

---

## Summary

QubitCache proposes a KV-cache compression method that reframes the problem around preserving attention relationships rather than individual tokens. It introduces a hybrid architecture where ~15% of tokens (anchors, recent, and attention-selected critical tokens) are kept in classical storage, while attention patterns for the remaining 85% are encoded into a compact probabilistic representation inspired by quantum amplitude encoding, then used as soft attention weights during inference. The method achieves 7× memory compression with 92–97% performance retention across five models and seven benchmarks, and shows particularly strong results on multi-hop reasoning tasks.

## Strengths

- **Compelling core insight backed by ablation evidence.** The paper's central thesis — that attention relationships matter more than individual tokens — is directly tested in Table 4. Removing attention-selected critical tokens causes a 20.4% F1 drop (0.491 → 0.391), while removing anchor or recent tokens leaves performance nearly unchanged. Random token selection with the same retention rate achieves only 0.335 F1, confirming that attention-guided selection, not arbitrary token preservation, drives performance.

- **Strong multi-hop reasoning results at aggressive compression.** On HotpotQA (Table 1), QubitCache achieves 15–25% higher F1 than token-eviction baselines across five models while retaining only 15% of tokens (vs. baselines' ~50%). For example, Mistral-7B: 0.459 (QubitCache) vs. 0.420 (H2O) vs. 0.403 (StreamingLLM). This directly supports the claim that soft probabilistic attention reconstruction preserves cross-document dependencies critical for multi-hop reasoning.

- **Comprehensive evaluation across model scales.** The paper evaluates on five models (4B–8B parameters) across seven benchmarks, plus scaling experiments on Llama-70B and Qwen-30B (Table 2) where QubitCache retains 96.9% and 89.0% of baseline performance respectively, outperforming all baselines. This breadth is a genuine strength.

- **Principled hybrid attention with value interpolation.** The soft attention mechanism (Eq. 7) combined with inverse-distance-weighted value interpolation (Eq. 6) provides a well-motivated alternative to binary token eviction, avoiding the catastrophic discontinuities that cause sliding-window methods to fail on long-range tasks (e.g., Contract Accuracy in Table 1, where StreamingLLM drops to 0.392 vs. QubitCache's 0.600 on Mistral-7B).

## Weaknesses

### Fatal

None that unambiguously invalidate the core claims from the paper as written.

### Major

- **The "No Quantum" ablation is critically underspecified, and the quantum component's benefit is modest.** Table 4 reports Full QubitCache at 0.491 F1 vs. "No Quantum" at 0.472 — a 3.9% relative improvement. The paper never defines what "No Quantum" entails (uniform weights? stored classical attention vector? no soft-attention at all?). Without this specification, the reader cannot assess whether the quantum encoding provides any benefit beyond a classical equivalent that stores the identical attention distribution as a float vector. The paper must compare against a classical variant that uses identically computed attention-derived probabilities stored conventionally, then used for the same soft-attention term in Eq. 7. The absence of this baseline prevents attribution of any gain to the quantum-inspired design.

- **No equal-budget comparison with baselines.** QubitCache retains 15% of tokens (7× compression) while baselines (H2O, ScissorHand, StreamingLLM) are evaluated at their ~50% retention (2× compression, as shown in Table 3). The paper's framing — "we achieve better performance at more aggressive compression" — is partly valid, but a proper evaluation would fix the memory budget or token retention ratio and compare all methods under that constraint. Without this, the headline compression-factor advantage is confounded with the aggressiveness of retention. The paper argues existing methods degrade catastrophically at higher compression ratios but never demonstrates this empirically.

### Minor

- **"Logarithmic compression beyond classical information-theoretic limits" is an overclaim.** The actual memory savings come from discarding 85% of KV vectors. The quantum state encoding stores a 512-dimensional probability vector (log₂512 = 9 qubits), which in classical simulation is just 512 floats — negligible compared to the saved KV cache. The quantum formalism provides a principled framework for encoding attention distributions compactly, but the paper overstates what this achieves in practice. The paper itself acknowledges this is a classical simulation (line 104), which partially mitigates but does not eliminate the issue.

- **No error bars or variance estimates.** Many reported improvements are small (e.g., PG19 F1: 0.121 vs. 0.113 for H2O on Mistral-7B), and without confidence intervals from multiple runs, the reader cannot distinguish signal from noise.

- **Missing latency and throughput measurements.** The method requires pre-compression attention computation and periodic re-evaluation (Section 3.4). End-to-end wall-clock time comparisons against baselines are absent, making it difficult to assess practical deployment viability beyond memory savings.

### Trivial

- The ablation study (Table 4) does not report which task or metric the F1 scores correspond to, making absolute numbers difficult to interpret in context.
- Figure 3's discussion of NISQ coherence constraints (e.g., "750ns execution time") is somewhat incongruous given that all experiments use classical simulation; this discussion is speculative.

## Nice-to-Haves

- A classical soft-attention baseline that stores the same attention-derived probability vector as a float array and applies it identically in Eq. 7 — this would cleanly isolate any quantum-specific benefit.
- Equal-budget experiments where H2O, ScissorHand, and StreamingLLM are configured to match QubitCache's 15% retention, to test the claim that token-eviction methods degrade catastrophically at aggressive compression.
- Sensitivity analysis of the λ mixing parameter (Eq. 7) and the segment size (512 tokens / 9 qubits).

## Removed Points

These points are flagged to be removed — treat them with caution.

- **Harsh Critic: "The quantum encoding is unnecessary and provides no genuine compression advantage — the actual compression comes entirely from discarding 85% of KV vectors."** REMOVED as a standalone fatal claim. The paper does not claim the quantum state provides the memory compression; it claims the quantum state enables preserving attention relationships *at* that compression level. The memory savings do come from the 15% retention. The review reframes this as a different concern: whether the quantum component adds value beyond a classical equivalent (see Major Weakness #1).

- **Harsh Critic: "The assertion that the paper is the 'first framework recognizing that attention patterns constitute the primary information carrier' ignores decades of attention analysis."** REMOVED as an overstatement. The paper explicitly cites prior work (Michel et al., 2019a; Choromanski et al., 2020) establishing attention pattern importance. The novelty claim is about *applying* this insight to KV-cache compression, not discovering the insight itself. The phrasing is mildly overclaimed but not fraudulent.

- **Harsh Critic: "The quantum parameter analysis (Figure 3) is performed on simulated circuits, so statements about coherence times and NISQ feasibility are irrelevant."** REMOVED as a misunderstanding. The paper explicitly states it operates as classical simulation (line 104). The NISQ discussion is forward-looking, not deceptive.

- **Harsh Critic: "O(n²) computation reintroduced during re-evaluation."** DEMOTED and moved to Nice-to-Haves. The paper briefly addresses this (Section 3.4: "reducing the amortized update cost to O(log n) per token") but lacks empirical substantiation. This is a reasonable concern but not a verified flaw in the paper as written.

- **Strength Finder: "Paradigm shift from token selection to relational preservation"** — KEPT as a genuine contribution but reframed without the "paradigm shift" rhetoric.

- **Strength Finder: "Well-justified quantum parameter choices grounded in NISQ constraints"** — REMOVED. The quantum parameter analysis (Figure 3) uses simulated circuits; the NISQ discussion is speculative and not a verified strength.

- **Strength Finder: "Empirical validation of the 7× memory compression and stability of the hybrid architecture"** — MERGED into the strengths about comprehensive evaluation and value interpolation.

## Novel Insights

The most interesting finding across the reviews is the tension at the heart of this paper: the core idea (preserving attention patterns rather than tokens) is genuinely valuable and well-supported by the ablation, yet the quantum formalism that the paper foregrounds as its primary contribution contributes only 3.9% in the ablation. This suggests that the meaningful contribution is the token-partitioning + attention-based selection + probabilistic soft-attention pipeline, while the quantum encoding is an elegant but largely interchangeable implementation detail. The paper would be stronger if it focused on what actually works — the attention-preserving compression strategy — rather than wrapping it in a quantum narrative that distracts from and oversells the real technical content.

## Suggestions

- **Restructure around the attention-preservation insight.** The quantum formalism is not the contribution; the insight that attention pattern preservation matters more than token preservation is. Lead with that, and present the probabilistic encoding as one (classically realizable) mechanism for achieving it.
- **Specify and strengthen the "No Quantum" ablation.** Define precisely what replaces the quantum state — ideally both a uniform-weight variant and a classical attention-vector variant — so the marginal contribution of quantum amplitude encoding is unambiguous.
- **Add equal-budget comparisons.** Run H2O, ScissorHand, and StreamingLLM at 15% retention and report degradation. If they truly fail catastrophically (as the paper asserts), this will dramatically strengthen the paper's case.
- **Provide latency benchmarks.** Even approximate wall-clock comparisons would help readers assess practical viability.
- **Tone down the claims.** Phrases like "logarithmic compression beyond classical information-theoretic limits" and "paradigm shift" should be replaced with precise, verifiable statements about what the method actually achieves.

## Score and Decision

**Calibration anchors reviewed:**

| Anchor | Round | Avg Score | Comparison |
|--------|-------|-----------|------------|
| LSH-E (0ZcQhdyI3n) | R1 | 3.83 | QubitCache clearly stronger: more comprehensive experiments, more baselines, stronger results |
| KVMerger (Q5VlpYRxGF) | R1 | 4.33 | QubitCache stronger: broader evaluation, more baselines, better multi-hop results |
| KV-Dict (FkXYvV7nEB) | R1 | 5.25 | Comparable: QubitCache has better breadth but KV-Dict has cleaner contribution framing |
| Critical KV (lRTDMGYCpy) | R2 | 5.75 | Critical KV has stronger theoretical foundation; QubitCache has better empirical breadth but quantum overselling |
| PyramidKV (jZVNmDiU86) | R2 | 5.60 | QubitCache comparable or slightly weaker due to quantum framing issues |
| VL-Cache (HMrcv7Q4Ub) | R2 | 6.00 | QubitCache weaker: VL-Cache had cleaner motivation, better-justified design, accept at 6.00 |
| FlexPrefill (OfjIlbelrT) | R1 | 8.00 | QubitCache clearly weaker |
| CBQ (eW4yh6HKz4) | R1 | 7.60 | QubitCache clearly weaker |

**Round 1 bracket:** 4.5–6.5. **Round 2 narrowed to:** 5.0. The paper has real contributions (attention-pattern preservation, comprehensive experiments, strong multi-hop results) but the quantum framing substantially oversells the contribution, the "No Quantum" ablation is critically underspecified, and there is no equal-budget baseline comparison. These issues pull it below the accept threshold occupied by VL-Cache (6.00) while its empirical breadth keeps it above the weaker KV-cache papers (3.83–4.33).

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>