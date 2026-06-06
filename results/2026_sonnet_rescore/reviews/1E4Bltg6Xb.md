## Summary
The paper proposes a Dynamics Feature Representation (DFR) framework for reinforcement-learning-based Dynamic Path Planning (DPP) on urban road networks. DFR introduces a two-stage hierarchical state refinement: (1) a policy attention mechanism that pre-trains a static distance-based policy to extract the union of top-*k* shortest paths as a task-relevant subgraph, and (2) an *n*-hop neighborhood method that further restricts the state to the agent's local context within that subgraph. Experiments on three urban subgraphs from Nanjing, Beijing-Chaoyang, and Shanghai-Pudong show DFR-augmented DQN, PPO, and GCN+DQN agents outperform their All-Dynamics (AD) counterparts on Mean GAP and Success Rate, while substantially reducing planning time and feature dimensionality.

---

## Strengths

- **Consistent cross-algorithm and cross-city improvement.** Figure 5 shows that DFR-enhanced variants (DQN+DFR, GCN+DQN+DFR, PPO+DFR) produce larger radar-chart triangle areas (on 1−GAP, SR, 1−CR) than their AD counterparts across all three subgraphs, indicating the benefit is not specific to one algorithm or city.
- **Substantial planning-time reduction with quantified numbers.** Section 5.2 reports average time reductions of 85.59% (DQN), 79.32% (PPO), and 46.08% (GCN+DQN) versus AD baselines, with mean latencies of 8.18 ± 1.74 ms (DQN/PPO) and 27.26 ± 6.8 ms (GCN+DQN), directly supporting real-time applicability.
- **Informative ablation with partial decomposition of contributions.** Figure 6's heatmaps over a grid of *k* ∈ {0.2, 0.4, 0.6, 0.8, 1.0, −1.0} × *n* ∈ {1, 2, 3, 4, −1} allow the reader to isolate the contribution of policy attention alone (k > 0, n = −1), n-hop alone (k = −1, n > 0), and both combined, providing genuine decomposition of the two DFR components.

---

## Weaknesses

### Fatal
*None.*

### Major

- **Traffic dynamics model is unspecified in the main text, undermining the temporal motivation.** Section 5.1 introduces a congestion factor β(v_i, v_j; t) ∈ [0.1, 1.5] but says nothing about its temporal evolution: Is β i.i.d. random per step, correlated (e.g., AR process), or drawn from real sensor data? Section 4.2 asserts that DFR "preserves temporal dependencies" and captures "local congestion propagation," but this claim requires temporal correlation in β to be meaningful. If β is i.i.d. noise at each step, there are no temporal patterns to preserve, and the PSR-motivated framing in the abstract and Section 4.2 collapses to a dimensionality-reduction heuristic with no temporal content. This is a central gap: the paper's theoretical narrative and empirical interpretation depend on the dynamics model, yet the model is not described.

- **The convergence claim in the abstract is not directly demonstrated.** The abstract states DFR "accelerates convergence compared to baselines," but Figure 6 bottom shows training curves only for DQN+DFR variants at k = 0.6 with varying n. The full AD baseline (k = −1.0, n = −1) curve is not plotted on the same axes. Without a side-by-side convergence comparison with DQN+AD, the headline convergence claim is unsubstantiated in the main text.

- **No comparison to any existing RL-based DPP state representation.** Footnote 3 exempts the paper from comparing to traditional planners on reasonable grounds, but the paper's own related-work section cites Du et al. (2024b), Zhao et al. (2025), and Lin et al. (2025) as prior RL-DPP methods using local or global state views — none appear as baselines. The only comparison is against naive full-graph AD inputs to a 64-unit MLP, which is a known-bad encoding at scale. A fixed-radius local neighborhood (no policy attention) could serve as a natural intermediate baseline for the policy attention contribution, beyond what the ablation at k = −1.0 already provides within the same DFR framework.

### Minor

- **CR > 100% for the AD baseline is inconsistent with the stated metric definition.** CR is defined as "the proportion of the reduced feature dimension after DFR to the original dimension, and lower is better." The heatmap in Figure 6 reports CR = 121.042 for (k = −1.0, n = −1) — the full AD baseline — and CR = 95.640 for (k = 1.0, n = −1). If the "original dimension" is the full graph's edge count, then the AD baseline should be exactly 100% (or 1.0 in fractional terms), not 121%. The paper does not explain what normalizing reference is used, making these values uninterpretable and CR's role as an objective metric unclear.

- **Test-set protocol is not reported.** Section 5.1 states that "the source and goal nodes are randomly sampled from a subgraph," and 75,600 training episodes are used. However, the number of test episodes, the OD sampling distribution at test time, and whether test OD pairs are distinct from training are not stated in the main text. Without this information, the SR and Mean GAP values in Figure 5 cannot be interpreted statistically.

- **PSR theoretical grounding is informal.** Section 4.2 invokes Predictive State Representations to justify that W_t'' is "theoretically sufficient," but Equations 6–8 state only that the optimal policy conditioned on W_t'' *approximates* the policy conditioned on W_t, with no formal bound, no condition under which the approximation holds, and no derivation connecting the n-hop subgraph to the PSR predictive-test framework. The invocation reads as post-hoc framing rather than an actual theoretical result.

### Trivial

- **Deployment guideline overgeneralizes from a single subgraph.** Section 5.3 concludes: "in large-scale graph deployment, configurations with moderate k and smaller n should be preferred." This guideline is drawn solely from ablation on Subgraph 1 (Nanjing). The paper should hedge that this is a heuristic recommendation conditioned on the experimental scale.

---

## Nice-to-Haves

- Including the DQN+AD training curve in Figure 6 bottom would directly substantiate the abstract's convergence claim with minimal effort.
- Specifying the β dynamics model (e.g., spatially correlated noise, or a real-data-calibrated process) and showing that results hold under temporally correlated dynamics would significantly strengthen the paper's narrative about capturing congestion propagation.
- Reporting test set size and providing confidence intervals (or multiple runs) on Mean GAP and SR would increase statistical interpretability.
- Self-adaptive selection of k and n (noted as future work in Section 6) would address the practical deployment concern directly.

---

## Removed Points

*These points are flagged as removed — treat them with caution.*

- **Harsh Critic: "Policy attention is a misnomer"** — The critic argues the policy-attention mechanism is "computationally equivalent to k-shortest paths" and is not "attention" in the Transformer sense. The paper explicitly acknowledges (Section 4.3) that this is a "hard, pre-computed attention based on the structural semantics of the task," not soft attention. The naming is a terminological choice the authors are transparent about. Removed as a nitpick on terminology.

- **Harsh Critic: "Baseline comparison is a strawman"** — Partially valid, but the paper's stated scope (footnote 3) is explicitly to study state representation quality *within* the RL paradigm, not to benchmark RL against classical planners. The AD baseline (same algorithm, full-graph features) is the appropriate comparison for that claim. The retained Major weakness about missing prior RL-DPP state representations is a more precise form of this concern.

- **Harsh Critic: "Section 5.1 says single DPP task but episodes sample randomly"** — Reading Section 5.1 carefully, "each scenario corresponds to a single DPP task" means each training episode is a task instance with a freshly sampled OD pair and dynamics sequence, which is consistent with 75,600 training episodes. There is no contradiction. Removed as a misreading.

- **Strength Finder: "Strong theoretical grounding via PSR"** — Conflated with the retained Minor weakness above. The PSR invocation is informal; retaining this as a strength would directly contradict a verified weakness. Removed.

---

## Novel Insights

The ablation decomposition in Figure 6 is the most instructive part of the paper. The heatmap at k = −1.0, n ∈ {1,2,3,4} (policy attention disabled, n-hop only) versus k ∈ {0.2,...,1.0}, n = −1 (policy attention only, no n-hop) versus the full DFR grid reveals that n-hop alone substantially reduces Mean GAP (from 0.176 at n = −1 to 0.114 at n = 4 when k = −1.0), while moderate policy attention adds further but more unpredictable benefit. This suggests the n-hop neighborhood is the dominant contributor to performance improvement, while the policy attention primarily drives dimensionality reduction — a nuance not prominently discussed in the paper's narrative, which presents both components as co-equal contributions.

---

## Suggestions

1. **Add β dynamics description**: State exactly how the congestion factor evolves over time (e.g., "drawn i.i.d. from Uniform[0.1, 1.5]" or "follows a first-order Markov process with transition matrix X"). If the β process has temporal autocorrelation, report its properties and show that DFR's advantage holds under varying degrees of temporal structure.
2. **Fix or redefine CR**: Clarify what "original dimension" means (total edge count of the full graph? something else?) and explain why the AD baseline (k = −1.0, n = −1) produces CR = 121 instead of 100.
3. **Add AD training curve to Figure 6**: Plot the DQN+AD convergence curve on the same axes as the DFR variants to directly demonstrate the convergence speedup claimed in the abstract.
4. **Report test-set size**: State explicitly how many test episodes are used, how OD pairs are drawn at test time, and the resulting SR/Mean GAP standard deviations (or confidence intervals across seeds).
5. **Discuss why n dominates over k**: The ablation results suggest n-hop is the primary performance driver; explicitly analyzing this would give practitioners clearer tuning guidance and strengthen the paper's theoretical narrative.

---

## Evaluation on Key Axes

- **Originality**: The combination of pre-trained distance policy for subgraph extraction with n-hop local neighborhoods is a sensible and moderately novel contribution; neither component is individually new, but their principled combination for DPP state design has value.
- **Importance of research question**: DPP with RL is practically relevant; state representation design is a genuine bottleneck.
- **Claims well supported**: The main empirical improvement is supported, but the convergence claim is not directly demonstrated, the dynamics model is unspecified, and the CR metric has a definition inconsistency.
- **Soundness of experiments**: The ablation design is good; the cross-algorithm, cross-city evaluation is reasonable; but the narrow scope (three small subgraphs, unknown test-set size) limits generalizability.
- **Clarity of writing**: Generally clear, with well-structured methodology; the CR metric definition and training-curve caption leave gaps.
- **Value to research community**: Provides a reusable framework and practical ablation insights; limited by the absence of comparison to existing methods and informal theoretical claims.

---

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>3</importance>
<claims_supported>2</claims_supported>
<soundness>2</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>