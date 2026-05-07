Now I have a thorough understanding of the paper and calibration anchors. Let me compose the final review.

## Summary

The paper argues that CLT-based confidence intervals systematically fail for LLM evaluations with small sample sizes (fewer than a few hundred datapoints), producing under-coverage, invalid intervals, and misleading uncertainty estimates. It demonstrates this across five settings—IID Bernoulli accuracy, clustered questions, independent model comparison, paired model comparison, and F1-scores—through simulation experiments comparing CLT, bootstrap, Wilson, Clopper-Pearson, and Bayesian intervals. The paper recommends Wilson score intervals for the simple proportion case and Bayesian credible intervals for more complex settings, providing working code snippets and an open-source Python library.

## Strengths

- **Clear, actionable position with immediate practical consequence.** The central claim—"don't use the CLT for small-N LLM evals"—is easy to summarize, directly challenges widespread practice, and the paper provides drop-in replacements (Wilson score intervals are one line in scipy, Bayesian posteriors for Bernoulli are closed-form). Table 1 summarizes the tradeoffs concisely.

- **Systematic demonstration across multiple realistic failure modes.** The paper shows CLT intervals failing in five distinct settings (§3.1–3.5), each corresponding to a common LLM evaluation scenario. This breadth makes the argument much harder to dismiss than a single failure mode would: intervals extending beyond [0,1] (Figure 1), systematic undercoverage (Figure 2), bootstrap also failing (§3.1), no frequentist method for clustered data (§3.2), and CLT inapplicability to non-linear metrics like odds ratios and F1 (§3.3, §3.5).

- **Identification of a genuinely growing problem.** §1 makes a compelling case that LLM evaluation is shifting toward smaller, specialized benchmarks (AIME with 15 problems, FrontierMath categories with <3 samples, MLE Bench with 75), and even large benchmarks decompose into small sub-tasks. This grounds the statistical argument in a real trend rather than a hypothetical concern.

- **Insightful connections between frequentist and Bayesian methods.** The paper notes (citing Thulin 2014 and Altham 1969) that Clopper-Pearson corresponds to Bayesian with improper priors removed and Fisher's exact test corresponds to conservative Bayesian priors Beta(1,0) and Beta(0,1). This provides theoretical depth beyond "use Bayes" and helps practitioners understand *why* the alternatives work.

- **Practical code and reproducibility.** Snippets 1–3 are immediately usable, and a Python library is provided. A position paper that tells practitioners to stop doing X while making the alternative trivially adoptable has much higher impact potential.

## Weaknesses

### Fatal
None.

### Major

- **Prior-data matching in the main experiments inflates the apparent advantage of Bayesian methods.** In the primary experiments (§3.1 and throughout), the ground-truth θ is drawn from Beta(1,1) and the Bayesian method uses a Beta(1,1) prior. When prior and data-generating distribution match, Bayesian methods enjoy excellent frequentist coverage by construction—a well-known property that may not hold under mismatch. The paper partially addresses this in Appendix I, finding that "Bayesian coverage performance generally does not fall below that of CLT-based methods," but this critical mitigation is relegated to the appendix where many readers will miss it, and the main figures and coverage numbers all benefit from prior-data alignment. Bringing key mismatch results into the main text and clearly stating the caveat would substantially strengthen credibility.

- **The broad framing ("Don't Use the CLT in LLM Evals") overstates the evidence scope.** The strongest evidence concerns Bernoulli/proportion outcomes. The F1 section (§3.5) is thinner—only Bayesian and bootstrap are compared, no specialized frequentist alternatives for F1 intervals are considered, and the delta method is dismissed briefly. Many common LLM evaluation metrics (continuous scores, Likert-scale judgments, Elo ratings) are not covered. The paper would be more honest and more useful if it explicitly scoped its strongest recommendation to proportion-based evaluations while clearly acknowledging which settings remain untested.

### Minor

- **No concrete guidance on where the CLT transition occurs, despite having the data.** The title warns about "fewer than a few hundred" datapoints, and Section 4 explicitly defers on specifying a threshold N*. The paper has data at N=3, 10, 30, 100, and up to 300 for the clustered setting—enough to give practitioners concrete guidance like "at N≥200 with θ not near 0 or 1, CLT coverage is within X pp of nominal." Without this, a practitioner is left knowing the CLT fails at N=3 but unsure whether it's acceptable at N=150. The paper's own recommendation to always use the better methods (since they're as easy and perform no worse at large N) partly addresses this, but more specific calibration data would be valuable.

- **The "just use more data" counterargument about wide intervals at small N is unaddressed.** When N is very small (e.g., 3 problems), even well-calibrated Bayesian intervals will be very wide—potentially spanning the entire [0,1] range. The paper focuses on coverage (whether intervals contain the truth) but does not discuss what practitioners should *conclude* from very wide intervals. If a 95% credible interval for model comparison includes both positive and negative values, the evaluation may not support meaningful conclusions regardless of the method. This is relevant context that would strengthen the discussion.

## Nice-to-Haves

- Empirical validation on real benchmark comparisons (beyond the LangChain vignette) showing that the recommended methods produce meaningfully different conclusions about whether two models are significantly different.

- Consideration of continuity corrections or Agresti-Coull adjustments to the CLT interval, which are CLT-based alternatives that partially address the boundary problems shown in Figure 1. The paper frames its comparison as "CLT vs. alternatives" but some readers may wonder about CLT-adjacent fixes.

- A more thorough comparison for the F1-score setting, including specialized frequentist approaches from the statistical literature on F1 confidence intervals.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **"Overclaiming" in the title.** The title "Don't Use the CLT in LLM Evals" is provocative but standard for position papers. The subtitle "With Fewer Than a Few Hundred Datapoints" does scope the claim. The actual recommendation in the paper is reasonable (use better methods since they're as easy and perform no worse). This is not a factual falsehood or self-contradiction—it's provocative framing appropriate for a position paper. However, the *specific* way the title is broader than the evidence *is* kept as a Major weakness above (scope of evidence, not tone).

- **The paper needs novel experiments/baselines/ablations.** The harsh critic notes missing specialized frequentist methods for F1 in §3.5. This is partially valid (kept as a Nice-to-Have), but the paper's central method is argumentation and simulation comparison, not novel method development. Demanding complete exploration of all possible frequentist alternatives for every metric would turn this from a position paper into a research methods paper.

- **Wilson score undermines the main recommendation for Bayesian methods.** The critic argues that Wilson intervals solve the simple case, so why go Bayesian? The paper *does* address this: it recommends Wilson for the simple IID case (§3.1) and Bayesian methods specifically for more complex settings (clustered, paired comparison, non-linear metrics) where no good frequentist alternative exists. The paper's Table 1 clearly shows this. This counterargument is addressed.

- **Formatting and presentation nitpicks** (parser artifacts, figure descriptions, etc.) are removed per policy.

- **Missing appendix references.** The parser strips appendices from all papers; these exist in the original submission.

## Novel Insights

The connection between Fisher's exact test and Bayesian priors under improper Betas (citing Altham 1969) is an elegant theoretical insight that explains *why* exact frequentist methods over-cover: they correspond to assuming the most extreme scenario. This bridges frequentist and Bayesian reasoning in a way that is directly actionable for practitioners choosing between methods.

## Suggestions

- Move the key prior-mismatch results from Appendix I into the main text (at least one figure/table showing that Bayesian methods still outperform CLT under mismatch), and add a prominent caveat that the main experiments use matching priors.

- Rename or add a subtitle that reflects the evidence scope more accurately, e.g., "Don't Use the CLT for Proportion-Based LLM Evals With Small Samples" or add a clear statement in the abstract acknowledging that the strongest evidence covers proportion outcomes and model comparisons, with F1 as an extension.

- Add a brief discussion of what wide intervals *mean* for practical decision-making at very small N, acknowledging that even calibrated methods may not yield actionable conclusions when data is extremely scarce.

## Score and Decision

**Calibration comparison:**
- **d7hqAhLvWG** (ASR comparison critique, avg 6.25, Accept): Similar statistical-methodology-critique paper with measurement theory framing, actionable recommendations. Our paper has more systematic simulation evidence but less theoretical depth in its framework.
- **yqKfMr0yvY** (LLM-as-judge critique, avg 7.67, Accept): Stronger theoretical framework (measurement theory) with clearer normative recommendations; our paper has more empirical evidence but prior-data matching weakness.
- **5X4GDSUumr** (No Champions in LTSF, avg 7, Reject): Very strong empirical work (3500+ experiments) but still rejected; position papers with primarily empirical backing don't always score as high.
- **FJF1sa6elQ** (Model Multifacetedness, avg 3.33, Reject): Much weaker—vague framework, no concrete evidence, not actionable. Our paper is clearly well above this.
- **vFae5rRman** (Benchmarking is Broken, avg 6, Accept): Similar "reform practice" paper with practical proposal. Our paper has stronger empirical backing.
- **tMJvb9JDsd** (Stop Overvaluing MAD, avg 7, Reject): Strong empirical evidence but rejected. Slightly higher quality than ours but received reject.

This paper has a clear position, strong simulation evidence across five settings, practical code, and addresses a genuinely growing problem. Its main weaknesses (prior-data matching, scope breadth beyond proportions, no N* threshold) are real but partly addressed and don't invalidate the core argument. It falls in the range of accepted position papers about statistical methodology in ML evaluation (6–7 range). The prior-matching issue is the most significant concern but is mitigated by appendix analysis showing Bayesian methods still outperform CLT under mismatch. I place it slightly above the "benchmarking is broken" paper (6) and below the ASR critique (6.25) and LLM-as-judge paper (7.67).

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>