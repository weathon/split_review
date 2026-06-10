Here is my final consolidated review:

---

## Summary

This paper empirically and theoretically studies how Temperature Scaling (TS) calibration interacts with Conformal Prediction (CP) methods for deep classifiers. It documents a previously overlooked trade-off: applying TS before adaptive CP methods (APS and RAPS) improves class-conditional coverage but *increases* prediction set sizes. The paper provides a clean theoretical result (Theorem 1) showing TS monotonically decreases APS/RAPS scores, a local analysis attempting to explain the set-size increase, and guidelines for practitioners to navigate the trade-off.

## Strengths

1. **Clear empirical discovery of a genuine TS–CP trade-off.** Tables 1–2 and Figure 2 provide consistent evidence across three datasets and six architectures. For example, on CIFAR-100 ResNet50, TS calibration improves TopCovGap for APS from 12.6% to 9.0% while average set size increases from 5.31 to 9.14. The finding is well-documented, the opposite directions of the two effects are clearly shown, and the result generalizes across multiple settings.

2. **Clean, universal theoretical result (Theorem 1 + Corollary 1).** Theorem 1 proves that for *any* sorted probability vector, TS with T>1 strictly decreases the cumulative sum of top-L entries. This is a non-trivial inequality with no data assumptions. Corollary 1 then establishes that the APS/RAPS threshold decreases monotonically with T. These results are crisp and correctly identified as directly useful (e.g., motivating polynomial fitting of q̂(T)).

3. **Per-sample "microscopic" analysis ruling out outlier-driven effects.** Figure 1 breaks down set-size changes sample-by-sample across 100 trials, showing the aggregate increase reflects a systematic distributional shift (~1/3 of samples see increase, ~1/2 unchanged, only a small minority see decrease). This granularity goes beyond what typical CP studies provide and strengthens the empirical claim.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **The theoretical analysis overclaims relative to what is actually proven.** The abstract and introduction claim to "provide a reasoning for the phenomenon" of increased set sizes. Theorem 1 and Corollary 1 only address scores and thresholds — they do not, by themselves, predict that set sizes increase (both the numerator and denominator of the decision rule change). The main attempt at explanation is Theorem 4 (local analysis), which establishes that for a *specific* perturbation vector $\mathbf{r} = [\delta, -\delta/(C-1), \dots, -\delta/(C-1)]^\top$, the gap function $g$ increases locally when $T$ exceeds a complex bound (line 569). This is a narrow result about a single ascent direction at a single point — it does not compare two different samples at finite distances or establish the required global inequality. The paper's own language ("it provides a formal reasoning why it is *likely*") acknowledges this gap, but the introduction/abstract set higher expectations. **Why it matters:** A reader expecting a complete theoretical account will find the gap between the claims and what is delivered significant, which can undermine trust in the paper's framing even though the empirical contribution stands.

2. **No uncertainty quantification despite 100 trials.** The paper reports "median-of-means along 100 trials" but provides no standard errors, confidence intervals, or any measure of dispersion for any metric. For small-effect cases (CIFAR-10 APS: 1.04 → 1.13; RAPS: 0.98 → 1.05), the absolute changes are tiny and the reader cannot assess whether the effect is reliable. Similarly, some TopCovGap differences between pre- and post-TS are as small as 0.2–0.8 percentage points — potentially within trial-to-trial variability. The paper follows the reporting convention of Angelopoulos et al. (2020), but its core claim is about the *direction and magnitude* of an effect, making this omission consequential. **Why it matters:** Weakens the evidential foundation for claims about effect size, particularly for high-accuracy settings where effects are small.

3. **The practical guideline does not go beyond a straightforward grid search.** The paper proposes using two temperatures — $T^*$ for calibration and $\hat{T}$ for the CP trade-off — and fitting a polynomial to $\hat{q}(T)$ (lines 434–454). The paper acknowledges that one "does not know in advance what values of the metrics are obtained per value of $\hat{T}$" (line 438) and that the curves were generated using data "not accessible to the user in practice" (line 440). This amounts to: compute curves for many T values on held-out data, then pick one. This is a reasonable suggestion but not a novel or non-obvious procedure, and it is not validated with an experiment demonstrating its practical utility. **Why it matters:** The paper frames this as a contribution (lines 62–66), but the guideline's novelty and practical value are limited.

4. **The bound in Theorem 4 is not connected to the experimental settings.** The lower bound on $T$ (line 569) involves $C$, $L$, $\pi_1$, and a norm term whose behavior is not empirically evaluated. Readers cannot tell whether the temperatures used in the experiments ($T^* \approx 1.0$–$1.8$) satisfy this bound for the actual models and datasets. Without verification, the relevance of the theorem to the empirical phenomenon is unclear. **Why it matters:** A theoretical result whose conditions are not checked in the settings it is meant to explain has limited explanatory force.

### Trivial

None.

## Nice-to-Haves

- **Add variance information.** Standard errors or interquartile ranges for AvgSize, TopCovGap, and MarCovGap would substantially strengthen the empirical evidence. This is the single highest-leverage improvement.
- **Validate the dual-temperature guideline** with an experiment where $\hat{T}$ is chosen on a held-out subset to achieve a target trade-off, demonstrating that the procedure works in practice.
- **Report alternative class-conditional coverage metrics** (e.g., average per-class gap or worst-class gap) alongside Top-5% to demonstrate robustness of the findings to metric choice.
- **Verify the bound in Theorem 4** for representative samples from the experimental settings, or simplify the bound to something more interpretable.

## Removed Points

These points were flagged by the reviewers but removed after verification against the paper:

- **"The surprising finding is less surprising than claimed"** — Removed. The paper's finding that TS *increases* prediction set sizes is genuinely non-obvious from Theorem 1 alone, which only shows that scores and thresholds both decrease. Which effect dominates (and thus whether set sizes increase or decrease) is not predictable from Theorem 1. The paper's "surprising" framing is appropriate given that the directional effect on set sizes runs opposite to what a casual reader might expect from "better calibration."
- **"Proposition 1 is informal/unproven"** — Removed. The proposition is stated clearly; its proof is likely in the appendix (stripped by the parser). The proposition's content is a reasonable observation and the paper's discussion of it is appropriately measured.
- **"TopCovGap metric not well-justified"** — Removed. The paper provides explicit justification ("due to the high variance in the maximal class deviation," line 237). The concern about sensitivity to the 5% threshold is speculative.
- **"Lack of comparison with other calibration methods"** — Removed. The paper explicitly scopes itself to studying TS, the most common calibration method. Comparing across calibration methods is a different study.
- **Strength Finder's claim about "Proposition tying TS effects to misclassified samples"** — Removed. The proposition is a simple observation rather than a deep theoretical result, and its practical implications are limited.
- **Strength Finder's claim about "Actionable dual-temperature guideline"** — Removed from strengths. The guideline is essentially a grid search with acknowledged limitations; keeping it as a strength would overstate its value. It is noted in the summary and retained as a minor weakness above.

## Novel Insights

None beyond the paper's own contributions. The synthesis of the reviews does not reveal a perspective on the paper that the paper itself does not articulate.

## Suggestions

1. Add standard errors or confidence bands to all reported metrics (AvgSize, TopCovGap, MarCovGap). With 100 trials, this is straightforward and would significantly strengthen the empirical claims.
2. Reframe the theoretical contribution to be precise about what Theorem 4 achieves — a local gradient analysis under a specific perturbation direction — rather than suggesting it provides a complete "reasoning for the phenomenon."
3. Either verify that the bound in Theorem 4 is satisfied for representative experimental settings, or develop a simplified bound that is more interpretable and checkable.
4. Validate the dual-temperature guideline with a concrete experiment where practitioners use the proposed procedure to achieve a target trade-off point on held-out data.

## Score and Decision

This paper makes a genuine contribution: it documents a real and previously overlooked trade-off between TS calibration and adaptive CP methods, supports it with consistent empirical evidence across multiple architectures and datasets, and provides some useful theoretical results (Theorem 1, Corollary 1). The weaknesses — overclaiming in the theoretical analysis, missing error bars, the limited novelty of the guideline, and the unverified bound in Theorem 4 — are real but not fatal. The core empirical finding stands on its own and is valuable to the community.

Given the top-tier venue standards, this is a solid paper with a clear contribution and addressable weaknesses.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>