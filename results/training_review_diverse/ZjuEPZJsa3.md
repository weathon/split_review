Now I have all the information needed. Let me construct the final consolidated review.

## Summary

This paper introduces a new decoding task: given a single participant's eye movements over a paragraph, predict whether they were engaged in ordinary reading for comprehension or in information seeking. The authors adapt 10 existing models, evaluate them under three generalization regimes (New Item, New Participant, New Item & Participant), introduce a logistic ensemble, and conduct an error analysis using rich annotations from the OneStop dataset. The work addresses a well-motivated and understudied question, and the breadth of modeling is commendable.

## Strengths

- **First systematic evaluation of reading-goal decoding from eye movements.** The paper defines a clean task and provides a thorough benchmark with 10 models spanning diverse architectural strategies (global, word-level, fixation-level; eye-only and multimodal), establishing a solid foundation for future work.

- **Rigorous multi-level generalization evaluation.** The three regimes (New Item, New Participant, New Item & Participant) reveal different facets of model generalization and honestly expose where models struggle. The sharp drop from New Item (74.7%) to New Item & Participant (62.6%) is informative and the paper does not hide it.

- **Interpretable error analysis.** Using linear mixed-effects models with rich annotations (reading time before/within/after critical span, paragraph position, question difficulty, etc.), the analysis identifies that reading time before and after the critical span is the strongest predictor of classification difficulty. This provides mechanistic insight beyond raw accuracy and connects the modeling results to prior psycholinguistic findings.

- **Ensemble reveals complementary signal.** The logistic ensemble improves over the best single model in all regimes and is the only model that significantly beats the reading-time baseline in the hardest (New Item & Participant) regime (64.3% vs. 60.4%). This suggests that different models capture partially non-overlapping aspects of the eye-movement signal.

- **Appropriate statistical methodology.** Linear mixed-effects models with random effects for participants and paragraphs are used to account for the non-i.i.d. structure of the data, which is a best practice for repeated-measures designs.

## Weaknesses

### Fatal

None.

### Major

- **Between-subjects design creates a participant-identity confound that is not resolved.** Every participant read all 54 paragraphs under a single reading goal. In the New Item regime (where the model has seen the participant's other paragraphs during training), the model can learn idiosyncratic participant-specific patterns that correlate perfectly with the goal label — it need not learn about the reading goal per se. The paper acknowledges this possibility in one sentence (line 212: "it could alternatively reflect… an ability… to identify the participant") but does not quantify or control for it. The most telling evidence is the New Item & Participant regime, where this confound is removed: here, *no individual model significantly outperforms the simple Reading Time baseline* (Table 1: 62.6% for RoBERTa-Eye-F vs. 60.4%, n.s.), and only the ensemble reaches significance (64.3%). The gap between the inflated New Item results (up to 77.3%) and the cleaned results (~62–64%) strongly suggests that much of the reported accuracy derives from participant recognition rather than goal decoding.

- **The central claim is overstated relative to the strongest evidence.** The abstract and introduction state that "eye movements contain highly valuable signals for this task" and that "it is indeed possible to perform this task with relatively high accuracy rates." The 74.7–77.3% figures cited for this claim come from the New Item regime, which is precisely the regime most affected by the confound. The cleanest test (New Item & Participant) yields at best 64.3% — a 4% absolute improvement over a reading-time baseline that itself requires no eye-tracking. This is a modest result, and referring to "highly valuable signals" or "high accuracy rates" without prominently caveating the confound is misleading.

- **The error analysis is itself potentially confounded by participant identity.** The analysis (Section 6) uses predictions from RoBERTa-Eye-F, which achieves its best performance in the New Item regime — the regime most susceptible to participant recognition. The finding that "slower readers are easier to correctly classify as ordinary reading" could reflect that participants with slower overall reading styles are easier to identify, not that the model has learned about reading goals. Repeating this analysis on predictions from the New Item & Participant regime (where participant identity is unavailable) would be necessary to confirm the findings are about goal decoding.

- **No auxiliary experiment to test the participant-identity hypothesis.** Despite explicitly raising the possibility that models function as participant detectors, the paper does not run the most obvious control: can the same models predict *participant ID* from eye movements on this dataset? If they can (which is plausible given prior work on eye-movement-based user identification, cited in the ethics statement), the main results are plausibly driven by that confound. This is the single most important missing piece.

### Minor

- **No correction for multiple comparisons across model × regime tests.** The paper tests 10 models × 4 regimes = 40 comparisons against the Reading Time baseline (plus ensemble comparisons) without any multiple-testing correction. Some of the marginal significances (e.g., single-star entries) may not survive correction. (Bonferroni is used only in the error analysis, suggesting awareness of the issue.)

- **The confound affects the ensemble evaluation in the New Item regime.** The logistic ensemble is trained on validation-set predictions. Since the validation set and the New Item test set share participants, the ensemble could learn to weight models that serve as participant detectors. This concern does not apply to the New Item & Participant regime (where all participants are unseen), which is the regime where the ensemble's result is most important, but it complicates interpretation of the New Item ensemble result (77.3%).

### Trivial

None.

## Nice-to-Haves

- **Feature importance analysis for the logistic ensemble:** Which individual models contribute most to the ensemble? This could reveal whether fixation-based models capture genuinely different signal from word-based or global models, and whether the ensemble's advantage in the New Item & Participant regime comes from combining models with complementary weaknesses.

- **Within-participant analysis:** If the dataset allowed it (e.g., a subset of participants who read under both goals), a within-subject analysis would completely eliminate the participant-identity confound.

## Removed Points

- **"No ROC/AUC for the ensemble"** — The paper includes ROC curves and AUC results in the appendix (line 212), so this criticism is factually incorrect.
- **"Discussion of limitations does not address the between-subjects confound"** — The paper does address this confound in Section 5 (line 212), though not in the Discussion section. The substance of this concern is already covered by the major weaknesses above.
- **"Missing related works"** — Removed per instructions (no external sources to confirm).
- **Formatting/typo nitpicks from reviews** — Removed per instructions (parser artifacts).

## Novel Insights

The reviews surface a genuinely insightful point that goes beyond the paper's own analysis: the between-subjects confound does not just weaken the New Item results — it also potentially invalidates the error analysis, because the features found to correlate with prediction accuracy (e.g., reading time before/after critical span) may simply be features that help identify the participant. The reviewers' suggestion to run the error analysis on the New Item & Participant regime predictions is a concrete way to separate goal-relevant patterns from participant-identification artifacts. This reframing — that the paper's interpretable findings may themselves be confounded — is a more serious concern than the paper's own acknowledgement suggests.

## Suggestions

1. **Run a participant-identification control experiment.** Can the same models predict which participant generated each trial? If yes, the main results must be re-analyzed conditioning on participant identity, and the central claims must be substantially tempered.

2. **Re-center the New Item & Participant regime as the primary evidence.** The ensemble's 64.3% (significant vs. baseline) is the cleanest result. Frame the paper around this finding and discuss the other regimes with explicit caveats about the confound.

3. **Repeat the error analysis using predictions from the New Item & Participant regime** to ensure the identified features reflect goal-relevant patterns, not participant-identification cues.

4. **Apply multiple-testing correction** to the 40+ model × regime comparisons in Table 1, or at minimum report which results survive correction.

## Score and Decision

The paper tackles a novel and well-motivated task, and the breadth of modeling, rigorous evaluation protocol, and interpretable error analysis are genuine strengths. However, the between-subjects design creates a structural confound between reading goal and participant identity that undermines the primary claim. The paper's own strongest evidence comes from the New Item & Participant regime, where no individual model significantly beats a simple reading-time baseline and the ensemble achieves only 64.3%. The abstract and introduction's framing of "highly valuable signals" and "high accuracy rates" is not supported by the cleanest available evidence. The confound must be addressed and the claims substantially tempered before the paper can make a reliable contribution.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>