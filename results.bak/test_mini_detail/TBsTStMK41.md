Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper addresses the problem of desk-rejecting papers when authors exceed per-author submission limits at AI conferences. It formalizes existing desk-rejection policies (ALLREJECT, FORWARDREJECT) and proposes a new optimization-based approach: formulating the problem as an integer program maximizing the number of desk-accepted papers, then solving via LP relaxation and a custom rounding algorithm. Experiments on 11 years of ICLR data (2013–2025) show consistent improvements over both baselines, reducing desk-rejections by up to 19.23% and running in under 54 seconds.

## Strengths

1. **First formal optimization framework for desk-rejection allocation.** The paper reframes a real policy problem—which papers to desk-reject when an author exceeds a submission limit—as a maximum-desk-acceptance integer program (Definition 4.1), moving beyond the purely feasibility-oriented formulation used in current practice. This is a principled departure from existing heuristics.

2. **Consistent empirical improvement on real conference data over 11 years.** Table 3 shows that the proposed method reduces desk-rejections across nearly all tested submission limits (b ∈ {4,…,25}) and all ICLR years (2018–2025), with relative improvements reaching 19.23% (ICLR 2024, b=22). The improvements are especially pronounced in recent, larger conferences (ICLR 2024, 2025), where the method shows gains across every tested limit.

3. **Practical efficiency.** All results in Table 3 were computed in at most 53.64 seconds on modest hardware (2 vCPUs, 13 GB RAM). This demonstrates feasibility for real conference workflows at scales up to ~11,000 papers.

4. **Rigorous formalization of current policies.** The paper provides explicit pseudocode for the two baseline policies (ALLREJECT and FORWARDREJECT) together with correctness proofs (Propositions 3.5, 3.6), making the baseline comparison precise and reproducible.

## Weaknesses

### Fatal
None.

### Major

1. **Unjustified modification of the LP relaxation constraint (Definition 4.3 vs. Definition 4.1).** The integer program (Definition 4.1) uses constraint `Ax ≤ b·1_n` (each author has limit b). The LP relaxation (Definition 4.3) instead uses `Ax ≤ b - 1_n`, tightening each constraint by 1. The paper presents this as the straightforward relaxation but provides no explanation or analysis of this modification. The change is non-trivial—it affects which solutions are feasible in the LP and consequently the quality of the roundable solution. Even if this tightening is intentional and justified in the appendix, the main text must explain the rationale (e.g., that the buffer of 1 is needed to absorb rounding increases). As written, a reader cannot evaluate whether the claimed improvements come from the optimization or from solving a more constrained problem.

2. **Rounding algorithm underspecified in the main text (Algorithm 3, step 14).** Step 14 states: "Find the set S_i ⊆ (S ∩ T_i) such that Σ_{j∈S_i} x̃_j ≥ (1 − x_l)" with a claimed O(k₁) time, but provides no method for constructing such a set, nor argues that such a set always exists. Whether a feasible S_i can always be found depends on properties of the LP solution that are not analyzed in the main text. While a full correctness proof may exist in Appendix B (which is stripped by the parser), the main text should at minimum outline the existence argument or cite the relevant lemma. Without this, the algorithm's correctness guarantee (Theorem 4.6) cannot be verified from the main text alone.

### Minor

3. **Presentation of ALLREJECT baseline.** The paper groups ALLREJECT alongside FORWARDREJECT as "existing policies used by major conferences." In practice, the CVPR 2025 policy ("retaining only those papers with the smallest submission IDs") corresponds to FORWARDREJECT, not ALLREJECT. While ALLREJECT is a reasonable comparator (it shows what the naive per-author-union approach produces), the framing that both are "current desk-rejection policies" overstates the operational relevance of ALLREJECT. This does not undermine the core results since FORWARDREJECT is the stronger baseline and the paper's main comparisons are against it, but the framing should be more precise.

### Trivial

- Remark 4.5 contains what appears to be a typographical error: "desk-rejection maximized desk rejection" likely intended "maximizing desk acceptance."

## Nice-to-Haves

- **Comparison to the true integer optimum.** The paper never compares the LP+rounding solution to the exact IP optimum (e.g., on small years like ICLR 2013/2014 where an IP solver would be tractable). Such a comparison would directly validate whether the relaxation+rounding approach is near-optimal, rather than just better than the heuristics.
- **Scalability discussion for larger conferences.** With submissions at some venues approaching 50k–100k, a brief discussion of how the LP-based approach scales (e.g., whether the PuLP default solver would remain practical) would strengthen practical applicability.
- **Discussion of alternative welfare criteria.** The current objective (maximizing total desk-accepted papers) is utilitarian. A brief discussion of alternative criteria (e.g., maximizing the number of distinct authors with at least one accepted paper) would be a useful future direction reference.

## Removed Points

These points from the inputs were flagged for removal and should be treated with caution:

- **Criticism about rounding algorithm correctness not being verifiable** (Harsh Critic point 2, "the algorithm's correctness is not established"): The paper states "Complete proofs are provided in Appendix B." Per policy, appendix content is stripped by the parser and exists in the original submission. However, the underspecification of Algorithm 3 step 14 in the main text is retained as a Minor weakness (point 2 above), since readers should not need the appendix to understand how the algorithm executes.
- **Criticism about "no experiments compare to true IP optimum":** Downgraded to Nice-to-Have—this would strengthen the paper but is not a flaw, as the paper's claims are about beating existing baselines, not achieving optimality.
- **Criticism about "safe authors" preprocessing being potentially problematic:** The paper defines safe authors as those whose papers have no co-authors exceeding the limit. This means all authors of those papers are safe, so the analysis is sound.
- **Criticism about runtime comparison not being given:** The paper reports absolute runtime and focuses on practicality relative to conference workflows (hours→days), not relative micro-benchmarking against trivial baselines. This is appropriate.
- **Criticism about "no experiments incorporated the use of GPUs" being irrelevant:** Correct—this is a descriptive statement, not a claim of GPU usage.
- **Criticism about "random initialization in Algorithm 4 being unexplained":** The paper later states "The experiments are deterministic and contain no randomness, so we report single results without variances." The random initialization comment in Algorithm 4 likely refers to solver initialization (which many LP solvers accept), and its practical role is clarified by the deterministic claim.
- **Strength Finder strengths about "important problem" / "practical relevance" without specific evidence dropped** as generic / not concrete enough.
- **Strength Finder claim about "Rigorous formalization of current desk-rejection policies"** kept but downgraded to supporting point.
- **Strength Finder claim about "Documentation of submission limits across major AI conferences"** dropped as it's just Table 1 which is straightforward data collection.

## Novel Insights

None beyond the paper's own contributions. The reviews do not synthesize a new observation about the paper that the paper itself does not state.

## Suggestions

1. **Explain the b-1_n constraint.** In the LP relaxation, clearly state why the constraints are tightened by 1, and note that this provides a buffer so rounding up fractional values does not violate the original IP constraints. If the tightening has a provable effect on the approximation ratio, state it.

2. **Specify the rounding subroutine concretely.** In Algorithm 3 step 14, either (a) provide a concrete greedy method for selecting S_i (e.g., sort fractional papers by decreasing x̃ⱼ and take the smallest prefix whose sum reaches the threshold), or (b) cite the specific lemma from Appendix B that proves existence and provides the construction.

3. **Clarify the baseline framing.** Acknowledge that ALLREJECT is a conceptual baseline rather than a commonly deployed policy, and note that FORWARDREJECT is the algorithm that corresponds to the "smallest submission ID" rule used by conferences like CVPR.

4. **Add small-instance IP comparison.** For ICLR 2013–2017 (or synthetic small instances), solve the exact IP with a commercial solver (Gurobi/CPLEX) and report the optimality gap of the LP+rounding solution. This would significantly strengthen the claim that the method is near-optimal.

## Score and Decision

**Round 1 bracket:** Based on initial calibration search, I placed this paper between 3.5 and 7.5. Weak anchors at ≤3.5 (papers that were rejected with serious flaws), middle anchors at 3.5–7.5 (mixed-quality papers).

**Round 2 narrowing:** I retrieved anchors in the 4–6 and 5.5–7.5 ranges. Reading the full reviews of four anchor papers:
- *L2P-MIP* (6.5, Accept): More technically sophisticated (learning to presolve for MIP), comprehensive multi-dataset experiments, strong practical claims. The desk-rejection paper has cleaner problem framing but is weaker technically and has only one dataset. → Paper is below 6.5.
- *Primal-Dual GNN* (5.25, Reject): Rejected for missing baselines and unconvincing results. The desk-rejection paper has better experiments but similar-level technical contribution. → Roughly comparable, slightly better.
- *ROS: Relax-Optimize-Sample for Max-k-Cut* (5.67, Reject): Similar method structure (relaxation + rounding), rejected for limited contribution and missing baselines. The desk-rejection paper's contribution is more novel (first to formalize this problem) but its technical gaps (unexplained constraint modification, algorithm underspecification) are similar in severity. → Comparable.
- *Evo-Step for OR* (5.5, Reject): Strong empirical results but presentation issues and unclear novelty. The desk-rejection paper has better presentation but similar novelty concerns. → Comparable.

The desk-rejection paper sits near the bottom of this range because (a) the LP constraint modification is unexplained, which is a genuine gap in the method specification, and (b) the empirical evaluation, while clean, is limited to one conference. However, it has real strengths: it addresses an underexplored problem, provides formal baselines, and demonstrates consistent improvement on real data.

**Final score: 5.0.** The paper has genuine contributions but contains a material technical gap (unjustified LP constraint change) that must be resolved. The contribution is not strong enough in its current form to warrant acceptance at ICLR but is a solid basis for resubmission with the technical issues addressed.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>