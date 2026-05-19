- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 3, 8
Now I will produce the consolidated final review.

## Summary

This paper identifies and analyzes a persistent quality gap between gated-convolution language models (H3, Hyena, RWKV) and attention-based Transformers on language modeling. Through controlled pretraining of 17 models across 70M–1.4B parameters, the authors find that 82% of the perplexity gap is concentrated on tokens requiring associative recall (AR) — despite AR hits comprising only 6.4% of tokens. To explain this, they formalize Multi-Query Associative Recall (MQAR), a synthetic task requiring multiple recalls per forward pass at varying positions with large vocabularies. They prove theoretically (via an equivalency between gated convolutions and arithmetic circuits) and demonstrate empirically that gated-convolution models require model dimension to scale linearly with sequence length to solve MQAR, while attention solves it with constant dimension. Informed by this analysis, they show that replacing 6–10% of layers with input-dependent sparse attention on repeated bigram positions closes 85–97% of the gap to attention while maintaining sub-quadratic complexity.

## Strengths

1. **Fine-grained attribution of the perplexity gap to a specific failure mode.** The paper isolates that 82% of the quality gap between gated convolutions and attention is attributable to AR hits (6.4% of tokens), despite using a transparently heuristic definition. This granularity goes well beyond aggregated perplexity comparisons and directly guides architectural intervention. The finding that a 70M attention model outperforms a 1.4B Hyena model on the AR slice (2.41 vs. 3.43 PPL) is striking and practically informative.

2. **MQAR formalization improves on prior synthetic benchmarks.** Prior AR tasks used single-query, fixed-position setups with tiny vocabularies — settings where gated convolutions appear to match attention perfectly. The MQAR definition (Definition 1) requires multiple recalls per forward pass at varying positions with vocabularies larger than model dimension, better capturing real-language demands and reconciling the discrepancy between prior synthetic successes and real-world perplexity gaps.

3. **Theoretical capacity bounds with clear empirical corroboration.** Theorem 1 proves that data-independent gated convolutions (Coyote) require parameters that scale with sequence length to solve MQAR, while Proposition 1 shows attention requires constant dimension. The empirical scaling laws (Figure 2) directly validate this: gated-convolution models (H3, Hyena, RWKV, Coyote) need model dimension ≥ sequence length to exceed 90% accuracy on MQAR, while attention achieves perfect accuracy with constant dimension 64. The Coyote operator (Theorem 2) elegantly unifies the analysis across seemingly disparate gated-convolution architectures.

4. **Controlled experiments isolating input-dependence as the key factor.** The paper compares programmatic selection (attention only on repeated bigram tokens), learned selection (top-k with noise and auxiliary loss), random selection, and full attention. Programmatic selection closes 85% of the AR gap while random selection fails, cleanly demonstrating that the benefit comes from targeting recall-requiring positions rather than any sparse attention pattern. The 360M-parameter hybrid with full attention outperforms the pure Transformer baseline by 0.85 PPL, showing that gated convolutions are complementary to attention when the right architectural interventions are applied.

## Weaknesses

### Fatal
None.

### Major

1. **Theory does not fully explain the empirical gap; the depth-scaling prediction is untested.** Theorem 1 shows Coyote *can* solve MQAR with near-linear parameters and poly-log depth, but the paper uses only 2-layer models in synthetic experiments and finds that gated convolutions fail unless d ≥ N. The paper acknowledges this ("the poly-logarithmic number of layers... is undesirable in practice," line 206) but never tests whether deeper gated-convolution models (e.g., 4 or 8 layers) with moderate width succeed on MQAR. If deeper models still fail, the theory is incomplete as an explanation of the observed gap. If they succeed, the practical bottleneck is training depth rather than architectural impossibility — a substantially different conclusion. This experiment is straightforward to run and directly connects the theory to the empirical claims.

2. **The 82% gap attribution rests on an unvalidated heuristic.** The AR hit heuristic (repeated bigram with training frequency ≤ 1250) is a coarse proxy. The paper transparently acknowledges this (line 101: "It is challenging to derive a quantitative measure of associative recall performance on the Pile because we don't know which next token predictions in raw text require associative recall"), but the central quantitative result — that 82% of the gap is "explained by" AR — inherits all the heuristic's limitations. The heuristic does not verify that the token's difficulty is *caused by* the need for recall rather than by other distributional properties (e.g., these tokens may concentrate in certain syntactic positions or genres). The paper uses causal language ("82% of the gap is explained by each model's ability to recall information," abstract) where the evidence supports only a correlational claim: AR hits account for 82% of the perplexity gap under a specific operational definition. While this is still informative, the interpretation should be softened to reflect the heuristic's limitations.

### Minor

3. **No ablation of the number or placement of attention layers in hybrids.** The paper uses 3 attention layers out of ~30–50 in the hybrids but does not test whether 1 layer suffices, or whether attention must be placed at specific depths (first layers, last layers, or distributed). This underdetermines the "minimal modifications" claim: the observed improvement could partly reflect any added capacity rather than input-dependence for recall specifically.

4. **No sensitivity analysis of the learned selection's k hyperparameter.** The learned selection uses k=256 and closes 72% of the gap, but the paper does not report performance at other values of k (e.g., k=64 or k=512). This is needed to assess how efficiently the learned selection uses its attention budget and whether the gap closure is robust.

5. **The 18% residual gap is left unanalyzed.** The paper's narrative implies AR is the dominant issue, but 18% of the gap is not explained by AR hits. Analyzing what other capabilities gated convolutions lack would be valuable for future architecture design.

### Trivial
None.

## Nice-to-Haves

- Validate the AR hit heuristic via human judgments or a controlled dataset where recall requirements are known, to ground the 82% claim more strongly.
- Compare programmatic selection to a stronger control: attention with a learned but input-independent (e.g., fixed-stride) sparsity pattern, which would better separate the effects of input-dependence from sparsity.
- Report per-architecture breakdown of the percentage of gap attributed to AR hits (not just the average).
- Report wall-clock training throughput and GPU hours for the hybrid architectures alongside theoretical FLOPs, since actual efficiency matters for "efficient language models."

## Removed Points

These points are flagged as removed; treat them with caution:

- **"1250 threshold is arbitrary":** The threshold is explicitly justified as filtering common bigrams likely memorized during training (line 102). A single threshold is a simplification but not a flaw — the main Figure 1 shows the gap varies smoothly with frequency, supporting the qualitative conclusion regardless of the exact cutoff.
- **"AR heuristic conflates distinct phenomena (proper names, function words, etc.)":** Speculative — the paper does not provide evidence that these subtypes behave differently, and the heuristic is transparently defined.
- **"Programmatic selection costs O(N) memory/scanning":** O(N) is sub-quadratic and trivially compatible with the paper's efficiency claims. Not a flaw.
- **"Proposition 1 assumes attention without softmax":** The paper explicitly states "even without using soft-max" (line 197) — the authors are aware and this is standard practice in theoretical analyses.
- **"Poly-log blowup not specified more precisely":** Standard \tilde{O} notation in theory papers, where poly-log factors are intentionally hidden. This is convention, not a flaw.
- **"Random selection control doesn't control for position":** The random baseline is a standard control showing that unstructured sparsity does not close the gap. A fixed-stride control would be a stronger comparison but the current control is informative as-is.
- **"Missing appendix content / proofs":** These are stripped by PDF parsing; they exist in the original submission.
- **"Missing related works":** Cannot be verified — the paper may cite relevant works in the stripped appendix.
- **Formatting nits, typos, punctuation issues, garbled characters:** Parser artifacts, not author errors.

## Novel Insights

The key synthesis across the two reviews is that the paper's contributions are asymmetric in strength: the *empirical findings* (gated convolutions underperform on repeated bigrams, sparse attention on those positions closes the gap) are solid, practically useful, and well-supported; the *theoretical framing* as an explanation of the gap is more tentative than the paper's narrative suggests. The theory proves that gated convolutions *could* solve MQAR with sufficient depth — which implies the observed failure is about *learning efficiency* or *practical depth constraints* rather than architectural impossibility. This distinction is important: the paper's empirical intervention (adding a small amount of input-dependent mixing) works, but the mechanism by which it works may be simpler than the paper claims (adding expressivity at key positions rather than fundamentally overcoming a representational bottleneck). The MQAR framework itself is the most durable contribution — it provides a better diagnostic than prior synthetic tasks regardless of whether the theoretical bounds are tight.

## Suggestions

1. **Test depth scaling on synthetic MQAR.** Run the Figure 2 experiment with 4- and 8-layer gated-convolution models. If deeper models solve MQAR at smaller widths, this would directly validate the theory's prediction and strengthen the claim that insufficient depth is the practical bottleneck. If they still fail at all widths, the theory would need revision.

2. **Ablate the number and placement of attention layers in hybrids.** Test whether 1 attention layer (instead of 3) suffices, and whether attention must be placed at specific depths (e.g., only the last layers, only the first, or distributed). This would tighten the "minimal modifications" narrative and potentially reduce the overhead of the proposed fix.

3. **Soften the causal language around the 82% figure.** Reframe this as: "AR hits, under our heuristic definition, account for 82% of the perplexity gap" rather than "the gap is explained by failure of associative recall." The heuristic is reasonable but cannot distinguish causation from correlation.

4. **Ablate the k hyperparameter in learned selection** (e.g., k = 64, 128, 256, 512) to show sensitivity and help practitioners choose the attention budget.

5. **Briefly discuss what might cause the residual 18% gap** — even a speculative paragraph would be valuable for guiding future architectural research.
