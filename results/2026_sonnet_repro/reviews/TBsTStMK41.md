Now let me run calibration searches to score this paper properly.Now I have enough information to write the final review. Let me compile everything.

---

## Summary

The paper formalizes the AI conference desk-rejection problem under per-author submission limits as an integer program (the "maximum desk-acceptance" problem), then proposes a two-stage solution: solve an LP relaxation and apply a greedy rounding scheme (MAXROUNDING, Algorithm 3) to recover a feasible binary solution. The method is evaluated on 11 years of real ICLR submission data (2013–2025) and consistently outperforms two baseline policies (ALLREJECT and FORWARDREJECT) in the number of papers desk-rejected, achieving relative improvements up to 19.23%, with all computations completing within 54 seconds.

---

## Strengths

- **Principled IP formulation that directly maximizes accepted papers.** Definition 4.1 casts desk-rejection as a binary optimization problem with an explicit objective to maximize the number of papers forwarded to review, in contrast to the existing feasibility-only approach (Definition 3.1). This is a clean and well-motivated re-framing.

- **Consistent empirical improvements across all 11 years and nearly all b values.** Table 3 shows that the proposed method never underperforms the strongest baseline (FORWARDREJECT) and, for large-scale years like ICLR 2024 and 2025, delivers improvements at every tested b value (e.g., 10–13% across all b ∈ {4, ..., 25} for ICLR 2025, saving over 300 papers at b = 4). The gains are not limited to one cherry-picked configuration.

- **Practical scalability.** The end-to-end pipeline on ICLR 2025 data (n = 11,672, 61,992 authorship entries) completes in at most 53.64 seconds on a modest server. This demonstrates the method is immediately deployable at conference scale.

- **Well-formalized baselines with complexity analysis.** Algorithms 1 and 2 are given formal pseudocode, correctness proofs (Propositions 3.5 and 3.6), and complexity bounds, ensuring the comparison is against clearly defined policies that match current practice.

---

## Weaknesses

### Fatal
None.

### Major

- **Unexplained constraint discrepancy between the IP and the LP "relaxation."** Definition 4.1 (the IP) uses constraint $Ax \leq b \cdot \mathbf{1}_n$ (each author's total ≤ b), while Definition 4.3 (the LP) uses $Ax \leq b - \mathbf{1}_n$ (each author's total ≤ b−1). These are not the same. The LP is strictly *tighter* than the IP in every constraint, which means it is not a relaxation in the traditional sense — it solves a harder feasibility problem on the RHS. The paper never explains this change. The most plausible intent is that the tighter LP provides one unit of slack per author, so that when MAXROUNDING rounds a fractional variable from $x_l \in (0,1)$ up to 1, the author sum can increase by at most $1 - x_l < 1$ without ever breaching the original constraint $b \cdot \mathbf{1}_n$. This would be a deliberate and correct design choice — but it is stated nowhere in the main text. Without this explanation, the "LP relaxation" label is misleading, and the correctness argument for Theorem 4.6 (whose proof is in the appendix) cannot be followed by a reader of the main paper. This must be addressed explicitly in the main text.

- **No optimality guarantee or gap analysis.** The paper's stated goal is to *maximize* desk-accepted papers (Definition 4.1), but Theorem 4.6 establishes only *feasibility* of the rounded solution, not optimality. MAXROUNDING is a greedy scheme (take the fractional variable with the highest LP value, round it up, eliminate conflicting fractionals) that can sub-optimally discard papers. There is no reported comparison between the LP objective value (an upper bound on the IP optimum) and the rounded solution's objective. As a result, the claim to "maximize" is not demonstrated — the method is shown to *improve over simple heuristics*, which is weaker. Reporting the LP upper bound alongside rounded results in Table 3 would allow readers to assess how close to optimal the algorithm actually is in practice.

### Minor

- **"Up to 19.23%" headline foregrounds the best-case configuration.** The 19.23% improvement comes from a single cell (ICLR 2024, b = 22), where the absolute difference is 5 papers (26 → 21). While the paper's overall improvements are genuine and consistent (see above), presenting this specific maximum in the title and abstract without a complementary summary statistic (e.g., median improvement when nonzero, or improvement at the practically relevant b = 25 / b = 10 settings) overstates typical impact.

- **FORWARDREJECT/REVERSEREJECT equivalence ignores which papers are rejected.** Section 3.2 notes that Algorithms 2 and 5 are "equivalent" and defers Algorithm 5 to the appendix. The equivalence holds in the number of rejections, but not in *which* papers are rejected. The ethics statement highlights protecting early-career researchers; this is in tension with treating ordering-based policies as interchangeable without discussing the author-welfare implications of ordering.

- **NP-hardness of the unit-profit case is asserted but not formally reduced.** Section 4.2 states the problem "cannot be solved efficiently in general" and cites the multi-dimensional knapsack literature. However, the standard MKP hardness argument uses varying item profits. The unit-profit case (all papers contribute equally to the objective) may have additional structure that tightens or weakens this claim. The paper does not provide even a sketch reduction for this specific instantiation. Given that NP-hardness motivates the LP approach, at minimum a note on the relationship to equal-profit set packing would strengthen the argument.

### Trivial
None.

---

## Nice-to-Haves

- Report LP upper bounds alongside rounded solutions in Table 3. This single addition would transform the empirical section from "we beat baselines" to "we are near-optimal," substantially strengthening the paper.
- A simple "greedy repair" post-processing pass (after rounding, attempt to include any remaining desk-rejected paper whose inclusion would not violate any author constraint) could cheaply recover additional papers and is worth exploring.
- At the b values used by real conferences (e.g., b = 10 for AAAI, b = 25 for CVPR), emphasize these specific results prominently rather than the maximum across all configurations.
- Consider briefly sketching the interaction with reviewer assignment, since any practical deployment couples desk-rejection with a matching pipeline.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: LP constraint discrepancy as possibly a parser/OCR artifact.** The harsh critic raised the possibility that the difference between `b · 1_n` and `b − 1_n` is a parser artifact. It is not: the paper explicitly writes both forms in separate definitions, making this a real design difference. The criticism is retained (as a Major weakness) because the paper uses a deliberately tighter LP without explanation.

- **Harsh Critic: Simulation validity may break due to behavioral differences.** The claim is that ICLR submission behavior would differ under a known limit. While conceptually true, the paper is transparent that its experiments are counterfactual simulations (Section 5.1), and the acknowledgment of the small OpenReview data gap is reasonable. There is no specific quantification problem anchored to a concrete figure or table. Removed as speculation.

- **Harsh Critic: High co-authorship density cascades in rounding.** This is a concern about potential edge cases in Algorithm 3 for papers with 15+ authors. The ICLR data (Table 2, ASPA ≈ 3.1–3.3, k₂ typically small) does not suggest this is a meaningful issue empirically. Removed as insufficiently grounded.

- **Strength Finder: Utilitarian social welfare as a strength.** The claim that framing the objective as utilitarian social welfare is a contribution is generic — maximizing a count is the most elementary utilitarian formulation. Removed as insufficiently specific.

- **Strength Finder: Reproducible empirical setup as a distinct strength.** Standard pseudocode, a public API, and a named open-source solver constitute ordinary good practice, not a paper-specific strength. Removed as generic.

---

## Novel Insights

The paper's most underexplored observation is that the LP constraint must be tightened to $b - \mathbf{1}_n$ (rather than $b \cdot \mathbf{1}_n$) to make the greedy rounding provably feasible. This "tight LP for valid rounding" pattern — solving a stricter LP to create slack that absorbs the rounding loss — is a specific structural decision that the paper uses correctly but never names or explains. Were this spelled out, it would be a clean and teachable method-design insight. As currently written, it remains implicit and potentially confusing.

---

## Suggestions

1. Add a paragraph in Section 4.2 explicitly explaining why the LP uses $b - \mathbf{1}_n$ instead of $b \cdot \mathbf{1}_n$, connecting it to the rounding argument in Theorem 4.6.
2. Add a column to Table 3 (or a supplementary table) reporting the LP objective value, so readers can assess the optimality gap of the rounded solution.
3. In the abstract and title, replace "up to 19.23%" with a more representative summary (e.g., "consistently 7–19% fewer desk rejections").
4. Include a brief formal argument (even just a reduction sketch) establishing NP-hardness for the unit-profit case, or explicitly cite a result that covers it.

---

## Score and Decision

**Calibration anchors retrieved:**

| Path | Avg Score | Round | Comparison to Paper |
|---|---|---|---|
| C9pndmSjg6 (Portfolio MIQP) | 3.00 | R1 weak | Much weaker — primarily heuristic with minimal theory and no real data |
| yYylDyLnzt (Dantzig-Wolfe + RL) | 3.00 | R1 weak | Weaker — toy experiments, methodology unclear |
| joMMM9eadc (Diffusion for IP) | 6.25 | R1 mid | Stronger — novel DL-based approach to a core CS problem; better theoretical backing |
| 2oWRumm67L (Light-MILPopt) | 5.00 | R1 mid | Comparable — applied optimization, real experiments, accepted |
| 6hvtSLkKeZ (CCBPP Encoder-Decoder) | 6.40 | R1 mid | Slightly stronger — cleaner technical contribution |
| ylhKbwJrjC (Mechanism design + MAB) | 4.67 | R2 narrow | Weaker — deeper theoretical gaps, narrower relevance |
| SVd9Ffcdp8 (DRL for sequential auctions) | 5.75 | R2 narrow | Comparable — real problem, empirical results, but toy data; paper under review has real data advantage |
| C9YyVygCpG (Max-min fair bandit) | 5.75 | R2 narrow | Comparable — tighter theory but narrower practical scope |
| INow59Vurm (GNNs for LP) | 5.50 | R2 narrow | Comparable — interesting connection but weaker practical grounding |

**Round 1 bracket:** 4.5–6.5.

**Round 2 narrowing:** The paper under review is notably stronger than the 4.67 anchor (ylhKbwJrjC) in terms of practical relevance, real-world data, and consistent empirical support. It is comparable to the 5.5–5.75 anchors (SVd9Ffcdp8, INow59Vurm, C9YyVygCpG) in terms of technical depth, though it benefits from a more timely and practically significant problem. The major unresolved issue (LP constraint discrepancy unexplained, no optimality gap) is a notable weakness that prevents it from reaching the 6.25–6.5 range where papers have tighter theoretical grounding. The empirical results are solid but not exceptional enough to compensate.

**Axes evaluation:**
- *Originality*: Moderate — first formal treatment of per-author submission limit optimization, but the techniques (LP+rounding) are standard.
- *Importance*: High — directly applicable to a growing real-world problem in AI conference management.
- *Claims supported*: Partially — improvements over baselines are well-supported; "maximizes" claim is not.
- *Soundness*: Moderate — algorithm works empirically, but the LP formulation has an unexplained discrepancy.
- *Clarity*: Fair — pseudocode and empirical tables are clear; the LP constraint choice is opaque.
- *Value to community*: Moderate-high — provides a ready-to-use tool for conference organizers.

**Final score: 5.0** — The paper addresses a timely and real problem, has consistent empirical validation, and provides a practical tool. However, the unexplained LP constraint change undermines the theoretical framing, and the lack of any optimality analysis leaves the "maximize" claim unsubstantiated. These are fixable issues, but as written they represent a meaningful gap between stated claims and demonstrated evidence. The paper is between the 4.67 (rejected with significant contribution gaps) and 5.75 (rejected but with clearer method execution) anchors, landing at 5.0.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>