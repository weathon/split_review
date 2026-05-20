Now I have all the information I need to write a thorough, calibrated final review.

## Summary
This paper proposes a spectral-tensor hybrid method for learning discrete POMDP parameters (transition and observation matrices) from action-observation sequences. The key theoretical contribution is extending the connection between Predictive State Representations (PSRs) and tensor decompositions to recover parameters up to a "full-rank observability partition" — grouping states that share identical observation distributions across all full-rank actions — thereby relaxing the per-action uniqueness assumption required by prior tensor approaches. The method is evaluated on several standard POMDPs (Tiger, T-Maze, Sense-Float-Reset) and two hallway domains where the learned explicit transition/observation models enable state-based reward specification that PSRs alone cannot provide.

## Strengths

1. **Novel theoretical characterization of recoverable structure (Theorem 1, Lemma 1).** The paper formally characterizes what can and cannot be recovered from the PSR similarity transform when states share observation distributions across full-rank actions. The result that the similarity transform can be recovered up to the full-rank observability partition — and that states within the same partition cannot be separated — is a precise, rigorous advance over prior work that assumed per-action uniqueness (Azizzadenesheli et al., 2016; Guo et al., 2016). Lemma 1's characterization of when eigenvalues of the random-weighted sum are distinct is clean and well-stated.

2. **Relaxation of restrictive assumptions from prior tensor methods.** Prior tensor-decomposition approaches required each action's observation distribution to be unique for every state. The proposed method instead leverages all full-rank actions simultaneously via joint diagonalization, recovering partition-level models when states share observation distributions. This meaningfully expands the class of learnable POMDPs, as demonstrated by the Sense-Float-Reset domain where most states share observation patterns.

3. **Empirical demonstration that explicit models enable reward specification.** The hallway experiments (Figure 4) concretely demonstrate that having explicit transition/observation likelihoods enables state-based reward design that works where observation-based rewards fail. In the noisy hallway, where the middle state's observation distribution is ambiguous, only methods using state-level rewards (Ours_state, EM_state) can successfully direct the agent, while observation-based methods (Ours_obs, PSR_obs) fail. This validates the paper's key practical motivation.

4. **Well-chosen running example (Sense-Float-Reset).** The illustrative domain (Figure 1) is used throughout to concretely explain observability partitions, the effect of full-rank vs. singular actions, and the output of the algorithm (Figure 2). This makes the theoretical ideas significantly more accessible than abstract exposition alone would.

## Weaknesses

### Fatal
None.

### Major

1. **The algorithm for partition recovery is under-specified in the main text (Sections 4.2–4.3).** The paper states that the joint diagonalization via random weighted sums yields eigenvectors that mix states within the same partition, and that Q = P⁻¹P' is block-diagonal with blocks corresponding to partitions. However, the text does not clearly explain **how** the algorithm discovers which entries belong to the same block from the eigendecomposition. The eigenvalues from the random weighted sum are distinct across partitions and repeated within them (Lemma 1) — this implies that the partition structure is revealed by the multiplicity of eigenvalues, but the paper never explicitly states this operational step. The final transformation using a random block-diagonal rotation R (lines 410–413) is presented without justification of how R is constructed or how the block structure is determined. The paper also does not explain how the joint diagonalization method of He et al. (2024) handles the resulting degenerate eigenspaces to choose a specific basis. These details may appear in the (stripped) appendix, but the main text should provide enough algorithmic intuition for a reader to assess correctness. As it stands, the key step connecting the joint diagonalization to the partition-level transform of Theorem 1 is too vague.

2. **T-Maze convergence failure is not discussed.** For T-Maze, the observation matrix error for the proposed method plateaus at about 2–3 L1 error (far from zero even at 10⁶ interactions), and the estimated number of states does not convincingly converge to the true value. The paper is completely silent on this. Since this domain is one of only four experimental benchmarks, the lack of discussion undermines the convergence claims. The authors should explain whether the assumptions (full-rank actions, ergodicity) hold for this domain, what the algorithm actually recovers, and why it struggles relative to Tiger and Sense-Float-Reset.

### Minor

1. **The PSR comparison on parameter error is not explained.** Figure 3 reports "Obs. matrix error" and "Trans. matrix error" for a method labeled "PSR." However, the paper never explains how transition and observation matrices were extracted from the PSR model — PSRs do not directly yield these matrices. If the extraction used the same or a related tensor procedure applied to the PSR's M^{ao} matrices, the comparison would be between two tensor-based approaches (the paper's joint diagonalization vs. a single-action approach), not a fundamentally different method. If some other procedure was used, it must be stated. Without this clarification, the comparison in Rows 2–3 of Figure 3 is opaque.

2. **Reward-specification experiment is limited in scope.** The claimed advantage for state-based reward specification is demonstrated on two hallway domains that share the same 3-state transition structure, differing only in the observation model of the middle state. In the directional hallway, the paper's own results show that observation-based methods (Ours_obs, PSR_obs) outperform the state-based method (Ours_state) at low sample sizes, but the paper does not discuss this trade-off or quantify when state-based rewards are actually needed. A broader evaluation across more diverse POMDPs (e.g., different partition sizes, different reward structures) would strengthen the claim that explicit likelihoods are practically valuable for reward specification.

3. **The EM baseline is standard but weak.** EM is known to converge to poor local minima in POMDP learning, and the results confirm this. Including an oracle EM (with the correct number of states) or a variational baseline would provide a more informative comparison, especially since the paper claims the main advantage is recovering explicit models, and EM is the only non-spectral baseline.

### Trivial
- The algorithmic step of identifying full-rank actions (A_full) is described as a "threshold test on the singular value decomposition" with no discussion of how the threshold is set or how robust the algorithm is to misidentification.
- Theorem 1 uses the phrasing "there exists an algorithm" rather than presenting the algorithm directly, which is an unusual framing for a constructive result.

## Nice-to-Haves
- A pseudocode listing of the full algorithm would significantly improve reproducibility and clarity.
- Reporting empirical runtime and complexity would help readers assess scalability, especially since the method involves constructing and decomposing large Hankel matrices.
- A finite-sample analysis summary (currently deferred to the stripped appendix) would strengthen the paper's theoretical contribution.
- Validating the algorithm on the Sense-Float-Reset example by showing the recovered partition-level transition/observation matrices side-by-side with ground truth would directly illustrate Theorem 1.

## Removed Points
- **Criticism that the appendix is missing/stripped and that proofs are absent**: The parser strips these from all submissions; they exist in the original paper.
- **Accusation that the algorithm "merely assumes the partition is known"**: The paper explicitly describes how the joint diagonalization reveals the partition through eigenvalue multiplicities (Lemma 1, Section 4.2). The description could be clearer, but the paper does not assume the partition is known.
- **Criticism that the T-Maze error "far from zero" was somehow misrepresented**: The paper does not claim perfect convergence on T-Maze; the issue is that it fails to discuss this result, which is a genuine gap but not a misrepresentation.
- **Request for more related work**: This would require external knowledge that the reviewer cannot verify.
- **Formatting/style nitpicks and typo complaints**: These are parser artifacts, not author errors.
- **Generic complaints about "evaluation lacking rigor" without concrete anchors**: The retained criticisms are all anchored to specific figures, equations, or sections.

## Novel Insights
The harsh critic correctly identified that the noisy hallway result is unsurprising — the domain is designed so that observation-based rewards fail. However, a more subtle point that neither reviewer fully develops is that the paper's claimed advantage (reward specification) is actually a general property of any method that recovers explicit O/T matrices, not specific to the proposed tensor approach. In the directional hallway, EM_state (which uses the same state-based reward strategy) works comparably to Ours_state once data is sufficient. The real contribution is thus not that explicit models enable reward specification per se, but that the proposed tensor method can recover these explicit models where EM fails — a distinction the paper sometimes conflates. A crisper separation of "recovery of explicit models" from "utility of explicit models" would strengthen the framing.

## Suggestions
1. **Rewrite Sections 4.2–4.3 to give a clear algorithmic description.** Include: (a) how the partition is extracted from the eigenvalue multiplicities of the random weighted sum, (b) how the block-diagonal rotation R is constructed, and (c) a concrete step-by-step procedure or pseudocode. The Sense-Float-Reset example could be carried through to show the recovered partition-level matrices.
2. **Discuss T-Maze explicitly.** Explain whether the assumptions hold, why the method plateaus at high error, and what the algorithm actually recovers in this domain.
3. **Clarify the PSR parameter error comparison.** State clearly how O and T matrices were obtained from the PSR for comparison, or remove the PSR lines from parameter-error rows if they cannot be meaningfully computed.
4. **Expand the reward-specification evaluation.** Include at least one additional domain with a different structure (e.g., RockSample or a domain with more than 3 states and different partition sizes) to demonstrate the advantage more convincingly.
5. **Move the proof sketches and algorithmic details from the appendix into the main text** for the key steps of the algorithm, particularly the construction of the final transform \tilde{P}.

### Score and Decision

**Calibration anchors (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/1GkzDABbME.md` | 5.00 | R1,R2 | **Learning Mixtures of LDS via Hybrid Tensor-EM** — Well-written, clear methodology, strong experiments. Our paper is less polished and has weaker experimental validation. |
| `/home/wg25r/review_agent/human_reviews_2026/zbRh0eSl7Q.md` | 4.50 | R1,R2 | **Optimistic Value Iteration for Low-Rank POMGs** — Pure theory, no experiments, limited novelty. Our paper has experiments and more novel theory; slightly stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/kxzYGDL4fY.md` | 4.00 | R1 | **Probing in the Dark: State Entropy for POMDPs** — Theory + experiments on self-designed benchmarks only. Similar evaluation scope; our theory is arguably more novel. |
| `/home/wg25r/review_agent/human_reviews_2026/hABW989AOr.md` | 4.50 | R1,R2 | **Tensor Power Methods** — Different topic. Less relevant. |
| `/home/wg25r/review_agent/human_reviews_2026/8jYuRCHYxv.md` | 3.00 | R1 | **Missingness-MDPs** — Weak anchor. Our paper is clearly stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/tpjCWgyE6j.md` | 6.00 | R2 | **Policy Regret Minimization in POMGs** — Pure theory, narrower scope. |
| `/home/wg25r/review_agent/human_reviews_2026/tHmiydOQhn.md` | 6.00 | R2 | **Spectral Bellman Method** — Well-executed with good experiments. Our paper is clearly below this. |
| `/home/wg25r/review_agent/human_reviews_2026/1VMmT0xwX5.md` | 3.00 | R1 | **Koopman/Spectral** — Weak anchor. |
| `/home/wg25r/review_agent/human_reviews_2026/BQIzu1T6F0.md` | 6.00 | R2 | **Controlling LDS** — Different topic but well-executed. |
| `/home/wg25r/review_agent/human_reviews_2026/SX9A72RPU3.md` | 4.50 | R2 | **TT covariance estimation** — Different topic. |
| `/home/wg25r/review_agent/human_reviews_2026/TlTygHKvRt.md` | 4.50 | R2 | **Universal Learning of Nonlinear Dynamics** — Different topic. |

**Round-1 bracket:** Between weak anchors (~3) and strong anchors (~8), narrowed to plausible range 4–6 based on similarity to MoLDS-LDS (5.0) and POMDP entropy papers (4.0).

**Round-2 narrowing:** Compared against MoLDS-LDS (5.0, accepted), POMDP entropy (4.0, accepted), and POMG value iteration (4.5, rejected). The paper's theoretical contribution is stronger than the entropy paper and comparable to the MoLDS paper, but its exposition is substantially less clear and its experiments have gaps (T-Maze convergence unexplained, PSR comparison unclear). The MoLDS paper at 5.0 was well-written with clear methodology and real-data experiments — our paper is clearly below that standard. The POMG paper at 4.5 had no experiments at all, making it a different type of contribution. The POMDP entropy paper at 4.0 had similar evaluation limitations.

**Final score:** 4.5 — reflecting a genuinely novel theoretical contribution that advances the state of the art in spectral POMDP learning, weighed against significant gaps in algorithm exposition and experimental completeness that require major revision before the paper is fully convincing.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>