## Summary
# Final Review Report

## Summary
This paper addresses the "view forgetting" phenomenon in multi-view learning, where models degrade on prior views as new views are incrementally introduced. The authors propose Hebbian View Orthogonal Projection (HVOP), a brain-inspired framework that constructs a Knowledge Transfer Space (KTS) and employs recursive lateral connections with Hebbian learning (Oja rule) to approximate orthogonal projection. This mechanism aims to filter gradient updates, preventing interference with prior knowledge while facilitating cross-view knowledge transfer. Extensive experiments on six multi-view node classification benchmarks demonstrate that HVOP outperforms static multi-view and continual learning baselines in knowledge retention and transfer. While the biological inspiration and orthogonal projection idea are promising, the manuscript suffers from vague mathematical formulations, overclaimed causal links in ablation studies, and insufficient statistical rigor in experiments.

## Strengths
1. **Novel Problem Formulation:** The paper clearly identifies "view forgetting" as a distinct challenge in multi-view incremental learning, differentiating it from standard task/class-incremental continual learning. This framing highlights a practical gap in dynamic multi-view scenarios.
2. **Biologically Inspired Mechanism:** The integration of Hebbian learning (Oja rule) to dynamically approximate orthogonal projection is a creative and computationally efficient alternative to static SVD-based gradient projection methods.
3. **Comprehensive Empirical Evaluation:** The method is evaluated across six diverse multi-view node classification datasets, comparing against both static multi-view and incremental learning baselines, demonstrating consistent performance gains.
4. **Clear Visualization of Forgetting:** Figures 1 and 4 effectively illustrate the view forgetting phenomenon and the stabilizing effect of HVOP, providing intuitive support for the proposed mechanism.

## Weaknesses
1. **Mathematical Rigor and Notation Clarity:** The derivation of orthogonal projection via Hebbian learning lacks mathematical grounding. The equivalence between $I - KK^T$ (SVD-based) and $I - R^T R$ (Oja rule-based) is asserted without convergence proof or dimensional clarification. Loss function notations ($L_{RE}$, $L_{CE}$) are inconsistent and ambiguously defined.
2. **Overclaimed Causal Links in Ablation:** The ablation study (Fig. 5) removes the orthogonal projection module and claims this "strongly validates the role of the forgetting problem in constraining transfer." This is a causal overreach; stability improvements do not directly prove transfer mechanisms without isolated controls.
3. **Insufficient Statistical and Fairness Rigor:** Table 1 compares static and incremental methods without acknowledging information asymmetry. The "MAF1" metric is undefined, and statistical significance tests are missing. Variance reporting is present but not leveraged for significance testing.
4. **Vague Biological-to-Algorithmic Mapping:** The introduction and methodology rely heavily on biological metaphors (hippocampus, lateral connections) without explicitly mapping each concept to a concrete mathematical operation. This risks appearing as decorative packaging rather than a functional design principle.
5. **Conclusion Lacks Limitations and Bounded Claims:** The conclusion repeats introduction claims without summarizing validated findings, acknowledging limitations (e.g., computational overhead, dataset scope), or proposing concrete future work.

## Key Issues
1. **Mathematical Validity of Orthogonal Projection Approximation (Critical):** The core claim that Hebbian learning (Oja rule) approximates orthogonal projection lacks rigorous derivation. Without proving that $R^T R \approx KK^T$ under the proposed update rule, the mechanism's validity is questionable.
2. **Causal Overreach in Ablation Analysis (Major):** The ablation study attributes performance stability directly to "solving forgetting" and "enabling transfer," but does not isolate these effects. Stability is a prerequisite for transfer, not proof of it.
3. **Unfair Baseline Comparison and Missing Metrics (Major):** Comparing static multi-view methods (full view access) with incremental methods (sequential access) without acknowledging information asymmetry misleads readers. The undefined "MAF1" metric and lack of statistical tests reduce result credibility.
4. **Ambiguous Loss Function and Notation Definitions (Major):** Inconsistent notation in $L_{RE}$ and $L_{CE}$ (e.g., $\hat{y}_{ij}$ vs $y_{ij}$, undefined $\sigma$ activation) hinders reproducibility and may lead to implementation errors.
5. **Vague Biological-to-Algorithmic Mapping (Minor):** The heavy reliance on biological metaphors without explicit mathematical translation reduces technical clarity and risks appearing as decorative framing.

## Actionable Suggestions
1. **Formalize Orthogonal Projection Derivation:** Provide a convergence argument or citation showing that the Oja rule update $R_{t+1} = R_t + \eta(x_t y_t^T - y_t y_t^T R_t)$ ensures $R^T R \approx KK^T$. Explicitly state the dimensionality of $R$ and clarify whether projection is applied to gradients or features.
2. **Isolate Stability vs. Transfer in Ablation:** Redesign the ablation study to separately measure (a) retention on old views (stability) and (b) performance gain on new views beyond single-view baselines (transfer). Use matched-capacity controls to rule out parameter count confounds.
3. **Standardize Metrics and Add Statistical Tests:** Define MAF1 explicitly (e.g., Macro-Averaged F1). Add paired t-tests or bootstrap confidence intervals against the strongest incremental baseline (MVCIL). Acknowledge the information asymmetry between static and incremental baselines in the analysis.
4. **Clarify Loss Function Notation:** Standardize cross-entropy notation: let $y_i$ be the one-hot label and $\hat{y}_i$ be the predicted probability. Clarify that $\sigma$ in $L_{RE}$ is a sigmoid activation applied to the similarity matrix $Q Q^T$.
5. **Map Biological Concepts to Mathematical Operations:** Replace vague biological metaphors with explicit algorithmic mappings. For example: "Hippocampal consolidation $\rightarrow$ KTS orthogonal projection," "Synaptic plasticity $\rightarrow$ Oja rule update," "Lateral connections $\rightarrow$ Recursive feature fusion."

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** Traditional multi-view learning methods struggle with dynamic, incrementally arriving views, often suffering from "view forgetting" where prior knowledge degrades as new views are introduced.
- **S2 (Prior Gap):** Existing continual learning strategies focus on task/class boundaries and fail to exploit the consistency and complementarity inherent in multi-view data, leading to inefficient knowledge transfer.
- **S3 (Proposed Method):** We propose Hebbian View Orthogonal Projection (HVOP), a view transfer learning framework that constructs a Knowledge Transfer Space (KTS) to minimize interference between old and new views.
- **S4 (Technical Core):** HVOP employs recursive lateral connections and Hebbian learning (via the Oja rule) to dynamically approximate orthogonal projection, ensuring gradient updates for new views remain orthogonal to the principal subspace of prior views.
- **S5 (Key Result & Scope):** Extensive experiments on six multi-view node classification benchmarks demonstrate that HVOP significantly mitigates view forgetting and achieves superior knowledge retention and transfer compared to static multi-view and continual learning baselines.

### Introduction Outline (Complete)
- **P1 (Big Picture & Practical Stakes):** Modern computational environments increasingly encounter dynamic, incrementally arriving data views (e.g., evolving medical imaging, expanding social networks). Traditional multi-view methods, designed for static datasets, struggle to adapt without costly retraining or knowledge erosion.
- **P2 (Concrete Gap):** This "view forgetting" phenomenon limits overall knowledge integration. Unlike standard continual learning, multi-view incremental learning must additionally exploit cross-view consistency and complementarity, which existing gradient regularization methods (e.g., EWC, SI) do not address.
- **P3 (Proposed Solution & Biological Inspiration):** Drawing inspiration from the brain’s ability to integrate new sensory inputs while retaining past memories, we propose HVOP. We translate neural mechanisms into concrete algorithmic modules: hippocampal consolidation $\rightarrow$ KTS orthogonal projection, synaptic plasticity $\rightarrow$ Oja rule update, and lateral connections $\rightarrow$ recursive feature fusion.
- **P4 (Evidence Preview):** Experiments on six benchmarks show HVOP stabilizes performance against view quality fluctuations and outperforms incremental baselines in both retention and transfer. Ablation studies confirm the critical role of orthogonal projection in preventing interference.
- **P5 (Contribution Summary):** (1) Formalize view forgetting and propose view transfer learning as a distinct setting. (2) Introduce HVOP with dynamic orthogonal projection via Hebbian learning. (3) Demonstrate superior retention/transfer performance with comprehensive ablation analysis.

## Priority Revision Plan
| Priority | Action Item | Expected Impact | Effort |
|---|---|---|---|
| **P0** | Formalize orthogonal projection derivation: prove $R^T R \approx KK^T$ under Oja rule, clarify dimensions. | Validates core mechanism; removes mathematical ambiguity. | Medium |
| **P0** | Redesign ablation to isolate stability vs. transfer; add matched-capacity controls. | Strengthens causal claims; prevents overreach. | High |
| **P0** | Define MAF1 metric; add statistical significance tests against MVCIL. | Improves result credibility and fairness. | Low |
| **P1** | Standardize loss function notation ($L_{RE}$, $L_{CE}$) and clarify activation functions. | Enhances reproducibility and implementation clarity. | Low |
| **P1** | Map biological concepts explicitly to mathematical operations in Intro/Method. | Improves technical clarity; reduces decorative framing. | Medium |
| **P2** | Rewrite conclusion to summarize validated findings, acknowledge limitations, and propose future work. | Improves scientific discipline and reader trust. | Low |

**Page Coverage Audit:**
- Page 1 (Abstract/Intro): Covered (2 annotations)
- Page 2 (Intro/Fig 1): Covered (1 annotation)
- Page 3 (Intro/Related Work): Covered (1 annotation)
- Page 4 (Method Overview): Covered (1 annotation)
- Page 5 (Sec 3.1-3.2): Covered (1 annotation)
- Page 6 (Sec 3.3-3.4): Covered (1 annotation)
- Page 7 (Sec 3.4/Loss): Covered (1 annotation)
- Page 8 (Exp/Table 1): Covered (1 annotation)
- Page 9-10 (Ablation/Conclusion): Covered (1 annotation)
- All substantive paragraphs in Abstract, Introduction, Method, Experiments, and Conclusion are covered.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | HVOP vs. SOTA baselines | 6 datasets, static & incremental baselines | ACC, P, R, MAF1 | HVOP outperforms most baselines | Superior overall perception | Unfair static vs. incremental comparison; undefined MAF1 |
| E2 | View forgetting relief (Fig 4) | GCN vs. HVOP on NGs/Animals | Accuracy over views | HVOP shows smoother decline | Strong memory retention | Lacks statistical tests; no variance analysis |
| E3 | Knowledge transfer verification (Fig 5) | Single-view vs. HVOP streaming | Accuracy over views | HVOP > single-view | Effective knowledge transfer | Causal link to transfer not isolated |
| E4 | Ablation: remove orthogonal projection | HVOP w/o projection | Accuracy stability | Performance fluctuates significantly | Projection stabilizes learning | Overclaims "solves forgetting"; no matched control |
| E5 | Convergence & view order (Fig 6) | Loss curves & permutation accuracy | Loss, Accuracy | Stable loss; order-invariant | Robust to view sequence | Limited to one dataset (NGs) |

### Research-Theme Gap Diagnosis
- **Causal Isolation Gap:** The ablation study does not separate stability (retention) from transfer (new view gain). Without matched-capacity controls, gains may stem from architectural differences rather than orthogonal projection.
- **Statistical Rigor Gap:** Missing significance tests and undefined metrics reduce confidence in reported gains.
- **Generalization Gap:** Evaluation is limited to node classification; no OOD or cross-domain tests are provided.

### Proposed Research Experiments (P0/P1/P2)
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|---|---|---|---|---|---|---|---|
| Stability vs. Transfer | Orthogonal projection primarily improves stability, not transfer. | Measure retention drop ($\Delta_{old}$) and new-view gain ($\Delta_{new}$) separately. | HVOP w/o projection, HVOP w/o lateral connections | $\Delta_{old}$, $\Delta_{new}$ | Projection reduces $\Delta_{old}$ significantly | Low | Isolates mechanism contribution |
| Statistical Significance | HVOP gains are statistically significant over MVCIL. | Run 5 seeds per dataset; perform paired t-tests. | MVCIL, SI, MAS | p-values, CI | p < 0.05 for key datasets | Medium | Validates result credibility |
| OOD Generalization | HVOP generalizes to unseen view distributions. | Train on subset of views, test on held-out view types. | Static baselines, MVCIL | ACC drop | Smaller drop than baselines | High | Strengthens robustness claims |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 5.5/10  
**Post-Revision Target:** [7.0, 8.0]/10

**Scoring Rationale:**  
The paper addresses a meaningful problem (view forgetting in multi-view incremental learning) and proposes a creative mechanism (Hebbian orthogonal projection). However, the current manuscript suffers from mathematical ambiguity in the core derivation, overclaimed causal links in ablation studies, and insufficient statistical rigor. These issues reduce confidence in the validity and novelty of the claims. With rigorous derivation, isolated ablation controls, and statistical validation, the paper could significantly improve its scientific defensibility and impact.

---

### ASCII Diagram — Paper Structure & Evidence Map
```text
[Problem: View forgetting in multi-view incremental learning]
    -> [Gap: Static methods lack adaptability; CL methods ignore view complementarity]
    -> [Solution: HVOP with KTS + Hebbian orthogonal projection]
    -> [Evidence: Table 1 (SOTA comparison), Fig 4-5 (Retention/Transfer), Fig 6 (Stability)]
    -> [Risk: Mathematical derivation unproven; ablation overclaims causal transfer]
    -> [Fix: Formalize Oja convergence; isolate stability vs. transfer; add significance tests]
```

### ASCII Diagram — Revision Strategy Roadmap
```text
Stage 1 (Immediate): Clarify notation, define MAF1, map biological concepts to math.
Stage 2 (This Week): Add convergence argument for Oja rule; redesign ablation for stability/transfer isolation.
Stage 3 (Before Submission): Run 5-seed experiments with significance tests; rewrite conclusion with limitations.
```

### ASCII Diagram — Related-Work Taxonomy Tree (Layered)
```text
Multi-View Incremental Learning (Root)
├── Branch 1: Static Multi-View Fusion
│   ├── Leaf 1.1: Uncertainty-aware fusion (DUANet)
│   └── Leaf 1.2: Consistency/Complementarity capture (LGCNFF, RCML)
├── Branch 2: Continual Learning Adaptations
│   ├── Leaf 2.1: Gradient regularization (EWC, SI, MAS)
│   └── Leaf 2.2: Class-incremental multi-view (MVCIL)
└── Branch 3: Brain-Inspired Mechanisms (This Paper)
    ├── Leaf 3.1: Hebbian learning for principal component extraction
    └── Leaf 3.2: Orthogonal projection for gradient interference mitigation
```

**Novelty Verification Note:**  
External literature verification was unavailable in this run (Retrieval-Disabled Mode active). Novelty verdicts for C1-C3 are deferred to manual verification. Based on internal audit, the view incremental setting and Hebbian orthogonal projection mechanism appear partially novel, but overlap with gradient projection memory (Saha et al.) and multi-view continual learning (Li et al.) requires careful positioning.