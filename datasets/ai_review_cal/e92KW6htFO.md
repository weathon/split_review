- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 3, 6
I have thoroughly read the paper and cross-checked the reviewer claims against the text. Let me now produce the consolidated review.

---

## Summary

This paper identifies underestimation of the cost value function as a key factor behind constraint violations in Constrained RL, and proposes MICE (Memory-driven Intrinsic Cost Estimation). MICE maintains a "flashbulb memory" of unsafe trajectories and augments the cost value update with an intrinsic cost signal computed from the similarity between the current trajectory and stored unsafe experiences. The paper provides theoretical bounds on constraint violations (Theorem 2) and convergence guarantees (Theorem 3), and demonstrates empirically across Safety Gym and Safety MuJoCo that MICE reduces cumulative costs while maintaining or improving reward relative to CPO, PID Lagrangian, Saute, and Simmer.

## Strengths

- **Identification of underestimation bias in CRL cost value functions.** Section 4.1 adapts the classic overestimation argument (Fujimoto et al., Thrun & Schwartz) to cost minimization, demonstrating theoretically and empirically (Figure 2) that cost critics in CPO and PID Lagrangian systematically underestimate true costs. This is a well-grounded observation that clarifies why constraint violations persist in existing methods.

- **Strong and consistent empirical reduction in constraint violations.** Figures 3–4 show that MICE achieves substantially lower cumulative costs than four baselines across four Safety Gym tasks and three Safety MuJoCo tasks, while matching or exceeding baseline reward. In Safety MuJoCo, MICE attains zero velocity-constraint violation. The results use 6 seeds with mean and variance reported.

- **Verifiable correction of underestimation.** Figure 5a–b directly measures the gap between cost value estimates and true values, showing that MICE shifts the estimation error from negative (underestimation) toward zero, while baselines remain negatively biased. This provides direct evidence that the intrinsic cost mechanism corrects the specific bias the paper targets.

- **Theoretical worst-case constraint bound.** Theorem 2 provides an upper bound \(J_C(\pi_{k+1}) \leq d - I + \frac{\sqrt{2\delta}\gamma\epsilon_C^{\pi_{k+1}}}{(1-\gamma)^2}\) that includes a negative intrinsic term \(-I\), formally showing that the intrinsic cost can tighten the violation bound relative to CPO.

## Weaknesses

### Fatal
None.

### Major

- **Ablation study does not isolate the memory component.** The ablation in Figure 6 compares MICE against versions adding constants (5, 10, 15) to the cost value function. This only rules out the trivial hypothesis that any positive offset works—it does not test whether the *memory-driven* nature of the intrinsic cost is responsible for the improvement. The paper claims the intrinsic cost contains "more memory-related and task-related information" (line 218), but the current ablation cannot support this claim. A proper ablation would compare MICE against: (a) a version using a fixed learned (but memory-independent) intrinsic cost, (b) a version with randomly shuffled memory trajectories that break meaningful similarity comparisons, or (c) a version that removes the similarity computation and simply adds a uniform safety bonus to all states. Without such controls, the contribution of the memory mechanism itself remains unvalidated.

- **Causal link between underestimation and violations is asserted but not causally isolated.** The paper states that "underestimation of the cost value function is a key factor in constraint violations" and uses this as the central motivation for MICE. The evidence is: (i) a theoretical argument that minimization bias produces underestimation (Section 4.1), and (ii) a correlation between negative estimation error (Figure 2) and the fact that baselines violate constraints. MICE corrects the underestimation *and* reduces violations, but the experimental design does not rule out alternative explanations—for instance, the intrinsic cost could reduce violations simply by acting as a state-dependent safety penalty that lowers the effective constraint threshold, independent of any bias correction. A controlled experiment that artificially introduces underestimation into a well-calibrated algorithm and measures whether violations increase, or that compares MICE against a method that reduces violations through a different mechanism, would substantially strengthen the causal claim.

### Minor

- **Trajectory similarity metric is not validated.** The intrinsic cost (Equation 3) uses Euclidean distance between the current trajectory and stored unsafe trajectories (with weighting by \(W\)). For high-dimensional continuous state spaces (e.g., Safety Gym's observations), Euclidean distance in raw trajectory space is a weak proxy for semantic similarity. The random projection layer in the generator \(G_\phi\) is mentioned but not described (dimensionality, fixed vs. learned), and the generator's training labels are derived from the same raw Euclidean distance (Equation 5), so any metric weakness is inherited. The paper provides no analysis or visualization to confirm that the distance function reliably identifies trajectories that are genuinely similar to unsafe experiences. If the metric is noisy, the intrinsic cost could produce false alarms (overly conservative policy) or miss hazards.

- **Theory-practice gap acknowledged but not discussed.** Theorem 3 assumes a lookup table, finite MDP, and infinite sampling of every state-action pair—conditions that do not hold in the continuous state/action environments used in the experiments. Theorem 2's bound includes the term \(I = \mathbb{E}[\sum\gamma^t c_t^I]\), which itself depends on the memory that changes over training, so the bound is not directly computable without further characterization of \(I\). The paper does not discuss how function approximation affects the convergence analysis or whether the bound approximately holds in practice. While such theory-practice gaps are common in RL papers, acknowledging them explicitly and providing a brief justification (e.g., citing known results for nonlinear Q-learning) would strengthen the paper.

- **Several implementation details underspecified in the main text.** The following are not specified: the intrinsic discount factor \(\gamma_I\) and how iteration number \(k\) is counted (global step? per episode?), the weight \(\omega\) in Equation 4, the update frequency of the intrinsic generator \(G_\phi\) (every unsafe trajectory? minibatches?), and the dimensionality of the random projection layer. The reproducibility statement (line 231) is truncated by parser issues; if the appendix contains these details the authors should ensure they are complete.

- **Sensitivity analysis on a single environment.** The hyperparameter sensitivity study (Figure 7) is performed only on SafetyCarCircle-v0. While the results are informative, generalizability to other environments is unclear.

### Trivial
None that survive filtering.

## Nice-to-Haves

- A controlled experiment artificially introducing cost underestimation and measuring its effect on violations would strengthen the paper's causal narrative.
- A comparison of training time and memory overhead between MICE and baselines would help practitioners assess the computational cost of the memory module.
- A limitations section discussing scenarios where the method may struggle (e.g., when unsafe trajectories are rare, memory contains few entries, or the Euclidean metric is misleading) would improve the paper's completeness.

## Removed Points

These points were raised in the reviews but are removed for the following reasons:

- **Missing statistical significance tests**: The paper reports mean and standard deviation with 6 seeds (line 204), which is standard practice in the RL community. Demanding formal p-values or significance tests for every comparison is a formatting/style preference, not a substantive weakness.
- **Missing hyperparameter details attributed to incomplete appendix**: The parser strips appendices from all papers. If the original submission contains a complete hyperparameter table and training details in the appendix, this criticism does not apply. (The main-text underspecification noted in Minor Weaknesses is retained because those details should be in the main body for readability.)
- **"Random projection layer" criticism as a reproducibility concern**: The paper mentions the layer (line 94) and cites Zhu et al. (2020) for the technique. The critic's request for exact dimensionality is a trivial implementation detail.
- **Criticism about baseline tuning**: The paper states experiments used "uniform conditions" (line 204–205). Speculating that this disadvantages baselines without evidence is not a concrete weakness.
- **Criticism about missing proof in appendix**: Parser-stripped content; the proof exists in the original submission.
- **Strength from Strength Finder about "theoretical justification for trust-region constraint" (Theorem 1)**: This is a generic bound that applies to any cost advantage, not specific to MICE. It is not a core strength of the paper's contribution.
- **Strength from Strength Finder about "effective sensitivity to constraint thresholds"**: This is a supporting result that confirms a claimed property; it is not among the paper's strongest contributions.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface an observation about the paper that the authors themselves did not make.

## Suggestions

1. **Replace or augment the constant-bias ablation** with comparisons against (a) a version that removes the similarity computation and adds a fixed learned intrinsic cost, (b) a version with randomly shuffled memory trajectories, and (c) a version that uses a non-memory-based safety bonus (e.g., a small positive cost for all state-action pairs visited in any violation episode). These would isolate whether the memory-driven similarity mechanism specifically drives the improvement.
2. **Validate the trajectory similarity metric** by showing a correlation between computed intrinsic cost and actual future violation risk (e.g., plotting intrinsic cost vs. probability of exceeding the cost threshold within the next \(k\) steps), or by visualizing the latent space learned by the random projection layer.
3. **Discuss the gap between the tabular convergence analysis and the function-approximation setting**, referencing relevant results (e.g., nonlinear Q-learning convergence) to clarify the extent to which Theorem 3 applies.
4. **Specify all hyperparameters in the main text or a table** — particularly \(\gamma_I\), \(\omega\), the update schedule for \(G_\phi\), and the projection layer dimensionality.
5. **Tone down the causal claim** from "underestimation is *the* key factor" to "underestimation is *a* key factor that we identify and correct," which is better supported by the evidence.
