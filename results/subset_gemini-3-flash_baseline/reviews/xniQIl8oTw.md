## Summary
The paper introduces CORectifier, a novel training paradigm for Neural Combinatorial Optimization (NCO) that hybridizes Reinforcement Learning (RL) and Imitation Learning (IL). To address the common RL issues of reward sparsity and ineffective exploration in large action spaces, the authors propose a "rectification" mechanism where segments of a model-generated trajectory are probabilistically replaced with high-quality segments from reference solutions. This hierarchical supervision operates at the batch, instance, and sub-instance levels, allowing the model to escape local optima while maintaining the sequential decision-making flexibility of RL.

## Strengths
- **Originality and Hybridization**: The paper presents a well-motivated bridge between RL and IL/SL. Unlike vanilla IL which forces the model to follow a static template, the proposed rectification allows for "interleaved" exploration, where the model can learn from expert sub-trajectories while still exploring the state space.
- **Strong Empirical Performance**: The method demonstrates significant improvements over established RL baselines (AM, POMO, Sym-NCO) across five different COPs (TSP, ATSP, PCTSP, CVRP, KP). The reduction in the optimality gap on TSP-500 (up to 89.8% improvement over RL baselines) is particularly impressive.
- **Generalization and Scalability**: The paper provides evidence of strong zero-shot generalization on real-world benchmarks like TSPLIB and CVRPLIB, outperforming specialized models. It also successfully scales RL-based solvers to 500-node instances, a known bottleneck for the RL4CO community.
- **Versatility**: The authors demonstrate that CORectifier can be applied as a "plug-in" to various backbones (AM, POMO, MatNet), suggesting broad utility for the NCO community.

## Weaknesses
### Fatal
None.

### Major
- **Reliance on High-Quality Labels**: While the paper frames this as a hybrid approach, the performance gain is heavily dependent on the availability of oracle solutions (Concorde, LKH-3, HGS). In scenarios where such oracles are computationally prohibitive or unavailable (the very reason we often seek NCO solvers), the "rectification" signal disappears. The paper would benefit from a discussion or experiment on how the model performs when the "expert" data is of mediocre quality (e.g., from a fast but sub-optimal heuristic).
- **Computational Overhead of Training**: The rectification process involves retrieving successor actions from reference tours and performing feasibility checks during the training loop. While the authors provide inference times, a more detailed analysis of the training time overhead compared to vanilla RL (POMO/AM) is missing.

### Minor
- **Hyper-parameter Sensitivity**: The tri-level rectification introduces several new hyper-parameters ($p_{batch}, p_{inst}, \alpha, \beta$). Although the authors provide a sensitivity study in Figure 5 and Table 6, the optimal settings seem to vary significantly between tasks (e.g., ATSP requires much higher rectification probabilities than TSP). This might make the method harder to tune for new, unseen COPs.
- **Baseline Comparison**: While the paper compares against many SL and RL methods, it omits some very recent hybrid or "search-based" NCO methods that might provide a tighter competition in the 500+ node range, though the current comparison is already quite extensive.

### Trivial
None.

## Nice-to-Haves
- An analysis of the "Rectification Success Rate": How often does the feasibility check (Eq. 10) fail during training? This would provide insight into how well the expert trajectories align with the states reached by the RL agent's exploration.

## Novel Insights
The core novel insight is the "Intra-instance" rectification mechanism. By treating expert solutions as decomposable signals rather than rigid templates, the authors show that a single optimal tour can provide an exponential number of "guiding fragments." This effectively solves the data efficiency problem in SL-based NCO and the exploration problem in RL-based NCO simultaneously. The observation that injecting random-length expert segments at random steps leads to higher trajectory entropy (Fig 6) is counter-intuitive but suggests that expert guidance, when applied stochastically, actually prevents the policy from collapsing into a few narrow modes.

## Suggestions
- Include a "Training Time" comparison table in the final version to quantify the overhead of the rectification logic.
- Conduct a "Robustness to Expert Quality" experiment where the reference solutions are intentionally degraded (e.g., using a 1-opt or 0.9-optimal solver) to see if the RRL paradigm still provides a boost over vanilla RL.

## Score and Decision
The paper is a strong contribution to the NCO field. It addresses a fundamental limitation of RL solvers (scalability and exploration) with a technically sound and empirically validated method. The results on large-scale instances (TSP-500) and the cross-task validation make it a valuable addition to ICLR.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>