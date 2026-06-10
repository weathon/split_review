## Summary
This paper proposes a method for learning discrete POMDP parameters from action-observation sequences by connecting PSR spectral learning with tensor decomposition. The core contribution is Theorem 1, which guarantees recovery of observation and transition matrices up to a "full-rank observability partition," using joint diagonalization via random weighted sums of observation matrices to estimate the similarity transform converting a PSR model into explicit POMDP parameters.

## Strengths
- **Well-developed theoretical framework with precise guarantees.** Proposition 1 (line 85) connects PSR models to POMDP parameters via an unknown similarity transform, Theorem 1 (lines 117–145) gives exact recovery guarantees up to the full-rank observability partition with explicit equations (Eqs. 10–15), and Lemma 1 (line 177) provides a probabilistic guarantee for the random weighting scheme. Proofs are provided in the appendix.

- **Strictly broader applicability than prior tensor decomposition methods.** Prior methods (Azizzadenesheli et al., 2016; Guo et al., 2016) require unique per-state observation distributions *for each individual action*. The paper relaxes this by aggregating across all full-rank actions via random weighted sums (Eq. 18, lines 171–175). This is concretely demonstrated on Sense-Float-Reset (Fig. 1), where all non-leftmost states have identical observation distributions for every action, yet the method still learns partition-level transitions — something prior tensor methods cannot handle.

- **Concrete demonstration of explicit-parameter advantage over PSRs.** Figure 4 shows a "noisy hallway" domain where assigning rewards to observations (the only option for PSRs) fails because the uniform belief and goal-state belief yield the same mixture observation distribution. The learned POMDP enables state-based reward assignment using the highest-entropy state, which successfully directs the agent.

- **Well-designed stress-test domain.** Sense-Float-Reset (Fig. 1) is specifically constructed to challenge the method with singular transition matrices (reset action), pervasive observation aliasing (all but two states share observations), and nontrivial reward structure. It is used consistently to illustrate both theoretical claims (Fig. 2) and empirical performance (Fig. 3).

## Weaknesses

### Fatal
None.

### Major
- **Extremely small-scale experiments limit practical significance.** Every domain has 2–4 states, 2–3 actions, and 2–3 observations. The Hankel matrix dimensions grow exponentially with maximum sequence length (Eq. 6, lines 59–63), and even these tiny domains require 10³–10⁶ interactions for convergence (Figure 3) and up to 10⁷ for reward specification experiments (Figure 4). The complete absence of any experiment beyond 4 states makes it impossible to assess whether the method is directionally practical for realistic problems. This gap between the motivating vision (robot manipulation, locking mechanisms — line 13) and the experimental evaluation is substantial.

- **The primary claimed advantage (reward specification) is demonstrated only on bespoke domains.** The two hallway domains are explicitly "introduced" by the authors (line 228) and designed so that "observation and transition matrices can be fully recovered by our method" (line 229). In the "noisy hallway," the observation-based reward strategy fails by construction — the uniform belief and middle-state belief produce the same mixture observation distribution. The state-based reward strategy succeeds only after transition matrices converge (~10⁶–10⁷ interactions, Figure 4 bottom row). No evidence is provided that this advantage generalizes beyond domains designed to showcase it.

### Minor
- **Partition-level recovery is theorized but not evaluated in terms of planning cost.** Theorem 1 is the key theoretical result, and Sense-Float-Reset has a nontrivial partition. However, the paper never analyzes what is *lost* by having only partition-level transitions — e.g., how planning with partition-level transitions compares to ground-truth. Line 233 notes planning performance is "similar across all models learned," which is expected since PSR and the learned POMDP make identical predictions. The interesting question — whether partition granularity suffices for planning — remains unanswered.

- **Domain naming confusion.** Line 229 states *noisy hallway* has "directional" observations and *directional hallway* has "noisy" observations. This swap between domain names and their observation types is confusing and should be clarified.

### Trivial
None.

## Nice-to-Haves
- A moderate-scale experiment (e.g., 6–8 states) to demonstrate scalability beyond toy problems.
- Wall-clock time and Hankel matrix size analysis for existing domains.
- Comparison with at least one neural/deep RL baseline to situate the method in the broader landscape (though the paper's scope is deliberately limited to spectral methods).

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Missing comparison with deep RL approaches**: The harsh critic raised this, but the paper explicitly scopes itself to spectral/tensor decomposition approaches and discusses deep learning in related work (lines 248–249). This is scope creep.
- **EM baseline fairness concern**: EM is configured with the same number of states as PSR/SVD (line 210–211), which is a fair comparison setup.
- **Finite-sample rank estimation sensitivity**: Deferred to Appendix B.1, which is standard practice for this type of paper. Not a critical main-text omission.
- **Strength about "rigorous experimental evaluation" from Strength Finder**: While 100 seeds per configuration is good practice, the experiments are on 2–4 state POMDPs, so the rigor of seed count is undercut by the scale limitation. Partially invalid given the Major weakness on scale.

## Novel Insights
The paper makes a genuine contribution in connecting two previously separate lines of work: PSR spectral learning (which recovers predictive models but not explicit parameters) and tensor decomposition (which recovers explicit parameters but under restrictive per-action uniqueness assumptions). The key insight is that by aggregating observation distributions across all full-rank actions via random weighted sums, one can recover parameters up to a partition rather than requiring per-state uniqueness. This is a meaningful theoretical generalization, though its practical implications remain untested at scale.

## Suggestions
- Expand at least one domain (e.g., Sense-Float-Reset) to 6–8 states to provide evidence of scalability.
- Evaluate planning quality under partition-level vs. ground-truth transitions to assess what the partition ambiguity costs in practice.
- Clarify the domain naming in the hallway experiments (line 229).

## Calibration Report

**All retrieved anchors:**
| Paper | Avg Score | Round | Comparison |
|-------|-----------|-------|------------|
| Stochastic Safe Action Model Learning | 3.00 | 1 | No experiments, poor presentation — clearly weaker |
| DHTM | 3.00 | 1 | Predictive state learning, poor clarity — weaker |
| Structured World Models | 3.00 | 1 | FSM learning, mixed quality — weaker |
| Bender's Oracle for Safe RL | 3.40 | 1 | Safe RL, different focus — weaker |
| Non-negative Tensor Mixture | 4.25 | 2 | Tensor decomposition, limited scope — weaker |
| Structured Predictive Representations | 4.80 | 1 | GNN + predictive state, limited novelty — weaker |
| Limitation of Transformer for HMMs | 5.25 | 2 | HMM learning, experiments-heavy but shallow — comparable |
| Cognitive Map Formation | 5.25 | 1 | POMDP learning, extensions — comparable |
| Provable Representation for POMDPs | 5.33 | 1 | POMDP theory + experiments, incremental — slightly weaker |
| POMDP Hardness/Tractability | 5.75 | 2 | POMDP theory, no experiments — comparable |
| OPE in POMDPs | 6.00 | 2 | Pure theory, accepted, clean separation — slightly stronger |
| Provable Learning for DEC-POMDPs | 6.17 | 2 | DEC-POMDP theory, no experiments, rejected — comparable |
| Proto Successor Measure | 6.75 | 1 | Novel theory + broader experiments — stronger |
| Policy Gradient for Confounded POMDPs | 8.00 | 1 | Accepted, much broader scope — much stronger |

**Round-1 bracket:** 5.0–6.5
**Round-2 narrowing:** 5.5–6.0
**Final score:** 5.5

The paper sits slightly below the OPE in POMDPs paper (6.00, accepted) which proved a broadly impactful model-free/model-based separation result, and comparable to the DEC-POMDP paper (6.17, rejected) and POMDP Hardness paper (5.75, rejected) in contribution level but with more empirical content. The genuine theoretical novelty (Theorem 1, partition-level recovery) is offset by the extreme small-scale experiments that prevent assessment of practical significance.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>