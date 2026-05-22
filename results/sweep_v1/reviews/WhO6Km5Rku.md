Now I have all the information needed. Let me write the consolidated review.

## Summary

The paper proposes QubitCache, a hybrid KV-cache compression method that keeps ~15% of tokens in classical storage (anchor, recent, and attention-critical tokens) and encodes the attention patterns of the remaining 85% of tokens into quantum-inspired amplitude encodings (using 9-qubit states). During inference, non-critical tokens contribute through interpolated value vectors weighted by measurement probabilities from the quantum state, while preserved tokens contribute through standard attention. The method is implemented as a classical simulation of the quantum circuits.

## Strengths

- **Attention-based token selection empirically dominates random selection.** Table 4 shows that removing attention-critical tokens causes a 20.4% F1 drop, while removing anchors or recent tokens causes only 0.6% drops. Random token selection at 49.8% retention (3.3× more tokens than QubitCache's 15%) achieves only 68.2% of QubitCache's performance, cleanly validating that attention-based relational structure is more important than arbitrary token preservation.

- **Consistent advantage over token-selection baselines on multi-hop reasoning.** On HotpotQA, QubitCache outperforms all baselines (e.g., Qwen2-7B: 0.604 F1 vs. next-best GEAR 0.545, vs. H2O 0.487). The advantage is sustained across all five evaluated models.

- **Broad experimental coverage.** Evaluations span five models (4B–8B) and seven benchmarks including long-context tasks. A scaling experiment to Llama-70B and Qwen-30B is also provided, showing the method generalizes beyond smaller models.

- **Concrete memory measurement.** Table 3 reports actual GPU memory consumption (0.55 GB for QubitCache vs. 3.91 GB for FullKV on 8K-token sequences), with explicit complexity accounting.

## Weaknesses

### Major

- **Overstated quantum compression claims.** The paper claims "logarithmic compression beyond classical information-theoretic limits" (Abstract). The method is implemented as a *classical simulation* of a 9-qubit circuit, which stores all 512 complex amplitudes — exactly the same information content as a classical 512-element probability vector. The logarithmic encoding claim is valid only if the method ran on actual quantum hardware, which it does not. The paper acknowledges classical simulation (Section 3.2.2: "the current implementation operates as a classical simulation") but then continues to claim logarithmic compression, which is misleading. In the current implementation, the quantum encoding provides zero memory savings beyond what storing 512 floats directly would cost.

- **Unfair comparison with baselines.** Table 1 compares QubitCache (15% token retention, 7× compression) against H2O, ScissorHand, and StreamingLLM at only 2× compression (50% retention). The paper claims "15-25% higher F1 scores" over these methods, but this advantage is largely an artifact of comparing at different compression ratios. The paper does not provide the critical comparison: how do H2O/ScissorHand perform at the same 15% retention? Without this, the claimed "superiority" cannot be attributed to the method's design rather than its more aggressive compression target.

- **Minimal empirical evidence that the quantum encoding provides useful information.** Table 4 shows Full QubitCache (0.491) vs. No Quantum (0.472) — a 3.9% relative improvement. Critically, the paper does not specify what "No Quantum" replaces the quantum probabilities with (uniform attention? some other baseline?), making this comparison uninterpretable. Furthermore, the Random+Quantum (0.335) vs. Random No Quantum (0.334) difference is effectively zero (<0.3%), suggesting the quantum encoding provides essentially no useful signal when the token selection is random. The paper attributes the 3.9% gain in the non-random case to "quantum amplitude encoding" but does not rule out that it comes from an interaction with the attention-based token selection or the interpolation scheme.

- **The attention distribution is frozen from the initial encoding pass and not updated for new queries.** Equations (3)–(5) compute the quantum state from attention scores during the initial forward pass. During autoregressive generation, new queries require attention to all past tokens, but the quantum state encodes only the static "aggregated attention importance" from the initial encoding. The paper provides no mechanism to update or condition this distribution on new queries, meaning the probabilistic weights used during generation are fixed from the prefill phase. Section 3.4's update strategy only re-evaluates token *categories* (promoting recent tokens to critical), not the quantum-encoded attention distribution itself. This is a structural gap: the method assumes the attention distribution over non-critical tokens is static, which is not true for changing queries.

- **Non-standard and potentially unreliable evaluation setup.** PG19 (a language modeling benchmark) is evaluated with F1 rather than the standard perplexity, yielding implausibly low values (FullKV Mistral-7B: 0.124 F1; DeepSeek-Coder: 0.193 F1). These numbers do not correspond to any known evaluation protocol for PG19, making them unverifiable and casting doubt on the evaluation pipeline.

### Minor

- **Qubit-count ablation (Figure 3a) is inconsistent with the segment size.** The paper uses 512-token segments, requiring ⌈log₂(512)⌉ = 9 qubits. But the ablation varies qubits from 4 to 15. With 4 qubits, only 16 tokens can be represented — this implies a different segment size or encoding scheme was used for this experiment, which is not explained. Similarly, 15 qubits covers up to 32,768 tokens, far more than the 512-token segments.

- **The 7× compression ratio comes almost entirely from token selection, not quantum encoding.** With 15% token retention, token-selection alone gives ~6.67× compression. The quantum component adds at most 0.33× (from the negligible log N term). The paper's framing implies the quantum encoding is responsible for the compression gains, but the ablation shows the quantum component contributes at most 3.9% performance improvement and negligible memory savings.

- **"No Quantum" ablation is underspecified.** The critical baseline for isolating the quantum contribution is not clearly described. How are the probabilistic weights p_j(ψ) replaced? Without this, the 3.9% improvement cannot be attributed to the quantum encoding specifically.

- **HotpotQA degradation from FullKV is not reconciled with the "92-97% retention" claim.** On Mistral-7B, QubitCache achieves 0.459 F1 vs. FullKV 0.566 — that's 81% retention, well below the claimed 92-97% range. The 92-97% figure appears to be an average across tasks that includes short-context tasks (PG19, PIQA) where compression has less impact, masking the degradation on harder multi-hop tasks.

### Trivial

- The PG19 column in Table 1 is labeled "F1" but language modeling is standardly evaluated with perplexity. This should be clarified.
- The random baselines in Table 4 use 49.8% token retention vs. QubitCache's 15%, which is not explained in the table caption.

## Nice-to-Haves

- Compare QubitCache at equal retention ratios against all baselines (e.g., at 15% retention for H2O, ScissorHand) to isolate the method's contribution from the choice of compression budget.
- Clarify what "No Quantum" means in Table 4: are the quantum probabilities replaced by uniform attention, cached attention, or some other baseline?
- Evaluate on additional multi-hop reasoning benchmarks such as MuSiQue or 2WikiMultihop to strengthen the multi-hop claim.
- Provide a controlled experiment isolating the quantum component: compare (a) attention-based token selection + value interpolation only vs. (b) the same with quantum encoding vs. (c) storing a classical probability vector instead of the quantum state.

## Removed Points

- **"The method does not compress the KV cache" (Harsh Critic Issue 1, first sentence).** This is factually wrong. The method stores K/V vectors for only ~15% of tokens, achieving ~6.67× compression through token eviction alone. The quantum encoding is an add-on for attention-weight generation, not the compression mechanism itself. The critic conflates "the quantum encoding doesn't provide compression" with "the method doesn't compress."

- **"Storing these amplitudes (classically) requires 512 numbers, not 9" (Harsh Critic Issue 2).** The paper explicitly acknowledges it is a classical simulation (Section 3.2.2). The logarithmic claim is about the number of qubits needed on quantum hardware, not about classical storage. This is retained as a Major weakness (overstated claims) but removed as a standalone "fundamental misunderstanding."

- **"The random baselines use 49.8% of tokens... which undermines the conclusion" (part of Harsh Critic Issue 4).** Actually, random having *more* tokens (49.8% vs. 15%) yet performing *worse* (0.335 vs. 0.491) *strengthens* the paper's conclusion about attention-based selection being critical. The critic's framing that this "undermines" the conclusion misreads the direction of the evidence.

- **"Figure 3b shows 103% of baseline performance" (from Harsh Critic)** — this just means performance recovers to slightly above FullKV, not that there's an inconsistency.

- **Missing related works** — removed as per policy; I cannot verify their existence.

- **"StreamingLLM's performance is surprisingly high"** — subjective claim without evidence; the numbers are what they are.

- **"The GEAR numbers are not sourced and may be misconfigured"** — speculative; the paper cites Kang et al. 2024 for GEAR.

- **Various formatting and style nitpicks** — removed as parser artifacts.

## Novel Insights

None beyond the paper's own contributions. The core empirical finding — that attention-based token selection dominates random selection at the same or even lower retention rates — is a well-established result in prior KV cache compression literature (H2O, ScissorHand, etc.) and is not unique to this work. The quantum-inspired encoding provides marginal benefit (~3.9%) and is not convincingly shown to preserve relational structure beyond what simpler interpolation methods could achieve.

## Suggestions

1. **Rebaseline at equal retention ratios.** Evaluate all methods (H2O, ScissorHand, StreamingLLM, GEAR) at the same 15% token retention used by QubitCache. Present this as the primary comparison table. Only then can the method's claimed advantages be assessed fairly.

2. **Clarify the "No Quantum" baseline.** Explicitly state what replaces the quantum measurement probabilities — this is critical for interpreting the 3.9% gain. If replaced by uniform attention, compare against also storing the full attention histogram classically to show whether the quantum formalism provides any benefit over storing the same 512 floats directly.

3. **Reconcile the 92-97% retention claim with per-task numbers.** Either report average retention with error bars per model, or explain why certain tasks (HotpotQA at 81% for Mistral-7B) fall outside the claimed range. If certain tasks are excluded from the average, state which and why.

4. **Explain the qubit-count ablation scaling.** When varying from 4 to 15 qubits, does the segment size change accordingly? A 4-qubit state can only index 16 tokens — if segments are still 512 tokens, the experiment is meaningless. This must be clarified.

5. **Either run on actual quantum hardware or remove "beyond classical limits" claims.** The paper's current strongest claim ("logarithmic compression beyond classical information-theoretic limits") is not supported by the classical simulation implementation. If the method stays as a classical simulation, reframe as "quantum-inspired probabilistic encoding" without claiming information-theoretic advantages over classical methods.

## Score and Decision

**Calibration Anchors:**

| Anchor | Avg Human Score | Comparison |
|--------|----------------|-----------|
| IntelLLM (4QWPCTLq20) | 3.00 | Similar KV cache compression paper; QubitCache has broader experiments but more serious claims-inflation issues |
| LSH-E (0ZcQhdyI3n) | 3.83 | Similar evaluation flaws; QubitCache has more extensive evaluation but similarly unfair comparisons |
| HeadKV (FJFVmeXusW) | 6.50 | Well-scoped contributions with fair evaluation; QubitCache's claims are significantly more overstated relative to evidence |
| CAKE (EQgEMAD4kv) | 7.00 | Strong, well-executed paper with sound evaluation; QubitCache falls well short of this bar due to overstated claims and unfair comparisons |
| QPA (bB0OKNpznp) | 6.00 | Quantum-inspired method with similar quantum-vs-classical framing issues; QubitCache has more extensive experiments but the quantum component is even less justified |
| Quantum Entanglement for Attention (3jRzJVf3OQ) | 4.50 | Quantum attention paper with limited practical significance; QubitCache has more concrete application but similar quantum formalism overclaims |
| TgTxJALwDz (Noisy Quantum Comm) | 2.33 | Weak quantum+ML paper with fundamental misunderstanding; QubitCache is better empirically but shares similar quantum-advantage overclaims |

**Score rationale:** The paper has a legitimate empirical finding (attention-based token selection + value interpolation works well) and extensive experiments. However, three issues prevent acceptance: (1) the core claim of "logarithmic compression beyond classical limits" is not supported by the classical-simulation implementation; (2) the comparison against baselines at 2× compression when QubitCache uses 7× is unfair, making claimed advantages uninterpretable; (3) the quantum component provides at most 3.9% improvement and is not convincingly shown to be useful. These overclaims are structural, not cosmetic. The underlying hybrid architecture (token selection + interpolation + frozen attention distribution) is a reasonable engineering approach but does not constitute a novel contribution at ICLR's bar, especially given that the quantum framing is essentially decorative in the implemented classical simulation.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>