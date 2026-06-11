Now I have sufficient calibration. Let me produce the final consolidated review.

## Summary

This paper connects Predictive State Representation (PSR) spectral learning with tensor decomposition methods to recover explicit POMDP transition and observation parameters from action-observation sequences. The key theoretical contribution is Theorem 1, which characterizes recovery up to a "full-rank observability partition" — states that share the same observation distributions across all full-rank actions are grouped, and the method recovers transition probabilities between these partitions rather than individual states. The paper demonstrates that this partition-level model enables a form of post-hoc reward specification (assigning rewards based on latent state properties) that black-box PSRs cannot support.

## Strengths

1. **Relaxes the per-action uniqueness assumption of prior tensor methods.** Prior spectral/tensor approaches (Azizzadenesheli et al., 2016; Guo et al., 2016) required that observation distributions be unique for every state for *each individual action*. The paper's method aggregates across *all* full-rank actions simultaneously (Section 1, lines 21-23), enabling recovery in domains (like Tiger) where per-action uniqueness fails but the aggregated collection is unique. This is a concrete, formally described relaxation.

2. **Formal characterization of the fundamental recovery ambiguity.** Theorem 1 (Section 4.1) and the block-diagonal analysis (Section 4.3) precisely characterize what can and cannot be recovered: when states share observation distributions across all full-rank actions, the method recovers transitions between *partitions* of states rather than individual states. The post-processing step (Eq. 12, lines 185-199) converting non-unique eigenvectors into partition-level likelihoods is a non-trivial algorithmic contribution that goes beyond prior work's silence on this ambiguity. Lemma 1 (Section 4.2, Eq. 18) adapts the random-weighted-sum joint diagonalization of He et al. (2024) to the POMDP setting, providing a principled way to resolve eigenvalue multiplicity.

3. **Empirical demonstration that partition-level models enable reward specification PSRs cannot.** Figure 4 shows that in the noisy hallway domain, the uniform belief state and the belief concentrated on the middle state yield identical observation mixtures, making observation-based reward specification fail — but the state-based reward specification using the learned POMDP recovers correct behavior. PSRs, lacking explicit transition/observation likelihoods, cannot support this operation. This concretely validates the motivation for recovering explicit POMDP parameters.

4. **Planning performance matches PSRs and ground truth.** Figure 3 (Row 4) shows that PO-UCT planning using the learned partition-level POMDP achieves total reward comparable to the ground-truth POMDP and the PSR across Tiger, T-Maze, and Sense-Float-Reset (3 and 4 state variants), suggesting the partition-level recovery is practically sufficient for planning despite not recovering individual-state transitions in some cases.

## Weaknesses

### Major

1. **Evaluation limited to toy domains (2-5 states).** The paper evaluates on Tiger (2 states), T-Maze (a few states), Sense-Float-Reset (3 and 4 states), and hallway domains (3 states). These are standard benchmarks but vanishingly small. The Hankel matrix construction requires enumerating action-observation subsequences, and its size grows as O((|A|·|O|)^L). The paper acknowledges scalability as future work (Section 7), but this admission means the method is currently demonstrated only on problems far from the motivating scenario (autonomous robots learning cabinet mechanisms). The gap between the demonstrated capability and the claimed motivation is vast. This is the single largest weakness.

2. **Requirement for full-rank transition actions is a hard structural constraint.** The method requires at least one action with a full-rank transition matrix. The paper discusses failure-prone robot actions as a source of full-rank transitions (Section 4.1.1, the convex combination p_succ T + (1-p_succ)I model). However, this is a modeling choice rather than a property of the system being learned — it requires the system to have actions *designed* to fail stochastically. Many POMDPs of interest (including the motivating cabinet mechanism example from Baum et al., 2017, which likely has deterministic transitions) may not satisfy this. The paper's own running example (Sense-Float-Reset) has a singular "reset" action; the method relies on "sense" and "float" being full-rank. This is constructed, not guaranteed about real systems. The title and abstract understate this caveat.

### Minor

3. **Reward specification experiment is a favorable proof-of-concept, not a competitive evaluation.** The noisy hallway domain is explicitly constructed so that observation-based reward fails (the uniform belief and middle-state-concentrated belief yield identical observation mixtures), making the comparison one-sided. In the directional domain (where both strategies work), observation-based reward (Ours_obs, PSR_obs) actually outperforms state-based reward (Ours_state, EM_state) — see Figure 4, top row, column 3. The paper attributes this to "slow convergence of transition matrices" (line 243), which is a limitation of the method, not a neutral observation. The experiment demonstrates the *existence* of a capability gap, but does not convincingly quantify when state-based reward is practically beneficial.

4. **Section 4.3 post-processing step is underspecified.** The description of the "random block-diagonal rotation matrix R, whose blocks correspond to the full-rank observability partition" (lines 196-199) is too vague to be reproducible without the appendix. What constitutes a "rotation" in this context — an orthogonal matrix? How is the block structure determined in practice? The notation "$P^{t-1}m_0$" is confusing (P has been used throughout as the similarity transform, and the superscript t-1 suggesting exponentiation is not meaningful in that context). This step is critical for converting P' into the transform $\tilde{P}$ that satisfies Theorem 1.

5. **No finite-sample analysis in the main text.** Theorem 1 is stated in the infinite-data regime (line 115: "Our statement is given in the regime of infinite data; for parameters introduced for finite data, see Appendix B.1"). The main text contains no convergence rates, sample complexity bounds, or finite-sample guarantees. The experimental results in Figure 3 show irregular convergence across domains (e.g., T-Maze observation matrix error doesn't convincingly converge to zero within 10^6 samples), and without theoretical guidance it is difficult to know what to expect for a new domain.

### Trivial

6. Confusing notation in lines 196-199 where "$P^{t-1}m_0$" appears to misuse P as both the similarity transform and something else, combined with an apparent exponentiation.

## Nice-to-Haves

- Include random restart details for the EM baseline (how many restarts, best vs. average reporting).
- An ablation of sensitivity to the random block-diagonal rotation matrix R would clarify whether results are stable across random draws.
- The discussion of full-rank transitions in robot manipulation (Section 4.1.1) could acknowledge that more complex failure modes (transitions to off-nominal states rather than self-loops) may or may not preserve full-rank properties.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that the method only recovers partition-level information (from Harsh Critic):** This is the paper's *stated* contribution — Theorem 1 explicitly characterizes this ambiguity. The paper is transparent about when full vs. partition-level recovery occurs. This is a feature described by the paper, not an undiscovered flaw. Removed because it misunderstands the paper's claims.

- **Criticism claiming Tiger is "the simplest POMDP possible":** Tiger is a standard, widely-used benchmark in the POMDP literature. Using standard benchmarks is not a weakness. Removed.

- **Speculative criticism about whether the cabinet mechanism example would satisfy the method's assumptions:** The paper uses this as motivating context, not as a claim that the method directly applies to that specific system. The criticism depends on information not in the paper. Removed as speculation.

- **Criticism about missing related works:** Hard rule prohibits this — I cannot confirm or deny the existence of related works.

- **Criticism about missing appendix content (proofs, finite-sample details):** The parser strips appendixes from all submissions; these exist in the original. Hard rule prohibits mentioning missing appendix content.

- **Criticism that the Hankel matrix scaling issue is "not discussed":** The paper explicitly acknowledges scalability as future work in Section 7 ("In the future, we intend to improve our method to scale to larger problems").

- **Generic "insufficient evaluation" framing without concrete anchor (from Strength Finder's removed strengths):** Removed as not concrete enough to be useful.

## Novel Insights

None beyond the paper's own contributions. The connection between PSR spectral learning and tensor decomposition for POMDP parameter recovery is the paper's core insight.

## Suggestions

1. **Include at least one moderately larger domain (e.g., 8-12 states)** to demonstrate the approach can function beyond the toy regime. The current 2-5 state evaluation is the primary barrier to assessing practical relevance.

2. **Provide a frank characterization of how often the conditions for full vs. partition-level recovery arise in practice**, and separately, how often the full-rank action requirement is satisfied — not just in robot manipulation with failure probabilities but across common POMDP benchmarks.

3. **Clarify the notation and algorithmic steps in Section 4.3.** The description of the post-processing with the random block-diagonal rotation matrix R needs sufficient detail to be reproducible from the main text alone (define "rotation," describe how block structure is determined, clarify what $P^{t-1}m_0$ means).

4. **Address the "slow convergence of transition matrices" issue** that causes state-based reward to underperform observation-based reward in the directional domain. If this is a systematic limitation, discuss it more prominently; if it can be mitigated, show how.

## Score and Decision

**Calibration Report:**

**Round 1 (Bracketing, 4 queries):** Initial bracket estimated between 4.0 and 7.0.

**Round 2 (Narrowing, 3 queries — 12 anchor papers examined, 4 read in full):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| KrtGfTGaGe (Wasserstein Believer) | 4.50 | R1+R2 | Our paper is stronger — no latent state assumption required |
| B5kAfAC7hO (Provable Representation) | 5.33 | R1+R2 | Our paper has clearer novelty; comparable overall |
| fkrYDQaHOJ (Koopman Dynamics) | 5.50 | R2 | Comparable — our paper has stronger theory, weaker experiments |
| Qja5s0K3VX (Statistical Tractability OPE) | 6.00 | R1+R2 | Their pure theory contribution is stronger; our paper is slightly weaker |
| Q00CO1Tm6M (Theoretical Hardness POMDPs) | 5.75 | R1+R2 | Comparable theory papers; our paper has empirical component |
| sEv6vHIUnu (Structured Pred. Rep.) | 4.80 | R2 | Our paper is stronger — more principled theory |
| Oq8bDXRf4F (Cognitive Maps) | 5.25 | R2 | Our paper is slightly stronger — clearer contribution |
| BgcapX9ers (HOO-POMDP) | 5.00 | R2 | Our paper is stronger |

**Final assessment:** The paper sits above the 4.5-5.0 cluster and is comparable to the 5.5-5.75 cluster. It has a cleaner theoretical contribution than the 5.33 paper (Provable Representation) but weaker empirical evaluation than the 5.50 paper (Koopman Dynamics). Positioned at 5.5 — a solid theoretical contribution with proof-of-concept experiments, honestly scoped with "Towards" in the title, but significantly limited by the small-scale evaluation and the full-rank action requirement.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>