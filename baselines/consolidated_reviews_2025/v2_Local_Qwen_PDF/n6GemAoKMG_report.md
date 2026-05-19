## Summary
# Final Review Report

## Summary

This paper proposes Evolutionary Attack (EvA), a black-box adversarial attack framework for Graph Neural Networks (GNNs) that leverages a genetic algorithm (GA) to directly optimize discrete edge perturbations. Unlike prevalent gradient-based methods that rely on continuous relaxation and differentiable proxy losses, EvA operates natively in the discrete combinatorial space. The authors introduce a sparse encoding scheme to reduce memory complexity and demonstrate that EvA significantly outperforms state-of-the-art gradient-based baselines (e.g., PRBCD) in reducing node classification accuracy. Furthermore, the black-box nature of EvA enables novel attack objectives that are difficult to optimize via gradients, specifically targeting robustness certificates and conformal prediction sets. The paper provides extensive empirical evaluations across multiple datasets, models, and threat models, highlighting the sub-optimality of gradient-based relaxations and the untapped potential of search-based attacks.

## Strengths
1. **Conceptual Shift from Gradient Relaxation:** The paper correctly identifies a fundamental limitation of gradient-based graph attacks: the reliance on continuous relaxation and differentiable proxies, which can lead to sub-optimal discrete solutions and false security. Proposing a direct discrete optimization via GA is a timely and valuable contribution.
2. **Novel Attack Objectives:** Leveraging the black-box nature of EvA to attack robustness certificates and conformal prediction sets is highly innovative. These objectives involve non-differentiable components (e.g., majority voting, quantile computation) that are notoriously difficult for gradient-based methods, demonstrating the practical versatility of the proposed framework.
3. **Sparse Encoding and Efficiency:** The introduction of a sparse index-based encoding that directly enforces the perturbation budget is a clever engineering contribution. It reduces memory overhead and enables batch evaluation, making the GA approach computationally feasible despite its high query complexity.
4. **Comprehensive Empirical Evaluation:** The paper provides extensive experiments across multiple datasets (Cora-ML, Citeseer, PubMed), models (GCN, GAT, APPNP, GPRGNN), and threat models (global, local, targeted, inductive, transductive). The consistent outperformance of EvA over strong baselines like PRBCD provides robust evidence for the core claim.

## Weaknesses
1. **Overstated Claims on Gradient Limitations:** The introduction claims EvA "fixes all five" challenges of gradient-based attacks, including white-box access and quadratic memory complexity. However, EvA still assumes full knowledge of the graph structure and labels (a strong structural white-box assumption), and its memory complexity scales with population size $O(|S| \cdot \epsilon \cdot E)$, not just the budget. This overstatement reduces scientific rigor.
2. **Lack of Random Search Control:** The paper attributes EvA's superiority to the GA's ability to avoid local optima. Without a random search baseline using the same evaluation budget, it is unclear whether the performance gain stems from the evolutionary operators (crossover/mutation) or simply from the larger number of forward passes enabled by EvA's efficiency.
3. **Ambiguous Metric Reporting:** The abstract claims an "~11% additional accuracy drop" without specifying whether this is absolute or relative, or the exact scope (datasets/models/budgets). Similarly, the claim that EvA drops accuracy "below the MLP level" lacks explicit MLP baseline values for grounding.
4. **Assumption Sensitivity in Novel Objectives:** The conformal attack assumes using the entire unlabeled set as the calibration set. While theoretically justified by exchangeability, this assumption may not hold perfectly in practice. The paper lacks validation of the attack's robustness under standard, smaller calibration splits.
5. **Query Complexity Limitation:** EvA requires hundreds of thousands of forward passes, which is unrealistic for many practical black-box scenarios. The paper acknowledges this but does not quantify the query budget or compare it to standard practical limits, leaving the trade-off between effectiveness and efficiency under-contextualized.

## Key Issues
1. **Causal Attribution of Performance Gains:** The core claim is that GA's evolutionary operators enable superior exploration compared to gradient-based relaxation. However, without a matched-budget random search control, the observed gains could be confounded by EvA's ability to perform more forward passes. This threatens the validity of the "untapped potential of search-based attacks" conclusion.
2. **Defensibility of "First" Claims:** The paper claims to introduce the "first graph certificate attack" and "first conformal attack on graphs." Without precise scoping (e.g., structural vs. feature perturbations, specific threat models) and cautious phrasing ("to our knowledge"), these claims are vulnerable to prior work that may have attacked similar objectives under different assumptions.
3. **Memory Complexity Inconsistency:** The introduction claims $O(\epsilon \cdot E)$ memory complexity, omitting the population size factor $|S|$. This creates a factual inconsistency with the Method section ($O(|S| \cdot \epsilon \cdot E)$) and misleads readers about the true memory footprint of the GA approach.
4. **Strawman Comparison for Sparse Encoding:** Contrasting EvA's sparse encoding against a "naive" $O(N^2)$ dense representation ignores that modern baselines (e.g., PRBCD) already use block-coordinate descent to mitigate memory issues. This framing overstates the novelty of the sparse encoding contribution.

## Actionable Suggestions
1. **Add Random Search Control:** Include a random search baseline with the same evaluation budget (number of forward passes) as EvA. This will isolate the contribution of evolutionary operators (crossover/mutation) from the sheer volume of evaluations, strengthening the causal claim about GA's exploratory power.
2. **Bound and Clarify "First" Claims:** Rephrase claims about certificate and conformal attacks to "to our knowledge, the first structural attacks targeting..." and explicitly define the threat model scope. Add a brief discussion in Related Work to differentiate from prior feature-based or white-box certificate attacks.
3. **Correct Memory Complexity Statement:** Update the introduction and abstract to state memory complexity as $O(|S| \cdot \epsilon \cdot E)$, acknowledging the population size dependency. Clarify that sparse encoding provides a complementary efficiency gain over block-coordinate descent rather than solving a fundamental quadratic memory problem.
4. **Ground Metric Claims:** In the abstract and results, specify whether the "~11% additional drop" refers to absolute accuracy points. Provide explicit MLP baseline accuracy values when claiming EvA drops performance "below the MLP level" to ensure the claim is verifiable and contextualized.
5. **Validate Conformal Attack Assumptions:** Add an ablation in the appendix testing the conformal attack under standard, smaller calibration splits (e.g., 10-20% of unlabeled nodes) to demonstrate that the coverage degradation is robust to calibration set size and not an artifact of using the entire unlabeled set.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** Graph Neural Networks are vulnerable to small structural perturbations, yet current attacks rely on gradient-based relaxations that are sub-optimal and restricted to differentiable objectives.
- **S2 (Significance/Challenge):** This reliance limits attack effectiveness, assumes white-box access, and prevents targeting complex non-differentiable defenses like robustness certificates.
- **S3 (Prior Gap):** Gradient methods struggle with the discrete combinatorial nature of edge perturbations and often get stuck in local minima or require inefficient proxy losses.
- **S4 (Proposed Method):** We propose Evolutionary Attack (EvA), a black-box framework that uses a genetic algorithm to directly optimize discrete edge perturbations, featuring a sparse encoding for memory efficiency.
- **S5 (Key Result & Implication):** EvA outperforms SOTA gradient attacks by ~11% absolute accuracy drop and enables novel attacks on certificates and conformal sets, highlighting the untapped potential of search-based adversarial strategies.

### Introduction Outline (Complete)
- **P1 (Big Picture & Gap):** Establish GNN robustness importance. Detail the 5 core limitations of gradient-based attacks (relaxation, proxy loss, white-box, false security, memory) and introduce EvA as a direct discrete optimizer that addresses these constraints.
- **P2 (Method Intuition & Efficiency):** Explain the GA mechanism (population, fitness, crossover, mutation) and the sparse index-based encoding. Clarify that memory scales with population size and budget, enabling batch evaluation without dense gradient storage.
- **P3 (Novel Objectives):** Leverage the black-box nature to introduce attacks on robustness certificates and conformal prediction sets. Emphasize that these non-differentiable objectives are intractable for gradient methods but straightforward for EvA via fitness function modification.
- **P4 (Empirical Evidence):** Preview key results: EvA consistently outperforms PRBCD across datasets/models, drops accuracy below MLP baselines with small budgets, and maintains effectiveness under local constraints.
- **P5 (Contribution Summary):** Consolidate contributions: (1) EvA framework for discrete black-box attacks, (2) sparse encoding for efficiency, (3) novel certificate/conformal attacks, (4) empirical demonstration of gradient sub-optimality.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Add random search control with matched evaluation budget. | Isolates GA operator contribution from query budget advantages; strengthens causal claim. | Medium |
| **P0** | Correct memory complexity claim to $O(|S| \cdot \epsilon \cdot E)$ and acknowledge baseline block-coordinate descent. | Fixes factual inconsistency; improves scientific rigor and fairness. | Low |
| **P1** | Bound "first" claims for certificate/conformal attacks with "to our knowledge" and precise scoping. | Prevents rejection due to prior work overlap; improves defensibility. | Low |
| **P1** | Ground "~11% drop" and "below MLP" claims with explicit metric definitions and baseline values. | Enhances result interpretability and reproducibility. | Low |
| **P2** | Validate conformal attack under standard smaller calibration splits. | Demonstrates robustness of the attack to calibration assumptions. | Medium |
| **P2** | Quantify query complexity (total forward passes) and compare to practical black-box budgets. | Contextualizes the trade-off between effectiveness and efficiency. | Low |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | EvA outperforms gradient attacks on vanilla models. | CoraML, Citeseer, PubMed; GCN, GAT, APPNP, GPRGNN; Inductive/Transductive. | Accuracy | EvA drops accuracy significantly more than PRBCD/LRBCD. | C1, C2 | Lacks random search control. |
| E2 | EvA effectiveness under local constraints. | Same as E1 + local budget $\epsilon_{loc}=0.5$. | Accuracy | EvA-Local outperforms LRBCD; constrained EvA sometimes beats unconstrained baselines. | C2 | Needs concrete dataset examples for "beats unconstrained" claim. |
| E3 | Targeted attack performance. | Node-by-node attack, budget 1-10 edges. | Success rate / Perturbations | EvA outperforms PRBCD for budget $\ge 2$. | C1 | Uses tanh-margin proxy without ablation. |
| E4 | Attack on robustness certificates. | Sparse smoothing on GPRGNN. | Certified ratio / Cert accuracy | Certified ratio drops below MLP level; clean accuracy preserved. | C3 | MC variance control not explicitly discussed. |
| E5 | Attack on conformal prediction. | Inductive CP on GCN. | Coverage / Set size | Coverage drops quickly; set size increases. | C3 | Assumes entire unlabeled set for calibration. |
| E6 | Scaling and mutation ablation. | PubMed; varying population size, steps, mutation types. | Accuracy | ATM consistently improves performance; scaling helps EvA but not PRBCD. | C1 | No random search baseline for scaling. |

### Research-Theme Gap Diagnosis
The core research value lies in demonstrating that discrete search-based attacks are fundamentally more effective than gradient relaxations. However, the current evidence conflates search quality with evaluation budget. Additionally, the novelty of certificate/conformal attacks relies on strong assumptions (e.g., calibration set size) that need validation to ensure practical relevance.

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| C1 (GA superiority) | GA operators provide genuine exploration advantage over random search. | Run random search with same forward pass budget as EvA. | Random Search, PRBCD | Accuracy drop | EvA significantly outperforms random search. | Low | Isolates causal mechanism of GA success. |
| C3 (Conformal robustness) | Conformal attack generalizes to standard calibration splits. | Repeat E5 with 10%, 20%, 50% of unlabeled nodes as calibration. | Standard CP setup | Coverage drop | Consistent coverage degradation across split sizes. | Medium | Validates practical threat model assumption. |
| C2 (Query efficiency) | Query complexity is a trade-off for effectiveness. | Quantify total forward passes for EvA vs. query budgets in practical settings. | Practical black-box limits | Passes / Accuracy | Clear Pareto frontier visualization. | Low | Contextualizes limitation and guides future work. |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6/10

**Rationale:** The paper presents a compelling and timely contribution by shifting the focus from gradient-based relaxations to direct discrete optimization via genetic algorithms. The empirical results are strong, demonstrating consistent outperformance over SOTA baselines and enabling novel attack objectives (certificates, conformal prediction) that are difficult for gradient methods. However, the score is moderated by several key issues: the lack of a random search control to isolate the contribution of evolutionary operators from evaluation budget advantages, overstated claims regarding memory complexity and white-box assumptions, and insufficient scoping of "first" claims for novel objectives. Addressing these issues would significantly strengthen the paper's scientific rigor and defensibility.

**Post-Revision Target:** [7, 8]/10

**Path to Target:** Adding a matched-budget random search control, correcting the memory complexity statement, bounding the "first" claims with precise scoping, and grounding metric claims with explicit baselines would resolve the major validity and objectivity concerns, elevating the paper to a strong acceptance candidate.