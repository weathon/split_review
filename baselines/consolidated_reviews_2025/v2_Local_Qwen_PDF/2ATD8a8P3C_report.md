## Summary
# Final Review Report

## Summary
This paper proposes a general framework for conformal structured prediction, addressing the limitation of standard conformal prediction methods that produce large, uninterpretable flat label sets for complex structured outputs (e.g., text, code, hierarchical labels). The core challenge identified is the breakdown of monotonicity between the conformal threshold $\tau$ and coverage/set size in structured settings. To handle this, the authors adapt techniques from the learn-then-test framework, employing a sequential statistical testing procedure to estimate the optimal threshold. The framework is extended to provide probably approximately correct (PAC) coverage guarantees and instantiated for directed acyclic graph (DAG) structures using an integer programming formulation. Empirical evaluations across five domains (MNIST digits, ImageNet hierarchical classification, SQuAD question answering, MBPP code generation, and GoEmotions) demonstrate that the proposed method constructs significantly smaller, interpretable prediction sets while satisfying desired marginal and PAC coverage guarantees, outperforming monotonic baselines.

## Strengths
1. **Clear Problem Formulation and Motivation**: The paper effectively identifies a critical gap in conformal prediction: standard methods produce uninterpretable flat sets for structured outputs. The motivation for structured prediction sets is well-articulated and practically relevant.
2. **Theoretical Soundness**: The proposed sequential testing framework correctly handles the non-monotonicity challenge. The extension to PAC guarantees (Theorem 3.2) is theoretically rigorous and provides stronger reliability assurances for safety-critical applications.
3. **General and Flexible Framework**: The abstraction of the structured prediction set space $\tilde{Y}$ and the mapping $\gamma$ allows the framework to be applied to diverse domains (hierarchies, intervals, partial programs) without modifying the core algorithm.
4. **Comprehensive Empirical Validation**: The evaluation across five distinct domains demonstrates the versatility and effectiveness of the approach. The consistent improvement in prediction set size over monotonic baselines strongly supports the methodological advantage.
5. **Practical Instantiation**: The integer programming formulation for DAG-structured sets is well-designed and efficiently solvable for the problem sizes encountered, providing a concrete and implementable solution.

## Weaknesses
1. **Limited Discussion of Computational Scalability**: While the integer programming formulation is efficient for the tested DAG sizes, the paper does not thoroughly discuss scalability to very large or dense DAGs. The NP-hard nature of IP is acknowledged only implicitly, and potential approximation algorithms or heuristics for larger-scale settings are not explored.
2. **Abstract and Introduction Could Be Tighter**: The abstract omits the core methodological challenge (non-monotonicity) and the specific algorithmic strategy. The introduction opening is slightly verbose and could more directly connect the interpretability gap to the need for structured sets.
3. **Contribution Statement Density**: The contributions are presented as a single dense paragraph. Breaking them into a bulleted list would improve readability and help reviewers quickly identify the distinct technical advances (framework, PAC extension, DAG instantiation).
4. **Missing Explicit Causal Link in Results**: The results section demonstrates size improvements over baselines but does not explicitly connect this to the non-monotonic search flexibility. Adding a sentence to make this causal link clear would strengthen the argument.
5. **Conclusion Lacks Empirical Summary and Future Directions**: The conclusion summarizes the framework but omits the key empirical finding (smaller sets than baseline) and does not mention limitations or future work, missing an opportunity for a more balanced closing.

## Key Issues
1. **Non-Monotonicity Explanation**: The breakdown of monotonicity in structured prediction is a central methodological challenge. The current explanation could better clarify *why* monotonicity fails (due to the discrete, combinatorial nature of structured sets causing coverage to fluctuate non-monotonically as $\tau$ increases). Explicitly stating this will strengthen the motivation for the sequential testing approach.
2. **PAC Proof Clarity**: The proof of Theorem 3.2 correctly extends the learn-then-test idea to PAC guarantees but could be more explicit about the connection between the sequential search and the PAC bound. Clarifying that the algorithm returns the *last valid* threshold before the first invalid one, and that the PAC test controls the probability of falsely accepting an invalid threshold, will improve theoretical transparency.
3. **DAG Structure Generality**: The distinction between the DAG structure on the *space of prediction sets* versus the *label space* is a key insight for the framework's generality. This point is currently buried and should be highlighted earlier to clarify that users can define arbitrary DAG structures over label subsets regardless of the underlying label topology.
4. **IP Scalability Acknowledgment**: Given that integer programming is generally NP-hard, briefly acknowledging computational complexity and noting that the specific constraint structure allows efficient solving in practice will preempt reviewer concerns about scalability to larger DAGs.
5. **Results Causal Link**: The empirical size improvements over baselines should be explicitly linked to the methodological advantage of non-monotonic search flexibility. This causal connection reinforces the practical value of the proposed framework.

## Actionable Suggestions
1. **Restructure Abstract**: Revise the abstract into a compact 5-sentence logic: (1) Problem & significance, (2) Prior gap, (3) Core methodological challenge & solution (non-monotonicity handled via sequential testing), (4) Key theoretical contribution (PAC guarantees), (5) Empirical validation. Explicitly mention the non-monotonicity challenge and PAC extension.
2. **Tighten Introduction Opening**: Consolidate the first two paragraphs to quickly establish the stakes (DNN reliability requires uncertainty quantification) and immediately pivot to the interpretability gap for structured outputs. Clearly state the lack of general algorithms as the core gap.
3. **Bullet-Point Contributions**: Break the contributions paragraph into a bulleted list separating the three core advances: (1) general framework handling non-monotonicity, (2) PAC guarantee extension, (3) efficient DAG instantiation via integer programming.
4. **Clarify Non-Monotonicity Mechanism**: In the method intuition paragraph, explicitly explain *why* monotonicity breaks (discrete combinatorial structures cause coverage to fluctuate as $\tau$ increases). This strengthens the motivation for sequential testing.
5. **Strengthen PAC Proof Explanation**: Add a sentence bridging the sequential search logic with the PAC probability bound, clarifying that returning the last valid threshold before the first invalid one ensures the PAC guarantee holds with probability $1-\delta$.
6. **Highlight DAG Generality**: Move the insight that the DAG structure applies to the *prediction set space* (not just the label space) earlier in the DAG formulation section and emphasize it to highlight framework flexibility.
7. **Acknowledge IP Scalability**: Add a brief note on computational complexity and solver efficiency, referencing Appendix A.2, to address potential scalability concerns.
8. **Link Results to Methodology**: In the results discussion, explicitly connect the observed size improvements to the non-monotonic search flexibility, reinforcing the causal argument.
9. **Enhance Conclusion**: Summarize the key empirical finding (smaller sets than baseline) and add a brief sentence on limitations (e.g., IP solve time for dense DAGs) or future work (e.g., approximate algorithms for larger DAGs).

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain)**: Conformal prediction provides distribution-free coverage guarantees but traditionally outputs flat label sets that become uninterpretable for complex structured outputs like text or hierarchical labels.
- **S2 (Significance/Challenge)**: Standard methods ignore label space structure, leading to large prediction sets that hinder practical deployment in safety-critical or human-interfacing applications.
- **S3 (Prior Gap)**: Existing domain-specific approaches lack a general framework and often enforce restrictive monotonicity assumptions that limit set compactness.
- **S4 (Proposed Method)**: We propose a general framework for conformal structured prediction that handles inherent non-monotonicity via a sequential statistical testing procedure, extending to PAC guarantees.
- **S5 (Key Result/Implication)**: Empirical evaluations across five domains demonstrate that our method constructs significantly smaller, interpretable prediction sets while satisfying desired coverage guarantees, outperforming monotonic baselines.

### Introduction Outline (Complete)
- **P1 (Big Picture & Stakes)**: DNN reliability requires robust uncertainty quantification. Conformal prediction offers rigorous coverage guarantees but produces uninterpretable flat sets for structured outputs.
- **P2 (Concrete Gap)**: Naive application of standard CP ignores label structure, yielding large sets. Prior work targets specific domains (code, QA) without a unified framework or handling of non-monotonicity.
- **P3 (Proposed Solution & Intuition)**: We introduce a general framework that searches over interpretable structured sets. By adapting learn-then-test techniques, we sequentially test thresholds to bypass monotonicity requirements.
- **P4 (Method Details & DAG Instantiation)**: The framework supports marginal and PAC guarantees. We instantiate it for DAG-structured sets (hierarchies, intervals, partial programs) via integer programming.
- **P5 (Evidence Preview & Contributions)**: Experiments across five domains show smaller sets than baselines with guaranteed coverage. Contributions: (1) general non-monotonic framework, (2) PAC extension, (3) efficient DAG instantiation.

## Priority Revision Plan
| Priority | Action | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Restructure Abstract & Introduction: Explicitly mention non-monotonicity challenge, PAC contribution, and tighten motivation flow. | Improves methodological clarity, impact, and reader engagement from the start. | Low |
| **P0** | Bullet-Point Contributions: Separate framework, PAC extension, and DAG instantiation into distinct bullet points. | Enhances readability and helps reviewers quickly identify technical advances. | Low |
| **P1** | Clarify Non-Monotonicity Mechanism: Explain *why* monotonicity breaks (discrete combinatorial structures) in the method intuition paragraph. | Strengthens motivation for sequential testing and theoretical transparency. | Low |
| **P1** | Strengthen PAC Proof Explanation: Add sentence bridging sequential search logic with PAC probability bound. | Improves theoretical rigor and proof clarity. | Low |
| **P1** | Link Results to Methodology: Explicitly connect size improvements to non-monotonic search flexibility. | Reinforces causal argument and practical value of the framework. | Low |
| **P2** | Highlight DAG Generality: Emphasize that DAG structure applies to prediction set space, not just label space. | Highlights framework flexibility and generality. | Low |
| **P2** | Acknowledge IP Scalability: Add brief note on computational complexity and solver efficiency. | Preempts scalability concerns. | Low |
| **P2** | Enhance Conclusion: Summarize key empirical finding and add limitations/future work. | Provides balanced closing and forward-looking perspective. | Low |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Validate coverage guarantees (marginal/PAC) across domains | 5 domains (MNIST, ImageNet, SQuAD, MBPP, GoEmotions); held-out test set; baseline from Khakhar et al. | Coverage Rate, Avg Set Size | Coverage meets/exceeds desired level; size smaller than baseline | Framework achieves guarantees and compact sets | Baseline comparison limited to one monotonic method |
| E2 | Analyze hyperparameter sensitivity ($m$, $\epsilon$, $\delta$) | Vary $m \in \{1,2,4,8\}$, $\epsilon \in \{0.05,0.1,0.15,0.2\}$, $\delta \in \{0.1,0.01,0.001\}$ | Coverage Rate, Avg Set Size | Size decreases with $\epsilon, \delta, m$; coverage stable | Hyperparameters control interpretability/coverage trade-off | Sensitivity analysis focused on QA task |
| E3 | Evaluate computational cost & scalability | Measure IP solve time and $\tau$ estimation time across domains | Solve Time (s/hr) | Fast for small DAGs; scales with density/size | IP formulation is practical for tested sizes | Dense/large DAGs may incur high solve times |

### Research-Theme Gap Diagnosis
- **Robustness to Distribution Shift**: No out-of-domain (OOD) evaluation is reported. It is unclear how structured sets behave under covariate shift or label noise.
- **Scalability to Large DAGs**: While IP solves efficiently for current sizes, performance on very large or dense DAGs (e.g., full WordNet hierarchies) is not thoroughly stress-tested.
- **Alternative Structured Spaces**: The framework is instantiated for DAGs, but other structured spaces (e.g., manifolds, graphs with cycles) are not explored.

### Proposed Research Experiments (P0/P1/P2)
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Estimated Cost/Time | Expected Paper-Quality Gain |
|---|---|---|---|---|---|---|---|
| OOD Robustness | Structured sets maintain coverage under distribution shift | Evaluate on shifted splits (e.g., ImageNet-R, SQuAD adversarial) | Standard CP, Monotonic Baseline | Coverage Rate, Size Delta | Coverage $\ge 1-\epsilon$ with reasonable size increase | Low (1-2 days) | Strengthens reliability claims |
| Large-Scale Scalability | IP solve time remains manageable for larger DAGs | Test on full WordNet hierarchy or synthetic dense DAGs | Heuristic approximations (if available) | Solve Time, Optimality Gap | Solve time $< 1$ min per sample | Medium (3-5 days) | Addresses scalability concerns |
| Alternative Structures | Framework extends to non-DAG structures (e.g., interval graphs) | Instantiate for interval-based or graph-structured label spaces | Domain-specific baselines | Coverage Rate, Size | Comparable performance to DAG instantiation | Medium (1 week) | Demonstrates broader applicability |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score**: 7.5/10

**Post-Revision Target**: [8.0, 9.0]/10

**Scoring Rationale**:
The paper presents a theoretically sound and practically valuable framework for conformal structured prediction. The core contribution—handling non-monotonicity via sequential testing to produce compact, interpretable sets—is novel and well-executed. The extension to PAC guarantees and the efficient DAG instantiation via integer programming are significant technical advances. Empirical results across five domains strongly support the claims, demonstrating consistent improvements over monotonic baselines.

The score is slightly moderated by the need for tighter narrative framing (abstract/introduction), more explicit causal links in the results discussion, and a brief acknowledgment of IP scalability limitations. These are largely writing and presentation issues rather than fundamental scientific flaws. With the recommended revisions, the paper would be highly competitive for top-tier venues.

**Top-Meat-Bottom Opinion**:
*Top*: The paper effectively addresses a critical gap in conformal prediction by introducing a general framework for structured prediction sets. The theoretical treatment of non-monotonicity and PAC guarantees is rigorous, and the empirical validation is comprehensive and convincing.
*Meat*: The main areas for improvement are narrative clarity (explicitly connecting non-monotonicity to size improvements) and scalability discussion (acknowledging IP complexity). The contribution statement and conclusion could also be strengthened with better structure and empirical summary.
*Bottom*: Overall, this is a strong contribution to uncertainty quantification. Addressing the minor writing and framing suggestions will significantly enhance readability and impact, making it a compelling addition to the conformal prediction literature.