## Summary
# Final Review Report

## Summary
This paper addresses the computational bottleneck of hyperparameter optimization (HPO) and neural architecture search (NAS) by proposing Hyperparameter-Calibrated Dataset Condensation (HCDC). Standard dataset condensation methods optimize synthetic data for a single pre-specified architecture, leading to poor generalization and ranking flips when evaluated across multiple architectures. HCDC reformulates condensation under an HPO framework, theoretically showing that preserving performance rankings is equivalent to aligning hyperparameter gradients (hypergradients) on an extended search space. The method uses implicit differentiation and Neumann series approximation to efficiently compute and match hypergradients between original and condensed datasets. Experiments on image (CIFAR-10/100) and graph (Cora, Citeseer, Ogbn-arxiv, Reddit) benchmarks demonstrate that HCDC significantly improves Spearman's rank correlation and accelerates NAS algorithms (DARTS-PT, REINFORCE) while preserving selection accuracy.

## Strengths
1. **Clear Motivation and Problem Formulation:** The paper identifies a critical gap in standard dataset condensation—its failure to preserve performance rankings across multiple architectures—and clearly motivates the need for a hyperparameter-aware condensation objective.
2. **Theoretical Insight:** The equivalence between ranking preservation and hypergradient alignment on an extended search space provides a novel theoretical foundation for dataset condensation in the context of HPO/NAS.
3. **Efficient Implementation:** The use of implicit differentiation and Neumann series approximation allows for efficient hypergradient computation with constant memory overhead, making the method scalable.
4. **Strong Empirical Results:** HCDC demonstrates significant improvements in Spearman's rank correlation over strong baselines (DC, DSA, TM) on both image and graph datasets, and effectively speeds up off-the-shelf NAS algorithms while maintaining selection accuracy.
5. **Broad Applicability:** The method is validated on both discrete (architecture search) and continuous (GNN convolution filter) hyperparameter spaces, demonstrating versatility.

## Weaknesses
1. **Theoretical Assumptions on Local-to-Global Equivalence:** Theorem 1 claims equivalence between hypergradient alignment and ranking preservation based on a first-order Taylor approximation. This approximation is only locally valid, and the paper does not sufficiently justify how local alignment integrates to preserve global rankings across potentially non-convex loss landscapes.
2. **Strong Assumption in Extended Search Space Construction:** For discrete search spaces, the method constructs extended paths via HPO trajectories and assumes they converge to the same or equivalent optima. In practice, non-convex HPO landscapes often yield distinct local optima, which may undermine the connectivity assumption and the validity of the alignment objective.
3. **Missing Ablation Studies:** The paper lacks ablation studies on critical design choices, such as the number of HPO trajectories, the length of trajectories, the impact of Neumann series truncation steps, and the sensitivity to the choice of the base SDC method for $S_{train}$.
4. **Incomplete Efficiency Analysis:** While Table 3 reports search time speedups, it omits the one-time computational cost of generating the HCDC condensed dataset. Without reporting condensation overhead and break-even points, the total efficiency gain is incomplete.
5. **Lack of Mechanistic Analysis:** The results section reports strong correlations but does not analyze *why* HCDC succeeds where trajectory-matching methods fail, missing an opportunity to provide deeper scientific insight.

## Key Issues
1. **Validity of Theorem 1 Equivalence:** The equivalence between hypergradient alignment and hyperparameter calibration relies on a first-order Taylor approximation. Without explicit smoothness assumptions or bounds on the approximation error, the claim that local alignment guarantees global ranking preservation is mathematically overreaching. This threatens the theoretical foundation of the method.
2. **Connectivity Assumption in Extended Search Space:** The construction of $\tilde{\Lambda}$ assumes HPO trajectories converge to a common optimum. If trajectories converge to distinct local optima (common in NAS), the "connected" paths may not accurately represent the global ranking structure, potentially leading to misaligned gradients along irrelevant paths.
3. **Missing Condensation Overhead Reporting:** The efficiency claims in Table 3 are incomplete without reporting the one-time cost of generating $S_{val}$ via HCDC. Reviewers cannot assess the net computational savings or the break-even point for different search space sizes.
4. **Lack of Ablation on Design Choices:** The performance of HCDC may be sensitive to the number of trajectories, trajectory length, and Neumann series truncation steps. The absence of ablation studies makes it difficult to verify the robustness of these design choices and to guide future implementations.

## Actionable Suggestions
1. **Clarify Theorem 1 Assumptions:** Revise Theorem 1 to explicitly state the smoothness assumptions required for the first-order approximation to hold. Add a discussion on the conditions under which local gradient alignment integrates to preserve global rankings, or bound the claim to "local hyperparameter calibration."
2. **Relax or Verify Connectivity Assumption:** In Section 5.2, clarify whether the HPO trajectories are treated as a strict topological guarantee or a heuristic continuous relaxation. If heuristic, provide empirical evidence (e.g., plotting trajectory endpoints) to show whether they converge to similar optima in the tested search spaces.
3. **Report Condensation Overhead:** Add a paragraph or table reporting the one-time training time for generating $S_{val}$ via HCDC. Calculate and report the break-even point (number of search iterations where HCDC becomes faster than original data search) to provide a complete efficiency analysis.
4. **Add Ablation Studies:** Include ablation experiments on: (a) the number of HPO trajectories used to construct $\tilde{\Lambda}$, (b) the length of these trajectories, and (c) the number of Neumann series truncation steps. This will validate the robustness of the design choices.
5. **Enhance Mechanistic Analysis:** Add a discussion analyzing why HCDC outperforms trajectory-matching methods. For example, discuss whether hypergradient alignment forces the condensed set to capture global data manifold properties rather than overfitting to single-model training dynamics.
6. **Improve Related Work Positioning:** Add a dedicated paragraph contrasting HCDC with trajectory-matching methods (e.g., TM) and explicitly stating why their objectives fail to preserve cross-architecture rankings.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** Dataset condensation reduces training costs by synthesizing small proxy datasets, but standard methods overfit to single architectures and fail to preserve performance rankings across hyperparameters.
- **S2 (Significance/Challenge):** This ranking failure makes existing condensation methods inadequate for hyperparameter optimization (HPO) and neural architecture search (NAS), which require consistent relative performance evaluation.
- **S3 (Prior Gap):** Current gradient-matching and trajectory-matching objectives optimize for fixed architectures, lacking a mechanism to capture cross-architecture sensitivity.
- **S4 (Proposed Method):** We propose Hyperparameter-Calibrated Dataset Condensation (HCDC), which aligns hyperparameter gradients (hypergradients) on an extended search space to preserve validation-performance rankings.
- **S5 (Key Result & Implication):** HCDC drastically improves ranking correlation (e.g., from negative to 0.74 on CIFAR-10) and accelerates NAS by up to 6x while maintaining selection accuracy, enabling efficient architecture search on condensed data.

### Introduction Outline (Complete)
- **P1 (Big Picture & Motivation):** Deep learning success relies on HPO/NAS, which requires training numerous models on the same data, posing significant computational challenges. Reducing data size for faster search is crucial.
- **P2 (Prior Work & Gap):** Dataset condensation reduces sample size but is designed for single architectures. Empirical evidence shows condensed data often exhibits negative correlation with original rankings across architectures, making it unsuitable for NAS.
- **P3 (Core Insight & Solution):** We reformulate condensation under an HPO framework and show that ranking preservation is equivalent to aligning hypergradients. This local alignment ensures consistent loss changes across the search space.
- **P4 (Method Overview):** We propose HCDC, which efficiently computes hypergradients via implicit differentiation and constructs an extended continuous search space for discrete hyperparameters.
- **P5 (Evidence Preview):** Experiments on image and graph benchmarks demonstrate that HCDC significantly outperforms coreset and condensation baselines in ranking correlation and speeds up off-the-shelf NAS algorithms.
- **P6 (Contributions):** Explicitly list the three contributions: (1) theoretical equivalence, (2) HCDC algorithm, (3) empirical validation on images/graphs.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Clarify Theorem 1 assumptions and bound the equivalence claim to local calibration or add smoothness justification. | Resolves theoretical validity concern; strengthens scientific rigor. | Low |
| **P0** | Report condensation training overhead and calculate break-even points for efficiency claims. | Completes efficiency analysis; prevents reviewer criticism on incomplete speedup claims. | Low |
| **P1** | Relax or empirically verify the connectivity assumption in extended search space construction (Section 5.2). | Addresses major assumption risk; improves method defensibility. | Medium |
| **P1** | Add ablation studies on trajectory count, length, and Neumann series truncation steps. | Validates design choices; improves reproducibility and robustness claims. | Medium |
| **P2** | Enhance mechanistic analysis of why HCDC outperforms trajectory-matching methods. | Provides deeper scientific insight; strengthens contribution narrative. | Low |
| **P2** | Improve Related Work positioning against trajectory-matching baselines. | Clarifies novelty; helps reviewers understand differentiation. | Low |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | HCDC preserves architecture rankings better than baselines. | CIFAR-10/100, NAS-Bench-201 (100 networks), 50 epochs, 5 seeds. Baselines: Random, K-Center, Herding, DC, DSA, DM, KIP, TM. | Spearman's rank correlation, Test accuracy of best selected. | HCDC achieves 0.74/0.63 correlation vs negative/low for baselines. | Ranking preservation claim. | Lacks ablation on design choices. |
| E2 | HCDC preserves GNN convolution filter rankings. | Cora, Citeseer, Ogbn-arxiv, Reddit. Continuous hyperparameter space. Baselines: Random, GCond-X, GCond. | Spearman's correlation, Test accuracy. | HCDC consistently outperforms baselines across compression ratios. | Applicability to continuous spaces. | No ablation on trajectory construction. |
| E3 | HCDC speeds up off-the-shelf NAS. | DARTS-PT and REINFORCE on condensed datasets. | Search time (sec), Test accuracy. | HCDC reduces search time significantly (e.g., 35.5s vs 229s for DARTS-PT). | Efficiency claim. | Missing condensation overhead reporting. |

### Research-Theme Gap Diagnosis
The core research value (new knowledge on hypergradient alignment for ranking preservation) is well-supported by E1-E3. However, the reproducibility and robustness claims are weakly supported due to missing ablation studies and overhead reporting. The impact on practice is clear but incomplete without break-even analysis.

### Proposed Research Experiments (P0/P1/P2)
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Estimated Cost/Time | Expected Paper-Quality Gain |
|---|---|---|---|---|---|---|---|
| Robustness of design choices | Performance is stable across trajectory counts and lengths. | Vary trajectory count (p/2, p, 2p) and length (T/2, T, 2T). | Fixed HCDC setup. | Correlation, Test accuracy. | <5% performance drop. | 1-2 days GPU time. | Validates method robustness; improves reproducibility. |
| Total efficiency gain | HCDC provides net savings after condensation overhead. | Report condensation training time; calculate break-even iterations. | Original data search. | Total time (condensation + search). | Break-even at reasonable iterations. | 0 days (reporting). | Completes efficiency analysis; prevents reviewer criticism. |
| Mechanistic insight | HCDC captures global manifold properties better than TM. | Analyze condensed data distribution/coverage vs TM. | TM baseline. | Coverage metrics, Correlation. | HCDC shows broader coverage. | 1 day analysis. | Provides deeper scientific insight; strengthens narrative. |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6/10

**Rationale:** The paper presents a novel and well-motivated approach to dataset condensation for hyperparameter search, with strong empirical results demonstrating significant improvements in ranking correlation and search efficiency. The theoretical insight linking ranking preservation to hypergradient alignment is compelling. However, the score is moderated by concerns regarding the mathematical rigor of Theorem 1 (local-to-global equivalence assumption), the strong connectivity assumption in the extended search space construction, and the incomplete efficiency analysis (missing condensation overhead). These issues do not invalidate the core contribution but require clarification and additional reporting to ensure scientific defensibility.

**Post-Revision Target:** [7, 8]/10

**Justification:** If the authors clarify the theoretical assumptions, report the condensation overhead, and add basic ablation studies, the paper will address the major validity and completeness concerns. The strong empirical performance and clear motivation position it well for acceptance with minor revisions.