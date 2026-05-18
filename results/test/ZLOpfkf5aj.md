Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the consolidated review.

## Summary

This paper introduces Sable, a cooperative MARL algorithm that replaces the attention mechanism in the MAT architecture with the retention mechanism from Retentive Networks (RetNets). Sable's key architectural innovation is that retention's recurrent/chunkwise formulations enable processing entire episode trajectories with a hidden state (temporal memory) while maintaining O(N) memory scaling with respect to agent count, compared to O(N²) for attention. The paper evaluates Sable across 45 tasks in 6 environments, achieving the highest mean return in 34/45 tasks, and demonstrates scaling to over 1000 agents on a custom environment (Neom) with linear memory usage.

## Strengths

- **Extensive and rigorous empirical evaluation.** Sable is tested across 45 tasks spanning 6 diverse environments (discrete and continuous action spaces, sparse and dense rewards), with 10 independent trials per task, 95% bootstrap confidence intervals, and per-environment aggregated probability-of-improvement metrics (Figure 2, Table 1). This is substantially larger than typical MARL evaluations.

- **Linear memory scaling with maintained performance.** The scaling experiments (Figure 4) show Sable using GPU memory comparable to the fully decentralized IPPO and dramatically less than MAT (which exceeds 80GB at 1024 agents), while maintaining stable learning — IPPO's performance degrades at scale but Sable's does not. This directly supports the central claim of combining memory efficiency with performance.

- **Effective temporal memory via retention architecture.** The ablation in Figure 5b demonstrates that Sable can chunk rollout trajectories up to 16× smaller than full length while preserving performance, confirming that its chunkwise retention mechanism efficiently captures long temporal context — a capability MAT lacks entirely.

- **Careful architectural adaptation of retention to MARL.** The paper makes nontrivial modifications to the retention mechanism for the MARL setting: equalizing decay across agents within the same timestep (no agent is "favored" by ordering), handling episode termination boundaries in the decay matrix, and constructing block-diagonal decay for full self-retention in the encoder. These adaptations are clearly motivated and mathematically specified (Equations 8–11).

- **Transparent reporting of confidence intervals and overlap.** Table 1 marks with asterisks when a method's CI overlaps with the best-performing method, allowing readers to assess statistical separation themselves.

## Weaknesses

### Fatal
None.

### Major

- **Abstract and conclusion conflate mean ranking with statistical significance.** The abstract states Sable "significantly outperform[s] existing state-of-the-art methods in the majority of tasks (34 out of 45, roughly 75%)" and the conclusion repeats this language. However, the 34/45 count comes from mean episode return ranking (Table 1, line 461: "Sable exceeds baseline performance on 34 out of 45 tasks"), not from the paper's own significance criterion (probability of improvement > 0.5 with all CI values > 0.5, line 342). Per-task inspection of Table 1 shows that many of Sable's wins involve overlapping confidence intervals — for example, on RWARE small-4ag, MAT achieves 13.39 vs Sable's 10.75; on RWARE xlarge-4ag, MAT achieves 3.24 vs Sable's 2.21. The proper claim is that Sable achieves the *highest mean return* in 75% of tasks, with *significant* improvement by the paper's own definition applying to a smaller, unstated subset. This is fixable by revising the abstract/conclusion wording to match what the evidence actually supports, but in its current form it is misleading.

### Minor

- **Ablation does not isolate whether retention itself or temporal memory drives gains.** The ablation (Figure 5a) tests whether MAT benefits from Sable's implementation details (RMSNorm, SwiGLU) and shows Sable still outperforms MAT-with-tricks. However, this compares Sable (retention + full trajectory processing) against MAT (attention, no temporal history). It does not separate whether the gains come from (a) the retention operator vs. attention, or (b) the ability to condition on entire episode histories versus single-timestep processing. A controlled comparison — e.g., Sable with hidden state zeroed each timestep vs. Sable with full temporal memory — would pin down the source of improvement. Without this, the attribution of gains to the core architectural innovation is partial.

- **Scaling experiments rely on a simple environment (Neom).** The 1024-agent scaling results are conducted on Neom, a custom environment where agents learn a periodic 1D pattern with a Manhattan-distance reward. The coordination problem is weak — agents mostly learn a repeated pattern independently. The paper acknowledges this limitation (Section 5.2, lines 473–474) but the conclusion (line 574) still presents scaling to 1000+ agents as a general capability without bounding the claim. LBF scaling to 128 agents is more realistic but still limited. The claim would be stronger with at least one scaling experiment on a non-trivial coordination task.

- **Throughput advantage is asserted but not systematically measured.** The paper claims "up to 6.5× faster" throughput than MAT (Figure 1, middle panel), but no dedicated experimental section describes how this was measured, for which tasks, or at which agent counts beyond the single number. Given the paper's emphasis on efficiency, this is a notable gap.

- **Key hyperparameter values not reported.** Despite 40 trials of TPE tuning per task, no table of tuned hyperparameters (learning rate, chunk size, number of RetNet layers, hidden dimension, etc.) is provided. This limits reproducibility and makes it hard to assess whether the comparison was fair across methods.

### Trivial

- **"Theoretical convergence guarantees" could mislead.** The paper states "Sable has theoretical convergence guarantees" (line 49), but these are inherited from the multi-agent advantage decomposition theorem (used identically by MAT and HAPPO). The paper clearly explains the connection (line 246), so it is not incorrect — but the phrasing may give the impression of a novel proof, which it is not.

## Nice-to-Haves

- A temporal-memory ablation (Sable with zeroed hidden state vs. Sable with full history) to isolate the contribution of retention itself vs. temporal context.
- Systematic throughput measurements across multiple agent counts and batch sizes.
- Memory usage analysis as a function of both agent count AND trajectory length.
- One scaling experiment on a more complex partially observable task (e.g., LBF with many agents) to complement Neom.
- A supplementary table of tuned hyperparameters for reproducibility.

## Removed Points

These points were raised by reviewers but are removed or downgraded per the review guidelines:

1. *"Theoretical convergence claim is not a new result"* — This is true but the paper already explains the connection to the advantage decomposition theorem. Trivial clarification, not a weakness.
2. *"Missing related works"* — Per guidelines, we cannot confirm existence of missing references; removed.
3. *"Missing appendix / proofs in appendix"* — These are parser-stripped sections; the original submission has them.
4. *"Comparison on MABrax is on-policy vs off-policy on unequal footing"* — The paper acknowledges this caveat (line 461: off-policy methods do ~15× more gradient updates) and notes this actually makes Sable's performance *more* impressive on MPE. This is already addressed.
5. *"Criticism about Sable tying with IPPO on SMAX"* — SMAX results show Sable ties IPPO on only 1/11 tasks (3s5z); on most SMAX tasks Sable leads or IPPO leads. The critic overstates the overlap.

## Novel Insights

The reviews surface two observations more interesting than the paper's own framing. First, the real tension is not "retention vs. attention" but "can you get the benefit of temporal history without quadratic cost" — Sable succeeds at this, but so might Transformer-XL or other recurrent variants applied to MAT. The paper's contribution would be sharpened by explicitly framing against this broader design space rather than just MAT. Second, the Neom environment, while simple, actually tests something important: whether shared-reward credit assignment can work at 1000+ agents. The fact that IPPO (decentralized) degrades at 1024 agents while Sable (centralized with temporal memory) maintains stable performance is arguably the most striking result in the paper and could be highlighted more.

## Suggestions

1. **Revise abstract and conclusion** to replace "significantly outperform" with "achieve the highest mean return" or "outperform in 75% of tasks" when referring to the 34/45 count. Reserve "significant" for tasks meeting the paper's own POI-based significance criterion.
2. **Add a controlled temporal-memory ablation** (Sable with hidden state reset each timestep vs. full Sable) to isolate the source of gains.
3. **Bound the scalability claims** explicitly: "Sable scales to 1000+ agents in environments with per-agent independent reward structure; scaling in tasks requiring complex coordination remains future work."
4. **Report throughput methodology** and measurements across agent counts to substantiate the 6.5× claim in the main text.
5. **Include a hyperparameter table** for all methods and tasks.

## Score and Decision

The paper makes a genuine contribution — adapting retention to MARL with careful architectural modifications is novel, the evaluation is thorough, and the memory/scaling results are convincing. The main weakness is overclaiming in the abstract/conclusion, which is easily fixable. The ablation gap is real but partial (the existing ablation still demonstrates retention beats attention with matched engineering tricks). I recommend acceptance with minor revisions to address the overclaiming and to add a clearer temporal-memory analysis.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>