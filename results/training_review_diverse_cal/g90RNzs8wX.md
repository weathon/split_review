Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper introduces UBGOD, a benchmark that unifies unsupervised graph-level anomaly detection (GLAD) and graph-level out-of-distribution detection (GLOD) under the umbrella of "generalized graph-level OOD detection." It compares 16 representative methods across 35 datasets spanning four scenarios (intrinsic anomaly, class-based anomaly, inter-dataset shift, intra-dataset shift), and evaluates them along four dimensions: effectiveness, generalizability (near-OOD vs. far-OOD), robustness (training set contamination), and efficiency. The paper also provides an open-source codebase.

## Strengths

- **First unified benchmark bridging GLAD and GLOD.** The paper is the first to systematically consolidate 16 methods from two previously siloed research areas under a common evaluation framework with standardized splits and protocols (Section 3). The conceptual unification, while not a new theoretical insight per se, is practically valuable for the community.

- **Large-scale and diverse dataset coverage.** The benchmark encompasses 35 datasets across four distinct detection scenarios (intrinsic anomaly, class-based anomaly, inter-dataset shift, intra-dataset shift), as detailed in Section 3.1 and Table 1. This diversity enables testing of generalizability and reveals meaningful heterogeneity in method performance (Observation 2: no universally superior method).

- **Multi-dimensional analysis beyond single-metric evaluation.** Rather than only reporting aggregate rankings, the paper separately analyzes effectiveness (RQ1, Section 4.1), generalizability to near-OOD vs. far-OOD (RQ2, Section 4.2), robustness to training set contamination (RQ3, Section 4.3), and time/memory efficiency (RQ4, Section 4.4). This provides a holistic picture not available in prior isolated evaluations.

- **Open-source codebase for community adoption.** The paper provides a unified codebase (listed as a contribution) to facilitate reproduction, quick implementation, and future extensions — a critical enabling resource for a benchmark paper.

## Weaknesses

### Fatal
None.

### Major

- **Hyperparameter search conducted on the test set (Section 3.3), undermining comparative conclusions.** The paper states: "To obtain the performance upper bounds of various methods on GLAD/GLOD tasks, we conduct a random search to find the optimal hyperparameters w.r.t. their performance on the testing set" (line 118). This is not a minor protocol choice — it fundamentally compromises the paper's comparative findings. The rankings, the identification of "SOTA" methods (Observation 1), the end-to-end vs. 2-step comparisons (Observation 4), and the near-OOD / far-OOD and robustness analyses all inherit this bias. Tuning on the test set rewards methods with more flexible hyperparameter spaces and larger search budgets, and yields overoptimistic estimates that may not generalize.

  The paper attempts to justify this by noting that anomaly/OOD labels are unavailable during training for unsupervised scenarios (line 116), which is true. However, this does not force test-set tuning — one could use a held-out portion of ID data with an unsupervised criterion (e.g., reconstruction loss, contrastive loss, anomaly score on ID-only validation) to guide hyperparameter selection. The paper frames the results as "upper bounds," yet draws definitive comparative conclusions (e.g., "SOTA GLAD/GLOD methods show excellent performance," "end-to-end methods consistently outperform 2-step methods") without clearly separating "upper bound" analysis from realistic comparison. This disconnect between the acknowledged limitation and the way results are interpreted is the paper's most significant flaw.

  **Why this is major, not fatal:** The benchmark framework itself (datasets, method collection, splits, codebase) remains a valuable contribution independent of the specific performance numbers. The flaw is fixable through re-running experiments with a proper validation protocol. However, the comparative conclusions in the current submission cannot be trusted.

### Minor

- **Key findings are primarily descriptive rather than diagnostic.** Observations such as "no universally superior method" (Observation 2) and "performance degrades with increasing contamination" (Observation 7) are essentially restatements of results. The paper would be stronger if it offered explanations for *why* certain methods work better on specific dataset types (e.g., intrinsic vs. class-based anomaly, near vs. far OOD). While descriptive benchmarking is acceptable and common, deeper diagnostic analysis would increase scientific depth.

- **No standard deviations in the main performance table.** The paper reports averaging 5 runs (line 143) but does not include standard deviations or confidence intervals in the main table (Table ~~1~~). Box plots in Figure 2 partially compensate by showing distributional information, but the numeric table should include variability measures — especially for a benchmark where readers need to assess whether observed differences between methods are meaningful.

- **The "unification" framing is slightly oversold.** The paper occasionally presents the GLAD/GLOD unification as a novelty (e.g., "first comprehensive and unified benchmark") when prior surveys (e.g., Yang et al. 2021) already group these tasks conceptually. The practical contribution — breadth of comparison and standardized evaluation — is genuine, but the framing slightly overstates the novelty of the unification itself.

### Trivial

None.

## Nice-to-Haves

- **Near-OOD / far-OOD analysis could control for confounding factors.** In the intra-inter dataset setting (Setting A), near-OOD and far-OOD differ not only in distribution shift distance but also in graph structure, size, and feature distributions. A more controlled study (e.g., using a single dataset with synthetic degrees of distribution shift) would strengthen the generalizability conclusions.

- **Robustness experiment (RQ3) acknowledges but does not address the test-set-tuning confound.** Since the robustness analysis uses the same test-set-tuned hyperparameters, the observed sensitivity could partly be an artifact of overfitting to clean test data. This should be explicitly discussed as a limitation.

- **Additional analysis explaining which method properties (e.g., contrastive learning, one-class classification, knowledge distillation) correlate with performance on specific dataset types** would make the findings more actionable for method developers.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"No code or data in the submission"** — Removed per hard rules: the paper cites the codebase as a contribution; questioning its existence or release status is not permitted.

- **"Conceptual unification is not a new insight" framing as a weakness** — Removed per hard rules: the paper's contribution is the benchmark, not a theoretical advance. Evaluating a benchmark paper against the expectation of novel theory is evaluating against the wrong paper class.

- **Various formatting/style nitpicks** — Removed per hard rules.

## Novel Insights

The most genuinely novel observation is that near-OOD detection is consistently harder than far-OOD detection across methods (Observation 5), and that GLOD methods exhibit a particularly large performance gap between near and far conditions in the intra-inter dataset setting (Observation 6). This suggests that current GLOD methods are learning dataset-specific distributional signatures rather than capturing the essential characteristics of ID data. This finding, if confirmed with a proper validation protocol, would be a useful challenge problem for the community. Otherwise, the paper's insights are largely consistent with what one would expect from aggregating prior isolated evaluations.

## Suggestions

1. **Replace test-set hyperparameter selection with a proper validation procedure.** The single highest-leverage improvement: use a held-out portion of ID data with an unsupervised criterion (e.g., reconstruction loss, contrastive loss, or a threshold on anomaly scores for an ID-only set) to select hyperparameters. If the authors wish to keep "upper bound" results, clearly separate them from the primary "fair comparison" results and do not use upper-bound-tuned numbers to draw comparative conclusions.

2. **Report standard deviations or confidence intervals** in the main performance tables (not just box plots) to help readers assess whether observed differences between methods are meaningful.

3. **Explicitly discuss the limitation** of test-set tuning and its impact on the comparative conclusions in the paper itself, not just in the implementation details section — especially when interpreting the key findings.

4. **Add a dedicated "limitations" or "caveats" paragraph** that addresses the generalizability of the findings given the experimental protocol choices.

## Score and Decision

**Score:** This paper addresses an important gap (unifying two siloed research areas) with a genuinely useful collection of datasets, methods, and code. The multi-dimensional evaluation framework is well-designed. However, the test-set hyperparameter tuning is a significant methodological flaw that makes the comparative conclusions unreliable for the paper's main claims. The benchmark framework itself remains valuable, but the paper as submitted cannot be accepted without addressing this issue.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>