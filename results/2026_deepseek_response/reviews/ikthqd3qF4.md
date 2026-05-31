Now I have all the calibration I need. Let me write the final consolidated review.

## Summary

This paper derives observable lower bounds on precision and relative recall for unsupervised anonymous record linkage by exploiting a structural constraint: an individual can originate at most one first-lien mortgage. The bounds depend only on the origination probability and the rate of multiple-origination clusters, making them computable without any labeled data. The method is instantiated via hierarchical clustering and applied to 65.5 million HMDA mortgage records to detect "cross-applicants" (individuals submitting multiple applications), reporting an implied 92.3% precision at the preferred tuning. Corollaries extend the bounds to recall, Fβ, and weighted precision-recall summaries, enabling principled model selection without labels.

## Strengths

1. **Novel theoretical framework with practical utility.** Theorem 1 and Corollaries 1–2 derive lower bounds on precision, recall, and weighted summaries (Fβ, Wλ) that depend only on observable quantities — the origination probability p and the fraction of multi-origination clusters. The bounds are method-agnostic and applicable wherever a structural constraint limits positive outcomes per individual (mortgages, insurance, college admissions, job offers). This clean theoretical contribution is the paper's strongest asset.

2. **Simulation validates bound tightness under ideal conditions.** Figures 3a and 4a show close resemblance between the ground-truth precision (using individual identifiers) and the method's implied lower bound in the simulated setting. This demonstrates that when the data match the assumed structure, the bound is informative enough to be practically useful.

3. **Scalable real-world demonstration.** The method is applied to 65.5 million HMDA records using an O(ℓ²) hierarchical clustering algorithm (nearest-neighbor chain, `fastcluster`), demonstrating that the approach works at real-world scale. The precision-sample-size frontier (Figure 5) provides a clear visual for tuning without labels.

## Weaknesses

### Major

1. **No external validation of the real-data results.** The HMDA application's "92.3% precision" claim rests entirely on the method's own assumptions — there is no manual audit of sampled clusters, no cross-matching against credit bureau data or other sources, and no sensitivity analysis testing how violations of Assumptions 1–2 would affect the bound in real data. The simulation validates the method only under a data-generating process specifically designed to match the assumptions. Without any convergent validity check, the reader cannot assess whether the clusters reflect genuine cross-applicants or artifacts of the independence and monotonicity assumptions. This is the most significant gap.

2. **The headline "92.3% precision" conflates a lower bound with a point estimate.** The abstract and results sections state that the method "identifies cross-applicants with an estimated 92.3% precision" (lines 9, 35) and "estimate[s] that 92.3% are true cross-applicants" (line 240). What the method actually produces is a lower bound on precision after dropping known false-positive clusters (Equation 2). While the methodology section correctly discusses bounds, the results framing overstates the strength of the evidence. The safe claim is "at least 92.3% precision under the maintained assumptions."

### Minor

3. **No uncertainty quantification.** The precision bound (and the bound on recall) is reported as a point estimate with no confidence interval, bootstrap, or sensitivity analysis around uncertainty in the estimate of p (origination probability) or the fraction of multi-origination clusters. For a method that is supposed to enable principled model selection, this omission limits practical usefulness.

4. **Limited robustness testing in simulation.** The simulation tests only the scenario where data are generated to match the method's assumptions (applications from the same applicant differ only slightly on continuous variables). No adversarial simulation examines what happens when: (a) different applicants coincidentally submit very similar applications (hard false positives), (b) origination decisions are correlated across borrowers (violating Assumption 1), or (c) partitions constructed from categorical variables split genuine cross-applicants.

5. **Notation inconsistency in Equation (1).** The displayed equation shows "Pr[False] ≥ ..." while the text describes it as a "lower bound on precision." Since precision = 1 − Pr[False], the inequality direction in the display seems ambiguous. If Pr[False] is among retained clusters, this should be clarified. (The empirical version in Equation (2) uses "≥" for α̂(θ), which is a lower bound on precision, suggesting Equation (1) may have a sign error relative to how it is used.)

6. **Reproducibility gaps.** The weight vectors for the distance function, the specific set of 96 tuning parameter combinations tested, and the exact distance functions considered are not described in the main text. These are relegated to an appendix that was stripped from the submission, making independent verification difficult based on the main text alone.

### Trivial

7. Minor presentation artifacts from PDF extraction (duplicated figure captions, missing section numbers) do not affect the scientific content.

## Nice-to-Haves

- A manual audit or external validation of even a modest sample of identified clusters would substantially strengthen the real-data application.
- Adversarial simulation experiments testing the bound's sensitivity to assumption violations.
- Bootstrap confidence intervals around the precision bound.
- More explicit discussion of when the method should not be used (e.g., settings where the structural constraint is weak or origination outcomes are strongly correlated).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Assumption 1 makes the bound go the wrong direction" (Harsh Critic).** The critic argued that positive correlation in origination decisions would cause Pr[Mult|False] to exceed p², making the bound understate false positives. This reasoning is backwards: positive correlation would increase Pr[Mult|False] beyond p², making the inequality Pr[Mult] = Pr[False]·Pr[Mult|False] even harder to satisfy for a given Pr[Mult], which makes the bound more conservative (tighter bound on Pr[False], not looser). The bound Pr[False] ≤ Pr[Mult]/p² remains valid; the direction of the inequality is unaffected. This criticism is factually incorrect.

- **"Circular evaluation" (bound used for both selection and evaluation).** The critic argued that using the same bound to select parameters and report performance is circular. However, in the absence of labels, this is the standard operating procedure — and the simulation (Figures 3a vs 4a) provides independent evidence that the bound tracks actual precision. The criticism overstates the concern.

- **"Overclaims novelty" / "missing related work."** Removed per instructions: missing references cannot be confirmed as a genuine weakness; the paper qualifies its claim with "to our knowledge."

- **"Categorical variables split cross-applicants" (race/sex/age partitions).** The paper acknowledges this concern explicitly in footnote 5 (line 246) as an application-specific modeling choice.

- **Generic/superficial strengths** that lack concrete evidence (e.g., "the problem is important," "this is a valuable contribution to the community") are removed. Only specific, evidenced strengths are retained.

## Novel Insights

None beyond the paper's own contributions. The two sets of reviews do not surface a perspective that the paper itself does not already articulate about its contributions and limitations.

## Suggestions

1. Qualify the 92.3% result as "at least 92.3% precision (a lower bound)" in the abstract and conclusion to avoid conflating the bound with a point estimate.
2. Add a small-scale manual validation study (e.g., auditing 200–500 sampled clusters against public property records or other sources) to provide convergent evidence.
3. Include a bootstrap procedure to attach confidence intervals around the precision bound.
4. Add simulation experiments where Assumption 1 is explicitly violated (correlated origination decisions across borrowers) to measure how much the bound degrades.
5. Report the distance function weights and a representative subset of the 96 tuning configurations in the main text or in a clearly referenced appendix table.

---

**Calibration Report**

Round 1 bracket: The paper clearly outperforms the weak-band anchors (scores 2.5–3.4) and is clearly weaker than the strong-band anchors (scores 8.0). Initial bracket: **4.0–6.5**.

Round 2 anchors:
- **`f9RvYpXhFI` (Fréchet bounds for PWS), avg 5.50** — The closest methodological analog (bounds for evaluation without labels). The Fréchet paper has stronger theoretical development (asymptotic distributions, confidence intervals) and broader empirical validation. The current paper has a cleaner, more directly applicable theoretical contribution but weaker empirical validation (no ground-truth check in the real application). Slightly weaker overall.
- **`6tqgL8VluV` (Guaranteed error for DB operations), avg 6.00 (scores: 8,5,8,3)** — Mixed reviews; theoretical bounds for learned database operations with limited experiments. The current paper has a clearer presentation and more concrete application, but the fundamental evidence gap is more serious.
- **`NO6Tv6QcDs` (Limits to scalable evaluation), avg 6.50** — Stronger paper with a clean theoretical result and better empirical validation. The current paper is clearly below this standard.
- **`uLCtVTzFhg` (Contrastive PU learning), avg 5.75 (scores: 6,3,8,6)** — The current paper is comparable in overall quality but has a cleaner contribution; the PU paper had one enthusiastic review (8) and one skeptical one (3), while the current paper would likely receive more uniform mid-range scores.

**Final score: 5.0.** The paper has a genuinely novel theoretical contribution and a technically competent application, but the absence of any external validation in the real-data setting and the conflation of a lower bound with a point estimate are substantial weaknesses that prevent a higher score. It is a solid paper with real potential but needs major strengthening of the empirical evidence.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>