- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3
Now I have all the information I need. Let me produce the final review.

## Summary
This paper proposes an end-to-end reinforcement learning framework for the Flexible Job Shop Problem (FJSP) that couples a generative model (which assigns operations to machines step-by-step) with an improvement model (which refines partial solutions by reinserting operations), trained jointly via DuelingDQN. The use of graph attention networks (GAT) enables handling of variable-size instances. An ablation experiment (Table 3) shows that using both models together outperforms either model alone.

## Strengths
- **Joint training of generation and improvement is validated by ablation.** Table 3 shows that the combined framework achieves lower makespan than using only the generation model or only the improvement model (with any initial solution). This directly supports the paper's central architectural contribution.
- **The GNN-based architecture enables variable-size input processing.** By using GAT with non-square adjacency matrices for insertion positions, machine queues, and job sequences, the model can handle FJSP instances of different sizes without architectural modification — a clear advance over MLP/CNN-based DRL methods that are tied to fixed-size inputs.
- **Ablation on training data diversity shows value.** Table 4 provides evidence that training on a more diverse set of small instances (adding 5×3 data to 10×5 data) improves performance on unseen test sizes, supporting the claim that the paradigm can benefit from broader training data.
- **Performance on public benchmarks is competitive with prior DRL methods.** On two standard FJSP benchmarks (Table 2), the method shows makespan values comparable to cited DRL approaches [29,30].

## Weaknesses

### Major
- **Baseline comparison on random instances is limited to PDR heuristics only (Table 1).** Priority dispatching rules are simple, fast heuristics known to produce low-quality solutions. Outperforming them is necessary but not sufficient to demonstrate an advance. The paper does not compare against any constructive search, meta-heuristic, or re-implemented DRL method on these random instances. This significantly weakens the claim of "better performance."

- **Runtime claims against meta-heuristics are unsupported.** On public benchmarks (Table 2), the paper admits that RGA and 2SGA achieve better makespan, then claims "the calculation time we spent was much less than that of these meta-heuristic methods" — but provides **zero runtime numbers** for RGA or 2SGA. Without this data, the "shorter time" part of the paper's central claim is unsubstantiated.

- **Comparison with prior DRL methods on public benchmarks is unreliable.** The paper states it "directly cited the best data from the articles for comparison." This means differences in compute hardware, training setup, hyperparameter tuning, and instance preprocessing are uncontrolled. The reported advantages may reflect experimental confounds rather than genuine algorithmic superiority.

- **Generalization experiments do not demonstrate "superior generalizability."** The largest test instance is 10×10 (Table 4). Testing on instances of similar or only slightly larger size than training (5×3, 10×5) does not constitute a meaningful generalization evaluation. The paper would need to test on substantially larger instances (e.g., 20×10, 30×20, 50×20) to support the strong generalization claim.

- **Reward formulation for the generative model is unexamined.** The generative model receives a reward equal to the difference in \(C_{\max}\) of the *partial* solution after adding one operation. The makespan of a partial schedule (computed only over assigned operations) may not correlate well with the final makespan, since later assignments can shift critical paths. This is a known pitfall in constructive RL for scheduling. The paper provides no analysis, ablation, or alternative reward design to validate this choice. If the proxy reward misleads learning, the generative model's policy may be suboptimal regardless of the joint training.

### Minor
- **No variance or statistical significance reported.** All tables report single values (presumably averages), with no standard deviations, confidence intervals, or information about number of runs. Given the stochastic policies and random instance generation, the reader cannot assess whether reported differences are meaningful or within noise.
- **Random instance generation procedure is not described.** The paper says instances are "randomly synthesized" but does not specify the distributions used for processing times, machine compatibilities, or job lengths. This hinders reproducibility.
- **The improvement model's step count function \(n_t\) is never defined.** The paper describes it as "a hand-craft function related to the order of step \(t\)" but provides no explicit formula or schedule. This directly affects the runtime and behavior of the method.
- **No sensitivity analysis for key hyperparameters.** The exchange interval \(K=500\) and experience pool capacity of 5000 are given without motivation or ablation. Whether performance is robust to these choices is unknown.
- **Gurobi gap metric is ambiguous.** Table 1 reports "Gap to Gurobi Solver" without specifying the solver's time limit, optimality tolerance, or whether the reported gaps are for provably optimal solutions. For larger instances, Gurobi's own gap may be non-zero, making the metric uninterpretable.
- **No comparison of generation model alone with beam search.** A natural baseline — using the generative model with beam search (keeping top-k partial trajectories) — is absent. Such an experiment would isolate whether the improvement model adds value beyond generating multiple candidate solutions. The paper only compares the full framework to the generative model used greedily.
- **State representation uses average pooling without discussion.** The paper pools all operation node embeddings via mean pooling to form the state vector. Alternative aggregation methods (e.g., attention-based readout) could better preserve structural information; the paper does not justify this design choice.
- **No discussion of limitations.** The paper does not acknowledge that the improvement model's single-operation reinsertion move may struggle to escape local optima, or discuss the computational overhead of the \(n_t\) improvement steps.

### Trivial
- Training episode count is inconsistent: line 179 states max episodes \(E=200000\) while line 188 says the optimal model used 100,000 episodes.

## Nice-to-Haves
- Report wall-clock runtime for all baseline methods (meta-heuristics and DRL) under the same hardware conditions.
- Re-implement or run prior DRL methods and a simple genetic algorithm on the same instances for a fair comparison.
- Test on substantially larger instances (20×10, 30×20, 50×20) to substantiate the generalization claim.
- Run an ablation where the generative model receives a different reward (e.g., terminal reward only, or proxy gap to a lower bound) and compare learning curves.
- Report results over 5–10 random seeds with variance.
- Explicitly define the \(n_t\) function and study its sensitivity.
- Add an ablation comparing the generative model with beam search vs. the full framework.

## Removed Points
*(These points are flagged to be removed; treat them with caution.)*

- **"Generalization-Improving Model" section title typo** — Removed as a formatting/typo point per policy.
- **"GAT for non-square adjacency matrices needs clearer explanation"** — Removed because the paper already explains this limitation: "since \(A_J\) is not a square matrix, the GAT layers cannot be stacked" (lines 114-130). The paper adequately describes the use of single-layer GAT for non-square cases.
- **"Table 2 is visually garbled"** — Removed as a parser artifact.
- **"GAN/BERT-like joint training comparison missing"** — Removed as a strawman; the paper does not claim similarity to GAN or BERT training.
- **"Missing related works"** — Removed per policy (cannot verify external knowledge).
- **"Missing related works details in appendix"** — Removed per policy (appendix stripped by parser).
- **"GAT attention heads not specified"** — The paper specifies number of layers, embedding dimension, and other architectural details; the number of attention heads is a common omitted detail but falls under the "trivial hyperparameter" category per policy. Removed.

## Novel Insights
The harsh critic identifies a genuine tension in the paper: the joint training of generation and improvement models is a plausible and interesting idea, but the evaluation is insufficient to support the strong claims made. The most interesting observation is that the paper's own Table 2 implicitly concedes that meta-heuristics produce better solutions — the paper's defense is runtime, but no runtime data is provided. This creates a situation where the paper's headline claims ("better performance in shorter time" and "superior generalizability") are neither fully supported nor fully refuted by the evidence presented, placing the paper in a zone where additional experiments could potentially redeem it but the current submission does not meet the evidentiary bar.

Beyond the paper's own contributions, the reviews converge on a consistent diagnosis: the framework design is reasonable, the ablation is informative, but the experimental scope is too narrow for the claims made. No genuinely novel insight emerges beyond this.

## Suggestions
1. **Expand baseline comparison.** At minimum, re-implement or run one meta-heuristic (e.g., a standard GA) and one prior DRL method [29,30] on the same random and public instances, reporting both makespan and wall-clock time.
2. **Test on truly larger instances.** Evaluate on e.g., 20×10, 30×20, and 50×20 Brandimarte or Hurink instances to support the generalization claim.
3. **Report variance.** Run all stochastic methods over multiple seeds and report standard deviations or interquartile ranges.
4. **Define \(n_t\) explicitly** and justify the choice of \(K=500\) with a sensitivity analysis.
5. **Describe the random instance generation procedure** (processing time distributions, machine compatibility rates, job length distributions) to enable reproducibility.
6. **Clarify the Gurobi gap metric** by specifying the solver configuration (time limit, MIP gap tolerance).
7. **Acknowledge limitations** — the single-operation reinsertion move, potential reward misalignment in the generative model, and computational cost of improvement steps.
