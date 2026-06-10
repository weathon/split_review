## Summary

MADiff proposes an attention-augmented diffusion model framework for offline multi-agent learning. It formulates multi-agent problems as conditional trajectory generation, using cross-agent attention layers inserted into agent-wise U-Nets to model inter-agent coordination. The framework is designed to support four operating modes — decentralized policy, centralized controller, teammate modeling, and trajectory prediction — and is evaluated on MPE, MA Mujoco, SMAC (offline MARL), and NBA trajectory prediction.

## Strengths

- **Ablation study cleanly isolates the coordination mechanism.** The comparison between attention-based and independent variants (Figure 4) shows a dramatic gap on the hardest coordination task (World: ~120+ vs. ~40–60), providing direct causal evidence that the attention modules — and not other aspects of the architecture — drive the coordination gains. This is the strongest piece of evidence in the paper.

- **Unified treatment of four multi-agent modes in a single architecture.** The paper demonstrates decentralized execution (MADiff-D), centralized control (MADiff-C), teammate modeling (Section 3.6 with a "Consistent Ratio" curve showing proactive plan correction), and trajectory prediction — all with the same attention-augmented diffusion backbone. This unification is conceptually clean and the teammate modeling visualization (Figure 3) is accompanied by a reasonable quantitative proxy.

- **Competitive results across diverse benchmarks with clear best-in-class on several tasks.** MADiff variants achieve the top result on the majority of the 33 task-dataset combinations in Table 1 (e.g., MADiff-C on MPE Tag Expert: 168.3 vs. OMAR's 116.2, MADiff-D on World Medium: 124.2 vs. OMAR's 74.6). On NBA trajectory prediction (Table 2), MADiff-C nearly halves baller2vec++'s ADE at both trajectory lengths (7.92 vs. 15.15 at length 20; 17.24 vs. 32.07 at length 64).

- **Honest limitations section with targeted empirical follow-up.** The paper explicitly acknowledges limitations in scalability and stochasticity (Section 5), then conducts controlled SMACv2 experiments to probe the stochasticity limitation — isolating the condition (both position and unit-type randomness present) under which performance degrades relative to MA-ICQ. This level of specificity is more useful than a generic caveat.

## Weaknesses

### Fatal
None.

### Major

- **The primary sequence-modeling baseline (MADT) is absent from two of three offline MARL benchmarks with no explanation.** MADT (Meng et al., 2021) is the most directly comparable autoregressive sequence-modeling baseline — the paper's own contrast is "diffusion vs. transformer sequence modeling." Yet Table 1 shows MADT results only on SMAC (4 of 12 entries) and as "–" for all 12 MPE entries and all 9 MA Mujoco entries. The paper explains that MPE baselines come from Pan et al. (2022) and MA Mujoco baselines from Formanek et al. (2023) (lines 303–306), but never states why MADT was not run on these benchmarks. Since the authors operationalized MADT themselves on SMAC, the technical barrier to running it on the other benchmarks is unclear. Without this comparison, the reader cannot tell whether MADiff's gains come from the diffusion framework or simply from better architecture/hyperparameter choices.

### Minor

- **The abstract/contributions claim "superior performance" without qualification, even though baselines outperform MADiff on several settings.** Table 1 shows clear cases where baselines beat MADiff: on SMAC Poor datasets, MA-ICQ outperforms MADiff on 3/4 maps (e.g., 3m Poor: 14.4 vs. 8.9; 2s3z Poor: 12.1 vs. 9.9; 8m Poor: 10.8 vs. 5.1); on MPE Spread Random, OMAR (34.4) decisively beats both MADiff variants (7.2, 5.0); on MA Mujoco 2halfcheetah Medium, MA-TD3+BC (2561) beats MADiff-D (2215). The limitations section (lines 405–409) acknowledges that sequence models "tend to underperform Q-learning-based algorithms in environments with high stochasticity," but the abstract and contributions section never qualify the "superior performance" framing to reflect this pattern.

- **Key hyperparameters needed for reproduction are missing.** The trajectory horizon \(H\), classifier-free guidance scale \(\omega\), and number of diffusion steps \(K\) are never specified for any task set. The paper also does not describe what the "Good," "Medium," and "Poor" dataset qualities on MA Mujoco correspond to in terms of return thresholds. These are standard details that affect both reproducibility and the interpretation of results.

- **SMACv2 experiments are reported only qualitatively.** Lines 411–414 state "our method performs worse than the Q-learning-based SOTA, MAICQ, only when both types of stochasticity are present" but provide no numerical results, tables, or figures. This limits the usefulness of the otherwise well-motivated ablation.

- **The cross-agent attention mechanism is underspecified.** The paper states that attention is applied to skip-connected features \(c^i_l\) and uses multi-head attention to fuse information across agents (lines 117–123), but does not specify which agent's features serve as queries vs. keys/values, how many attention heads are used, or how the attention outputs are integrated back into each agent's decoder pathway. For a paper whose architectural novelty centers on this mechanism, the level of detail is insufficient for exact reproduction.

### Trivial

- **Results are reported over only 3 seeds.** Some comparisons show overlapping standard errors (e.g., SMAC 5m6m Medium: MADiff-D 17.5±0.6 vs. MA-CQL 17.0±1.2; SMAC 2s3z Good: MADiff-D 19.4±0.1 vs. MA-ICQ 19.6±0.3). While 3 seeds is common in multi-agent RL, several of the claimed "wins" would benefit from more seeds or formal significance testing to distinguish genuine improvements from noise.

## Nice-to-Haves

- Report inference latency and computational cost relative to baselines, since MADiff-D generates full joint trajectories for all agents at each step.
- Ablate the guidance scale \(\omega\) and trajectory horizon \(H\) on one task per testbed to demonstrate robustness.
- Provide numerical results for the SMACv2 ablation to replace the purely qualitative description.

## Removed Points

These points were raised in the reviews but are removed after verification against the paper:

- *"Baseline results on MA Mujoco raise concerns about evaluation fairness (OMAR far below BC)."* The paper explicitly states these baselines are "adopted from Formanek et al. (2023)" (line 305) — they are published results, not the authors' runs. OMAR's known weakness on continuous control was documented by the source paper itself. The concern is speculative about another group's published benchmark, not a verifiable flaw in this paper.
- *"MADT characterization is misleading."* The paper's description of MADT as learning "an independent model for each agent without modeling agent interactions" (line 195) is accurate for the MADT formulation as originally published. Mentioning later modifications that post-date the cited paper is not required.
- *"Details of decentralized execution mechanism are unclear."* The paper provides a clear matrix formulation in Equation 5 (lines 160–177) showing how each agent conditions on its own observation while generating trajectories for all agents. The notation is explicit.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Run MADT on MPE and MA Mujoco using the authors' own implementation (already operational on SMAC) and report the results. This one comparison would directly validate the paper's central claim about diffusion vs. autoregressive sequence modeling and is the single most impactful addition.

2. Add a table of hyperparameters (\(H\), \(K\), \(\omega\), number of attention heads, dataset return thresholds) for each testbed, either in the main paper or supplementary material.

3. Qualify the "superior performance" language in the abstract and contributions to reflect the pattern that emerges from the data: MADiff is competitive on high-quality data and sometimes weaker than Q-learning methods on low-quality/stochastic settings. Replace "superior performances" with language such as "competitive or superior performances, with particular strength on high-quality data."

4. Provide numerical results for the SMACv2 experiments — even a small table — to make the otherwise well-designed analysis actionable for readers.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Weak Accept</decision>