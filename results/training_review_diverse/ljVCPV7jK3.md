Now I have all the information needed. Let me write the consolidated final review.

## Summary

This paper addresses fair classification under the "demographic scarce regime" — where sensitive attributes are available for only a subset of data. The authors propose FairDSR, a two-phase framework: (1) train an uncertainty-aware attribute classifier using self-ensembling with Monte Carlo dropout, and (2) apply fairness constraints (via exponentiated gradient) only on samples whose predicted sensitive attributes have low uncertainty. The key insight is that enforcing fairness on samples with *uncertain* proxy attributes harms the fairness-accuracy tradeoff, while selective enforcement on *low-uncertainty* samples can shift the Pareto frontier. Experiments across five datasets (Adult, Compas, LSAC, CelebA, New Adult) compare against six baselines including proxy-based and fairness-without-demographics methods. The paper further validates the hypothesis using conformal prediction as an alternative uncertainty measure.

## Strengths

1. **Novel and well-motivated hypothesis**: The paper identifies and validates a non-obvious insight — that uncertainty in the sensitive-attribute classifier mediates downstream fairness-accuracy tradeoffs, and that selective enforcement on low-uncertainty samples yields better tradeoffs than naively using all proxy predictions. The supporting analysis (Table showing correlation between average attribute uncertainty and model unfairness; Figure showing fairness improves when training on high-uncertainty samples without fairness constraints) grounds this insight empirically.

2. **Comprehensive empirical validation**: Experiments span five real-world benchmarks, compare against six competitive baselines (FairRF, FairDA, CGL, ARL, DRO, CVaR-DRO), and evaluate three variants of the proposed method (certain, weighted, uncertain). Results are reported with standard deviations over 7 runs. The Pareto-front visualizations allow assessment across the full tradeoff space rather than cherry-picked operating points.

3. **Robustness across uncertainty measures**: The ablation with conformal prediction (Section on conformal predictions) demonstrates that the core hypothesis holds under a principled alternative uncertainty quantification framework. The consistency-loss ablation isolates the contribution of the semi-supervised training design, and the confidence-interval ablation (showing worse performance) further supports the choice of MC dropout.

4. **Well-designed ablations**: The paper systematically examines competing explanations — the uncertainty threshold ablation explores the regime where different thresholds are optimal; the consistency-loss ablation shows the teacher-student training improves uncertainty estimation; the conformal prediction ablation generalizes the finding beyond MC dropout. These strengthen the paper's internal validity.

## Weaknesses

### Major

1. **Central claim is overstated relative to the evidence**. The abstract states the framework "can outperform models trained with fairness constraints on the true sensitive attributes in most benchmarks," and the contribution list claims FairDSR "can significantly outperform" the true-attribute baseline. The evidence does not consistently support this:
   - **Adult** (Table 1): FairDSR (certain) and VanilaFairness (true attributes) are essentially tied. FairDSR is slightly better on ΔEOP (0.015 vs 0.021) but slightly worse on ΔDP (0.007 vs 0.005) and ΔEOD (0.018 vs 0.017). Accuracy differs by 0.001. These are at best comparable, not "outperform."
   - **Compas** (Table 2): FairDSR (certain) is *worse* on every fairness metric (ΔDP: 0.085 vs 0.032; ΔEOP: 0.067 vs 0.039; ΔEOD: 0.074 vs 0.041) while achieving higher accuracy (0.676 vs 0.634). This is a different point on the tradeoff curve, not a clear improvement.
   - The conformal prediction ablation on Adult shows Pareto fronts that "achieve better ... even ground truth sensitive attributes (clean)," but this is on one dataset with one uncertainty measure.

   The paper's real contribution — that uncertainty-based selective enforcement can shift the Pareto frontier in useful ways, often matching and sometimes surpassing the true-attribute baseline in specific tradeoff regimes — is still significant. But claiming systematic outperformance invites skepticism and distracts from the genuine insight. The authors should reframe the central claim to match what the evidence shows.

2. **Missing controlled experiment: separation of subset selection from proxy quality**. FairDSR (certain) enforces fairness constraints only on the subset $\mathcal{D}_1'$ (samples with uncertainty below threshold $H$), while the VanilaFairness baseline enforces constraints on *all* training data. This confounds two effects: (a) the quality of the proxy attributes on the selected subset, and (b) the fact that constraints are applied to a smaller, cleaner subset. The paper does not include the experiment of applying fairness constraints with *true* sensitive attributes on the same subset $\mathcal{D}_1'$ (and on a random subset of the same size). Without this control, it is impossible to attribute the observed improvement to the proxy attributes rather than to subset selection or reduced constraint satisfaction load.

   The uncertainty threshold ablation (Figure for ablation) partially addresses the subset-size question by varying $H$, but it does not substitute for the true-attribute-on-subset control. This experiment directly determines whether the paper's main finding is about proxy quality or about selective enforcement, and is feasible given the authors have access to true attributes.

### Minor

3. **Evaluation relies on held-out sensitive attributes that the scarce regime denies**. The paper assumes a test set where sensitive attributes are observed to report true fairness violations (30% of $\mathcal{D}_1$). The authors acknowledge this and mention active sampling as an alternative, but do not investigate whether their findings are robust to settings where even evaluation must rely on proxy-based bias estimation. For a practitioner in a genuine scarce regime, this assumption may not hold. While this is standard practice in the literature (and the paper is clear about it), a discussion of how results might change under proxy-based bias estimation would strengthen practical relevance.

4. **Tables report a single operating point without explaining selection criterion**. Tables 1 and 2 report one point per method, but the paper evaluates tradeoffs via Pareto fronts. It is unclear how the reported point was selected (fixed $\lambda$? closest to origin on Pareto curve?). The Pareto-front figures are the more appropriate comparison tool, but the tables should clarify how the representative point was chosen to avoid cherry-picking concerns.

### Trivial

- The labels "certain" and "uncertain" for the FairDSR variants are slightly misleading — "certain" means low-uncertainty, not provably certain. The paper acknowledges this framing but "low-uncertainty" / "high-uncertainty" would be more precise.

## Nice-to-Haves

- A controlled experiment using true sensitive attributes on the same low-uncertainty subset $\mathcal{D}_1'$ (this is already listed as a Major weakness — it is important enough to be required, not just nice-to-have).
- Discussion of failure modes: when would uncertainty-based selection hurt (e.g., well-calibrated attribute classifier with low uncertainty for all samples)?
- Sensitivity analysis for the $\mathcal{D}_2$/$\mathcal{D}_1$ split ratio (the paper mentions the appendix covers a 5% setting, which addresses this partially).

## Removed Points

These points from the reviewers are flagged for removal — treat with caution:

- **Harsh critic's comment about "\updated markers" suggesting revision history**: This is a formatting artifact/observation about the paper's presentation, not a substantive weakness. Removed per formatting nitpick rule.
- **Harsh critic's claim about "appendix ablation on dataset size is mentioned but stripped"**: The parser strips appendix content from all papers; the original submission contains it. Removed per rule about missing appendix criticisms.
- **Harsh critic's suggestion to rename "certain" to "low-uncertainty"**: A presentation suggestion, moved to Trivial above.
- **Strength Finder's strength #3 ("Surprising ability to match or exceed true-attribute models")**: This conflicts with the verified weakness that the "outperform" claim is overstated. The paper does show *comparable* or *better-in-specific-regimes* results, but framing this as a strength without qualification would contradict the verified weakness. The observation is retained in tempered form in the Strengths section (items 1 and 4) and in the Weaknesses section (item 1).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the central claim**. Replace "outperform models trained with fairness constraints on true sensitive attributes" with something like: "We show that strategic use of uncertainty estimates can shift the fairness-accuracy Pareto frontier, achieving tradeoffs comparable to (and in some regimes better than) models using ground-truth sensitive attributes, while outperforming all proxy-based baselines." This is honest and still a strong contribution.

2. **Add the controlled experiment**: Train VanilaFairness (true attributes) on $\mathcal{D}_1'$ (the low-uncertainty subset) and on a random sample of the same size. If true attributes on the subset match or beat FairDSR, the contribution is about subset selection; if FairDSR still wins, the contribution is about proxy quality. Either outcome is informative.

3. **Clarify how the single operating point in Tables 1–2 was selected** (e.g., "results for $\lambda = 0.5$" or "the point on the Pareto curve minimizing Euclidean distance to perfect fairness").

4. **Add a brief discussion** of how results might change if evaluation must use proxy-based bias estimation (citing Awasthi et al.'s active sampling approach as one direction).

## Score and Decision

This paper addresses a timely and important problem with a well-motivated method, extensive empirical validation across five datasets, multiple baselines, and robust ablations (consistency loss, conformal prediction, confidence intervals). The core insight — that selective fairness enforcement on low-uncertainty proxy attributes improves tradeoffs — is genuinely novel and well-supported.

However, the paper is weakened by an overstated central claim that the evidence does not fully support, and by a missing controlled experiment that would isolate the mechanism of improvement. These issues are fixable: the claim can be reframed to match the evidence (which is still a strong contribution), and the controlled experiment is feasible. With these revisions, the paper would make a solid contribution to the demographic scarce regime literature.

I recommend **conditional acceptance** subject to the authors (1) reframing the central claim to match the evidence, and (2) adding the controlled experiment separating subset selection from proxy quality.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>