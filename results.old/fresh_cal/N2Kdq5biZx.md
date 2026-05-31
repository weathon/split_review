Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper frames offline-to-online (OtO) reinforcement learning as an exploration problem rather than the standard bias-correction problem, and introduces PTGOOD (Planning to Go Out-of-Distribution). PTGOOD uses the Conditional Entropy Bottleneck to estimate the behavior policy's occupancy measure, then employs non-myopic tree search to select actions that are both out-of-distribution relative to the offline dataset and near the improving policy. Experiments on seven continuous-control environment-dataset combinations show PTGOOD achieves the highest returns in all settings (statistically significant in 5/7).

## Strengths

1. **Novel framing and analysis of the OtO problem.** The paper systematically demonstrates (Section 4) that standard online exploration methods have serious compatibility issues in the OtO setting: intrinsic rewards can destroy offline initializations (Figure 1 shows returns collapse from ~7000 to near zero with large λ), and different ensemble types for UCB exploration produce inconsistent uncertainty rankings (e.g., Spearman ρ of -0.67 between Value and Policy in Hopper, Table 1). This analysis is absent from prior OtO work and provides principled motivation for PTGOOD's design.

2. **Consistently strong empirical results.** Table 2 shows PTGOOD achieves the highest average undiscounted returns in all 7 environment-dataset combinations (5/7 statistically significant by Welch's t-test), with substantial margins over baselines in several settings (e.g., Hopper Random: PTGOOD 3246 vs. next-best UCB(T) 2251; Humanoid MR: PTGOOD 15050 vs. next-best UCB(Q) 13183). PTGOOD also avoids the premature policy convergence that many baselines exhibit (Figure 2/3).

3. **Evidence that policy-constraint methods fail with suboptimal behavior policies.** The paper shows Cal-QL, which enforces closeness to the behavior policy, achieves negative or near-zero returns on all Random datasets and performs far below PTGOOD on Medium Replay datasets. This directly supports the paper's decision to forgo constraint mechanisms entirely.

4. **Controlled planning noise ablation (Section 6.4).** The sweep over ε values in two environments provides clear evidence that PTGOOD's "closeness" criterion is essential: both too-small (ε=0.001) and too-large (ε=10) noise degrade performance relative to the optimal intermediate value, validating the design choice to add small noise during planning.

## Weaknesses

### Fatal
None. The paper's core claims (PTGOOD achieves strong returns, constraint mechanisms are unnecessary) are supported by the empirical evidence, even if some supporting analyses are missing.

### Major

1. **Missing ablation to isolate the rate-based OOD signal from the tree search structure.** PTGOOD's planning has two entangled components: a multi-step tree search (width w, depth d) and a rate-based scoring of candidate trajectories. The paper provides no ablation that replaces the rate objective with a uniform or random signal while keeping the tree search identical. The noise-sweep in Section 6.4 tests only the planning noise ε, not the contribution of the OOD rate. Without this ablation, it is unclear whether PTGOOD's gains come from the novel OOD targeting or simply from the multi-step lookahead of the tree search itself. This directly affects the paper's central claim that "planning to go out-of-distribution" drives improvement.

2. **Planning hyperparameters (w, d) are not reported.** Section 5.3 defines the planning tree with width w and depth d but never states what values are used in any experiment. These parameters determine both the computational cost and the effectiveness of PTGOOD's planning, and their omission is a fundamental reproducibility issue. At minimum, per-task values and a sensitivity analysis should be provided.

### Minor

1. **Computational cost of planning is not discussed.** PTGOOD's tree search requires multiple forward passes through the learned dynamics model per environment step (up to w × d model calls), while all baselines sample the policy once per step. The paper never reports wall-clock time, number of model calls, or any computational budget comparison. While this does not invalidate the results (returns are measured per environment step, the standard metric), it makes it difficult for practitioners to assess whether PTGOOD's gains are worth the additional computation. A discussion of the trade-off is needed.

2. **No comparison to a myopic (depth=1) version of PTGOOD.** One of the paper's stated advantages over UCB methods is non-myopic planning, but this claim is not directly supported by an ablation comparing depth=1 vs. depth=d. This would be straightforward to add and would strengthen a central claim.

3. **Missing implementation details.** Several details needed for reproducibility are absent from the main text: CEB training specifics (latent dimensionality, architectures, optimizer, batch size, number of training steps), the offline pretraining protocol (number of gradient steps, convergence criterion), and the exact procedure for collecting the custom DMC Walker, Ant, and Humanoid datasets (number of transitions, behavior policy performance). The paper does not reference an appendix where these might be provided.

4. **Choice of CEB over alternatives is not justified.** The paper uses CEB for density estimation but does not explain why it is chosen over simpler alternatives such as a VAE, kernel density estimation, or RND itself, given that these are cited in the related work. A brief justification would help.

### Trivial
None.

## Nice-to-Haves
- A one-step (depth=1) ablation of PTGOOD to directly support the non-myopic planning claim.
- A discussion of how rates are aggregated along the tree (e.g., whether discounting or normalization is applied).
- Adding standard RND (without DeRL) to the main comparison table for completeness.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"The decoupled RND/DeRL baseline is not compared to standard RND in the main experiments."** — The paper does show standard RND alone in the λ-sweep analysis (Section 4.1, Figure 1) and RND/DeRL is the improved variant in the main experiments. The comparison between the two is implicit in the design; removing this concern.

- **"The rate objective's connection to exploration is not theoretically justified."** — The paper provides an intuitive justification (maximizing rates targets OOD regions near the improving policy). Theoretical analysis is not standard for an empirical systems paper. WEAKENED to a nice-to-have at most.

- **"Cal-QL learns well on some MR datasets at 2M steps"** (implied as contradicting a claim). — The paper itself acknowledges this ("it does learn a good policy in the remaining Medium Replay datasets at the end of the two million online steps") and the key point is that PTGOOD achieves success within 50k steps. This is not a weakness.

- **"5 seeds gives low statistical power for the t-test"** — While true, the paper finds significance in 5/7 settings despite this, which strengthens rather than weakens the results. This is a generic methodological remark, not a specific flaw.

- **Complaints that PTGOOD's advantage could be from "brute-force planning compute"** — This framing is too strong. The paper's comparison metric (returns per environment step) is standard in RL; using the dynamics model for planning during data collection is a legitimate design choice, not a confound. However, the related concern about wanting an ablation isolating the rate signal is retained as a Major weakness above.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the need for an ablation study and full hyperparameter disclosure but do not identify conceptual issues the paper's own analysis missed.

## Suggestions
1. Add an ablation comparing PTGOOD (with rate scoring) against PTGOOD with uniform/random scoring in the same tree-search framework, on at least 2-3 environments. This directly isolates the contribution of the OOD objective.
2. Report the planning width w and depth d used for each environment, ideally with a sensitivity analysis showing how performance varies with these parameters.
3. Add a brief discussion of the computational cost of tree search (number of model calls per environment step) and acknowledge the trade-off. If feasible, include a wall-clock comparison.
4. Add a depth=1 ablation to support the claim that non-myopic planning is beneficial.
5. Provide missing implementation details (CEB training, offline pretraining protocol, dataset construction) either in the main text or a clearly-referenced appendix.

## Score and Decision

The paper presents a well-motivated, novel approach with strong and consistent empirical results. The core weaknesses are the missing ablation isolating the OOD signal from the tree search and the unreported planning hyperparameters — both are fixable and do not invalidate the paper's contributions. The analysis of existing exploration methods in the OtO setting is itself a valuable contribution.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>