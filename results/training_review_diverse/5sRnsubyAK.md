Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper proposes Constant Q Cepstral Coefficients (CQCC) — a feature set originally developed for anti-spoofing — for classifying neurodegenerative disorders (Parkinson's Disease and ALS) from sustained vowel phonations. The authors argue that CQCC's geometrically-spaced frequency bins and form-invariance property provide better spectrotemporal resolution for capturing disease-related vocal signatures than the standard MFCC. They report that CQCC outperforms MFCC, Jitter, Shimmer, and Teager Energy features under Random Forest and SVM classifiers across binary and multi-class tasks on two databases.

## Strengths

- **Principled theoretical motivation for CQCC over MFCC**: Section 3.1.1 provides a mathematically grounded explanation of why the CQT's form-invariance property is achievable with a window function that depends on both time and frequency (satisfying BIBO stability), while the STFT-based MFCC cannot achieve this with a realizable stable window. This theoretical distinction between CQT and STFT is well-articulated and provides a genuine reason why CQCC might better handle pitch variation in pathological speech — a dimension prior ND classification work has not explored.

- **Consistent accuracy advantage across multiple tasks and classifiers**: The reported results in Tables 4–6 show CQCC outperforming MFCC not in one but in several distinct evaluation settings: binary healthy-vs-pathological (Table 4), three-way PD-vs-ALS-vs-Healthy (Table 5), and pairwise PD-vs-ALS (Table 6), under both RF and SVM. While the magnitude of the improvement is questionable (see Weaknesses), the consistency across tasks provides some support for the idea that CQCC captures information MFCC does not.

- **Evaluation on two different neurodegenerative diseases**: Using both the Italian Parkinson's database and the Minsk2019 ALS database demonstrates that the proposed method generalizes beyond a single disorder, which is a step beyond work focusing on a single pathology.

## Weaknesses

### Fatal

None. The core idea (CQCC for ND classification) is not inherently invalid. However, see Major weaknesses.

### Major

1. **Experimental validation is insufficient to support the reported accuracy numbers**. The datasets are very small (Table 2, not text-readable but attested by the reviewer's numbers: ~28 PD, ~12 HC from Italian database; ~11 ALS, ~14 HC from Minsk database). The paper uses a single 80/20 train/test split with no cross-validation. On a combined dataset of ~65 samples, an 80/20 split yields a test set of ~13 samples, meaning the claimed absolute improvements of 5.6% and 7.7% could represent a difference of just 1–2 samples. No confidence intervals, no standard deviations across multiple splits, and no statistical significance tests are reported. The binary classification result of **99% accuracy with RF** is particularly suspicious under these conditions — a single lucky split can easily produce such numbers by chance. This issue cuts across every quantitative claim in the paper (Tables 4–6). Without repeated stratified k-fold cross-validation, the reader cannot distinguish genuine feature superiority from a favorable test split. This is the most serious weakness and prevents acceptance in the current form.

2. **Uncontrolled feature dimensionality confounds the comparison**: The paper uses 20 CQCC coefficients against 13 MFCC coefficients (line 173) without explanation or control. Higher-dimensional features generally provide greater discriminative power, especially with tree-based classifiers, unless a dimensionality penalty is applied. The paper does not attempt to match feature sizes (13 vs. 13 or 20 vs. 20), does not discuss whether larger CQCC dimensionality could explain the observed gains, and does not analyze which coefficients drive the improvement. The 5.6% and 7.7% improvements are therefore not interpretable as evidence of CQCC's superiority over MFCC — they may partly reflect an unequal feature count.

3. **The form-invariance property is invoked as a theoretical justification but never empirically validated**: The abstract and Section 3.1.1 explicitly tie CQCC's expected advantage to the form-invariance property, claiming it "ensures consistent feature representation across varying pitch and tonal conditions, thereby enhancing classification robustness." However, **no experiment tests pitch variation**, no analysis measures feature stability under pitch shifts, and no connection is drawn between form-invariance and the classification tasks studied. The paper does not even check whether subjects in the datasets differ in pitch. The form-invariance discussion is theoretically competent but decorative — there is zero evidence that it explains the observed performance difference. This disconnect between the paper's central theoretical argument and its experiments is a significant gap.

### Minor

1. **LDA visualization on training data is not a valid validation**: Figure 3 shows LDA projections fitted to the same features used for classification, then interpreted qualitatively as showing "clearer separation" for CQCC. This is circular — LDA always finds the projection that best separates training classes; the apparent separation reflects training-data geometry and is heavily influenced by the tiny sample size. This does not constitute evidence that CQCC generalizes better than MFCC. A proper analysis would measure separability on held-out data or use a bounded quantitative metric (e.g., Davies-Bouldin index).

2. **Missing per-class metrics**: Only overall accuracy is reported. With class imbalance (PD ≈ 28, HC ≈ 12, ALS ≈ 11), overall accuracy can be misleading. Without confusion matrices and per-class precision/recall/F1, it is impossible to tell whether CQCC improves all classes equally or masks failures on minority classes (particularly the ALS group with ~11 samples).

3. **SMOTE application details are underspecified**: The paper states "The imbalance in dataset was handled using SMOTE" (line 157) but does not state whether SMOTE was applied before or after the train/test split, nor whether it was applied only to the training data. Applying SMOTE before splitting causes data leakage (synthetic samples derived from test data contaminate training). This is a standard concern and must be clarified.

4. **Spectrographic analysis (Section 5.1) is descriptive and disconnected from the feature experiments**: The analysis describes expected spectrogram differences among ALS, PD, and healthy speakers (pitch instability, monotonicity, etc.) but never links these observations back to why CQCC should capture them better than MFCC. This section reads as background knowledge rather than an analysis that supports the paper's contribution.

5. **No discussion of limitations**: The paper lacks a section acknowledging the small dataset sizes, the use of sustained vowels rather than conversational speech (which limits clinical applicability), potential recording-level confounds, and the absence of statistical rigor. A limitations section is standard for papers with constrained experimental conditions.

6. **Copy-paste artifacts suggest careless preparation**: Lines 73 and 157 refer to "infant cry classification" and "cry signals" — clearly text adapted from Patil et al. 2023 (infant cries) that was not revised for the adult neurodegenerative disease context. While not substantive, this undermines confidence in the care taken with the experimental work.

### Trivial

- No hyperparameter search was performed for RF or SVM (fixed: n_estimators=100, C=1, RBF kernel); while not fatal, tuning would strengthen confidence that CQCC's advantage is not an artifact of suboptimal baselines.
- The pseudo-code in Algorithm 1 has parser-induced artifacts (line numbers, notation) but the original would be readable.

## Nice-to-Haves

- Run repeated stratified k-fold cross-validation (e.g., 10 runs of 5-fold) and report mean accuracy ± std. This is the minimum requirement given the dataset sizes.
- Control for dimensionality: compare CQCC and MFCC at matched coefficient counts (13 vs. 13 or 20 vs. 20) to isolate the effect of the constant-Q representation from the effect of more features.
- Test the form-invariance claim directly by pitch-shifting test samples and measuring whether CQCC-based classifiers degrade less than MFCC-based ones.
- Release the exact data splits and code for reproducibility.

## Removed Points

- **Criticism about Algorithm 1 pseudo-code being ambiguous** (line 83 shows "78::" and garbled notation): These are PDF parser formatting artifacts, not author errors. The original submission's pseudo-code is presumably readable.
- **LDA visualization as a strength** (from Strength Finder: "provides visual corroboration"): This conflicts with the verified weakness that the LDA is circular (fitted to training data, interpreted qualitatively). The weakness wins; the strength is removed.

## Novel Insights

The key methodological observation connecting the reviews is that the paper's core theoretical argument (form-invariance) and its experimental evidence operate in completely separate worlds — the theory predicts robustness to pitch variation, but the experiments test task-level classification accuracy on fixed-pitch sustained vowels. Neither the reviewers nor the paper connect these two levels. This gap is more fundamental than any individual experimental flaw: even with perfect cross-validation, the paper would not actually validate its stated theoretical premise.

## Suggestions

1. **Replace the single 80/20 split with repeated stratified cross-validation** (at minimum 10 runs of 5-fold). Report mean accuracy, standard deviation, and per-class F1-scores with confusion matrices. This is non-negotiable for the current experimental design to be credible.

2. **Feature dimensionality must be controlled**. Either match the number of coefficients (13 CQCC vs. 13 MFCC, and 20 vs. 20) or use a feature selection method to pick the best k from each set. Without this, the claimed advantage of CQCC over MFCC is not interpretable.

3. **Either test the form-invariance property empirically or remove it from the abstract/claims**. Add a simple pitch-shift experiment: artificially shift the pitch of test utterances (e.g., ±2, ±5 semitones), measure accuracy degradation for CQCC vs. MFCC classifiers. If the property cannot be tested, the paper should be honest that form-invariance is a theoretical motivation, not a validated component of the results.

4. **Add a dedicated Limitations section** acknowledging the small dataset sizes, the use of sustained vowels versus conversational speech, potential recording-session confounds, and the absence of statistical significance testing.

## Score and Decision

The paper addresses a meaningful problem (feature extraction for ND classification) with a theoretically interesting feature set (CQCC) that has not been applied to this domain. The form-invariance discussion is a genuine strength in terms of motivation. However, the experimental validation is too weak to support the core claims. The small datasets, single 80/20 split with no cross-validation, uncontrolled feature dimensionality, and untested form-invariance premise collectively make the reported accuracy numbers uninterpretable. The paper cannot be accepted in its current form.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>