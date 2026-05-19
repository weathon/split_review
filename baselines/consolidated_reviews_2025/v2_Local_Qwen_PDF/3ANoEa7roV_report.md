## Summary
This paper presents SynMeter, a systematic evaluation framework for tabular data synthesis algorithms. The authors critique existing evaluation metrics and propose new metrics for fidelity (Wasserstein-based), privacy (Membership Disclosure Score, MDS), and utility (Machine Learning Affinity, MLA). They also introduce a unified tuning objective to improve hyperparameter selection. Extensive experiments on 12 datasets and 8 synthesizers reveal that diffusion models achieve superior fidelity and utility but pose significant privacy risks, whereas statistical methods remain robust under differential privacy constraints. The paper provides actionable guidelines for selecting synthesizers based on specific privacy-utility trade-offs.

## Strengths
1. **Comprehensive Evaluation Framework:** The paper introduces SynMeter, a unified framework that addresses the fragmentation in current tabular data synthesis evaluations. By integrating fidelity, privacy, and utility metrics into a single pipeline, it provides a practical tool for researchers and practitioners.
2. **Novel Privacy Metric (MDS):** The Membership Disclosure Score offers a principled approach to assessing empirical privacy risks for heuristically private synthesizers. The shadow training technique effectively captures memorization effects that syntactic metrics like DCR fail to detect.
3. **Actionable Empirical Insights:** The extensive experiments on 12 datasets and 8 synthesizers yield clear, actionable guidelines. The finding that diffusion models excel in fidelity but compromise privacy, while statistical methods remain robust under DP, provides valuable direction for method selection.
4. **Unified Tuning Objective:** The proposal of a composite tuning objective based on the new metrics is a significant practical contribution. It addresses the common issue of suboptimal default hyperparameters and enables fairer comparisons across synthesizers.

## Weaknesses
1. **Conceptual Novelty of Fidelity Metric:** The proposed Wasserstein-based fidelity metric admits that its categorical component is equivalent to Total Variation Distance (TVD). This undermines the claim of a novel unified metric, as it is essentially a hybrid of existing metrics. The lack of principled normalization when summing numerical and categorical distances further weakens its defensibility.
2. **Theoretical Grounding of MDS:** The transition from the theoretical definition of disclosure risk (comparing output distributions) to the practical MDS metric (comparing nearest-neighbor distances) lacks theoretical justification. The reliance on nearest-neighbor distance can be noisy and sensitive to outliers, and the high computational cost (20 shadow models, 100 samples each) limits scalability.
3. **Arbitrary Tuning Coefficients:** The unified tuning objective combines metrics with different scales using arbitrary coefficients ($\alpha_1 = \alpha_2 = \alpha_3 = 1/3$). Without normalization, this weighting is unjustified and may favor metrics with larger numerical ranges. The risk of overfitting to the validation set is also not addressed.
4. **Vague Empirical Claims:** The abstract and introduction lack specific empirical findings, relying on vague phrases like "interesting findings." The overview of results lacks quantitative context (e.g., magnitude of performance drops under DP), reducing the impact of the conclusions.

## Key Issues
1. **Fidelity Metric Hybrid Nature:** The Wasserstein-based fidelity metric is not a novel unified metric but a hybrid of Wasserstein distance (for numerical) and Total Variation Distance (for categorical). The paper acknowledges this "slight misuse of terminology" but does not address the scale mismatch when summing these distances. This reduces the conceptual novelty and mathematical rigor of the contribution.
2. **MDS Approximation Justification:** The Membership Disclosure Score approximates distributional divergence using nearest-neighbor distance. This simplification is not theoretically justified and may be sensitive to outliers. The high computational cost also limits its practical adoption as a standard evaluation tool.
3. **Tuning Objective Normalization:** The composite tuning objective lacks metric normalization, leading to arbitrary weighting. This can bias the hyperparameter selection towards metrics with larger numerical ranges and risks overfitting to the validation set.
4. **Quantitative Context Missing:** The empirical results lack quantitative context. Claims about performance drops under DP or CTGAN's underperformance are qualitative, reducing the impact and reproducibility of the findings.

## Actionable Suggestions
1. **Reframe Fidelity Metric:** Explicitly frame the Wasserstein-based metric as a unified *protocol* rather than a novel mathematical metric. Acknowledge that the categorical component is TVD and justify why this hybrid approach is preferable. Introduce normalization for each marginal distance before aggregation to address scale mismatches.
2. **Justify MDS Approximation:** Provide empirical or theoretical justification for using nearest-neighbor distance as a proxy for distributional divergence. Discuss the computational complexity and propose a cheaper approximation (e.g., subsampling or fewer shadow models) for large datasets. Clarify that MDS measures empirical memorization risk rather than formal privacy guarantees.
3. **Normalize Tuning Objective:** Normalize each metric to a [0,1] range before aggregation in the tuning objective to ensure equal contribution. Explicitly justify the coefficient choices and discuss the risk of validation set overfitting. Consider using a separate hold-out set for final evaluation.
4. **Add Quantitative Context:** Include representative quantitative results in the abstract and overview (e.g., "fidelity drops by over 50% for deep generative models under strict DP"). This will strengthen the impact of the findings and improve reproducibility.
5. **Clarify MLA Metric:** Separate MLA scores for classification and regression tasks to avoid mixing incompatible metrics. Normalize performance gaps to a common scale before averaging and explicitly state the evaluator selection protocol.

## Storyline Options + Writing Outlines
### Abstract Outline
- **S1 (Problem):** Tabular data synthesis is critical for privacy-preserving data sharing, but evaluating synthesizers remains challenging due to fragmented metrics.
- **S2 (Gap):** Existing metrics fail to capture the fidelity-privacy-utility trade-offs and lack standardized tuning protocols, hindering fair comparisons.
- **S3 (Method):** We propose SynMeter, a unified evaluation framework with new metrics for fidelity (Wasserstein-based), privacy (Membership Disclosure Score), and utility (Machine Learning Affinity), along with a composite tuning objective.
- **S4 (Results):** Extensive experiments on 12 datasets and 8 synthesizers reveal that diffusion models excel in fidelity but compromise privacy, while statistical methods remain robust under differential privacy.
- **S5 (Impact):** Our framework provides actionable guidelines for selecting synthesizers based on specific privacy-utility requirements.

### Introduction Outline
- **P1 (Motivation):** Establish the importance of tabular data synthesis for privacy-preserving data sharing and the proliferation of synthesizers (statistical vs. deep generative).
- **P2 (Gap):** Critique current evaluation practices: fragmented metrics, lack of tuning protocols, and inability to compare HP vs DP methods fairly.
- **P3 (Solution):** Introduce SynMeter as a systematic framework addressing these gaps with unified metrics and a tuning objective.
- **P4 (Contributions):** List the four main contributions: fidelity metric, privacy metric (MDS), utility metric (MLA), and the SynMeter framework with tuning.
- **P5 (Preview):** Briefly preview the key empirical findings (diffusion models vs. statistical methods trade-off) to hook the reader.

## Priority Revision Plan
| Priority | Action | Expected Impact |
|---|---|---|
| P0 | Reframe fidelity metric as a unified protocol and add normalization for heterogeneous distances. | Strengthens conceptual novelty and mathematical rigor. |
| P0 | Justify MDS nearest-neighbor approximation and discuss computational scalability. | Improves defensibility and practical applicability of privacy metric. |
| P1 | Normalize metrics in tuning objective and justify coefficient choices. | Ensures fair hyperparameter selection and reduces overfitting risk. |
| P1 | Add quantitative context to abstract and overview (e.g., performance drop percentages). | Enhances impact and reproducibility of empirical findings. |
| P2 | Separate MLA scores for classification and regression tasks. | Improves metric reliability and comparability across datasets. |
| P2 | Soften critique of MIAs and acknowledge limitations of duplication experiment. | Increases objectivity and fairness in related work comparison. |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Evaluate MDS effectiveness vs DCR/MIAs | PATE-GAN (varying $\epsilon$), TabDDPM (duplication) | MDS, DCR, TPR@1%FPR | MDS detects privacy risks better | MDS is reliable | Duplication experiment is artificial |
| E2 | Assess tuning objective impact | 8 synthesizers, 12 datasets | Fidelity, MLA, Query Error | Tuning improves all metrics | Tuning is beneficial | Coefficients are arbitrary |
| E3 | Overall synthesizer comparison | HP vs DP synthesizers | Fidelity, MDS, MLA, Query Error | Diffusion models excel in fidelity/utility but compromise privacy | Trade-off exists | Lacks quantitative context |
| E4 | In-depth analysis of CTGAN/TabDDPM | Learning trajectory analysis | Wasserstein distance | CTGAN stagnates due to preprocessing; TabDDPM minimizes Wasserstein | Mechanism explained | Limited to Bean dataset |

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Estimated Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| MDS Scalability | Subsampling shadow models maintains accuracy | Vary number of shadow models (5, 10, 20) | Full MDS computation | Correlation with full MDS | Correlation > 0.9 | Low | Improves practical applicability |
| Tuning Normalization | Normalized metrics yield more stable tuning | Normalize metrics to [0,1] before aggregation | Original tuning objective | Variance across seeds | Lower variance | Low | Strengthens tuning protocol |
| Real-world Memorization | Rare minority samples increase MDS | Add rare samples to training set | Baseline dataset | MDS, Fidelity | MDS increases with rare samples | Medium | Validates MDS in realistic settings |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
Final Score: 6/10
Post-Revision Target: [7, 8]/10

**Rationale:** The paper makes a valuable practical contribution by introducing SynMeter, a unified evaluation framework for tabular data synthesis. The empirical findings regarding the fidelity-privacy-utility trade-offs are insightful and actionable. However, the conceptual novelty of the proposed metrics is weakened by the hybrid nature of the fidelity metric and the lack of theoretical grounding for the MDS approximation. The arbitrary tuning coefficients and lack of quantitative context in the results further reduce the rigor. Addressing these issues through normalization, justification, and clearer framing would significantly strengthen the paper's defensibility and impact.