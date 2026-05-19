I have verified all claims against the paper. Now I will compose the final consolidated review.

---

## Summary

This paper investigates whether effective dimensionality — a Hessian-based measure of how many parameter directions are determined by the data — correlates with adversarial robustness across a broad set of vision models. Through experiments on 5+ architecture families (ResNet, ShuffleNet, YOLOv8, MobileNetV2, RepVGG, VGG) across 3 datasets (ImageNet, CIFAR-10/100) and 3 attack types (PGD, AutoAttack, Gaussian noise), the authors find that models with lower effective dimensionality tend to exhibit better adversarial robustness. The adversarial training experiments (AT, TRADES, MART, AWP) provide the cleanest evidence, showing a consistent linear relationship with R² ≥ 0.73 between dimensionality reduction and robustness improvement.

## Strengths

- **Large-scale, cross-architecture empirical study**: The paper tests 6 model families, 3 datasets, and 3 attack types (Section 3), providing the broadest evaluation of effective dimensionality for robustness to date. This scale gives the findings substantially more weight than prior work on smaller model sets.

- **Quantified, clean results under adversarial training**: Section 4.4 reports specific dimensionality reductions (e.g., AWP+ED reduces effective dimensionality by 29.3% for ResNet18, 30.4% for WRN28, 31.3% for WRN34) and shows a linear regression with R² ≥ 0.73 for all three models. The derived relationship — a drop of 10 in effective dimensionality corresponds to ~5.5% absolute improvement in relative adversarial performance — is the paper's most concrete quantitative finding.

- **Relative performance metric**: The paper introduces \(p_r = p^*/p\) (Section 3), which normalizes for baseline accuracy differences across architectures. This is a sensible methodological choice that directly addresses a known confound in cross-architecture robustness comparisons.

- **Honest limitation reporting**: The paper explicitly identifies outlier behavior (ResNet on ImageNet, VGG on CIFAR) in Sections 4.1 and 4.3, acknowledges the correlational nature of the findings in Section 5.1, and discusses the need for further theoretical work without overstating what the evidence supports in the discussion section.

## Weaknesses

### Fatal
None.

### Major

- **The central claim of a "near-linear inverse relationship" is not quantitatively supported for the main cross-architecture experiment.** The headline finding rests on Figure 3, which shows scatter plots of (effective dimensionality, relative adversarial performance) across multiple model families and datasets. However, the paper reports **no correlation coefficients, regression lines, or R² values** for any of the nine panels in this figure. The textual description oscillates between "general negative correlation," "clear inverse relationship," and "some inconsistencies" — language that is appropriate for an exploratory finding but does not match the strong "near-linear" framing in the abstract and conclusion. By contrast, the adversarial training experiment (Section 4.4) *does* report R² ≥ 0.73 and a concrete slope. The reader needs to know the strength of the same relationship in the primary experiment to evaluate the paper's central claim. (The paper has this data — it simply doesn't quantify it.)

- **The paper claims effective dimensionality is "more nuanced and effective" than prior robustness measures without a direct comparison.** The abstract and conclusion state that effective dimensionality provides "a more nuanced and effective metric than parameter count or previously-tested measures" (boundary thickness, flatness, Lipschitzness). The paper does compare against parameter count (Section 4.2), showing a weak cross-family correlation, but never benchmarks effective dimensionality against boundary thickness, flatness, or Lipschitzness on the same models. Citing Kim et al. (2023) that those measures are inadequate does not demonstrate that effective dimensionality is *more effective* — it only shows it is another candidate that also correlates. A head-to-head comparison (e.g., R² or rank correlation for each metric on the same model set) would substantiate this claim; without it, the claim is unsupported.

- **Outliers are identified but not adequately analyzed, undercutting the generality claim.** ResNet on ImageNet and VGG on CIFAR are explicitly flagged as outliers in both Figure 1 and Figure 3. The paper states that "the robustness of these outliers tends to follow the trend of their effective dimensionality regardless" (Section 4.1), but **no evidence is presented to support this assertion**. If ResNet on ImageNet has roughly constant effective dimensionality across model scales (Figure 1), then all ResNet variants should have similar robustness according to the paper's logic — but the paper does not verify this. The scatter plots (Figure 3) mix all architectures with shared markers, making it impossible for the reader to evaluate whether the outlier families actually follow or contradict the trend. Given that ResNet and VGG are among the most widely used architectures, this is a significant gap.

### Minor

- **PGD and AutoAttack implementation details are not reported in the main text.** The paper specifies the epsilon range (1/255 to 8/255) and Gaussian noise sigma values (0.05–0.4), but does not report PGD iteration count, step size, or the specific AutoAttack configuration. These parameters affect the strength of the attack and thus the measured robustness values.

- **The use of different accuracy metrics across attacks is unexplained.** Figure 3's caption states: "We report the top-5 accuracy for AutoAttack and the top-1 accuracy for PGD and GN." The paper does not justify why different metrics are used for different attacks. This makes within-dataset comparisons across attack types impossible and raises the question of whether the observed trends are robust to the choice of accuracy metric.

- **The relative performance metric's potential artifacts are not checked.** Using \(p_r = p^*/p\) normalizes for baseline accuracy, but can produce counterintuitive values: a low-accuracy model may appear more robust simply because it has little headroom to drop, while a high-accuracy model may show a larger relative drop even if its absolute accuracy under attack is higher. The paper does not check whether the observed correlations hold when using absolute accuracy under attack, or when controlling for clean accuracy. Effective dimensionality may itself correlate with clean accuracy, making this check important.

- **The adversarial training experiments test only ResNet-family architectures.** All three models (ResNet18, WRN28, WRN34) are ResNet variants. The clean linear trend (R² ≥ 0.73) may be architecture-specific. The paper notes this implicitly but should explicitly flag that the linearity of the dimensionality–robustness relationship under AT has not been verified for other architectural families (e.g., ShuffleNet, MobileNet).

### Trivial

- The paper uses both "it's" (line 56, 58) where "its" is intended — a minor grammatical issue.

## Nice-to-Haves

- A rough estimate of the computational cost of computing effective dimensionality (e.g., GPU-hours for a ResNet-50 on ImageNet) would help readers assess practical utility for model selection.
- Error bars or confidence intervals on the AT experiment data points (which likely have multiple runs from the MAIR framework) would strengthen the quantitative claims.
- Including a within-family analysis (e.g., "for ShuffleNet variants on ImageNet, does effective dimensionality predict robustness?") would help control for architectural confounds.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"No comparison to existing robustness metrics"** — This is partially retained in the Major weakness above (overclaiming effectiveness without comparison). What is removed: the specific suggestion to reference "Kim et al. 2023 correlations," since the paper already cites this work and the criticism is about missing experiments, not missing references.

2. **"The computational method for effective dimensionality is underspecified"** — Removed because the paper explicitly states it uses "a slightly modified version of the code provided by Maddox et al. (2020)" (Section 3), which is a standard and sufficient level of detail for an empirical study. Reproducibility is anchored in the public codebase.

3. **"No error bars or confidence intervals" for main experiment** — Removed because the main experiment uses deterministic pre-trained weights (single-run evaluation is standard for this setting). The AT experiment point is partially retained as a Nice-to-Have.

4. **"Reproducible use of established frameworks" (Strength Finder)** — Removed as generic; citing public code is standard practice and does not represent a distinct strength.

5. **"Controlled relative performance metric" as standalone strength** — Retained; it genuinely addresses a known confound. The potential artifacts are noted separately.

## Novel Insights

The harsh critic's most valuable observation is that the paper's abstract and conclusion overstate what the evidence supports — the main experiment lacks quantitative rigor (no R², no correlation coefficients) while the AT experiment that does have quantitative backing is limited to ResNet variants. This tension between the strength of the language and the strength of the evidence is the central issue. The strength finder correctly identifies that the AT results are the cleanest part of the paper and that the honest limitation reporting is a genuine asset. The most interesting synthesis: the paper would be substantially stronger if it applied the same quantitative discipline (regression, R² reporting) used in the AT section to the main cross-architecture experiment, and if it acknowledged the ResNet/ImageNet and VGG/CIFAR outliers as genuine bound cases for the theory rather than passing over them with an unsupported assertion.

## Suggestions

1. **Quantify the main correlation.** For each panel in Figure 3, report Spearman rank correlation and/or R² from a linear fit. If a "near-linear inverse relationship" is claimed, demonstrate it with numbers. A pooled regression across all models (with confidence bands) would make the headline claim testable.

2. **Add a direct comparison against at least one prior robustness metric** (e.g., log parameter count, boundary thickness proxy, or local Lipschitz estimate) on the same model set using the same regression framework. This either validates the claim of being "more effective" or correctly tempers it.

3. **Analyze the outliers explicitly.** Show, with separate markers or sub-panels, whether ResNet/ImageNet and VGG/CIFAR follow or contradict the general trend. If they follow it (as claimed), demonstrate this quantitatively; if they do not, acknowledge the limitation clearly.

4. **Validate the relative performance metric** by checking whether the main results replicate using absolute accuracy under attack and/or adding clean accuracy as a control variable.

5. **Report PGD parameters** (iterations, step size) and **justify the use of top-5 vs top-1 accuracy** across different attacks.

## Score and Decision

**Originality:** 6/10 — The idea of using effective dimensionality for robustness is not entirely novel (it builds on Maddox et al.), but the large-scale systematic empirical investigation across this many architectures and datasets is an original contribution.

**Importance of research question:** 8/10 — Finding reliable robustness metrics for model selection is an important open problem.

**Claims supported:** 5/10 — The headline "near-linear" claim is not quantitatively supported for the main experiment; the "more effective than prior measures" claim lacks direct comparison. The AT results are well-supported.

**Soundness of experiments:** 6/10 — Broad coverage of architectures and datasets is a strength. Missing attack parameters, unvalidated relative performance metric, and unanalyzed outliers weaken the soundness.

**Clarity of writing:** 7/10 — Generally well-written and structured. The honest limitations section is clear. Some overclaiming in abstract/conclusion.

**Value to the community:** 7/10 — The empirical findings are useful for practitioners and could inspire further research on complexity-based robustness measures. The AT results in particular provide concrete guidance.

Overall, the paper has a genuine empirical contribution — the relationship between effective dimensionality and robustness is real, and the AT experiments are the strongest evidence to date. However, the paper's rhetorical framing overreaches the evidence: the main experiment lacks the quantitative backing needed to support "near-linear inverse relationship," and the claim of superiority over prior measures is unsupported by comparison. These are fixable with additional analysis, but as presented the claims outpace the evidence.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>