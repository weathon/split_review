## Summary
# Final Review Report

## Summary
This paper investigates neural scaling laws for Time Series Foundation Models (TSFMs), extending prior work that focused primarily on in-distribution (ID) data to out-of-distribution (OOD) scenarios. The authors train encoder-only and decoder-only Transformers across varying parameter counts, compute budgets, and dataset sizes, establishing power-law scaling relationships for both ID and OOD performance. Additionally, the paper conducts case studies on two state-of-the-art TSFMs (Moirai and Chronos) to analyze how architectural enhancements impact scalability. The key findings reveal that OOD scaling follows a parallel power law to ID scaling, and that while architectural modifications often improve ID performance, they can reduce OOD scaling efficiency. The paper concludes with practical design principles for balancing model size, data volume, and compute in TSFM development.

## Strengths
1. **Comprehensive Empirical Scope:** The paper conducts a rigorous and large-scale empirical study, training models across five orders of magnitude in parameter size and evaluating scaling laws across three core factors (parameters, compute, data) for both ID and OOD settings. This systematic approach provides a solid foundation for TSFM scaling analysis.
2. **Valuable OOD Extension:** Extending scaling laws to OOD scenarios addresses a critical gap in the literature. The finding that OOD NLL scaling follows a parallel power law to ID scaling is highly insightful and provides a predictable framework for estimating generalization gains.
3. **Architectural Comparative Analysis:** The inclusion of encoder-only vs. decoder-only Transformers, along with case studies on Moirai and Chronos, offers practical insights into how specific architectural choices (e.g., discrete tokenization, multi-scale patching) impact scaling efficiency and generalization.
4. **Actionable Design Principles:** The derivation of practical guidelines, such as the sublinear data-model scaling relationship ($D \propto N^{0.8}$), provides concrete, evidence-based recommendations for researchers and practitioners designing TSFMs.

## Weaknesses
1. **Lack of Component-Level Ablation for Architectural Claims:** The paper claims that architectural enhancements in Moirai and Chronos "compromise OOD scalability," but it does not isolate which specific modules (e.g., any-variate attention, multi-scale patching, discrete tokenization) are responsible. Without ablation studies, this remains a correlation rather than a causal finding, limiting the actionable value of the architectural analysis.
2. **Overstated Generalization Claims:** Statements such as "increasing model size may enable them to perform equally well on both ID and OOD data" are slightly overstated. The evidence shows that scaling narrows the ID/OOD performance gap (via larger OOD exponents in MAPE), but does not necessarily equalize absolute performance. These claims require tighter bounding to maintain scientific rigor.
3. **Formatting and Typographical Errors:** Several key equations (Eq. 1, Eq. 2, and the data-model scaling relationship in Section 4) suffer from line-break formatting issues that break the mathematical expressions. Additionally, minor typos (e.g., "Appendidx B", "We have also study") reduce professional polish and can confuse readers verifying derivations.
4. **Limited Discussion on Data Filtering Bias:** The pre-training corpus undergoes strict quality filtering (SNR > 20 dB) and domain balancing. While this ensures clean scaling laws, it may bias results toward highly predictable time series, potentially overestimating OOD performance in noisier real-world scenarios. The paper lacks a sensitivity analysis or discussion on how lower SNR thresholds might alter the observed scaling exponents.

## Key Issues
1. **Causal Attribution Gap in Architectural Analysis (Major):** The core claim that architectural enhancements reduce OOD scalability lacks component-level ablation. Readers cannot determine whether multi-scale patching, any-variate attention, or discrete tokenization is the primary driver of this effect. This limits the paper's ability to provide precise architectural guidance.
2. **Equation Formatting and Reproducibility Risks (Minor):** Broken equation formatting in Eq. 1, Eq. 2, and Section 4 obscures the mathematical derivations. While the underlying logic is sound, these artifacts hinder reproducibility and require immediate correction.
3. **Claim Bounding and Objectivity (Minor):** Several claims regarding OOD performance parity and model size superiority are slightly overstated relative to the empirical evidence. Tightening these claims to reflect gap reduction rather than absolute parity will improve scientific defensibility.

## Actionable Suggestions
1. **Add Component-Level Ablations:** For Moirai and Chronos, conduct ablation studies isolating key modules (e.g., remove multi-scale patching or any-variate attention) to identify which components specifically reduce OOD scaling efficiency. If full ablations are too costly, provide a detailed hypothesis-driven discussion on why these modules might overfit to ID distributional specifics.
2. **Fix Equation Formatting and Typos:** Correct the line-break artifacts in Eq. 1, Eq. 2, and the data-model scaling relationship in Section 4. Ensure all mathematical expressions are rendered clearly (e.g., using LaTeX display mode). Fix minor typos such as "Appendidx" and "We have also study."
3. **Bound Generalization Claims:** Revise statements like "perform equally well on both ID and OOD data" to "narrow the ID/OOD performance gap." Explicitly acknowledge that while scaling exponents may converge, absolute performance parity is not guaranteed without further validation.
4. **Discuss Data Filtering Bias:** Add a paragraph in Appendix A or Section 4 discussing how the SNR > 20 dB filtering threshold impacts the generalizability of the scaling laws. Consider providing a small sensitivity analysis with a lower SNR threshold to demonstrate robustness.
5. **Strengthen Abstract Quantitative Hooks:** Include one key quantitative finding in the abstract (e.g., the approximate scaling exponent difference or the parameter threshold where OOD gains emerge) to make the contribution more tangible for readers.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** Scaling laws provide critical insights for designing Time Series Foundation Models (TSFMs), but prior work has largely ignored out-of-distribution (OOD) behavior and architectural impacts.
- **S2 (Significance/Challenge):** Without predictable OOD scaling frameworks, massive resource investments in TSFMs risk inefficiency and poor generalization.
- **S3 (Prior Gap):** Existing studies focus on in-distribution (ID) scaling, leaving the transferability of scaling laws and the role of model architecture underexplored.
- **S4 (Proposed Method):** We examine encoder-only and decoder-only Transformers across varying parameters, compute, and data sizes, establishing power-law scaling for both ID and OOD settings, and analyze case studies of Moirai and Chronos.
- **S5 (Key Result & Implication):** We find that OOD NLL scaling parallels ID scaling, and architectural enhancements often trade OOD scalability for ID gains, leading to actionable design principles for balanced TSFM development.

### Introduction Outline (Complete)
- **P1 (Big Picture & Motivation):** Time series forecasting is shifting from task-specific models to universal TSFMs (e.g., Timer, Moirai), driven by scaling in data and parameters. However, blind scaling lacks a predictable return-on-investment framework.
- **P2 (Research Gap):** While neural scaling laws are established for ID data, their applicability to OOD scenarios remains unknown. Furthermore, the impact of diverse TSFM architectures on scalability is unstudied, raising questions about optimal design choices.
- **P3 (Proposed Solution & Evidence):** We empirically investigate scaling laws across three core factors (parameters, compute, data) for ID and OOD settings. We compare encoder-only and decoder-only Transformers and analyze advanced architectures (Moirai, Chronos) to isolate architectural effects.
- **P4 (Contribution Summary):** (1) Extend scaling laws to OOD, revealing parallel power-law behavior. (2) Benchmark architectural impacts, showing trade-offs between ID performance and OOD scalability. (3) Provide practical design principles for data-model-compute balancing in TSFMs.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Fix equation formatting (Eq. 1, Eq. 2, Sec 4) and typos ("Appendidx", "study") | Improves reproducibility and professional polish; removes reader confusion. | Low |
| **P0** | Bound OOD generalization claims (e.g., "narrow gap" vs "equal performance") | Enhances scientific defensibility and objectivity. | Low |
| **P1** | Add component-level ablation or hypothesis-driven discussion for Moirai/Chronos OOD degradation | Strengthens causal attribution and architectural guidance. | Medium |
| **P1** | Discuss data filtering bias (SNR > 20 dB) and potential impact on scaling laws | Improves transparency and generalizability claims. | Low |
| **P2** | Include quantitative hooks in Abstract (e.g., scaling exponent values) | Makes contributions more tangible and engaging. | Low |

**Revision Order:** Start with P0 items to ensure mathematical clarity and claim accuracy. Proceed to P1 items to deepen the architectural analysis and data discussion. Finally, polish the abstract with P2 quantitative details.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Parameter scaling for encoder-only TSFMs | 1K-100M params, full corpus | NLL, MAPE | Power-law scaling in ID/OOD | C1 | No variance reporting |
| E2 | Compute scaling for encoder-only TSFMs | Varying compute budgets | NLL, MAPE | Power-law scaling, lower bounds | C1 | Noise in training loss |
| E3 | Data scaling for encoder-only TSFMs | 10M-1B time points | NLL, MAPE | Power-law scaling, ID more sensitive | C1 | Fixed model size (1B) |
| E4 | Architecture comparison (Enc vs Dec) | Same training setup | NLL | Similar OOD scalability, Enc better ID | C2 | No component ablation |
| E5 | Case study: Moirai vs Baseline | Encoder-only baseline | NLL | Moirai improves ID, reduces OOD slope | C2 | Causal module unknown |
| E6 | Case study: Chronos vs Baseline | Decoder-only baseline | NLL, SMAPE | Chronos discrete NLL limits scaling | C2 | Metric dependency |

### Research-Theme Gap Diagnosis
The core research value lies in establishing predictable OOD scaling laws and architectural trade-offs. However, the lack of component-level ablations weakens the causal explanation for architectural impacts. Additionally, variance reporting and sensitivity to data filtering thresholds are missing, limiting robustness claims.

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls | Metrics | Success Criterion | Cost | Gain |
|---|---|---|---|---|---|---|---|
| C2 (Architectural impact) | Multi-scale patching reduces OOD scalability | Ablate Moirai modules (patching, attention) | Full Moirai | NLL, MAPE | Isolate module effect | Medium | High causal clarity |
| C1 (OOD scaling robustness) | Scaling laws hold under lower SNR | Train on SNR > 10 dB subset | SNR > 20 dB baseline | NLL exponents | Exponents remain stable | Low | Validates generalizability |
| C1 (Statistical reliability) | Gains are statistically significant | Multi-seed training (≥3 seeds) | Single seed | Mean±std NLL | Overlapping CIs | Medium | Improves rigor |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10

**Rationale:** The paper makes a valuable contribution by extending neural scaling laws to OOD scenarios for TSFMs and providing practical design principles. The empirical scope is comprehensive, and the findings on parallel ID/OOD scaling are insightful. However, the score is moderated by the lack of component-level ablations to causally explain architectural impacts, several equation formatting issues that hinder reproducibility, and slightly overstated generalization claims. With targeted revisions to bound claims, fix formatting, and deepen the architectural analysis, the paper's rigor and impact would significantly improve.

**Post-Revision Target:** [7.5, 8.5]/10