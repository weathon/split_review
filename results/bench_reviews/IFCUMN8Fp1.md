Now I have sufficient context. Let me write the final consolidated review.

## Summary

This paper bridges Predictive State Representations (PSRs) and tensor-decomposition methods to learn discrete POMDP parameters (transition and observation matrices) from action-observation sequences. The key theoretical contribution relaxes prior tensor methods' requirement that every action have state-distinct observation distributions, instead recovering parameters up to a "full-rank observability partition" — aggregates of states that share observation distributions across all full-rank actions. Experiments on Tiger, T-Maze, and Sense-Float-Reset show convergence of estimated parameters, and a reward-specification study on small custom hallway domains demonstrates a case where explicit likelihoods enable planning behavior not achievable with PSRs alone.

## Strengths

- **Relaxes a genuine restriction of prior tensor-based POMDP learning.** Prior work (Azizzadenesheli et al., 2016; Guo et al., 2016) requires each action's observation distribution to be state-distinct. This paper weakens that to requiring distinct observation distributions only when *aggregated across all full-rank actions* (Theorem 1). This is a meaningful theoretical generalization, and the proof structure (Lemma 1 → Lemma 4 → Theorem 1) is logically coherent and technically sound.

- **Establishes a novel connection between PSRs and explicit parameter recovery.** The paper proves that the similarity transform needed to convert a linear PSR into explicit state-transition and observation matrices can be estimated from the PSR itself via joint diagonalization of matrices derived from full-rank actions (Eq. 18, Lemma 1). This connection between two previously separate traditions (spectral PSR learning and tensor decomposition) is non-trivial and well-supported by the proofs in Appendix A.

- **Convergence to ground-truth parameters is empirically demonstrated.** Figure 3 shows that the estimated observation and partition-level transition errors (L₁ norm) decrease with more data and approach zero across three benchmark POMDPs, while EM consistently fails to recover correct likelihoods. State-count estimation also converges.

- **Honest about the fundamental limitation.** Theorem 1 precisely characterizes what can and cannot be recovered (the full-rank observability partition). The paper does not overclaim — it identifies the partition as the fundamental ambiguity and Theorem 1 is correctly stated.

## Weaknesses

### Major

- **The empirical case for the method's main advantage (reward specification via explicit likelihoods) is weak and limited in scale.** The reward-specification experiments (Figure 4) are conducted only on two custom 3-state hallway domains, and the two domains tell opposite stories:
  - In the *directional* domain (where observation-based rewards suffice), the state-based strategy (the claimed advantage) "performs poorly due to slow convergence of transition matrices."
  - In the *noisy* domain (where state-based rewards are genuinely needed), the approach requires 10⁷ interactions to begin approaching ground-truth performance, and the advantage over the observation-based baseline emerges only at the highest data regime.
  
  Moreover, both hallway domains are explicitly designed to be *fully recoverable* by the method (Appendix C.5.3: "It is important to note that these domains are fully-recoverable by our algorithm"). This means the experiments never test reward specification under the very condition the paper identifies as the core challenge — nontrivial full-rank observability partitions. The motivating examples (locking mechanisms, Sense-Float-Reset) belong precisely to this case. Testing reward specification on a domain like Sense-Float-Reset with a nontrivial partition would be necessary to substantiate the claim that partition-level parameters enable meaningful reward specification.

- **The method's sample complexity is a practical concern that is not adequately addressed.** The noisy-hallway reward specification requires 10⁷ interactions to work well. The sensitivity analysis (Tables 2–4) reveals that for T-Maze with 14 states, *no* parameter setting reliably succeeds at state-count estimation. The paper does not hypothesize why — whether this is a fundamental signal-to-noise ratio limitation, an observability-length issue, or a rank-estimation problem. Given that the method scales exponentially in the observability length (Appendix B.2: O(|S|·(|A||O|)^{2(n_obs+1)})), this creates a serious practical ceiling: the method is effectively feasible only for POMDPs with very small state spaces and short-range dependencies.

- **Figure 3's presentation conflates two different evaluation regimes.** The L₁ errors for observation and transition matrices are reported only for runs where the estimated number of states matches the ground truth (a selection bias that the caption acknowledges but does not correct). The planning performance (row 4) is reported for *all* runs, including those where state-count estimation failed. Disaggregating planning performance by whether state-count estimation succeeded would clarify whether the method's planning utility depends on first getting the state count right — if planning is robust to state-count errors, that is a positive result; if it degrades sharply, it underscores the importance of rank estimation.

### Minor

- **Sensitivity analysis shows severe degradation on larger problems, with no explanation.** Tables 2–4 show that for T-Maze beyond ~6 states, very few parameter settings yield correct state-count estimates, and for 14 states the method entirely fails. Is this an observability-length issue (the Hankel size is too small)? A signal-to-noise issue? A fundamental limitation of spectral methods for larger state spaces? The paper should offer some hypothesis and diagnostic evidence (e.g., the singular value gap as a function of state count).

- **The reward-specification experiments would benefit from analyzing convergence rates.** The paper notes (Appendix C.4) that "accurate transitions are required to correctly assign reward to the desired goal state" and that the method's transition estimates converge more slowly than the PSR's predictions because the eigendecomposition adds an extra layer of estimation error. A plot of transition-matrix L₁ error vs. planning reward for the hallway domains would help link the two.

- **Selection bias in Figure 3's L₁ error reporting.** As the caption notes, transition error curves are truncated because they are only reported when the state count matches ground truth. This means the curves show performance on the most favorable subset of runs. The paper should report, at minimum, the fraction of runs that are excluded at each data size.

### Trivial

- The abstract states "Our experiments suggest that these partition-level transition models learned by our method, with a sufficient amount of data, meets the performance of PSRs" — there is a subject-verb agreement error ("models... meets").

## Nice-to-Haves

- **Visualizing what partition-level parameters look like for a nontrivial case.** Figure 8 shows a learned Tiger model (full recovery). Showing a learned model for Sense-Float-Reset (where only partition-level recovery is possible) would help readers visualize what the algorithm actually outputs and how partition-level transitions are interpreted.

- **Adaptive stopping for data collection.** The paper uses predetermined data sizes. Monitoring convergence of the Hankel matrix's singular values to stop data collection adaptively would be a practical improvement.

- **Singular value spectrum plots.** Plotting the singular value spectrum of the empirical Hankel matrix as a function of data size would help build intuition for why rank estimation succeeds or fails.

- **Handling mixed full-rank and singular actions.** The paper currently filters out singular actions entirely. A discussion of whether singular actions can still inform partition identification would strengthen the paper's treatment of realistic POMDPs.

## Removed Points

These points were flagged but are inaccurate, confused, or fall under the removal rules:

- **"PSR with reward relabeling missing baseline"** — The critic suggests relabeling a PSR's predictive distributions with a new reward function. But this *is* effectively what the "PSR, obs" strategy in Figure 4 already does: a PSR can only assign rewards to observed (action, observation) pairs, not to latent states. The "obs" condition is already the natural PSR-based reward-specification baseline. The critic's suggestion does not correspond to a distinct or feasible alternative.

- **"EM not run on reward-specification task"** — Figure 4's legend includes "EM, state" for both domains. The critic is factually wrong.

- **"Paper does not discuss p=1/2"** — Proposition 2 (Appendix A.6) explicitly addresses the p=1/2 case and proves it leads to singularity. The paper does discuss this.

- **"Paper does not discuss that algorithm only needs at least one full-rank action"** — Algorithm 1 (lines 9–11) explicitly filters for full-rank actions via a minimum-singular-value threshold. The paper states "the algorithm requires at least one action to be full-rank" is implicit in the construction.

- **"Exponential runtime not discussed in main text"** — This is a presentation choice, not an error. The complexity analysis is in Appendix B.2 as is standard for technical details. The paper notes the exponential dependence honestly.

## Novel Insights

Beyond the paper's own contributions, the reviews do not yield a genuinely novel synthesis that the authors themselves have not already identified. The tension between the theoretical generalization (relaxing the per-action uniqueness assumption) and the empirical limitations (small-scale experiments, large data demands, failure on larger POMDPs) is the central theme that emerges from the reviews.

## Suggestions

1. **Test reward specification on a domain with a nontrivial full-rank observability partition** (e.g., Sense-Float-Reset). This is the critical missing experiment: it would either demonstrate that partition-level parameters are practically useful for reward specification, or honestly reveal the method's limits.

2. **Disaggregate planning results by whether state-count estimation succeeded.** This would clarify whether the method's planning utility hinges on correct rank estimation.

3. **Add diagnostic analysis of why the method fails on larger T-Maze instances.** Plot the singular value gap of the Hankel matrix as a function of state count to show whether the rank becomes harder to detect, or whether the observability length is the bottleneck.

4. **Quantify the gap between finite-sample and asymptotic guarantees more systematically.** The paper's theoretical guarantees are asymptotic; a finite-sample analysis (even empirical) of how estimation error propagates through the eigendecomposition to the final parameters would be valuable.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|-----------|
| `/home/wg25r/review_agent/human_reviews_2026/1GkzDABbME.md` (LDS + Tensor-EM) | 5.00 | Similar methodological approach (tensor + spectral for latent variable models) with stronger real-data validation; this paper has weaker empirical validation but comparable theory quality. |
| `/home/wg25r/review_agent/human_reviews_2026/tHmiydOQhn.md` (Spectral Bellman Method) | 6.00 | Stronger empirical results and cleaner experimental design; this paper's experiments are narrower but its theoretical contribution is distinct and honest about limitations. |
| `/home/wg25r/review_agent/human_reviews_2026/kxzYGDL4fY.md` (POMDP State Entropy) | 4.00 | Comparable in scope — both tackle POMDP representation problems with limited-scale experiments. That paper was accepted as poster despite benchmark concerns. |
| `/home/wg25r/review_agent/human_reviews_2026/zbRh0eSl7Q.md` (POMG value iteration) | 4.50 | Pure theory paper with minimal empirics; rejected. This paper has stronger empirical support but a narrower theoretical contribution. |
| `/home/wg25r/review_agent/human_reviews_2026/8jYuRCHYxv.md` (Missingness-MDPs) | 3.00 | Weaker in both theory and experiments; this paper is significantly stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/baqHtQDaIK.md` (Spectral Decomposed VI) | 2.67 | Much weaker and more confused contribution; this paper is clearly better. |

The paper makes a genuine theoretical contribution (connecting PSRs and tensor methods with a relaxed assumption), states its limitations honestly, and provides reasonable empirical support for parameter convergence. However, the central practical claim (reward specification via explicit likelihoods) is only weakly supported: the experiments are on tiny custom domains, require massive data, and do not test the nontrivial-partition case that the method's own theory identifies as the key challenge. The method also fails without explanation on larger POMDPs and scales exponentially in the observability length. Relative to the anchors, the contribution sits between the 5.00-level (solid methodology paper with adequate empirics) and the 4.50-level (modest contribution with weak validation).

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>