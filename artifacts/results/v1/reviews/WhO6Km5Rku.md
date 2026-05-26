Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes QubitCache, a hybrid classical-quantum framework for KV cache compression that preserves attention patterns (relationships between tokens) rather than individual tokens. The approach retains 15% of tokens in classical storage (anchor, recent, and "critical" tokens identified via accumulated attention scores) while encoding the attention distributions of the remaining 85% into 9-qubit quantum amplitude states. During inference, the compressed tokens contribute via query-independent probabilistic weights reconstructed from these quantum states. The method reports 7× memory reduction (0.55 GB vs 3.91 GB) on Llama-8B and claims 92–97% of baseline performance retention across models and tasks.

## Strengths

- **Ablation study directly validates the relational-preservation hypothesis.** Table 4 shows that removing attention-selected critical tokens causes a catastrophic 20.4% F1 drop, whereas removing position-based heuristics (anchor/recent) causes only 0.6% degradation. Random token selection at the same retention ratio yields 0.335 F1 vs. Full QubitCache's 0.491. This experimentally isolates that the attention-based selection mechanism — not the quantum encoding — drives most of the performance, which is a clean and falsifiable empirical finding.

- **7× measured memory reduction with clear complexity breakdown.** Table 3 reports 0.55 GB vs 3.91 GB for FullKV (7.1×) on 8K-token sequences with Llama-8B, surpassing all baselines (token-selection methods: 2×; quantized GEAR: 6.7×). The complexity formula O(L×H×0.15S×D + log N) honestly separates the classical and quantum contributions, unlike the abstract's framing.

- **Scaling evidence on 70B/30B models.** Table 2 shows QubitCache retains 96.9% (Llama-70B) and 89.0% (Qwen-30B) of uncompressed F1 on NarrativeQA, degrading less than all other compression methods (e.g., StreamingLLM loses 16.6% and 26.9%). This provides some evidence that larger models are more resilient to this form of compression.

## Weaknesses

### Major

- **The "92–97% of baseline performance" claim is not supported by the paper's own data.** Checking Table 1 systematically: DeepSeek-Coder achieves 75.5% (0.256/0.339) on HotpotQA, 75.9% (0.202/0.266) on SummScreen, 80.8% (0.156/0.193) on PG19, and 87.8% (0.822/0.936) on PIQA — none within 92–97%. Mistral-7B achieves 81.1% on HotpotQA. Llama-8B achieves 84.9% on TriviaQA. This range appears in the abstract ("maintaining 92-97% of baseline performance across five models and six benchmarks"), introduction, contribution list, and conclusion. It is factually contradicted by Table 1. This is a significant overclaim that undermines trust in the paper's quantitative narrative.

- **PG19 evaluated with F1 instead of the standard perplexity, without justification.** PG19 (Rae et al., 2019) is a language modeling benchmark uniformly evaluated by perplexity in the literature. The paper provides no definition or derivation of how F1 is computed for next-token prediction, no citation for using F1 on PG19, and no explanation for deviating from the standard metric. Because a reader cannot verify what is being measured, the PG19 column in Table 1 is effectively uninterpretable. This raises concerns about the evaluation integrity more broadly.

- **No latency or throughput measurements for an efficiency paper.** The paper's title and abstract position QubitCache as a method for efficient inference, yet the experimental section reports only memory consumption. For a method that involves simulating 9-qubit quantum circuits (state-vector multiplication, measurement sampling) at every segment boundary, the runtime cost is non-obvious and could easily outweigh the memory benefit. Without wall-clock time or tokens-per-second measurements, the practical feasibility claim is incomplete.

- **No error bars, confidence intervals, or multi-seed variance reporting.** All results in Tables 1, 2, and 4 appear to be single runs. Given that several comparative differences are small (e.g., 0.472 vs 0.491 in the quantum ablation), a reader cannot assess whether these differences are statistically meaningful.

- **The compressed-token "soft attention" is query-independent, but this architectural divergence is not discussed.** Equations (2) and (7) show that pⱼ(ψ) = |⟨j|ψ⟩|² is determined solely from the pre-computed mean attention distribution (Eqs. 3–5) and does not depend on the current query Qₜ. For 85% of tokens, the model cannot perform content-based retrieval — a fundamental departure from standard transformer attention. The paper refers to this as "soft attention" (contrasting with binary eviction), which conflates continuous weighting with query-dependent retrieval. The implications (e.g., breakdown on tasks requiring fine-grained query-specific lookups) are not analyzed or acknowledged.

### Minor

- **The 7× compression is overwhelmingly driven by discarding 85% of tokens; the quantum component contributes negligible memory savings.** Table 3's complexity formula makes this clear (0.15S×D dominates; +log N is negligible), but the abstract and introduction attribute the compression to "quantum amplitude encoding achieving logarithmic compression beyond classical information-theoretic limits." The 3.9% F1 gain from the quantum component in Table 4 is real but modest, and the narrative should be re-centered.

- **No matched-budget comparisons against token-selection baselines.** The paper compares QubitCache (15% retention + quantum) against H2O and ScissorHand at their standard 50% retention. While the "No Quantum" ablation (0.472 F1) partially addresses the 15%-retention baseline, the paper does not show what H2O or ScissorHand achieve when forced to 15% retention. This would directly isolate the benefit of the distributional-preservation approach over standard eviction at the same budget.

- **Averaging attention across all layers and heads (Eq. 4) without analysis of information loss.** Multi-head attention exhibits known specialization patterns (Clark et al., 2019). Averaging across all layers and heads before quantum encoding collapses this structure. The paper does not ablate or discuss what is lost.

- **The +log N memory complexity describes the theoretical quantum state size, but the classical simulation must materialize 2⁹ = 512 amplitudes per segment.** The paper acknowledges the implementation is classical simulation (Section 3.2.2) but does not report the materialization cost. The logarithmic claim is a forward-looking theoretical property, not a property of the evaluated system.

### Trivial

- Table 2 caption text is repeated twice in Section 4.3.

## Nice-to-Haves

- Compare against a classical distributional baseline (e.g., storing a top-k probability mass vector per segment instead of a quantum state) to directly test whether the quantum formalism provides any advantage over a classical compressed representation of the attention distribution.
- Analyze per-head variance of attention patterns before aggregation in Eq. (4) to quantify what is lost.

## Removed Points

These points were raised by reviewers but are removed or demoted after verification:

- **"Numerical inconsistency in 15.6% gap" (Harsh Critic point 4).** Removed. The paper states a 15.6% gap between Full QubitCache (0.491) and Random+Quantum (0.335). The absolute difference is 0.156 = 15.6 percentage points. This is numerically consistent. The harsh critic's calculation of ~46% treats the gap as a relative percentage of the random baseline, which is a different quantity. The paper is not wrong.
- **"Soft attention is fundamentally not attention."** This is reframed as a Major weakness (query-independence) rather than a fatal flaw, because the paper's core claim is about preserving distributional traces vs. discarding them — not about achieving standard query-key matching for compressed tokens. However, the terminology remains misleading.
- **"Missing related works" / reproducibility nitpicks.** Following the hard rules, these are removed.
- **"The method's performance retention comes despite this simplification, not from the quantum framing"** — this is speculation, not a verified claim. The ablation shows that attention-based selection drives most of the gain and quantum adds ~4%, which is consistent with what the paper shows (though the narrative overemphasizes the quantum component).

## Novel Insights

The single most interesting finding from the reviews — one the paper itself does not fully develop — is that averaging attention across all 32 layers and 32 heads (Eq. 4) before quantum encoding is a radical information bottleneck. The paper presents this as an implementation detail, but it means the quantum state encodes only the mean attention pattern, losing all layer-specific and head-specific specialization. The fact that the method still recovers 0.491 F1 with this collapsed representation is itself noteworthy: it suggests that either (a) the mean attention distribution carries surprisingly rich information, or (b) the 15% preserved tokens are doing most of the work and the quantum encoding is merely providing a coarse regularizing prior. The paper's ablation partially disentangles (b) but does not test (a). A controlled experiment comparing mean-based encoding against per-head encoding (at commensurate qubit budgets) would clarify the information-theoretic trade-off and could inform a general principle about attention distribution collapse in compressed transformers.

## Suggestions

1. **Correct the 92–97% claim.** Recompute retention percentages across all model–task pairs in Table 1 and report the actual range. If the range is wider (e.g., 75–99%), report that honestly and discuss where the method struggles.
2. **Replace PG19 F1 with perplexity or provide a rigorous definition and citation.** Without this, the PG19 column is unverifiable.
3. **Report latency and throughput** (tokens/second, with and without compression) on at least one model to establish practical feasibility.
4. **Add error bars** (minimum 3 seeds) for all main results.
5. **Include matched-budget baselines** — evaluate H2O and ScissorHand at 15% retention to enable direct isolation of the quantum component's benefit.
6. **Explicitly discuss the query-independence of the compressed-token branch** as a design choice with documented trade-offs, including an analysis of which attention patterns or reasoning types are most affected.
7. **Re-center the narrative** to honestly reflect that the primary compression (7×) comes from aggressive token selection (85% eviction), with the quantum encoding providing a modest (~4%) additional performance improvement on top.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Query Bucket | Comparison |
|--------|-----------|-------------|------------|
| LSH-E (0ZcQhdyI3n) | 3.83 | topic-low | KV cache compression paper rejected for missing baselines, no latency numbers, and limited evaluation. The paper under review has broader evaluation but worse overclaiming and a metric issue. |
| Preserving Large Activations (Uhvy5u90UY) | 3.50 | topic-low | KV cache pruning paper rejected for limited novelty, no latency, and overclaimed results. Similar failure modes to this paper. |
| ChunkKV (8sglLco8Ti) | 5.25 | topic-mid | KV cache compression paper rejected but with more careful claims and proper evaluation protocols. Notably does not overclaim. |
| Identify Critical KV (lRTDMGYCpy) | 5.75 | topic-mid | Stronger theoretical grounding and more rigorous evaluation than the paper under review. |
| Don't Discard/MiKV (CRQ8JuQDEd) | 5.00 | topic-mid | Mixed-precision KV cache paper with thorough evaluation. More careful about claim boundaries. |
| CAKE (EQgEMAD4kv) | 7.00 | topic-high | Accepted KV cache paper with actual latency speedups (10×), comprehensive evaluation, and measured performance. Far exceeds this paper's evaluation rigor. |
| QPA (bB0OKNpznp) | 6.00 | quantum-inspired | Accepted quantum-inspired LLM paper, but on PEFT (different setting). Still, more careful about not overclaiming quantum benefits. |

The low-band topic anchors (LSH-E 3.83, Preserving Large Activations 3.50) failed on missing latency/throughput, overclaiming results, and insufficient evaluation rigor. The paper under review shares all three failures: it reports no runtime measurements, the "92–97%" claim is contradicted by its own data, and the PG19 F1 metric is unjustified. The mid-band papers (ChunkKV 5.25, Identify Critical KV 5.75, MiKV 5.00) are more careful with their claims and evaluation. This paper is closer in quality to the low-band anchors than the mid-band ones, placing it firmly in the bottom-quartile range.

**Score: 3.5**

**Decision: Reject**

The paper identifies a genuinely interesting perspective — preserving distributional attention traces rather than discarding evicted tokens entirely — and the ablation study (Table 4) cleanly validates that attention-based selection matters. However, the evaluation has multiple issues that prevent acceptance in its current form: the headline "92-97% performance retention" claim is contradicted by the paper's own Table 1; the use of F1 on PG19 (a language modeling benchmark standardly evaluated by perplexity) is unexplained and unverifiable; there are no latency/throughput measurements for an efficiency paper; and the query-independent nature of the compressed-token branch is a significant architectural detail that goes unexamined. These issues collectively undermine confidence in the empirical findings. The core idea deserves exploration, but the paper needs substantial revision — particularly correction of the overclaimed results, proper metric justification, and missing efficiency analysis — before it can be considered for publication.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>