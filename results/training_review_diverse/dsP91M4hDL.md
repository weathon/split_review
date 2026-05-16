Now I have all the information I need. Let me synthesize the final review.

## Summary

TC-MoE proposes augmenting Mixture-of-Experts architectures by multiplying each expert by the ternary set {-1, 0, 1}, creating an expanded expert space (E⁻¹, E⁰, E¹) without modifying the underlying routing algorithm. This allows the standard Top-K router to activate zero-cost experts (E⁰) to skip unnecessary computation or sign-flipped experts (E⁻¹) that may better contribute to the output. The paper introduces a custom load-balancing loss and a reward loss to manage the heterogeneous expert types, and demonstrates consistent accuracy improvements (~1.1% average) alongside efficiency gains (up to 9% fewer activated experts) over Top-K and Top-P baselines.

## Strengths

- **Consistent accuracy and efficiency improvements across multiple settings.** Table 1 shows TC-MoE outperforms Top-K baselines by 0.83–1.18% on average across nine benchmarks while simultaneously reducing activated experts by 7–9% and FLOPs by 5.1–6.5%. These gains hold across two datasets (RedPajama, FineWeb) and three model sizes.
- **Novel, conceptually clean architectural augmentation.** Rather than redesigning the router (as in prior work), TC-MoE expands the expert space via ternary multiplication—a simple operation that introduces only negligible router-parameter overhead (§3.2). This design can be paired with any standard Top-K router, making it complementary to router-focused improvements.
- **Targeted loss design for heterogeneous experts.** The proposed load-balancing loss (§3.3) correctly handles the fact that E⁰ experts cost nothing and that Eᵢ¹ and Eᵢ⁻¹ reside on the same device, achieving near-perfect workload balance (Figure 7). The reward loss (§3.4) provides a principled, tunable mechanism to encourage zero-expert activation, with Figure 3 showing TC-MoE consistently outperforms competitors across different activation budgets.
- **Empirical validation of the core motivation.** Figures 4–5 directly visualize the reduction in unnecessary (negatively-contributing) activations under TC-MoE compared to the baseline, confirming that the mechanism works as intended.

## Weaknesses

### Fatal
None.

### Major

- **Missing comparison against Expert Choice routing.** The paper discusses Expert Choice routing (Zhou et al., 2022) in §2 and correctly notes that it "modifies the routing scheme," yet does not include it as a baseline. Expert Choice is the most directly comparable prior method that also allows variable expert activation (via capacity-based token selection). Without this comparison, it is difficult to assess whether TC-MoE's gains represent an advance over the state of the art in flexible routing or merely an improvement over fixed-K routing. The inclusion of Top-P (Huang et al., 2024) partially addresses the threshold-based routing family, but Expert Choice remains the most glaring omission.
- **Confounded ablation: expert-space expansion vs. auxiliary losses.** Table 3 compares expert-set variants ({1}, {-1,1}, {0,1}, {-1,0,1}) but does not isolate the effect of the new auxiliary losses. The baseline row {1} presumably uses the standard Top-K without the proposed losses, while the ternary rows use both the expanded expert set and the new losses. Consequently, the observed gains conflate two factors: the ternary expert expansion and the novel load-balancing/reward losses. A control experiment that applies the proposed losses to the *original* expert space (without ternary expansion) would be needed to quantify the additive value of the expansion itself.

### Minor

- **Missing hyperparameter values for α₁ and α₂.** The total loss is ℒ = ℒ_lm + α₁ℒ_aux + α₂ℒ_rwd (Equation 13), but no values for α₁ or α₂ are reported anywhere in the paper. This omission makes it impossible to reproduce the results or understand the sensitivity of the efficiency–effectiveness trade-off to the reward coefficient.
- **The {−1,1} ablation and the reward loss.** The ablation in Table 3 includes a {−1,1} variant (no E⁰ experts), but the reward loss targets E⁰. The paper does not clarify whether the reward loss is disabled in this setting or how its absence affects the comparison.
- **The "Random drop" baseline's hyperparameter p is unreported.** The Random drop variant (§4.1) uses an unspecified probability p. Since Random drop is one of the three comparison methods, the missing p value limits reproducibility.
- **Routing computational cost is not quantified.** The paper reports FLOPs reductions from fewer expert activations but acknowledges that the router's logit computation grows from O(Nd) to O((N+K)d) (§3.2). For small models, this routing overhead could be non-negligible relative to the savings. Reporting wall-time per step or total FLOPs including routing would strengthen the efficiency claims.

### Trivial

- None beyond the minor items listed above.

## Nice-to-Haves

- Adding Expert Choice (Zhou et al., 2022) as a baseline would substantially strengthen the evaluation.
- A control experiment applying the proposed load-balancing and reward losses to the *original* expert space (without ternary expansion) would cleanly isolate the contribution of the ternary expansion itself.
- Reporting α₂ sensitivity (e.g., a sweep showing HellaSwag accuracy vs. average activated experts) would demonstrate the stability of the efficiency–effectiveness trade-off.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"K identical zero experts not justified"** — The paper *does* justify this design choice (line 99: "as this is sufficient for the Top-K router to activate any number from 0 to K of these experts"). Removed as factually incorrect.
- **"100B tokens modest, 1.4B parameters small"** — Subjective standard; many recent MoE papers train at comparable or smaller scales. Removed as an unfair expectation.
- **"Load-balancing loss lacks analysis w.r.t. K and N"** — The paper provides empirical load-balance results (Figure 7). A theoretical analysis of how the loss scales with K/N is beyond the paper's scope. Removed.
- **"Activation ratio analysis lacks mechanistic explanation"** — Descriptive analysis of activation patterns across layers (Figures 6, 8) is standard practice. The demand for mechanistic explanation is scope creep. Removed.
- **"ARC-Easy load-balance deviation not discussed"** — The paper *does* discuss this (line 233: "On ARC-Easy, we observe a slight deviation..."). Removed as factually incorrect.
- **"Figures 1a/1b experimental setup omitted"** — The paper states "in a model with 2 activated experts out of 8" (line 22), which is sufficient for a motivational figure. Removed as nitpick.
- **"None of the routing-improvement methods from §2 are implemented"** — This is incorrect; Top-P (Huang et al., 2024), a threshold-based router, *is* implemented. Only Expert Choice (Zhou et al., 2022) is missing. Corrected in the Major weaknesses above.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine methodological gap (confounded ablation) and a missing baseline (Expert Choice), but do not contribute new analytical insights beyond those already present in the paper's analysis.

## Suggestions

1. **Add Expert Choice (Zhou et al., 2022) as a baseline.** This is the most directly comparable prior method and its omission is the single biggest gap in the evaluation.
2. **Add a control ablation** that applies the proposed load-balancing and reward losses to the *original* expert space without ternary expansion. This would isolate the additive value of the expansion from the losses.
3. **Report the values of α₁ and α₂** used in all experiments, and include a sensitivity analysis for α₂ showing the efficiency–effectiveness trade-off.
4. **Clarify the {−1,1} ablation setup** — specify whether the reward loss was disabled for this variant.
5. **Report wall-time or total-FLOPs** (including routing) to substantiate the claim that the routing overhead is negligible.

## Score and Decision

The paper presents a genuinely novel and simple idea for improving MoE routing, with consistently positive results across multiple benchmarks and model sizes. However, the evaluation has two substantive gaps: a missing comparison against Expert Choice routing (the most relevant prior work on variable-expert activation) and a confounded ablation that does not isolate the ternary expansion from the auxiliary losses. These issues are addressable in revision but weaken the paper's current evidence for its core claims.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>