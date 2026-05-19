Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper provides a formal theoretical and empirical analysis of open-set noise in learning with noisy labels (LNL). It introduces a complete noise transition matrix that accounts for multiple outlier classes, defines two pragmatic learning regimes (fitted and overfitted), and proves that open-set noise causes less classification error inflation than closed-set noise under a class-concentrated assumption. The paper also constructs CIFAR100-O and ImageNet-O datasets, examines entropy-based open-set noise detection, and proposes OOD detection as a complementary evaluation framework for LNL methods.

## Strengths

- **Formal definition of the complete noise transition matrix (Definition 3.1).** Unlike prior work (Xia et al. 2022) that collapses all open-set noise into a single meta-class, this paper models open-set noise as originating from multiple outlier classes via a structured matrix with a zero-block for unknown outlier labels. This provides a principled foundation for comparing open-set and closed-set noise.

- **Theorem 3.7 and its empirical validation.** The theorem proves that, under the class-concentrated assumption, open-set noise yields strictly less classification error inflation than closed-set noise at the same total noise ratio. Figure 2(a/b) validates this across CIFAR100-O and ImageNet-O at multiple noise ratios in both the fitted and overfitted regimes — clean, controlled experiments that match the theory.

- **Distinction between "easy" and "hard" open-set noise.** The paper introduces a categorization based on ID/OOD separability that explains why some open-set noise is detectable via entropy while other types are not. This adds useful nuance beyond prior binary treatments.

- **Construction of CIFAR100-O and ImageNet-O datasets.** These provide controlled benchmarks for studying open-set noise modes, filling a gap in available LNL evaluation resources.

- **Novel empirical finding about OOD detection.** Figure 2(c/d) demonstrates contrasting trends: open-set noise degrades OOD detection performance while closed-set noise can improve it. This is a nontrivial insight that suggests OOD detection as a more sensitive evaluation axis for LNL methods than classification accuracy alone.

## Weaknesses

### Fatal
None. The core theoretical and empirical contributions are substantiated and no verified error invalidates the paper's central claims.

### Major

- **OOD detection metric is not specified.** The paper reports "OOD detection performance" in Figure 2(c/d) and cites Hendrycks & Gimpel (2016), but never states which metric is plotted (AUROC? AUPR? FPR@95TPR?). This is a reproducibility gap that must be closed. The finding itself is interesting, but without a specified metric the reader cannot interpret the curves or compare against future work.

- **Entropy-based detection experiments are purely qualitative.** Section 4.2 presents only histograms of prediction entropy (Figure 3) and relies on visual inspection to conclude that entropy dynamics are more effective for easy than hard open-set noise. No quantitative detection metrics are reported (e.g., AUROC for distinguishing open-set noise from clean samples). Since the paper explicitly analyzes entropy-based detection in Section 3.4, the experiments should provide quantitative validation of the theoretical prediction.

### Minor

- **Clarity issue in the overfitted case formula (Remark 3.6).** The definition states that the model "completely memorises the noisy labels" (outputting a one-hot at the realized noisy label yⁿ), but the formula ΔE_x = max[p₁,...,p_A] − Σᵢ₌₁^A (p_i · Σⱼ p_j T_{ji}) computes the *expected* error rate inflation marginalized over the noise process (i.e., max_k p_k − E_{yⁿ}[p_{yⁿ}]), not the inflation for a specific yⁿ realization. This is not mathematically wrong — the expected quantity is valid and meaningful for population-level analysis — but the paper does not articulate this distinction. The definition and the formula appear mismatched as written, which risks confusion and needs explicit clarification.

- **No experimental results on the WebVision open-set test set.** The paper constructs an open-set test set for WebVision (mentioned in the abstract and Figure 1), but presents no experimental results on it. Including even a single experiment validating that the theoretical trends (open-set noise causing less accuracy degradation) hold on real web-crawled data would substantially strengthen the empirical contribution.

- **No error bars or statistical significance.** All experiments appear to be single-run. Given that noise is injected probabilistically and multiple random seeds would affect both the noise composition and the training outcomes, error bars (or at minimum results averaged over 3+ seeds) are expected for a study paper claiming empirical validation of theoretical trends.

### Trivial

- In Section 3.3 lines 139–144, the paper writes "toainnsguae caotsniscte ntairoc vmealpnsioeson rwaeot. aFlysylrtez,e" — garbled text from the extracted figure/equation area (parsing artifact). The original submission presumably has clean text.

## Nice-to-Haves

- A simulation or ablation that relaxes the class-concentrated assumption would help establish the generality of Theorem 3.7 beyond the limiting case.
- The fitted case experiments use a "Pretrained-ResNet18" but do not specify which pretrained weights (ImageNet? Places?). This can affect what counts as an outlier class and should be stated.

## Removed Points

These points were flagged by the reviewers but are removed for the reasons stated:

1. **"The overfitted case formula is invalid / Theorem 3.7 is suspect."** — The critic claimed the formula was inconsistent with the definition. As analyzed above, the formula computes the *expected* error rate inflation over the noise process, which is a mathematically valid quantity and does not invalidate the theorem. The issue is one of clarity, not correctness. Demoted from "fatal" to "minor" and retained above.

2. **"Section 3.4 theoretical analysis is missing from the main text."** — The parser strips appendix/supplementary content. The original submission contains this section. Removed per hard rule.

3. **"Proof of Theorem 3.7 is not in the main text."** — Same reason: the proof is in the appendix (stripped by parser). Removed per hard rule.

4. **"Cannot independently verify the theorem because the proof is missing."** — Speculative gap based on a missing appendix. Removed per hard rule.

5. **"Missing related works."** — I cannot verify this from external sources. Removed per hard rule.

6. **Strength Finder point: "This paper provides a comprehensive theoretical and empirical analysis..."** — Generic praise, not a specific strength. Removed.

7. **Strength Finder point: "The most important evidence supporting this contribution is the tight coupling between Theorem 3.7 and the controlled experiments..."** — Redundant with listed strengths. Removed.

## Novel Insights

The most interesting observation that goes beyond the paper's own framing is the asymmetry between how open-set and closed-set noise affect classification accuracy versus OOD detection: open-set noise has a weaker negative effect on accuracy but a stronger negative effect on OOD detection, while closed-set noise is the opposite. This suggests that the standard LNL evaluation protocol (classification accuracy on inlier classes) systematically under-reports the harm of open-set noise, which is a genuine insight for the community. The entropy analysis also reveals a practical limitation: entropy-based detection, widely used in LNL sample selection, fails for hard open-set noise — a finding that could inform the design of better noise detection mechanisms.

## Suggestions

1. **Specify the OOD detection metric used in Figure 2(c/d)** and ideally report multiple metrics (AUROC, AUPR, FPR@95TPR) for completeness.
2. **Add quantitative detection metrics (e.g., AUROC) to the entropy dynamics experiments** in Section 4.2, such as a plot of detection AUROC vs. warm-up epochs for easy and hard open-set noise.
3. **Clarify Remark 3.6** by stating explicitly that the overfitted case formula computes the *expected* error rate inflation over the noise process, and briefly explain the relationship between this expectation and the definition of the overfitted case.
4. **Include error bars** (at least 3 random seeds) for key experiments.
5. **Add at least one experiment on the WebVision open-set test set** to validate that the theoretical trends hold on real-world noisy data.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>