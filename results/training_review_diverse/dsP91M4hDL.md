I have verified the key claims. Let me now write the consolidated review.

## Summary

This paper proposes TC-MoE, which expands the expert space in Mixture-of-Experts (MoE) models by multiplying each expert with the ternary set {-1, 0, 1}, creating sign-flipped (E⁻¹) and zero-cost null (E⁰) variants. This allows the Top-K router to select from a richer set of options—avoiding negative-contribution activations via E⁰ and benefiting from sign-flipped expert outputs via E⁻¹—without adding expert parameters. The paper also introduces a tailored load balancing loss and a reward loss (α₂) claimed to enable a flexible efficiency-effectiveness trade-off. Experiments on models up to ~400M parameters trained on 100B tokens show consistent accuracy gains (0.8–1.2%) with reduced activated experts (up to 9%).

## Strengths

- **Novel and well-motivated expert-space expansion.** The core idea—adding E⁻¹ (sign-flipped) and E⁰ (zero-cost null) variants of existing experts—is clever, simple, and directly addresses two concrete limitations identified in the paper: unnecessary activations (Figure 1a) and underutilization of negative-weight potential (Figure 1b). This approach is distinct from prior work that modifies the routing mechanism itself.

- **Consistent empirical improvements across settings.** On the base model (RedPajama), TC-MoE achieves 49.54% average accuracy, surpassing Top-K (+0.83%), Random drop (+0.88%), and Top-P (+0.71%), while simultaneously reducing activated experts by 9.0% and FLOPs by 6.5% (Table 1). Improvements hold across different model sizes (tiny, base, fine-grained base) and datasets (RedPajama, FineWeb), and under varying activation budgets (Figure 3).

- **Ablation study validates each component.** Table 3 isolates the contribution of each subset: {–1,1} adds +0.29% accuracy (same K); {0,1} adds +0.52% with fewer activated experts; the full {-1,0,1} gives the best combined result. This cleanly demonstrates that both E⁻¹ (quality) and E⁰ (efficiency) contribute meaningfully.

- **New load balancing and reward losses are principled adaptations.** The load balancing loss (Eqs. 4–7) correctly treats E⁰ as cost-free and balances Eᵢ¹+Eᵢ⁻¹ for device-aware parallelism. The reward loss (Eq. 12) provides a mechanism to encourage E⁰ activation by assigning a negative gradient to its gate values. Layer-wise activation analysis (Figures 6, 8) reveals structured, interpretable patterns of how the model learns to use the expanded space.

## Weaknesses

### Fatal
None.

### Major

1. **Internal contradiction about whether the routing scheme is modified.** The paper repeatedly claims it addresses limitations "without modifying the routing scheme" (Abstract, lines 28, 111). Yet Section 3.2 states: "Furthermore, we find that making a **small improvement to the Top-K routing scheme** by always activating experts from E⁰ is beneficial" (line 113). If "always activating" means forcing at least one E⁰ expert into the selected set, the routing logic is indeed modified—directly contradicting the paper's central framing. If it means something else (e.g., a learned behavior rather than a forced inclusion), the text is too vague to disambiguate. Footnote 3 presumably clarifies this but is in the stripped appendix. This ambiguity undermines the paper's primary narrative and needs explicit resolution in the main text.

2. **The claimed "flexible trade-off" via α₂ is empirically unsupported.** The paper repeatedly asserts that the reward loss enables a flexible trade-off between efficiency and effectiveness (Abstract, Section 3.4, Table 1 caption, line 196). However, **no experiment varies α₂** to demonstrate this trade-off. The main results show only a single operating point. Without a plot of accuracy (or LM loss) vs. average number of costly activated experts for multiple α₂ values, this central claim remains unvalidated. Additionally, the actual values of α₁ and α₂ used in the main experiments are never reported, making the results impossible to reproduce precisely.

3. **Incomplete comparison against Top-P across settings.** Top-P (Huang et al., 2024) is a direct competitor that also enables dynamic expert activation. Table 1 includes Top-P only for the base model on RedPajama. For the fine-grained base on RedPajama and both model sizes on FineWeb, Top-P comparisons are absent. Since the paper claims TC-MoE outperforms competitors broadly, these missing comparisons weaken the experimental support.

### Minor

1. **No statistical reliability measures.** All results appear to come from a single run without standard deviations or confidence intervals. Given the 0.7–1.2% improvements on benchmarks with non-trivial variance (MMLU, BoolQ), it is unclear whether some gains are statistically significant. While single-run large-scale pre-training is common practice, the paper should acknowledge this limitation.

2. **No hyperparameter sensitivity analysis.** Beyond the missing α₂ trade-off curve, there is no analysis of how the load balancing factor α₁ and reward factor α₂ interact. Since both losses affect which experts get activated, their combined effect is unknown. A sensitivity table or grid would strengthen the paper.

3. **The unnecessary-activations analysis (Figures 4–5) is qualitative.** The histograms show distribution shifts but are not accompanied by a quantitative metric (e.g., percentage of activations with negative contribution). Adding a numerical comparison would strengthen this analysis.

4. **Router computational overhead is not measured.** The expanded space has 2N+K experts vs. N in the baseline (e.g., 18 vs. 8 for N=8, K=2—a 2.25× increase), which is small relative to FFN cost but should still be explicitly measured (wall-clock time per token) to substantiate the "negligible" claim.

5. **Gradient explanation is simplified.** The paper treats the reward loss gradient ($-\frac{1}{T}$) as directly affecting gate values, but the gradient with respect to *router parameters* depends on the full backpropagation path through softmax/top-K/normalization. The explanation would benefit from acknowledging this complexity.

### Trivial
- The justification that K copies of E⁰ suffice (line 99) is only strictly correct if the router can freely select them; the "always activating" modification would require K+1 copies in some edge cases. Minor and fixable.
- The load balancing loss (a covariance-like term) is presented without intuition for why this form was chosen over more standard alternatives.

## Nice-to-Haves
- A discussion of whether the method scales to larger models (e.g., 7B+) and whether the load balancing or reward losses would need adjustment.
- Quantitative metric for unnecessary activations (e.g., percentage of negative-contribution activations) to complement Figures 4–5.
- Reporting the actual α₁ and α₂ values used, and ideally a small sensitivity table.

## Removed Points
- **"The paper should cover additional domains/tasks"**: No reviewer made this specific demand, so not applicable.
- **Harsh critic's "Other Observations" sub-items about load balancing loss form and number of E⁰ experts**: These are kept above in Minor/Trivial sections as they are reasonable but not central.
- **"The gradient with respect to router parameters depends on how g_{E⁰} is produced" (Issue 2, second sub-bullet)**: Kept as Minor #5 above—it's a valid nuance but not a structural flaw.
- **Strength Finder's claim that the method works "without changing the routing algorithm"**: This conflicts with the verified weakness about routing ambiguity. The strength of the ternary expansion idea is retained; the claim about routing modification is dropped from the strength description.

## Novel Insights

A genuinely novel observation emerges from the reviews: TC-MoE's ternary expansion implicitly achieves what prior work achieves through routing modification—specifically, the ability to avoid negative-contribution activations and explore sign-flipped outputs—but does so by giving the *same* Top-K router a richer action space. This creates an interesting design principle: rather than constraining or reprogramming the router's logic, one can expand the set of actions available to it. The reward loss then acts as a soft prior on this action space, nudging the router toward efficiency without hard constraints. This "action-space expansion" perspective is distinct from the "routing algorithm improvement" paradigm and could generalize to other sparse gating problems beyond MoE.

## Suggestions

1. **Resolve the routing ambiguity explicitly.** State clearly whether the "always activating experts from E⁰" modifies the Top-K algorithm or is a learned behavior. If it is a modification, adjust the paper's framing to acknowledge this and present the routing adjustment + expert-space expansion as a combined contribution.

2. **Add the α₂ trade-off curve.** This is the single most impactful experiment the authors could add: plot accuracy (or LM loss) vs. average number of costly activated experts for 4–5 values of α₂, with α₁ held fixed. This single figure would validate the paper's central claim about flexible efficiency-effectiveness control.

3. **Add Top-P to the missing settings** (fine-grained base on RedPajama, both model sizes on FineWeb), or explicitly justify their omission.

4. **Report α₁ and α₂ values** used in the main experiments, and add a brief sensitivity analysis.

5. **Add a quantitative metric** to the unnecessary-activations analysis (e.g., percentage of activations with negative contribution for baseline vs. TC-MoE).

## Score and Decision

The core idea is clever, well-motivated, and the empirical results are consistently positive across multiple settings. However, the paper's central framing is undermined by an unresolved contradiction about whether the routing scheme is modified, and a key claimed capability (the α₂ trade-off) is entirely unsupported. These are fixable issues, but in their current form they prevent the paper from being fully convincing. I lean toward borderline acceptance conditional on addressing these issues, but as presented the weaknesses are significant enough to warrant a cautious assessment.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>