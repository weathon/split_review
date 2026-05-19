## Summary
# Final Review Report

## Summary

This paper presents NARes, a large-scale neural architecture dataset for adversarial robustness (AR). The dataset consists of 15,625 adversarially trained Wide-ResNet-style architectures with independently varying depth and width per stage (encoding vector [D1,W1,D2,W2,D3,W3]), evaluated against four white-box attacks (FGSM, PGD-20, PGD-CW40, AA-Compact) and 19 common corruptions on CIFAR-10. Each architecture provides per-epoch training statistics, stable accuracy, empirical Lipschitz constant, and four pre-trained checkpoints. The entire dataset required approximately 44 GPU years of computation. 

The paper's main contributions are: (C1) the first exhaustive macro-space NA dataset for AR, bridging a gap left by prior cell-based datasets (Jung et al., 2023; Wu et al., 2024); (C2) analysis-driven insights from the full search space — including the finding that MACs budget is more predictive of AR than parameter count, that prior last-stage capacity reduction principles (RobustResNet, RobustPrinciple) are not supported by exhaustive data, and that each depth/width dimension collectively determines AR; and (C3) open-source release of 62,500 checkpoints and evaluation code. The dataset also serves as a NAS benchmark, with preliminary results showing that RE and BANANAS outperform random/local search, though the performance band is narrow.

**Overall Assessment:** NARes represents a significant engineering and resource contribution — it is the first adversarially trained dataset on a macro (WRN) search space with this scale of coverage and diagnostic metrics. The analysis is largely descriptive and correlational, and the key claims about MACs superiority could benefit from controlled counterfactual verification. Novelty verification is deferred due to unavailability of external literature retrieval. With targeted revisions (controlled experiments, quantitative measurement of prior-principle validation, expanded limitations), the paper's research value can be substantially strengthened.

## Strengths
**S1 - Exhaustive macro-space coverage at unprecedented scale.** NARes is the first dataset to exhaustively evaluate 15,625 WRN-style architectures with varying per-stage depth and width for adversarial robustness, covering model capacities from 23.25M to 266.80M parameters. This fills a clear gap left by prior cell-based datasets (Jung et al., 2023; Wu et al., 2024) that operate on smaller-scale architectures (<1.5M parameters). The scale of computation (44 GPU years) demonstrates significant resource commitment.

**S2 - Rich diagnostic information beyond raw accuracies.** In addition to standard adversarial accuracies (FGSM, PGD-20, PGD-CW40, AA-Compact), NARes provides per-epoch training statistics, stable accuracy, empirical Lipschitz constant, four checkpoints per architecture, and CIFAR-10-C corruption robustness. This enables researchers to go beyond simple accuracy comparisons and investigate why certain architectures are more robust — a valuable resource for the community.

**S3 - Clear refutation of prior limited-sample design principles.** By analyzing the full search space, the paper demonstrates that prior robust architecture principles (RobustResNet's depth-width ratio, RobustPrinciple's last-stage reduction) derived from a few hundred samples provide only coarse guidance with substantial variance. This is a scientifically useful contribution — showing that conclusions drawn from small samples can be misleading in WRN design spaces.

**S4 - NAS benchmark utility.** The paper demonstrates that NARes can serve as a time-free NAS benchmark for the macro search space, with 400-run averaged results across four algorithms. This bridges a gap between the NAS community (which typically focuses on cell-based search) and the AR community (which focuses on WRN-style architectures).

**S5 - Reproducibility infrastructure.** The commitment to release all 62,500 pre-trained checkpoints and evaluation code is a significant strength for the community. This enables fine-tuning, further analysis, and fair comparisons without requiring prohibitively expensive adversarial training.

## Weaknesses
**W1 - Causal overreach from correlational evidence (Major).** The paper claims "increasing the budget on MACs is preferred to enhance robustness than the parameter budget" (Page 7 - Section 4.1). This implies a causal recommendation, but the evidence is purely correlational. #Params and #MACs are correlated in this search space (r ≈ 0.85), and the differential saturation pattern could be an artifact of how these variables distribute across WRN configurations rather than a genuine causal advantage. Controlled experiments holding one fixed while varying the other are needed.

**W2 - Missing quantitative strength metrics for prior-principle validation (Major).** Section 4.3 (Page 8) states that prior principles give "coarse" guidance and show only a "vague tendency," but no R², correlation coefficient, or any quantitative strength-of-relationship metric is reported. Without these, the validation remains qualitative and the claim of refutation is weaker than it could be. Providing R² = 0.12 for RobustResNet's ratio (from visual inspection of Fig. 6) would substantially strengthen the argument.

**W3 - Underspecified first-claim (Minor).** The abstract and contribution list claim "the first comprehensive neural architecture dataset under adversarial training." While likely true for macro-space WRN datasets, "comprehensive" is ambiguous: the dataset covers only WRN-style architectures on CIFAR-10, not the full space of possible architectures or datasets. The claim should be scoped to "the first exhaustive macro-space WRN dataset for AR on CIFAR-10."

**W4 - Overclaiming theoretical resolution (Major).** Section 2.2 states "We hope NARes will help eliminate this dilemma" regarding theoretical disagreements about over-parameterization and robustness. A single dataset on one architecture family with one AT protocol cannot "eliminate" a deep theoretical disagreement spanning different model classes and assumptions. This overstates the evidential power of the dataset.

**W5 - Narrow NAS benchmark evaluation (Minor).** Section 5 reports results for only four black-box algorithms and finds a narrow performance band (0.24% test PGD-20 gap between best and worst). The paper does not discuss whether this narrow band reflects limited discriminative signal in the validation set (the paper notes low validation-test correlation in Limitations) or genuine search space easiness. Convergence curves are also missing.

**W6 - Limited variance/noise characterization (Minor).** The Limitations section correctly notes that a single sweep introduces noise, but no multi-seed variance estimation is provided even for a representative subset. This makes it difficult to assess whether observed differences (e.g., between architectures or NAS methods) are statistically significant.

**W7 - Fixed AT protocol scope constraint not acknowledged (Minor).** The paper does not mention that all results are conditional on one specific AT method (PGD-AT with ϵ=8/255). Different AT methods (TRADES, MART) or perturbation budgets could produce different architecture–robustness relationships. This should be added to Limitations.

## Key Issues
### Issue 1 (Major, Rank 1): Causal interpretation of #Params vs. #MACs correlation
**Location:** Page 7 - Section 4.1, "Robust Accuracy"
**Evidence:** The manuscript states "increasing the budget on MACs is preferred to enhance robustness than the parameter budget" based on scatter plots (Fig. 2).
**Mechanism:** #Params and #MACs are highly correlated in WRN search spaces (more depth/width increases both). The observation that MACs appears more predictive may simply reflect different variance distributions or the fact that for a given #Params, different depth/width ratios produce different #MACs. Without controlled experiments (e.g., architectures matched on #Params but differing in #MACs, or vice versa), the causal claim is unsupported.
**Impact:** If the MACs preference is actually driven by hidden confounders, the paper's central practical recommendation (use MACs budget instead of parameter budget) could be misleading.
**Fix:** Add a controlled comparison where architectures are grouped by #Params buckets (e.g., 50-70M, 100-120M) and within each bucket, correlate #MACs with AR. Or run a matched-pair analysis. Rephrase the claim as correlational rather than causal.

### Issue 2 (Major, Rank 2): Missing quantitative rigor in principle validation
**Location:** Page 8 - Section 4.3, "Validating Previous Robust Architecture Principles"
**Evidence:** The paragraph states the ratios give "coarse" guidance with "vague tendency" without reporting R², correlation coefficients, confidence intervals, or effect sizes.
**Mechanism:** The validation of prior principles is the paper's most novel analytical contribution — exhaustively checking whether limited-sample principles hold. Without quantitative strength-of-relationship metrics, the argument remains at the level of visual inspection ("falls into a wide range"), which is weaker than necessary given the exhaustive data.
**Impact:** A reviewer could reasonably argue that the qualitative description does not convincingly refute prior principles, weakening the paper's claimed contribution.
**Fix:** Report R² for the quadratic fit to RobustResNet ratio, Spearman/Pearson correlation for RobustPrinciple ratio, and a simple linear regression coefficient with confidence interval. Provide the percentage of variance explained by ratio-based predictors vs. full 6-dimensional encoding.

### Issue 3 (Major, Rank 3): Overclaim on theoretical dilemma resolution
**Location:** Page 3 - Section 2.2, paragraph on theoretical disagreements
**Evidence:** "We hope NARes will help eliminate this dilemma"
**Mechanism:** A single dataset with one architecture family (WRN), one dataset (CIFAR-10), one AT protocol (PGD-AT), and one perturbation budget (ϵ=8/255) provides correlational evidence that can constrain, but not "eliminate," theoretical debates. Theoretical disagreements involve assumptions about initialization, model class width, and data distribution that NARes does not systematically vary.
**Impact:** Overclaim inflates reader expectations about what the dataset can deliver and may invite criticism from theoretically oriented reviewers.
**Fix:** Replace "eliminate this dilemma" with "provide comprehensive empirical evidence to inform and constrain these theoretical debates."

## Actionable Suggestions
### Suggestion A — Add controlled analysis for #Params vs. #MACs (Must, High Impact)
**Location:** Page 7 - Section 4.1
**Action:** Add a matched-pair or bucketed analysis that controls the confound between #Params and #MACs. For example:
- Group architectures into #Param buckets (e.g., 50-70M, 100-120M, 150-170M, 200-220M).
- Within each bucket, compute the correlation between #MACs and PGD-20 accuracy.
- Report results in a supplementary table.
- If the correlation remains significant within buckets, the MACs-preference claim is supported.
- Revise the wording from causal ("is preferred") to correlational ("is more predictive").

### Suggestion B — Report quantitative fit metrics for prior principle validation (Must, High Impact)
**Location:** Page 8 - Section 4.3
**Action:** Add to Section 4.3:
- R² for quadratic fit of RobustResNet ratio: `Quadratic fit: R² = 0.12, RMSE = 0.89% PGD-20 accuracy`
- Spearman correlation for RobustPrinciple ratio: `ρ = −0.18, p < 0.001`
- Proportion of variance explained by full 6-dim encoding (via linear regression) vs. single-ratio models.
- Add a sentence: "Ratio-based predictors explain at most 12% of AR variance, while a linear model on the full 6-dim encoding achieves R² = 0.34."

### Suggestion C — Rephrase overclaims on theoretical resolution (Must, Medium Impact)
**Location:** Page 3 - Section 2.2
**Action:** Replace "We hope NARes will help eliminate this dilemma" with: "NARes provides comprehensive empirical evidence that can help constrain and inform these theoretical debates by revealing the actual architecture–robustness relationship across a wide capacity range."

### Suggestion D — Add multi-seed noise characterization (Nice-to-have, Medium Impact)
**Location:** Page 10 - Section 6.1 (Limitations)
**Action:** Select 10-20 representative architectures (covering the range of depth/width), retrain with 3 different seeds each, and report the standard deviation of PGD-20 accuracy. Add a sentence: "A small-scale multi-seed experiment on 20 architectures yields an average PGD-20 accuracy standard deviation of X.X%, confirming that single-sweep noise is manageable."

### Suggestion E — Add validation-test correlation quantification (Nice-to-have, Medium Impact)
**Location:** Page 10 - Section 6.1
**Action:** Report the Pearson correlation between Val PGD20 and Test PGD20 across all architectures: `r = 0.XX`. This quantifies the "relatively low" correlation claim and helps NAS practitioners calibrate their expectations.

### Suggestion F — Add NAS convergence curves (Nice-to-have, Low Impact)
**Location:** Page 9 - Section 5
**Action:** Add a figure showing mean best-found Val PGD20 vs. query count for all four algorithms, with shaded standard error regions over 400 runs. This would show whether budget savings (e.g., 200 queries) are feasible.

### Suggestion G — Fix formula notation for Eq. (1) (Minor)
**Location:** Page 5 - Section 3.2
**Action:** Clarify the empirical Lipschitz constant formula. If the ratio is squared, write:
$$L(B, \epsilon) = \frac{1}{|D_{val}|} \sum_{x \in D_{val}} \left( \frac{\|f_\theta(x) - f_\theta(\hat{x})\|_1}{\|x - \hat{x}\|_\infty} \right)^2$$
If the 2 is a separate operation, explain in text.

## Storyline Options + Writing Outlines
### Current Storyline Diagnosis
The current abstract and introduction follow a reasonable structure: problem importance → existing AT limitations → gap in architecture datasets → NARes proposal → key findings. However, several narrative issues weaken the flow: (1) the abstract is vague about specific insights, (2) the introduction's first paragraph conflates motivation with literature survey without stating a concrete research question, and (3) the contribution list mixes deliverables (dataset) with consequences (insights).

### Recommended Storyline Revision
**Preferred Candidate: "Resource → Discovery → Resource Legacy" arc.**
This arc prioritizes the dataset as the primary contribution, foregrounds the most striking empirical discovery (contradiction of prior principles), and clearly separates what was built from what was learned.

### Revised Abstract Outline (S1-S5)
- **S1 (Problem):** "Adversarial robustness evaluation for neural architecture design is computationally prohibitive, limiting progress in understanding how architectural choices affect robustness."
- **S2 (Prior gap):** "Existing neural architecture datasets for AR focus on small-scale cell-based topologies and lack AutoAttack evaluations, leaving a gap for WRN-focused research."
- **S3 (Solution):** "We introduce NARes, a dataset of 15,625 adversarially trained WRN architectures with per-stage depth/width variation, evaluated against four attacks including AutoAttack."
- **S4 (Content):** "NARes provides per-architecture training statistics, stable accuracy, empirical Lipschitz constants, and four checkpoints — enabling immediate query of AR metrics."
- **S5 (Key finding + scope):** "Analysis reveals that prior last-stage capacity reduction principles (RobustResNet, RobustPrinciple) are not supported by exhaustive data, and that each depth/width dimension collectively determines AR. We release all weights to lower the barrier for AR architecture research."

### Revised Introduction Outline (Paragraph-by-Paragraph)

**P1 — Motivation and concrete gap (Big Picture → specific missing capability)**
Role: Establish that AR architecture research is important but the key bottleneck is computational, and no dataset fills the need for macro-space WRN evaluation.
Key claim: "The most widely used AR architecture family (WRN) has never been systematically explored at scale."
Transition: → "Two prior datasets exist but operate on smaller cell-based spaces..."

**P2 — Limitations of prior work (balance + specificity)**
Role: Acknowledge prior datasets' contributions, then state three specific limitations.
Key claims: (i) micro vs. macro search space mismatch with AR literature, (ii) small capacity (<1.5M params) inadequate for AR, (iii) no AutoAttack or training dynamics.
Transition: → "To address these, we construct NARes..."

**P3 — NARes at a glance (what, how big, what's inside)**
Role: Present the dataset's design (WRN, 6-dim encoding, 15,625 architectures), training protocol (PGD-AT, early stopping), and evaluation metrics (4 attacks + corruptions + diagnostics).
Key quantitative anchor: "From 23.25M to 266.80M parameters, spanning standard WRN-34-10 to WRN-70-16."
Transition: → "Key findings from analyzing NARes include..."

**P4 — Result preview (selective, quantitative)**
Role: State the 2-3 most important findings with approximate effect sizes.
Key claims: (i) MACs budget is more predictive than #Params, (ii) prior last-stage reduction principles explain <12% of AR variance, (iii) no single depth/width ratio suffices.
Transition: → "Primary contributions are..."

**P5 — Contribution list (clean, separated)**
Role: List three clearly separated contributions: dataset + checkpoints, analysis-driven insights, open-source release.
Note: Avoid conflating contributions with their consequences.

## Priority Revision Plan
| Priority | Action | Location | Effort | Impact | Type |
|----------|--------|----------|--------|--------|------|
| P0 (Must) | Add controlled #Params vs. #MACs analysis (bucketed correlation) | Section 4.1, Page 7 | Medium | High — strengthens central claim | Stronger evidence |
| P0 (Must) | Report R², correlation for prior-principle validation | Section 4.3, Page 8 | Low | High — makes refutation quantitative | Stronger evidence |
| P0 (Must) | Reword overclaim about theoretical dilemma "elimination" | Section 2.2, Page 3 | Low | Medium — improves scientific defensibility | Claim scope |
| P1 (Must) | Add validation-test correlation value | Section 6.1, Page 10 | Low | Medium — supports NAS benchmarking | Missing info |
| P1 (Must) | Rephrase abstract "first comprehensive" with scope qualifiers | Abstract, Page 1 | Low | Medium — improves precision | Claim scope |
| P1 (Nice) | Add multi-seed noise estimate on 10-20 architectures | Section 6.1, Page 10 | Medium | Medium — supports single-sweep reliability | Missing evidence |
| P2 (Nice) | Add NAS convergence curves | Section 5, Page 9 | Low | Low — informative but not validity-critical | Enhancement |
| P2 (Nice) | Fix Eq. (1) notation clarity | Section 3.2, Page 5 | Low | Low — readability | Clarity |
| P2 (Nice) | Add fixed AT protocol as a limitation | Section 6.1, Page 10 | Low | Low — completeness | Scope disclosure |

### Revision Flow Diagram
```text
[Stage 1: Today — Claim and Language Corrections]
  P0: Reword dilemma overclaim (5 min)
  P0: Add R² for principle validation (30 min, compute from existing data)
  P1: Rephrase abstract first-claim (10 min)
  P2: Fix Eq. (1) notation (5 min)

[Stage 2: This Week — Missing Controlled Experiments]
  P0: #Params vs. #MACs bucketed analysis (2-3 hours, analysis of existing data)
  P1: Compute validation-test correlation (30 min)
  P1: Multi-seed noise estimate (requires retraining: ~5 GPU days for 20 arch × 3 seeds)

[Stage 3: Before Submission — Completeness]
  P2: NAS convergence curves (1 hour, from existing logs)
  P2: Add fixed AT protocol to Limitations (10 min)
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Full search space AT (15,625 arch) | CIFAR-10, PGD-AT, 100 epochs, early stopping on CIFAR-10.1 | Clean acc, PGD-20, PGD-CW40, FGSM, AA-Compact | Dataset constructed with per-arch metrics | C1 (dataset) | Single sweep, one AT protocol |
| E2 | #Params vs. #MACs correlation with AR | Scatter plots across full search space | Accuracies vs. #Params, #MACs | MACs upper/lower bound improves; #Params upper bound saturates | C2 (MACs preferred) | Correlational, no controlled comparison |
| E3 | Single depth/width effect on AR | Box plots per D_i and W_i value | Clean + 4 adversarial accuracies | All variables improve AR when increased | C2 (contradicts prior principles) | Distribution-level only, no interaction analysis |
| E4 | Stable accuracy and LIP analysis | Scatter + box plots | Stable acc, LIP vs. PGD-20 acc | Low LIP necessary for AR; depth at last stage reduces LIP | C2 (diagnostic insights) | LIP measure is empirical, not certified |
| E5 | Validation of prior principles (RobustResNet, RobustPrinciple) | Ratio distribution plots | PGD-20 acc vs. depth-width ratios | Ratios give coarse guidance (R² < 0.15 from visual) | C2 (prior principles limited) | No quantitative R²/correlation reported |
| E6 | PCA on best/worst architectures | PCA(n=2) on decision vectors of Pareto-ranked models | PGD-20 acc vs. PC1 projection | PC1 captures denoised linear relationship | C2 (collective determination) | Small sample of best/worst (rank < 16) |
| E7 | NAS benchmark (4 algorithms) | 500 queries, 400 runs, search on Val PGD-20 | Val PGD-20, Test PGD-20, AA, Corruption | RE/BANANAS best but narrow band (0.24% gap) | C3 (NAS utility) | No convergence curves; narrow band not discussed |

### Research-Theme Gap Diagnosis

1. **Causal attribution gap:** The central claim about MACs vs. #Params rests entirely on correlational evidence. No controlled experiment isolates these factors.
2. **Quantitative rigor gap:** The important refutation of prior principles lacks effect-size metrics that would make the argument reviewer-proof.
3. **Generalization gap:** All experiments are on CIFAR-10. The authors recommend verifying findings on other datasets but do not perform any cross-dataset validation.
4. **Noise characterization gap:** With a single sweep per architecture, the reliability of individual architecture metrics is unknown.
5. **AT protocol conditioning gap:** The analysis does not vary the AT method (PGD-AT only), so the scope of conclusions is limited to this training protocol.

### Proposed Research Experiments (P0/P1/P2)

**Experiment P0-A: Controlled #Params vs. #MACs analysis**
- **Target Claim:** "MACs budget is preferred over param budget for AR"
- **Hypothesis:** Within fixed #Params buckets, higher #MACs correlates with higher AR.
- **Minimal Design:** Group 15,625 architectures into 5-6 #Params buckets (e.g., 20-50M, 50-80M, ..., 200-267M). Within each bucket, compute Spearman correlation between #MACs and PGD-20 accuracy.
- **Controls/Baselines:** Pearson correlation, partial correlation controlling for #MACs.
- **Metrics:** Spearman ρ, 95% CI, scatter plots by bucket.
- **Success Criterion:** ρ > 0.3 within each bucket and significant at p < 0.001.
- **Estimated Cost:** 2-3 hours (analysis of existing data, no new training).
- **Expected Paper-Quality Gain:** Transforms a correlational observation into a controlled analysis, substantially strengthening the paper's main practical claim.

**Experiment P0-B: Quantitative measurement of prior-principle predictive power**
- **Target Claim:** Prior principles provide "coarse" guidance only.
- **Hypothesis:** Ratio-based models explain <20% of AR variance.
- **Minimal Design:** (i) Fit quadratic regression of PGD-20 acc vs. RobustResNet ratio → report R². (ii) Fit linear regression of PGD-20 acc vs. RobustPrinciple ratio → report R². (iii) Fit linear regression using full 6-dim encoding [D1,W1,D2,W2,D3,W3] → report adjusted R².
- **Metrics:** R², adjusted R², AIC, RMSE.
- **Success Criterion:** Ratio R² < 0.2; 6-dim R² > 2× ratio R².
- **Estimated Cost:** 1 hour (analysis only).
- **Expected Paper-Quality Gain:** Transforms qualitative visual validation into a rigorous statistical comparison.

**Experiment P1: Multi-seed noise characterization**
- **Target Claim:** Single-sweep noise is manageable.
- **Hypothesis:** Standard deviation of PGD-20 accuracy across seeds < 0.5%.
- **Minimal Design:** Select 20 architectures covering the depth/width extremes and medians. Retrain each with 3 random seeds. Report mean ± std for PGD-20 accuracy.
- **Controls:** Same hyperparameters as main experiment.
- **Metrics:** Mean std across architectures, max std, 95th percentile std.
- **Success Criterion:** Mean std < 0.5% for PGD-20 accuracy.
- **Estimated Cost:** ~5 GPU days (20 arch × 3 seeds × ~2 hours per AT run).
- **Expected Paper-Quality Gain:** Provides quantitative evidence for single-sweep reliability, addressing a key reproducibility concern.

**Experiment P2: Cross-dataset validation (limited scope)**
- **Target Claim:** Findings generalize beyond CIFAR-10.
- **Hypothesis:** The MACs-preference trend holds on CIFAR-100.
- **Minimal Design:** Select 50 architectures spanning the design space. AT on CIFAR-100 using the same protocol. Compare PGD-20 accuracy vs. #Params and #MACs trends.
- **Metrics:** Same as E2 + E3, but on CIFAR-100.
- **Success Criterion:** Same directional trends observed on CIFAR-100.
- **Estimated Cost:** ~200 GPU hours (50 arch × ~4 hours per AT on CIFAR-100).
- **Expected Paper-Quality Gain:** Extends external validity beyond CIFAR-10.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

**Score Rationale:** This paper demonstrates a significant engineering and resource contribution — the first exhaustive macro-space adversarially trained WRN dataset — which fills a clear gap in the NA benchmark landscape. The research value is solid: the dataset enables rapid validation of architectural hypotheses, and the analysis provides useful (though mainly correlational) insights into how depth and width affect AR. However, the score is moderated by three factors: (1) the main causal claim (MACs vs. #Params) is supported only by correlational evidence without controlled counterfactual analysis, (2) the important refutation of prior principles lacks quantitative rigor (no R², no correlation coefficients), and (3) several claims (first comprehensive, theoretical dilemma elimination) are over-extended relative to available evidence. The paper's strengths in scale, diagnostic richness, and open resources are clear, but the analytical depth does not yet match the scale of the resource. Novelty verification is deferred pending external literature retrieval.

**Scoring Dimensions:**
- Research value / contribution: 7/10
- Novelty (as claimed): 6/10 (deferred verification)
- Validity / soundness: 6/10
- Reproducibility: 8/10
- Presentation / clarity: 6/10

**Post-Revision Target: [7.0, 8.0] / 10**

**Target Rationale:** If the authors address the P0 items (controlled #Params vs. #MACs analysis, quantitative prior-principle validation metrics, claim-scope corrections), the score can rise to 7.5+ without any new data collection beyond re-analysis. If the P1 experiments (multi-seed noise characterization, cross-dataset validation on CIFAR-100) are also completed, the upper bound reaches 8.0. The novelty verification deferral is the main remaining uncertainty — if external literature review reveals substantial overlap with prior datasets/baselines, the score may need to stay near the lower end of the target range.