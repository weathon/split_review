I now have a thorough understanding of the paper and the calibration landscape. Let me write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me compose the full review now.

---

**My round-1 bracket**: Based on the calibration, weak anchors (scores 2-3) are papers on basic KV compression and unrelated quantum ML papers. Strong anchors (7.5+) are well-executed, clean papers on model compression. QubitCache sits between these, in the 3.5-5.5 range — it has a more novel idea than the weak band but more validity issues than the middle band. The **initial bracket is [3.5, 5.5]**.

**Round 2 narrowing**: Inside this bracket, MiKV (5.0, rejected) and DynamicKV (4.4, rejected) and KVMerger (4.33, rejected) are the most comparable anchors. QubitCache has stronger novelty than MiKV (which was rejected for limited novelty despite decent evaluation) but has more severe evaluation validity issues (unfair comparison at different compression ratios, overclaimed results). Compared to DynamicKV (4.4), QubitCache has a more surprising idea but less trustworthy evaluation. The decorative quantum framing adds another penalty vs. these cleanly-presented papers. This points to a score around **4.0**.

---

Here is my final review:

## Summary

QubitCache proposes a KV-cache compression method for LLMs that replaces binary token eviction with a "soft attention" mechanism. The core insight — that attention patterns between tokens carry essential relational information worth preserving — is sensible and supported by the ablation study (Table 4). The method retains ~15% of tokens as classical key-value pairs and encodes the aggregated attention distribution of the remaining 85% into a 512-element probability vector (framed as a 9-qubit quantum amplitude encoding), which is then used to compute interpolated value vectors during attention. Results show 7× memory reduction while maintaining 92-97% of uncompressed performance across several benchmarks.

## Strengths

1. **Well-motivated core insight with clean validation.** The ablation study (Table 4) is the paper's strongest piece of evidence. Removing critical tokens (selected by accumulated attention) causes a 20.4% F1 drop, while removing position-based tokens (anchor/recent) degrades performance by only 0.6% each. Random token selection with the quantum encoding achieves only 68.2% of QubitCache's F1. This directly validates the paper's central claim that attention-weighted selection, not arbitrary retention, drives compression quality.

2. **Competitive performance on multi-hop reasoning despite aggressive compression.** On HotpotQA, QubitCache (at 15% retention) outperforms all compression baselines across most model/model pairs — e.g., Qwen2-7B: 0.604 vs. ScissorHand 0.555, H2O 0.487; Phi-4-mini: 0.553 vs. H2O 0.390 — while retaining far fewer tokens.

3. **Scalability demonstration on larger models.** Table 2 shows QubitCache maintaining 96.9% of Full KV performance on Llama-70B (0.216 vs. 0.223 F1) and outperforming all compression baselines, suggesting the method does not break down at scale.

4. **Memory efficiency.** Table 3 reports 0.55 GB for QubitCache vs. 0.59 GB for GEAR at the same sequence length, achieving the highest compression ratio (7.0×) among methods compared.

## Weaknesses

### Major

1. **Uncontrolled comparison: QubitCache operates at 7× compression while token-selection baselines are evaluated at only 2×.** The paper's headline results (Table 1) compare QubitCache at 15% token retention against H2O, ScissorHand, and StreamingLLM at 50% retention (as shown in Table 3). This means QubitCache uses 3.5× less memory, so its superior scores may simply reflect having fewer total tokens to attend to rather than any fundamental advantage of relational preservation. Without a controlled memory curve (performance vs. compression ratio for all methods), the central superiority claims are uninterpretable. The issue is acknowledged in passing (abstract says "15% vs 50%") but never addressed experimentally.

2. **Attention aggregation across all heads and layers discards the relational information the method claims to preserve.** Eqs. (3)-(5) compute per-token attention scores per head, then average across all heads and layers into a single distribution, which is encoded into one quantum state per segment and reused across all heads during reconstruction (Section 3.4: "cached for reuse across attention heads"). Multi-head attention captures distinct relational structures per head; collapsing them into one distribution loses this information. The paper provides no justification or ablation for this design choice, and it conflicts with the stated motivation of "preserving relational structure."

3. **The 15-25% multi-hop improvement claim is overgeneralized.** Examining HotpotQA F1 against the *stronger* baseline in each row of Table 1: Mistral-7B improves only 3.6% over ScissorHand (0.459 vs 0.443); Qwen2-7B improves 8.8% over ScissorHand (0.604 vs 0.555); Llama-8B improves 1.6% over H2O (0.510 vs 0.502). Only a few cases reach the claimed range, and the absolute gap from Full KV remains large (e.g., Mistral-7B: 0.459 vs 0.566). The claim as stated in the abstract is not consistently supported.

### Minor

4. **The quantum encoding provides no demonstrated advantage over a classical alternative.** The implementation stores a 512-element probability vector (classical simulation). The paper's own ablation shows only a 3.9% improvement from the quantum component (Full QubitCache 0.491 vs. No Quantum 0.472), and there is no baseline that stores a classical softmax distribution for evicted tokens — the most direct competitor. The quantum formalism is decorative for this implementation; the method could be described as "store an aggregated attention probability vector and use it for weighted interpolation of evicted values." The claimed "logarithmic compression beyond classical limits" applies only to actual quantum hardware, not the classical simulation evaluated here.

5. **Missing baseline: a simple classical distribution cache for evicted tokens.** The "No Quantum" row in Table 4 likely discards non-critical tokens entirely rather than storing any distribution. A proper control would store the same 512-element softmax attention vector per segment as a classical probability table, enabling a direct test of whether the quantum-inspired framing adds anything over classical storage of the same distribution.

6. **No reporting of computational overhead.** The paper mentions gate fusion, parallel encoding, and adaptive shot allocation but gives no wall-clock time, FLOPs, or latency comparison against baselines. Quantum circuit simulation is known to introduce overhead, and without efficiency numbers, the practical applicability is unclear.

7. **No variance or statistical significance reporting.** All numbers appear to be point estimates. For a method involving stochastic reconstruction (quantum state measurement), reporting variance across runs is standard practice.

### Trivial

8. **Inconsistency between Figure 1 and the text.** The figure caption labels the quantum state as **a**₁^{(l,h)} (implying per-layer, per-head encoding), but Section 3.2.1 Eq. (4) averages across all layers and heads. The notation in the figure suggests more granular encoding than what is actually implemented.

## Nice-to-Haves

- A controlled memory experiment where each baseline is evaluated at the same 7× compression as QubitCache, to determine whether the claimed advantage holds at equal budgets.
- An ablation where each attention head gets its own distribution (at some cost), to quantify what is lost by the current aggregation.
- A purely classical variant that stores the same attention vector without quantum terminology, to isolate the contribution of the distribution-based reconstruction from the quantum framing.

## Removed Points

- **Theoretical guarantee is untestable** (harsh critic point #5): The appendix containing the proof was stripped by the parsing process. Per policy, criticisms of missing appendix content are removed. The paper's claim of a bounded reconstruction error cannot be evaluated from the visible text, but this is a submission-format artifact, not a paper flaw.
- **"Fundamental architectural inconsistency" / "breaks the method's stated motivation"**: The harsh critic describes the head-aggregation as a "structural flaw that breaks the method." This is an overstatement. The aggregation is a design choice; it weakens the method's ability to claim it preserves "attention patterns" but does not break the core idea of probabilistic reconstruction. I have downgraded this to a Major weakness.
- **Several minor format/style nitpicks** from the harsh critic and section-by-section notes (e.g., "Section 3.4 update mechanism is vague" without concrete specification of what is missing) are removed as insufficiently grounded.
- **Strength finder's generic strengths** ("important problem," "timely topic") are removed as superficial.

## Novel Insights

The reviews surface a tension that the paper itself does not fully acknowledge: the core algorithmic contribution — storing an approximate attention distribution for evicted tokens to enable soft reconstruction — is actually **independent of the quantum framing**. The quantum terminology provides a visually striking packaging (amplitude encoding, measurement, NISQ feasibility) but the 3.9% improvement from the quantum component in the ablation study is modest enough that a classical softmax cache could plausibly match it. The genuinely interesting question raised by this paper is whether storing any attention-weighted distribution for evicted tokens (classical or quantum) consistently outperforms binary eviction at the same memory budget. The current evaluation does not answer this question, but the paper's framing makes it a worthwhile direction to investigate.

## Suggestions

1. **Run baselines at matched compression ratios.** Plot performance curves for all methods across a range of memory budgets (e.g., 2×, 4×, 7×). Without this, the headline comparisons are not interpretable.
2. **Add a classical distribution cache baseline.** Store the same 512-element attention vector per segment as a simple probability table. If performance matches QubitCache, the quantum simulation is unnecessary.
3. **Either justify the head/layer aggregation or fix it.** Show an ablation with per-head encoding, or provide evidence that attention distributions are sufficiently similar across heads that averaging is harmless.
4. **Tone down the multi-hop claim.** The data support consistent improvement over H2O/ScissorHand in most cases, but the magnitude varies from 1.6% to 24%. A more precise claim would give the range observed (e.g., "1-24% improvement, with typical gains of 5-15%") and acknowledge the variability.

## Score and Decision

**Bracket determination (Round 1):** Three-band search over KV-cache compression papers returned weak anchors (avg 2.0-3.0, all rejected), middle anchors (avg 4.0-6.5, mix of reject and poster), and strong anchors (avg 7.6-8.2, accept). QubitCache is clearly above the weak band (more novel idea, more empirical scope) but far below the strong band (validity issues, loss of confidence). **Initial bracket: [3.5, 5.5].**

**Narrowing (Round 2):** Inside the bracket, the most comparable anchors are MiKV (5.0, rejected — limited novelty, decent eval), DynamicKV (4.4, rejected — clean but incremental), KVMerger (4.33, rejected — comparison concerns), and Palu (5.75, accepted poster — solid execution). QubitCache has stronger novelty than MiKV/DynamicKV but more severe evaluation problems (especially the uncontrolled compression comparison and decorative quantum framing that adds complexity without demonstrated benefit). The scrutiny applied to MiKV and DynamicKV would likely be applied even more critically here. **Final score: 4.0**, calibrated as below MiKV (5.0) and KVMerger (4.33) because the core experimental comparison is invalidated by the different compression budgets.

**Anchors retrieved across all rounds:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| SqueezeAttention (9HK2rHNAhd) | 5.5 | R1 | Clean evaluation, moderate novelty. Weaker than QubitCache in novelty but more trustworthy. |
| HeadKV (FJFVmeXusW) | 6.5 | R1, R2 | Well-executed with fair comparisons. QubitCache is below this. |
| MiKV (CRQ8JuQDEd) | 5.0 | R1, R2 | Rejected for limited novelty. QubitCache has more novelty but worse eval validity. |
| KVMerger (Q5VlpYRxGF) | 4.33 | R1, R2 | Had comparison concerns. QubitCache has similar severity of issues + framing concerns. |
| DynamicKV (uHkfU4TaPh) | 4.4 | R2 | Clean presentation, moderate novelty. QubitCache more novel but less trustworthy. |
| Palu (LWMS4pk2vK) | 5.75 | R2 | Accepted poster. Solid execution. QubitCache is below this. |

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>