Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper develops a decision-theoretic framework for minimax-optimal decision-making under *partial* calibration guarantees (\(\mathcal{H}\)-calibration). The main contributions are: (1) a duality-based characterization (Theorem 3.1) of the optimal robust policy for any finite-dimensional \(\mathcal{H}\), yielding a computable procedure; (2) the identification of *decision calibration* as the minimal condition under which the plug-in best-response policy is recovered as minimax-optimal (Theorem 4.1), with a sharp collapse result that any richer \(\mathcal{H}\) preserves this property (Theorem 4.2); and (3) practical corollaries showing that squared-loss-trained models automatically satisfy a useful partial calibration condition (Proposition 4.4), enabling application without explicit calibration training. The paper is primarily a theoretical contribution, supported by proof-of-concept experiments on two regression datasets.

## Strengths

1. **Decision calibration as a sharp threshold for plug-in optimality (Theorems 4.1, 4.2).** Prior work established that decision calibration implies no-swap-regret, but this paper proves a stronger statement: under decision calibration, the plug-in best response is *minimax optimal* among *all* forecast-to-action policies. The sharp transition (collapse) shown in Theorem 4.2—that any \(\mathcal{H}\) containing the decision-calibration indicators suffices—is a clean, non-trivial insight that clarifies exactly which calibration guarantees suffice for decision-theoretic "trustworthiness."

2. **General duality characterization (Theorem 3.1).** The paper provides a closed-form description of the minimax-optimal robust policy for any finite-dimensional \(\mathcal{H}\) via dual multipliers and pointwise convex minimization. This is the first general result of its kind and yields an explicit two-step computational procedure, which is a substantive technical contribution.

3. **Self-orthogonality from squared-loss training (Proposition 4.4).** The observation that any model with a linear last layer trained to stationarity under MSE automatically satisfies a useful \(\mathcal{H}\)-calibration condition is practically valuable. It bridges the theory to practitioners who cannot control the training pipeline.

4. **Clear writing and structure.** The paper is well-organized, the motivation is crisp, and the theoretical development is presented accessibly with helpful schematic figures (Figures 1 and 2).

## Weaknesses

### Fatal
None.

### Major

1. **Thin experimental validation relative to practical claims.** The experiments are limited to two one-dimensional regression datasets, each with only 3 actions. No error bars, confidence intervals, or multiple runs are reported, making it impossible to assess whether the reported utility differences (0.01–0.02) are statistically meaningful. There are no baselines beyond the plug-in vs. robust comparison—e.g., no comparison to a simple fixed-action rule, a mean-response baseline, or a recalibrated predictor (e.g., isotonic regression + best response). Without these, it is unclear whether the robust policy actually improves on what a practitioner might already do. The paper claims the robust policy "dominates" the plug-in under adversarial evaluation, but the gains are marginal and unquantified. This gap is significant because the paper's framing ("robust decision making with partially calibrated forecasts") suggests practical applicability, yet the experiments do not convincingly substantiate it.

2. **Unaddressed gap between exact theory and approximate practice.** The theoretical guarantees (Theorems 3.1, 4.1, 4.2) assume *exact* \(\mathcal{H}\)-calibration. The experiments rely on a forecaster that only "approximately satisfies" \(\mathcal{H}\)-calibration (Section 5, line 299), and the paper acknowledges approximate calibration only via a reference to Appendix B (which was stripped by the parser). The main body provides no sensitivity analysis, robustness bounds, or empirical verification that the approximate calibration error is small enough to preserve the theoretical optimality guarantees. A decision-maker relying on these results has no formal protection when the calibration condition is only approximately met.

### Minor

3. **Adversarial distribution construction is not fully specified.** The paper describes two types of adversarial evaluation ("worst case tailored to the plug-in policy" and "worst case induced by the robust dual") but does not describe the precise algorithm used to construct them. This makes the experimental results difficult to reproduce or extend.

4. **No empirical verification of the self-orthogonality condition.** Proposition 4.4 provides the theoretical basis for using the squared-loss-trained MLP, but the experiments never verify the key moment condition (e.g., empirical correlation between \(f(X)\) and residuals) on the calibration split. The reader must take it on faith that the trained model is sufficiently close to a first-order stationary point.

5. **Computational procedure for estimating dual multipliers is under-described.** The paper states that \(\lambda^*\) can be computed via convex optimization but does not detail how this was done in the experiments (e.g., algorithm used, convergence criteria, number of calibration samples needed). For a paper that claims practical applicability, this omission limits reproducibility.

### Trivial

6. No error bars or variance measures are reported for any experimental result.

## Nice-to-Haves

- **Sensitivity analysis for approximate calibration.** An analysis bounding the suboptimality gap as a function of \(\max_{h\in\mathcal{H}} |\mathbb{E}[h(f(X))(Y-f(X))]|\) would bridge the theory–practice gap and substantially strengthen the paper.
- **Additional baselines** such as mean-response policy, best-response to recalibrated forecasts (e.g., isotonic regression), or a naive shrinkage estimator.
- **Extension to a multiclass classification dataset** to demonstrate that the framework applies beyond 1D regression.
- **Visualization** of \(a_{\text{robust}}(v)\) vs. \(a_{\text{BR}}(v)\) as functions of \(v\) to illustrate when conservatism kicks in.
- **Sample complexity analysis** for estimating the dual multipliers \(\lambda^*\) from finite calibration data.

## Removed Points

These points were flagged but are removed with justification:

1. **"Duality argument glosses over weak* compactness of \(\mathcal{Q}\)"** (Harsh Critic, Section 3). This is a technical concern about a proof deferred to the appendix, which was stripped by the parser. There is no evidence from the main text that the proof is unsound; this is speculation about a missing appendix.

2. **"Decision calibration requires task-specific test classes, which limits practical reach"** (Harsh Critic). The paper is transparent about this (Corollary 4.3 discusses the multi-task scenario explicitly). This is a known property of the framework, not an unacknowledged weakness. It is inherent to the problem definition and not a flaw in the paper's execution.

3. **"Missing related works"** (from Strength Finder sections that were generic). Per instructions, missing related works cannot be flagged without external sources.

4. **Strength: "Empirical validation under calibration-preserving adversarial shifts (Table 1)."** This conflicts with verified weakness #1 (thin experiments, no baselines, no error bars). The table is too thin to count as a genuine strength.

5. **Strength: "Simultaneous optimality for multiple decision problems (Corollary 4.3)."** This is a straightforward corollary of the main theorems and does not represent an independent strength.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no genuinely novel observation about the work that the authors themselves do not state or imply. The main gap (thin experiments) is standard and expected; the theoretical contribution is as presented.

## Suggestions

1. **Add standard errors or confidence intervals** to all experimental results (e.g., over 5–10 random train/calibration/test splits).
2. **Include at least one meaningful baseline**, such as (a) best response to a recalibrated forecaster (e.g., isotonic regression on calibration split) or (b) a constant-action policy that always takes the intermediate action.
3. **Verify and report the empirical calibration error** (e.g., \(|\mathbb{E}[f(X)(Y-f(X))]|\)) on the calibration split to confirm the self-orthogonality condition is approximately satisfied.
4. **Provide a concrete algorithm** for constructing the adversarial evaluation distributions and for estimating \(\lambda^*\) from finite data.
5. **Add a multiclass experiment** (e.g., 3–5 classes) to demonstrate that the framework is not limited to 1D regression.
6. **Discuss the suboptimality gap** under approximate \(\mathcal{H}\)-calibration either theoretically or via simulation.

## Score and Decision

**Calibration against anchors (from batch retrieval):**

| Path | Avg Human Score | Comparison |
|------|----------------|-----------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/TId1SHe8JG.md` | 7.50 | Stronger on both theory and experiments than this paper |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/uuPkll6i7m.md` | 6.75 | Comparable theoretical depth + stronger experimental evaluation |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/X0epAjg0hd.md` | 5.67 | Similar pattern (theory contribution, weak experiments); this paper has stronger theory |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/92yrETgM6G.md` | 4.00 | Weaker theoretical contribution; this paper is clearly stronger |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ZBL26FX0FT.md` | 3.00 | Poor presentation and weak everything; this paper is substantially better |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/stUKwWBuBm.md` | 8.00 | Stronger in all dimensions; this paper does not match this level |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/WoJzHQIIUk.md` | 1.50 | This paper is far superior |

**Assessment by axis:**
- **Originality:** High. Connecting partial calibration to minimax-optimal decision-making via duality, and identifying decision calibration as the sharp threshold, is novel.
- **Importance of research question:** High. The question of how to act on partially calibrated forecasts is fundamental for trustworthy ML in high-dimensional settings.
- **Claims well-supported:** Partially. The theoretical claims are well-supported by proofs; the practical claims ("robust policy dominates") are only weakly supported by the experiments.
- **Soundness of experiments:** Low. Two datasets, no error bars, no baselines, no verification of calibration condition, insufficiently described adversarial construction.
- **Clarity:** Good. The paper is well-written and the structure is clear.
- **Value to community:** The theoretical results will be of interest to the calibration and decision-making communities. The experiments are too thin to drive practical adoption.

The paper makes a genuine theoretical contribution but the experimental validation is significantly below what the paper's framing promises. The theory is solid enough to stand, but the paper would be substantially stronger with proper empirical validation. I score it at the upper end of the mid-range, slightly above the calibration evaluation paper (5.67) due to stronger theoretical novelty, but below the certified calibration paper (6.75) which had both theory and thorough experiments.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>