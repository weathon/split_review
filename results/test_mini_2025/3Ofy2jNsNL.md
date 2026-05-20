Now let me write the final consolidated review.

## Summary

This paper proposes ACT-IN-LLM, a method for compressing vision tokens inside LLM layers (rather than before the LLM) in Multimodal Large Language Models. The key ideas are: (1) retain all query tokens across layers to avoid irreversible information loss, (2) compress only key/value tokens within each self-attention layer, guided by the previous layer's attention weights (specifically, the last token's attention row), and (3) apply hierarchical compression ratios that increase with layer depth and are higher for high-resolution tokens than low-resolution tokens. The paper provides a theoretical framing through a unified compression-matrix formulation and proves that the proposed KV-only compression yields a better low-rank approximation than query-side or full compression. Experiments on a controlled setup (Table 2) show a +5.5 absolute point gain over FastV on high-resolution benchmarks while using ~83% of the full model's forward-pass time, and scaling experiments (up to 7B LLM, 1.2M SFT data) show the method remains effective at larger scales.

## Strengths

- **Well-motivated by a clear empirical study (Figure 2)**: The paper directly demonstrates that dropping vision tokens at early layers causes a ~15% performance gap on high-resolution benchmarks, and that tokens receiving low attention in early layers can become important later. This concretely motivates the core claim — that compressing within layers, guided by cross-modal attention, is preferable to pre-LLM or early-layer compression.

- **Controlled experimental comparison (Table 2)**: All compression methods are compared under identical training settings (same vision encoder, LLM, cropping strategy, training data, and SFT protocol). ACT-IN-LLM achieves 45.4% high-resolution average vs. FastV's 39.9% (+5.5 absolute points), and even without training (43.5%) it beats all trained prior methods. The single-forward-pass time (515ms, 83% of full) is competitive with other compression methods.

- **Theoretical justification via low-rank approximation (Theorems 1–3)**: The paper provides a unified formulation of different compression strategies (Eq. 7–9) and proves that KV-only compression (ACM) is strictly closer to full attention than Pre-LLM/Early-LLM compression or FlexAttention, under empirically verified assumptions (vision tokens receive less attention than text tokens; vision attention weights are low-rank). While proofs are deferred to the appendix, the framing is clean and the assumptions are tested in Figure 5.

- **Thorough ablation study (Tables 4a–4c, Table 5)**: The ablations isolate the effect of hierarchical vs. uniform compression ratios, distinct ratios for high- vs. low-resolution tokens, different compression methods (attention-weight selection, average pooling, learnable projection), and the proportion and placement of ACM layers. The best configuration is convincingly identified as hierarchical ratios with higher compression for high-resolution tokens, uniformly applied across ~70% of layers.

- **Scaling behavior (Figure 7)**: The method shows consistent improvement with LLM size (0.5B → 3B → 7B) and SFT data size (0.5M → 0.7M → 1.2M), suggesting it will continue to work at larger scales.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Inconsistent claimed improvement percentage**: The abstract states "6.3% improvement over existing token compression techniques," the introduction states "6.2% improvement," and the results text (page 7) says "outperforms 5.5% over the previous SOTA." From Table 2, the actual absolute gain over FastV (the previous SOTA) is +5.5 points. The abstract/intro numbers are ambiguous — they may refer to a different baseline or a relative improvement — but the inconsistency erodes precision and should be resolved with a single unambiguous statement.

2. **Selection relies on a single row of the attention matrix without comparison to alternatives**: The ACM uses only the last token's attention row (from the previous layer) to decide which vision tokens to keep in K/V. The paper argues the last token "encodes the complete multimodal context" (page 4), but this is not obviously optimal for all query positions — different text tokens may need different visual information. The ablation (Table 4b) confirms attention-weight selection works best among the tested options, but none of those alternatives use per-query or per-head selection. A head-to-head comparison with, or at least a discussion of, per-query or aggregated selection strategies (e.g., averaging over all text tokens) would strengthen the paper's argument about why the last-token row is sufficient. As presented, this design choice is empirically validated but not fully analyzed.

3. **No comparison with a full-token baseline at larger scales (Figure 7)**: The scaling experiments show ACT-IN-LLM improving with model/data size, but there is no full-token baseline at these scales. Without it, we cannot tell whether the compression loss widens or narrows with scale. The controlled comparison (Table 2) provides this at one scale (7B, 774K data), but the gap at larger scales remains unmeasured.

4. **No variance or statistical significance reported**: Benchmark scores are reported from single runs without confidence intervals. Some benchmarks (e.g., MME) have known high variance. While single-run reporting is common in this field, at least an error bar or multi-run verification on one key benchmark would strengthen the evidence, especially for small margins with other methods in Table 3.

### Trivial

1. **Head averaging not specified**: The method description (Eq. 3 and Figure 4 caption) refers to "the averaged attention weight from the i-1-th layer" without specifying whether this is averaged over attention heads. This should be stated explicitly.

2. **Selection overhead not quantified**: The ACM involves computing attention weights, performing top-K selection (O(N log N) per layer), and subsampling K/V. The paper reports end-to-end time (515ms vs. 621ms for full) but does not break down how much of the remaining time is spent on selection vs. the reduced self-attention. A brief overhead analysis would be helpful for practitioners.

## Nice-to-Haves

- An ablation comparing the last-token attention row with alternative aggregation strategies (e.g., averaging over all text token attention rows, or taking the maximum) would directly address the concern about the single-row selection mechanism.
- Reporting latency/throughput for varying numbers of image slices (2, 4, 8) beyond the single setting in Table 2 would strengthen the practical claims about the ~20% reduction.

## Removed Points

- **Criticism about the theoretical analysis being "incomplete" or "not fully convincing"**: The harsh critic states the theory is "suggestive but not fully convincing on its own." However, the paper is primarily an empirical systems paper. The theorems are clearly stated with assumptions, and empirical verification of those assumptions is provided (Figure 5). Deferring proofs to the appendix is standard practice at top venues. This criticism is weakened because the paper does not claim the theory as a standalone contribution — it is presented as supporting justification for the method design.
- **Request for an "oracle" ablation that masks K/V but keeps all tokens**: The critic suggests comparing with a setting that zeroes out contributions from removed K/V tokens but keeps all Q. This is a tangential experiment — the method's core claim is about the K/V-selection mechanism enabled by retaining all Q, not about isolating the effect of the mask structure. This is a reasonable suggestion for a follow-up study, not a weakness of the current paper.
- **Missing implementation details about the sparse mask**: The paper states the sampled causal mask is computed via Eq. 6 (indexing into M_i). The specific implementation (masked_fill vs. block-sparse kernels) is a low-level engineering detail inappropriate to require in a 9-page main paper.
- **Missing discussion of limitations**: While a formal limitations paragraph would strengthen the paper, the absence of one is a formatting choice, not a substantive flaw. The paper's empirical evidence is sufficient to assess its contribution without an explicit limitations section.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no observation that meaningfully reframes or deepens the paper's findings.

## Suggestions

1. Unify the claimed improvement numbers across the abstract, introduction, and results (recommend using the verified +5.5% over FastV from Table 2).
2. Clarify whether the "averaged attention weight" in Eq. 3 is averaged over heads, and if so, how many heads are averaged.
3. Add a brief discussion of why the last token's attention row suffices for selection (or acknowledge that per-query selection is a potential extension).
4. Include a full-token baseline at the 7B/1.2M scale in the scaling experiments (Figure 7), or at least note the gap as a limitation.
5. Quantify the overhead of the selection step (attention weight computation + top-K per layer) separately from the end-to-end time.

## Score and Decision

### Calibration

**Round 1 — Bracketing (all queries on "vision token compression multimodal LLM efficient attention"):**
- Weak band (score < 3.5): **PyramidDrop** (avg 3.0, withdrawn/reject) — similar topic but unclear method and incomplete comparisons; this paper is substantially stronger.
- Middle band (3.5–7.5): **Matryoshka MM** (6.0, poster) — variable-length visual tokens, simple but effective; this paper has comparable experimental rigor and stronger controlled comparisons. **Unraveling Visual Info Flow** (4.4, withdrawn) — token pruning from information flow analysis, with insufficient ablations and limited novelty.
- Strong band (> 7.5): **Language Model Beats Diffusion** (8.0, poster) — substantially different topic (visual generation/tokenizer); not a meaningful direct comparison.

**Round 2 — Narrowing (4.5–7.5):**
- **EMMA** (5.33, reject) — lightweight cross-modality fusion; limited novelty (similar to LLaVA) and small improvements; this paper is stronger in both novelty and improvement magnitude.
- **Adaptive Length Image Tokenization** (5.75, poster) — variable-length visual tokenization via recurrent refinement; solid work, comparable quality, but different problem setting.
- **HeadKV** (6.5, poster) — head-level KV cache compression for LLMs; different modality (text-only) but methodologically related (selective KV compression); this paper is comparable in thoroughness.
- **See What You Are Told** (5.75, poster) — visual attention sink analysis in LMMs; different type of contribution (analysis vs. method).

**Bracket statement**: Round 1 placed this paper in [4.5, 7.0]. Round 2 narrowed it: the paper is clearly stronger than EMMA (5.33, rejected) and Adaptive Length Tokenization (5.75) in terms of experimental rigor and contribution size. It is comparable to Matryoshka MM (6.0) and HeadKV (6.5), both accepted as posters. The paper has minor inconsistencies and one genuine design limitation (single-row selection uncompared with per-query alternatives), but the core contribution is well-supported.

**Final score**: 6.0 — solid accept. The method is clearly effective, the experiments are carefully controlled, and the limitations are addressable.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>