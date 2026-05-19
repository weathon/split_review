## Summary
# Final Review Report

## Summary
This paper addresses Variable Subset Forecasting (VSF), a challenging scenario where test-time variables are a strict subset of training variables, leading to input dimension mismatch and severe distribution shifts. The authors categorize these shifts into inter-series (changing cross-variable correlations) and intra-series (temporal distribution changes) types. To mitigate these issues, they propose Shift-Resilient Diffusive Imputation (SRDI), which integrates a divide-and-conquer denoising strategy to disentangle invariant and variant patterns for inter-series shift, and a meta-learning framework for rapid temporal adaptation to intra-series shift. Experiments on four real-world datasets demonstrate that SRDI significantly improves forecasting accuracy compared to partial baselines and existing imputation methods. While the problem formulation is practical and the dual-shift analysis is insightful, the manuscript requires clarification on diffusion step notation, meta-learning hyperparameters, and rigorous justification for claims of outperforming Oracle baselines.

## Strengths
1. **Practical Problem Formulation:** The paper addresses Variable Subset Forecasting (VSF), a highly relevant challenge in real-world IoT and sensor networks where test-time variable availability is often incomplete. The formalization of VSF as an imputation-then-forecast pipeline with input dimension mismatch is clear and well-motivated.
2. **Insightful Shift Categorization:** The distinction between inter-series shift (dynamic cross-variable correlations) and intra-series shift (temporal distribution changes) provides a structured framework for analyzing distribution shifts in VSF. This categorization directly informs the methodological design.
3. **Innovative Methodological Integration:** The combination of a divide-and-conquer denoising strategy (disentangling invariant/variant patterns) with a meta-learning adaptation framework is a creative approach to simultaneously addressing spatial and temporal shifts. The invariant-variant dispatcher with correlation disparity regularization is a novel contribution to diffusion-based imputation.
4. **Comprehensive Empirical Validation:** The paper evaluates SRDI across four diverse real-world datasets (traffic, solar, ECG) and multiple forecasting backbones, demonstrating consistent improvements over partial baselines and competitive performance against state-of-the-art imputation methods.

## Weaknesses
1. **Notational Ambiguity in Diffusion Process:** Section 4.1 defines an $R$-step diffusion process but later states that inference uses $R=1$ (single-step). This creates a notational conflict between the multi-step equations and the single-step inference description, obscuring the actual denoising mechanism and computational complexity.
2. **Unjustified Oracle Superiority Claim:** The paper claims SRDI "outperforms the oracle" in most datasets. Outperforming a baseline with full variable access is highly unusual and raises concerns about potential data leakage, inconsistent evaluation protocols, or suboptimal Oracle tuning. This claim lacks rigorous justification or ablation analysis.
3. **Missing Meta-Learning Hyperparameters:** The meta-training and adaptation stages are critical to the method but lack key hyperparameters. The number of inner-loop gradient steps, adaptation iterations, and the proportion of pseudo-missing variables are not specified in the main text or appendix, hindering reproducibility.
4. **Generic Related Work Organization:** The Related Work section lists methods chronologically rather than organizing them by comparison axes. It fails to explicitly contrast SRDI with the strongest baselines (e.g., CSDI, PRISTI, FDW) in terms of their specific inability to handle VSF shifts, weakening the novelty positioning.
5. **Insufficient Ablation Rigor:** The ablation studies report performance degradation for removed modules but do not explicitly state whether training budgets (epochs/steps) are matched across variants. Additionally, standard deviations are missing from ablation tables, making it difficult to assess statistical reliability.

## Key Issues
1. **Validity Risk: Oracle Comparison Protocol (Critical)**
   - **Problem:** Claiming SRDI outperforms the Oracle baseline without explicit justification suggests potential unfair comparison or data leakage.
   - **Impact:** Undermines credibility of the core performance claims.
   - **Fix:** Verify that Oracle and SRDI use identical forecasting backbones, hyperparameters, and evaluation splits. Provide an ablation analyzing the "denoising effect" of diffusion that might explain marginal Oracle improvements. Bound the claim to specific datasets where the gain is statistically significant.

2. **Reproducibility Risk: Missing Meta-Learning Hyperparameters (Major)**
   - **Problem:** The number of inner-loop steps, adaptation iterations, and pseudo-missing variable ratios are not reported.
   - **Impact:** Prevents exact reproduction of the adaptation stage and assessment of inference latency.
   - **Fix:** Add a dedicated hyperparameter table in Appendix A.6 listing `meta_inner_steps`, `adaptation_iterations`, and `pseudo_missing_ratio`. Clarify that `num steps: 1` refers to diffusion inference steps.

3. **Clarity Risk: Diffusion Step Notation Conflict (Major)**
   - **Problem:** Equations define an $R$-step process, but text implies $R=1$ at inference.
   - **Impact:** Confuses readers about whether the model uses multi-step refinement or single-step prediction.
   - **Fix:** Explicitly state that the model adopts a single-step diffusion process for efficiency ($R=1$). Align notation $X_{N/S}^1$ and $X_{N/S}^R$ throughout Section 4.1.

4. **Methodological Risk: Unmatched Ablation Budgets (Major)**
   - **Problem:** Ablation variants may have different training complexities, confounding the attribution of performance gains to specific modules.
   - **Impact:** Weakens causal claims about the necessity of invariant-variant disentanglement and meta-learning.
   - **Fix:** Explicitly state that all ablation variants are trained with identical computational budgets (epochs/steps). Report mean±std across multiple seeds in Appendix Table 3.

## Actionable Suggestions
1. **Clarify Diffusion Inference Steps:** In Section 4.1, explicitly state that the model uses a single-step diffusion process ($R=1$) for inference efficiency. Replace ambiguous notation $X_{N/S}^R$ with $X_{N/S}^1$ in the inference description to align with the equations.
2. **Justify Oracle Comparisons:** Add a paragraph in Section 6.2 discussing why SRDI occasionally outperforms the Oracle. Verify that the Oracle baseline uses the same forecasting backbone and hyperparameters. If the gain is due to a denoising effect, explicitly state this and provide an ablation comparing raw Oracle inputs vs. diffusion-refined inputs.
3. **Report Meta-Learning Hyperparameters:** In Appendix A.6, add entries for `meta_inner_steps` (e.g., 1), `adaptation_iterations` (e.g., 5), and `pseudo_missing_ratio` (e.g., 20%). Clarify that these settings balance adaptation accuracy with inference latency.
4. **Match Ablation Budgets:** In Section 6.3 and Appendix D, explicitly state that all ablation variants (SRDI-TS, SRDI-IV, SRDI-M, etc.) are trained for identical epochs and computational budgets. Add standard deviations to Appendix Table 3 to demonstrate statistical reliability.
5. **Reorganize Related Work:** Restructure Section 2 into thematic categories: (1) Traditional Imputation Methods, (2) Diffusion-Based Imputation, (3) Variable Subset Forecasting. For each category, summarize representative methods, state their limitations regarding distribution shift, and explicitly differentiate SRDI.
6. **Bound Novelty Claims:** In the Introduction and Abstract, replace "marking the first known application" with "to our knowledge, one of the first diffusion-based approaches tailored for VSF." This bounds the claim and reduces reviewer pushback if comparable prior work exists.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Context):** Variable Subset Forecasting (VSF) addresses the challenge of predicting time series when test-time variables are a strict subset of training variables, a scenario prone to severe distribution shifts.
- **S2 (Core Challenge):** We categorize these shifts into inter-series (changing cross-variable correlations) and intra-series (temporal distribution changes) types, which degrade standard imputation-then-forecast pipelines.
- **S3 (Proposed Method):** To mitigate this, we propose Shift-Resilient Diffusive Imputation (SRDI), which integrates a divide-and-conquer denoising strategy to disentangle invariant and variant patterns, coupled with a meta-learning framework for rapid temporal adaptation.
- **S4 (Key Result):** Extensive experiments on four real-world datasets demonstrate that SRDI reduces MAE by up to 37.79% compared to partial baselines and consistently outperforms existing imputation methods under identical VSF settings.
- **S5 (Bounded Implication):** These results highlight the effectiveness of explicitly modeling distribution shifts for robust variable subset forecasting, with code available for reproducibility.

### Introduction Outline (Complete)
- **P1 (Motivation & VSF Definition):** Introduce sensor failures in IoT leading to missing variables. Define VSF as forecasting with $S \ll N$ variables. Explicitly state the input dimension mismatch bottleneck that necessitates imputation or adaptation.
- **P2 (Gap & Shift Analysis):** Identify two types of distribution shift in VSF: inter-series (dynamic correlations) and intra-series (temporal changes). Explain why prior imputation methods fail (static assumptions, lack of adaptation).
- **P3 (Solution Overview - Inter-Series):** Introduce the divide-and-conquer denoising strategy. Explain how disentangling invariant (stable correlations) and variant (dynamic correlations) patterns mitigates inter-series shift.
- **P4 (Solution Overview - Intra-Series):** Introduce the meta-learning strategy. Explain how treating time windows as tasks enables rapid adaptation to intra-series distribution changes.
- **P5 (Contributions):** List 3 concise contributions: (1) Diffusion-based imputation tailored for VSF, (2) Formal categorization of VSF shifts, (3) Divide-and-conquer denoising + meta-learning framework. Remove generic experimental validation bullet.

## Priority Revision Plan
| Priority | Issue | Action | Expected Impact |
|---|---|---|---|
| **P0** | Oracle Superiority Claim | Verify evaluation protocol; add ablation analyzing denoising effect; bound claim to specific datasets. | Resolves critical validity concern; prevents rejection due to suspected leakage/unfair comparison. |
| **P0** | Missing Meta-Learning Hyperparameters | Add `meta_inner_steps`, `adaptation_iterations`, `pseudo_missing_ratio` to Appendix A.6. | Ensures full reproducibility of adaptation stage. |
| **P1** | Diffusion Step Notation Conflict | Explicitly state $R=1$ for inference; align $X_{N/S}^1$ and $X_{N/S}^R$ notation in Sec 4.1. | Improves methodological clarity and reduces reader confusion. |
| **P1** | Unmatched Ablation Budgets | State identical training budgets for all variants; add std devs to Appendix Table 3. | Strengthens causal claims about module necessity. |
| **P2** | Related Work Organization | Reorganize into thematic categories; explicitly contrast SRDI with CSDI/PRISTI/FDW. | Improves novelty positioning and literature coverage. |
| **P2** | Abstract/Intro Claim Bounding | Replace "first known application" with "to our knowledge, one of the first..."; add concrete metric deltas. | Increases scientific defensibility and impact. |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | SRDI vs Partial/Oracle | 4 datasets, 4 backbones | MAE, RMSE | SRDI improves MAE by 12-37% vs Partial; occasionally beats Oracle | Imputation effectiveness | Oracle superiority lacks justification |
| E2 | SRDI vs SOTA Imputation | ECG5000, METR-LA, MTGNN | MAE, RMSE | SRDI outperforms CSDI, PRISTI, FDW, etc. | Competitive imputation quality | Limited to 2 datasets in main text |
| E3 | Ablation: Spatiotemporal | ECG5000, remove TS/T/S modules | MAE, RMSE | Full model best; removing modules degrades performance | Necessity of TSR module | Budget matching not explicit |
| E4 | Ablation: Invariant-Variant | ECG5000, remove dispatcher/variant | MAE, RMSE | SRDI-IV and SRDI-V underperform | Effectiveness of disentanglement | Variance reporting missing |
| E5 | Ablation: Meta-Learning | ECG5000, remove meta/adaptation | MAE, RMSE | SRDI-M underperforms | Necessity of adaptation | Inference latency not analyzed |
| E6 | Dispatcher Visualization | ECG5000, METR-LA, etc. | Correlation diff | Variant pattern shows higher fluctuations | Dispatcher distinguishes patterns | Qualitative only |

### Research-Theme Gap Diagnosis
The core research value (robust VSF under distribution shift) is well-supported by E1-E2. However, the causal attribution of gains to specific modules (E3-E5) is weakened by missing budget matching and variance reporting. The practical deployment feasibility is not assessed due to missing inference latency analysis for the meta-adaptation stage.

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Oracle Superiority | SRDI denoising effect explains Oracle gains | Compare Oracle raw inputs vs. diffusion-refined inputs | Oracle baseline | MAE, RMSE | Gain statistically significant | Low | Validates denoising hypothesis |
| Adaptation Latency | Meta-adaptation adds manageable inference overhead | Measure inference time for SRDI vs. baselines | CSDI, PRISTI | Latency (ms) | <2x baseline latency | Low | Assesses deployment feasibility |
| Cross-Dataset Robustness | SRDI generalizes to unseen domains | Train on METR-LA, test on TRAFFIC | FDW, GINAR | MAE, RMSE | <20% performance drop | Medium | Demonstrates generalization |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10

**Rationale:** The paper addresses a practical and well-motivated problem (Variable Subset Forecasting) and proposes a creative solution combining divide-and-conquer diffusion with meta-learning. The dual-shift analysis (inter-series and intra-series) is insightful and directly informs the methodological design. However, the score is reduced due to critical validity concerns regarding the Oracle comparison protocol, missing meta-learning hyperparameters that hinder reproducibility, and notational ambiguities in the diffusion process. With rigorous justification of Oracle gains, explicit reporting of adaptation hyperparameters, and matched ablation budgets, the paper would significantly strengthen its scientific defensibility.

**Post-Revision Target:** [7.5, 8.5]/10

**Expected Gains after Revision:**
- Resolving the Oracle comparison concern will eliminate the primary validity risk.
- Adding meta-learning hyperparameters and ablation variance will ensure full reproducibility and statistical reliability.
- Clarifying diffusion notation and bounding novelty claims will improve clarity and objectivity.
- These fixes will elevate the paper from a promising but flawed submission to a robust, publication-ready contribution.