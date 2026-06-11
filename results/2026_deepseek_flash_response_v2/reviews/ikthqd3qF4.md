## Summary

This paper proposes a novel theoretical framework for deriving observable lower bounds on precision and recall in unsupervised record linkage, exploiting a structural constraint (at most one first-lien mortgage per individual). The key result (Theorem 1) bounds precision from below using only the unconditional origination probability and the observed fraction of clusters with multiple originations — requiring no labeled data. The authors instantiate this with a hierarchical clustering algorithm applied to 65.5M HMDA mortgage records, reporting 92.3% precision at their preferred specification. A simulation validates that the bound closely tracks true precision.

## Strengths

1. **Label-free precision bound from observable quantities (Theorem 1).** The derivation is clever and genuinely novel: precision ≥ 1 − Pr[Mult]/p² depends only on two observable quantities. The structural constraint (at most one first-lien mortgage per person) guarantees true-positive clusters have zero probability of multiple originations, so any observed cluster with multiple originations is necessarily a false positive. This insight enables model evaluation without any ground-truth labels — a distinctive contribution relative to prior record-linkage work.

2. **Empirical validation that the bound tracks true precision in simulation.** Figures 3a (true precision from ground-truth identifiers) and 4a (label-free lower bound) show close correspondence. At ε=0.06 in the "with date" specification, the bound is 93.7% while true precision is ~95%. This is the strongest evidence that the theoretical machinery works in practice — the bound is not just valid but reasonably tight in a controlled setting.

3. **Scalable implementation on 65.5M records.** The paper adopts the nearest-neighbor chain algorithm for complete-linkage clustering (O(ℓ²) worst-case), making agglomerative clustering feasible at scale. The combination of a novel theoretical bound with a scalable implementation is what makes the empirical application possible.

4. **Extended bounds for recall and model selection (Corollaries 1 and 2).** These show that hyperparameter tuning reduces to maximizing fully observable quantities, because P_tot cancels out as a constant. This provides a principled model-selection framework from a single structural constraint, with practical utility demonstrated via the frontier in Figure 5.

5. **Practical refinement by discarding known false positives (Equation 1).** Clusters with multiple originations are guaranteed false positives and can be removed, yielding a strictly tighter precision bound. This is a simple but effective post-processing step.

## Weaknesses

### Major

- **No comparison to alternative record-linkage methods.** The paper presents its clustering algorithm and bounds without comparing to any baseline (e.g., exact matching on key fields, threshold-based matching, probabilistic Fellegi–Sunter models, or learned matching approaches). The simulation compares "with date" vs "without date," which is an ablation within the same method, not a comparison to an alternative approach. Since the paper lists the clustering instantiation as its second contribution, readers cannot assess whether this specific algorithm is effective relative to reasonable alternatives. Adding even simple baselines would substantiate the claim that the bounds "enable both hyper-parameter tuning and cross-model comparisons," which is currently demonstrated only for tuning ε within a single algorithm.

### Minor

- **The "92.3% precision" headline omits that it is a lower bound.** The abstract states "Our preferred specification identifies cross-applicants with 92.3% precision" without saying "at least." The conclusion similarly says "achieving an estimated precision of 92.3%." While the body correctly frames it as a bound (Section 2.2, Theorem 1), the abstract's phrasing naturally reads as a point estimate. This is a presentation issue, not a technical error, but it overstates the finding.

- **The recall of 92% is reported only in the simulation (line 216), but the abstract's "minimal loss in relative recall" appears adjacent to the 92.3% figure.** This could mislead readers into thinking both precision and recall are known for the real application, when recall cannot be measured in the HMDA data because P_tot is unknown. The distinction between simulation and application is correct in the body but could be sharper.

- **Assumption 1 (independence of origination decisions across borrowers) receives only brief discussion.** The paper asserts the assumptions "do not appear very strong" (line 138) but does not discuss how macroeconomic correlations (interest rates, housing prices) would affect the bounds. To the credit of the authors, positive correlation would tighten rather than loosen the bound, making the reported 92.3% conservative. But this reasoning is not articulated in the paper, and a sensitivity analysis would strengthen trust in the method.

- **The empirical origination probability p̂ for the HMDA data is not reported.** In the simulation, p̂ = 0.7917 is stated explicitly. For the real application, the reader cannot assess how p̂² relates to Pr[Mult] and thus cannot gauge how informative the bound is without performing their own calculation. This is a straightforward omission.

- **Restriction to size-2 clusters is acknowledged but not justified in substance.** Footnote 4 says clusters with more than two applications are dropped "to keep the discussion as simple as possible." This discards cases where an individual submits three or more near-identical applications, which could be substantively important. The paper does not report how many such larger clusters were excluded or whether they are rare enough to ignore.

### Trivial

None.

## Nice-to-Haves

- Provide full details of the 96 distance-function/ε combinations tested in the main text, or at least characterize the types of distance functions used.
- Add a simulation that more closely mimics the real HMDA data's covariate distribution and noise structure, to strengthen the bridge between simulated and real-data performance.
- Report the empirical bounds' sensitivity to the choice of partition variables.

## Removed Points

The following points from the Harsh Critic were removed per protocol:

1. *Missing related work discussion (record linkage literature).* — Per protocol: "DO NOT mention missing related works, as you do not have external sources to confirm their existence."
2. *The bound could be far from true precision in real HMDA data.* — Speculative: no evidence is presented that the bound is loose, and the simulation suggests it is reasonably tight. This is a valid concern but not verifiable as a weakness from the paper alone.
3. *Criticisms about missing appendix contents.* — Per protocol: appendices exist in the original submission and were stripped by the parser.
4. *References to "not yet released" or reproducibility concerns about confidential data.* — Per protocol: cited datasets are assumed to exist.
5. *Section-by-section notes about the proof being in the appendix.* — Per protocol: appendices exist in the original submission.
6. *Formatting/style nitpicks.* — Per protocol.
7. *The critic's "no evidence about tightness in the real HMDA data" claim is demoted from fatal to minor because it is speculative* — the bound is mathematically valid; looseness would only make it more conservative.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a useful observation that the theoretical framework could be strengthened by demonstrating cross-model comparisons, but this is already implied by the paper's framing.

## Suggestions

1. Reframe the abstract's headline claim as "precision of at least 92.3%" to accurately reflect that this is a lower bound.
2. Add at least 2–3 baselines (e.g., exact matching, threshold-based matching, a simple learned approach) to the simulation to contextualize the clustering algorithm's performance.
3. Report p̂ and Pr[Mult] for the HMDA application so readers can independently assess bound tightness.
4. Discuss how violations of Assumption 1 would affect the bound, particularly noting that positive correlation makes it conservative.
5. Provide summary statistics on how many size-3+ clusters were excluded and whether their inclusion would change the results.

## Score and Decision

**Calibration anchors used:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| f9RvYpXhFI.md (Frechet bounds) | 5.50 | R1 | Weaker: Our bound is cleaner, doesn't require P(Y|Z), has simulation validation |
| HvkXPQhQvv.md (SSME) | 6.00 | R1 | Comparable: Similar quality, our contribution more novel, their experiments more comprehensive |
| oyFCgkkLUK.md (αMax-B-CUBED) | 4.75 | R1 | Weaker: Much smaller scope, limited experiments |
| 6tqgL8VluV.md (Learned DB Ops) | 6.00 | R2 | Comparable: Both have theoretical contributions with some evaluation gaps |

**Round 1 bracket:** The paper sits between the weak band (avg < 3.5, topically unrelated papers) and the strong band (avg > 7.5, papers with thorough evaluations). The middle band anchors ranged from 4.75 (αMax-B-CUBED) to 6.00 (SSME). Our paper is clearly stronger than 4.75 papers and comparable to 5.5–6.0 papers. **Round 2 narrowing:** The learned DB Ops paper (6.00) is the closest comparator — both have theoretical lower-bound contributions with some empirical evaluation gaps. Our paper has a cleaner theoretical result (no need to estimate P(Y|Z)) and stronger simulation validation, but shares the weakness of missing important baselines. **Final score 6.0,** positioned near the upper end of comparable anchors because the core theoretical contribution is cleaner than the Frechet bounds paper (5.5), but not above 6.5 due to the lack of baselines and the framing issue.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>