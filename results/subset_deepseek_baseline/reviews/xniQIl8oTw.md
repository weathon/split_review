## Summary
This paper proposes CORectifier, a novel learning paradigm for Neural Combinatorial Optimization (NCO) that hybridizes Reinforcement Learning (RL) with supervised/imitation learning through a "rectification" mechanism. During training, segments of policy-generated trajectories are probabilistically replaced with high-quality segments from reference solutions at batch, instance, and intra-instance levels, addressing RL's reward sparsity and sample inefficiency. The method achieves substantial improvements over both RL-based and SL-based baselines across TSP, ATSP, PCTSP, CVRP, and KP, with particular gains in scalability to larger problem instances.

## Strengths
- **Novel and well-motivated approach**: The rectified RL paradigm offers a principled way to inject expert guidance into RL training for CO without sacrificing the sequential decision-making flexibility that makes RL attractive for constraint-rich problems. The hierarchical (batch/instance/intra-instance) design is thoughtful and addresses a genuine limitation of prior hybrid approaches.
- **Comprehensive empirical evaluation**: The paper evaluates across 5 CO problems (TSP, ATSP, PCTSP, CVRP, KP) with multiple scales (up to 500 nodes), includes comparisons against both RL-based and SL-based methods, and provides generalization tests on real-world benchmarks (TSPLIB, CVRPLIB). The ablation studies, hyperparameter analyses, and diversity/stability analyses are thorough.
- **Strong and consistent results**: CORectifier achieves up to 59.7% performance gains over RL baselines and 26.5% over SL baselines, with particularly impressive scalability improvements (89.8% gap reduction on TSP-500). The method consistently outperforms prior RL-based approaches across all tested problems and scales.
- **General applicability**: The framework is demonstrated to work with multiple backbone architectures (POMO, MatNet, AM) and extends beyond routing problems to KP, suggesting broad utility.

## Weaknesses
### Fatal
None.

### Major
- **Limited novelty relative to existing hybrid approaches**: The core idea of interleaving expert demonstrations with RL exploration has been extensively explored in robotics (e.g., GAIL, DAGGER, Hindsight Experience Replay) and sequential prediction (scheduled sampling, professor forcing). While the paper acknowledges some of these connections, it does not clearly articulate what is fundamentally new about the proposed rectification mechanism beyond applying existing ideas to CO. The "hierarchical" aspect (batch/instance/intra-instance) is primarily a hyperparameter configuration rather than a structural innovation.
- **Theoretical justification is weak**: The paper claims a "conceptual proof sketch" in Appendix G but does not provide rigorous theoretical guarantees for why rectification improves learning. The claim that expert trajectories satisfy a quality margin (Eq. 4) is tautological—it simply asserts that expert solutions are better than random policy samples. There is no analysis of bias introduced by rectification, convergence properties, or how the method avoids learning to rely on expert segments rather than improving the policy itself.
- **Comparison fairness concerns**: The paper compares against heatmap-guided SL methods that use greedy decoding without search, while many of these methods achieve much better results with beam search or Monte Carlo Tree Search. The claim of "26.5% gains over SL-based baselines" is misleading when the comparison is against SL methods operating in a different regime (heatmap prediction vs. sequential decision). A fairer comparison would evaluate all methods under similar decoding budgets.

### Minor
- **The two-stage training pipeline is not fully justified**: The IL pre-training stage is described as "optional" but the ablation study shows mixed results—on PCTSP, the version without IL pre-training actually performs better (3.407% vs 3.593%). The paper does not provide clear guidance on when to use IL pre-training versus when to skip it.
- **Hyperparameter sensitivity is under-explored**: While Figure 5 shows stability across p_batch and p_inst values, the paper does not investigate interaction effects between these parameters. The cosine-annealing scheduler for rectification parameters adds complexity without clear evidence that it outperforms fixed schedules.
- **The "first NCO attempt to explore synergy between RL and SL/IL" claim is overstated**: Prior work such as BQ-NCO (Drakulic et al., 2023) and GOAL (Drakulic et al., 2025) already explored supervised learning for sequential decision CO solvers, and methods like DAGGER have been applied to CO. The paper should more carefully position its contribution relative to these existing hybrid approaches.

### Trivial
- The paper uses "Beto et al., 2023" as a citation for Sym-NCO in Table 1, but the correct author is Kim et al., 2022 (as cited elsewhere). This appears to be a citation error.
- Some table formatting issues (e.g., "Beto" instead of "Kim" in Table 1, "Dhakal" instead of "Drakulic" in Table 2) suggest careless proofreading.

## Nice-to-Haves
- An analysis of how the quality of reference solutions affects CORectifier's performance would be valuable—the paper claims it degrades to vanilla RL in the worst case, but empirical validation of this claim would strengthen the paper.
- A comparison against DAGGER or similar imitation+RL hybrid methods adapted to CO would help position the contribution relative to existing techniques.
- The paper could benefit from a more detailed discussion of when rectification is most beneficial (e.g., early vs. late in training, for which problem types).

## Novel Insights
None beyond the paper's own contributions. The paper's main insight—that injecting expert segments into RL trajectories can improve sample efficiency for CO—is a useful application of existing ideas from imitation learning and scheduled sampling, but does not reveal fundamentally new understanding about combinatorial optimization or reinforcement learning.

## Suggestions
- Clarify the novelty of the rectification mechanism relative to existing hybrid IL-RL approaches (e.g., DAGGER, GAIL, scheduled sampling) and provide a clear technical distinction.
- Add a theoretical analysis of the bias-variance tradeoff introduced by rectification, or at minimum provide empirical evidence about how the method affects the policy gradient estimator.
- Include comparisons against heatmap-guided SL methods with search (beam search, MCTS) to provide a more complete picture of relative performance.
- Provide clearer guidance on when to use IL pre-training versus starting directly with rectified RL.

## Score and Decision
The paper presents a well-executed empirical study with a practical method that achieves strong results across multiple CO problems. However, the novelty is incremental—the core idea of mixing expert demonstrations with RL exploration is well-established in other domains, and the paper does not provide sufficient theoretical or methodological innovation to warrant the highest scores. The empirical contributions are solid and the method is clearly useful, but the paper would benefit from more careful positioning relative to existing hybrid approaches and stronger theoretical grounding.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>