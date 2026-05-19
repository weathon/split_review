## Summary
# Final Review Report

## Summary
This paper introduces LayerDAG, a layerwise autoregressive diffusion model for generating Directed Acyclic Graphs (DAGs). The authors address the challenge of modeling strong directional and logical dependencies in large-scale DAGs, which are crucial for system benchmarking and hardware synthesis. LayerDAG uniquely decomposes a DAG into a sequence of bipartite graphs based on node depth, enabling autoregressive generation for directional dependencies and discrete diffusion for logical dependencies within each layer. Extensive experiments on synthetic datasets with strict logical rules and real-world datasets (TPU Tile, HLS, NA-Edge) demonstrate that LayerDAG outperforms existing autoregressive and diffusion-based baselines in validity, statistical fidelity, and surrogate model training performance. The work also introduces a flexible layer-index-based denoising schedule to balance generation quality and efficiency.

## Strengths
1. **Novel Methodological Integration**: The combination of autoregressive layerwise generation with discrete diffusion effectively addresses the dual challenges of directional and logical dependencies in DAGs. The unique layerwise tokenization based on longest-path depth ensures permutation invariance and natural acyclicity.
2. **Strong Empirical Validation**: The paper provides comprehensive experiments across synthetic datasets with strict logical constraints and three diverse real-world datasets (TPU, FPGA, edge devices). The consistent outperformance of baselines in validity and surrogate model training metrics strongly supports the method's effectiveness.
3. **Practical Application Focus**: By targeting large-scale system benchmarking and hardware synthesis, the work addresses a high-impact practical need. The use of ML-based surrogate models as a proxy evaluation metric is a creative and computationally feasible approach for assessing generated DAG quality.
4. **Flexible Efficiency Trade-off**: The layer-index-based denoising schedule is a practical contribution that allows users to balance generation quality and computational cost, adapting to varying layer complexities.

## Weaknesses
1. **Novelty Claim Bounding**: The claim of being the "first to use autoregressive diffusion models for DAG generation" requires careful bounding. Recent works (e.g., EDGE, GRAPHARM) combine autoregression and diffusion for undirected graph generation. The manuscript should explicitly distinguish LayerDAG's adaptation to *directed* graphs with strict topological constraints from these undirected hybrids.
2. **Surrogate Model Evaluation Limitations**: The ML-based evaluation protocol relies on surrogate models (BiMPNN, Kaggle top-5) to assess DAG quality. The evaluation is inherently bounded by the surrogate model's capacity. If the surrogate cannot fully capture structure-to-metric relationships, it may underestimate the fidelity of generated DAGs. This limitation should be explicitly acknowledged.
3. **Conditional Generation Implementation Details**: The mechanism for integrating label embeddings $y$ into node representations is underspecified (e.g., concatenation vs. cross-attention). Clarifying this detail is important for reproducibility, especially given the varying scales of system metrics like runtime and resource usage.
4. **Conclusion Depth**: The conclusion is overly brief (two sentences) and merely restates the abstract. It lacks a summary of validated findings, bounded limitations, and prioritized future work, which are standard for a strong closing.

## Key Issues
1. **Claim-Evidence Alignment for Novelty**: The "first to use autoregressive diffusion for DAGs" claim risks overreach if not explicitly bounded against undirected AR-diffusion hybrids. *Impact*: May lead to reviewer skepticism regarding novelty positioning. *Fix*: Reposition claim to emphasize adaptation to directed graphs with topological constraints.
2. **Proxy Evaluation Bottleneck**: Relying on surrogate models for DAG quality assessment introduces a capacity bottleneck. *Impact*: Limits the upper bound of demonstrable generative fidelity. *Fix*: Explicitly acknowledge surrogate limitations and discuss how stronger surrogates might further validate LayerDAG's gains.
3. **Reproducibility of Conditional Generation**: Lack of specifics on label integration mechanism. *Impact*: Hinders exact reproduction of conditional generation results. *Fix*: Specify integration method (e.g., cross-attention) and label dimensionality in the method section.

## Actionable Suggestions
1. **Bound Novelty Claims**: In the Introduction and Related Work, explicitly contrast LayerDAG with undirected AR-diffusion models (e.g., EDGE, GRAPHARM). State that LayerDAG is the first to adapt this hybrid paradigm to *directed* graphs with strict topological constraints, clarifying the exact methodological gap.
2. **Clarify Conditional Generation**: In Section 3.2, specify how label embeddings $y$ are integrated into node representations (e.g., via cross-attention or FiLM). Mention the dimensionality and scaling of $y$ for different datasets (TPU runtime vs. FPGA resource usage).
3. **Acknowledge Surrogate Limitations**: In Section 5.2, add a paragraph acknowledging that the ML-based evaluation is bounded by surrogate model capacity. Discuss how this limitation affects the interpretation of results and suggest using stronger surrogates or direct hardware validation in future work.
4. **Expand Conclusion**: Rewrite the Conclusion to include three concise parts: (a) validated findings (validity gains, surrogate improvements), (b) bounded limitations (categorical attributes, proxy evaluation), and (c) prioritized future work (continuous attributes, live hardware validation).
5. **Deepen LP Dataset Analysis**: In Section 5.1, explicitly explain why baselines struggle with set-level balance constraints (e.g., node-wise autoregression lacks global layer awareness, mixture-of-Bernoulli lacks expressive capacity).

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain)**: Directed Acyclic Graphs (DAGs) are crucial for hardware synthesis and compiler optimization, but generating realistic large-scale DAGs is challenging due to strict directional and logical dependencies.
- **S2 (Significance/Challenge)**: Existing generative models struggle to maintain structural validity and statistical fidelity when scaling to hundreds of nodes, limiting their utility for system benchmarking.
- **S3 (Prior Gap)**: Prior autoregressive models impose artificial node orderings that violate DAG inductive biases, while diffusion models ignore directional constraints essential to DAGs.
- **S4 (Proposed Method)**: We introduce LayerDAG, a layerwise autoregressive diffusion model that uniquely decomposes DAGs into sequences of bipartite graphs, leveraging autoregression for directional dependencies and discrete diffusion for logical dependencies within each layer.
- **S5 (Key Result & Implication)**: Extensive experiments on synthetic and real-world datasets (TPU, FPGA, edge devices) show LayerDAG achieves up to 20% absolute validity gains and significantly improves surrogate model training accuracy, enabling privacy-preserving, compute-efficient system benchmarking.

### Introduction Outline (Complete)
- **P1 (Big Picture & Problem)**: Define DAGs and their role in modeling complex dependencies. Pivot quickly to the *generative* challenge: why generating DAGs is distinct from analyzing them, emphasizing directional and logical constraints.
- **P2 (Motivation & Stakes)**: Highlight the practical need for synthetic DAGs: collecting real workload DAGs is prohibitively expensive and raises IP concerns. Generative models offer a privacy-preserving, efficient alternative for benchmarking and co-design.
- **P3 (Technical Gap)**: Contrast DAG generation with undirected graph generation. Explain why existing autoregressive (node-wise ordering bias) and diffusion (ignores directionality) models fall short for large-scale DAGs.
- **P4 (Solution Preview)**: Introduce LayerDAG's core idea: unique layerwise tokenization based on node depth, enabling permutation-invariant autoregressive generation combined with set-level diffusion for logical rules.
- **P5 (Contributions & Evidence)**: Explicitly list contributions: (1) novel layerwise bipartite tokenization, (2) hybrid AR-diffusion framework for DAGs, (3) scalable generation up to ~400 nodes, (4) superior performance in validity and surrogate model training across diverse platforms.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Bound novelty claims against undirected AR-diffusion hybrids (EDGE, GRAPHARM) in Intro/Related Work. | Prevents reviewer skepticism on novelty positioning; clarifies exact methodological gap. | Low |
| **P0** | Specify conditional generation label integration mechanism (e.g., cross-attention) in Section 3.2. | Improves reproducibility and methodological transparency. | Low |
| **P1** | Acknowledge surrogate model capacity limitations in Section 5.2 evaluation discussion. | Strengthens objectivity and bounds claim scope appropriately. | Low |
| **P1** | Expand Conclusion to include validated findings, limitations, and future work. | Provides a stronger, more standard academic closing. | Low |
| **P2** | Deepen LP dataset analysis by explaining baseline failure modes (node-wise vs. set-level constraints). | Enhances technical depth and insight into why LayerDAG succeeds. | Medium |
| **P2** | Add brief intuitive explanation of longest-path-based layerwise partition uniqueness in Section 3.1. | Improves readability and conceptual clarity for broader audiences. | Low |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Capture strong logical rules | Synthetic LP dataset ($\rho \in \{0, 0.5, 1\}$); Baselines: D-VAE, GraphRNN, GraphPNAS, OneShotDAG | Validity, W1, MMD | LayerDAG achieves ~20% absolute validity gain at $\rho=0$ | Validity under strict constraints | Synthetic constraints may not fully reflect real-world complexity |
| E2 | Conditional generation for real-world datasets | TPU Tile, HLS, NA-Edge; 80/10/10 split; ML-based surrogate evaluation (BiMPNN) | Pearson, MAE, W1, MMD | LayerDAG consistently outperforms baselines in surrogate training | Practical benchmarking utility | Surrogate capacity bottlenecks evaluation |
| E3 | Label generalization (OOD) | TPU Tile quantile exclusion (4th/5th); BiMPNN & Kaggle top-5 surrogates | Pearson, MAE, W1, MMD | LayerDAG maintains positive correlation in extrapolation; baselines fail | Generalization to unseen metrics | Extrapolation gains remain modest (Pearson ~0.2) |
| E4 | Quality-efficiency trade-off | LP, TPU Tile, HLS; Layer-index vs. constant denoising schedule | Validity/Pearson vs. Time | Layer-index schedule yields better quality at same time budget | Flexible efficiency control | Assumes complexity increases with layer depth |

### Research-Theme Gap Diagnosis
The core research-value claim of enabling privacy-preserving, compute-efficient system benchmarking is well-supported by surrogate model improvements. However, the reliance on proxy evaluation (surrogate models) leaves a gap in direct hardware validation. Additionally, the focus on categorical node attributes limits applicability to domains with continuous structural properties.

### Proposed Research Experiments (P0/P1/P2)
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Estimated Cost/Time | Expected Paper-Quality Gain |
|---|---|---|---|---|---|---|---|
| Direct hardware validation | Generated DAGs correlate with actual hardware performance beyond surrogate predictions. | Sample LayerDAG DAGs; execute on small FPGA/TPU cluster; measure runtime/resource usage. | Real DAGs, GraphPNAS | Runtime correlation, Resource delta | Correlation > 0.7 with ground truth | Medium (2-3 weeks) | Strongly validates practical utility |
| Continuous attributes | LayerDAG extends to continuous node attributes without validity loss. | Modify D3PM to continuous diffusion; test on dataset with real-valued attributes. | Categorical LayerDAG | Validity, MMD (continuous) | Validity > 0.8, MMD < 0.1 | Low (1 week) | Broadens method applicability |
| Surrogate capacity ablation | Stronger surrogates reveal larger gaps between LayerDAG and baselines. | Train larger GNN surrogates (e.g., GraphTransformer) on synthetic vs real data. | BiMPNN surrogate | Pearson, MAE | LayerDAG gap increases with surrogate capacity | Medium (1-2 weeks) | Confirms surrogate bottleneck limitation |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
Final Score: 7.5/10
Post-Revision Target: [8.0, 9.0]/10

**Scoring Rationale**: The paper presents a novel and well-executed method for DAG generation, effectively combining autoregressive and diffusion paradigms to address directional and logical dependencies. The empirical validation is comprehensive, covering synthetic strict-constraint datasets and diverse real-world platforms. The score reflects strong research value and methodological soundness, tempered slightly by the need to bound novelty claims against undirected AR-diffusion hybrids and acknowledge surrogate evaluation limitations. With minor revisions to clarify conditional generation details, expand the conclusion, and deepen the analysis of baseline failure modes, the paper can achieve a higher score.