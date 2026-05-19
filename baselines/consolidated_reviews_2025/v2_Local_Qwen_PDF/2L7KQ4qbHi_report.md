## Summary
# Final Review Report

## Summary
This paper introduces "concept forgetting," a framework for making pre-trained classification models independent of specific undesired concepts (e.g., sensitive attributes or spurious correlations). The authors propose Label ANnealing (LAN), an iterative algorithm that redistributes pseudo-labels based on model confidence to enforce concept neutrality while minimizing empirical risk change. The method is evaluated on MNIST, CIFAR-10, miniImageNet, and CelebA, demonstrating significant reductions in a proposed "concept violation" metric with minimal accuracy loss compared to fairness baselines. The paper also provides a theoretical bound on loss degradation and ablation studies on learning rates and iterations.

## Strengths
1. **Clear Problem Formulation:** The paper clearly distinguishes concept forgetting from machine unlearning, providing a well-motivated framework for decoupling specific attributes from model predictions.
2. **Efficient Algorithm Design:** LAN is computationally efficient, requiring minimal epochs (often just one) to achieve significant concept violation reduction, making it practical for dynamic environments.
3. **Comprehensive Empirical Evaluation:** The method is evaluated across multiple datasets (MNIST, CIFAR-10, miniImageNet, CelebA) and architectures, with strong trade-off plots demonstrating superiority over fairness baselines.
4. **Theoretical Grounding:** The inclusion of a theoretical bound on loss degradation (Theorem 1) provides valuable insight into the relationship between initial concept violation and performance retention.

## Weaknesses
1. **Missing Variance Reporting:** The results section reports point estimates without variance or standard deviation across multiple random seeds, making it impossible to assess statistical reliability.
2. **Unclear Hyperparameter Tuning Protocol:** The comparison with baselines lacks explicit details on computational budgets and hyperparameter search spaces, raising concerns about fair comparison.
3. **Verbose and Distracting Contributions:** The contribution list includes unnecessary analogies (material science "annealing") and excessive numerical results, cluttering the introduction and obscuring core technical novelty.
4. **Loose Theoretical Bound:** The theoretical bound on loss degradation scales linearly with iterations $E$, contradicting empirical observations that performance improves with $E$. This discrepancy is not explained.
5. **Limited Discussion of Failure Modes:** The conclusion lacks specific limitations, such as performance degradation when the target concept is intrinsically correlated with the prediction label.

## Key Issues
1. **Statistical Reliability:** The absence of variance reporting (mean ± std over ≥3 seeds) for all key metrics undermines confidence in the reported gains. This is a critical reproducibility gap.
2. **Fair Comparison Protocol:** Without explicit details on hyperparameter tuning budgets for baselines vs. LAN, the trade-off superiority claims may be biased. Baselines like FERMI often require extensive tuning.
3. **Theoretical-Empirical Mismatch:** The linear degradation of the theoretical bound with iterations $E$ contradicts empirical improvements. This looseness needs acknowledgment to maintain theoretical credibility.
4. **Concept-Label Intrinsic Correlation:** The method's behavior when the forgetting concept is causally linked to the target label is not discussed. In such cases, concept forgetting may fundamentally degrade accuracy, representing a hard limitation.

## Actionable Suggestions
1. **Add Variance Reporting:** Report mean ± standard deviation over at least three random seeds for all concept violation and accuracy metrics in Tables 1 and 2.
2. **Clarify Tuning Protocol:** Explicitly state the hyperparameter search space and computational budget for both LAN and baselines. Provide a fixed-hyperparameter comparison if baselines were tuned more extensively.
3. **Condense Contributions:** Remove the material science analogy and detailed percentage lists from the contribution bullets. Focus on framework, algorithm mechanism, and empirical trade-offs.
4. **Explain Theoretical-Empirical Gap:** Add a brief discussion acknowledging that the theoretical bound assumes worst-case label changes, whereas empirical pseudo-labels stabilize quickly, allowing performance improvement with $E$.
5. **Discuss Intrinsic Correlations:** In the conclusion, explicitly state that LAN may struggle when the target concept is causally linked to the prediction label, and suggest future work on handling such cases.

## Storyline Options + Writing Outlines
### Abstract Outline
- **S1 (Context):** Deep learning models often inadvertently learn biased or noisy concepts from training data, undermining fairness and generalization.
- **S2 (Gap):** Existing approaches like machine unlearning remove data influence rather than concepts, while fairness methods often require computationally expensive retraining.
- **S3 (Solution):** We propose Label ANnealing (LAN), an iterative algorithm that redistributes pseudo-labels to decouple target concepts from model predictions efficiently.
- **S4 (Evidence):** LAN reduces concept violation by up to 85% across multiple datasets while maintaining high accuracy, outperforming fairness baselines in the accuracy-violation trade-off.

### Introduction Outline
- **P1 (Motivation):** DL models learn diverse concepts, but some are undesired (sensitive attributes, spurious correlations). Need to selectively forget these without degrading utility.
- **P2 (Gap & Distinction):** Machine unlearning removes specific data points, not pervasive features. Concept forgetting targets feature-level decoupling.
- **P3 (Solution Preview):** LAN iteratively redistributes pseudo-labels based on model confidence, enforcing concept neutrality with minimal empirical risk change.
- **P4 (Contributions):** (1) Framework & metric, (2) LAN algorithm, (3) Empirical validation of superior trade-offs.

## Priority Revision Plan
| Priority | Action | Expected Impact |
|---|---|---|
| P0 | Add variance reporting (mean ± std over ≥3 seeds) for all key metrics. | Establishes statistical reliability and reproducibility. |
| P0 | Clarify hyperparameter tuning protocol for baselines vs. LAN. | Ensures fair comparison and validates trade-off superiority claims. |
| P1 | Condense contributions and remove material science analogy. | Improves readability and focuses on technical novelty. |
| P1 | Explain theoretical-empirical mismatch regarding iterations $E$. | Strengthens theoretical credibility and clarifies bound looseness. |
| P2 | Discuss intrinsic concept-label correlations in conclusion. | Honestly bounds method applicability and guides future work. |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Binary concept forgetting efficacy | MNIST, CIFAR-10, CelebA, miniImageNet | $\hat{V}_C$, $A_D$ | Significant violation reduction with minimal accuracy loss | C3 | No variance reported |
| E2 | Multi-level concept forgetting | CelebA (Hair Color, Facial Hair) | $\hat{V}_C$, $A_D$ | ~63.52% violation reduction | C3 | Limited to one dataset |
| E3 | Baseline comparison | FERMI, Continuous-Fairness, Fairness-KDE | Trade-off plots | LAN achieves better trade-off | C3 | Tuning budget unclear |
| E4 | Learning rate ablation | Multiple datasets | $\hat{V}_C$, $A_D$ | Non-monotonic behavior observed | Mechanism insight | Selection guideline missing |

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Estimated Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Statistical Reliability | Results are stable across seeds. | Run LAN 3-5 times with different seeds. | Same baselines. | Mean ± std $\hat{V}_C$, $A_D$ | Low variance | Low | Validates reproducibility |
| Fair Comparison | LAN superiority holds under fixed budgets. | Fix hyperparameters for all methods. | FERMI, etc. | Trade-off plots | LAN still dominates | Medium | Ensures unbiased comparison |
| Intrinsic Correlation | LAN degrades when concept is causal to label. | Create synthetic dataset with strong correlation. | Random baseline. | Accuracy drop | Quantify limitation | Low | Bounds method applicability |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6/10
The paper presents a well-motivated framework and an efficient algorithm for concept forgetting, with strong empirical trade-offs. However, the lack of variance reporting, unclear hyperparameter tuning protocols, and verbose presentation detract from the overall rigor and readability. Addressing these issues would significantly strengthen the contribution.

**Post-Revision Target:** [7, 8]/10
With proper variance reporting, fair comparison details, and streamlined writing, the paper would meet the standards for publication with high confidence.