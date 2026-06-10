## Summary

This paper investigates how adapter placement in transformer networks affects transfer learning performance. It formalizes the search space as a graph, introduces long-range and recurrent adapters beyond standard parallel/sequential placements, and shows empirically that placement significantly impacts performance in a task-dependent manner. The paper further proposes the Gradient Guided Adapters (GGA) algorithm, which uses gradient rank to greedily select adapter locations. On iNaturalist18, GGA matches 24 parallel adapters with as few as 3 adapters, and the approach scales to a 1-billion-parameter ViT-g/14 model.

## Strengths

- **Empirical demonstration that placement matters and is task-dependent (Figure 1, Section 3.3):** On SVHN, early-layer placement is best; on Clevr-Count, the same placement is the worst. The cross-task correlation matrix (Figure 3) quantifies non-transferability, with near-zero correlations between small VTAB-1K datasets. This directly challenges the common practice of uniform adapter insertion.

- **Principled graph-based formalization of the search space (Section 4):** The paper shows standard parallel/sequential placements cover only (2n-1)/n² ≈ 8% of possible connections for ViT-B. The single-adapter heatmaps (Figure 3) then demonstrate that recurrent adapters (i>j edges) consistently appear among top-3 placements across iNaturalist18, Places365, Clevr-Count, SST2, and MNLI. The control for FLOPs (ruling out edge (24,0) as the optimal recurrent placement) strengthens the finding.

- **Concrete efficiency result from GGA (Figure 5a,b):** GGA matches the performance of 24 parallel adapters using ~3 adapters on iNaturalist18 and ~12 on Places365 — an up to 8× reduction. The algorithm is simple, the discounting mechanism is intuitively motivated, and the comparison against top-k, first-k, last-k, and random selection is reasonable.

- **Scaling demonstration on ViT-g/14 (Figure 5c):** GGA is evaluated on a 1-billion-parameter model with 40 layers (6561 possible locations), consistently outperforming parallel adapters especially in low-parameter regimes. This confirms the approach is not limited to small architectures.

## Weaknesses

### Fatal
None.

### Major

- **The claim that gradient rank is the best predictor among "various options" is asserted without empirical evidence.** Line 237 states: "We investigate various options, including the common matrix norms and find that the rank of the gradient matrix shows the strongest correlation with single-adapter training loss and test accuracy." No table, figure, or ablation comparing rank against Frobenius norm, spectral norm, trace, or any other matrix statistic is provided anywhere in the paper. The only justification is an intuitive argument about scale-invariance. Since the paper's central methodological contribution (and the entire GGA algorithm) depends on *rank specifically* being the right aggregation function, this is a significant evidential gap. The paper should report Spearman correlations for competing metrics on at least one dataset to support this claim.

- **GGA is evaluated only on the two vision datasets where gradient-rank correlation is strongest (iNaturalist18, Places365).** The text datasets (MNLI, SST2) and remaining VTAB tasks — where the paper acknowledges correlation is "significantly lower" (line 251) — are never tested with GGA. This leaves the question of GGA's generality substantially open. The paper's conclusions about GGA being an effective selection strategy are contingent on an unstated precondition. At minimum, GGA should be evaluated on MNLI and SST2.

- **No sensitivity analysis for the discount parameter γ.** Only γ=0.6 is used and compared against γ=0 (no discounting). Without a sweep (e.g., γ ∈ {0.2, 0.4, 0.6, 0.8, 0.99} on one dataset), it is impossible to know whether the specific value is critical or whether any distance-based discounting suffices. (Anchored in Section 6.2, line 287.)

### Minor

- **The "random" baseline in the GGA experiments (Figure 5) is not clearly defined for varying N.** Section 5.2 samples 100 random combinations of *24 adapters* and reports the *maximum* performance. How this baseline is constructed for smaller adapter counts (3, 6, 12, etc.) is not explained, making the comparison partially opaque.

- **The adapter bottleneck rank r is not specified for the ViT-B experiments.** The paper defines r as the adapter's bottleneck dimension (line 66) and varies it in the ViT-g/14 experiment, but never states the value used for the main ViT-B/16 results across all datasets. This affects the parameter count and thus the fairness of comparisons in Table 1 and Figure 5.

- **The claim that GGA "requires significantly less computation" (line 31) is unquantified.** The scoring procedure requires forward pass + backward pass + SVD-based numerical rank estimation for all 625 (or 6561) placements. No wall-clock time or FLOP comparison is provided against alternatives (e.g., training a few adapters or a small grid search).

- **Spearman correlation values are shown only as labels in Figure 4 rather than in a table.** While the figure is readable, a table would enable precise comparison and make the paper more useful as a reference.

### Trivial
None.

## Nice-to-Haves
- Ablation comparing gradient rank against Frobenius norm, spectral norm, and trace as predictors on one dataset.
- γ sensitivity sweep on iNaturalist18 or Places365.
- GGA evaluation on MNLI and/or SST2.
- Specification of adapter rank r used in all experiments.

## Removed Points
Points from the inputs that were filtered out with brief justification:

- **"Extended MAX comparison is biased"** (Harsh Critic's Critical Issue 1): The paper explicitly frames Table 1 as an existence proof (line 185: "Our aim is to demonstrate the *existence* of better placement assignments"). For an existence claim, comparing the max over 100 random draws against fixed baselines is the correct protocol — the question is "does a better configuration exist?" not "is the extended space typically better?" The paper's conclusion phrasing is slightly loose but not methodologically flawed. This does not belong as a major weakness.

- **"Gradient rank correlation is selective" as a fatal flaw**: The paper acknowledges weaker correlation on dSpr-Loc, SVHN, SST2 (line 251). The paper does not claim universal strong correlation. This is an honest reporting of empirical results, not a flaw.

- **"Missing baselines: random search in extended space"** (part of Critical Issue 4): The paper *does* compare against random selection from Section 5.2. The construction for varying N needs clarification but the baseline exists.

- **"No statistical testing"**: Reporting means and standard deviations is standard for this type of empirical work.

- **Missing related works**: Cannot verify external literature; removed per hard rules.

- **Formatting/style/typo complaints**: These are parser artifacts, not author errors.

- **Strength Finder's generic strengths** (e.g., "the problem is important"): Removed as insufficiently specific to this paper's concrete contributions.

## Novel Insights

The reviews surface one useful observation beyond the paper's own framing: the finding that gradient rank correlates well on large datasets but poorly on small ones (dSpr-Loc, SVHN, SST2) creates an ironic tension — the predictor is weakest on the very VTAB-1K tasks where exhaustive search is most feasible (only 1,000 training examples) and strongest on the large datasets where training an extra adapter for comparison is also relatively cheap. This tension is acknowledged by the paper but not deeply analyzed; it represents a meaningful direction for future work on the practical utility of this approach.

## Suggestions

1. **Essential:** Provide a table comparing Spearman correlations of gradient rank vs. Frobenius norm, spectral norm, and trace for at least one vision dataset and one text dataset. This is necessary to support the claim that rank is the best aggregation function.
2. **Essential:** Evaluate GGA on MNLI and/or SST2 to bound its generality beyond the two favorable vision datasets.
3. Add a γ sensitivity plot on iNaturalist18 (γ ∈ {0, 0.2, 0.4, 0.6, 0.8, 0.99}) to show robustness.
4. Clearly specify the adapter rank r used for ViT-B experiments.
5. Clarify how the "random" baseline in Figure 5 is constructed for each adapter count N.
6. Report Spearman correlations in a table, supplementing Figure 4.
7. Provide a rough wall-clock or FLOP estimate for the GGA scoring procedure.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>