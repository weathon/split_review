## Summary

This paper introduces a new decoding task: given a single trial of eye movements over a paragraph, predict whether the reader was engaged in *ordinary reading* or *information seeking*. Using the OneStop dataset (360 participants, ~19k trials), the authors adapt 10 prior models spanning different architectural strategies and introduce a logistic ensemble. They evaluate three generalization regimes (New Item, New Participant, Both) and find that the ensemble significantly outperforms the reading-time baseline in all regimes, including the hardest (New Item & Participant: 64.3% vs. 60.4%). An error analysis leveraging critical-span annotations reveals interpretable factors of task difficulty.

## Strengths

- **First systematic formulation and evaluation of the reading-goal decoding task.** Prior work was limited to descriptive group-level analyses (Hahn et al. 2023, Shubi et al. 2023); this is the first paper to demonstrate automatic per-trial classification. The three-way generalization split (New Item / New Participant / Both) is a principled design that cleanly separates different sources of generalization and reveals the between-subjects confound rather than hiding it.

- **Large-scale, ecologically valid dataset and diverse model suite.** The OneStop dataset (360 participants, 30 real articles, manually annotated critical spans) is substantially larger and more naturalistic than prior benchmarks (e.g., ZuCo: 18 participants, artificial sentence-level annotation tasks). The paper applies 10 models covering global, word-level, fixation-level, and cross-attention architectures, with a Cohen's κ analysis demonstrating moderate complementarity across models.

- **Logistic ensemble achieves statistically significant gains in the hardest regime.** The ensemble is the only model that significantly beats the reading-time baseline in the New Item & Participant regime (64.3% vs. 60.4%, p < 0.05), where no single model reaches significance. This demonstrates genuine complementary signal across models.

- **Interpretable error analysis grounded in psycholinguistic findings.** Using a mixed-effects model on trial features (reading time before/after critical span, critical span length, paragraph position), the analysis reveals that the most important predictors of classification difficulty are reading time in critical-span-adjacent regions, aligning with prior work on information-seeking behavior. This goes beyond accuracy reporting to provide qualitative insights about the task itself.

## Weaknesses

### Fatal

None.

### Major

- **Between-subjects design confounds the headline New Item results with participant identity.** Every participant contributes trials under only one reading goal. In the New Item regime, the model sees other trials from the same participant during training — all sharing the same label. High accuracy (74.7% for RoBERTa-Eye-F) can therefore be driven by learning to identify the participant rather than decoding reading goals. The paper acknowledges this confound (lines 212–213: "it could alternatively reflect, at least in part, an ability...to identify the participant"), but the 74.7% result is still presented prominently and feeds into the overall "All" aggregate (68.5%), which inflates the claimed performance. The sharp performance drop from New Item (74.7%) to New Participant (63.1%) confirms that a substantial fraction of the signal in New Item is identity-driven. A control experiment — e.g., training a classifier on participant-level features to predict the majority label, or testing with randomized labels preserving the between-subjects structure — is needed to quantify how much of the New Item performance is genuine goal decoding vs. participant identification.

- **The ensemble evaluation lacks basic baselines.** The Logistic Ensemble (a logistic regression on the 10 models' probability outputs, trained on the validation set) is not compared against simple aggregation strategies such as averaging the 10 models' probabilities or majority voting. Without these baselines, it is unclear whether the ensemble gains are due to genuinely complementary signal or to overfitting the validation set. This is fixable but needs to be addressed to validate the ensemble claim.

### Minor

- **Gains over the reading-time baseline in non-confounded regimes are modest.** In the New Participant regime, the best single model reaches 63.2% vs. 58.9% baseline — a 4.3 pp gain. In the New Item & Participant regime, no single model significantly beats the baseline; only the ensemble does (64.3% vs. 60.4%, ~3.9 pp). While statistically significant, these improvements are small in practical terms. The abstract's claim that "eye movements contain highly valuable signals" overstates the effect size relative to what the clean (non-confounded) evaluations actually show.

- **No variance or confidence intervals reported across folds.** Table 1 reports accuracy point estimates without standard deviations, inter-quartile ranges, or any measure of variance across the 10 cross-validation folds. This makes it difficult to assess the stability of the reported numbers, especially for models with close margins.

- **Error analysis uses the model most confounded with participant identity (RoBERTa-Eye-F).** The error analysis (Section 6) examines which trial features predict correct classification by RoBERTa-Eye-F — exactly the model most confounded with identity. If that model's predictions partly reflect participant identity, the features associated with "difficulty" may also be confounded. Repeating the analysis with the best New Participant model (RoBERTa-Eye-W) would provide a cleaner picture of genuinely task-relevant difficulty.

- **Between-subjects confound is not flagged in the Introduction or Task description.** The confound and its consequences are only discussed in the Results section (lines 212–213). Readers encountering the 74.7% result in the abstract or the task formulation in Section 2 have no warning that the most favorable evaluation regime is structurally incapable of disentangling goal decoding from participant identification. This should be stated upfront.

### Trivial

- The mixed-effects model in the error analysis uses simplified random intercepts due to convergence issues (noted in a footnote, line 280), but the stability of the reported coefficient estimates under this simplification is not examined.

- The error analysis reports coefficient magnitudes and p-values but no confidence intervals around the point estimates.

## Nice-to-Haves

- A within-subject analysis is impossible with the current dataset (each participant has only one label), but the paper could more explicitly discuss the need for a within-subject data collection as the definitive test of goal decoding, rather than burying this in future work.

- A human-upper-bound calibration: can a human judge classify a trial correctly given only the scanpath (without the text)?

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The coefficients in the error analysis lack clarity on effect sizes — not standardized betas"** — REMOVED as factually incorrect. The paper explicitly states (line 280): "we normalize each feature to be a z-score (zero mean and unit variance)" and the figure caption says "Predictors are z-normalized." The coefficients ARE standardized betas. The point about missing confidence intervals is kept (in Trivial).

- **"Critical modeling details deferred to appendix"** — REMOVED per policy: appendix content exists in the original submission and is stripped by the parser. The level of main-text detail appears commensurate with prior work in this area.

- **"Missing related works"** — REMOVED per policy not to hypothesize about missing references.

- **Strength Finder: generic/superficial strengths** — None of the Strength Finder's listed strengths are generic; all are specific and evidence-backed. No removals needed.

## Novel Insights

None beyond the paper's own contributions. The most notable emergent insight from the reviews is a methodological one: the three-way generalization split (New Item / New Participant / Both) serves as an implicit diagnostic for confounds. The sharp accuracy drop between New Item (74.7%) and New Participant (63.1%) immediately reveals that participant identity is a strong alternative explanation — making this evaluation design a template for future work on biometric decoding tasks where participant identity and label may be correlated.

## Suggestions

1. **Add critical control experiments.** Run a participant-identity baseline (train a classifier to predict reading goal from participant-level features alone) and a label-permutation test (randomize labels while preserving between-subjects structure) to bound how much of the New Item result is identity-driven.

2. **Add ensemble baselines.** Compare the Logistic Ensemble against simple averaging and majority voting of the 10 model outputs. If the logistic regression does not significantly beat these, the complementarity claim is weak.

3. **Report variance across folds.** Add standard deviations or bootstrapped confidence intervals to Table 1.

4. **Recalibrate the claims.** The abstract and conclusion should qualifiy "highly valuable signals" by explicitly noting the confound and the modest effect sizes in the non-confounded regimes. Present the ensemble's New Item & Participant result as the cleanest evidence.

5. **Repeat the error analysis with the best New Participant model** (RoBERTa-Eye-W) to verify that the same features predict difficulty in a non-confounded setting.

6. **Flag the confound upfront** — in the Introduction or Task description — so readers are aware before encountering the headline results.

## Score and Decision

**Originality:** 7/10 — The task formulation is genuinely novel; prior work only showed average differences, not per-trial decoding.

**Importance of question:** 8/10 — Reading goal decoding is an understudied problem with practical implications for adaptive reading interfaces and cognitive diagnostics.

**Claims supported:** 5/10 — The main claim is partially supported but overstated; the confound weakens the headline results substantially.

**Soundness of experiments:** 6/10 — The evaluation framework is principled and the statistical tests are appropriate, but missing control experiments and ensemble baselines are significant gaps.

**Clarity of writing:** 7/10 — Generally clear and well-structured; the confound could be disclosed earlier.

**Value to community:** 7/10 — The task, evaluation framework, model comparison, and error analysis provide a useful starting point for future work.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>