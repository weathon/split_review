Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper identifies a confound in prior safe semi-supervised learning (SSL) evaluations: previous work fixed the total size of the unlabeled set while varying the proportion of unseen-class data, thereby simultaneously changing the amount of seen-class data and creating a spurious correlation. The authors propose RE-SSL, a corrected evaluation framework that holds seen-class unlabeled data constant while varying only unseen-class data. Using 15 algorithms, five evaluation metrics (R_slope, GM, WAD, BAD, P_AD≥0), and experiments across five factors (sample count, category count, category index, nearness, label distribution), they demonstrate that unseen-class unlabeled data does not necessarily harm SSL performance and can sometimes be beneficial.

## Strengths

1. **Clear identification of a confound in prior safe SSL evaluations.** Section 1 and Figures 1–2 present a structural causal model showing that fixing total unlabeled size while varying unseen-class proportion creates a confound between seen-class and unseen-class data. This is a conceptually sound and important methodological correction to the standard evaluation practice in safe SSL.

2. **Controlled-variable evaluation framework (RE-SSL).** Section 3.1 and Figure 2b describe a dataset construction that fixes \(r_s\) (seen-class proportion) and varies only \(r_u\) (unseen-class proportion), directly addressing the identified confound. This provides a principled template for future evaluations in this area.

3. **Systematic multi-factor empirical study.** The paper evaluates 15 SSL algorithms across five dimensions (Sections 5.3–5.4, Tables 1–6): sample-number, category-number, category-index, nearness, and label distribution. This breadth substantially exceeds prior safe-SSL studies and reveals that different algorithms respond differently to different factors.

4. **Empirical evidence that unseen classes can improve SSL performance.** Tables 1 and 2 report positive WAD/BAD values for several methods (e.g., ICT on CIFAR-10: WAD=0.010; FlexMatch on CIFAR-10: BAD=0.166), directly contradicting the prior assumption that unseen classes always degrade performance. Section 5.3 documents these cases with concrete metrics.

5. **Characterization of algorithm-specific robustness profiles.** Table 6 and the analysis in Section 5.3 identify which algorithms are consistently robust (PseudoLabel, ICT, UASD, CAFA) and which are sensitive (FixMatch, OpenMatch, FreeMatch). This offers actionable guidance for model selection when unseen classes are expected.

## Weaknesses

### Fatal
None.

### Major

1. **No direct empirical comparison between the old protocol and RE-SSL.** The paper's central narrative is that prior evaluations are "flawed" and produce "misleading conclusions" (line 4). However, the paper does not actually run any algorithm under the old (confounded) protocol and compare the results to the new protocol to demonstrate that the conclusions would differ. The critique is logically well-motivated (Figures 1–2), but the paper would be substantially stronger if it showed—for at least one representative algorithm like FixMatch—that the old protocol suggests a steep accuracy decline while RE-SSL shows a flat or positive trend. Without this comparison, the claim that prior conclusions were wrong remains theoretical rather than empirically demonstrated.

2. **Confounded nearness experiment (CIFAR-10 vs. MNIST).** The nearness experiment compares near OOD (CIFAR-10 unseen classes from the same dataset) with far OOD (MNIST, a different dataset) in Table 4 and Section 5.4 (lines 161–163). This comparison simultaneously changes dataset resolution, color space (RGB vs. grayscale), domain, and label semantics. The paper states "the smaller the semantic shift and distribution shift from the seen classes to the unseen classes, the less damage to the SSL models" and calls this conclusion "clearly valid" (line 163). This conclusion is plausible but not rigorously supported by the confounded design. A controlled comparison—e.g., using CIFAR-100 subclasses with varying semantic distance, or synthetically perturbed versions of the same data—would be more informative. This does not invalidate the paper's core contribution but weakens one specific empirical claim.

3. **Arbitrary thresholds in the robustness definitions.** Definitions 1 and 2 define global and local robustness in terms of thresholds \(\delta_g\), \(\delta_w\), and \(\delta_b\). In the analysis (Section 5.3, line 128), the paper states "assume that \(\sigma_g\) equals -0.020" (notation inconsistency: \(\sigma_g\) vs. \(\delta_g\)) with **no justification** for this specific value. The reader has no way to assess whether -0.020 is meaningful, conservative, or arbitrary. The definitions would be more useful either without thresholds (as continuous comparisons) or with a principled choice anchored to statistical significance, empirical distribution across algorithms, or practical significance.

### Minor

1. **Missing error bars / standard deviations.** All tables report average accuracy over three seeds without any measure of variance (e.g., standard deviation or confidence intervals). Given that some claims depend on trends (e.g., FixMatch's sharp decline at \(C_n=4\) in Table 3), the absence of variance information makes it difficult to assess whether observed differences are reliable or driven by noise.

2. **Unilateral favorable-asymmetry in the comparison fairness rule.** The paper's framework always benefits the baselines when there is any asymmetry in comparison. While this ensures fairness toward prior methods, it sets a high bar for demonstrating improvement. This is more of a design choice than a flaw, but it should be explicitly acknowledged as a limitation, as it could obscure scenarios where the proposed method genuinely outperforms baselines on measures not covered by the established evaluation criteria.

### Trivial

- The notation inconsistency between \(\sigma_g\) (used in the analysis, line 128) and \(\delta_g\) (used in Definition 1, line 94) for the same threshold should be resolved.
- The set of \(r\) values {0, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0} is irregularly spaced (note the 0.4→0.5→0.6 cluster). Some justification for this choice would be helpful but is not essential.

## Nice-to-Haves

- The paper notes that accuracy sometimes *increases* as the number of unseen categories grows (Table 3, line 155) and that some methods show trends under imbalanced label distributions (Table 5, line 170). These interesting phenomena are reported but not explained. A brief discussion of possible mechanisms (e.g., regularization effects, improved feature learning via diversity) would enrich the analysis.
- The structural causal model (Figure 1) is used only for motivation. The paper could note that it is an illustrative causal graph rather than a quantitative causal inference model, to preempt overclaim concerns.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The claim that the paper 'pioneers a structural causal model' is overblown"** (harsh critic). The paper does use this phrasing (line 196). However, evaluating rhetorical flair is a style judgment, not a scientific weakness. The paper's contribution is the controlled-variable insight, not the causal graph per se. Removed as a style nitpick rather than a substantive flaw.
- **"Does not discuss the possibility that seen-class unlabeled data may itself have distribution shift"** (harsh critic). The paper explicitly acknowledges this in Section 7 (Line 189): "seen classes in unlabeled data may also experience shifts in feature and label distributions." Removed because the paper already addresses it.
- **"The definition of local robustness for BAD seems to define best-case robustness"** (harsh critic). The paper's naming is consistent: BAD measures the most positive change (best-case). Removed as a misinterpretation — the paper is correct.
- **"Missing related works"** (implied). Removed per instructions: I do not have external sources to verify whether works are missing.
- **Various formatting nitpicks** (harsh critic's section-by-section notes about figure placement, etc.). Removed as parser artifacts or style issues.
- **Strength Finder strengths that are generic or sycophantic** — none of the six listed strengths fall into this category; all are concrete and evidence-backed.

## Novel Insights

None beyond the paper's own contributions. The key insight — that prior safe-SSL evaluations confounded seen-class and unseen-class data by fixing total unlabeled size — is the paper's own contribution, not a synthesis from the reviews. The reviewers' perspectives converge on three corrigible weaknesses (missing old-vs-new comparison, confounded nearness experiment, arbitrary thresholds) but do not add an unanticipated analytical angle beyond what the paper already provides.

## Suggestions

1. **Run a direct comparison experiment (highest priority).** Pick 2–3 representative algorithms (e.g., FixMatch, ICT, PseudoLabel), evaluate them under both the old protocol (fix total unlabeled size, vary \(r_u\)) and RE-SSL (fix \(r_s\), vary \(r_u\)), and plot accuracy vs. \(r_u\) for both. If the old protocol shows a steep decline while RE-SSL shows a flat/positive trend, this would dramatically reinforce the paper's thesis.
2. **Justify or remove the thresholds in Definitions 1–2.** Either anchor \(\delta_g\) to statistical significance (e.g., the standard error of the R_slope estimate across seeds) or practical significance (e.g., what slope corresponds to a 1% accuracy drop over the full range), or remove the thresholds from the definitions and simply report continuous values.
3. **Redesign the nearness experiment or downgrade the claim.** Use a controlled setting such as selecting semantically closer/farther unseen classes within CIFAR-100, or using corrupted/augmented versions of the same data to vary "nearness" without changing dataset domain. Alternatively, acknowledge the confound explicitly in the limitations and soften the conclusion.
4. **Add error bars** to all tables showing average accuracy or R_slope values, using the three random seeds already collected.

## Score and Decision

This paper makes a genuine and well-motivated methodological contribution: it identifies a real confound in prior safe-SSL evaluations and proposes a corrected framework. The empirical study is broad (15 algorithms, 5 factors) and produces useful findings (e.g., that unseen classes can sometimes improve performance). The three major weaknesses are corrigible and do not invalidate the core insight. However, the paper would be substantially stronger if it empirically demonstrated that the old protocol produces different conclusions, which is central to its narrative. The threshold issue and the confounded nearness experiment are secondary but should be addressed.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>