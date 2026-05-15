Now I have all the information needed to produce the final review. Let me synthesize everything.

---

## Summary

The paper proposes VTruST, a data-centric framework for controllable subset selection that balances accuracy, fairness, and robustness. The key technical contribution is an online variant of Orthogonal Matching Pursuit (OMP) that greedily replaces selected datapoints during training rather than scanning the full dataset at each selection step. The framework allows users to specify tradeoffs between trustworthiness metrics via a weighted composite value function. Empirical results on social, image, and scientific datasets show that models trained on VTruST-selected subsets achieve competitive or better fairness/robustness compared to several baselines, and the paper provides qualitative post-hoc explanations of why selected subsets are effective.

## Strengths

- **Novel online OMP algorithm for efficient subset selection.** The paper proposes an online variant of Orthogonal Matching Pursuit that handles streaming features (new columns per epoch) and a moving target vector. The DataReplace mechanism swaps a selected point when a new point improves the approximation, with per-epoch complexity O(ωM(N−ω)) instead of standard OMP's O(ωMN). This is a genuine algorithmic contribution that makes the data-centric framework computationally feasible during training. (Section 3.3, Algorithms 1 and 2)

- **User-controllable tradeoffs across multiple trustworthiness metrics.** The paper defines additive value functions for accuracy, fairness, and robustness and shows they can be linearly combined via a user-specified weight λ to form composite value functions (e.g., V_af, V_ar, V_rf). The Pareto frontier plots (Figure 1) demonstrate that varying λ yields meaningful tradeoffs. This directly supports the "controllable framework" claim. (Section 3.2, Figures 1a/1b)

- **Demonstrated effectiveness on scientific and image datasets beyond simple benchmarks.** VTruST-R is evaluated on Spinodal and EOSL particle physics datasets with label noise (Table 3) and on CIFAR10, MNIST, TinyImagenet with corrupted test sets (Table 2), showing improved robust accuracy compared to random selection and SSR baselines. The scientific dataset results (e.g., Spinodal 40% RA: 78.36 vs Random 61.11) demonstrate generality beyond standard computer vision benchmarks.

- **Data-centric explanations provide insight into selection behavior.** The analysis of selected subsets using Counterfactual Token Fairness Gap (CF-Gap) for fairness and uncertainty/distinctiveness for robustness (Section 4.3) offers a plausible account of why VTruST-selected subsets lead to improved metrics — e.g., VTruST-F subsets show lower median CF-Gap and more diverse sensitive-attribute combinations than SSFR, and VTruST-R tends to select harder augmentations (impulse noise, glass blur) rather than easier ones.

## Weaknesses

### Fatal
None.

### Major

- **The mathematical justification for the fairness value function additivity is unsound.** Line 96 claims: "$ed(\theta,\cD'_1)+ed(\theta,\cD'_2) = ed(\theta,(\cD'_1+ \cD'_2))$ also holds true, thus $\cV_f$ turning out to be additive." This is false. The function $ed$ involves a max of absolute group-wise loss differences; the max operator is not additive over disjoint validation sets. A simple counterexample: if the two validation subsets have opposing biases that cancel when combined, the sum of individual $ed$ values can far exceed the $ed$ of the combined set. Moreover, $ed$ involves $\max$ and absolute values, making it non-differentiable — the second-order Taylor expansion used to derive features $\vec{X}_i^k$ in Section 3.1 may not be valid for this objective. 

  **However**, this is not fatal: the fairness value function $\cV_f(\cD') = \sum_t \sum_i (ed(\theta_t^i,\cD')-ed(\theta_t^{i-1},\cD'))$ is *additive over training datapoints and epochs by construction* (it is a telescoping sum), which is the additivity the sparse approximation framework actually requires. The false claim about validation-set additivity is an unnecessary and incorrect justification, and the non-differentiability of $ed$ means the Taylor-expansion-based feature derivation for the fairness component lacks rigorous support. The empirical fairness results may still be valid, but the paper's theoretical scaffolding for the fairness metric is shaky.

- **The headline "∼10–20% improvement" claim in the Introduction is not consistently supported by the reported numbers.** In Table 1, VTruST-F ties FairMixup on COMPAS EO disparity (both 0.15). In Table 2, robust accuracy improvements range from ~0.6% (MNIST 60%) to ~38% (TinyImagenet 60% vs SSR) — a much wider spread than "10–20%." The paper never defines whether "10–20%" refers to absolute or relative improvement, and no single number or consistent range fits all the tables. The empirical results are still positive overall, but the specific percentage claim is exaggerated and imprecise.

### Minor

- **Theorem 1 does not provide an algorithmic guarantee.** Theorem 1 (Section 3.3) essentially restates the DataReplace module's replacement condition: if a candidate feature has higher residual correlation than a currently selected non-optimal feature with negative coefficient, it will be selected. This is a description of the algorithm's heuristic, not a theorem establishing convergence, optimality, or approximation guarantees. It contributes no formal grounding beyond what is already apparent from the algorithm description.

- **The claim that data-centric approaches "eliminate algorithmic bias" (line 24) is an overstatement.** Selecting a subset of training data is itself an algorithmic choice that introduces selection bias. The framework moves the locus of bias from the training algorithm to the data selection procedure; it does not eliminate it. The follow-up qualification ("easier to interpret") is reasonable, but the initial claim is too strong.

- **On several fairness metrics, VTruST-F is tied with or only marginally better than baselines.** On COMPAS, VTruST-F and FairMixup both achieve EO disparity 0.15. On MEPS20, FairMixup achieves EO 0.02 vs VTruST-F 0.01 (a 0.01 difference), but FairMixup's error rate is 0.89 (catastrophically high) vs VTruST-F's 0.09. The paper does not adequately discuss that FairMixup essentially sacrifices all accuracy for fairness, making the comparison less straightforward than "VTruST-F outperforms all baselines."

- **The data-centric explanations (CF-Gap, uncertainty/distinctiveness) are qualitative and anecdotal.** The analysis in Section 4.3 relies on histograms and a few hand-picked examples (10 samples per method). While suggestive, this does not establish a causal link between the selected subsets and the observed fairness/robustness outcomes. The paper would benefit from a quantitative correlation analysis (e.g., does CF-Gap distribution on the selected subset predict test-set fairness?).

- **The algorithm description contains some unclear notation.** In Algorithm 1, line 10, and Algorithm 2, the notation $\vec{X}_q^p$ for $p,q \in S_{t-1}$ is not fully explained — specifically, whether features are stored per-epoch or recomputed, and how the double index $(p,q)$ maps to the original data points. The replacement condition $(\pi' + \gamma) > \pi_{max}$ with $\gamma \leq 0$ is heuristic and is not derived from any optimization principle, which limits insight into when replacements are beneficial.

### Trivial
- The abstract contains a stray comment " <- trailing '%' for backward compatibility of .sty file" — almost certainly a LaTeX artifact from compilation, not present in the original submission.
- Some figure references (e.g., "Figure 1a") describe Pareto plots that appear only for Adult Census; the paper does not clarify whether Pareto frontiers for other datasets are qualitatively similar.

## Nice-to-Haves
- Compare VTruST-F to other *data-centric* fairness baselines (e.g., stratified sampling by sensitive attributes, influence-based selection with fairness-aware validation loss) to strengthen the claim that the advantage comes from the data-centric approach rather than the specific model-centric baselines chosen.
- Provide a sensitivity analysis of the online OMP's performance when the accuracy-only value function (which is cleanly additive) is used, to validate that the algorithm behaves as expected in the well-understood setting before moving to fairness/robustness.
- Report relative percentage improvements in a consistent manner (e.g., a dedicated column or supplementary table) to clarify the scope of the "10–20%" claim.

## Removed Points
- *Criticism about Taylor expansion truncation ignoring error terms:* This is standard practice in gradient-based value function approximations (e.g., TracIn, influence functions) and is a generic concern applicable to all such methods, not a specific flaw of this paper.
- *Criticism that UAug/SAug baselines are not described in enough detail:* The paper provides brief descriptions (Section 4.2); the level of detail is adequate for a conference paper and consistent with how baselines are described in comparable works.
- *Criticism about "not yet released" or unverifiable references:* The paper cites all baselines and datasets from published works; these exist by assumption per the review guidelines.
- *Strength about "Theoretical optimality condition guides algorithm behavior":* Theorem 1 is weak (as noted above), and claiming it as a strength overstates its value.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Fix the fairness value function additivity justification.** Remove the false claim about $ed$ being additive over validation sets. Instead, note that $\cV_f$ is additive over training points by construction (it is a sum of per-step differences), and discuss the implications of the non-differentiability of $ed$ for the Taylor expansion. Consider using a differentiable surrogate for equalized odds disparity (e.g., a soft approximation to the max) or explicitly use subgradients.
2. **Replace or qualify the "10–20%" claim** with a more precise statement (e.g., "improvements ranging from 1–40% depending on the metric and dataset") to accurately reflect the empirical results.
3. **Degenerate Theorem 1 to a remark** rather than presenting it as a theorem, since it describes the algorithm's replacement heuristic rather than providing a formal guarantee.
4. **Add quantitative correlation analysis** for the data-centric explanations (e.g., rank-correlation between per-point CF-Gap and influence on test-set fairness) to move beyond anecdotal evidence.

## Score and Decision

The paper tackles an important and timely problem — controllable data-centric trustworthy AI — and proposes a novel online OMP algorithm that is a genuine technical contribution. The empirical results are generally positive across fairness, robustness, and scientific datasets. However, the paper has a significant mathematical flaw in its justification of the fairness value function's additivity (though the core method does not collapse because the required additivity holds by construction). The performance claims are somewhat overstated, and the theoretical "theorem" is not substantive. These are real gaps but not fatal — the paper's core contribution (the online OMP framework) remains valid and the empirical results are still meaningful. With revisions to the mathematical justification and a more careful presentation of results, this could be a solid contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>