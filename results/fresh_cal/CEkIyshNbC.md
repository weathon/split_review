Now I have verified all claims against the paper. Let me compose the final review.

---

## Summary

This paper empirically investigates the double descent phenomenon in deep learning by analyzing the learned feature space. It proposes a metric \(P\) — the proportion of noisy training samples whose \(k\)-nearest-clean neighbors share the original (clean) label — and claims that over-parameterized models "isolate" noisy samples among clean samples of the same class, causing the second descent. Experiments cover FCNNs on MNIST, CNNs on CIFAR-10, and ResNet18s on CIFAR-10.

## Strengths

- **Novel metric \(P\) to operationalize noise handling in feature space.** The paper introduces a concrete, repeatable procedure (Equation 1, Section 3.3) using \(k\)-NN with cosine similarity on penultimate-layer representations to quantify whether noisy training points are embedded among clean samples of their original class. This provides an operational definition of "isolating" noise that goes beyond prior qualitative discussions.

- **Empirical correlation between \(P\) and test accuracy holds for two of three architectures.** For FCNNs on MNIST, \(P\) rises to nearly 100% after the interpolation threshold, closely mirroring test accuracy (Figures 1b,c). For CNNs on CIFAR-10, \(P\) rises to ~60%, again tracking test accuracy (Figures 2b,c). The paper explicitly notes this alignment (Section 4, paragraph on FCNN results; paragraph on CNN results).

- **Honest reporting of the contradictory ResNet18 result.** The paper acknowledges that for ResNet18, \(P\) drops to zero at the interpolation threshold (Section 4, line 173: "this observation contradicts our hypothesis"). It introduces a complementary analysis using assigned noisy labels rather than clean labels, showing that over-parameterized ResNets predict noisy labels with high accuracy. While this undermines the central claim, the transparency is a methodological strength.

## Weaknesses

### Fatal
None.

### Major

- **The ResNet18 result directly contradicts the proposed mechanism, and the paper does not resolve this contradiction.** The central claim is that over-parameterized models "isolate" noisy samples among clean samples of the *same original class*, and this explains double descent. For ResNet18 on CIFAR-10, \(P\) (clean-label accuracy) drops to **zero** at the interpolation threshold and stays there (Figure 3). The complementary analysis shows that \(k\)-NN predicts the *assigned noisy* labels instead, meaning the model has not isolated noise among clean samples — it has memorized the noise. The paper's attempted resolution (that "over-parameterized CNNs surpass ResNets by 5% in test accuracy," stated without figure reference) does not explain *why* the mechanism works for FCNNs and CNNs but reverses for ResNets. A proposed mechanism that fails for one of three architectures — and that architecture (ResNet18) is the most practically relevant — is not a general explanation of double descent. The paper offers no principled account for this architectural dependency.

- **The claimed correlation between \(P\) and test accuracy is supported only by visual inspection, with no quantitative evidence.** The paper states repeatedly that \(P\) "aligns" with test accuracy and is opposite to test loss, but no correlation coefficients, rank correlations, or mutual information measures are provided. For CNNs on CIFAR-10, the rise in \(P\) after the threshold is modest (from ~40% to ~60%), while test accuracy rises more substantially — it is unclear how closely they track. The paper calls \(P\) a "weak predictor of generalization performance" but offers no statistical validation for this claim. Given that the paper's main empirical contribution is this correlation, the lack of quantitative support is a significant gap.

- **The "perfect learner vs. imperfect learner" theoretical framework in the Conclusion (Figure 4) is speculative and unsupported by the experiments.** The paper introduces a taxonomy claiming that double descent arises only for "imperfect learners with sub-optimal regularization" (Section 5). However, the experiments never vary regularization, never test models with optimal early stopping or explicit regularization, and never demonstrate that a "perfect learner" suppresses double descent. The diagram (Figure 4) is purely illustrative. Presenting this as a finding or implication of the paper's experiments is misleading; it is an untested conjecture.

### Minor

- **The \(k\) value for the \(k\)-NN analysis of \(P\) is never specified.** Section 3.3 defines \(P\) using \(k\)-nearest neighbors within the clean subset, but the value of \(k\) is absent from the entire paper. The qualitative behavior of \(P\) across architectures could be sensitive to this choice. This is a concrete reproducibility gap for a paper centered on this metric.

- **Different training regimes across architectures complicate cross-architecture comparisons.** FCNNs are trained for 4000 epochs with one learning rate schedule, while CNNs and ResNets are trained for 200 epochs with a different schedule. The paper does not discuss whether the differing training lengths or schedules affect the observed patterns of \(P\).

- **No variability or confidence information is reported.** The paper states that experiments are "replicated multiple times" and results are averaged (Section 3.2), but no error bars, standard deviations, or confidence intervals appear on any curve. Given that each experiment involves resampled label noise, this is a standard reporting expectation.

- **The claim that "over-parameterized CNNs surpass ResNets by 5% in test accuracy" is stated without a figure or table reference.** The reader cannot verify this claim from the provided figures. This is important because the paper uses this comparison to argue that the \(P\) metric is linked to generalization.

- **The claim that the noise-isolation phenomenon "has not been previously documented" (Abstract) is overstated.** The connection between noise memorization and feature-space geometry in over-parameterized models is discussed in the existing literature cited by the paper itself (e.g., Gamba et al. 2022 on interpolation sharpness for clean vs. noisy points; the benign overfitting literature). The specific \(k\)-NN operationalization may be new, but the broad claim of novelty is too strong.

### Trivial

- The prose defining \(P\) (Section 3.3) is slightly ambiguous: it should clarify more explicitly that the majority vote is computed over *clean training* neighbors specifically. The equation is correct, but the surrounding text could be clearer.

## Nice-to-Haves

- Computing correlation coefficients (Spearman rank or similar) between \(P\) and test accuracy across model widths would substantiate the paper's central claim.
- Varying the \(k\) in \(k\)-NN and showing robustness of the qualitative patterns would strengthen the analysis.
- Direct measures of feature-space separation beyond \(k\)-NN (e.g., distance ratios between noisy-clean and noisy-noisy pairs) would triangulate the "isolation" claim.
- An ablation contrasting models with and without explicit regularization (e.g., weight decay) could test the "imperfect learner" speculation in the Conclusion.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"No discussion of competing explanations"** (Harsh Critic). The paper's Related Work section (Section 2) explicitly cites bias-variance decomposition (Yang et al. 2020), decision boundaries (Somepalli et al. 2022), and interpolation sharpness (Gamba et al. 2022). The paper engages with these in the text (lines 30–32). This criticism is factually incorrect. **Removed.**

- **"Cosine similarity normalization unclear" / "whether representations are normalized before computing distances matters"** (Harsh Critic). The paper defines cosine similarity as \(S_C(A,B) = (A·B)/(\|A\|\|B\|)\) (line 76), which inherently normalizes the vectors. The computation is fully specified. **Removed.**

- **"Whether the peak is an artifact of optimization"** (Harsh Critic, "catastrophic overfitting early in SGD"). This is pure speculation with no evidence or basis in the paper. **Removed.**

- **"Reproducibility concerns about undisclosed hyperparameters"** (Harsh Critic Section-by-section on missing replicates number, etc.). The paper states experiments are replicated and averaged (line 67). The number of replicates is not a standard requirement for submission and falls under the "trivial implementation details" exclusion. **Removed.**

- **Strength Finder strength conflated about "comparative analysis across architectures revealing nuanced behavior"** — This is retained (in Strengths) but only the honest-reporting aspect is kept; the claim that this "supports" the paper's thesis is not kept because the finding contradicts the thesis. Adjusted accordingly.

## Novel Insights

None beyond the paper's own contributions. The reviews add no genuinely novel observation — the harsh critic's structural critique (ResNet contradiction undermines the mechanism) is a valid analysis of what the paper itself reports, not a new scientific insight.

## Suggestions

- **Resolve or explicitly bound the ResNet18 contradiction.** Rather than saying "this contradicts our hypothesis" and pivoting to a CNNs-vs-ResNets comparison, the paper should either revise the hypothesis to account for architectural dependency, or present this as a finding that the noise-isolation mechanism is architecture-specific. A more honest framing: "For some architectures (FCNN, simple CNN), we observe noise-isolation correlated with double descent; for ResNet18, we observe the opposite — memorization of noise. This suggests the mechanism depends on architectural properties (e.g., depth, skip connections)."

- **Provide quantitative evidence for the \(P\)-performance correlation.** Compute Spearman rank correlation (or similar) across model widths for each architecture/noise-level combination. Report confidence intervals for key curves.

- **Specify \(k\) for the \(k\)-NN analysis and justify the choice.** Ideally, show that the qualitative pattern is robust to the choice of \(k\).

- **Either remove the "perfect/imperfect learner" discussion from the Conclusion or add experiments that test it** (e.g., comparing models with and without weight decay or early stopping).

- **Add error bars or confidence intervals** to at least the main curves (test error, test accuracy, \(P\)) to show variability across replicates.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>