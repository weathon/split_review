Now I have a thorough understanding of the paper. Let me write the final consolidated review.

---

## Summary

This paper formalizes the problem of submission-limit–based desk rejection at AI conferences as a maximum desk-acceptance integer program (Definition 4.1) and proposes a two-stage algorithm: solve an LP relaxation (Definition 4.3), then round fractional solutions via a greedy procedure (Algorithm 3, MAXROUNDING). Evaluated on 11 years of real ICLR submission data, the method consistently accepts more papers than the two baseline policies (ALLREJECT and FORWARDREJECT) at all tested submission limits $b \in \{4,\ldots,25\}$, with relative improvements ranging from ~4% to 19.23%. The algorithm runs in at most 53.64 seconds on full-scale ICLR data, making it immediately deployable.

---

## Strengths

- **Clean, well-motivated problem formulation.** Definition 4.1 turns a vague conference policy into a crisp integer program with an explicit objective (maximize desk-accepted papers) grounded in utilitarian social welfare. This is a clear improvement over the feasibility-only Definition 3.1, which merely enforces the constraint without minimizing rejections.

- **Provable feasibility guarantee.** Theorem 4.6 establishes that MAXROUNDING always returns a valid $\{0,1\}$ vector satisfying the per-author limit, removing any risk of the optimizer accidentally violating conference rules. This is a necessary property for a policy tool.

- **Consistent and practically significant empirical improvements.** Table 3 shows that the method outperforms FORWARDREJECT in every case where desk rejections are nonzero. For ICLR 2024 and 2025 (the two largest datasets), improvements are 7–19% across all $b$ values, corresponding to absolute savings of dozens to hundreds of papers per setting (e.g., 2984 → 2668 at b=4 for ICLR 2025, saving 316 authors from desk rejection).

- **Practical scalability.** Despite solving an LP over up to 11,672 papers, the full pipeline runs in ≤53.64 seconds on a 2-vCPU server—well within any practical conference workflow.

- **Rigorous baseline formalization.** Algorithms 1 and 2 are given formal correctness proofs (Propositions 3.5 and 3.6), so the comparison is against well-specified policies rather than informally described heuristics.

---

## Weaknesses

### Fatal
None.

### Major

- **The LP in Definition 4.3 is not a standard relaxation of the IP in Definition 4.1 — the constraint change is unexplained.**
  Definition 4.1 uses constraint $Ax \leq b \cdot \mathbf{1}_n$; Definition 4.3 uses $Ax \leq b - \mathbf{1}_n$ (i.e., each author is allowed at most $b-1$ papers, not $b$). These are strictly different: the LP solves a *tighter* problem than the IP, not a relaxed one. This has two consequences. First, the label "LP relaxation" is wrong; this is an LP with a stricter constraint used as a guide for rounding, not a relaxation in the standard sense. Second, the LP objective value is a *lower* bound on the IP optimal rather than the usual upper bound, so the LP cannot serve as a certificate of near-optimality. Theorem 4.6 establishes only feasibility, not approximation quality, so the missing upper bound matters. The paper offers no explanation for why the RHS was tightened to $b-1$. One plausible design rationale: if the LP satisfies $Ax \leq (b-1)\mathbf{1}_n$, then rounding any single fractional $x_l$ up to 1 increases each author's count by at most $1-x_l < 1$, guaranteeing the author's running total is strictly less than $b$ on that step—which gives exactly one unit of slack per rounding step. But this argument is neither stated nor verified in the paper, and even if true it does not extend cleanly to multiple sequential roundings within Algorithm 3's loop. This is the most important issue to resolve in revision: either confirm the $b-\mathbf{1}_n$ constraint is intentional, explain why it preserves correctness throughout the iterative rounding (not just the first step), and rename the LP accordingly; or fix it to $b\cdot\mathbf{1}_n$, restore the standard relaxation framing, and verify correctness of MAXROUNDING under that formulation.

- **No optimality gap analysis; the "maximize" framing overstates what is demonstrated.**
  Definition 4.1 and the abstract/title frame the method as *maximizing* desk acceptance, but MAXROUNDING (Algorithm 3) is a greedy heuristic (round the largest fractional variable first, eliminate the minimum necessary to restore feasibility). This is not guaranteed to be optimal, and no approximation ratio is provided. The gap between the LP objective and the rounded integer solution is never reported—neither in Table 3 nor elsewhere. Without LP upper bounds alongside rounded results, readers cannot know whether the algorithm achieves near-optimality or merely beats simple baselines. Reporting the LP objective value as a column in Table 3 would be a minor computational addition and would immediately resolve this concern.

### Minor

- **The "19.23%" headline figure is cherry-picked without sufficient framing.** Table 3 shows that 19.23% (ICLR 2024, $b=22$) is the single maximum across all year × $b$ combinations. The absolute improvement at that cell is 5 papers (26 → 21) out of 7,404 submissions. The paper uses "up to" language, which is technically accurate, but the title and abstract lead with this number in a way that suggests it characterizes typical performance. A more representative summary—e.g., the median relative improvement across all year × $b$ cells where rejections are nonzero—would better convey the method's average benefit. (For ICLR 2025 alone, the improvements range from 8.51% to 13.05%, which are already compelling and more representative.)

- **The counterfactual simulation assumption is underacknowledged.** ICLR does not actually enforce submission limits, so all experiments simulate "what would happen if the limit were $b$." Authors who know a limit exists would behave differently (e.g., choosing which papers to submit strategically). The paper notes data incompleteness briefly ("some papers may be missed by the OpenReview API") but does not discuss behavioral counterfactuals. This does not undermine the results, but it should be noted more explicitly as a limitation.

### Trivial

- The claim that the "forward" and "reverse" versions of the sequential policy (Algorithms 2 and 5) are "equivalent" holds only in aggregate count of rejections. The *identity* of which papers are rejected differs, which matters for the paper's ethical framing about early-career researchers. The paper should clarify that equivalence is in number only.

---

## Nice-to-Haves

- Report LP objective values alongside rounded results in Table 3 to show the optimality gap.
- After MAXROUNDING, a cheap "greedy repair" pass (iterate over desk-rejected fractional papers and add back any that fit) could recover additional accepted papers at negligible cost.
- Highlight absolute improvements at $b$ values used by real conferences ($b=25$ for CVPR, $b=10$ for AAAI) to make the practical impact more concrete.
- The mismatch between the utilitarian-maximization objective and the stated goal of protecting early-career researchers deserves at least a sentence in the main text acknowledging that not all papers contribute equally to author welfare.
- Sketch the connection to reviewer assignment systems (mentioned in the conclusion) more concretely, since that is the operational context in which this algorithm would run.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"NP-hardness proof is insufficiently formal"** (Harsh Critic): The paper says the problem "cannot be solved efficiently in general" and appeals to multi-dimensional knapsack. For a practical systems/policy paper, citing the standard reduction via MDK is adequate. Demanding a formal reduction from 3-dimensional matching is scope creep for this venue.

- **"FORWARDREJECT and REVERSEREJECT equivalence undermines the ethical framing"** (Harsh Critic): Elevated to Trivial rather than removed entirely; it is a real but small presentation issue.

- **"Data quality gap for ICLR 2025 could affect results"** (Harsh Critic): The paper explicitly acknowledges this ("some papers may be missed … this gap is small relative to public ICLR statistics"). The concern is addressed, even if briefly, and is speculative about magnitude.

- **"Simulation validity—authors would behave differently under known limits"** (Harsh Critic): Moved to Minor. The behavioral-counterfactual argument is worth a sentence but does not invalidate the empirical evaluation.

- **Generic strength: "addresses an important problem"** (Strength Finder): Removed as a standalone strength per filtering rules; incorporated into the specific evidence-backed strengths above.

- **Reproducibility concerns about code/data not yet released** (implicit in Strength Finder): The reproducibility statement says code and data will be released upon acceptance; the pseudo-code and data acquisition procedure are fully specified. This is standard and not a weakness.

---

## Novel Insights

The paper's most insightful contribution is the observation that FORWARDREJECT—which is widely used in practice and significantly better than ALLREJECT—still leaves a meaningful optimality gap (10–19% in recent large-scale ICLR years) that can be recovered by a principled LP-based approach. The framing of desk rejection as an integer program with utilitarian welfare objective is elegant and positions it as a policy-design problem rather than a scheduling heuristic. The empirical finding that relative improvement grows with conference scale (near-zero for ICLR 2018, up to 19% for ICLR 2024) is particularly compelling as AI conference sizes are trajectory to continue growing.

---

## Suggestions

1. **Resolve the LP constraint discrepancy** (highest priority): Decide whether the LP uses $b\cdot\mathbf{1}_n$ or $(b-1)\cdot\mathbf{1}_n$, state the reason clearly in the main text, and verify that the correctness proof of MAXROUNDING is consistent with that choice.
2. **Add LP objective values to Table 3**: Report the fractional LP objective alongside the rounded integer result to provide an empirical optimality gap bound.
3. **Reword the abstract/title**: Replace "up to 19%" with a more representative figure (e.g., "consistently 7–19%") or add a parenthetical noting the typical range.
4. **Clarify the simulation assumption**: Add a sentence noting that submission behavior may differ if limits are enforced in advance, and that these results should be interpreted as showing the allocation efficiency gain, conditional on the observed submission patterns.

---

## Score and Decision

**Originality**: The application of LP relaxation + rounding to conference desk-rejection policy is novel. The technical approach is standard, but the problem formulation and deployment context are fresh. *(3/5)*

**Importance of research question**: High and timely. As submission volumes at AI conferences surge, principled desk-rejection policy matters for thousands of researchers. *(5/5)*

**Claims well supported**: Partially. The empirical claims are well supported by Table 3. The "maximization" claim is not fully supported because no optimality gap is reported and the LP constraint issue casts doubt on whether a true upper bound is available. *(3/5)*

**Soundness of experiments**: The experimental setup is clean, the baselines are appropriate and well-formalized, and the evaluation covers 11 years of real data. Simulation over a venue that doesn't enforce limits is a limitation but not a fatal one. *(3/5)*

**Clarity of writing**: Generally clear and well-structured. The LP constraint discrepancy represents a genuine confusion in the technical presentation. *(3/5)*

**Value to research community**: Practically deployable, reproducible, and addresses a concrete policy problem with broad reach across the AI conference ecosystem. *(4/5)*

The paper has a genuine and timely contribution, and the empirical evidence of consistent improvement is compelling. However, the unexplained LP constraint discrepancy ($b - \mathbf{1}_n$ vs. $b \cdot \mathbf{1}_n$) is a real technical gap that calls into question whether the "LP relaxation" terminology is accurate and whether the rounding procedure is correct as stated. Coupled with the absence of any optimality gap analysis, these issues require revision before the paper can be accepted. The issues are fixable, but they are not cosmetic.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>5</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>