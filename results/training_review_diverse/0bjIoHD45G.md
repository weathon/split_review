Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper identifies two reasons deep learning lags behind tree-based methods on tabular data: (1) the presence of numerical features that behave categorically ("implicitly categorical features" or ICF) which neural networks handle poorly due to their uniform numerical processing, and (2) the bias of deep networks toward overly-smooth solutions. The authors propose statistical tests (chi-squared, ANOVA, mutual information) to detect ICF features and encode them categorically, and adapt Learned Fourier Features (LFF) from vision/graphics to tabular data to mitigate smoothness bias. On a 68-dataset benchmark, the combined method (ResNet+F|C) achieves best-run performance that matches or exceeds XGBoost on classification tasks, with notable "spikes" on some datasets.

## Strengths

1. **Identification of implicitly categorical features is a genuinely useful observation about tabular data.** The paper coins the ICF concept and provides concrete examples (e.g., the eye movements dataset where assignment/line/word numbers are numerical but categorical in nature). This is a real insight that helps explain why DL struggles on certain datasets. Evidence: Section 1 (lines 12-13), Section 3.2 (lines 63-65).

2. **Both proposed components (ICF encoding and LFF) are shown to be independently beneficial through ablation analysis.** The paper separates the contributions in Section 5.4 (Figure 5), demonstrating that on some datasets (eye movements, electricity) the ICF component drives the gains, while on others (year, covertype) the LFF component dominates. This complementarity supports the paper's thesis that these are distinct, addressable issues. Evidence: Section 5.4, lines 182-184.

3. **The improvement is robust across two fundamentally different backbone architectures (MLP and 1D convolutional ResNet).** This strengthens the generality of the findings, showing that the preprocessing benefits are not architecture-specific. Evidence: Figure 2 shows both MLP+F|C and ResNet+F|C substantially outperform their respective baselines across all task subcategories.

4. **Comprehensive empirical evaluation on 68 datasets from an established benchmark, following the original setup closely.** The paper uses 150 random search runs per model, totaling 51,000 runs, providing a thorough investigation. Evidence: Section 4 (line 118-120), Section 5 (line 127).

## Weaknesses

### Major

1. **No comparison against existing deep tabular methods that address the same issues.** The paper frames its contribution around closing the DL-to-tree gap but only compares against a plain MLP, a 1D convolutional ResNet, and XGBoost. Critically, Gorishniy et al. (2022) — which the paper acknowledges as "closely related" — already proposed piecewise linear embeddings and periodic activation functions to handle categorical-like numerical features and non-smooth functions. Without comparing against these or other established deep tabular methods (e.g., FT-Transformer), it is impossible to determine whether the proposed ICF+LFF preprocessing offers benefits beyond what existing methods already achieve, or whether the gains simply reflect moving from a naive MLP to a more thoughtful architecture. The title claim of "closing the gap" is credible only if the gap relative to XGBoost is closed without sacrificing ground against the best deep tabular methods — but that comparison is absent.

2. **The reported performance is based on best-run selection, but the method is unreliable — the "spiking" behavior means a typical run does not match XGBoost.** The authors themselves acknowledge this contradiction: Figure 3 (performance profiles averaging over the top eight runs) paints a much weaker picture than Figure 2 (budget plots selecting the single best run). The paper attributes this to "spiking" (Section 5.3), where a lucky hyperparameter draw finds a good ICF encoding. In practice, a user would not know a priori which random seed will produce the spike. The abstract states the method "achieves a performance that closely matches or surpasses XGBoost," but this is only true under best-run selection for classification tasks, and even then only on a subset of datasets. The paper would benefit from a more measured framing that acknowledges the method finds good encodings *when the search lands on them*, rather than suggesting the method itself is a reliable alternative to XGBoost.

### Minor

3. **The ICF detection procedure is underspecified, particularly the binning method.** The paper states features are "binned" for the statistical tests but never specifies the number of bins, whether binning is equal-width or equal-frequency, or any other detail. This is a reproducibility gap. While the detection thresholds are treated as hyperparameters in the search, the binning strategy is a separate design choice that could materially affect which features are flagged as ICF.

4. **No ablation comparing LFF to existing periodic activation functions (Gorishniy et al., 2022).** The paper describes the architectural differences (LinearLFF mixes features via linear projection; Conv1x1LFF uses parameter sharing; periodic activations embed features separately) but provides no experimental comparison. Without this, it is unclear whether the specific form of Fourier embedding matters or whether any mechanism for non-smooth representations would produce similar gains.

### Trivial

5. **The description of the chi-squared p-value in Section 3.2 is technically incorrect.** The text states a low p-value "measures the evidence against a null hypothesis that the two categorical features are correlated" (line 65). The null hypothesis for the chi-squared test of independence is that the variables are *independent*, not correlated. A low p-value provides evidence against independence (i.e., in favor of correlation). The practical conclusion (low p-value → encode as categorical) is unaffected, but this should be corrected.

## Nice-to-Haves

- A controlled ablation fixing a single ICF threshold (rather than treating detection as part of the hyperparameter search) would help demonstrate whether the method works without extensive tuning.
- Reporting reliability metrics (e.g., probability of beating XGBoost within a given budget) alongside best-run performance would give a more balanced picture of the method's practical utility.

## Removed Points

- **yprop_4_1 exclusion (Harsh Critic: "should be explicitly justified"):** The paper already justifies this at line 127 ("We exclude datasets where no model achieves a performance higher than 0.1... to avoid introducing misleading statistics"). This is a misread by the reviewer.
- **"RESNET architecture uses 1D convolutions along the feature dimension, which is not a standard choice":** The paper explicitly motivates this choice via rotational invariance arguments (Section 3.4, line 109). This is a design rationale, not a weakness.
- **Mutual info formula appears garbled (Equation 3):** The reviewer acknowledges the parser may be responsible. Per the hard rules, parser artifacts are removed.
- **Generic strength from Strength Finder that conflicts with verified weaknesses:** Dropped per instructions.
- **"Missing appendix, missing proofs in appendix":** Per hard rules, parser-stripped sections are not author errors.
- **Demand for SOTA deep baselines framed as fatal:** The lack of comparison is a real weakness (kept in Major), but the reviewer's framing that the contribution is "severely undercut" is overwrought — the paper's primary claim is about closing the gap to tree-based methods, and the XGBoost comparison is the relevant one for that claim.

## Novel Insights

The most interesting observation from the combined reviews — beyond the paper's own contributions — is the inherent tension between the paper's findings and the reliability criterion that practitioners actually care about. The "spiking" phenomenon shows that ICF detection via simple statistical tests can occasionally unlock dramatic improvements (best-run beating XGBoost by a wide margin on some datasets), but the same tests fail to do so consistently across random seeds. This suggests that the *signal* the paper identifies (numerical features with categorical characteristics) is real and impactful, but the *detection method* (threshold-based statistical tests) is too crude to reliably identify the right features. A more robust detection mechanism — or end-to-end learning of which features should be treated as categorical — could be a more impactful contribution. The paper's main value may be in drawing attention to this phenomenon rather than in the specific detection method proposed.

## Suggestions

1. **Add at least one strong deep tabular baseline** (e.g., MLP with periodic activations from Gorishniy et al. 2022, or FT-Transformer) on a subset of datasets to establish that the ICF+LFF preprocessing offers benefits beyond existing published techniques.
2. **Specify the binning method** (number of bins, equal-width vs. equal-frequency) for reproducibility.
3. **Re-frame the central claim** to honestly reflect the spiking behavior: e.g., "Our preprocessing occasionally (when the right encoding is found) enables deep methods to match or surpass XGBoost, though the gains are inconsistent across random seeds."
4. **Run a controlled ablation** with a fixed ICF threshold (not as a hyperparameter) to demonstrate the method works without extensive search.
5. **Correct the chi-squared p-value description** in Section 3.2.

## Score and Decision

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>