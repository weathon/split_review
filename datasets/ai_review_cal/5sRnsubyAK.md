- Decision: Reject
- Avg Score: 3.75
- Scores: 5, 6, 3, 1
Now I have all the information I need. Let me synthesize the final consolidated review.

## Summary

This paper applies Constant Q Cepstral Coefficients (CQCC) — geometrically-spaced cepstral features with a form-invariance property derived from the Constant Q Transform — to classify Parkinson's Disease, Amyotrophic Lateral Sclerosis, and healthy controls from sustained vowel phonations. On two databases (Italian Parkinson's and Minsk2019 ALS), the authors report that CQCC + Random Forest/SVM outperforms MFCC by 5.6–7.7% absolute accuracy in multi-class classification and achieves 99% accuracy in binary healthy-vs-pathological classification. The paper also provides LDA visualizations and spectrographic analyses to motivate the feature set.

## Strengths

- **Clear quantitative improvement over MFCC**: Table 5 reports absolute accuracy gains of 5.6% (RF) and 7.7% (SVM) for CQCC over MFCC in multi-class classification on combined databases, and Table 6 shows CQCC achieving 86.1% (SVM) on ALS-vs-PD classification — a concrete demonstration of the proposed method's advantage over a widely-used standard feature set.

- **Evaluation on two independent, clinically-sourced databases**: The paper uses the Italian Parkinson's Voice and Speech dataset (168 PD, 152 HC) and the Minsk2019 ALS database (105 ALS, 106 HC), covering two distinct neurodegenerative disorders from different cohorts, which supports generalizability beyond a single clinical site.

- **Theoretical motivation via form-invariance**: Section 3.1.1 provides a mathematical derivation showing that CQT's window function depends on both time and frequency (eqs. 10–12), satisfying the form-invariance condition that STFT cannot satisfy with stable filters. This provides a principled, physics-grounded rationale for why CQCC might be better suited for capturing quasi-periodic vocal pathology signals than fixed-resolution MFCC.

- **LDA visualization corroborating class separability**: Figure 3 shows that CQCC features produce tighter and more distinct LDA-projected clusters among ALS, PD, and healthy classes compared to MFCC, providing visual support for the quantitative accuracy differences.

## Weaknesses

### Major

- **Underspecified train/test split — risk of within-subject data leakage**: The paper states (Section 4.1) that "for training and testing, we used 80% and 20% of the data" but never specifies whether this split was performed at the *patient* level or the *recording* level. Since each patient contributes multiple sustained vowel recordings, a recording-level split would place recordings from the same patient in both training and test sets, artificially inflating accuracy via within-subject correlation. The reported 99% accuracy (CQCC+RF, Table 4) is unusually high for cross-subject pathological speech classification, making this omission consequential. Without this detail, the paper's central quantitative claims cannot be trusted. This is the single most important issue the authors must resolve.

### Minor

- **Unequal feature dimensionality in comparison**: CQCC uses 20 coefficients while MFCC uses 13 (Section 4.3). This is an asymmetric comparison — extra coefficients provide more information capacity regardless of the feature type. The authors should either match the dimensionality (e.g., compare 20-vs-20 or ablate CQCC to 13) or provide justification for why 20 vs. 13 is methodologically sound.

- **Only classification accuracy reported; no metrics robust to imbalance**: The paper relies solely on accuracy (Section 4.2: "Evaluation Metrics: Performance of all systems is evaluated using % classification accuracy"). For datasets with class imbalance (addressed via SMOTE rather than inherent balance), accuracy can be misleading. Missing F1-score, AUC, sensitivity, and specificity make it impossible to assess whether improvements are meaningful across all classes.

- **Databases D1/D2/D3 not clearly defined**: The paper introduces D2 for binary classification (Section 5.2.1) and D1/D3 for multi-class tasks (Section 5.2.2), but never specifies their exact composition — which source database(s) each comprises, which classes, or what distinguishes D1 from D3. Table 5 and Table 6 report results without sufficient context to understand what task is being evaluated. This undermines reproducibility.

- **Form-invariance claim is not empirically validated**: The abstract and conclusion assert that CQCC's effectiveness "is underpinned by the form-invariance property," but no experiment isolates whether form-invariance (vs. other CQT characteristics like geometric frequency spacing, variable window length, or simply having more coefficients) drives the performance difference. The theoretical derivation is sound but remains disconnected from the empirical evidence.

- **Overstated novelty claim**: The paper states "this is the first study of its kind on sustained vowel sounds for multi neurodegenerative disorder classification and analysis" (Section 2), yet it cites Suhas et al. (2020), which performs exactly this task (PD/ALS/HC classification on vowel sounds using Mel-spectrograms). The genuine contribution — applying CQCC to ND classification — is incremental and valid, but the framing as "first" is inaccurate.

- **Key CQCC extraction hyperparameters unreported**: The paper defines the number of bins per octave \(B\) and quality factor \(P\) mathematically (eqs. 5–6) but never states their experimental values. Similarly, the resampling method in Algorithm 1 is unspecified ("resample" — linear interpolation? spline?). These gaps prevent reproduction.

- **No cross-validation**: The evaluation uses a single 80/20 split with no cross-validation (k-fold or LOO). Given the relatively small dataset sizes, this increases variance in the reported results and makes them less reliable.

### Trivial

- **Classifier hyperparameters fixed without justification**: RF uses 100 estimators (random state 42) and SVM uses RBF kernel with C=1, with no tuning or justification for these choices. While not fatal, this weakens the claim of optimal performance.
- **Spectrographic analysis (Section 5.1) is qualitative and provides no quantitative support** for the classification results; it functions as descriptive background rather than evidence.

## Nice-to-Haves

- Report results on the original (non-SMOTE) distribution alongside SMOTE-balanced results to demonstrate robustness.
- Include standard metrics robust to imbalance: F1-score, AUC, sensitivity/specificity.
- Match dimensionality between CQCC and MFCC, or ablate the number of CQCC coefficients to show performance is not simply from extra dimensions.
- Provide controlled experiments isolating the form-invariance property (e.g., compare CQCC against CQT without DCT, or MFCC with logarithmically-spaced filterbanks, or resampled CQT features).
- Report statistical significance (e.g., McNemar's test or paired bootstrap) for claimed improvements.
- Discuss potential confounds (age, gender, disease severity, recording conditions) that are known to affect vocal features in PD and ALS.

## Removed Points

**These points are flagged to be removed; treat them with caution:**
- *"The introduction mixes general health statistics with technical motivation in a disjointed way"* — Removed as a subjective stylistic nitpick that does not affect the paper's technical validity.
- *"Literature coverage is thin"* — Removed per the instruction not to mention missing related works, as I cannot independently verify their existence.
- *"The CQT/CQCC derivation is largely copied from earlier work without sufficient adaptation"* — Removed because the paper cites the original sources (Brown 1991, Todisco et al. 2017, Patil et al. 2023) and presents these derivations for context when applying them to a new domain, which is standard practice.
- *"No end-to-end deep learning baseline"* — Removed as scope creep; the paper explicitly uses shallow classifiers with handcrafted features, which is a legitimate methodological choice.
- *"Competing time-frequency representations (wavelet, spectrogram CNNs) not included"* — Removed as scope creep; the paper compares against standard baselines (MFCC, Jitter, Shimmer, Teager Energy) and adding more is a nice-to-have, not a flaw.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a tension not explored by the paper itself: the form-invariance property is presented as a *theoretical* advantage of CQT over STFT, but the paper's experimental design compares CQCC (a full cepstral feature set) against MFCC (a different full cepstral feature set), so the claimed advantage is confounded with many other differences (number of coefficients, frequency spacing, window length, the DCT pipeline). Neither reviewer resolved this confounding — they correctly identify it but do not propose a clean experimental design for isolating form-invariance independently of the other CQT-specific properties. The most actionable insight from the merge is that the patient-level split question dominates all other concerns and must be clarified before any other weakness warrants significant rebuttal attention.

## Suggestions

1. **Clarify the train/test split immediately.** State explicitly — in a single sentence — whether splitting was per-patient or per-recording. If per-patient, report the number of unique subjects in train and test. If per-recording, re-run all experiments with a patient-level split and report the corrected results. This single change determines whether the paper's claims are valid or invalid.

2. **Match feature dimensionality** between CQCC and MFCC, or add an ablation showing that CQCC's advantage persists when both use the same number of coefficients.

3. **Report F1-score, sensitivity, and specificity** alongside accuracy for all tables to address the class imbalance concern.

4. **Clearly define D1, D2, D3** — state their exact database composition (which source, which classes, how many subjects) in the experimental setup, not just in passing during the results section.

5. **Tone down novelty claims.** Acknowledge Suhas et al. (2020) as prior work on multi-class ND classification using sustained vowels, and frame the contribution as *applying CQCC to this domain for the first time* rather than "first study of its kind."
