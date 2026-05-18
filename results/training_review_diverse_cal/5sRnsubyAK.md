I have all the information I need. Let me now produce the final consolidated review.

## Summary

This paper proposes using Constant Q Cepstral Coefficients (CQCC) as a feature set for classifying Parkinson's disease, Amyotrophic Lateral Sclerosis, and healthy controls from sustained vowel phonations. The authors compare CQCC against MFCC, Jitter, Shimmer, and Teager Energy features using Random Forest and SVM classifiers on two publicly available clinical databases. The paper provides a mathematical derivation of the CQT's form-invariance property as theoretical motivation and reports that CQCC achieves absolute accuracy improvements of 5.6% (RF) and 7.7% (SVM) over MFCC in multi-class classification.

## Strengths

- **Consistent accuracy gains across multiple classification tasks.** The paper reports that CQCC outperforms MFCC and traditional acoustic measures on binary healthy-vs-pathological (99% with RF), multi-class Parkinson's-vs-ALS-vs-Healthy (5.6–7.7% improvement), and ALS-vs-PD discrimination (86.1% with SVM). The same direction of improvement holds across all three tasks, which is consistent with the paper's central claim.

- **Theoretical grounding of CQCC via the form-invariance property.** Section 3.1.1 provides a formal mathematical derivation showing why the CQT analysis window (which depends on both time and frequency) satisfies form-invariance, while the STFT window (time-only) does not. The paper connects this to Flanagan's cochlear model, grounding the CQT advantage in auditory theory that is absent from standard MFCC-based approaches.

- **Validation on two distinct clinical databases.** The study uses the Italian Parkinson's Voice and Speech dataset (Dimauro & Girardi, 2019) and the Minsk2019 ALS database (Vashkevich et al., 2019), covering different languages, recording conditions, and disease populations. Table 2 provides participant statistics (sex/disease distribution), and the consistent CQCC advantage across both databases supports cross-population generalizability.

- **Comprehensive baseline comparison.** The paper systematically evaluates five feature sets (CQCC, MFCC, Jitter, Shimmer, Teager Energy) across three classifiers and three classification scenarios, showing that traditional prosodic and perturbation measures consistently underperform CQCC.

## Weaknesses

### Major

- **The dataset splits D1, D2, and D3 are never defined, making the core experimental setup uninterpretable.** Section 5.2.1 introduces D2 for binary healthy-vs-pathological classification, and Section 5.2.2 introduces "new databases D1 and D3" for multi-class tasks, stating only that they contain "two different pathologies, along with healthy controls from both databases." The paper does not specify which pathologies go into which split, how the original Italian PD and Minsk2019 ALS databases were recombined, how many samples each class contains in each split, or whether any subjects appear in multiple splits. Without this information, the results in Tables 4–6 cannot be properly interpreted, compared, or reproduced. This is a fundamental experimental reporting gap given that the paper's contribution hinges on these numerical results.

- **Results are reported from a single 80/20 train-test split without cross-validation, error bars, or any measure of variance.** Every accuracy reported is a point estimate from one random split. With datasets of at most ~200–300 participants (Table 2), a single split can produce unreliable estimates. The 99% RF+CQCC accuracy (Table 4) is particularly suspicious in this context — it could reflect an easy binary separation or a fortuitous split. Without cross-validation (e.g., 5-fold or leave-one-subject-out) and standard deviations, these numbers cannot be trusted as reliable estimates of generalization performance. This is a minimum standard for small-dataset speech pathology studies.

- **The comparison between CQCC (20 coefficients) and MFCC (13 coefficients) is confounded by feature dimensionality.** As stated in Section 4.3, CQCC uses 54% more features than MFCC. With small datasets and no cross-validation, the observed accuracy gap could partly reflect overfitting from higher-dimensional features rather than the inherent superiority of CQCC's time-frequency representation. A controlled comparison (matching coefficient counts or using internal validation to select the optimal dimensionality for each feature set) is needed to attribute the gains to the feature type rather than its dimensionality.

### Minor

- **The form-invariance property is invoked as a theoretical justification but never empirically tested.** The abstract claims form-invariance "ensures consistent feature representation across varying pitch and tonal conditions, thereby enhancing classification robustness," and Section 3.1.1 provides a mathematical derivation. However, no experiment tests this mechanism — no pitch-shifting, no feature stability comparison across different fundamental frequencies, no demonstration that form-invariance explains the observed accuracy gains. The theory and experiments are disconnected, making the theoretical framing decorative rather than evidential.

- **SMOTE application is underspecified.** The paper states "The imbalance in dataset was handled using SMOTE" (Section 4.1) but does not specify whether SMOTE was applied before or after the train-test split. Applying it before the split would leak information from the test set into training, potentially inflating accuracy estimates.

- **Classifier hyperparameters are fixed without tuning or sensitivity analysis.** RF uses 100 trees with random state 42; SVM uses an RBF kernel with C=1. No hyperparameter search, ablation, or sensitivity analysis is reported. It is unclear whether the reported results are robust to reasonable variations in these choices.

- **"Cry signals" appears as a copy-paste artifact.** Section 4.1 refers to "cry signals" when describing the PD and ALS sustained vowel datasets — an artifact from the infant cry classification literature (Patil et al., 2023) cited in the related work. This suggests insufficient proofreading.

- **No statistical significance testing.** The paper claims CQCC "significantly outperform[s]" MFCC (Abstract) without any statistical test (e.g., McNemar's or paired bootstrap) to support this claim. The observed accuracy differences may or may not be statistically significant given the small sample sizes.

### Trivial

None.

## Nice-to-Haves

- A pitch-shifting experiment directly testing whether CQCC representations are more stable than MFCC across varying fundamental frequencies would connect the theoretical form-invariance claim to the empirical results.
- Confusion matrices or per-class precision/recall would clarify where CQCC gains come from (e.g., better ALS detection vs. better PD detection).
- Statistical significance testing to support claims of "outperformance."

## Removed Points

These points raised by reviewers were removed because they reflect parsing artifacts, reviewer misreading, or do not apply to this paper's category:

1. **"Key tables are missing (images not parsed)"** — The tables are included as images in the original submission; the parser stripped their visual rendering. This is a parsing artifact, not an author error. The key numerical claims (99%, 5.6%, 7.7%, 86.1%) are stated in the text.
2. **"LDA plots not visible"** — Same parsing artifact; the plots exist in the original submission.
3. **Claims about missing appendix content** — The parser strips these sections from all papers.

## Novel Insights

None beyond the paper's own contributions. The core observation — that CQCC may capture fine-grained spectral detail useful for differentiating neurodegenerative disorders from sustained vowels — is worth investigating, but the review process did not surface any insight beyond what the paper itself asserts.

## Suggestions

1. **Define D1, D2, and D3 explicitly.** Provide the composition, per-class counts, and recombination strategy for each split. Ideally, release these exact splits to enable reproducibility.
2. **Replace single-split accuracies with cross-validated results** (e.g., 5-fold or leave-one-subject-out) and report mean accuracy ± standard deviation. This is the minimum standard for the claims being made.
3. **Control for feature dimensionality** by either matching the number of coefficients across CQCC and MFCC, or plotting accuracy as a function of the number of coefficients for both feature sets to show the comparison is not an artifact.
4. **Clarify whether SMOTE was applied before or after the train-test split.** If before, re-run with SMOTE applied only to the training folds to avoid information leakage.
5. **Add statistical significance testing** (e.g., McNemar's test) to support the claim that CQCC "significantly outperforms" alternatives.
6. **Either test the form-invariance claim empirically** (e.g., via pitch-shifted recordings) or temper the theoretical claims in the abstract to reflect that the paper does not empirically isolate this mechanism.
7. **Correct the "cry signals" error** and other minor copy-paste artifacts.

## Score and Decision

**Originality:** 5/10 — Applying CQCC (already established in antispoofing and infant cry) to neurodegenerative disorder classification is a useful transfer, not a fundamentally new idea.
**Importance of research question:** 7/10 — Non-invasive diagnostic aids for neurodegenerative disorders are a worthwhile goal.
**Support for claims:** 3/10 — The claims are not adequately supported due to missing dataset definitions, no cross-validation, and confounded feature dimensionality.
**Soundness of experiments:** 3/10 — Single 80/20 split, no error bars, uncontrolled dimensionality, undefined dataset splits.
**Clarity of writing:** 5/10 — The mathematical derivation is clear, but the experimental reporting is vague. Copy-paste artifacts reduce clarity.
**Value to the community:** 4/10 — The idea has potential value, but in its current form the results are not reliable enough to build upon.

The paper identifies a plausible feature candidate and provides a theoretical motivation, but the experimental evaluation has significant methodological gaps that prevent the reader from trusting the central claims. The undefined dataset splits, absence of cross-validation, and confounded feature dimensionality are not minor oversights — they are foundational to whether the claimed improvements are real. A major revision addressing these issues could make this a useful contribution.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>