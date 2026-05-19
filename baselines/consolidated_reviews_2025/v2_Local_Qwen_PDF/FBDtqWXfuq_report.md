## Summary
# Final Review Report

## Summary
This paper introduces Modality-Collaborated Federated Learning (MCFL), a novel setting that enables collaboration among uni-modal clients without requiring multi-modal data or explicit alignment at the client level. To address the challenges of model heterogeneity and modality gaps in MCFL, the authors propose FedCola, a framework leveraging a modality-agnostic transformer enhanced with three key strategies: cross-modal Attention Sharing, Modality Compensation for aggregation alignment, and Temporal Modality Warm-up. Comprehensive experiments on vision and language benchmarks demonstrate that FedCola consistently outperforms adapted baselines (Uni-FedAvg and CreamFL), establishing a robust new baseline for MCFL. The paper provides valuable insights into parameter-sharing mechanisms and aggregation biases in cross-modal federated settings.

## Strengths
1. **Novel and Practical Setting:** The introduction of MCFL addresses a realistic gap in federated learning where clients possess distinct uni-modal data that cannot be easily aligned. This setting is highly relevant for decentralized domains like healthcare and IoT.
2. **Systematic Methodological Exploration:** The paper systematically investigates three critical dimensions of cross-modal collaboration: parameter-sharing granularity, aggregation alignment, and temporal modality arrangement. The empirical ablation studies clearly justify the design choices (e.g., Attention Sharing over FFN Sharing).
3. **Strong Baseline Establishment:** By adapting and rigorously comparing against Uni-FedAvg and CreamFL, the paper provides a solid, reproducible baseline for future research in modality-collaborated federated learning.
4. **Clear Problem Formalization:** The mathematical formulation of the MCFL setting, including the distinction between modality-specific and shared parameters, is precise and facilitates clear understanding of the aggregation constraints.

## Weaknesses
1. **Lack of Statistical Significance and Variance Reporting:** The experimental results report single-point accuracy values without standard deviations or confidence intervals across multiple random seeds. Given that some improvements are marginal (e.g., Modality Warm-up adding ~0.3%), the statistical reliability of these gains is unverified.
2. **Limited Scope of Modalities and Tasks:** The evaluation is restricted to vision (CIFAR-100, OrganAMNIST) and language (AGNEWS, MTSamples) classification tasks. The generalizability of FedCola to other modalities (e.g., audio, video) or more complex downstream tasks (e.g., generation, detection) remains untested.
3. **Insufficient Analysis of Modality Bias Mechanism:** While the paper identifies that Vanilla MAT suffers from modality bias (favoring language due to sample size imbalance), the root cause analysis is somewhat superficial. It is unclear whether the bias stems purely from aggregation weighting, optimization dynamics, or inherent architectural inductive biases of the transformer.
4. **Overclaiming in Abstract and Introduction:** The abstract and introduction use strong phrasing ("substantial advancement," "significantly outperforms") without immediately anchoring these claims to concrete metrics. This reduces the initial impact and scientific defensibility.

## Key Issues
1. **Statistical Reliability of Marginal Gains:** The ablation study (Table 5) shows that Modality Compensation and Modality Warm-up provide relatively small improvements (~0.5% and ~0.3%, respectively). Without variance reporting over multiple seeds, it is impossible to determine if these gains are statistically significant or merely artifacts of random initialization. This threatens the validity of claiming these components as "crucial."
2. **Causal Attribution of Attention Sharing:** The paper attributes the success of Attention Sharing to its "adeptness at harnessing cross-modal knowledge." However, without a matched-capacity control or deeper representation analysis (e.g., feature similarity metrics), it is difficult to rule out that the gain is simply due to the specific parameter count distribution or optimization dynamics rather than a fundamental superiority of attention mechanisms for cross-modal transfer.
3. **Evaluation Metric Disconnect:** The optimization objective minimizes empirical risk (loss), but the evaluation metric is the equal-weighted mean of Top-1 Accuracy. The non-linear relationship between loss and accuracy, especially across different modalities with varying class complexities (e.g., CIFAR-100 vs. AGNEWS), means that minimizing the summed loss does not guarantee balanced accuracy improvements. This disconnect is not explicitly addressed.

## Actionable Suggestions
1. **Add Variance Reporting:** Re-run all main experiments and ablations with at least 3 different random seeds. Report mean ± standard deviation for all accuracy metrics. Perform paired t-tests or report confidence intervals to validate the statistical significance of marginal gains (especially for Modality Compensation and Warm-up).
2. **Deepen Bias Analysis:** Conduct a more detailed analysis of the modality bias in Vanilla MAT. Investigate whether the bias persists when sample sizes are balanced (e.g., subsampling AGNEWS to match CIFAR-100). This will clarify if the bias is driven by data imbalance or inherent architectural properties.
3. **Strengthen Causal Attribution:** To better justify Attention Sharing, consider adding a representation similarity analysis (e.g., CKA or PCA visualization) comparing features from shared attention layers vs. shared FFN layers. This will provide direct evidence of cross-modal knowledge transfer.
4. **Refine Claim Wording:** Replace strong, unquantified claims in the abstract and introduction with bounded, evidence-backed statements. For example, change "significantly outperforms" to "achieves up to 8.58% higher average accuracy on evaluated benchmarks."
5. **Clarify Optimization-Evaluation Alignment:** Explicitly discuss the relationship between the summed loss objective and the equal-weighted accuracy metric. Consider adding a small ablation showing how different weighting schemes in the loss function affect the final balanced accuracy.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** Federated Learning (FL) has predominantly focused on uni-modal scenarios, limiting the system's ability to leverage diverse multi-modal data sources.
- **S2 (Significance/Challenge):** Real-world decentralized applications often involve clients with distinct uni-modal data (e.g., medical images vs. transcriptions) that cannot be easily aligned, yet share high-level semantic knowledge.
- **S3 (Prior Gap):** Existing multi-modal FL frameworks rely on multi-modal clients or public alignment datasets, making them impractical for strictly uni-modal, privacy-sensitive settings.
- **S4 (Proposed Method):** We introduce Modality-Collaborated Federated Learning (MCFL) and propose FedCola, a framework leveraging modality-agnostic transformers enhanced with Attention Sharing, Modality Compensation, and Temporal Modality Warm-up.
- **S5 (Key Result & Implication):** Comprehensive evaluations on vision and language benchmarks demonstrate that FedCola achieves up to 8.58% higher average accuracy than strong baselines, establishing a robust new baseline for uni-modal collaboration.

### Introduction Outline (Complete)
- **P1 (Big Picture & FL Context):** Establish standard FL and its success in uni-modal settings. Introduce the limitation: exclusion of clients with different modalities despite potential semantic overlap.
- **P2 (Prior Work & Gap):** Review FMML works (Xiong et al., Yu et al.). Highlight their reliance on multi-modal clients or public datasets for alignment. Emphasize the practical bottlenecks (data scarcity, privacy risks, alignment complexity).
- **P3 (Motivation for MCFL):** Propose MCFL as a practical alternative. Define the two core principles: uni-modal-only clients and equal-weighted individual modality evaluation. Use the healthcare example to ground the motivation.
- **P4 (Challenges & Method Intuition):** Identify model heterogeneity and modality gap as key challenges. Introduce modality-agnostic transformers as the architectural solution, but note the empirical bias issue (Vanilla MAT failure).
- **P5 (FedCola Framework & Contributions):** Summarize the three research questions (parameter-sharing, aggregation, temporal arrangement). Present FedCola's three strategies. List contributions explicitly, naming the technical mechanisms.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0 (Critical)** | Add variance reporting (mean ± std over ≥3 seeds) for all main results and ablations. | Validates statistical significance of marginal gains; prevents rejection due to reliability concerns. | Medium |
| **P0 (Critical)** | Refine abstract and introduction claims to be bounded and evidence-backed (e.g., add specific accuracy gains). | Improves scientific defensibility and reader trust; aligns claims with actual results. | Low |
| **P1 (High)** | Conduct sample-size balanced ablation to isolate modality bias causes in Vanilla MAT. | Deepens mechanistic understanding; strengthens the motivation for Modality Compensation. | Medium |
| **P1 (High)** | Clarify the relationship between the summed loss objective and the equal-weighted accuracy metric. | Resolves optimization-evaluation disconnect; improves methodological rigor. | Low |
| **P2 (Medium)** | Add representation similarity analysis (e.g., CKA) to support the Attention Sharing claim. | Provides direct evidence of cross-modal knowledge transfer; strengthens causal attribution. | High |
| **P2 (Medium)** | Expand evaluation to one additional modality or task (e.g., audio classification) to demonstrate broader generalizability. | Increases the perceived scope and impact of the MCFL setting. | High |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Vanilla MAT suffers from modality bias. | CIFAR-100 + AGNEWS, Nv=Nl=4, α=0.5. Baseline: Vanilla MAT vs Uni-FedAvg. | Top-1 Acc | Vision acc drops to 3.58%; Language slightly improves. | Modality gap exists. | Single seed; bias mechanism not fully isolated. |
| E2 | Attention Sharing is superior to FFN/All/None sharing. | Same as E1. Strategies: Attention, FFN, Vision-only, Language-only. | Top-1 Acc | Attention Sharing achieves 72.92% Avg Acc. | Cross-modal attention is effective. | Lacks representation-level evidence. |
| E3 | Modality Compensation fixes aggregation misalignment. | Imbalanced client settings (Nv=4, Nl=16). | Top-1 Acc | MC improves Avg Acc by +1.6% in high imbalance. | MC addresses sample imbalance bias. | Gain is marginal in balanced settings. |
| E4 | Modality Warm-up improves initialization. | 3-stage warm-up strategies. | Top-1 Acc | Vision warm-up yields best results; HD stage helps correlated data. | Temporal arrangement matters. | Communication cost trade-off not fully quantified. |
| E5 | FedCola outperforms baselines across scenarios. | 6 FL scenarios (varying N, α, r). Baselines: Uni-FedAvg, CreamFL. | Top-1 Acc | FedCola wins in all Avg Acc and most uni-modal Acc. | FedCola is a robust baseline. | No variance reporting; limited to vision/language. |

### Research-Theme Gap Diagnosis
The core research value lies in demonstrating that uni-modal clients can collaborate effectively without alignment. However, the current evidence is weakly supported in terms of statistical reliability (single-seed results) and mechanistic depth (why attention sharing works, exact source of Vanilla MAT bias). The impact on practice is clear, but reproducibility is hindered by missing variance data.

### Proposed Research Experiments (P0/P1/P2)
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost/Time | Expected Gain |
|---|---|---|---|---|---|---|---|
| Statistical Reliability | Gains are consistent across random initializations. | Re-run E5 with 3 seeds. | Same baselines. | Mean ± Std Acc | Std < 1% of mean gain. | Low (1-2 days) | Validates marginal gains. |
| Bias Mechanism | Vanilla MAT bias is driven by sample size imbalance. | Subsample AGNEWS to match CIFAR-100 size. | Vanilla MAT (balanced vs imbalanced). | Top-1 Acc | Bias reduces significantly when balanced. | Low (1 day) | Isolates bias root cause. |
| Causal Attribution | Shared attention layers transfer cross-modal features. | Compute CKA similarity between modality features. | Attention Sharing vs FFN Sharing. | CKA Score | Higher cross-modal CKA for Attention. | Medium (3 days) | Strengthens mechanism claim. |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10
**Post-Revision Target:** [7.5, 8.5]/10

**Scoring Rationale:**
The paper proposes a highly relevant and practical setting (MCFL) and delivers a well-structured framework (FedCola) with clear empirical gains over strong baselines. The systematic exploration of parameter-sharing, aggregation, and temporal arrangement demonstrates solid methodological rigor. However, the score is moderated by the lack of statistical variance reporting, which undermines confidence in marginal ablation gains, and the somewhat superficial analysis of the modality bias mechanism. The evaluation is also limited to vision and language classification. With the addition of multi-seed variance reporting, deeper bias analysis, and refined claim bounding, the paper would significantly strengthen its scientific defensibility and impact, justifying a higher post-revision score.