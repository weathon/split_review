Now I have all the information needed. Let me construct the final review.

## Summary

This paper formalizes the desk-rejection problem caused by per-author submission limits at AI conferences as an integer program (maximizing the number of papers that proceed to review while respecting per-author caps), then proposes solving it via LP relaxation followed by a dedicated rounding algorithm. The method is evaluated on 11 years of ICLR submission data against two baseline policies (ALLREJECT and FORWARDREJECT), showing consistent improvements of up to 19.23% in reducing unnecessary desk-rejections.

## Strengths

- **Novel problem formalization and practical framing.** The paper is, to my knowledge, the first to cast the conference desk-rejection process as an explicit optimization problem (the maximum desk-acceptance submission limit problem, Definitions 4.1 and 4.3). This formalization is a clear conceptual advance over the ad-hoc rules (Algorithms 1 and 2) currently used by conferences, and it opens the door to principled improvements.

- **Consistent and substantial empirical improvement on real data.** Table 3 shows that the proposed method reduces desk-rejections across nearly every combination of year (ICLR 2018–2025) and submission limit (b = 4 to 25). The headline result of 19.23% relative improvement (ICLR 2024, b=22) over the stronger baseline (FORWARDREJECT) is well-supported. The trend showing larger improvements for larger conferences (ICLR 2024, 2025) is also compelling.

- **Practical efficiency.** All results were computed within at most 53.64 seconds using a standard LP solver (PuLP) on modest hardware (2 vCPUs), demonstrating that the approach scales to real conference sizes (~10⁴ papers, ~3×10⁴ authors).

- **Theoretical guarantee for the rounding step.** Theorem 4.6 (proved in Appendix B) guarantees that Algorithm 3 always produces a feasible binary solution satisfying all author limits. This distinguishes the method from blind heuristics.

- **Evaluation on longitudinal data spanning 11 years of ICLR.** Using real submission records (2013–2025) with varying scales (67 to 11,672 papers) gives the empirical findings broader credibility than a single-year snapshot would.

## Weaknesses

### Major

- **Missing comparison to the exact IP optimum for small instances.** The paper compares only against two heuristic baselines. For the smallest years (ICLR 2013 with 67 papers and 161 authors, ICLR 2014 with 69 papers and 187 authors), solving the integer program (Definition 4.1) to optimality with a standard MILP solver would be trivial. Such a comparison would reveal how close the LP-relaxation+rounding solution is to the true optimum, and would substantially strengthen the claim that the method is near-optimal rather than merely "better than two baselines." Without it, the reader only knows the method outperforms ALLREJECT and FORWARDREJECT — useful but incomplete evidence.

- **Limited baselines and lack of comparison with even simple alternatives.** The paper compares only against ALLREJECT (Algorithm 1) and FORWARDREJECT (Algorithm 2). A simple greedy baseline — e.g., selecting papers to retain by fewest co-authors, or by lowest author-overload — would help test whether the improvement comes from optimization per se or merely from being a better heuristic than FORWARDREJECT. Since FORWARDREJECT is already the best existing policy, this is the most important missing comparator. (Note: this is a different concern from the IP-optimum comparison above — one tests optimality, the other tests whether a simpler greedy could match the LP+rounding approach.)

### Minor

- **Potential typo in the LP relaxation constraint (Definition 4.3) that creates a textual inconsistency.** The IP (Definition 4.1) uses constraint `Ax ≤ b·1_n`, while the LP relaxation (Definition 4.3) states `Ax ≤ b − 1_n` (an n-vector where every entry is b−1). This is stricter than the IP's constraint and is almost certainly a typesetting error (`−` in place of `·`). The rounding algorithm (Algorithm 3, line 13) checks against the correct limit `b`, not `b−1`, which creates a textual inconsistency. If the implementation used the correct constraint `b·1_n` (as the empirical results strongly suggest), this is a presentation error that does not affect the validity of the results, but it must be corrected. The authors should clarify whether the text or the implementation is incorrect and fix the definition accordingly.

- **The rounding algorithm's construction of set S_i (Algorithm 3, line 14) is not clearly justified in the main text.** The algorithm states "Find the set S_i ⊆ (S ∩ T_i) such that ∑_{j∈S_i} \tilde{x}_j ≥ (1 − x_l)" and claims O(k₁) time, but does not explain how such a set can always be found or why it can be constructed in linear time. The paper defers the proof to Appendix B (which is stripped from the submission), but the main text should at least sketch the reasoning (e.g., a brief note that the LP constraint guarantees existence and a simple greedy selection suffices). This does not threaten correctness — the appendix presumably provides the proof — but it makes the main paper harder to evaluate independently.

- **No discussion of the integrality gap of the LP relaxation.** Since the method solves an LP and then rounds, the quality of the final solution depends on how tight the LP relaxation is. The paper provides no analysis (theoretical or empirical) of the integrality gap. An empirical gap analysis — comparing the LP objective to the IP optimum for small instances — would be a natural complement.

- **Limited fairness discussion of the optimization's distributional consequences.** The method maximizes total retained papers, but this could concentrate rejections onto a small set of authors. Current policies (reject by submission ID) are crude but mechanically uniform; the optimization approach could produce outcomes where one author loses several papers while another keeps all of theirs, as long as the total is maximized. The ethics statement acknowledges early-career researchers but does not engage with this trade-off. This does not invalidate the contribution, but it is a real limitation worth addressing.

### Trivial

- "enabling desk-rejection maximized desk rejection" appears to be a minor grammatical error (page 6). This does not affect understanding.

## Nice-to-Haves

- Comparison to the exact IP optimum for ICLR 2013–2014 to quantify the optimality gap closed by the LP+rounding heuristic.
- A simple greedy baseline (e.g., retain papers with fewest authors first) to test whether the improvement is due to optimization or just better heuristics.
- Empirical analysis of the integrality gap for small instances.
- Statistical variance or sensitivity analysis (the experiments are reported as deterministic single runs; some discussion of robustness would be helpful).
- A more thorough discussion of the fairness-efficiency trade-off, perhaps analyzing the distribution of rejections across authors under the proposed method vs. baselines.

## Novel Insights

None beyond the paper's own contributions. The core observation — that desk-rejection under author limits can be cast as an IP and solved practically via LP+rounding — is the paper's own contribution. The harsh critic's suggestion that the rounding construction might be impossible in O(k₁) time is not borne out by the available information (the appendix contains the proof). The fairness-efficiency tension is a valid observation but not a novel insight specific to this paper.

## Suggestions

- Correct the LP relaxation constraint in Definition 4.3 from `Ax ≤ b − 1_n` to `Ax ≤ b·1_n` (matching the IP's constraint), and explicitly confirm that the implementation uses the correct constraint.
- Add a brief explanation of why the set S_i in Algorithm 3, line 14 always exists and can be found greedily in O(k₁) time, even if the full proof remains in the appendix.
- Add an experiment comparing against the exact IP optimum for ICLR 2013 and/or 2014, where the problem is small enough to solve optimally.

## Score and Decision

Let me run the calibration search results through my analysis.

**Bracketing (Round 1):** The paper sits above the weak-anchor band (avg ~3.0, which contains general MILP/optimization papers with clear flaws) and well below the strong-anchor band (avg ~8.0, which contains papers with major theoretical contributions and very strong experimental backing). The middle band (3.5–7.5) contains the paper.

**Narrowing (Round 2):** 
- The 5.0 anchor (k-hyperplane clustering) is weaker than the current paper — it had unclear experiments and no real-data evaluation.
- The 5.67 anchor (peer review benchmark) had evaluation methodology concerns; the current paper is cleaner methodologically.
- The 6.0 anchor (MILP reoptimization) is comparable in quality — both have practical contributions with some gaps in baselines/comparisons.
- The 6.67 anchor (Neur2RO) is somewhat stronger — it has more technical depth and is accepted.
- The 7.5 anchor (approximation with predictions) is clearly stronger (accepted with 8,8,6,8).

Comparing the paper to these anchors, it is clearly above score 5 papers (well-defined problem, real data, clean results) but not at the level of score 7+ papers (some missing analyses, a textual error, limited baselines). Within the 5.5–6.5 band, the paper sits comfortably: it has a clear practical contribution with solid evidence, but the missing optimality comparison, limited baseline set, and the LP constraint typo prevent it from reaching the stronger end of the range. I place it at **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>