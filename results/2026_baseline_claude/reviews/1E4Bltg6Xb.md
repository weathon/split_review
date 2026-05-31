## Summary

This paper proposes a Dynamics Feature Representation (DFR) framework for Reinforcement Learning-based Dynamic Path Planning (DPP) in urban road networks. DFR addresses the information completeness vs. computational efficiency trade-off in state representation via a two-step hierarchical refinement: (1) a **policy attention** mechanism that pre-trains a distance-based policy to extract the top-*k* shortest paths and form a task-relevant subgraph, and (2) an **n-hop neighborhood** method that further localizes the features around the agent's current node. Experiments on three Chinese urban road networks demonstrate improved Mean GAP, Success Rate, and substantial reduction in feature dimensionality and planning time across three RL backbones (DQN, PPO, GCN+DQN).

---

## Strengths

- **Practical motivation and clean formulation.** The completeness-efficiency dilemma in state design for RL-based DPP is a genuine bottleneck. The hierarchical W → W' → W'' pipeline (Equation 5) is clearly formulated and principled.
- **Modular and generalizable framework.** DFR is applied as a plug-in wrapper to three heterogeneous RL algorithms (DQN, PPO, GCN+DQN) and consistently improves performance, demonstrating algorithm-agnostic utility.
- **Substantial efficiency gains.** DFR reduces planning time by 79–86% for DQN and PPO while maintaining or improving route quality, which is practically significant.
- **Systematic ablation.** The joint grid search over *k* and *n* (Figure 6) yields actionable conclusions: n ≥ 2 captures sufficient local context with diminishing returns beyond n = 3, and moderate *k* avoids over-fitting to a narrow subgraph.

---

## Weaknesses

### Fatal
None identified.

### Major

1. **Single OD pair per experiment.** The setup states "each scenario corresponds to a *single* DPP task with a source node, a goal node, and a dynamics sequence." This directly undermines the claim of a general framework: the policy attention subgraph (top-*k* shortest paths) is built for one fixed (source, destination) pair, so the reported performance measures only a single task. Real deployment requires handling arbitrary OD pairs, and it is unclear how the framework scales or generalizes when the subgraph must be recomputed for every new pair.

2. **"Policy attention" is K-shortest paths in disguise.** The pre-trained distance-based policy π*_d optimizes for static shortest paths and is used solely to enumerate the top-*k* shortest paths in the static graph. This is functionally identical to running Yen's K-Shortest Paths algorithm or similar graph-theoretic methods — no learning or attention in the neural-network sense is required. The framing as "policy attention" significantly overstates the technical novelty; the same subgraph extraction could be done analytically without RL pre-training.

3. **No graph size reported; scalability claims are unsubstantiated.** Figure 4's "nodes/edges" fields are not captured by the parser, so the actual scale of the three subgraphs is unknown from the text. The paper claims DFR is suitable for "real-world traffic scenarios" and "large-scale graphs," but scalability is demonstrated only on subgraph extractions of unspecified and potentially modest size.

4. **Theoretical guarantees are informal.** Equations 6–8 use "≈" to assert that the policy conditioned on compressed features approximates the policy on full dynamics, but no bound, assumption, or proof is provided. The appeal to Predictive State Representations (PSR) is analogical rather than rigorous — W'' is not formally shown to be a sufficient statistic under any measurable criterion.

5. **No non-RL comparison baseline.** Dynamic Dijkstra is used to compute ground-truth paths but not included as a planning baseline. Without this comparison it is impossible to assess whether RL is actually competitive in the studied settings, making the argument that DFR+RL provides practical value circular.

### Minor

1. The choice to pre-rank "top-100 shortest paths" as the pool from which *k* is selected is an ad-hoc design choice (why 100?) that the paper does not justify or ablate.
2. The bottom of Figure 6 shows training curves only for varying *n* at a fixed *k* = 0.6, omitting the key comparison between DFR and full-dynamics (AD) over training epochs. Showing convergence speed difference between DFR and AD is the claimed advantage but is missing from the ablation figures.
3. SR at *n* = 1 is consistently poor (0.67–0.76) across all *k* values, yet 1-hop locality is included in ablations without discussion of why such a small neighborhood practically impairs navigation to the goal.

### Trivial

- "headmaps" in the Figure 6 caption appears to be a typo (should be "heatmaps").

---

## Nice-to-Haves

- Evaluate on a diverse set of randomly sampled OD pairs rather than a single task per subgraph, to demonstrate that policy attention generalizes or can be amortized across multiple routes.
- Include dynamic Dijkstra (and possibly A* with dynamic costs) as planning baselines to provide an absolute performance reference.
- Compare the "policy attention" RL pre-training approach with direct Yen's K-Shortest Paths computation to clarify whether RL adds anything over the classical algorithm.
- Report pre-training cost of π*_d and show that the offline computation is tractable for city-scale graphs.

---

## Novel Insights

The empirical finding that n-hop neighborhood size is a more reliable and predictable lever than the path-count parameter *k* for tuning DFR is a useful practical insight: increasing *n* from 1 to 2 yields the largest performance jump, with saturation thereafter, while *k* has a non-monotone and harder-to-tune effect. The result that GCN+DQN's high Success Rate coexists with high GAP (the model reaches the destination but ignores dynamic edge weights) is an interesting diagnostic: structural encoding alone does not guarantee sensitivity to traffic changes, and feature compression via DFR counter-intuitively improves dynamic sensitivity. These are concrete and actionable findings for practitioners.

---

## Suggestions

- Restructure Section 4.3 to be explicit that the "policy attention" pre-training is equivalent to running a K-shortest-paths algorithm on the static graph, and discuss whether RL adds computational overhead or modeling benefit relative to that baseline.
- Add an experiment with at least 50–100 randomly sampled OD pairs per subgraph to test generalization beyond the single-task setting.
- Provide a formal or semi-formal argument (e.g., via mutual information or sufficient statistics) for when W'' is a good proxy for the full dynamics W.
- Report graph node/edge counts clearly in the main text so readers can assess the scale of experiments without needing to parse figure metadata.

---

## Score and Decision

The paper identifies a real problem and proposes a clean hierarchical framework with practical gains. However, the central technical contribution (policy attention) reduces to K-shortest paths enumeration rather than a genuine learning-based attention mechanism, the single-OD-pair experimental setup limits generalizability claims, and the theoretical analysis is largely aspirational. These are substantive issues that weigh against acceptance.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>