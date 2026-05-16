Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper introduces Conservative Density Estimation (CDE), a novel offline RL algorithm that integrates pessimism into the stationary distribution space — combining DICE-based marginal importance sampling with an explicit density constraint on out-of-distribution (OOD) state-action pairs. CDE addresses the support mismatch problem that plagues prior DICE methods by using a mixed proposal distribution and a closed-form bound on the OOD importance ratio. The method demonstrates strong empirical performance on sparse-reward and scarce-data D4RL benchmarks, with theoretical guarantees bounding the concentrability coefficient and performance gap.

## Strengths

- **Novel application of pessimism in stationary distribution space.** The paper is the first to explicitly constrain the density of the stationary distribution for OOD state-action pairs (Eq. 4–6), a principled integration of conservative regularization with DICE-based marginal importance sampling that directly targets the support mismatch problem identified in prior DICE work (Section 3.2).

- **Theoretical guarantees bounding the OOD concentrability ratio and performance gap.** Proposition 2 and Theorem 1 prove that CDE automatically bounds the importance ratio for OOD state-actions without assuming bounded concentrability, a common assumption in prior work. Theorem 2 bounds the performance gap in terms of state marginal mismatch and data size, providing theoretical justification for CDE's robustness in data-limited regimes.

- **Consistently strong empirical results on sparse-reward and scarce-data settings across diverse domains.** CDE matches or surpasses all baselines on 8 of 9 Maze2D/Adroit tasks (Table 1) and achieves the highest success rate on 3 of 6 sparse-MuJoCo tasks (Table 2). In the scarce-data setting (Figure 1), CDE maintains high rewards across dataset sizes (1%–30% trajectories) while baselines like OptiDICE collapse at 1%, directly demonstrating the effectiveness of the mixed proposal and density constraint.

- **Mixed proposal distribution effectively mitigates DICE support mismatch.** The construction $\hat{d}^\mathcal{D} = \zeta d^\mathcal{D} + (1-\zeta)\mu$ (Section 3.2.1) is a clean solution to the support mismatch issue in importance sampling, and the empirical results in Figure 1 validate that this design prevents the sharp degradation OptiDICE suffers under scarce data.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Overclaimed "state-of-the-art on D4RL" in the abstract.** The abstract claims "state-of-the-art performance on the D4RL benchmark," but the paper tests only a subset of D4RL tasks (3 Maze2D, 8 Adroit, 6 MuJoCo) and uses a modified sparse-reward variant of MuJoCo rather than the standard dense-reward tasks. The results are competitive on the tasks tested, but the blanket claim is broader than the evidence supports and should be narrowed to reflect the specific evaluation settings.

- **No explicit ablation isolating the OOD density constraint from the other design choices.** CDE combines a mixed proposal, two-phase training, closed-form advantage update, and GMM behavior policy. The only study that varies conservatism (the ε heatmaps in Figure 3) is qualitative. An explicit ablation — e.g., setting ε → ∞ or λ = 0 to effectively remove the OOD constraint and measuring the performance change on at least one task — would isolate the contribution of the core novelty. The comparison with OptiDICE provides partial implicit evidence (since OptiDICE is DICE without the OOD constraint), but a direct within-CDE ablation would be significantly cleaner.

- **Unclear baseline configuration for the custom sparse-MuJoCo and scarce-data settings.** The paper states it "adopts the scores of baselines if they are reported in the original paper" (line 234). For Table 1 (standard D4RL sparse-reward tasks), reported scores are appropriate. However, for the custom sparse-MuJoCo tasks (Table 2) and scarce-data experiments (Figure 1), the baselines must have been run by the authors, but no details are provided on whether hyperparameters were re-tuned for these non-standard settings or simply kept at default values. Since methods like CQL and IQL are sensitive to their penalty/expectile coefficients, this warrants clarification. The paper says "we keep hyperparameters the same for experiments in the same domain" — this is a reasonable approach, but the statement should be made explicit for the custom settings.

- **Quantitative results for the ε parameter study are missing.** The heatmaps in Figure 3 are interesting qualitatively, showing where the agent gets stuck under different conservatism levels. However, there are no quantitative scores (reward or success rate) plotted against ε values, and no direct comparison with CQL's sensitivity to its own conservatism parameter. This weakens the claim that CDE "controls conservatism more precisely than CQL."

- **No convergence criterion specified for the two-phase training.** Algorithm 1 states that policy extraction begins "after the value function converges" (line 169), but no criterion (e.g., loss threshold, fixed number of iterations) is given. A plot of value objective convergence or a sensitivity analysis on training length would improve reproducibility.

- **The sparse-MuJoCo construction uses a fixed 75th percentile threshold** with no sensitivity analysis. The relative ranking of methods could depend on this choice. A brief discussion of how this threshold was selected and whether results are stable across reasonable choices would strengthen the evaluation.

### Trivial

- The choice of Δa (the L∞ threshold defining OOD actions) is not discussed or ablated. Since it appears in the bound of Theorem 1, a brief comment on its practical setting would be helpful.

- The ζ parameter study tests only three values (0.5, 0.8, 0.9) on a subset of tasks. The trend is clear but the range is narrow.

- The bias introduced by the hard cap on importance ratios (Proposition 2) is not discussed in the limitations.

## Nice-to-Haves

- A discussion of whether performance would degrade if a simpler behavior model (e.g., a single Gaussian) replaced the GMM. This would clarify whether the GMM is important for the method's success.
- A brief comment on the bias-variance trade-off created by the hard cap $\tilde{\epsilon}$ on importance ratios, and practical guidance on tuning it.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **Criticism about Eq. (1) / Bellman flow constraint not being explained.** The paper explicitly cites OptiDICE and follows standard DICE methodology for using Lagrange multipliers v(s) to convert the constraint. This is standard background knowledge in the DICE literature, not a gap in the paper.

- **Criticism about Proposition 2's closed-form λ* ignoring normalization constraints.** The paper states in line 136 that a normalization constraint is added "in practice" following prior work (Gendice). The closed-form solution for w* from the Lagrangian inner maximization is standard and correct; normalization is handled as a separate practical step. This is not a flaw.

- **Criticism about Eq. (8) / policy extraction TV term depending on unknown optimal marginal.** The paper explicitly acknowledges this limitation in the discussion of Theorem 2 (lines 216–217). The authors are transparent about the bound's dependence on this term. Repeating it as a weakness is redundant.

- **Criticism about scarce-data trajectory subsampling changing distribution.** The paper explicitly states it samples trajectories (line 291), which is a well-defined procedure for creating smaller datasets. Whether to subsample trajectories or i.i.d. transitions is a design choice; neither is wrong. This is a methodological observation, not a weakness.

- **Strength 5 from Strength Finder** (about parameter study providing controlled insight into conservatism–performance trade-off) is dropped because the parameter study is only qualitative and conflicts with the verified weakness about missing quantitative results.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Narrow the SOTA claim** in the abstract and introduction to reflect the specific tasks evaluated (selected sparse-reward D4RL tasks, plus a custom sparse-MuJoCo variant), or provide evidence on the full D4RL benchmark.

2. **Add an explicit ablation** removing the OOD constraint (ε → ∞) on at least one Maze2D and one sparse-MuJoCo task, with tabular results comparing quantitative scores.

3. **Clarify baseline tuning for custom settings.** State explicitly whether the same hyperparameters from the original papers were used for the sparse-MuJoCo and scarce-data experiments, and if re-tuning was performed, report the search范围和 best values.

4. **Add quantitative curves for the ε parameter study** (score vs. ε) and, if feasible, a direct comparison with CQL's sensitivity to its penalty coefficient on the same tasks.

5. **Specify a convergence criterion** for the value learning phase in Algorithm 1, or report how many iterations were typically sufficient.

## Score and Decision

The paper presents a genuinely novel idea (pessimism in stationary distribution space) with clean theoretical support and strong empirical results on the tasks tested. The weaknesses are all addressable in revision — none threaten the core contribution. The paper merits acceptance with minor revisions.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>