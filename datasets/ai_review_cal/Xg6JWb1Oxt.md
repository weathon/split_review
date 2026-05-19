- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 6, 5, 6, 5, 8
Now I have a thorough understanding of the paper and can evaluate each reviewer claim against the actual paper content.

## Summary

This paper proposes VfO (Value from Observations), a simple offline imitation-from-observation algorithm that uses a value function with binary or discriminator-based rewards to transfer information from action-free expert demonstrations to action-labeled background data. It also introduces SIBench, a new benchmark where background data has continuously varying quality (rather than bimodal expert/random mixtures), and validates SIBench via self-improvement experiments showing correlation between offline benchmark performance and iterative improvement. The contributions are: (1) SIBench as a more representative benchmark, (2) the VfO algorithm, and (3) initial demonstration of self-improvement for IfO.

---

## Strengths

1. **SIBench validated against actual self-improvement.** The paper constructs SIBench with background policies of continuously varying quality (Section 4.1) and then directly validates it by showing that offline SIBench results correlate with iterative self-improvement experiments (Section 4.6, Figures 6–7): VfO-bin succeeds where SMODICE fails on both SIBench and the self-improvement loop. This validation strengthens the claim that SIBench is more representative of practical self-improvement scenarios than the bimodal benchmarks used in prior IfO work.

2. **VfO achieves near-oracle performance on several domains.** On Ant, HalfCheetah, and Walker2D (VfO-disc) in SIBench evaluation (Figure 2), VfO obtains cumulative returns close to AWR with ground-truth rewards, despite lacking both action labels on expert data and any reward signal. This is a genuinely strong result for a simple method.

3. **Successful demonstration of iterative self-improvement.** The self-improvement experiments (Section 4.6) show VfO-bin bootstrapping from near-random seed data to strong performance over 20 iterations on multiple D4RL domains (Figure 6), and showing positive results on 2/3 Robomimic tasks (Figure 7). The paper identifies the saw-tooth improvement pattern and discusses the phenomenon, which provides useful signal for future work.

4. **Broad evaluation across domains, settings, and data distributions.** The paper evaluates VfO, SMODICE, DILO, BC, and oracle AWR across D4RL (low-dimensional state), Robomimic (state and vision), using both SIBench and bimodal data. The bimodal results (Figure 4) are particularly informative as they delineate when each family of methods succeeds, helping the community understand the limitations of existing benchmarks.

---

## Weaknesses

### Fatal
None.

### Major

1. **No statistical rigor anywhere in the paper.** No error bars, confidence intervals, standard deviations, or multiple-seed results are reported for any experiment. The boxplots in Figures 2–5 aggregate across data quality levels *within a single run per level*. The self-improvement plots (Figures 6–7) are single-trajectory without replication. Given the well-known variance of RL and offline RL methods, this makes it impossible to assess whether observed differences (e.g., VfO outperforming SMODICE on SIBench) are systematic or due to noise. The paper's strongest claim — "VfO-bin obtains performance similar to the AWR oracle in all settings" — rests on unreplicated runs. This substantially weakens the evidential foundation of every quantitative result.

2. **Baseline tuning on SIBench is not discussed, raising fairness concerns.** The paper's central empirical argument that VfO outperforms SMODICE and DILO on SIBench hinges on these baselines being poorly suited to the continuous-quality data distribution. However, the paper provides no evidence that SMODICE/DILO were tuned (e.g., via hyperparameter search) for this new distribution — the paper does not discuss any tuning procedure. The paper shows SMODICE/DILO work well on the bimodal benchmark (Figure 4), confirming their implementations are functional, but the absence of tuning discussion for SIBench leaves open the possibility that the baselines could perform better with appropriate hyperparameters. The self-improvement validation (Section 4.6) partially mitigates this by showing SIBench results correlate with iterative improvement for both VfO-bin and SMODICE, but only two methods are compared in the self-improvement loop.

### Minor

1. **Overclaim about "bootstrapping to mastery."** The paper states (Section 4.6): "bootstrapping imitation learning to mastery via self-collection starting from low signal... is an open problem" — framing VfO's results as addressing this. However, on Hopper, VfO-bin converges around 1500–2000 cumulative return, well below expert level (~3000+), and the paper itself notes "All methods underperform on the Hopper task" (Section 4.3). On Robomimic, VfO-bin is described as "good on two out of three tasks" (Section 4.6 caption) rather than achieving mastery. The claims about matching oracle AWR "in all settings" are also undercut by the Hopper results. The results are positive, but the language overstates what the evidence supports.

2. **BCO listed as a baseline but never shown.** The paper lists BCO (Torabi et al., 2018a) as a baseline in Section 4.2, but its results never appear in any figure or table across the entire experimental section. BCO — which uses inverse dynamics + BC — is a natural and important baseline for the IfO setting, and its absence from the results is a clear omission.

3. **Missing implementation details hurt reproducibility.** Several details needed to reproduce VfO are not specified: (a) the mixture parameter α for sampling from D_E vs. D_B is listed as a required input (Algorithm 1) but never explained or given a value; (b) the value function update uses v_{k-1}(s') as the TD target without a target network (Algorithm 1, line 58) — a deliberate design choice that should be discussed; (c) for VfO-disc, no architecture, update frequency, or training procedure for the discriminator is provided; (d) no learning rates, network architectures, or other optimization details are given.

4. **SIBench data generation lacks precise specification.** The paper describes training BC policies with varying numbers of demonstrations (e.g., "10, 20, 50, 100, 200, 500, 1000" — these are not explicitly stated in the paper; the paper's text only says "vary the number of demonstrations" without giving exact numbers for any domain). The exact quality levels, number of episodes per level, and whether background data for each level comes from a single policy or multiple policies are not specified. This hinders reproduction and comparison.

5. **Vision-based results are very thin.** The image-based experiments (Section 4.5, Figure 5) show improvement only on Lift (with modest gains), while no improvement is visible on the other tasks. The paper's claim that VfO works "even in high-dimensional, difficult settings" overstates results that are limited to a single positive data point.

6. **The explanation for SMODICE/DILO failure is speculative.** The paper hypothesizes (Section 4.3) that SMODICE/DILO suffer from residual-gradient-style issues due to the absence of stop-gradients or target networks, but provides no ablation or analysis to substantiate this. A simple experiment (e.g., adding target networks to SMODICE/DILO) would have turned this into a genuine contribution rather than speculation.

### Trivial
None.

---

## Nice-to-Haves
- Run all experiments with multiple seeds (3–5) and report means/variance.
- Conduct a controlled hyperparameter search (e.g., learning rate, reward scaling, temperature) for SMODICE/DILO on a SIBench development subset to rule out unfair comparison.
- Include BCO results in the figures.
- Provide a table of SIBench quality levels, dataset sizes, and returns for each domain.
- Add an ablation adding target networks to SMODICE/DILO to test the residual-gradient hypothesis.
- Clarify whether VfO's value function uses target networks or stop-gradients and discuss the design choice.

---

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Section 4.2 is incomplete in the parsed text" / "text abruptly jumps mid-2022"**: Both are artifacts of the PDF extraction parser. Section 4.2 is present (lines 63–65), and the "2022)" fragment at line 31 is a line-break artifact. These reflect parser errors, not author errors. → **Remove.**
- **Criticisms about missing appendix / missing proofs in appendix**: The rules state these sections were stripped by the parser and exist in the original submission. → **Remove.**
- **Criticism about missing related works**: The reviewer mentions the paper should cite certain other methods, but as per instructions, I cannot verify the existence or relevance of missing citations without external sources. → **Remove.**
- **"The framing of 'large-scale' ... is inspirational but disconnected from the actual experiments"**: While this observation has some surface validity, it is a scope criticism (the paper is working towards a larger vision, not claiming to have achieved it). The paper's title says "Towards Large-Scale Imitation Learning," which accurately reflects the aspirational framing. → **Remove as scope creep.** The paper explicitly frames the experiments as a "first step" toward this vision, making the criticism a mismatch with the stated scope.

---

## Novel Insights

None beyond the paper's own contributions. The two reviews largely converge on the same points: the paper's core ideas (SIBench, VfO) are sound and the benchmark-validation loop is a genuine contribution, but the evidential base is weakened by the absence of statistical rigor (no error bars, no multiple seeds) and insufficient detail about baseline tuning. The harsh critic's observation that SIBench's continuous-quality data may be fundamentally different from the bimodal setups of prior work, and that this distinction explains the performance reversal (VfO works on SIBench but not on bimodal; SMODICE/DILO work on bimodal but not on SIBench), is insightful and worth keeping as an organizing theme — but it is already present in the paper itself.

---

## Suggestions

1. **Add multiple seeds and error bars** to all experiments. This is the single highest-impact improvement and the most common expectation for empirical ML/RL papers.
2. **Run a controlled hyperparameter search for baselines on SIBench**, even if small (e.g., 3 learning rates × 2 temperature values). Report both the best and default performances to demonstrate that VfO's advantage is robust.
3. **Include BCO results** in the SIBench figures, and consider adding an inverse-dynamics+BC baseline trained on the full background data.
4. **Provide a reproducibility appendix** (even if short) with exact SIBench quality levels, hyperparameters for all methods, and architecture details.
5. **Tone down the "mastery" language** for Hopper and Robomimic where results are below expert or mixed. Replace with "substantial improvement" or "competitive with oracle" and be precise about which domains support which claims.

---
