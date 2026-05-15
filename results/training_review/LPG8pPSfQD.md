Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper presents DistRL, an asynchronous distributed reinforcement learning framework for fine-tuning on-device mobile control agents. The framework decouples trajectory collection (on worker machines running Android emulators) from policy learning (on a central GPU host), using a FIFO queue for asynchronous communication. The authors also propose A-RIDE, an off-policy RL algorithm combining Retrace corrections, Distributed Prioritized Experience Replay (DPER), and a trajectory-level value estimator. Experiments on AitW benchmark tasks show DistRL achieves ~3× training efficiency improvement, ~2.4× faster data collection, and ~20% relative success rate improvement (73.2% vs. 61.2%) over the synchronous DigiRL baseline.

## Strengths

- **Significant and clearly demonstrated training efficiency gains**: DistRL reaches target success rates ~3× faster in wall-clock time than DigiRL (Figure 3a), and collects ~2.4× more trajectories (800 vs. 300 in 6k seconds, Figure 3c). These are objective, metric-independent measurements that directly support the core claim of improved efficiency.

- **Substantial end-task success rate improvement with good statistical hygiene**: On the AitW General test set, DistRL achieves 73.2% vs. DigiRL (multi) 61.2% — a ~20% relative improvement — with lower standard deviation (±1.1 vs. ±2.4, Table 1). The gap is consistent across both General and Web Shopping tasks and across training/test splits, strengthening the claim.

- **Well-motivated and clean system architecture**: The asynchronous host-worker design with environment snapshots and FIFO trajectory queue is a principled solution to the synchronization bottleneck identified in DigiRL. The near-linear scalability (Figure 3d, ~7.7 trajectories/minute approaching the ideal upper bound with 192 CPUs) validates the architecture empirically.

- **Ablation study confirms individual component contributions**: Removing DPER drops success rate by ~8%, and removing Retrace drops it by ~6% with training instability (Figure 4b). This provides causal evidence that both algorithmic components contribute meaningfully.

- **Automated evaluator validated against human judgment**: Section 6.3 shows the Gemini-based evaluator achieves <2% discrepancy with human evaluation when using the last screenshot + last two actions, with careful analysis of how longer contexts degrade accuracy. This validation is a methodological strength, even though it does not fully resolve the evaluation independence concern.

## Weaknesses

### Fatal
None.

### Major

1. **Evaluation metric is provided by the same VLM that generates training rewards, creating a risk — partially but not fully addressed**

   The agent is trained to maximize rewards from Gemini-1.5-pro and then evaluated using the same Gemini model with the same prompt strategy. While Section 6.3 validates the evaluator against human judgments across different policies (<2% discrepancy), this does not fully rule out the possibility that the trained policy exploits specific patterns that satisfy Gemini's particular decision boundary without genuinely completing tasks. The validation tests the evaluator's correlation with humans on trajectories — it does not test whether the trained agent has learned to exploit evaluator-specific shortcuts. The paper would be substantially strengthened by: (a) human evaluation on the test set, (b) evaluation using a different VLM as an independent judge, or (c) programmatic verification on a subset of tasks. Without this, the headline 20% relative improvement claim carries residual uncertainty that goes beyond a normal methodological caveat.

2. **Hardware configuration for baselines is underspecified, making efficiency comparisons incompletely interpretable**

   The paper reports 3× training efficiency and 2.4× faster data collection relative to DigiRL, but does not specify the hardware setup used for the DigiRL baselines (single and multi). DistRL uses 4× V100 GPUs for the host learner and 2 worker machines with 192 vCPUs running 32 emulators. If DigiRL was evaluated with fewer resources, the speedups could partly reflect resource scaling rather than algorithmic or architectural advantage. The DigiRL-DistRL Async variant (DigiRL's algorithm in DistRL's framework) partially addresses this by isolating framework effects, but this variant is only reported in the training curves (Figure 3a) and never appears in the main results table (Table 1), making it impossible to fully separate framework effects from algorithm effects in the final success rate numbers. The paper should either match computational budgets or report normalized metrics (e.g., success rate per GPU-hour).

3. **Several components of the A-RIDE algorithm are insufficiently specified for reproducibility**

   - **Trajectory-level value estimator $V_{\text{traj}}$**: The paper says it "filter[s] the replay buffer to retain only high-value trajectories" (line 138), but provides no threshold, mechanism, or integration details. Does it discard trajectories entirely or reweight them? This component is also never ablated, so its individual contribution is unknown.
   - **Behavior policy $\mu$**: The policy loss (Eq. 1) uses importance sampling ratio $\rho_t = \pi(a_t|s_t)/\mu(a_t|s_t)$, but the paper never explains how $\mu$ is obtained or stored for trajectories collected asynchronously with outdated policies. This is essential for the off-policy correction to be implementable.
   - **Reward penalty on "unexpected behaviors like repetition"** (line 87): No formula, scaling factor, or detection method is provided. Since this affects the reward for every transition, it could substantially influence the learned policy.
   - **Retrace applied to $V$ instead of $Q$**: The paper applies Retrace-style corrections to the state-value function (line 173), which is a deviation from standard Retrace (which corrects $Q$). The paper does not justify why this is preferable or discuss how it interacts with the binary-classification formulation of $V(s)$ (a probability in [0,1]) receiving a real-valued correction.

   These gaps mean the algorithm cannot be independently reproduced, and the ablations (which remove only full components like DPER or Retrace) do not conclusively attribute the gains to the specific design choices.

### Minor

1. **Limited statistical testing**: Results are reported over three runs with standard deviations, but the paper does not perform statistical significance tests (e.g., Welch's t-test) for the key comparisons (73.2% vs. 61.2%). While the gap appears large, formal testing would strengthen confidence given the small number of runs.

2. **Missing ablations that would help attribute the gains**: The ablation study removes DPER and Retrace but not other components: (a) the trajectory-level value estimator $V_{\text{traj}}$ is not ablated, (b) no comparison against a simple off-policy baseline (e.g., DQN with prioritized replay) to benchmark A-RIDE's overall complexity, (c) importance sampling is not ablated (setting $\rho_t=1$) to test whether off-policy correction matters in this setting.

3. **No analysis of importance sampling ratio distribution**: The paper uses $\rho_t$ for off-policy correction but never reports its empirical distribution. If ratios are close to 1, the correction may be unnecessary; if large, variance could be high. Reporting this would help readers assess whether the Retrace correction is actually needed.

4. **Convergence curves lack variance shading**: Figure 3a-c show training curves without confidence intervals or shaded regions across runs. Adding these would help assess the reliability of observed gaps, especially for the wall-clock comparison.

### Trivial

None.

## Nice-to-Haves

- Human evaluation on a subset of the test set, or evaluation using a different VLM as independent judge.
- Hardware-matched baseline comparison with normalized metrics (success rate per GPU-hour).
- Including the DigiRL-DistRL Async variant in the main results table (Table 1) to separate framework gains from algorithm gains.
- Qualitative case studies showing trajectories where DistRL succeeds and DigiRL fails.
- Reporting the empirical distribution of importance sampling ratios $\rho_t$ during training.
- Adding a simple off-policy baseline (e.g., DQN with replay) to benchmark A-RIDE's sophistication versus simpler alternatives.

## Removed Points

These points are flagged to be removed and should be treated with caution:

- **Claim that advantage computation uses TD error, not advantage function**: The paper's formulation $A(s_t,a_t) = r + \gamma V(s_{t+1}) - V(s_t)$ is a standard one-step advantage estimate in actor-critic methods. The critic's assertion that this "is one-step TD error, not the advantage function" is factually incorrect. The TD error **is** a valid estimate of the advantage when $V$ is used as a baseline. → REMOVED (factually wrong)

- **Claim that single-CPU speed is not reported, making Figure 3d uninterpretable**: The paper explicitly states (lines 253-254) that the Ideal Upper Bound is "profiled by measuring the collection speed when a single CPU handles the task." The single-CPU measurement is performed; the numerical value is not printed in the text but is used to construct the plotted ideal bound. The figure is interpretable. → REMOVED (critic missed this detail)

- **Claim that AitW test set evaluation contradicts the paper's criticism of offline datasets**: The paper trains through online RL interactions and evaluates on a held-out AitW test set. Using a static test set for evaluation does not contradict the claim that static training data is insufficient for learning. The critic conflates the role of training data (which is collected online) with evaluation data (which is held-out for standardized comparison). → REMOVED (misunderstands paper)

- **Claim of inconsistency between "last screenshot + last two actions" and "last X images"**: The paper uses the last screenshot (1 image) + last 2 actions as its chosen input. Figure 4 validates this choice by plotting how accuracy varies with different numbers of images. There is no inconsistency. → REMOVED (misunderstands experimental methodology)

- **Criticism about missing appendix sections**: The parser strips appendix sections from all papers; they exist in the original submission. → REMOVED (per hard rules)

- **Generic strength about "practical problem"**: Strength Finder claimed "Practical problem: Online RL fine-tuning for mobile control agents is a relevant and under-addressed problem." This is too generic to be informative. → REMOVED (generic)

## Novel Insights

The most interesting observation emerging from this review is the tension between the paper's two core claims — efficiency and effectiveness. The training efficiency gains (3× faster, 2.4× more trajectories) are measured with objective, metric-independent methodologies (wall-clock time, trajectory counts, scalability curves) and constitute the stronger, less disputable contribution. The success rate improvements depend on the VLM-based evaluator that also provides the training reward, creating an evaluation independence issue that, while partially mitigated by human-validation (<2% discrepancy), introduces irreducible uncertainty. This asymmetry means the paper's strongest empirical contribution is the system architecture and its demonstrated scalability, not necessarily the absolute performance numbers. A productive framing for future work would be to separate the system contribution (asynchronous distributed framework) from the algorithmic contribution (A-RIDE) more sharply in evaluations.

## Suggestions

1. **Address the evaluator dependency** by either (a) conducting a human evaluation on a subset of test instructions to verify the 20% improvement holds under human judgment, or (b) reporting results using a second independent VLM evaluator (e.g., GPT-4V) alongside the primary Gemini-based metric.

2. **Specify the hardware configuration used for DigiRL baselines**, and either match computational budgets or report normalized metrics. Include the DigiRL-DistRL Async variant in the main results table to cleanly separate framework effects from algorithm effects.

3. **Fill the algorithmic specification gaps**: clarify the $V_{\text{traj}}$ filtering mechanism and threshold, explain how $\mu$ (behavior policy) is stored and accessed for importance sampling, provide the formula and scaling factor for the repetition penalty, and discuss how the Retrace correction interacts with the binary-classification formulation of $V(s)$.

4. **Add ablations for the trajectory-level value estimator** and for importance sampling (set $\rho_t=1$ as a baseline) to more rigorously attribute the gains.

5. **Add statistical significance tests** for the key comparisons and include variance shading on training curves.

## Score and Decision

This paper makes a genuine contribution in system design for distributed RL fine-tuning of mobile control agents. The asynchronous architecture is well-motivated, the scalability results are convincing, and the training efficiency improvements are objectively measured. However, the evaluation independence issue surrounding the main success rate claims, the underspecified hardware comparison, and the algorithmic reproducibility gaps are substantive concerns that prevent full acceptance of the central claims in their current form. The paper would benefit from a moderate revision addressing these issues, particularly the evaluator dependency and hardware specification.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>