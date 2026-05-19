## Summary
# Final Review Report

## Summary

This paper proposes Curvature-Constrained Message Passing (CCMP), a framework designed to mitigate over-squashing in Graph Neural Networks (GNNs) by leveraging local structural properties, specifically edge curvature. The authors introduce a curvature-constrained homophily metric to analyze community behavior and propose dissociating message propagation along positive and negative curvature edges. By filtering the adjacency matrix based on Ollivier or Augmented Forman curvature, CCMP aims to remove topological bottlenecks without excessive graph densification. Experiments on 11 node classification datasets demonstrate that CCMP consistently outperforms state-of-the-art rewiring baselines (e.g., SDRF, FOSR, DIGL), particularly in heterophilic settings, while increasing the normalized spectral gap. The core contribution lies in the practical application of curvature-based edge filtering as a plug-and-play rewiring strategy for MPNNs.

## Strengths
1. **Clear Motivation and Practical Relevance:** The paper addresses the well-known over-squashing problem in GNNs, which limits the effectiveness of deep message passing. Leveraging edge curvature to identify and bypass structural bottlenecks is a geometrically grounded and intuitive approach.
2. **Comprehensive Empirical Evaluation:** The authors evaluate CCMP on 11 diverse datasets (both homophilic and heterophilic) using two popular backbones (GCN and GAT). The comparison against strong rewiring baselines (SDRF, FOSR, DIGL, FA) provides a solid benchmark for assessing the method's effectiveness.
3. **Novel Curvature-Constrained Homophily Metric:** The introduction of $\beta^+$ and $\beta^-$ offers a finer-grained analysis of graph structure by correlating edge curvature with label similarity. This metric provides valuable insights into how curvature filtering affects community cohesion.
4. **Computational Efficiency:** By passively filtering edges rather than actively optimizing the graph structure (as in SDRF), CCMP reduces computational overhead. The reported 10-40% reduction in computational cost on large datasets is a significant practical advantage.

## Weaknesses
1. **Insufficient Differentiation from Prior Curvature-Aware GNNs:** The paper fails to clearly distinguish CCMP from existing curvature-based methods, particularly Curvature Graph Networks (CGN) by Ye et al. (2019). While CGN uses curvature for attention weighting (soft filtering), CCMP uses it for adjacency masking (hard rewiring). This critical distinction is not explicitly articulated, obscuring the method's novelty.
2. **Manual Per-Dataset Configuration Tuning:** The optimal CCMP configuration (positive vs. negative curvature, one-hop vs. two-hop) is manually selected for each dataset and deferred to the appendix. The lack of an automated selection heuristic or a robust default configuration undermines the claim that CCMP is a general-purpose framework and reduces its practical reproducibility.
3. **Arbitrary Curvature Threshold Selection:** The curvature-constrained homophily metric relies on a threshold $\epsilon = 0$ to separate positive and negative curvature edges. This choice is presented without theoretical justification or sensitivity analysis, raising concerns about its generalizability across different graph structures.
4. **Incomplete Theoretical Grounding for Over-Squashing Mitigation:** The paper uses the normalized spectral gap as the primary evidence for over-squashing mitigation. While a larger spectral gap indicates better graph expansion, it is only a proxy for information contraction. Direct information-theoretic metrics or gradient flow analysis would provide stronger theoretical validation.
5. **Notation and Formal Definition Gaps:** Equation (8) contains a notation error (using $h^{(\ell)}$ instead of $h^{(\ell-1)}$ in aggregation), and the two-hop curvature propagation strategy lacks a formal mathematical definition of the neighborhood $\mathcal{N}^+_2(i)$, hindering precise reproducibility.

## Key Issues
1. **Novelty Overlap with CGN (Ye et al., 2019):** The core idea of using Ollivier curvature to guide message passing is not new. CGN already demonstrates that curvature-aware attention improves node classification. The manuscript must explicitly contrast hard adjacency masking (CCMP) with soft attention weighting (CGN) and justify why structural rewiring is superior to feature-level modulation for mitigating over-squashing.
2. **Reproducibility of Configuration Selection:** The reliance on manually tuned, dataset-specific curvature configurations (positive/negative, one-hop/two-hop) makes the method difficult to apply to unseen graphs. Without a default strategy or validation-based selection protocol, the "plug-and-play" claim is not fully supported.
3. **Proxy Metric for Over-Squashing:** Using the normalized spectral gap as the sole evidence for over-squashing mitigation is theoretically incomplete. Spectral gap measures graph expansion but does not directly quantify information contraction or gradient vanishing. The authors should acknowledge this limitation and consider complementary metrics (e.g., mutual information or feature variance analysis).
4. **Statistical Significance of Gains:** The reported accuracy improvements (e.g., 14.24% average gain) are compelling but lack statistical significance testing. Given the variance across 100 random splits, paired t-tests or confidence intervals are necessary to confirm that the gains are not due to random seed fluctuations.

## Actionable Suggestions
1. **Explicitly Contrast with CGN:** Add a dedicated paragraph in the Related Work or Method section comparing CCMP with Curvature Graph Networks (Ye et al., 2019). Clarify that CCMP performs hard structural rewiring to remove topological bottlenecks, whereas CGN performs soft attention weighting to improve feature alignment. Highlight that hard rewiring is more effective for mitigating over-squashing because it directly alters the receptive field topology.
2. **Introduce a Default Configuration Strategy:** Propose a simple heuristic for configuration selection, such as using positive curvature filtering for homophilic graphs and negative curvature filtering for heterophilic graphs (based on the $\beta^+$/$\beta^-$ analysis). Report the performance of this default strategy across all datasets to demonstrate robustness without manual tuning.
3. **Justify the $\epsilon = 0$ Threshold:** Provide a theoretical or empirical justification for choosing $\epsilon = 0$ as the boundary between positive and negative curvature. Include a brief sensitivity analysis showing how performance varies with $\epsilon \in \{-0.1, 0, 0.1\}$ to validate the robustness of this choice.
4. **Add Statistical Significance Testing:** Perform paired t-tests or report confidence intervals for the accuracy gains over the strongest baselines (SDRF, FOSR). This will strengthen the claim that CCMP's improvements are statistically reliable and not due to random seed variance.
5. **Correct Notation and Formalize Two-Hop Propagation:** Fix Equation (8) to use $h^{(\ell-1)}_j$ in the aggregation step. Add a formal mathematical definition for the two-hop curvature-constrained neighborhood $\mathcal{N}^+_2(i)$ and clarify whether two-hop messages are concatenated or summed with one-hop messages.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem):** Graph neural networks suffer from over-squashing, where information from exponentially growing receptive fields is compressed into fixed-size node representations, limiting long-range dependency modeling.
- **S2 (Gap):** Existing rewiring methods (e.g., spectral gap maximization, diffusion) often ignore local geometric bottlenecks identified by edge curvature, leading to suboptimal connectivity or high computational costs.
- **S3 (Solution):** We propose Curvature-Constrained Message Passing (CCMP), a plug-and-play framework that mitigates over-squashing by dissociating message propagation along positive and negative curvature edges.
- **S4 (Mechanism):** By filtering the adjacency matrix based on Ollivier or Augmented Forman curvature, CCMP preserves intra-community flow while bypassing structural bottlenecks without excessive graph densification.
- **S5 (Result):** Experiments on 11 datasets demonstrate that CCMP consistently outperforms state-of-the-art rewiring baselines, particularly in heterophilic settings, while reducing computational overhead by up to 40%.

### Introduction Outline (Complete)
- **P1 (Big Picture):** GNNs are powerful for graph-structured data but struggle with long-range interactions due to the message passing paradigm's reliance on local aggregation.
- **P2 (Problem):** Stacking layers to increase receptive fields leads to over-smoothing and, more critically, over-squashing, where information bottlenecks prevent distant node features from effectively influencing local representations.
- **P3 (Gap):** While rewiring methods address over-squashing by modifying graph connectivity, they often lack geometric precision. Recent work links edge curvature to bottlenecks, but existing curvature-aware models (e.g., CGN) focus on attention weighting rather than structural rewiring.
- **P4 (Solution):** We introduce CCMP, which leverages curvature-constrained homophily to guide hard adjacency masking. By selectively propagating messages through positive or negative curvature edges, CCMP directly removes topological bottlenecks.
- **P5 (Evidence):** We validate CCMP on 11 homophilic and heterophilic datasets, showing significant accuracy gains over SDRF and FOSR, increased spectral gap, and reduced computational cost.
- **P6 (Contributions):** (1) Curvature-constrained homophily metric. (2) CCMP framework with flexible one/two-hop strategies. (3) Comprehensive empirical validation of over-squashing mitigation.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Explicitly contrast CCMP with CGN (Ye et al., 2019) in Related Work/Method. | Resolves novelty overlap concern; clarifies hard rewiring vs. soft attention. | Low |
| **P0** | Introduce a default configuration heuristic (e.g., positive for homophilic, negative for heterophilic). | Improves reproducibility and supports "plug-and-play" claim. | Medium |
| **P1** | Add statistical significance tests (paired t-tests) for accuracy gains. | Strengthens empirical claims; confirms gains are not due to seed variance. | Low |
| **P1** | Justify $\epsilon = 0$ threshold and add sensitivity analysis. | Validates theoretical grounding of curvature-constrained homophily. | Medium |
| **P2** | Correct Equation (8) notation and formalize two-hop neighborhood definition. | Improves mathematical rigor and reproducibility. | Low |
| **P2** | Acknowledge spectral gap as a proxy and discuss complementary over-squashing metrics. | Enhances theoretical completeness and defensibility. | Low |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | CCMP improves node classification over rewiring baselines. | 11 datasets, GCN/GAT, 100 splits. | Accuracy, Std Dev. | CCMP outperforms SDRF/FOSR on 6/7 heterophilic datasets. | Performance gain claim. | Lacks statistical significance tests. |
| E2 | Curvature filtering mitigates over-squashing. | Squirrel, Actor, Roman-Empire. | Normalized Spectral Gap. | Spectral gap increases by 5-87%. | Over-squashing mitigation claim. | Spectral gap is a proxy, not direct measure. |
| E3 | CCMP reduces computational cost. | Large datasets (Squirrel, Actor). | Training time reduction. | 10-40% cost reduction via graph sparsification. | Efficiency claim. | Memory/latency not reported. |

### Research-Theme Gap Diagnosis
The core claim of over-squashing mitigation relies heavily on spectral gap improvement, which measures graph expansion but not information contraction. Additionally, the manual configuration selection limits the method's generalizability to unseen graphs.

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Over-squashing mitigation | CCMP preserves more input-output information than baselines. | Compute mutual information between input features and final embeddings. | Base GCN, SDRF, FOSR. | Mutual Information, Feature Variance. | Higher MI/variance than baselines. | Low | Stronger theoretical validation. |
| Configuration robustness | A default heuristic (homophily-based) performs near-optimal. | Apply default config (positive for homo, negative for hetero) across all datasets. | Manually tuned CCMP. | Accuracy drop vs. tuned. | <1% accuracy drop. | Low | Proves plug-and-play utility. |
| Statistical reliability | Accuracy gains are statistically significant. | Paired t-tests over 100 splits. | Strongest baseline per dataset. | p-value, Confidence Intervals. | p < 0.05. | Low | Confirms empirical gains. |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6/10

**Rationale:** The paper addresses a highly relevant problem (over-squashing) with a geometrically grounded solution (curvature-constrained message passing). The empirical evaluation is comprehensive, covering 11 datasets and strong baselines, and the reported gains are compelling. However, the novelty is partially obscured by insufficient differentiation from prior curvature-aware methods (e.g., CGN), and the reliance on manually tuned configurations undermines the method's practical utility. The theoretical grounding for over-squashing mitigation is also incomplete, relying on spectral gap as a proxy rather than direct information-theoretic metrics. With explicit contrast to CGN, a default configuration heuristic, and statistical significance testing, the paper's impact and defensibility would significantly improve.

**Post-Revision Target:** [7, 8]/10

**Justification:** If the authors clearly articulate the hard rewiring vs. soft attention distinction, provide a robust default configuration strategy, and add statistical validation, the novelty and reproducibility concerns will be resolved. This would elevate the paper to a strong accept, given its solid empirical foundation and practical efficiency gains.