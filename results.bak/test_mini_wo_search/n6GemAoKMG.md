Good, I've verified the key claims. The paper explicitly states they scaled PRBCD by increasing both the number of steps AND the block size — the harsh critic's claim that they "only increase the block-coordinate subspace size" is factually incorrect. Let me now write the consolidated review.

## Summary

The paper proposes EvA, a genetic-algorithm-based framework for adversarial attacks on graph structure that directly optimizes discrete edge perturbations without gradient relaxation. EvA achieves substantially larger accuracy reductions than the state-of-the-art gradient-based attack PRBCD across three benchmark datasets (CoraML, Citeseer, PubMed) and multiple GNN architectures, and its black-box nature enables two novel attack objectives: reducing randomized-smoothing certificates and breaking conformal prediction guarantees.

## Strengths

- **Consistent and large accuracy improvement over SOTA.** EvA outperforms PRBCD by a notable margin across all datasets, models (GCN, SoftMedian-GDC), and budgets tested. For example, on CoraML with GCN at 5% budget, EvA achieves 50.8% accuracy vs. PRBCD's 61.2% (Fig. 5), with average gains of ~11% reported. The gap is consistent across vanilla and adversarially trained models.

- **Novel attack objectives enabled by black-box optimization.** EvA introduces the first graph structure attack on randomized-smoothing certificates (reducing certified ratio below the MLP baseline) and the first attack on conformal prediction for inductive GNNs (Fig. 4). These objectives involve non-differentiable operations (majority voting, quantile computation) that would require complex relaxations for gradient-based methods but are trivial to define as fitness functions in EvA.

- **Memory-efficient sparse encoding (Section 3).** EvA encodes perturbations as index vectors rather than dense gradient matrices, yielding O(|S|·ε·|E|) memory complexity compared to the O(|S|·n²) of naive gradient-based approaches. This is a genuine practical advantage.

- **Direct discrete optimization avoids gradient pitfalls.** Section 4 shows that even when using the same margin-based loss function as PRBCD, EvA substantially outperforms it (Fig. 2, left), demonstrating that the advantage comes from the discrete search itself, not from a different loss function.

- **Fine-grained analysis of attack solutions (Fig. 7).** The label-diversity, degree-distribution, and margin analyses provide concrete insight into *why* EvA finds better solutions: it distributes perturbations more uniformly across classes and targets higher-margin/higher-degree nodes compared to PRBCD's more concentrated perturbations.

## Weaknesses

### Fatal
None.

### Major

- **Computational budget is not controlled in the comparison.** The central empirical claim — that EvA reveals gradient-based attacks to be far from optimal — is confounded by asymmetric compute budgets. EvA uses a population of hundreds of individuals over many generations, each requiring forward passes. While the paper attempts to scale PRBCD (increasing both steps and block size, Fig. 3) and notes the query-cost limitation, there is no direct comparison at matched forward-pass counts or wall-clock time. Without this, the reader cannot determine whether EvA's advantage comes from fundamentally better search or simply from using orders of magnitude more model evaluations. This weakens the message that "gradient-based attacks are suboptimal" — it may simply be that the gradient-based method was given less compute. The paper acknowledges query cost in its limitations, but the main results are presented without this caveat foregrounded.

### Minor

- **No variance information in main figures.** Results are averaged over five data splits (standard for this literature), but no error bars, standard deviations, or confidence intervals appear in any main figure (Fig. 1, 2, 3, 5, 6). While the gaps are large enough that statistical significance is plausible, the reader cannot assess whether the reported differences are systematic or within the noise of the evaluation.

- **Novel-objective evaluations are thin.** The certificate attack is demonstrated on only one dataset (CoraML) with one configuration (B_{0,3}, sparse smoothing). The conformal attack shows coverage *decreases* as budget increases, but does not explicitly verify whether coverage drops *below the nominal 1-α guarantee* (which would truly "break" conformal prediction). The set-size attack similarly shows increases but no critical threshold. These attacks are interesting but need more thorough evaluation to fully substantiate.

- **The headline 11% claim lacks direct support in the main text.** The abstract's claim that "EvA reduces the accuracy by an additional ~11% on average" is not accompanied by a table or explicit computation in the main body. While the figures (e.g., Fig. 5) visually support substantial gaps, the headline quantitative result should be reported explicitly with uncertainty.

- **Evaluation limited to three small datasets (CoraML, Citeseer, PubMed).** These are standard benchmarks, but they are all under 20k nodes. The paper acknowledges scalability concerns in its limitations, but the lack of any results on a moderately larger graph limits the generality of the claimed significance.

- **"Stacking perturbations" technique is underspecified (Section 4).** The paper states that perturbed graphs are "combined into one large (disconnected) graph" for batched inference, but does not explain how disconnected graphs are combined in practice (e.g., block-diagonal construction, handling of feature matrices, padding). This is important for reproducibility.

### Trivial
None.

## Nice-to-Haves

- Include simpler search-based baselines (random search, hill climbing, beam search) to isolate whether the GA's sophistication is necessary or any search approach outperforms gradients.
- Provide wall-clock time or forward-pass counts alongside accuracy comparisons.
- Add hyperparameter sensitivity analysis (population size, mutation rate, number of generations) to guide practitioners applying EvA to new datasets.
- For the conformal attack, explicitly test whether coverage drops below the 1-α guarantee.

## Removed Points

These points were raised by reviewers but are removed or corrected after cross-checking against the paper:

- **"PRBCD was not scaled on number of steps"** — The paper *explicitly* states (Section 4, Fig. 3): "For a fair comparison, we also attempted to scale PRBCD by increasing the number of steps and the size of the block coordinate subspace." The reviewer's claim that "they only increase the block-coordinate subspace size, not the number of steps" is factually incorrect. Removed.

- **"Memory complexity claim is misleading"** — The reviewer argues that the paper's claim about quadratic memory for gradient-based methods is misleading because PRBCD uses blocks. The paper's claim refers to general gradient-based attacks, and the paper itself notes "tricks like block coordinate descent are needed." The statement is accurate in context. Removed.

- **"Code not provided"** — The paper states "we have uploaded the complete anonymized codebase on OpenReview." This is standard for double-blind review. Removed per instructions about reproducibility nitpicks.

- **Generic speculative concerns** (e.g., "could the metric be measuring a proxy?", "are confounders controlled?") that lack a concrete anchor in the paper text. Removed.

- **Generic strengths** (e.g., "this paper addressed an important problem") that lack specific evidence. Removed.

## Novel Insights

Both reviewers independently converge on the observation that the paper's main contribution is not the GA itself (which is off-the-shelf) but the *demonstration that discrete search consistently finds qualitatively different and substantially better attack solutions than gradient-based methods*. The label-diversity and margin analyses (Fig. 7) are particularly illuminating: they show EvA does not simply find "more of the same" but discovers a fundamentally different class of solutions (more evenly distributed across labels, targeting higher-margin nodes). This reframes the contribution from "we built a better attack" to "here is evidence that the gradient-based attack paradigm systematically under-explores the solution space." The novel-objective attacks (certificates, conformal) then follow naturally from this paradigm shift rather than being add-ons.

## Suggestions

1. **Control for computational cost.** Add an experiment matching forward-pass counts (or wall-clock time) between EvA and PRBCD, showing accuracy reduction vs. compute budget. If EvA still wins at matched budget, the claim becomes unassailable.
2. **Add error bars** to all main figures. If 5 splits are insufficient for meaningful error bars, increase to 10+ splits or report bootstrapped confidence intervals.
3. **Explicitly compute and report the 11% claim** in a table with standard errors, broken down by dataset/model/budget.
4. **Strengthen the novel-objective evaluations:** show certificate attack on a second dataset; for the conformal attack, explicitly check whether coverage drops below 1-α.
5. **Add one moderately larger dataset** (e.g., ogbn-arxiv with subsampled test set, or full PubMed) to partially address the scalability concern.
6. **Clarify the stacking perturbations implementation** with pseudocode or a diagram showing how disconnected graphs are batched.

## Score and Decision

This paper makes a genuine contribution: it demonstrates that discrete evolutionary search consistently finds substantially better graph attacks than gradient-based methods, and the black-box formulation unlocks entirely new attack objectives. The core claims are supported by consistent evidence across multiple datasets, models, and training setups. The main weaknesses — uncontrolled compute budget, absent variance reporting, thin novel-objective evaluation — are real but addressable in revision and do not undermine the paper's central insight. The paper is clearly above the acceptance bar for a top venue.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>