Now I have a thorough understanding of both the paper and the calibration anchors. Let me write my consolidated review.

---

## Summary

This paper proposes the Dynamics Feature Representation (DFR) framework for RL-based dynamic path planning (DPP) in urban road networks. DFR compresses high-dimensional global traffic dynamics into compact, decision-relevant features through a two-stage hierarchical refinement: (1) a policy attention mechanism extracts a task-relevant subgraph using distance-based shortest paths, and (2) n-hop neighborhoods further localize features around the agent's current position. Experiments on three real-world road networks (Nanjing, Chaoyang, Pudong) across three RL algorithms (DQN, PPO, GCN+DQN) show that DFR improves solution quality metrics (GAP, SR) while dramatically reducing input dimensionality, yielding planning-time reductions of up to 85%.

## Strengths

- **Well-motivated problem with clear framing.** The paper articulates a genuine dilemma in RL-based DPP: global dynamics are complete but computationally prohibitive, while local dynamics are efficient but risk missing critical information. The "sufficient yet compact" framing is crisp and well-justified (Section 4.1).

- **Consistent empirical results across diverse settings.** The paper evaluates on three real OpenStreetMap urban networks and three RL algorithms (DQN, PPO, GCN+DQN), showing DFR consistently improves mean GAP, success rate, and compactness relative to the All-Dynamics baseline (Figure 5). This cross-domain consistency reduces concern that results are environment- or algorithm-specific.

- **Systematic ablation provides actionable insights.** Section 5.3 varies the policy attention fraction \(k\) and hop radius \(n\) across a grid, revealing that moderate \(k\) and small \(n\) are sufficient, and that increasing \(n\) beyond a point yields diminishing returns (Figure 6). This is a practically useful guide for deployment.

- **Substantial planning-time efficiency gains.** DFR reduces planning time by 85.59% (DQN), 46.08% (GCN+DQN), and 79.32% (PPO) relative to All-Dynamics baselines (Section 5.2), while maintaining or improving solution quality. These are meaningful practical benefits.

- **Honest about limitations.** The paper acknowledges that \(k\) and \(n\) are manually tuned (Section 6) and that the distance-based policy attention is an approximation, not a provably optimal filtering mechanism (Section 4.3, lines 396–403). This candor is commendable.

## Weaknesses

### Fatal

None. The core claim — that hierarchical compression via policy attention and n-hop neighborhoods is an effective state representation strategy for RL-based DPP — is supported by the experimental evidence.

### Major

- **Theoretical claims via PSR are overstated.** Section 4.2 states that grounding DFR in Predictive State Representations "guarantees that the resulting representations are compact, temporally predictive, and theoretically sufficient" (line 364–365). The paper provides no formal proof linking the n-hop neighborhood construction to PSR sufficiency, nor does it demonstrate that \(W_t''\) actually predicts future observations. The PSR discussion is conceptual inspiration, not a rigorous theoretical foundation. The language of "guarantees" should be substantially softened or the gap between the conceptual appeal and the actual method should be made explicit.

- **Missing baselines leave the contribution of policy attention incompletely isolated.** The primary comparison is DFR vs. AD (All Dynamics). While DFR clearly outperforms AD, this does not disentangle whether the *specific design* of policy attention is responsible, or whether any dimensionality reduction would suffice. The ablation in Section 5.3 does vary \(k\) (including \(k=-1\) to disable policy attention), but the paper does not explicitly compare (a) n-hop-only without policy attention (\(k=-1, n>0\)) against full DFR, nor (b) a random subgraph of equivalent size against the distance-based subgraph. Without these controls, the unique value of the policy attention mechanism — as opposed to mere dimensionality reduction — remains unclear.

### Minor

- **The distance-based heuristic may fail under certain congestion patterns, and failure modes are unexplored.** The paper acknowledges that \(\pi_d^*\) is distance-based and does not incorporate time-varying edge weights (Section 4.3). While the experiments demonstrate success under the tested dynamics, the paper provides no analysis of when this heuristic might break down (e.g., when severe congestion makes a longer-distance path systematically faster). The paper would benefit from characterizing the conditions under which the distance-based subgraph contains the true time-optimal path.

- **Dynamics generation process is underdescribed.** Section 5.1 specifies that edge weights are parameterized by a congestion factor \(\beta \in [0.1, 1.5]\), but does not describe how \(\beta\) evolves over time and across edges (i.i.d.? correlated? does it follow realistic patterns like rush-hour waves?). The structure of the dynamics directly affects how much time-optimal paths diverge from distance-shortest paths, so this omission limits the reader's ability to assess the generality of the results.

- **Ablation caps candidate paths at top-100.** Section 5.3 restricts the policy attention subgraph to the top-100 shortest paths. While this may be adequate for the subgraph sizes tested (Subgraph 1 of Nanjing), the paper does not discuss whether this cap is sufficient for larger graphs where many more alternative routes may be relevant. The generality of the ablation findings to larger-scale deployments is therefore uncertain.

### Trivial

- **The "dynamic Dijkstra algorithm" for ground-truth computation is not explained.** Section 5.1 mentions it in passing (line 462) but provides no detail on how Dijkstra's algorithm is adapted to time-varying edge weights. A brief clarification (e.g., whether FIFO is assumed, how time-dependent costs are aggregated) would aid reproducibility.

## Nice-to-Haves

- **Adaptive \(k\) and \(n\) selection.** The authors themselves note that manual tuning of \(k\) and \(n\) limits practical applicability (Section 6). An adaptive mechanism — such as growing the subgraph when the agent's uncertainty is high — would be a natural extension.

- **Learned compression baseline.** Comparing DFR against a generic learned compression method (e.g., an autoencoder over edge weights) would help quantify how much the task-aware design of DFR contributes beyond what a task-agnostic compressor could achieve.

- **Case studies of divergence between distance-based and time-optimal paths.** Visualizing concrete instances where the distance-based subgraph excludes the true time-optimal path (and showing whether the learned policy still succeeds) would strengthen the practical validation.

## Removed Points

*These points are flagged to be removed — treat them with caution.*

1. **Harsh Critic: "The policy attention subgraph is selected using distance-based shortest paths, which is misaligned with the objective... The entire DFR framework's claim of 'sufficiency' is unsupported."** — Partially valid as a limitation but the critic overstates the case. The paper explicitly acknowledges that \(\pi_d^*\) is distance-based only (Section 4.3, lines 396–403) and argues it as a reasonable heuristic, not a proof. The criticism that this is "fundamentally flawed" and a "fatal" error is itself an overstatement. Moved the substantive kernel to Major/Minor weaknesses above; the "fatal" framing is removed.

2. **Harsh Critic: "The experimental design uses a critically weak baseline that inflates apparent improvements."** — AD is not a "trivially weak" baseline in the context of this paper's research question. The paper explicitly frames the problem as a trade-off between global completeness and local efficiency, and AD represents the global-completeness endpoint. Comparing against AD directly addresses the paper's stated goal: can we compress without losing too much information? The critic's framing that AD is "prohibitively expensive" is actually the paper's own argument for why compression is needed. The specific missing baselines (n-hop-only, random subgraph) are kept as a Major weakness.

3. **Harsh Critic: "CR is not an independent measure of quality; it is a direct consequence of the method's design."** — CR is presented as an efficiency metric alongside quality metrics (GAP, SR). The paper never claims CR measures quality; it measures compactness, which is explicitly one of the paper's stated goals ("sufficient yet compact"). The critic's objection misreads the paper's use of the metric. Removed.

4. **Strength Finder: "The method is grounded in a principled theoretical foundation [via PSR]."** — Conflicts with the verified weakness that the PSR link is overstated. The PSR discussion is conceptual motivation, not a rigorous foundation. Kept in weakened form (acknowledged as conceptual inspiration rather than formal guarantee).

5. **Harsh Critic: "The paper cites multiple preprints... as though they are peer-reviewed work."** — Per instructions, criticism about reference status is removed. The existence of cited works is assumed.

6. **Harsh Critic: "The ablation studies restrict attention to the top-100 shortest paths... This cap may be far too small."** — Kept as a Minor weakness since it's a legitimate concern about the generality of the ablation findings.

## Novel Insights

None beyond the paper's own contributions. The hierarchical two-stage compression idea (global task-aware filtering → local agent-centric decoupling) is a clean conceptual framework, but it is an engineering contribution rather than a fundamentally novel insight. The ablation finding that moderate \(k\) and small \(n\) suffice, and that \(k\) has a more complex and less predictable impact than \(n\), is a useful empirical observation for practitioners.

## Suggestions

1. **Add a random subgraph baseline.** Replace the policy attention subgraph with a random subgraph of equal edge count; this would isolate whether distance-based selection specifically matters or any compression helps.

2. **Characterize the coverage of the distance-based subgraph.** For the tested dynamics, report what fraction of ground-truth time-optimal paths are fully contained within the distance-based policy attention subgraph. This would directly address the "sufficiency" concern.

3. **Describe the dynamics generation process.** Specify how \(\beta(v_i, v_j; t)\) evolves — is it i.i.d. per edge per timestep, or does it follow spatially/temporally correlated patterns? This is essential for readers to assess the generality of results.

4. **Tone down the PSR language.** Replace "guarantees" with "motivates" or "provides intuition for." The PSR framework is a useful conceptual lens but the paper does not prove formal sufficiency.

5. **Clarify the dynamic Dijkstra ground-truth computation.** A sentence explaining how time-dependent edge costs are handled (e.g., FIFO assumption, time-expanded graph, or stepwise aggregation) would improve reproducibility.

## Score and Decision

### Anchor comparisons

| Anchor | Path | Avg Score | Comparison |
|--------|------|-----------|------------|
| RL for dynamic VRP | `bisWxwcK8D.md` | 2.50 | Rejected for limited baselines, methodological gaps, limited novelty. Current paper has clearer contributions and more systematic evaluation. |
| RL parking path planning | `T98uLLyWiM.md` | 3.50 | Rejected mainly for weak baselines (one classical heuristic). Current paper has more baselines (3 RL algorithms × 2 conditions) and better ablation. |
| Dynamic drone pickup/delivery | `leoXWCu6CO.md` | 3.60 | Methodological gaps, presentation issues. Current paper is better structured and more systematic. |
| RL+VLM traffic signal control | `36xNdrIUXa.md` | 4.00 | All 4s, rejected. Current paper has stronger experimental support and clearer methodology. |
| Neural MO routing on multigraphs | `55laGcPNZZ.md` | 5.33 | Accept (Poster). First in a new setting, clear novelty, but scalability issues. Comparable quality; current paper has less novelty but more practical focus. |
| Koopman traffic flow prediction | `fhDqFk4DgI.md` | 6.00 | Accept (Poster). Solid methodology, all 6s. Current paper has less theoretical depth. |
| Plan-R1 trajectory planning | `uusTA1rBhR.md` | 6.50 | Accept (Poster). Strong methodology, SOTA, clear contributions. Current paper is not at this level. |
| Triple-BERT ride-sharing | `symgW6FhA6.md` | 6.50 | Accept (Oral). Innovative architecture, strong results. Current paper's contribution is more modest. |

The paper makes a solid, well-executed engineering contribution — a hierarchical compression framework that demonstrably improves RL-based DPP across multiple settings. The experiments are systematic (3 cities × 3 algorithms) and the ablation is informative. However, the theoretical claims are overstated, key baselines are missing, and the dynamics generation process is underdescribed. These issues are substantive but addressable.

The paper is stronger than the rejected 2.5–4.0 anchors (which had severe methodological gaps or very limited evaluation), but falls short of the 6.0+ accept anchors (which have clearer novelty or more thorough evaluation). It lands in the borderline region comparable to the 5.33 multigraph routing paper.

**Overall assessment:** The contribution is genuine but its scope is narrower than the framing suggests. With the missing baselines and softened theoretical claims, this could be a solid poster. In its current form, the combination of overstated theory and incomplete baseline isolation brings it to the borderline.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>