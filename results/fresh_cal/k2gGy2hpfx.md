Now I have all the information I need. Let me produce the final consolidated review.

## Final Review

## Summary
This paper addresses the practical problem of adapting conformal prediction (CP) to distribution shifts when test-time labels are unavailable. It proposes ECP, which scales CP score functions by an entropy quantile computed from unlabeled test data, and EACP, which additionally updates the base model via test-time adaptation (ETA). The methods are evaluated across diverse datasets (ImageNet variants, WILDS benchmark), architectures (ResNet, DenseNet, ViT), and shift types (stationary, continuous), showing consistent coverage improvement over standard CP baselines.

## Strengths
- **EACP_2 recovers near-target coverage on most ImageNet-C corruption types and severities**: Table 2 shows EACP_2 achieves coverage of 0.90 or higher on 18 out of 20 displayed (corruption, severity) pairs (e.g., Contrast severity 4: 0.92, Gaussian Noise severity 4: 0.90, Motion Blur severity 4: 0.91), whereas standard SCP drops as low as 0.09 on Contrast severity 5. This directly supports the core claim of improving CP quality under distribution shifts without test labels.
- **EACP_2 nearly matches supervised online CP methods on continuous shifts with far smaller set sizes**: Table 3 (gradual shift) shows EACP_2 achieves average coverage 0.88 vs. supervised FACI (0.90) and MAGL (0.90), yet EACP_2 has average set size 22.4—an order of magnitude smaller than FACI (101) and MAGL (117). This demonstrates competitive performance with label-requiring methods.
- **Methods generalize across multiple architectures without hyperparameter tuning**: Figure 4 shows consistent coverage improvement over SCP and ETA across all 19 ImageNet-C corruptions using the same methodology for ResNet-50, DenseNet-121, and vision transformers, demonstrating robustness to model choice.
- **Evaluation include local metrics (LCE, LSS) beyond averages**: Table 3 reports worst local coverage error and set size over sliding windows of 128 points, providing fine-grained assessment that standard average metrics miss. EACP_2 reduces local coverage error compared to unsupervised baselines (gradual shift LCE_128: 0.20 vs. ETA 0.52).
- **Novel synthesis of TTA and CP**: The paper identifies and bridges the gap between test-time adaptation and conformal prediction—two previously disconnected lines of work—demonstrating that TTA's uncertainty estimates can inform CP's set construction under distribution shift.

## Weaknesses

### Fatal
None.

### Major
- **The β = 1−α quantile choice is a heuristic whose reliability on unseen shift types is unestablished.** The paper sets the entropy quantile level β equal to the target coverage rate 1−α, justified only empirically via Figure 2 on the evaluated datasets. The paper itself acknowledges this works "for all but the most severe distribution shifts" (line 99), and indeed on ImageNet-R and ImageNet-A, coverage remains far below target (EACP_2: 0.80 and 0.30 respectively, Table 1). There is no principled guidance for how to set β on a novel shift type, or how to diagnose when the heuristic is failing. Since the method sacrifices formal coverage guarantees, the robustness of this choice to unseen shift types is a first-order concern. While the empirical evidence across the tested datasets is substantial, the lack of any theoretical anchor or diagnostic for failure limits the method's deployability in practice.

### Minor
- **All results are point estimates without uncertainty quantification.** Coverage and set size metrics are reported without confidence intervals, standard deviations, or significance tests. For a method that sacrifices formal CP guarantees, rigorous empirical validation is important—especially for near-target coverage claims (e.g., 0.91 vs 0.90 on ImageNet-V2, Table 1) where differences may be within noise. This is standard practice in large-scale CP benchmarks, but the paper would be strengthened by reporting variability (e.g., over multiple calibration splits or model seeds).
- **The transductive nature of the method is not discussed as a limitation.** ECP computes the entropy quantile \(u_{D_\text{test}}\) from the entire test set and applies it to the same test points. This is clearly described but not flagged as a transductive procedure that cannot be applied point-by-point in a streaming setting (unlike standard split CP). Behavior on small test sets (where the quantile estimate would be noisy) is not analyzed.
- **Number of classes is not reported for any dataset**, making set sizes difficult to interpret relative to the label space. For example, EACP_2 achieves average set size 177 on RXRX1 (Table 1); without knowing the number of classes, a reader cannot assess whether this is practically useful or nearly vacuous.
- **Hyperparameter details for the ETA subroutine are not reported** (learning rate, batch size, momentum, etc.), which hinders reproducibility and makes it impossible to assess whether the results are sensitive to these choices. Computational cost (runtime of EACP vs. simpler baselines) is also not discussed.

### Trivial
- The paper does not explicitly state whether the entropy quantile is recomputed per-batch or per-dataset after each ETA model update in EACP, leaving a minor ambiguity in the procedure description.

## Nice-to-Haves
- **Additional label-free baselines** would strengthen the empirical comparison: e.g., temperature scaling on test-set softmax outputs, or a direct reweighting approach (using entropy to weight calibration samples as in covariate-shift CP). The current baseline set (SCP, NAIVE, ETA) is adequate but not exhaustive.
- Reporting **dataset class counts** would make set-size values interpretable at a glance.
- A brief **limitations paragraph** in the conclusion—explicitly discussing the heuristic quantile choice, transductive nature, and known failure modes (severe shifts)—would improve the paper's scholarly integrity.

## Removed Points
Points that were considered but removed after cross-checking against the paper:

- **"Incomplete baseline comparisons" / "NAIVE baseline poorly motivated"**: The paper clearly describes the NAIVE baseline (line 160-161: "forming prediction sets by including classes until their cumulative probability... without any prior calibration"). The existing baseline set (SCP, NAIVE, ETA, supervised OCP methods) is substantial. The suggested additional baselines (temperature scaling, reweighting) are reasonable extensions but not omissions severe enough to be a weakness. Moved to Nice-to-Have.
- **"Figure 3 analysis is post-hoc"**: The paper explicitly acknowledges this at line 148 ("we empirically evaluate the ideal choice in a post-hoc manner"), so this criticism adds no new information.
- **"Missing related work (Garg et al., 2022)"**: Per rule, missing related works are not to be mentioned as they cannot be independently verified.
- **"Optimistic bias from transductive nature"**: The critic's claim that the transductive factor is "tailored to the particular entropy distribution of that test set" is speculative; the scaling factor is a single global quantile applied uniformly, not per-point optimized.
- **"Formatting/style nitpicks"** and **"reproducibility nitpicks about trivial implementation details"**: Removed per filtering rules.
- **Strength Finder claims about "the hyperparameter β is fixed to 1−α and shown to work consistently" vs. the weakness about β**: Both perspectives are valid and represent the same fact viewed differently. The weakness is retained as Major (since it identifies a genuine limitation), and the strength is retained because the empirical evidence across datasets is indeed a strength.

## Novel Insights
None beyond the paper's own contributions. The two reviews largely converge on the paper's strengths (strong empirical evaluation, novel TTA+CP synthesis) and weaknesses (heuristic quantile choice, lack of statistical uncertainty). No reviewer raised a genuinely novel observation that the paper itself does not contain.

## Suggestions
1. **Provide a robustness analysis for the β choice**: Either show theoretically motivated bounds, or present a sensitivity analysis across a wider range of synthetic shifts with known properties to characterize when β ≈ 1−α works and when it fails. A practical diagnostic (e.g., "if the entropy quantile exceeds X, the heuristic may fail") would greatly improve deployability.
2. **Add confidence intervals or standard deviations** to the main tables (at least Table 1 and Table 2), reporting variability over calibration splits or model seeds, to substantiate near-target coverage claims.
3. **Explicitly acknowledge the method's limitations** in a dedicated paragraph: transductive nature, heuristic quantile choice, known failure cases (severe shifts like ImageNet-A), and reliance on entropy–shift correlation.
4. **Report class counts** for all datasets and add a brief discussion of set-size interpretability relative to the label space.
5. **Provide ETA hyperparameters** (learning rate, batch size, etc.) either in the main text or appendix, and optionally report the relative runtime of EACP vs. simpler methods to inform practitioners.

## Score and Decision

The paper tackles an important and practical problem—adapting CP to distribution shifts without test labels—with a novel, intuitively motivated solution. The experimental evaluation is thorough across diverse datasets, architectures, and shift types, and the results convincingly show that EACP_2 recovers near-target coverage where standard CP fails badly. The novel synthesis of test-time adaptation with conformal prediction is a genuine contribution. The main limitation is the heuristic choice of β = 1−α, which lacks theoretical grounding and fails on the most severe shifts, but the paper provides substantial empirical support across the tested datasets. The absence of statistical uncertainty quantification and explicit limitations discussion are addressable weaknesses.

**Overall**: A solid empirical contribution to an important problem, with clear evidence of effectiveness across a broad range of settings, tempered by a heuristic core design choice and some presentation gaps. Recommend acceptance with revisions.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>