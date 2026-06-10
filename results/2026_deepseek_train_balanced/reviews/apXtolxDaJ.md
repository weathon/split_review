Here is my consolidated review.

---

## Summary

This paper proposes BEER, a regularizer for value networks in DRL that adaptively controls the representation rank by enforcing an upper bound on the cosine similarity between consecutive state-action representations. The bound is derived from the Bellman equation (Theorem 1), and the regularizer uses a ReLU gate so that it only penalizes when the bound is violated, unlike prior methods (InFeR, DR3) that unboundedly maximize rank. BEER is evaluated on illustrative tasks (Lunar Lander, Grid World) showing adaptive rank behavior, and on 12 DMControl continuous control tasks where it outperforms baselines including SAC, TD3, DR3, and InFeR.

## Strengths

1. **Principled theoretical derivation from the Bellman equation**: Theorem 1 (Eq. 112–114) and Remark 1 (Eq. 121–122) derive an upper bound on the inner product and cosine similarity of consecutive state-action representations directly from the Bellman equation. This provides a theoretically grounded stopping criterion for representation rank regularization, contrasting with prior methods (InFeR, DR3) that unboundedly maximize rank without any RL-theoretic justification.

2. **ReLU-gated design makes regularization genuinely adaptive**: The regularizer in Eq. 140–144 uses ReLU so it penalizes only when cosine similarity exceeds the theoretical bound and contributes zero gradient otherwise. This is a clean algorithmic improvement — the regularizer turns itself on/off automatically based on whether the Bellman-derived constraint is violated, without needing manual tuning of regularization strength per task.

3. **Contrasting adaptive behavior across environments provides direct evidence of the mechanism**: On Grid World (simple, line 206), BEER produces *higher* representation rank than InFeR and DQN. On Lunar Lander (complex, Fig 1b), BEER produces *lower* rank. This bidirectional adjustment — not simply pushing rank in one direction — is the paper's strongest evidence that the regularizer genuinely adapts to task complexity rather than applying a fixed force.

4. **Top scores on all 12 DMControl tasks with fixed hyperparameters**: Table 1 shows BEER winning on every DMControl task (average 535.8 vs. 335.0 for SAC, 265.4 for TD3, 272.2 for InFeR, 223.3 for DR3), with β=1e-3 held constant across all tasks and no reported engineering tricks (line 204). The margins on several tasks (Acrobot Swingup: 260.5 vs. 46.2; Hopper Hop: 383.6 vs. 22.0; Cartpole Swingup Sparse: 750.8 vs. 147.6) are dramatic.

## Weaknesses

### Major

1. **Approximation error on DMControl tasks is not properly defined, undermining the mechanistic claim**. The paper defines approximation error for Lunar Lander as "the absolute difference between the estimated and the true value functions" (line 179), where the true Q-function is computable via dynamic programming. However, for the DMControl tasks, Section 4.2 (lines 250–251) and Figure 4 present "approximation error curves" without ever stating how the "true" Q-value is obtained. In high-dimensional continuous control, the optimal Q-function is unknown. If the TD target is used as a proxy, this is circular — the loss being minimized is precisely the distance to the TD target. If Monte Carlo returns are used, the rollout length and bias handling must be specified. As presented, the reader cannot determine what is being plotted, and the claim that "BEER reduces approximation error on DMControl" (a central piece of the paper's narrative connecting the regularizer's mechanism to performance) is unsubstantiated.

2. **The base algorithm for DMControl experiments is unclear, and the comparison against SAC/TD3 may conflate base algorithm effects with the regularizer's contribution**. The paper states BEER is "combined with the deterministic policy gradient method" (line 216, citing DPG and DDPG). Algorithm 1 shows a single Q-function without clipped double Q-learning, no target policy smoothing, and DDPG-style updates. Yet the baselines include SAC and TD3, which are substantially stronger algorithms than DDPG on DMControl. If BEER's base is DDPG, the reported improvements over SAC (60%) and TD3 (101.9%) are anomalous enough that the regularizer's independent contribution is difficult to isolate from base algorithm differences. No ablation with BEER applied on top of SAC or TD3 is provided to disentangle these effects. The comparison against rank-focused baselines (DR3, InFeR) is more relevant, but the headline framing emphasizes SAC and TD3 comparisons, making the evaluation protocol ambiguous.

3. **The theoretical bound becomes vacuous on zero-reward transitions, a limitation neither acknowledged nor investigated**. When the reward r=0 — the dominant case in sparse-reward settings — the bound in Eq. 121 simplifies to (‖ϕ(s,a)‖² + γ²‖ϕ(s',a')‖²) / (2γ‖ϕ(s,a)‖‖ϕ(s',a')‖). By the AM-GM inequality, this is always ≥ 1. Since cosine similarity is at most 1, the inequality cos ≤ (≥1) is always satisfied, and the ReLU input in the regularizer is always ≤ 0 — meaning the regularizer never fires on zero-reward transitions. The paper includes Cartpole Swingup Sparse (Table 1, line 237), a task where most transitions have r=0, and reports BEER achieving 750.8 vs. SAC's 147.6. If the regularizer is inactive throughout most of the training data, this improvement cannot be explained by the paper's stated mechanism. The paper should at minimum discuss this limitation; the absence of any analysis is a methodological gap.

### Minor

4. **Gap between theory (expectation) and practice (single sample) is not discussed**. Theorem 1 involves the *expectation* E[ϕ(s',a')] of the next-state representation (Eq. 112, 121), but the regularizer in Eq. 141–143 uses a *single sample* ϕ(s',a') from the target network (with stop gradient). While this single-sample approximation is standard practice in RL (the TD target itself uses it), it introduces a bias relative to the theoretical bound that the paper does not acknowledge. Since the bound is the paper's central theoretical contribution, this gap warrants at least a brief discussion.

5. **"12 out of 12 by a large margin" overstates the evidence for some tasks**. While BEER has the numerically highest average score on all 12 tasks, on several tasks (e.g., Finger Spin: 983.6 ± 6.8 vs. InFeR 966.0 ± 21.8 vs. SAC 956.5 ± 43.0 vs. TD3 957.9 ± 26.9) the differences are well within one standard deviation. Describing all 12 victories as "by a large margin" (Table caption, line 220) is imprecise; the margins vary substantially across tasks. This is a framing issue rather than a substantive flaw, but it undermines trust in the paper's presentation.

### Trivial

None.

## Nice-to-Haves

- Adding BEER on top of SAC and TD3 (rather than only on DPG) would directly address the comparison fairness concern and establish whether the regularizer is complementary to existing strong algorithms.
- A brief discussion of the sample-versus-expectation gap in the regularizer (Section 3.2) would improve theoretical rigor without changing the method.
- Reporting wall-clock time or relative compute overhead of BEER vs. baselines would help practitioners assess the method's practicality.

## Removed Points

- **Critic's comment about the matrix-form/operator-norm derivation being "unnecessarily complex"**: This is a presentational nitpick, not a substantive weakness. The derivation is mathematically valid. Removed per formatting/style rule.
- **Critic's complaint that the Cauchy-Schwarz approach would be "more transparent"**: Same nitpick. Removed.
- **Critic's claim that "12 out of 12" claim overstates the evidence because "claiming BEER outperforms on all 12 tasks based on point estimates without reporting statistical significance tests is standard in DRL"** and thus this "inflates the result": This was partially kept (see Weakness 5) but the full original criticism was overly aggressive — the paper indeed shows BEER numerically ahead on all 12 tasks; the inflation is specifically about the "large margin" framing, not the winning claim itself.
- **Strength Finder's "BEER achieves best scores on all 12 DMC tasks"**: Kept in Strengths but with the caveat from Weakness 5 noted. The strength itself (factual top scores) stands; only the "large margin" framing is critiqued.
- **Critic's Section-by-Section note about the regularizer can "also decrease rank when similarity is already below the bound"**: This is an incorrect reading of the paper — when ReLU outputs 0, rank is unchanged *from this term*, but the paper never claims the regularizer *decreases* rank. Removed as misunderstanding the paper.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's analysis of the sparse-reward bound vacuity is a genuinely novel observation that the paper missed, but it is captured in Weakness 3 above rather than constituting a separate insight.

## Suggestions

1. **Define the approximation error metric for DMControl explicitly** in Section 4.2. State how the "true" Q-value is obtained (e.g., Monte Carlo returns with specified rollout length, or a specific proxy) so that Figure 4 is interpretable.
2. **Clarify the base algorithm** used for DMControl experiments. If it is DDPG, state this explicitly. If it incorporates any TD3 or SAC design elements (clipped double Q, target smoothing, entropy), list them. Add a SAC+BEER or TD3+BEER ablation to isolate the regularizer's effect.
3. **Discuss the sparse-reward limitation** in either Section 3.2 or 6. Acknowledge that when r=0, the bound is always ≥ 1 and the regularizer does not fire on those transitions, and explain how the method still works in practice (e.g., through non-zero reward transitions or sampling noise).
4. **Add a brief remark** in Section 3.2 about the gap between the expectation-based theory and the single-sample implementation.
5. **Tone down the "large margin" language** in the Table 1 caption for tasks where standard deviations substantially overlap (e.g., Finger Spin). Consider reporting effect sizes or confidence intervals.

## Score and Decision

The paper's core idea — deriving representation rank constraints from the Bellman equation and implementing them via an adaptive ReLU-gated regularizer — is genuinely novel and well-motivated. The theoretical bound (Theorem 1) is sound, and the illustrative experiments on Lunar Lander and Grid World provide credible evidence that BEER adaptively controls representation rank in the claimed direction. These contributions are solid and publishable in principle.

However, the main empirical evaluation on DMControl has two structural problems: (1) the approximation error metric — central to the paper's mechanistic narrative — is undefined for these tasks, and (2) the base algorithm is not clearly specified, making the comparison against SAC and TD3 difficult to interpret. Additionally, a theoretical limitation (the bound's vacuity on zero-reward transitions) that directly affects the sparse-reward results is overlooked entirely. These issues prevent the paper from establishing its headline performance claims at the standard expected by ICLR.

The paper has a strong core and the weaknesses are addressable, but in its current form the empirical evidence does not convincingly support the claimed scale of improvement.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>