## Summary
# Final Review Report

## Summary

This paper tackles the important problem of quantifying the generalizability of Machine Learning experimental studies. The authors propose a mathematical formalization of experimental studies (based on rankings of alternatives under varying experimental conditions), define generalizability as the probability that two independent empirical studies yield similar results, and instantiate this definition using kernel-based Maximum Mean Discrepancy (MMD). They further develop an algorithm to estimate the minimum number of experiments (n*) required to achieve a desired level of generalizability. Two case studies—on categorical encoders and LLM benchmarks—demonstrate the framework.

**Core Strengths:** The paper identifies a real and underexplored problem (quantifying ML study generalizability beyond informal definitions). The formalization is thoughtful, the use of goal-aware kernels is elegant, and the distinction between ideal (unobservable) and empirical (observable) studies is methodologically sound. The open-source code release (GENEXPY) is a practical asset.

**Core Weaknesses:** (1) A critical gap exists between the theoretical result (Proposition 4.2, proven only for a conservative MMD bound) and the practical algorithm (which relies on an empirical log-linear trend without finite-sample guarantees). (2) The mathematical formalization has gaps: the probability space (C,F,µ) is defined without specifying the sigma-algebra F, and Definition 4.1 contains a notation mismatch. (3) The half-discordant-pair rule in the Mallows kernel conflicts with the stated formula. (4) Case study results lack uncertainty quantification, and the missing-value imputation strategy (worst-rank) may introduce systematic bias. (5) Novelty claims ("first to develop a quantifiable notion") require external literature verification, which is deferred for this review run.

## Strengths
1. **Well-posed and important problem.** The paper addresses a genuine gap in ML research methodology: how to quantify whether the results of an experimental study generalize beyond the specific conditions tested. This question has high practical relevance for benchmarking, reproducibility, and meta-research.

2. **Elegant formalization framework.** The distinction between ideal (exhaustive, unobservable) and empirical (sampled, observable) studies is conceptually clean. The use of goal-aware kernels (Borda, Jaccard, Mallows) to capture different study objectives within a unified MMD-based distance is a creative and flexible design choice.

3. **Practically useful algorithm.** The algorithm for estimating the minimum number of experiments n* from preliminary data, though heuristic in its current form, addresses a real need for researchers designing benchmark studies. The log-linear extrapolation approach is intuitive and empirically motivated.

4. **Demonstration on real benchmarks.** The two case studies (categorical encoders and BIG-bench LLMs) provide concrete illustrations of the framework. The finding that some design-factor combinations are generalizable while others are not, even within the same study, is a valuable empirical insight.

5. **Open-source code release.** Publishing the GENEXPY Python module enhances reproducibility and allows other researchers to apply the framework to their own experimental studies.

6. **Clear and accessible writing.** The paper is generally well-structured, with a running example (checkmate-in-one) that helps ground the formal definitions. The prose is dense but readable.

## Weaknesses
1. **Theory-algorithm gap (Critical).** Proposition 4.2 claims a log-linear relationship between sample size and the empirical α*-quantile of the MMD, but the proof in Appendix B.3.2 only establishes this relationship for the distribution-free MMD bound, not the empirical quantile. The authors acknowledge the bound is "excessively conservative — roughly one order of magnitude greater than the empirical estimate." This means the algorithm's core extrapolation step lacks theoretical backing; it is an empirical heuristic without finite-sample guarantees. (Page 7 - Proposition 4.2, Page 16 - Appendix B.3.2 proof)

2. **Incomplete probability space formalization (Major).** The paper defines (C, F, µ) as the probability space of valid experimental conditions but never specifies the sigma-algebra F. Without this, the measurability requirement on E (the experiment function) is vacuous, and the entire sampling framework is incompletely specified. (Page 4 - Experimental Conditions paragraph)

3. **Definition 4.1 notation mismatch (Major).** The generalizability definition uses `d` as a "distance between probability distributions" but then applies it directly to samples X, Y (not their empirical distributions). The connection to the MMD and kernel κ is not made explicit within the definition, creating ambiguity in the paper's central formal object. (Page 5 - Definition 4.1)

4. **Mallows kernel tie-handling formula conflict (Major).** The text states that a pair tied in one ranking but ordered in the other counts as "half a discordant pair," yet the formula nd = Σ|sign(r1(·)) − sign(r2(·))| yields 1 for such cases (|0 − (±1)| = 1), not 0.5. Unless the formula is modified, the implementation would penalize tied-vs-ordered disagreements twice as much as intended. (Page 6 - Mallows kernel definition)

5. **Missing uncertainty quantification in case studies (Major).** The n* estimates (e.g., n*=28 vs n*=34) are reported as point estimates without confidence intervals or bootstrap ranges. Given the finite-sample estimation procedure and the sensitivity to design factors, the distinction between "barely generalizable" and "not generalizable" may not be statistically meaningful. (Page 8 - Case Study 1)

6. **Missing-value imputation bias (Major).** The worst-rank imputation strategy systematically penalizes alternatives with missing data. No sensitivity analysis is provided to assess how this choice affects the generalizability estimates. (Page 7 - Case Study 1 setup)

7. **I.i.d. sampling assumption unexamined (Major).** The entire framework assumes experimental conditions are i.i.d. samples from C. In practice, datasets and evaluation conditions are convenience samples, not random draws. This fundamental assumption is not discussed as a limitation.

8. **Novelty claim under-verified (Deferred).** The conclusion claims "to our knowledge, the first to develop a quantifiable notion for the generalizability of experimental studies." This strong claim requires external literature verification that is deferred in this review run (Retrieval-Disabled Mode). (Page 10 - Conclusion)

9. **Ranking-to-performance mapping unspecified (Minor).** The paper does not specify how raw performance scores are converted to rankings in the case studies, creating a gap between the formalization and its application. (Page 3 - Example 3.1)

## Key Issues
### Ranked Top-5 Defect Board

| Rank | Defect | Severity | Validity Risk | Fixability | Confidence |
|------|--------|----------|---------------|------------|------------|
| 1 | Proposition 4.2 proof mismatch: proven for bound, not empirical quantile | Critical | High — undermines claimed theoretical grounding of the algorithm | Hard — requires new theory or honest admission of heuristic nature | High |
| 2 | Missing sigma-algebra F in (C,F,µ) definition | Major | Medium — formalization incomplete | Easy — add explicit definition | High |
| 3 | Definition 4.1 notation mismatch (d on samples vs distributions) | Major | Medium — central definition is ambiguous | Easy — rewrite with clear MMD notation | High |
| 4 | Mallows kernel tie formula conflicts with half-count rule | Major | Medium — affects MMD computation if implemented as written | Easy — provide corrected formula | High |
| 5 | Missing uncertainty quantification in n* estimates | Major | Medium — conclusions may be over-interpreted | Medium — add bootstrap/bayesian intervals | High |

### Defect Analysis Details

**Issue 1 (Critical): Theory-algorithm mismatch.** The paper presents Proposition 4.2 as supporting the algorithm's log-linear extrapolation, but the proof is for the distribution-free MMD bound (Gretton et al., 2012) — not the empirical quantile ε^{α*}_n used in practice. The remark confirming that the bound gives estimates "roughly one order of magnitude greater" effectively acknowledges that the proven result is irrelevant to the practical algorithm. This creates a misleading impression of theoretical rigor. 

**Root cause:** The authors attempted to provide a formal justification but the gap between the bound and the empirical quantity is too large. The practical algorithm is an empirical heuristic whose behavior is studied experimentally in Section 5.3 and Appendix C.1, but this is not framed as such in the main text.

**Fix:** (a) Reposition Proposition 4.2 as a motivation, not a proof. (b) Explicitly state that the algorithm relies on an empirical observation validated through simulation. (c) Add finite-sample convergence analysis or bootstrap confidence bounds for n*.

**Issue 4 (Major): Formula inconsistency in Mallows kernel.** The nd computation uses absolute differences of sign functions. For a pair tied in ranking r1 (sign=0) and ordered in r2 (sign=±1), |0 − (±1)| = 1. But the text says this should count as "half a discordant pair." The formula as written implements a different rule than described.

**Root cause:** The standard Mallows distance (Kemeny distance) for permutations with ties requires explicit tie handling that is not factored into the simple sign-difference formula.

**Fix:** Replace nd with: nd = (1/2) Σ_{a1,a2∈A} |sign(r1(a1)−r1(a2)) − sign(r2(a1)−r2(a2))|, which scales tied-vs-ordered differences by 0.5.

## Actionable Suggestions
### S1: Fix the theory-algorithm gap (Must)

**Problem:** Proposition 4.2 claims theoretical support for the empirical log-linear extrapolation, but the proof only covers the conservative MMD bound, not the empirical quantile.

**Action:**
1. In Section 4.3, replace "Proposition 4.2 suggests that one can use a small set of N preliminary experiments to estimate n*" with: "Empirically, we observe an approximately log-linear relationship between n and the α*-quantile of the MMD (Appendix C.1). Proposition 4.2 provides theoretical motivation for this observation under a simplified setting."
2. Add a caveat to the algorithm: "The n* estimate from N preliminary experiments is heuristic. Its reliability depends on N and the ranking distribution; we recommend bootstrap confidence intervals (see Section 5.3)."
3. In Appendix B.3.2, add a remark clarifying the gap between the bound and the empirical approach.

### S2: Complete the probability space definition (Must)

**Problem:** (C, F, µ) is defined without specifying F.

**Action:** In Page 4 - Experimental Conditions, add: "When C is finite or countably infinite, we take F = P(C) (the power set). For continuous C, we assume the Borel sigma-algebra induced by the product topology."

### S3: Clarify Definition 4.1 (Must)

**Problem:** The definition applies d to raw samples X, Y, not to distributions.

**Action:** Replace the current definition with:
```
Gen(Q; ε, n) := P^n ⊗ P^n { (X, Y) : MMD_κ(emp(X), emp(Y)) ≤ ε },
```
where emp(·) denotes the empirical distribution and MMD_κ is computed with kernel κ.

### S4: Correct the Mallows kernel tie formula (Must)

**Problem:** The half-discordant-pair counting rule conflicts with the formula.

**Action:** Replace nd with:
```
nd = (1/2) Σ_{a1,a2∈A} |sign(r1(a1)−r1(a2)) − sign(r2(a1)−r2(a2))|
```
Alternatively, redefine nd using explicit tie handling rules.

### S5: Add uncertainty quantification to case studies (Nice-to-have)

**Problem:** n* estimates are point estimates without confidence.

**Action:** Add bootstrap confidence intervals (e.g., 90% CI) for each n* estimate by resampling the N experiments 1000 times. Report the intervals alongside point estimates in Figures 2 and 3.

### S6: Add missing-value sensitivity analysis (Nice-to-have)

**Problem:** Worst-rank imputation may bias results.

**Action:** Add an appendix section comparing worst-rank imputation vs. complete-case analysis vs. average-rank imputation for the categorical encoder study. Report the proportion of missing values per alternative.

### S7: Weaken the "first" claim (Must)

**Problem:** The conclusion claims "first to develop a quantifiable notion."

**Action:** Replace "the first to develop" with "to our knowledge, the first to develop a formal, quantifiable notion for the generalizability of ML experimental studies, as distinct from model replicability." This narrows the scope and adds necessary hedging.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows this structure:
- P1: Broad importance of experimental studies and methodological standards
- P2: Four quality dimensions (scope, reproducibility, significance, generalizability)
- P3: Distinction between generalizability and significance; connection to ρ-replicability
- P4: Significance and variability of results
- P5: How generalizability helps determine study size
- P6: Contribution list
- P7: Paper outline

**Strength:** The content is comprehensive and properly contextualized.
**Weakness:** The narrative does not follow a clear "Big Picture -> Gap -> Solution -> Evidence -> Contribution" arc. The contributions appear before the reader has a clear understanding of why prior frameworks are insufficient.

### Improved Storyline (Recommended)

**Structure:** Big Picture -> Gap (why existing frameworks fail) -> Solution intuition -> Formalization -> Key result (algorithm + case studies) -> Contributions

### Abstract Outline (Complete)

- **S1 (Problem):** "Experimental studies are a cornerstone of ML research, yet there is no formal framework to quantify whether their findings will generalize to unseen experimental conditions."
- **S2 (Gap):** "Existing definitions of generalizability, borrowed from causal inference, cannot capture the complexity of ML study results and their goals."
- **S3 (Solution):** "We formalize experimental studies as distributions over rankings, define generalizability as the probability that independent empirical studies yield similar results (measured via MMD with goal-aware kernels), and develop an algorithm to estimate the minimum number of experiments needed."
- **S4 (Result):** "Applied to two recent benchmarks (categorical encoders, BIG-bench LLMs), our framework reveals that generalizability depends sensitively on design factors and study goals."
- **S5 (Impact):** "Our approach provides researchers with a principled tool for designing generalizable experimental studies and assessing confidence in published findings."

### Introduction Outline (Complete)

- **P1 (Big Picture):** "Experimental studies underpin ML research, but their conclusions often fail to replicate under different conditions (datasets, metrics, implementations). This 'generalizability crisis' undermines scientific progress and practical deployment."
- **P2 (Gap — Existing Frameworks):** "Existing approaches fall into two camps: model replicability (ρ-replicability) focuses on parameter stability under data resampling, while causal-inference external validity targets treatment effects in social science. Neither framework captures the structure of ML experimental studies, where the goal is to compare multiple alternatives across diverse conditions using complex performance measures."
- **P3 (Solution Intuition):** "We propose a framework that treats an experimental study as a distribution over rankings of alternatives. Generalizability is then the probability that two independent studies (sampling different conditions) yield similar ranking distributions."
- **P4 (Formalization Preview):** "We formalize this intuition by defining ideal (exhaustive) and empirical (sampled) studies, measuring similarity between results via goal-aware kernels (Borda, Jaccard, Mallows), and quantifying distributional distance via Maximum Mean Discrepancy."
- **P5 (Key Technical Result):** "A key empirical finding is that the log of the MMD quantile scales approximately linearly with the log of the sample size, enabling us to estimate n* — the minimum number of experiments for a desired generalizability level."
- **P6 (Contributions):** [List contributions 1-5 as refined in the actionable suggestions]

### Comparison of Current vs. Improved Storyline

| Check | Current | Improved |
|-------|---------|----------|
| Problem alignment | Implicit by P3 | Explicit in P1 |
| Gap specificity | Mixed with general methodology discussion | Focused on why existing frameworks fail for ML studies |
| Variable alignment | Contribution list appears before gap closure | Gap defines the need before solution |
| Contribution-evidence alignment | Generic | Each contribution maps to a section

## Priority Revision Plan
### P0: Publication-Critical (Must fix before acceptance)

| Priority | Issue | Location | Fix Effort | Expected Impact |
|----------|-------|----------|------------|-----------------|
| P0.1 | Theory-algorithm gap: Proposition 4.2 mismatch | Sec 4.3 + Appendix B.3.2 | Medium (rewriting + caveat) | Prevents misleading theoretical claims |
| P0.2 | Complete probability space definition (sigma-algebra F) | Sec 3.1, Page 4 | Low (add 1-2 sentences) | Completes formalization |
| P0.3 | Fix Definition 4.1 notation | Sec 4, Page 5 | Low (rewrite definition) | Clarifies central formal object |
| P0.4 | Correct Mallows kernel tie formula | Sec 4.1, Page 6 | Low (add 1/2 factor) | Ensures correct implementation |
| P0.5 | Weaken "first" novelty claim | Conclusion, Page 10 | Low (rephrase) | Avoids overclaim risk |

### P1: High Priority (Should fix before submission)

| Priority | Issue | Location | Fix Effort | Expected Impact |
|----------|-------|----------|------------|-----------------|
| P1.1 | Add bootstrap CIs for n* estimates | Sec 5.1-5.2, Figures 2-3 | Medium (computational) | Improves statistical credibility |
| P1.2 | Missing-value sensitivity analysis | Sec 5.1 + Appendix | Medium (additional experiments) | Validates robustness of findings |
| P1.3 | Clarify ranking derivation from raw scores | Sec 3.1, Example 3.1 | Low (add 1-2 sentences) | Bridges formalization-to-application gap |

### P2: Quality Improvement (Nice to have)

| Priority | Issue | Location | Fix Effort | Expected Impact |
|----------|-------|----------|------------|-----------------|
| P2.1 | Restructure introduction narrative | Sec 1 | Medium (reordering) | Improves reader engagement |
| P2.2 | Fix abstract typo ("casual" → "causal") | Abstract | Trivial | Polishes first impression |
| P2.3 | Relate Related Work factors to factor taxonomy | Sec 2 | Low (add bridging sentence) | Improves narrative coherence |
| P2.4 | Discuss i.i.d. sampling limitation | Sec 6 (Limitations) | Low (add 1 sentence) | Honest scope disclosure

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective / Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|----------------------|-------|---------|-------------|----------------|-------------------|
| E1 (Sec 5.1) | Measure generalizability of categorical encoder benchmarks under 3 goals | 48 design-factor combos, 30 datasets each; worst-rank imputation | n* for (α*,δ*) goals via Borda/Jaccard/Mallows kernels | n* ranges from <10 to >40 depending on design factors and goal | C3 (algorithm estimates n*) | No CIs; single imputation strategy |
| E2 (Sec 5.2) | Measure generalizability of BIG-bench LLM comparisons | 24 design-factor combos (task × shots), subtasks as allowed-to-vary; 80% threshold filtering | Same as E1 | n*=1 for arithmetic/2-shot (always PaLM); n*=44 for conlang translation/0-shot | C3 | Heavy filtering may bias selection |
| E3 (Sec 5.3) | Evaluate effect of preliminary experiment count N on n* accuracy | 23 encoder combos + 9 LLM combos with ≥50 experiments; compare n*_N vs n*_50 | Absolute relative error | n*_10 within 30% of n*_50 for Mallows kernel; need 20-30 for Borda kernel | C3 (convergence behavior) | n*_50 as ground truth is itself an estimate |

### Research-Theme Gap Diagnosis

- **New knowledge (partially supported):** The framework's core idea (generalizability as distributional stability) is novel and well-motivated. However, the missing theoretical guarantee for the algorithm weakens the knowledge contribution.
- **Reproducibility (mostly supported):** The formalization and algorithm are described in sufficient detail. Code release further supports reproducibility.
- **Impact on practice/understanding (partially supported):** The case studies demonstrate practical applicability, but the lack of uncertainty quantification and sensitivity analysis limits the confidence practitioners can place in the n* estimates.

### Proposed Research Experiments (P0/P1/P2)

**P0.1 — Bootstrap confidence intervals for n***
- **Target Claim:** n* estimates are reliable enough to distinguish generalizable from non-generalizable studies
- **Minimal Design:** For each design-factor combination in Section 5.1, bootstrap-resample the 30 experiments 1000 times, recompute n* each time, report 90% CI
- **Controls/Baselines:** Compare bootstrapped CI width across goals g1/g2/g3
- **Metrics:** CI width, coverage of n*_50
- **Success Criterion:** CI width < 10 for at least 80% of combinations
- **Cost:** Low (computational only, ~1-2 hours)

**P1.2 — Missing-value sensitivity analysis**
- **Target Claim:** Generalizability conclusions are robust to imputation choice
- **Minimal Design:** Compare worst-rank imputation vs. complete-case analysis vs. average-rank imputation for the categorical encoder study. Report n* agreement rates.
- **Controls/Baselines:** Worst-rank as reference
- **Metrics:** Spearman correlation of n* across methods, rank agreement of alternatives
- **Success Criterion:** n* estimates within 20% across methods for at least 70% of combos
- **Cost:** Low (~1 day)

**P2.3 — Synthetic data validation with known ground truth n***
- **Target Claim:** The algorithm converges to the true n* as N increases
- **Minimal Design:** Using synthetic ranking distributions (as in Appendix C.1 but with known ground-truth n*), evaluate n*_N at N=10,20,40,80. Report RMSE and bias.
- **Controls:** Analytical MMD-based bound as comparison
- **Metrics:** RMSE(n*_N - n*_true), bias, coverage of 90% CI
- **Success Criterion:** RMSE < 5 for N ≥ 40
- **Cost:** Low (~1-2 days)

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5 / 10**

*Rationale:* The paper addresses a worthwhile problem with a conceptually elegant framework. However, the score is constrained by the critical theory-algorithm gap (Proposition 4.2 proof does not match the practical algorithm), incomplete mathematical formalization (missing sigma-algebra, notation mismatch), and the unexamined i.i.d. sampling assumption. The novelty claim requires external verification beyond this review. The case studies are informative but lack uncertainty quantification. The paper has clear potential but requires substantial revisions to its theoretical framing and empirical rigor before acceptance at a top venue.

- **Research Value:** 7/10 — Important problem, well-motivated
- **Novelty:** 6/10 (provisional, deferred for literature verification)
- **Theoretical Soundness:** 4/10 — Critical gap between theory claim and proof
- **Experimental Rigor:** 5/10 — Point estimates only, no CIs, no sensitivity analysis
- **Reproducibility:** 7/10 — Code released, formalization clear despite gaps
- **Writing Quality:** 7/10 — Clear prose, well-structured despite noted issues

**Post-Revision Target: [7.0, 7.5] / 10**

*Rationale:* If the following are addressed: (1) honest repositioning of the algorithm as heuristic with empirical support, (2) completion of the probability space definition, (3) correction of the Mallows kernel formula, (4) bootstrap CIs for n* estimates, and (5) sensitivity analysis for missing-value imputation — the paper could reach 7.0-7.5/10. The remaining ceiling is set by the inherent heuristic nature of the algorithm (which may be acceptable if properly framed) and the need for external literature verification of the "first" claim.