Now I have a thorough understanding of the paper. Let me compose the final review.

## Summary

This paper introduces **stochastic partial-multivariate methods** for multivariate time-series forecasting, generalizing existing univariate (S=1), deterministic partial-multivariate (Dirac-delta P), and complete-multivariate (S=D) approaches into a unified framework. The authors propose **SPMformer**, a Transformer that stochastically samples feature subsets of size S and computes attention only within each subset. Training uses random partitioning to avoid redundancy/omission, and inference can average over multiple random partitionings. Experiments across long-term, short-term, and probabilistic forecasting (13/15 best scores) demonstrate consistent SOTA performance, along with computational efficiency and robustness to missing features.

---

## Strengths

- **Conceptual unification of forecasting paradigms (Section 3.1).** The paper formalizes how univariate (S=1), deterministic partial-multivariate (Dirac-delta distribution over subsets), and complete-multivariate (S=D) methods are all special cases of the stochastic partial-multivariate framework. This is a genuine conceptual contribution that places disparate prior work in a common lens.

- **Consistent and broad empirical superiority (Tables 1–3).** SPMformer achieves the best score in 13 out of 15 settings across long-term, short-term, and probabilistic forecasting tasks, against a strong set of baselines including PatchTST, iTransformer, Crossformer, TSMixer, and TimesNet. This breadth of empirical success is the paper's strongest evidence and is not undermined by any of the identified weaknesses.

- **Empirically validated U-shaped performance curve with optimal subset size (Figure 3, Table 4).** The paper systematically varies S and demonstrates that partial-multivariate settings (1 < S < D/2) consistently outperform both univariate (S=1) and complete-multivariate (S=D) extremes, confirming the central design intuition with clear experimental evidence.

- **Inference-time stochastic averaging improves performance with a transparent trade-off (Figure 5).** The paper shows that repeating inference with different random subsets and averaging outputs monotonically reduces test MSE as N_I increases, providing a practical accuracy lever that practitioners can calibrate to their latency budget.

- **Computational efficiency and missing-feature robustness (Figures 6–7).** The inter-feature attention cost of SPMformer scales as O(S·D) with small S (e.g., S=20–30 for D=862), substantially cheaper than O(D²). The missing-feature experiment demonstrates a genuine practical advantage over the complete-multivariate variant of the same architecture.

---

## Weaknesses

### Fatal
None.

### Major

- **Theoretical analysis in Section 3.5 uses flawed PAC-Bayes reasoning and should not be presented as a formal justification.** The paper claims that the PAC-Bayes bound's m (number of training instances) varies with S because m ∝ (D choose S) — "each subset is regarded as a separate instance." This is incorrect: m refers to the number of training examples drawn from the data distribution, which is fixed (≈ total time-series windows), not to the combinatorial number of feature subsets. Theorem 2 is stated without proof, and the authors admit they cannot evaluate H(Q) to compare the magnitudes of the effects. The empirical finding of a U-shaped curve is real and valuable, but the formal theoretical covering is unsound. The paper would be stronger stating the intuition as a conjecture or empirical observation rather than as a theorem-backed rationale. *(Verified: lines 114–120 explicitly state "m ∝ (D choose S)" because "each subset is regarded as a separate instance"; this is fundamentally wrong.)*

### Minor

- **Controlled comparison against a deterministic version of SPMformer is absent.** The paper's unique claim is that *stochastic* grouping outperforms *deterministic* grouping. While Figure 4 varies the subset-pool size (showing more subsets → better performance), and CAMELOT is included as a deterministic baseline, there is no direct ablation where SPMformer is trained with a *fixed* set of subsets (e.g., one fixed partition reused every iteration) while keeping all other architecture choices identical. Such a comparison would cleanly isolate the benefit of stochasticity over determinism. Figure 4 partially addresses this (α=1 approximates a fixed pool), but a cleaner ablation with a truly frozen partition would strengthen the core claim.

- **The inference cost claim ("without any additional computation cost") is misleading.** The paper describes running the model N_I times and averaging outputs, which clearly multiplies inference FLOPs by N_I. *(Verified: line 98 contains a truncated sentence; the claim as extracted is "without any additional computation cost (i…" — even if completed differently, the N_I× cost is real and should be explicitly acknowledged with a trade-off discussion.)* Figure 5(a) shows accuracy gains versus N_I, but the corresponding cost axis is missing. A practical MSE-vs-FLOPs plot would make the trade-off actionable for practitioners.

- **No confidence intervals, error bars, or multi-seed results are reported.** All metrics appear as point estimates without standard deviations or significance tests. Given the known variability of forecasting metrics across random seeds and data splits, reporting error bars (e.g., over 3–5 runs) would make the empirical claims more convincing and allow readers to assess whether the reported margins over baselines are statistically reliable.

- **Baseline hyperparameter fairness is not clearly stated.** The paper does not specify whether baselines were retrained with tuned hyperparameters under a fair budget or taken from previously reported numbers. If the latter, the comparison may systematically favor SPMformer due to more careful tuning. This should be clarified in the experimental setup.

- **No dedicated limitations section.** The paper acknowledges some limitations indirectly (e.g., the assumption D is divisible by S, the use of uniform P when prior knowledge is unavailable), but a candid paragraph discussing these and other constraints (e.g., sensitivity to S choice, the cost of temporal attention not addressed by the scheme) would improve the paper's credibility and steer future work.

### Trivial

- **Subset size choices (S) lack a validation study.** The paper states S=3 for ETT (D=7), S=20 for Traffic (D=862), etc., satisfying 1 < S < D/2, but does not describe a validation procedure for selecting these values. A small validation study on one or two datasets showing that chosen S are near the optimum of the U-shaped curve would increase confidence.

- **The α values in the subset-pool experiment (Figure 4) are not motivated.** The sequence α ∈ {1, 400, 1600, 6400, Max} is used without explanation of how these values were determined.

---

## Nice-to-Haves

- An ablation comparing random partitioning (Algorithm 1) against naïve uniform sampling (independent sampling without the disjoint constraint) to justify the design choice.
- A discussion of how the method generalizes to cases where D is not divisible by S (e.g., padding or partial subsets).
- An exploration of learned/non-uniform P distributions guided by feature-attention scores, building on the preliminary analysis in Table 5.

---

## Removed Points

- **"The missing-features experiment (Figure 6) is unfair because SPMformer excludes missing features while CMformer pads with zeros."** This comparison is between SPMformer and its complete-multivariate variant (same architecture, S < D vs. S = D). It is a fair ablation demonstrating a real structural advantage of the partial-multivariate design, not a claim of SOTA missing-data handling. The point is that the partial-multivariate design *inherently* handles missing features — this is correct and worth showing.

- **"Figure 7 FLOPs comparison should include total model FLOPs."** The paper explicitly scopes the comparison to inter-feature attention FLOPs and states this clearly. The figure serves its stated purpose as a lower-bound comparison.

- **"The subset pool experiment α values and the averaging over forecast horizons are poorly motivated / hide variation."** The paper references a supplement for per-horizon results (standard in this field), and the α values, while not motivated in detail, support the claimed monotonic trend. These are at most presentation nitpicks.

- **"The ETT subset size S=3 is close to D/2=3.5."** This is factually correct by design (1 < S < D/2 is satisfied) and the U-shaped results confirm S=3 outperforms S=1 and S=7.

- Strengths removed from Strength Finder: None of the strengths were generic or conflicting with verified weaknesses, except the claim of a "PAC-Bayes theoretical rationale" — since the theory is flawed, this framing is adjusted. The empirical finding (U-shaped curve, Figure 3) is still a genuine strength and is kept.

---

## Novel Insights

Beyond the paper's own contributions, the reviews surface the following novel perspective: the paper's core empirical finding — that optimal subset size S* lies between 1 and D/2 across diverse datasets — is robust and interesting even without the attempted PAC-Bayes justification. The U-shaped MSE curve (Figure 3) and the pool-size sensitivity (Figure 4) suggest that the benefit of stochastic partial-multivariate modeling may stem from a variance-reduction / data-augmentation effect: stochastically sampling different feature subsets acts as an implicit ensemble regularizer, similar to how dropout or Mixup introduce beneficial stochasticity. This intuition is more plausible and better supported than the formal PAC-Bayes argument, and the paper would benefit from reframing the analysis in these terms. The missing-features robustness experiment (Figure 6) is also more interesting than the review gives it credit for — it shows that the partial-multivariate design has a *graceful degradation* property under feature dropouts that complete-multivariate architectures cannot replicate without dedicated missing-data machinery.

---

## Suggestions

1. **Remove or substantially downgrade the PAC-Bayes theoretical analysis (Section 3.5).** Replace it with an intuitive argument (e.g., variance reduction via stochastic grouping, connections to dropout/mixup/ensemble methods, or a simpler bias-variance decomposition). The empirical U-shaped curves and pool-size experiments already provide strong evidence for the claims — the flawed formal framing only weakens the paper.

2. **Add a controlled ablation comparing stochastic vs. deterministic SPMformer.** Train SPMformer with a single fixed partition (reused every iteration) vs. random partitioning, keeping all other hyperparameters identical. This would directly isolate the benefit of stochasticity — the paper's unique contribution.

3. **Acknowledge and quantify the inference-time cost of the N_I averaging technique.** Add an MSE-vs-inference-FLOPs (or wall-clock time) plot for varying N_I. This turns the current misleading claim into a transparent, actionable trade-off for practitioners.

4. **Add confidence intervals or error bars** over at least 3 random seeds for the main results, and clarify whether baselines were retrained under a fair tuning budget.

5. **Add a brief limitations paragraph** covering: the assumption that D is divisible by S, the reliance on uniform P when prior knowledge is absent, the sensitivity of results to the choice of S, and the quadratic temporal-attention cost (not addressed by the feature-level stochasticity).

---

## Score and Decision

The paper introduces a genuinely novel and well-motivated idea — stochastic partial-multivariate modeling — and backs it with strong empirical evidence across multiple forecasting tasks. The main issues are fixable: the theoretical analysis needs substantial correction (or removal), a more direct deterministic-vs-stochastic ablation would strengthen the core claim, and several presentation gaps should be addressed. The empirical contribution itself is significant and the method is of clear interest to the community. These problems do not invalidate the paper's core claims but do require a major revision.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>