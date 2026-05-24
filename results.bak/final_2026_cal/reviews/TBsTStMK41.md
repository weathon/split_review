Now I have all the information needed. Let me synthesize the final review.

**Round 1 bracket**: The paper sits between 3.5 and 7.5. Comparing to anchors: below the 5.50-5.33 Accept-level papers (which have stronger technical contributions or more comprehensive benchmarking), above the 4.00 Reject-level papers (which have more fundamental methodology issues).

**Round 2 narrowing**: Compared to anchors at 5.33 (FrontierCO) and 5.50 (RRNCO, OR-PRM), this paper is slightly weaker due to the exposition error in Definition 4.3 and the modest technical contribution (standard LP + greedy rounding without guarantees). However, it has cleaner focus and consistent real-data evaluation. Final score anchored at 5.0.

---

## Summary

This paper formalizes the desk-rejection problem under per-author submission limits as an integer program (maximizing the number of papers that proceed to review). It proposes a two-stage solver: LP relaxation followed by a greedy rounding scheme. On 11 years of ICLR data (2013–2025), the method consistently outperforms existing policies (ALLREJECT and FORWARDREJECT), reducing desk-rejections by up to 19.23% relative while running in under 54 seconds for the largest instance (11,672 papers).

## Strengths

- **Well-motivated practical problem.** The paper addresses a real and growing issue in AI conferences: per-author submission limits that desk-reject papers by simple ID order. The formalization of this as an optimization problem is a clean, first-principles approach that clearly improves over status-quo policies.

- **Consistent empirical improvements on 11 years of real data.** Table 3 shows the proposed method beats both baselines on every ICLR year from 2018 to 2025 across nearly all submission limits \(b\). The improvement is meaningful in the regimes that matter most — e.g., \(b=4\) for ICLR 2025: 2,984 desk-rejections (FORWARDREJECT) → 2,668 (Ours), a 10.59% reduction saving 316 papers. The evaluation spans the full growth of ICLR from 67 submissions (2013) to 11,672 (2025).

- **Practical efficiency.** All experiments complete within 53.64 seconds on modest hardware (2 vCPUs, 13GB RAM). The LP + rounding pipeline is fast enough for real conference operations, which is a nontrivial practical advantage over exact IP solving.

- **Explicit modeling of current policies as baselines.** Algorithms 1 and 2 formalize the actual policies used by venues like CVPR 2025, enabling a fair, apples-to-apples comparison. This transparency is valuable.

## Weaknesses

### Major

- **Definition 4.3 (LP relaxation) has an incorrect constraint.** The IP in Definition 4.1 has \(Ax \le b\cdot\mathbf{1}_n\). The LP in Definition 4.3 is written with \(Ax \le b - \mathbf{1}_n\). If interpreted literally, this tightens each author's capacity from \(b\) to \(b-1\), which means the LP is *not* a relaxation of the IP — it is a different, stricter problem. The paper must clarify whether this is a typesetting error (intended: \(b\cdot\mathbf{1}_n\)) or whether the implementation used the tighter constraint. If the latter, the empirical comparison to baselines that enforce \(b\) would be invalid. This is a serious exposition error that undermines confidence in the method's specification until resolved.

- **The rounding algorithm (Algorithm 3) has no approximation guarantee, and the gap to the LP optimum is unreported.** Theorem 4.6 only proves feasibility of the rounded solution, not any bound on the objective relative to the LP or integer optimum. The algorithm is an ad-hoc greedy heuristic. The paper should at minimum report the LP objective (an upper bound) alongside the rounded objective to quantify the rounding gap, as is standard practice in LP-rounding papers.

- **Step 14 of Algorithm 3 is underspecified.** The algorithm states "Find the set \(S_i \subseteq (S \cap T_i)\) such that \(\sum_{j \in S_i} \tilde{x}_j \geq (1 - x_l)\)" but does not specify *how* this set is selected (e.g., greedily by smallest fractional value, largest, or any order). The paper claims experiments are deterministic, so a fixed selection rule exists but is not stated. This harms reproducibility.

### Minor

- **No comparison to exact IP solutions for small instances.** For early ICLR years (2013: 67 papers, 2014: 69 papers), the IP could be solved to optimality with a standard solver in seconds. Reporting the optimal objective would (a) validate how close the LP+rounding pipeline is to optimal, and (b) provide a useful upper bound on the baselines' suboptimality.

- **The 19.23% headline improvement occurs in a low desk-rejection regime.** For ICLR 2024 at \(b=22\), the improvement is 26 → 21 desk-rejected papers (5 papers out of 7,404). While the relative metric is legitimate, the absolute effect is small. The paper should better foreground the practically significant regimes (e.g., \(b=4\)–\(10\)) where absolute savings are hundreds of papers.

- **The runtime comparison to baselines is omitted.** FORWARDREJECT runs in \(O(mk_2)\) — effectively milliseconds. The paper reports ≤53.64s for the LP method without acknowledging this trade-off or discussing whether the extra compute is justified in a conference operations setting.

- **The paper claims to "establish the computational hardness of the problem" (Introduction) but no hardness analysis appears in the main text.** While the problem is trivially NP-hard (multi-dimensional knapsack), this claimed contribution is not developed.

### Trivial

- None beyond what is listed above.

## Nice-to-Haves

- Report the LP optimum alongside the rounded integer objective for each setting to quantify the rounding gap.
- Compare against a simple greedy baseline that sorts papers by number of co-authors (fewest authors first) — a natural heuristic that would test whether the optimization formulation truly adds value over intelligent ordering.
- Ablate the rounding algorithm's selection rule (step 14 of Algorithm 3) to assess sensitivity.
- Test on synthetic data with ground-truth optimal solutions to validate the method's proximity to optimality.

## Removed Points

- *The paper cites Cohen et al. (2021) for an \(O(m^{2.37})\) time bound.* This is a theoretical result for a specific interior-point method, not for the PuLP solver used. However, the paper frames this as "For instance" — it does not claim PuLP achieves this bound. The criticism overstates the issue.
- *No discussion of variance.* Since experiments are deterministic, variance is not applicable. The paper correctly notes this.
- *"The conclusion claims transformative social impact."* This is a minor rhetorical overstatement common in conclusions. Not a substantive weakness.
- *Missing related work on knapsack/hypergraph b-matchings.* The paper explicitly notes prior work on this problem is scarce, which is accurate. The connection is not essential and suggesting it is scope creep.
- *Strength Finder strength about "correctness guarantees for rounding."* The guarantee is only feasibility, not optimality. This is noted in the weaknesses section. The guarantee is still a valid strength — it ensures the rounded solution doesn't violate the limit — but it's correctly contextualized.

## Novel Insights

None beyond the paper's own contributions. The key insight — that desk-rejection under per-author limits can be formulated as an IP and solved via LP + rounding — is the paper's contribution itself.

## Suggestions

1. **Fix Definition 4.3** — correct the constraint to \(Ax \le b\cdot\mathbf{1}_n\) and explicitly state that the same constraint is used in the implementation.
2. **Report the LP objective** alongside the rounded objective in Table 3 to quantify the rounding gap.
3. **Specify the selection rule** in step 14 of Algorithm 3 (e.g., "greedily by smallest fractional value").
4. **Solve the exact IP** for the smallest ICLR years (2013, 2014, 2017) and report the optimal gap for all methods.

## Score and Decision

**Calibration anchors (all rounds):**

| Anchor ID | Avg Score | Round | Comparison |
|---|---|---|---|
| pejtgHH7Eh | 4.00 | 1 (low) | VRG for MILP — more methodology issues, weaker evaluation. Current paper is stronger. |
| 5owXQrvnl2 | 4.00 | 1 (low) | MIP-LP gap mitigation — limited novelty, weak theory. Current paper is stronger. |
| 8LCdjf7uIk | 4.00 | 1 (low) | LLM for B&B scheduling — narrow scope, less complete evaluation. Current paper is stronger. |
| vqNg2Vl8o1 | 5.50 | 1 (mid) | Constraint reduction for MILP — deeper theory, accepted as Poster. Current paper is slightly weaker (exposition error, simpler method). |
| BVprkacwFY | 5.33 | 2 (narrow) | FrontierCO benchmark — broader scope and more thorough. Current paper is comparable but slightly weaker (exposition error). |
| sKvo9ZZfpe | 5.50 | 2 (narrow) | RRNCO for real-world routing — stronger architecture contribution. Current paper is slightly weaker. |
| tFEAzYdz92 | 5.50 | 2 (narrow) | OR-PRM for operations research — mixed reviews (8,4,2,8), deeper pipeline. Current paper is cleaner but less ambitious. |

**Round 1 bracket**: [3.5, 7.5]  
**Round 2 narrowing**: Compared against the 5.33–5.50 Accept-level anchors, the current paper has a cleaner focus but a more modest technical contribution and a notable exposition error. It is stronger than the 4.00 Reject-level anchors, which have more fundamental flaws.  
**Final score position**: Slightly below the 5.33–5.50 Accept anchors due to the Definition 4.3 error and lack of LP rounding gap analysis, but well above the 4.00 Reject anchors.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>