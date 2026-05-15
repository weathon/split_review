Here is my consolidated review:

---

## Summary

This paper proposes three stabilized components for Transformer training — StableInit (a modified initialization), StableNorm (a normalization with tunable exponent \(d^\alpha\) instead of \(\sqrt{d}\)), and StableAtten (a stabilized attention mechanism) — and combines them into a "Stable-Transformer." The paper presents a Jacobian analysis for StableNorm, showing that replacing \(\sqrt{d}\) with \(d^\alpha\) (\(\alpha<0.5\)) scales down gradients. Experiments on GPT2-Small (124M), GPT2-Medium (350M), and ViT-Large show modest performance improvements (e.g., 2.827 vs 2.848 validation loss for GPT2-S).

## Strengths

- **StableNorm is cleanly motivated and defined.** Eq. (2) for StableNorm is clearly presented (line 76), its Jacobian is derived (line 84), and the scalar factor \(d^\alpha/\sqrt{\|x\|^2+\epsilon}\) is correctly identified as controlling gradient scale. The gradient scaling intuition (\(d^{0.45}\) vs \(d^{0.5}\) for \(d=4096\), factor 0.66) is concrete and intuitive.

- **Empirical ablation over \(\alpha\) is informative.** Five values of \(\alpha\) (0.0, 0.125, 0.25, 0.375, 0.5) are tested on both GPT and ViT (Figure 3), demonstrating a trade-off between gradient vanishing (small \(\alpha\)) and instability (large \(\alpha\)). The no-warmup evaluation is a nice stress test for stability.

- **Final-task improvements are consistently positive.** StableGPT-S/M both achieve better validation loss than their GPT2 counterparts, and StableViT-L improves accuracy from 81.3% to 82.4%. The gains are modest but directionally consistent across tasks and model sizes.

## Weaknesses

### Fatal
None.

### Major

1. **The abstract claims experiments at 1B parameters / 200 layers that were not performed.** Lines 4–5 and line 30 both state that the method was evaluated "on large model (1B parameters) and deep model (200 layers)." However, Section 2 (line 33) explicitly says: *"Due to time and computational costs, we only use GPT2-Small (GPT2-S), GPT2-Medium (GPT2-M)"* — both far below 1B parameters. No depth ablation at or near 200 layers is presented. This is a direct contradiction between the paper's headline claims and its actual experiments. Overstating experimental scope at this level undermines the paper's credibility and must be corrected.

2. **StableInit and StableAtten are never actually defined in the available text.** The paper repeatedly references "StableInit (defined in Eq. 1)" (line 24) and "StableAtten (defined in Eq. 3)" (line 28), but neither equation appears. Section 3.1 (lines 38–44) ends abruptly after mentioning a random matrix theorem without presenting StableInit, any bound on its Lipschitz constant, or any equation. Section 3.3.1 (lines 106–144) ends with "Precisely, we have the following theorem" (line 141) and then the section terminates — no theorem statement, no definition of StableAtten, no analysis. The paper's claimed contributions are thus two-thirds incomplete. This is not about appendix-deferred proofs; these sections in the main body are substantively missing.

3. **The conclusion claims theoretical derivations that are absent.** Line 168 states: *"Specifically, we derived an upper bound and a lower bound for the expectations of the maximum and the minimum of the singular values of weight matrix obtained from Xavier initialization."* No such derivation appears anywhere in the paper. The paper also claims in line 24 to have proved Xavier's Lipschitz constant is bounded by 2 and StableInit's by 1, but neither proof is present.

### Minor

1. **The theoretical justification connecting the centering comparison to the exponent change is loose.** Theorem 2 compares LayerNorm (with centering) to RMSNorm (without centering), showing RMSNorm is "less likely" to reach the maximum scalar factor. This comparison is about centering, not about the exponent — the paper then proposes changing the exponent from 0.5 to \(\alpha\) for a different reason (the \(\sqrt{d}\) growth). The logical flow (centering → centering irrelevant → exponent matters) is present but could be streamlined. This does not invalidate the StableNorm proposal, but the theoretical motivation feels assembled from two partially disconnected observations.

2. **No gradient norm measurements are reported.** The paper's core argument for StableNorm is that it controls gradient scale, yet no direct gradient-norm measurements (across layers, training steps, or \(\alpha\) values) are shown. Only loss curves under no-warmup are provided. This makes the "stability" argument somewhat indirect.

3. **No statistical significance reported for small performance gains.** The improvements are modest (0.021 drop in validation loss for GPT2-S, 1.1% accuracy gain for ViT-L). No confidence intervals, multiple-seed runs, or significance tests are reported. It is unclear whether these gains are robust or within the noise of a single run.

4. **No ablation isolating the three components in the full Stable-Transformer.** The paper claims all three components (StableInit, StableNorm, StableAtten) contribute to the Stable-Transformer, but only StableNorm is evaluated individually (Figure 3). The full model results (Figure 1) combine all three changes without ablating their individual contributions.

### Trivial
- The paper states that ViT-Large and ViT-Huge setups are described (line 32), but only ViT-L results are shown.

## Nice-to-Haves
- Reporting learning-rate sensitivity / tolerance for the combined method (the paper claims larger LR tolerance but does not show a sweep).
- Providing gradient-norm measurements to directly validate the gradient-scaling argument for StableNorm.
- A principled rule for selecting \(\alpha\) as a function of hidden dimension \(d\), rather than empirical tuning.

## Removed Points

1. **Criticism about "ignoring the projection matrix \((I-xx^\top/(\|x\|^2+\epsilon))\)"** — the paper explicitly bounds the projection matrix's maximum singular value by 1 (line 57) and includes it in the Jacobian derivation (line 84). The maximum singular value analysis of the full Jacobian is \(d^\alpha/\sqrt{\epsilon}\cdot1\cdot\|\gamma\|_\infty\), which is correct as an upper bound. This criticism is factually inaccurate.

2. **Criticism about "both attain maximum at \(x=0\)" (for Theorem 2)** — for LayerNorm with centering, the maximum occurs when \(\|y\|=0\) (i.e., any constant vector), not when \(x=0\). The paper's claim that RMSNorm "is less likely to obtain the maximum value" is actually defensible because RMSNorm requires the more restrictive condition \(x=0\). This specific sub-point is incorrect.

3. **Strength about "StableInit is provably more stable than Xavier initialization"** — this strength conflicts with the verified weakness that StableInit is never defined or analyzed in the available text. The claim cannot be evaluated and is removed per the rule that when a strength and weakness disagree, the weakness wins.

4. **Criticism about \(\gamma\) being ignored** — the paper includes \(\mathrm{diag}(\gamma)\) in the Jacobian (line 84). At initialization, \(\gamma=1\). The paper acknowledges \(\gamma\) is learnable. The analysis is about the Jacobian's structure, not about \(\gamma\)'s dynamics, which is a reasonable scope choice for an initial analysis.

5. **Generic strength about "motivation is timely and important"** — removed as too generic to be informative.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any insight about the paper that the paper itself does not state.

## Suggestions

1. **Correct the experimental claims.** Either remove the "1B parameters" and "200 layers" statements from the abstract and introduction, or add those experiments. The current text is misleading.

2. **Complete the missing definitions.** Eq. (1) for StableInit, Eq. (3) for StableAtten, and their associated theorems must be present in the paper for it to be evaluable.

3. **Add an ablation study** separating the individual contributions of StableInit, StableNorm, and StableAtten in the full Stable-Transformer.

4. **Report multiple seeds or confidence intervals** for the performance numbers, given the modest gains.

5. **Include gradient-norm measurements** (across layers and training steps) to directly support the gradient-scaling argument for StableNorm.

## Score and Decision

MY FINAL SCORE: <pineapple>3.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>