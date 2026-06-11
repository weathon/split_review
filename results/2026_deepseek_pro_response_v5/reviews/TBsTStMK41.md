Now let me finalize the review with the complete analysis. The comparison is clear: my paper is stronger than the rejected k-hyperplane clustering paper (5.0 — simulated data only, potential error in a corollary) and comparable to Light-MILPopt (5.0, accepted — but with more technical ML novelty). It is weaker than the GNN-for-LP paper (5.5, accepted — genuine theoretical insight with average-case analysis). The major weaknesses (underspecified algorithm, misleading claims, missing optimality analysis) pull it below the accept line.

---

## Summary
This paper formalizes submission-limit-based desk-rejection at AI conferences as an integer program (maximizing retained papers subject to per-author caps), proposes an LP-relaxation + deterministic-rounding algorithm (OPTREJECT), and evaluates on 11 years of ICLR submission data. The method consistently reduces desk-rejections compared to the two greedy policies currently used by major venues, with relative improvements reaching up to 19.23% on ICLR 2024 (b=22).

## Strengths
- **Novel formalization of a real policy problem**: The paper is the first to cast submission-limit desk-rejection as a discrete optimization problem (Definition 4.1), and the formulation cleanly captures the actual policies used by CVPR, ICCV, AAAI, KDD, IJCAI, and others (Table 1). This is a genuine contribution with practical relevance.
- **Consistent empirical improvement across all tested settings**: Across all 64 (dataset, b) combinations in Table 3, OPTREJECT never performs worse than either baseline (ALLREJECT, FORWARDREJECT), and shows 10–19% relative improvement on the largest recent datasets (ICLR 2024–2025). The result is uniform and well-evidenced.
- **Practical runtime on real-world instances**: The algorithm completes in ≤53.64 seconds on the largest instance (ICLR 2025: 11,672 papers, 38,495 authors, 61,992 nonzero entries), demonstrating viability for actual conference use.
- **Clean algorithmic exposition with full pseudocode**: All four algorithms include line-by-line time-complexity annotations, making the method straightforward to re-implement.

## Weaknesses

### Fatal
None.

### Major
- **Missing optimality analysis**: For an optimization paper, the central empirical question is whether the method actually optimizes the objective well. The paper never reports the LP upper bound (the optimal value of the relaxation in Definition 4.3), which is trivially available from the LP solve. Without this, the improvement over greedy baselines cannot be distinguished from "better than a weak baseline" vs. "near-optimal." A column or row in Table 3 showing the LP upper bound would immediately reveal the integrality gap and quantify how much headroom remains.
- **Rounding algorithm is underspecified at a critical step**: Algorithm 3, line 14 says "Find the set S_i ⊆ (S ∩ T_i) such that Σ_{j∈S_i} x̃_j ≥ (1 − x_l)" but does not specify *which* such set to select (e.g., by largest x̃_j, smallest, arbitrary?). Different selection rules could produce meaningfully different solutions, and the correctness claim (Theorem 4.6) cannot hold for *any* arbitrary choice unless the proof addresses a specific selection rule or shows all choices are equivalent.
- **Misleading claims in the introduction**: The introduction (Section 1, line 45) states the method uses "randomized rounding" and that the paper "establish[es] the computational hardness of the problem." In reality, Algorithm 3 is purely deterministic (confirmed by Section 5.1, line 374: "experiments are deterministic and contain no randomness"), and the paper provides no NP-hardness proof — only a gesture at the multi-dimensional knapsack connection (Section 4.2). These overstatements misrepresent the paper's actual technical contributions.

### Minor
- **No formal NP-hardness proof**: The paper claims the problem "cannot be solved efficiently in general" and relates it to multi-dimensional knapsack, but provides no reduction or hardness result. This weakens the motivation for using relaxation+rounding.
- **No ordering-sensitivity analysis for FORWARDREJECT**: FORWARDREJECT processes papers in submission-ID order (Algorithm 2), making its performance dependent on arbitrary ID assignment. The paper never explores how much of OPTREJECT's improvement comes from global optimization vs. simply avoiding a bad ordering (e.g., by randomizing IDs and reporting the distribution).
- **Disconnect between motivation and objective**: The ethics statement emphasizes helping early-career researchers, but the optimization objective (maximize total accepted papers) treats all papers and authors identically and does not encode any equity notion.

### Trivial
- Introduction claims evaluation on "11 years of ICLR data" but main-table results (Table 3) cover only 2018–2025 (8 years); earlier years are relegated to appendix. The abstract slightly overstates scope.
- The "randomized rounding" vs. deterministic algorithm inconsistency (line 45 vs. Algorithm 3 and line 374) should be corrected.

## Nice-to-Haves
- Report the LP upper bound alongside rounded solutions for every (year, b) setting to quantify the integrality gap.
- Provide a worst-case bound on how much objective value the rounding algorithm can destroy per iteration.
- Randomize submission-ID ordering for FORWARDREJECT and report the distribution of outcomes.
- Solve the ILP exactly for small ICLR years (2013–2019, where m ≤ 1419) using an off-the-shelf solver to establish the true optimum.
- Discuss strategy-proofness: does the proposed policy remain incentive-compatible if authors know the algorithm?

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"No approximation guarantee is provided — this is unusual / structural"**: The paper presents itself as a practical method, not a theoretical contribution. The absence is noted but does not rise to the level of a standalone weakness separate from the optimality analysis concern. Merged into the major weakness about missing LP bounds.
- **"The constraint reads 'Ax ≤ b − 1_n' rather than 'Ax ≤ b · 1_n'"**: This is a PDF parser artifact (the dot was mangled into a minus sign). The original submission almost certainly has the correct constraint. Removed.
- **"The technical contribution is a straightforward application of standard techniques"**: This is a venue-fit judgment about novelty rather than a verifiable flaw. The paper does apply standard LP+rounding, but applying known techniques to a new problem domain can be a valid contribution. Retained as context only.
- **"The paper never formally states computational complexity / missing NP-hardness proof"**: Already captured under Minor. Removed as duplicate.
- **"Strategy-proofness / incentive problems not addressed"**: This is outside the paper's stated scope (optimizing the desk-rejection policy given fixed submissions, not mechanism design). Removed.
- **"Running time of ≤53.64 seconds is reported without specifying which instance"**: The paper states "all the numbers in Table 3 are computed within at most 53.64 seconds," clearly implying the largest instance (ICLR 2025). This is a nitpick. Removed.
- **"Missing related works"**: Per hard rules, I do not flag missing related works. Removed.

## Novel Insights
The paper's key insight — that submission-limit desk-rejection can be productively viewed as a packing problem rather than a feasibility check — is genuinely novel for the conference-policy domain. The demonstration that a simple LP+rounding approach consistently beats current policies on real data, with the gap growing as conferences scale (ICLR 2024–2025), provides actionable evidence that current policies are leaving substantial author welfare on the table. This is a finding that conference organizers should know about regardless of the paper's acceptance.

## Suggestions
- Add a column or row to Table 3 showing the LP upper bound for each (year, b) setting — this is the single most impactful improvement the paper could make.
- Specify the selection rule in Algorithm 3 line 14 explicitly (e.g., "select papers with largest x̃_j until the cumulative sum exceeds (1 − x_l)").
- Either remove the "randomized rounding" claim from the introduction or adapt the algorithm to actually use randomization and discuss the tradeoff.
- For small instances (ICLR 2013–2019), solve the ILP exactly and report the true optimum alongside the LP bound to establish near-optimality.

## Score and Decision

**Anchor comparison:**
- `ghk8lnOYRq` (k-hyperplane clustering, 5.00, Reject, Round 1/2): Theoretical contributions but no real-world data, potential error in a corollary. Our paper has stronger empirical evaluation but weaker theoretical depth. Comparable overall.
- `2oWRumm67L` (Light-MILPopt, 5.00, Accept, Round 1/2): ML-based MILP framework with more technical novelty in the ML component. Our paper has a cleaner, more impactful application but less algorithmic novelty. Comparable.
- `INow59Vurm` (GNN for LP, 5.50, Accept, Round 2): Genuine theoretical insight connecting GNNs to distributed LP algorithms, but no experiments. Our paper has comprehensive experiments but a more standard technique. Our paper is weaker.
- `scdGzuwC9u` (Reoptimization for MILP, 6.00, Reject, Round 1): Stronger technical contribution with a two-stage framework for dynamic MILPs. Our paper is weaker.
- `vYBzgwkwZb` (BiQAP, 5.67, Reject, Round 2): Neural bi-level optimization, more technically novel. Our paper is weaker.

**Round 1 bracket:** 4.5–6.5

**Round 2 narrowing:** The paper is most comparable to the 5.0 anchors (k-hyperplane clustering and Light-MILPopt). It has a cleaner application and stronger empirical evaluation than k-hyperplane clustering but significantly less theoretical depth. It has a clearer real-world impact than Light-MILPopt but less algorithmic novelty. The GNN-for-LP paper at 5.5 was accepted with genuine theoretical insights despite lacking experiments — our paper's LP+rounding approach is more standard by comparison. The BiQAP and Neural Solver Selection papers at 5.67–5.75 were rejected with stronger technical contributions. Given the major weaknesses (underspecified algorithm, misleading claims, missing optimality analysis), our paper lands at 5.0, Reject.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>