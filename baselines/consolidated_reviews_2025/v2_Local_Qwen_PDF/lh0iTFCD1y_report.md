## Summary
# Final Review Report

## Summary
The paper introduces LUMA, a novel multimodal benchmark dataset designed for evaluating Uncertainty Quantification (UQ) methods under controlled noise and diversity conditions. LUMA extends CIFAR-10/100 with aligned audio (extracted from speech corpora) and text (generated via Gemma-7B) modalities across 50 classes. The authors provide a Python toolkit for injecting modality-specific aleatoric and epistemic uncertainties, including data diversity control, sample noise, label noise, and OOD injection. Baseline evaluations using Monte-Carlo Dropout (MCD), Deep Ensembles (DE), and Reliable Conflictive Multi-View Learning (RCML) demonstrate the dataset's utility, particularly highlighting RCML's superior OOD detection capability compared to MCD and DE. The work addresses a clear gap in multimodal UQ benchmarking by enabling fine-grained, realistic uncertainty injection.

## Strengths
1. **Clear Problem Formulation and Motivation:** The paper identifies a critical gap in Multimodal Uncertainty Quantification (MUQ) benchmarking: the lack of datasets that allow controlled, modality-specific uncertainty injection. The motivation for moving beyond simple Gaussian noise to realistic, parameterized perturbations is well-articulated.
2. **Comprehensive Dataset Construction:** LUMA thoughtfully integrates three distinct modalities (image, audio, text) with careful alignment strategies. The use of diverse audio corpora and LLM-generated text, combined with rigorous validation pipelines (Whisper transcription, manual annotation, bias filtering), demonstrates high data quality and reproducibility.
3. **Actionable Benchmarking Toolkit:** The provided Python package for generating dataset variants with controlled diversity, noise, and OOD samples is a significant practical contribution. It lowers the barrier for researchers to evaluate UQ methods under standardized, reproducible conditions.
4. **Insightful Baseline Evaluations:** The comparative analysis of MCD, DE, and RCML provides valuable initial insights. The finding that RCML achieves strong OOD detection (0.91 AUC) while MCD/DE struggle (~0.5 AUC) effectively validates the dataset's capacity to differentiate UQ method robustness.

## Weaknesses
1. **Lack of Variance Reporting and Statistical Significance:** The experimental results (Tables 1 and 2) report point estimates without variance (e.g., mean ± std over multiple seeds) or statistical significance tests. This limits the ability to assess the stability and reliability of the reported uncertainty metrics and OOD AUC scores.
2. **Ambiguous Mathematical Notation:** Equation 1 for diversity control is presented with fragmented notation in the manuscript, making it difficult to reproduce exactly. The relationship between the inverse distance, the exponent $k$, and the categorical sampling distribution needs precise mathematical formulation.
3. **Overstated Comparative Claims:** The conclusion that MCD and DE "fail" at OOD detection is strong and potentially overstated. While valid under the reported baseline settings, MCD/DE performance is sensitive to architecture and tuning. The claim should be bounded to the specific experimental setup to maintain scientific rigor.
4. **Missing Implementation Details for UQ Metrics:** Section 4.2 defines uncertainty metrics but omits critical reproducibility details, such as the number of Monte Carlo passes for MCD and the exact aggregation method for aleatoric/epistemic probabilities.
5. **Abstract Lacks Concrete Empirical Findings:** The abstract ends with a forward-looking anticipation rather than summarizing the key validated results. Including a concise statement of the main empirical finding (e.g., RCML's superior OOD detection) would significantly strengthen the abstract's impact.

## Key Issues
1. **Reproducibility Risk in Diversity Control (Page 6):** The fragmented notation of Equation 1 prevents exact replication of the diversity sampling mechanism. Without a clear mathematical definition of the inverse distance weighting and categorical distribution, other researchers cannot reliably reproduce the dataset variants.
2. **Statistical Reliability of Benchmarking Results (Page 9):** The absence of variance reporting across random seeds undermines confidence in the comparative claims. Small differences in uncertainty metrics or AUC scores could be due to random initialization rather than methodological superiority.
3. **Scope Overreach in Baseline Critique (Page 10):** Declaring that MCD and DE "fail" at OOD detection without acknowledging architectural sensitivity or calibration techniques risks misleading readers about the general capabilities of these widely used UQ methods.
4. **Missing UQ Implementation Details (Page 8):** Omitting the number of MC passes and probability aggregation details hinders the ability to benchmark new methods against the reported baselines fairly.

## Actionable Suggestions
1. **Rewrite Equation 1 with Standard Notation:** Replace the fragmented formula with a clear mathematical definition: $D_i = \| F_i - \mu_C \|_2^{-k}$, where $\mu_C$ is the class mean. Explicitly state that samples are drawn from a categorical distribution proportional to $D_i$, and clarify the effect of $k$ on diversity.
2. **Add Variance Reporting to Tables 1 and 2:** Re-run baseline evaluations with at least 3 random seeds. Report results as mean ± standard deviation. Add a brief note on statistical significance if differences are marginal.
3. **Bound Comparative Claims in Discussion:** Revise the statement that MCD/DE "fail" to: "Under our baseline configuration, MCD and DE struggle to provide epistemic uncertainty values suitable for OOD detection on LUMA (~0.5 AUC), whereas RCML demonstrates robustness (0.91 AUC)."
4. **Specify UQ Implementation Details:** In Section 4.2, add the number of Monte Carlo passes (e.g., 50) and clarify how aleatoric/epistemic probabilities are aggregated across passes or ensemble members.
5. **Strengthen Abstract with Key Findings:** Append one sentence to the abstract summarizing the main empirical result: "Baseline evaluations demonstrate that RCML achieves 0.91 AUC for OOD detection, significantly outperforming MCD and DE, thereby validating LUMA's utility for differentiating UQ robustness."

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem/Domain):** Multimodal Deep Learning enhances decision-making but struggles with trustworthiness under uncertainty.
- **S2 (Significance/Challenge):** Developing robust MUQ methods requires benchmarks that can isolate and control modality-specific uncertainties.
- **S3 (Prior Gap):** Existing datasets lack fine-grained, parameterized uncertainty injection, relying instead on simplistic noise models.
- **S4 (Proposed Method):** We introduce LUMA, a multimodal dataset (image/audio/text) with a Python toolkit for controlled diversity, noise, and OOD injection.
- **S5 (Key Result/Implication):** Baseline evaluations reveal RCML's superior OOD detection (0.91 AUC) versus MCD/DE limitations, validating LUMA's capacity to differentiate UQ robustness.

### Introduction Outline (Complete)
- **P1 (Big Picture):** Establish the rise of MDL in safety-critical domains and the necessity of trustworthiness/UQ.
- **P2 (Concrete Gap):** Identify the lack of controlled, modality-specific uncertainty injection in current benchmarks, hindering rigorous MUQ evaluation.
- **P3 (Proposed Solution):** Introduce LUMA's core design: aligned multimodal data with parameterized uncertainty controls (diversity, noise, OOD).
- **P4 (Evidence Preview):** Preview baseline findings showing how LUMA exposes limitations in standard UQ methods (MCD/DE) while validating robust approaches (RCML).
- **P5 (Contribution Summary):** List the three contributions: dataset, toolkit, and baseline models, explicitly linking them to the gap and evidence.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Rewrite Eq. 1 with precise mathematical notation and clarify sampling distribution. | Eliminates reproducibility ambiguity for diversity control. | Low |
| **P0** | Add variance reporting (mean ± std over ≥3 seeds) to Tables 1 and 2. | Strengthens statistical reliability of benchmarking claims. | Medium |
| **P1** | Bound comparative claims about MCD/DE failure to the specific baseline setup. | Improves scientific rigor and prevents scope overreach. | Low |
| **P1** | Specify UQ implementation details (MC passes, aggregation method) in Section 4.2. | Enables fair replication and comparison by future work. | Low |
| **P2** | Update abstract and conclusion to include key empirical findings and limitations. | Enhances narrative closure and reader comprehension. | Low |

**Page Coverage Audit:**
- Page 1: 2 annotations (Abstract, Intro) - Covered
- Page 2: 2 annotations (Contributions, Limitations) - Covered
- Page 3: 1 annotation (Image Modality) - Covered
- Page 6: 1 annotation (Dataset Compilation/Eq. 1) - Covered
- Page 8: 1 annotation (Uncertainty Metrics) - Covered
- Page 9: 1 annotation (Results Tables) - Covered
- Page 10: 2 annotations (Discussion, Conclusion) - Covered
- Appendix: Skipped (boilerplate/license details do not affect core scientific claims).

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Controlled noise increases UQ metrics | Clean vs. Diversity/Label/Sample Noise variants | Aleatoric/Epistemic Entropy | Noise generally increases uncertainty; diversity reduction decreases it in MCD/DE | Toolkit effectively modulates uncertainty | No variance reported |
| E2 | RCML outperforms MCD/DE in OOD detection | LUMA OOD split (8 classes) | AUC Score | RCML: 0.91 AUC; MCD/DE: ~0.5 AUC | RCML robustness validated | Single-seed point estimate |
| E3 | UQ methods respond to label noise | 0-25% label noise sweep | Aleatoric/Epistemic Uncertainty | RCML consistently raises uncertainty; MCD/DE inconsistent | Dataset differentiates UQ quality | Limited to multimodal late-fusion baselines |

### Research-Theme Gap Diagnosis
The core research value (new benchmark for MUQ) is well-supported, but reproducibility and statistical robustness are weakly supported due to missing variance reporting and ambiguous formula notation. The impact on practice is high, but current baselines are simple; advanced fusion or calibration techniques are not tested.

### Proposed Research Experiments (P0/P1/P2)
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Statistical Reliability | Results are stable across random seeds | Re-run E1/E2/E3 with 3-5 seeds | Same baselines | Mean ± Std, p-values | Std < 5% of mean | Low | Validates robustness claims |
| Advanced UQ Methods | Calibration/fusion improves MCD/DE | Apply temperature scaling or early fusion | MCD/DE baselines | AUC, ECE | AUC > 0.7 for MCD/DE | Medium | Bounds failure claims |
| Cross-Dataset Generalization | LUMA-trained UQ transfers to other datasets | Evaluate on CUB/Scene15 | LUMA baselines | OOD AUC, Accuracy | Consistent performance | Medium | Demonstrates practical utility |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10
The paper presents a valuable and well-motivated benchmark dataset for multimodal uncertainty quantification. The dataset construction is rigorous, and the toolkit addresses a clear community need. However, the score is moderated by the lack of variance reporting, ambiguous mathematical notation in the diversity control formula, and slightly overstated comparative claims regarding baseline failures. These issues are fixable and do not invalidate the core contribution.

**Post-Revision Target:** [7.5, 8.5]/10
If the authors add multi-seed variance reporting, clarify Equation 1, bound the comparative claims, and include key findings in the abstract/conclusion, the paper will meet the standards for a strong acceptance. The research value and reproducibility will be significantly enhanced.