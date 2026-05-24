Now I have sufficient anchors. Let me produce the final consolidated review.

## Summary

This paper investigates output alignment for 1-bit post-training quantization (PTQ) of LLMs. It identifies three failure modes of naive output matching: (1) layer-wise output matching doesn't guarantee block-level loss reduction, (2) quantization errors accumulate across layers, and (3) output matching can degrade attention mechanisms. To address these, it proposes a selective block-level output alignment strategy that accounts for accumulated errors via an "Output Error" objective, and introduces an Attention Matrix Preservation (AMP) mechanism. Experiments on OPT (1.3B-30B), LLaMA-2 (7B, 13B), and LLaMA-3 (8B) show improvements over prior 1-bit PTQ methods across most settings.

## Strengths

1. **Diagnoses genuine failure modes of naive output matching**: The paper clearly identifies and experimentally demonstrates three problems with layer-wise output alignment in 1-bit PTQ. The preliminary analysis (Section 3) is informative — Figure 1 shows that minimizing layer-level output loss can actually increase block-level loss for some layers, and Figure 2 quantifies how error accumulation causes the ARB-X objective to diverge from the true target as depth increases. This analysis is a genuine contribution.

2. **Consistent improvements over prior 1-bit PTQ methods across most settings**: Table 1 shows that the proposed method outperforms PB-LLM, BiLLM, ARB-RC, and ARB-X on all OPT model sizes (1.3B-30B) across C4, WikiText2, and PTB datasets. For OPT-1.3B, improvements over ARB-RC are meaningful (e.g., C4: 27.70→24.69, PTB: 43.03→38.18). Table 2 shows similar gains on LLaMA models on C4 and WikiText2, and on PTB for LLaMA-2-13B and LLaMA-3-8B.

3. **Ablation studies validate the design choices**: Table 3 shows that removing AMP causes LLaMA-2-7B perplexity on C4 to jump from 19.25 to 29.12 (~10 points), confirming AMP's importance for LLaMA architectures. Table 4 shows that using Output Error instead of Activation-conditioned Error provides a 0.7 perplexity improvement on C4, validating that accounting for accumulated errors matters.

4. **Closed-form update derivation**: The paper derives analytical solutions (Eqs. 5-8) for quantization parameters α_r, α_c, and B under the Output Error objective. This avoids iterative gradient-based tuning and is a technically sound contribution.

## Weaknesses

### Fatal

None.

### Major

1. **Mathematical error in the AMP derivation (Eq. 9)**: The paper writes `max L_AMP = || (X̂ŴŴ^T X̂^T) ⊙ (XWW^T X^T) ||` and then equates this to `Tr[X̂ŴŴ^T X̂^T XWW^T X^T]`. This step is not mathematically justified: the (squared) Frobenius norm of a Hadamard product equals `sum_ij (a_ij·b_ij)^2`, while the trace equals `sum_ij a_ij·b_ij`. These are different quantities. The trace formulation from line 144 onward (using the Frobenius inner product ⟨A, B⟩_F = Tr[AB^T]) is a reasonable objective for maximizing alignment, but the paper's opening line with the Hadamard product and norm is incorrect. This means the central AMP mechanism, which Table 3 shows is responsible for ~10 perplexity points on LLaMA, is presented with flawed mathematics. The mechanism itself (masking updates based on gradient signs of a similarity preservation objective) is plausible, but the derivation must be corrected.

2. **PTB failure on LLaMA-2-7B is dismissed rather than analyzed**: On LLaMA-2-7B PTB, the method achieves perplexity 3166, which is substantially worse than PB-LLM (657), ARB-RC (763), and ARB-X (681). The paper states "the large perplexity indicates that the metric cannot provide a meaningful evaluation" — this is not an acceptable justification. PTB is a standard benchmark used by all baselines in the same evaluation suite, and those baselines obtain meaningful numbers. The paper should analyze why this failure occurs (e.g., domain sensitivity of the AMP mechanism, calibration data distribution mismatch) rather than dismissing the metric. This failure also contradicts the abstract's claim of "consistently outperforming" existing methods.

3. **Selective layer-wise strategy lacks empirical justification**: The paper restricts output alignment to "only the last fully connected layer of each block" because it "has the most direct impact on the block loss" (Section 4.2). However, no ablation or analysis is provided to support this claim. The preliminary analysis (Figure 1) shows that ARB-X outperforms ARB on most layers but underperforms on some — but it does not identify which layers those are or why the last layer is the critical one. Without such evidence, the design choice appears arbitrary. Since Table 3 shows AMP is the dominant contributor (especially for LLaMA), the selective strategy may add unnecessary complexity without demonstrable benefit.

### Minor

1. **Equation (2) typo**: The paper writes `||X̂Ŵ - X̂Ŵ||_F^2` which is identically zero; the intended expression is clearly `||X̂W - X̂Ŵ||_F^2` (the ARB-X objective). This is a minor typo but should be fixed.

2. **Improvements over ARB-RC narrow substantially on larger models**: On OPT-30B C4, the improvement over ARB-RC is 13.34→13.15 (0.19). On LLaMA-2-7B C4, it's 20.4→19.25 (1.15). The paper does not report statistical significance or variance, making it unclear whether smaller gaps are meaningful. While single-run reporting is standard in this field, the most critical comparisons would benefit from some indication of reliability.

### Trivial

1. Equation (2) typo (||X̂Ŵ - X̂Ŵ|| instead of ||X̂W - X̂Ŵ||).

## Nice-to-Haves

- Reformulate the AMP objective more cleanly: replace the incorrect `||A ⊙ B||` with the Frobenius inner product `⟨A, B⟩_F = Tr[AB^T]`, and clarify why maximizing this preserves token similarity structure. This would resolve the mathematical concern without altering the actual algorithm.
- Provide an ablation comparing the last-layer selection against other choices (e.g., first layer, all layers, or a data-driven selection) to justify the design.
- Report zero-shot results for LLaMA models (mentioned as in the appendix but not included in the main text).
- Include a brief discussion of computational overhead in the main paper rather than deferring entirely to the appendix.

## Removed Points

These points were flagged by reviewers but removed after verification against the paper:

- "The AMP objective is ill-posed because maximizing a norm is unusual": The paper's intent is clearly to maximize alignment between similarity matrices, which is standard practice. The issue is only in the first line of Eq (9); the trace-based formulation from line 144 onward is well-defined.
- "No justification for why a binary mask (sign) is used": Using sign-based masking for binary decisions in quantization is standard practice. The reviewer's concern is not specific to this paper.
- "Missing related works": Cannot be verified without external sources; per guidelines this should not be mentioned.
- "No statistical significance reported": This is the norm for 1-bit PTQ papers; most cited baselines also report single-run results.
- "Calibration details missing": The paper states experiments follow prior work; the details are standard for the field.
- "Overhead analysis relegated to appendix": This is a presentation choice, not a weakness of the work. The paper states overhead details are in Appendix D.
- Generic strength about "important problem" from the strength finder: Removed as generic/superficial.

## Novel Insights

The synthesis of the three failure modes of output matching — block-level misalignment, error accumulation, and attention degradation — and their varying severity across architectures (OPT vs. LLaMA) is the paper's most interesting insight. The finding that AMP is far more impactful for LLaMA (10+ perplexity points) than for OPT (~0.1-0.2 points) and the hypothesis that this relates to RMSNorm vs. LayerNorm is a genuine architectural insight worth further investigation. The connection between normalization strategy and sensitivity to attention-preserving quantization is not something prior 1-bit PTQ work has explored.

## Suggestions

1. **Fix the AMP derivation**: Replace the incorrect `||A ⊙ B||` with the Frobenius inner product `⟨A, B⟩_F = Tr[AB^T]`. This does not change the algorithm (the trace formulation and gradient computations are correct), but the mathematical presentation must be accurate.
2. **Acknowledge and analyze the PTB failure**: Either provide an explanation for why the method fails on LLaMA-2-7B PTB, or temper the "consistently outperforms" claim to acknowledge this exception.
3. **Justify the selective layer choice**: Add a simple ablation comparing last-layer, first-layer, all-layer, and random-layer output alignment to validate the design choice.
4. **Tone down the abstract claim**: Replace "consistently outperforms" with more precise language that acknowledges the specific settings where the method excels and where it doesn't.

## Score and Decision

**Round 1 bracketing**: Paper sits between weak anchors at ~3.0-3.5 (e.g., "1-Bit Quantization Meets Structured Pruning" at 3.20) and strong anchors at ~7.5+ (which are on non-quantization topics). The relevant middle band is 3.5-7.5, narrowed to approximately 4-6.

**Round 2 narrowing**: Retrieved anchors:
- DBellQuant (4.00, Reject): Similar-level PTQ paper with worse reproducibility issues and less thorough evaluation. Our paper is stronger.
- Rethinking 1-bit Optimization (4.00, Reject): Had similar PTB confusion issues but our paper has more complete evaluation.
- PBS2P (4.50, Reject): Comparable in quality. Our paper has more novel analysis but also similar-level weaknesses.
- PT^2-LLM (4.50, Accept Poster): Comparable in quality. Similar strengths (good empirical results) and similar-level weaknesses (unsubstantiated claims, weak theoretical grounding for one component).
- TurboBoA (4.80, Accept Poster): Stronger in mathematical rigor and empirical evaluation. Our paper is weaker.

The most direct comparators are PBS2P (4.50) and PT^2-LLM (4.50). Our paper has comparable analytical depth and empirical breadth, but the AMP math error and the PTB dismissal are more severe shortcomings than what those papers faced.

**Final score**: 4.5. The paper identifies genuine problems and proposes a reasonable framework, but the mathematical error in a core component and the dismissal of a clear failure case prevent it from being above this threshold. The underlying ideas are worth pursuing, but the paper needs substantial revision before acceptance.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>