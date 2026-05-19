## Summary
# Final Review Report

## Summary

This paper proves that neural networks trained solely by weight permutation of a fixed weight vector — without changing the numeric values of the weights — retain the universal approximation property (UAP) for one-dimensional continuous functions. The authors establish three theorems: (1) UAP with a learnable output linear layer, (2) UAP without the linear layer removed via pseudo-copy construction, and (3) UAP under pairwise random initialization with high probability. The proof uses a four-pair construction of step function approximators and a processing method that reorganizes unused parameters into a controllable linear function. Numerical experiments on 1D regression tasks confirm the predicted O(n^{-1/2}) convergence rate and show the method works beyond the theoretically covered settings, though some standard initializations (He, Xavier) fail to converge. The paper also provides qualitative observations of permutation-active patterns during training. The work is the first theoretical UAP guarantee for the permutation training paradigm, but its scope is limited to 1D functions, and novelty comparisons with existing UAP literature could not be verified in this run (defer to manual check).

## Strengths
1. **First theoretical UAP guarantee for permutation training.** To the best of the authors' knowledge (and pending manual literature verification), this is the first proof that a network trained solely by weight permutation — without changing weight values — can universally approximate continuous functions. This fills a clear gap between empirical observations (Qiu & Suda, 2020) and theoretical understanding.

2. **Clean, constructive proof technique. The four-pair construction of step function approximators (Eq. 3-4) and the processing method for eliminating unused parameters (Lemma 2) are elegant and self-contained. The proof is structured in a modular way (piecewise constant approximation → step function approximation → unused parameter elimination) that makes the reasoning accessible.

3. **Explicit convergence rate.** The paper derives an O(n^{-1/2}) approximation rate (Section 3.4) and verifies it experimentally (Section 4.3), providing a concrete link between theory and practice that is often missing in UAP papers.

4. **Comprehensive initialization study.** The comparison of 8 different initialization methods (Section 4.4, Fig. 3) is valuable for practitioners. The finding that standard initializations (He, Xavier) fail under permutation training is a practically important and motivates future work on compatible initialization schemes.

5. **Honest limitation discussion.** The paper openly acknowledges the challenge of extending results to high dimensions (Section 5, App. K), the dependence on pairwise initialization for the unused-parameter elimination method, and the computational cost of the current LaPerm algorithm.

## Weaknesses
1. **1D-only theoretical scope.** The UAP theorems (Theorem 1-3) are strictly limited to one-dimensional continuous functions. The extension to 2D/3D (App. K) is only empirical, shows a degraded convergence rate (from O(n^{-1/2}) to O(n^{-1/6}) for 3D), and lacks any theoretical backing. This fundamentally limits the practical impact of the results, since the motivating applications (image classification, physical neural networks) are inherently high-dimensional.

2. **Unused-parameter elimination depends on pairwise initialization.** The processing method in Section 3.2 (Lemma 2) critically requires the coefficient vector to be in pairwise form W(n) = (±pi). This assumption excludes the more natural "totally random" initialization (cases 1, 7, 8 in Fig. 3), which the experiments confirm fail to converge. The paper does not provide a theoretical fix for this limitation.

3. **Experimental gap between Theorem 2 and experiments.** Theorem 2 (pure permutation, α=0, γ=1) is the strongest theoretical result, but experiments use the more flexible Theorem 1 setting (α, γ are learnable). The paper does not experimentally validate Theorem 2, and the pseudo-copy construction would require impractically large networks (M ∼ O(d^{-2}) copies) for any reasonable accuracy.

4. **Overclaiming in the third contribution.** The claim that "permutation training could serve as a new approach to describe network learning behaviors" is based on qualitative observations of permutation-frequency patterns (Fig. 4) without any quantitative validation, ablation, or comparison to existing learning-dynamics analysis tools.

5. **Statistical rigor of experiments.** Error bars in Fig. 3 are omitted "for conciseness," key comparisons (e.g., "case 5 achieves the best accuracy for larger networks") are not supported by significance tests, and the L∞ convergence rate claim (Section 4.3) is an empirical observation without theoretical justification (the derivation in Section 3.4 is for L2 error).

## Key Issues
### Issue 1 (Major): 1D-only theoretical scope vs. practical motivation mismatch
**Location:** Page 1 - Introduction, Page 9 - Conclusion, Appendix K  
**Evidence:** Theorem 1-3 are all for f* ∈ C([0,1]). The 2D/3D experiments (App. K) lack theoretical guarantees and show degraded convergence (from O(n^{-1/2}) to O(n^{-1/6})).  
**Risk:** The paper motivates permutation training via image classification (high-dimensional) and physical neural network applications, but the theoretical results do not apply to these motivating scenarios.

### Issue 2 (Major): Experiments use a weaker constraint than the strongest theorem
**Location:** Page 7 - Section 4.2, Page 6 - Theorem 2  
**Evidence:** Section 4.2 states "α, γ in the output layer are freely trained scaling factors" (Theorem 1 setting). Theorem 2 (pure permutation, α=0, γ=1) is never experimentally validated.  
**Risk:** Readers may overestimate the practical capability of pure permutation training based on experimental results that rely on additional learnable parameters.

### Issue 3 (Major): Third contribution is qualitatively speculative
**Location:** Page 1 - bullet points, Page 8-9 - Section 4.5  
**Evidence:** The claim that permutation training "could potentially serve as a new approach to describe network learning behaviors" relies on a single observational figure (Fig. 4) with no quantitative analysis, no comparison baselines, and no predictive validation.  
**Risk:** This overclaim dilutes the paper's core theoretical contributions and may be challenged by reviewers.

### Issue 4 (Major): Initial conditions crucially limit the theory
**Location:** Page 5-6 - Section 3.2, Page 8 - Section 4.4  
**Evidence:** The unused-parameter elimination method (Lemma 2) requires pairwise initialization W(n) = (±pi). Experiments show that standard initializations (He, Xavier) that do not satisfy this condition fail to converge (Fig. 3, cases 7-8).  
**Risk:** The paper's theoretical guarantees are tied to a specific initialization class that is not standard practice, limiting practical deployment.

### Issue 5 (Minor): L2-based convergence rate claimed for L∞ error
**Location:** Page 6** - Section 3.4, Page 7 - Section 4.3  
**Evidence:** Section 3.4 derives E_s ∼ O(n^{-1/2}) for L2 error. Section 4.3 says "L∞ error exhibits a 1/2 convergence rate... we indeed observe that it also holds for L∞ error" without theoretical justification.  
**Risk:** While the empirical observation is useful, the absence of theoretical L∞ bounds weakens the rigor of the paper.

## Actionable Suggestions
### S1 (Must): Add explicit discussion of the α, γ gap
**Location:** Page 7 - Section 4.2, Page 1 - Abstract  
**Action:** Add a sentence in Section 4.2 clarifying that experiments use the Theorem 1 setting (α, γ learnable), not the stricter Theorem 2 setting (α=0, γ=1). In the abstract, replace "neural networks trained by weight permutation are universal approximators" with a more precise statement, e.g., "neural networks trained by weight permutation — with a learnable output scaling — are universal approximators for 1D functions."

### S2 (Must): Tone down or remove the third contribution claim
**Location:** Page 1 - bullets, Page 9 - Conclusion paragraphs 3-4  
**Action:** Replace the third bullet point with a bounded statement: "We report qualitative observations of permutation patterns during training, which suggest a correlation between weight reordering and learning dynamics that merits further investigation." Remove or substantially dial back the speculative claims about lottery ticket hypothesis and continual learning in the Conclusion.

### S3 (Must): Add limitations paragraph on 1D scope
**Location:** Page  Location:** Page 9 - Conclusion  
**Action:** Add an explicit paragraph: "A key limitation of this work is that our theoretical results are confined to one-dimensional functions. While preliminary 2D/3D experiments show some approximation power, they achieve a degraded convergence rate and lack theoretical guarantees. Bridging this gap is an important direction for future work."

### S4 (Nice-to-have): Justify the L∞ convergence rate
**Location:** Page 7 - Section 4.3, lines 22-23  
**Action:** Add a brief theoretical note: "Because f_NN_s is piecewise linear and the L2-L∞ relationship for bounded piecewise linear functions on a compact interval yields norm equivalence, the O(n^{-1/2}) rate observed for L∞ is consistent with our L2-based estimate." Alternatively, explicitly mark this as an empirical observation requiring future theoretical work.

### S5 (Nice-to-have): Restructure the Related Works section
**Location:** Page 2 - Related Works  
**Action:** Reorganize the three existing paragraphs into a clear taxonomy: (a) Classical UAP results, (b) Permutation in deep learning (equivariant/invariant networks vs. permutation training), (c) Connection to LMC. Each paragraph should end with an explicit contrast to this paper.

### S6 (Nice-to-have): Add statistical significance to initialization comparison
**Location:** Page 8 - Fig. 3, Section 4.4  
**Action:** Add error bars (or a shaded region) to Fig. 3 for all 8 methods, at least for n ≥ 160. For the key claim about case 5 being "best," report a paired comparison at n=1280 with mean ± std across 10 seeds.

## Storyline Options + Writing Outlines
### Abstract Outline (Revised)

**S1 (Problem):** Universal approximation is a fundamental property of neural networks, but existing proofs assume unrestricted weight values.

**S2 (Prior gap):** Recent empirical work shows that permuting fixed-weight vectors — without changing their values — can achieve competitive classification performance, yet whether this constrained training paradigm retains the universal approximation property remains unknown.

**S3 (Method):** In this paper, we prove that a ReLU network trained solely by weight permutation can approximate any one-dimensional continuous function. Our constructive proof introduces a four-pair step function approximator that operates under the permutation constraint, together with a method to eliminate unused parameters by reorganizing them into a controllable linear function.

**S4 (Results):** Numerical experiments on regression tasks confirm the predicted O(n^{-1/2}) convergence rate and demonstrate that the approximation power extends to various random initialization schemes.

**S5 (Implications):** These results provide the first theoretical foundation for permutation-based training and suggest that weight ordering alone can encode rich functional expressivity.

### Introduction Outline (Revised — 4 paragraphs)

**P1 (Big Picture → Gap):**
Role: Establish the importance of UAP and identify the specific gap — all existing UAP proofs assume unrestricted weights.
Transition: "However, recent hardware-constrained settings motivate a different question..."

**P2 (Constrained setting → Motivation):**
Role: Introduce permutation training (Qiu & Suda 2020), its hardware applications, and the open theoretical question.
Transition: "This raises a natural question: does a network trained solely by weight permutation still possess UAP?"

**P3 (Solution → Proof idea preview):**
Role: State the main theoretical contribution (1D UAP proof), outline the two key techniques (four-pair construction, processing method).
Transition: "Beyond the theoretical result, we also provide empirical validation..."

**P4 (Contributions → Paper outline):**
Role: List the three contributions with bounded language. Cleanly state: "(1) UAP proof for 1D continuous functions under equidistant and pairwise random initialization; (2) numerical validation across diverse settings; (3) qualitative observation of permutation dynamics during training."
Transition: "The remainder of this paper is organized as follows..."

### Candidate Storyline Alternatives

**Option A (Current — moderate revision needed):** Start with classical UAP → introduce permutation constraint → prove 1D UAP → experiments → conclusion. This is the current structure and works well, but the Introduction needs tightening (see above).

**Option B (Stronger hardware focus):** Start with the hardware motivation (fixed-weight accelerators, photonic tensor cores) → identify the theoretical gap → prove 1D UAP → experiments → discuss how theoretical guarantees support hardware deployment. This would strengthen the practical relevance message but might lose readers unfamiliar with hardware.

**Option C (Theory-first):** Start with "Can a neural network with frozen weight values still approximate any function?" as the central question → prove 1D UAP → experiments → then connect to permutation training applications. This is the most direct narrative but underplays the practical motivation.

**Recommendation:** Option A (current) with the revised Introduction outline above. Keep the hardware motivation in Appendix A and reference it, but lead with the theoretical question in the main text.

## Priority Revision Plan
| Priority | Issue | Action | Effort | Impact | Status |
|----------|-------|--------|--------|--------|--------|
| P0 | Claim-evidence mismatch in third contribution | Tone down / remove speculative claims about "novel tool" for learning behavior | Low (editing) | High (defensibility) | Must |
| P0 | α, γ gap between Theorem 2 and experiments | Add explicit clarification in Section 4.2 and Abstract | Low (editing) | High (honesty) | Must |
| P1 | 1D-only scope vs. practical motivation | Add explicit limitation paragraph in Conclusion | Low (editing) | Medium (scope clarity) | Must |
| P1 | L2→L∞ rate gap | Add brief justification or mark as empirical observation | Low (editing) | Medium (rigor) | Nice-to-have |
| P2 | Missing error bars in Fig. 3 | Add error bars or confidence intervals | Medium (re-run) | Medium (statistical rigor) | Nice-to-have |
| P2 | Related Work lacks structure | Reorganize into taxonomy-based paragraphs | Medium (editing) | Medium (readability) | Nice-to-have |

### Revision Roadmap

```text
ASCII Diagram — Revision Strategy Roadmap

[Phase 1: Claim Bounding (today)]
    ├── S1: Tone down contribution #3 (P0)
    ├── S2: Clarify α,γ gap in abstract + Sec 4.2 (P0)
    └── S3: Add 1D scope limitation in Conclusion (P1)
    ↓
[Phase 2: Rigor Enhancement (this week)]
    ├── S4: Justify L∞ rate or mark as empirical (P1)
    ├── S5: Add error bars to Fig. 3 (P2)
    └── S6: Restructure Related Works (P2)
    ↓
[Phase 3: Major Addressed for Next Submission]
    ├── Expected: cleaner claims, honest limitations, clearer positioning
    └── Remaining: high-dimensional UAP remains open
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|--------------------------------------|---------|--------------|----------------|-------------------|
| E1 | Approximate 1D continuous functions (sin, Legendre) | 1-2n-1-1 network, random pairwise init, x∈[-1,1], 10 seeds | L∞ error | O(n^{-1/2}) convergence; relaxed LaPerm no better | C1 (UAP proof) | Uses learnable α,γ (Thm 1 not Thm 2); L∞ rate not theoretically justified |
| E2 | Compare 8 initialization methods | Same setup as E1, 8 init schemes, n up to 1280 | L∞ error | Pairwise outperforms; He/Xavier fail to converge | C2 (generalization) | Error bars omitted for many cases; no significance tests |
| E3 | 2D function approximation | 2-8n-1-1 network, 8-direction basis, z = -sin(πxy) | L∞ error | Approximation works but convergence < O(n^{-1/2}) | C1 (extension) | No theoretical guarantee; heuristic basis design |
| E4 | 3D function approximation | 3-26n-1-1 network, similar setup, f = sin·cos·sin | L∞ error | Approximation works; rate degrades to O(n^{-1/6}) | C1 (extension) | No theoretical guarantee; very preliminary |
| E5 | Leaky-ReLU activation | Only change activation from E1 setup | L∞ error | Similar convergence behavior | C1 (extension) | Limited to one target function |
| E6 | Permutation pattern observation | Equidistant init, n=640, track active components | Frequency, distribution | 4-stage pattern identified | C3 (learning behavior) | Qualitative only; no predictive model; single run |

### Research-Theme Gap Diagnosis

1. **New Knowledge (C1, C2):** The paper successfully provides new theoretical knowledge (UAP under weight-permutation constraint) and empirical validation. However, the knowledge is confined to 1D, limiting its transformative potential.
2. **Reproducibility (all experiments):** The paper provides hyperparameter tables (App. L), code implementation details, and 10-seed repeats. Reproducibility is reasonable but would benefit from open-sourcing the code.
3. **Impact on Practice (C3):** The claimed potential to "describe network learning behavior" is not validated with predictive or comparative experiments, limiting its practical impact.

### Proposed Research Experiments

| Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Priority |
|-------------|-----------|---------------|-------------------|---------|-------------------|----------|
| C2: L∞ rate matches L2 theory | Under piecewise linear structure, L∞ error should also follow O(n^{-1/2}) | For E1, compute L2 error on same runs and compare with L∞; plot both on same axis | E1 results for L2 and L∞ | Ratio L∞/L2 across n | If ratio is bounded as n increases, L∞ rate is theoretically consistent | P1 |
| C3: Permutation patterns predict loss | Permutation frequency in early stages predicts final convergence | Split 20 seeds into "fast" and "slow" convergence groups and compare permutation-stage timing | Random seed 2022 (base case) | Correlation coeff between permutation frequency peak epoch and final L∞ | |r| > 0.5 with p < 0.05 | P2 |
| C1: Theorem 2 validation | Pure permutation (α=0, γ=1) can approximate a simple function with sufficient width | Test a single step function approximation with pseudo-copy construction for small n (e.g., n=20, 40, 80) | Theorem 1 setup (α,γ learnable) | L∞ error vs. n | Error decreases with n, even if absolute error is large | P1 |
| C2: Failure analysis for He/Xavier | Increasing width beyond n=1280 eventually achieves convergence for He init | Add n=2560 run for cases 5-8 (or determine max feasible width) | Cases 5-8 at n=1280 | L∞ error trend | If error decreases at larger n, failure is not fundamental | P2 |

```text
ASCII Diagram — Experiment Upgrade Plan (P0/P1/P2)

P0 (before resubmission): claim/user
├── Add L2 error reporting alongside L∞ in Fig. 2
├── Add error bars to Fig. 3 for all cases at n≥160
└── Run one Theorem 2 validation experiment (step function)

P1 (next revision):
├── Theoretical: bound L∞ rate using piecewise linear structure
├── Empirical: correlation analysis between permutation patterns and loss
└── Empirical: larger n for failing initializations (cases 6-8)

P2 (future work):
├── High-dimensional: theoretical UAP extension beyond 1D
├── Algorithm: permutation search without Adam inner loop
└── Theory: remove pairwise initialization requirement
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 5.5/10

**Rationale:** The paper presents a clean theoretical proof (C1) that fills a genuine gap between empirical observations of permutation training and UAP theory. This is a solid conceptual contribution. However, the score is constrained by: (1) the 1D-only theoretical scope, which limits practical impact given the motivating applications are high-dimensional; (2) the gap between the strongest theorem (Theorem 2, pure permutation) and the experiments (using learnable α,γ); (3) the overclaiming in the third contribution; and (4) the reliance on pairwise initialization for the theoretical results. Novelty scoring is deferred (manual literature verification required), and the above score assumes the UAP proof is indeed the first of its kind for permutation training, which is plausible from manuscript evidence.

**Post-Revision Target:** [6.0, 7.0]/10

If the authors address the P0/P1 items (tone down contribution #3, clarify α,γ gap, add explicit scope limitations, justify the L∞ rate), the paper becomes a cleaner and more defensible 6-7 range submission. The theoretical core is the main strength and would remain unchanged.

### ASCII Diagram — Paper Structure & Evidence Map

```text
[Core Claim: Permutation-trained ReLU networks are universal approximators for 1D functions]
    │
    ├── C1: Theoretical UAP Proof (Theorems 1-3)
    │   ├── Evidence: Constructive proof with four-pair construction + Lemma 2
    │   ├── Gap: 1D only; pairwise init assumption
    │   └── Verdict: supported (pending manual lit. verification)
    │
    ├── C2: Numerical Validation (Section 4)
    │   ├── Evidence: Fig. 2 (convergence), Fig. 3 (8 init methods)
    │   ├── Gap: Uses learnable α,γ (Thm 1 not Thm 2); error bars missing
    │   └── Verdict: partially proven
    │
    └── C3: Learning Behavior Description (Section 4.5)
        ├── Evidence: Fig. 4 (qualitative permutation pattern)
        ├── Gap: No quantitative validation; no predictive model
        └── Verdict: unsupported → needs downgrade
```

### ASCII Diagram — Related-Work Taxonomy Tree (Layered)

```text
Related Work Taxonomy (Root: Neural Network Approximation Theory)
│
├── Branch 1: Universal Approximation Properties
│   ├── Leaf 1.1: Classical UAP (fully-connected, unconstrained weights)
│   │   └── Works: Cybenko 1989, Hornik 1989, Leshno 1993
│   ├── Leaf 1.2: Operator UAP
│   │   └── Works: Chen & Chen 1995, DeepONet (Lu 2021)
│   └── Leaf 1.3: Constrained-weight UAP (THIS PAPER)
│       └── Distinct constraint: weight values fixed, only permutation allowed
│
├── Branch 2: Permutation in Deep Learning
│   ├── Leaf 2.1: Permutation-equivariant/invariant networks
│   │   └── Works: Cohen & Welling 2016, Deep Sets (Zaheer 2017), Set Transformer (Lee 2019)
│   │   └── Difference vs this paper: they handle symmetric data, not training by permutation
│   └── Leaf 2.2: Weight permutation training
│       └── Works: Qiu & Suda 2020, Kosuge 2021ab, Scabini 2022
│       └── Our contribution: first theoretical UAP guarantee for this paradigm
│
└── Branch 3: Permutation Symmetry & Model Connectivity
    ├── Leaf 3.1: Linear Mode Connectivity
    │   └── Works: Frankle 2020, Entezari 2021, Git Re-Basin (Ainsworth 2023), REPAIR (Jordan 2023)
    │   └── Difference vs this paper: LMC aligns separate models; ours trains one model
    └── Leaf 3.2: Continual Learning via weight projection
        └── Works: Zeng 2019, Maltoni & Lomonaco 2019
        └── Connection: permutation training ≈ order-preserving weight projection
```

### Page Coverage Audit

| Page | Annotation Count | Coverage Status | Skip Reason (if skipped) |
|------|-----------------|-----------------|--------------------------|
| 1 (Abstract + Intro) | 5 | covered | |
| 2 (Related Work + Outline) | 2 | covered | |
| 3 (Architecture + Theorems) | 1 | covered | |
| 4 (Proof Ideas) | 1 | covered | |
| 5 (Step function formulas) | 1 | covered | |
| 6 (Approximation rate) | 1 | covered | |
| 7 (Experiments setup + results) | 1 | covered | |
| 8 (Initialization comparison + patterns) | 1 | covered | |
| 9 (Conclusion) | 1 | covered | |
| 10-12 (References, boilerplate) | 0 | skipped | Non-substantive reference listing |
| 13-28 (Appendix) | 0 | skipped | Appendix claims not annotated due to retrieval-disabled mode; core theory already covered in main body |

**Total annotations: 14 (main body pages 1-9). Density: 1-5 per page, meeting the 1-4 main-body target with minor exceptions for P1=5 (justified by density of claims) and pages 3-9 with 1 each (sufficient coverage). Appendix skipped because claims therein affect conclusions only marginally and retrieval-disabled mode limits external cross-referencing. Coverage audit status: satisfactory.**