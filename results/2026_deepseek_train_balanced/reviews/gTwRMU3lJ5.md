## Summary

This paper introduces LoRA-Pro, a PEFT method that adjusts the gradients of LoRA's low-rank matrices so that their "equivalent gradient" on the weight matrix better approximates the full fine-tuning gradient. The key theoretical contribution is a closed-form solution (Theorem 1) showing that optimal adjusted gradients can be expressed in terms of the standard LoRA gradients without explicitly requiring the full gradient tensor. The method is evaluated across NLU (T5-base), dialogue/math/code (Llama-2-7B), and image classification (CLIP-ViT-B/16), consistently outperforming baselines including LoRA, LoRA+, DoRA, and LoRA-GA while adding only ~1% training time overhead.

## Strengths

- **Novel theoretical connection between LoRA and full fine-tuning.** Section 2.2 establishes that updating A and B with gradients g^A and g^B is equivalent to updating W with a virtual low-rank gradient \tilde{g} = s B g^A + s g^B A. This is a precise, non-trivial insight that grounds the method in a rigorous optimization framework rather than heuristic intuition.

- **Closed-form optimal solution that avoids materializing the full gradient.** Theorem 1 proves that the optimal g^A and g^B minimizing ||\tilde{g} - g||^2_F can be expressed using only the standard LoRA gradients (g^A_{lora}, g^B_{lora}) and small r×r matrix operations. The second form of each equation in Theorem 1 (lines 184-186) shows this explicitly. This makes the method practical — the adjustment step operates on r×r matrices rather than requiring the m×n gradient tensor.

- **Consistent improvements across diverse domains with minimal overhead.** Tables 1-3 show LoRA-Pro outperforming all PEFT baselines on NLU (88.44 average on GLUE vs. full FT's 87.91), LLM tasks (e.g., HumanEval at r=128: 34.55 vs. full FT's 35.31 and LoRA-GA's 23.05), and image classification (best on all 7 datasets). Table 5 shows this comes at only ~0.8 GB extra memory and ~1% training time — because all extra computations involve small r×r matrices (lines 517-522).

- **Loss decrease guarantee.** Theorem 2 (lines 218-225) proves that the proposed updates ensure dL ≤ 0, expressed as a negative sum of two Frobenius norms. This is stronger than the heuristic guarantees of most LoRA variants and addresses the natural concern that naively matching gradients could compromise loss minimization.

- **Empirical validation of the full-rank assumption.** Figure 1 (lines 470-483) tracks rank dynamics and confirms that A and B achieve full rank after the first update step, supporting the condition required by Theorem 1's closed-form solution.

## Weaknesses

### Major

- **No direct measurement of gradient alignment during training.** The entire method is motivated by minimizing ||\tilde{g} - g||^2_F — the paper defines the objective in Eq. 4, derives optimal solutions, and claims this bridges the gap with full FT. Yet it never reports this norm during training. A plot of ||\tilde{g} - g||_F over training steps for LoRA-Pro vs. vanilla LoRA would directly validate whether the adjustment achieves its intended effect. Without it, the gradient-matching mechanism is assumed rather than verified. This is the single most important missing experiment for a method whose core thesis is gradient alignment.

### Minor

- **LoRA-GA omitted from image classification experiments (Section 4.3).** The paper compares against LoRA, rsLoRA, LoRA+, and DoRA on 7 image classification datasets, but excludes LoRA-GA — the closest prior work and the primary competitor on NLU and LLM tasks. The paper claims "To provide a comprehensive comparison" (line 420) yet omits the most informative baseline. LoRA-Pro already achieves state-of-the-art against the included baselines, so this doesn't threaten the results, but it leaves a gap in the evidence across this domain.

- **The practical advantage of the Sylvester equation solution for X is unclear from the ablation.** Table 4 shows the Zero solution (X=0) achieving GSM8K 53.83 vs. Sylvester 54.23 (diff 0.40), and HumanEval 22.96 vs. 22.76 (Zero marginally better). The paper justifies choosing Sylvester by citing "high variance" in the Zero solution (std 1.96 vs. 0.35 on HumanEval), which is reasonable, but the mean differences are small. The paper would benefit from acknowledging that the Sylvester equation's practical benefit over simpler alternatives is modest, or providing evidence (e.g., additional datasets) where it clearly matters.

- **Overfitting explanations invoked without supporting evidence.** The paper attributes LoRA-Pro surpassing full FT on NLU (line 313) and underperforming on MT-Bench (lines 380-381) to overfitting in full fine-tuning. These are plausible but remain speculative — the paper provides no training-set accuracy curves, loss trajectories, or other empirical evidence to support the claim. Adding these would strengthen the narrative.

- **First training step under the full-rank assumption is not explained.** Theorem 1 assumes A and B are full-rank. The paper acknowledges (line 473) that B is initialized as zero and thus not full-rank initially, and shows both matrices become full-rank after one update. But it does not explain what update is used for this first step — since (B^TB)^{-1} is undefined when B=0, the first step presumably falls back to standard LoRA updates or another mechanism. A brief implementation note would improve reproducibility.

### Trivial

- None.

## Nice-to-Haves

- Including a measurement of ||\tilde{g} - g||_F over training steps for LoRA-Pro vs. vanilla LoRA would directly verify the gradient-matching mechanism.
- Adding LoRA-GA to the image classification comparison would complete the evaluation picture.
- Providing training accuracy/loss curves to support the overfitting explanations.
- Reporting whether the first training step uses a fallback (e.g., standard LoRA gradients) before the full-rank condition is met.
- Statistical significance tests for the headline comparisons (e.g., LoRA-Pro vs. LoRA-GA on HumanEval).

## Removed Points

These are criticisms from the original reviewer inputs that were filtered out after verification against the paper:

- **Criticism that the "not explicitly depend on g" claim is misleading:** Removed. The claim is technically correct in both forms presented in Theorem 1. While g is used to compute g^A_{lora} in the backward pass (standard in any LoRA variant), the closed-form solution for the adjusted gradients g^A, g^B can be expressed without g explicitly appearing. The framing is slightly inflated but not false.
- **Criticism about statistical rigor (no significance tests):** Downgraded to Nice-to-Have. Reporting means and std from 3 runs is standard practice in this field; significance tests are not the norm.
- **Criticism that X-selection ablation undermines "claimed importance" of Sylvester equation:** Demoted from the harsh critic's "Critical Issue" to Minor. The paper presents the ablation honestly and acknowledges the high-variance issue. The Sylvester solution is theoretically principled, and its practical improvement, while modest, is directionally positive on two of three metrics with lower variance.
- **Strength Finder strengths about generic problem importance:** Removed. The strengths kept are all specific to this paper's concrete contributions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a training-time plot of ||\tilde{g} - g||_F for LoRA-Pro vs. vanilla LoRA across steps. This single experiment would provide the missing link between motivation and results.
2. Either include LoRA-GA in the image classification experiments, or explicitly note the reason for its absence (e.g., if LoRA-GA's original paper does not report image classification results and reproducing it would be non-trivial).
3. Briefly note how the first training step is handled when B=0 (fallback to standard LoRA gradients?).
4. Add training-set accuracy/loss curves to support the overfitting claims about full FT vs. LoRA-Pro.
5. Consider adding a brief discussion of when X matters more (perhaps at higher ranks or on specific task types) to contextualize the ablation results.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>