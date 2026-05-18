Here is the consolidated meta-review.

---

## Summary

This paper proposes Bootstrapped Model Predictive Control (BMPC), which replaces the model-free policy and value learning in TD-MPC2 with a bootstrapped expert-iteration loop: the network policy learns by imitating an MPC expert, and the improved policy in turn enables on-policy model-based TD-learning for the value function. A "lazy reanalyze" mechanism replans for only 0.8% of training samples, keeping wall-time overhead at 10–20%. On 42 continuous control tasks (DMControl + HumanoidBench), BMPC substantially outperforms TD-MPC2, DreamerV3, and SAC on high-dimensional locomotion, achieving a 300% improvement in steps-to-solve (90k vs. 360k) while using fewer parameters (3M vs. 5M).

## Strengths

1. **Identifies and resolves a genuine limitation of MPC-based MBRL.** The paper pinpoints the performance gap between the network policy and the MPC policy in TD-MPC2 (Figure 2), diagnoses it as insufficient model-free policy learning, and shows that BMPC closes this gap via expert imitation — the network policy nearly matches the MPC policy on challenging tasks like Dog Run and Humanoid Run (Figure 6). The decomposition is clean.

2. **Substantial and well-documented data-efficiency gains.** On 7 high-dimensional DMControl locomotion tasks, BMPC achieves an average of 90k steps to reach 90% asymptotic reward versus 360k for TD-MPC2 — a 300% improvement (Section 5.1, Figure 4). Learning curves show faster convergence and tighter confidence intervals across 5 seeds.

3. **Ablation cleanly isolates the mechanism of improvement.** Figure 7a decomposes the contribution: Variants 1 and 2 (using a better policy only for guiding MPC, without changing value learning) do not improve performance; Variant 3 (expert imitation + Q-iteration) improves but less than full BMPC; only the combination of expert imitation with on-policy model-based TD-learning yields the full gain. This rules out the concern that gains come merely from a different value-learning objective or better hyperparameters.

4. **Lazy reanalyze is practically useful and well-ablated.** The mechanism achieves a reanalyze ratio of 0.8% vs. the 99% typical in tree-search expert iteration (Ye et al., 2021; Wang et al., 2024), and Figure 7b shows that further increasing reanalyze frequency beyond k=10 yields negligible benefit. Training wall-time increases by only 10–20% (Table 1), making the method practical.

5. **Comprehensive evaluation across diverse tasks.** Tested on 42 tasks (28 DMControl + 14 HumanoidBench), including environments with up to 61-dimensional action spaces, with consistent superiority or competitiveness across the suite. The network size is also reduced (3M vs. 5M parameters) as an orthogonal efficiency gain.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Missing variance metrics in wall-time comparison (Table 1).** The table reports "Mean of 3 runs" for training time and time-to-solve without any standard deviation, confidence interval, or per-run breakdown. Since the time-to-solve advantage on Dog Walk is roughly 2×, this could be within run-to-run noise if variance is high. All other experimental results use 5 seeds with 95% CIs, making this omission conspicuous for a central efficiency claim. The concern does not invalidate the results but weakens the quantitative strength of the wall-time comparison.

2. **Lazy reanalyze is framed as a novel mechanism but is primarily an empirical observation about a natural engineering choice.** For MPC, replanning every sample is computationally prohibitive, so any practical implementation would naturally adopt some form of periodic replanning. The paper's insight — that a 0.8% replanning ratio suffices — is useful and well-demonstrated, but the algorithmic novelty of lazy reanalyze is modest. The contribution here is an empirical finding about when and how infrequently replanning can be done, not a fundamentally new algorithmic concept. Readers should calibrate expectations accordingly.

### Trivial

1. **No explicit discussion of tasks where BMPC underperforms or is merely comparable.** The paper honestly states "superior or comparable performance" (line 153), and Figure 3 visually shows tasks where curves nearly overlap (e.g., Quadruped Walk, Humanoid Stand). However, the paper does not explicitly enumerate or analyze cases where BMPC does not improve over TD-MPC2. A brief discussion of the characteristics of tasks where the benefit is marginal would improve transparency and help readers understand the method's boundary conditions.

## Nice-to-Haves

- **Expert action staleness analysis.** The lazy reanalyze mechanism stores expert distributions from past MPC runs. The paper argues a 0.8% reanalyze ratio is sufficient but does not directly measure how outdated these stored actions become relative to the current policy. A plot of KL divergence between stored and fresh MPC distributions over training would strengthen the empirical justification.

- **Additional ablation: use the original TD-MPC2 max-Q policy as the imitation target.** The current ablation (Figure 7a) decomposes the contribution of expert imitation vs. value learning. An additional variant — using the original max-Q policy (before BMPC's bootstrapping) as the imitation target while keeping everything else the same — would further isolate whether the benefit comes from having any imitation target closer to the MPC expert, or whether the iterative bootstrapping is essential.

- **Longer TD horizon when world model supports it.** The paper notes (line 115) that the TD horizon is limited to N=1 because the world model is trained with a short horizon (H=3). An experiment training the world model with a longer horizon (e.g., H=5 or 10) and testing whether a longer TD horizon becomes beneficial would directly support the stated future direction.

- **Beyond TD-MPC2's architecture.** The method is demonstrated only within TD-MPC2's world model and MPPI planner. A discussion of whether the same bootstrapped imitation idea could apply to other plan-based MBRL frameworks (e.g., DreamerV3's latent planning) and what architectural changes would be needed would strengthen the paper's generalizability claims.

## Removed Points

- **"Improvement might be from better hyperparameter tuning or a different value-learning objective."** — The reviewer raised this as a *potential* concern but immediately noted it is addressed by the ablation in Figure 7a. Not a weakness the reviewer actually asserts; the paper's ablation handles it. Removed as non-applicable.

- **"The paper relies entirely on a single world model architecture (TD-MPC2's) and MPPI."** — This demands the method be demonstrated outside its stated scope. The paper is explicitly built on TD-MPC2; testing across other architectures would be a different (broader) paper. Moved to Nice-to-Haves under "Beyond TD-MPC2's architecture."

- **"The ablated variants change multiple things at once; a cleaner isolation would sharpen the central claim."** — The reviewer's suggested additional variant is a refinement, not a flaw in the existing ablation. The current ablation (Figure 7a) already isolates the key factors: Variant 1 separates "policy used for guidance" from "policy used for value learning," and Variant 3 separates Q-iteration from model-based TD-learning. The existing decomposition is already clean.

## Novel Insights

The reviews collectively surface an observation that goes beyond the paper's own framing: BMPC demonstrates that the bottleneck in TD-MPC2 is not in the MPC planning itself (which works well) but in the *coupling* between the network policy and value function under model-free learning. By breaking this coupling through expert imitation and on-policy TD-learning, BMPC shows that value learning — not policy guidance — is the primary channel through which a better network policy improves MPC. The ablation in Figure 7a is the key evidence: Variants 1 and 2 confirm that guiding MPC with a better policy, without changing value learning, yields no improvement. This suggests that in plan-based MBRL, the value function's accuracy may be substantially more important than the policy prior's quality for planning effectiveness. This insight — that the value function is the rate-limiting factor — is more specific than the paper's general claim about "better policy and value learning" and could guide future work in MPC-based MBRL.

## Suggestions

1. Add standard deviations or 95% CIs to the wall-time table (Table 1), at minimum showing per-run values.
2. Add a brief paragraph discussing the characteristics of tasks where BMPC provides the largest vs. smallest improvements over TD-MPC2.
3. Consider plotting the KL divergence between stored and fresh expert distributions over training to directly validate the lazy reanalyze assumption.

## Score and Decision

**Originality:** 6/10 — Expert iteration is an established paradigm; the specific adaptation to MPC-based MBRL with model-based TD-learning is novel and well-executed.

**Importance of question:** 8/10 — Continuous control with high-dimensional action spaces is practically important, and improving data efficiency in MPC-based methods is a timely problem.

**Claims support:** 8/10 — Core claims are well-supported by ablations and comprehensive benchmarks; wall-time comparison is slightly under-supported.

**Soundness:** 8/10 — Experimental design is sound; ablations are informative; no fatal flaws.

**Clarity:** 7/10 — Well-structured and clear; could be more transparent about boundary conditions.

**Value to community:** 8/10 — The method is practical, the code is released, and the improvements on high-dimensional locomotion are substantial.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>