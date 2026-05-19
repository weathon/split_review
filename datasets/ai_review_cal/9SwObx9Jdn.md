- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 5, 3
Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

This paper proposes a "midpoint tree" framework for learning to generate geodesics on manifolds where only local (infinitesimal) metric information is available. Instead of generating paths sequentially (which suffers from sparse rewards), the method trains an actor-critic pair: the actor predicts midpoints between endpoint pairs, and the critic predicts distances. Paths are constructed by recursively inserting midpoints. The paper provides theoretical justification (Propositions 1–3) showing that if the actor-critic pair satisfies certain functional equations, they converge to the true geodesic midpoints and distances. Experiments on five diverse environments (Matsumoto metric, car-like constraints, 2D obstacles, 7-DoF robotic arm, three-agent collision avoidance) show that the method outperforms sequential RL (PPO) and a policy-gradient baseline on the harder tasks.

## Strengths

- **Theoretical motivation for why midpoints are necessary**: Proposition 1 and Remark 1 prove that using an argmin of squared sums (midpoint property) is required for recovering true geodesics, while simply minimizing a sum of distances can lead to biased generation. The "Inter" ablation (predicting arbitrary intermediate points) experimentally confirms this: success rates decrease with training in multiple environments (Figure 2). This tight coupling between theory and ablation is strong evidence for the paper's core insight.

- **Actor-critic algorithm with explicit geometric losses**: Algorithm 1 defines a practical training procedure with a clear structure. The actor loss (Eq. 13) directly instantiates the midpoint condition via a squared-sum term, augmented with a smoothness term derived from the four-point relation and an optional symmetry term. This design is cleanly motivated by the theoretical analysis.

- **Empirical success on hard, high-dimensional tasks**: The proposed method achieves the highest success rates in the unidirectional car-like environment (~80% for Our-C), the 7-DoF robotic arm environment (~80% for Our-T), and the three-agent environment (~60% for Our-C), where sequential RL (Seq) plateaus below ~20% and PG is near 0%. These are non-trivial planning domains with asymmetric metrics, high-dimensional configuration spaces, or complex collision constraints—precisely the settings where the paper claims an advantage.

- **Rigorous treatment of the Finslerian setting**: Proposition 3 proves that the function C defined via coordinate-space linearization (Eq. 14) satisfies Assumption 1 (local approximation of the distance), formally connecting the theoretical framework to differential geometry. The obstacle handling extension (Section 4.5) also preserves these properties, making the method applicable to global planning.

- **Honest acknowledgment of limitations**: The conclusion (Section 6) explicitly states that convergence conditions are not established, that the continuous midpoint property may only hold locally, and that depth scheduling remains heuristic. This transparency strengthens the paper.

## Weaknesses

### Major

- **Gap between the theoretical iterative construction and the practical algorithm**: Section 3.3 describes an iterative procedure using a *series* of actors π_i and critics V_i, with convergence guarantees under equicontinuity assumptions (Proposition 2). The actual algorithm (Algorithm 1) trains a *single* actor and critic with a depth-scheduling heuristic to approximate this series. The paper honestly acknowledges this gap ("we were not able to discuss the conditions under which iterations converge," "the continuous midpoint property may only be satisfied locally"), but the consequence is that the theory provides a *justification* for midpoint prediction rather than *guarantees* for the learning procedure. The paper would be significantly stronger by either (a) showing that under specific conditions the single-network depth-scheduling scheme approximates the iterative fixed point, or (b) providing a simple verification experiment (e.g., on a known manifold) that the learned V and π converge to the true distance and midpoint functions.

### Minor

- **Success rate as primary metric does not directly measure geodesic quality**: The main result (Figure 2) reports success rates defined as all adjacent waypoints having C-value ≤ ε. This measures feasibility and local length control but not whether the generated path is near-minimal length. The paper explains this choice (Section 5.2: "metrics are only defined locally and lengths thus cannot be calculated unless the success condition is satisfied") and does provide winning-rate path-length comparisons in the appendix (Table 3), but relegating this to the appendix understates the geodesic quality evidence. Presenting a path-length-normalized metric in the main paper would make the central claim ("generation of geodesics") more directly supported.

- **The PG baseline is too weak to be informative**: The policy gradient baseline (PG) fails on nearly all tasks and environments, including failing "to even generate a smooth curve" in the simplest environment. The paper attributes this to possibly undertrained policies or instability without a critic. While the comparison to sequential RL (PPO, a mature algorithm) is meaningful, the near-total failure of PG means it adds little evidential value—the gap over a collapsing baseline is not a strong result.

- **Seq baseline uses a hand-designed reward function**: The sequential RL baseline's reward (Eq. 15) involves domain-specific engineering that the paper acknowledges "may be possible to improve." The proposed method does not require reward engineering. While this is framed as an advantage of the proposed method, it also means the Seq baseline may not be operating at its full potential, making the comparison somewhat asymmetric.

### Trivial

- No trivial issues identified.

## Nice-to-Haves

- **Comparison with a classical planner** (e.g., RRT*, fast marching, or a shooting-based geodesic solver) for the low-dimensional environments would contextualize the RL-based results and show whether the learned policy is competitive with established non-learning approaches. This is not required for the paper's core claim (which is about *learning* to generate geodesics), but would strengthen the practical impact claims.

- **Computational cost analysis**: Reporting wall-clock time per training run or per evaluation call would help assess practical feasibility, especially since the method calls C (and the actor) many times per path generation.

- **Critic prediction error analysis**: The paper does not evaluate how well V_ϕ approximates true distances (or Monte Carlo estimates thereof), which is central to the actor-critic approach. A plot of critic prediction error vs. pair distance over the course of training would be informative.

## Removed Points

- **"The paper does not include an ablation that compares actor-critic with policy gradient with a critic but without the midpoint-specific loss terms"** — This is factually incorrect. The "Inter" ablation (Section 5.1) uses the critic V_ϕ with sum-of-V loss instead of squared-sum-of-V loss, directly testing the importance of the midpoint constraint while keeping the critic. This is exactly the requested comparison.

- **"Missing RRT* / FMT* / numerical geodesic solver baseline" as a required comparison** — The paper's contribution is about *learning* a policy that generalizes across endpoint pairs, which is a fundamentally different setting from one-shot classical planners. The paper's comparisons against other learning-based methods (Seq via PPO, PG) are appropriate for its stated scope. This point is moved to Nice-to-Haves as a suggestion for strengthening.

- **"The paper would be significantly stronger if it reported normalized path length relative to the optimum...as a primary metric, rather than relegating it to an appendix"** — This is a fair suggestion (kept as Minor above), but the paper does provide path-length winning-rate tables in the appendix and explains why success rate is the primary metric (distance cannot be computed for failed generations). The criticism is maintained in weakened form.

- **Speculative concerns about convergence**: The harsh critic's comments about whether the method could converge to wrong functions are based on the paper's own stated limitations (Section 6), not on specific evidence. These are already covered by the Major weakness about the theory-algorithm gap.

- **Generic strengths from the Strength Finder that lack concrete evidence**: All six identified strengths are specific, evidence-grounded, and retained.

## Novel Insights

The reviews surface a tension that the paper itself acknowledges but does not fully resolve: the theoretical analysis (Proposition 2) assumes an iterative construction with a series of functions and an equicontinuity condition, while the practical algorithm uses a single network with depth scheduling. The paper's framing as a *justification* for midpoint prediction (rather than a convergence analysis) is reasonable, but the strength of the claims in the abstract ("prove the soundness") leans more heavily on the theory than the experiments alone would warrant. A novel observation from synthesizing the reviews is that the paper's strongest evidence comes not from the formal theory but from the combination of (1) the theoretical argument that midpoints are necessary (Remark 1) and (2) the experimental confirmation that the "Inter" variant (arbitrary intermediates) fails while the midpoint variant succeeds. This two-pronged case is more compelling than either component alone, and future work in this direction could profitably focus on tightening the convergence link.

## Suggestions

- Present the path-length winning-rate results (currently in Appendix, Table 3) more prominently in the main paper, either as a secondary figure or a summary sentence in Section 5.4.
- Add a brief paragraph after Proposition 2 explicitly connecting the iterative construction to the single-network algorithm, explaining why the depth-scheduling heuristic approximates the series (as the authors do briefly in Section 5.1 but could expand).
- Consider adding one classical planning baseline (e.g., RRT* for the obstacle environments) to anchor the absolute difficulty of the tasks and provide a reference point for the learned policy's performance.
- Report critic prediction error over training to demonstrate that the distance estimates are improving as intended.
