Now I have sufficient calibration data. Let me write the consolidated review.

---

## Summary

This paper proposes EvA, a genetic-algorithm-based attack on graph structure that directly optimizes the adversarial objective in the discrete domain, bypassing the relaxations required by gradient-based methods. EvA operates in a black-box manner (no gradient access), uses a sparse encoding giving O(|S|·ε·|ℰ|) memory complexity, and can optimize non-differentiable objectives. Experiments show consistent improvements over SOTA gradient attacks (PRBCD/LRBCD) across multiple datasets and models, with ~11% average additional accuracy reduction. The paper also demonstrates the first attacks on two novel objectives: reducing robustness certificate ratios and breaking conformal prediction guarantees.

---

## Strengths

1. **Large and consistent improvements over SOTA gradient-based attacks.** EvA reduces accuracy far below PRBCD across vanilla GCN, adversarially trained GCN, and SoftMedian-GDC on CoraML (Figure 5), with the trend holding across multiple datasets and perturbation budgets. The ~11% average improvement over the best previous attack is substantial in this domain, where baselines typically differ by only a few percent.

2. **Linear memory complexity in the attack budget.** The sparse encoding (Section 3) stores only the indices of flipped edges, giving O(|S|·ε·|ℰ[𝒱_att:𝒱]|) memory instead of the quadratic O(N²) required by gradient methods that materialize the full gradient matrix. This is a genuine practical advantage.

3. **Enables attacks on non-differentiable objectives (certificates and conformal prediction).** Section 5.1 introduces what the paper claims are the first graph certificate attack and the first conformal attack on graphs. Figure 4 provides evidence that these objectives (which contain non-differentiable components like majority voting and quantile computation) can be attacked. The fact that the same GA framework handles these without any architectural changes supports the paper's claim that black-box search is a versatile alternative.

4. **Informative ablations.** The experiments isolating the effect of adaptive targeted mutation (ATM) over uniform mutation (Figure 2, right), the comparison of accuracy vs. cross-entropy vs. margin as fitness functions (Figure 2, left), and the scaling analysis (Figure 3) collectively demonstrate that the authors understand *why* their method works and which components drive the improvement.

---

## Weaknesses

### Major

- **No baselines for the certificate and conformal attacks.** Figure 4 shows the effects of EvA on certified ratio and conformal coverage/set size, but there is no comparison against any baseline — not even random perturbation at the same budget, or a trivial heuristic such as greedy edge selection. Since these are claimed as "first" attacks, the reader cannot determine whether the GA contributes anything meaningful for these objectives, or whether any method that flips edges (even randomly) would produce similar degradation. This is the most significant evaluation gap, as it directly affects two of the paper's showcased contributions.

### Minor

- **Computational comparison with PRBCD is incompletely controlled.** The paper attempts to address fairness by scaling PRBCD's block size (Figure 3, middle), and mentions in text that increasing PRBCD's number of training steps also did not help. However, no figure or table shows the effect of increasing PRBCD's gradient steps. Since EvA uses thousands of forward passes (population × generations), and PRBCD typically uses 100–200 gradient steps, the reader cannot fully assess whether the performance gap is due to the GA's search capability or simply to greater computational effort. The paper acknowledges query efficiency as a limitation but the headline "far from optimal" claim would be strengthened by a more transparent compute comparison.

- **No variance reporting in main figures.** Results are averaged over five data splits, but standard deviations or confidence intervals are not shown in Figures 2, 3, or 5. Given that the claimed improvement over PRBCD is at some budget levels only 5–10% absolute, variance could affect conclusions. The paper would benefit from at least tabular reporting of variance.

### Trivial

- **Duplicate edge handling in the sparse encoding is underspecified.** The paper states "The perturbation vector can contain repeated elements" but does not explain how duplicates are resolved during evaluation. Since the perturbation matrix is constructed as P_z[p,q] = 1 ⇔ ∃ j: s[j] = Π⁻¹(p,q) (existential, so duplicates map to the same edge), the duplicate is harmless — but this should be stated explicitly for reproducibility.

---

## Nice-to-Haves

- Adding a random perturbation baseline for the certificate and conformal attacks would substantially strengthen the paper's secondary claims.
- Reporting the number of model evaluations used by each method (forward passes for EvA, forward+backward for PRBCD) would make the computational fairness discussion more transparent.
- Exploring hyperparameter sensitivity for mutation probability and crossover rate would improve reproducibility.

---

## Removed Points

- **Criticism that Figure 1 uses transductive setting but the paper argues transductive is unrealistic:** The paper clearly labels Figure 1 as transductive and states "For completeness, in § A we compare attacks in the transductive setting as well." This is a supplemental illustration, not a core claim. The main experiments use the inductive setup as promised.
- **Complaint about missing appendix results (Citeseer, PubMed):** The parser strips appendix sections from all papers; these results exist in the original submission.
- **"Abstract's O(ε·E) complexity is misleading because population size multiplies it":** The full paper (Section 3) gives the complete O(|S|·ε·|ℰ[𝒱_att:𝒱]|) expression including population size. The abstract's simplification is standard practice.
- **Strength Finder's generic strengths** (e.g., "the paper addressed an important problem") removed as superficial.
- **Strength about "Works under local budget constraints while still beating the local gradient alternative":** Retained as Supporting (not Core strength) but it conflates two separate results; kept in spirit but de-emphasized.

---

## Novel Insights

The reviews surface an interesting tension that the paper itself does not directly address: EvA's advantage comes from directly solving the discrete optimization problem, yet the GA is itself a heuristic with no optimality guarantees. The paper shows that the GA empirically finds better solutions than gradient descent on a relaxed problem, but the *mechanism* for why discrete search outperforms relaxed+rounding remains unclear. The ablation on fitness functions (Figure 2, left) is the closest the paper comes to explaining this: margin loss helps PRBCD but EvA+margin still outperforms PRBCD+margin, suggesting that the key advantage is the GA's ability to avoid bad local minima in the discrete space — not just the loss function choice. A formal characterization of when and why discrete search beats relaxed gradient optimization would be a valuable follow-up.

---

## Suggestions

1. **Add a random perturbation baseline** for the certificate and conformal attacks (uniform random edge flips at the same budget). If the GA outperforms random, the contribution for these objectives is validated; if not, the claim should be appropriately scoped.
2. **Run PRBCD for many more gradient steps** (e.g., 1000+) and report the results alongside the block-size scaling experiments, to fully substantiate the claim that gradient attacks "get stuck."
3. **Add error bars or variance tables** to the main results, especially for the headline comparisons in Figures 2 and 5.
4. **Clarify the duplicate handling** in the encoding: state explicitly that the mapping to the perturbation matrix uses existential quantification (∃) so duplicates are ignored, or describe the deduplication mechanism used.

---

## Score and Decision

**Calibration anchors** (all rounds):

| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| GOttack (YbURbViE7l) | 6.5 | R1/R2 | Graph attack paper accepted as Poster; shows <1% improvement over baselines; less impressive results but cleaner evaluation. EvA shows larger improvements but has evaluation gaps. |
| Long-distance Poisoning (QHfIe4chR5) | 4.5 | R1 | Rejected; limited novelty, strong threat model assumptions. EvA is substantially stronger. |
| GSBA^K (htX7AoHyln) | 6.5 | R2 | Black-box attack accepted as Poster; novel top-K setting, clean evaluations. EvA has a more foundational contribution but less complete evaluation for secondary claims. |
| Directed Graphs Robustness (oKGDfMrD4A) | 5.75 | R2 | Rejected; logic flaws, confusing contributions. EvA is clearly stronger. |
| IDEA (FPpLTTvzR0) | 6.25 | R2 | Rejected; defense paper, different domain. Not directly comparable. |
| Provable Robustness (TVwD2zIQ1F) | 6.5 | R2 | Rejected despite high scores due to limited scope. |
| GREAT (iWCfiDxLIY) | 3.0 | R1 | Withdrawn; different topic. |
| Channel Pruning Attack (4NtrMSkvOy) | 3.0 | R1 | Withdrawn; different topic. |

**Round 1 bracket:** Between ~4 and ~8 (clearly above rejected anchors but below oral-quality papers on different topics).

**Round 2 narrowing:** Compared to GOttack (6.5, accepted Poster) — EvA shows much larger improvements over baselines (~11% vs <1%), but its evaluation of novel secondary contributions (certificate/conformal attacks) lacks baselines. EvA is comparable to slightly stronger than GOttack in overall quality, but the evaluation gap tempers the score.

**Final score: 6.5.** The paper makes a clear, well-supported core contribution (GA for graph attacks outperforms gradient methods by a large margin) with practical advantages (linear memory, black-box operation). The secondary contributions (first certificate and conformal attacks) are innovative but their evaluation is incomplete. The weaknesses are fixable and do not undermine the paper's primary claims.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>