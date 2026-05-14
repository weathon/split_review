Now I have a thorough understanding of the paper and the anchor papers. Let me compose the final consolidated review.

---

## Summary

This paper presents a method for learning explicit transition and observation matrices of discrete POMDPs from action-observation sequences collected under a uniform random exploration policy. The key idea is to first learn a Predictive State Representation (PSR) via spectral decomposition of a Hankel matrix, then apply a tensor-decomposition-based joint diagonalization procedure to recover the unknown similarity transform that obscures explicit likelihoods in standard PSRs. The method recovers transition and observation parameters up to a *full-rank observability partition* — states that share identical observation distributions across all full-rank actions are grouped together. Theorem 1 formally characterizes this recoverable structure. Experiments on Tiger, T-Maze, and Sense-Float-Reset show that the learned partition-level models support planning performance comparable to PSRs, and reward-specification experiments on hallway domains demonstrate the practical value of having explicit observation likelihoods.

## Strengths

- **Novel theoretical unification of PSR learning and tensor decomposition.** Theorem 1 provides a formal characterization of what is recoverable (transitions and observations up to a partition of states with identical observation distributions across full-rank actions), going beyond prior tensor methods that require per-action observation uniqueness (Azizzadenesheli et al., 2016; Guo et al., 2016). Lemma 1 and the joint diagonalization via random sums (Eq. 18) provide a clean mechanism for aggregating information across all full-rank actions simultaneously.

- **Empirically validated planning performance.** Across Tiger, T-Maze, and Sense-Float-Reset, PO-UCT planning with the learned partition-level models yields total rewards statistically indistinguishable from planning with PSRs or ground-truth models (Figure 3, row 4). This demonstrates that the partition-level abstraction is sufficient for effective planning.

- **Demonstrated practical benefit of explicit likelihoods.** The reward-specification experiments (Figure 4) show that having access to explicit observation matrices enables reward assignment based on hidden state, which outperforms observation-only reward assignment in the noisy hallway domain — a capability PSRs cannot provide without relearning.

- **Well-grounded modeling assumptions.** Section 4.1.1 and Proposition 2 connect the full-rank transition assumption to realistic robot manipulation models (e.g., actions with failure probabilities modeled as convex combinations of desired transitions and self-loops), and ergodicity is supported by passive sensing actions common in robotics.

## Weaknesses

### Fatal

None.

### Major

- **Theoretical-practical gap in the similarity transform construction.** Theorem 1 and its proof (Appendix A.5) require a random block-diagonal rotation matrix \(R\) whose blocks align with the full-rank observability partition. The experimental implementation, however, applies a fully dense random rotation \(R'\) to the SVD factors before computing the PSR and then sets \(R = I\) (Appendix B.1, lines 1724-1728). The paper acknowledges this simplification but provides no analysis of whether the resulting transform \(\tilde{P} = P' \cdot \text{diag}(P'^{-1} m_\infty)\) still satisfies the guarantees of Theorem 1. The proof in A.5 relies on the block-diagonal structure of \(R\) to guarantee that entries of \(R^T Q^{-1} \mathbf{1}\) are nonzero almost surely, which ensures invertibility of the diagonal scaling matrix. Without this guarantee, the construction could fail in edge cases. That the method works empirically is encouraging but does not close the theoretical gap. This weakens the paper's claim that the experimental results are grounded in Theorem 1.

### Minor

- **Reward-specification experiments limited to fully recoverable domains.** The claim that explicit observation/transition likelihoods enable post-hoc reward specification is demonstrated only on the noisy hallway and directional hallway domains, where the method recovers the full POMDP (singleton partitions). It is not shown whether partition-level models (e.g., from Sense-Float-Reset, which has a nontrivial observability partition) can support meaningful reward specification. This is the hard case that differentiates the method from prior work, and the empirical case for the method's main practical advantage remains incomplete for that setting.

- **Missing empirical comparison with prior tensor-decomposition methods.** The paper claims improved generality over Azizzadenesheli et al. (2016) and Guo et al. (2016) by aggregating observations from all full-rank actions rather than processing actions independently. This is a genuine theoretical advantage, but no empirical comparison is provided on domains where both approaches are applicable (e.g., Tiger). Such a comparison would strengthen the claim and help readers understand trade-offs.

- **Transition error curves conditionally truncated.** Row 3 of Figure 3 reports transition matrix error only when the estimated number of states matches the ground truth. The paper is transparent about this (the caption acknowledges it), and the number-of-states curves (Row 1) already show when estimation succeeds. However, this conditional reporting means the transition-error metric does not reflect failure cases where the state count is misestimated — a limitation readers should be aware of when interpreting convergence.

- **Parameter sensitivity acknowledged but not fully resolved.** The algorithm requires three thresholds (SVD reciprocal condition number, minimum singular value for full-rank detection, observation similarity for partition detection). The sensitivity analysis in Appendix C.2 shows that these parameters influence results, and the paper notes that larger Hankel matrices ease parameter selection. However, the lack of an automated selection procedure is a practical barrier to reproducibility and deployment. This is mitigated by the paper's honest discussion and the fact that threshold-dependence is a known challenge for spectral methods generally.

### Trivial

None.

## Nice-to-Haves

- Extending the reward-specification experiments to a domain with nontrivial full-rank observability partitions (e.g., Sense-Float-Reset) would compellingly demonstrate the method's value in the regime where prior tensor methods fail.

- A formal justification (or theorem) showing that the dense-rotation shortcut used in experiments preserves the partition-level recovery guarantees of Theorem 1, or a modification of the experiments to use the theoretically correct block-diagonal construction, would close the most significant gap in the paper.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic Point 3 (Missing comparison with prior tensor methods) was rated as "evidential" in the original critique with a demand that would seem to imply the paper's contribution is unsupported without it.** The paper's contribution is theoretical generality — the method works on a broader class of POMDPs than Azizzadenesheli et al. (2016) and Guo et al. (2016). An empirical comparison on domains where both are applicable (e.g., Tiger) would be valuable validation but is not necessary to establish the theoretical advance. The paper already compares against EM and PSRs, which are the most relevant practical baselines. Retained as a Minor weakness with reduced severity.

- **The harsh critic's "Structural" classification of Point 2 (reward specification only on fully recoverable domains).** The paper's claim about leveraging likelihoods for reward specification is demonstrated, just not on the hardest case. This is not structural — it's a scope limitation. Retained as Minor.

- **Strength Finder's claim that "Relaxation of per-action uniqueness" is a supporting strength with evidence from Section 4.2, Eq. 18, and Lemma 1.** This is valid and retained as a key strength merged into the first bullet under Strengths.

- **Strength Finder generic claims.** Removed generic phrasing like "this paper addressed an important problem" — the remaining strengths are all backed by specific paper content.

## Novel Insights

The paper's key insight — that a linear PSR model can be "unwound" via tensor-decomposition-style joint diagonalization to recover explicit observation and transition matrices up to a partition defined by observation-distribution equivalence — is genuinely novel and well-motivated. Prior work treated PSRs as black-box predictive models, and prior tensor methods assumed per-action observation uniqueness. The observation that aggregating across all full-rank actions via random weighted sums (Lemma 1) simultaneously relaxes the per-action assumption and produces a well-defined partition structure is elegant and opens a new direction for spectral POMDP learning.

## Suggestions

- **Close the theory-practice gap.** Either prove that the dense-rotation shortcut preserves the Theorem 1 guarantees (or state a modified theorem that covers the experimental setup), or modify the implementation to use the block-diagonal construction as specified in Algorithm 1. This is the single most important improvement.

- **Add a reward-specification experiment on Sense-Float-Reset** to demonstrate that partition-level models (not just fully recovered POMDPs) can be used for meaningful reward assignment. For example, designate the partition containing the +1 reward state and compare planner behavior with observation-only reward assignment.

- **Include Azizzadenesheli et al. (2016) as a baseline on Tiger,** where both methods are applicable. This would empirically validate the claimed advantage of aggregating actions and help readers calibrate the method against the closest prior work.

- **Report transition error for all seeds**, not only those where state count is correctly estimated, perhaps by reporting a combined metric or noting the failure rate separately for transparency.

## Score and Decision

### Anchor Comparison

| Path | Avg Human Score | Comparison to Paper Under Review |
|------|-----------------|----------------------------------|
| `/home/wg25r/review_agent/human_reviews_2026/tHmiydOQhn.md` | 6.00 | Spectral Bellman Method: similar profile — good theory, experiments with missing baselines, some theoretical gaps. This paper is slightly weaker due to the explicit theory-practice gap. |
| `/home/wg25r/review_agent/human_reviews_2026/1GkzDABbME.md` | 5.00 | Tensor-EM for LDS mixtures: provable guarantees + practical algorithm + real data. Similar quality; the current paper has a more novel theoretical bridge but less comprehensive experiments. |
| `/home/wg25r/review_agent/human_reviews_2026/kxzYGDL4fY.md` | 4.00 | POMDP state entropy: good idea, limited environments, accepted poster. This paper is stronger — it has a more substantial theoretical contribution and broader experimental validation. |
| `/home/wg25r/review_agent/human_reviews_2026/zbRh0eSl7Q.md` | 4.50 | OVI for POMGs: theory-heavy, no experiments, rejected. The current paper is stronger with both theory and experiments. |
| `/home/wg25r/review_agent/human_reviews_2026/BxJsXD1zQ0.md` | 1.50 | Spectral probe reliability: claims unsupported by experiments, rejected. The current paper is dramatically stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/Z3nbvxUat0.md` | 3.00 | Generative cognitive maps: rejected. This paper is clearly stronger. |

**Calibration rationale:** The paper makes a genuine theoretical contribution (Theorem 1, unification of PSRs and tensor methods), has transparent and reasonably thorough experiments, and addresses an important problem. The main weaknesses — a theory-practice gap in the rotation construction and limited scope of reward-specification experiments — are real but addressable. The paper is comparable to anchor papers in the 5.0-6.0 range. The explicit theoretical-practical gap (acknowledged but not resolved) pulls it slightly below the 6.0 anchor toward the 5.0 anchor. I score it **5.0**, corresponding to a borderline accept (poster).

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>