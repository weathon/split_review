Now I have a thorough understanding. Let me compile the final review.

## Summary

This paper introduces ACTIVE, an offline RL algorithm combining two components for in-sample learning: (1) an ensemble of V-functions (IVE) that uses the ensemble minimum for bootstrapping to mitigate overfitting of value functions, and (2) an adaptive cloning temperature (ACT) based on dual gradient descent to dynamically adjust the regularization level during policy extraction. The method is evaluated on D4RL benchmarks and shows improvements over IQL and SQL baselines, particularly on AntMaze and suboptimal MuJoCo datasets.

## Strengths

- **Identifies and empirically demonstrates a concrete failure mode in in-sample value learning**: The paper provides clear evidence (Figure 1) that V-functions in IQL/SQL can overfit to initial Q-errors, leading to instability that prevents using larger expectiles or smaller α. SQL diverges with α=0.1 while the ensemble-based variant (IVE-SQL) remains stable. This is a specific, previously under-explored problem that the paper then addresses.

- **Clean ablation isolating the contributions of each component**: Figures 6(a) and 6(b) show that IVE mainly benefits AntMaze tasks (where value propagation is critical) while ACT mainly improves performance on suboptimal MuJoCo datasets (where cloned behavior hurts). This disentanglement strengthens the algorithmic design rationale substantially.

- **Demonstrates consistent performance gains on challenging datasets**: In Table 2, ACTIVE-I and ACTIVE-S systematically outperform their IQL/SQL baselines on AntMaze-diverse, kitchen-mixed, and medium-replay MuJoCo datasets across multiple seeds. The improvements are meaningful where the baselines struggle most.

- **Practical run-time efficiency analysis**: Table 3 reports that with small networks, the ensemble overhead is modest due to parallelization, addressing a natural concern about ensemble-based methods.

## Weaknesses

### Fatal

None.

### Major

- **The theoretical analysis (Section 4.3) does not provide the support the paper claims.** Theorem 4.5 relies on Assumption 4.3 (fixed implicit policy throughout training), which the authors themselves admit is "a strong one which is not satisfied in the actual IQL algorithm." The NTK framework at infinite width is a distant idealization from the practical finite-width setting. More importantly, the derivation connects the ensemble-min bootstrapping in Equation (7) to a term B defined as a square-root of ensemble variance of initial V-outputs, but the paper does not explain how the min operator (as opposed to ensemble averaging or variance penalization) specifically yields this term. The paper's abstract states "We theoretically show that the V-ensemble suppresses the accumulation of initial value errors" — this overstates what the analysis actually delivers given its acknowledged assumptions. The gap between the theorem's premises and the algorithm's operation is wide enough that the theory provides intuition at best, not a formal justification.

### Minor

- **Baseline results are taken from original papers rather than re-run under identical conditions.** Table 2 explicitly notes that results for CQL, TD3+BC, IQL, and SQL are "taken from the authors." D4RL scores can vary substantially across implementations and random seeds (e.g., IQL on antmaze-umaze-d-v2 is listed as 62.8, while some public replications report different numbers). Without a shared evaluation protocol (same number of seeds, evaluation episodes, hyperparameter sweeps), the relative gains claimed for ACTIVE are less precisely calibrated than they would be with a controlled rerun.

- **Missing comparison with ensemble methods (SAC-N, EDAC) on MuJoCo tasks.** The paper compares ACTIVE to RORL and MSG on AntMaze and SAC-N on Kitchen, finding SAC-N fails on Kitchen. However, SAC-N and EDAC are known to perform well on MuJoCo, and a direct comparison there would substantiate the claim that the in-sample ensemble is "advantageous" or that a smaller ensemble suffices. Without this, the claim is supported only on the tasks where out-of-sample ensembles struggle, which is a weaker test.

- **The adaptive temperature's target H_𝒟 is left underspecified.** Remark 5.1 notes that "estimating the optimal H_𝒟 is difficult" and the paper acknowledges it varies with dataset quality. However, no default value, heuristic, or principled estimation method is provided. Figure 5 shows that different H_𝒟 values affect performance, but the paper does not reveal what values were actually used in the main experiments, hurting reproducibility.

- **The over-regularization diagnosis is asserted but not directly measured.** The paper motivates both the V-ensemble and adaptive temperature by arguing that existing in-sample methods suffer from over-regularization, yet no direct evidence is provided — no tracking of effective KL divergence between learned and behavior policy, no quantification of advantage sparsity dynamics during training, and no measurement of actual regularization levels across datasets of varying quality. Figure 1 primarily demonstrates a stability problem (divergence), not over-regularization per se. The ablation study (Figure 6) indirectly supports the benefit, but the motivating narrative remains partially untested.

### Trivial

- The paper does not give a clear practical guideline for choosing between ACTIVE-I and ACTIVE-S beyond using whichever base loss (IQL vs. SQL) the practitioner prefers. A simple decision rule (e.g., "use ACTIVE-I when expectile tuning is desired, ACTIVE-S when SQL's α formulation is preferred") would improve usability.

## Nice-to-Haves

- A direct measurement of ensemble disagreement vs. value error over the course of training (as the paper already mentions in its "Strengthening" suggestions) would visually confirm the core mechanism.
- A simpler, more direct analysis of the bias-variance trade-off induced by min_i V_i, without the NTK machinery, would be more informative than the current theorem.

## Removed Points

- **Strength about "theoretical justification" (Strength Finder Point 2)**: This conflicts with the verified weakness that the theory relies on an assumption invalid in practice and provides weak support. Per the rule that when a strength and verified weakness disagree, the weakness wins, this strength is moved here.
- **Complaint about Algorithm 1 not being in main text (Harsh Critic "Other Observations")**: The parser strips appendix content; the algorithm exists in the original submission. Removed per rule about missing appendix complaints.
- **Criticism that B is "ensemble variance" while the algorithm uses "min"**: The paper itself connects the min to the variance (via the Royston approximation and the Gaussian assumption in Section 4.2), so this is partially addressed, and the theorem is about the overall update dynamics, not a direct equation-level match.
- **Individual sentence-level nitpicks** (e.g., specific phrasing about "this sentence in the intro"): Removed as pedantry that doesn't affect the contribution assessment.

## Novel Insights

None beyond the paper's own contributions. The key insight — that in-sample V-functions can overfit to initial Q-errors and that an ensemble minimum during bootstrapping stabilizes this — is the paper's own contribution, and the reviews do not add a perspective that transcends it.

## Suggestions

1. **Rerun the key baselines (IQL, SQL) under the same evaluation protocol** (same seeds, same evaluation episodes) to put the relative gains on firmer footing. If this is infeasible, provide a sensitivity analysis table showing the range of published IQL/SQL scores and where ACTIVE falls within that distribution.

2. **Add a MuJoCo comparison table for ACTIVE vs. SAC-N/EDAC** with similar ensemble sizes. This directly addresses the most significant gap in the empirical evaluation. Even if the results are mixed, the honesty would strengthen the paper.

3. **Provide a concrete heuristic or default value for H_𝒟** — for instance, setting it to the average log-likelihood of the uniform policy over the action space, or a percentile of the behavior policy's log-likelihood. Without this, the adaptive temperature component is difficult to reproduce.

4. **Dilute the theoretical claims** to match what the analysis actually delivers. Replace "We theoretically show" with "We provide a theoretical intuition under idealized assumptions (fixed implicit policy, infinite width NTK) that..." Acknowledging the gap in the abstract or introduction would better align claims with evidence.

5. **Add at least one direct measurement of regularization strength** — e.g., plot the effective KL divergence D_KL(π || μ) over training for IQL, SQL, and ACTIVE on datasets where over-regularization is claimed. This would directly validate the motivating narrative.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>