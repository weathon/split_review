## Summary

This paper identifies "disguised procedural unfairness"—the problem that standard causal fairness methods can inadvertently alter neutral (non-problematic) components of the data-generating process while also failing to ensure the greatest benefit for the least advantaged. The authors propose a decoupling framework that uses *reference points* (fixed values assigned to tail nodes of objectionable edges) together with a value-instantiation rule, and configures those reference points via optimization to maximize outcomes for the least advantaged, operationalizing Rawls's Difference Principle. The paper provides a formal linear illustration and one real-data demonstration on UCI Adult.

## Strengths

1. **Clear identification and formal illustration of a genuine, overlooked problem (disguised procedural unfairness).** Section 3 (Figures 1 and associated matrices) concretely shows that enforcing existing causal fairness constraints (Kilbertus et al., Nabi & Shpitser, Chiappa) can arbitrarily alter neutral data-generating components — a violation they quantify via signed relative deviations in a heat map. This is not a speculative critique; the paper traces the exact mechanism.

2. **Principled decoupling framework with a well-specified algorithmic procedure.** Algorithm 1 (Value Instantiation Rule) provides a step-by-step procedure that assigns reference points to inputs of objectionable edges while leaving neutral edges intact (using downstream values or original data values). Algorithm 2 shows how to aggregate local causal modules. The framework handles non-additive models via the "direct correction" option and is grounded in causal modularity.

3. **Operationalization of Rawls's Difference Principle as a tractable optimization problem.** Equation (4) formulates the configuration of reference points as an argmax over the Cartesian product of tail-node domains, maximizing the expected predicted outcome for the least advantaged. This connects a philosophical principle to a concrete computational procedure.

4. **Demonstration that decoupling does not reduce to flipping the protected feature.** The UCI Adult experiment (Section 5.2) finds that the reference point for the edge *marital status* → *income* is set to "married," while the edge *sex* → *income* does not flip sex. This is an interesting and non-obvious result showing the method identifies actionable components beyond canonical protected attributes.

## Weaknesses

### Fatal
None.

### Major

1. **Insufficient empirical evaluation to support the claimed effectiveness of the framework.** The experimental evidence consists of: (a) a simulated linear example that is purely illustrative, and (b) one real-world dataset (UCI Adult) compared against **a single baseline** (Path-Specific Counterfactual Fairness, Chiappa et al., 2019). No comparisons against other causal fairness methods (e.g., approaches from Kilbertus et al., Nabi & Shpitser, Kusner et al., or any non-causal fairness baselines) are provided. The paper claims the framework "boosts approval rates" and "provides more opportunities for the least advantaged," but with only one comparator it is impossible to assess whether this advantage is robust or coincidental.

2. **No statistical variability or uncertainty reported.** All results are presented as point estimates without confidence intervals, standard deviations across runs, or significance tests. This is particularly concerning given that the reference-point optimization (Equation 4) involves a search over discrete configurations — the stability of the selected configuration across random seeds or different data splits is not examined.

3. **No ablation or sensitivity analysis for critical design choices.** The framework requires specifying (i) which edges are "objectionable," (ii) the causal graph structure, and (iii) the optimization over reference-point values. The paper does not study how results change when different sets of edges are designated as objectionable, how sensitive the outcome is to errors or incompleteness in the causal graph, or how the reference-point optimization behaves under different optimization strategies. These are not minor concerns: a framework whose outputs depend heavily on untested design choices has unclear practical reliability.

### Minor

1. **Single baseline obscures the fairness-accuracy trade-off.** The comparison against PSCF shows that the proposed method improves approval rates for females, but the paper does not report the corresponding accuracy (or any utility metric) for the unconstrained baseline, PSCF, or the proposed method. Without understanding the accuracy cost, it is difficult to evaluate practical viability. Even a simple table reporting accuracy and group-wise acceptance rates across methods would help.

2. **Specification burden is significant with limited guidance.** The method requires a known causal graph, a specified set of objectionable edges, and discrete optimization over reference-point values. The paper acknowledges this is a framework rather than a drop-in tool, but it does not provide practical guidance on how practitioners should identify objectionable edges, how to proceed when the causal graph is uncertain, or what the computational cost of the optimization is (especially as the number of objectionable edges grows). This limits the paper's actionable contribution.

3. **UCI Adult dataset is dated.** While not a fatal issue, the Adult dataset from 1994 has known shortcomings (Ding et al., 2021). Given the conceptual nature of the contribution, this is acceptable for a proof-of-concept, but it weakens the force of the empirical demonstration.

### Trivial
None.

## Nice-to-Haves
- A second real-world experiment on a modern dataset (e.g., ACSIncome) would substantially strengthen the empirical case.
- An ablation varying which edges are designated as objectionable would clarify the framework's robustness.
- Reporting accuracy alongside fairness metrics would help assess the fairness-accuracy trade-off.
- A discussion or experiment on how errors/incompleteness in the causal graph affect the framework's outputs.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"No evidence this framework works as claimed"** (*Harsh Critic* — removed as too broad/overstated). The paper does provide some evidence: both the linear illustration (conceptual validation) and the UCI Adult experiment (limited empirical validation) support the claims. The weakness is properly framed above as *insufficient* evidence, not *no* evidence.
- **"Method introduces significant complexity"** (*Harsh Critic* — removed from weakness section, partially captured as Minor #2). This is inherent to the method's nature as a principled framework; it is better expressed as a practical limitation (see Minor #2) rather than a weakness of soundness.
- **"Not yet released / cannot be independently verified"** (*Harsh Critic implicit framing* — removed per Hard Rules). The paper cites existing models, tools, and datasets; questioning their existence is not permitted.
- **Strength Finder generic strengths** — Strengths like "the paper addressed an important problem" (present in several strength finder entries) have been dropped as too generic. Only concrete, paper-specific strengths are retained.

## Novel Insights
The most interesting observation across the reviews is that the paper's core contribution is genuinely conceptual — identifying disguised procedural unfairness as a failure mode distinct from outcome-based unfairness — rather than algorithmic. This is both the paper's greatest strength and the source of its evaluation gap. The reviews highlight an interesting asymmetry: a conceptually novel paper in fairness can receive valid criticism for thin experiments without that criticism invalidating the conceptual contribution. This suggests that the main value of the paper may lie in reframing how the community thinks about procedural fairness constraints, more than in the specific algorithmic framework proposed. The finding that reference points do not reduce to flipping the protected attribute (Section 5.2) is a specific, actionable insight that could inform how future procedural fairness methods are designed.

## Suggestions
1. **Expand the empirical evaluation substantially.** Add at least one additional dataset (e.g., ACSIncome or COMPAS), compare against multiple baselines (not just PSCF), and report statistical variability (confidence intervals or standard deviations over multiple runs).
2. **Include ablation studies** varying which edges are designated as objectionable, and analyze sensitivity to the causal graph structure.
3. **Report utility metrics** (accuracy/precision/recall) alongside fairness metrics so the fairness-accuracy trade-off is transparent.
4. **Consider presenting the paper primarily as a conceptual/foundational contribution** and tempering the empirical claims, or alternatively, substantially expand the experimental validation to match typical expectations for a framework paper.

## Score and Decision

**Bracketing (Round 1):** Three queries anchored on topics similar to this paper (causal fairness, decoupling, Rawlsian procedural justice).

| Anchor Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| zmYx32SSOR — "Advancing Equitable AI" | 1.00 | R1 | Much weaker; no clear conceptual novelty |
| kJ2X6wZVlD — "Causal Proximal Policy Optimization" | 2.67 | R1 | Different topic; similar evaluation weakness |
| Lr3B8miY4X — "Fair-SP" | 2.50 | R1 | Different topic, synthetic-data approach |
| MlJWmdx5jY — "Diff-Fair" | 3.00 | R1 | Stronger experiments but weaker novelty; our paper has better conceptual contribution |
| tD4kTBNE20 — "ICCFL" | 4.00 | R1, R2 | More extensive experiments (4 datasets, 6 baselines) but lower novelty and clarity issues; comparable overall quality |
| JA5j9DEoy1 — "Causally Fair Node Classification" | 4.00 | R1, R2 | Similar empirical scope limitations; theoretical assumptions questioned |
| C5Ihi4bVQt — "LLMs on Trial" | 4.00 | R2 | Different domain (LLM evaluation); stronger empirical methodology |
| GLlx240C5B — "Locally-Persistent Bias" | 3.00 | R2 | Lower novelty (derivative combination); our paper is clearly stronger on originality |
| kJOJstzxPD — "Learning to Be Fair" | 3.50 | R2 | Different framing; limited empirical validation similar to ours |
| Vv3PGcSn7c — "ROC Fair Classification" | 5.50 | R1, R2 | Stronger paper overall: elegant theory + reasonable experiments + good baselines |
| mVrLvbwXI4 — "Group Fairness Meets the Black Box" | 4.67 | R2 | Stronger experiments (5 datasets, 4 LLMs) but limited novelty; comparable overall |
| qOyF214xmg — "Transducing Language Models" | 8.00 | R1 | Not comparable (different topic); listed to show extreme anchor |
| Ahdsg2nkNH — "Multilevel Control Functional" | 8.00 | R1 | Not comparable |
| UJ2UUjT2ko — "Mixing Mechanisms" | 8.00 | R1 | Not comparable |
| 9gw03JpKK4 — "Gaia2" | 8.00 | R1 | Not comparable |

**Round-1 bracket:** [3.5, 5.0]

**Narrowing (Round 2):** Additional anchors placed the paper closest to the 4.0–4.67 range. The paper has stronger conceptual novelty than the 4.0 anchors (ICCFL, Causally Fair Node Classification) but noticeably weaker empirical validation. Compared to the 4.67 anchor (Group Fairness Meets the Black Box with 5 datasets, 4 LLMs, 3 fairness algorithms), our paper is weaker empirically but stronger conceptually. The 5.50 anchor (ROC Fair Classification) is clearly stronger on all dimensions.

**Final score:** 4.0 — the paper identifies a genuine conceptual gap and proposes a principled, philosophically grounded framework, but the empirical case is far too thin to support the claimed contributions, with only one baseline, one real dataset, no statistical reporting, and no ablation analysis.

## Score and Decision
MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>