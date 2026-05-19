## Summary
This paper introduces FROND (FRactional-Order graph Neural Dynamical network), a framework that extends integer-order continuous Graph Neural Networks by incorporating Caputo fractional derivatives (order β ∈ (0,1]). The core idea is to replace the standard first-order time derivative d/dt in graph neural diffusion models with a fractional derivative D^β_t, which inherently captures the entire history of the feature evolution through a convolution integral. This introduces non-Markovian, memory-dependent dynamics into the feature propagation process.

The paper makes three main contributions: (C1) a generalized continuous GNN framework using fractional calculus that subsumes existing integer-order models (GRAND, GRAND++, GraphCON, CDE, GREAD) as special cases when β=1; (C2) a non-Markovian random walk interpretation of the linear diffusion variant (F-GRAND-l) with a proof of algebraic (Θ(t^{-β})) rather than exponential convergence to stationarity, analytically supporting oversmoothing mitigation; (C3) extensive empirical validation showing that fractional adaptations consistently outperform their integer-order counterparts across node and graph classification benchmarks, with the largest gains on tree-structured datasets.

The theoretical analysis (Theorems 1-2) is rigorous for the linear diffusion case, and the experiments are broad (10+ datasets, 5 base architectures). However, several key weaknesses are identified: the theoretical guarantees are scoped exclusively to the linear F-GRAND-l variant, computational complexity increases to O(K²) for the fractional solver, the fractal-to-β connection is asserted but only weakly supported empirically, and performance gains on standard benchmarks are modest (0.5-2%) with overlapping variances.

## Strengths
1. **Novel conceptual framework**: FROND is the first systematic framework to introduce time-fractional derivatives into continuous GNNs, generalizing a broad class of existing models (GRAND, GRAND++, GraphCON, CDE, GREAD). This is a principled mathematical extension rather than an ad-hoc architectural modification.

2. **Rigorous theoretical analysis for linear case**: Theorem 2 provides a clean result—algebraic convergence Θ(t^{-β}) vs exponential O(e^{-rt})—that formally demonstrates why fractional dynamics can mitigate oversmoothing. The connection to non-Markovian random walks (Theorem 1, Corollary 1) is elegant and provides interpretability for the memory mechanism.

3. **Comprehensive empirical validation**: The paper evaluates FROND across 10+ datasets and 5 base architectures, including standard benchmarks (Cora, Citeseer, Pubmed), tree-structured graphs (Airport, Disease), large-scale graphs (ogbn-arxiv, ogbn-products), heterophilic graphs (Roman-empire, Wiki-cooc), and graph classification (Politifact, Gossipcop). This breadth convincingly demonstrates the framework's generality.

4. **No additional training parameters**: FROND improves performance without adding trainable parameters to the backbone models—the fractional order β is a fixed hyperparameter. This is a practical advantage for deployment.

5. **Strong oversmoothing mitigation**: The empirical demonstration that F-GRAND-l maintains stable performance up to 256 layers (Table 14, Fig. 2) while GRAND-l degrades (e.g., Airport: 97.0%→94.91% vs 80.5%→53.0%) is compelling evidence of practical benefit, especially for deep GNN architectures.

6. **Open-source code and solver library**: The paper releases both the research code and a standalone torchfde library, supporting reproducibility and community adoption of fractional differential equation solvers in deep learning.

## Weaknesses
The following weaknesses are organized by severity and impact on the paper's overall contribution and validity.

**W1. Theoretical claims over-scoped relative to empirical breadth (Severity: Major, Validity Risk: High)**
The core theoretical contributions—non-Markovian random walk interpretation (Section 3.2), Theorem 1, and Theorem 2 (algebraic convergence)—are proven exclusively for the linear diffusion variant F-GRAND-l (D^β_t X = -LX). However, the paper presents these results as general properties of the FROND framework ("FROND's capability to apprehend more complex dynamics than integer-order continuous GNNs," Remark 1). The non-linear attention-based variants (F-GRAND-nl, F-CDE, F-GRAND++, F-GREAD, F-GraphCON) have no equivalent theoretical backing for oversmoothing mitigation. Their performance is supported only empirically.

**W2. Fractal-to-β connection asserted but insufficiently validated (Severity: Major, Validity Risk: Medium)**
The Introduction claims "a direct connection between the fractal dimension of these structures and the order β in fractional derivatives" (citing physics references for fractal media, not graphs). The empirical validation (Table 18, Appendix D.11) uses only 5 datasets with noisy trends—e.g., Pubmed (fractal dim=2.25) has optimal β=0.9, similar to Citeseer (fractal dim=0.62) with β=0.9. The correlation claimed ("larger fractal dimension → smaller optimal β") is not statistically tested. This central physical motivation remains speculative.

**W3. Statistical reliability of performance gains (Severity: Major, Validity Risk: Medium)**
On standard benchmarks (Cora, Citeseer, Pubmed, CoauthorCS, Computer, Photo, CoauthorPhy, ogbn-arxiv), F-GRAND-l improvements over GRAND-l are modest (0.3-1.5%). Given overlapping standard deviations (e.g., Cora: 84.8±1.1 vs 83.6±1.0), the improvements may not be statistically significant. No paired significance tests are reported. The dramatic gains on Airport/Disease are impressive but GRAND-l exhibits extremely high variance on those datasets (±9.6 on Airport), suggesting instability rather than a clear advantage.

**W4. Computational cost not adequately discussed in main text (Severity: Minor, Practical Impact: Medium)**
The fractional predictor (Eq. 17) requires O(K²) operations for K integration steps due to the full-memory summation, vs O(K) for standard neural ODE solvers. At T=64 (K=64), this is ~2000 vs 64 function evaluations. The main text does not mention this overhead, deferring it to Appendix D.6. The short memory principle reduces cost but introduces approximation error.

**W5. Valid transition probability constraint unexamined (Severity: Major, Validity Risk: High)**
The non-Markovian random walk transition (11) requires c₁ - σ^β ≥ 0 for validity (c₁=β). For β=0.1, this requires σ ≤ 10^{-10}, which is impractically small. This constraint is not discussed, and its implications for the Theorem 1 limit nσ=t are not analyzed.

**W6. Conclusion overclaims (Severity: Minor, Credibility Risk: Low)**
The conclusion states "significant advancement in graph representation learning, addressing key challenges" without bounding the scope. No limitations are mentioned in the main-text conclusion (they appear only in the appendix, p.42). The paper omits from the conclusion the limitations noted in this review: linear-only guarantees, O(K²) cost, and the need for β tuning.

## Key Issues
### Issue 1 (Critical): Theoretical oversmoothing guarantee is scope-mismatched with framework-level claims

**Location**: Page 2 - Contributions (C2), Page 6 - Theorem 2, Page 9 - Conclusion  
**Evidence**: The non-Markovian random walk interpretation (Section 3.2) and Theorem 2's algebraic convergence result are proven only for F-GRAND-l (linear diffusion: D^β_t X = -LX). The paper's framework-level claims (abstract, conclusion, contribution list) present this as a general property of FROND.  
**Risk**: A reader may incorrectly infer that all FROND variants (F-GRAND-nl, F-CDE, F-GRAND++, F-GREAD, F-GraphCON) provably mitigate oversmoothing through slow algebraic convergence. The empirical oversmoothing experiments (Section 4.3) also use only F-GRAND-l, not the nonlinear variants.  
**Fix**: (Must) Scope all theoretical claims to F-GRAND-l explicitly. Add a sentence in the contribution list, abstract, and conclusion clarifying this scope. (Nice-to-have) Provide empirical oversmoothing analysis for at least one nonlinear variant.

### Issue 2 (Major): Valid probability constraint in random walk transition undermines Theorem 1's approximation for small β

**Location**: Page 5 - Equation (11) and surrounding text  
**Evidence**: The random walk transition (11) defines P(stay at current) = c₁ - σ^β, requiring σ^β ≤ c₁ = β for validity. For β=0.1 (used in experiments: F-GRAND-nl Airport β=0.1, Table 1), this requires σ ≤ 10^{-10}. Theorem 1's limit nσ=t requires σ→0 and n→∞ simultaneously, but the practical constraint is orders of magnitude more restrictive than the "σ is assumed to be small enough" statement suggests.  
**Risk**: The theoretical connection between the random walk and F-GRAND-l may break down for the small β values used in practice, weakening the claimed theoretical justification for oversmoothing mitigation.  
**Fix**: (Must) Explicitly derive and discuss the constraint σ^β ≤ β. Provide bounds on the approximation error when this condition is violated at practical step sizes. (Nice-to-have) Provide experimental validation of the random walk approximation at different β values.

### Issue 3 (Major): Fractal-to-β connection is overstated

**Location**: Page 1-2 - Introduction (fractal motivation paragraph), Page 2 - Contributions, Page 30 (Appendix D.11)  
**Evidence**: The introduction claims "a direct connection between the fractal dimension...and the order β" citing Nigmatullin (1992) and Tarasov (2011)—references about physical fractal media, not graph datasets. The empirical evidence (Table 18, 5 datasets) shows a noisy trend (Cora fractal dim=1.22, β=0.9; Citeseer dim=0.62, β=0.9) that is not statistically tested.  
**Risk**: This is presented as a key motivation for the work (the "compelling insight" paragraph). If the connection is weak, the core motivation for why fractional calculus is specifically suited for graph data (beyond general function approximation) is diminished.  
**Fix**: (Must) Downgrade the claim from "direct connection" to "suggestive empirical trend requiring further investigation." Add statistical significance tests for the fractal dimension-β correlation. (Nice-to-have) Expand the fractal dimension analysis to more datasets.

### Issue 4 (Major): Statistical significance of empirical gains is not established

**Location**: Page 8 - Table 1, Section 4.1 Performance paragraph  
**Evidence**: On 8 of 10 datasets, F-GRAND-l's improvement over GRAND-l is within overlapping standard deviations. No paired significance tests (t-test, Wilcoxon) are reported. On Computer, GAT has ±19.0 standard deviation—suggesting unstable training that may affect baseline reliability.  
**Risk**: The paper's central empirical claim ("consistently improved performance") may not hold under rigorous statistical testing for the majority of standard benchmarks.  
**Fix**: (Must) Report paired significance tests (at least for the GRAND vs F-GRAND comparison on each dataset). Provide effect sizes and confidence intervals. (Nice-to-have) Report results over more seeds (currently appears to be 5 based on typical convention).

## Actionable Suggestions
### S1. Scope theoretical claims to the linear variant (Must, P0)
**Target**: Page 1 Abstract, Page 2 Contributions (C2), Page 6 Remark 1, Page 9 Conclusion
**Action**: Add explicit scope qualifiers. In the abstract, change "we demonstrate analytically that oversmoothing can be mitigated" to "for the linear diffusion variant, we analytically demonstrate oversmoothing mitigation." In the contribution list, add: "This theoretical result is established for the linear F-GRAND-l model; oversmoothing resistance in nonlinear variants is validated empirically."
**Expected benefit**: Prevents overclaiming by aligning the scope of theoretical claims with the scope of proofs.

### S2. Address the random walk probability constraint (Must, P0)
**Target**: Page 5, Section 3.2, around Equation (11)
**Action**: Derive and state the condition σ^β ≤ β required for valid transition probabilities. Discuss its implications: for β=0.1, σ must be ≤ 10^{-10}. Add a paragraph analyzing how this affects the approximation quality of Theorem 1 when practical step sizes are larger. Consider providing a modified transition definition that remains valid for larger σ.
**Expected benefit**: Theoretical connection between the random walk and F-GRAND-l becomes fully rigorous. Currently, the validity gap for small β values used in practice weakens an otherwise elegant theoretical contribution.

### S3. Add statistical significance testing (Must, P1)
**Target**: Section 4.1, Table 1
**Action**: Report paired t-test or Wilcoxon signed-rank test results comparing F-GRAND vs GRAND across repeated trials. Use at least 5 independent seeds with different train/val/test splits. Report Cohen's d effect sizes for each dataset comparison. Mark statistically significant improvements (p<0.05) in Table 1.
**Expected benefit**: Establishes whether the observed 0.5-2% improvements on standard benchmarks are reliable or within noise range. This directly affects the credibility of the central empirical claim.

### S4. Tone down fractal-to-β claims (Must, P1)
**Target**: Page 1-2, Introduction (fractal motivation paragraph)
**Action**: Replace "direct connection" with "theoretical motivation inspired by physical systems" or "suggestive empirical relationship." Add a sentence acknowledging that the fractal dimension-β correlation in graph data requires further validation with more datasets and statistical testing. Move the strong claim from the introduction to a more qualified statement in the experiments section.
**Expected benefit**: Aligns the paper's motivational framing with the actual evidence strength, improving scientific honesty without diminishing the interesting empirical observation.

### S5. Expand limitations section (Must, P1)
**Target**: Page 42 (Appendix, Limitations)
**Action**: Add the following limitations that are currently missing: (a) computational O(K²) cost of the fractional solver; (b) theoretical guarantees limited to linear diffusion only; (c) Theorem 2 requires strongly connected and aperiodic graphs; (d) β tuning adds hyperparameter burden and gains are modest on standard benchmarks when β≈1.
**Expected benefit**: Scientific completeness. The single current limitation (spatial fractional derivatives) is not the most important one.

### S6. Add complexity analysis to main text (Nice-to-have, P2)
**Target**: Page 7, Section 3.3 (Solving FROND)
**Action**: Add one sentence noting the O(K²) vs O(K) complexity of the fractional solver compared to integer-order ODE solvers, and reference Appendix D.6 for detailed timing.
**Expected benefit**: Practical users can make informed decisions about the cost-performance tradeoff without diving into the appendix.

### S7. Add fixed-β control experiment (Nice-to-have, P2)
**Target**: Section 4.3 (Oversmoothing) or Section 4.4 (Ablation)
**Action**: Run the oversmoothing experiment (deep networks, Fig. 2) with a fixed β (e.g., β=0.7) across all datasets, without per-dataset tuning. This tests whether the advantage comes from fractional dynamics per se or from the additional tuning flexibility.
**Expected benefit**: Clarifies the source of improvement—a key question for understanding the mechanism.

## Storyline Options + Writing Outlines
### Current Storyline Analysis

The current introduction (Pages 1-2) has this structure:
- P1: GNNs have excelled → many GNN types → continuous GNNs based on ODEs
- P2: Integer-order continuous GNNs limited to β=1 or 2 → fractional calculus works in physics → fractional derivatives consider history
- P3: We introduce FROND framework → generalizes integer-order derivative → assures equivalent performance
- P4: Distinction from Maskey et al. and Liu et al.
- P5: Fractal graph datasets → FDEs describe fractal dynamics → optimal β may reveal fractality
- P6: Main contributions (C1-C3)

**Problems**: (a) P1 is a literature list without a clear gap statement; (b) The physical motivation (fractal media) appears in P5 after the framework is already introduced; (c) The gap (Markovian limitation of integer-order ODEs) is only implicit; (d) P5's strong claim (fractal-β connection) is motivation but presented as a contribution.

### Recommended Storyline (Option A: "Memory Matters")

**Abstract Outline (S1-S5)**:
- S1 (Problem): Continuous GNNs model node feature evolution via ODEs, but ODEs enforce Markovian dynamics—updates depend only on current state.
- S2 (Gap): Real-world graphs with long-range dependencies and fractal-like structures require memory-aware dynamics.
- S3 (Proposal): We introduce FROND, replacing integer-order with Caputo fractional derivatives (order β) to incorporate historical dependence.
- S4 (Theory): For the linear diffusion variant, we prove algebraic convergence Θ(t^{-β}) vs exponential, analytically demonstrating oversmoothing mitigation.
- S5 (Empirics): FROND variants based on 5 architectures consistently outperform integer-order counterparts across 10+ datasets, with strongest gains on tree-structured graphs.

**Introduction Outline (P1-P5)**:

P1: **Define the problem clearly** — "Graph neural networks achieve state-of-the-art on many tasks but suffer from oversmoothing at depth. Continuous GNNs address this through ODE-based feature propagation. However, all existing continuous GNNs use integer-order derivatives (β=1 or 2), which assume feature updates depend only on the instantaneous state—a Markovian assumption."

P2: **State the limitation precisely** — "This Markovian assumption is restrictive for several reasons. First, [argument: graphs with long-range dependencies need memory]. Second, [argument: many real-world graphs have fractal structure where dynamics are better described by fractional equations]. Third, [argument: the connection between graph structure and optimal dynamics may require learnable memory depth.]"

P3: **Bridge to fractional calculus** — "Fractional calculus generalizes derivative order to any real β, with the Caputo derivative naturally integrating the function's entire history. This provides a principled mathematical framework for memory-dependent dynamics."

P4: **Introduce FROND** — "We propose FROND, which replaces d/dt with D^β_t in continuous GNN dynamics. The key properties are: (i) β=1 recovers existing models; (ii) β<1 introduces controllable memory; (iii) the framework adds no training parameters."

P5: **Preview contributions** — Explicit contributions with scope: (C1) FROND framework; (C2) theoretical analysis for linear diffusion + empirical oversmoothing validation; (C3) comprehensive experiments across 5 base architectures.

### Alternative Storyline (Option B: "From ODE to FDE")
P1: ODE-based continuous GNNs and their limitations
P2: Fractional calculus as a natural extension
P3: FROND framework and model examples
P4: Theoretical analysis (memory interpretation via random walk)
P5: Empirical evidence
This is closer to the current structure but with a clearer gap statement in P1.

### Recommended Choice: Option A
Option A better aligns with the three alignment checks:
- **Problem alignment**: Clearly states Markovian limitation → FROND with fractional derivative addresses it directly
- **Variable alignment**: Core concept (fractional derivative β) appears as the main method variable throughout
- **Contribution-evidence alignment**: Theoretical claim (C2) scoped to linear variant; empirical evidence supports broader applicability

## Priority Revision Plan
```text
ASCII Diagram — Revision Strategy Roadmap
[P0: Claim overreach (theoretical scope)]
    -> Fix: Scope all theoretical claims to F-GRAND-l explicitly
    -> Sections affected: Abstract, C2, Conclusion
    -> Expected: Claims become defensible, no overpromising

[P0: Random walk probability constraint]
    -> Fix: Derive σ^β ≤ β condition, add analysis
    -> Sections affected: Section 3.2, Eq. (11)
    -> Expected: Theory becomes fully rigorous

[P1: Statistical significance]
    -> Fix: Add paired tests, effect sizes
    -> Sections affected: Section 4.1, Table 1
    -> Expected: Empirical claims become statistically grounded

[P1: Fractal-to-β overstatement]
    -> Fix: Downgrade "direct connection" to "suggestive trend"
    -> Sections affected: Introduction, Appendix D.11
    -> Expected: Motivation honest, no overclaim

[P1: Expand limitations]
    -> Fix: Add missing limitations (cost, scope, β tuning)
    -> Sections affected: Limitations section (p.42)
    -> Expected: Scientific transparency

[P2: Complexity discussion in main text]
    -> Fix: Add one sentence on O(K²) cost
    -> Sections affected: Section 3.3
    -> Expected: Reader informed of practical tradeoff

[P2: Fixed-β control experiment]
    -> Fix: Add experiment with fixed β across datasets
    -> Sections affected: Section 4.3 or 4.4
    -> Expected: Clarifies source of improvement
```

### Prioritized Action Items

**P0 (Must fix, pre-publication)**:
1. Scope theoretical claims: Revise Abstract, C2, Remark 1, Conclusion to explicitly state that the random walk interpretation and Theorem 2 apply to the linear F-GRAND-l variant only. (Est. effort: 2 hours for text changes)
2. Fix random walk constraint: Derive σ^β ≤ β condition, analyze implications for small β, and add a paragraph in Section 3.2. (Est. effort: 1 day for analysis + writing)

**P1 (Should fix before final submission)**:
3. Add statistical significance: Run paired tests (t-test or Wilcoxon) for all F-GRAND vs GRAND comparisons. Report in Table 1 with markers. (Est. effort: 2 days for re-running experiments)
4. Tone down fractal claims: Replace "direct connection" with "suggestive empirical trend" in Introduction. Add qualifications in Appendix D.11. (Est. effort: 1 hour)
5. Expand limitations: Add 4 missing limitations to the Limitations section. (Est. effort: 1 hour)

**P2 (Nice-to-have)**:
6. Add O(K²) complexity note in main text Section 3.3. (Est. effort: 15 minutes)
7. Fixed-β control experiment. (Est. effort: 1 day of computation)

## Experiment Inventory & Research Experiment Plan
### A. Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 (Table 1) | F-GRAND outperforms GRAND on node classification | 10 datasets, random splits, F-GRAND-l/nl vs GRAND-l/nl, GCN, GAT, HGCN, GIL | Accuracy (%) | F-GRAND-l best on 8/10 datasets; dramatic gains on Airport/Disease | C3 (compatibility) | No significance tests; variance overlap on many datasets |
| E2 (Table 2) | F-GRAND outperforms GRAND on graph classification | Fake-NewsNet (POL, GOS), 3 feature types | Accuracy (%) | F-GRAND-l best on 5/6 settings | C3 (compatibility) | Only 2 datasets; small improvement on GOS |
| E3 (Fig 2, Table 14) | F-GRAND mitigates oversmoothing at depth | Cora, Citeseer, Airport; depths 4-256 layers | Accuracy (%) | F-GRAND-l stable up to 256 layers; GRAND-l degrades | C2 (oversmoothing) | Only F-GRAND-l tested; nonlinear variants not included |
| E4 (Table 3, 15) | β ablation: effect of fractional order | Cora, Airport; β∈[0.1, 1.0] | Accuracy (%) | Smaller β better for Airport; larger β better for Cora | C2 (memory tuning) | Only 2 datasets in main text |
| E5 (Table 4) | F-CDE outperforms CDE on heterophilic graphs | 6 large heterophilic datasets | Accuracy (%) | F-CDE improves on 5/6 datasets | C3 (compatibility) | F-CDE ties CDE on 'Questions' dataset |
| E6 (Table 7) | Scalability on ogbn-products | ogbn-products, mini-batch (GraphSAINT) | Accuracy (%) | F-GRAND-l 77.25% vs GRAND-l 75.56% | C3 (scalability) | Falls short of GraphSAGE (78.29%) |
| E7 (Table 8) | Solver variant comparison | Cora, Airport; Predictor, PC, Short Mem, L1 | Accuracy (%) | Variants perform comparably; Short Mem slightly worse on Cora | Method validation | Only 2 datasets; limited insight into numerical accuracy |
| E8 (Table 16) | Adversarial robustness | Cora, Citeseer; Metattack 0-25% | Accuracy (%) | F-GRAND-nl more robust than GRAND-nl at high perturbation | Robustness | Only 2 datasets; specific attack only |
| E9 (Tables 19-25, Appx E) | FROND on other backbones (GRAND++, GREAD, GraphCON) | Various datasets per backbone | Accuracy (%) | FROND variants consistently outperform integer-order counterparts | C3 (general applicability) | Gains vary; some ties |

### B. Research-Theme Gap Diagnosis

**What is missing from the completed experiments:**

1. **Causal mechanism evidence**: The paper attributes gains to "memory-dependent dynamics" and "slow algebraic convergence," but no experiment directly measures whether the FROND solver actually produces different (more history-dependent) feature trajectories than the integer-order solver. A feature trajectory similarity analysis is missing.

2. **Computational cost tradeoff**: While Appendix D.6 reports timing, there is no experiment showing the accuracy-vs-cost Pareto frontier for different β values and solver variants across multiple datasets.

3. **Hyperparameter sensitivity**: β tuning is central to the method, but there is no analysis of how sensitive results are to β misspecification (e.g., using β=0.7 when optimal is 0.5).

4. **Nonlinear variant theory**: No empirical evidence that the oversmoothing claims extend to attention-based FROND variants.

### C. Proposed Research Experiments (P0/P1/P2)

**P0 Experiment: Fixed-β control for oversmoothing**
- Target Claim: C2 (Fractional dynamics inherently mitigate oversmoothing)
- Hypothesis: The advantage persists even without dataset-specific β tuning
- Design: Repeat oversmoothing experiments (Fig. 2) with β=0.7 fixed across all datasets and depths, without per-dataset optimization
- Controls: Same as current oversmoothing setup (fixed splitting, basic predictor)
- Metrics: Accuracy vs depth curves; compare to GRAND (β=1) and tuned-β F-GRAND
- Success Criterion: Fixed β=0.7 F-GRAND-l consistently outperforms GRAND-l at depths >16
- Estimated Cost/Time: ~1 day (reuse existing code)
- Expected Gain: Directly tests whether the benefit comes from fractional dynamics or β tuning

**P1 Experiment: Feature trajectory analysis**
- Target Claim: C2 (Memory-dependent dynamics)
- Hypothesis: F-GRAND-l with β<1 produces feature trajectories that differ qualitatively from GRAND-l (β=1), especially in early-time behavior
- Design: Compute feature trajectories X(t) for t=0..T at fixed intervals. Measure (a) cosine similarity between successive time steps, (b) total variation distance from final converged state, (c) effective memory (autocorrelation of feature changes)
- Controls: Same initial features, same graph, same F operator, only β varies
- Metrics: Trajectory smoothness, convergence speed, memory length
- Success Criterion: β<1 shows slower convergence, higher autocorrelation, and non-smooth early trajectories
- Estimated Cost/Time: ~2 days
- Expected Gain: Provides mechanistic evidence for the claimed memory effects, beyond just accuracy numbers

**P2 Experiment: β sensitivity and misspecification analysis**
- Target Claim: Practical usability of FROND
- Hypothesis: The method is not overly sensitive to β misspecification
- Design: For Cora, Citeseer, Airport, and 2 heterophilic datasets, run F-GRAND-l with β = optimal − 0.2, optimal − 0.1, optimal, optimal + 0.1, optimal + 0.2. Report accuracy degradation from optimal
- Controls: Same hyperparameters except β
- Metrics: Accuracy drop from optimal β; rank correlation between β and accuracy
- Success Criterion: Accuracy drop < 1% when β is within 0.1 of optimal
- Estimated Cost/Time: ~1-2 days
- Expected Gain: Guides practitioners on β tuning effort required for deployment

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5/10**

This score reflects the following assessment:

- **Research Value & Novelty (7/10)**: The introduction of time-fractional derivatives into continuous GNNs is a genuinely novel conceptual contribution with good theoretical grounding for the linear case. The framework's generality (subsuming 5+ existing models) adds value. However, novelty is partially tempered by the fact that fractional calculus is a well-established mathematical tool, and its application to GNNs follows a relatively direct path (replacing d/dt with D^β_t in existing ODE-based models). The fractal-to-β connection contribution is interesting but unvalidated.

- **Validity & Soundness (6/10)**: The theoretical analysis is sound for the linear variant but scoped more narrowly than claimed. The random walk analysis has an unexamined validity constraint (σ^β ≤ β). Empirical soundness is weakened by the absence of statistical significance testing—many gains overlap with standard deviations. The oversmoothing experiments are convincing but only cover the linear variant.

- **Reproducibility & Completeness (7/10)**: Code is provided, and the experimental setup is clearly described. The FDE solver is open-sourced. Hyperparameters are partially specified (with code). However, key implementation details (e.g., exact number of random seeds, β search procedure) could be clearer.

- **Writing & Presentation (6/10)**: The paper is generally well-written but has significant overclaiming issues (scope of theoretical results, fractal-β connection). The introduction could be better organized with a clearer gap statement. The conclusion omits necessary limitations.

**Post-Revision Target: [7.5, 8.0]/10**

If the authors address the P0 and P1 items (scope theoretical claims, fix random walk constraint, add significance tests, tone down fractal claims, expand limitations), the paper would reach 7.5-8.0/10. The core contribution is solid, and the main issues are about claim scoping and evidence rigor rather than fundamental flaws.

### Page Coverage Audit

| Page | Annotation Count | Coverage Status | Notes |
|------|-----------------|----------------|-------|
| 1 (Abstract + Intro P1-P3) | 3 | Covered | Abstract scope; Intro P1 narrative; Intro P2 physics bridge |
| 2 (Intro P4-P6 + Prelim) | 3 | Covered | P4 distinction; P5 fractal claim; C2 scope; Prelim |
| 3 (Prelim cont.) | 1 | Covered | Laplacian notation clarity |
| 4 (FROND Framework) | 1 | Covered | Solution regularity for β<1 |
| 5 (Random Walk Model) | 1 | Covered | Valid probability constraint |
| 6 (Theorems 1-2) | 1 | Covered | Graph assumptions for Theorem 2 |
| 7 (Solvers) | 1 | Covered | Computational complexity O(K²) |
| 8 (Results Table 1) | 1 | Covered | Statistical significance |
| 9 (Graph CLS, Oversmooth, Ablation, Conclusion) | 3 | Covered | β-tuning asymmetry; Conclusion overclaim |
| 10-17 (References) | 0 | Skipped | Reference list, non-substantive |
| 18-41 (Appendices A-E) | 0 | Skipped | Supplementary material; substantive claims checked |
| 42 (Limitations + Broader Impact) | 1 | Covered | Missing limitations |
| **Total** | **16** | | |

**Skipped paragraphs**: Reference pages (10-17) are non-substantive. Appendix materials (18-41) are supplementary derivations and additional results; key claims from appendices are cross-referenced in main-text annotations. All substantive paragraphs in Abstract, Introduction, Method, Experiments, and Conclusion are covered.