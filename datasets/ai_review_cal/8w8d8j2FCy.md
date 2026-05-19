- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 8, 5, 6
Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper presents MENTOR, which introduces two complementary improvements to model-free visual RL: (1) replacing the standard MLP policy backbone with a mixture-of-experts (MoE) architecture to reduce gradient conflicts through modular expert specialization, and (2) a task-oriented perturbation mechanism that samples from a weight distribution formed by top-performing agents rather than random noise. The method is evaluated across 12 simulation tasks (DMC, Meta-World, Adroit) and three challenging real-world robotic manipulation tasks (Peg Insertion, Cable Routing, Tabletop Golf), consistently outperforming strong baselines including DrM, DrQ-v2, ALIX, and TACO.

## Strengths

- **Direct empirical evidence of gradient conflict reduction via MoE in multi-task settings**: Figure 2 (right) shows that the MoE agent maintains positive cosine similarity between gradients of opposing tasks, while the MLP agent exhibits frequent negative values. This provides direct evidence supporting the paper's core architectural claim, and is accompanied by expert usage analysis (Figure 2, left) showing task-specialized experts.

- **Validation that task-oriented perturbation yields useful candidates**: Figure 4(c) demonstrates that perturbation candidates sampled from the heuristically updated distribution achieve steadily increasing episode rewards (sometimes exceeding the agent's own reward), while random-noise candidates from DrM yield zero reward. This directly supports the paper's optimization claim.

- **Superior real-world performance with controlled ablation**: Table 1 reports MENTOR achieving an 83% average success rate across three real-world tasks versus 32% for DrM under equal training time. The ablation rows show that removing the MoE backbone or replacing task-oriented perturbation with random noise each causes approximately a 30% performance drop, confirming the individual contribution of both components.

- **Comprehensive simulated evaluation across multiple domains**: Figure 5 shows MENTOR outperforming four strong baselines on all 12 tasks spanning DMC (continuous locomotion), Meta-World (manipulation), and Adroit (dexterous manipulation), including sparse-reward and high-dimensional action space settings. Four random seeds are used for simulation experiments.

- **Time-efficiency comparison on real-world tasks**: Figure 6 reports that DrM requires on average 37% more training time to reach the same performance level as MENTOR, providing a practical efficiency metric beyond raw success rates.

## Weaknesses

### Fatal
None.

### Major

- **Key hyperparameters of the task-oriented perturbation mechanism are not reported, and the Gaussian assumption over weight space is not justified.** The algorithm relies on a set size \(N\) and perturbation interval \(T_p\) (both mentioned in the pseudocode, Algorithm 1, lines 137–145) and a per-weight Gaussian fit over the top-performing agents' weights. None of these values are specified anywhere in the paper, and the choice to model the high-dimensional weight distribution with an independent Gaussian (rather than, e.g., using the best agent directly or a weighted average) is not motivated or analyzed. Since the perturbation mechanism is one of the paper's two core contributions, these omissions prevent full assessment of its design robustness and make exact reproduction difficult.

- **Computational cost and model capacity are not compared against baselines.** The MoE architecture (16 experts, top-4 routing) likely has significantly more total parameters than a standard MLP, even if only a subset is active per forward pass. The paper does not report parameter counts, FLOPs per forward pass, or inference latency. This makes it difficult to disentangle whether gains come from the claimed gradient-conflict-reduction mechanism versus simply increased capacity. An ablation controlling for capacity (e.g., a wider or deeper MLP) would substantially strengthen the architectural claim.

### Minor

- **Gradient conflict reduction as an explanation for single-task improvement is only indirectly supported.** The paper provides strong gradient cosine-similarity evidence for the multi-task setting (Figure 2), but for single tasks (e.g., Assembly in Figure 3) the evidence is limited to expert activation patterns showing stage division. The paper's own framing (abstract, contributions) links gradient conflict alleviation to performance gains broadly, but for single tasks the mechanism is inferred rather than directly measured. The claim is reasonable and the expert specialization patterns are suggestive, but a direct gradient conflict comparison between MLP and MoE on a single challenging task would close this gap.

- **No load-balancing loss or expert usage entropy is reported for the MoE router.** In the MoE literature, an auxiliary load-balancing loss is standard to prevent expert collapse, where the router assigns all inputs to a small subset of experts. The paper shows expert specialization (Figure 3) without discussing whether this emerges naturally or whether collapse was observed during training. Reporting expert activation entropy or adding a load-balancing loss would improve the MoE contribution's rigor.

- **Real-world experiments lack training seed information.** While simulation experiments use four random seeds (stated in the Figure 5 caption), the real-world experiments do not report the number of training seeds. Only evaluation rollouts are described ("each subtask in Peg Insertion is rolled out 10 times, while Cable Routing and Tabletop Golf are rolled out 20 times"). Acknowledging the seed count (even if 1 due to cost) and discussing variability would improve credibility.

- **Learning curves for real-world tasks are not shown.** Only final success rates (Table 1) and a time-efficiency comparison (Figure 6) are provided. Learning curves showing success rate over episodes for all compared methods would make the efficiency gains transparent and address concerns about whether the large gap (e.g., 1.0 vs 0.1 on Arrow peg) reflects sample efficiency versus other factors.

### Trivial
None.

## Nice-to-Haves

- A direct gradient conflict comparison (cosine similarity) between MLP and MoE on a single challenging task (e.g., the Assembly task already analyzed) would directly support the gradient-conflict-reduction claim for single-task settings.
- A hyperparameter sensitivity study for the set size \(N\) and perturbation interval \(T_p\) on a simulation task (e.g., Hopper Hop) would demonstrate robustness and guide practitioners.
- Adding a load-balancing loss or reporting expert usage entropy would align with MoE community standards and strengthen the architectural contribution.
- Including an ablation of MoE alone (without task-oriented perturbation) in simulation benchmarks, paralleling the real-world ablation in Table 1, would further isolate the contribution of each component.

## Removed Points

- **"The real-world experiments raise questions about fair comparison (different environment steps per wall-clock time)"** — Removed because the paper already provides a time-efficiency comparison (Figure 6) showing DrM requires 37% more training time to match MENTOR's performance, and the critic's concern about MENTOR potentially processing fewer steps (due to MoE overhead) would actually make the comparison *conservative* (favoring DrM). The concern is speculative and partially addressed.
- **"The gradient conflict framing in the introduction sets up a dichotomy not fully resolved"** — Removed as a stylistic/general observation that does not identify a concrete flaw with the paper's contribution or execution.
- **"The set updates based on a single noisy episode reward without smoothing"** — This is a design description, not a weakness. The set update rule is clearly specified in Algorithm 1; the critic's concern about "noisy" rewards is a speculation about what *might* go wrong rather than an identified problem.
- **"The number of real-world seeds is not reported (appears to be a single training run)"** — Included in Minor weaknesses above (seed information not reported), but the critic's speculation ("given the cost") is removed as not grounded in paper content.
- **Strength Finder: generic/superficial framing dropped** — The Strength Finder's summarization language framing certain results as "single most important evidence" is kept only where associated with concrete, specific evidence (Table 1). Generic superlatives without specific citation are dropped.

## Novel Insights

The harsh critic's most insightful observation is the disconnection between the multi-task gradient conflict analysis (which is clean and well-supported) and the single-task application (where the same mechanism is claimed but evidenced only through qualitative expert activation patterns). This reveals a broader pattern in the paper: the two contributions are validated at different levels of rigor. The perturbation mechanism is validated through both quantitative (Figure 4) and ablation (Table 1) evidence, while the MoE contribution — though clearly effective in aggregate — lacks a targeted ablation controlling for capacity and lacks direct mechanism validation for single-task settings. The Strength Finder correctly identifies that the real-world experimental result (Table 1) is the paper's strongest evidence, as it combines both contributions in a practically demanding setting that few prior visual RL papers attempt.

## Suggestions

1. Report the specific values for \(N\) (set size) and \(T_p\) (perturbation interval) used in all experiments, and provide a brief discussion of the Gaussian independence assumption over the weight space.
2. Include parameter counts and a rough inference-time comparison between MENTOR and the MLP-based baselines, so readers can assess whether gains are driven by capacity or the claimed gradient-conflict mechanism.
3. Add a gradient cosine similarity comparison between MLP and MoE on at least one single challenging task (e.g., Assembly) to directly support the gradient-conflict-reduction claim for single-task scenarios.
