Now I have all the data I need. Let me synthesize my analysis and write the final review.

**Round 1 bracket**: The paper sits between approximately 3.5 and 6.5. Below 4 are papers with weak/insufficient experiments (ViRL-TSC at 4.0). Above 6 are papers with strong theory and comprehensive experiments (MMCKM at 6.0). Our paper falls in the middle.

**Round 2 narrowing**: Comparing to HMAGAT (4.50, Accept Poster) — our paper has a less thorough experimental design but a clearer motivation. To RAST-MoE-RL (5.00, Reject) — similar in having a solid framework but gaps in evaluation. To Graph-Theoretic Intrinsic Reward (4.67, Accept Poster) — our paper has weaker theoretical grounding.

The paper's verified gaps (no error bars, untested central assumption, unfair AD architecture comparison, action space ambiguity) push it toward the lower end of this range. The consistent improvements across 3 algorithms and 3 maps push it upward. Final score: **4.5**.

Now let me write the review, carefully filtering the harsh critic's claims.

Let me verify which harsh critic criticisms are valid by checking the paper:

1. **Unvalidated core assumption**: Partially valid. The paper does not empirically verify that distance-based subgraphs contain near-optimal time paths. But the paper also doesn't claim this with certainty — it says "emphasizing edges along the shortest paths ensures that critical dynamics influencing near-optimal planning decisions are captured." Also, the ablation shows that larger k improves performance, which provides indirect support. Keep as Major, not Fatal.

2. **Action space ambiguity**: Partially valid. The MDP defines actions as neighbors in the graph but doesn't specify whether restricted to subgraph. The state only has dynamics info for subgraph edges. But this is a realistic partial observability setting — the paper acknowledges this trade-off. Keep as Minor.

3. **Untuned AD architecture**: Valid. The same 64-unit MLP is used for all inputs despite AD having 121k-dim input and DFR having few hundred. This is a real concern about fairness. Keep as Major.

4. **No statistical significance**: Valid confirmed by grep. No error bars on main results. Keep as Major.

5. **PSR justification is superficial**: Valid, but this is a minor issue — it's a rhetorical gesture not a formal proof. Demote to Minor.

6. **Missing comparison to learned compression (VAE/GNN encoder)**: This is a scope-creep request. The paper's contribution is about using distance as a prior for attention, not about comparing to learned compression. Move to Nice-to-Have.

7. **k effects being "complex and less predictable" undermines core claim**: This is a misinterpretation. The paper honestly acknowledges a finding and gives practical recommendations. Remove.

8. **Congestion factor too simple**: The paper uses β∈[0.1,1.5] which is a scaling factor on base speed. This is a valid limitation to note but not a fatal one. Keep as Minor.

9. **No comparison to local-view baseline**: The ablation does include k=-1.0 (no policy attention) which is essentially a local view. This is addressed. Remove.

Now let me also filter the Strength Finder's claims:

1. **Systematic empirical validation**: Confirmed — 3 algorithms × 3 maps = 9 settings. Keep.
2. **PSR theoretical grounding**: This is weak — the PSR reference is rhetorical, not a real theoretical contribution. Remove (conflicts with verified weakness).
3. **Detailed ablation study**: Confirmed — heatmaps for k and n variations. Keep.
4. **Quantified planning time reduction**: Confirmed — reported with variance. Keep.

The claim about PSR being a "theoretical grounding" conflicts with the verified weakness that it's superficial. Per instructions: "when a strength and weakness disagree, the weakness wins." Remove the PSR strength.## Summary

The paper proposes Dynamics Feature Representation (DFR), a hierarchical framework that refines high-dimensional global traffic dynamics into compact, decision-relevant features for RL-based dynamic path planning in urban road networks. DFR uses a pre-trained distance-based policy to select a task-relevant subgraph (policy attention), then extracts n-hop neighborhoods around the agent as local dynamics features. Experiments across three real-world road networks and three RL algorithms (DQN, PPO, GCN+DQN) show consistent improvements in GAP, success rate, and compactness rate alongside large planning-time reductions.

## Strengths

- **Consistent empirical validation across multiple algorithms and domains**: The paper evaluates DFR with DQN, PPO, and GCN+DQN on three distinct urban road networks from OpenStreetMap (Nanjing, Chaoyang/Beijing, Pudong/Shanghai). DFR-enhanced models achieve larger radar-triangle areas across all configurations (Figure 5), directly supporting the claim that DFR improves both performance and efficiency.

- **Detailed ablation study characterizing parameter sensitivity**: Section 5.3 provides systematic heatmaps (Figure 6) for Mean GAP, SR, and CR over combinations of k (policy attention strength) and n (neighborhood depth). The paper identifies clear trends (diminishing returns with increasing n, complex effects of k) and offers practical recommendations for deployment — showing genuine understanding of the method's sensitivity.

- **Quantified computational efficiency gains**: The paper reports average planning time reductions of 85.59%, 46.08%, and 79.32% compared to the All Dynamics (AD) baselines, with concrete measured times (8.18±1.74 ms for DQN/PPO). This demonstrates that DFR's feature compression translates directly into practical computational savings.

- **Clear problem motivation and framing**: The paper effectively articulates the completeness-efficiency trade-off in state representation for RL-based DPP, and the distinction between "dynamic" (replanning) and "dynamics" (traffic evolution) is well-drawn and maintained throughout.

## Weaknesses

### Fatal
None.

### Major

- **Central assumption unvalidated: the distance-based subgraph may not contain near-optimal time-based routes.** The entire DFR pipeline rests on the claim that a pre-trained distance-based policy identifies a subgraph sufficient for time-based routing under dynamic traffic. The paper provides no experiment that checks whether the policy attention subgraph actually contains the ground-truth optimal time path (computed via dynamic Dijkstra, which the paper already uses as a benchmark). In real urban networks, congestion can make the time-optimal path diverge substantially from the shortest-distance path. The ablation study only sweeps *k* and *n* within the subgraph — it does not test whether the subgraph itself excludes better alternatives. This is the paper's central claim and it remains unsubstantiated.

- **No statistical significance or variance reporting for main results.** The main results (Figure 5) are reported as single values with no error bars, standard deviations, or multiple-seed runs. Given the modest absolute improvements (e.g., SR from 0.864 to ~0.905), it is not possible to assess whether these differences are meaningful or due to random variation. This is a basic evidential requirement that the paper does not meet.

- **Unfair comparison between DFR and All Dynamics (AD) baselines due to untuned architecture.** Both DFR-enhanced models and AD baselines use the same MLP architecture (64-unit embedding + two 64-unit hidden layers), despite the AD input dimension being orders of magnitude larger (full graph of ~121k edges vs. a few hundred for DFR). This architecture is clearly undersized for AD, making the comparison tendentious: DFR's advantage may partly reflect that the network capacity is better matched to a lower-dimensional input, not that the feature selection is better *per se*. The paper should either tune the AD architecture (scale width/depth with input size) or verify that performance is insensitive to capacity.

### Minor

- **Action space ambiguity regarding subgraph boundaries.** The MDP defines actions as moving to neighbors in the graph (Section 3.2), but does not clarify whether actions are restricted to the policy-attention subgraph. The state's dynamics features only cover edges within the subgraph intersected with n-hop neighborhoods. If the agent can move outside the subgraph, its state would lack dynamics information for those edges, creating a partial observability issue. If actions are restricted, the optimality ceiling imposed by the subgraph is not analyzed. The paper should state the action space explicitly.

- **Congestion dynamics are relatively simple.** The congestion factor β ∈ [0.1, 1.5] only scales base speed, not modeling more complex phenomena (e.g., road closures, asymmetric delays, cascading congestion). This simplicity may favor the distance-based subgraph assumption. The paper should acknowledge this limitation more explicitly.

- **PSR grounding is rhetorical rather than substantive.** Section 4.2 invokes Predictive State Representations as a theoretical foundation, but the paper neither verifies that W''_t satisfies PSR properties (what predictions suffice?) nor uses PSR theory to derive any results. The PSR reference provides framing, not evidence.

### Trivial
- None.

## Nice-to-Haves
- The paper could include a baseline that learns a compressed state representation from the full graph (e.g., a VAE or small GNN encoder) to directly test whether the distance-based prior is better than a learned one.
- The authors could directly measure what fraction of ground-truth optimal time paths are contained within the policy attention subgraph for various k, to validate their central assumption.

## Removed Points

- **"k effects being complex undermines policy attention reliability"**: The paper honestly acknowledges this finding and gives practical recommendations ("moderate k, smaller n"). This is an empirical observation, not a weakness in the method. Removed because the paper treats it transparently.

- **"Missing related work"**: Cannot be confirmed without external sources. Removed per instructions.

- **"PSR theoretical grounding is a strength"** (from Strength Finder): This claim conflicts with the verified weakness that the PSR grounding is superficial. Per instructions, when strength and weakness disagree, weakness wins. Removed.

- **"No comparison to local-view baseline"**: The ablation includes k=-1.0 (disabling policy attention), which functionally serves as a local-view baseline. Removed.

- **"Computation of n-hop intersection at each step is not zero cost"**: The paper states this overhead is "negligible" rather than "zero," and the n-hop computation depends only on fixed topology. The PT measurements (8ms) support the negligible-cost claim. Removed.

- **"Dynamic vs. dynamics distinction inconsistently maintained"**: The paper uses "dynamic" for replanning and "dynamics" for traffic evolution consistently. Removed as factually wrong.

## Novel Insights

The reviews surface a tension that is genuinely interesting: the paper's core insight — that distance-based structural priors can guide attention for time-based dynamic routing — is intuitively appealing and the empirical results are consistent, but the paper never closes the loop by directly measuring whether the distance-selected subgraph actually contains the time-optimal path. This creates an uncomfortable gap between the claim and the evidence that is unusual for an otherwise well-motivated empirical paper. A direct validation of this assumption (e.g., "for k=0.6, 94% of optimal time paths are fully contained in the subgraph") would either strongly confirm the approach or reveal its limitations.

## Suggestions
1. **Validate the central assumption directly**: For each test scenario, report what fraction of the ground-truth optimal time path (computed by dynamic Dijkstra) is contained within the policy attention subgraph, across varying k. This single experiment would substantially strengthen the paper.
2. **Add multiple-seed runs** (at least 5) with standard deviations to all main results and ablation experiments.
3. **Tune the AD baseline architecture** or verify that results are robust to increasing AD network capacity.
4. **Clarify the action space** explicitly and discuss any optimality gap introduced by subgraph restriction.
5. **Acknowledge the simplicity of the congestion model** (β-scaling only) as a limitation.

## Score and Decision

Based on calibration against human-reviewed anchors:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| ViRL-TSC (traffic signal RL) | 4.00 | R1 | Our paper has a stronger technical contribution and more experiments |
| HMAGAT (hypergraph MAPF) | 4.50 | R2 | Similar quality — both have well-motivated ideas but execution gaps. HMAGAT has more thorough experiments |
| Graph-Theoretic Intrinsic Reward | 4.67 | R2 | Our paper is slightly weaker — less theoretical grounding, more missing validation |
| SMART-R1 (traffic sim RL) | 5.00 | R1 | Similar scope and depth, SMART-R1 has SOTA results on benchmark |
| RAST-MoE-RL (ride-hailing RL) | 5.00 | R2 | Similar — solid framework, comparable experimental scope |
| MMCKM (traffic flow prediction) | 6.00 | R1 | Clearly stronger — more theoretical depth and rigorous evaluation |

**Round 1 bracket**: 3.5–6.5. **Round 2 narrowing** placed the paper near the 4.5–5.0 range, comparable to HMAGAT (4.50) and RAST-MoE-RL (5.00). The paper's consistent empirical trends across 3 maps × 3 algorithms are a genuine strength, but the unvalidated central assumption, missing error bars, and unfair baseline comparison are significant methodological gaps that current human-reviewed anchors at this score level do not share to the same degree. This pushes the score below 5.0.

The paper addresses a real and well-motivated problem with a clean, intuitive idea. However, the evidence in its current form is not rigorous enough to confidently accept: the core assumption is unvalidated, the comparisons may overstate DFR's advantage due to architecture mismatch, and results lack statistical grounding. The contribution is real but modest, and the methodological gaps are fixable.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>