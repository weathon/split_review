## Summary
# Final Review Report

## Summary
This paper introduces FoundTS, a comprehensive and unified benchmark designed for the quantitative evaluation of time series forecasting (TSF) foundation models. Addressing the lack of standardized evaluation protocols in the rapidly growing field of TSF foundation models, FoundTS provides a unified pipeline that standardizes critical experimental settings such as data splitting, normalization, and few-shot sampling. The benchmark covers a diverse range of models, including both LLM-based and time-series pre-trained foundation models, alongside state-of-the-art specific baselines. Extensive experiments are conducted across 14 datasets spanning 10 domains and varying statistical characteristics, under zero-shot, few-shot, and full-shot evaluation strategies. The results reveal that no single foundation model dominates across all settings; pre-trained TS models excel in data-scarce scenarios but often underperform specific models when full training data is available. The paper also highlights that the scaling law does not strictly hold for current TSF foundation models, offering actionable insights for future architectural design and pre-training strategies.

## Strengths
1. **Comprehensive and Timely Benchmark:** The paper addresses a critical gap in the TSF community by providing a unified benchmark for foundation models, which have emerged rapidly but lack standardized evaluation protocols. FoundTS's inclusion of both LLM-based and time-series pre-trained models, alongside specific baselines, makes it a highly valuable resource.
2. **Standardized Evaluation Pipeline:** The standardization of experimental settings (data splitting, normalization, lookback/prediction lengths, and few-shot sampling) directly tackles the reproducibility and comparability issues prevalent in current literature. This methodological rigor significantly enhances the reliability of the reported results.
3. **Diverse Dataset Coverage:** The benchmark covers 14 datasets across 10 domains and evaluates models against 7 statistical characteristics (e.g., seasonality, non-Gaussianity, shifting). This diversity allows for a nuanced analysis of model robustness and generalization capabilities under varying data conditions.
4. **Actionable Insights:** The extensive experiments yield meaningful findings, such as the limited applicability of scaling laws in TSF foundation models, the superior few-shot performance of pre-trained TS models over LLM-based models, and the distinct advantages of specific models in full-shot scenarios. These insights provide clear directions for future research.

## Weaknesses
1. **Limited Statistical Rigor in Results Reporting:** The paper reports mean MSE/MAE across prediction lengths but lacks variance reporting (e.g., mean ± std over multiple random seeds) and statistical significance tests. Given that performance differences between models are often marginal (e.g., within 0.01-0.05 MSE), the absence of variance metrics makes it difficult to assess the reliability and stability of the observed rankings.
2. **Insufficient Analysis of LLM-Based Model Failures:** While the paper notes that many LLM-based models underperform pre-trained TS models and even specific models, the analysis of *why* this occurs is somewhat superficial. The claim that "cross-modal information in texts... renders them less effective" is plausible but not empirically validated. A deeper investigation into representation misalignment or prompt sensitivity would strengthen this conclusion.
3. **Full-Shot Evaluation Scope Limitation:** The full-shot evaluation only includes a subset of foundation models (Timer, UniTS, TTM, GPT4TS, UniTime) due to training time constraints. While a 5-hour training limit is mentioned, this selective inclusion may bias the full-shot comparison. The paper should more explicitly discuss how this constraint affects the generalizability of the full-shot findings.
4. **Generic Contribution Statements:** The contribution statements in the introduction are somewhat generic ("identify pros and cons", "offer insights"). They could be more impactful by explicitly highlighting the specific, counter-intuitive findings (e.g., scaling law violations, architecture trade-offs) that the benchmark reveals.

## Key Issues
1. **Statistical Reliability of Model Rankings:** Without variance reporting or significance tests, the observed performance differences between models (especially in few-shot and full-shot settings) cannot be confidently attributed to architectural superiority rather than random initialization or data split variance. This limits the decisiveness of the benchmark's conclusions.
2. **Causal Attribution in Analysis:** The paper attributes performance gaps to factors like "cross-modal information" or "scaling law violations" without controlled ablations to isolate these variables. For instance, the underperformance of LLM-based models could stem from prompt design, parameter-efficient fine-tuning limitations, or representation misalignment, but the paper does not disentangle these confounders.
3. **Reproducibility of Foundation Model Fine-Tuning:** While the benchmark standardizes data splitting and sampling, the fine-tuning protocols for foundation models (e.g., learning rate schedules, optimizer choices, early stopping patience) are not uniformly detailed across all models. Some models may have been evaluated using suboptimal hyperparameters, potentially skewing the comparison.

## Actionable Suggestions
1. **Add Variance and Significance Reporting:** Report mean ± standard deviation over at least 3 random seeds for all key results (Tables 4-6). Include paired statistical significance tests (e.g., t-test or bootstrap) when comparing the top-performing foundation models against the strongest specific baselines. This will substantially increase the credibility of the rankings.
2. **Deepen LLM-Based Model Analysis:** Conduct a targeted ablation study on LLM-based models to isolate the sources of their underperformance. For example, compare different prompt templates, evaluate the impact of parameter-efficient fine-tuning vs. full fine-tuning, and analyze representation alignment using t-SNE or similarity metrics. This will provide actionable insights for improving LLM adaptation to TSF.
3. **Clarify Full-Shot Training Constraints:** Explicitly document the hyperparameter search space and training budgets for the foundation models included in the full-shot evaluation. If a 5-hour limit was enforced, discuss how this might disadvantage models with slower convergence rates and suggest a follow-up study with extended training budgets.
4. **Refine Contribution Statements:** Rewrite the contribution bullet points to highlight specific, counter-intuitive findings (e.g., "Reveals that scaling laws do not strictly hold for TSF foundation models, with smaller architectures like TTM achieving competitive performance against much larger models"). This will make the paper's impact more immediately apparent to readers.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** Time Series Forecasting (TSF) is critical in finance, weather, and energy management, yet most models struggle to generalize across domains.
- **S2 (Significance/Challenge):** While foundation models pre-trained on large-scale data aim to overcome this, the rapid emergence of diverse architectures has outpaced rigorous, standardized evaluation.
- **S3 (Prior Gap):** Existing benchmarks lack unified pipelines, support limited evaluation strategies (e.g., missing few-shot), and often ignore LLM-based foundation models, hindering fair comparison.
- **S4 (Proposed Method):** We propose FoundTS, a comprehensive benchmark that standardizes evaluation across zero-shot, few-shot, and full-shot strategies, covering both LLM-based and time-series pre-trained models alongside specific baselines.
- **S5 (Key Result & Impact):** Extensive experiments on 14 datasets reveal that no single model dominates; pre-trained TS models excel in data-scarce settings but lag in full-shot scenarios. These findings highlight scaling law limitations and offer actionable directions for future model design.

### Introduction Outline (Complete)
- **P1 (Big Picture & Motivation):** Establish TSF as a core functionality in critical applications. Highlight the limitation of specific models (poor generalization) and introduce foundation models as a promising solution leveraging universal temporal representations.
- **P2 (Research Gap):** Note that while foundation models are emerging, understanding their strengths/limitations is limited. Existing research focuses on qualitative analysis, lacking rigorous quantitative evaluation and standardized protocols.
- **P3 (Problem Specifics):** Detail the inconsistencies in current experimental setups (sampling types, lookback lengths, metrics) using Table 1. Explain how these inconsistencies introduce confounding variables and hinder reproducibility.
- **P4 (Solution & Contributions):** Introduce FoundTS as a unified benchmark addressing these gaps. Explicitly list contributions: (1) Diversified models/datasets, (2) Comprehensive/fair evaluation pipeline, (3) In-depth quantitative insights (e.g., scaling law violations, architecture trade-offs).
- **P5 (Evidence Preview):** Briefly preview key findings (e.g., pre-trained models excel in few-shot but lag in full-shot; no single model dominates) to hook the reader and transition to the method section.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0 (Critical)** | Add variance reporting (mean ± std over ≥3 seeds) and statistical significance tests to Tables 4-6. | Establishes statistical reliability of model rankings and prevents overclaiming marginal gains. | Medium |
| **P0 (Critical)** | Refine contribution statements to highlight specific, counter-intuitive findings (e.g., scaling law violations). | Increases the perceived novelty and impact of the benchmark's insights. | Low |
| **P1 (High)** | Deepen analysis of LLM-based model underperformance with targeted ablations (prompt sensitivity, fine-tuning scope). | Provides actionable insights for improving LLM adaptation to TSF and strengthens causal claims. | High |
| **P1 (High)** | Clarify full-shot training constraints and document hyperparameter search spaces for all evaluated models. | Improves reproducibility and addresses potential biases from selective model inclusion. | Medium |
| **P2 (Medium)** | Improve narrative flow in Abstract and Introduction using the provided outlines. | Enhances readability and ensures clear problem-gap-solution alignment. | Low |
| **P2 (Medium)** | Add a brief discussion on the computational costs (FLOPs, memory) of foundation models vs. specific models. | Provides a more holistic view of practical deployment feasibility. | Low |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Zero-shot generalization of pre-trained TS models | 14 datasets, 6 models | MSE, MAE | No single model dominates; pre-trained models excel on small datasets. | Pre-trained models show promise but haven't surpassed data-intensive training. | Lacks variance reporting; limited to pre-trained models. |
| E2 | Few-shot (5%) comparison across model types | 10 datasets, 17 models | MSE, MAE | Pre-trained TS models generally outperform LLM-based and specific models. | Pre-trained models are superior in data-scarce scenarios. | Training time capped at 5 hours; missing variance. |
| E3 | Full-shot performance comparison | 6 datasets, 12 models | MSE, MAE | Specific models often outperform foundation models when full data is available. | Foundation models have room for improvement in full-shot settings. | Selective inclusion of foundation models due to training time. |
| E4 | Channel independence vs. dependence analysis | 10 datasets, 4 models | MSE | Channel-dependent models (MOIRAI) outperform independent ones on correlated data but lag behind specific models. | MOIRAI's channel modeling has scalability limitations. | Lacks deep architectural analysis of *why* MOIRAI underperforms. |
| E5 | Architecture & scaling law investigation | ETT datasets, 7 models | MSE, Params | Scaling law does not strictly hold; smaller models (TTM, ROSE) are competitive. | Parameter count is not the only path to performance. | Limited to zero-shot ETT results; lacks efficiency metrics (FLOPs). |
| E6 | Pretrain vs. No Pretrain ablation | 2 datasets, 11 models | MSE, MAE | Pre-trained TS models benefit significantly from pre-training; LLM-based models sometimes degrade. | Pre-training knowledge transfer is modality-dependent. | Only 2 datasets used; lacks representation alignment analysis. |

### Research-Theme Gap Diagnosis
The core research value of FoundTS lies in providing a standardized, reproducible benchmark for TSF foundation models. However, the current evidence is weakly supported in terms of statistical reliability (missing variance/significance tests) and causal attribution (superficial analysis of LLM failures and scaling law violations). Additionally, the practical impact on deployment is underexplored due to missing computational cost metrics.

### Proposed Research Experiments (P0/P1/P2)
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost/Time | Expected Gain |
|---|---|---|---|---|---|---|---|
| Statistical Reliability | Performance differences are statistically significant. | Re-run E1-E3 over 3 random seeds. | Same models/datasets. | Mean ± Std MSE/MAE, p-values. | p < 0.05 for top model vs. baseline. | Medium (1-2 weeks) | High credibility boost. |
| LLM Adaptation Failure | Prompt sensitivity and fine-tuning scope drive LLM underperformance. | Ablate prompt templates and PEFT vs. full fine-tuning for GPT4TS/Time-LLM. | Pre-trained TS models. | MSE/MAE, Representation Similarity. | Identify optimal adaptation strategy. | High (2-3 weeks) | Actionable insights for LLM-TSF. |
| Computational Efficiency | Foundation models have higher inference/training costs than specific models. | Measure FLOPs, peak memory, and latency for all models. | Specific baselines. | FLOPs, Memory (GB), Latency (ms). | Quantify efficiency-performance trade-offs. | Low (3-5 days) | Holistic deployment feasibility view. |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10

**Rationale:** The paper presents a timely and highly valuable benchmark (FoundTS) that addresses a critical gap in the TSF foundation model literature. The standardized evaluation pipeline, diverse dataset coverage, and comprehensive model inclusion are significant strengths. The findings provide actionable insights, such as the limited applicability of scaling laws and the distinct advantages of pre-trained models in data-scarce scenarios. However, the score is moderated by the lack of statistical rigor (missing variance reporting and significance tests), which limits the reliability of the model rankings. Additionally, the analysis of LLM-based model failures and full-shot training constraints could be deeper. With the suggested revisions (particularly adding variance reporting and refining the analysis), the paper's impact and credibility would be substantially enhanced.

**Post-Revision Target:** [7.5, 8.5]/10