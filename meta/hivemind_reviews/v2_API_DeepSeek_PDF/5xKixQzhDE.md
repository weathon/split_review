## Summary
# Final Review Report

## Summary

This paper proposes Hyperparameter-Calibrated Dataset Condensation (HCDC), a method for generating condensed synthetic datasets that preserve the validation-performance rankings of models with different hyperparameters or architectures. Unlike standard dataset condensation methods that match parameter-space gradients for a single fixed architecture, HCDC aligns hyperparameter-space gradients (hypergradients) computed on the original and condensed validation datasets. The method uses the implicit function theorem (IFT) with Neumann series approximation for efficient hypergradient computation, and constructs an extended search space via HPO trajectories to handle discrete hyperparameters. Experiments on image (CIFAR-10/100 with NAS-Bench-201) and graph (Cora, Citeseer, Ogbn-arxiv, Reddit) benchmarks show that HCDC substantially improves Spearman rank correlations (0.74 on CIFAR-10, 0.63 on CIFAR-100) compared to existing methods (best baseline ≤ 0.19), and accelerates NAS algorithms by 4-6x while preserving search outcome quality.

The paper addresses a practically important problem — making hyperparameter/architecture search faster via dataset condensation — and proposes a technically grounded solution with the hypergradient alignment formulation. The theoretical connection between ranking preservation and hypergradient alignment (Theorem 1) is a meaningful) is a conceptual contribution. However, several gaps limit the current version: (1) the extended search space construction relies on an unverified convergence assumption that affects Theorem 1's applicability, (2) the experimental comparison has confounds (architectural truncation, asymmetric validation set allocation) that may inflate HCDC's relative advantage, (3) the computational overhead of HCDC condensation itself is not reported, and (4) novelty claims cannot be fully verified without external literature search (deferred).

## Strengths
**S1. Well-motivated problem formulation.** The paper identifies a genuine limitation of existing dataset condensation methods — their inability to preserve performance rankings across different hyperparameters/architectures — and clearly articulates why this limits their use for hyperparameter search. The motivating observation that standard condensation can produce negatively correlated rankings is compelling.

**S2. Clean theoretical connection.** The equivalence between hyperparameter calibration (HC) and hypergradient alignment (Theorem 1) provides a principled foundation for the method. The derivation from first-order Taylor expansion to cosine distance minimization is mathematically sound and gives the method a clear optimization target. This is a genuine conceptual contribution beyond simply applying existing gradient matching ideas.

**S3. Broad experimental evaluation across modalities.** The paper evaluates HCDC on both image data (CIFAR-10/100 with NAS-Bench-201) and graph data (four benchmarks with GNN convolution filter search), demonstrating applicability across different data types. The inclusion of both grid search and gradient-based NAS (DARTS-PT, REINFORCE) searches strengthens the practical relevance.

**S4. Modular and practical design.** The decoupling of Strain (learned via standard condensation) and Sval (learned via hypergradient alignment) is a practical design choice that leverages existing condensation methods while adding targeted optimization for ranking preservation. The use of IFT and Neumann series for efficient hypergradient computation builds on established techniques, making the method implementable.

**S5. Clear empirical advantage over baselines.** The Spearman correlation improvements in Table 1 (HCDC: 0.74 vs best baseline 0.19 on CIFAR-10) are large and consistent, demonstrating that the hypergradient alignment objective effectively addresses the ranking preservation problem that standard condensation methods cannot solve.

## Weaknesses
**W1. Unverified convergence assumption for extended search space (Major).** The construction of ~Λ for discrete hyperparameters assumes that all p HPO trajectories converge to the same or equivalent optima, forming a connected set. This assumption is critical for Theorem 1's equivalence guarantee (which requires a connected and compact set) but is not empirically verified. If trajectories diverge, the theoretical foundation for hypergradient alignment may not hold in practice.

**W2. Discretization gap between theory and practice (Major).** Theorem 1 establishes equivalence between hypergradient alignment and hyperparameter calibration over a *continuous* connected set ~Λ. However, the practical objective (Eq. HCDC) evaluates alignment only at discrete sampled λ points. The gap between the continuous theoretical guarantee and the discrete practical implementation is not discussed, and no analysis is provided on how many samples are needed for the practical objective to approximate the theoretical guarantee.

**W3. Experimental confounds may inflate HCDC's advantage (Major).** (a) Architectural truncation (15→3 blocks) during search may disproportionately harm standard condensation methods that were designed for full-depth networks. (b) Baselines use a random split of their condensed data for validation, while HCDC receives a dedicated Sval optimized for ranking. This asymmetric validation set allocation gives HCDC an inherent advantage not controlled for.

**W4. Missing computational overhead reporting (Major).** The paper reports search time speedups (Table 3) but does not report the time or cost of the HCDC condensation process itself. If HCDC's condensation phase is substantially more expensive than standard condensation, the total time-to-result may be less favorable than the search speedup alone suggests.

**W5. Limited analysis of ranking errors (Minor).** The paper reports aggregate Spearman correlations but does not analyze where ranking errors occur (e.g., among similar-performing architectures vs. large-gap pairs). The relatively large standard deviation of HCDC's correlation (0.21 on CIFAR-10) suggests sensitivity to initialization that is not discussed.

**W6. Graph condensation details underspecified (Minor).** The adaptation of HCDC to graph data is described at a high level, but key details are missing: whether Sval consists of synthetic node features or selected real nodes, how the graph structure is handled, and how the hypergradient computation differs for graph neural networks.

**W7. Novelty verification deferred (System limitation).** Due to Retrieval-Disabled Mode in this run, external literature comparison cannot be performed. The novelty of the hypergradient alignment formulation relative to existing hyperparameter optimization and dataset condensation methods cannot be fully assessed without external retrieval. This is noted as a deferred manual verification requirement.

## Key Issues
### Issue 1: Extended search space connectivity assumption (Critical for Theorem 1 validity)
**Location:** Page 4 - HPO formulation challenges, Page 6 - Section 5.2 Extended Search Space
**Severity:** Major

The paper constructs ~Λ for discrete hyperparameter spaces by assuming all HPO trajectories converge to the same optima, forming a connected set. This assumption directly affects whether Theorem 1's equivalence guarantee applies. Without empirical verification (e.g., measuring trajectory endpoint distances, visualizing convergence patterns), readers cannot assess whether the theoretical foundation holds for the tested search spaces. The paper should add an empirical analysis of trajectory convergence for the NAS-Bench-201 search space and the graph convolution filter spaces.

### Issue 2: Theory-practice discretization gap (Major)
**Location:** Page 5 - Theorem 1, Eq. (HCDC)
**Severity:** Major

Theorem 1 requires hypergradient alignment over the entire continuous set ~Λ, but the practical objective only enforces alignment at discrete sampled λ points. The paper does not analyze this gap or provide guidance on how many samples are needed. This is a common issue in IFT-based methods, but it should be explicitly acknowledged and bounded.

### Issue 3: Experimental comparison confounds (Major)
**Location:** Page 7-8 - Experiments, Table 1, Table 3
**Severity:** Major

Two confounds may inflate HCDC's reported advantage: (a) architectural truncation from 15 to 3 blocks, and (b) asymmetric validation set allocation (baselines use random split, HCDC uses optimized Sval). Both should be controlled in ablation studies to verify the robustness of HCDC's ranking improvements.

### Issue 4: Missing condensation cost reporting (Major)
**Location:** Table 3, Conclusion
**Severity:** Major

The paper reports search time speedups but omits the condensation time for HCDC vs. baselines. The total time-to-solution (condensation + search) is what matters for practical adoption, and this is not provided.

### Issue 5: Unaddressed sensitivity to Strain quality (Minor)
**Location:** Algorithm 1, Section 5.1
**Severity:** Minor

HCDC keeps Strain fixed and only optimizes Sval. The quality of Sval's hypergradients depends on the model trained on Strain. If Strain is of poor quality (e.g., because the standard condensation method used to generate it is not well-suited to the data), the hypergradient alignment may be compromised. The paper does not study how the choice of SDC method for Strain affects HCDC's performance.

## Actionable Suggestions
### Suggestion 1: Verify extended search space connectivity (Must)
**Location:** Page 6 - Section 5.2
**Action:** Add an empirical analysis showing that HPO trajectories from different discrete λi converge to nearby optima in the continuously relaxed space. For NAS-Bench-201, visualize the trajectory endpoints in the continuous relaxation space and report the pairwise distance between trajectory endpoints. If convergence is not uniform, discuss how violations affect HCDC's ranking preservation and propose mitigations (e.g., weighting trajectories by convergence quality, or using a soft connectivity measure instead of hard convergence).

### Suggestion 2: Add discretization gap analysis (Must)
**Location:** Page 5 - Theorem 1 and Eq. (HCDC)
**Action:** Add a remark after Theorem 1 that the practical objective evaluates alignment at discrete sampled points, and the number of samples affects how closely the practical objective approximates the continuous guarantee. Provide guidance: "In our experiments, we sample K points per trajectory (K=10) and find that increasing beyond 20 yields diminishing returns in validation correlation. We recommend future users set K proportional to the dimensionality of ~Λ."

### Suggestion 3: Control for experimental confounds (Must)
**Location:** Page 7-8 - Experiments
**Actions:**
(a) Add an ablation experiment where all baselines receive the same total condensation budget (e.g., 50 images/class) and are allowed to allocate it between Strain and Sval as they choose (e.g., 40+10 split). This controls for the asymmetric validation set advantage.
(b) Add an experiment with full-depth architectures (15 blocks) using a larger condensation budget (e.g., 200 images/class) to verify that HCDC's ranking advantage persists without architectural truncation. If full-depth architectures cannot be trained on condensed data, explicitly state this as a limitation.

### Suggestion 4: Report condensation time overhead (Must)
**Location:** Table 3
**Action:** Add a column "Condensation Time" to Table 3 reporting the time required to generate the condensed dataset for each method (Random, DC, HCDC). Also add a "Total Time (Condensation + Search)" column. This is critical for practitioners evaluating whether HCDC's search quality improvements justify its potentially higher condensation cost.

### Suggestion 5: Analyze ranking error patterns (Nice-to-have)
**Location:** Page 8 - Image ranking results
**Action:** Add an analysis paragraph examining: (a) distribution of ranking errors across architecture pairs (are errors concentrated among similar-accuracy architectures or do they also involve large-gap pairs?), (b) correlation between Strain quality and HCDC ranking quality, (c) the Kendall tau correlation (more interpretable than Spearman for top-k selection).

### Suggestion 6: Clarify graph condensation details (Nice-to-have)
**Location:** Page 9 - Graph experiments
**Action:** Clearly state: (a) whether Sval for graph data consists of synthetic node features or real node features from the original graph, (b) whether the graph structure (adjacency matrix) is condensed or kept as the induced subgraph from selected nodes, (c) how hypergradients are computed for GNNs given the discrete graph structure.

### Suggestion 7: Bound claim language (Nice-to-have)
**Location:** Throughout
**Action:** Replace absolute comparative claims with bounded ones. For instance, "HCDC can enable faster hyperparameter search while the other condensation and coreset methods cannot" → "HCDC enables faster hyperparameter search with higher fidelity ranking than existing methods under our evaluated settings."

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)

**S1 (Problem & Domain):** "Dataset condensation reduces the computational cost of training multiple models by compressing a large dataset into a small synthetic set, but existing methods fail to preserve performance rankings across different hyperparameters and architectures, limiting their use for hyperparameter search."

**S2 (Gap):** "Standard condensation methods match parameter-space gradients for a single fixed architecture, producing condensed data that can yield negatively correlated rankings when used with different hyperparameters."

**S3 (Solution):** "We propose Hyperparameter-Calibrated Dataset Condensation (HCDC), which instead aligns hyperparameter-space gradients (hypergradients) between the original and condensed validation datasets, computed via implicit differentiation with efficient inverse Hessian approximation."

**S4 (Method Design):** "HCDC learns a synthetic validation set via hypergradient alignment while keeping a separately condensed training set fixed, enabling the condensed data to preserve the relative performance ranking of different hyperparameter choices."

**S5 (Result & Scope):** "On image (CIFAR-10/100) and graph (Cora, Citeseer, Ogbn-arxiv, Reddit) benchmarks, HCDC achieves Spearman correlations of 0.63-0.90, substantially outperforming existing condensation methods (best baseline ≤ 0.19), and accelerates neural architecture search by 4-6x while preserving search outcome quality."

### Introduction Outline (Complete)

**Paragraph 1 (The Problem — Big Picture):** 
Role: Establish stakes — hyperparameter/architecture search is computationally expensive because it requires training many models on the same large data.
Claim: Reducing this cost via data efficiency is important but current condensation methods are inadequate for search because they optimize for a single architecture.
Current defect: Opens with generic "deep learning success" statement; does not directly connect cost problem to condensation methods' limitation for search.
Transition to P2: "This failure to generalize across hyperparameters stems from a fundamental design choice in existing methods."

**Paragraph 2 (The Gap — Why Existing Methods Fail):**
Role: Explain why gradient matching for a fixed λ produces condensed data that mis-ranks architectures.
Claim: Existing methods match ∇θLtrain at a single λ; when λ varies, the gradient signal from condensed data diverges from the original, breaking ranking consistency.
Should include: Concrete example of ranking reversal (as currently present) + explanation of root cause analysis.
Transition to P3: "This observation motivates reformulating the condensation objective."

**Paragraph 3 (The Solution — Our Approach):**
Role: Present HCDC concept at intuitive level.
Claim: Ranking preservation is equivalent to hypergradient alignment; we enforce this via cosine distance minimization over an extended search space.
Should include: Brief mention of IFT/Neumann series (no more than 2 sentences), extended search space concept, and the modular Strain+Sval design.
Transition to P4: "We validate this approach across diverse settings."

**Paragraph 4 (The Evidence — Previews Results):**
Role: Summarize key empirical findings.
Claim: HCDC achieves high Spearman correlation on images and graphs, accelerates NAS by 4-6x.
Should include: Concrete numbers (0.74 Corr. on CIFAR-10, best baseline 0.19), graph results, and NAS speedup.
Transition to P5: "Our contributions are three-fold."

**Paragraph 5 (Contributions):**
Role: Explicit numbered contributions list.
Items: (1) Formulation + equivalence, (2) HCDC algorithm, (3) Experimental validation across modalities.
Maintain bounded language.

### Current Storyline vs Recommended Revision

The current introduction is structurally sound but can be improved in two ways:

1. **Front-load the problem specificity:** The first paragraph should immediately contrast "training many models for search" with "condensation methods are designed for single models" rather than opening with generic deep learning success.

2. **Add a bridging paragraph** between the gap (ranking reversal) and the solution (hypergradient alignment) that explains why gradient matching's fixed-λ limitation naturally leads to considering hypergradients. Currently the jump from "standard condensation fails for NAS" to "reformulate under HPO framework" is too abrupt.

## Priority Revision Plan
### P0 Items (Must-fix before resubmission)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P0.1 | Extended search space connectivity assumption | Add empirical verification of trajectory convergence for all tested search spaces | Validates Theorem 1's applicability; addresses a core theoretical concern | Medium (add analysis section) |
| P0.2 | Discretization gap between theory and practice | Add remark and sampling guidance after Theorem 1 | Clarifies the relationship between continuous theory and discrete practice | Low (add 2-3 sentences) |
| P0.3 | Experimental confounds (architectural truncation, asymmetric validation) | Add controlled ablation experiments | Ensures reported improvements are not artifacts of experimental design | Medium (2 additional experiments) |
| P0.4 | Missing condensation time reporting | Add condensation time and total time to Table 3 | Enables practitioners to evaluate total cost-benefit | Low (report existing data) |

### P1 Items (Should-fix for strong revision)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P1.1 | Ranking error analysis | Add analysis of error distribution and sensitivity to Strain quality | Improves understanding of when HCDC works and why | Medium |
| P1.2 | Graph condensation details | Clarify Sval representation and hypergradient computation for graphs | Improves reproducibility for graph learning community | Low (add 1 paragraph) |
| P1.3 | Claim language bounding | Replace absolute comparative claims with bounded statements | Improves scientific defensibility | Low (text edits) |

### P2 Items (Nice-to-have for quality improvement)

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P2.1 | Related work reorganization | Restructure as thematic subsections | Improves readability and positioning | Medium |
| P2.2 | Introduction narrative tightening | Front-load problem specificity, add bridging paragraph | Improves reader engagement and clarity | Medium |
| P2.3 | Conclusion with bounded findings | Restructure to validated findings → limitations → future work | Improves conclusion impact and scientific precision | Low |

### Revision Strategy Roadmap

```text
[Current manuscript]
    |
    v
[P0 Fixes - Theoretical rigor]
    ├── Verify trajectory convergence (P0.1)
    ├── Add discretization gap remark (P0.2)
    ├── Controlled ablation experiments (P0.3)
    └── Report condensation time (P0.4)
    |
    v
[P1 Fixes - Experimental depth]
    ├── Ranking error analysis (P1.1)
    ├── Graph condensation details (P1.2)
    └── Claim language bounding (P1.3)
    |
    v
[P2 Fixes - Presentation quality]
    ├── Related work reorganization (P2.1)
    ├── Introduction narrative tightening (P2.2)
    └── Conclusion restructuring (P2.3)
    |
    v
[Revised manuscript with stronger theoretical grounding,
fairer experimental comparison, and clearer presentation
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Image architecture ranking preservation | CIFAR-10/100, NAS-Bench-201 (100 archs), 50 img/class, 50 epochs, 5 seeds | Spearman Corr., Test Perf. of selected arch | HCDC achieves Corr. 0.74/0.63; baselines ≤0.19 | C1 (ranking preservation via hypergradient alignment) | Confound: architectural truncation (15→3 blocks); asymmetric validation split |
| E2 | Image NAS speedup | CIFAR-10, DARTS-PT & REINFORCE, 100 arch search space | Search time (sec), Test Perf. | HCDC: 35.5s/91.9% (DARTS-PT), Original: 229s/92.7% | C3 (faster NAS with preserved outcome) | Condensation time not reported; small search space only |
| E3 | Graph convolution filter ranking | Cora, Citeseer, Ogbn-arxiv, Reddit; 2-layer GNN, 3 compression ratios | Spearman Corr. (80 configs), Test Perf. | HCDC Corr. 0.77-0.90; best baseline ≤0.76 | C1, C2 (method works for graphs) | Graph condensation details underspecified |
| E4 | Graph NAS speedup | Ogbn-arxiv, ctrain/n=0.5%, GraphNAS search | Search time vs. Test Perf. curve | HCDC finds better architectures faster | C3 (speedup orthogonal to search strategy) | Single dataset, single compression ratio |
| E5 | Condensed data visualization | CIFAR-10, HCDC Sval samples | Qualitative (Fig. 3) | Synthetic validation images shown | Illustrative only | No quantitative evaluation of visual quality |

### Research-Theme Gap Diagnosis

1. **New Knowledge — What is genuinely learned?** The paper establishes that hypergradient alignment preserves ranking, but does not deeply analyze *why* gradient matching fails for multi-λ while hypergradient matching succeeds. A mechanistic understanding (e.g., does hypergradient alignment capture cross-architecture interactions that gradient matching misses?) would strengthen the knowledge contribution.

2. **Reproducibility/Reusability — Can others implement HCDC?** The algorithm is described but several details are left to appendices (complexity analysis, extended space construction). Missing: hyperparameter choices (K, Tθ, Tλ, ηθ, ηλ, ηS), Strain generation method for graphs, and computational environment details.

3. **Potential to Change Practice — Would practitioners adopt HCDC?** The missing condensation time reporting is a key barrier to assessing practical value. If HCDC condensation takes 10x condensation cost is 10x that is 10x more expensive than standard condensation, the total time savings may be modest. This needs clarification.

### Proposed Research Experiments

#### P0 Experiments (Must-do before resubmission)

**Exp P0.1: Trajectory Convergence Verification**
- Target Claim: "~Λ is connected via convergent HPO trajectories" (affects Theorem 1)
- Hypothesis: HPO trajectories from different discrete λ_i converge to a common region in the continuously relaxed space
- Minimal Design: For NAS-Bench-201, initialize 100 trajectories from each architecture's continuous relaxation; run gradient-based optimization on L*_optimization on L*_S(λ) for 50 steps; measure pairwise endpoint distances
- Controls/Baselines: Compare against random-walk trajectories as null distribution
- Metrics: Mean pairwise endpoint distance, proportion of trajectory pairs within epsilon-ball
- Success Criterion: >90% of trajectory pairs have endpoint distance < 0.1 (normalized)
- Estimated Cost: Low (can be computed using existing HCDC infrastructure)
- Expected Gain: Validates the core theoretical assumption

**Exp P0.2: Controlled Ablation — Validation Split Parity**
- Target Claim: "HCDC outperforms baselines in ranking preservation"
- Hypothesis: Even with matched validation set allocation, HCDC outperforms baselines
- Minimal Design: Give all methods the same budget (50 img/class total). Baselines can reserve 10 img/class as validation set. HCDC uses 40 img/class for Strain + 10 optimized Sval. Compare Corr. and Perf.
- Controls/Baselines: Random, K-Center, DC, DSA, DM with optimized vs. random validation split
- Success Criterion: HCDC still achieves Corr. > 0.6, statistically significant over next best baseline
- Estimated Cost: Medium (re-run baseline experiments with new allocation)
- Expected Gain: Removes the main experimental confound

**Exp P0.3: Condensation Time Reporting**
- Target Claim: "HCDC enables faster hyperparameter search"
- Minimal Design: Record condensation time for Random, DC, HCDC on CIFAR-10 at 50 img/class
- Report: Condensation time, Search time, Total time
- Expected Gain: Enables practitioners to evaluate total cost-benefit

#### P1 Experiments (Should-do for strong revision)

**Exp P1.1: Ranking Error Analysis**
- Target Claim: "HCDC preserves the outcome with high accuracy"
- Hypothesis: Ranking errors are concentrated among architectures with similar performance
- Design: For each method, compute Kendall tau, plot error vs. performance gap, identify whether HCDC correctly identifies top-k architectures
- Success Criterion: HCDC's top-10 architectures include the true top-3 with high probability

**Exp P1.2: Strain Quality Sensitivity**
- Target Claim: "HCDC is robust to Strain quality"
- Hypothesis: HCDC's ranking quality degrades gracefully with poorer Strain
- Design: Generate Strain using different SDC methods (DC, DSA, DM, random) and measure HCDC's resulting Corr.
- Success Criterion: HCDC's Corr. stays above 0.5 regardless of Strain method

#### P2 Experiments (Nice-to-have)

**Exp P2.1: Larger Search Space NAS**
- Test scalability claim by evaluating HCDC on a larger NAS search space (e.g., 1000+ architectures)

### Experiment Upgrade Plan

```text
[Completed Experiments]
    E1 (Image ranking) ---- P0.2 (controlled ablation) --> [Defensible ranking claim]
    E3 (Graph ranking) ---- P0.1 (trajectory convergence) --> [Validated theory]
    E2/E4 (NAS speedup) ---- P0.3 (condensation time) --> [Complete cost picture]
                                       |
                                       v
                         P1.1 (error analysis) --> [Understanding]
                         P1.2 (Strain sensitivity) --> [Robustness]
                                       |
                                       v
                         P2.1 (larger search space) --> [Scalability]
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### Final Score: 6.5 / 10

**Rationale:** The paper addresses an important and well-motivated problem with a technically grounded approach (hypergradient alignment). The empirical results show substantial improvements over existing methods. However, the score is constrained by: (1) the core theoretical assumption (trajectory convergence) is unverified, (2) experimental confounds reduce confidence in the reported advantage magnitude, (3) missing condensation cost reporting limits practical assessment, and (4) novelty cannot be fully evaluated without external retrieval. The research value contribution — a new formulation for ranking-preserving condensation — is solid, but the current evidence level supports "demonstration of feasibility" rather than "established method with verified advantages."

### Post-Revision Target: [7.5, 8.5] / 10

**Rationale:** If the P0 items are fully addressed (trajectory convergence verified, experimental confounds controlled, condensation time reported, and discretization gap clarified), the paper's theoretical grounding and empirical credibility would be substantially strengthened. The upper bound of 8.5 assumes novelty is confirmed via external literature review and the controlled experiments support the current conclusions. The lower bound of 7.5 assumes partial verification with some residual uncertainty.

### Page Coverage Audit

| Page | Annotation Count | Coverage Status | Skip Reason |
|------|-----------------|----------------|-------------|
| 1 (Abstract + Intro P1-P2) | 2 | Covered | - |
| 2 (Intro P3-P5 + Fig 1) | 1 | Covered | - |
| 3 (SDC background) | 1 | Covered | - |
| 4 (HPO formulation + challenges) | 1 | Covered | - |
| 5 (Theorem 1 + Eq. HCDC) | 1 | Covered | - |
| 6 (IFT implementation + algorithm) | 2 | Covered | - |
| 7 (Related Work + Table 1 + Exp setup) | 2 | Covered | - |
| 8 (Table 2, Table 3, image ranking, NAS speedup) | 2 | Covered | - |
| 9 (Graph experiments + Conclusion) | 2 | Covered | - |
| 10-14 (References + Appendix) | 0 | Skipped | Reference list only; appendix details not required for main-body audit |

### ASCII Diagram — Paper Structure & Evidence Map

```text
[Problem: Expensive hyperparameter search needs fast proxy]
    |
    v
[Gap: Standard condensation methods (GM at fixed λ)
     produce negatively correlated rankings across λ]
    |
    v
[Core Idea: Align hypergradients ∇λL*_T and ∇λL*_S
     instead of parameter gradients ∇θLtrain]
    |
    v
[Theoretical Justification: Theorem 1 — hypergradient
     alignment ⇔ hyperparameter ranking preservation on connected ~Λ]
    |
    v
[Implementation: IFT + Neumann series for ∇λL*;
     extended ~Λ via HPO trajectories for discrete Λ]
    |
    v
[Evidence: Image (Corr 0.74 vs ≤0.19) and graph (Corr 0.77-0.90)
     ranking preservation + NAS speedup 4-6x]
    |
    v
[Gaps: (1) ~Λ connectivity unverified, (2) discretization gap,
     (3) experimental confounds, (4) condensation cost unreported]
```

### ASCII Diagram — Related-Work Taxonomy Tree

```text
Dataset Reduction for ML Training (Root)
├── Branch 1: Coreset Selection (subset from real data)
│   ├── Leaf 1.1: Diversity-based [Aljundi 2019, Iyer 2021]
│   ├── Leaf 1.2: Distance/cluster-based [Rebuffi 2017, Chen 2010, Sener 2018]
│   └── Leaf 1.3: Forgetfulness-based [Toneva 2018, Paul 2021]
├── Branch 2: Dataset Condensation (synthetic data generation)
│   ├── Leaf 2.1: Meta-learning/bi-level [Wang 2018, Bohdal 2020, Nguyen 2020/21]
│   ├── Leaf 2.2: Gradient matching [Zhao 2020, Zhao & Bilen 2021a, Kim 2022]
│   ├── Leaf 2.3: Distribution matching [Zhao & Bilen 2021b]
│   ├── Leaf 2.4: Trajectory matching [Cazenavette 2022]
│   └── Leaf 2.5: Hypergradient alignment (HCDC - THIS PAPER)
└── Branch 3: Graph Reduction Methods
    ├── Leaf 3.1: Graph sparsification/coarsening [Loukas 2018/19, Huang 2021]
    └── Leaf 3.2 Graph condensation [Jin 2021/22, Liu 2022]
```

### ASCII Diagram — Revision Strategy Roadmap

```text
Stage 1 (P0 — Theoretical rigor)
    [Trajectory convergence analysis]
        -> Verifies ~Λ connectivity assumption
        -> Strengthens Theorem 1 applicability
    [Discretization gap remark]
        -> Clarifies theory-practice relationship
    [Controlled ablation experiments]
        -> Removes experimental confounds
    [Condensation time reporting]
        -> Enables total cost assessment

Stage 2 (P1 — Experimental depth)
    [Ranking error analysis]
        -> Understanding of failure modes
    [Graph condensation details]
        -> Reproducibility for graph community
    [Claim language bounding]
        -> Scientific defensibility

Stage 3 (P2 — Presentation)
    [Related work reorganization]
    [Introduction narrative tightening]
    [Conclusion restructuring]
        -> Reader engagement and clarity

Expected Outcome:
    Manuscript with verified theoretical assumptions,
    fair empirical comparison, and complete cost reporting
```

### Contribution-level Novelty Conclusion

**Retrieval-Disabled Mode Notice:** External literature verification is unavailable in this run (paper_search not started due to missing_base_url). Novelty/comparison conclusions are intentionally deferred and should be verified manually.

The paper's claimed contributions are:
- **C1:** Study of data condensation for hyperparameter search and equivalence between ranking preservation and hypergradient alignment.
- **C2:** HCDC algorithm using hypergradient alignment.
- **C3:** Empirical demonstration across images and graphs.

Without external retrieval, we cannot determine whether the hypergradient alignment formulation for condensation has been previously explored. The technical approach builds on known IFT and Neumann series techniques (Lorraine et al., 2020) and gradient matching (Zhao et al., 2020), so the novelty lies in the specific application to ranking-preserving condensation. A manual literature check is needed to verify that no prior work has proposed hypergradient alignment for dataset condensation.

Deferred verdict tags (preliminary assessment): The problem formulation (ranking preservation via condensation) appears novel, but the technical components (IFT, Neumann series, cosine distance matching) are individually known. The contribution is plausible as a new application-driven integration of existing techniques.