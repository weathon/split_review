Now I have all the information needed. Let me produce the final consolidated review.

## Summary

The paper proposes a spectral method to learn explicit transition and observation matrices of a discrete POMDP from action-observation sequences, relaxing prior tensor-method assumptions that every action must have full-rank transitions and per-state unique observation distributions. The key theoretical contribution connects PSR learning and tensor decomposition to recover parameters up to a "full-rank observability partition" — groups of states sharing identical observation distributions across all full-rank actions. Experiments on 2–4 state domains show that the method's parameter estimates converge to ground truth while EM fails, and the recovered models perform comparably to PSRs in planning.

## Strengths

- **Relaxes restrictive assumptions of prior tensor methods**: The method handles POMDPs where states share observation distributions (nontrivial observability partitions) and accommodates singular transition matrices — cases where existing tensor approaches (Azizzadenesheli et al., 2016; Guo et al., 2016) would fail. This is formalized in Theorem 1 and demonstrated on the Sense-Float-Reset domain.

- **Clean theoretical guarantee of partition-level recovery**: Theorem 1 proves that the algorithm recovers correct sums over partition blocks for initial belief, joint likelihoods, and the final vector under infinite data. The connection from Hankel matrix factorization (Eqs. 1–9) through Proposition 1 to the joint-diagonalization procedure (Eqs. 16–18) is well-structured.

- **Empirical convergence of model parameters**: Figure 3 shows observation-matrix and transition-matrix L1 errors approaching zero with sufficient data across Tiger, T-Maze, and Sense-Float-Reset (3- and 4-state), while EM consistently converges to wrong parameters. Results are averaged over 100 seeds, establishing statistical reliability.

- **Practical justification for the full-rank action assumption**: Section 4.1.1 grounds the key assumption in robotics — actions with stochastic success/failure (e.g., gripper slips modeled as \(p_{\text{succ}}T + (1-p_{\text{succ}})I\)) naturally produce full-rank transition matrices, connecting the theory to real-world applicability.

## Weaknesses

### Major

- **The reward-specification experiment does not convincingly demonstrate the claimed advantage of state-based rewards.** The paper argues that explicit state models enable state-based reward specification after learning — a capability PSRs lack. The experiment in Figure 4 attempts to show this in the "noisy" hallway domain, where observation-based reward should fail because different belief states yield the same observation mixture. However, the results show `Ours_obs` and `PSR_obs` (both observation-based) achieving higher total hacked reward than `Ours_state` (state-based) across most of the data range. The figure caption itself states "In all cases, 'Ours_obs' and 'PSR_obs' achieve higher rewards faster than other methods." While the paper notes that `Ours_state` "performs well after the transition matrices begin to converge," the data shown does not clearly establish that state-based reward outperforms observation-based reward in the regime where it is claimed to be necessary. This weakens the paper's motivational claim that explicit state models are valuable for downstream reward specification, though it does not invalidate the core algorithmic contribution.

- **Experimental evaluation is limited to small (2–4 state) toy domains.** All domains are hand-crafted to satisfy the method's assumptions (full-rank actions, ergodicity, rank-identical-to-number-of-states). The paper motivates the problem with furniture locking mechanisms (Baum et al., 2017) but provides no evidence of scaling to larger problems, more states, larger observation spaces, or violated assumptions. The paper acknowledges scaling as future work, but the gap between motivation and evaluation is large enough that the practical significance of the contribution remains unclear.

### Minor

- **The full-rank action assumption, while practically motivated, significantly restricts applicability.** The method can only learn observation distributions from actions with full-rank transition matrices. Non-full-rank actions contribute no information to the joint diagonalization step. The paper's example of robot manipulation actions (Section 4.1.1) shows one plausible class, but the paper does not discuss how common or easily verifiable full-rank actions are beyond this single example, nor how the method degrades when only a subset of actions satisfy the condition.

- **No analysis of finite-sample numerical stability.** The method requires inverting \(M^a\) for each full-rank action (Eq. 17). The paper does not discuss how ill-conditioned matrices (which can arise from finite-sample estimation error near singularities) are handled, nor any regularization strategy. This could be a practical obstacle for deployment.

- **The method's dependence on correctly estimating the rank of the Hankel matrix (exactly equalling the number of states) is not stress-tested.** The paper does not analyze or experiment with how the algorithm behaves when the rank is misspecified (too large or too small) due to finite-sample estimation error.

### Trivial

- The naming of the two hallway domains is confusing: "noisy hallway" has directional observations, while "directional hallway" has noisy (random) observations. This reverse naming makes the experimental narrative harder to follow and could lead to misinterpretation.

## Nice-to-Haves

- A controlled experiment where observation-based reward provably fails and state-based reward succeeds would substantially strengthen the motivational claim. This requires a domain where states in the same partition produce identical observation distributions for *all* actions and full-rank actions (a nontrivial full-rank observability partition with ambiguous observations for the goal state).
- A scaling experiment on a medium-sized POMDP (e.g., 10–20 states) to characterize how errors grow with state count would help contextualize the toy-domain results.
- A head-to-head comparison with the tensor methods of Azizzadenesheli et al. (2016) and Guo et al. (2016) on domains where those methods apply would clarify the empirical benefits of the paper's more general approach.

## Removed Points

These points are flagged to be removed, treat them with caution:
- **"Key step deferred to the appendix"** (Harsh Critic #3): The parser strips appendix content from all papers. The proof exists in the original submission. Per the rules: removed.
- **"Missing related works"**: Per the rules, we cannot flag missing related works as we lack external sources to confirm their existence.
- **"The eigenvalue analysis of p_succ T + (1-p_succ)I"**: The critic's concern about permutation matrices with eigenvalue -1 does not apply to the specific matrix structure described in the paper (deterministic target matrices with a single 1 per row; eigenvalues are 1 and 0). With p_succ ≠ 1/2, 1 the matrix is full-rank as claimed. The paper also references Appendix A.6 for the full justification.
- **Strength "Enables state-based reward specification"**: Retained in weakened form as the experiment does provide *some* evidence (the method does learn models that support state-based reward) but the claimed advantage is not clearly demonstrated. The core strength — that the method produces explicit models — is already captured by the empirical convergence strength.

## Novel Insights

None beyond the paper's own contributions. The two reviews identify a genuine tension: the paper's theoretical contribution (recovering POMDP parameters up to a partition) is clean and well-supported, but its key applied claim (state-based reward is valuable in noisy-observation settings) is not validated by the presented experiment. The paper would benefit from either adjusting the claim to match the evidence or redesigning the experiment.

## Suggestions

1. Redesign the reward-specification experiment: construct a domain where states in the same full-rank observability partition have observationally-equivalent signatures across *all* actions, yet the task requires distinguishing them. In such a domain, observation-based reward would provably fail and state-based reward would succeed, cleanly demonstrating the claimed advantage.
2. Add a brief discussion of finite-sample regularization for the matrix inversion in Eq. 17 and rank-selection heuristics when the true rank is uncertain.
3. Include at least one ablation showing the effect of misspecified rank on the recovered parameters.
4. Clarify the naming convention in the hallway domains to avoid confusion.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing**: Queried for "learning POMDP parameters from action-observation sequences spectral methods" across three bands.

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| 8jYuRCHYxv | 3.00 | R1-low | Missingness-MDPs. Weaker theory and empirical eval. Our paper is stronger. |
| 1VMmT0xwX5 | 3.00 | R1-low | Koopman spectral estimation. Less related; similar quality level. |
| gOdaIESaMi | 3.00 | R1-low | Parameterized action spaces. Less relevant. |
| tHmiydOQhn | 6.00 | R1-mid | Spectral Bellman Method (Accept, Poster). Stronger experiments (Atari), comparable theoretical depth. Our paper is somewhat weaker experimentally. |
| tpjCWgyE6j | 6.00 | R1-mid | Policy Regret in POMGs. Purely theoretical; withdrawn/rejected. Different style. |
| qtjAiNYLBw | 4.00 | R1-mid | Distributional POMDP VI (Reject). Had clarity issues and weak experiments. Our paper is stronger. |
| zbRh0eSl7Q | 4.50 | R1-mid | Optimistic VI for POMGs (Reject). Theoretical but missing experiments. Our paper has more concrete empirical validation. |
| qOyF214xmg | 8.00 | R1-high | Transducing LMs (Accept). Unrelated topic. |
| yRtgZ1K8hO | 8.00 | R1-high | Matrix sign methods (Accept Oral). Unrelated. |

**Round 1 bracket**: 4.5 – 6.5

**Round 2 — Narrowing**: Queried for spectrally-relevant tensor/PSR methods in (4.5, 6.5) and (5.0, 7.0).

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| 1GkzDABbME | 5.00 | R2 | Learning Mixtures of LDS via Tensor-EM (Accept, Poster). Similar structure: tensor + EM for latent variable models. Has real data (neural). Our paper has clearer theory but weaker empirical validation. Comparable overall. |
| tHmiydOQhn | 6.00 | R2 | (Repeat) Spectral Bellman Method. |
| lcEw5NcSij | 6.00 | R2 | Schrödinger eigenfunction for SOC. Less related. |
| mOSRwj2iIL | 5.50 | R2 | Learning Stable Reservoir (Reject). Strong theory but dense presentation. Our paper is more accessible and has cleaner experiments. |
| NGThArVrD3 | 6.00 | R2 | Neural mechanisms discovery. Less related. |
| 0lct7PrPgS | 6.00 | R2 | Learning sparse LSSMs (Accept Poster). Comparable quality, different topic. |

**Final score determination**: The paper under review has a genuine theoretical contribution (Theorem 1 with partition-level recovery) that is cleaner and better-motivated than the 5.0 MoLDS anchor (accepted poster). The experiments are more limited — only 2–4 state toy domains vs. synthetic + real neural data. The reward-specification experiment weakens rather than strengthens the applied motivation. Comparing against the 5.0 anchor (accepted) and the 4.0/4.5 anchors (rejected), the paper sits between them: its theory is stronger than those rejected anchors, and its empirical work is cleaner than the 4.0 POMDP VI paper, but the experiments are narrower than the 5.0 MoLDS paper. A score of **5.5** is appropriate.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>