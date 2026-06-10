## Summary

This paper proposes EfficientSkip, a training paradigm that converts a dense pre-trained transformer LLM into a sparse variant where tokens can skip individual layers. The method introduces binary gates with a borrowed-gradient trick applied to both attention and FFN sub-blocks, uses a KL divergence threshold to adaptively control the skip rate, and employs LoRA-based continual pre-training on only millions of tokens. Experiments on Gemma 2B instruction-tuned with MT-Bench demonstrate feasibility of the approach, and ablations provide insights into gating design choices and skip patterns.

## Strengths

- **Dense-to-sparse transformation demonstrated with extremely limited resources.** The paper shows that a 2B parameter LLM can be converted into a sparse variant using only ~6 hours of training per 1M tokens on a single A100 GPU (Section 4.2), producing skip rates at reported MC values around 0.2 (Section 4.4). This directly supports the core claim that dense-to-sparse conversion is possible without training from scratch, contrasting with MoD-style approaches that require orders of magnitude more data.

- **Binary gates (not continuous weights) shown to be necessary for the dense-to-sparse setting.** The ablation in Section 4.8 (Table 1) provides direct evidence: when continuous weights (as in MoD) are substituted for binary gates, training "failed to converge during continual pre-training." This is a genuine architectural insight — pre-trained weights cannot easily adapt to distorted hidden states they have never seen, whereas binary gates avoid that distortion. The borrowed-gradient trick (Eq. 114–117) is a clean solution.

- **Adaptive skip ratio via KL divergence threshold, unlike fixed-ratio approaches.** The threshold-based loss gating (Section 3.3) learns how many tokens to skip based on content, rather than imposing a fixed skip ratio per sentence as in MoD. Section 4.6 shows that the relationship between threshold and ΔSkip is close to linear, offering practical control.

- **Comprehensive intra-method ablations with quantitative MC comparisons.** Table 1 reports four ablations (no gating on attention → +0.71 MC, weights vs. binary gates → training fails, k-to-all vs. k-to-k attention → +1.48 MC, partial parameter freezing) with MC differences large enough to be meaningful. These provide empirical justification for each design decision.

- **Mechanistic explanation of why skipped layers do not harm output.** Section 4.9 demonstrates that the per-layer output vectors of skipped tokens have near-uniform softmax distributions (entropy close to ln(V), shown in Figure 6), providing a theoretical grounding for why tokens can skip layers without perturbing the final distribution.

- **POS-tag analysis yielding non-obvious findings.** The case study (Section 4.10, Figure 7) reveals specific patterns: numbers are the most-skipped POS tag, conjunctions the least-skipped, and no tokens skip the first three or last two layers. These are concrete, non-trivial observations.

## Weaknesses

### Fatal

None.

### Major

1. **No baseline comparisons.** The experiments contain zero comparisons against any alternative approach — not MoD, not random skipping, not early-exit methods, not CODA. Every result compares variants of EfficientSkip against other variants of EfficientSkip. This is a structural gap because the contribution implies the learned skipping is better than trivial alternatives, but there is no evidence to support that claim. For example, does the learned router outperform skipping the same proportion of layers at random? Does it outperform a fixed-skip heuristic (e.g., skip every even-numbered layer)? Without such baselines, the reader cannot assess whether the method produces useful skipping or merely *some* skipping. The paper's framing explicitly contrasts with MoD (lines 21, 23), yet no comparison is made. Addressing this requires a fundamentally different experimental design.

2. **Raw MT-Bench scores are never reported, making MC uninterpretable in isolation.** The paper exclusively reports MC = ΔPerf / ΔSkip, where ΔPerf is the *percentage* performance loss relative to the base model. No absolute MT-Bench scores are given for either the base model or any transformed model. Since the base model's absolute score is unknown, a claim like "MC ≈ 0.2, meaning we lose 20% of a performance unit per full unit of skip" cannot be translated into a practical assessment of model quality. A model losing 20% relative performance dropping from 6.0 to 4.8 is very different from dropping from 9.0 to 7.2. The MC metric is a useful secondary measure but cannot substitute for reporting primary performance numbers, especially given MT-Bench's known variance on 80 questions. Without raw scores, the evidence does not reveal what quality of model the method actually produces.

3. **Insufficient evaluation scope.** The method is evaluated on a single model (Gemma 2B instruction-tuned) using a single benchmark (MT-Bench, 80 questions). No perplexity evaluation is reported (which would directly validate whether the KL threshold controls distributional deviation), and no standard reasoning/knowledge benchmarks (MMLU, HellaSwag, ARC, etc.) are included. This matters because: (a) MT-Bench's small size means differences may not be statistically reliable; (b) instruction-tuned models may behave differently from base models; (c) the 2B scale leaves unclear whether the method generalizes to larger models where efficiency gains would matter more. The paper cannot support claims of general applicability with only one model and one benchmark.

### Minor

- **Inference speedup under-quantified.** Figure 5 shows that relative inference time decreases with ΔSkip, but the paper provides no wall-clock speedup numbers, no breakdown of overhead sources, and no quantification of the acknowledged KV-cache overhead (line 209: "calculation of KV-cache even if the layer is skipped"). For a method whose purpose is efficiency, the reader needs to know: at a realistic skip rate (e.g., 50% of layers skipped), what actual speedup is achieved, and how much is consumed by overhead?

- **Some claims are over-interpreted.** The paper states that "Numbers are more likely to skip layers... This explains why Gemma 2B is performing badly on math as it is not sensitive to numbers" (Section 4.10). This is post-hoc reasoning from a correlation observed on a single generation. Gemma 2B may perform badly on math for many other reasons (model size, training data, tokenization). The causal claim is not supported.

- **The loss gating formulation is ambiguous for a critical edge case.** Equation 9 defines the loss only for ℒ_KL < t; the "else" case (ℒ_KL ≥ t) is described in text but not given an explicit equation. The sg(ℒ_skip) term appears in the shown expression but it is unclear how it behaves when ℒ_KL ≥ t.

### Trivial

None.

## Nice-to-Haves

- Reporting per-category MT-Bench breakdowns would make the POS analysis more actionable and reveal which tasks tolerate more skipping.
- Perplexity on held-out data would directly validate whether the KL threshold effectively controls distributional deviation from the base model.
- Testing at a larger scale (e.g., 7B) would substantially strengthen generalizability claims.

## Removed Points

The following points from the inputs were removed as per the filtering guidelines:

- **Criticism about missing hyperparameters (LoRA alpha, dropout, optimizer settings).** The rule against nitpicks about undisclosed trivial implementation details applies here: the paper reports learning rate (1e-5), batch size (4), LoRA rank (64), training time (~6 hrs/1M tokens), and training data selection method. The remaining unspecified details (optimizer choice, LoRA alpha, dropout) are standard defaults in the QLoRA ecosystem and do not threaten reproducibility.
- **Criticism that "90K being optimal... if the method degrades with more data, that is a significant limitation."** The paper already acknowledges this counterintuitive finding and offers a plausible explanation (distribution mismatch with SlimPajama). It is presented as an empirical observation, not a failure, and the paper does not claim to solve scaling. This is a finding, not a weakness.
- **Criticism about "no guidance on how to select threshold for a different model."** This is a generic request; threshold selection is standard hyperparameter tuning for any method and not specific to this paper.
- **Strength Finder's claim that "MC scores around 0.2" is the single most important evidence.** This overstates the conclusiveness of MC without raw scores; the strength is retained in the review but calibrated.

## Novel Insights

None beyond the paper's own contributions. The key insight — that binary gates are necessary for dense-to-sparse conversion because pre-trained weights cannot adapt to distorted hidden states — is genuinely novel and well-supported by the ablation. The finding that skipped layers produce near-uniform distributions (Section 4.9) is a useful mechanistic analysis. However, these insights are already presented in the paper.

## Suggestions

1. **Report absolute MT-Bench scores** for the base model and every transformed configuration, alongside the MC metric. This is the single highest-impact improvement.
2. **Add at least two baseline comparisons:** (a) random skipping at matched skip rates, and (b) a fixed-skip heuristic (e.g., skip all even-indexed layers). These are cheap to run and would directly validate whether the learned router adds value.
3. **Quantify wall-clock speedup** with a breakdown of overhead (attention computation for skipped tokens, router evaluation cost, KV-cache overhead). A table showing actual inference time (in seconds) at different ΔSkip values would clarify practical utility.
4. **Add perplexity on a held-out dataset** to validate that the KL threshold controls distributional deviation as claimed.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>