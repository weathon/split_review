## Summary
# Final Review Report

## Summary

This paper addresses a fundamental challenge in offline reinforcement learning (RL) with sparse continuous policies: the out-of-support action problem. When dataset actions fall outside the finite support of a sparse policy, standard log-likelihood evaluations become undefined, causing learning failure. The authors propose Fat-to-Thin Policy Optimization (FtTPO), a two-stage framework that first learns an infinite-support "fat" proposal policy from the offline dataset and then distills its knowledge into a sparse "thin" actor policy via reverse KL minimization. Instantiated with the q-Gaussian family, FtTPO effectively handles support mismatch and demonstrates competitive performance on safety-critical treatment simulations and standard MuJoCo benchmarks. The paper makes a clear contribution by formalizing the out-of-support issue and providing a systematic, theoretically motivated solution that avoids ad-hoc workarounds.

## Strengths
1. **Clear Problem Formulation:** The paper identifies a well-defined and practically significant gap: the incompatibility between finite-support sparse policies and standard offline RL loss functions that require evaluating arbitrary dataset actions. The mathematical formalization of the out-of-support action failure mode (Section 3.1) is rigorous and easy to follow.

2. **Elegant Two-Stage Mechanism:** The fat-to-thin policy distillation framework is conceptually clean and theoretically motivated. Using an infinite-support proposal policy to capture high-reward regions, followed by reverse KL minimization to truncate heavy tails into a sparse actor, provides a principled solution to the support mismatch problem.

3. **Strong Empirical Validation:** The experiments on the safety-critical treatment simulation effectively demonstrate the practical value of sparse policies for concentrating probability mass on safe action regions. The MuJoCo results further challenge the assumption that sparsity inherently degrades performance, showing that FtTPO competes favorably with full-support baselines.

4. **Reproducibility and Transparency:** The authors provide clear algorithmic descriptions (Algorithm 3), detailed hyperparameter settings in the appendix, and open-source code, which significantly enhances the paper's reproducibility and potential impact.

## Weaknesses
1. **Safety-Reward Equivalence Assumption:** The paper equates higher cumulative reward with safety-respecting behavior in the treatment simulation. While acknowledged as a simplification, this assumption conflates reward maximization with explicit constraint satisfaction. True safety-critical RL typically requires formal constraint handling (e.g., CPO, Lagrangian methods), and sparse support alone does not guarantee safety without verified bounds.

2. **Limited Theoretical Analysis:** The paper lacks theoretical guarantees for the fat-to-thin distillation process. Specifically, there is no analysis of convergence properties, sample complexity, or error bounds when distilling from an infinite-support proposal to a finite-support actor under reverse KL minimization. This limits the understanding of when and why the method succeeds or fails.

3. **Compute Efficiency Trade-off:** Maintaining two policy networks (fat and thin) approximately doubles the training computation time compared to single-policy baselines (15 hours vs. 6-8 hours). While the inference cost remains similar, the training overhead should be more explicitly discussed as a practical limitation, especially for large-scale offline RL applications.

4. **Scope of "First" Claims:** The contributions claim to be the "first" to investigate the out-of-support issue and propose a deep offline RL framework for sparse policies. Without comprehensive external literature verification, these claims risk overreach. The novelty should be more carefully scoped to the specific fat-to-thin distillation mechanism and q-Gaussian instantiation.

## Key Issues
1. **Claim-Evidence Alignment on Safety:** The paper claims sparse policies enable "safety-aware" learning, but the empirical validation relies solely on reward maximization in a synthetic environment where safety is encoded as a penalty. This does not constitute rigorous safety verification. Without explicit constraint satisfaction metrics or out-of-distribution safety tests, the safety claim remains partially supported.

2. **Missing Ablation on Mean-Copying Mechanism:** The stabilization technique of copying the proposal mean to the actor before every update is critical to training stability but lacks ablation analysis. Readers cannot assess how sensitive the method is to this heuristic or whether alternative alignment strategies (e.g., variance matching, support projection) might be more robust.

3. **Generalization Beyond Tested Settings:** The experiments are limited to one synthetic treatment environment and standard MuJoCo locomotion tasks. The method's effectiveness in higher-dimensional action spaces, partially observable settings, or real-world robotic datasets remains unverified, limiting the generalizability of the conclusions.

4. **Novelty Scoping and Literature Context:** Due to retrieval limitations in this review run, the "first" claims regarding out-of-support action handling and deep offline sparse policy learning require manual verification against recent literature. The novelty should be conservatively scoped to the specific fat-to-thin distillation mechanism and q-Gaussian instantiation until broader context is established.

## Actionable Suggestions
1. **Strengthen Safety Validation:** Add an explicit safety constraint metric (e.g., violation rate of cumulative dosage threshold) alongside reward scores. If possible, include one out-of-distribution or perturbed treatment scenario to test whether the sparse policy maintains safety under distribution shift.

2. **Ablate the Mean-Copying Heuristic:** Include an ablation study comparing the current mean-copying strategy against alternatives: (a) no copying, (b) copying both mean and variance, (c) support projection. Report training stability and final performance to quantify the heuristic's contribution.

3. **Clarify q-Exponential Filtering Threshold:** In Section 4.3, explicitly state the mathematical threshold for action truncation: $Q(s, a) - V(s) < -\tau / (1-q)$. Provide a brief visualization or table showing how different $q$ values affect the proportion of filtered actions across datasets.

4. **Scope Novelty Claims Conservatively:** Replace absolute "first" claims with scoped statements, e.g., "To our knowledge, this is the first framework to address out-of-support actions in offline RL via fat-to-thin policy distillation." Add a paragraph in Related Work explicitly contrasting FtTPO with two-stage methods like GAC and SPOT.

5. **Improve Introduction Narrative Flow:** Restructure the introduction to follow a clearer arc: (1) practical motivation for sparse policies in safety-critical RL, (2) fundamental incompatibility with offline learning losses, (3) failure of ad-hoc solutions, (4) proposed fat-to-thin distillation intuition, (5) empirical validation preview. This will significantly improve reader engagement and claim clarity.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)
- **S1 (Problem & Domain):** Sparse continuous policies assign strictly zero probability to certain actions, offering structural advantages for safety-critical reinforcement learning where specific actions must be avoided.
- **S2 (Significance/Challenge):** Combining sparse policies with offline RL enables learning from logged data without online exploration risks, but creates a fundamental incompatibility: dataset actions frequently fall outside the sparse policy's finite support, causing undefined log-likelihoods and learning failure.
- **S3 (Prior Gap):** Existing methods rely on ad-hoc workarounds like Gaussian approximation or random action replacement, which either violate safety constraints or introduce high variance and bias.
- **S4 (Proposed Method):** We propose Fat-to-Thin Policy Optimization (FtTPO), a two-stage framework that learns an infinite-support proposal policy from the offline dataset and distills its knowledge into a sparse actor policy via reverse KL minimization.
- **S5 (Key Result & Bounded Implication):** Instantiated with the q-Gaussian family, FtTPO successfully handles out-of-support actions and demonstrates competitive performance on safety-critical treatment simulations and standard MuJoCo benchmarks, showing that sparsity does not inherently degrade offline RL performance.

### Introduction Outline (Complete)
- **P1 (Big Picture & Motivation):** Establish the practical need for sparse policies in safety-critical domains (e.g., medical treatment, robotics) where dangerous actions must be strictly avoided. Contrast with standard Gaussian policies that assign nonzero probability everywhere.
- **P2 (Research Gap):** Identify the core technical barrier: offline RL algorithms require evaluating dataset actions under the current policy, but sparse policies have finite support, leading to undefined log-likelihoods when dataset actions fall outside the support.
- **P3 (Failure of Prior Solutions):** Explain why existing ad-hoc methods fail. Gaussian approximations destroy safety guarantees; random replacement introduces bias/variance; reverse KL alone causes mode collapse. This establishes the need for a systematic solution.
- **P4 (Proposed Solution Intuition):** Introduce the fat-to-thin distillation intuition: use an infinite-support "fat" policy to robustly learn from the dataset, then distill its high-reward knowledge into a "thin" sparse policy that truncates heavy tails while preserving safety.
- **P5 (Evidence Preview & Contributions):** Preview empirical results showing FtTPO learns tightly concentrated, safety-aware policies that compete with full-support baselines. List contributions: (1) formalizing the out-of-support issue, (2) proposing FtTPO framework, (3) comprehensive empirical validation on safety-critical and standard benchmarks.

## Priority Revision Plan
| Priority | Task | Effort | Expected Impact |
|---|---|---|---|
| **P0** | Scope novelty claims and add explicit comparison with GAC/SPOT in Related Work. | Low | Improves defensibility and prevents rejection on novelty grounds. |
| **P0** | Add safety constraint violation metrics alongside reward scores in Section 5.1. | Medium | Strengthens the core safety-awareness claim with direct evidence. |
| **P1** | Ablate the mean-copying stabilization heuristic (no copy, variance copy, support projection). | Medium | Quantifies the contribution of a critical implementation detail. |
| **P1** | Clarify q-exponential filtering threshold mathematically and visualize filtered action proportions. | Low | Improves method transparency and reproducibility. |
| **P2** | Restructure Introduction following the provided outline (Big Picture -> Gap -> Failure of Priors -> Solution -> Evidence). | Medium | Significantly improves narrative flow and reader engagement. |
| **P2** | Discuss compute efficiency trade-off explicitly (15h vs 6-8h) and justify overhead. | Low | Enhances practical transparency and sets realistic expectations. |

**Execution Order:** Complete P0 items first to secure claim defensibility. Then execute P1 experiments to strengthen methodological rigor. Finally, apply P2 writing improvements to polish the narrative.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory
| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1 | Sparse policies learn safer, concentrated actions in treatment simulation. | Synthetic treatment env (Li et al., 2023), 50 trajectories, 24 steps. | Cumulative reward, policy density plots. | FtTPO outperforms baselines; learns tightly concentrated sparse policy. | Safety-aware sparse learning is feasible. | Safety equated with reward; no explicit constraint violation metric. |
| E2 | FtTPO competes with full-support baselines on standard offline RL tasks. | D4RL MuJoCo (9 datasets), 1M steps, 10 seeds. | Normalized score, learning curves. | FtTPO matches/exceeds IQL, XQL, InAC across environments. | Sparsity does not inherently degrade performance. | No statistical significance tests reported. |
| E3 | Ablation: KL minimization vs SPOT, heavy-tailed vs Gaussian proposal. | MuJoCo datasets, variant comparisons. | Final score proportion relative to FtTPO. | Simple KL actor loss on par with SPOT; heavy-tailed proposal superior to Gaussian. | Design choices are robust and well-justified. | Limited to final scores; AUC analysis only in appendix. |

### Research-Theme Gap Diagnosis
The core research value—enabling safe, sparse offline policies—is well-supported empirically but lacks theoretical grounding and explicit safety constraint validation. The compute overhead and stabilization heuristics need deeper analysis to establish practical deployment feasibility.

### Proposed Research Experiments
| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost/Time | Expected Gain |
|---|---|---|---|---|---|---|---|
| Safety constraint satisfaction | Sparse policies violate safety constraints less frequently than Gaussian baselines. | Run treatment env with explicit dosage threshold tracking. | IQL, XQL, SQL | Constraint violation rate, reward | Violation rate < 5% with competitive reward | 1 day | Direct safety evidence |
| Mean-copying necessity | Copying proposal mean stabilizes actor training and prevents support drift. | Ablate: no copy, variance copy, support projection. | Standard FtTPO | Training stability (variance), final score | Standard FtTPO shows lowest variance & highest score | 2 days | Quantifies heuristic value |
| Distribution shift robustness | Sparse policies maintain performance under mild environment perturbations. | Perturb treatment dynamics (noise, parameter shifts). | Full-support baselines | Relative performance drop | FtTPO drop < baseline drop | 3 days | Validates robustness claim |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6.5/10

**Post-Revision Target:** [7.5, 8.5]/10

**Scoring Rationale:** The paper addresses a well-defined and practically significant problem in offline RL with sparse policies. The fat-to-thin distillation mechanism is conceptually elegant and empirically validated on safety-critical and standard benchmarks. However, the score is moderated by the lack of explicit safety constraint metrics, limited theoretical analysis, and unscoped novelty claims. Addressing the P0/P1 revision items—particularly adding safety violation metrics, ablating the mean-copying heuristic, and scoping novelty claims—would significantly strengthen the paper's defensibility and impact, justifying the post-revision target.

---

### ASCII Diagram — Paper Structure & Evidence Map
```text
[Problem: Out-of-support actions in offline RL with sparse policies]
    -> [Evidence: Forward KL loss returns -inf when dataset actions fall outside support]
    -> [Gap: Ad-hoc solutions (Gaussian approx, RAR, reverse KL) fail theoretically/empirically]
    -> [Solution: Fat-to-Thin Policy Optimization (FtTPO)]
        -> [Mechanism: Infinite-support proposal learns from data -> Reverse KL distills to sparse actor]
    -> [Validation: Treatment simulation (safety concentration) + MuJoCo (competitive performance)]
    -> [Limitation: Safety equated with reward; no theoretical guarantees; 2x compute overhead]
```

### ASCII Diagram — Revision Strategy Roadmap
```text
[P0: Scope novelty claims + compare with GAC/SPOT]
    -> [Impact: Prevents novelty rejection; clarifies positioning]
[P0: Add safety constraint violation metrics]
    -> [Impact: Directly validates core safety-awareness claim]
[P1: Ablate mean-copying heuristic]
    -> [Impact: Quantifies stabilization mechanism; improves reproducibility]
[P1: Clarify q-exp filtering threshold]
    -> [Impact: Enhances method transparency]
[P2: Restructure Introduction narrative]
    -> [Impact: Improves reader engagement and claim clarity]
```

### ASCII Diagram — Related-Work Taxonomy Tree (Layered)
```text
Offline RL Policy Optimization (Root)
├── Branch 1: Support Structure
│   ├── Leaf 1.1: Infinite-support policies (Gaussian, Student-t) [Standard baselines]
│   └── Leaf 1.2: Finite-support sparse policies (q-Gaussian, Sparsemax) [This paper]
├── Branch 2: Learning Paradigm
│   ├── Leaf 2.1: Single-stage actor-critic (IQL, XQL, SQL) [Baselines]
│   └── Leaf 2.2: Two-stage distillation (GAC, SPOT, FtTPO) [This paper]
└── Branch 3: Safety Handling
    ├── Leaf 3.1: Reward-encoded safety (penalty functions) [This paper]
    └── Leaf 3.2: Constraint-based safety (CPO, Lagrangian) [Future work]
```