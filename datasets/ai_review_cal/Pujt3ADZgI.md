- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have a thorough understanding of the paper and both reviews. Let me construct the final consolidated review.

## Summary

The paper proposes INPO (Iterative Nash Policy Optimization), an online algorithm for aligning LLMs under general (non-BT) preferences. It formulates alignment as a two-player game and uses online mirror descent (OMD) to approximate the Nash policy. The key claimed innovation is a population loss that bypasses explicit estimation of expected win rates. The paper provides convergence theory (O(1/T) last-iterate) and reports strong empirical results on AlpacaEval 2.0 (42.6% LC WR) and Arena-Hard (37.8%) with an 8B LLaMA-3 model.

## Strengths

1. **Strong empirical results on standard benchmarks.** Table 1 shows that INPO (PM) achieves 42.6% on AlpacaEval 2.0 and 37.8% on Arena-Hard, substantially outperforming all 8B baselines (Iterative DPO: 28.5%/29.6%, SPPO: 32.8%/29.2%) and several larger models. The improvement over SPPO represents a ~30% relative gain on AlpacaEval 2.0.

2. **Last-iterate convergence guarantee at O(1/T).** Theorem 2 establishes that KL(π*, π_T) ≤ 32C²/(τ²(T+1)) with time-varying η. This is practically useful (no need to average policies) and stronger than average-iterate guarantees common in game-theoretic learning.

3. **Practical query efficiency.** The tournament strategy uses O(K) preference queries per prompt (11 comparisons for K=8 responses), compared to O(K²) for methods that estimate expected win rates (Section 4.1). This is a concrete practical advantage clearly described.

4. **Ablation validating KL regularization.** Table 3 shows consistent degradation when τ=0 (e.g., AlpacaEval 2.0 drops from 42.6% to 41.6% with PM), supporting the design choice in the game objective.

## Weaknesses

### Major

1. **Proposition 1 (equivalence between L_t and the population loss) appears to be incorrect under general preferences.** This is the paper's central technical claim and the basis for connecting the practical algorithm to the OMD theory.

   **Verification.** The paper defines (Eq. 8/6):
   L_t(π) = E_{y,y'~π_t}[(h_t(π,y,y') − (P(y≻π_t)−P(y'≻π_t))/η)²]
   
   And the population loss (Eq. 10):
   E_{y,y'~π_t, y_w,y_l~λ_p(y,y')}[(h_t(π,y_w,y_l) − 1/(2η))²]
   
   Let Δ = P(y≻π_t)−P(y'≻π_t) and P = P(y≻y'). Expanding the inner expectation of the population loss over λ_p for a fixed pair (y,y') yields: h² + (1−2P)h/η + 1/(4η²). The corresponding integrand in L_t is h² − 2Δh/η + Δ²/η². The difference is:
   L_t(π) − PopLoss(π) = E[(2P − 2Δ − 1)h/η] + (E[Δ²] − 1/4)/η²
   
   The second term is independent of π. For the first term to be independent of π (so the losses differ by a π-independent constant), we need 2P(y≻y') − 2Δ − 1 = 0 for all (y,y') in the support of π_t, i.e., P(y≻π_t) − P(y'≻π_t) = P(y≻y') − 0.5. This condition does not hold under general preferences, nor is it implied by the BT model (contra the critic's claim — see below). Therefore, the equality stated in Proposition 1 is not generally valid.
   
   **Why it matters.** If Proposition 1 is incorrect, the algorithm implemented via Eq. (10) does not actually perform the OMD update from Eq. (6), breaking the link between the theory (Theorems 1-3) and the practical method. The empirical results may still be valid, but the paper's core theoretical contribution is undermined.

2. **No direct experimental validation of the claimed loss equivalence.** The paper compares INPO against iterative DPO and SPPO — different algorithms with different query structures. There is no ablation that isolates whether the population loss actually reproduces the OMD update. For instance, comparing INPO against a variant that explicitly estimates P(y≻π_t) (as in SPPO) under the same iterative framework would test whether the proposed loss behaves as claimed. Given the theoretical concern above, this missing experiment is consequential.

3. **Insufficient baselines.** Only two online RLHF baselines are reported (iterative DPO and SPPO). No comparison is provided against online IPO (Calandriello et al., 2024), which shares similar motivations and operates under general preferences, nor against other iterative game-theoretic approaches. The paper states "substantial improvement over state-of-the-art online RLHF algorithms" but the baseline set is narrow.

### Minor

1. **Limited iterations (T=3).** The theory provides last-iterate convergence at rate O(1/T) and the algorithm uses only T=3 iterations. No plot of performance vs. iteration is provided, leaving the empirical convergence behavior uncharacterized. Performance might improve further with more iterations.

2. **No statistical uncertainty reported.** Results are reported as point estimates without confidence intervals. Given the stochastic nature of the preference model and GPT-4-based evaluation, variance is non-negligible. This limits the reliability of the reported improvements.

3. **Assumption 1 (bounded log density ratio) not checked empirically.** The bound B appears in the theoretical rates but is never estimated or verified in experiments. The practical plausibility of this assumption for the LLaMA-3-8B model is not discussed.

4. **The comparison to SPPO has a structural asymmetry.** SPPO requires a preference model that outputs scores (not just binary preferences) and uses O(K²) queries, while INPO uses binary preferences with O(K) queries. The paper frames this as an advantage of INPO, but the different query budgets and model requirements mean the comparison does not isolate the contribution of the proposed loss.

### Trivial

- None.

## Nice-to-Haves

- A plot showing AlpacaEval 2.0 / Arena-Hard performance as a function of iteration number would strengthen the empirical claims and validate the convergence theory.
- A small-scale experiment with a tractable response space (e.g., a synthetic setup) where the OMD update can be computed exactly could test whether the minimizer of the population loss matches the true OMD policy.
- Comparison to online IPO would position the work more thoroughly within the general-preference RLHF literature.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh critic's claim that "the equivalence condition is precisely the BT model assumption."** The condition required for Proposition 1 is P(y≻π_t)−P(y'≻π_t) = P(y≻y')−0.5. Under the BT model, P(y≻π_t) = E[σ(R(y)−R(y''))] and P(y≻y') = σ(R(y)−R(y')). These are not equal in general (a simple counterexample: let π_t be a point mass on a response with very high reward, then both sides of P(y≻π_t)−P(y'≻π_t) ≈ 0, but σ(R(y)−R(y'))−0.5 can be arbitrary in (−0.5,0.5)). The critic's identification of this as "the BT condition" is factually incorrect. *This error does not, however, salvage Proposition 1; the mathematical problem remains.*
- **Critic's "Section-by-Section Notes" about Assumption 1 being "never estimated or checked."** This is included as Minor weakness #3 above but with reduced severity — this assumption is standard in the literature.
- **Strength Finder's claim about "novel loss objective that bypasses expected win-rate estimation."** This is kept as a strength of the *design motivation*, with appropriate caveats given the Proposition 1 concern.
- **Strength Finder's claim about "Theoretical justification for the algorithm design."** This is partially undermined by the Proposition 1 issue; retained implicitly via the theoretical guarantees (which may not apply to the implemented algorithm).
- **Strength Finder's generic/superficial claims about importance of the problem** — removed as not concrete.
- **Critic's suggestion that "weaknesses about missing appendix, missing proofs in appendix" are actionable** — removed per instructions; the parser strips appendices.

## Novel Insights

The two reviews present a sharp tension that reveals something genuinely interesting. The Harsh Critic identifies a genuine mathematical gap (Proposition 1's claimed equivalence does not hold under general preferences), but then overreaches by mislabeling the required condition as "the BT assumption" — an error that dilutes the credibility of an otherwise substantive criticism. Meanwhile, the Strength Finder correctly highlights the strong empirical results and clean algorithmic motivation but overlooks the foundational issue. The synthesis reveals that INPO likely works well in practice despite (not because of) its claimed theoretical justification — the population loss may serve as a reasonable heuristic approximation to the OMD update, and the tournament sampling plus iterative self-play structure may be the real drivers of performance. This is a class of paper where the practical contribution may be valid and valuable even if the formal bridge between theory and algorithm is broken, but the authors would need to honestly reframe the contribution as such.

## Suggestions

1. **Address Proposition 1.** Provide a full, correct derivation of the relationship between L_t(π) and the population loss, or honestly acknowledge that the population loss is an approximation and characterize the approximation error. If the equivalence cannot be fixed, remove the theoretical guarantees from the main claims and present the algorithm as a well-motivated heuristic with strong empirical support.

2. **Add a controlled ablation.** Compare INPO against a version of the algorithm that explicitly estimates P(y≻π_t) via O(K²) queries (as in SPPO's framework but under the INPO iteration structure). This would isolate the impact of the proposed loss.

3. **Add more baselines** including online IPO, and show error bars or confidence intervals for the main results.

4. **Extend Figure 1** (if available in appendix) to show performance vs. iteration across all T≥3 iterations, demonstrating the empirical convergence behavior.
