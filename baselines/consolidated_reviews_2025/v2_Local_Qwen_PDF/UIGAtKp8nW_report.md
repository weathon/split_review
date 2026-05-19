## Summary
The paper introduces MUBEN, a comprehensive benchmark for evaluating uncertainty quantification (UQ) methods applied to pre-trained molecular representation models. The authors systematically assess diverse UQ strategies (deterministic, Bayesian, calibration, ensembles) across multiple backbone architectures (ChemBERTa, GROVER, Uni-Mol, DNN, etc.) and molecular descriptors. Experiments are conducted on standard MoleculeNet datasets under both scaffold (OOD) and random (IID) splits. The study provides practical insights into the trade-offs between predictive accuracy, calibration quality, and computational cost, highlighting that Deep Ensembles consistently improve performance at high compute cost, while Temperature Scaling and MC Dropout offer efficient alternatives for classification.

## Strengths
1. **Comprehensive Benchmark Scope:** MUBEN covers a wide range of modern pre-trained molecular backbones (string, 2D graph, 3D conformer) and pairs them with diverse UQ methods, addressing a clear gap in systematic evaluation.
2. **Rigorous Evaluation Protocol:** The use of scaffold splitting to simulate OOD conditions, alongside random splits for IID comparison, provides a robust assessment of generalization and calibration behaviors.
3. **Actionable Insights:** The paper delivers clear, practical guidelines for practitioners, such as recommending Temperature Scaling for efficient classification calibration and BBP/SGLD for regression uncertainty, balancing performance with computational feasibility.
4. **Reproducibility Effort:** The authors provide detailed implementation notes, hyperparameter settings, and open-source code, facilitating community adoption and extension.

## Weaknesses
1. **Vague Novelty Positioning:** The related work section lists prior benchmarks but does not explicitly contrast MUBEN's methodology, backbone coverage, or evaluation protocols with the closest molecular UQ studies, weakening the novelty claim.
2. **Conflated Accuracy and Calibration Claims:** The results introduction implies that UQ methods generally mitigate distribution gaps to improve test results, which is misleading for post-hoc methods (e.g., Temperature Scaling) that only recalibrate outputs without altering predictive accuracy.
3. **Absolute Language in Conclusions:** Statements like "Deep Ensembles assures performance enhancement under all circumstances" are overly strong and risk being challenged; bounding these claims to evaluated settings would improve scientific rigor.
4. **Limited Discussion on Class Imbalance Impact:** Several datasets (e.g., MUV, HIV) exhibit extreme label imbalance, which can skew calibration metrics like ECE. The manuscript does not sufficiently discuss how this imbalance affects UQ evaluation or whether class-weighting strategies were applied.
5. **Symbolic Cost Analysis Lacks Empirical Grounding:** Table 6 provides symbolic computational costs but omits concrete timing examples, making it difficult for practitioners to assess real-world deployment feasibility across backbones of varying sizes.

## Key Issues
1. **Claim-Evidence Alignment on UQ Benefits:** The manuscript occasionally conflates improvements in predictive accuracy with improvements in uncertainty calibration. Only stochastic/ensemble methods (Deep Ensembles, MC Dropout) explore broader loss landscapes to potentially improve point predictions; post-hoc methods solely adjust confidence scores. This distinction must be explicitly maintained throughout the results discussion.
2. **Novelty Differentiation:** The gap statement identifies limitations in prior work but lacks a direct, side-by-side comparison with the most relevant molecular UQ benchmarks. Explicitly stating which backbones, UQ categories, or evaluation splits were missing in prior studies will strengthen the contribution claim.
3. **Defensibility of Absolute Claims:** Phrases like "assures performance enhancement under all circumstances" are scientifically risky. Benchmark results are inherently bounded by the specific hyperparameter grids, backbone versions, and dataset splits evaluated. Claims should be bounded to reflect this scope.

## Actionable Suggestions
1. **Refine Abstract Closing:** Replace the vague final sentence with a concrete summary of the top empirical finding (e.g., "Deep Ensembles consistently enhance calibration but incur high compute costs, while Temperature Scaling offers an efficient alternative for classification").
2. **Strengthen Introduction Motivation:** Explicitly link the high cost of experimental validation to the necessity of uncertainty-aware predictions for guiding downstream decisions (e.g., active learning, filtering false positives).
3. **Synthesize Related Work:** Group prior UQ studies by method category or scope limitation rather than listing them. Add a sentence explicitly contrasting MUBEN with the closest molecular benchmarks to clarify missing backbones/methods.
4. **Clarify Results Interpretation:** Distinguish between UQ methods that improve predictive accuracy (ensembles, MC Dropout) and those that only improve calibration (Temperature Scaling, Platt Scaling) to avoid conflating generalization with confidence estimation.
5. **Bound Conclusion Claims:** Replace absolute phrasing ("assures performance enhancement under all circumstances") with bounded language ("consistently improves performance across evaluated settings"). Expand limitations to specify hyperparameter search spaces and backbone versions.
6. **Address Class Imbalance in Appendix:** Add a note explaining how extreme label imbalance (e.g., MUV LIR > 0.99) impacts calibration metrics and confirm whether class-weighted losses were used during training.
7. **Ground Computational Costs:** Supplement the symbolic cost table with concrete empirical timing examples (e.g., wall-clock hours on an A100 GPU) for a representative backbone to improve practical feasibility assessment.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- S1 (Problem & Domain): Large molecular representation models excel at property prediction but often exhibit overconfidence on out-of-distribution test data.
- S2 (Significance/Challenge): Reliable uncertainty estimates are critical for high-stakes downstream applications like drug discovery, yet selecting appropriate UQ methods remains underexplored.
- S3 (Prior Gap): Existing studies evaluate limited UQ strategies on narrow task subsets or older architectures, lacking a systematic comparison across modern pre-trained backbones.
- S4 (Proposed Method): We present MUBEN, a comprehensive benchmark evaluating diverse UQ categories (deterministic, Bayesian, calibration, ensembles) across state-of-the-art molecular backbones and descriptors.
- S5 (Key Result & Implication): Our experiments reveal that Deep Ensembles consistently improve calibration at high compute cost, while Temperature Scaling and MC Dropout offer efficient alternatives for classification, providing actionable guidelines for uncertainty-critical deployments.

### Introduction Outline (Complete)
- P1 (Big Picture & Motivation): Molecular representation learning accelerates scientific discovery but relies on expensive experimental data. Self-supervised pre-training mitigates data scarcity, yet models must also quantify uncertainty to guide costly downstream decisions.
- P2 (Problem & Prior Work): Calibrated uncertainty enables robust high-throughput screening and active learning. While several works apply UQ to molecular prediction, they typically focus on isolated methods or limited property categories, leaving backbone-UQ interactions poorly understood.
- P3 (Gap Statement): Prior benchmarks lack comprehensive coverage of modern pre-trained backbones (e.g., 3D conformer-based models) and diverse UQ strategies, and rarely evaluate performance under rigorous out-of-distribution splits.
- P4 (Solution & Contributions): We introduce MUBEN to systematically assess UQ performance across multiple backbones and descriptors. Contributions: (1) a broad benchmark spanning diverse UQ categories and architectures, (2) analysis of backbone-UQ interactions under OOD/IID settings, and (3) practical selection guidelines for practitioners.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| P0 (Must) | Refine Abstract & Intro to explicitly link expensive data costs to the need for UQ, and add a concrete key result sentence. | Improves reader engagement and clearly communicates empirical contribution upfront. | Low |
| P0 (Must) | Clarify Results section to distinguish between UQ methods that improve predictive accuracy (ensembles) vs. those that only improve calibration (post-hoc). | Prevents scientific misinterpretation and strengthens claim-evidence alignment. | Low |
| P1 (High) | Strengthen Related Work by explicitly contrasting MUBEN with prior molecular UQ benchmarks (missing backbones, splits, methods). | Solidifies novelty claim and positions the benchmark more effectively. | Medium |
| P1 (High) | Bound absolute claims in Conclusion (e.g., Deep Ensembles performance) and specify concrete limitations (hyperparameter scope). | Increases scientific rigor and defensibility against reviewer challenges. | Low |
| P2 (Medium) | Add empirical timing examples to Appendix C cost table and discuss class imbalance impact on UQ metrics in Appendix A. | Grounds feasibility claims and improves reproducibility/transparency. | Medium |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Evaluate UQ methods across diverse backbones | 6 backbones, 8 UQ methods, 14 datasets (scaffold split) | ROC-AUC, RMSE, MAE, ECE, NLL, BS, CE | Deep Ensembles consistently improve calibration; Uni-Mol strongest but overconfident | C1, C2 | Coarse hyperparameter grids |
| E2 | Compare OOD vs IID performance | Scaffold split vs Random split on subset of datasets | Same as E1 | Scaffold splits reveal larger UQ gaps; Bayesian methods struggle on IID balanced data | C2 | Limited random split datasets |
| E3 | Assess frozen backbone impact | Freeze backbone weights, fine-tune only head | Same as E1 | Frozen backbones underperform significantly; fine-tuning is critical | C2 | Not evaluated across all UQ methods |

### Research-Theme Gap Diagnosis
The core research value lies in providing actionable guidelines for selecting UQ methods under computational constraints. However, the current experiments lack a direct analysis of the accuracy-calibration trade-off curve (e.g., Expected Calibration Error vs. ROC-AUC) to help practitioners make explicit budget-aware decisions. Additionally, the impact of extreme class imbalance on calibration metrics is not explicitly quantified.

### Proposed Research Experiments (P0/P1/P2)
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| C3 (Practical Guidelines) | There is a quantifiable trade-off between calibration quality and predictive accuracy across UQ methods. | Plot ECE/NLL vs ROC-AUC/RMSE for all backbone-UQ pairs. | Deterministic baseline | Accuracy-Calibration Pareto frontier | Clear Pareto frontiers emerge | Low | Directly supports budget-aware method selection |
| C2 (OOD/IID Analysis) | Extreme class imbalance skews calibration metrics independently of UQ method quality. | Evaluate UQ on balanced vs imbalanced subsets of MUV/HIV. | Class-weighted vs unweighted loss | ECE, Brier Score | Imbalance effect quantified | Medium | Clarifies dataset-specific UQ challenges |
| C1 (Benchmark Scope) | Symbolic computational costs do not reflect real-world deployment feasibility. | Report wall-clock training/inference times for ChemBERTa/Uni-Mol. | Hardware: A100 GPU | Hours/minutes per epoch | Concrete timing table added | Low | Grounds feasibility claims for practitioners |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
Final Score: 6/10
Post-Revision Target: [7, 8]/10

**Justification:** The paper presents a valuable and timely benchmark (MUBEN) that addresses a clear need in the molecular machine learning community. The experimental scope is broad, covering diverse backbones, UQ methods, and evaluation splits, and the results provide actionable insights for practitioners. However, the current score is held back by vague novelty positioning, occasional conflation of predictive accuracy with calibration improvements, and overly absolute claims in the conclusion. With targeted revisions to clarify the accuracy-calibration distinction, strengthen the related work contrast, and bound the empirical claims, the paper can easily reach a strong acceptance score.