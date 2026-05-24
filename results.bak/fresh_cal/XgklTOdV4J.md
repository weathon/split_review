Now I have a thorough understanding of the paper and all the reviewer claims. Let me craft the final consolidated review.

---

## Summary

DualAug proposes a dual-branch data augmentation framework that applies heavy augmentation alongside a standard (basic) augmentation branch, then uses an online OOD detector (MSP-based threshold via the 3σ rule on basic-branch scores) to filter out-of-distribution heavy-augmented samples, replacing them with their basic-augmented counterparts. The method wraps around existing automated augmentation policies (AA, RA, DeepAA) and is evaluated on supervised, semi-supervised (FixMatch), and self-supervised (SimSiam) settings.

## Strengths

1. **Direct empirical validation of the motivating insight (Figure 1):** The paper shows quantitatively that heavy RandAugment alone degrades CIFAR-100 accuracy (red line descending), but after filtering OOD data the same heavy augmentation recovers and even exceeds the best moderate-augmentation accuracy (green line). This directly supports the paper's central claim that OOD rejection enables exploitation of heavy augmentation.

2. **Consistent improvement across multiple automated augmentation methods and datasets:** Tables 1 and 2 show that DualAug improves AA, RA, and DeepAA on CIFAR-10, CIFAR-100, SVHN, and ImageNet — every single comparison (19/19 in Tables 1 and 2) shows a gain. The consistency across methods and scales is strong collective evidence that the framework generalizes beyond any single policy.

3. **Demonstrated effectiveness beyond supervised classification:** Section 4.2 (FixMatch, Table 4) and Section 4.3 (SimSiam, Table 5) show that DualAug also improves semi-supervised and self-supervised learning (e.g., FixMatch +0.33pp with 4k labels on CIFAR-10; SimSiam +0.44pp on ImageNet linear eval). This breadth is uncommon among augmentation methods.

4. **Component ablation cleanly confirms the design (Table 6):** The ablation on WRN-28-2/CIFAR-100 shows that heavy augmentation alone collapses accuracy (78.34→73.32), adding the OOD detector without the basic branch nearly recovers baseline (78.40), mixing without OOD detection hurts (77.43), and the full DualAug achieves the best (78.89). This provides clear causal evidence for each component.

5. **Efficient OOD detection without a separate model (Table 7):** The online detector (training model itself) outperforms a pre-trained offline detector (83.42 vs. 83.34) while saving memory and computation, explicitly contrasted with TeachAugment's extra teacher model.

6. **Practical analysis of heavy augmentation variants (Table 8):** Comparing more transformation types, larger magnitudes, and more transformations shows that increasing the *number* of transformations is most effective (83.60 vs. 82.10 for more types), giving actionable guidance.

## Weaknesses

### Major

1. **Many individual improvements are modest and fall within plausible noise range of the baselines.** While every comparison trends positive, several improvements are smaller than the baseline standard deviation (e.g., CIFAR-10 WRN-40-2 + DeepAA: +0.03pp vs SD 0.07; CIFAR-100 WRN-40-2 + DeepAA: +0.06pp vs SD 0.07; CIFAR-100 WRN-40-2 + AA: +0.20pp vs SD 0.26). The ImageNet results (Table 2) report no error bars at all. With only three runs, the statistical evidence for the smallest gains is weak. The paper would be strengthened by reporting confidence intervals or significance tests, or running more seeds. **Why it matters:** The paper's central claim is that DualAug *improves* existing methods; if the smallest gains are statistical noise, the headline claim is overbroad.

2. **Only one method is tested in the semi-supervised and self-supervised settings each.** FixMatch (semi-supervised) and SimSiam (self-supervised) are single data points. The paper cites UDA, SoftMatch, MoCo, and SimCLR in the text but does not test any of them. **Why it matters:** The claim of generalization "to other task settings" would be stronger with at least one additional method per setting.

### Minor

3. **The Gaussian assumption for MSP scores is stated but not validated.** The paper says "we simply assume all elements of S_basic form a Gaussian distribution" to justify the 3σ threshold. MSP scores are bounded [0,1] and typically non-Gaussian (often bimodal). The paper provides empirical score distributions (Figure 4) but no normality test (Q-Q plot, KS test, etc.) or sensitivity analysis comparing the 3σ rule to a nonparametric alternative (e.g., percentile-based threshold). The ablation shows the mechanism works, but the thresholding strategy's theoretical justification is unsubstantiated.

4. **No computational overhead measurement.** The abstract claims "reasonable time and computational cost" but no training time, FLOPs, or throughput numbers are reported. Since DualAug forward-passes every sample through the model for both basic and heavy branches, the overhead is potentially substantial. Practitioners adopting DualAug have no basis to judge the cost.

5. **No analysis of what gets filtered.** The paper does not report how many heavy-augmented samples are classified as OOD, how this fraction changes over training, or show examples of filtered (OOD) vs. kept samples. Understanding what the detector discards would build intuition and reveal potential failure modes (e.g., discarding hard but valid views).

6. **Threshold computation details are underspecified.** The text defines S_basic as "the set which collects all scores," but does not state whether μ and σ are computed batch-wise, via running averages, or over the full dataset. The Figure 4 caption says τ is "averaged by iterations in one epoch," implying per-iteration computation, but this is not in the main text. This affects reproducibility.

7. **Heavy augmentation implementation analysis (Table 8) is only tested with RandAugment as the base.** Whether the finding that "increasing the number of transformations is best" holds for AA, DeepAA, or other policies is not explored.

### Trivial

- None that warrant listing; the paper is clearly written and formatted.

## Nice-to-Haves

- Test at least one additional semi-supervised method (e.g., UDA or SoftMatch) and one additional self-supervised method (e.g., SimCLR or MoCo) to strengthen the generalization claim.
- Validate the Gaussian assumption with a simple Q-Q plot or compare the 3σ rule against a percentile-based threshold in an ablation.
- Report training time or relative throughput to ground the "reasonable cost" claim.
- Visualize a few examples of heavy-augmented samples that were kept vs. filtered to build intuition.
- The warm-up length (20% of epochs) is reasonable but was tuned only on CIFAR-100; a brief analysis of its sensitivity on another dataset would increase confidence.

## Removed Points

- **"Improvements are frequently within noise" (overstated framing):** The critic claimed "many" improvements are within baseline SD. In fact, only 3 of 16 supervised comparisons fall into this category; the remaining 13 exceed baseline SD, often by a wide margin (e.g., CIFAR-100 WRN-40-2 + RA: +0.44pp vs SD 0.12; SVHN WRN-40-2 + AA: +0.29pp vs SD 0.07). Moreover, the *consistent direction* of all 19+ comparisons is itself strong evidence. The underlying concern about statistical significance is real (kept as Major #1), but the "frequently within noise" framing is misleadingly severe. — *Reason: factually overstated.*

- **"Missing comparison with KeepAugment / curriculum-strength approaches":** KeepAugment is already cited in the related work. The paper's contribution is a general wrapper for automated augmentation methods, not a competitor to salience-preserving augmentation. — *Reason: scope creep; the paper cites it but focuses on a different technical approach.*

- **"Should compare with MixUp/label smoothing as simple baselines":** The paper's mechanism (OOD filtering for heavy augmentation) is conceptually distinct from MixUp/label smoothing. This is not a standard comparison for this problem. — *Reason: not a standard or necessary baseline for this specific contribution.*

- **"The improvement for 250 labels semi-supervised (95.04→95.23) is likely not significant":** While the absolute gain is modest, the SD is large for both (0.68 vs 0.45) and the 4000-label result (95.77→96.10, ±0.06 vs ±0.05) shows a cleaner gain. This single point is not a core weakness beyond what is already captured by Major #1. — *Reason: subsumed by Major #1.*

- **Various formatting/style/strawman points** from the section-by-section notes that were not verified as substantive weaknesses.

## Novel Insights

None beyond the paper's own contributions. The reviews surface mostly predictable methodological concerns (statistical significance, assumption validation) and do not identify a new angle on the work that the authors themselves missed.

## Suggestions

1. **Run more seeds (≥5) on the smallest-gain settings** (CIFAR-10 WRN-40-2 + DeepAA, CIFAR-100 WRN-40-2 + DeepAA) and report whether improvements hold. Include error bars on ImageNet results.
2. **Add a brief validation of the Gaussian assumption:** a kernel density estimate of S_basic superimposed with a fitted Gaussian, or a comparison to a percentile-based threshold (e.g., keep top 95%).
3. **Measure and report training time overhead** relative to the baseline augmentation alone, for at least one setting.
4. **Add a figure or table** showing the fraction of heavy-augmented samples flagged as OOD during training, with a few example images of kept vs. filtered samples.

## Score and Decision

The paper presents a clean, well-motivated idea with consistent (if modest) experimental support across multiple tasks. The ablations convincingly validate the design. The primary weaknesses — modest effect sizes in some comparisons, thin generalization evidence outside supervised learning, and unvalidated Gaussian assumption — are real but addressable and do not undermine the core contribution. The paper is above the acceptance threshold.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>