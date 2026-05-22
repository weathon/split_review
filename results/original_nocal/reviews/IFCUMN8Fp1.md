Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper connects spectral learning of Predictive State Representations (PSRs) with tensor decomposition methods to learn explicit POMDP transition and observation matrices from action-observation sequences. The core theoretical contribution is that these matrices can be recovered up to a *full-rank observability partition* — states sharing the same observation distributions across all full-rank actions are grouped together. The algorithm is evaluated on Tiger, T-Maze, and Sense-Float-Reset, showing that partition-level models match PSR planning performance while additionally enabling state-based reward specification that PSRs cannot support.

## Strengths

1. **Theorem 1 provides a rigorous characterization of what can be learned (partition-level recovery).** The theorem formalizes that spectral methods recover transition and observation parameters up to the full-rank observability partition, and Equations (13)–(15) show that summing over partition indices yields correct likelihoods. This extends prior tensor methods (Azizzadenesheli et al., 2016; Guo et al., 2016) that required per-action unique observation distributions, and provides a formal boundary on what is fundamentally learnable.

2. **Figure 3 (row 4) shows planning performance comparable to PSRs across diverse domains.** Using PO-UCT as the planner, the learned partition-level models achieve total rewards that are statistically indistinguishable from ground-truth and PSR-based planning on Tiger, T-Maze, and Sense-Float-Reset. This directly supports the claim that partition-level models are practically useful for downstream planning.

3. **Figure 4 demonstrates a concrete advantage of explicit likelihoods that PSRs cannot provide.** In the noisy hallway domain, the method's ability to assign rewards based on the highest-entropy state (using learned observation matrices) yields higher total hacked reward than observation-based reward assignment with PSRs. As the paper notes (Section 5), "the uniform belief state…does not elicit the correct behavior from the planner" while "the planner that uses the rewards emitted from the highest-entropy state performs well." This validates the motivation for learning explicit models.

4. **Section 4.1.1 provides a realistic justification for full-rank transitions.** The argument that manipulation actions modeled as convex combinations \(p_{succ}T + (1-p_{succ})I\) are full-rank under mild conditions connects the method's assumptions to practical robotics scenarios (citing Kaelbling & Lozano-Pérez, 2013; Garrett et al., 2020).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Section 4.3 algorithm description is terse; key steps deferred to the appendix.** The transition from the block-diagonal ambiguity (\(Q = P^{-1}P'\)) to the specific formula \(\text{diag}(RP'^{-1}m_\infty)RP'^{-1}\) is described in only a few sentences. The random block-diagonal rotation matrix \(R\) is introduced but its structure depends on the partition, which is what the method is trying to recover. While Appendix A.5 is referenced for the proof, the main text would benefit from a brief sketch of *why* this particular form works, e.g., how the diag rescaling properly marginalizes the block-diagonal blocks. Readers unfamiliar with the spectral POMDP literature may struggle to connect the steps.

2. **EM baseline description lacks detail on initialization and restarts.** The paper states EM is run with "a number of states determined by the number of components of the truncated SVD" but does not specify whether multiple restarts were used or how initialization was handled. EM for POMDPs is notoriously sensitive to initialization, and the observed performance gap between EM and spectral methods (Figure 3) could partly reflect this sensitivity rather than a fundamental limitation of EM. This should be stated explicitly.

3. **The hallway domains' full-recoverability claim could be better scoped.** The paper states the novel domains' "observation and transition matrices can be fully recovered by our method" (Section 5). This is true by design — these domains have a trivial (singleton) full-rank observability partition — but a brief note clarifying this would prevent the impression that the claim contradicts the general partition-level result.

### Trivial

1. **Figure 1's observation labels are underspecified.** The figure caption labels nodes with observations (e.g., a yellow state with "obs:1") but does not indicate which action this observation corresponds to. Since the float action emits observation 0 for all states (as stated in Section 4), the "obs:1" label must correspond to the sense or reset action. Adding action context to the label would eliminate potential confusion.

## Nice-to-Haves

- Include an explicit ablation of the random block-diagonal rotation step to isolate whether this heuristic is necessary or whether simpler alternatives (e.g., just using the joint diagonalization eigenvectors) suffice for planning.
- For Sense-Float-Reset, directly visualize the learned partition structure (aggregated transition matrix over partition indices vs. ground truth partition-level transitions) to make the theoretical claim tangible.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Critical Issue 1 (transition error inconsistency):** The harsh critic claimed that the near-zero transition error for Sense-Float-Reset contradicts the paper's partition-level claim, suggesting the error metric might compare against state-level ground truth. **Removed because** the paper explicitly states (line 314) that it measures "the L1 error of learned observation and **partition-level transition likelihoods** against ground truth." The comparison is against partition-level aggregated ground truth, consistent with Theorem 1. No contradiction exists.

- **"The float action text contradicts Figure 1":** The critic noted that the text says the float action emits observation 0 for all states, while Figure 1 labels a yellow state "obs:1." **Removed because** the figure does not specify which action's observation is being labeled. The observation label corresponds to the sense/reset action (which has different observations), not the float action. This is a minor figure-labeling ambiguity, not an inconsistency.

- **Multiple section-by-section nitpicks** (proof sketch absent, missing comparison with RNNs, lack of finite-sample analysis, visualizations, etc.): **Removed because** these are scope-creep requests or standard conference-level presentation choices (deferring to appendices). The paper provides proofs in Appendix A.5, compares against the relevant baselines (PSR and EM), and uses standard evaluation practices for the spectral POMDP literature.

- **Strength Finder's generic strengths** (e.g., "the paper addresses an important problem," "the motivation is clear"): **Removed because** these are superficial and lack specific evidence anchors.

## Novel Insights

None beyond the paper's own contributions. The two reviews agree on the paper's strengths (Theorem 1, planning parity with PSRs, reward specification advantage) and raise no fundamentally new observations that the paper itself does not already articulate. The main insight — that the conjunction of PSRs and tensor decomposition yields partition-level models while supporting downstream reward manipulation — is the paper's own contribution.

## Suggestions

1. Expand Section 4.3 in the main text with a 2–3 sentence intuition of why \(\text{diag}(RP'^{-1}m_\infty)RP'^{-1}\) resolves the block-diagonal ambiguity, even if the full proof remains in the appendix.
2. State explicitly whether EM was run with multiple random restarts or a specific initialization strategy.
3. Clarify the Figure 1 observation labels to indicate which action(s) they correspond to, or add a note that observations vary per action.

## Score and Decision

The paper makes a genuine theoretical contribution (Theorem 1, Lemma 1) that extends the known boundaries of spectral POMDP learning, and provides solid empirical evidence that partition-level models match PSR planning performance while enabling reward specification that PSRs cannot. The weaknesses identified (terse algorithm description in Section 4.3, EM initialization ambiguity, minor figure labeling) are all addressable with minor revisions and do not threaten the core claims.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>