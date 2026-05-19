## Summary
# Final Review Report

## Summary
This paper introduces Cyclic Neural Networks (Cyclic NN), a novel ANN design paradigm that relaxes the Directed Acyclic Graph (DAG) constraint by allowing flexible, cyclic connections between computational neurons. Inspired by biological neural connectivity, the authors propose Graph Over Multi-layer Perceptron (GOMLP) as a concrete instantiation, trained using localized Forward-Forward (FF) objectives. Experiments on MNIST, 20 Newsgroups, and IMDB demonstrate that Cyclic NN can match or exceed the performance of standard layer-by-layer DAG networks. The paper claims that this architecture enables FF training to outperform Back-Propagation (BP) for the first time. While the biological inspiration and architectural flexibility are compelling, the manuscript suffers from mathematical inconsistencies in the loss formulation, lack of matched-capacity baselines, overclaims regarding novelty and performance, and insufficient ablation studies to isolate the contribution of cyclic topology. With targeted revisions to mathematical rigor, experimental fairness, and claim bounding, the paper could make a meaningful contribution to localized learning and graph-structured ANNs.

## Strengths
1. **Novel Architectural Paradigm:** The proposal to relax DAG constraints and explore cyclic graph topologies for ANNs is conceptually interesting and aligns with growing interest in biologically plausible and structurally flexible neural architectures.
2. **Localized Training Integration:** Combining cyclic connectivity with the Forward-Forward (FF) algorithm provides a coherent framework for localized learning, avoiding global gradient dependencies and enabling independent neuron optimization.
3. **Empirical Validation on Multiple Benchmarks:** The paper evaluates GOMLP on three diverse datasets (MNIST, 20 Newsgroups, IMDB) and reports variance across 20 random seeds, demonstrating reasonable experimental rigor.
4. **Clear Graph Generator Exploration:** Testing multiple graph structures (Chain, Cycle, Complete, WS, BA) provides insight into how connectivity patterns influence localized learning dynamics, offering a useful ablation dimension.
5. **Open Science Commitment:** The authors release code and provide detailed dataset statistics and hyperparameter settings in the appendix, supporting reproducibility.

## Weaknesses
1. **Mathematical Inconsistency in Loss Formulation:** Equation (6) defines the local loss using binary cross-entropy with a goodness function $p(h) = \sigma(\sum h_i^2 - \theta \cdot d(h))$, where $\sigma$ is ReLU. ReLU outputs values in $[0, \infty)$, making $\log(p(h))$ mathematically invalid when $p(h) \le 0$ or unbounded. BCE requires probabilities in $(0,1)$. This flaw threatens training stability and reproducibility.
2. **Lack of Matched-Capacity Baselines:** The claim that FF-Complete outperforms BP-Chain* is undermined by significant differences in parameter counts and training dynamics. Without matched-capacity controls, it is unclear whether gains stem from cyclic topology, increased capacity, or label fusion design.
3. **Label Leakage and Shortcut Learning Risk:** Direct concatenation of features and one-hot labels ($h || y_{true}$) injects label information into every neuron. This creates a high risk of trivial memorization, where neurons learn label shortcuts rather than meaningful feature representations. The paper does not provide ablation or analysis to rule out this confound.
4. **Overclaims and Unbounded Language:** Phrases like "transformative Cyclic Neural Networks," "superiority over current layer-by-layer DAG neural networks," and "first time FF beats BP" are presented as universal facts, but experiments only cover three simple benchmarks with a 4-neuron setup. These claims require strict bounding to tested settings.
5. **Insufficient Ablation and Statistical Validation:** The ablation study removes $L_N$ and $L_{Readout}$, but removing $L_{Readout}$ naturally collapses performance, offering little insight. Figure 4 uses misleadingly narrow y-axis scales that magnify minor fluctuations. No statistical significance tests are reported to confirm robustness across seeds.
6. **Complexity Analysis Overstates Parallelism:** Section 3.5 claims $O(|E|)$ complexity due to "asynchronous parallel update," but FF training typically updates neurons sequentially or in mini-batches. True asynchronous updates require lock-free optimization and stale gradient handling, which are not described.

## Key Issues
1. **Invalid Loss Function (Critical):** The use of ReLU in the goodness function combined with log in BCE (Eq. 6) causes mathematical invalidity and potential NaN gradients. This must be corrected to sigmoid or softmax to ensure $p(h) \in (0,1)$.
2. **Unfair Baseline Comparison (Major):** FF-Complete vs. BP-Chain* lacks matched parameter counts and training steps. The performance gap could be due to capacity differences rather than cyclic topology. Matched-capacity controls are essential.
3. **Label Shortcut Learning Risk (Major):** Direct label concatenation enables trivial memorization. Without disentangled fusion or ablation showing feature-only learning, the claim of robust representation learning is unverified.
4. **Overstated Novelty and Impact (Major):** Claims of "transformative" design and "first time FF beats BP" are unbounded and lack statistical validation. The results are limited to simple tabular/text benchmarks with 4 neurons.
5. **Misleading Visualization and Ablation (Minor):** Figure 4 uses narrow axis scales that exaggerate sensitivity. The ablation study lacks graph density controls and statistical tests, reducing interpretability.

## Actionable Suggestions
1. **Fix Loss Formulation:** Replace ReLU with sigmoid in the goodness function: $p(h) = \text{sigmoid}(\sum_i h_i^2 - \theta \cdot d(h))$. This ensures $p(h) \in (0,1)$ and stabilizes BCE optimization. Clarify gradient update frequency in Algorithm 1.
2. **Add Matched-Capacity Baselines:** Train BP and FF models with identical parameter counts, layer widths, and training steps. Report paired significance tests (e.g., bootstrap CI or t-test) across 20 seeds to validate performance gaps.
3. **Mitigate Label Leakage:** Explore feature-label disentangled fusion (e.g., attention-based mixing or separate label conditioning) to prevent trivial memorization. Add an ablation comparing direct concatenation vs. disentangled fusion.
4. **Bound Claims and Language:** Replace "transformative" and "first time FF beats BP" with bounded statements: "On evaluated benchmarks, FF-Complete matches/exceeds BP-Chain*, suggesting cyclic topology can compensate for localized learning limitations." Acknowledge dataset and scale limitations.
5. **Improve Visualization and Ablation:** Use full-range y-axis scales in Figure 4. Add ablation comparing graph densities (Chain vs. Cycle vs. Complete) with fixed $T$ and $\theta$. Report statistical significance for all comparisons.
6. **Clarify Complexity and Parallelism:** Acknowledge that asynchronous parallelism is constrained by hardware synchronization. State that effective complexity is $O(|E| \cdot |V|)$ per step, with $T$ bounded by over-smoothing risks.

## Storyline Options + Writing Outlines
### Abstract Outline (S1-S5)
- **S1 (Problem/Domain):** Current ANNs rely on DAG constraints and global back-propagation, limiting architectural flexibility and biological plausibility.
- **S2 (Significance/Challenge):** Relaxing DAG constraints could enable richer information flow and support localized learning paradigms, but requires new training objectives.
- **S3 (Gap):** Existing localized methods (e.g., FF, FA) struggle to match BP performance under standard layer-by-layer topologies.
- **S4 (Method):** We propose Cyclic Neural Networks (Cyclic NN), which allow flexible graph connections and are trained via localized FF objectives. We instantiate this as Graph Over MLP (GOMLP).
- **S5 (Result/Implication):** Experiments on MNIST, 20 Newsgroups, and IMDB show Cyclic NN matches/exceeds DAG baselines, suggesting architectural flexibility can compensate for localized learning limitations.

### Introduction Outline (P1-P4)
- **P1 (Motivation/Gap):** DAG structures enforce rigid information flow and global gradient dependencies. Question: Can ANNs perform competitively without DAG constraints?
- **P2 (Biological Inspiration):** Biological neural systems exhibit cyclic, graph-structured connectivity. While not a direct blueprint, this motivates exploring flexible topologies for static data processing.
- **P3 (Method Intuition):** Cyclic NN combines flexible graph connectivity with localized FF training. Neurons optimize independently using local goodness scores, eliminating cross-neuron gradient propagation.
- **P4 (Evidence/Contributions):** We introduce GOMLP, evaluate multiple graph generators, and demonstrate competitive performance on tabular/text benchmarks. Contributions: (1) conceptual framework for non-DAG ANNs, (2) GOMLP instantiation, (3) empirical validation of FF under cyclic topology.

## Priority Revision Plan
| Priority | Action | Expected Impact | Effort |
|---|---|---|---|
| **P0 (Critical)** | Fix Eq. 6 loss formulation: replace ReLU with sigmoid in goodness function. | Resolves mathematical invalidity and training instability. | Low |
| **P0 (Critical)** | Add matched-capacity BP/FF baselines with identical parameters and steps. | Validates whether gains stem from cyclic topology or capacity differences. | Medium |
| **P1 (Major)** | Bound claims: replace "transformative" and "first time FF beats BP" with scoped statements. | Improves scientific credibility and reviewer acceptance. | Low |
| **P1 (Major)** | Add statistical significance tests (bootstrap CI/t-test) across 20 seeds. | Confirms robustness of performance gaps. | Low |
| **P1 (Major)** | Expand limitations to include label shortcut risk and scalability constraints. | Addresses methodological weaknesses proactively. | Low |
| **P2 (Minor)** | Adjust Figure 4 y-axis scales to full range; add graph density ablation. | Improves visualization clarity and interpretability. | Medium |
| **P2 (Minor)** | Clarify complexity analysis: acknowledge hardware synchronization limits. | Aligns theoretical claims with practical implementation. | Low |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Limitation |
|---|---|---|---|---|---|---|
| E1 | Compare FF-Complete vs BP-Chain*/FF-Chain | MNIST, NewsGroup, IMDB; 4 neurons | Error rate (%) | FF-Complete matches/exceeds BP on MNIST/NewsGroup | FF can compete with BP under cyclic topology | Unmatched capacity; no significance tests |
| E2 | Hyperparameter sensitivity ($T$, $\theta$) | FF-Complete; $T \in [1,6]$, $\theta \in [0,5]$ | Error rate (%) | Optimal $T \approx 2-4$; $\theta > 0$ essential | Propagation steps and threshold matter | Narrow axis scales exaggerate variance |
| E3 | Ablation ($L_N$, $L_{Readout}$) | FF-Complete; remove losses | Error rate (%) | Removing $L_{Readout}$ collapses performance; $L_N$ removal increases error | Both losses are necessary | Lacks graph density control |

### Research-Theme Gap Diagnosis
The core claim that cyclic topology enables FF to outperform BP is weakly supported due to capacity mismatches and label shortcut risks. Reproducibility is aided by code release but hindered by mathematical inconsistencies in Eq. 6. Impact on practice is limited to simple benchmarks; scalability and over-smoothing remain unaddressed.

### Proposed Research Experiments (P0/P1/P2)
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Cost/Time | Expected Gain |
|---|---|---|---|---|---|---|---|
| FF beats BP due to cyclic topology | Matched-capacity FF-Complete outperforms BP-Chain | Train BP/FF with identical params/steps | BP-Chain (matched), FF-Chain | Error rate, CI | Statistically significant gain | 1 week | Validates architectural contribution |
| Label fusion does not cause shortcuts | Disentangled fusion matches direct concat | Compare concat vs attention-based mixing | Direct concat baseline | Error rate, feature-only eval | No performance drop | 3 days | Rules out shortcut learning |
| Graph density influences stability | Complete graphs stabilize over sparse | Compare Chain/Cycle/Complete with fixed $T$ | Chain, Cycle baselines | Error rate, convergence curves | Complete graph shows best stability | 2 days | Clarifies topology impact |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 4.5/10  
**Rationale:** The paper presents an interesting architectural paradigm (Cyclic NN) and integrates it with localized FF training. However, the current submission is held back by a critical mathematical flaw in the loss formulation (Eq. 6), lack of matched-capacity baselines, unbounded claims, and insufficient ablation to isolate the contribution of cyclic topology. The label shortcut risk and misleading visualizations further reduce confidence in the reported gains. With rigorous revisions to mathematical correctness, experimental fairness, and claim bounding, the paper could reach a competitive standard.

**Post-Revision Target:** [6.5, 7.5]/10  
**Conditions for Improvement:** (1) Fix loss formulation to ensure mathematical validity, (2) add matched-capacity BP/FF controls with statistical significance tests, (3) bound claims to evaluated settings and acknowledge limitations, (4) improve visualization and ablation clarity. If these are addressed, the paper would make a solid contribution to localized learning and graph-structured ANNs.