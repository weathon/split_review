## Summary

The paper proposes a decentralized training framework that combines parameter-server architectures, pipeline parallelism (with frontal/backward servers), and a task-pool scheduling mechanism to train transformer models across heterogeneous, unreliable internet-connected devices. The framework separates devices into reliable (parameter servers) and unreliable (clients) groups, uses a task pool to handle device disconnections, and employs hierarchical graph clustering with simulated annealing for pipeline stage allocation. Controlled experiments show up to 1.3× speedup over Swarm, and a real-world deployment trains across cloud HPCs and consumer GPUs.

## Strengths

- **Novel task-pool mechanism for handling device disconnections without data reiteration**: The framework maintains a coordinated task pool in both frontal and backward servers that detects unresponsive clients via timeout, posts unfinished tasks, and lets other clients pick them up by recomputing activations from paired gradients (Section 3.2.1, "Task Pool"). Controlled experiments (Section 4.2) validate this design with up to 1.3× speedup over Swarm, especially at 50–60% disconnection rates and higher unreliable-device ratios, where baselines "must reiterate the lost training data when the original device disconnects."

- **Real-world validation on genuinely heterogeneous internet-connected GPUs**: The paper trains across cloud HPC (RTX 4090s), campus HPC (RTX 4090s), and six consumer RTX 3080s connected via commodity ISP with a custom VPN for NAT traversal (Section 4.4). Actual end-to-end bandwidth and latency are measured across all device pairs (Figure 3). This goes substantially beyond simulation-only evaluations typical in prior decentralized training work.

- **Formal latency model enabling scheduling where standard DP-based approaches fail**: Equations 1–2 provide a closed-form cost model for data-parallel and pipeline time under heterogeneous communication. The paper correctly identifies that prior DP-based schedulers (DAPPLE, PipeDream) rely on optimal substructure that "does not exist" because the graph "lacks a defined axis" (Section 3.3.3), motivating a graph-clustering formulation.

- **Systematic scalability evaluation under high disconnection rates**: The paper scales from 8 to 32 V100 GPUs with 50–150ms latency variation, 100–300 Mb/s bandwidth variation, and 50–90% per-batch disconnection probability, comparing against Swarm and Dapple, with 30 trials per configuration (Section 4.3).

## Weaknesses

### Fatal
None.

### Major

1. **Real-world experiment does not compare against any baseline method.** The real-world experiment (Section 4.4) only compares three configurations (2, 3, and 4 stages) of *the proposed method itself*. There is no comparison against Swarm, DeDLOC, PipeDream, or any alternative. The experiment thus tests whether the scheduler's choice of stage count is sensible, but it does **not** test whether the overall framework outperforms existing approaches in a realistic setting. The paper's central claim—that the framework enables training that would otherwise be infeasible or slower—is not supported by this experiment. This is a significant evidential gap.

2. **Model identity and hyperparameter confusion.** The paper claims to train "Llama-33B" (citing Touvron et al. 2023) with "hyperparameters similar to those in the original paper Lan et al. (2019)" (Section 4.4). (a) "Llama-33B" is not a standard variant: Llama 1 (Touvron et al. 2023) comes in 7B/13B/30B/65B; Llama 2 in 7B/13B/70B; Llama 3 in 8B/70B/405B. "33B" does not match any cited source. (b) Lan et al. (2019) is the ALBERT paper, not the Llama paper—referencing it for Llama hyperparameters is incoherent. It is unclear what model was actually trained and what training configuration was used. This is a serious reproducibility concern for a paper whose primary experimental evidence is training a stated model.

### Minor

1. **The scheduler's "near-optimal" claim is not well-justified.** The pipeline time approximation used in hierarchical clustering (Equation 3, line 176) assumes perfect load balance ($DT_k \approx \frac{B|H|}{d p \sum C_s}$), which is circular—load balancing is precisely what the scheduler is supposed to achieve, not a premise to assume. The approximation also discards intra-cluster communication, justified by saying clustering "minimizes the distance within the cluster," but cluster distance and pipeline time are not the same objective. The stopping criterion likewise depends on this approximation. While heuristic approaches are reasonable for a systems paper, the language ("near-optimal," "optimal configuration") overstates the rigor of what is provided.

2. **No variance or confidence intervals reported.** The scalability experiment was run 30 times (Section 4.3), but only averaged results are reported. Given the extreme disconnection probabilities (50–90% per batch), variance is likely substantial. Without any measure of spread, it is impossible to assess whether observed improvements over baselines are statistically significant or within noise.

3. **Several experimental design details are underspecified.** The paper does not report: simulated annealing hyperparameters (temperature schedule, number of iterations), task-pool timeout values, learning rate schedule, optimizer used, or training duration. The "customized VPN" is mentioned but not described. These omissions hinder reproducibility.

4. **The disconnection model is extreme and undiscussed.** Devices have a 50–90% per-batch probability of disconnection with reconnection in the next batch (Section 4.3). This models devices flapping in and out every 1–2 batches, which is an extreme scenario that may not correspond to real internet behavior (where disconnections tend to be correlated in time). The paper does not discuss this modeling choice or its representativeness.

### Trivial
None. (Issues flagged in the raw text extraction are parser artifacts, not paper errors.)

## Nice-to-Haves

- Include at least one baseline comparison (Swarm or DeDLOC) in the real-world experiment. This is the single change that would most strengthen the paper.
- Report numerical throughput values (tokens/sec) and scaling efficiency percentages in the text alongside figures.
- Discuss how the DPU asynchronous scheme interacts with the task-pool mechanism in terms of gradient staleness and convergence behavior.

## Removed Points

These points were raised in the input reviews but are removed or demoted per the filtering rules:

- **"Swarm using the same allocation as the proposed method is unfair"** (Harsh Critic Point 2): REMOVED. The asymmetry favors the baseline (Swarm receives the authors' optimized allocation), which is a stronger test for the proposed method.
- **"Results are inaccessible because they are in figures"** (Harsh Critic Point 1): DEMOTED. Figures are the standard presentation format in papers. The valid sub-concern (no numerical tables in prose) is addressed in Minor weaknesses.
- **"Misses related work on federated learning, gradient compression"**: REMOVED per the rule prohibiting claims about missing related works without external sources.
- **"Equation 1 is a descriptive identity"**: DEMOTED into Minor weakness 1. The equation is a standard cost model; the real issue is the gap between it and the "near-optimal" claim.
- **"Typos and formatting issues"**: REMOVED per the rule that text-extraction artifacts are not author errors.
- **Strength Finder's generic praise** (e.g., "addressing an important problem"): REMOVED as generic/superficial.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Clarify the model identity: state exactly which model variant was trained, with correct parameter count and citation. If it is Llama-30B, correct the number; if a non-standard variant, explain.
2. Add a baseline comparison (Swarm or DeDLOC) to the real-world experiment. This is the highest-priority improvement.
3. Report numerical results (throughput in tokens/sec, loss values, scaling efficiency) with confidence intervals, especially for the 30-run experiment.
4. Replace "near-optimal" / "optimal" language with "heuristic" or "approximate" to accurately describe the scheduling approach.
5. Specify all training hyperparameters, optimizer, learning rate, batch size per device, simulated annealing schedule, and timeout values.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>