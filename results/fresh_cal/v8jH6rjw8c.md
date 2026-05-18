Now I have all the information needed. Let me write the consolidated final review.

## Summary

This paper addresses the problem of learning from data that is simultaneously long-tailed and noisily labeled. The authors first empirically demonstrate that existing robust methods have disparate impacts on different sub-populations (head vs. tail). They then propose a **Fairness Regularizer (FR)** that penalizes performance gaps between sub-populations, added as a differentiable penalty on top of any base loss function. Experiments on CIFAR-10, CIFAR-100, CIFAR-10N, CIFAR-100N, Animal-10N, and Clothing1M show that adding FR (especially the G2 variant with a head/tail split) yields consistent accuracy improvements across six base methods.

## Strengths

1. **Well-motivated and clearly motivated problem.** The observation in Figure 1 (Section 3) — that existing robust methods for noisy or long-tailed data improve some sub-populations at the cost of hurting others — is concretely demonstrated and provides a compelling rationale for the fairness perspective. The empirical analysis in Section 3 (influence functions at both population and sample levels) independently grounds the approach.

2. **Simple, plug-in regularizer with broad compatibility.** FR is a single differentiable term added to any existing loss. The paper evaluates it on 6 base methods (CE, LS, NLS, Focal, PL, Logit-adj) across 48 synthetic settings and 4 real-world datasets. This breadth of testing demonstrates the method's general applicability.

3. **Consistent positive trends, especially for FR(G2).** In Table 1, CE+FR(G2) improves over CE in 22/24 settings (CIFAR-10 and CIFAR-100, both noise types). The paired t-test in Table 2 shows statistically significant (p<0.1) positive improvements in 11/12 method-dataset combinations for FR(G2). Real-world datasets in Table 3 show consistent gains, including notable ones (e.g., +5.9 points for Logit-adj on Animal-10N at r=100).

4. **Demonstrates improvement specifically on tail classes.** Figure 5 visualizes per-class accuracy changes and confirms that FR boosts the worst-performing (tail) sub-populations while rarely harming head classes, directly supporting the paper's claimed mechanism.

5. **Validated on real-world noisy long-tailed datasets.** Experiments on CIFAR-10N (3 noise levels), CIFAR-100N, CIFAR-20N, Animal-10N, and Clothing1M show the method generalizes beyond synthetic noise settings.

## Weaknesses

### Major

1. **No standard deviations or confidence intervals reported for any individual experiment.** All tables report single accuracy numbers. Many improvements are small (e.g., 80.46 vs 79.75 on CIFAR-10, +0.3–0.5% on Clothing1M). Without variance estimates, it is impossible to assess whether these differences are within run-to-run noise. The pooled t-test (Table 2) aggregates across 12 heterogeneous settings per dataset (different noise types, imbalance ratios), which does not substitute for per-experiment uncertainty reporting. This is the single most consequential evidential gap in the paper.

2. **No experimental comparison against methods specifically designed for the joint long-tailed + noisy label problem.** The related work (line 42) cites Wei et al. 2021, Karthik et al. 2021, and Zhong et al. 2019 as decoupled approaches that address both problems jointly. The evaluation compares FR+baseline only against the baseline alone — not against these existing joint methods. While FR is framed as a plug-in regularizer, the paper's central claim is about "improving learning from noisily labeled long-tailed data," and a reader cannot assess whether the gains from FR match, exceed, or fall short of the strongest existing approaches to this exact problem.

### Minor

3. **Theoretical justification is too thin to support the paper's framing.** The "observation" on line 193–197 (binary Gaussian example showing fairness constraints return the Bayes optimal classifier) is a toy illustration, not a general theorem. It is not connected to the proposed relaxation (which replaces accuracy with prediction confidence). The paper's title and introduction claim to "theoretically show" something, but the theoretical content is minimal. This is not fatal for an empirical paper, but the framing overstates what is delivered.

4. **Method success depends on the sub-population split, with limited guidance.** FR(KNN) works on CIFAR-10 but often degrades on CIFAR-100 (due to small per-sub-population batch sizes). FR(G2) works more consistently but relies on an ImageNet pre-trained model to define a binary head/tail split. The paper acknowledges this (line 324) but does not provide a clear principle for choosing the split in practice. A practitioner has little guidance on whether to use KNN, G2, or something else for a new dataset.

5. **Some individual settings show decreased performance.** For example, on CIFAR-10 Imb ρ=0.5 r=50, CE+FR(KNN) = 46.69 vs CE = 47.51 (a decrease). The paper's claim that FR "consistently improves" (line 324) is slightly overstated for FR(KNN), though FR(G2) does improve in this specific case (49.43). The table only highlights improvements in green without indicating decreases, which slightly masks the full picture.

### Trivial

6. **The relaxation uses prediction confidence instead of accuracy (Eq. 4).** The gap between average confidence and true accuracy can be large (e.g., overconfident wrong predictions). This discrepancy is acknowledged implicitly but not discussed.

7. **Linking the empirical analysis (Section 3) to the method (Section 4) could be tighter.** Section 3 uses k-means clustering on features to define sub-populations, while FR experiments use either KNN clustering or the G2 method. The analysis figures (influence functions) and the regularizer are conceptually connected but not empirically linked (e.g., by showing that FR reduces the variance of influence across sub-populations).

## Nice-to-Haves

- Report standard deviations over at least 3 runs for a representative subset of experiments (e.g., CIFAR-10/100 at ρ=0.2, r=10 and r=100 for 2–3 baselines). This would substantially strengthen confidence in the results.
- Add a comparison to one or two existing joint long-tailed + noisy-label methods (e.g., Wei et al. 2021) on a subset of settings. This would clarify whether FR is merely catching up to existing solutions or providing a genuinely new advantage.
- Ablate the sub-population split choice more thoroughly: compare FR applied with ground-truth class labels, random splits, G2, and KNN with different K values to guide practitioners.
- Connect the empirical analysis to the method more directly, e.g., by showing that FR reduces the variance of influence function values across sub-populations.

## Removed Points

- **Criticism about "no code or reproducibility details beyond hyperparameters"**: The paper provides architecture (ResNet-32 for CIFAR, VGG-19 for Animal-10N), optimizer (SGD), and learning rate schedule. Additional implementation details are standard and the paper states the fixed λ values used. This is within the norm for a conference submission.
- **Criticism that the paper "does not discuss limitations"**: While the paper could be more explicit about limitations, it does acknowledge the KNN variant's failure on CIFAR-100 and the reason (batch size issue). The absence of an explicit "Limitations" section is a presentation choice, not a fatal omission.
- **Strength Finder's claim about "Table 2" (referring to real-world results)**: The relevance of this strength is intact; the strength is about real-world validation, which is a genuine contribution. No conflict with verified weaknesses.
- **Strength Finder's generic strengths about "addressing an important problem"**: Removed as too generic.
- **Criticism about the observation being "qualitative; no statistical test"**: The observations in Section 3 are qualitative illustrations meant to motivate the method, not formal hypothesis tests. This is appropriate for a motivation section.

## Novel Insights

Beyond the paper's own contributions, no genuinely novel insight emerges from the reviews. The reviewers largely agree on the paper's strengths (well-motivated problem, simple method, extensive empirical evaluation) and weaknesses (lack of variance reporting, thin theory, dependence on split choice).

## Suggestions

1. **Report error bars.** This is the single most impactful improvement. Add standard deviations over at least 3 runs for a representative subset of Table 1 and all of Table 3. Show that the improvements are outside run-to-run noise.
2. **Add at least one joint-method baseline.** Pick one of the cited decoupled approaches (e.g., Wei et al. 2021) and compare on a representative subset (e.g., CIFAR-10/100 at ρ=0.2 and 0.5, r=10 and r=100). This directly addresses the most common reader concern.
3. **Tone down the "theoretical" claims.** Rename the observation box to what it is: an illustrative example. The paper is empirically strong; it does not need inflated theoretical framing.
4. **Add a simple decision rule for choosing between KNN and G2.** Based on the observed failure mode (small per-sub-population batches on CIFAR-100), propose a heuristic: use G2 when K would make the average batch size per sub-population < 2.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Comparison to this paper |
|------|-----------|--------------------------|
| `/home/.../RwiUmrEHgR.md` (Long-tail CSL) | 3.00 | Clearly weaker: fewer baselines, no real-world validation, no statistical testing |
| `/home/.../d18RgYF6Y7.md` (Fair classifiers w/o fair training) | 5.20 | Comparable: similar empirical scope, but this paper has more extensive experiments |
| `/home/.../OeKp3AdiVO.md` (Logits retargeting for LTR) | 6.25 | Slightly stronger: better theoretical analysis, comparable empirical scope |
| `/home/.../3GurO0kRue.md` (Harmonizing implicit subpopulations) | 6.50 | Stronger: has error bars, theoretical guarantees, and comparable experiments |
| `/home/.../NnyD0Rjx2B.md` (fairret framework) | 6.00 | Comparable framing but different scope; this paper has more task-specific experiments |

**Decision:** This paper addresses a relevant and under-studied problem with a simple, well-motivated regularizer that shows consistent positive trends across an extensive experimental campaign. However, the absence of error bars on individual experiments makes it impossible to assess the statistical significance of many small improvements, and the lack of comparison to existing joint methods leaves the core contribution partially unvalidated against the strongest alternatives. The paper would benefit from revision addressing these issues. In its current form, it does not quite meet the acceptance bar for a top venue.

MY FINAL SCORE: 5.0
MY FINAL DECISION: Reject