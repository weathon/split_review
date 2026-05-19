## Summary
# Final Review Report

## Summary
This paper introduces NARes, a large-scale neural architecture dataset for adversarial robustness (AR) comprising 15,625 unique wide residual network (WRN) architectures. The dataset addresses a critical gap in existing resources by focusing on a macro search space (varying depths and widths) rather than micro cell topologies, and by providing comprehensive metrics including AutoAttack evaluation, stable accuracy, and empirical Lipschitz constants. Through exhaustive adversarial training and evaluation on CIFAR-10, the authors derive several key insights: (1) increasing MACs is more effective for AR than increasing parameters alone, (2) stable accuracy correlates strongly with AR while lower Lipschitz constants are a necessary condition, and (3) previously proposed architectural principles (e.g., reducing last-stage capacity) do not consistently hold under large-scale evaluation. The paper also demonstrates NARes as a benchmark for black-box neural architecture search (NAS). While the dataset represents a significant computational investment and provides valuable empirical grounding for AR research, the manuscript would benefit from tighter scoping of novelty claims, clearer statistical phrasing in the analysis, and more explicit discussion of methodological limitations such as fixed hyperparameters and low validation-test correlation.

## Strengths
1. **Substantial Computational Contribution:** The authors have invested approximately 44 GPU years to adversarially train and evaluate 15,625 unique WRN architectures. This exhaustive coverage of a macro search space is a rare and valuable resource that significantly lowers the barrier to entry for AR research.
2. **Rich Diagnostic Metrics:** Beyond standard adversarial accuracies, the dataset provides fine-grained training statistics, stable accuracy, and empirical Lipschitz constants. These metrics enable deeper mechanistic analysis of how architecture choices influence robustness and training dynamics.
3. **Empirical Refutation of Prior Principles:** The large-scale evaluation provides strong empirical evidence challenging previously proposed architectural principles (e.g., RobustResNet, RobustPrinciple). By revealing high variance in accuracy for fixed depth-width ratios, the paper demonstrates the limitations of sampling-based studies and highlights the necessity of exhaustive evaluation.
4. **Clear Dataset Design and Reproducibility:** The design space is well-defined (6-dimensional vector for depths and widths), and the training protocol is transparent. The release of 62,500 checkpoints and evaluation code fosters reproducibility and enables future fine-tuning or analysis by the community.
5. **NAS Benchmark Application:** The paper effectively demonstrates the utility of NARes as a time-free benchmark for black-box NAS algorithms, showing that advanced search techniques (e.g., BANANAS, RE) can effectively navigate the macro search space.

## Weaknesses
1. **Fixed Hyperparameters Across Varying Capacities:** The dataset uses a fixed set of hyperparameters for all 15,625 models, ranging from 23M to 266M parameters. Larger models often require different learning rates, batch sizes, or training schedules to converge optimally. This limitation may bias the insights toward smaller models and underrepresent the potential of larger architectures, threatening the validity of conclusions regarding capacity benefits.
2. **Low Validation-Test Correlation:** The paper acknowledges a relatively low correlation between validation and test accuracy (Appendix A.3). This is a critical limitation for the proposed NAS benchmark application, as black-box NAS algorithms rely on validation scores as proxies. The weak proxy metric significantly reduces the reliability and utility of the dataset for NAS research.
3. **Ambiguous Statistical Phrasing:** In Section 4.1, the terms "upper bound" and "lower bound" are used to describe accuracy distributions, which is ambiguous and potentially misleading. It is unclear whether these refer to theoretical limits or empirical percentiles. Clearer statistical terminology is needed to accurately convey the observed trends.
4. **Limited Dataset Scope (CIFAR-10 Only):** The entire dataset is built on CIFAR-10. While computationally necessary, this limits the generalizability of the architectural insights to larger, more complex datasets (e.g., ImageNet). The findings may not translate directly to real-world deployment scenarios.
5. **Informal and Overconfident Phrasing:** Several sections contain informal phrasing (e.g., "coarse architectural manual", "migrate the noise") or overconfident claims (e.g., "all of our models are considered applicable to the AR scenario") that reduce scientific rigor and professionalism.

## Key Issues
1. **Fairness of Fixed Hyperparameter Training:** The use of identical hyperparameters for models with a 10x parameter difference is a major methodological concern. Without tuning, larger models may suffer from underfitting or unstable training, artificially depressing their robustness scores. This confounds the analysis of capacity benefits and may lead to incorrect conclusions about the saturation of AR with increased parameters.
2. **Utility of NAS Benchmark Given Low Proxy Correlation:** The paper positions NARes as a NAS benchmark, yet explicitly notes low validation-test accuracy correlation. For NAS algorithms that optimize validation performance, this weak correlation means that architectures found to be "optimal" on the validation set may not generalize to the test set. This fundamentally limits the dataset's value for proxy-based NAS research unless surrogate metrics or multi-fidelity strategies are proposed.
3. **Generalizability Beyond CIFAR-10:** All insights and architectural principles are derived from CIFAR-10. Adversarial robustness behaviors can differ significantly across datasets due to varying complexity and decision boundary structures. The lack of validation on a second dataset (e.g., CIFAR-100 or Tiny ImageNet) leaves the generalizability of the findings unverified.
4. **Statistical Rigor in Trend Analysis:** The analysis in Section 4.1 relies on visual inspection of scatter plots and box plots to claim trends (e.g., MACs vs. AR). The absence of formal statistical tests (e.g., correlation coefficients, regression significance) weakens the empirical claims. Additionally, the ambiguous use of "upper/lower bound" terminology obscures the actual statistical distribution of model performances.

## Actionable Suggestions
1. **Acknowledge and Mitigate Hyperparameter Bias:** Explicitly discuss the limitation of fixed hyperparameters in the main text or limitations section. If computationally feasible, provide a small ablation study showing how a subset of large models performs with tuned hyperparameters. Alternatively, justify the fixed setting by emphasizing dataset comparability and standard practice in NA benchmarks.
2. **Strengthen NAS Benchmark Discussion:** Address the low validation-test correlation more directly. Propose potential solutions for NAS algorithms, such as using multi-fidelity evaluation (e.g., early stopping metrics, surrogate losses) or ensemble-based validation. Clarify that NARes is best suited for algorithms that can leverage the rich diagnostic metrics (e.g., LIP, stable accuracy) rather than relying solely on validation accuracy.
3. **Improve Statistical Phrasing and Rigor:** Replace ambiguous terms like "upper/lower bound" with precise statistical language (e.g., "ceiling/floor of the accuracy distribution"). Add correlation coefficients or regression significance tests to support the claims in Section 4.1. Ensure all claims are bounded to the evaluated search space and dataset.
4. **Refine Tone and Professionalism:** Correct typos (e.g., "demend", "AutoAtack", "migrate") and replace informal phrasing (e.g., "coarse architectural manual") with precise scientific language. Soften overconfident claims (e.g., "all models are applicable") to reflect the wide capacity spectrum.
5. **Expand Generalizability Discussion:** While a full second dataset may be infeasible, discuss how the observed architectural principles might transfer to larger datasets. Cite prior work on cross-dataset robustness transfer to ground the discussion.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** Adversarial robustness is critical for deployment, but architectural design for robustness is hindered by high computational costs.
- **S2 (Significance/Challenge):** Existing neural architecture datasets focus on micro search spaces or small-scale models, leaving a gap in understanding macro architectural impacts on robustness.
- **S3 (Prior Gap):** Prior datasets lack exhaustive coverage of WRN-style macro spaces, high-capacity models, and comprehensive diagnostic metrics (e.g., AutoAttack, Lipschitz constants).
- **S4 (Proposed Method):** We introduce NARes, the first large-scale dataset comprising 15,625 adversarially trained WRN architectures with varying depths and widths, evaluated against multiple attacks and corruptions.
- **S5 (Key Result & Implication):** NARes reveals that MACs budget is more critical than parameters for robustness, refutes prior depth-width ratio principles, and provides a high-resolution resource for future AR and NAS research.

### Introduction Outline (Complete)
- **P1 (Big Picture & Motivation):** Establish the importance of adversarial robustness and the growing recognition that network architecture plays a pivotal role, beyond just training techniques.
- **P2 (Concrete Gap):** Critique existing NA datasets (Jung et al., Wu et al.) for focusing on micro spaces, small capacities, and lacking training metrics/AutoAttack. Explicitly link the micro/macro gap to the dominance of WRNs in AR theory/empirics.
- **P3 (Proposed Solution):** Introduce NARes as a macro-space dataset with 15,625 architectures, high capacity range, and rich diagnostic metrics. Highlight the mitigation of robust overfitting via validation sets.
- **P4 (Evidence Preview):** Summarize key takeaways: MACs > params, stable accuracy/LIP relationships, refutation of prior principles, and collective determination of AR by all depth/width values. Bound claims to the evaluated search space.
- **P5 (NAS Benchmark & Contributions):** Position NARes as a time-free NAS benchmark for macro spaces. List contributions: (1) First large-scale macro NA dataset for AR, (2) New architectural insights, (3) Accessible weights and evaluation code.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Acknowledge fixed hyperparameter limitation and justify dataset comparability. | Addresses major validity concern regarding capacity bias. | Low (text revision) |
| **P0** | Strengthen NAS benchmark discussion by addressing low val-test correlation. | Clarifies dataset utility and proposes mitigation strategies for NAS. | Low-Medium (text revision) |
| **P1** | Replace ambiguous "upper/lower bound" terminology with precise statistical phrasing. | Improves clarity and scientific rigor of trend analysis. | Low (text revision) |
| **P1** | Correct typos ("demend", "AutoAtack", "migrate") and refine informal phrasing. | Enhances professionalism and readability. | Low (text revision) |
| **P2** | Add correlation coefficients or regression significance tests to Section 4.1. | Strengthens empirical claims with formal statistical evidence. | Medium (analysis) |
| **P2** | Discuss generalizability of insights to larger datasets (e.g., CIFAR-100). | Bounds claims and provides context for future work. | Low (text revision) |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Evaluate AR across macro WRN space | 15,625 WRNs, CIFAR-10, AT (PGD) | Clean/Adv Acc, LIP, Stable Acc | MACs > Params for AR; Last-stage capacity reduction not always beneficial | C1, C2 | Fixed hyperparameters may bias large models |
| E2 | Validate prior principles (RobustResNet, RobustPrinciple) | NARes subset, depth-width ratios | PGD20 Acc | High variance for fixed ratios; principles are coarse | C2 | Limited to CIFAR-10 |
| E3 | Analyze stable accuracy & LIP relationships | NARes, PGD20 attack | Stable Acc, LIP, PGD Acc | Stable Acc correlates with AR; Low LIP is necessary condition | C2 | LIP computation details unclear |
| E4 | NAS benchmark evaluation | Random, Local, RE, BANANAS (500 queries) | Val/Test Acc, AA-Compact | Advanced NAS (BANANAS/RE) outperforms classical search | C3 | Low val-test correlation limits proxy utility |

### Research-Theme Gap Diagnosis
The core research value lies in providing a high-resolution empirical landscape for AR architecture design. However, the validity of capacity-related insights is weakened by the fixed-hyperparameter training protocol. Additionally, the NAS benchmark application is undermined by the low validation-test correlation, which is not fully addressed with mitigation strategies.

### Proposed Research Experiments (P0/P1/P2)
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Capacity benefits are not artifacts of fixed hyperparameters | Tuning LR/epochs for large models improves AR beyond current dataset bounds | Retrain top 10% largest models with tuned schedules | Fixed-hyperparameter baselines from NARes | PGD20, AA-Compact Acc | >1% improvement in top models | Medium | Validates capacity insights |
| NAS utility can be improved with surrogate metrics | Multi-fidelity or LIP-based proxies correlate better with test AR | Evaluate NAS using LIP or early-stopping metrics as objectives | Validation-accuracy-based NAS | Test PGD20 Acc, Correlation | Higher test acc or correlation | Low | Strengthens NAS benchmark claim |
| Insights generalize to CIFAR-100 | Architectural trends (MACs > Params, LIP necessity) hold on larger dataset | Train/evaluate a stratified subset (e.g., 500 models) on CIFAR-100 | NARes CIFAR-10 results | PGD20 Acc, LIP | Consistent trends | High | Bounds generalizability claims |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6/10

**Rationale:** The paper presents a substantial computational contribution with NARes, providing a valuable resource for adversarial robustness research. The dataset's scale, macro search space focus, and rich diagnostic metrics are significant strengths. However, the score is moderated by methodological concerns regarding fixed hyperparameters across varying capacities, which may bias capacity-related insights. Additionally, the low validation-test correlation limits the utility of the proposed NAS benchmark, and the manuscript would benefit from tighter statistical phrasing and more explicit discussion of limitations. With revisions addressing these issues, the paper has strong potential.

**Post-Revision Target:** [7, 8]/10

**ASCII Diagram — Paper Structure & Evidence Map**
```text
[Problem: High compute barrier for AR architecture research]
    -> [Gap: Prior datasets focus on micro spaces/small models]
    -> [Solution: NARes (15,625 WRNs, macro space, rich metrics)]
    -> [Evidence: Exhaustive AT evaluation, AutoAttack, LIP, Stable Acc]
    -> [Insights: MACs > Params, Refutation of prior principles, NAS benchmark]
    -> [Limitations: Fixed hyperparameters, Low val-test correlation, CIFAR-10 only]
```

**ASCII Diagram — Revision Strategy Roadmap**
```text
[P0: Acknowledge fixed-hyperparameter bias] -> [Justify comparability / Add ablation]
[P0: Address low val-test correlation] -> [Propose surrogate metrics / Multi-fidelity NAS]
[P1: Refine statistical phrasing] -> [Replace 'bounds' with distribution terms / Add correlations]
[P1: Correct typos & informal tone] -> [Professional polish throughout]
```

**ASCII Diagram — Related-Work Taxonomy Tree (Layered)**
```text
Adversarial Robustness Architecture Research (Root)
├── Branch 1: Manual Design Principles
│   ├── Leaf 1.1: WRN Depth/Width Ratios (RobustResNet, RobustPrinciple)
│   └── Leaf 1.2: Lipschitz Constant Connections (RobustWRN)
├── Branch 2: Automated Design (NAS)
│   ├── Leaf 2.1: Micro Space NAS (NAS-Bench-201 based)
│   └── Leaf 2.2: Macro Space NAS (Limited prior work)
└── Branch 3: Neural Architecture Datasets
    ├── Leaf 3.1: Micro Space Datasets (Jung et al., Wu et al.)
    └── Leaf 3.2: Macro Space Datasets (NARes - This Paper)
```