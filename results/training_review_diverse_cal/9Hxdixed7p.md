Now I have a thorough understanding of the paper and can cross-check every claim. Let me write the final consolidated review.

---

## Summary

This paper identifies three interrelated phenomena ("3D-properties") that arise during DPO training: (1) the likelihood of rejected responses drops far faster than that of chosen responses; (2) DPO degrades into mere response suppression as the gradient for the chosen response vanishes; (3) probability disperses to unseen responses. The authors provide a gradient-based theoretical analysis at the response-probability level, validate the dynamics with a carefully designed toy model, and conduct experiments on Baichuan2-13B/33B across math reasoning and instruction-following tasks. They also propose regularization techniques (Flex-DPO and SFT-loss augmentation) and contrast DPO with RM-based alignment methods to explain DPO's relative suboptimality.

## Strengths

1. **Novel gradient-based theoretical framework for DPO's dynamic instability.** The closed-form analysis of ∂ℓ/∂π⁺ and ∂ℓ/∂π⁻ (Corollaries 1–3) provides a clear, mathematically grounded explanation for why the rejected-response gradient dominates over the course of training and why the chosen-response gradient eventually collapses. This goes beyond prior concurrent work (Feng et al., 2024; Xu et al., 2024a), which focused on endpoint analysis or offered partial explanations. The analysis cleanly explains known empirical observations (likelihood decrease of both responses, suboptimality relative to RM-based methods, on-policy superiority) under a unified framework.

2. **Well-designed toy model that directly visualizes the 3D-properties.** The three-layer MLP with a discretized response space (chosen/rejected/unseen blocks) provides clear, controlled empirical validation of all three corollaries (Figures 2 and 3). The four-scenario design (varying on-policy vs. off-policy for chosen/rejected responses) cleanly isolates how the distribution gap affects the severity of the 3D-properties, establishing a strong causal link between theory and observed dynamics.

3. **Systematic empirical demonstration that on-policy DPO mitigates the 3D-properties.** Using Baichuan2-13B/33B on MATH* and SuperCLUE-Math (Table 1), the paper shows that Scenario 1 (both responses on-policy) yields the best performance across all four configurations. This is consistent with the theoretical prediction that a smaller distribution gap delays the decline of the rejected-response likelihood, and provides actionable guidance for practitioners.

4. **Clean theoretical and empirical comparison showing that RM training avoids the 3D-properties.** The paper proves analytically that the gradient ratio for the reward model is balanced (Section 3.4, Equation 6), unlike DPO's imbalanced gradient ratio. Figure 5 empirically confirms that RM training is more stable than DPO training. The PPO comparison on poem and slogan generation (Table 2) further demonstrates the downstream gap, linking it back to the 3D-properties framework.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core contributions (the 3D-properties framework, the explanation for on-policy superiority, and the contrast with RM-based methods) are well-supported by the combination of theoretical analysis, toy-model validation, and real LLM experiments. The weaknesses below are substantive but do not invalidate the paper's central claims.

### Minor

1. **Gradient analysis operates at the response-probability level without fully bridging to token-level parameter dynamics.** The paper derives gradients ∂ℓ/∂π⁺ and ∂ℓ/∂π⁻, which characterize the loss pressure on the probability of entire responses. In real autoregressive LLMs, the parameter update ∇_θ ℓ depends on how changes to shared token probabilities mediate these response-level gradients. The paper acknowledges this gap only in passing (the toy-model discussion notes that "chosen and rejected responses ... often share common tokens"), but Corollaries 1–3 are presented as if the response-level gradients directly govern the optimization. Explicitly discussing how the token-level decomposition affects or preserves the qualitative conclusions would strengthen the theoretical framing. This is a limitation of the current analysis, not a fatal flaw — the core qualitative insight (the gradient ratio π⁺/π⁻ drives imbalance) is likely to persist at the parameter level.

2. **The dispersion effect (Corollary 3) is described with imprecise language.** The argument that decreasing probability mass on chosen+rejected responses will "randomly disperse into other unseen responses" is too loose. A decrease in the probability of specific responses does not mechanically imply random dispersion — it could concentrate on semantically similar responses, degenerate repetitions, or other structured modes. The toy model empirically validates that dispersion *does* occur in its simplified setting (because the response space is partitioned into blocks), but the theoretical argument alone does not guarantee this behavior in real LLMs with a vast, structured output space. The paper would benefit from a more precise statement about what drives dispersion and under what conditions it occurs.

3. **The Flex-DPO loss function is not explicitly stated.** The paper introduces "adaptive values of β to control the rate at which the likelihood of rejected responses declines" and mentions fixing β⁺ while varying β⁻ (Section 4.3), but never writes the modified loss function. The reader is left to infer that the symmetric β in the standard DPO loss is replaced by separate β⁺ and β⁻ coefficients. This should be stated explicitly, as it is a core component of the proposed method.

4. **No direct likelihood trajectory measurements from real LLMs.** The paper validates the 3D-properties directly in the toy model (Figure 2) but relies on downstream task performance (accuracy, GPT-4 scores) for real LLMs. While these metrics are relevant, they do not directly confirm that the predicted gradient imbalance, likelihood suppression, and dispersion are occurring during real LLM training. Adding log-probability curves for chosen, rejected, and held-out responses over the course of real LLM training — analogous to Figure 2 — would substantially strengthen the link between theory and practice. The paper acknowledges this as a limitation of scope.

5. **The PPO comparison is limited to two creative-generation tasks.** Table 2 shows that DPO underperforms PPO on poem and slogan generation, but a comparison on MATH or a broader instruction-following benchmark would strengthen the claim that RM-based alignment avoids the 3D-properties in general. As it stands, the comparison is suggestive but narrow.

6. **The "broader RM-free alignment" claim is not strongly supported.** The abstract states that the findings "extend to broader RM-free alignment strategies," but the paper only includes a brief comparison with IPO and SLiC in Table 9, and provides no theoretical analysis of whether those methods exhibit analogous gradient imbalances. The paper does acknowledge this limitation in the conclusion.

### Trivial
- The β < 1 assumption in Corollary 2 is stated (line 135) but not justified or discussed until the point of use. It would be helpful to note early that this condition holds for typical DPO hyperparameter ranges (β ≈ 0.1–0.5).

## Nice-to-Haves
- Log-probability trajectory plots from real LLMs during DPO training (chosen, rejected, and held-out responses), to directly validate the 3D-properties rather than relying on task-performance proxies.
- Error bars or confidence intervals for the regularization results (Figure 4, Table 9) to assess the significance of the observed improvements.
- A brief theoretical analysis of whether the gradient imbalance identified for DPO also affects other RM-free methods (e.g., SimPO, IPO) to substantiate the claimed broader applicability.
- A transfer experiment on a more commonly used model family (e.g., Llama-2/3) to improve comparability with the broader preference-optimization literature.

## Removed Points
These points are flagged to be removed; treat them with caution.
- The critic's claim that the β<1 assumption "should be stated and justified early" — the paper does state it (line 135), making this a reader-speed bump rather than a missing piece. Moved to Trivial.
- The critic's characterization of the Baichuan2 model choice as limiting comparability — the paper need not match every concurrent work's model zoo to be valid. Moved to Nice-to-Haves.
- The critic's framing that the gradient analysis "reflects the intended pressure rather than actual optimization dynamics" as a critical/fatal issue — this is an acknowledged limitation of the response-probability level of analysis, and the paper is transparent about what it computes. The qualitative conclusions hold. Kept as a minor weakness (point 1 above) but downgraded from its original severity.
- The Strength Finder's claim of "comprehensive empirical demonstration... [and] direct empirical comparison" — the strengths are retained but tempered by the verified weaknesses (e.g., no direct likelihood measurements, limited PPO comparison).

## Novel Insights
The reviews collectively surface a tension that the paper does not fully resolve: the response-level gradient analysis is elegant and yields clean closed-form corollaries, but the step from "the gradient ratio for response probabilities is π⁺/π⁻" to "parameter updates in autoregressive LLMs exhibit the same imbalance" involves token-level compositional effects that the paper glosses over. This gap does not undermine the paper's conceptual contribution — the 3D-properties framework is valuable regardless — but pinpoints where a follow-up could provide a deeper mechanistic understanding. The fact that the field is actively debating DPO's limitations (as evidenced by the concurrent work discussed in Section 2.2) makes the paper's synthesis of these phenomena into a coherent framework timely and useful.

## Suggestions
1. State the Flex-DPO loss function explicitly (e.g., a small equation showing β⁺ and β⁻ separate coefficients).
2. Add at least one experiment showing log-probability trajectories from a real LLM during DPO training (even on a small subset) to directly confirm the 3D-properties in a realistic setting.
3. Tighten the language around Corollary 3: clarify that dispersion is a *tendency* (not a guarantee) and discuss the conditions under which it occurs or could fail to occur.
4. Add a brief note in Section 3.1 explaining that the response-level gradient analysis captures the directional pressure on the loss, while the actual parameter update depends on token-level sharing; note that the qualitative conclusions are expected to hold because the gradient ratio π⁺/π⁻ is invariant to the parameterization.
5. Include confidence intervals or significance tests for the regularization results to substantiate claimed improvements.

## Score and Decision

The paper makes a genuine contribution by identifying and theoretically grounding the 3D-properties — a unified explanation for several known but poorly understood phenomena in DPO training. The analysis is rigorous within its chosen level of abstraction, the toy-model validation is convincing, and the real LLM experiments support the main claims. The weaknesses (response-level vs. parameter-level gap, imprecise dispersion justification, incomplete specification of Flex-DPO, missing direct likelihood evidence from real models) are real but addressable in a revision and do not invalidate the core contribution. The paper offers clear practical guidance (prefer on-policy data, control the decline rate of rejected responses) grounded in theoretical understanding.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>