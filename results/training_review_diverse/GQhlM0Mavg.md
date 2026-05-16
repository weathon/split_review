Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This position paper argues that Out-of-Distribution (OOD) detection and Conformal Prediction (CP) are naturally linked and can benefit from cross-fertilization. The two main contributions are: (1) adapting CP-based FPR corrections from Bates et al. (2022) to define "conformal AUROC" and "conformal FPR@TPRβ" metrics that provide conservative FPR estimates with user-specified confidence, demonstrated on OpenOOD and ADBench; (2) exploring whether OOD scores (ReAct, Gram, KNN, Mahalanobis, ODIN) can serve as nonconformity scores for CP prediction sets.

## Strengths

- **Formalizes the under-explored link between OOD evaluation metrics and CP via p-values and the Beta-distributed FPR**: The paper connects OOD metrics (AUROC, FPR@TPRβ) to hypothesis testing, then shows the empirical FPR follows a Beta distribution conditioned on the calibration set (Equation 8, Section 4.3). This grounding enables the principled application of CP corrections to OOD evaluation — a genuine conceptual contribution beyond prior work that treated OOD and CP separately.

- **Proposes conformal AUROC and conformal FPR@TPRβ and evaluates the correction on two major OOD benchmarks**: The paper adapts corrections from Bates et al. (2022) to define these new metrics and demonstrates their effect on OpenOOD (Table 1) and ADBench (Figure 3). The results show the correction is large enough to matter (often >1% AUROC drop) but not so large as to invalidate top baselines, supporting the practical value of the approach for safety-critical applications.

- **Provides a compelling empirical illustration of FPR variability using SVHN**: By splitting 530k+ SVHN extra images into 53 disjoint calibration sets, the paper shows the histogram of empirical FPR values closely matches the theoretical Beta distribution (Figure 1, Section 4.3.1), making concrete why finite-sample evaluation can be over-optimistic.

- **Usefully distinguishes conformal metrics from standard CP procedures (Remark 4.1)**: The paper correctly notes that conformal FPR correction does not require an additional calibration split — the correction applies directly to the estimated FPR from the existing validation set, which is a practical advantage worth highlighting.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Section 5 (OOD scores as nonconformity scores) is exploratory with mixed results, but the conclusion overstates the findings**: The paper's own text in Section 5 states that "all OOD scores are inefficient for CP" and most underperform standard softmax-based scores. Mahalanobis and KNN show only marginal improvements (e.g., Mahalanobis LAC efficiency 5.91 vs. softmax LAC 6.42 on CIFAR-10). Yet the Conclusion claims "we could use OOD to improve existing CP techniques by using OOD scores as nonconformity scores" and "some of them, especially Mahalanobis and KNN, are good candidates." The evidence supports a more cautious interpretation: the exploration is preliminary, most OOD scores do not help, and a few deserve future investigation. The transformation from OOD scores to class-dependent scores via a softmax-like normalization is also presented without justification or comparison to using raw scores directly. This section would be more honest and still valuable if framed as a preliminary negative result with promising exceptions.

- **Experimental reporting has gaps that hinder reproducibility and interpretation**: (a) Different δ values are used for OpenOOD (δ=0.01) and ADBench (δ=0.05) without any justification or discussion of the trade-off. (b) Validation set sizes (n_val) are not reported per benchmark/dataset, making it impossible to assess whether the correction is appropriate. (c) Variance or confidence intervals are not reported for the OpenOOD and ADBench results (though standard deviations are reported for the CP results in Section 5). These details matter because the correction's magnitude depends directly on n_val and δ.

- **The conformal FPR@TPRβ metric is defined but never evaluated**: Sections 4.4 and 4.5 motivate both conformal AUROC and conformal FPR@TPRβ, and the paper notes that FPR@TPR95 is a standard OOD metric. Yet the experiments only report conformal AUROC results. Reporting at least one conformal FPR@TPRβ result would strengthen the empirical illustration.

- **No discussion of how to choose δ or the conservativeness-informativeness trade-off**: The paper presents δ as a user-defined parameter but provides no guidance on its selection (0.01 vs. 0.05 can produce meaningfully different corrections). A practitioner reading this would not know how to set δ in their own application, which limits the paper's practical utility.

### Trivial

- **Abstract phrasing slightly ambiguous about what is guaranteed**: The abstract says conformal metrics "provide probabilistic conservativeness guarantees on the variability of these metrics." Section 4.4 correctly clarifies that the guarantee applies to the FPR component (each FPR threshold is conservative with prob. 1−δ) and that the AUROC "use[s] conservative estimates of the FPR" — not that the AUROC itself has a high-probability guarantee. The abstract could be more precise.

- **The paper would benefit from reporting the specific OOD datasets used within OpenOOD's Near/Far grouping**, rather than just referencing the benchmark guidelines.

## Nice-to-Haves

- Compare the conformal correction with alternative approaches to handling finite-sample variability (e.g., bootstrap confidence intervals) to help position the contribution.
- Include per-dataset results (at least in an appendix) for ADBench rather than only aggregated scatter plots.
- Add a brief justification for why the Monte Carlo correction was chosen over Simes/DKWM/Asymptotic for the main experiments.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The Introduction seems truncated"**: This is a parser artifact — the original submission contains the full text.
- **"The formulas are garbled in the parsed text"**: Parser artifact; not an author error.
- **"No code release or reproducibility checklist mentioned"**: The hard rules require removing nitpicks about reproducibility that are not central methodological gaps. Code release is a wishlist item, not a flaw in the paper's reasoning.
- **"No comparison with bootstrap confidence intervals"**: Scope creep for a position paper; the paper is not proposing a replacement for all finite-sample methods but showing a specific CP-based approach.
- **"No discussion of what to do with TPR variability"**: Since the correction only targets the FPR side, this is an acknowledged asymmetry and could be noted as future work; it is not a flaw in what the paper does claim.

## Novel Insights

None beyond the paper's own contributions. The main insight — that the empirical FPR in OOD evaluation is a Beta-distributed random variable whose variability can be corrected using CP theory — is the paper's own contribution, not something synthesized from the reviews.

## Suggestions

1. **Reframe Section 5 explicitly** as a preliminary exploration / negative result: "We investigated whether OOD scores can replace traditional CP nonconformity scores. Most perform worse, but Mahalanobis and KNN show marginal improvements and merit further study." This aligns with the evidence and is still a useful finding.
2. **Justify the choice of δ** (or at minimum, state that it is application-dependent and show results for both values on at least one benchmark).
3. **Report n_val for each benchmark** used (and ideally per dataset for ADBench) so readers can gauge correction magnitude.
4. **Add at least one conformal FPR@TPRβ result** to match the paper's stated scope.
5. **Tighten the abstract language** about what the guarantee applies to.

## Score and Decision

The paper's core contribution — formalizing the connection between OOD evaluation and CP corrections, and demonstrating it on major benchmarks — is solid, well-motivated, and practically relevant. The weaknesses are all minor: Section 5 overstates its findings slightly, experimental reporting could be more thorough, and a few details would improve reproducibility. These are addressable in revision and do not undermine the paper's main thesis. The paper succeeds as a position paper with empirical illustrations: it advances a useful perspective, provides working definitions, and backs them with sufficient evidence.

Score: 7.0/10 — Accept.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>