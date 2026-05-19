## Summary
# Final Review Report

## Summary
This paper proposes the difference-of-submodular Bregman divergence (DBD), a novel framework for defining meaningful divergences on discrete spaces. Building on the submodular-Bregman divergence of Iyer & Bilmes (2012b), the authors address two key limitations: the identifiability issue (requiring strict submodularity) and the limited expressiveness of ad-hoc submodular functions. By leveraging the strong difference-of-submodular (DS) decomposition, the authors theoretically prove that valid divergences can be constructed from arbitrary set functions. They further propose a learnable formulation using permutation-invariant neural networks ($\epsilon$-PointNet) and demonstrate improved performance on set clustering and retrieval tasks compared to fixed submodular baselines. The work bridges discrete convex analysis and modern metric learning, offering a flexible tool for structure-preserving distance measures.

## Strengths
1. **Theoretical Rigor and Novelty**: The paper provides a solid theoretical foundation by formally establishing the identifiability conditions for submodular-Bregman divergences (Theorem 3.1) and extending the framework to arbitrary set functions via strong DS decomposition (Theorem 3.1'). The proof that expressive power strictly increases with the richness of the underlying function class (Theorem 3.4) is a valuable theoretical contribution.
2. **Clear Motivation and Problem Formulation**: The introduction effectively identifies the limitations of classical set metrics and prior submodular-Bregman approaches (ad-hoc function choice, identifiability gaps). The transition from continuous Bregman divergences to discrete analogs is logically structured and well-motivated.
3. **Empirical Validation**: The experiments on ModelNet40 demonstrate the practical utility of the proposed DBD. The ablation studies comparing different supergradients (grow, shrink, bar) and the impact of DS decomposition provide insightful analysis into the behavior of the divergence components.
4. **Reproducibility Efforts**: The authors provide code for reproducing experiments and include detailed proofs in the appendix, which supports transparency and facilitates future research in discrete divergence learning.

## Weaknesses
1. **Methodological Opacity on Differentiability**: Section 4 introduces the DBD formulation but omits critical details on how gradients are backpropagated through the subgradient selection. The Learning Procedure mentions using the extreme point via a greedy algorithm, which is inherently non-differentiable. Without clarifying the use of a straight-through estimator or differentiable relaxation, the training mechanism is not fully reproducible.
2. **Unbounded Performance Claims**: The abstract and introduction repeatedly claim that the method "significantly improves" performance without anchoring these statements to specific benchmarks or quantitative deltas. This overstates the empirical contribution and reduces defensibility.
3. **Baseline Reproducibility Issues**: Appendix B.2 explicitly states that the MVTN baseline score was borrowed from the original paper because reproduction failed. Relying on un-reproduced baseline scores introduces comparison bias and weakens the validity of the SOTA comparison claims.
4. **Statistical Reporting Gaps**: The results section claims that the bar supergradient is "inferior with statistical significance" but does not report the specific statistical test or p-values used. Mean ± standard deviation alone is insufficient to formally establish significance.
5. **Notation Ambiguity**: Definition 2.2 uses the identical symbol $\partial f(Y)$ for both the subdifferential and superdifferential, which can cause confusion in subsequent theoretical derivations.

## Key Issues
1. **Differentiability of Subgradient Selection (Major)**: The core training loop relies on computing subgradients $h^1_Y$ and supergradients $g^2_Y$. If the extreme point is selected via a greedy algorithm, the operation is non-differentiable. The manuscript must explicitly state how gradient flow is handled (e.g., straight-through estimator, $\epsilon$-relaxation) to ensure the method is implementable and reproducible.
2. **Benchmark Comparison Validity (Major)**: Borrowing the MVTN baseline score without reproduction under the exact same protocol introduces significant comparison bias. The claim that DBD "closely approaches" or outperforms MVTN is weakened by this discrepancy. Direct comparisons should only be made against fully reproduced baselines.
3. **Statistical Significance Claims (Minor)**: Asserting statistical significance for the bar supergradient's inferior performance without reporting the test method or p-values reduces empirical rigor. Readers cannot verify the claim based on mean ± std alone.
4. **Claim-Evidence Alignment (Minor)**: Repeated use of "significantly improves" in the abstract and introduction without quantitative anchors or scope bounding creates an overclaim risk. Performance gains should be explicitly tied to the evaluated datasets and metrics.

## Actionable Suggestions
1. **Clarify Differentiability Mechanism**: In Section 4, explicitly describe how gradients are backpropagated through the subgradient selection. If using the $\epsilon$-PointNet relaxation ($\epsilon > 0$) to obtain differentiable approximations, state this clearly. If a straight-through estimator is used, justify its stability and impact on convergence.
2. **Reproduce or Separate Baselines**: Attempt to reproduce the MVTN baseline under the exact same evaluation protocol. If reproduction remains infeasible, clearly separate the comparison in Table 4 and the main text, noting that MVTN scores are borrowed and not directly comparable. Focus claims on the reproduced Densepoint baseline.
3. **Report Statistical Tests**: When claiming statistical significance (e.g., for the bar supergradient), explicitly state the test used (e.g., paired t-test) and report the p-values. This transforms qualitative observations into verifiable empirical claims.
4. **Bound Performance Claims**: Revise the abstract and introduction to replace "significantly improves" with bounded, evidence-based statements (e.g., "outperforms fixed submodular baselines on ModelNet40 clustering by X%"). Add a representative quantitative result to the abstract.
5. **Fix Notation Conflict**: Update Definition 2.2 to use distinct symbols for subdifferential ($\partial f(Y)$) and superdifferential ($\partial^+ f(Y)$ or $\bar{\partial} f(Y)$) to prevent ambiguity in Theorem 3.1 and Equation (9).
6. **Add Limitations Discussion**: In the Conclusion, add a concise paragraph acknowledging practical limitations, such as the computational overhead of subgradient computation and sensitivity to the relaxation parameter $\epsilon$.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain)**: Bregman divergences are fundamental for continuous spaces, but defining meaningful analogs for discrete sets remains challenging due to the lack of differentiable structure.
- **S2 (Prior Gap)**: Existing submodular-Bregman divergences rely on ad-hoc generating functions and lack guaranteed identifiability without strict submodularity, limiting their expressiveness and theoretical soundness.
- **S3 (Method)**: We propose the difference-of-submodular Bregman divergence (DBD), which leverages strong DS decomposition to construct valid divergences from arbitrary set functions, strictly increasing expressive power with richer function classes.
- **S4 (Learnable Formulation)**: We parameterize the generating functions using permutation-invariant neural networks ($\epsilon$-PointNet), enabling end-to-end learning of structure-preserving distance measures.
- **S5 (Result & Bounded Implication)**: Experiments on set clustering and retrieval demonstrate that DBD captures complex structural dependencies and outperforms fixed submodular baselines on evaluated benchmarks.

### Introduction Outline (Complete)
- **P1 (Big Picture)**: Define divergence and Bregman divergence in continuous spaces, highlighting their central role in ML (clustering, optimization).
- **P2 (Discrete Challenge)**: Explain why discrete spaces (e.g., point clouds, item sets) are harder to model; classical set metrics fail on large ground sets due to sparse intersections.
- **P3 (Prior Work & Gaps)**: Introduce submodular-Bregman divergence (Iyer & Bilmes, 2012b). Identify two critical gaps: (a) identifiability requires strict submodularity, which is often unverified; (b) ad-hoc function choices limit expressiveness to simple set operations.
- **P4 (Proposed Solution)**: Present DBD as a generalization using strong DS decomposition, allowing arbitrary set functions while guaranteeing divergence axioms.
- **P5 (Learnable Framework)**: Motivate the use of permutation-invariant NNs to adapt the divergence to data-driven tasks, bridging theory and practice.
- **P6 (Contributions)**: Enumerate three clear contributions: (1) theoretical identifiability proof, (2) expressive power extension via DS decomposition, (3) empirical validation on clustering/retrieval.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Clarify differentiability mechanism in Section 4 (straight-through vs $\epsilon$-relaxation). | Ensures methodological reproducibility and resolves major validity concern. | Low |
| **P0** | Reproduce MVTN baseline or clearly separate borrowed scores in Table 4. | Eliminates comparison bias and strengthens empirical claims. | Medium |
| **P1** | Report statistical tests and p-values for significance claims in Section 5. | Improves empirical rigor and defensibility of ablation results. | Low |
| **P1** | Bound performance claims in Abstract/Intro with specific metrics/datasets. | Aligns narrative with evidence, reduces overclaim risk. | Low |
| **P2** | Fix notation conflict in Definition 2.2 ($\partial$ vs $\partial^+$). | Prevents reader confusion in theoretical derivations. | Low |
| **P2** | Add limitations paragraph to Conclusion (computational cost, $\epsilon$ sensitivity). | Enhances scientific maturity and transparency. | Low |

**Execution Strategy**: Address P0 items first to secure methodological and empirical validity. Then refine P1 items to tighten claim-evidence alignment. Finally, apply P2 polish for notation and structural completeness.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | DBD behaves as proper divergence (non-negative, smaller for similar sets) | MNIST toy sets (n=50k, M=3,4), triplet loss | Qualitative DBD values | DBD values align with label similarity | Theoretical identifiability | Toy setting lacks real-world complexity |
| E2 | DBD improves set clustering over fixed submodular baselines | ModelNet40 (9843/2468), k-means, $\epsilon \in \{0, 0.001\}$ | Rand Index | DBD w/ decomposition outperforms fixed baselines significantly | Expressiveness gain | No statistical test reported for significance claims |
| E3 | DBD enables effective set retrieval | ModelNet40, top-5 retrieval, $\epsilon=0$ | mAP, Qualitative visuals | Retrieves same-class shapes; mAP ~90.13 | Practical utility | MVTN baseline score borrowed, not reproduced |
| E4 | Ablation: impact of supergradient type and DS decomposition | ModelNet40, grow/shrink/bar supergradients, w/ vs w/o DS | Rand Index | Bar supergradient inferior; DS reduces variance | Component analysis | Variance reduction not statistically tested |

### Research-Theme Gap Diagnosis
The core claim of "increased expressive power leading to better downstream performance" is supported by E2 and E3, but the causal link between DS decomposition and performance gains is partially confounded by the learnable NN capacity. The borrowed MVTN score weakens the SOTA comparison. Statistical rigor is lacking for significance claims.

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Causal role of DS decomposition | DS decomposition provides genuine expressiveness gain beyond parameter count | Matched-capacity control: single NN with same params as f1+f2 | w/o DS (matched params) | Rand Index, mAP | DS still outperforms matched control | Low | Isolates decomposition benefit from capacity |
| Statistical reliability | Performance gains are stable across random seeds | 10 seeds reported, add paired t-test vs strongest baseline | Fixed submodular baselines | p-values | p < 0.05 for key comparisons | Low | Validates significance claims |
| Baseline fairness | DBD outperforms reproduced SOTA methods | Reproduce MVTN under exact same protocol | MVTN (reproduced) | mAP | Direct comparable delta | Medium | Eliminates benchmark bias |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score**: 6.5/10
The paper presents a theoretically sound and novel extension of Bregman divergences to discrete spaces, with clear motivation and solid empirical validation on clustering and retrieval tasks. The theoretical contributions (identifiability proof, expressive power extension via DS decomposition) are strong and well-structured. However, the score is moderated by methodological opacity regarding subgradient differentiability, unbounded performance claims, and the reliance on borrowed baseline scores, which introduce reproducibility and comparison bias risks.

**Post-Revision Target**: [7.5, 8.5]/10
If the authors clarify the differentiability mechanism, reproduce or properly separate the MVTN baseline, report statistical tests for significance claims, and bound performance statements with concrete evidence, the paper will achieve high methodological rigor and empirical defensibility. The core theoretical and practical contributions are sufficiently valuable to warrant a strong acceptance after these targeted revisions.