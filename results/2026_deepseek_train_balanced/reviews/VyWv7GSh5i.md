## Summary

This paper presents VLB-IRL, a variational inference approach to inverse reinforcement learning. The method derives a lower bound on the log-likelihood of expert trajectories from a probabilistic graphical model with an optimality node, showing that optimizing this bound w.r.t. the reward is equivalent to minimizing reverse KL divergence between an approximated optimality distribution conditioned on reward and the true optimality distribution conditioned on state-action pairs. Experiments on MuJoCo benchmarks and Assistive Gym environments compare VLB-IRL against GAIL, AIRL, $f$-IRL, EBIL, and IQ-Learn.

## Strengths

- **Principled PGM-based derivation of an IRL objective.** The paper constructs a probabilistic graphical model explicitly embedding the reward and optimality variables, and derives a variational lower bound on the trajectory log-likelihood from first principles. The derivation is mathematically valid (contrary to one reviewer's claim — see Removed Points). This PGM framing is genuinely absent from prior adversarial IRL methods, which are typically motivated by GAN-based cost learning rather than probabilistic inference.

- **Strong results on Assistive Gym.** VLB-IRL is the only method achieving positive mean returns on all three assistive robotics tasks (FeedingSawyer: 88.11 ± 52.95, BedBathingSawyer: 10.86 ± 13.94, ScratchItchSawyer: 11.94 ± 24.44), while every baseline (GAIL, AIRL, $f$-IRL, IQ-Learn) produces consistently negative returns. This is a genuine differentiator in a realistic, goal-based setting where most prior methods fail entirely.

- **Consistent (though marginal) improvement on all five optimal MuJoCo domains.** VLB-IRL is the only method bolded as statistically best (t-test, α=0.01) on all five domains in Table 1, including LunarLander (267.99 vs next-best 255.58), Hopper (3588.41 vs 3523.88), Walker2d (4779.76 vs 4719.93), HalfCheetah (9677.64 vs 9618.82), and Ant (5422.10 vs 5321.00). No baseline achieves this across all tasks.

- **Formal bound connecting reward variance to approximation quality.** Theorem 2.3 provides a bound on the approximation error when using $q(\mathcal{O}_t \mid \mathbb{E}[r_t])$ to approximate $p(\mathcal{O}_t|s_t,a_t)$ in terms of $\mathrm{Var}[r_t]$, offering a principled justification for why low-variance reward estimates enable reliable optimality approximation.

## Weaknesses

### Fatal
None.

### Major

None. The core weaknesses are at the minor level — no single issue invalidates the paper's contribution.

### Minor

- **Theorem-to-algorithm gap in the approximation error bound.** Theorem 2.3 bounds the error of $q(\mathcal{O}_t \mid \mathbb{E}[r_t])$ approximating $p(\mathcal{O}_t|s_t,a_t)$, but the algorithm uses $q(\mathcal{O}_t \mid r_t)$ with a *sampled* reward value (line 182). The paper acknowledges this (line 222: "if the variance of $r_t$ is small enough, then we can use $r_t$ to estimate $\mathbb{E}[r_t]$"), but provides no empirical verification that reward variance is indeed small in practice, nor any analysis of when this approximation breaks down. A direct empirical check (e.g., reporting $\mathrm{Var}[r_t]$ during training) would substantially strengthen the paper.

- **Marginal performance gains on standard MuJoCo benchmarks.** The improvements over the best baseline on optimal-expert MuJoCo tasks range from 0.6% (HalfCheetah) to 1.9% (Ant). On Walker2d and HalfCheetah, the 1σ confidence intervals overlap with the best baseline's. With only 5 random seeds and no reported confidence intervals beyond standard deviation, the statistical significance of these small margins is questionable. The paper's claim of "improved learning performance" (contribution 3) is technically true but overstated relative to the magnitude of improvement.

- **Noisy trajectory generalization is mixed.** On 2 of 5 noisy-trajectory tasks (LunarLander and Walker2d), VLB-IRL underperforms the noisy expert (237.61 vs 240.60 and 3694.82 vs 3873.86). The paper's claim of "comparable or higher reward on average" (line 327) is accurate for LunarLander but generous for Walker2d (~4.6% below). The broader claim that "previous IRL techniques fail to generalize well when noisy trajectories are provided" (line 352) is supported on 3 of 5 tasks; the failures on the other two should be discussed.

- **Algorithm details are underspecified.** Algorithm 1 does not specify which RL algorithm is used for the policy update step (line 6), the frequency of policy vs. reward updates, optimization hyperparameters, reward network architecture, or how $\mathrm{Var}(r_t)$ is estimated (over which samples?). The experiment section mentions TD3 and PPO, but the mapping between these and specific algorithm steps is unclear. These details are necessary for reproducibility. No code release is mentioned.

- **Missing baselines on LunarLander.** In Table 1, $f$-IRL and IQ-Learn have missing entries for LunarLander. In Table 2, AIRL and IQ-Learn are missing for the same domain. This makes it impossible to compare all methods on all tasks.

- **No ablation study.** The method combines three components: the classifier $C_{\bm{\theta}}$, the advantage-based $q(\mathcal{O}_t|r_t)$, and the variance penalty $\lambda \mathrm{Var}(r_t)$. Without an ablation, it is unclear which components drive the performance. This is particularly relevant given the marginal gains on standard benchmarks — ablations would clarify whether the complex variational machinery is necessary or whether a simpler heuristic suffices.

### Trivial

- The paper presents two graphical models (Figure 1) but only the model without $V_t$ is used in the core derivation. The value-based model appears only in the heuristic construction of the advantage-based optimality function (line 196–205). The exposition would be clearer if this were explicitly connected earlier.

## Nice-to-Haves

- Measure reward recovery quality directly (e.g., correlation with true reward, comparisons of learned reward functions against ground-truth), not just downstream policy performance. This would directly test whether the method succeeds at its stated goal of reward learning.
- Run more random seeds (e.g., 10–20) and report proper confidence intervals (95% bootstrap CIs) and pairwise significance tests with corrections for multiple comparisons, especially given the small performance gaps on MuJoCo.
- Add an ablation study isolating the contributions of the classifier, the advantage-based optimality, and the variance penalty.
- Verify empirically that reward variance is small enough for $q(\mathcal{O}_t|r_t)$ to approximate $q(\mathcal{O}_t \mid \mathbb{E}[r_t])$ reliably, as assumed in the connection between Theorem 2.3 and the algorithm.

## Removed Points

The following points from the inputs were removed after verification against the paper:

- **"Derivation is mathematically invalid / structural flaw."** The critic claimed that introducing $q(\mathcal{O}_t|r_t)$ after marginalizing out $r_t$ is invalid because "the numerator does not depend on $r_t$ while the denominator does." This is incorrect: the expression $\frac{p(\mathcal{O}_t|s_t,a_t)}{q(\mathcal{O}_t|r_t)} q(\mathcal{O}_t|r_t) = p(\mathcal{O}_t|s_t,a_t)$ is algebraically valid for any positive $q$ — the $r_t$ dependence cancels. Multiplying an integral by $q/q=1$ and applying Jensen's inequality to obtain a lower bound is a standard mathematical operation. The derivation is unconventional for variational inference but not invalid. (The critic's category-error framing is itself a misunderstanding of the algebra.)

- **"Theorem 2.4 does not connect to algorithm because algorithm never achieves identity."** Every KL-based method characterizes the optimum theoretically without reaching it exactly. This is standard practice and not a weakness.

- **"Two graphical models are confusing."** The V_t model feeds into the advantage-based optimality construction (Section 2.3). This connection is present in the paper.

- **"Unclear why instant-reward optimality is presented."** The paper explicitly states it "is not sufficient" (line 188) and adopts the advantage form. This is clear exposition, not a flaw.

- **"AIRL forward-KL claim is presented as fact despite dispute."** The paper mentions the dispute at line 416 ("this has been disputed by \citet{firl2020corl}"). The critic's concern is already addressed.

- **"Abstract claims about unknown dynamics are unsupported."** The abstract mentions "unknown dynamics" as a general challenge in the field, not as a claim addressed by this paper.

- **"Noisy expert construction conflates noise with suboptimality."** Using a weaker RL algorithm (A2C/PPO) to generate suboptimal trajectories is a reasonable and commonly used approach for constructing "noisy" demonstrations. The paper explicitly describes this (line 327).

- **Critic's claim about Ant overlap being "No":** Actually, VLB-IRL (5422 ± 83, 1σ range [5339, 5505]) and GAIL (5321 ± 27, 1σ range [5294, 5348]) do overlap at [5339, 5348]. The critic's own numbers contradict their claim.

- **Pure formatting/style nitpicks and missing appendix/proof complaints** removed per hard rules.

## Novel Insights

The most interesting observation from cross-referencing the reviews is the contrast between the critic's confident dismissal of the derivation as "invalid" and the actual algebra showing it is mathematically sound. This error highlights a broader pattern: the critic's strongest claims (fatal derivation flaw, theorem-algorithm disconnect) rest on misinterpretations rather than genuine weaknesses. The paper's real limitations are more mundane — small empirical margins, incomplete ablation, and loose theory-algorithm connection — none of which are fatal. The Assistive Gym results emerge as the single strongest piece of evidence, which is notably underweighted by the harsh critic relative to the MuJoCo results.

## Suggestions

1. **Address the theorem-algorithm gap empirically.** Report the empirical variance of $r_t$ during training to justify the connection between Theorem 2.3 (about $\mathbb{E}[r_t]$) and the algorithm (which uses sampled $r_t$). If variance is small, this validates the theory. If not, the paper should acknowledge this limitation.

2. **Add an ablation study.** Disentangle the contributions of (a) the GAIL-style classifier, (b) the advantage-based $q(\mathcal{O}_t|r_t)$, and (c) the variance penalty $\lambda \mathrm{Var}(r_t)$. Without this, it is unclear what the variational lower bound framework adds beyond existing adversarial IRL methods.

3. **Provide full reproducibility details:** specify the RL algorithm used for the policy update step, optimizer and hyperparameters, reward network architecture, how $\mathrm{Var}(r_t)$ is estimated, the inner-loop RL steps per outer-loop IRL iteration, and release code.

4. **Report proper confidence intervals** (95% bootstrapped or t-based) and significance tests, especially given the small performance gaps on MuJoCo (0.6–1.9%). With only 5 seeds, the claim of statistical best via t-test (Table 1 caption) may not be robust.

5. **Discuss the two noisy-trajectory failures** (LunarLander, Walker2d) explicitly rather than summarizing with "comparable or higher reward on average." A direct analysis of why the method underperforms the noisy expert on these domains would strengthen the paper.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>