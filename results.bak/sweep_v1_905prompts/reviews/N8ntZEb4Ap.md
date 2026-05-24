## Summary

AutoNFS proposes a fully differentiable neural feature selection method that uses Gumbel-Sigmoid sampling to learn a binary mask and a cardinality penalty to automatically determine how many features to retain, without requiring the user to specify a feature budget *a priori*. The method is evaluated on 11 OpenML benchmarks (with 3 corruption scenarios against 10 baselines) and on 24 real-world metagenomic datasets, with additional complexity and feature-quality analyses.

---

## Strengths

- **Automatic cardinality determination is a genuine practical advantage.** The penalty term $\mathcal{L}_{\text{select}} = \frac{1}{D}\sum m_j$ lets AutoNFS learn *how many* features to keep, eliminating a hyperparameter that most FS methods require (Table 1, RHS, shows reductions e.g., 28→14 for Higgs, 27→14 for Helena). This is clearly demonstrated and fills a real gap.

- **Comprehensive benchmark evaluation.** The paper follows the Cherepanova et al. (2023) benchmark, evaluating on 11 datasets across 3 corruption scenarios with 10 baseline methods including Lasso, LassoNet, XGBoost, RF, Deep Lasso, and others (Figure 2). The consistent rank advantage (lowest average rank across all three scenarios) is a meaningful signal even accounting for the sparsity confound discussed below.

- **Feature-quality analyses go beyond raw accuracy.** The misselection error analysis (Figure 3a, AutoNFS achieves zero errors on random and corrupted features) and the predictive power analysis (Figure 3b, average decrease of 0.313 if any selected feature is removed) provide complementary evidence that the method is identifying genuinely relevant features, not just any small subset.

- **Real-world validation on metagenomic data.** Experiments on 24 biological datasets reduce average dimensionality from 535 to 41 (7.7%) while slightly improving accuracy for both MLP (+0.8 pp) and RF (+1.2 pp) downstream classifiers (Table 2). This demonstrates practical applicability in a high-stakes domain.

- **Computational complexity analysis across five orders of magnitude.** The log-log plot (Figure 4a) from $10^2$ to $10^5$ features with confidence intervals over 5 runs (Figure 4b) is a more thorough scaling evaluation than most feature selection papers provide.

---

## Weaknesses

### Fatal

None.

### Major

- **Baseline comparison is not controlled for sparsity, confounding the central performance claim.** All baseline methods are constrained to select exactly $D$ features (the original dimension), while AutoNFS automatically selects far fewer (e.g., 65 out of 128 for AL; 65–90% reductions). The paper acknowledges this asymmetry but does not address it experimentally. This means the reported performance advantage could partly reflect the *quantity* of features retained (AutoNFS discards more noise because it is allowed to) rather than the *quality* of the selection mechanism. A proper comparison would either (a) tune each baseline's sparsity hyperparameter to match AutoNFS's budget, or (b) report performance across a range of feature counts for all methods. Without this, the headline claim that AutoNFS "consistently outperforms all competitive methods" (Figure 2) is not fully supported by the evidence.

- **The near-constant complexity claim ($\alpha \approx 0.08$) is empirically reported but physically unexplained.** The masking network $f_\phi$ has an output layer of size $D$, requiring at least $O(H \cdot D)$ multiply-adds per batch. Other methods with $O(D)$ complexity (ANOVA, Mutual Information) correctly show $\alpha \approx 1.0$. The paper does not explain what is being timed ("Feature Time"), whether it excludes the task network, or how linear-in-$D$ operations in $f_\phi$'s output layer produce $\alpha \approx 0.08$. Even if the empirical observation is correct (e.g., because constant overheads dominate in this implementation), the paper's framing as "nearly constant computational overhead regardless of input dimensionality" (§1, §5) and "significant algorithmic advancement" (§4.3) overstates what can be concluded without a theoretical justification or a breakdown of where time is spent.

### Minor

- **The metagenomic evaluation lacks comparisons to other feature selection methods.** Only "no feature selection" (full data) is used as a baseline. The paper's title and abstract claim AutoNFS outperforms "both classical and neural FS methods," but this is not tested on the real-world data. Including even one or two common FS methods (e.g., Lasso, RF importance) on these datasets would substantially strengthen the real-world validation.

- **No statistical significance tests accompany the rankings in Figure 2.** The differences in average rank (e.g., AutoNFS 2.1 vs. Deep Lasso 3.8 in the corrupted scenario) appear meaningful, but without a Friedman test with post-hoc Nemenyi or similar, it is unclear whether the gaps are statistically reliable across datasets.

- **The masking network design is not motivated or ablated.** The architecture passes a fixed random embedding $e$ through a neural network $f_\phi$ to produce logits, rather than learning the logits directly as $D$ free parameters. The paper does not explain why this parameterization is beneficial or test whether it matters.

### Trivial

- **GFS-NetWork naming inconsistency in Figure 2.** The figure and table label the method as "GFS-NetWork" while the rest of the paper uses "AutoNFS." The caption says "AutoNFS (GFS-NetWork)" without explanation. This appears to be a leftover from an earlier naming convention and should be unified.

- **Inconsistency in the selection penalty formula.** Section 3.3 defines $\mathcal{L}_{\text{select}} = \frac{1}{D}\sum_j m_j$, but Algorithm 1 (line 14) writes $\frac{1}{B}\sum_j m_j$. These differ by a factor of $B/D$ and should be reconciled.

---

## Nice-to-Haves

- An ablation comparing the full masking network $f_\phi(e)$ against learning logits directly as $D$ free parameters would clarify whether the network adds value.
- Sensitivity analysis for $\lambda$ (the sparsity-accuracy tradeoff) in the main text rather than only in the appendix would strengthen the "automatic" claim.
- Including STG and Hard-Concrete as baselines (both discussed in related work but absent from the benchmark) would better position the method relative to the most related differentiable FS approaches.

---

## Removed Points

(Points from the inputs that were filtered as noise, speculation, or factually incorrect.)

- **"Baselines are not performing selection in any meaningful sense"** — Removed because it is factually incorrect. Baselines select $D$ features out of $1.5D$ (original + corrupted), which is genuine selection.
- **"Naming inconsistency casts doubt on whether the evaluation pipeline was run for the exact method described"** — Removed as overwrought speculation. The caption is consistent ("AutoNFS (GFS-NetWork)"), suggesting a previous name.
- **"The paper should not be accepted in its current form"** from the harsh critic's overall assessment — treated as an input to judgment, not a factual weakness.
- **Strength Finder strengths about "near-constant computational complexity"** — Not removed entirely but downgraded by framing the complexity claim as requiring justification.
- **Strength Finder claim "consistently best average rank across three feature corruption scenarios"** — Retained in Strengths but caveated in Weaknesses due to the sparsity confound.
- **Criticism about $\lambda=1$ making "automatic" overstated** — Weakened to nice-to-have; fixing $\lambda$ and still getting good results across datasets is a reasonable design choice, not a flaw.
- **Criticism about missing related works** — Removed as per policy (cannot verify missing references).
- **Formatting, typo, and appendix-related criticisms** — Removed as per policy.
- **"The method is not novel in the context of existing differentiable FS approaches"** — Removed as a subjective opinion not backed by specific evidence, and the paper does cite STG, Hard-Concrete, Concrete Autoencoders, and LassoNet in related work.

---

## Novel Insights

None beyond the paper's own contributions. The key tension — that automatic cardinality is a genuine practical advantage but that demonstrating it fairly requires controlling for sparsity in baselines — is well-recognized in the FS literature and is the central unresolved issue in this submission.

---

## Suggestions

1. **Redesign the main benchmark to control for sparsity.** Either tune each baseline's sparsity hyperparameter to match AutoNFS's automatically chosen budget, or report performance curves across a range of feature counts for all methods. This is the single change that would most improve the paper's evidential strength.

2. **Provide a clear definition of "Feature Time"** in the complexity analysis and explain why linear-in-$D$ operations in $f_\phi$ do not dominate the scaling. If the near-constant observation is real, include a theoretical complexity analysis (e.g., showing that the $O(D)$ cost is amortized over a large batch size or dominated by the task network's constant overhead).

3. **Add FS baselines to the metagenomic evaluation** (e.g., Lasso, RF importance with a threshold) to support the claim that AutoNFS outperforms other FS methods on real-world data, not just on synthetic corruption benchmarks.

---

## Score and Decision

I calibrate against the following anchors from the human-review corpus:

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| difFOCI | KiN7g8mf9N | 6.00 | R1 middle | Accepted. Stronger theoretical grounding; experiments less comprehensive but better controlled. AutoNFS is weaker. |
| RelChaNet | 3M3jtMDjUb | 5.25 | R2 | Rejected. Comparable scope (neural FS, multi-dataset eval) but AutoNFS has more datasets and a cleaner method. However, AutoNFS's evaluation confound is more severe. |
| Unsupervised FS dynamic approach | Ai4L058yoO | 4.50 | R1 middle | Rejected. Weak method description and limited experiments. AutoNFS is clearly stronger in method clarity and evaluation breadth. |
| Feature selection with neural MI | lt6xKGGWov | 2.33 | R1 weak | Rejected. Poor execution. AutoNFS is substantially better. |

**Round 1 bracket**: I queried weak anchors (score < 3.5), middle anchors (3.5–7.5), and strong anchors (> 7.5). The strong anchors (scores 8–8.2, about LLM pre-training and sparse autoencoders) are in a completely different league and are not comparable. The paper clearly sits in the middle band.

**Round 2 narrowing**: Inside the middle band, RelChaNet (5.25, rejected) is the most topically similar — both are neural network FS methods with multi-dataset evaluations. AutoNFS has a cleaner method formulation and more extensive experiments, but the RelChaNet evaluation is more carefully controlled (it does not have the sparsity confound). The difFOCI paper (6.0, accepted) has stronger theoretical support. Comparing against these anchors, AutoNFS's core evaluation flaw prevents it from reaching the 6.0 bar, but its method is cleaner than the 4.5 anchor. **Final score: 4.5.**

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>