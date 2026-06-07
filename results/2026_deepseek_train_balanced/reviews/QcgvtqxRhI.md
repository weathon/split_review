Now I have a comprehensive understanding of the paper. Let me write the final consolidated review.

## Final Review

---

## Summary

BOSS proposes a one-shot subset selection method that jointly considers diversity (feature coverage) and difficulty (label variability) for data-efficient deep learning. The method is motivated by a balanced core-set loss bound that decomposes into feature-difference and label-variability terms, and uses a sinusoidal importance function with two tunable parameters (peak location c, sharpness α) to control the trade-off between these two objectives based on subset size. Experiments on SVHN, CIFAR-10/100, and Tiny-ImageNet show consistent improvements over seven baselines.

## Strengths

- **Clear problem framing and motivation.** The paper correctly identifies that existing subset selection methods optimize for diversity or difficulty alone, which cannot faithfully represent the joint distribution P(x,y). This framing is well-supported by examples (Figure 1) and by the synthetic experiments (Figure 4).

- **Theoretical insight about subset-size-dependent balance.** The analysis of the core-set bound (Section 3.2) yields a useful qualitative insight: at small subset sizes, the feature-diversity term dominates the bound (missing a whole cluster causes large loss), while at larger sizes, the label-variability term becomes the bottleneck. This insight is empirically validated by Figure 4 (synthetic) and Figure 5(a,b) (real datasets, where optimal c increases with budget).

- **Expressiveness of the importance function.** The sinusoidal function Z(D) = [(sin(π(D−c))+1)/2]^α provides flexible control over which difficulty levels to prioritize (via c) and how sharply (via α), going beyond CCS's discrete stratification. The ablation (Table 2) confirms that combining diversity and difficulty via this function substantially outperforms either component alone (e.g., Tiny-ImageNet at 10%: Diversity alone 28.90%, Difficulty alone 22.20%, combined 33.95%).

- **Consistent empirical gains, especially in the low-budget regime.** Across all four datasets and multiple subset sizes (Table 1), BOSS outperforms all seven baselines. The margins are largest at the smallest budgets (e.g., CIFAR-100 at 10%: BOSS 40.85% vs. next-best CCS 38.80%; Tiny-ImageNet at 10%: BOSS 33.95% vs. CCS 31.68%), which directly corroborates the paper's core thesis that balanced selection is most valuable when subsets are small.

- **Clean ablation study.** Table 2 decomposes the method into Diversity-only, Difficulty-only, Diversity+Difficulty, and the full method including cutoff. The finding that Difficulty-only performs worst at 10% budget (CIFAR-10: 69.31% vs. Diversity-only 80.76%) is consistent with the theoretical prediction that ignoring diversity causes loose bounds at small subset sizes.

## Weaknesses

### Major

- **Theorem 2's "proof" does not rigorously establish a lower bound.** The proof (lines 105–111) proceeds through a chain of approximations (≈), not inequalities. It assumes both a dense neighborhood (δ_x → 0) and that one sample is correctly predicted (||y_j − η₀(x_j)|| ≈ 0), then produces an *approximate equality* ||y_i − y_j|| ≈ ||y_i − η₀(x_i)||. No step yields a provable inequality. Furthermore, the EL2N score is defined as 𝔼_t[||η₀(x) − y||] over multiple initial models, but the proof only considers a single model η₀. The step that bridges from a per-pair approximation to an expectation over models is not justified. The synthetic visualization in Figure 2 shows correlation, which is suggestive but does not constitute a proof of a lower-bounding relationship. Claiming that "EL2N lower bounds label variability" is substantially stronger than what the evidence supports.

- **Gap between the additive theoretical bound and the multiplicative objective function.** Theorem 1's balanced loss bound has an additive form: Σ_i (λ^η||x_i − x_j|| + λ^y||y_i − y_j||). This suggests minimizing a *sum* of feature-distance and label-distance terms. However, the proposed selection function F(S) = Σ_i maxⱼ Sim(x_i, x_j) · Z(x_j, y_j) uses *multiplication* of a diversity term and a difficulty-modulated weight. The paper simply states "we use multiplication since we remain agnostic about the Lipschitz coefficients" (line 145), which does not explain why multiplication is appropriate when the bound is additive. One could equally argue for an additive form (Sim(x_i, x_j) + λ·Z(x_j, y_j)), or any other combination. The paper presents the theory as justifying the method, but the connection is qualitative inspiration rather than a derivation. This weakens the claim that "samples are selected so that the balanced core-set loss bound is minimized."

- **No documented parameter selection protocol for c, α, β.** The paper states general trends (c increases with subset size, α increases with subset size, β higher for small subsets) but does not specify the exact parameter values used for each dataset and each subset size in Table 1. Were these values tuned on a held-out validation set, or selected based on test-set performance? Without a reproducible protocol, it is unclear whether BOSS's gains stem from its core idea or from per-dataset parameter cherry-picking. For a method whose core claim is "balanced selection according to subset size and the nature of dataset," this is a significant evidential gap.

### Minor

- **No error bars or measures of uncertainty.** Results are reported as "averaged over five runs" (line 167) but no standard deviations, confidence intervals, or statistical tests are provided. The paper claims BOSS "significantly outperforms all the competitive baselines," but the reader cannot assess whether the reported margins are reliable.

- **No reporting of selection-time computational cost.** The paper's motivation is data-efficient training, yet the cost of the selection procedure itself is not reported. BOSS uses a greedy submodular maximization that can require O(|V|·|S|·d) operations (where d is feature dimension), which could be substantial for Tiny-ImageNet (100k images). Reporting selection time relative to baselines would help practitioners evaluate the practical trade-off.

- **Strong assumption in Theorem 1.** The bound assumes l(η(x_j), y_j) = 0 for every selected sample (line 70) — i.e., the model achieves zero training loss on the entire subset. While overparameterized networks can approximate this, it is not guaranteed for arbitrary subset sizes, making the bound approximate rather than exact.

- **Theorem 1 is a standard Lipschitz decomposition.** The balanced core-set loss bound is obtained by applying the triangle inequality to the Sener & Savarese (2018) core-set bound and splitting the loss difference into feature and label components via Lipschitz continuity. This is a routine algebraic manipulation and does not constitute a novel theoretical result. The paper's phrasing ("a novel balanced core-set loss bound") overclaims its theoretical novelty. This does not invalidate the paper — the value lies in using the decomposition to motivate method design.

### Trivial

None.

## Nice-to-Haves

- **Add a simpler additive baseline.** The most natural baseline would be: F(S) = Σ_i maxⱼ [Sim(x_i, x_j) + λ·Z(x_j, y_j)] — the additive form suggested by the bound. Comparing this to the proposed multiplicative form would clarify whether the multiplication is necessary or whether any joint scoring suffices.

- **Clarify the role of class-balanced sampling.** The paper states "we sample the subset in a class-balanced fashion" (line 167), which itself provides a diversity guarantee. The ablation (Table 2) shows that Diversity+Difficulty outperforms Diversity-only, so class balancing is not doing all the work. But discussing how class-balanced sampling interacts with the facility-location diversity objective would help.

- **Sensitivity analysis for c, α, β.** Figure 5 shows parameter impact qualitatively but does not report how much performance varies across reasonable parameter ranges. If the method is sensitive to these choices, the parameter selection burden is acute.

## Removed Points

The following points from the input reviews were identified as invalid or noise and are listed here for completeness:

1. *"Table 1 is an image — the actual numerical values cannot be read from the parsed text."* — Parser artifact; the original PDF table is readable.
2. *"The proof sketch contains apparent typesetting errors (e.g., subscript S vs. 𝒮 inconsistency)."* — Parser artifact.
3. *"The submodularity claim is stated without proof."* — The reviewer acknowledges the claim is correct (weighted facility location functions are submodular); this is not a weakness.
4. *"The paper does not clearly delineate what is borrowed from CCS."* — The paper explicitly states "we will adopt the cutoff mechanism as in (Zheng et al., 2023)" (line 145), which is sufficiently clear.
5. *"Missing related works"* — Per instructions, this is not verifiable without external sources.
6. Strength Finder's claim that *"Theorem 2 establishes a formal connection between the EL2N difficulty score and the label variability term"* — Removed because the proof is not rigorous (see Major weakness above), so this claimed strength is invalid.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the gap between the additive theoretical bound and the multiplicative objective as the most important issue, which is a methodological concern the paper itself does not fully address. The reviews do not contribute additional conceptual insights beyond what the authors provide.

## Suggestions

1. **Provide explicit parameter values** (c, α, β) used for each dataset and subset size in Table 1, along with a reproducible protocol for selecting them (e.g., tune on a held-out validation split).
2. **Tighten the theory-method connection** by either (a) deriving the importance function from the additive bound under reasonable assumptions, or (b) acknowledging the heuristic nature of the multiplicative form and presenting it as an engineering choice inspired by (rather than derived from) theory.
3. **Report standard deviations** for all main results, and add a brief statement on whether differences from the best baseline are statistically significant.
4. **Report selection time** for BOSS and baselines on at least one dataset.
5. **Clarify Theorem 2** by either (a) providing a rigorous proof of the claimed lower bound, or (b) reframing it as an empirical observation (as supported by Figure 2) rather than a theorem.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>