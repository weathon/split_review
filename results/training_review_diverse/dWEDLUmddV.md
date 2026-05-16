## Summary

This paper identifies a previously overlooked problem in trajectory-matching dataset distillation: matching different segments of the expert trajectory can exhibit negative correlations, which leads to an increase in accumulated trajectory error. The authors provide a theoretical analysis (Theorem 1) linking negative correlations to accumulated error, empirically characterize these correlations across different IPCs using Pearson correlation coefficient heatmaps, and propose ConTra—a concurrent training strategy that simultaneously matches multiple trajectory segments using multi-task learning. The method consistently outperforms prior TM-based methods (MTT, DATM) on CIFAR-10/100, Tiny ImageNet, and serves as a plug-in module improving existing methods by 0.3–3.6%.

## Strengths

- **Identifies and quantifies a genuinely overlooked problem in TM-based dataset distillation.** The paper systematically demonstrates that matching different trajectory segments exhibits negative correlations (Figure 2, Section 4.2) and provides a cogent explanation of why this occurs and how it varies with IPC. This goes meaningfully beyond prior work (MTT, DATM, FTD) that treated segment matching as independent.

- **Validates concurrent training as both a standalone method and a plug-in module.** Table 1 shows ConTra surpasses DATM by 3.1%/1.5% on CIFAR-10 at IPC 1/10. Critically, Table 3 shows that simply adding concurrent training to MTT yields gains of 1.1–3.6%, and to DATM yields 0.3–1.6%. This directly demonstrates that the negative correlation problem is real and the proposed fix is broadly applicable.

- **The theoretical framing (Theorem 1) provides a clean formalization** of how negative correlations can cause accumulated trajectory error to increase rather than decrease when segments are matched sequentially. The decomposition of accumulated error into matching errors + initialization errors is a useful conceptual tool for the community.

- **Thorough empirical characterization of correlation patterns.** The paper shows that negative correlations shift from the lower-triangular region (small IPC) to the upper-triangular region (large IPC), and provides a plausible explanation based on training dynamics and information capacity. Figure 3 further shows that ConTra converts negative correlations to positive ones across nearly all segments.

- **Ablation studies isolate key design choices.** The analysis of number of tasks K (Figure 4, left), balance coefficient β (Figure 4, right), and curriculum learning (Table 4, left) each support the motivated design of ConTra.

- **Cross-architecture generalization results (Table 2)** show ConTra achieves the best performance among TM-based methods across several popular model architectures (ResNet, VGG, etc.).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The causal link between negative correlation and accumulated error is plausible but not directly measured.** Theorem 1 decomposes the accumulated error, and the paper argues that negative correlations cause minimizing one δ_i to increase others, potentially raising ε_{T-1}. However, the paper never directly measures ε_{T-1} under sequential vs. concurrent training to confirm this mechanism. The evidence is instead indirect: concurrent training produces positive correlations (Figure 3) and better final accuracy (Tables 1, 3). Directly measuring the accumulated error during evaluation would strengthen the claimed mechanism.

2. **The correlation analysis uses a single reference trajectory τ_o.** Section 4.2 establishes "a complete τ_o as the reference trajectory" for computing PCC heatmaps. It is not shown whether the correlation patterns are consistent across different expert trajectories (different random seeds, different model initializations). If the negative correlation structure is highly variable, the proposed remedy might not generalize as cleanly. Reporting mean/variance across multiple trajectories would strengthen the claim that negative correlation is "prevalent."

3. **No analysis of gradient conflicts during concurrent training.** The paper's key claim is that concurrent training resolves negative correlations, but it does not analyze whether the gradients from different segment losses actually conflict during joint optimization. Directly measuring the cosine similarity between gradients of different segment losses during training would provide direct evidence for the claimed mechanism. The ablation on β partially addresses this, but gradient-level analysis is absent.

4. **The continual-learning framing is somewhat rhetorical.** The paper frames concurrent training as derived from the continual-learning insight that MTL is an "upper bound" and SL a "lower bound." However, the method is straightforwardly multi-task learning applied to trajectory segments—a natural idea once the problem is identified. The continual-learning framing does not generate testable predictions or design decisions beyond what MTL already provides. The paper mentions trying EWC and SI ("they do bring some improvements") without presenting the numbers, which makes it hard to evaluate whether this framing is empirically grounded or merely post-hoc.

5. **The Pearson correlations in Section 4.2 may partly reflect overall optimization dynamics.** The matching losses for different epochs all depend on the same evolving synthetic dataset S. When the synthetic dataset converges, losses for all segments decrease together—producing positive correlation—regardless of whether the segments genuinely "conflict." The paper should acknowledge this confound and discuss how it was accounted for in interpreting the negative-correlation signal.

6. **Cost analysis needs clarification on memory.** The paper claims "ConTra does not incur additional GPU memory costs, as we can compute the gradient of different tasks and backpropagate them separately." Separate backpropagation (sequential backward passes with gradient accumulation) does reuse memory, but the statement as written could be misinterpreted. A brief clarification of the implementation (e.g., "using gradient accumulation across segments with no added memory budget") would resolve this.

### Trivial
None.

## Nice-to-Haves

- A comparison to uncertainty-weighted multi-task learning (Kendall et al., 2018) or dynamic prioritization for combining segment losses would contextualize the choice of simple averaging.
- A study of how the optimal number of tasks K varies with IPC across CIFAR-100 and Tiny ImageNet (currently only shown on CIFAR-10, Figure 4 left) would increase confidence in the method's robustness.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Section 6.6 provides unsubstantiated claims about ImageNet-1K, NAS, and ViT generalization without results."** — The cross-references in Section 6.6 (e.g., "1.5", "2", "3", "4") appear to point to appendix content that the parser strips. Per hard rules, weaknesses about missing appendix content are removed.

2. **"EWC and SI experiments are not presented."** — The paper mentions these experiments qualitatively. This is a brief acknowledgment of attempted alternatives, not a core missing experiment. The point is subsumed by Minor #4 (rhetorical framing) at reduced severity.

3. **"Concurrent training's novelty is overstated because it's just MTL."** — The paper never claims MTL is a novel training technique; it claims that *identifying the negative correlation problem and framing trajectory matching as continual learning* is novel, and that MTL is the natural solution. This is an accurate description, not overstatement. However, the rhetorical strength of the continual-learning framing is a valid concern (kept as Minor #4).

4. **"Missing comparison to other multi-task variants."** — This is scope creep / a nice-to-have, not a weakness.

## Novel Insights

The reviews converge on a perspective that goes slightly beyond the paper's own framing: the paper's most valuable contribution is not the concurrent training method itself (which is straightforward MTL) but rather the *diagnosis* that trajectory-segment matching exhibits structured negative correlations, that these correlations shift characteristically with IPC, and that this explains why prior TM methods underperform at low IPC. The real insight is that the trajectory-matching objective is implicitly a multi-objective optimization problem—each segment is a conflicting objective—and naive sequential optimization is provably suboptimal. This reframing has implications beyond the specific ConTra method: any future TM method would do well to account for inter-segment correlations rather than treating them as independent.

## Suggestions

1. **Directly measure ε_{T-1}** (the accumulated error from Definition 1) for the sequential sampling baseline and for ConTra. A plot of accumulated error over training iterations would directly confirm the claimed mechanism and is the single most impactful addition.
2. **Report correlation heatmaps with mean/variance across multiple expert trajectories** (different random seeds) to strengthen the claim that negative correlation is a general phenomenon.
3. **Present results for EWC/SI in a small table** or remove the claim to avoid unverifiable statements.
4. **Clarify the memory cost claim** in Section 6.5 by specifying that gradient accumulation is used across segments.
5. **Acknowledge the confound** in Section 4.2 that Pearson correlations between losses of different epochs on the same evolving synthetic dataset partly reflect overall convergence dynamics.

## Score and Decision

The paper identifies a real and consequential problem in trajectory-matching dataset distillation, provides a thoughtful analysis, and proposes a simple, effective, and generalizable solution validated on standard benchmarks. The weaknesses are not structural: they concern depth of evidence (direct ε measurement, multi-trajectory analysis, gradient conflict analysis) rather than validity of the core claims. The paper would be a strong addition to the dataset distillation literature.

**Originality:** Good — the negative-correlation diagnosis is novel and non-obvious.  
**Importance:** Good — addresses a bottleneck in a popular method class.  
**Claims supported:** Mostly — core empirical claims are well-supported; the causal mechanism has indirect support.  
**Soundness:** Good — experiments are properly controlled, ablations are thorough.  
**Clarity:** Adequate — writing is clear; Section 6.6 cross-references are garbled (parser issue).  
**Value to community:** Good — the plug-in nature means the method can be immediately adopted.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>