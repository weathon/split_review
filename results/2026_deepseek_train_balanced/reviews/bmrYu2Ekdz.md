## Summary

This paper introduces PolyPythias, a multi-seed extension of the Pythia model suite consisting of 45 new training runs (9 new seeds × 5 model sizes from 14M to 410M parameters) with ~7k publicly released checkpoints. The authors use this resource to study LM pre-training stability across downstream performance, linguistic representations, and parameter dynamics, identifying two outlier training runs (410M, seeds 3 and 4) and analyzing learning phases common across model sizes. The resource itself fills a genuine gap in publicly available multi-seed decoder-only training data.

## Strengths

- **Largest publicly released multi-seed, multi-size decoder-only training suite with dense checkpoint coverage.** The paper introduces 45 new training runs (9 seeds × 5 sizes, 154 checkpoints per run ≈ 7k total checkpoints) with released pre-tokenized and pre-shuffled datasets per seed. This is compared explicitly against prior resources: MultiBERTs (25 seeds, 1 encoder-only size, limited intermediate checkpoints), Karamcheti et al. (10 runs, 2 decoder-only sizes), and Madaan et al. (10 runs, 1 size, not publicly available) — §1. No prior resource provides this combination of seed count, size range, checkpoint density, and public release for decoder-only models.

- **Systematic triangulation of outlier identification across three independent levels of analysis.** Outlier runs (410M seeds 3 and 4) are flagged via a principled ±2 SD threshold on downstream accuracy across multiple tasks (§3.2), independently confirmed by training maps that exhibit forking (a non-linear transition structure absent from all other runs — §5.2, Fig. 4), and traced to specific loss spikes (App. A). The paper further identifies the specific parameter changes driving this forking (Table 3), showing that outlier runs fail the state ②→③ transition and exhibit abnormal transitions driven by increased variance of singular values. This multi-level convergence is stronger than prior single-method outlier analyses.

- **Convergent evidence for two specific learning phases that generalize across architectures.** Downstream accuracy (§3.2, Fig. 1), representational metrics (macro-F1, codelength ratio, SSA — §4.2, Fig. 3), and HMM state transitions (§5.2, Table 1, Fig. 4) all independently locate an initial learning phase at steps 10³–10⁴ and a critical learning phase at steps 10⁴–10⁵. The paper explicitly notes this matches prior findings for encoder-only models (Müller-Eberstein et al., 2023) and LSTM architectures (Saphra & Lopez, 2019) — §6.

## Weaknesses

### Major

- **The "early deviation" observation in Section 5.2 is not properly validated as a forward-looking finding.** The paper states that "the outlier runs start to deviate from the other runs long before they show worse scores on the performance metrics." However, the HMM is fitted on the *full* trajectory of all checkpoints for each run, and state assignment (via Viterbi or equivalent) uses information from the entire sequence. The qualitative observation in Fig. 4 is suggestive, but a genuine demonstration of early detection would require fitting HMMs using only data up to an early cutoff (e.g., step 10k or 20k) and checking whether outliers are already identifiable. This is not done, so the "early deviation" claim conflates retrospective description with true early detection.

- **The regression analyses (Tables 1, 2) lack any robustness evaluation despite a very small effective sample size.** For the 410M model, n=10 data points are used in the linear regression of bag-of-states against z-scores. The reported R² = 0.99 (410M's own HMM) and R² > 0.9 (zero-shot cross-size HMMs) are heavily influenced by the two outlier points (seeds 3 and 4) being far from the mean — with 2/10 points driving most of the variance. No cross-validation, leave-one-out analysis, bootstrapping, or any robustness check is performed. Without such validation, the R² values primarily measure descriptive fit, not predictive power. The paper should report leave-one-out or permutation-based significance tests, and clearly communicate the small effective sample size.

- **The abstract's framing ("show the potential of using these methods to predict training stability") overclaims relative to what the experiments demonstrate.** The "zero-shot prediction" in Section 5.2 is cross-size post-hoc state assignment: an HMM trained on a smaller model's *full* trajectory is used to assign states to the 410M's *full* trajectory. This is not forward prediction of training outcomes from early data, nor is it a test of whether the method works on unseen runs. The paper acknowledges this limitation in passing ("We leave the investigation of which properties can be predicted from the bag-of-states of early checkpoint metrics as future work"), but the abstract and Section 6 discussion ("predict training maps in a 'zero-shot' fashion... suggesting that statistics... are informative of their larger counterparts") convey a stronger claim than the evidence supports. The claims should be recalibrated to distinguish between (a) cross-size transfer of descriptive HMMs and (b) forward prediction of training outcomes.

### Minor

- **The cross-size representational correlation analysis (§4.2) reports r ≈ 0.99 for macro-F1, but this metric is monotonically increasing over training for all model sizes.** When any two monotonic sequences are compared, the Pearson correlation will be high by construction, regardless of whether the trajectories encode meaningful information about representational dynamics. The paper does not discuss this base-rate issue. The codelength ratio and SSA metrics are less affected by this artifact and provide more informative evidence.

- **Checkpoint evaluation leaves a notable gap between steps 512 and 1k, and between 1k and 3k (§3.1).** Given that step 10³ is identified as critical across multiple analyses (initial learning phase, inter-seed agreement peak, emergence of coherent outputs), the absence of checkpoints between 512 and 1k (488 steps) and between 1k and 3k (2,000 steps) means important dynamics in this region are undersampled. This is a data limitation worth acknowledging more explicitly.

- **The paper does not examine whether the 410M outlier seeds (3 and 4) show anomalous patterns in the representational analyses (§4).** Outlier seeds are identified via accuracy (§3.2) and training maps (§5), but there is no check of whether these same seeds exhibit divergent representational dynamics in the MDL probing metrics (macro-F1, codelength ratio, SSA). This would strengthen the triangulation claim.

- **The claim that "all benchmarks still improve past the optimal token count predicted by the Chinchilla scaling law" (§6) is stated without quantitative support.** No numbers or figures are provided to substantiate the degree of improvement or the specific token counts involved.

### Trivial

None.

## Nice-to-Haves

- Future work could genuinely test forward prediction by using only early-checkpoint data (e.g., first 10k steps) for HMM fitting and evaluating whether bag-of-states from early data predicts final performance on held-out seeds.
- Reporting the coefficient of variation (std/mean) for each metric across seeds would provide a more interpretable measure of stability than raw standard deviations.
- A bootstrap-based confidence interval on the regression R² values would strengthen the evaluation without requiring more data.

## Removed Points

These points were raised by the reviewers but removed after verification against the paper:

- **"Outlier detection and predictive modeling rest on n=2 observations"** — the regression analyses use all 10 seeds for 410M (n=10), not just 2. The two outliers strongly influence the results, but the analysis does not "rest on" them alone. The removed framing was replaced with a more accurate criticism about small sample size and lack of robustness checks.
- **"Dual claims in tension"** — "largely stable with rare outliers" is a coherent characterization, not a contradiction. Removed as a manufactured tension.
- **κ ≈ 0.5 as "~25% disagreement"** — this is a misinterpretation of Cohen's κ, which is chance-corrected agreement. Removed.
- **"Remarkable" claim about outliers** — the paper uses "remarkably" to note the small number of outliers found, and the critic's single-task binomial calculation does not account for the cross-task consistency of the same two seeds.
- **HMM state count criticism** — the paper already states that |S|=5 is "optimal (or close to optimal) for all sizes." Removed as already addressed.
- **Bias reliability criticism** — the paper explicitly acknowledges the reliability issue ("the large variance observed for the bias measures reflects the poor reliability"). Removed as already addressed.
- **Formatting, grammar, style, and missing appendix/content criticisms** — removed per hard rules (parser artifacts, not author errors).
- **Generic "evaluation lacks rigor" / "baselines may not be fair" area sweeps** — removed for lacking concrete anchors in the paper.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a genuine tension the authors should address: the paper simultaneously wants to claim that LM pre-training is "largely stable" and that the training-map methodology can detect and characterize outliers. These are compatible in principle, but the paper never defines what level of seed-induced variation would constitute meaningful instability versus acceptable noise. With κ ≈ 0.5 (moderate agreement) on downstream predictions and 2/10 seeds at 410M being clear outliers, different readers will draw different conclusions about stability. The paper would benefit from a more nuanced characterization — e.g., reporting the coefficient of variation per metric rather than a binary stable/outlier distinction, and discussing what level of variation matters for different use cases (benchmarking vs. deployment vs. scientific understanding of learning dynamics).

## Suggestions

1. Recalibrate the claims: distinguish clearly between (a) cross-size transfer of descriptive HMMs and (b) forward prediction of training outcomes. The abstract and conclusion should reflect what the experiments actually demonstrated.
2. Add robustness checks for the regression analyses: report leave-one-out cross-validation or bootstrap confidence intervals for the R² values in Tables 1 and 2.
3. Clarify the "early deviation" finding by noting that the HMM uses full-trajectory information for state assignment, and add a forward-only analysis (HMM fitted on early checkpoints only) if feasible, or explicitly flag this as an open question.
4. Address the monotonicity artifact in §4.2 by explicitly discussing why macro-F1 correlations are inflated and what the non-monotonic metrics (SSA, codelength ratio) independently show.
5. Add a quantitative statement for the Chinchilla scaling law claim (§6), or remove it.

## Score and Decision

<score>6.0</score>
<decision>Accept</decision>