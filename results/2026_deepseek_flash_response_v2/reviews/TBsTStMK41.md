I now have a solid calibration. Let me produce the final review.

## Summary

This paper formalizes the per-author submission-limit desk-rejection problem used by AI conferences as an integer program (maximizing papers retained under author caps), proposes a two-stage LP relaxation + deterministic rounding solution, and evaluates it on 11 years of real ICLR data. The method consistently reduces desk-rejections compared to current policies, with relative improvements up to 19.23%, running in under 54 seconds on commodity hardware.

## Strengths

1. **Consistent empirical improvement on 11 years of real data**: Table 3 shows the proposed method outperforms both the naive ALLREJECT and the stronger FORWARDREJECT baseline across nearly all submission-limit settings on real ICLR submissions 2018–2025. The improvements are systematic, not cherry-picked — they appear across multiple values of *b* (4–25) and across years, and are naturally zero only when the limit is so generous that no desk-rejections are needed.

2. **Principled formalization of a practical problem**: The paper formally defines the maximum desk-acceptance submission limit problem (Definition 4.1) as an integer program, providing a clean mathematical foundation for a problem that conferences currently handle with ad-hoc heuristics (e.g., "reject papers with the largest submission IDs"). This formalization is a genuine conceptual contribution that opens the problem to further optimization research.

3. **Provable feasibility guarantee with practical efficiency**: Theorem 4.6 proves the rounding algorithm always produces a feasible solution respecting all author constraints, and the entire pipeline runs within 53.64 seconds on 2-vCPU hardware (Section 5.2). The combination of formal correctness and practical speed is directly relevant to deployment by conference organizers.

4. **Non-trivial baselines**: The paper compares against FORWARDREJECT (Algorithm 2), a carefully designed sequential greedy that is strictly stronger than the naive ALLREJECT policy actually used by conferences. The reported improvements are against this stronger comparator, not a strawman.

## Weaknesses

### Fatal
None.

### Major

1. **The LP relaxation uses a *tighter* constraint than the IP without explanation.** The IP (Definition 4.1) constrains each author to at most *b* papers: `Ax ≤ b·1_n`. The LP relaxation (Definition 4.3) uses `Ax ≤ b − 1_n` — effectively a per-author limit of *b−1*. This is the opposite of what a relaxation should do (typically one relaxes constraints, not tightens them), and the paper provides no justification for this change. If the intention is to create slack for rounding, it must be stated explicitly, and its effect on the objective value must be characterized. Without explanation, the reader cannot assess whether the LP even provides a valid upper bound on the IP optimum, or whether the method's performance is artificially limited by this tighter bound.

2. **The baselines depend on an arbitrary ordering whose impact is not explored.** FORWARDREJECT processes papers in submission-ID order. Any ordering yields a feasible solution, and different orderings can produce different acceptance counts. The paper does not test alternative orderings (e.g., random permutations, author-count ordering) to characterize the range of outcomes the greedy approach can achieve. A baseline that tries many orderings and reports the distribution would establish whether the LP+rounding improvement is due to genuine optimization or simply to picking a better ordering than the specific one used. This is important because the current comparison conflates the quality of the method with the luck of the draw in the chosen ordering.

3. **No comparison against the IP optimum or optimality gap.** The paper claims the IP "cannot be solved efficiently in general" (Section 4.2) but does not attempt to solve the *specific* ICLR instances with a MILP solver under a reasonable time budget. The LP relaxation objective provides an upper bound on the IP optimum; reporting this bound alongside the LP+rounding solution would give a data-dependent optimality gap. Without this, the reader cannot tell whether the method closes 10% or 90% of the gap to the true optimum. If the gap is large, the headline improvement over arbitrary baselines is much less meaningful.

### Minor

4. **"Randomized rounding" in the introduction mismatches the actual deterministic algorithm.** Line 45 describes "randomized rounding," but Algorithm 3 (MAXROUNDING) is entirely deterministic — it picks the largest fractional value, sets it to 1, and greedily zeros out conflicting variables. The paper should either use randomized rounding or correct the description. This mismatch could mislead readers about the method's properties.

5. **Algorithm 4 mentions "Randomly initialize x₀" but experiments are claimed deterministic** (Section 5.1, line 374). LP solvers typically ignore the initial point, so the statement is harmless but internally inconsistent and should be reconciled.

6. **Absolute improvements are modest in many settings.** The 19.23% relative improvement corresponds to saving 5 additional papers out of 7,404 (ICLR 2024, b=22). For the largest year (ICLR 2025, b=4), the absolute improvement is 316 out of 11,672 (2.7% absolute). While 316 papers is practically meaningful, the relative framing inflates gains when the baseline already performs reasonably. Reporting absolute percentages alongside relative ones would give a more balanced picture.

### Trivial
7. The paper overstates technical novelty — the LP-relax-and-round approach is a textbook technique applied to a new domain. The applied contribution is real and valuable; the framing should be calibrated accordingly.

## Nice-to-Haves

- Analyze the distributional impact: does the optimization method favor papers with fewer co-authors (since they consume fewer author slots)? This is relevant to the fairness discussion in the ethics statement.
- Test FORWARDREJECT on, say, 100 random paper orderings to establish the range of greedy outcomes and clarify how much of the improvement comes from optimization vs. ordering luck.
- Extend evaluation to data from other conferences (e.g., via the OpenReview API for conferences with public records) to test generalizability beyond ICLR.

## Removed Points

The following points from the inputs were removed or downgraded:

1. **"Randomized rounding" vs deterministic (Harsh Critic #1)**: Retained as Minor Weakness #4 — a real inconsistency but not core to the paper's claims.
2. **"The rounding algorithm has no approximation guarantees" (Harsh Critic #1)**: Removed. The paper only claims feasibility (Theorem 4.6), not optimality. The critic is criticizing an unclaimed property.
3. **"Line 14 of Algorithm 3 requires solving a subset-sum-like problem" (Harsh Critic)**: Removed as speculative — the paper claims O(k₁) time and Appendix B contains the proof. Without access to the appendix, this criticism cannot be verified from the paper as written.
4. **"Direct transformative social impact is hyperbolic" (Harsh Critic)**: Removed as a style nitpick.
5. **"The paper claims computational hardness but doesn't substantiate it" (Harsh Critic)**: Removed — the paper cites the multidimensional knapsack problem (Kellerer et al., 2004), which is a standard reference for NP-hardness.
6. **"Missing related works" / reproducibility concerns about unreleased data**: Removed per hard rules — the paper cites its sources, and reproducibility statements about code release upon acceptance are appropriate.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine methodological concern (the LP constraint tightening) that the paper itself does not flag and that a reader focused on the empirical results might miss.

## Suggestions

1. **Resolve the LP constraint discrepancy.** Clearly explain why the LP uses `b − 1_n` instead of `b·1_n`. If it is intentional (e.g., to guarantee post-rounding feasibility), justify it formally and quantify the cost in objective value.
2. **Run FORWARDREJECT on multiple random paper orderings** and report the distribution (min, max, mean, std) of accepted papers. This would directly establish how much of the apparent improvement is due to the optimization vs. ordering luck.
3. **Report the LP objective value alongside the LP+rounding solution** to provide an upper bound on the IP optimum and compute a data-dependent optimality gap. This would substantially strengthen the empirical claims.

## Calibration

**Round 1 bracket:** [4.0, 6.0]

**Anchor papers retrieved:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/psDvcWtFdE.md (DIG-MILP) | 3.00 | R1, weak | Weaker — minor novelty, no significant improvement over random. Our paper is clearly stronger. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/C9pndmSjg6.md (Portfolio Opt) | 3.00 | R1, weak | Weaker — standard relaxation techniques without strong empirical validation. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/KD9F5Ap878.md (OptiBench) | 5.00 | R1, middle / R2 lower | Comparable — both have clear applied contributions with some gaps. Our paper is cleaner. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/uV3Gdoq2ez.md (Peer Review LLM) | 5.67 | R1, middle | Similar quality — both address timely peer-review problems with real data and have methodological concerns. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/INow59Vurm.md (GNN for LP) | 5.50 | R2 upper | Our paper is stronger — it has real experiments and a clear applied contribution vs. this paper's purely theoretical analysis with no experiments. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/scdGzuwC9u.md (MILP Reopt) | 6.00 | R2 upper | Our paper is weaker — that paper has a more sophisticated ML+MILP framework and stronger experiments. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/o0oroLuPLZ.md (Sp-R-IP) | 4.60 | R2 lower | Our paper is stronger — more extensive real-data evaluation and cleaner problem formulation. |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/wsb9GNh1Oi.md (Multiple Init Solutions) | 5.75 | R1, middle | Our paper is comparable — similar empirical thoroughness, but that paper has stronger technical novelty. |

**Final score determination:** The paper is clearly above the 3.0-level papers (which lack significant experimental validation) and below the 6.0-level paper (which has stronger technical novelty). It is most comparable to papers in the 4.6–5.67 range. Among these, the paper distinguishes itself with 11 years of real data and a clean problem formulation, but is held back by the unexplained LP constraint discrepancy and weak baseline analysis. The score of **5.0** reflects a paper with a real applied contribution and solid evaluation that falls short of top-venue standards in methodological rigor.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>