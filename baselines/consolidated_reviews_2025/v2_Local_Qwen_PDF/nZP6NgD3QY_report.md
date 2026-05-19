## Summary
# Final Review Report

## Summary
This paper addresses the challenge of data-free multi-task learning (MTL) via model merging, specifically focusing on the sensitivity of task arithmetic methods to fixed merging coefficients. The authors propose **AdaMerging**, an unsupervised framework that adaptively learns task-wise or layer-wise merging coefficients by minimizing prediction entropy on unlabeled test samples. The core intuition is that entropy minimization serves as an effective surrogate for cross-entropy loss, implicitly aligning conflicting task vectors toward consensus regions in the weight space. Evaluated on eight image classification datasets using ViT-B/32 and ViT-L/14, AdaMerging demonstrates substantial improvements in average accuracy (up to 11% over Task Arithmetic), generalization to unseen tasks, and robustness under common image corruptions. The paper provides clear empirical validation and insightful analysis of the learned coefficient patterns across network layers. However, the novelty of applying entropy minimization to coefficient optimization is incremental, and the empirical section would benefit from multi-seed variance reporting and explicit coefficient constraints to ensure stability.

## Strengths
1. **Clear and Compelling Motivation:** The paper effectively identifies the fixed global merging coefficient as a primary bottleneck in task arithmetic, providing a strong rationale for adaptive, task-wise, and layer-wise coefficient learning.
2. **Effective Unsupervised Optimization:** Leveraging entropy minimization on unlabeled test data as a surrogate objective is a practical and elegant solution that aligns with the data-free merging paradigm, avoiding the need for original training data or expensive grid search.
3. **Strong Empirical Performance:** AdaMerging demonstrates substantial and consistent improvements over strong baselines (Task Arithmetic, Ties-Merging) across multiple model architectures (ViT-B/32, ViT-L/14) and evaluation dimensions (accuracy, generalization, robustness).
4. **Insightful Coefficient Analysis:** The observation that shallow layers learn smaller coefficients while deeper layers learn larger ones provides valuable mechanistic insight into how entropy minimization balances general feature preservation with task-specific adaptation.

## Weaknesses
1. **Incremental Novelty of Entropy Minimization:** Applying entropy minimization to optimize merging coefficients is a straightforward adaptation of test-time adaptation (TTA) techniques. The core mechanism lacks theoretical grounding beyond empirical correlation with prediction loss, making the contribution feel more like an engineering heuristic than a fundamental methodological advance.
2. **Missing Statistical Rigor:** The experimental results report only single-run accuracy values. Without variance reporting (mean ± std over multiple seeds) or statistical significance tests, it is difficult to assess the stability of the observed gains, particularly for tasks with smaller margins.
3. **Lack of Coefficient Constraints:** The optimization formulation does not explicitly constrain the merging coefficients $\lambda$. During gradient-based entropy minimization, coefficients could grow arbitrarily large, potentially over-amplifying task vectors and destabilizing the pre-trained representation. The absence of bounds or regularization raises reproducibility and stability concerns.
4. **Overstated Generalization Claims:** The paper claims "superior generalization capabilities" based on two held-out tasks per split. This evaluation protocol is limited and does not constitute rigorous out-of-distribution (OOD) generalization testing. The claims should be bounded to the specific evaluated settings.

## Key Issues
1. **Coefficient Stability and Optimization Dynamics:** Without explicit constraints (e.g., $\lambda \in [0, 1]$ or $L_2$ regularization), the entropy minimization objective may drive coefficients to extreme values. This risks over-amplifying task-specific features and degrading the pre-trained model's general representation. The manuscript should clarify how coefficient growth is controlled during optimization.
2. **Empirical Reproducibility and Statistical Validity:** Reporting single-run results limits the ability to verify the stability of AdaMerging. Multi-seed variance reporting is essential to confirm that the 11% improvement on ViT-B/32 is not an artifact of specific initialization or data sampling.
3. **Theoretical Justification for Entropy Proxy:** The paper relies on empirical correlation (Spearman coefficient) to justify entropy minimization as a surrogate for cross-entropy loss. A more rigorous theoretical analysis or ablation study comparing entropy against other unsupervised proxies (e.g., confidence maximization, margin maximization) would strengthen the methodological foundation.

## Actionable Suggestions
1. **Add Coefficient Constraints:** Explicitly bound the merging coefficients during optimization (e.g., $\lambda \in [0, 1]$ via sigmoid parameterization or projection) and report the final coefficient distributions. This will ensure stability and prevent feature over-amplification.
2. **Report Multi-Seed Variance:** Re-run key experiments (Tables 1-3) over at least three random seeds and report mean $\pm$ standard deviation. This will substantiate the statistical reliability of the claimed improvements.
3. **Strengthen Theoretical Justification:** Include a brief ablation comparing entropy minimization against alternative unsupervised proxies (e.g., prediction confidence, margin maximization) to demonstrate why entropy is the most effective surrogate for task vector alignment.
4. **Refine Generalization Claims:** Bound the generalization claims to the specific evaluated settings and consider adding one additional OOD benchmark (e.g., domain-shifted image datasets) to provide stronger evidence of transferability.
5. **Tighten Narrative Flow:** Consolidate the contribution list into three focused points (bottleneck identification, AdaMerging framework, empirical validation) and remove promotional phrasing ("remarkable", "significantly enhanced") to improve scientific objectivity.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** Multi-task learning (MTL) via model merging enables data-free knowledge transfer, but naive task arithmetic suffers from severe performance degradation due to task conflicts.
- **S2 (Significance/Challenge):** The fixed global merging coefficient in existing methods fails to account for varying task importance and layer-wise feature heterogeneity, creating a substantial gap with traditional MTL.
- **S3 (Prior Gap):** Grid search for optimal coefficients is computationally infeasible for task-wise or layer-wise adaptation, and no automated, data-free optimization strategy currently exists.
- **S4 (Proposed Method):** We propose AdaMerging, an unsupervised framework that adaptively learns task-wise or layer-wise merging coefficients by minimizing prediction entropy on unlabeled test samples.
- **S5 (Key Result & Bounded Implication):** Evaluated on eight image classification tasks, AdaMerging improves average accuracy by up to 11% over SOTA baselines, demonstrating enhanced generalization and robustness under distribution shifts.

### Introduction Outline (Complete)
- **P1 (Big Picture & Motivation):** Establish MTL's value and the shift toward data-free model merging in the foundation model era due to data privacy and computational constraints.
- **P2 (Gap Identification):** Introduce task arithmetic and highlight the critical bottleneck: fixed global coefficients cause severe performance sensitivity and task interference.
- **P3 (Problem Formalization):** Quantify the search space complexity (K×L coefficients) to justify why grid search fails and motivate the need for automated gradient-based optimization.
- **P4 (Method Intuition):** Explain how entropy minimization implicitly aligns conflicting task vectors toward consensus regions, reducing interference without requiring labels.
- **P5 (Evidence Preview):** Preview the strong empirical gains in accuracy, generalization, and robustness, along with the insightful shallow/deep layer coefficient patterns.
- **P6 (Contribution Summary):** Consolidate into three focused contributions: bottleneck identification, AdaMerging framework, and comprehensive empirical validation.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Add coefficient constraints ($\lambda \in [0, 1]$) and report final distributions. | Ensures optimization stability and prevents feature over-amplification. | Low |
| **P0** | Report mean ± std over ≥3 seeds for Tables 1-3. | Substantiates statistical reliability of claimed improvements. | Medium |
| **P1** | Consolidate contributions into 3 focused points; remove hype phrasing. | Sharpens scientific impact and improves objectivity. | Low |
| **P1** | Link shallow/deep layer coefficient patterns to entropy minimization mechanism. | Elevates analysis from descriptive to mechanistic insight. | Low |
| **P2** | Add ablation comparing entropy against other unsupervised proxies. | Strengthens theoretical justification for surrogate objective. | Medium |
| **P2** | Bound generalization claims and consider one additional OOD benchmark. | Improves defensibility of transferability statements. | High |

**Traceability:** P0 items directly address coefficient stability and reproducibility risks identified in Key Issues. P1 items improve narrative coherence and analytical depth. P2 items provide optional but valuable theoretical and empirical strengthening.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | AdaMerging improves MTL accuracy over baselines. | ViT-B/32, ViT-L/14 on 8 tasks. | Avg Acc | +11% over Task Arithmetic. | Performance gain | Single-run results. |
| E2 | AdaMerging generalizes to unseen tasks. | 6 seen / 2 unseen splits. | Avg Acc on unseen | +4.4% to +9.1% gains. | Generalization | Limited held-out tasks. |
| E3 | AdaMerging is robust to distribution shifts. | 7 corruption types (Hendrycks). | Avg Acc under corruption | +5.8% to +11.2% gains. | Robustness | Only 4 tasks evaluated. |
| E4 | Entropy correlates with prediction loss. | 8 tasks, Spearman correlation. | Correlation coeff | High positive correlation (0.87). | Proxy validity | Empirical only. |
| E5 | Layer-wise coefficients vary by depth. | ViT-B/32, coefficient visualization. | Coefficient values | Shallow < Deep layers. | Mechanistic insight | Descriptive analysis. |

### Research-Theme Gap Diagnosis
The core research value (adaptive coefficient learning) is well-supported, but statistical reliability (multi-seed variance) and optimization stability (coefficient constraints) are weakly addressed. The generalization claim relies on a limited evaluation protocol.

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Statistical Reliability | Gains are stable across seeds. | Re-run E1 over 3 seeds. | Task Arithmetic, Ties-Merging | Mean ± Std | Std < 1% | Low | Validates robustness. |
| Optimization Stability | Bounded $\lambda$ prevents degradation. | Add sigmoid constraint to $\lambda$. | Unconstrained AdaMerging | Avg Acc, Coeff dist | Stable acc, $\lambda \in [0,1]$ | Low | Ensures reproducibility. |
| Proxy Comparison | Entropy is superior to other proxies. | Compare entropy vs confidence/margin. | Confidence max, Margin max | Avg Acc | Entropy wins | Medium | Strengthens justification. |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6/10

**Rationale:** The paper presents a practical and effective solution to a well-identified bottleneck in task arithmetic (coefficient sensitivity). The empirical results are strong, demonstrating substantial gains in accuracy, generalization, and robustness. However, the novelty of applying entropy minimization to coefficient optimization is incremental, and the lack of multi-seed variance reporting and explicit coefficient constraints limits statistical rigor and reproducibility. With the suggested revisions (P0 items), the paper would significantly improve in defensibility and scientific impact.

**Post-Revision Target:** [7, 8]/10