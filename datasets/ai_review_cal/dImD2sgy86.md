- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6
Now I have thoroughly read the paper and can produce a consolidated review by verifying all claims against the actual text.

Let me now produce the final review.

## Summary

The paper develops a principled framework (SCLD) that unifies Sequential Monte Carlo (SMC) methods with diffusion-based samplers by viewing both through continuous-time path space measures. The key innovations are: (1) decomposing Radon-Nikodym derivatives across subtrajectories to enable interleaving of learned SDE transitions with resampling and MCMC steps; (2) adopting a log-variance loss (over KL) that provably avoids exponential-in-dimension variance blowup and enables off-policy training with replay buffers; and (3) demonstrating on 11 benchmarks that SCLD achieves state-of-the-art performance, often using only 10% of the training budget of prior diffusion-based samplers (3000 vs 40000 gradient steps).

## Strengths

- **Principled unification of SMC and diffusion-based samplers via path space measures.** The paper derives an explicit Radon-Nikodym derivative (Lemma 1) and decomposes it across subtrajectories (Eq. 6/12), enabling rigorous integration of learned SDE transitions with resampling and MCMC at arbitrary times. This is a concrete advance captured in the comparison table (Table 1), showing SCLD uniquely combines learned transitions, stochastic transitions, end-to-end training, particle methods, discretization flexibility, and finite-time convergence — a combination no prior method achieves.

- **Strong empirical performance with dramatic training efficiency.** SCLD achieves the best ELBO on 4 of 5 tasks (Table 1) and the best Sinkhorn distance on 4 of 6 tasks (Table 2). On the Robot1/Robot4 tasks, SCLD is the only method that approximately recovers the true multimodal distribution (Figure 3). Crucially, these results are obtained with 3000 gradient steps vs 40000 for CMCD variants, and Figure 4 confirms the advantage holds in wall-clock time as well.

- **Log-variance loss with theoretical advantage.** Proposition 1 proves that the relative error of the KL divergence estimator scales exponentially with dimension when importance-weighted corrections are needed, whereas the log-variance divergence avoids this issue. This provides theoretical grounding for the practical loss used in Algorithm 2 (detached trajectories, replay buffers without high-variance importance weighting).

- **Comprehensive ablation studies.** The paper systematically studies the effect of varying the number of SMC subtrajectories at training and evaluation time across multiple tasks (Figure 5), provides visual evidence of mode coverage (Figure 3), and includes extensive additional experiments in the appendix (ablation without MCMC, KL vs LV training, timing information, etc.).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **MCMC refinement as a potential confound.** SCLD uses one HMC step (10 leapfrog steps) after each subtrajectory, whereas the primary diffusion-based baselines (CMCD-KL, CMCD-LV, DDS, PIS) do not. The paper acknowledges this and includes an ablation study in the appendix (sec:NoMCMC). However, the main tables and the headline "10% training budget" claim do not separate the effect of MCMC from the learned SDE control. While this does not undermine the overall contribution (the combined method is what is proposed), a reader cannot determine from the main text whether the gains come primarily from the SMC+diffusion integration or from the MCMC refinement. The ablation results in the appendix are critical for this interpretation.

- **"10% training budget" claim is precise for gradient steps but imperfectly calibrated for cost.** The paper states "SCLD and CMCD steps require similar amounts of time for these tasks (see sec:timings)" and Figure 4 uses wall-clock time on the x-axis. However, the "10%" framing (3000 vs 40000 gradient steps) could be read as a 10× cost reduction, while SCLD's per-iteration overhead (resampling, HMC, buffer operations) may not be perfectly comparable. The paper largely addresses this through its convergence plots and timing appendix, but a per-task wall-clock table in the main text would remove ambiguity.

### Trivial

- The number of subtrajectories (N=4 for synthetic tasks, N=128 for others) is described as "robust" but the rationale for this two-tier split — 4 vs 128 — is somewhat ad-hoc. The heatmap analysis (Figure 5) partially justifies the choice, but a more systematic selection rule would strengthen the practical guidance.

## Nice-to-Haves

- **Direct empirical validation of log-variance vs KL variance scaling.** Proposition 1 is proven for product-path measures (independent dimensions). While the paper includes a KL vs LV ablation (KLAblation), a direct empirical demonstration of estimator variance growing with dimension in non-product settings would strengthen the claim that LV is critical for scalability.

- **Failure mode / limitation discussion.** The paper acknowledges tasks where SCLD is not best (Funnel, LGCP) but would benefit from a brief discussion of when SMC resampling might harm performance or when pure CMCD would be preferable to SCLD.

## Removed Points

**From Harsh Critic:**
- "Log-variance loss scaling advantage is theoretically motivated but not directly validated" → Moved here. This is a nice-to-have suggestion, not a weakness. The paper provides Proposition 1 (theory) and a KL vs LV ablation (empirical), which is reasonable support for the design choice.
- "Proposition 1 is for product-path measures" → Moved here. The paper explicitly acknowledges this ("stylized" setting with independent dimensions, line 271) and uses it to illustrate the scaling concern. This is appropriately scoped.
- "Sensitivity analysis for the number of subtrajectories" → The paper already provides a dedicated heatmap analysis (Figure 5) studying this across four tasks. This criticism is already addressed.
- "Paper would benefit from discussion of failure modes" → Moved to Nice-to-Haves above.

**From Strength Finder:**
- All five strengths listed are concrete, specific, and verified against the paper. Kept.

## Novel Insights

None beyond the paper's own contributions. The paper's core insight — that SMC resampling and MCMC can be rigorously embedded within diffusion-based samplers via path space measure decomposition — is itself the novel contribution. The reviews do not surface additional insights beyond what the paper already provides.

## Suggestions

1. In the main text, briefly summarize the results of the no-MCMC ablation study (currently only in the appendix). This would help readers directly assess whether the primary gains come from the SMC+diffusion framework or from the MCMC refinement, and would fully address the most significant reviewer concern.
2. Include a per-task wall-clock time table (or at least a sentence summarizing the timing appendix's conclusions) in the main experiments section, so the "10%" claim is fully transparent.
3. Add a short paragraph to the conclusion or a limitations section discussing when SCLD might not be the best choice (e.g., based on the Funnel and LGCP results).
