Now I have sufficient calibration data. Let me write the final review.

## Summary

This paper combines spectral learning of Predictive State Representations (PSRs) with tensor-decomposition methods to recover explicit POMDP transition and observation matrices from action-observation trajectories. The key theoretical contribution (Theorem 1) characterizes that the method recovers these matrices up to a "full-rank observability partition" — states that share observation distributions across all full-rank actions are grouped, but sums over partition indices yield correct likelihoods. Experiments on Tiger, T-Maze, Sense-Float-Reset, and hallway domains show the learned models approach PSR-level planning performance while additionally enabling state-based reward specification, which PSRs cannot do.

## Strengths

- **Theorem 1 precisely characterizes what is recoverable.** The paper formally states that the similarity transform can be recovered such that sums over partition-level indices yield correct likelihoods, even when individual state probabilities are not identifiable. This advances over prior tensor methods (Azizzadenesheli et al., 2016; Guo et al., 2016) that assumed full recovery, and gives the community a clear boundary on what spectral methods can and cannot identify.

- **Clear empirical demonstration of a practical advantage over PSRs.** Figure 4 (noisy hallway domain, third column) shows that after the model is learned, assigning rewards to states using the recovered transition and observation matrices ("Ours_state") allows the planner to drive the system to the middle hallway state, while a PSR that can only assign rewards to observations fails. This directly validates the claim that explicit likelihoods enable downstream model manipulation.

- **Convergence of learned parameters toward ground truth.** Figure 3 shows that observation and transition matrix errors decrease toward zero as data increases across Tiger, T-Maze, and Sense-Float-Reset, while EM baselines stagnate at high error. The trends are consistent with the theoretical expectation.

- **Joint diagonalization via random weighting (Lemma 1) is a clean extension.** The proof that random weighting of observation-transition products yields distinct eigenvalues for states in different full-rank observability partitions is a principled way to identify the partition structure non-heuristically.

## Weaknesses

### Major

- **Algorithmic description of the similarity-transform construction (Section 4.3) is too compressed for reproducibility.** The central step — converting the ambiguous eigenbasis from joint diagonalization into the transform \(\tilde{P}\) required by Theorem 1 — is described in only a few sentences. The paper introduces a "random block-diagonal rotation matrix \(R\) whose blocks correspond to the full-rank observability partition" and states the final transform as \(\text{diag}(RP'^{-1}m_\infty)RP'^{-1}\), but does not explain in the main text (1) how the blocks of \(R\) are algorithmically determined from the eigenvalue multiplicity pattern, (2) how \(R\) is sampled, or (3) why the random rotation does not break correctness beyond a pointer to Appendix A.5. While the partition structure is indeed identifiable through eigenvalue multiplicities (Lemma 1), the algorithmic steps connecting that identification to the final \(\tilde{P}\) need to be concretely specified in the main text for the paper's central claim to be reproducible. This is an addressable clarity issue, not a fatal flaw, but it is the paper's most significant weakness.

- **Error computation for learned parameters is underspecified.** Figures 3 and 4 report "Obs. matrix error" and "Trans. matrix error" against ground truth, but the paper does not describe how the learned parameters are aligned to ground-truth states. Since the recovered model is defined only up to a permutation of states (or up to a partition for non-singleton blocks), the error metric is meaningless without specifying a matching procedure (e.g., Hungarian assignment of observation vectors or partition indices). The caption of Figure 3 notes that "This error is only measurable once the estimated number of states matches that of ground truth," which partially addresses when the error is computed, but says nothing about how the alignment between learned and ground-truth indices is resolved.

### Minor

- **No direct experimental comparison against prior tensor-decomposition POMDP learners** (Azizzadenesheli et al., 2016; Guo et al., 2016). The paper motivates its contribution by stating these methods require unique observation distributions per state, which would make them fail on domains like Sense-Float-Reset. A direct comparison on domains where these methods *can* apply (e.g., Tiger, where each state has unique observations) would strengthen the claims about the method's relaxations being meaningful.

- **Sensitivity to the SVD truncation threshold and the threshold for identifying full-rank actions is not ablated.** The method relies on thresholds for rank determination and action classification, but no ablation study is provided. Since practical application of spectral methods depends on robust threshold selection, this omission limits usability guidance.

- **The claim that "the second strategy performs poorly due to slow convergence of transition matrices" (p. 9) is vague.** The convergence of transition errors is not shown alongside the reward curves in Figure 4, so this claim is not directly evidenced on the page.

### Trivial

- Figure 3 and 4 captions are long and dense. Separating key observations from visual descriptions would improve readability.

## Nice-to-Haves

- A discussion of how the history truncation length is chosen for the Hankel matrix and what the memory requirements are for the tested domains would help practitioners.
- An extension discussion about non-uniform exploration policies would be useful, since the method currently assumes uniform random actions.

## Removed Points

- **"Circular dependency" in Section 4.3 (Harsh Critic).** The critic claims that constructing R's blocks from the observability partition creates a circular dependency because "that partition is exactly what the algorithm is supposed to recover." This is incorrect: the partition is identified *earlier* through eigenvalue multiplicities of the random-weighted sum (Lemma 1). The eigenvectors have equal eigenvalues for states in the same partition, which reveals the partition structure before the rotation step. Removed for factual inaccuracy.

- **Speculation about what the appendix does/does not prove (Harsh Critic).** Statements like "if the appendix (which we cannot see) does not provide a tight proof" are removed per instructions. The criticism of main-text vagueness is retained (above), but speculation about appendix content is removed.

- **Generic strength about "addressing an important problem" (Strength Finder).** The strength "the problem is important" is generic and lacks specific evidence. Removed.

- **Strength about handling singular transition matrices (Strength Finder).** This is a minor technical point that is not a core strength of the paper. The Sense-Float-Reset example does include a rank-1 reset action, but this is more of a demonstration of the method's scope than a primary contribution. Moved here.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Expand Section 4.3 with a step-by-step algorithmic description (numbered pseudocode) of how \(\tilde{P}\) is computed from the PSR model components and the eigenvalue multiplicity pattern.
2. Explicitly describe the permutation/alignment procedure used to compute parameter errors against ground truth, or justify why the reported errors are meaningful without such alignment.
3. Add an ablation experiment on the SVD truncation threshold and the full-rank action classification threshold.
4. Include at least one direct comparison against Azizzadenesheli et al. (2016) or a conceptually similar tensor baseline.

## Score and Decision

**Calibration Report**

*Round 1 (Bracketing):*
- Weak band (avg < 3.5): 5AbtYdHlr3 (3.00), fnO5h1CFyh (3.00), B7cZvTQsUN (3.00), RAdBtquPiI (3.40) — all rejects with weaker contributions.
- Middle band (3.5–7.5): B5kAfAC7hO (5.33, reject), KrtGfTGaGe (4.50, accept), Q00CO1Tm6M (5.75, reject), Qja5s0K3VX (6.00, accept).
- Strong band (avg > 7.5): 8BAkNCqpGW (8.00), OeQE9zsztS (8.00 — unrelated topic), 5t57omGVMw (8.00 — unrelated topic).

*Initial bracket:* 4.0–6.5.

*Round 2 (Narrowing within bracket):*
- sEv6vHIUnu (4.80, reject): GNN predictive representations in RL. The current paper has a stronger theoretical contribution (Theorem 1 vs. a minor architectural modification), clearer problem framing, and more comprehensive experiments.
- Hcb2cgPbMg (6.25, accept), 41WIgfdd5o (6.25, accept): Strong theoretical papers with tight guarantees. The current paper is weaker on theoretical rigor but has practical reward-specification experiments.
- GdTOzdAX5A (5.75, reject): Switching dynamical system identifiability. Comparable technical depth, but the current paper has the advantage of empirical demonstrations on standard benchmarks.

*Final bracket:* 5.0–6.0. The paper is better than the 4.80–5.33 rejects (stronger theory, clearer experimental advantages) but lacks the complete theoretical tightness of the 6.0–6.25 accepts. The core contribution is solid and the experiments show a concrete advantage over PSRs, but the algorithmic description in Section 4.3 needs expansion and the parameter error evaluation needs clarification. I rate this paper at 5.5.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>