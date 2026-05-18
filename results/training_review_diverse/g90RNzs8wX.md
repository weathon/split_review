Now I have thoroughly read and cross-checked the paper against all the reviewer claims. Let me write the final consolidated review.

## Summary

This paper introduces UB-GOLD, the first unified benchmark bridging unsupervised Graph-Level Anomaly Detection (GLAD) and Graph-Level Out-of-Distribution Detection (GLOD) under a common "generalized graph-level OOD detection" framework. It compares 16 methods across 35 datasets spanning four realistic scenarios (intrinsic anomaly, class-based anomaly, inter-dataset shift, intra-dataset shift) and provides multi-dimensional analysis covering effectiveness, generalizability (near-OOD vs. far-OOD), robustness (training set contamination), and efficiency.

## Strengths

- **First unified benchmark bridging GLAD and GLOD.** The paper explicitly identifies that these two research areas "have been studied independently in the literature and have distinct evaluation setups" (Section 1, paragraph 2). It provides a formal generalized problem definition (Section 2) and systematically compares methods from both fields under one framework — a contribution no prior work has provided. This unification is the paper's central and genuine contribution.

- **Multi-dimensional analysis yields actionable insights beyond a leaderboard.** The benchmark evaluates generalizability (near-OOD vs. far-OOD, Fig. 4), robustness (training set contamination at 0–30%, Fig. 5), and efficiency (time and memory, Fig. 6) — not just a performance table. The finding that "near-OOD samples are harder to detect" (Observation 186) and that "end-to-end methods outperform 2-step methods in both performance and computational costs" (Observation 190) provide concrete guidance for practitioners.

- **Controlled robustness analysis models realistic data contamination.** The perturbation experiment (0%, 10%, 20%, 30% OOD contamination in the training set) is a practical stress test rarely performed in existing GLAD/GLOD evaluations. The differential sensitivity documented across methods (e.g., GLADC shows minimal degradation, OCGTL declines sharply on PROTEINS) is a useful finding for method selection under noisy training conditions.

## Weaknesses

### Fatal

None. The test-set tuning issue (detailed below) is a major methodological concern but does not invalidate the paper's core contribution — the unification framework, the four-scenario taxonomy, and the multi-dimensional analysis structure remain valuable. The key qualitative findings (near-OOD harder than far-OOD, end-to-end > 2-step, performance degrades with contamination) are relative patterns likely robust to the tuning protocol.

### Major

- **Hyperparameter tuning performed directly on the test set (Section 3.3, line 118).** The paper states: "we conduct a random search to find the optimal hyperparameters w.r.t. their performance on the testing set." This violates standard benchmarking practice: reported performance numbers reflect fit to test labels rather than genuine generalization. The paper frames this as obtaining "performance upper bounds" and cites OpenOOD as precedent, which is transparent but does not resolve the issue. Methods with more hyperparameters or higher tuning sensitivity are systematically advantaged. This concern propagates across all four research questions (RQ1–RQ3) since the same tuned models are used. The absolute rankings and performance claims in Table 1 and the key observation that "SOTA GLAD/GLOD methods show excellent performance" rest on numbers whose reliability as a benchmark for future comparison is compromised. The efficiency analysis (RQ4) is less affected as it uses default settings.

  *Why this is not fatal:* The paper is transparent about the practice; the core contribution (unification framework) is separate from the absolute numbers; and the relative qualitative findings (e.g., near-OOD > far-OOD difficulty, end-to-end > 2-step) are likely robust. The paper's value as a unified evaluation *framework* remains, even though the specific results need to be taken as upper bounds rather than realistic assessments.

### Minor

- **Standard deviations / confidence intervals not reported.** The paper states "5 runs of experiments" and reports averages (Section 4, line 143), but no measure of variability is given. This makes it difficult for readers to assess whether observed performance gaps between methods are meaningful. Adding std or error bars would substantially strengthen the benchmark's utility.

- **Inconsistency between performance and efficiency evaluation protocols.** The main performance comparison uses test-set-tuned hyperparameters, while the efficiency analysis (Section 4.4, line 232) uses default settings. This means the efficiency numbers do not exactly correspond to the models whose effectiveness is reported. The efficiency observations about architectural properties (e.g., kernel methods being slower) are likely robust, but the paper should clarify this mismatch.

- **Only two unsupervised GLOD methods are included (GOOD-D and GraphDE).** The paper acknowledges this limitation (Section 3.2) and scopes itself to unsupervised methods, excluding post-hoc approaches and label-dependent methods. This is a defensible scope choice, but the framing as a "comprehensive" benchmark for "GLAD and GLOD" should be read with this caveat — the GLOD coverage is thin relative to GLAD (6 methods).

- **Near-OOD definition partially recycles existing dataset types.** Setting A for the generalizability experiment defines intra-dataset samples with different class labels as near-OOD — this is effectively the class-based anomaly scenario (Type II) already part of GLAD. While the near-OOD vs. far-OOD comparison is still informative, it does not introduce a fundamentally new challenge beyond what the main evaluation already covers.

### Trivial

- None.

## Nice-to-Haves

- The paper would benefit from investigating *why* certain methods fail on near-OOD or under contamination — e.g., by analyzing learned representations or OOD scores — rather than only documenting the performance degradation. This would move from observation to explanation.

- Presenting results under both default and validation-tuned settings would give readers a sense of sensitivity to hyperparameter choice, addressing the test-set-tuning concern even if a full re-run is impractical.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Strength from Strength Finder: "Rigorous and reproducible experimental setup."** This claimed strength conflicts with the verified weakness about test-set tuning (the "rigorous" part is undermined). The reproducibility aspects (open-source codebase, 5 runs) remain positive but are not strong enough to counterbalance the tuning issue. Removed per the rule that when a strength and verified weakness disagree, the weakness wins.

- **Criticism about Table~\ref{tab:dataset} not being visible.** The harsh reviewer noted that this table is "referenced but not visible." In the original submission (not the parser-extracted text), this table exists. This is a parser artifact, not an author error. Removed per hard rules on missing appendix/table artifacts.

- **Criticism that the paper "lacks a discussion of the split definitions."** The paper explicitly states (line 116) "Detailed splits are provided in Table~\ref{tab:dataset}" and "we adopted the splits from Liu et al. (2023) and Li et al. (2022)." This is sufficient documentation. Removed as factually incorrect about what the paper contains.

- **Criticism that robustness results are "contingent on hyperparameters having been tuned on a now-contaminated test set."** The test set used for evaluation in the robustness experiment is the same clean test set; the *training* set is contaminated. The hyperparameters were tuned on the clean test set. The broader point that the robustness results inherit the test-set-tuning problem is valid and already captured in the Major weakness above. The specific inaccuracy about a "contaminated test set" is removed.

## Novel Insights

None beyond the paper's own contributions. The reviewer feedback does not surface an unarticulated insight that the paper itself does not already convey.

## Suggestions

1. **Address the test-set-tuning issue directly.** The most impactful fix is to adopt a proper validation protocol. In unsupervised anomaly/OOD detection, one can draw a held-out split from the ID training data and use an unsupervised criterion (e.g., reconstruction error, one-class score, or held-out likelihood) for model selection. Alternatively, report results under both default and validation-tuned settings and clearly flag which numbers are upper bounds vs. realistic assessments. Even a discussion acknowledging how this practice might affect the reported rankings (e.g., methods with fewer hyperparameters are less affected) would strengthen the paper.

2. **Add standard deviations or confidence intervals** to Table~\ref{tab:AUROC_optimization} or report per-run variability. Given 5 runs per method-dataset combination, this is straightforward and would substantially improve the benchmark's reliability assessment.

3. **Explicitly state in the abstract and introduction** that the reported performance numbers are "upper bounds obtained by tuning on test labels" rather than claims of true generalization performance, so readers immediately calibrate their expectations.

4. **Align the efficiency analysis protocol** with the performance analysis protocol, or at minimum acknowledge the mismatch and discuss whether it could affect the combined effectiveness-efficiency conclusions.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>