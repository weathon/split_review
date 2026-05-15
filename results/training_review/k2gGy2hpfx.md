Here is my consolidated meta-review after thorough verification against the paper.

---

## Summary

This paper addresses conformal prediction (CP) under distribution shifts when test labels are unavailable. The authors propose ECP (Entropy scaled CP), which scales CP score functions by a quantile of the base model's prediction entropy on the test set, and EACP, which adds test-time adaptation (entropy minimization via the ETA algorithm) to refine the model and reduce set sizes. The key insight is that prediction entropy correlates with distribution shift severity, so scaling by it can mitigate CP's under-coverage. Experiments across ImageNet variants, WILDS, ImageNet-C, and continuous shift settings show that EACP₂ substantially closes the coverage gap on moderate shifts while producing smaller sets than supervised OCP methods.

## Strengths

- **Novel combination of uncertainty scaling and test-time adaptation for label-free CP under distribution shifts.** The paper identifies a meaningful gap — CP under arbitrary shifts without labels — and proposes a clean, intuitive solution. The idea of using an entropy quantile (defined on the test set as a whole, not per-instance) as a scaling factor for conformal scores is original, and coupling this with TTA to shrink sets adds practical value. The results in Table 1 (e.g., ImageNet-V2: SCP=0.81 → EACP₂=0.91; ImageNet-R: SCP=0.50 → EACP₂=0.80; iWildCam: SCP=0.84 → EACP₂=0.89) demonstrate the method's effectiveness on moderate shifts.

- **Unusually broad and thorough empirical evaluation.** The paper covers 6 stationary-shift datasets (including real-world WILDS benchmarks), 19 ImageNet-C corruption types × 5 severities, continuous shift streams (gradual and sudden), and multiple architectures (ResNet-50/101/152, ViT-B/16). The methodology and hyperparameters are fixed across all architectures (Fig. 4), which strengthens the claim of robustness. The color-coded tables and "hugging the target" plots effectively communicate the trend of coverage recovery.

- **Competitive label-free performance on continuous shifts with dramatically smaller set sizes.** In Table 3, EACP₂ achieves 0.88 average coverage (vs. 0.90 for supervised methods FACI/MAGL) on gradual shifts while producing sets 4–5× smaller (22.4 vs. 101–117). This is a genuinely interesting result — the method trades a small coverage gap for substantially more efficient prediction sets, all without requiring test labels.

- **Empirical validation of a simple default hyperparameter rule.** The paper commits to β = 1−α throughout all experiments and validates this choice in Figure 2 across multiple datasets and α values. While not theoretically derived, the rule is intuitive (use the same quantile for entropy as the target coverage) and avoids per-dataset tuning.

## Weaknesses

### Fatal
None.

### Major

1. **Abandonment of distribution-free coverage guarantees without a substitute theoretical justification.** The paper explicitly acknowledges "the loss of statistical guarantees" (Contributions paragraph) and that "it is impossible to guarantee Eq.(1) without restrictions on the shift" (Section 3). This is honest, but it means the method is a heuristic whose behavior is purely empirical. While this does not invalidate the paper's contribution — many useful methods are heuristics — it fundamentally changes what the paper offers: it is no longer a conformal prediction method in the formal sense but rather an uncertainty-aware heuristic for set prediction. The abstract and introduction should more prominently foreground this caveat rather than only the contributions list.

2. **The claim of "nearly match the performance of supervised algorithms" (abstract) is overstated given the evidence.** Table 3 shows EACP₂ achieves 0.88 average coverage vs. 0.90 for supervised methods — close on average coverage, but the local coverage error (LCE₁₂₈) is substantially worse (0.20 vs. 0.05–0.07 for gradual shifts). The set size comparison also involves a different regime: supervised methods optimize coverage ex post facto with label access, while EACP₂'s smaller sets partially reflect systematically lower (and more variable) local coverage. This is an apples-to-oranges comparison, and the "nearly match" framing should be qualified (e.g., "achieve comparable average coverage with smaller sets but worse worst-case local coverage").

### Minor

3. **Poor performance on the hardest shifts (ImageNet-A) is under-emphasized.** EACP₂ achieves only 0.30 coverage on ImageNet-A — a 70% shortfall from the 0.90 target, despite going from SCP's 0.03 (a 10× relative improvement). While the paper acknowledges "all but the most challenging datasets," the scale of this failure (and the fact that it represents a realistic adversarial distribution shift) should temper the conclusions throughout the abstract and introduction. The paper's claim of generality is weakened by this result.

4. **The β = 1−α rule, while simple and validated, would benefit from a held-out validation analysis.** The paper presents Figure 2 as a justification that β = 1−α works well, but the datasets plotted overlap with those used in the main evaluation. Although the paper states it "perform[s] all the experiments with this direct relationship" (suggesting the rule was chosen a priori), a cleaner approach would be to hold out one corruption type for selecting β and evaluate on the rest. As presented, readers cannot fully rule out that the figure influenced the choice.

5. **The interaction between TTA (entropy minimization) and entropy-based scaling is not analyzed, and confirmation bias is not discussed.** Minimizing entropy on unlabeled test data can increase confidence on incorrect predictions under distribution shift — a well-known phenomenon in the TTA literature. The paper does not examine whether EACP's improved coverage stems from genuinely better-calibrated scores or from overconfident but wrong predictions that happen to pass the scaled threshold. Diagnostic experiments decomposing coverage improvement into accuracy improvement (from TTA) vs. scaling effect would clarify the mechanism.

6. **Only linear/quadratic scaling is used in experiments, but Figure 3 suggests higher-order scaling may be needed on severe shifts.** The paper notes this ("a higher-order polynomial is required on more difficult shifts, such as ImageNet-R") but does not experiment with cubic or higher scaling. This is a plausible cause of the poor ImageNet-A results and should be stated as a clear limitation in the method section, not just in the figure caption.

### Trivial

7. **The ETA subroutine is described too briefly for standalone reproducibility.** The paper says "one could simply call ETA as a subroutine" and gives a one-sentence summary of its filtering/reweighting scheme. While citing the original paper is acceptable, a slightly more detailed description (or pseudocode in an appendix) would improve reproducibility.

## Nice-to-Haves

- A decomposition of coverage improvement into (a) accuracy gain from TTA vs. (b) pure scaling effect, to clarify whether TTA helps for the right reasons.
- Example prediction sets from SCP, ECP, and EACP on a few test images to illustrate the mechanism qualitatively.
- A per-class or per-difficulty breakdown on RXRX1 to explain why SCP produces moderate sets (81.8) while EACP₂ produces much larger sets (177) despite being closer to target coverage.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that "RXRX1 (177) are more than ⅓ of the label space (which is 1,029 classes)."** Factually wrong: 177/1029 ≈ 17%, not "more than ⅓." Removed as a factual error.
- **Criticism that Figure 1 is "a single scatter plot without error bars or per‑severity breakdown."** The paper explicitly states "Darker shades represent greater severity levels of ImageNet-C corruptions," so per-severity information is present. Removed as a misreading.
- **Generic claim that the method "could equally well be achieved by a naive threshold adjustment."** This is conjectural and unsupported — the paper shows that naive baselines (NAIVE, SCP, ETA alone) all fail to recover coverage, so there is no evidence a simple threshold adjustment would match EACP's performance.
- **Demand for "confidence intervals" on benchmark results and "theoretical proofs."** These are non-standard expectations for an empirical systems paper in this field; moved here.
- **Demand for "user studies."** Out of scope for a purely algorithmic contribution.

## Novel Insights

None beyond the paper's own contributions. The reviews surface useful diagnostic questions (confirmation bias risk, decomposition of TTA vs. scaling effects, need for held-out β validation) but do not generate synthetic insights beyond what the paper already provides.

## Suggestions

1. **Tone down the "nearly match" claim** to something like "achieve competitive average coverage with substantially smaller prediction sets, though with higher local coverage volatility." This would be more precise and defensible.

2. **Add diagnostic experiments decomposing the TTA contribution:** report test accuracy alongside coverage for SCP, ECP, and EACP on a subset of datasets, and compute whether the coverage improvement from TTA exceeds what would be expected from accuracy improvement alone. This would help address the confirmation bias concern.

3. **Acknowledge the ImageNet-A failure more prominently** in the abstract and conclusion, and discuss the regime of shifts where the method is expected to work vs. fail (e.g., "severe out-of-distribution shifts where the entropy quantile saturates").

4. **Consider a held-out validation experiment for β** where one corruption type is used to select the rule and performance is reported on the remaining types. This would strengthen the claim that β=1−α generalizes.

5. **Explicitly note in Section 4.3** that linear/quadratic scaling is a pragmatic choice validated on moderate shifts, and that higher-order scaling may be needed for severe shifts (linking to Figure 3).

## Score and Decision

This paper tackles a timely and important problem with a clean, intuitive idea and an unusually thorough experimental evaluation. The main weaknesses — lack of formal guarantees, overclaimed comparison with supervised methods, poor performance on hardest shifts, and undiagnosed TTA interaction — are real but do not invalidate the core empirical contribution. The method demonstrably improves coverage on moderate distribution shifts without labels, often recovering the target 0.90 rate, and achieves competitive results on continuous shifts with much smaller set sizes than supervised alternatives. These results represent a useful step forward for label-free CP under distribution shifts.

The paper would benefit from toning down its stronger claims, adding diagnostic experiments on the TTA mechanism, and more prominently acknowledging failure cases. These are addressable in revision.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>