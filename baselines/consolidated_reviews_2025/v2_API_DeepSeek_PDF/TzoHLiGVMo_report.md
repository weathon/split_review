## Summary
This paper presents ODEFormer, a transformer-based model for symbolic regression of multidimensional ordinary differential equation (ODE) systems from observed trajectory data. The model is an encoder-decoder transformer (86M parameters, asymmetric 4-layer encoder / 16-layer decoder) pre-trained on 50M synthetically generated ODE examples. It takes as input a noisy, irregularly sampled trajectory and outputs the symbolic form of the ODE's right-hand side in prefix notation. The paper introduces ODEBench, a curated benchmark of 63 real-world ODE systems (1D-4D). Experiments on synthetic data, the Strogatz dataset, and ODEBench show that ODEFormer achieves competitive or superior reconstruction and generalization accuracy compared to existing methods (genetic programming, SINDy, ProGED), with substantially faster inference (seconds vs. minutes) and better robustness to noise and subsampling. The conclusion honestly discusses limitations including restriction to first-order ODEs, need for full state observability, difficulty with chaotic systems, and single-trajectory inference.

**Core contribution:** Extending transformer-based symbolic ODE inference from univariate to multivariate systems, with a carefully designed data generation pipeline and a new benchmark.

**Novelty note:** External literature verification was not available in this run (Retrieval-Disabled Mode). Novelty claims are marked as deferred manual verification in the relevant sections below.

## Strengths
1. **Timely and well-motivated problem.** The paper addresses the important and challenging task of inferring symbolic ODEs from observational data, which has broad applications across scientific disciplines. The distinction between functional SR and dynamical SR is clearly motivated.

2. **Comprehensive experimental evaluation.** The evaluation spans synthetic data, the existing Strogatz benchmark, and the newly introduced ODEBench (63 ODEs, 1D-4D), with multiple noise levels (σ=0 to 0.05), subsampling rates (ρ=0, 0.5), and two evaluation protocols (reconstruction and generalization). Comparison against 12 baseline methods is thorough.

3. **Honest limitation discussion.** The conclusion candidly discusses four specific limitations (first-order only, full observability required, struggles with chaos, single-trajectory), which is refreshingly transparent compared to many ML papers. The final sentence positioning ODEFormer as a hypothesis generator is appropriately cautious.

4. **Practical inference speed.** After one-time pre-training, ODEFormer produces predictions in seconds versus minutes for most baselines. This practical advantage is substantial for exploratory scientific analysis where researchers may need to test many candidate systems.

5. **Methodologically sound architecture choices.** The asymmetric encoder-decoder design (4/16 layers), the removal of positional embeddings (since time is tokenized), and the embedding module for variable-dimensionality inputs are well-reasoned adaptations of the standard transformer to the dynamical SR task.

6. **Valuable new benchmark.** ODEBench fills a gap in the dynamical SR evaluation landscape by providing a larger, more diverse, and better-integrated collection of ODE systems than the previously available Strogatz dataset.

## Weaknesses
1. **Data generation filtering biases (Major).** The 90% probabilistic discard of low-oscillation systems is a strong heuristic with no sensitivity analysis. The training distribution may substantially differ from the natural ODE distribution, and the effect on generalization is not characterized.

2. **Reconstruction-based candidate selection (Major).** The decoding strategy selects candidates based on reconstruction R2, but the paper's own results (Appendix G) show reconstruction and generalization are not well-correlated. This selection criterion may systematically favor overfitting solutions.

3. **Statistical rigor gaps (Moderate).** Key experimental results (Figure 3 ablation study, Figure 4/5 comparisons) lack confidence intervals, error bars, or significance tests. The reader cannot assess the reliability of reported trends.

4. **Inference-time rescaling vulnerability (Moderate).** The normalization xi(t) -> xi(t)/xi(t0) fails when any component of the initial condition is zero, which occurs in benchmark systems. This issue is not discussed.

5. **"First" claim scope (Moderate).** The paper claims to be "the first transformer able to infer multidimensional ODE systems" but the closely related NSODE (Becker et al. 2023) already demonstrated transformer-based ODE inference. The novelty lies specifically in the multidimensional extension, which should be stated more precisely.

6. **Training distribution vs. real-world gap (Moderate).** The paper does not discuss how well the synthetic training distribution (random operator trees with specific priors) matches real-world ODE structure. Performance on out-of-distribution systems may degrade unpredictably.

7. **Constant optimization fragility (Minor).** The optional BFGS refinement step assumes predicted constants need only slight refinement, but no analysis of optimization success rate or sensitivity is provided.

## Key Issues
### Issue 1: Data generation filtering bias (Major, Validity Risk: Medium)
The filtering heuristic discards 90% of rapidly converging systems without sensitivity analysis. This creates an unknown selection bias in the training distribution. The paper should analyze how varying the filtering probability affects downstream performance and report the composition of the final training set by dynamical regime (divergent, oscillatory, convergent).

### Issue 2: Candidate selection metric misalignment (Major, Validity Risk: High)
Using reconstruction R2 as the selection criterion for beam sampling candidates is problematic because the paper demonstrates that reconstruction and generalization (symbolic recovery) are not well correlated. This means the selection metric may systematically favor symbolically incorrect solutions that happen to fit the observed trajectory. The paper should evaluate alternative selection criteria (e.g., trajectory prediction on held-out time segments, complexity-penalized scores) and report how selection strategy affects generalization accuracy.

### Issue 3: Zero-initial-condition rescaling failure (Moderate, Reproducibility Risk: Medium)
The inference-time rescaling `xi(t) -> xi(t)/xi(t0)` is undefined when xi(t0)=0, which occurs in benchmark ODEs. This could silently affect evaluation results. The paper should either modify the normalization (adding epsilon, using max-value scaling) or explicitly exclude cases where the transformation is ill-defined.

### Issue 4: Statistical evidence gaps (Moderate, Confidence Risk: Medium)
Missing variance/confidence information across key experimental figures (Figure 3, 4, 5) prevents readers from assessing the reliability of reported performance differences. Adding bootstrap confidence intervals or standard deviations from multi-seed runs would substantially strengthen the empirical claims.

### Issue 5: "First" claim without external verification (Moderate, Novelty Clarity Risk)
The paper claims to be "the first transformer" for multidimensional ODE inference. While the comparison with Becker et al. (2023) is provided, external literature verification was unavailable in this run. The claim should be scoped more precisely to "first transformer for *multidimensional* dynamical SR" with an explicit acknowledgment of the need for community verification.

## Actionable Suggestions
### Must-fix items (publication-critical)

1. **Fix rescaling normalization** (Page 6, Inference-time rescaling). Replace `xi(t) -> xi(t)/xi(t0)` with `xi(t) -> xi(t) / max(epsilon, |xi(t0)|)` or use max-absolute-value normalization over the trajectory. Provide a brief analysis of how many benchmark ODEs have zero-valued initial components and whether this affected results.

2. **Report statistical significance** (Figure 3, 4, 5). Add bootstrap confidence intervals (±95%) or error bars to ablation plots. Report the number of evaluation seeds used and variance across runs.

3. **Justify or replace candidate selection criterion** (Page 5, Decoding strategy). Provide an ablation comparing selection based on: (a) reconstruction R2 (current), (b) held-out time segment R2, (c) complexity-penalized score. Report whether alternative selection improves generalization accuracy.

4. **Document training set composition after filtering** (Page 4, Filtering data). Report the distribution of ODE types in the final training set (divergent, convergent, oscillatory) and the effective discard rate. Perform a sensitivity analysis with different filtering probabilities (e.g., 50%, 70%, 90%) on a small validation set.

### Nice-to-have items (quality improvement)

5. **Add distribution-shift limitation** (Page 9, Conclusion). Add a fifth limitation about the gap between synthetic training distribution and real-world ODE structure.

6. **Analyze BFGS optimization success rate** (Appendix D). Report the fraction of cases where constant optimization improves vs. degrades performance, with statistics across noise levels.

7. **Improve abstract precision** (Page 1). Replace "first transformer" with "first transformer for multidimensional systems" and replace "consistently outperforms" with a more specific description of the advantage pattern (best on average, especially under noise/subsampling).

8. **Add multi-trajectory failure analysis** (Page 9). Briefly analyze why logit aggregation experiments for multiple trajectories did not work — was it a mismatch in decoder conditioning or insufficient trajectory diversity?

## Storyline Options + Writing Outlines
### Current Storyline Assessment
The current introduction follows a: Big Picture (ML for science) → Black-box limitation (NODE) → Symbolic regression alternative → Functional vs dynamical SR distinction → Contributions → Problem setting. This structure is functional but the first two paragraphs are somewhat generic, and the key differentiation (multidimensional vs. prior univariate transformer approaches) arrives relatively late.

### Recommended Storyline: "Problem→Gap→Idea→Evidence→Contribution"
We recommend restructuring the introduction into a tighter 4-paragraph narrative:

**P1: Concrete scientific problem.** Start directly with the challenge of inferring ODEs from trajectory data, not with general ML enthusiasm. State: "Many scientific disciplines rely on modeling systems of interacting variables via ordinary differential equations. A key bottleneck is discovering these ODEs from observational data — a task known as dynamical symbolic regression." This establishes stakes within two sentences.

**P2: Why prior approaches fall short.** Contrast: (a) NODE produces black-box models, (b) GP-based SR requires per-system optimization and finite-difference derivatives (which amplify noise), (c) SINDy is limited to linear combinations of prespecified basis functions, (d) Existing transformer approaches (Becker et al. 2023) are restricted to univariate systems. End with: "A method that can infer multidimensional symbolic ODEs from noisy, irregularly sampled data in a single forward pass remains an open challenge."

**P3: Our solution.** Introduce ODEFormer as a transformer pretrained on 50M synthetic ODEs that handles multidimensional systems (up to D=6) with an embedding module for variable-dimensionality inputs. State the key technical insight: the model learns to map directly from observed trajectories to symbolic expressions without needing derivative approximations.

**P4: Results and contributions.** Summarize key empirical findings: higher average accuracy than 12 baselines, robustness to noise/subsampling, inference in seconds vs minutes, and the new ODEBench benchmark.

### Abstract Outline (Complete)

**S1 (Problem):** Inferring symbolic ordinary differential equations from observed trajectory data is a key challenge for scientific discovery, particularly for multidimensional systems where existing methods require separate optimization or finite-difference derivative approximations.

**S2 (Gap):** Prior transformer-based symbolic regression has been limited to univariate scalar-valued functions or single-variable ODEs, leaving multidimensional systems unexplored.

**S3 (Method):** We introduce ODEFormer, an encoder-decoder transformer pre-trained on 50M synthetic ODEs that takes noisy, irregularly sampled multivariate trajectories as input and outputs the symbolic form of the governing ODE.

**S4 (Results):** On two benchmarks — the existing Strogatz dataset and the newly curated ODEBench (63 systems, 1D-4D) — ODEFormer achieves higher average accuracy than 12 baseline methods, particularly under noise and subsampling, while reducing inference time from minutes to seconds.

**S5 (Impact):** We release our code, model weights, and ODEBench to facilitate reproducible research and practical application of symbolic ODE discovery.

### Introduction Outline (Complete)

**Paragraph 1 — Problem and stakes:**
Role: Establish the practical importance of discovering ODEs from data. Avoid generic ML enthusiasm; instead start directly with: "Discovering the governing equations of dynamical systems from observational data is a fundamental problem across physics, biology, and engineering." Then state the core difficulty: we observe only trajectories, not the underlying function f in dx/dt = f(x).

**Paragraph 2 — Prior work and limitations:**
Role: Survey prior approaches (NODE, SINDy, GP-based SR, transformer-based SR) and explain why none solves multidimensional dynamical SR end-to-end. Key transition: "While transformers have shown promise for symbolic regression of scalar functions and univariate ODEs, extending them to multidimensional ODE systems requires addressing three challenges: variable-dimensionality inputs, scalable data generation for stable multi-dimensional dynamics, and evaluation protocols that assess symbolic recovery beyond reconstruction accuracy."

**Paragraph 3 — Proposed approach:**
Role: Present ODEFormer at a high level. State the three key design choices: (i) embedding module with zero-padding to handle variable dimensions, (ii) large-scale synthetic data generation with filtering heuristics, (iii) inference-time rescaling for arbitrary time ranges and initial conditions. Emphasize that the model requires no derivative approximations and no per-system optimization after pretraining.

**Paragraph 4 — Contributions and results:**
Role: Explicitly list contributions and preview key results. State: (1) first transformer for multidimensional dynamical SR, (2) ODEBench benchmark, (3) superior average accuracy and robustness on two benchmarks. Include specific numbers: "On ODEBench, ODEFormer achieves X% reconstruction accuracy at σ=0.02 vs. Y% for the best baseline, with inference taking seconds rather than minutes."

## Priority Revision Plan
### P0: Must address before re-submission

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P0 | Candidate selection metric (Key Issue 2) | Compare reconstruction R2 vs. held-out-segment R2 vs. complexity-penalized selection; report delta in generalization accuracy | High — directly affects reported performance validity | Medium (adds one experiment, re-run inference) |
| P0 | Rescaling normalization (Key Issue 3) | Fix xi(t)/xi(t0) to handle zero initial conditions | High — affects evaluation correctness | Low (modify one normalization function) |
| P0 | Statistical evidence (Key Issue 4) | Add confidence intervals to Figure 3 and bootstrap variance to Figures 4-5 | Moderate — improves reader trust in conclusions | Low (computational, from existing results) |

### P1: Important improvements

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P1 | Data filtering bias (Key Issue 1) | Report final training composition; sensitivity analysis on filtering probability | Moderate — clarifies training distribution | Medium (re-train with different thresholds) |
| P1 | "First" claim precision | Reword abstract and contributions to specify "multidimensional" scope | Moderate — improves defensibility | Low (text edit) |
| P1 | Distribution-shift limitation | Add fifth limitation about synthetic-to-real gap (see annotation on Page 9) | Moderate — improves honesty | Low (text edit) |

### P2: Quality polish

| Priority | Issue | Action | Expected Impact | Effort |
|----------|-------|--------|-----------------|--------|
| P2 | BFGS optimization analysis | Report success rate of constant optimization per noise level | Minor — documents engineering detail | Low (compute from existing logs) |
| P2 | Multi-trajectory failure analysis | Add brief analysis of why logit aggregation failed | Minor — guides future work | Low (text edit) |
| P2 | Abstract revision | Tighten to 5-sentence structure (see Storyline Options section) | Minor — improves first impression | Low (text edit) |

```text
ASCII Diagram — Revision Strategy Roadmap
[P0: Rescaling fix] → [P0: Selection metric ablation] → [P0: Add error bars]
       ↓                        ↓                         ↓
[Validity protected]    [Accuracy claims justified]  [Reader confidence up]
       ↓                        ↓                         ↓
              [P1: Data filtering analysis] → [P1: Claim scoping]
                           ↓                          ↓
              [Training dist. understood]    [Novelty clear]
                           ↓
              [P2: BFGS analysis + Abstract polish]
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 | Synthetic ablation (Fig 3) | 10,000 test samples from training distribution; vary dimension, operators, points | Accuracy (% R2>0.9) | Performance degrades with dimension/operators; insensitive to #points | Model scaling properties | No error bars or CI |
| E2 | Reconstruction on Strogatz (Fig 4a) | 7 ODEs × 4 ICs; σ ∈ {0..0.05}, ρ ∈ {0,0.5} | Accuracy, complexity, time | ODEFormer best on average; competitive with PySR on clean data | Superior average accuracy | Small benchmark (28 samples) |
| E3 | Reconstruction on ODEBench (Fig 4b) | 63 ODEs × 2 ICs; same noise/subsampling | Accuracy, complexity, time | ODEFormer best on average; ODEFormer(opt) sometimes better | ODEBench utility; robustness | No per-system difficulty analysis |
| E4 | Generalization on ODEBench (Fig 5) | Same as E3 but new initial condition | Accuracy (% R2>0.9) | Half drop vs reconstruction; ODEFormer best on avg | Generalization is harder; selection metric matters | No analysis of which systems fail |
| E5 | Missing data chunks (Appendix F) | Strogatz; drop intervals [T0,T1] | Accuracy, median R2 | ODEFormer robust to missing intervals | Robustness to irregular gaps | Limited to Strogatz (small N) |
| E6 | Cross-dataset comparison vs NSODE (Appendix H.2) | Textbook, Classic, Large datasets from Becker et al. | median R2, accuracy | Similar to NSODE; slightly lower accuracy on Large | Cross-distribution generalization | NSODE not tested on multivariate |

### Research-Theme Gap Diagnosis

- **New knowledge claim (moderate support):** The paper demonstrates that transformer-based symbolic regression can be extended to multidimensional ODEs. This is supported by experiments on synthetic data and ODEBench. However, the extent to which this generalizes to *truly novel* real-world systems (outside the curated benchmark) remains unclear.
- **Reproducibility (good):** Code, model weights, and benchmark are publicly released, which is excellent. The data generation procedure is described in detail.
- **Impact on practice (potential but unvalidated):** The paper's claim of "hypothesis generation across the sciences" is plausible but unvalidated — no real-world scientific discovery case study is provided.

### Proposed Research Experiments (P0/P1/P2)

| Exp ID | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Quality Gain |
|--------|-------------|------------|---------------|-------------------|---------|------------------|-----------|--------------|
| R1 (P0) | Candidate selection bias (Key Issue 2) | Replacing reconstruction R2 with held-out-segment R2 improves generalization accuracy | Compare 3 selection strategies on ODEBench: (a) recon R2 (current), (b) held-out last 20% time, (c) complexity-penalized (R2 - λ*complexity) | Same beam candidates, same noise levels | Generalization accuracy (R2>0.9) | >=5% absolute improvement over current selection | 1-2 GPU-hours | High — validates core evaluation |
| R2 (P0) | Statistical evidence (Key Issue 4) | Reported trends hold with CI | Bootstrap 1000 samples from existing eval outputs; report 95% CI | N/A (analysis-only) | CI width for accuracy at each config | CI width < 10% for main comparisons | <1 hour (analysis) | High — adds rigor |
| R3 (P1) | Filtering bias (Key Issue 1) | Performance is robust to filtering probability | Train 3 models with filtering probability 50%, 70%, 90%; compare on ODEBench reconstruction | Same architecture, same training data volume | Accuracy (R2>0.9) | Difference between conditions < 5% | ~9 GPU-days (3 runs × 3 days) | Medium — clarifies training bias |
| R4 (P1) | Distribution-shift robustness | ODEFormer generalizes to OOD systems | Create OOD test set: systems with max tree depth >6, operators outside training set (tanh, exp), coefficient ranges [0.001, 100] | Same model (no retraining) | Accuracy (R2>0.9) for in-distribution vs. OOD | OOD accuracy within 15% of in-distribution | 1-2 days (curation + eval) | Medium — bounds generalization |
| R5 (P2) | BFGS optimization analysis | BFGS improves accuracy for most candidates | Report % of ODEBench cases where BFGS improves R2, stratified by noise level | ODEFormer vs ODEFormer(opt) | % improved, % degraded, % unchanged | >= 60% improved | <1 hour (analysis) | Minor — documents robustness |

```text
ASCII Diagram — Experiment Upgrade Plan (P0/P1/P2 sequencing)

Stage 1 (P0, this week):
[R1: Selection metric ablation] ──→ [R2: Bootstrap CIs]
        ↓                                   ↓
   Fix evaluation pipeline            Solidify reported numbers

Stage 2 (P1, next 2 weeks):
[R3: Filtering sensitivity] ──→ [R4: OOD generalization]
        ↓                                   ↓
   Understand training bias            Bound real-world claims

Stage 3 (P2, optional):
[R5: BFGS success analysis]
        ↓
   Document engineering robustness
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

*Evidence-based rationale:* The paper addresses a well-motivated and practically important problem, presents a technically sound architecture, and provides extensive experimental evaluation across multiple benchmarks and baselines. The code and benchmark release is commendable. However, the score is constrained by: (a) unresolved concerns about the candidate selection metric's alignment with symbolic recovery (Key Issue 2), (b) lack of statistical rigor (no confidence intervals, Key Issue 4), (c) the "first" claim requiring external verification (deferred due to Retrieval-Disabled Mode), and (d) potential data generation filtering biases (Key Issue 1). The research value is solid — extending transformer-based SR to multidimensional systems is a genuine contribution — but the current evidence has several gaps that prevent a higher score.

**Post-Revision Target: [7.5, 8.0] / 10**

This target assumes all P0 items are addressed (rescaling fix, selection metric ablation, statistical evidence). If the selection metric ablation shows consistent improvement and the filtering sensitivity analysis reveals no major bias, the paper could reach 7.5-8.0, positioning it as a solid ICLR-level contribution. Full resolution of all P1 items (distribution-shift analysis, claim scoping) could push toward 8.0.

### Final Opinion

**Top:** ODEFormer tackles a practically important problem — inferring symbolic ODEs from noisy trajectory data — and demonstrates that a transformer-based approach can scale to multidimensional systems, a significant extension beyond prior univariate work. The comprehensive benchmarking (12 baselines, two benchmarks) and honest limitation discussion are strengths.

**Meat:** The paper's empirical claims are weakened by three issues. First, the candidate selection criterion (reconstruction R2) may not align with the goal of symbolic recovery, as the paper's own data shows reconstruction and generalization are decoupled. Second, key figures lack statistical confidence measures, making it difficult to assess whether reported differences are reliable. Third, the aggressive data filtering (90% discard of low-oscillation systems) introduces an uncharacterized selection bias in the training distribution. The novelty claim ("first transformer for multidimensional ODEs") requires scoping and external verification.

**Bottom:** With targeted revisions — fixing the normalization issue, adding a selection metric ablation, and providing statistical confidence intervals — the paper's core contribution would be substantially strengthened. I am supportive of this work and look forward to seeing the revised version.

```text
ASCII Diagram — Paper Structure & Evidence Map

[Problem: Symbolic ODE inference from noisy trajectories]
    │
    ├── [Claim C1: First transformer for multidimensional ODE SR]
    │       └── Evidence: Comparison with Becker et al. (univariate only)
    │       └── Verdict: Deferred (needs external lit verification)
    │
    ├── [Claim C2: Superior accuracy and robustness]
    │       ├── Evidence: Fig 4 (Strogatz), Fig 4 (ODEBench) — avg rankings
    │       └── GAP: No CI/error bars; selection metric may overstate
    │
    ├── [Claim C3: ODEBench as new standard benchmark]
    │       └── Evidence: 63 ODEs, well-documented, code released
    │       └── Strength: Fills genuine gap in evaluation landscape
    │
    └── [Key Method: Encoder-decoder transformer + synthetic pretraining]
            ├── Evidence: Architecture description + training details
            └── GAP: Filtering bias (90% probabilistic discard) uncharacterized
```

```text
ASCII Diagram — Related-Work Taxonomy Tree (Layered)

Dynamical System Identification
├── Branch 1: Black-box neural approaches
│   ├── Leaf 1.1: Neural ODEs (Chen et al. 2018)
│   └── Leaf 1.2: Physics-informed NNs (Raissi et al. 2019)
│   └── Difference from ODEFormer: No symbolic output
│
├── Branch 2: Sparse identification
│   ├── Leaf 2.1: SINDy (Brunton et al. 2016) — linear in basis fn
│   └── Leaf 2.2: SINDy variants (polynomial, trigonometric bases)
│   └── Difference from ODEFormer: Limited to linear combos of prespecified bases
│
├── Branch 3: Genetic programming SR
│   ├── Leaf 3.1: GP for dynamical SR (Gaucel et al., La Cava et al.)
│   ├── Leaf 3.2: Hybrid NN+GP (Atkinson et al. 2019)
│   └── Leaf 3.3: ProGED (Omejc et al. 2023) — PCFG-based
│   └── Difference from ODEFormer: Per-system optimization required
│
├── Branch 4: Transformer-based SR
│   ├── Leaf 4.1: Functional SR (Biggio et al., Kamienny et al.)
│   ├── Leaf 4.2: Univariate ODE SR (Becker et al. 2023)
│   └── Leaf 4.3: Multivariate ODE SR (ODEFormer — THIS PAPER)
│   └── Value contribution: Extends transformer SR to multi-dim systems
│
└── NEW VALUE SOLVED by ODEFormer:
    End-to-end symbolic ODE discovery for multidimensional systems
    from noisy, irregularly sampled data, without per-system optimization
```