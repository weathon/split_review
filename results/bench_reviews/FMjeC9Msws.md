## Summary

This paper conducts a large-scale systematic study (400,000+ GPU-hours) of RL compute scaling for LLMs, proposing a sigmoidal compute-performance curve (Equation 1) that separates asymptotic performance (A) from compute efficiency (B). Through extensive ablations — including off-policy setup, loss functions, precision, normalization, and curriculum — the authors develop SCALERL, a recipe whose 100,000 GPU-hour run follows its extrapolated scaling curve. The paper provides empirical evidence that some design choices (loss type, FP32 precision) affect the asymptote A, while most others (loss aggregation, advantage normalization, curriculum) primarily modulate efficiency B.

## Strengths

- **Unprecedented experimental scale for academic RL research.** 400,000 GPU-hours across systematic ablations, with individual runs up to 100,000 GPU-hours (3.5× larger than ProRL), enables observations impossible at smaller scales. The 100k GPU-hour SCALERL run with validated extrapolation from 50k is genuinely impressive.

- **Clean, principled distinction between asymptote (A) and efficiency (B).** The sigmoidal framework (Equation 1) provides a coherent language for characterizing design choices — identifying which affect the ceiling (loss type, FP32 precision) versus which affect speed of convergence (aggregation, normalization, curriculum). This separation is practically useful and methodologically sound.

- **Rigorous leave-one-out ablations at 16k GPU-hours.** Each component of SCALERL is validated by reverting it individually at a fixed large compute budget, providing strong evidence for the cumulative contribution of each design choice even when individual effects are modest.

- **Generalization across multiple compute axes.** The paper validates the scaling framework across model size (8B dense to 17B×16 MoE), batch size (2.5× larger), generation length (up to 32K tokens), and multi-task settings (math + code), with extrapolated curves aligning with extended training in all cases.

- **Downstream generalization correlation.** AIME-24 results (Figure 1b) show that in-distribution validation performance correlates with downstream benchmark gains, bridging the gap between the paper's primary metric and practical relevance.

## Weaknesses

### Fatal
None.

### Major

1. **"Predictive scaling" is demonstrated via within-run extrapolation, not cross-run prediction.** The paper's central claim is about predicting performance at larger compute from smaller-scale runs. However, every demonstration (Figures 1, 2, 5, 6) fits the sigmoidal curve on the *first half* of a single run and validates on the *second half of the same run*. This tests curve-fitting stability, not genuine cross-scale prediction where independent runs at different total compute budgets predict a held-out larger run. The gold standard — fitting on, say, three runs at 5k, 10k, and 20k GPU-hours and predicting performance at 100k — is absent. The paper would be stronger if it reframed its contribution around *early-to-late extrapolation within a recipe* rather than claiming the full analogy to pre-training scaling laws (which predict across independent compute budgets, model sizes, and data amounts). This gap does not invalidate the paper's empirical contributions, but the central methodological claim is oversold.

2. **No multi-seed experiments or confidence intervals for key comparisons.** All results are from single runs. The LOO experiments report B values ranging from 1.62 to 2.09 (Figure 5), but without multiple seeds or confidence intervals, it is impossible to assess whether these differences are statistically significant. This matters because: (a) the paper's framework hinges on quantifying small B differences across design choices, and (b) RL training is known to be noisy. For a paper whose core contribution is a *quantitative* framework with fitted parameters, the absence of uncertainty quantification is a gap.

### Minor

1. **Comparison against prior methods (Figure 2) lacks evidence of controlled re-implementation.** SCALERL is compared against DeepSeek (GRPO), Qwen2.5 (DAPO), Magistral, and MiniMax. While these are implemented as described in their respective papers, there is no evidence that each method was given *equivalent tuning effort* or hyperparameter sweeps in the paper's codebase. SCALERL is the product of extensive iterative refinement (the paper's own ablations), while the comparison methods are implemented once. This creates an apples-to-oranges comparison that weakens the "surpasses all other methods" claim. The paper references Appendix A.17 for recipe descriptions, but without explicit controlled tuning, this remains a concern.

2. **Limited domain scope.** The bulk of experiments focus on verifiable math tasks with an 8B dense model. While the paper includes some code experiments and a MoE model, the generality of the framework across other domains (e.g., instruction following, safety, creative generation) is not established. The paper acknowledges this as a limitation, but it constrains the practical relevance of the scaling framework.

3. **The forward ablations (Section 3) use uneven compute budgets.** Some ablations run to 3.5k GPU-hours, others to 4k or more, because certain configurations destabilize beyond these budgets (Appendix A.16). This makes cross-comparison of A and B values across those early ablations unreliable. The paper partially addresses this with the LOO experiments at a fixed 16k budget, but the forward ablations are a key part of the evidence chain.

### Trivial
None.

## Nice-to-Haves

- **Confidence intervals on fitted A and B parameters** (e.g., via bootstrapping) would substantially strengthen the paper's quantitative claims, especially for the LOO experiments where B differences are small.
- **A demonstration of cross-run prediction** (fitting on multiple independent runs of different total compute to predict a held-out run) would validate the predictive claim more convincingly.
- **Additional downstream benchmarks beyond AIME-24** would strengthen the generalization story.

## Removed Points
*These points are flagged to be removed; treat them with caution:*

- *"The paper conflates scaling with performance at large compute"* — This is a misreading. The paper explicitly separates A (asymptote) and B (efficiency) and treats them as distinct properties. The LOO experiments showing similar asymptotes is a feature (validating the framework's ability to isolate B effects), not a flaw. **REMOVED** (misunderstands the paper).
- *"Lacks the core feature of pre-training scaling laws: parametric predictions across multiple independent axes"* — The paper explicitly scopes itself to RL compute scaling, not multi-parameter scaling laws (Section 7, "Future work"). This is scope creep. **REMOVED**.
- *"Motivation for sigmoidal over power-law is relegated to appendix"* — Standard practice; many papers place detailed justification in the appendix. **REMOVED** (format/style nitpick).
- *"Dismissal of related work is too harsh"* — Subjective opinion; the paper's characterization is defensible and specific. **REMOVED**.
- *"Scaling claims only apply to in-distribution validation"* — The paper explicitly acknowledges this limitation in Section 7. **REMOVED** (paper already addresses).
- *"Extrapolated curve is essentially a continuation of the same trend"* — This is literally what predictive extrapolation is; it being "the same trend" is the point. **REMOVED** (nonsensical criticism).
- *Strength: "Development of SCALERL, a recipe that scales predictably and outperforms existing methods"* — KEPT but caveated. The outperformance claim is weakened by the controlled comparison concern.
- *Various formatting/style nitpicks* — **REMOVED** (parser artifacts).
- *Complaints about predictive validation being limited* — KEPT as a major weakness but reframed: the paper does within-run extrapolation, which *is* a form of prediction, but cross-run would be stronger. The original reviewer's characterization that it "undermines the central methodological claim" is too harsh.

## Novel Insights

The most interesting observation from the reviews is the tension between what the paper claims ("predictive scaling methodology") and what it demonstrates (within-run early-to-late extrapolation). This reflects a deeper question about scaling law evaluation: pre-training scaling laws are valued because they predict *across* independent runs (different model sizes, data amounts, compute budgets), whereas this paper's validation is *within* a single run (early steps → later steps). The fields of RL and pre-training may have fundamentally different scaling structures — RL dynamics are path-dependent and recipe-specific in ways that pre-training loss curves are not — and directly importing the "scaling law" conceptual framework may set the wrong expectations. The paper's genuine empirical contribution (documenting which design choices matter at scale) is arguably stronger than its methodological framing would suggest.

## Suggestions

1. **Reframe the contribution.** The paper's strongest finding is not that it "predicts scaling" in the pre-training sense, but that it provides a coherent empirical framework (A vs. B) for characterizing RL design choices at scale and identifies which components truly matter. This framing is more defensible and still highly valuable.
2. **Add uncertainty quantification.** Even a single additional seed for key runs (Figure 5) or bootstrap confidence intervals on fitted parameters would substantially strengthen the quantitative claims.
3. **Acknowledge the within-run nature of the predictions explicitly.** The abstract and introduction should clarify that extrapolation is from early training to later training of the same recipe, not from small-scale standalone runs to large-scale standalone runs.

## Score and Decision

Calibration anchors (all from ICLR 2026 human reviews):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `KBut2YCZ4g.md` — Scaling Behaviors of LLM RL Post-Training | 3.50 (Reject) | Similar topic, but this paper's experiments are much larger (400k vs ~?), methodology is cleaner, and it actually validates extrapolations. Significantly stronger. |
| `dnuIoVjeGR.md` — Unified Neural Scaling Laws | 3.00 (Reject) | Criticized for overfitting and complexity; this paper's sigmoidal fit is simpler and more targeted. Stronger contribution. |
| `YwEh20x8ud.md` — BroRL | 4.00 (Reject) | Limited to 1.5B models with marginal gains. This paper operates at much larger scale with clearer methodology. Stronger. |
| `kFcP5facrQ.md` — Charting the Frontier | 4.50 (Reject) | Methodological paper about efficient scaling law fitting. Less directly comparable but similar rigor level. This paper is somewhat stronger empirically. |
| `SdHmA6BYVJ.md` — On Predictability of RL Dynamics | 5.50 (Accept Poster) | Different angle (parameter dynamics) but similar level of contribution. Both have single-seed limitations. Comparable quality. |
| `R0JM3BWP7W.md` — Tricks or Traps? | 6.00 (Accept Poster) | Cleaner controlled experiments for RL technique analysis, but narrower scope. This paper has broader contribution (scaling framework + recipe) but weaker on statistical rigor. Comparable. |
| `5wmetrh9cn.md` — Mirage or Method? | 6.00 (Accept Poster) | Well-executed empirical study. This paper's contribution is more practically oriented. Slightly below in execution quality. |

The paper has genuine, large-scale empirical contributions that are rare in academic RL research, and the A/B framework is practically useful. However, the predictive scaling claim is oversold relative to what is actually demonstrated (within-run early-to-late extrapolation rather than cross-run prediction), and the absence of multi-seed statistics undermines the quantitative strength of the framework. Compared to accepted anchors, the paper's scale and scope are strengths, but its methodological rigor on the central claim is weaker. The paper deserves acceptance but not as a top-tier submission.

**Score: 5.5**

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>