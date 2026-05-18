Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper presents an EM-based unified framework for non-negative tensor decomposition that optimizes the Kullback–Leibler divergence. The key insight is establishing a relationship between low-rank tensor approximation and many-body approximation, which yields closed-form update rules for the M-step across CP, Tucker, and Train decompositions. The framework also supports mixtures of low-rank tensors and adaptive noise terms. Experiments on eight categorical datasets compare the method against MPS, Born Machine, and Locally Purified State baselines, with the proposed mixture model (CPTrainON) reported to achieve the best performance on seven of eight datasets.

## Strengths

- **Closed-form M-step for Tucker and Train decompositions.** The paper derives exact closed-form solutions for the many-body approximation of Tucker (Equation 5) and Train (Equation 6) decompositions, enabling updates of all parameters without gradient methods or inner iterations in the M-step. This directly eliminates learning-rate tuning and double-iterative optimization, a concrete advance over prior piecemeal approaches.

- **Unified EM framework handling multiple low-rank structures and mixtures.** Section 3.1 presents a single EM-based objective (Equation 7) that generalizes across CP, Tucker, and Train decompositions, their mixtures, and adaptive noise terms — with both the E-step and M-step being convex. The framework also handles tree-structured tensor networks (Section 3.3) by decomposing them into solvable many-body approximations.

- **Convergence guarantee without learning rate tuning.** The EM procedure is guaranteed to monotonically increase the objective function (referenced to Theorem in supplementary), a formal advantage over gradient-based alternatives that require careful learning-rate selection.

- **Linear computational complexity in the number of observations N.** Section 3.2 derives that EM-CP has complexity O(γ N D R) and EM-Train has O(γ D N R²), exploiting sparsity of the empirical tensor. This addresses the scalability challenge raised in the introduction.

- **Adaptive noise term for robust modeling.** Section 3.4 introduces a learnable uniform-noise component for regularization. The paper reports (Table 2 in supplementary) that this prevents large errors when models are overparameterized, and the noise mixing parameter is learned from data rather than set as a hyperparameter.

- **Strong empirical results on real categorical benchmarks.** Table 1 shows CPTrainON achieving the lowest test cross-entropy on 7 of 8 datasets against established tensor-network baselines (MPS, BM, LPS).

## Weaknesses

### Fatal
None.

### Major

- **Asymmetric application of mode reordering creates a fairness concern in baseline comparisons.** The proposed CPTrainON includes a data-dependent mode reordering based on pairwise NMI (lines 209–210). MPS is functionally equivalent to a tensor train decomposition and is known to be sensitive to mode ordering — the paper itself acknowledges this ("The tensor train decomposition results are influenced by the order of the modes"). However, the reordering is not applied to the MPS (or BM/LPS) baselines. Since MPS accuracy can vary significantly with mode ordering, the baselines may be operating at an artificial disadvantage. The paper defers analysis of reordering effectiveness to the supplementary material but does not address this fairness concern in the main experimental design. This weakens the claim of "superior generalization compared to conventional tensor-based approaches" made in the abstract, because the reported advantage is partially confounded with a preprocessing step that is not shared with baselines.

### Minor

- **The main table does not compare individual EM methods to baselines on test data.** Table 1 only reports the full mixture model CPTrainON (with reordering + noise + mixture) against baselines. While Figure 2 shows validation curves for individual methods (CP, Train, Tucker, CPTrain), it does not directly compare them to baselines on the test set. The paper references supplementary material ("A more detailed comparison, including EMCP, can be found in Section~\ref{ap:sub:exp}") but the main text leaves unaddressed whether a single-component EM-Train or EM-Tucker already outperforms baselines, or whether the improvement comes primarily from the mixture/noise/reordering additions. The core contribution of the unified closed-form EM would be more convincingly validated by showing individual methods against baselines in the main table.

- **The "simultaneous closed-form updates" phrasing slightly overstates the Train case.** The abstract and contribution list state the framework provides "simultaneous closed-form updates for all parameters in the M-step." For Train decomposition, the efficient computation of Equation (8) requires sequential cumulative products (Equation 13), and the tensor M used in the update depends on the current estimate of all cores via Φ = Q/P. While it is true that no inner gradient iterations are needed — all cores are updated once per M-step from the same E-step result — the phrasing "simultaneous" could be misinterpreted as implying fully parallelizable parameter updates, which is not strictly the case for Train. The paper would benefit from clarifying this.

- **No analysis of the Chess2 failure case.** The method does not beat baselines on Chess2 (the paper states "CPTrainON has the best generalization performance on all datasets except Chess2"). No explanation or analysis is offered for why the method fails on this particular dataset, which would help delineate the method's limitations.

- **Runtimes and convergence speed not reported.** While the paper provides theoretical complexity analysis, an empirical comparison of wall-clock time or iterations-to-convergence against baselines (especially on the largest dataset) would substantiate the claimed scalability advantage.

### Trivial
None.

## Nice-to-Haves

- Applying the proposed mode reordering to MPS baselines to assess whether the reported advantage shrinks or disappears.
- Including an ablation table in the main text showing test performance of (i) plain single decomposition, (ii) + noise, (iii) + reordering, (iv) + mixture, alongside baselines.
- A brief derivation sketch of the closed-form solution for at least one of Tucker/Train in the main text (e.g., using Lagrange multipliers) to make the main body more self-contained.
- Reporting initialization sensitivity more comprehensively (e.g., best-run results or histograms over seeds, not just standard errors).

## Removed Points

- **"Closed-form solutions require verification / proofs are in supplementary":** The harsh critic questions the correctness of Equations (6) and (8) because proofs are deferred to supplementary material. Per review policy, missing appendix content is a parser artifact and should not be considered a weakness. The paper states "We formally derive the above closed-form solutions in Theorems~\ref{th:Tucker} and~\ref{th:Train} in the supplementary material" — this is standard practice and not a flaw.

- **"Missing comparison to standard non-negative tensor factorization methods (Huang et al. 2017)":** The paper cites Huang et al. 2017 (for EM-CP) and states that a comparison including EMCP is in supplementary. The baselines used (MPS, BM, LPS) are the established tensor-network density estimation methods from the relevant literature (glasser2019expressive). Demanding exhaustive comparisons to every related method is scope creep.

- **"Transition from MBA objective to closed-form formulas is abrupt":** This is a presentation preference, not a substantive weakness. The paper provides the formulas and references theorems in supplementary.

- **"Reordering algorithm is vague":** The paper actually provides a concrete step-by-step example with 5 features (lines 210), and the reordering is a heuristic preprocessing step whose effectiveness is analyzed in supplementary.

- **"Standard errors are insufficient / need statistical significance tests":** Reporting means and standard errors from 10 random initializations is standard practice for this type of experiment. Demanding formal significance tests is a nice-to-have, not a weakness.

- **"Mixture model is not a direct validation of the framework's core contribution":** The paper shows validation curves for individual methods (Figure 2) which partially addresses this. The claim is about the framework's flexibility, not that every individual method beats baselines. This overstates the concern.

- **All pure formatting, typos, or presentation nitpicks** are parser artifacts and removed per policy.

## Novel Insights

None beyond the paper's own contributions. The reviewers' analyses largely recapitulate what the paper itself makes clear: the core contribution is the closed-form MBA-to-low-rank connection; the main weakness is that the experimental comparison does not fully isolate the effect of the core contribution from the additional components (reordering, mixture, noise).

## Suggestions

1. **Apply the same mode reordering to MPS baselines** (or compare without reordering) to establish a fair baseline comparison. This is the single most impactful improvement.
2. **Add a test-set comparison table** showing EM-CP, EM-Train, EM-Tucker (each with noise term) against MPS, BM, LPS alongside CPTrainON, so readers can see the contribution of each component.
3. **Rephrase "simultaneous closed-form updates"** to something like "closed-form updates for all parameters in each M-step without inner iterations" to avoid any misinterpretation about parallelism.
4. **Include a brief derivation sketch** for one of the closed-form solutions (e.g., the Tucker case via Lagrange multipliers) in the main text, so the core mathematics is accessible without the supplementary.
5. **Add a brief discussion** of why Chess2 is a failure case and what characteristics of the dataset cause difficulty.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>