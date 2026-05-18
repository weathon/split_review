Now I have verified the paper content against the reviewer claims. Let me construct the final consolidated review.

## Summary

This paper identifies a confounding flaw in prior evaluations of how unseen-class unlabeled data affects SSL models: prior work fixed total unlabeled dataset size while varying unseen-class proportion, which inadvertently changed seen-class proportion. The authors propose RE-SSL, a controlled-variable evaluation framework that fixes seen-class quantity while varying unseen-class samples across five dimensions (sample count, category number, category index, nearness, and label distribution). They introduce five robustness metrics and evaluate 15 SSL algorithms on CIFAR-10/100, finding that unseen classes do not necessarily harm SSL models and can even help under specific conditions.

## Strengths

- **Identifies a fundamental confounding flaw in prior SSL evaluations**: The paper constructs a structural causal model (Figure 1) showing that fixing total unlabeled size while varying unseen-class proportion creates a spurious correlation between seen-class and unseen-class unlabeled data. The RE-SSL framework (Figure 2b) removes this confound by fixing $r_s$ while varying $r_u$, providing a causally sounder evaluation baseline. This conceptual contribution is the paper's strongest and most original element.

- **Comprehensive, multi-dimensional analysis across five factors**: Beyond the sample-count factor ($r$), RE-SSL systematically investigates category-number ($C_n$, Table 3), category-index ($C_i$, Table 4), nearness (near vs. far OOD, Table 4), and label distribution ($C_{ib}$, Table 5). This breadth is genuinely informative and goes well beyond what is typical in safe SSL evaluations — Table 6's per-factor GM aggregation showing that models are most sensitive to $r$ (avg GM=0.170) and most robust to $C_{ib}$ (avg GM=0.040) is a useful empirical finding.

- **Introduction of five targeted robustness metrics**: The paper defines $R_{slope}$, GM, WAD, BAD, and $P_{AD\geq0}$ (Eqs. 1–5) to capture both global and local robustness. These go beyond single-point accuracy comparisons and enable fine-grained analysis (e.g., FixMatch's $R_{slope}=-0.223$ vs. ICT's near-zero slope on CIFAR-10, Table 1).

- **Actionable insights for practitioners**: Table 6 provides per-algorithm $F_{avg}$ rankings identifying PseudoLabel, PiModel, and ICT as most robust to unseen classes while FixMatch is most sensitive. The analysis explains why adaptive-threshold methods (FlexMatch, FreeMatch, SoftMatch) improve upon FixMatch's fixed-threshold design — a concrete design lesson for SSL in open-world scenarios.

## Weaknesses

### Major

- **No measures of variance reported for any experimental result**. The paper states that three seeds (0, 1, 2) were used per sampling point with averages reported, but no standard deviations, confidence intervals, or ranges are provided. This makes it impossible to assess whether the observed differences between methods or between $r$ levels are meaningful relative to noise. For example, the claim that PseudoLabel's accuracy at $r=0.2$ (0.743) exceeds that at $r=0$ (0.730) cannot be evaluated. Similarly, the paper describes FixMatch showing a "significantly low accuracy" at $C_i=6$ (0.504) without any error bars to justify the word "significantly." This is a standard expectation for an empirical paper that draws conclusions about trends and comparisons, and its absence weakens the entire quantitative foundation. The core conceptual contribution (identifying the confound) does not depend on these numbers, but the empirical claims about which methods are robust/sensitive and under which conditions do.

### Minor

- **The abstract's "enhancement" claim is broader than the primary experiment supports.** The abstract states that "under certain conditions, unseen classes may even enhance them [SSL models]." In the main experiment (Tables 1 and 2), where the number of unseen-class samples ($r$) is varied while seen-class quantity is held constant, the vast majority of methods show negative or near-zero slopes. The evidence for enhancement comes primarily from the category-number factor ($C_n$, Table 3) and local BAD values (e.g., FlexMatch BAD=0.166). The abstract and introduction do not distinguish between these factors, making the headline claim appear broader than what the primary $r$-factor experiment supports. The paper's strongest and best-supported message is that previous evaluations *overstated* the harm of unseen classes (robustness), while "enhancement" is a secondary finding under specific conditions. Restructuring the narrative around robustness first and enhancement as a specific exception would better match the evidence.

- **The robustness definitions rely on an arbitrary threshold.** Definition 1 states that an algorithm exhibits $\delta_g$-slope robustness if $R_{slope} \ge \delta_g$. In Section 5.3, the authors "assume that $\sigma_g$ equals -0.020" without justifying why -0.020 is a meaningful cutoff. No theory or reference anchors this value. The raw $R_{slope}$ values provided in the tables are informative on their own; the threshold-based classification adds little and introduces subjectivity. The paper would be stronger by presenting the raw values and letting the reader judge significance (e.g., "a slope of -0.02 means 2 percentage points of accuracy lost across the full $r$ range").

### Trivial

- **No explanation for the choice of $r$ values (0, 0.2, 0.4, 0.5, 0.6, 0.8, 1.0)**. The non-uniform spacing (the inclusion of 0.5) is not justified. This is a minor documentation gap.

## Nice-to-Haves

- **Replicate one prior evaluation protocol** (e.g., from DS3L or Safe-Student) on the same datasets and overlay RE-SSL results to visually demonstrate the confounding effect. The paper argues that prior evaluations are confounded but never shows that the confounding leads to different conclusions. A direct comparison would make the paper's central critique much more concrete and compelling.

- **Discuss how results might generalize** beyond CIFAR-10/100 (e.g., higher-resolution datasets, different backbone architectures). A study that challenges a widely held belief should at least address potential limits on generality. The paper acknowledges this gap only indirectly via the Limitations section.

- **The $r=0.5$ point choice** could be briefly justified, given that all metrics depend on these seven points.

## Removed Points

These points from the reviews are removed per the filtering rules; they are listed here for completeness only and should be treated with caution.

- **"No direct comparison to the flawed evaluation framework"** — flagged as absence but this is an enhancement suggestion, not a weakness. Moved to Nice-to-Haves above.
- **"The metric definitions are presented with integrals that are then computed as discrete sums, which is fine but jarring"** — the paper explicitly addresses this on line 84 ("The integrals in Eq. 1 and Eq. 2 are computed as accumulation operations based on empirical values"), so the criticism is already resolved by the paper.
- **Generic/encompassing strength from Strength Finder** such as "this paper addressed an important problem" — not included as they lack specific content tied to the paper.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's core findings and do not surface novel interpretations that the paper itself does not already articulate.

## Suggestions

1. Add standard deviations (or at least min/max ranges) to all accuracy tables for the three-seed runs. Even a supplementary table of standard deviations for the main CIFAR-10 results would dramatically increase confidence in the quantitative claims.
2. Restructure the narrative to center on "robustness" as the primary finding and present "enhancement" as a specific exception tied to the category-number ($C_n$) factor and local BAD values, rather than lumping both under the same headline claim.
3. Replace the threshold-based robustness classification (Definition 1 with $\sigma_g=-0.020$) with direct comparison of raw $R_{slope}$ values, optionally interpreting their practical significance in percentage-point terms.
4. Provide a brief justification for the $r$ sampling points, especially the inclusion of $r=0.5$.

## Score and Decision

The paper makes a genuinely useful conceptual contribution (identifying the confounding flaw in prior SSL evaluations) and offers broad experiments across 15 algorithms and 5 factors. The RE-SSL framework and metrics are sound methodological contributions. However, the absence of error bars is a significant weakness for an empirical paper that makes comparative claims about method robustness — it prevents the reader from assessing the reliability of the quantitative findings. The framing mismatch around "enhancement" is addressable. With revisions to add variance reporting and tighten the narrative, this would be a solid contribution. In its current form, the lack of statistical rigor is a material weakness, but not fatal to the core conceptual contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>