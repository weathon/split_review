## Summary
This paper proposes a general framework for conformal prediction in structured prediction settings. The key idea is to construct structured prediction sets — compact, interpretable representations (such as coarse labels in a hierarchy or intervals) that implicitly encode potentially large sets of concrete labels — while providing formal coverage guarantees, either marginal or PAC. The framework adapts the learn-then-test algorithm to handle the non-monotonic relationship between the threshold parameter τ and coverage/set-size in structured label spaces. It is instantiated for directed acyclic graph (DAG)-structured prediction sets via an integer programming formulation, and validated across five domains: MNIST-digit prediction, ImageNet hierarchical classification, SQuAD year-answering, MBPP code generation, and GoEmotions emotion classification. The empirical results show that coverage guarantees are satisfied while prediction set sizes are smaller than the baseline adapted from Khakhar et al. (2023).

## Strengths
1. **Novel Problem Framing**: The paper addresses an important and under-explored problem — extending conformal prediction to structured label spaces where prediction sets must be interpretable. This fills a clear gap between standard conformal prediction (classification/regression) and domain-specific structured prediction methods.

2. **General-Purpose Framework**: Rather than proposing yet another domain-specific conformal method, the paper develops a general algorithmic framework that can accommodate arbitrary user-specified structured prediction set spaces through the abstract components (search space ˜Y, mapping γ, size function σ). This architectural generality is the paper's primary contribution.

3. **Dual Coverage Guarantees**: The framework provides both marginal and PAC (training-conditional) coverage guarantees. The PAC extension (Theorem 3.2) goes beyond straightforward application of learn-then-test and represents a genuine methodological contribution for structured prediction.

4. **Clean Integer Programming Formulation**: The DAG-structured prediction set optimization (Eq. 3-8) is elegantly formulated with clear Boolean constraints and a correct linearization. This makes the method implementable and the algorithmic choices transparent.

5. **Diverse Empirical Validation**: The method is evaluated on five distinct domains spanning image classification, question answering, code generation, digit prediction, and emotion classification. This breadth convincingly demonstrates the framework's generality.

6. **Reproducibility Practices**: The code is publicly available, and the experimental setup details (hyperparameter ranges, calibration set sizes, number of runs with standard deviations) are clearly documented.

## Weaknesses
1. **Barrier to Adoption (Non-Monotonicity Treatment)**: The core algorithmic innovation — adapting learn-then-test to handle non-monotonic τ search in structured prediction — is described at a high level without concrete analysis of how much efficiency is lost compared to monotonic settings. The paper does not provide theoretical guarantees on the statistical efficiency of the sequential test (e.g., how many candidate τ values are needed, or the probability of stopping prematurely). 

2. **Baseline Fairness and Transparency**: The only baseline (adapted from Khakhar et al., 2023) is described at a very high level. The adaptation process and whether the comparison is fair (same IP solver, same τ granularity, same calibration split) are not detailed. Since the baseline deliberately restricts prediction set structure to enforce monotonicity, it may produce larger sets by design, making the comparison favor the proposed method by construction.

3. **Limited Main-Text Experimental Results**: Only one of the five domains (SQuAD question answering) appears in the main paper's results section. Results for MNIST, ImageNet, code generation, and GoEmotions are deferred to the appendix. This weakens the paper's core claim of cross-domain validity, as a reader scanning the main text sees only one domain.

4. **Missing Ablation Studies**: The paper does not ablate its own design choices. For instance: how much does the integer programming formulation matter vs. a greedy heuristic? How does performance vary with the candidate threshold set size k? Is the sequential search significantly more expensive than a single binary search (if monotonicity held)?

5. **Absence of Limitations Discussion**: The conclusion does not discuss any limitations. Key limitations include: (a) IP scalability for dense DAGs, (b) dependence on well-calibrated scoring functions g, (c) reliance on user-provided search spaces, and (d) the lack of guarantee that the sequential testing procedure finds the optimal τ.

6. **PAC Proof Inconsistency**: The proof of Theorem 3.2 contains an apparent inconsistency in the inequality direction between μ (the error probability under invalid τ) and ϵ. While the final result is likely correct, the exposition needs correction (see annotation on Page 5).

## Key Issues
### Issue 1: PAC Proof Exposition Error (Page 5)
**Severity: Major | Fixable: Yes**

The proof of Theorem 3.2 contains an inconsistency in the inequality direction. The text states "Since τ0 is invalid, we have μ > ϵ" but then writes "μ ≤ ϵ" in the next sentence when applying the Binomial CDF monotonicity. The correct reasoning is: since the Binomial CDF F(ℓ; n, p) is monotonically *decreasing* in p, when μ > ϵ we have F(ℓ; n, μ) < F(ℓ; n, ϵ) < δ, which still gives the desired bound. The "μ ≤ ϵ" statement is erroneous and should be removed or corrected to "μ ≥ ϵ".

**Action**: Replace "μ ≤ ϵ" with "μ ≥ ϵ" and clarify the monotonicity direction.

### Issue 2: Baseline Comparison Transparency (Page 8)
**Severity: Major | Fixable: Yes**

The baseline adaptation from Khakhar et al. (2023) is described in only two sentences. The reader cannot assess whether the comparison is fair — whether both methods use the same IP solver, same candidate thresholds, same calibration split, and same scoring function. Since the baseline enforces monotonicity by restricting prediction set structure, it may produce larger sets by design, making the comparison structurally favoring the proposed method.

**Action**: Add a dedicated paragraph describing the baseline adaptation, including: (a) how monotonicity is enforced, (b) what structural restrictions are imposed, (c) whether the same IP solver and threshold set are used, and (d) any computational budget differences.

### Issue 3: Missing Main-Text Results for 4 of 5 Domains (Page 9)
**Severity: Moderate | Fixable: Yes**

Only the SQuAD question answering results appear in the main paper. Results for MNIST, ImageNet, code generation, and GoEmotions are in Appendix A.4. This weakens the cross-domain generality claim.

**Action**: Add a compact summary table in the main text showing coverage rate and average prediction set size for all five domains at default hyperparameters (m=4, ϵ=0.1, δ=0.01 for PAC).

### Issue 4: No Ablation or Sensitivity Analysis
**Severity: Moderate | Fixable: Yes**

The paper does not ablate its own design choices. Key unknowns include: (a) sensitivity to the candidate threshold set size k, (b) comparison of IP-based optimization vs. greedy heuristics, (c) impact of the scoring function calibration quality, and (d) how the sequential search cost compares to an idealized monotonic search.

**Action**: Add at least one ablation experiment: vary k (number of candidate τ values) and report coverage/size tradeoff; compare IP solver vs. a greedy top-down selection heuristic.

### Issue 5: Missing Limitations Section (Page 10)
**Severity: Moderate | Fixable: Yes**

The conclusion does not discuss any limitations of the proposed framework.

**Action**: Add a limitations paragraph covering: IP scalability for dense DAGs, dependence on well-calibrated scoring functions, reliance on user-provided search spaces, and the heuristic nature of the sequential τ search.

## Actionable Suggestions
### S1: Fix PAC Proof Exposition (Must)
**Location**: Page 5, Theorem 3.2 proof
**Problem**: The inequality direction between μ and ϵ is inconsistent.
**Fix**: Replace the sentence "where the first inequality follows since the CDF of the Binomial (n, p) is monotonically decreasing in p and μ ≤ ϵ" with "where the first inequality follows since the CDF of the Binomial (n, p) is monotonically decreasing in p and μ > ϵ (so F(ℓ; n, μ) < F(ℓ; n, ϵ))".

### S2: Add Baseline Adaptation Details (Must)
**Location**: Page 8, Section 5.1, Baseline paragraph
**Problem**: The baseline is described too briefly.
**Fix**: Add a paragraph specifying: (a) how the Khakhar et al. method is generalized to DAGs, (b) whether the same IP solver and threshold set are used, (c) what structural restrictions are imposed to enforce monotonicity, and (d) any computational budget differences.

### S3: Add Cross-Domain Summary Table in Main Text (Must)
**Location**: Page 9, before Section 5.2
**Problem**: Only one domain's results appear in the main text.
**Fix**: Add a table showing coverage rate and average prediction set size for all five domains at default hyperparameters (m=4, ϵ=0.1, δ=0.01 for PAC). Include the baseline comparison for each domain.

### S4: Add Ablation Study (Nice-to-have)
**Location**: New subsection in Section 5
**Problem**: No ablation of design choices.
**Fix**: Add an experiment varying the number of candidate thresholds k (e.g., k=10, 20, 50, 100) and reporting coverage/size tradeoff. Also compare IP-based optimization against a greedy heuristic (e.g., select top-m nodes by cumulative probability).

### S5: Add Limitations Paragraph (Must)
**Location**: Page 10, Conclusion
**Problem**: No limitations are discussed.
**Fix**: Add a paragraph acknowledging: (a) IP scalability for dense DAGs, (b) dependence on well-calibrated scoring functions, (c) reliance on user-provided search spaces, and (d) the heuristic nature of the sequential τ search.

### S6: Strengthen Abstract (Nice-to-have)
**Location**: Page 1, Abstract
**Problem**: Abstract does not mention the two coverage guarantee types or the learn-then-test adaptation.
**Fix**: Revise to include: "providing both marginal and PAC coverage guarantees" and "adapting the learn-then-test framework to handle non-monotonic structured search spaces".

### S7: Clarify Scoring Function Requirements (Nice-to-have)
**Location**: Page 4, Section 2
**Problem**: The statement "we make no assumptions about g" is too permissive.
**Fix**: Add a clarification that the approach is most effective when g(x,·) is approximately calibrated (e.g., softmax-normalized), and specify what properties are needed for the cumulative constraint in Eq. (1) to be meaningful.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current narrative flow is:
1. General DNN/UQ motivation → 2. Conformal prediction introduction → 3. Gap: structured prediction not handled → 4. Framework overview (non-monotonicity, learn-then-test, DAG) → 5. Contributions → 6. Related work → 7. Problem formulation → 8. Algorithm → 9. DAG IP → 10. Experiments → 11. Conclusion

**Strengths**: Technically accurate and well-organized. The progression from abstract concepts to concrete formulation is logical.

**Weaknesses**: (a) The introduction opens too generically (first two paragraphs could be from any conformal prediction paper). (b) The core technical challenge (non-monotonicity) is introduced late in the introductory material. (c) The five-paragraph introduction mixes motivation, related work, and methodology without clear paragraph roles.

### Abstract Outline

**S1 (Problem)**: Conformal prediction provides distribution-free coverage guarantees but is limited to simple label spaces.
**S2 (Gap)**: Structured outputs need interpretable prediction sets, yet existing methods are domain-specific.
**S3 (Solution)**: We propose a general framework for conformal structured prediction that adapts learn-then-test to handle non-monotonic τ search and provides marginal/PAC guarantees.
**S4 (Instantiation)**: We instantiate this for DAG-structured prediction sets via integer programming.
**S5 (Results)**: Valid coverage and smaller sets with significantly smaller size than baselines across five domains.

### Introduction Outline (Revised, 4-paragraph structure)

**P1 — Hook and Stakes** (Problem + Significance):
Role: Establish why structured prediction UQ matters.
Claim: Conformal prediction is powerful but designed for simple label spaces.
Transition: "However, many practical prediction problems involve complex structured outputs."

**P2 — Gap** (What's Missing):
Role: Identify the precise gap — general algorithms for structured prediction sets.
Claim: Domain-specific methods exist but lack generality; the core technical barrier is non-monotonicity.
Transition: "To address this gap, we propose the authors propose a general algorithmic framework."

**P3 — Solution Overview** (What We Do):
Role: High-level description without technical details.
Claim: Framework with abstract components (search space, mapping, size function), sequential testing, and PAC extension.
Transition: "We instantiate this framework for an important special case."

**P4 — DAG Instantiation and Plan** (How):
Role: Connect framework to concrete DAG IP formulation.
Claim: Integer programming for DAG-structured prediction sets.
Transition: "We validate our approach across five domains."

### Revised Title Options

Current: "Conformal Structured Prediction"
Option A: "A General Framework for Conformal Prediction with Structured Outputs"
Option B: "Conformal Structured Prediction: Coverage-Guaranteed Uncertainty Quantification for Hierarchical and Complex Label Spaces"
Option C: "Learn-Then-Test for Structured Prediction: A General Conformal Prediction Framework with Marginal and PAC Guarantees"

Recommended: Option A — balanced between specificity and breadth.

## Priority Revision Plan
### P0 (Critical — Must Fix Before Resubmission)

| Priority | Issue | Action | Effort | Impact |
|----------|-------|--------|--------|--------|
| P0 | PAC proof inconsistency (Page 5) | Correct μ ≤ ϵ → μ > ϵ | 5 min | High: Fixes mathematical error |
| P0 | Missing limitations | Add limitations paragraph to Conclusion | 15 min | High: Improves scientific integrity |
| P0 | Baseline fairness | Add detailed baseline adaptation description | 30 min | High: Validates empirical comparison |

### P1 (Important — Should Fix)

| Priority | Issue | Action | Effort | Impact |
|----------|-------|--------|--------|--------|
| P1 | Results only show 1/5 domains | Add cross-domain summary table | 1 hr | High: Supports generality claim |
| P1 | Introduction too generic | Restructure to 4-paragraph arc | 1 hr | Medium: Improves readability |
| P1 | Abstract too vague | Add two guarantee types + learn-then-test | 15 min | Medium: Better surveyability |

### P2 (Nice-to-Have)

| Priority | Issue | Action | Effort | Impact |
|----------|-------|--------|--------|--------|
| P2 | No ablation study | Add k-variation experiment | 2 hr | Medium: Strengthens robustness |
| P2 | Scoring function ambiguity | Clarify g(x,y) normalization requirements | 15 min | Low: Improves clarity |
| P2 | Title too generic | Consider Option A or B | 10 min | Low: Improves first impression |

### ASCII Diagram — Revision Strategy Roadmap

```text
[Current manuscript]
    │
    ├── P0 fixes (1 day)
    │   ├── Fix PAC proof inconsistency
    │   ├── Add limitations paragraph
    │   └── Detail baseline adaptation
    │   └── Expected: clean math + honest boundaries + fair comparison
    │
    ├── P1 fixes (1-2 days)
    │   ├── Add cross-domain summary table
    │   ├── Restructure introduction arc
    │   └── Revise abstract for precision
    │   └── Expected: stronger narrative + complete evidence
    │
    └── P2 fixes (flexible)
        ├── Add ablation study
        ├── Clarify scoring function
        └── Consider title revision
        └── Expected: robustness evidence + clarity
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Domain | Objective | Setup | Metrics | Main Outcome | Claim Supported | Limitation |
|--------|--------|-----------|-------|---------|-------------|----------------|-----------|
| E1 | SQuAD QA (dates) | Validate coverage & size for interval-based prediction sets | Llama-3.1-70B, 262 examples, DAG of 51 layers/650 nodes | Coverage rate, avg set size | Valid coverage above 1-ϵ; size ≤ baseline | C1 | Only one domain in main text |
| E2 | 2-digit MNIST | Validate for digit-string prediction | Feedforward network, k=2, DAG of 3 layers/111 nodes | Same as E1 | Valid coverage; size improves over baseline | C1 | Appendix only |
| E3 | 3-digit MNIST | Scalability to larger digit strings | Same network, k=3, DAG of 4 layers/1111 nodes | Same as E1 | Valid coverage; IP slower for larger DAG | C2 | IP cost higher; appendix only |
| E4 | ImageNet | Hierarchical label prediction | ResNet-50, 1000-class, WordNet hierarchy (18 layers/1816 nodes) | Same as E1 | Valid coverage; structured sets more interpretable | C1, C3 | Appendix only |
| E5 | MBPP code generation | Partial program prediction sets | GPT-4o-mini, AST-based DAG | Same as E1 | Valid coverage; partial programs interpretable | C1 | Appendix only |
| E6 | GoEmotions | Emotion label prediction | RoBERTa-base, 27 emotion categories, 58K comments | Same as E1 | Valid coverage | C1 | Appendix only |
| E7 | Computational cost | Running time comparison | All five domains | Solve time per IP, total τ estimation time | Faster than baseline for most domains | C2 | 3-digit MNIST slower |

### Research-Theme Gap Diagnosis

- **New Knowledge**: The paper successfully demonstrates that structured prediction sets with coverage guarantees can be computed via a general framework. This is genuine new knowledge, but the empirical contribution is weakened by relegating 4/5 domains to the appendix.
- **Reproducibility**: The code is available and the IP formulation is clear, but the baseline adaptation is underspecified, making the main comparison hard to reproduce independently.
- **Impact on Practice**: The framework could influence how practitioners deploy conformal prediction for complex outputs, but the computational cost (IP solving) and dependence on user-provided search spaces may limit adoption without further tooling.

### Proposed Research Experiments

**P0 Experiment — Candidate Threshold Sensitivity**
- **Target Claim**: C1 (framework generality), C2 (algorithm efficiency)
- **Hypothesis**: The number of candidate thresholds k affects the coverage-size tradeoff.
- **Minimal Design**: Vary k ∈ {5, 10, 20, 50, 100} on the SQuAD dataset, with m=4, ϵ=0.1.
- **Controls**: Same calibration split, same IP solver.
- **Metrics**: Coverage rate, average set size, τ estimation time.
- **Success Criterion**: Coverage remains above 1-ϵ for all k, with diminishing returns in size reduction beyond k=20.
- **Estimated Cost**: ~2 hours (IP solving).
- **Expected Quality Gain**: Provides robustness evidence for the algorithmic design.

**P1 Experiment — Greedy Heuristic vs. IP Optimization**
- **Target Claim**: C2 (IP formulation effectiveness)
- **Hypothesis**: A greedy heuristic (select top-m nodes by cumulative leaf probability) may perform close to IP for well-calibrated g.
- **Minimal Design**: Compare IP-based hτ(x) vs. greedy selection on SQuAD and ImageNet.
- **Controls**: Same candidate thresholds, same calibration set.
- **Metrics**: Coverage rate, average set size, solve time.
- **Success Criterion**: Greedy achieves coverage within 1% of IP with 10× faster solve time.
- **Estimated Cost**: ~1 hour.
- **Expected Quality Gain**: Provides practical guidance for scalability.

**P2 Experiment — Scoring Function Calibration Impact**
- **Target Claim**: C1 (framework applicability)
- **Hypothesis**: Miscalibrated g leads to larger prediction sets even with valid sets with same coverage.
- **Minimal Design**: On ImageNet, On SQuAD, compare softmax-calibrated vs. raw logit scores as g.
- **Controls**: Same DAG, same candidate thresholds.
- **Metrics**: Average set size, coverage rate.
- **Success Criterion**: Calibrated scores produce strictly smaller set sizes at same coverage level.
- **Estimated Cost**: ~1 hour.
- **Expected Quality Gain**: Clarifies the "no assumptions about g" statement and provides practical guidance.

### ASCII Diagram — Experiment Upgrade Plan

```text
[Existing experiments: 5 domains, 2 guarantees]
    │
    ├── P0: Candidate threshold sensitivity (k variation)
    │   └── Validates algorithmic robustness
    │
    ├── P1: Greedy heuristic vs. IP optimization
    │   └── Validates practical scalability
    │
    └── P2: Scoring function calibration impact
        └── Clarifies g(x,y) requirements
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score**: 7.6/10

**Reasoning**: The paper addresses a genuinely important problem (conformal prediction for structured outputs) with a clean, general framework. The core ideas — adapting learn-then-test for non-monotonic τ search, providing both marginal and PAC guarantees, and formulating DAG-structured prediction as an IP — are technically sound and novel within the conformal prediction literature. The empirical validation across five domains demonstrates generality.

However, the score is reduced due to: (1) the PAC proof contains a minor but notable exposition error (inconsistent inequality direction); (2) the baseline comparison lacks transparency, making it hard to assess fairness; (3) only 1/5 domain results appear in the main text, weakening the cross-domain claim; (4) no ablation studies validate design choices; and (5) the conclusion lacks a limitations section. These issues are all fixable but collectively lower confidence in the current presentation.

**Post-Revision Target**: [7, 8]/10

** 

If all P0 items (PAC proof fix, limitations section, baseline transparency) and key P1 items (cross-domain summary table, introduction restructuring) are addressed, the paper could reach 7-8/10, reflecting solid technical contribution with clear empirical support.

**Score Dimensions**:
- Research Value: 8/10 — Important problem, well-motivated
- Novelty: 7/10 — General framework with PAC extension is novel
- Technical Soundness: 6/10 — Clean theory but proof error and missing ablations
- Empirical Rigor: 6/10 — Good breadth but missing main-text results and ablation
- Reproducibility: 6/10 — Code available but baseline underspecified
- Clarity: 7/10 — Generally well-written but introduction could be tightened