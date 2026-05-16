Now I have all the information I need. Let me carefully construct the final review, cross-referencing every claim.

---

## Summary

This paper proposes applying Constant Q Cepstral Coefficients (CQCC) — a feature set borrowed from antispoofing and infant cry classification — to the task of classifying neurodegenerative disorders (Parkinson's disease and ALS) from sustained vowel phonations. The authors report absolute accuracy gains of 5.6% (RF) and 7.7% (SVM) over MFCC, and also compare against Jitter, Shimmer, and Teager Energy. The theoretical motivation (Section 3.1.1) derives the form-invariance property of the Constant Q Transform as a principled explanation for why CQCC may capture pitch-varying spectral cues better than STFT-based features.

## Strengths

1. **Theoretical grounding via form-invariance (Section 3.1.1).** The paper provides a clear mathematical derivation showing that the CQT window function depends on both time and frequency, which allows a stable, BIBO-satisfying form-invariance condition that the STFT cannot achieve with a practical filter. This is a principled motivation for why CQCC might be better suited to pathological speech than MFCC, and goes beyond a purely empirical comparison.

2. **First application of CQCC to multi-class neurodegenerative disorder classification on sustained vowels.** The paper explicitly identifies this gap (lines 25–27) and fills it with results on three-class (Healthy vs. PD vs. ALS) and pairwise (PD vs. ALS) classification. This is a genuine application transfer, even though CQCC itself is not a novel feature.

3. **Comprehensive baseline comparison across multiple feature types.** The paper compares CQCC against MFCC, Jitter, Shimmer, and Teager Energy using two classifiers (RF and SVM) across multiple classification tasks (Tables 4–6). CQCC achieves the highest accuracy in every configuration, showing consistent superiority over a diverse set of acoustic measures.

4. **Validation on two separate databases.** The study uses both the Italian Parkinson's Voice and Speech dataset and the Minsk2019 ALS database, which provides some evidence that the findings are not dataset-specific.

## Weaknesses

### Fatal
None.

### Major

1. **Unfair feature dimensionality comparison (20 CQCC vs. 13 MFCC).** Section 4.3 (line 173) explicitly states that 20 CQCC coefficients were compared against 13 MFCC coefficients. This 54% difference in feature count is a confound — higher-dimensional features can inflate classifier performance even if the features themselves are not intrinsically better, especially with a high-capacity classifier like Random Forest. The claimed 5.6%–7.7% improvements may partially or entirely reflect feature count rather than the inherent quality of CQCC. The authors must either match the number of coefficients (e.g., 20 of each) or demonstrate that the advantage persists after controlling for dimensionality.

2. **Single train–test split with no cross-validation or statistical reliability.** The paper uses a single 80–20 split on datasets with roughly 56–114 total samples (Section 4.1, line 157), yielding test sets of size ~11–23. No standard deviations, confidence intervals, or repeated experiments are provided. On such small test sets, a single accuracy number (e.g., 99% for CQCC+RF) could easily be a fluke — misclassifying just one or two samples swings accuracy by 5–10 points. At minimum, stratified k-fold cross-validation (or repeated splits) with mean ± std must be reported for the results to be credible.

3. **SMOTE application ambiguity with potential data leakage.** The paper states "The imabalance in dataset was handled using SMOTE" (line 157) but does not specify whether SMOTE was applied *before* or *after* the train–test split. If applied before splitting, synthetic samples from the test-set distribution could leak into training and inflate accuracy. Even if applied after, details such as the k-neighbors parameter and sampling strategy are missing. This is a methodological gap that casts doubt on the validity of all reported results.

4. **Only classification accuracy reported; no per-class metrics.** Section 4.2 (line 169) states that performance is evaluated using "% classification accuracy." For imbalanced datasets — even with SMOTE — accuracy alone can be misleading. Precision, recall, and F1-score for each class, along with confusion matrices, are needed to verify that high accuracy is not driven by one class at the expense of another, and that SMOTE has not introduced artifacts.

### Minor

5. **Missing CQCC parameters for reproducibility.** The paper specifies `f_min = 20 Hz` and 20 coefficients (line 173), and defines the number of bins per octave `B` in Equation (5) (line 89–92), but never states what value of `B` was actually used in the experiments. The quality factor `P` (also defined in Equation 5) is thus also unspecified. These parameters affect the filter bank geometry and can influence performance. Without them, the experiments cannot be reproduced.

6. **Large and unexplained RF/SVM accuracy gap.** In Table 4, CQCC achieves 99% with RF but only 63.4% with SVM — a 35.6 point gap. This is not discussed and is suspicious. It suggests either the SVM is poorly configured (default C=1 may be inappropriate for these features) or the RF is overfitting. Without hyperparameter tuning or cross-validation, neither explanation can be ruled out, making the results uninterpretable.

7. **D1 and D3 databases are not clearly defined.** Line 216 states "Two new databases D1 and D3 were prepared" but gives no concrete composition — which pathologies do they contain? With what class distribution? This is essential for interpreting Tables 5–6.

8. **LDA plots are only qualitative.** Figure 3 and the associated discussion (lines 236–247) rely on visual inspection to claim that CQCC yields better class separation than MFCC. The authors should report a quantitative metric (e.g., Davies–Bouldin index, silhouette score, or LDA-based classification accuracy) to support this claim.

9. **No hyperparameter tuning.** Both RF (100 estimators, random_state=42) and SVM (RBF, C=1) are used with default/arbitrary parameters (Section 4.2, lines 169–170). Without tuning (e.g., grid search with internal cross-validation), the comparison is biased toward whichever classifier happens to work better with defaults, and the results may not reflect optimal performance for either feature set.

10. **Form-invariance theory is not empirically validated or connected to the experiments.** Section 3.1.1 provides a mathematically interesting derivation of the form-invariance property, but no experiment demonstrates that this property actually benefits the classification task (e.g., by artificially transposing a sample and showing that CQCC features are more stable under pitch shifts than MFCC). The theory feels compartmentalized from the results.

11. **No statistical significance tests.** Given the small test sets and single split, a paired test (e.g., McNemar's) between classifiers or feature sets would be valuable to assess whether the reported differences are significant.

12. **Conclusions overstate the findings.** Phrases like "comprehensively assessed" and "most effective feature" (lines 249–251) are not justified given the experimental weaknesses (single split, no cross-validation, unfair comparison, missing per-class metrics, potential data leakage from SMOTE).

### Trivial
13. **No limitations section.** The paper does not discuss limitations such as small sample size, only two disorders, single recording session per participant, or the lack of cross-dataset generalization testing.

14. **Per-vowel analysis not provided.** The datasets contain all vowel sounds, but results are aggregated. Disaggregated per-vowel results could be informative.

## Nice-to-Haves
- The paper could be strengthened by empirically validating the form-invariance property (e.g., pitch-shift robustness test connecting the theory to the application).
- Per-vowel breakdowns could identify which phonemes carry the most discriminative information.
- A cross-dataset generalization experiment (train on one dataset, test on another) would substantially increase confidence in the approach.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Garbled column headers in Tables 5–6"** — Removed per hard rule: formatting/parser artifacts in the review environment are not author errors.
- **Criticism that CQCC is "not novel" as a feature** — The paper does not claim CQCC is a new feature; it claims this is the first application to multi-class ND classification on sustained vowels. The critic's framing as a weakness is a strawman; the paper acknowledges the origin of CQCC (line 23).
- **"Introduction is overly generic"** — This is a stylistic judgment, not a substantive weakness. The introduction appropriately motivates the problem for an interdisciplinary audience.
- **"No evaluation of feature-level effects (ablation)"** — While an ablation would strengthen the paper, demanding it as a weakness overstates its necessity. Moved to Nice-to-Haves implicitly.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the key tension: an interesting, theoretically motivated proposal undermined by experimental evaluation that cannot support its claims. The core insight remains the paper's own: CQCC + form-invariance is a principled alternative to MFCC for pathological speech, but the evidence presented is too weak to validate it.

## Suggestions

1. **Match the feature count.** Extract 20 MFCC and 20 CQCC coefficients (or 13 of each) to eliminate dimensionality as a confound.
2. **Replace the single split with stratified k-fold cross-validation (at least 5-fold)** and report mean ± std for accuracy, precision, recall, and F1 per class.
3. **Clarify the SMOTE procedure** — specify that it is applied *after* the train–test split, and describe the sampling strategy (k-neighbors, target ratio).
4. **Specify the value of `B` (bins per octave) and `P`** used in the CQT computation.
5. **Define D1 and D3 concretely** — state the exact class composition and source databases for each.
6. **Tune both classifiers** (e.g., grid search with internal cross-validation) rather than using default parameters.
7. **Add a quantitative separability metric** for the LDA plots (e.g., silhouette score or Davies–Bouldin index).
8. **Add a limitations section** acknowledging small sample size, only two disorders, and no cross-dataset validation.

## Score and Decision

This paper tackles an interesting and well-motivated problem: applying CQCC features to the classification of neurodegenerative disorders, with a solid theoretical foundation in the form-invariance property of the CQT. However, the experimental evaluation has several major weaknesses that prevent the results from being credible. The unfair dimensionality comparison (20 vs. 13 coefficients), the reliance on a single train–test split without any variance measure, the ambiguity around SMOTE application, and the omission of per-class metrics collectively mean that the reported accuracy gains cannot be trusted as reliable or generalizable. These are not minor presentation issues — they directly affect whether the paper's central claim is supported. The paper would need substantial reworking of its experimental methodology to make a convincing case.

**Originality / Research Question Importance:** Good — the application of CQCC to ND classification is novel and the problem is important.  
**Claims Support / Experimental Soundness:** Weak — the experiments have multiple confounds and insufficient rigor.  
**Clarity:** Adequate — the theoretical sections are clear, but the experimental description is missing key details.  
**Value to Community:** Potential is there, but the current evidence is insufficient to validate the approach.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>