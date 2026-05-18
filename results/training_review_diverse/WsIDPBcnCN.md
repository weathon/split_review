Now I have sufficient information to cross-check all reviewer claims against the paper. Let me produce the final consolidated review.

---

## Summary

This paper introduces Plasticity-Driven Sparsity Training (PlaD), a dense-to-sparse training method for deep reinforcement learning. PlaD combines iterative magnitude pruning with two novel components — periodic replay buffer reset (to mitigate non-stationarity) and dynamic weight rescaling (DWR, to stabilize training). The paper also introduces the Weight Shrinkage Ratio (WSR) metric to document that implicit sparsity increases during conventional dense DRL training. Evaluated on MuJoCo continuous control tasks with SAC, PlaD achieves performance matching or exceeding that of dense models at sparsity levels above 90%, substantially outperforming existing sparse-to-sparse baselines.

## Strengths

1. **Strong empirical performance at very high sparsity.** PlaD achieves 99.2% of dense model performance on HalfCheetah at 90% sparsity (vs. 82.5% for the nearest baseline) and 103.0% on Ant at 90% sparsity (vs. 71.7% for Magnitude). These margins over existing sparse training methods are substantial and well-documented across multiple MuJoCo tasks (Fig. 5, 10 of 12 tasks at ≥85% sparsity).

2. **Ablation validates both components are necessary in the sparse setting.** Table 1 shows that removing either the memory reset or DWR significantly degrades performance at high sparsity (e.g., Hopper-v4: PlaD 86.1% vs. w/o DWR 64.2% vs. w/o Reset 55.0%), demonstrating that the two components jointly drive the reported results.

3. **Periodic reset vs. fixed small buffer analysis.** Figure 6 directly compares resetting the buffer against using a fixed small buffer of the same size; reset outperforms in 3 of 4 tasks at 90% sparsity (e.g., Hopper-v4: ~110% vs. ~80% normalized). This shows the reset mechanism itself — not merely reduced buffer size — is the driver.

4. **Novelty of the WSR analysis.** The paper documents, via the Weight Shrinkage Ratio and feasible pruning ratio experiments (Figs. 2–3), that dense DRL training progressively increases implicit sparsity. This observation across both SAC/MuJoCo and DQN/Atari provides empirical motivation for why dense-to-sparse training may be preferable to sparse-to-sparse in DRL — a perspective that was not previously articulated in the literature.

5. **PlaD exceeds dense performance in several settings.** At 85% sparsity on Walker2d, PlaD reaches approximately 130% of the dense SAC baseline — a surprising and practically relevant result that warrants further investigation.

## Weaknesses

### Fatal
None.

### Major

1. **Missing control: dense SAC with memory reset + DWR without pruning.** The paper's central narrative is that PlaD preserves plasticity *under sparsity*. However, there is no experiment applying memory reset and DWR to dense SAC (without any pruning). If this dense version also substantially outperforms vanilla SAC, then the observed gains could reflect generic algorithmic improvements rather than a sparsity-specific plasticity intervention. The ablation in Table 1 shows these components are necessary in the sparse setting, but it does not disentangle whether they would help equally in the dense setting. This confound does **not** invalidate the empirical comparison against other *sparse* training methods (PlaD clearly beats them), but it does weaken the mechanistic claim about sparsity and plasticity, and the claim that PlaD "achieves higher performance than the dense performance" is ambiguous without knowing whether dense SAC augmented with the same components would also improve. This is the most important issue to address.

2. **Limited evaluation domain.** PlaD is tested only on MuJoCo continuous control with SAC. While the paper's motivating WSR analysis covers both Atari/DQN and MuJoCo/SAC (Figs. 2–3), PlaD itself is never evaluated on discrete-action, pixel-based, or other continuous-control domains. The paper also does not compare against recent plasticity-focused methods adapted to the sparse setting (e.g., dormant neuron reactivation from Sokar et al., 2023, or layer normalization from Lyle et al., 2023) — techniques that intersect with PlaD's motivation. These omissions limit the generality of the claimed state-of-the-art status.

### Minor

1. **Missing implementation details for reproducibility.** The paper does not specify: (i) the reset frequency for the replay buffer (how often is it emptied?); (ii) the pruning schedule for IMP (number of rounds, fraction of weights removed per round, at which training steps pruning occurs); (iii) the total number of training steps for PlaD. The text says "periodically reset the replay buffer to empty (0.2M)" without clarifying whether 0.2M is the buffer capacity, the interval between resets, or the number of samples collected after reset. These details are needed to reproduce and build upon the work.

2. **No computational cost comparison.** The paper argues that sparse-to-sparse training "may escalate the overall computational cost" and that PlaD is more efficient, but it provides no wall-clock time, total FLOPs, or training-step comparison. Since memory reset and DWR add overhead, and IMP is known to require multiple prune-retrain cycles, a cost-benefit analysis is needed to substantiate the efficiency claim.

3. **Strong claim of exceeding dense performance lacks mechanistic depth.** The paper reports PlaD reaching ~130% of dense SAC performance on Walker2d at 85% sparsity. The explanation ("reduced non-stationarity and improved gradient flow") is high-level and not supported by direct evidence (e.g., gradient norm measurements, representation analysis). This is a noteworthy result that would benefit from a deeper mechanistic account.

4. **Indirect plasticity evidence.** The paper connects PlaD's success to plasticity preservation through downstream performance gains and the WSR/f easible-pruning analysis. It does not directly measure established plasticity indicators for PlaD itself (e.g., dormant neuron fraction as in Sokar et al., 2023, effective rank as in Kumar et al., 2021). The link between PlaD's components and plasticity remains correlational rather than causal.

### Trivial

- The Gaussian example illustrating WSR (Section 4.1) could be clearer about how D[N2|N1] = 56.8% and D[N3|N2] = 59.4% are computed from the sampling process. The concept is understandable but the exposition is terse.

## Nice-to-Haves

- A dense SAC baseline augmented with memory reset + DWR (no pruning) would resolve the central confound described above. This single experiment would clarify whether PlaD's gains are sparsity-specific or general.
- Measuring dormant neuron fraction or effective rank for PlaD vs. dense SAC and sparse baselines at matched sparsity levels would provide direct evidence for the plasticity narrative.
- Including at least one discrete/visual domain (e.g., Atari with DQN or a variant) would strengthen the generality claim.
- Reporting the reset frequency, pruning schedule, and total training steps in the main text would improve reproducibility.
- A simple wall-clock or FLOPs comparison would support the efficiency argument.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The WSR Gaussian example is confusing"** — The example is functional: it shows that WSR increases with variance growth, which is precisely the concept needed. The reviewer's confusion does not indicate a paper flaw.
- **"Duplicate sentence in the abstract"** — This is a parser artifact from PDF extraction; the original submission does not have this issue.
- **"Missing related works"** — Per policy, I cannot verify what related works exist or are missing; the paper's related work section covers the relevant areas (sparse training, plasticity in DRL, network resetting).
- **Critic's suggestion that sparse-to-sparse vs. dense-to-sparse plasticity should be directly compared via dormant neuron ratios** — This is a reasonable suggestion but goes beyond what the paper claims; the paper establishes a plausible motivation via WSR, and the main contribution is the method itself, not a comprehensive plasticity comparison across paradigms.
- **Critic's framing that the missing dense control "undermines the central claim"** — The claim that PlaD produces better sparse models is empirically supported. The missing control weakens the *mechanistic narrative*, not the primary empirical result.

## Novel Insights

Across both the strengths and weaknesses, a clear picture emerges: PlaD's combination of memory reset and DWR produces empirically impressive results, but the paper's interpretive framing (sparsity-specific plasticity preservation) is not yet uniquely supported by the evidence. The reviewers independently converge on the same critical missing experiment — dense SAC with the same auxiliary components — as the single change that would most clarify the contribution. This kind of convergent diagnosis is itself insightful: the paper would be substantially strengthened not by adding complexity but by a single, clean control that the authors appear to have the infrastructure to run. The WSR metric is a genuinely novel observational contribution that could have standalone value independent of PlaD.

## Suggestions

1. **Run the dense control experiment.** Apply memory reset + DWR to dense SAC without any pruning. If performance improves relative to vanilla SAC, the paper's narrative should acknowledge that memory reset and DWR are general plasticity improvements that also benefit sparse training, not sparsity-specific solutions. If performance does not improve, the current narrative is validated. Either outcome strengthens the paper.

2. **Specify all missing implementation details** (reset frequency, pruning schedule, number of training steps) in a dedicated reproducibility section.

3. **Add at least one direct plasticity metric** (dormant neuron ratio, effective rank, or gradient norms) comparing PlaD against both dense SAC and sparse baselines at matched sparsity levels.

4. **Include a computational cost comparison** — even a simple wall-clock time or total training steps comparison would support the efficiency claims against sparse-to-sparse methods.

5. **Add a brief discussion** of why PlaD provides only modest gains at lower sparsity (50%) but excels at high sparsity (85–90%), as this pattern directly supports the plasticity motivation.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>