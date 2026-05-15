Now I have a thorough understanding of the paper and have verified every critic claim against the actual text. Let me produce the consolidated review.

---

## Summary

This paper studies LLM training stability using an 830M-parameter model trained at high learning rates to force divergence. It extends prior work (SMALL, VISION) by analyzing L2 norms of all linear-layer outputs (not just attention logits) during divergence, identifying that QKV, Proj, and FC2 outputs grow most severely. Based on this analysis, the paper proposes and evaluates several normalization strategies: QK_FC_norm (adding LN after Proj and FC2 alongside QK LN), QKV_norm (removing pre-QKV LN and adding post-QKV LN), and QK_norm_cap (QK LN combined with softmax capping). The two latter methods achieve a 1.5× higher stable learning rate compared to QK_norm alone, and all three methods show perplexity improvements (10.84–11.00 vs. 11.19 baseline) when trained at a normal learning rate.

## Strengths

- **Systematic divergence analysis across all linear layers**: The paper measures L2 norms of weights, inputs, and outputs for QKV, Proj, FC1, and FC2 layers in converged and diverged models (Table L2_NORM). It identifies that QKV, Proj, and FC2 outputs grow >2× during divergence, which extends prior work that focused only on attention logits (VISION, SMALL) and directly motivates the proposed normalization placements.

- **Two methods achieve a clear 1.5× improvement in stable learning rate**: Table DIVERGE shows that QKV_norm and QK_norm_cap converge at LR=60e-3 while the strongest prior methods (QK_norm, soft_cap) diverge at that rate. This is a practically meaningful stability improvement demonstrated on a controlled experimental setup.

- **Thorough side-by-side comparison of multiple stability methods**: The paper evaluates seven baseline/modified methods (σReparam, soft_temp, soft_cap, soft_clip, LayerScale, QK_norm, QK_FC_norm) under identical model architecture, training data, and learning rate schedule in Table DIVERGE, providing a useful unified benchmark.

- **Clarifying negative result**: QK_FC_norm (adding LN after Proj and FC2) shows no stability improvement over QK_norm alone. This negative result is informative — it suggests the primary divergence bottleneck resides in the QK/QKV layers rather than later projections, testing the paper's own hypothesis directly.

- **Perplexity improvements accompany stability gains**: Table PPL shows that the proposed methods yield perplexity 10.84–11.00 vs. baseline 11.19 and soft_cap 11.24 after 0.2T tokens, indicating that the architectural changes that improve stability do not degrade — and in fact improve — model quality.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The 1.5× LR improvement claim rests on single-seed experiments with a coarse grid**. The divergence thresholds in Table DIVERGE are determined from a single initialization seed and a coarse LR grid (6e-3, 8e-3, 20e-3, 40e-3, 60e-3, 80e-3). The 1.5× claim depends on exactly one grid step (QKV_norm/QK_norm_cap converge at 60e-3 whereas QK_norm diverges at 60e-3). While using the same seed across all methods controls for initialization, multiple seeds and a finer grid would establish whether the precise magnitude of the improvement is statistically robust. Adding intermediate LRs (e.g., 50e-3, 70e-3) would also clarify the exact threshold.

- **The divergence criterion is not formally defined**. The paper states it checks "validation loss function as described in section DIV," but Section DIV only shows an example plot with one "converges" curve and one "diverges" curve. No formal threshold (e.g., NaN loss, loss exceeding N× the minimum, rate of increase) is specified. This makes the binary classification in Table DIVERGE ambiguous and difficult to reproduce precisely.

- **QKV_norm design conflates two architectural changes without full ablation**. The QKV_norm method simultaneously removes the pre-QKV LN and adds post-QKV LN. The paper motivates this with a hypothesis (pre-LN is redundant because QK LN already normalizes the signals), but does not test intermediates (e.g., removing pre-LN without adding post-QKV LN, or adding post-QKV LN while keeping pre-LN). A full 2×2 factorial ablation would strengthen the mechanistic claim that the post-QKV LN is the critical addition and that removing pre-LN is harmless.

- **The perplexity comparison is not controlled for number or placement of LN layers**. The methods in Table PPL add or reposition LN layers compared to the bf16 baseline. The fact that all such methods achieve lower perplexity (10.84–11.00 vs. 11.19) while soft_cap (which does not add LN) does not improve perplexity (11.24) is suggestive, but the paper does not include a control that adds LN in a position believed to be irrelevant to stability. This would help disentangle whether the perplexity improvement stems from the stability mechanisms specifically or simply from adding more normalization layers. The observation is still empirically valid — these architectures achieve better perplexity — but the causal attribution could be sharper.

- **The use of proprietary training data limits full reproducibility**. The paper trains on a mixture of public and proprietary datasets. While this is common in industrial LLM research, it prevents exact reproduction of the perplexity numbers or divergence behaviors by third parties.

### Trivial

- The softmax clipping hyperparameters (ζ=1.03, γ=-0.03) and softmax capping value (capping=50) are presented without sensitivity analysis or justification.
- The confidence interval reported in Table PPL ("±0.1 at 95% level") is stated without explaining the computation method (e.g., bootstrap over evaluation examples, or multiple runs). This is a minor transparency issue.
- The softmax demonstration (Figure SOFT) is pedagogical rather than quantitative — it illustrates why large logit magnitudes cause attention collapse in general but does not directly measure this mechanism in the actual trained models.

## Nice-to-Haves

- Repeating the divergence threshold experiments with at least 3 seeds per LR per method and reporting the fraction of runs that diverge would improve statistical rigor.
- A finer-grained LR grid (e.g., adding 50e-3, 70e-3) would sharpen the precision of the 1.5× claim.
- For QKV_norm, testing the four variants (pre-LN only, post-QKV LN only, both, neither) would isolate the contribution of each design choice.
- Extending the methods to larger model scales (1B, 7B) or to downstream task evaluation would increase the impact and generalizability.

## Removed Points

These points are flagged to be removed, treat them with caution:

- "The perplexity comparison is confounded and does not support the claimed improvements" — The critic claimed that the perplexity drop could be entirely due to added normalization capacity independent of stability. However, the paper reports an empirical comparison of architectures at the same learning rate; the finding that these specific architectures achieve lower perplexity is a valid empirical result regardless of mechanism. The claim is not about causal attribution to "stability mechanisms" vs. "extra normalization" — it is an empirical observation about the methods as designed. The criticism overstates the issue. (Kept a softened version about lack of control for number of LN layers as a minor weakness.)
- "With only a single run, confidence intervals are invalid" — Confidence intervals on perplexity can be validly computed from evaluation variance across test-set examples using a single trained model. The paper does not explain the computation, but the CI is not inherently invalid.
- "The softmax demonstration does not prove this is the mechanism" — The softmax figure is an illustrative example; the actual evidence for the mechanism comes from the L2 norm and gradient analyses (Tables L2_NORM, GRAD). The paper does not claim the figure alone proves causality.
- Various formatting/style nitpicks and complaints about missing appendix content — these reflect PDF extraction artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The key insight — that normalizing QKV output (and removing redundant pre-QKV LN) or combining QK LN with softmax capping each yield 1.5× higher stable LR than QK LN alone — is the paper's primary novel contribution. The secondary insight — that normalizing Proj and FC2 outputs does not further improve stability despite those layers exhibiting large magnitude growth during divergence — is a useful negative result that narrows the search space for future stability work.

## Suggestions

1. Clarify the divergence criterion with an explicit formal threshold (e.g., loss exceeds 2× the converging minimum, or NaN, or a sustained upward trend).
2. Add at least one additional seed to the divergence threshold experiments to demonstrate that the 1.5× advantage is not initialization-specific.
3. For QKV_norm, include an ablation that adds post-QKV LN without removing pre-LN to confirm that removing pre-LN is non-harmful.
4. Explain how the confidence interval in Table PPL was computed.
5. Consider adding a control model with extra LN in a non-stability-relevant position to help interpret whether the perplexity gains are specific to the proposed LN placements.

## Score and Decision

The paper addresses a practically important problem with a well-motivated methodology. The core empirical claims — that QKV_norm and QK_norm_cap improve stable learning rate by 1.5× over QK_norm and yield better perplexity at normal learning rates — are supported by the data presented, despite minor methodological caveats (single-seed thresholds, limited ablation depth). The systematic comparison of seven stability methods on a unified setup is a useful contribution. The weaknesses identified are minor and addressable; none undermine the paper's core contributions.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>