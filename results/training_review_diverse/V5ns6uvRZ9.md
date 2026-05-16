Here is the final consolidated review:

## Summary

This paper presents ACRE and OHARE, two algorithms that produce *lower bounds* (certificates) on the number of sample removals needed to shift an OLS regression coefficient along a user-specified direction. ACRE handles continuous features via a reduction to Maximal Subset Norm (MSN)-bounding. OHARE extends ACRE to datasets with one-hot encoded categorical features, using a reaveraging technique combined with dynamic programming to handle the singularities that arise. The algorithms are validated on 14 regressions from three landmark econometrics studies (Nightlights, Cash Transfer, OHIE), producing the first nontrivial robustness certificates for dimensions ≥4, with lower bounds that in some cases approach known upper bounds. The paper also provides tightness theorems showing nearly matching upper/lower bounds under distributional assumptions.

## Strengths

- **First practical nontrivial lower bounds for high-dimensional robustness auditing.** Prior algorithms either provided only heuristic upper bounds (AMIP, KZC21) or were computationally intractable beyond d ≤ 3 (Moitra et al., Freund et al.). The paper reports concrete lower bounds on k_sign for datasets with d up to 209 and n up to ~23,000 (Table 1). For example, OHARE certifies that ≥29 removals are needed to flip the main sign on the Nightlights regression (vs. upper bounds of 110–136 from AMIP/KZC21), whereas prior methods could not rule out the existence of arbitrarily small influential subsets.

- **Clever algorithmic contribution for one-hot encoded features.** The OHARE algorithm's reaveraging procedure (Gram–Schmidt orthogonalization between continuous features and dummy variables) combined with knapsack-style dynamic programming to bound removal effects per bucket is a well-motivated technical innovation. It addresses a genuine obstacle: standard spectral/continuous bounds diverge when removal empties a one-hot bucket, and the paper shows this obstacle arises in real datasets (e.g., ACRE certifying only 7 removals on Nightlights vs. OHARE's 29).

- **Rigorous theoretical analysis with technically novel concentration arguments.** The tightness proofs for both ACRE (Theorem 5.1) and OHARE (Theorem 6.1) are nontrivial and go beyond off-the-shelf tools. The divide-and-conquer concentration argument for OHARE (Lemmas 8.1–8.3, the bitwise cluster decomposition) is a technically interesting contribution that avoids stronger assumptions like |B_j| > d, and may be of independent interest.

- **Detailed empirical evaluation on benchmark datasets.** The paper audits 14 regressions from three high-profile studies, reports runtimes, memory usage, and comparisons to two baselines (AMIP, KZC21). The diagnostic use of the greedy lower bound (Algorithm 3) to identify the heavy-tailed land-ownership column and apply a log transform is a thoughtful demonstration of the tool's utility beyond just producing numbers.

## Weaknesses

### Major

- **Unclear handling of multiple categorical features in experiments.** The OHARE algorithm as presented and theoretically analyzed (Section 4, line 518) assumes *a single* one-hot encoded categorical feature: "Suppose that X_1,...,X_n ∈ R^{d+m} consist of d continuous-valued features and a single categorical feature with m categories, one-hot encoded." The analysis relies on the property that dummy columns remain perpendicular under any subset S (line 549–550), which holds for a single set of indicator variables partitioning [n]. However, several experimental datasets contain *multiple* sets of dummy variables. The Nightlights regression (Eq. 4) includes both country fixed effects (μ_i) and year fixed effects (δ_t). The paper acknowledges on line 1012 that "several different one-hot encodings" would be "beyond the scope of the OHARE algorithm" in the context of Cash Transfer data-cleaning, but does not clarify how this issue is handled in the actual experiments on Nightlights or OHIE (which also uses "several dummy variables," line 1059). The paper must either (a) clarify that only a *single* categorical feature per regression was treated with OHARE's special handling while others were included as regular features, (b) describe how multiple categorical features were combined or sequentially orthogonalized, or (c) acknowledge this as a limitation of the current experiments. Without this clarification, the reader cannot determine whether the empirical claims on these datasets are supported by the method as described.

### Minor

- **Distributional assumptions for tightness theorems are not checked against experimental datasets.** The OHARE tightness theorem (Thm. 6.1) requires that categorical features be *independent* of continuous features, that buckets satisfy n^ε√d < |B_j| < 0.49n, and that d ≤ n^{4/5}/ν. The paper does not check whether any of these conditions hold for the real datasets. This is a standard gap in theory+experiments papers (the algorithm's bounds are always valid; tightness is only guaranteed under assumptions), but a brief acknowledgment of which conditions are plausibly met or violated would strengthen the paper. The current presentation treats the theory as if it explains experimental success, when in practice the bounds may be loose for reasons the theory does not cover.

- **Scalability bottleneck acknowledged but underexplored.** The paper reports memory usage up to 51.53 GiB (OHIE Nodep Screen) and notes that storing three n×n matrices is the bottleneck (line 215–216). This limits applicability to n < ~30,000 on typical hardware. The paper acknowledges this but does not discuss potential mitigations (e.g., sketching, streaming, or block-decomposition approaches). This is a concrete practical limitation that constrains the method's utility for larger datasets.

- **The KU Triangle Inequality algorithm (Algorithm 5) is presented without runtime analysis or correctness justification.** The pseudocode is complex, and while the paper states it "uses a similar idea to RTI" (line 787), no analysis of its complexity or proof of correctness is given. Given that this algorithm is part of the OHARE pipeline used in experiments, a brief analysis would be helpful.

- **No experimental comparison showing runtime scaling with n and d.** The paper reports wall-clock times for individual datasets but does not provide a systematic scaling experiment (e.g., synthetic data with varying n,d) to demonstrate how runtime and bound quality degrade as dimensions grow. This would help readers assess applicability to their own settings.

### Trivial

- The AMIP description in the experiments section says it "does not even provide a formal upper bound on k_sign or k_sigma" (line 957), but AMIP *is* used as an upper bound in the experiments by iterative removal. This minor inconsistency in wording could confuse readers.

## Nice-to-Haves

- **k_σ bounds.** The paper focuses experiments on k_sign (sign-flip) but the introduction also highlights k_σ (shifting outside the confidence interval) as an important quantity. Reporting both would strengthen the empirical contribution.
- **A systematic comparison with prior lower-bound methods on small d (≤3) where they are tractable.** The paper states these methods don't scale to d≥4, which is plausible, but a small-scale validation on d≤3 would demonstrate that the algorithms produce comparable or better bounds on known instances.
- **Discussion of whether and how the algorithm could handle OLS with interaction terms between categorical and continuous features** (beyond the main effect), as this is common in econometrics.

## Removed Points

- *"The paper does not report k_σ bounds"* – The paper explicitly states it focuses on k_sign for comparison with prior work (line 142). This is a scope choice, not a weakness.
- *"No comparison with prior lower bounds (e.g., Moitra2022, Freund2023) on the same datasets"* – The paper explains these methods are intractable beyond d≤3 (line 82) and shows on synthetic data that Freund et al.'s algorithm yields trivial bounds (Fig. 1). This is adequately addressed.
- *"The paper does not report the upper bound from OHARE, only the lower bound"* – Not a structural issue; the lower bound is the main contribution. The upper bound is the same as ACRE's or can be trivially derived from AMIP/KZC.
- *"Typographical / formatting nitpicks"* – These are parser artifacts.
- *"Missing related work"* – Cannot verify without external sources per instructions.
- *"Missing appendix / proof details"* – The parser strips appendix material.

## Novel Insights

The key insight that emerges from this review is that the paper's main technical contribution — pushing robustness certificates past the singularity barrier caused by one-hot encodings — is both real and practically valuable. The OHARE algorithm's design (reaveraging + per-bucket MSN bounding + knapsack DP) is a principled solution to a specific problem that arises frequently in econometrics. However, the paper's framing slightly overclaims by treating all one-hot features as a single categorical variable, whereas real regressions often contain multiple sets of dummy variables (country, year, treatment group). The most interesting open question is whether the reaveraging approach can be generalized to handle multiple categorical features with non-orthogonal dummy columns, or whether a fundamentally different technique would be needed. The divide-and-conquer concentration argument (Section 8) is a genuine technical contribution that may be applicable to other problems involving averages of subgaussian vectors over a partition.

## Suggestions

1. **Clarify the handling of multiple categorical features in the experiments.** Specifically, for each dataset, state which categorical features were treated with OHARE's special handling and which were absorbed as regular features (or combined into a single categorical variable). If only one categorical feature per regression was handled by OHARE, explain why this suffices. If multiple were handled, describe the methodology and any additional assumptions.

2. **Add a limitations section** that discusses: (a) the single-categorical-feature scope of the current OHARE analysis, (b) the gap between tightness assumptions and real data, (c) the memory bottleneck, and (d) the range of n/d for which the method is practical.

3. **Add a brief correctness/runtime analysis for the KU Triangle Inequality algorithm**, or note it as a heuristic that performed well empirically.

4. **Include a small scaling experiment** on synthetic data to help readers understand how runtime and bound quality degrade with n and d.

## Score and Decision

This paper makes a compelling contribution: it introduces the first practical algorithms that produce nontrivial *lower bounds* on robustness for OLS regressions with hundreds of dimensions, validates them on important econometric benchmarks, and backs the algorithms with rigorous theory. The single unresolved issue — how multiple categorical features are handled in the experiments — is significant but does not invalidate the core algorithmic or theoretical contributions. The authors can address it through clarification in a revision.

**Score:** 7.0 / 10

**Decision:** Accept

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>