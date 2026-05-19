Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper introduces **submodular RL**, a framework where the reward is a submodular set function over the trajectory's visited states (capturing diminishing returns), generalizing standard additive-reward MDPs. It proves an inapproximability result (logarithmic hardness) for the general setting. It proposes **SubPO**, a policy gradient method that uses marginal gains rather than per-step rewards. Under two special cases — an "ε-bandit" MDP (connecting to DR-submodularity, yielding a 1-1/e or 1/2 approximation) and bounded curvature (yielding a (1-c) approximation) — it provides theoretical guarantees. Experiments across six environments (path planning, item collection, experiment design, building exploration, car racing, MuJoCo Ant) show SubPO outperforms a "modular RL" baseline that naïvely maximizes per-state submodular values.

---

## Strengths

1. **Clean formalization of submodular MDPs.** Section 2 defines the SMDP tuple ⟨S, A, P, ρ, H, F⟩ and shows that classical MDPs are a strict special case (additive rewards are modular set functions). This provides a principled framework that unifies additive and non-additive rewards in RL.

2. **Inapproximability result (Theorem 3.1).** The reduction from the submodular orienteering problem proves that even deterministic SMDPs cannot be approximated within Ω(log^{1−γ} OPT) unless NP ⊆ ZTIME(n^{polylog(n)}), ruling out constant-factor approximations in general. This is sound and establishes fundamental limits for the framework.

3. **Unbiased policy gradient estimator for submodular rewards.** Equation (7) derives ∇_θ J(π_θ) = E[ Σ_i ∇_θ log π_θ(a_i|s_i) ( Σ_{j=i}^{H−1} F(s_{j+1}|τ_{0:j}) − b(τ_{0:i}) ) ], a principled extension of policy gradients to submodular objectives via marginal gains, enabling practical stochastic optimization.

4. **DR-submodularity connection under ε-bandit SMDP.** Theorem 5.1 shows that for horizon-dependent policies on ε-bandit MDPs, the objective J(π) is monotone DR-submodular, connecting submodular RL to continuous submodular optimization and yielding constant-factor approximations (1/2 via any gradient-based optimizer, 1−1/e via Frank–Wolfe).

5. **Broad experimental scope across six environments.** The paper demonstrates SubPO on tasks ranging from discrete grid-worlds to high-dimensional continuous control (30D state, 8D action in MuJoCo Ant), showing the framework's versatility.

---

## Weaknesses

### Fatal
None.

### Major

1. **The curvature-based guarantee (Proposition restateboundedC) is insufficiently supported.** The proposition claims that for any tabular SMDP with submodular reward of curvature c, the policy "obtained via SubPO" satisfies J(π) ≥ (1−c) J(π*). The main text provides no proof sketch, deferring entirely to the appendix (which is stripped). Crucially, it does not clarify what "obtained via SubPO" means — does it require convergence to a global optimum? A stationary point? A single gradient step? Since SubPO is a generic gradient ascent algorithm on a potentially non-convex objective, the claimed guarantee is not obvious without additional reasoning about the optimization landscape. This proposition is listed as a core theoretical contribution, yet its grounding is opaque from the main text alone. The authors should either (a) provide a high-level proof sketch showing why the curvature bound transfers through the policy optimization process, or (b) weaken the claim to reflect what can actually be proven.

2. **The experimental comparison relies on a single, deliberately weak baseline.** The only baseline, "Modular RL" (MRL), maximizes Σ F({s}) — which by construction ignores diminishing returns and unsurprisingly gets stuck. Key missing comparisons:
   - For deterministic environments (gorilla, two-room), a greedy rollout baseline (at each step choose the action maximizing immediate marginal gain) would isolate whether the *stochastic policy gradient* adds value over a simple greedy planner.
   - For continuous environments (car racing, Ant), a standard RL method (PPO/SAC) with an additive reward engineered to also incentivize coverage would test whether the submodular formulation is genuinely beneficial or just a different proxy.
   
   Without such baselines, claims that SubPO is "sample efficient" or "scales well" relative to reasonable existing approaches are not supported — the paper only shows SubPO is better than a straw man. The paper acknowledges (line 371–372) that alternative reward functions could work with standard RL, but does not include such comparisons.

### Minor

3. **Theory-practice gap for the DR-submodularity guarantee.** The 1−1/e result (Section 5) relies on a Frank–Wolfe algorithm with tabular policies over a down-closed polytope, whereas the practical SubPO (Algorithm 1) uses vanilla gradient ascent on neural network policies. The paper does note (lines 223–224) that "any gradient-based optimizer" achieves 1/2-optimality for ε-bandit MDPs, so the connection is partially bridged. However, the experiments are not on ε-bandit MDPs, so neither guarantee directly applies to the empirical results. A clearer separation between theoretical algorithm variants (e.g., "SubPO-FW") and the practical algorithm would improve readability.

4. **"Sample efficiency" claim is not quantified.** The paper states SubPOm is more "sample efficient" than SubPOnm (e.g., line 288, 303), but this is only supported by the observation that SubPOm converges in fewer epochs. The number of episodes required to reach a given performance threshold is not reported. All methods use the same number of environment interactions, so the standard notion of sample efficiency (fewer interactions to reach a target) is not meaningfully demonstrated.

5. **The ε-bandit SMDP assumption (Definition 5.1) is very restrictive.** The assumption requires a "nearly deterministic" MDP where each state has a unique action leading to it with 1−ε probability. This is far from general MDP structure. The paper should more prominently state that this is a simplified setting used to connect to DR-submodularity theory, rather than presenting it as a practical scenario.

### Trivial
None of consequence.

---

## Nice-to-Haves

- **Variance analysis of the gradient estimator.** The estimator (Eq. 4) sums products of log-probabilities and marginal gains. A discussion of how variance scales with horizon H and how the baseline helps would strengthen the algorithmic contribution.
- **Ablation on the baseline.** The paper mentions using a baseline b(s) that estimates the cumulative sum of marginal gains (line 369), but does not study its effect. An ablation would help practitioners.
- **Limitations paragraph.** A candid discussion of when SubPO might fail (e.g., when gradient variance is too high, when the submodular function is not easily decomposable into time-ordered marginal gains) would improve the paper's candor.

---

## Removed Points

These points from the inputs were removed with justification:

- **"Curvature proposition is likely incorrect as stated"** (Harsh Critic #1): This claim is based on speculation about what the (stripped) appendix proof might contain. The critic admits "I cannot verify the proof." The paper states the proposition and references the appendix. The criticism that no proof sketch is provided in the main text is retained (Major #1), but the stronger assertion of incorrectness is not verifiable from the paper as written and is removed per the rule: *"If the harsh critic asserts something is 'fatal' or 'structural' but the assertion depends on information not present in the paper, DEMOTE to Minor or REMOVE."*

- **Missing hyperparameters / reproducibility nitpicks** (Harsh Critic's "Missing Parts"): The critic asks for hyperparameter choices, architecture details, etc. The paper states "Experiment details and extended empirical analysis are in the appendix" (line 299). The appendix is stripped by the parser. Per the rules: *"REMOVE nitpicks about reproducibility such as undisclosed hyperparameters"* and *"REMOVE weaknesses about missing appendix."*

- **"Missing related works"** (Strength Finder's suggestion about more related works): Per the rules: *"DO NOT mention missing related works, as you do not have external sources to confirm their existence."*

- **Generic "the evaluation lacks rigor" framing** (Harsh Critic's sweeping criticism): The specific, concrete complaint (only one baseline) is kept as Major #2. The broader assertion of lacking rigor without specific anchors is removed.

- **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem"): Per the rules: *"Drop strengths that are generic, superficial, or lack a specific citation or concrete content."* These are removed. The retained strengths are specific and grounded in the paper's content.

- **Strength Finder's "comprehensive empirical evaluation":** This phrasing is retained (Strength #5) but is qualified by the weakness that only one baseline was compared. The word "comprehensive" is appropriate for describing the breadth of environments, not the baseline coverage.

---

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs largely rephrase or critique the paper's stated claims rather than identifying unexpected connections or missed opportunities that the paper itself does not discuss.

---

## Suggestions

1. **Address the curvature proposition.** Either provide a clear proof sketch (even a few sentences) in the main text explaining why SubPO's policy satisfies J(π) ≥ (1−c)J(π*), or weaken the claim (e.g., specify that the bound holds at a stationary point, or under additional conditions on the policy optimization). As currently stated, the guarantee appears stronger than what the algorithm can reasonably deliver.

2. **Add at least one stronger baseline.** For deterministic environments (gorilla, two-room), include a greedy planner that at each step takes the action maximizing the immediate marginal gain Δ(v|visited). For continuous environments (car, Ant), compare to PPO with a reward = per-step marginal gain increment. This would directly test whether SubPO's stochastic gradient approach adds value beyond simpler alternatives.

3. **Separate the theoretical algorithm from the practical algorithm.** Rename the Frank–Wolfe variant (e.g., "SubPO-FW") and clarify that SubPO in experiments refers to the neural-network gradient-ascent version. Explain that the theoretical insight (marginal gains matter) carries over even when the formal guarantees (1−1/e) do not directly apply to the neural setting.

4. **Quantify sample efficiency.** Instead of "SubPOm is more sample efficient," report the number of episodes to reach, e.g., 90% of the final SubPOnm performance, and compare across methods.

5. **Acknowledge the ε-bandit assumption's restrictiveness more explicitly.** State clearly that this is a toy setting used for theoretical tractability and does not reflect the experimental domains.

---

## Score and Decision

**Calibration procedure:** I made three bracketing queries (scores [0,3], [4,7], [8,10]) on topics related to submodular/non-additive rewards in RL. Round 1 placed the paper in the [4, 6] bracket. Round 2 pulled anchors in [4.5, 6.5] and [3.5, 5.5]. 

**Anchors considered:**

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|--------------------------|
| K42xtH1sqG (Combinatorial Bandits) | 2.67 | R1 | Weaker; narrower problem scope, no submodular RL framework |
| M34Eyawzm5 (SubUrban, submodular RL) | 3.00 | R1 | Weaker; rejected, serious code ethics issue, weaker theoretical grounding |
| OEnIVaoOaI (Fusing Rewards & Prefs) | 3.00 | R1 | Weaker; unrelated technical approach |
| Ua6bRCHRFm (D2C-HRHR) | 3.00 | R1 | Weaker; unrelated problem |
| CwownEMv9z (Policy Gradient for Undiscounted) | 4.00 | R2 | Similar score; theoretical RL paper, comparable depth |
| kWM0etSpBG (GFlowNet) | 4.00 | R2 | Similar; policy-based training but different problem class |
| KFrmUwP6Jx (Mini-batch Submodular) | 3.50 | R2 | Weaker; rejected, marginal contribution |
| **A7v4VgOf3Y (RLVR dynamics)** | **4.67** | **R2** | **Slightly weaker; more narrow focus, rejected** |
| **HIi4lNsvXW (Submodular Max for SCM)** | **5.00** | **R1/R2** | **Comparable; accepted poster, similar theoretical ambition but cleaner experiments. Our paper has broader scope (RL) but weaker baselines.** |
| **swwelQtLRn (DMNL Bandits)** | **5.33** | **R2** | **Comparable; accepted poster, bridges submodularity with bandits, cleaner theory-experiment alignment. Our paper has broader scope (full RL) but less clean execution.** |
| KUlPxDQF3T (Actor-Critic Gradient Flow) | 5.50 | R2 | Stronger theoretical analysis but narrower focus |
| BeMtzSH1d7 (Submodular Min with Dueling Oracle) | 6.00 | R1 | Stronger; cleaner theoretical contribution, accepted |
| TdiRLe3rPA (From Ticks to Flows) | 6.50 | R2 | Stronger; deeper theoretical analysis |

The paper is most comparable to the DMNL Bandits paper (5.33, accepted) and the Submodular Max for SCM paper (5.00, accepted). It has a broader scope than either — introducing a full RL framework rather than a bandit or pure optimization variant — but the verified weaknesses (weak baselines, opaque curvature claim, theory-practice gap) pull it down relative to these anchors. I therefore place it at the lower end of the comparable range.

**Final score: 5.0**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>