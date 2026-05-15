Now I have a thorough understanding of the paper and can verify each claim. Let me synthesize the final review.

---

## Summary

This paper integrates decision-focused objectives into conformal prediction. The authors develop three methods—penalized conformal with λ tuning, Separable Penalized Ratio (hyperparameter-free for separable losses), and a greedy oracle for non-separable losses—all proven to maintain standard marginal coverage guarantees. Experiments on CIFAR-100, iNaturalist, ImageNet, and the Fitzpatrick dermatology dataset show 60–75% reductions in decision loss over standard conformal prediction, plus a real-world case study demonstrating clinically coherent prediction sets aligned with an expert disease hierarchy.

## Strengths

- **Novel and well-motivated problem formulation.** The paper identifies a genuine gap: conformal prediction guarantees coverage but ignores downstream utility, while decision-focused learning neglects uncertainty quantification. Bridging these is practically important and timely. The framing is clear throughout.

- **Multiple complementary methods with coverage guarantees.** The paper does not propose a single approach but a toolkit: penalized conformal (separable and non-separable), the hyperparameter-free Separable Penalized Ratio (Proposition 2), and the greedy oracle for non-separable losses (Proposition 3). All come with proven marginal coverage guarantees, which is non-trivial given the modifications.

- **Substantial and consistent empirical improvements.** The reported 60–75% decision loss reductions over standard conformal methods are demonstrated across four datasets and multiple loss functions. The Fitzpatrick dermatology case study with expert-defined hierarchies provides a compelling real-world demonstration beyond loss numbers—the resulting prediction sets are qualitatively more actionable.

- **Ablation on classifier quality strengthens practical relevance.** Figure 4 shows that the proposed methods outperform baseline conformal prediction across all levels of base model accuracy, including very noisy classifiers (~0.3 accuracy). This addresses a realistic concern for deployment in data-scarce domains.

- **Hyperparameter-free solution for separable losses.** The Separable Penalized Ratio (Section 3.1.1) derives a non-conformity score from the Neyman-Pearson lemma and then conformalizes it, avoiding λ tuning entirely while maintaining coverage. This is elegant and practically useful.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **No empirical comparison against Conformal Risk Control.** Conformal Risk Control (CRC; Angelopoulos et al., 2022) is correctly identified as the most closely related work, but the paper dismisses it with the claim that it "does not directly optimize the expected value of the chosen function" and that it "can be at the expense of statistical coverage." While CRC solves a different problem (controlling expected loss at a target level, rather than minimizing loss subject to coverage), an empirical comparison would contextualize the contribution. Without it, a reader cannot assess whether the proposed methods offer practical advantages over the closest existing alternative. This does not invalidate the paper's claims against standard conformal baselines, but it weakens the positioning.

- **Greedy algorithm for non-separable losses is presented without analysis of suboptimality.** The greedy algorithm (Equation 5) is described as a heuristic—the paper states it "works well for many losses in practice"—but it is never evaluated against any optimality baseline. For small label spaces where brute-force search is feasible, a suboptimality analysis would quantify how much the greedy ordering sacrifices compared to the true plug-in optimum. Without this, the claim that the method offers a "principled" solution for non-separable losses (beyond the two monotone loss functions tested) is unsubstantiated. The paper also tests only monotone non-decreasing losses (max distance, coverage); performance on loss functions with non-monotone or combinatorial structure (e.g., pairwise penalties) remains unknown.

- **Coverage verification after hyperparameter tuning is shown but could be more explicit.** The paper acknowledges that λ selection breaks exchangeability and proposes a sample-splitting procedure to restore it, with a coverage plot (Figure 2) showing empirical coverage "close to the expected preset value." However, the figure caption references only the iNaturalist dataset and the filename suggests a specific method (non_cbs). Providing per-method, per-dataset coverage tables or plots for the tuned penalized methods would more convincingly demonstrate that the coverage guarantee is not eroded in practice.

- **Random cost assignment in separable experiments is artificial.** The separable-loss experiments assign random costs ℓ(y) uniformly from {0.25, 0.5, 0.75, 1.0}. While this demonstrates algorithmic functionality, it does not reflect realistic use cases where costs would carry semantic meaning (e.g., test costs, treatment risks). The paper would benefit from at least one experiment with meaningful cost structure.

### Trivial

- The notation for L(y) in the non-separable linearization (Section 4.1) is slightly confusing: L(y) = L(S_{σ_k(x)}) where S_i is defined separately, and σ_k(x) is the position of y in the permutation. The double use of L for both the set-level loss and the per-label marginal sum is clear in context but could be simplified.

## Nice-to-Haves

- A comparison of set sizes across methods would help interpret the loss reductions: do the proposed methods achieve lower loss primarily by producing larger sets, or do they genuinely find sets with better composition?
- A sensitivity analysis of λ for the penalized methods (loss vs. λ, coverage vs. λ) on one dataset would illustrate the trade-off and validate the grid search approach more concretely.
- Guidelines for practitioners on when to use each of the three methods (penalized, Separable Penalized Ratio, greedy oracle) would increase the paper's practical impact.

## Removed Points

The following points from the reviewer inputs are removed with justification:

- **"Missing baseline comparison with CRC" framed as "fundamental gap"** — This is downgraded to Minor. CRC solves a related but distinct problem (controlling expected risk vs. minimizing loss subject to coverage). An empirical comparison would be informative, but its absence does not invalidate the paper's core claims against standard conformal baselines.
- **"Figure 1 not grounded in a specific algorithm"** — The paper uses standard split conformal as the baseline throughout; the caption describes the contrast without naming the specific non-conformity score, but the method is well-defined in Section 3. This is a presentation nitpick.
- **"Horvitz (1993) is tangential"** — The paper itself says "While not directly related to the previously mentioned methods" before discussing it. The paper is transparent about the indirect connection.
- **"Proposition 1 assumes bounded loss — maximum distance is unbounded"** — Graph distance on a finite hierarchy is bounded by the hierarchy's diameter. The criticism is factually wrong.
- **"Proposition 2 proof not provided"** — Missing appendix content; per instructions this is a parser artifact and must be removed.
- **"Figures described but not shown"** — Parser artifact; figures exist in the original submission.
- **"Base conformal method is not defined"** — The paper defines split conformal prediction in Section 3 and uses it consistently; "base conformal method" refers to this standard algorithm.
- **"iNaturalist uses only 51 classes — choice should be justified"** — The paper explicitly states it uses "the labels up to the class level" (taxonomic rank), which is a clear and reasonable design choice.
- **"Code is hidden / cannot be verified"** — The submission is under double-blind review; code will be released upon publication.
- **"Ablation conclusion is weak"** — The paper provides a qualitative conclusion supported by a figure; requesting exact numerical deltas is a presentation preference, not a flaw.
- **CRC description "inaccurate"** — The paper's description of CRC is somewhat reductive but not factually wrong. CRC controls expected loss at a level; the paper minimizes loss subject to coverage. These are different objectives.
- **Various grammatical/formatting nitpicks** — Parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews reinforce the paper's framing—the main insight is the systematic integration of downstream decision loss into conformal prediction with retained coverage guarantees—but do not add novel perspectives beyond what the paper itself articulates.

## Suggestions

1. Add an empirical comparison against Conformal Risk Control, even if the problem formulations differ. At minimum, show that CRC does not directly solve the same constrained optimization (loss minimization subject to coverage ≥ 1−α) and discuss the practical implications.
2. Provide a suboptimality analysis of the greedy oracle on a small label set (e.g., 10–15 classes) via brute-force enumeration, quantifying the gap between the greedy solution and the true plug-in optimum for both monotone and at least one non-monotone loss.
3. Include a supplementary table showing empirical coverage for each method (penalized with tuned λ, Separable Penalized Ratio, greedy oracle) on each dataset across multiple splits, confirming the guarantee holds post-tuning.
4. Add at least one separable-loss experiment with semantically meaningful costs (e.g., treatment costs or test costs) to demonstrate real-world applicability.

## Score and Decision

This paper makes a genuine contribution: it identifies a practical gap, proposes multiple principled solutions with coverage guarantees, and validates them thoroughly against standard baselines. The weaknesses are addressable and do not undermine the core claims. The paper is above the acceptance threshold.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>