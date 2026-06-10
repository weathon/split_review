## Summary

This paper introduces RLCD, a three-phase causal discovery algorithm for linear latent causal models where latent variables can serve as causes, effects, or mediators of both observed and other latent variables. The framework leverages rank constraints (via t-separation) on observed-variable covariance matrices to identify latent variable clusters, estimate their cardinalities, and recover the full causal structure. The key theoretical contributions include a generalization of PC's nonadjacency condition to settings with latent variables, the concept of atomic covers as minimal identifiable substructures, and identifiability guarantees under specified graphical conditions.

## Strengths

- **Generalization of PC's nonadjacency condition to latent-variable settings**: Theorem 1 (lines 286–304) and the accompanying Remark provide a sufficient condition for nonadjacency between observed variables that subsumes PC's condition when no latent variables exist. This is a genuine theoretical contribution that connects rank constraints to classical conditional independence reasoning.

- **Necessary and sufficient condition for latent variable existence under mild constraints**: Theorem 5 (Theorem~6 in the paper's numbering, line 510–515) sharpens the sufficient condition from Theorem 2 to necessary and sufficient under Condition~1 (Basic Graphical Conditions). This gives a clean theoretical characterization.

- **Empirical advantage over baselines across all graph types**: Tables 1 and 2 (lines 918–1006) show RLCD achieving the highest F1 scores across three graph types (Latent+tree, Latent+measm, Latent general) and three sample sizes (2k, 5k, 10k). On the most challenging "Latent general" graphs at 10k samples, RLCD achieves 0.80 (all-variable skeleton) vs. 0.45 for Hier. rank, with a clear margin that persists across all settings.

- **Unification of prior methods as special cases**: Corollary 1 (line 911–914) formally establishes that RLCD's output matches PC's when no latent variables exist and matches Hier. rank when there are no edges between observed variables. This positions RLCD as a principled generalization rather than an isolated method.

- **Phase 3 refinement addresses a concrete failure mode**: Theorem 6 (Theorems~7 in numbering, lines 878–881) guarantees that over-clustering errors from Phase 2 can be refined by re-running the cluster-finding on a pruned graph. The paper identifies a specific algorithmic failure mode and provides a correction mechanism, which is more principled than ignoring the issue.

## Weaknesses

### Major

- **FCI evaluation in Table 2 is not adequately explained and raises credibility concerns**: FCI is the canonical method for causal discovery with latent confounders over observed variables, yet it achieves F1 scores near 0.00 on observed-variable edges in the "Latent+tree" and "Latent+measm" settings (e.g., 0.00 at 2k and 5k, 0.03–0.05 at 10k). FCI outputs a PAG, not a skeleton, and the paper does not explain how the PAG was mapped to a skeleton for F1 computation, nor what significance threshold or configuration was used. An F1 of 0.00 on a structured graph in a setting FCI was designed for strongly suggests either misconfiguration or an incorrect evaluation protocol. This undermines confidence in the baseline comparisons.

- **No runtime or scalability analysis despite explicit efficiency claims**: The paper states that RLCD is "computationally efficient and scalable" (line 580) and that the search procedure is designed for "computational efficiency" (line 588), but provides zero runtime measurements, no complexity analysis, and no scaling experiments with increasing numbers of variables. The Phase 2 search iterates over the power set of covers, drawing sets X and C subject to cardinality constraints and running a rank test plus the NoCollider check for each combination. For even moderate numbers of observed variables (e.g., 50 in the personality dataset), the combinatorial complexity could be prohibitive. An efficiency claim without any supporting evidence is not appropriate at a top venue.

- **Number of experimental trials is not specified**: The paper says experiments were run "with different random seeds" (line 1043) but does not state how many. Standard deviations are provided but the reader cannot assess how many independent runs they are based on. This is a basic reproducibility requirement.

### Minor

- **Table 1 baseline comparison is informative but should be interpreted with care**: Table 1 reports F1 for "all variables V_G (both X_G and L_G)" for methods including PC, FCI, RCD, and GIN — methods whose output does not natively include latent variables. The paper does not explain how these baseline outputs were mapped onto a graph containing latent nodes for F1 computation. The evaluation details are deferred to the appendix, but the conceptual issue (evaluating methods on a task their output representation cannot express) warrants a clearer caveat in the main text. Table 2 (observed-variable edges only) provides the appropriate comparison and should be the primary evidence.

- **Real-world personality analysis is illustrative, not evidential**: The Big Five dataset analysis (lines 1046–1055) presents a learned graph with post-hoc interpretations ("reconciles two currently deemed distinct theories of personality") but no ground truth, no quantitative evaluation, no comparison against alternative models or factor-analytic results, and no stability/robustness checks. This is a reasonable case study to demonstrate real-world applicability but does not constitute experimental validation of the method's correctness.

- **The restrictiveness of the graphical conditions is not assessed**: Condition 1 requires that no latent variable be involved in any triangle structure, and Condition 2 (the collider condition) is complex. The paper does not discuss how often these conditions hold in practice or what happens when they are violated. The synthetic data is presumably generated to satisfy them, so experimental success does not reveal behavior on non-conforming graphs. This is a common gap in theoretical papers but limits practical guidance.

- **Graph operators O_min and O_s receive limited discussion**: The identifiability result (Theorem 6/7, lines 903–908) states that RLCD identifies the MEC of O_min(O_s(G)), not of G itself. The paper notes that observational rank information is invariant to these operators, but a reader is left wondering how large the gap between G and O_min(O_s(G)) can be in practice. A concrete example showing the difference would help.

### Trivial

- None that survive filtering.

## Nice-to-Haves

- An ablation study isolating the contribution of Phase 3 (cluster refinement) would help quantify its impact and verify the conditions for its success (Theorem 6/7).
- A sensitivity analysis of the rank-testing procedure (threshold, test type, sample size) would help practitioners understand when the method can be trusted and would address the gap between asymptotic theory and finite-sample behavior.
- A targeted experiment on graphs that are provably hard for prior methods (e.g., where FCI fails due to lack of conditional independence constraints) but feasible for RLCD would more directly demonstrate the advantage of the rank-based approach.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **Rank estimation underspecified leading to irreproducibility**: The harsh critic claimed the rank-testing procedure is underspecified. However, the paper explicitly states the details are in Appendix~\ref{ranktest}. The instruction is to remove weaknesses about missing appendix content; the appendix exists in the original submission. The remaining concern about finite-sample behavior vs. asymptotic theory is addressed as a nice-to-have above.

- **Baseline comparison "fundamentally invalid" for Table 1**: The harsh critic claimed Table 1 is "fundamentally invalid" because PC, FCI, RCD, GIN do not output latent nodes. This is an overstatement. It is standard practice in latent variable discovery papers to include methods that do not handle latents as baselines to quantify the benefit of modeling latents. Table 2 provides the fair comparison on observed-variable edges. The concern is retained in weakened form as a Minor weakness above.

- **Criticism that RCD and GIN are "not state-of-the-art as of 2026"**: Without external evidence of newer methods that should have been compared against, this is speculative. The paper compares against the most directly relevant prior work (Hier. rank, 2022) and established baselines.

- **Criticism about the paper's claim that RLCD "asymptotically returns the same graph as PC"**: The critic says the precise sense requires operators deferred to appendix. This is standard for theoretical claims with proofs in appendix.

- **Strength Finder's claim about the personality analysis being a strength**: The personality analysis is illustrative, not a quantitative validation. This conflicts with a verified weakness (see Minor weakness above) and is removed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the standard tension between ambitious theoretical scope and experimental thoroughness, but do not identify observations about the work that the authors themselves missed.

## Suggestions

1. **Explain the FCI evaluation protocol and verify the configuration**: In the rebuttal, clarify how FCI's PAG output was converted to a skeleton for F1 computation, the significance threshold used, and whether the rank-based CI test used in Phase 1 was also used for FCI. If FCI was used with an inappropriate base test or incorrect edge-type mapping, re-run the comparison and update the results.

2. **Add runtime measurements**: Provide wall-clock time for RLCD across the synthetic graph sizes and sample sizes used in the paper. Scale the number of observed variables (e.g., 10, 20, 50, 100) and report how runtime grows. Without this, the efficiency claims are unsubstantiated.

3. **Specify the number of experimental trials**: State the number of random seeds/trials for all experiments.

4. **Add a brief discussion of when Condition 1 and Condition 2 are likely to hold**: Even a qualitative discussion or simple counting experiment on random graphs would help readers gauge practical applicability.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>