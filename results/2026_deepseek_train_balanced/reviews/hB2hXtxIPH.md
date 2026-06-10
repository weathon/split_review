## Summary

This paper proposes Greedy Sequential Execution (GSE), a cooperative MARL method that jointly addresses homogeneous tasks (agents need similar actions) and heterogeneous tasks (agents need distinct actions). GSE introduces a value decomposition using utilities that depend on all other agents' actions $Q_c^i(\tau_i, u_i^-, a_i)$ and a theorem showing this satisfies the IGM principle. Since this form cannot be executed directly, the paper proposes sequential execution with a greedy marginal contribution as credit assignment target, approximating the optimal actions of later agents via a combination of behavior-policy greedy actions and Monte Carlo sampling. The method is evaluated on Multi-XOR, MAgent, and Overcooked environments against QMIX, MAVEN, CDS, and a Shapley-value baseline.

## Strengths

- **Consistent empirical advantage in mixed-task scenarios.** Across five MAgent tasks (Figure 4) and three Overcooked maps (Figure 5), GSE consistently outperforms all baselines in scenarios requiring both homogeneous and heterogeneous cooperation. The advantage is most pronounced in settings where baselines collapse to conservative (lazy) policies. This provides genuine evidence that the approach addresses a real limitation of prior methods.

- **Ablation evidence supporting both key components.** Figure 6 shows that (a) removing the greedy action estimate degrades performance, confirming its role in overcoming relative over-generalization, and (b) removing the marginal contribution target also degrades performance, confirming that the sequential execution policy cannot simply be trained via direct Q_tot fitting. These ablations concretely demonstrate that both components of the method contribute.

- **Clean diagnostic environment.** The Multi-XOR game (Section 5) cleanly isolates homogeneous, heterogeneous, and mixed challenges in a controllable one-step setting. The results show MAVEN succeeds on the homogeneous variant, CDS succeeds on the heterogeneous variant, and only GSE succeeds on the mixed variant — cleanly illustrating the paper's core thesis.

- **Scalability check.** The ablation with doubled/tripled agent counts (Figure 6, fourth plot) provides evidence that performance does not sharply degrade with larger agent groups, addressing a natural concern about sequential methods.

## Weaknesses

### Fatal
None.

### Major

- **No statistical reporting across the entire empirical evaluation.** All learning curves in Figures 3, 4, 5, and 6 are presented as single trajectories with no error bars, confidence intervals, or any indication of variance across random seeds. The paper states results qualitatively ("our method outperforms," "most methods converge to conservative policy") but never quantifies the reliability or significance of the advantage. This is a critical omission for an empirical paper at a top venue — the reader cannot distinguish systematic improvement from a lucky run.

- **Theorem 4.1 is presented as a theoretical contribution but is not substantive.** The theorem states that there exists a decomposition $Q_c^i(\tau_i, u_i^-, a_i)$ satisfying IGM for any $Q_{tot}$. Since $Q_c^i$ conditions on $u_i^-$ (all other agents' actions), the IGM condition is essentially tautological — if each agent knows everyone else's actions, the joint argmax trivially decomposes. The paper itself acknowledges this limitation ("cannot be directly used as the policy's value function," Section 4.2), yet the theorem is positioned with weight it does not carry (abstract: "proves that a value decomposition ... can represent the value decomposition given any reward function"). The value of the paper lies in the practical sequential execution approximation, not in this theoretical claim.

### Minor

- **The Overcooked evaluation narrows the baseline set post-hoc without a clear protocol.** The paper states "we compared our method with MAVEN and CDS as they represent methods that can handle complex homogeneous and heterogeneous tasks, respectively" — this justification appears only in the results section. QMIX and the Shapley baseline, which were evaluated on MAgent, are excluded from Overcooked. The paper would be stronger if the same baseline set were applied consistently across all environments, or if the selection criteria were pre-specified.

- **The derivation in Section 3.1 (Eqs. 4–5) is underspecified.** Variables $r_1$, $r_2$, and $p_b$ are introduced without a clear connection to the payoff matrices in Figure 1. The derivation of the inequality $\frac{r_1}{r_2} < \frac{2p_b - 1}{1 - p_b}$ is not walked through, making it difficult for the reader to verify the claimed trade-off. For a motivating analysis that frames the paper's entire approach, this should be clearly spelled out.

- **The approximation of $a_{i+1:n}^*$ via Monte Carlo sampling is unanalyzed.** The method approximates the optimal latter-agent actions by taking the max over $M$ random joint actions plus the behavior-policy greedy actions. The ablation (Figure 6, third plot) shows that $M=5$ suffices for the tested environments, but there is no discussion of how $M$ should scale with the number of agents, nor any analysis of whether this sparse search reliably estimates the true optimum. As the number of agents grows, the joint action space grows exponentially and $M=5$ becomes an increasingly poor search.

- **The monotonic mixing network used with $Q_c^i$ is architecturally unmotivated.** Section 4.1 states that $Q_c^i$ are combined through "a monotonic mixing network similar to QMIX." But if $Q_c^i$ already captures all interaction information (including other agents' actions), restricting the mixing network to monotonic functions is an odd choice that could limit representational capacity. The paper does not justify this design decision or ablate the choice of mixing architecture.

- **No reporting of computational cost.** The Monte Carlo sampling procedure (M random joint actions per agent per step) could add significant computational overhead relative to baselines. Training time, wall-clock speed, or sample efficiency comparisons are not provided, making it difficult to assess the method's practicality.

### Trivial

- The paper does not discuss sensitivity to execution order (e.g., randomized or learned ordering), which is a natural question for a sequential method.
- Figure captions are minimal and do not describe what is plotted (return? success rate?).

## Nice-to-Haves

- **Additional baselines for non-monotonic settings** (e.g., QTRAN, QPLEX, WQMIX) and **role-based heterogeneous methods** (e.g., RODE, ROMA) would strengthen the evaluation, though MAVEN and CDS already cover the two main categories the paper aims to unify.
- **Disentangling the sources of improvement.** An ablation comparing GSE against a non-sequential version using the same credit assignment would isolate whether the sequential execution structure itself drives the gains, or primarily the greedy marginal contribution.
- **Analysis of learned agent behaviors** (e.g., visitation patterns, policy visualization) in MAgent/Overcooked would help build intuition for why GSE succeeds where baselines fail.

## Removed Points

These points were flagged for removal with justifications:

- **"Circular dependency in the greedy marginal contribution definition"**: The reviewer claimed $\phi_i^*$ is defined circularly because $a_{i+1:n}^*$ maximizes $\phi_i$, which is the quantity being computed. This is a misunderstanding. The definition is $\phi_i^* = \max_{a_{i+1:n}} [Q_c^i(\cdot, a_{i+1:n}, \cdot) - V_c^i(\cdot, a_{i+1:n})]$, which is a well-defined optimization problem, not a circular definition. The practical challenge of computing this max is a separate concern (retained above as a Minor weakness about the Monte Carlo approximation being unanalyzed).

- **"Agent ID asymmetry biases the comparison"**: The reviewer argued that GSE's sequential order encodes positional information, making the comparison unfair. GSE uses $a_{1:i-1}$ as input (previous actions, not agent identities), which is a fundamentally different inductive bias. The paper explicitly acknowledges the asymmetry and the direction favors baselines (they receive agent ID; GSE does not). This does not bias the comparison against the baselines.

- **"The motivating analysis is only heuristic, not a formal impossibility result"**: The paper presents Section 3 as motivating examples, not as formal impossibility theorems. Criticizing it for not being a formal proof demands a scope the paper never claims.

- **"Claim that 'all other methods fail' is too strong"**: The paper explicitly says "except for MAVEN" when making this claim in both the Multi-XOR and MAgent results. The reviewer's criticism ignores this qualification.

- **"Scalability analysis only at small scale"**: The paper tests doubled/tripled agent counts. Criticizing the absolute scale demands scope expansion beyond the paper's stated evaluation.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the reviews is that the paper's ablation study (Figure 6) functions as a stronger argument than its theorem. The demonstration that removing greedy actions *or* marginal contributions both degrade performance provides causal evidence for the method's design decisions, which is more convincing than the vacuous IGM guarantee of Theorem 4.1. This suggests the paper would benefit from repositioning its contribution: the practical engineering insight (sequential execution + greedy marginal contribution with Monte Carlo search) is the genuine contribution, not the theoretical framing.

## Suggestions

1. **Add error bars.** Report means and standard deviations (or confidence intervals) over at least 5 random seeds for all experiments. This is the single most impactful improvement.
2. **Apply the same baseline set consistently.** Run QMIX and the Shapley baseline on Overcooked, or pre-specify the selection criteria.
3. **Clarify the derivation in Section 3.1.** Walk through the arithmetic connecting the payoff matrices to Eqs. (4–5), or simplify the analysis.
4. **Tone down the claim about Theorem 4.1.** Explicitly acknowledge that it is a sufficient condition under full action information — not a substantive theoretical result — and reposition the paper's novelty toward the practical approximation.
5. **Add an analysis of the Monte Carlo approximation.** Show how the estimated $a_{i+1:n}^*$ correlates with the true max as training progresses, or bound the probability of selecting a suboptimal action.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>