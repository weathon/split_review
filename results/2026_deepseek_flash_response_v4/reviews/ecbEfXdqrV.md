I have all the calibration needed. Let me now write the final review.

## Summary

This paper investigates whether the well-known "counterintuitive phenomenon" — where deep generative models assign higher likelihood to anomalous/out-of-distribution data than to in-distribution data — occurs in tabular anomaly detection. The authors propose a domain-agnostic formal definition of this phenomenon (Definition 3.3) based on relative AUROC performance against comparison models. Through extensive experiments on all 47 ADBench tabular datasets and 10 CV/NLP embedding datasets, benchmarked against 12 baselines, they show that NF-SLT (a normalizing flow with a simple likelihood test) achieves the highest average AUROC (0.8575), lowest fail ratio (0.02), and best average rank (3.43). The paper further provides theoretical analysis linking dimensionality to likelihood-gap inversion (Theorem 5.4) and empirical evidence using intrinsic dimension ratios to explain why tabular data differs from images.

## Strengths

1. **Exhaustive evaluation on the complete ADBench benchmark without selection bias.** The paper uses all 47 tabular datasets and 10 CV/NLP embedding datasets from ADBench (Section 4), explicitly citing Shwartz-Ziv & Armon (2022) to avoid cherry-picking. NF-SLT achieves the best average AUROC (0.8575), AUPRC (0.6398), average rank (3.43), Top2 Ratio (0.45), and a Fail Ratio of only 0.02 — far better than any of the 12 baselines (next best Fail Ratio is 0.13 for IF). This is the most comprehensive evaluation of likelihood-based tabular anomaly detection to date.

2. **Theoretical analysis connecting dimensionality to the likelihood gap.** Theorem 5.4 shows that under the independence assumption, the lower bound of the expected log-likelihood gap between normal and abnormal data decreases linearly with dimension d when H(P) − H(Q) > D_KL(Q‖P). Corollary 5.6 connects this to an inverse relationship between AUROC upper bound and dimension. While the independence assumption is strong, this formalizes an intuition that prior work (Caterini & Loaiza-Ganem, 2022) did not explicitly analyze.

3. **Quantitative analysis of feature correlation via intrinsic dimension ratio.** Section 5.2 introduces the d Ratio (intrinsic dimension / ambient dimension) to quantify overall feature correlation. Table 4 shows that image datasets have d Ratios of 0.002–0.019, while tabular datasets have much higher values (e.g., waveform 0.810, magicgamma 0.700). Figure 1 visualizes this gap with tabular datasets clustered near the identity line (avg. distance 0.488) versus images far below (avg. distance 2.14). This provides a concrete, measurable distinction between domains.

4. **Constructive dimensionality-reduction experiments on images.** Tables 2 and 3 provide direct empirical support: when ICA reduces image dimensions from 1024 to 30 under H(P) > H(Q), AUROC for CIFAR-100/SVHN rises from 0.0843 to 0.3490. Bilinear interpolation from 32×32 to 8×8 raises AUROC for CIFAR-100/SVHN from 0.0846 to 0.3918. The paper honestly acknowledges when results conflict with theory (SVHN/CelebA case in Table 3) and provides a reasoned explanation involving entropy changes from interpolation.

## Weaknesses

### Fatal

None.

### Major

1. **Framing mismatch between the original phenomenon and the operational definition.** The counterintuitive phenomenon in the literature (Nalisnick et al., 2019a; Kirichenko et al., 2020) refers to likelihood inversion — anomalies receiving higher likelihood than normal data. Definition 3.3 instead operationalizes it as the generative model being substantially outperformed by comparison models on AUROC. These are not the same construct: a model could suffer likelihood inversion yet still beat weak baselines, or correctly rank anomalies lower yet be outperformed by specialized methods. The abstract (line 9) states "unlike in the image domain where deep generative models frequently assign higher likelihoods to anomalous data, such counterintuitive behavior occurs far less often in tabular settings" — which a reader naturally interprets as addressing the original phenomenon. However, the experiments are designed around the redefined notion (relative AUROC performance). The paper transparently discusses the limitations of the raw likelihood-comparison view (lines 25–27), but the title and abstract create an expectation that the paper tests for the original phenomenon. The paper would be strengthened by clearly distinguishing between the original phenomenon and the proposed new definition, and ideally measuring both.

### Minor

2. **The strong independence assumption limits the theoretical analysis.** Theorem 5.4 assumes that both P and Q factorize as products of independent univariate distributions (line 142). Features in real tabular data are not independent. The paper acknowledges this limitation for the image-resizing experiment (line 164) but does not similarly qualify its applicability to tabular data. The theorem provides useful intuition but its scope is narrower than the general claims it is used to support.

3. **Hyperparameter selection protocol is ambiguous.** The evaluation section (line 122) states: "the hyperparameter combination with the highest average AUROC for all datasets is selected as the representative hyperparameter combination." It is unclear whether this means one global hyperparameter set was chosen to maximize average AUROC across all datasets, or per-dataset selection. This needs clarification.

4. **No confidence intervals or variance reported for the main results.** Results in Table 1 are reported as averages over 10 repeated experiments, but no standard deviations or confidence intervals are given. For cases like the 'yeast' dataset where the performance gap to the next model is only 0.02 AUROC, it is unclear whether this gap is statistically significant or within experimental noise.

5. **Cross-study comparison for intrinsic dimension estimates.** The ID estimates for image datasets in Table 4 and Figure 1 come from Pope et al. (2021), while estimates for tabular datasets are computed by the authors, potentially using different estimation configurations. The paper should note that this cross-study comparison introduces unknown systematic differences (e.g., the k parameter for MLE and TwoNN may differ between studies).

### Trivial

None.

## Nice-to-Haves

- **Direct measurement of likelihood inversion.** The paper could strengthen its claim by reporting, for each dataset, the proportion of anomalous test points whose likelihood exceeds the median (or some quantile) of normal-data likelihoods. This would directly measure whether the original phenomenon (likelihood inversion) occurs and complement the AUROC-based analysis.
- **The 'imdb' dataset exception** is discussed only briefly (NF-SLT scores 0.5013 vs. GOAD's 0.5398). Since this is the one CV/NLP embedding dataset where NF-SLT is not top-performing, a fuller discussion of what distinguishes this dataset would be helpful.

## Removed Points

These points were flagged by the Harsh Critic but are removed per review guidelines:

- **β and γ threshold values not specified** (Harsh Critic Critical Issue 2): REMOVED because the paper states "The fully rigorous formulation of Definition 3.3 is provided in Appendix B" (line 77). The parser strips appendix content from all papers; these values exist in the original submission. Per guidelines, criticisms about missing appendix content that was stripped by the parser must be removed.
- **CIFAR-10/SVHN baseline cherry-picking claim** (Harsh Critic Section 3 note): The critic speculates that "if one picked weaker baselines for the image case, the 'counterintuitive phenomenon' might not be detected." This is speculative — the paper uses published results (Morningstar et al., 2021; Sun et al., 2022) without manipulation. Per guidelines, speculative "what if" criticisms should be removed.
- **Missing appendix/proofs** (various references to Appendix D, F, G being unavailable): The parser strips appendix sections from all papers. Per guidelines, criticisms about missing appendix content are removed.
- **The criticism that "the theoretical apparatus is fragile when independence fails — which is the rule rather than the exception in real data"** overlaps with Weakness #2 above and is subsumed by it.

## Novel Insights

The most novel observation emerging from the reviews is the gap between the paper's framing and its operationalization. The paper claims to study the classic "counterintuitive phenomenon" (likelihood inversion) but actually studies whether a likelihood-based flow model is competitively outperformed by other anomaly detectors. This reframing is itself an interesting methodological contribution — the paper makes a reasonable case that raw likelihood comparison is insufficient — but the disconnect between the title/abstract's promise and the experiments' execution creates confusion about what is actually being claimed. A second insight is that the d Ratio analysis (intrinsic/ambient dimension) provides a genuinely novel way to quantify why the tabular and image domains differ, even if the cross-study methodological differences weaken the quantitative comparison.

## Suggestions

1. **Clarify the framing.** Distinguish explicitly between "likelihood inversion" (the original phenomenon) and "relative anomaly detection failure" (the proposed Definition 3.3). Either measure both, or clearly rebrand the paper's contribution as studying the latter.
2. **Report standard deviations or confidence intervals** for the main results in Table 1.
3. **Clarify the hyperparameter selection protocol** — is it per-dataset or global?
4. **Acknowledge the cross-study methodological differences** in ID estimation between Pope et al. (2021) and the authors' own computations.
5. **Discuss the 'imdb' exception** more thoroughly — what distinguishes this dataset that causes NF-SLT to underperform?

## Calibration Report

**Round 1 (bracketing):**
- Weak anchors (<3.5): Papers scoring 2.33–3.40 (tabular OOD, normalizing flows for OOD). Paper is clearly above these.
- Middle anchors (3.5–7.5): Papers scoring 3.60–6.25. Paper is in this range.
- Strong anchors (>7.5): Papers scoring 8.0 (four papers). Paper is clearly below these.
- **Initial bracket: 4.0–6.5**

**Round 2 (narrowing within bracket):**
- NCSNAD (5.75, Reject): Tabular AD with score networks, extensive experiments but limited novelty. Paper under review is slightly stronger in novelty of analysis.
- DRL (5.75, Accept): Tabular AD with representation learning. Comparable experimental breadth and quality.
- AVOID (6.00, Reject): VAE OOD detection with strong theoretical analysis but narrower scope. Paper is broader but less theoretically rigorous.
- FoMo-0D (5.75, Reject): Zero-shot tabular OD. Comparable quality with different strengths/weaknesses.
- Likelihood Peaks (5.67, Reject): Directly about the likelihood paradox with stronger theory. Paper is broader but less focused.
- **Narrowed range: 5.0–6.0**

**Round 3 (final check):** Additional anchors at 5.20 (time series AD benchmark) and 5.75 (TDD benchmark). Paper sits alongside these.

**Final score: 5.5.** The paper has substantial strengths (exhaustive evaluation, d Ratio analysis, dimensionality experiments) but is held back by a significant framing issue where the title/abstract imply studying the original likelihood-inversion phenomenon but the experiments operationalize a different construct (relative AUROC performance). This places it slightly below the strongest mid-range anchors but above incrementally novel work.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>