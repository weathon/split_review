Now I have a thorough understanding of the paper and all the review claims. Let me compose the final consolidated review.

---

## Summary

This paper proposes PRI (Pruning-Refinement-Identification), the first model-free algorithm for best policy identification (BPI) in online Constrained MDPs. Leveraging the "limited stochasticity" property — that an optimal CMDP policy has at most N stochastic decisions for N constraints — PRI identifies which states require stochastic decisions, learns the weights of the resulting greedy policies via iterative optimization, and then recovers a single near-optimal Markov policy from the empirical occupancy measure. For well-separated CMDPs, the paper claims $\tilde{\mathcal{O}}(H\sqrt{K})$ regret with zero constraint violation and a matching $\Omega(H\sqrt{K})$ lower bound.

## Strengths

- **First model-free PAC algorithm for BPI in online CMDPs.** As stated in the abstract and Section 2, PRI is the first model-free algorithm to converge to a single near-optimal policy in an online CMDP, whereas prior model-free methods (e.g., Triple-Q) only provide average-performance guarantees over a mixture of policies. This addresses an open problem.

- **Order-wise improvement over the best existing model-free regret bound.** The paper improves from $\tilde{\mathcal{O}}(H^4\sqrt{SA}K^{4/5})$ (Triple-Q) to $\tilde{\mathcal{O}}(H\sqrt{K})$. The dominating term in $K$ does not explicitly depend on $S$ or $A$, as noted in the abstract and Table 1.

- **Matching $\Omega(H\sqrt{K})$ lower bound for well-separated CMDPs.** Theorem 2 shows tightness up to polylog factors for the class of well-separated instances, which is the standard way to establish optimality.

- **Novel algorithmic framework exploiting the limited-stochasticity structural property.** The three-phase design (pruning → refinement → identification) grounded in Lemmas 1 and 2 is conceptually clean and well-motivated. The idea that a CMDP with few constraints is not much harder than an unconstrained MDP is insightful (Section 4, lines 122–141).

## Weaknesses

### Fatal
None.

### Major

- **Very weak experimental evaluation.** The experiment section (Section 6) provides essentially no description of the environments (number of states, actions, constraint thresholds, transition structure). Only one baseline (Triple-Q) is compared, with no model-based or alternative model-free baselines. The number of independent trials is not reported; "95% confidence interval" is stated without clarification of the variance source. The results cannot be independently reproduced or evaluated. For a paper making strong empirical claims, this is a significant deficiency.

- **Unjustified bound on the number of greedy policies ($M \leq 2^N$).** Line 332 claims that after pruning, $M \leq 2^N$ greedy policies are needed. However, from the definition $M = \prod_{h,x} |\tilde{\mathcal{D}}_{h,x}|$ (line 221) and Lemma 1 (at most $N$ stochastic decisions), the general bound should be $M \leq A^N$ (each of the $\leq N$ stochastic states can retain up to $A$ actions). The claim $M \leq 2^N$ is not justified in the paper and appears to assume each stochastic state retains at most 2 actions, which is not argued. While $N$ is typically small (and the paper notes this), the discrepancy between the stated bound and what the algorithm actually permits should be clarified.

### Minor

- **Unexplained threshold choices in the Compare subroutine.** The Compare subroutine (Algorithm 3) uses a threshold of $4/K^{0.03}$ for the reward difference and the exponent $0.03$ is not derived from any concentration argument. Similarly, the pruning phase uses $K^{0.25}$ episodes per Triple-Q run without justification that this is sufficient for the required concentration given Triple-Q's $\tilde{\mathcal{O}}(K^{4/5})$ regret scaling. These choices may be justified in the deferred proofs, but the main text offers no intuition.

- **The constraint $\alpha_m \geq 1/\log K$ in Decomposition-Opt may be restrictive.** The lower bound on the mixing weights (line 222, $1/\log K$) prevents the algorithm from recovering arbitrarily small weights that might be needed for an optimal mixture. No rationale is provided for this choice.

- **Strong reliance on the "well-separated" assumption without discussion of graceful degradation.** The entire theoretical guarantee depends on $\sigma_{\min}$ being a positive constant independent of $K$ (line 294). The paper does not discuss what happens when this assumption is violated or how the algorithm degrades when $\sigma_{\min}$ is small but positive. Given that this is a strong assumption (analogous to a reward gap in bandits), it deserves more thorough discussion.

### Trivial
- The "95% confidence interval" in Figures 1–2 is mentioned without specifying the number of independent trials used to compute it.

## Nice-to-Haves
- A discussion of how the algorithm behaves when the well-separated assumption is relaxed (e.g., does it degrade gracefully with $\sigma_{\min} \to 0$?)
- Comparison against at least one model-based baseline (e.g., OptPess-LP) to contextualize the model-free vs. model-based trade-off
- A brief complexity analysis of the refinement phase in terms of $N$ and $A$ to clarify when the algorithm is practical

## Removed Points
These points are flagged to be removed; treat them with caution.

1. **"Policy identification phase cannot recover a near-optimal Markov policy" (Harsh Critic, Point 1).** REMOVED — factually incorrect. In CMDP theory, any feasible occupancy measure $q$ induces a Markov policy $\pi_h(a|x) = q_h(x,a)/\sum_a q_h(x,a)$ with exactly that occupancy measure (line 120; see Altman 1999). The identification phase estimates the occupancy measure of the near-optimal mixed policy and constructs the corresponding Markov policy. This is a standard construction, not a flaw.

2. **"All theoretical results are stated without proof" (Harsh Critic, Point 3).** REMOVED — the parser stripped the appendix. Proofs exist in the original submission.

3. **Abstract/Introduction framing oversells results ("regret-optimal," independence from $S$ and $A$).** REMOVED — the paper clearly qualifies these claims by stating the well-separated assumption and noting the implicit $S,A$ dependence via "sufficiently large $K$" (lines 296, 365). The terminology "regret-optimal" is standard when upper and lower bounds match for a well-defined problem class.

4. **"Pruning phase uses Triple-Q for only $K^{0.25}$ episodes without justification."** The concentration analysis for this subroutine is in the appendix (stripped). The paper does claim a specific probability bound ($1 - \mathcal{O}(K^{-9/8})$, line 269), which would require the deferred proof. This is a standard practice for conference papers.

5. **"Only one baseline (Triple-Q) is compared."** While this is a genuine weakness of the experimental section (kept as "Major" above), the critic's framing as "cannot be reproduced or evaluated" is somewhat overblown given that the paper's primary contribution is theoretical, and the experiments are meant to be illustrative.

6. **Various formatting/style nitpicks** — removed per instructions.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Substantially expand the experiment section.** Provide full descriptions of the environments (state/action spaces, constraint thresholds, transition dynamics), report the number of independent trials, and include standard deviations. Add at least one model-based baseline and, if possible, the recent BPI algorithm by Moskovitz et al. (2023).
2. **Clarify the bound on $M$ (number of greedy policies).** Either justify the $M \leq 2^N$ claim or correct it to $M \leq A^N$ and discuss the practical implications.
3. **Provide intuition for the threshold choices** in the Compare subroutine (e.g., why $4/K^{0.03}$ and $K^{0.25}$ episodes) in the main text, even if rigorous proofs are deferred.
4. **Discuss the well-separated assumption more thoroughly**, including whether the algorithm degrades gracefully when the gap is small.
5. **Acknowledge the computational complexity** of the refinement phase when $N$ is not very small.

## Score and Decision
The paper tackles an important open problem and proposes a conceptually novel algorithmic framework grounded in a well-known structural property of CMDPs. The theoretical claims — first model-free BPI with $\tilde{\mathcal{O}}(H\sqrt{K})$ regret — are significant. The harsh critic's most severe objections are based on misunderstandings or are about missing appendices. However, the paper has genuine weaknesses: the experimental evaluation is far too sparse to be convincing, and several algorithmic choices (thresholds, the $M \leq 2^N$ claim) are left unjustified in the main text. These issues are addressable in revision and do not undermine the paper's core theoretical architecture.

I assign a borderline score. The theoretical contribution is novel and important, but the evaluation is too thin to fully support the claims, and some algorithmic details need clarification.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>