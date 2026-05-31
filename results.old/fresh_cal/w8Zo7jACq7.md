Now I have enough information to produce the consolidated review.

## Summary

This paper proposes PRI (Pruning-Refinement-Identification), the first model-free algorithm for best policy identification (BPI) in online Constrained MDPs. The algorithm leverages a known structural property of CMDPs — that there exists an optimal policy with at most N stochastic decisions (where N is the number of constraints) — and uses a three-phase approach: (1) prune unnecessary actions to identify where stochastic decisions are needed, (2) refine the weights of the resulting mixture of greedy policies, and (3) identify a single near-optimal policy from the occupancy measure. For well-separated CMDPs, PRI claims Õ(H√K) regret with zero constraint violation, matching a Ω(H√K) lower bound, and outputs a provably near-optimal policy. This significantly improves on the best existing model-free bound of Õ(H⁴√(SA)K^{4/5}) (Triple-Q).

## Strengths

- **First model-free BPI algorithm for online CMDPs with order-optimal regret.** The paper resolves an open problem by providing a model-free algorithm that identifies a single near-optimal policy (not just average-performance guarantees over a mixture) with Õ(H√K) regret, improving on the prior state-of-the-art bound of Õ(H⁴√(SA)K^{4/5}) from Triple-Q. The matching Ω(H√K) lower bound (Theorem 3.2) confirms tightness up to polylog factors.

- **Clever exploitation of the limited stochasticity property.** The paper uses a known structural result (Koo_88, Ros_89) — that an optimal CMDP policy has at most N stochastic decisions — to design a three-phase algorithm that identifies deterministic decisions via pruning, learns a small mixture of greedy policies, and extracts a single policy. This is arguably the natural algorithmic use of this structural property in a model-free online setting.

- **Asymptotic independence of the regret bound from state/action space sizes.** The leading term Õ(H√K) does not explicitly depend on S or A (line 365, though the threshold for "sufficiently large K" depends on them implicitly). This is a genuine departure from prior model-free bounds.

- **Experimental demonstration of practical advantage over Triple-Q.** On a synthetic CMDP, PRI achieves regret 6.89×10⁴ vs. Triple-Q's 1.57×10⁶, and on a grid-world, 1.69×10⁵ vs. 3.19×10⁶. Both with better constraint satisfaction. The learned policy's values closely match the LP-optimal solution in the synthetic case.

## Weaknesses

### Major

- **The well-separated assumption is a strong condition whose practical prevalence is undiscussed.** The paper defines σ_min as the minimum gap for which a reduced action space provably fails to contain an optimal policy (lines 291–294), and assumes it is a positive constant independent of K. No discussion is given of when this condition typically holds, what problem parameters it relates to, or whether common benchmark CMDPs satisfy it. The entire theoretical improvement over Triple-Q (Õ(√K) vs. Õ(K^{4/5})) is contingent on this assumption, yet the prior bound does not require it. The paper also acknowledges (line 365) that the threshold for "sufficiently large K" depends on S and A in an unspecified way, meaning the S/A-independence guarantee could be vacuous for practically relevant problem sizes.

### Minor

- **The claim that M ≤ 2^N (line 332) is stated without justification, and the computational cost of the refinement phase for larger N is unclear.** The refinement phase (Algorithm 4) iterates over all M greedy policies in each of √K rounds. The paper claims M ≤ 2^N, but this bound assumes each stochastic decision involves at most 2 actions, which is not justified by the limited stochasticity lemma alone (which only bounds the *count* of stochastic decisions, not the number of actions per stochastic decision). If a stochastic state-action set retains 3 or more actions after pruning, M could grow as quickly as (max |𝒟̃_{h,x}|)^N, potentially making the refinement phase computationally prohibitive even for moderate N.

- **Experimental evaluation lacks standard reproducibility details.** The paper reports regret and violation curves with "95% confidence intervals" (Figures 1–2) but does not specify the number of random seeds/independent runs, how the confidence intervals were computed, or whether the comparison with Triple-Q controls for identical total episode count and random seed alignment. The grid-world experiment additionally mentions "early stop heuristics" (line 395) that are not part of the described algorithm, making it unclear exactly what protocol was followed.

### Trivial

- The constraint violation plot labels (Figures 1–2) show negative values (indicating constraint satisfaction) but the y-axis labeling is not immediately self-explanatory.
- In line 143, "tightened constraints $\tilde{\rho}^{(n}=\rho^{(n)} + \epsilon_\rho$" has a mismatched brace.

## Nice-to-Haves

- A discussion of when the well-separated condition holds in typical CMDP benchmarks, or a relaxation of the assumption, would substantially strengthen the paper.
- An ablation study isolating the contribution of each phase (pruning, refinement, identification) would help understand which parts drive the empirical gains.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"No proofs are provided for any of the central theoretical claims."** — The harsh critic's primary "fatal" claim is that Section 5 (Analysis) states theorems without derivation. This criticism is removed per the instruction that the parser strips appendix sections from all papers; the detailed proofs are assumed to have existed in the original submission.

2. **"Reliance on Triple-Q: pruning phase uses Triple-Q as a subroutine... justification not provided."** — This criticism questions whether Triple-Q's average reward over K^{0.25} episodes is a reliable testing statistic. The paper claims Theorem 4.1 establishes the correctness of the pruning procedure with high probability. Since the proof of Theorem 4.1 is assumed to reside in the (stripped) appendix, this concern is addressed by that analysis.

3. **"M can be as large as A^N"** — The harsh critic claimed M ≤ A^N, but the paper actually asserts M ≤ 2^N (line 332). The corrected version of this concern is retained in Minor Weaknesses above (where the issue is lack of justification for M ≤ 2^N, not the specific value A^N).

4. **Strength: "Leverages a fundamental structural property"** — The strength finder credited this as a "supporting strength." This is retained in modified form in the Strengths section above (the clever *use* of the property is a strength, though the property itself is cited from prior work, which the paper correctly acknowledges).

5. **Strengths about lexical/problem importance framing** — Generic-sounding strengths about the problem being important are removed; only concrete, evidence-grounded strengths are retained.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any observation that the paper itself does not already articulate.

## Suggestions

1. Add a discussion section addressing the well-separated assumption: provide examples of when it holds, discuss its relationship to the minimum gap in linear programming for CMDPs, and clarify how large K needs to be relative to S, A, and σ_min before the leading Õ(H√K) term dominates.
2. Provide justification for the M ≤ 2^N bound, or discuss the computational implications when M is larger.
3. Add standard experimental details: number of independent trials, confidence interval construction method, random seed handling, and ensure the grid-world results report the unmodified algorithm (or justify the early-stop heuristic theoretically).

## Score and Decision

**Originality:** High — first model-free BPI algorithm for online CMDPs with optimal regret; the three-phase structure leveraging limited stochasticity is novel.  
**Importance of question:** High — addresses an open problem and achieves the model-free √K regret rate for the first time.  
**Claims supported:** Moderately — the algorithmic design is principled and the theorems are stated, but the central assumption (well-separatedness) is strong and its justification is limited. Experimental evidence is consistent with claims but lacks rigor in presentation.  
**Soundness:** Moderate — the algorithm design is coherent, but the strength of the well-separated assumption and lack of justification for M ≤ 2^N raise concerns.  
**Clarity:** Good — algorithms are described clearly; the paper is well-structured.  
**Value to community:** High if the theory holds; the approach of using structural sparsity for BPI in CMDPs is likely to inspire follow-up work.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>