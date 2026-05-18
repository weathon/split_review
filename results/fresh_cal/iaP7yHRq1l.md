Now I have a thorough understanding of the paper and can produce the consolidated review.

---

## Summary

This paper benchmarks 12 causal discovery algorithms (constraint-based, score-based, functional causal model-based, and differentiable/gradient-based) across 8 model-assumption violation scenarios (confounded, measurement error, unfaithful, autoregressive, heterogeneous, scale variation, missing data, mechanism violation). The authors execute over 70,000 experiments on more than 2,400 synthetic datasets and provide theoretical analysis (based on Loh & Bühlmann 2014) for linear differentiable methods under three misspecifications. The central finding is that differentiable methods exhibit competitive or optimal performance under most violations except scale variation, where they degrade.

---

## Strengths

1. **First extensive benchmark of differentiable methods under diverse assumption violations.** Prior work (Montagna et al., 2023) omitted differentiable methods entirely; Ng et al. (2024) evaluated differentiable methods but did not test misspecifications. This paper fills that gap with a large-scale study across 8 scenarios, 12 methods, and multiple graph types/sizes (ER, SF, GRP graphs with 10–50 nodes). The scope is clearly documented (Section 3.1.2 and lines 19–23 of Section 1).

2. **Novel investigation of nonlinear differentiable methods under scale variation.** Reisach et al. (2021) studied only linear methods under scale variation. This paper shows (Section 3.1.1, lines 108–114; Tables 3.1/3.2/4.1/4.2) that NOTEARS-MLP, GraN-DAG, and DAGMA also degrade under scale variation but still outperform PC and GES — a genuinely new finding.

3. **Fairer evaluation of CAM via an MLP-based nonlinear mechanism.** The paper identifies (Section 4.1.1) that CAM benefits from the GP-based nonlinear vanilla model, which aligns with CAM's assumptions. By introducing an MLP-parameterized mechanism (one hidden layer, size 100), the authors show NOTEARS-MLP outperforms CAM under almost all misspecifications, providing a more balanced comparison.

4. **Theoretical analysis for linear differentiable methods under three misspecifications.** Section 4.1.2 uses noise-ratio analysis (Loh & Bühlmann 2014, Theorems 7 and 9) to explain performance degradation under measurement error and unfaithful models, and maintained performance under missing data. This provides mechanistic insight beyond pure empirical results.

---

## Weaknesses

### Fatal
None. No verified weakness undermines the paper's core claims beyond repair.

### Major

- **Ambiguous hyperparameter selection protocol.** Section 3.3 reports tuning ranges for λ₁ and α, and Section 4 states: *"the hyperparameters for each method are determined as the optimal values relative to the specific dataset"* (line 147). No validation procedure (held-out set, cross-validation) is described. In a synthetic benchmark where ground truth is available, this implies oracle tuning — selecting hyperparameters that minimize the evaluation metric using knowledge of the true graph. This gives each method an optimistic upper bound and bypasses the real-world challenge of hyperparameter selection without ground truth. The paper should either (a) clarify whether a validation procedure was used and describe it, or (b) if oracle tuning was indeed used, acknowledge this as a limitation that inflates absolute performance numbers (though relative comparisons between methods remain meaningful, since all methods receive the same treatment).

- **Theoretical analysis covers only linear methods, while the paper's framing encompasses nonlinear methods.** Section 4.1.2 explicitly restricts its analysis to *linear* differentiable methods using least-squares scores (Loh & Bühlmann 2014). The paper's contributions (line 23) also specify "linear differentiable causal discovery methods." However, the title, abstract, and many high-level claims refer broadly to "differentiable causal discovery" without this qualifier. The nonlinear methods (NOTEARS-MLP, GraN-DAG, DAGMA) constitute a major part of the evaluation but receive no theoretical treatment. The paper would be stronger if it either extended the theoretical discussion to the nonlinear case (even conjecturally) or consistently separated the linear and nonlinear conclusions throughout.

- **The "mechanism violation" experiments are narrow in scope.** The conclusion that differentiable methods have a "significant advantage over CAM in all types of assumption violation scenarios except for scale variation" (Section 4.1.1, line 184) is drawn from the MLP setting with a single hidden layer of size 100. This is one nonlinear mechanism. Performance relative to CAM could differ under other nonlinear mechanisms (e.g., post-nonlinear models, different architectures). The claim should be tempered or supported by additional mechanism types.

### Minor

- **MEC evaluation bias is not discussed.** Following Zheng et al. (2018), the paper evaluates MEC-output methods (PC, GES, CAM) favorably by *"assuming the undirected edges in the MEC are in the correct direction"* (Section 3.4, line 140). This is a standard convention, but it gives an advantage to methods that only identify an equivalence class while penalizing differentiable methods that commit to directions. The paper should at minimum note this asymmetry and discuss whether the conclusions are robust to computing SHD/SID after converting all estimates to CPDAGs.

- **Main text shows only 10-node ER-2 results; full results are appendix-only.** The paper acknowledges this (line 147) due to space, and Figure 1 provides some aggregation. However, as a benchmark paper, the main findings would be more convincing if at least one additional graph size or density were summarized (e.g., average rank across all settings, or a concise aggregated table). Without this, it is difficult to assess whether the conclusions hold broadly or are specific to this configuration.

- **No statistical significance testing.** The paper reports means and standard deviations over 10 trials, but standard deviations often overlap substantially between methods. Claims like "always achieve optimal or competitive performance" (Section 4.1, line 154) would be strengthened by significance tests (e.g., Wilcoxon signed-rank tests comparing differentiable vs. non-differentiable groups across settings). The absence of such tests makes it hard to distinguish genuine differences from noise.

- **No code or reproducibility statement in the main text.** For a benchmark paper, a clear statement about code release, data generation code, and hyperparameter tuning details is essential. The appendix may contain this (it is stripped from the reviewed version), but the main text should include it.

- **Missing data procedure does not reflect realistic missing-data scenarios.** The paper's MCAR procedure deletes rows with missing values and regenerates data to keep sample size constant (Section 3.1.1, line 116). This isolates the effect of missingness from reduced sample size, which is a clean experimental design, but it does not match real-world settings where practitioners face smaller datasets. The paper should note this limitation.

### Trivial

- The tables (images) are dense and difficult to read. Graphical summaries (bar charts with error bars, heatmaps, or rank plots) would improve interpretability.
- Minor: The sentence about Sachs data (line 147) is truncated ("Sachs (Sachs et al."), suggesting the continuation is in the appendix. This should be resolved.

---

## Nice-to-Haves

- **Computational cost comparison.** Differentiable methods often scale better to large graphs than constraint-based methods. A runtime comparison would strengthen the practical-implementation argument made in Section 4.2.
- **Inclusion of a scale-invariant variant.** Citing Deng et al. (2024) on scale-invariant loss functions is informative, but the paper would be strengthened by experimentally testing at least one such variant.
- **Real-data validation.** The paper mentions the Sachs dataset (the main text sentence is truncated, suggesting the analysis is in the appendix). Including real-data results in the main text would add credibility to the claims about practical applicability.

---

## Removed Points

*These points were flagged in the source reviews but are removed from the main assessment with brief justification:*

- **"Hyperparameter ambiguity potentially invalidates the central empirical contribution"** (Harsh Critic, fatal framing). Removed: Oracle tuning in synthetic benchmarks is standard practice (e.g., Zheng et al. 2018, Lachapelle et al. 2019) and applies symmetrically to all compared methods. The relative comparison remains valid. The issue is retained as a Major weakness but not as fatal.

- **"MEC evaluation bias works against the claimed conclusion"** (Harsh Critic). Removed: The bias favors MEC methods (PC, GES), making it *harder* for differentiable methods to outperform them. If anything, this strengthens the paper's conclusion. The asymmetry is worth noting (retained as Minor) but the claim that it undermines the conclusion is incorrect.

- **"Dismissal of specialized methods is unsupported"** (Harsh Critic, on Section 1). Removed: This is introductory motivation, not a research claim. The paper's scope is clearly limited to i.i.d.-assuming methods.

- **"Does not test scale-invariant variants"** (Harsh Critic). Removed: The paper identifies scale variation as an open challenge and cites Deng et al. (2024) for a solution. A benchmark paper is not expected to solve every problem it documents.

- **"No comparison on real data"** and **"No discussion of computational cost"** (Harsh Critic). These are valid points but demoted to Nice-to-Haves, as the paper's core contribution is a controlled synthetic benchmark.

- **"Weak experimental design for mechanism violation"** (Harsh Critic, claiming PC/GES are agnostic to linearity). Removed: The mechanism-violation setup (linear data → nonlinear methods, nonlinear data → linear methods) follows established practice (Montagna et al. 2023). Some methods (PC, GES) use nonparametric tests and are indeed more agnostic, but the setup still violates the structural assumptions of methods that assume specific functional forms. The paper's conclusions about mechanism violation already acknowledge this nuance.

- **Generic/superficial strengths** from Strength Finder: general statements about "addressing an important problem" or "targeting an interesting question" are removed as they lack concrete evidence specific to this paper.

- **"These specifically designed algorithms also cannot be effectively employed for real data" asserted without evidence** (Harsh Critic, Section-by-Section). Removed: This is a brief introductory claim establishing motivation, not a core finding requiring empirical support.

---

## Novel Insights

The reviewers' critiques converge on one useful observation that goes beyond what the paper itself says: the paper's evidence for robustness is strongest when comparing methods within the same evaluation regime (oracle-tuned, same metric), but the paper's claims about *practical* robustness are weakened by the lack of non-oracle hyperparameter selection. This tension between a best-case benchmark and real-world applicability is common in the field, and the paper would benefit from explicitly discussing it rather than letting the ambiguity linger. The fact that differentiable methods remain competitive even when MEC-output methods receive favorable evaluation (undirected edges treated as correct) is an under-exploited argument in the paper's favor.

---

## Suggestions

1. **Clarify the hyperparameter selection protocol explicitly.** State whether the true graph was used to select hyperparameters. If so, note that this provides an upper bound and discuss how the comparison remains fair (all methods receive the same treatment). If a validation-based procedure was used, describe it.
2. **Add statistical significance comparisons** (e.g., average rank across all settings, or paired tests comparing differentiable vs. non-differentiable groups) to support claims of "optimal or competitive" performance.
3. **Show one additional summary in the main text** — e.g., average rank across all graph sizes/densities — to demonstrate that the 10-node ER-2 conclusions generalize.
4. **Scope the theoretical claims consistently.** Either add a brief discussion of nonlinear methods in the theory section, or modify high-level language to consistently say "linear differentiable methods" where theory applies.
5. **Discuss the MEC evaluation bias** and, if feasible, show that conclusions are robust when converting all estimates to CPDAGs before computing SHD.

---

## Score and Decision

**Originality:** 7/10 — First benchmark of differentiable methods under misspecification; fills a clear gap.  
**Importance of question:** 8/10 — Robustness of causal discovery is practically critical.  
**Claims well-supported:** 6/10 — Large experimental scope, but hyperparameter ambiguity and narrow main-text presentation weaken support.  
**Soundness of experiments:** 7/10 — Well-designed data generation and comprehensive scenarios, but oracle-tuning protocol and lack of significance testing reduce rigor.  
**Clarity:** 6/10 — Dense tables and truncated sentences hinder readability; scope ambiguity between linear vs. nonlinear theory.  
**Value to community:** 8/10 — The benchmarks, findings about scale variation in nonlinear methods, and CAM-MLP comparison will be useful reference points.

The paper makes a genuine contribution with a large-scale, well-motivated benchmark. The weaknesses are real but addressable: they concern clarity, scope of presentation, and protocol transparency rather than fatal methodological flaws. The core finding — that differentiable methods are broadly robust under misspecification except scale variation — is supported by the evidence as presented, albeit with caveats about oracle tuning.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>