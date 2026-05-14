Now I have all the information I need. Let me synthesize the final review.

**Key verification results**:
1. The paper claims "logarithmic compression beyond classical information-theoretic limits" (abstract) — but the classical simulation stores 512 amplitudes (same as the raw distribution). The compression comes from 15% token retention (dropping 85% of KV values), not from quantum encoding.
2. Baselines at 50% retention (2×) vs. QubitCache at 15% retention (7×) — comparison is unfair. Only GEAR at 6.7× is comparable.
3. Equation (7) confirms p_j(|ψ⟩) for non-critical tokens is independent of current query Q_t — verified as static.
4. Ablation (Table 4): quantum encoding provides only 3.9% improvement over classical fallback.

Let me also check the "No Quantum" ablation to verify the 3.9% claim:

From the paper (Table 4):
- Full QubitCache: 0.491 → No Quantum: 0.472 → (0.491-0.472)/0.491 = 3.87% drop

So the quantum part adds ~3.9%. This confirms the critic's point that most of the performance comes from the token selection, not the quantum encoding.

Now let me write the consolidated review.

For calibration, let me compare against my anchors:

1. **KVTC (avg 5.50)**: Solid KV cache compression paper with fair comparisons, clean methodology, real compression (PCA+quantization+entropy coding). QubitCache is substantially weaker — misleading framing, unfair comparisons, and the quantum part provides minimal benefit.

2. **VQKV (avg 2.50)**: Limited novelty, missing latency eval. QubitCache has somewhat more analytical contribution (ablation study), but its framing issues are more severe.

3. **Pitfalls of KV Cache (avg 4.00)**: Important problem framing, thorough analysis. QubitCache has less compelling contribution and more serious methodological issues.

4. **Hybrid Quantum Language Models (avg 2.50)**: Actually ran on quantum hardware, but small scale. QubitCache is similar in overclaiming quantum advantages.

5. **Joint Encoding of KV-Cache (avg 3.00)**: Modest compression (4.38×), but clean framing. QubitCache claims 7× but with unfair baselines.

I'll score this at **3.0**. The paper has a modestly useful idea (attention-based token selection + IDW interpolation) but buries it in overblown quantum framing and unfair comparisons. The verified weaknesses are major enough that the paper cannot be accepted in its current form.

Decision: Reject## Summary

QubitCache proposes a KV-cache compression method that retains 15% of tokens classically while encoding the attention patterns of the remaining 85% using quantum-inspired amplitude encoding (9 qubits per 512-token segment). The core intuition is that attention patterns carry more information than individual tokens. Token selection is driven by accumulated attention scores, and value vectors for non-critical tokens are reconstructed via inverse distance weighting (IDW) interpolation weighted by quantum-state measurement probabilities.

## Strengths

- **Attention-based token selection is empirically shown to be crucial.** The ablation study (Table 4) clearly demonstrates that removing attention-based critical token selection causes a 20.4% performance drop, while removing anchor or recent tokens has minimal effect (0.6% each). This provides evidence that identifying tokens via relational importance — rather than positional heuristics — is the key driver of performance.

- **Comprehensive multi-model, multi-benchmark evaluation.** Experiments span five models (4B–70B) and six datasets, including language modeling (PG19), multi-hop reasoning (HotpotQA, NarrativeQA), and summarization (GovReport). Results are broadly consistent across model sizes, with QubitCache retaining 92–97% of baseline performance at 7× compression relative to the GEAR baseline at similar compression.

- **Theoretical framing of bounded reconstruction error.** The paper provides a formal argument (rank-\(r\) preservation with bounded error) that distinguishes it from purely heuristic compression methods, even if the practical import of this guarantee is limited by the implementation's reliance on classical simulation.

## Weaknesses

### Fatal

None.

### Major

1. **The claimed "logarithmic compression" from quantum encoding does not materialize in the implemented system.** The abstract states that QubitCache achieves "logarithmic compression beyond classical information-theoretic limits." In the classical simulation actually used (Section 3.2.2, Appendix A.1.1), a 9-qubit state requires storing 2⁹ = 512 complex amplitudes — the same size as the 512-element attention weight vector it encodes. There is no compression of the attention distribution itself. The 7× memory reduction comes entirely from dropping 85% of KV value vectors (storing only 15% of tokens), not from any quantum advantage. The memory formula in Table 3 confirms this: the dominant term is \(O(L \times H \times 0.15S \times D)\) from token dropping, while the \(O(\log N)\) quantum term is negligible. The "No Quantum" ablation (Table 4) shows quantum encoding contributes only a 3.9% improvement, further confirming the quantum component is not the source of compression. This misrepresentation pervades the paper's framing.

2. **The experimental comparison against baselines is fundamentally unfair.** The paper's headline claims — "15–25% higher F1 on multi-hop reasoning" and comparison "despite 3.3× more aggressive compression" — pit QubitCache at 7× compression (15% token retention) against ScissorHand, H2O, and StreamingLLM at 2× compression (50% retention). The baselines would almost certainly degrade further at 7×. The comparison against GEAR (6.7×) is fair, and QubitCache does outperform it, but this legitimate comparison is conflated with the unfair one in the paper's main narrative. Without controlled compression ratios, the claimed advantages are uninterpretable as evidence of any fundamental superiority.

3. **The method replaces query-dependent attention with static weights for 85% of tokens, with no validation.** In Equation (7), attention for non-critical tokens uses \(p_j(|\psi\rangle)\) — measurement probabilities from the quantum state computed during the initial forward pass (Equations 3–5). The current query \(Q_t\) does not appear in this term. This means that for the 85% of tokens treated as non-critical, attention weights are frozen at their initial encoding and do not change as new tokens are generated. In standard transformer attention, every token's weight depends on the current query, which is critical for tasks like multi-hop reasoning where the relevance of past information evolves dynamically. The paper's token re-categorization mechanism (Section 3.4) handles boundary cases but does not update weights for tokens that remain non-critical. The paper provides no analysis or evidence that static weights suffice for dynamic generation.

### Minor

1. **The quantum formalism is largely unnecessary; the core contribution is a classical interpolation scheme.** Strip away the quantum vocabulary: QubitCache selects 15% of tokens via attention scores, drops the rest, and reconstructs their value vectors via IDW weighted by a static attention distribution. The 9-qubit amplitude encoding is just a way to store 512 attention weights (same as a classical vector). The paper would be more honestly framed as an attention-based token selection + interpolation method. The current framing risks misleading readers about the nature of the contribution.

2. **The ablation study shows the quantum component is near-negligible.** The "No Quantum" variant (0.472) achieves only 3.9% less F1 than Full QubitCache (0.491), while removing critical tokens drops performance by 20.4%. This suggests the quantum encoding is not the source of the method's effectiveness. The paper acknowledges this gap but does not adequately address why the quantum formalism is needed.

### Trivial

- Table 1 is difficult to parse due to the way model groups are stacked. A clearer separation between model blocks would improve readability.
- The paper uses "7× compression" and "0.15 retention ratio" inconsistently — it should clarify whether these refer to total sequence tokens or only non-critical tokens.

## Nice-to-Haves

- Evaluate all methods at equal compression ratios (e.g., 6×, 7×) to enable controlled comparison.
- Measure how well the static attention weights from the initial forward pass correlate with actual attention weights from subsequent queries during generation. This would validate or refute the method's core premise.
- Provide a purely classical baseline that stores the attention distribution as a 512-element vector (no quantum simulation) to isolate any benefit from the quantum framing.

## Removed Points

**These points are flagged to be removed; treat them with caution.**

- The harsh critic's claim that the paper fails to compare with equal compression ratios for ALL baselines is kept (it's valid for ScissorHand/H2O/StreamingLLM vs QubitCache), but the related claim that this "invalidates" the entire evaluation is softened — the GEAR comparison at 6.7× vs 7.0× is fair and does show QubitCache outperforms GEAR. The issue is that headline claims conflate the fair and unfair comparisons.
- The harsh critic's claim that "QubitCache would need to... show that static attention weights suffice" is kept as a Major weakness, but the claim that the method is "fundamentally unsuitable" for dynamic attention is softened — the preserved 15% of tokens still use query-dependent attention, so the model retains some dynamic capability.
- The Strength Finder's claim of "15-25% higher F1 despite 3.3× more aggressive compression" is moved here — it conflicts with the verified unfair-comparison weakness and should not appear as a strength without qualification.
- The Strength Finder's "paradigm shift from token selection to relational preservation" claim is dropped from strengths — the method still performs token selection (attention-based), not genuine relational state preservation. The ablation result is valuable but the "paradigm shift" framing is overblown.

## Novel Insights

The reviews surface a tension that the paper does not resolve: the relational-preservation framing is philosophically appealing but the actual mechanism (attention-weighted token selection + static distribution interpolation) is much closer to existing token-eviction methods than the paper admits. The most genuinely informative result — that attention-based selection dramatically outperforms random selection (Table 4) — is a useful empirical finding regardless of the quantum framing. However, this finding could have been obtained without any quantum formalism, and the paper's central practical question (whether static attention weights preserve enough relational information for autoregressive generation) remains unanswered. The quantum framing appears to be an attempt to claim a paradigm-level contribution where a modest algorithmic one exists.

## Suggestions

1. **Re-frame the paper honestly.** Drop the "beyond classical information-theoretic limits" claim. Acknowledge explicitly that the compression comes from selective token retention (15%) and that the quantum encoding only stores the attention distribution with no additional compression over a classical vector. Present the method as "attention-informed token selection with interpolated value reconstruction."

2. **Re-run baselines at matched compression ratios.** Evaluate ScissorHand, H2O, and StreamingLLM at 7× compression (or QubitCache at 2×) to produce a controlled comparison. The fair comparison against GEAR is a good start but incomplete.

3. **Validate the static-attention assumption.** Measure the correlation between initial-pass attention weights and actual query-dependent weights during generation for a representative sample of non-critical tokens. If correlation is high, the method is justified; if not, a different approach is needed.

4. **Run the "No Quantum" baseline more thoroughly.** If a purely classical variant (attention-based selection + IDW with a stored distribution vector) achieves near-identical results across all benchmarks, the quantum component should be presented as a conceptual inspiration rather than an operational contribution.

## Score and Decision

**Calibration anchors** (all from ICLR 2026 human reviews):

| Anchor Paper | Avg Score | Comparison |
|---|---|---|
| KVTC (KV cache transform coding) — aNVKROYpLB | 5.50 | Fair, well-controlled KV cache compression paper with clear methodology. QubitCache is substantially weaker — misleading framing, unfair key comparisons, unvalidated assumptions. |
| Joint Encoding of KV-Cache Blocks — M9SgtgvF7l | 3.00 | Modest compression scheme with clean presentation. QubitCache has a more interesting core idea (attention-based selection) but worse execution and framing. Comparable in overall quality. |
| VQKV (Vector Quantization) — YyxvRDh4d4 | 2.50 | Limited novelty, missing efficiency evaluation. QubitCache has more analytical content (ablation study) but also more severe framing issues. Slightly stronger than VQKV. |
| Pitfalls of KV Cache Compression — dDgoYv2f7Q | 4.00 | Important problem framing with thorough analysis. QubitCache's contribution is less compelling and its methodology less sound. Weaker than this anchor. |
| Practical Hybrid Quantum Language Models — TY6JBucZ56 | 2.50 | Actually ran on quantum hardware; modest contribution with overclaimed framing. Similar pattern of quantum-overclaiming to QubitCache. |

The paper has a legitimate core intuition (attention patterns matter more than individual tokens) and provides useful ablation evidence for this claim. However, the quantum framing is misleading about the source of compression, the experimental comparison against baselines at unequal compression ratios undermines the headline results, and the fundamental reliance on static attention weights for 85% of tokens is unvalidated. These are major issues that preclude acceptance. The paper's actual contribution — attention-informed token selection with IDW interpolation — would be a modest methodological variant at best. Compared to the calibration anchors, this paper falls between VQKV (2.50) and Joint Encoding (3.00), closer to the latter.

MY FINAL SCORE: <pineapple>3.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>