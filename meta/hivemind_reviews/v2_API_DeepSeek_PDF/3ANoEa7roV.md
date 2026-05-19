## Summary
# Final Review Report

## Summary

This paper presents SynMeter, a systematic evaluation framework for tabular data synthesis (also called synthesizers), along with three proposed evaluation metrics covering fidelity (Wasserstein distance-based), privacy (Membership Disclosure Score, MDS), and utility (Machine Learning Affinity and Query Error). The authors evaluate 10 synthesizer variants (6 HP and 4 DP) across 12 real-world datasets and provide a unified tuning objective that consistently improves synthetic data quality. Key findings include: (i) diffusion models (TabDDPM) achieve the best fidelity and utility among HP synthesizers but present significant privacy risks; (ii) statistical methods (MST, PrivSyn) are more resilient under differential privacy constraints; (iii) the proposed MDS metric is more effective at distinguishing privacy risks than existing syntactic metrics and MIAs. The paper is well-motivated, technically sound in most parts, and makes a useful contribution toward standardized evaluation of tabular data synthesis. However, several issues in metric justification, causal attribution, and statistical rigor need to be addressed before publication.

## Strengths
1. **Comprehensive and well-structured evaluation framework.** The paper tackles an important problem — the lack of standardized evaluation for tabular data synthesis — with a systematic approach covering fidelity, privacy, and utility. The three-axis evaluation design is thorough and covers the key concerns of data synthesis practitioners.

2. **Novel privacy metric with clear advantages over existing approaches.** The Membership Disclosure Score (MDS) is well-motivated, addresses known limitations of syntactic metrics (e.g., DCR's algorithm-independence and instability), and is empirically shown to be more effective at distinguishing privacy risks across synthesizers than existing MIAs. The shadow training technique with max-over-records formulation is a principled adaptation of membership inference concepts to the data synthesis setting.

3. **Unified tuning objective that demonstrably improves synthetic data quality.** The proposal to include a weighted combination of fidelity, MLA, and query error as a tuning objective is simple yet effective, with Table 1 showing consistent improvements across all synthesizers (up to 13.67% for TabDDPM). This addresses a practical gap, as many existing synthesizers lack tuning guidelines.

4. **Extensive empirical evaluation across diverse settings.** The evaluation covers 10 synthesizer variants, 12 datasets with varying sizes, types, and distributions, and multiple evaluation configurations (HP vs DP, varying privacy budgets). The inclusion of HALF and HISTOGRAM baselines for fidelity and SELF for privacy provides useful empirical bounds for interpreting results.

5. **Useful and actionable findings for practitioners.** The paper distills its results into clear guidelines (e.g., statistical methods for privacy-critical applications, diffusion models when data quality is paramount), which are directly usable by practitioners selecting synthesizers for their applications.

## Weaknesses
1. **Categorical Wasserstein distance is terminologically misleading.** The paper acknowledges that using Wasserstein distance for categorical attributes (Equation 5) is "a slight misuse of terminology" because the cost function reduces to total variation distance (0/∞ cost). This undermines the claimed advantage of "faithfulness" and "structure-aware" measurement for categorical data. The metric's value is strongest for numerical and mixed-type marginals, but the paper's framing suggests a unified advantage across all types.

2. **High standard deviation erroneously cited as evidence of robustness.** In Section 5.2, the paper states MDS "demonstrates robustness as a reliable privacy evaluation metric, as evidenced by its high standard deviation" (Page 7, line 144). This is factually incorrect: high standard deviation indicates instability, not robustness. The actual data in Table 13 shows MDS has low standard deviations, suggesting a writing error. This mistake reduces confidence in the paper's precision.

3. **Causal attribution for TabDDPM's success is unverified.** The paper attributes TabDDPM's superior performance to diffusion models minimizing Wasserstein distance (citing Kwon et al., 2022). However, the cited result holds under specific conditions (early stopping, particular noise schedules), and no controlled experiment isolates whether the Wasserstein minimization property or other architectural choices (e.g., multinomial diffusion for categorical variables) drive the improvement.

4. **Tuning objective excludes privacy without sufficient justification.** The unified tuning objective L(A) excludes MDS, justified only as yielding "negligible improvements." This creates a systematic bias: hyperparameters are selected to optimize fidelity and utility, potentially at the expense of privacy. The paper does not demonstrate that including MDS in the objective would not change the ranking of synthesizers.

5. **Statistical significance testing is missing for key comparisons.** The paper reports MDS, fidelity, and utility scores with standard deviations but does not perform statistical significance tests to determine whether observed differences between synthesizers are meaningful. Several comparisons (e.g., MST vs PrivSyn on Adult: 0.031 vs 0.046) have overlapping error ranges, making the ranking claims fragile without significance testing.

6. **MLP and Transformers in the ablation (Figure 11) show surprisingly poor performance on real data.** In Figure 11, even the "Real Data" baseline achieves only ~0.65 F1 for MLP and Transformers on the Magic dataset. This suggests suboptimal tuning of these models, which could bias the MLA metric against synthesizers that better serve these particular architectures.

7. **Computational cost of MDS is understated.** The claim that MDS is "practical and efficient" relies on a citation that "tabular synthesizers can be trained in just a few minutes." This is not uniformly true: deep generative models (TabDDPM, REaLTabFormer) can take hours per model, and MDS requires 20 shadow models + 100 synthetic datasets per model. The paper's own stability analysis uses only three relatively fast synthesizers.

## Key Issues
**Issue 1 (Critical): Factual error — "high standard deviation as evidence of robustness" (Page 7, Section 5.2)**
The paper states that MDS "demonstrates robustness as a reliable privacy evaluation metric, as evidenced by its high standard deviation." A high standard deviation is evidence of instability, not robustness. The actual data (Table 13) shows MDS has *low* standard deviations (0.001-0.003), indicating the authors likely meant "low" but wrote "high" erroneously. This is a clear factual contradiction that must be corrected.
- **Fix:** Change "high standard deviation" to "low standard deviation."
- **Must fix before publication.**

**Issue 2 (Major): Categorical Wasserstein distance misrepresents metric advantage (Page 3, Section 3.1)**
The paper claims Wasserstein distance offers "faithfulness" and "universality" for all attribute types, but the categorical cost function (0/∞ for same/different) collapses to total variation distance. The claimed "structure-aware" advantage does not apply to categorical marginals, yet the paper's framing implies a uniform benefit. This needs an honest bounds clarification.
- **Fix:** Explicitly state that for categorical-only marginals, the metric is equivalent to TVD; the Wasserstein framing adds value primarily for numerical and mixed marginals.

**Issue 3 (Major): Tuning objective's exclusion of privacy creates systematic evaluation bias (Page 5-6, Section 4)**
The tuning objective L(A) = α₁Fidelity + α₂MLA + α₃QueryError explicitly excludes privacy, justified only by "incorporating MDS yields negligible improvements." This is a design choice that could systematically select hyperparameters optimizing data quality at privacy's expense. The paper should either empirically demonstrate that including MDS does not change ranking, or acknowledge this as a limitation.
- **Fix:** Add sensitivity analysis showing rankings are stable when MDS is included/excluded, or clarify that privacy is treated as a post-hoc constraint.

**Issue 4 (Major): Missing statistical significance testing for core evaluation comparisons (Pages 7->Page 8, Section 5.3)**
All evaluation tables (Tables 3-12) report only mean ± std without significance tests. Given multiple close comparisons (e.g., TabDDPM vs REaLTabFormer on fidelity), the ranking claims are not statistically grounded.
- **Fix:** Add pairwise significance tests (e.g., Welch's t-test) for key comparisons or use confidence intervals.

**Issue 5 (Major): Causal chain for TabDDPM advantage is asserted, not verified (Page 9, Section 5.4)**
The paper claims TabDDPM excels because diffusion models minimize Wasserstein distance, citing Kwon et al. (2022). However, the cited result is conditional on specific settings. No ablation isolates this mechanism from other factors (e.g., multinomial diffusion, architecture choices).
- **Fix:** Qualify the causal claim as a "plausible explanation" and optionally add a controlled experiment (e.g., comparing diffusion with alternative loss functions).

## Actionable Suggestions
### S1. Fix the "high standard deviation" factual error (Must)
**Location:** Page 7 - Section 5.2, line 144
**Current text:** "...as evidenced by its high standard deviation."
**Problem:** Contradicts basic statistics; high std dev indicates unreliability, not robustness.
**Fix:** Replace with "low standard deviation" or "consistently small variance."
**Revised sentence:** "...MDS effectively detects privacy risks across all scenarios and demonstrates robustness as a reliable privacy evaluation metric, as evidenced by its consistently low variance across repeated evaluations."

### S2. Clarify the scope of Wasserstein-based fidelity metric (Must)
**Location:** Page 3 - Section 3.1
**Problem:** The paper claims "faithfulness" and "universality" for categorical attributes, but the metric reduces to TVD for categorical data.
**Action:** Add an explicit sentence stating: "For categorical-only marginals, the proposed metric is equivalent to total variation distance; the Wasserstein framing provides geometric advantages primarily for numerical and mixed-type marginals, while maintaining a unified formulation across all types."
**Expected benefit:** Eliminates terminological concerns and accurately bounds the contribution.

### S3. Add statistical significance testing to evaluation tables (Nice-to-have, high impact)
**Location:** Pages 7-8, Section 5.3
**Problem:** Tables 3-12 report mean ± std without determining whether observed differences are statistically significant.
**Action:** Add a supplementary analysis (in Appendix) with pairwise significance tests. For the main text, add a brief note: "We performed Welch's t-tests (α=0.05) on key comparisons; differences > X were statistically significant."
**Expected benefit:** Provides readers with confidence in the ranking conclusions.

### S4. Revisit tuning objective design (Nice-to-have)
**Location:** Page 5-6, Section 4
**Problem:** Excluding MDS from tuning creates potential bias.
**Action:** 
- Run a sensitivity analysis with L' = L + α₄·MDS and check if optimal hyperparameters change.
- Report results in Appendix C.5 alongside existing coefficient analysis.
- If rankings are stable, cite this as evidence that the exclusion is harmless.
**Expected benefit:** Strengthens the claim that the tuning framework is unbiased.

### S5. Add controlled ablation to verify TabDDPM causal claim (Nice-to-have, low-cost proxy)
**Location:** Page 9, Section 5.4
**Problem:** The causal attribution (diffusion → Wasserstein minimization → better fidelity) is unverified.
**Action (minimal):** Run TabDDPM with its default diffusion loss replaced by a KL-divergence-based objective (keep architecture identical). If performance drops, this supports the Wasserstein hypothesis; if not, the mechanism is elsewhere.
**Expected benefit:** Provides direct evidence for the paper's central explanatory claim about why TabDDPM excels.

### S6. Abstract number consistency (Nice-to-have)
**Location:** Page 1 - Abstract
**Problem:** "8 synthesizers" vs actual count of 10 variants.
**Action:** Update to "10 synthesizer variants (6 HP and 4 with DP guarantees)."
**Expected benefit:** Eliminates a minor inconsistency that careful readers notice.

## Storyline Options + Writing Outlines
### Current Storyline Assessment
The paper follows a clear structure: motivation → problem statement → proposed metrics → framework → experiments → discussion. The narrative arc is logical and easy to follow. However, the Introduction could be strengthened by more explicitly stating the *concrete limitations* of existing metrics (rather than generic statements like "lack of principled metrics") and by more clearly separating the paper's three contributions.

### Abstract Outline (Revised)
**S1 (Problem):** "Tabular data synthesis is increasingly used to share data while protecting privacy, but evaluating the quality, privacy, and utility of synthesizers lacks standardized metrics."
**S2 (Gap):** "Existing evaluation metrics are either fragmented across incompatible statistical measures, algorithm-independent and unstable, or fail to capture worst-case privacy risks."
**S3 (Method):** "We introduce SynMeter, a systematic evaluation framework with three new metrics: a Wasserstein-based fidelity metric, a Membership Disclosure Score (MDS) for privacy, and Machine Learning Affinity (MLA) for utility."
**S4 (Tuning):** "We also propose a unified tuning objective that consistently improves synthetic data quality across all methods."
**S5 (Findings):** "Evaluating 10 synthesizers on 12 datasets reveals that diffusion models achieve the best fidelity but expose privacy risks, while statistical methods are more resilient under differential privacy — providing actionable guidance for practitioners."

### Introduction Outline (Revised, 4 paragraphs)

**P1 — Establish stakes and concrete problem**
*Role:* Define the practical importance of tabular data evaluation and state the specific crisis (no standard metrics → cannot compare synthesizers reliably).
*Transition:* "However, existing evaluation approaches suffer from three fundamental limitations..."

**P2 — Critique existing metrics with concrete examples**
*Role:* Explain *which* metrics fail and *how*. Provide one concrete example per metric category (e.g., DCR's algorithm-independence, MIA's inability to differentiate privacy levels, correlation statistics' incomparability across attribute types).
*Transition:* "To address these limitations, we propose three new evaluation metrics..."

**P3 — Present proposed metrics and framework**
*Role:* Introduce Wasserstein-based fidelity (unified across types), MDS (algorithm-aware, worst-case privacy), MLA+QueryError (model-agnostic utility). Briefly introduce SynMeter and the tuning objective.
*Transition:* "Using these metrics, we conduct the first large-scale systematic comparison..."

**P4 — Preview findings and contributions**
*Role:* State the key empirical results (TabDDPM best HP, MST best DP, MDS > DCR/MIAs, tuning improves all) and the practical guidelines.
*Transition to method:* "We first define the formal evaluation framework and metrics in Sections 2-3."

## Priority Revision Plan
The following plan is ranked by impact on scientific validity and publication readiness.

```text
ASCII Diagram — Revision Strategy Roadmap

[P0: Factual error fix]
  -> "high std dev" -> "low std dev" (Page 7, line 144)
  -> 15-minute fix, eliminates factual contradiction
  -> Expected: removes a clear scientific error

[P0: Wasserstein scope clarification]
  -> Add explicit note about categorical TVD equivalence (Page 3)
  -> 1-hour rewrite, aligns claim with evidence
  -> Expected: eliminates terminological vulnerability

[P1: Smoothing the "categorical Wasserstein = misuse" admission]
  -> Acknowledge that for categorical-only marginals, metric = TVD
  -> 2-hour rewrite + verification
  -> Expected: strengthens metric credibility

[P1: Add statistical significance to key comparisons]
  -> Welch's t-test or bootstrap CIs for top-3 ranking claims
  -> ~1 day for analysis + supplementary table
  -> Expected: provides readers with confidence in rankings

[P2: Tuning objective sensitivity analysis]
  -> Run L' = L + α₄·MDS and check ranking stability
  -> ~2 days computational work
  -> Expected: validates tuning design choice

[P2: TabDDPM causal mechanism ablation (optional)]
  -> Replace diffusion loss with KL-based loss, compare fidelity
  -> ~3 days if using existing codebase
  -> Expected: strengthens the paper's central explanatory claim
```

### P0 — Must fix before submission (highest impact)
| # | Issue | Location | Effort | Expected Benefit |
|---|-------|----------|--------|-----------------|
| 1 | "High std dev" factual error | Page 7, §5.2 | 15 min | Removes clear scientific error |
| 2 | Wasserstein scope for categorical attributes | Page 3, §3.1 | 1 hour | Eliminates terminological vulnerability |

### P1 — High priority (should fix)
| # | Issue | Location | Effort | Expected Benefit |
|---|-------|----------|--------|-----------------|
| 3 | Acknowledge categorical Wasserstein = TVD | Page 3, §3.1 | 1-2 hours | Strengthens metric credibility |
| 4 | Add statistical significance tests | Tables 3-12 | 1 day | Provides ranking analysis | Provides confidence in comparisons |

### P2 — Nice-to-have (improves robustness)
| # | Issue | Location | Effort | Expected Benefit |
|---|-------|----------|--------|-----------------|
| 5 | Tuning objective sensitivity w.r.t. MDS | §5.2 + Appendix C.5 | 2 days compute | Validates unbiased tuning |
| 6 | TabDDPM causal mechanism ablation | §5.4 | 3 days compute | Strengthens explanatory claim |
| 7 | Abstract + §5.1 numeric consistency | Page 1, §5.1 | 30 min | Eliminates inconsistency |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|--------------|-----------------|-------------------|
| E1 | MDS effectiveness vs DCR/MIAs | PATE-GAN with varying ε; TabDDPM with varying duplicate ratios | MDS, DCR, TPR@1%FPR | MDS distinguishes privacy risks where DCR/MIAs fail (Figure 2) | C2: MDS as privacy metric | Only tested on 2 synthesizers + 1 dataset |
| E2 | MDS stability | 3 synthesizers, varying shadow models (5-25) and synthetic datasets (25-125) | MDS variance | Converges at 20 models + 100 datasets (Figure 3) | C2: MDS practicality | Only tested on fast synthesizers |
| E3 | Tuning objective effectiveness | Grid search on all synthesizers, compare default vs tuned | Fidelity(Dtrain/Dtest), MLA, Query Error | All synthesizers improve with tuning (Table 1) | C3: SynMeter tuning | Privacy not included in tuning |
| E4 | HP synthesizer ranking | 6 HP synthesizers, 12 datasets | Fidelity, MDS, MLA, Query Error | TabDDPM/REaLTabFormer best fidelity/utility; worst privacy (Figure 4) | C1-C3: evaluation framework | No significance tests |
| E5 | DP synthesizer ranking | 4 DP synthesizers (ε=1), 12 datasets | Fidelity, MLA, Query Error | MST/PrivSyn outperform deep generative under DP (Figure 5) | C1-C3: evaluation framework | No significance tests |
| E6 | CTGAN failure analysis | Learning trajectory on Bean dataset | Wasserstein distance across marginal types | Stagnation in all marginal types (Figure 6a) | C1: fidelity metric utility | Only 1 dataset analyzed |
| E7 | TabDDPM success analysis | Learning trajectory on Bean dataset | Wasserstein distance across marginal types | Rapid decrease across all marginals | Rapid decrease (Figure 6b) | C1: fidelity metric utility | Causal attribution unverified |
| E8 | Privacy budget impact | 4 DP synthesizers, ε ∈ {0.1, 0.5, 1, 2, 4, 8} | Wasserstein distance, MLA | Statistical methods robust at small ε (Figure 7) | Practical guidelines | Only 1 dataset (Bean) |

### Research-Theme Gap Diagnosis

1. **Causal mechanism gap:** The paper explains *that* TabDDPM outperforms other methods, but not *why* at the mechanism level. The Wasserstein minimization hypothesis is plausible but unverified.
2. **Generalization gap:** MDS effectiveness is demonstrated on only a limited set of cases (2 synthesizers for comparison with DCR/MIAs; stability on 3 fast synthesizers). Broader validation is needed.
3. **Tuning-privacy tradeoff gap:** The paper separates tuning from privacy without fully exploring whether the optimal hyperparameters differ when privacy is included in the objective.

### Proposed Research Experiments

```text
ASCII Diagram — Experiment Upgrade Plan (P0/P1/P2)

P0 (before submission):
  ┌─────────────────────────────────────────────┐
  │ Add statistical significance tests to E4-E5  │
  │ Method: Welch's t-test on all pairwise      │
  │ comparisons in Tables 3-12                  │
  │ Expected: ranking confidence intervals      │
  └─────────────────────────────────────────────┘

P1 (before next revision):
  ┌─────────────────────────────────────────────┐
  │ Broaden MDS validation (add 2 datasets +   │
  │ 2 slow synthesizers)                       │
  │ Method: Repeat E1 on Shoppers + News with  │
  │ TabDDPM and REaLTabFormer                  │
  │ Expected: confirms MDS practicality         │
  └─────────────────────────────────────────────┘

P2 (optional):
  ┌─────────────────────────────────────────────┐
  │ TabDDPM mechanism ablation                 │
  │ Method: Replace diffusion loss with KL-based │
  │ objective, compare fidelity                 │
  │ Expected: supports or refutes causal claim  │
  └─────────────────────────────────────────────┘
```

**Proposed Experiment P1-A: Statistical significance for ranking comparisons**
- **Target Claim:** C1-C3 ranking conclusions
- **Hypothesis:** Top-ranked synthesizers (TabDDPM, MST) are statistically significantly better than alternatives.
- **Design:** For each pair of synthesizers, compute Welch's t-test on 20 repeated evaluations.
- **Success Criterion:** At least 80% of top-2 vs rest comparisons are significant at α=0.05.
- **Cost:** ~1 day for analysis + supplementary table.
- **Expected Gain:** Provides rigorous support for all ranking claims.

**Proposed Experiment P1-B: Broader MDS validation**
- **Target Claim:** C2 (MDS as reliable privacy metric)
- **Hypothesis:** MDS remains stable and discriminative for larger/slower synthesizers.
- **Design:** Repeat E1 with TabDDPM and REaLTabFormer on 2 additional datasets (Shoppers, News).
- **Success Criterion:** MDS variance <0.01 across runs; clear separation between HP and DP variants.
- **Cost:** ~3 days compute (20 shadow models × 2 synthesizers × 2 = 80 model-hours).
- **Expected Gain:** Generalizes MDS validation beyond fast statistical methods.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5/10**

The paper makes a solid contribution to the tabular data synthesis evaluation literature. The proposed metrics (Wasserstein-based fidelity, MDS privacy scoring) are well-motivated and empirically validated. The SynMeter framework with its unified tuning objective provides practical value. However, several issues prevent a higher score:

- **Research value (7/10):** The systematic evaluation framework and empirical findings are genuinely useful. However, the novelty contribution is primarily evaluative rather than methodological — the paper introduces new *ways to measure* rather than new *ways to synthesize*, which limits its theoretical contribution.
- **Novelty (6/10):** The combination of Wasserstein distance for fidelity + shadow model-based MDS for privacy is reasonably novel in the tabular data synthesis context. However, both components draw heavily on existing techniques (optimal transport, membership inference attacks). The paper's novelty lies in their integration and empirical comparison rather than individual invention.
- **Validity/soundness (6/10):** The evaluation is extensive and well-designed, but the "high standard deviation" factual error, unverified causal attribution for TabDDPM, and missing significance tests reduce confidence in some claims.
- **Reproducibility (7/10):** The paper provides implementation details, hyperparameter search spaces, and code availability. The evaluation protocol is clearly described.

**Post-Revision Target: [7.5, 8.0]/10**

If the authors address the P0 and P1 issues (fix the factual error, clarify Wasserstein scope, add significance testing, provide tuning sensitivity analysis), the score would increase substantially because:
- The factual error would be eliminated, restoring confidence.
- Significance testing would provide rigorous support for ranking claims.
- The tuning sensitivity analysis would validate the framework design.
- The categorical Wasserstein clarification would align claims with evidence.

A revised version with these fixes would be a strong contribution suitable for a top-tier venue.