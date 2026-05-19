- Decision: Reject
- Avg Score: 5.75
- Scores: 8, 6, 3, 6
Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper introduces a new task: decoding whether a reader is engaged in ordinary reading or information seeking from their eye movements over a single paragraph. Using the large-scale OneStop dataset (360 participants, 19,438 trials), the authors systematically evaluate 10 state-of-the-art models across three generalization regimes (New Item, New Participant, New Item & Participant) and introduce a Logistic Ensemble that modestly outperforms individual models. An error analysis leveraging rich textual annotations (critical spans, paragraph position, question difficulty) identifies reading time before/after the critical span as the strongest predictor of classification difficulty.

## Strengths

- **First large-scale benchmark for reading-goal decoding from eye movements**: Using 360 participants and 19,438 trials (Section 4.1), this work goes substantially beyond prior predictive approaches (e.g., Hollenstein et al., 2023, with 18 participants and artificial annotation tasks). The scale allows meaningful evaluation of generalization.

- **Systematic evaluation across three ecologically motivated generalization regimes**: The New Item, New Participant, and combined regimes (Section 4.2, Table 1) cleanly separate different forms of generalization. The fact that all models struggle in the hardest (New Item & Participant) regime while achieving higher accuracy in New Item is informative about the nature of the task.

- **Ensemble model with complementary signal**: The Logistic Ensemble (Section 5.1) improves over the best single model in every regime and is the only model statistically better than the reading-time baseline in the hardest (New Item & Participant) regime. The Cohen's Kappa agreement analysis supports the claim that different models capture complementary information.

- **Interpretable error analysis using rich annotations**: The mixed-effects analysis (Section 6, Figure 3) leverages OneStop's unique annotation structure (critical spans, paragraph position, question difficulty) to identify interpretable factors driving task difficulty, going beyond mere accuracy reporting.

## Weaknesses

### Fatal
None.

### Major

- **Between-subjects design confound undermines interpretation of the strongest results.** The OneStop dataset uses a between-subjects design: each participant read all 54 paragraphs under a single reading goal (Section 4.1, line 120–122). Consequently, in the New Item evaluation regime — which produces the highest accuracies (74.7% for RoBERTa-Eye-F, 77.3% for the ensemble) — the model has seen multiple prior trials from the same participant, all with the same label. The model could therefore achieve high accuracy partly by learning to identify the participant from their eye-movement signature and predicting that participant's assigned label, a shortcut unrelated to decoding the reading goal. The authors acknowledge this in a single paragraph (line 212–213: "it could alternatively reflect… an ability of fixation based models to learn participant specific reading behavior… an ability that is not directly pertinent to the task at hand") but do not quantify or control for it. The New Participant regime avoids this confound and yields substantially lower accuracies (~63–65%). Given that the paper's claims emphasize the success of reading-goal decoding, this confound means the headline New Item results cannot be cleanly attributed to goal decoding. The paper would be substantially strengthened by (a) a control experiment (e.g., training a model to predict participant identity from eye movements to quantify how much signal is available for this shortcut) and (b) reframing the New Participant regime as the primary evidence for goal decoding.

- **Error analysis mixes confounded and clean trials, making interpretation ambiguous.** The error analysis in Section 6 (Figure 3) pools trials across all evaluation regimes, including New Item trials where correctness may partly reflect participant identifiability rather than goal-decoding difficulty. While the model includes `(1 | evaluation regime)` as a random effect, this only adjusts for mean differences across regimes — it does not address the possibility that the relationships between features (e.g., reading time before/after critical span) and correctness differ by regime. The analysis should be re-run separately on the New Participant regime (which is confound-free) to provide a clean interpretation. As presented, the error analysis is valuable but its feature coefficients may conflate two distinct phenomena.

### Minor

- **The reading-time baseline is a weak primary comparator.** The reading-time-per-word baseline (Section 4.3) is a single scalar feature, while the eye-movement models use hundreds or thousands of features. The logistic regression with global features (which the paper already includes as a model) provides a more informative baseline, as it already outperforms the reading-time baseline in the New Item regime (62.4% vs. 59.0%). The reading-time baseline is useful as a sanity check, but the paper should present the logistic regression as the primary benchmark for evaluating the value of richer eye-movement representations.

- **The between-subjects confound is not mentioned in the Discussion.** The Discussion (Section 9, lines 300–304) acknowledges room for improvement in the New Participant regime and other limitations, but does not revisit the confound that affects the interpretation of the New Item results. This should be explicitly discussed.

- **Typo in the ensemble's statistical test formula.** The R formula in the Figure 2 caption (line 235) reads `(paragraph ∣ parag)`, which appears to be a typo (likely intended as `(1 ∣ paragraph)` or similar). The main analysis in Table 1 uses `(model ∣ paragraph)`.

### Trivial
None.

## Nice-to-Haves

- A participant-identification control experiment (e.g., 360-way classification of participant identity from eye movements) to quantify the upper bound of the confound in the New Item regime.
- Per-participant accuracy breakdowns in the New Participant regime to show whether most participants are slightly above chance or a few are very high.
- Clarification of whether the ensemble's weights differ across folds or are stable.
- Discussion of whether a within-subject design (each participant reading under both goals on different passages) would be feasible for future work.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Reading time baseline is not a true 'eye-movement-free' baseline (requires knowing when the paragraph was finished)."** — Factually incorrect. The paper correctly states this baseline "does not require eye-tracking" (line 109). The paragraph finish time is obtained from a button press, not eye-tracking, so the paper's characterization is accurate. The valid concern about this being a weak comparator is retained in Minor weaknesses above.
- **"Description of each model is too brief to be informative or reproducible."** — The harsh critic themselves acknowledges this "is acceptable for a benchmark paper." It is not a substantive weakness.
- **"The confound is discussed only in a single sentence, then dismissed."** — The paper discusses the confound in approximately 3 sentences (lines 212–213). The characterization "dismissed" is the critic's framing; the paper does acknowledge the issue, though insufficiently. The substantive concern (lack of quantification/control) is retained in Major weaknesses above.
- Strength Finder claims about "rigorous statistical testing" and "comprehensive coverage of architectural strategies" — These are accurate observations but are already reflected in the Strengths section above at a more concrete level.

## Novel Insights

None beyond the paper's own contributions. The reviews do not introduce an observation about the work that the paper itself does not already articulate.

## Suggestions

1. **Quantify the participant-identification confound.** Train a model to predict participant identity (360-way classification) from the same eye-movement features. If such a model achieves high accuracy, the New Item reading-goal results must be interpreted with caution. This single experiment would substantially strengthen the paper.
2. **Re-run the error analysis on only New Participant trials.** This would provide a clean picture of which features genuinely affect goal-decoding difficulty, uncontaminated by the participant-identification shortcut.
3. **Reframe the presentation to emphasize New Participant results.** The abstract and introduction highlight the highest accuracies (74.7%, 77.3%) without caveat. Lead with the New Participant results (~63–65%) as the primary evidence for goal decoding, and present the New Item results with explicit discussion of the confound.
4. **Promote the logistic regression (global features) to the primary baseline.** It is a stronger and more informative comparator than the reading-time scalar, and it already exists in the paper.
