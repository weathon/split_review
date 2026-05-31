Now I have a thorough understanding of the paper. Let me write the consolidated review.

---

## Summary

This paper presents SPECTRUM, a framework for structure learning of probabilistic logical models (MLNs and PSL). The core idea replaces expensive exact inference with a cheap "utility" measure computed directly from mined patterns. The paper contributes: (1) a utility measure combining precision, symmetry correction, Bayesian prior, recall, and complexity; (2) a linear-time approximate pattern mining algorithm with completeness and uncertainty guarantees; and (3) a quadratic-time greedy rule selection algorithm. Empirical results show orders-of-magnitude speedups on relational datasets.

## Strengths

- **Novel cheap utility measure replacing the inference bottleneck.** The utility measure (Definition 6) combines precision, symmetry factor, Bayesian prior, recall, and complexity, all computable directly from mined pattern counts without running inference. This flips the prior paradigm of "approximate patterns + exact inference" to "exact patterns + approximate ranking" (Section 1, "Key idea").

- **Linear-time pattern mining with theoretical guarantees.** Algorithm 1 runs in worst-case O(|V|ND) (Theorem 2). Theorem 1 provides completeness guarantees for N-close nodes. Theorem 3 gives a scaling bound N ∝ O(MD/ε²) for ε-uncertainty of utility estimates, providing a principled accuracy–runtime trade-off. These guarantees extend beyond prior work (PRISM's pattern-level guarantees) to the utility of the entire theory.

- **Orders-of-magnitude speedup with accuracy improvement on MLN benchmarks.** On IMDB and WEBKB (Table 1), SPECTRUM reduces runtime to <1% of prior art (e.g., 0.8s vs 320s for PRISM on IMDB) while improving balanced accuracy by 16–19% (0.74 vs 0.58 on IMDB; 0.81 vs 0.65 on WEBKB). These improvements are reported with standard deviations over 5-fold cross-validation.

- **Scalability to datasets orders of magnitude larger than prior methods can handle.** Table 2 shows near-linear training time scaling from 6.8k facts (Citeseer, 2.08s) to 1.14M facts (Yelp, 348s). The paper explicitly notes that MLN baselines (LSM, PRISM) cannot scale to these sizes, so SPECTRUM enables structure learning at a scale previously infeasible.

- **Discovery of hand-engineered-quality rules on real PSL benchmarks.** On CAD, SPECTRUM automatically finds all 21 rules that were hand-engineered by domain experts (Section 7.2). On Yelp, it finds 6 of 8 rules, with the remaining 2 ruled out by a deliberately imposed restriction (term-constrainedness) that the paper acknowledges.

## Weaknesses

### Fatal
None.

### Major

- **No predictive accuracy reported for the four large-scale PSL datasets.** The PSL experiments (Citeseer, Cora, CAD, Yelp) report only structure learning times and the rules discovered. The abstract claims SPECTRUM "learns more accurate logical models orders of magnitude faster than previous methods on real-world datasets," but the accuracy component of this claim is only directly supported on the two small MLN benchmarks (IMDB, ~6.5k; WEBKB, ~4.6k). For the PSL datasets (up to 1.14M facts), the reader cannot assess whether the speed gains come at the cost of predictive quality. The paper argues that matching hand-engineered rules is evidence of quality, but this indirect evidence is not a substitute for reporting AUC, balanced accuracy, or F1 on held-out data — especially since the paper already uses pslpython for inference and thus has the pipeline in place to compute these metrics.

- **No ablation study isolating the utility measure's components.** The utility measure has four interacting corrections (symmetry factor, Bayesian prior, complexity factor, log-recall), each motivated with examples. However, there is no systematic evaluation that isolates the effect of each component on final accuracy. A simple baseline using raw precision without corrections, or precision with only one correction at a time, would clarify whether the added complexity is warranted. Since the entire pipeline depends on this measure, the absence of validation is a notable gap.

- **The comparison to prior structure learners is limited to two small datasets.** On MLN, SPECTRUM is compared to LSM, BOOSTR, and PRISM. On PSL, no competing structure learner is compared (the paper acknowledges baselines do not scale). While the paper provides a reasonable justification (first structure learner for PSL, baselines don't scale), the empirical claim of superiority over "previous methods" on large datasets rests on comparing runtime numbers alone — there is no accuracy comparison against any method on large data.

### Minor

- **The BOOSTR accuracy on WEBKB (0.12 ± 0.09) is suspiciously low** — far below even random chance for a multi-class problem — and is not explained in the experiments section. The paper mentions BOOSTR's known limitations in the related work section, but the anomaly deserves explicit discussion: was this a configuration issue (BOOSTR without user-defined patterns is known to degrade), or is there another cause?

- **The greedy algorithm (Algorithm 2) first filters to the top-M rules by individual utility before ordering by contribution to theory utility.** This means a rule with medium individual utility but high complementary value (non-redundant coverage) could be discarded in the initial filter, before the greedy ordering can consider it. The paper does not discuss this limitation or its potential impact.

- **Theorem 3 assumes a Zipfian pattern occurrence distribution**, which is not verified empirically. The bound N ∝ O(MD/ε²) and the specific setting N = MD/(|V|ε²) used in experiments rest on this assumption. The paper does not check whether real datasets follow a Zipfian distribution or how sensitive the results are to violations of this assumption.

- **The completeness guarantee (Theorem 1) is restricted to "N-close" nodes**, where the condition depends on the product of binary degrees along a path. For nodes with high binary degree, this condition becomes very restrictive, meaning few nodes qualify as N-close. The paper does not discuss how often this condition is satisfied in the real datasets used.

### Trivial
None.

## Nice-to-Haves

- Report accuracy (AUC or balanced accuracy) for the PSL datasets. This would substantially strengthen the paper's central claim.
- Add an ablation study comparing: (a) raw precision, (b) precision + symmetry, (c) precision + symmetry + prior, (d) full utility.
- Validate the theoretical parameter choice by running a small experiment varying ε and N on one dataset to show the actual error in utility estimates.
- Add a brief discussion of the weight learning method used for each experiment (e.g., contrastive divergence for MLN via Alchemy, or the specific PSL inference method).

## Removed Points

These points were flagged but are removed with justification:

- *"The symmetry factor/Bayesian prior/complexity factor choices appear ad-hoc."* — Removed. The paper provides concrete examples (Examples 1–3) motivating each component and formally defines them. Calling them "ad-hoc" is a subjective assessment; the design choices are explained. The real issue (lack of ablation) is already listed as a Major weakness.

- *"The comparison is unfair because SPECTRUM is not compared to any baseline on PSL."* — Weakened and moved to Major. The paper explicitly acknowledges this limitation ("the first complete structure learner that integrates with PSL; baselines do not scale"). The remaining issue (no accuracy comparison against any method on large data) is retained in Major.

- *"Missing code for reproducibility / 'variabilising constants up to isomorphism' is vague."* — Removed. The description of pattern-to-rule mapping is standard for this literature. Code release is a nice-to-have, not a weakness of the paper's scientific content. The paper provides hyperparameter settings, dataset splits, and standard deviations.

- *"No statistical significance testing."* — Removed. The paper reports standard deviations over cross-validation folds, and the accuracy gaps are large (16–19%). Formal significance testing is not standard practice in this subfield for such clear gaps.

- *"The paper should provide learning curves."* — Removed. This is a scope-expansion request beyond what any existing baseline provides.

## Novel Insights

Beyond the paper's own contributions, the two independent reviews converge on the same structural assessment: the paper's theoretical framework (utility measure, linear-time mining, ε-uncertainty guarantees) is genuinely novel and well-articulated, but the empirical evaluation is lopsided — extensive on scalability, thin on accuracy validation for the large-scale experiments. Neither reviewer disputes the core algorithmic claims; both identify the PSL accuracy gap as the single most impactful improvement the authors could make. This unanimity underscores that the paper's thesis is credible but incompletely substantiated.

## Suggestions

1. **Add accuracy results for the PSL datasets.** This is the single highest-leverage improvement. Report balanced accuracy, AUC, or F1 for Citeseer, Cora, CAD, and Yelp using the learned rules with pslpython. Compare against the hand-engineered theories as a baseline.
2. **Add an ablation study** isolating the contributions of the symmetry factor, Bayesian prior, complexity factor, and log-recall to the final accuracy on at least one MLN dataset.
3. **Discuss the BOOSTR anomaly on WEBKB** explicitly in the experiments section — even if the explanation is that BOOSTR requires user-defined patterns.
4. **Acknowledge the "chooseTop_M" filtering limitation** in the algorithm description, and consider whether a two-stage selection (e.g., top-2M then greedy) would mitigate it.
5. **Report the actual ε-uncertainty achieved** in practice for at least one dataset, rather than just using the theoretical bound as a parameter-setting rule.

## Score and Decision

**Originality:** High — flipping the paradigm from expensive exact inference to cheap approximate ranking is a genuinely novel idea for this problem space.  
**Importance of question:** High — structure learning scalability is a well-recognized bottleneck in neurosymbolic AI and probabilistic logic.  
**Claims support:** Moderate — the scalability and speed claims are well-supported; the accuracy claim is only supported on two small datasets and indirectly on PSL through rule discovery.  
**Soundness of experiments:** Moderate — proper protocols (cross-validation, standard deviations, comparison to standard baselines on MLN), but missing accuracy evaluation on the largest datasets.  
**Clarity of writing:** Good — the paper is generally well-structured and the formal definitions are clear.  
**Value to community:** High — if the accuracy results on PSL bear out, this could significantly advance structure learning practice.

The paper makes a clear algorithmic contribution with theoretical backing and demonstrates substantial speed improvements. The main weakness is the incomplete accuracy evaluation on the PSL datasets, which is a significant gap but not a fatal flaw given the paper's other contributions. With accuracy numbers for PSL, the paper would be strong.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>