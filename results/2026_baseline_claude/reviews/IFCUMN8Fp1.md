## Summary

This paper addresses learning the parameters of a discrete POMDP — transitions, observations, and initial belief — from a stream of action-observation pairs collected under a random exploration policy, without any prior knowledge of the state space. The core contribution is bridging Predictive State Representations (PSR) and tensor decomposition methods: the paper shows that a PSR identifies POMDP parameters up to an unknown similarity transform P, then provides an algorithm to estimate P via joint diagonalization of action-conditioned observation matrices. The learned model recovers transition and observation likelihoods exactly when states have unique aggregated observation distributions across full-rank actions; otherwise it recovers them up to a "full-rank observability partition" of the state space (Theorem 1). Explicit parameter recovery enables post-hoc reward specification, which is shown to outperform PSR-only approaches in noisy observation settings.

---

## Strengths

- **Meaningful theoretical characterization.** Theorem 1 precisely characterizes the information-theoretic limit of what spectral+tensor methods can learn, introducing the notion of the "full-rank observability partition" to describe when full recovery is possible versus partial (partition-level) recovery. This is a clean result with concrete implications.

- **Novel bridge between two learning paradigms.** Extending Carlyle & Paz (1971) / Balle et al. (2014) to show that the PSR similarity transform P is exactly what tensor decomposition methods need to estimate — and then deriving how joint diagonalization over *all* full-rank actions simultaneously resolves ambiguity better than prior per-action methods (Azizzadenesheli et al., 2016) — is a genuine conceptual advance.

- **Practical motivation for explicit parameters.** The reward-specification experiment (Figure 4) offers a compelling demonstration that PSRs are fundamentally limited when the planner must target states identifiable only by transition dynamics (e.g., the maximum-entropy state in the noisy hallway), while the learned POMDP supports this via explicit observation matrices. This is not a toy distinction; it matters for real planning pipelines.

- **Honest characterization of method limits.** The paper carefully identifies when full recovery is possible versus only partition-level recovery, and the Sense-Float-Reset running example concretely illustrates a nontrivial partition.

- **Statistical rigor.** Results are averaged over 100 seeds, giving well-calibrated uncertainty estimates in the figures.

---

## Weaknesses

### Fatal
None.

### Major

1. **Experimental scope is severely limited.** All planning experiments use POMDPs with 2–4 states (Tiger: 2 states, T-Maze: truncated to small depth, Sense-Float-Reset: 3–4 states). Scalability to, say, 10–50 state POMDPs is entirely deferred to future work, but the method involves constructing a Hankel matrix whose size grows exponentially with history/test length, and computing eigendecompositions of matrices sized by the number of states. There is no evidence — empirical or theoretical — that the approach remains tractable beyond these toy examples. This makes the paper's practical claims fragile.

2. **Algorithm description is incomplete.** The procedure for computing P̃ is spread across three subsections (4.1–4.3) with key steps embedded in prose, and no pseudocode consolidating the full pipeline. Given the complexity of the steps (SVD, joint diagonalization, block-diagonal rotation, diagonal scaling), the lack of a formal algorithm box substantially harms reproducibility. This is distinct from any appendix omission — the main paper itself leaves the reader assembling steps from fragments.

3. **Planning performance does not improve over PSR.** Figure 3 (rows 3–4) shows the learned partition-level POMDP matches PSR planning performance, but never exceeds it. For domains with nontrivial partitions, the additional machinery of tensor decomposition and joint diagonalization yields no measurable planning benefit over simply using a PSR. The benefit is demonstrated only in the reward-specification experiment (Figure 4), which uses newly introduced, small domains. This narrows the practical case for the method considerably.

### Minor

1. **Assumption on ergodicity is underdiscussed.** The paper requires the induced Markov chain to be ergodic (Section 3.3), but for large POMDPs with many states and limited actions, the mixing time can be very long, requiring an enormous dataset even before statistical estimation errors are considered. No mixing-time analysis or sample complexity bound is provided, making it hard to assess how many interactions are realistically required.

2. **EM baseline treatment is weak.** EM is known to get stuck in local optima, but the paper does not attempt multi-restart EM or warm-start EM from the PSR-estimated parameters. The comparison is informative (EM fails to converge globally), but is not a thorough evaluation of whether EM with good initialization could be competitive.

3. **The requirement for at least one full-rank action is restrictive in practice.** While the paper argues many manipulation actions are full-rank due to failure probabilities, several standard POMDP benchmarks lack full-rank actions and are excluded from the method's applicability without comment.

### Trivial

- The paper uses "POMDP 8-tuple" but lists 8 components without explicit counting; minor notational inconsistency.

---

## Nice-to-Haves

- A computational complexity analysis of the Hankel matrix construction and joint diagonalization step as a function of state count, action count, observation count, and sequence length would clarify scalability claims.
- An experiment on a 10–20 state POMDP (e.g., a corridor maze) would meaningfully strengthen the empirical contribution.
- A cleaner algorithmic description (pseudocode) of the full pipeline from data to POMDP parameters.

---

## Novel Insights

The core novel insight is that PSR methods and tensor decomposition methods, previously viewed as separate tracks for POMDP model learning, are naturally unified: PSRs identify the model up to a basis change P, and tensor decomposition (specifically joint diagonalization of action-conditioned observation matrices across *all* full-rank actions simultaneously) is the correct tool to recover P. The aggregation across all full-rank actions via random weighting is the key move that allows the method to go beyond individual per-action recovery (as in Azizzadenesheli et al., 2016), reducing ambiguity to the minimum inevitable "observability partition" structure. This is a tidy theoretical observation, even if the subsequent algorithmic development relies heavily on existing tools.

---

## Suggestions

- Add a table or pseudocode algorithm summarizing the full method end-to-end (from raw data stream to POMDP parameters).
- Add at least one experiment on a POMDP with ~10 states to give evidence of scalability beyond toy domains.
- Clarify whether the block-diagonal rotation step (end of Section 4.3) is algorithmically determined or requires user specification of the partition structure.
- Report wall-clock time or per-step computation cost as a function of problem size to make scaling intuitions concrete.

---

## Score and Decision

The paper makes a genuine theoretical contribution by precisely characterizing the limit of spectral+tensor POMDP learning through the observability partition concept, and by showing that post-hoc reward specification is enabled by explicit parameter recovery in a way PSRs cannot support. However, the experimental evaluation is confined to 2–4 state toy POMDPs (leaving scalability entirely unverified), the practical planning benefit over PSRs is demonstrated only in a narrow setting, and the algorithm description is incomplete. For ICLR, which expects strong empirical support alongside theoretical contributions, the paper does not yet provide sufficient evidence that the method scales or provides consistent practical advantages.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>