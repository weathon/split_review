Now I have all the verification needed. Let me produce the consolidated review.

## Summary

This paper proposes using Constant Q Cepstral Coefficients (CQCC) to classify neurodegenerative disorders (Parkinson's Disease, ALS, and healthy controls) from sustained vowel phonations. It compares CQCC against MFCC, Jitter, Shimmer, and Teager Energy using Random Forest and SVM classifiers on the Italian Parkinson's voice database and the Minsk2019 ALS database, reporting accuracy improvements of 5.6% and 7.7% over MFCC. The paper provides a theoretical derivation of the form-invariance property of the Constant-Q Transform as the motivation for why CQCC should outperform STFT-based features.

## Strengths

- **Novel application of CQCC to neurodegenerative speech classification:** While CQCC has been used in antispoofing (Todisco et al., 2017) and infant cry analysis (Patil et al., 2023), applying it to multi-class classification of Parkinson's Disease, ALS, and healthy controls is a plausible and underexplored direction. The multi-class setup (HC vs PD vs ALS) is less common than binary classification in this literature.

- **Comprehensive baseline comparisons:** The study compares CQCC against not only MFCC but also Jitter, Shimmer, and Teager Energy across three classification tasks (binary healthy-vs-pathology, multi-class, and inter-disease), systematically benchmarking against traditional acoustic measures used in prior work.

- **Validation across two distinct databases and multiple classification tasks:** Results are reported on both the Italian Parkinson's database and the Minsk2019 ALS database, covering binary, multi-class, and inter-disease classification scenarios, which provides breadth beyond a single dataset.

- **Theoretical discussion of form-invariance:** The derivation in Section 3.1.1 correctly identifies that CQT's window function depends on both time and frequency (unlike STFT's time-only window), and the paper connects this to the form-invariance property — a principled motivation for why CQCC might offer advantages for pitch-variable speech signals.

## Weaknesses

### Fatal
None.

### Major

- **Unfair feature dimensionality comparison invalidates the headline accuracy claims:** The paper's central quantitative result — that CQCC outperforms MFCC by 5.6% and 7.7% — compares **20 CQCC coefficients** against **13 MFCC coefficients** (Section 4.3, line 173). Higher-dimensional features can yield better classification accuracy simply by providing more degrees of freedom, especially on small datasets where overfitting risk is high. The paper does not control for this (e.g., equalizing dimensionality or showing CQCC still wins with fewer coefficients). This is a basic experimental design flaw; the reported improvements cannot be attributed to CQCC's inherent quality versus a dimensionality advantage.

- **No measure of variance on very small datasets makes results unreliable:** All accuracy numbers (Tables 4, 5, 6) are point estimates from a single 80/20 train-test split with no standard deviation, confidence intervals, or cross-validation. The datasets are small (Table 2: Italian Parkinson's ~80 samples, Minsk2019 ALS ~54 samples), so a single 80/20 split yields test sets of ~16 and ~11 samples respectively — each correct/incorrect prediction shifts accuracy by 6–9 percentage points. The reported 99% binary accuracy (Table 4) is especially suspicious under these conditions. Without k-fold cross-validation or repeated splits, the numerical results lack statistical grounding.

- **SMOTE application timing is not specified, risking data leakage:** Section 4.1 states "The imbalance in dataset was handled using SMOTE. For training and testing, we used 80% and 20% of the data, respectively." The paper does not specify whether SMOTE was applied before or after the train-test split. If applied before splitting, synthetic samples from the test distribution leak into training, inflating accuracy. The paper also does not state which classes were oversampled, the degree of oversampling, or the number of nearest neighbors used.

- **Form-invariance property is claimed as the mechanism for CQCC's superiority but is never empirically tested:** Sections 3.1.1 and the abstract state that CQCC's effectiveness is "underpinned by the form-invariance property" which "ensures consistent feature representation across varying pitch and tonal conditions." However, the paper conducts **zero experiments** that test this mechanism — no pitch-shifting evaluation, no noise robustness analysis, no cross-condition generalization test, no analysis of how feature distributions change under pitch variation. The form-invariance discussion remains purely theoretical and disconnected from the experimental section (Section 5). The paper therefore cannot attribute the observed accuracy differences to this mechanism rather than to dimensionality effects or data-specific characteristics.

### Minor

- **Database naming (D1, D2, D3) is never defined:** Section 5.2.1 refers to "database D2" and Section 5.2.2 introduces "new databases D1 and D3," but none of these are defined in the datasets section (Section 4.1), which describes only the Italian Parkinson's database and the Minsk2019 ALS database. This makes it unclear how the data was partitioned across experiments and harms reproducibility.

- **CQCC feature extraction parameters are underspecified:** The paper does not report the number of bins per octave (B) used, the maximum frequency, or the number of resampled bins before DCT (only "20 CQCC coefficients" is given). The value of B is introduced in equation (5) but never instantiated for the experiments, making the exact feature configuration irreproducible.

- **Classifiers use fixed, untuned hyperparameters:** RF (100 estimators, random_state=42) and SVM (RBF kernel, C=1) are used with no hyperparameter optimization. It is therefore unknown whether CQCC's advantage would hold under optimized baselines for each feature set.

- **LDA plots lack quantitative separation metrics:** Figure 3 is presented as evidence of "clearer separation" for CQCC, but no quantitative class-separability metric (e.g., Davies-Bouldin index, Fisher's ratio, silhouette score) is computed. The visual claim is subjective and not reproducible.

- **Novelty claim is narrow and self-serving:** The paper claims "no studies have reported on capturing the neurodegenerative disease on sustained vowel sounds through Form-Invariance property of CQT" and "this is the first study of its kind" (lines 25–27). However, the paper itself cites prior work using CQCC for pathological voice classification (Patil et al., 2023 for infant cry). Applying an existing feature to a new disorder category is a legitimate incremental contribution, but the "first" framing overstates the novelty.

### Trivial

- Line 216: "To that effectm" — appears to be a typo.
- Line 157: "imabalce" — typo for "imbalance."

## Nice-to-Haves

- Equalize feature dimensionality (e.g., use 13 CQCC coefficients or 20 MFCC coefficients) to produce a fair head-to-head comparison.
- Report results with k-fold cross-validation (e.g., 5-fold or 10-fold) with mean and standard deviation.
- Clarify SMOTE application: specify whether applied before or after splitting, the oversampling ratio, and k-neighbors parameter.
- Add an experiment that empirically tests form-invariance (e.g., pitch-shifting via audio resampling, comparing CQCC vs MFCC robustness).
- Tune classifier hyperparameters separately for each feature set to ensure baselines are not operating at suboptimal configurations.
- Define D1, D2, D3 explicitly and provide quantitative class-separability metrics for LDA analysis.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Abstract selectively omits results" (Harsh Critic §Critical Issues, point about 17.3% gain):** The abstract focuses on the CQCC vs MFCC comparison, which is the paper's central claim. The binary classification result (Table 4) involves a different task and comparison set. This is standard selective reporting, not suspicious omission.
- **"Irrelevant material (blood-brain barrier, WHO statistics)":** Background epidemiological and clinical context is standard in medical ML papers. Criticizing this is scope creep.
- **"Algorithm 1 is nearly a direct reproduction from prior work":** The paper clearly states "Adapted from (Patil et al., 2023)" and the novelty is in the application domain, not in proposing a new feature extraction algorithm. This criticism misreads the paper's contribution type.
- **Requests for pitch-shifting evaluation, noise robustness tests, cross-dataset generalization, or user studies:** These exceed the stated scope of the paper as an initial empirical evaluation. While they would strengthen the paper, their absence is not a flaw — the paper can be evaluated on what it does rather than what it does not attempt.
- **"Spectrographic analysis provides no quantitative evidence":** The spectrographic analysis (Section 5.1) is presented as qualitative/descriptive context, which is appropriate for that section. The paper does not claim it as experimental evidence.
- **"Feature vector inspection" / "example CQCC and MFCC vectors":** Nice-to-have but not a required element for an empirical systems paper at this stage.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no genuinely novel observation that the paper itself does not already contain or imply.

## Suggestions

1. **Fix the dimensionality mismatch as the highest priority.** Re-run experiments with equal numbers of CQCC and MFCC coefficients (e.g., 13 of each, or 20 of each). If CQCC still wins under equal dimensions, the core claim is credible. If not, the paper needs substantially different framing.

2. **Add cross-validation with error bars.** Given the very small dataset sizes (54–80 samples), report 5-fold or 10-fold cross-validation accuracy with mean and standard deviation. Without this, the numerical results cannot be interpreted meaningfully.

3. **Clarify SMOTE handling.** Specify whether SMOTE was applied before or after the train-test split. If before, re-run the experiments with SMOTE applied only to the training fold. Report the oversampling parameters (k-neighbors, sampling strategy).

4. **Define database naming.** Clearly explain what D1, D2, and D3 correspond to in terms of the two original databases (Italian Parkinson's and Minsk2019 ALS).

5. **Either test form-invariance empirically or de-emphasize the theoretical claim.** If form-invariance is central to the paper's narrative, include at minimum a pitch-shifting experiment where both CQCC and MFCC features are compared under pitch shifts. If this is not feasible, reframe the contribution around empirical observation rather than the theoretical mechanism.

6. **Specify all CQCC extraction parameters** — B (bins per octave), maximum frequency, and number of resampled bins — to enable reproduction.

## Score and Decision

The paper addresses a worthwhile direction — applying CQCC to neurodegenerative speech classification — and provides theoretical motivation for why this might work. However, the experimental validation has significant gaps that undermine the paper's core claims. The dimensionality mismatch (20 vs 13 coefficients) directly invalidates the headline accuracy comparison as evidence for CQCC's superiority. The absence of any variance measure on tiny datasets (test sets of ~11–16 samples), combined with unspecified SMOTE timing that risks data leakage, makes the numerical results unreliable. The central theoretical claim (form-invariance) is never tested. These issues are collectively too severe for the paper to support its conclusions in its current form.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>