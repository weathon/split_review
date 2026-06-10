## Summary

This paper introduces Branches, a dynamic programming and branch-&-bound algorithm for constructing optimal decision trees. Its core innovation is the "Purification Bound" — an upper bound on the state-action value of a split that admits a closed-form complexity analysis, unlike the bounds used by prior methods (OSDT, GOSDT). The algorithm is framed within an RL/MDP formalism for convenience, supports multi-categorical features directly (whereas all compared baselines require binary encoding), and is evaluated on 11 UCI datasets.

---

## Strengths

- **The Purification Bound enables a tractable closed-form complexity analysis.** Proposition 4 defines a bound (`-λ + n(l)/n`) on the optimal value of a split action that is both simple and structured to permit analytic counting of branch evaluations (Theorem 5, Corollary 6). The paper explicitly notes that OSDT's bound structure does not allow such analysis (line 309), making this a concrete differentiator. The numerical gap shown in Table 1 (e.g., 5.70×10⁴ vs. 5.61×10¹³ for q=10, λ=0.1) illustrates the bound-level difference, even though the paper candidly acknowledges OSDT's bound is unrealistically loose.

- **Direct native support for multi-categorical features is a genuine practical advantage.** All compared baselines (OSDT, GOSDT, DL8.5, MurTree, STreeD) require binary encoding, but Branches handles ordinal encoding directly. The results on ordinal-encoded datasets are the cleanest success in the paper: Branches solves problems in seconds that are infeasible for baselines (e.g., monk1-o: 0.02s, nursery-o: 0.26s, mushroom-o: 0.17s with objective 0.975 vs. 0.945 for the best binary-encoding baseline). This advantage is implementation-independent and non-trivial.

- **Branches consistently terminates in fewer iterations than GOSDT on every comparable benchmark.** Table 1 shows Branches using 10-50× fewer iterations in many cases (e.g., monk1-l: 617 vs. 30,000; monk2-l: 30,000 vs. 100,000; balance: 300,000 vs. 1,000,000). While the cross-algorithm comparability of "iterations" is not fully argued (see Weaknesses), the pattern is consistent across all 11 datasets and directly supports the claim that the Purification Bound improves pruning efficiency.

---

## Weaknesses

### Fatal
None.

### Major

- **The runtime comparison against GOSDT is confounded by implementation language, and the paper's treatment of this confound is asymmetric.** The paper is in Python; GOSDT is in C++. When GOSDT is faster (tic-tac-toe, car-eval, balance), the paper says: "we suspect that this is mainly due to GOSDT's optimised C++ implementation" (lines 395–396). But when Branches is faster (the majority of cases), the same language gap is not used to discount those wins. The invocation of PyGOSDT (a Python *wrapper* around C++, not a native reimplementation) as a bridge does not resolve the confound — it shows wrapper overhead, not algorithm-level comparison. The net result is that the runtime evidence supports only "Branches in Python is faster than GOSDT in C++ on some datasets and slower on others," which is weaker than the claim of algorithmic speed superiority. *(Verified at lines 395–396.)*

- **The λ penalty parameter is not reported for any experiment.** λ is central to the objective function (Eq. 6), the complexity bound (Corollary 6, which scales as 1/(Kλ)), and the entire accuracy-sparsity trade-off. Without knowing its value, the experiments are not reproducible, and the complexity-bound numbers in Table 1 cannot be verified or contextualized. Neither the experimental setup (Section 5) nor any table caption states the λ used. *(Verified by searching all occurrences of λ in the paper — none specify a numeric value for the experiments.)*

### Minor

- **The iteration count comparison between Branches and GOSDT is presented without defining commensurability.** The paper defines a Branches "iteration" as one Value Iteration cycle (Selection + Expansion + Backpropagation) in Section 3. But it never defines what constitutes an iteration in GOSDT or argues that the two definitions are comparable. The claim "Branches always converges in fewer iterations than GOSDT" (line 395) is used as central evidence for pruning efficiency, but the reader cannot assess whether the algorithms are counting the same kind of work. Even if the pattern is too consistent to be coincidental, the evidence would be stronger with a clear definition or an algorithm-independent measure (e.g., number of subproblems evaluated).

- **The complexity-bound comparison in Table 1 places undue emphasis on a bound the paper itself calls unrealistic.** The paper prominently contrasts Branches' bound (e.g., 5.70×10⁴) against OSDT's (e.g., 5.61×10¹³) but immediately concedes that OSDT's bound "do[es] not reflect OSDT's true complexity" and "is too loose" (line 309). The numbers are valid as a comparison of *bound tightness*, but the table is presented in a way that visually suggests Branches is computationally superior by many orders of magnitude — an inference the paper's own caveat undermines. This framing overstates what the complexity analysis actually demonstrates.

- **Limited experimental scope.** All 11 datasets are small and categorical only (the paper acknowledges the categorical limitation, line 410). No larger or harder instances are included that would stress-test scalability beyond the 5-minute timeout. The comparison also lacks an ablation isolating the Purification Bound's contribution (e.g., running Branches with a naive "best-so-far" bound to quantify the bound's pruning effect separately from the DP strategy).

### Trivial
None.

---

## Nice-to-Haves

- An ablation study running Branches without the Purification Bound (replacing it with a simple best-solution-found bound) would directly quantify the bound's contribution to pruning.
- A brief statement clarifying how the objective-function difference (splits vs. leaves, noted on line 112) was handled — e.g., whether baselines were configured to optimize the same objective or evaluated post-hoc on Branches' metric.

---

## Removed Points

- **Objective alignment criticism** — REMOVED. The paper's table captions state "objective here refers to the regularised objective objectiver" and the paper explicitly notes that OSDT/GOSDT penalize leaves instead of splits (line 112). Computing all methods' solutions on the same metric is standard evaluation practice, not an apples-to-oranges comparison.
- **Purification Bound is "elementary" / not novel** — REMOVED. Simplicity is a virtue in bounds; the paper's contribution is that this simple bound enables closed-form complexity analysis, which prior bounds do not.
- **Missing variance / statistical significance** — REMOVED. Deterministic algorithms on fixed benchmarks make this non-standard in the optimal-DT literature.
- **No numerical feature experiments** — REMOVED. The paper explicitly scopes itself to categorical features (line 410). Demanding numerical-feature experiments would be scope creep.
- **"Iterations" criticism suggesting the evidence is uninterpretable** — DOWNGRADED to Minor. The consistent pattern across 11 datasets is unlikely to be coincidental, but the lack of a clear cross-algorithm definition weakens the evidence.
- **Complexity bound criticism suggesting Table 1 should be removed** — DOWNGRADED to Minor. The bound comparison is valid as a *bound tightness* comparison, and the paper is transparent about the caveat. The issue is presentation, not error.

---

## Novel Insights

The most interesting observation that emerges from cross-referencing the reviews is that the paper's strongest evidence (ordinal-encoding results) and weakest evidence (runtime comparison against GOSDT) stem from the same root: the implementation-language confound. The ordinal-encoding advantage is immune to this confound because the baselines simply cannot operate on ordinal-encoded data — the speedups of 100× or more on ordinal datasets (e.g., nursery-o: 0.26s vs. nursery-l: GOSDT times out) are clearly algorithmic. On binary-encoded data where both methods can run, the runtime numbers are ambiguous, but the iteration counts consistently favor Branches. This suggests the paper would be well-served by foregrounding the ordinal results and iteration comparisons as its primary evidence, and sharply qualifying the raw runtime comparisons.

---

## Suggestions

1. **Report λ explicitly** in the experimental setup. Without it, the experiments are not reproducible.
2. **Restructure the empirical evidence** to prioritize (a) ordinal-encoding results (clean, confound-free), (b) iteration counts (consistent, algorithm-level), and (c) runtime only with explicit caveats about the Python/C++ gap.
3. **Define what constitutes an iteration for each compared method** or switch to an algorithm-independent metric (e.g., number of subproblems evaluated) to make the iteration comparison interpretable.
4. **Include an ablation** running Branches with the Purification Bound disabled to quantify the bound's contribution to search reduction.
5. **Reframe Table 1** as a comparison of bound tightness rather than implied computational superiority, given the paper's own acknowledgment that OSDT's bound is unrealistically loose.

---

## Score and Decision

**MY FINAL SCORE:** <score>5.0</score>
**MY FINAL DECISION:** <decision>Reject</decision>