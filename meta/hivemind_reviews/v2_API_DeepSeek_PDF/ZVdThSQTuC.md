## Summary
# Final Review Report

## Summary

This paper introduces a novel EEG dataset for semantic text relevance, comprising 23,270 time-locked word-level recordings from 15 participants who read Wikipedia documents relevant or irrelevant to self-selected topics. The dataset uses a controlled RSVP paradigm with fixed-duration word presentation (700ms) to minimize oculomotor confounds. The authors provide benchmark experiments with five models (EEGNet, LDA, LR, LSTM, UERCM) on two tasks (word relevance and sentence relevance classification) under two evaluation paradigms (cross-subject and within-subject).

**Core contribution claims (C1-C3):**
- **C1**: First publicly available EEG dataset specifically designed for semantic text relevance with time-locked word presentation.
- **C2**: Rigorously controlled experimental design (RSVP, interleaved topics, self-selected relevance) that minimizes confounding factors.
- **C3**: Comprehensive benchmark results with five models across two tasks and two evaluation paradigms, establishing baselines.

**Key strengths:** Well-motivated research question, careful experimental design for EEG recording, open data/code release, informative comparison with existing datasets (Table 1), and rigorous ERP analysis validating the relevance effect.

**Major weaknesses:** (1) Conceptual disconnect between subjective participant relevance and externally-annotated ground truth; (2) Unsubstantiated SOTA claims; (3) Near-perfect within-subject sentence-level scores that may reflect temporal confounds rather than relevance decoding; (4) Small homogeneous participant pool (N=15) limiting cross-subject generalization claims; (5) Missing key experimental details and control analyses.

**Novelty verdict (deferred):** Due to Retrieval-Disabled Mode in this run, external literature verification was not performed. Novelty conclusions are marked as deferred and require manual verification against prior works, particularly Eugster et al. (2014, 2016) and Ye et al. (2022).

## Strengths
**S1. Well-motivated research question.** The paper addresses a genuine gap: the lack of EEG datasets specifically designed to capture semantic text relevance through controlled, time-locked word presentation. This fills a meaningful niche between naturalistic reading datasets and fully artificial psycholinguistic experiments.

**S2. Rigorous experimental design.** The RSVP paradigm with fixed 700ms word duration, central fixation, luminance masking, and interleaved topic alternation demonstrates careful attention to EEG confounds. The self-selected topic design enhances ecological validity compared to forced-relevance paradigms.

**S3. Comprehensive dataset documentation.** The dataset size (23,270 word-level recordings) is substantial for a 15-participant EEG study. The authors provide detailed metadata, a datasheet following Gebru et al. (2018), open code/data release (upon acceptance), and clear documentation of preprocessing steps.

**S4. Informative comparison with existing datasets.** Table 1 provides a useful structured comparison of publicly available neurophysiological language-processing datasets across key dimensions (modality, participants, stimulus type, time-locking, task specificity), helping readers understand the positioning of the new dataset.

**S5. Rigorous ERP validation.** The four-factor repeated-measures ANOVA with robust main effects of relevance (all F-values > 30, p < 0.001) provides strong electrophysiological evidence that the experimental manipulation successfully modulated brain responses, validating the dataset's utility.

**S6. Multiple benchmark baselines.** Testing five models (from simple LDA/LR to deep EEGNet/LSTM/UERCM) across two tasks and two evaluation paradigms provides a useful starting point for future work, especially the within-subject vs. cross-subject comparison.

**S7. Transparent ethical considerations.** The paper includes a dedicated ethics section addressing EEG privacy risks and consent procedures, which is increasingly important for neurophysiological datasets.

## Weaknesses
**W1. Conceptual disconnect: subjective relevance vs. externally-annotated ground truth (Critical).** The paper's narrative emphasizes self-selected topic relevance as a subjective, user-specific construct. However, word-level ground truth is determined by three external annotators' majority vote, not by the participant. This means the word-level task predicts "topic relevance" (annotator consensus) rather than "personal relevance" (participant's own judgment). This disconnect undermines the ecological validity narrative and likely contributes to low cross-subject AUC scores (0.61-0.65).

**W2. Unsupported SOTA claims (Major).** The paper claims "state-of-the-art results (within-subject) when compared to previously reported results (Eugster et al., 2014; 2016)" without providing any direct comparison of experimental conditions, dataset sizes, or task definitions. This claim is unverifiable and potentially misleading. See Page 8 - Word Relevance Classification Task Results paragraph.

**W3. Suspiciously high within-subject sentence-level scores (Major).** LSTM achieves AUC 0.97 and Precision 0.94 for within-subject sentence classification. The jump from cross-subject (AUC 0.79) to within-subject (AUC 0.97) far exceeds what would be expected from fine-tuning alone. This pattern (also seen in UERCM: 0.67 to 0.92) suggests that sequential models may exploit session-level confounds (fatigue, attention fluctuations, electrode drift) rather than semantic relevance signals.

**W4. Small homogeneous participant pool (Major).** With only 15 participants, all right-handed, highly fluent in English, university-affiliated, and self-reported good mental health, the dataset's cross-subject generalization claims are severely limited. The cross-subject AUC scores (0.61-0.65, barely above chance) confirm this limitation.

**W5. Temporal feature window extends beyond stimulus offset (Major).** The 250-950ms feature window extends 250ms beyond the 700ms word presentation. The authors do not explain what stimulus is present during this 700-950ms period, raising concerns that features may capture post-word processes rather than target-word relevance.

**W6. Missing hyperparameter optimization and model selection details (Minor).** The authors state they used default parameters for all models, which is a reasonable baseline choice. However, no analysis is provided on how parameter choices affect results, limiting reproducibility guidance.

**W7. Potential topic imbalance confound (Minor).** Each participant selects one of two randomly-paired topics. Over the eight reading tasks, some topics will be selected more frequently than others (as confirmed in Appendix C.3). If some topics produce stronger neural responses than others, the label "relevance" may be partially confounded with topic-specific EEG patterns.

**W8. Conclusion overclaims downstream applications (Minor).** The conclusion lists IR, recommender systems, and user engagement as enabled applications, but none were tested. This overstates practical readiness.

## Key Issues
### Issue 1 (Critical): External annotators define "relevance," not participants
**Evidence**: Page 5 - Section 4.2, lines 84-98. Three external annotators determine word-level relevance via majority vote.
**Root cause**: The paper conflates "topic relevance" (objective word-to-topic association, assessed by annotators) with "personal relevance" (subjective, participant-specific experience, which is what the task design manipulates).
**Scientific impact**: The core claim that the dataset captures "semantic text relevance" as experienced by the reader is only partially true at the word level. The benchmark task actually predicts annotator-consensus topical relevance, not the participant's own relevance judgment.
**Required action**: (1) Explicitly acknowledge this distinction. (2) Add analysis correlating external labels with participant's self-reported interestingness/familiarity (collected in the study). (3) Consider adding a participant-self-annotation condition in future data collection.

### Issue 2 (Major): Unsubstantiated SOTA claim
**Evidence**: Page 8 - Section 5.4, lines 88-89. "We achieve state-of-the-art results (within-subject) when compared to the previously reported results (Eugster et al., 2014; 2016)."
**Root cause**: No direct comparison of task, metrics, dataset size, or experimental conditions is provided. The claim relies on a vague citation without evidence.
**Scientific impact**: May mislead readers about the performance level required for relevance-from-EEG decoding. Reduces credibility if challenged.
**Required action**: Replace with bounded comparative statement, or add a dedicated comparison table.

### Issue 3 (Major): Suspiciously high within-subject sentence scores
**Evidence**: Page 9 - Table 3. LSTM within-subject sentence AUC = 0.97 (SD 0.02), UERCM = 0.92 (SD 0.04). Cross-subject versions are much lower (0.79 and 0.67 respectively).
**Root cause**: The 0.18-0.25 AUC gain from cross-subject to within-subject for sequential models (LSTM, UERCM) far exceeds what fine-tuning alone should provide. This pattern is not seen for non-sequential models (LDA, LR), which perform worse in within-subject.
**Scientific impact**: Suggests that sequential models may be leveraging within-session temporal structure (fatigue, attention cycles, electrode drift) rather than genuine relevance signals. This would invalidate the claim that relevance is "successfully decoded."
**Required action**: Add a label-shuffling control experiment. Report per-participant scores. Discuss temporal confounds explicitly.

### Issue 4 (Major): Temporal window extends beyond stimulus offset without justification
**Evidence**: Page 7 - Section 5.3, lines 95-107. Features use 250-950ms window while words are shown for 700ms.
**Root cause**: The 700-950ms segment is within the inter-word interval. Without clarifying the screen state during this period, features may capture irrelevant visual processing.
**Required action**: Clarify visual display timing after 700ms. Compare results with 250-700ms truncated features.

### Issue 5 (Major): Cross-subject generalization limited by small homogeneous sample
**Evidence**: Page 9 - Discussion, lines 89-103. 15 participants, all right-handed, fluent, university students. Cross-subject AUC = 0.61-0.65.
**Root cause**: The sample size argument (citing Brysbaert 2019) applies to within-subject experimental designs, not cross-subject ML generalization.
**Required action**: Separate the sample size discussion into within-subject (adequate) and cross-subject (limited) components. Add diversity recruitment plans for future work.

## Actionable Suggestions
### Suggestion 1 (Must, High Impact): Reframe the narrative around the word-level annotation disconnect

**Problem**: The paper currently describes the word-level task as predicting "semantic relevance" without distinguishing between annotator-defined topical relevance and participant-defined personal relevance.

**Action**: Add a subsection titled "Relationship between external annotations and participant relevance" that:
- Explicitly states that word-level labels come from external annotator majority vote
- Reports the correlation between external labels and participants' self-reported interestingness/familiarity ratings (which were collected — see Page 4, lines 168-171)
- Discusses the implications of any mismatch for interpreting benchmark results

**Expected benefit**: Resolves the central conceptual tension and strengthens the paper's scientific honesty.

### Suggestion 2 (Must, High Impact): Add label-shuffling control for sentence-level within-subject results

**Problem**: The LSTM's AUC 0.97 for within-subject sentence classification is suspiciously high.

**Action**: Run a control experiment where sentence-level relevance labels are randomly permuted within each participant (preserving the same label distribution). Report the AUC of the LSTM and UERCM models on shuffled labels. If the shuffled AUC is substantially lower than 0.97 (as expected), this confirms genuine relevance decoding. If it remains high, this indicates temporal confounds.

**Expected benefit**: Directly addresses the validity concern about the near-perfect scores.

### Suggestion 3 (Must, High Impact): Replace SOTA claim with bounded comparison

**Problem**: The current SOTA claim is unsubstantiated.

**Action**: Replace "We achieve state-of-the-art results" with:
"Our within-subject results compare favorably with prior relevance-from-EEG studies (Eugster et al., 2014, 2016), though direct comparison is limited by differences in experimental paradigms. We provide these benchmarks to facilitate future comparisons on this dataset."

**Expected benefit**: Eliminates an unverifiable claim while preserving the value of the benchmark results.

### Suggestion 4 (Must, Medium Impact): Clarify temporal window and post-word stimulus

**Problem**: The 250-950ms window extends 250ms beyond the 700ms word presentation.

**Action**: (a) State explicitly what appears on screen at t=700ms to t=950ms (e.g., mask, next word, blank screen). (b) Report comparison of model performance using 250-700ms vs 250-950ms features.

**Expected benefit**: Ensures reproducibility and clarifies what neural processes the features capture.

### Suggestion 5 (Must, Medium Impact): Improve sample size discussion

**Problem**: Brysbaert (2019) citation conflates within-subject experimental power with cross-subject ML generalization.

**Action**: Restructure the Discussion paragraph to explicitly separate:
- Within-subject analysis: 15 participants provides sufficient per-subject trial count (>1500 words each)
- Cross-subject analysis: 15 homogeneous participants is limited; results should be interpreted as preliminary

**Expected benefit**: Prevents reviewers from rejecting the sample size argument as misapplied.

### Suggestion 6 (Should, Medium Impact): Add abstract with quantitative results

**Problem**: The current abstract does not report any performance numbers.

**Action**: Add key benchmark results: "Within-subject models achieve AUC up to 0.82 (word-level) and 0.97 (sentence-level), establishing baselines for future research on this dataset."

**Expected benefit**: Makes the abstract more informative and self-contained.

### Suggestion 7 (Should, Low Impact): Acknowledge sentence alternation carryover effects

**Problem**: The alternating sentence design may introduce context-switching confounds not discussed.

**Action**: Add a sentence in the Discussion acknowledging potential carryover effects and suggesting analysis of sentence position effects.

**Expected benefit**: Increases methodological transparency.

## Storyline Options + Writing Outlines
### Abstract Outline (Complete)

The abstract should follow a compact 5-sentence structure with key quantitative results:

**S1 (Problem & Domain):** "Electroencephalography (EEG) enables non-invasive measurement of brain activity during language processing, but existing datasets do not capture semantic text relevance through controlled word-level presentation."

**S2 (Gap):** "No publicly available EEG dataset combines time-locked word presentation with self-selected topic relevance, limiting research on neural correlates of relevance and brain-computer interfaces for information retrieval."

**S3 (Dataset Introduction):** "We release a dataset of 23,270 word-level EEG recordings (~700ms per word) from 15 participants who read Wikipedia documents relevant or irrelevant to self-selected topics."

**S4 (Key Results):** "Within-subject models achieve AUC up to 0.82 for word-level and 0.97 for sentence-level relevance classification, establishing baselines for future research."

**S5 (Impact):** "The dataset, code, and documentation are openly released to advance research on neural relevance processing, neuroadaptive systems, and brain-computer interfaces."

### Introduction Outline (Complete, 4 paragraphs)

**P1 (Motivation): Human relevance detection and the IR gap**
Role: Establish that humans rapidly assess relevance, but IR systems rely on behavioural signals rather than direct neural measures.
Transition: End with "An intriguing alternative is to infer relevance directly from the brain."
Key claim: Behavioural signals (clicks, dwell time) are indirect; brain signals offer a more direct measure of relevance.

**P2 (Prior EEG relevance work and its gap)**
Role: Review prior work on relevance from EEG — show that relevance responses are detectable, but existing datasets were not designed for this purpose.
Content: Pinkosova et al. (2020) showed graded relevance in brain signals; Hollenstein et al. (2021) used EEG to improve text representations; Ye et al. (2022) studied relevance in QA. However, none provide time-locked word-level EEG with self-selected topical relevance as the primary experimental variable.
Transition: End with specific gap statement.

**P3 (Our dataset and design)**
Role: Introduce the dataset — time-locked word presentation, self-selected topics, RSVP control, open release.
Content: Key design decisions and how they address confounds. Mention the 23,270 recordings, 15 participants, 30 topics.

**P4 (Benchmark experiments and contributions)**
Role: Preview the two tasks, two paradigms, five models. State contributions clearly.
Content: Word-level and sentence-level classification. Cross-subject and within-subject evaluation. Open code/data.
Contribution list should be explicit: (1) Novel dataset for time-locked semantic relevance, (2) Controlled experimental design, (3) Comprehensive benchmarks.

### Storyline Comparison

**Current storyline**: Broad cognition → IR behaviour → EEG relevance work → Gap → Dataset → Experiments.
**Weakness**: The transition from "cognition attends to relevance" to "IR uses behavioural signals" is abrupt. The gap is not clearly stated until the second paragraph.

**Proposed improved storyline (selected)**:
Big Picture (P1) → Prior EEG relevance gap (P2) → Our dataset design (P3) → Benchmarks + Contributions (P4)
**Why better**: Clearer logical flow, earlier focus on EEG (not general cognition), gap statement is explicit, and reader understands the dataset before seeing benchmark results.

### Alternative Storyline Candidates

**Candidate A (Application-driven):** Start with a BCI/IR application scenario, then introduce the dataset as an enabler. Better for interdisciplinary venues.

**Candidate B (Methodology-focused):** Start with EEG confounds in naturalistic reading → time-locked design as solution → dataset as validation. Better for psychophysiology venues.

## Priority Revision Plan
Ranked by severity and impact on paper validity.

| Priority | Issue | Effort | Impact | Action |
|----------|-------|--------|--------|--------|
| **P0** | Conceptual disconnect: external annotators as ground truth for subjective relevance | High | Validates core claim | Reframe narrative + add correlation analysis (Suggestion 1) |
| **P0** | Near-perfect within-subject sentence scores may reflect confounds | Medium | Threatens result validity | Add label-shuffling control (Suggestion 2) |
| **P1** | Unsubstantiated SOTA claim | Low | Credibility | Replace with bounded statement (Suggestion 3) |
| **P1** | Temporal window extends beyond stimulus offset | Low | Reproducibility | Clarify timing + compare truncation (Suggestion 4) |
| **P1** | Sample size defense conflates within/cross-subject | Low | Argument strength | Restructure discussion (Suggestion 5) |
| **P2** | Abstract lacks quantitative results | Low | Readability | Add key AUC numbers (Suggestion 6) |
| **P2** | Sentence alternation carryover not discussed | Low | Transparency | Add discussion sentence (Suggestion 7) |

### Revision Execution Order

**Phase 1 (Immediate — text revisions only, 1-2 days):**
1. Replace SOTA claim with bounded statement (Issue 2)
2. Reframe word-level annotation description (Issue 1)
3. Clarify temporal window and stimulus timing (Issue 4)
4. Restructure sample size discussion (Issue 5)

**Phase 2 (Experimental — control analyses, 1-2 weeks):**
5. Run label-shuffling control for sentence-level results (Issue 3)
6. Compare 250-700ms vs 250-950ms feature truncation (Issue 4)
7. Correlate external annotations with participant self-reports (Issue 1)

**Phase 3 (Polish — remaining improvements, 2-3 days):**
8. Update abstract with quantitative results
9. Add sentence alternation carryover discussion
10. Add proposed storyline improvements to introduction

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 | ERP validation: relevance modulates brain responses | 4-factor rm-ANOVA, 15 participants, 32 electrodes, 3 time bins | F-values, p-values | Main effect of relevance (F=72.83, p<.001); robust across bins | C2 (controlled design produces measurable relevance signal) | Post-hoc comparisons not fully reported; multiple comparisons not corrected |
| E2 | Word relevance classification (cross-subject) | 5 models, leave-one-participant-out CV | AUC, Precision, Recall | AUC 0.61-0.65 across models | C3 (baseline benchmarks) | Scores near chance; no significance testing against baseline |
| E3 | Word relevance classification (within-subject) | 5 models, 8-fold CV per participant | AUC, Precision, Recall | LSTM best (AUC 0.82); EEGNet 0.70 | C3 | No comparison with label-shuffled baseline |
| E4 | Sentence relevance classification (cross-subject) | 5 models, leave-one-participant-out | AUC, Precision, Recall | LSTM best (AUC 0.79); LDA 0.72 | C3 | LSTM precision SD 0.30 indicates instability |
| E5 | Sentence relevance classification (within-subject) | 5 models, 8-fold CV per participant | AUC, Precision, Recall | LSTM AUC 0.97; UERCM 0.92 | C3 | Suspiciously high; potential temporal confounds not addressed |

### Research-Theme Gap Diagnosis

**Gap 1: Annotator-participant relevance alignment.** The study collected participant ratings of interestingness and pre-knowledge (Section 3.3, lines 168-171) but never analyzes their correlation with external annotator labels. This is a missed opportunity that could validate (or invalidate) the ground truth labeling approach.

**Gap 2: Temporal confound control.** No experiment tests whether within-subject sentence-level results are robust to label permutation or temporal randomization. Without this control, the high AUC values cannot be confidently attributed to relevance decoding.

**Gap 3: Feature window sensitivity.** The choice of 250-950ms is not empirically justified versus shorter windows.

**Gap 4: Cross-subject generalization ceiling.** With cross-subject AUC at 0.61-0.65, it is unclear whether this reflects the difficulty of the task, insufficient data diversity, or suboptimal feature representation.

### Proposed Research Experiments

**P0 Experiment: Label-shuffling control for sentence-level within-subject results**
- Target Claim: C3 — that sentence relevance can be decoded from EEG
- Hypothesis: If the LSTM's AUC 0.97 reflects genuine relevance decoding, label-shuffled controls should yield AUC ~0.50
- Minimal Design: Permute sentence-level relevance labels within each participant (preserving label distribution); re-run LSTM and UERCM within-subject pipeline
- Controls/Baselines: Compare real-label AUC vs. shuffled AUC distribution (100 permutations)
- Metrics: AUC, accuracy gap between real and shuffled
- Success Criterion: Real AUC significantly higher (p<0.01, paired t-test) than shuffled AUC
- Estimated Cost/Time: Low — reuses existing code; ~2 hours computation
- Expected Gain: Resolves the most critical validity concern about the paper

**P1 Experiment: Feature window truncation comparison**
- Target Claim: C2/C3 — that 250-950ms features are appropriate
- Hypothesis: Relevant ERP components (P300, N400, P600) occur within the 250-700ms window; truncating to 250-700ms should not substantially reduce performance
- Minimal Design: Compare models (LSTM, EEGNet) with 250-700ms vs 250-950ms features
- Controls/Baselines: Same models, same hyperparameters, different window
- Metrics: AUC difference (delta)
- Success Criterion: Delta AUC < 0.03 between windows
- Estimated Cost/Time: Low — feature reshaping only; ~1 day
- Expected Gain: Clarifies whether post-word signals contribute to classification

**P1 Experiment: Annotator-participant agreement analysis**
- Target Claim: C1 — that the dataset captures "semantic text relevance"
- Hypothesis: External annotator labels correlate positively with participant self-reported interestingness and pre-knowledge
- Minimal Design: For each word, compare its external label (relevant/irrelevant) with the participant's ratings of the document's topic
- Controls/Baselines: Correlation coefficient against chance
- Metrics: Point-biserial correlation, Cohen's kappa
- Success Criterion: Significant positive correlation (p<0.05)
- Estimated Cost/Time: Low — data already collected; ~1 day analysis
- Expected Gain: Validates the ground truth approach; if correlation is weak, motivates major reframing

**P2 Experiment: Cross-subject generalization with data augmentation**
- Target Claim: C3 — cross-subject benchmarks
- Hypothesis: Cross-subject performance can be improved with domain adaptation or data augmentation
- Minimal Design: Compare baseline EEGNet with a simple domain-adversarial approach
- Metrics: AUC improvement over baseline
- Success Criterion: Improvement ≥ 0.05 AUC
- Estimated Cost/Time: Moderate — new implementation; ~1 week
- Expected Gain: Demonstrates whether the low cross-subject performance is fundamental or addressable

### ASCII Diagram — Experiment Upgrade Plan

```text
Phase 0 (P0, Critical): Label-Shuffling Control
  [Sentence within-subject results: LSTM AUC 0.97]
       -> [Shuffle labels per participant, 100 runs]
       -> [If shuffled AUC ~0.50: genuine decoding confirmed]
       -> [If shuffled AUC > 0.60: temporal confound present]
  Expected outcome: Evidence for or against validity of core classification claim

Phase 1 (P1, Important): Feature & Ground Truth Validation
  [P1a: Feature window 250-700ms vs 250-950ms comparison]
       -> [If delta < 0.03: current window is appropriate]
  [P1b: Annotator-participant label agreement]
       -> [If significant correlation: ground truth validated]
       -> [If weak correlation: major reframing needed]

Phase 2 (P2, Nice-to-have): Cross-subject Improvement
  [Domain adaptation for cross-subject decoding]
       -> [Target: improve AUC from ~0.64 to > 0.70]
       -> [If successful: dataset enables generalizable BCI]
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5 / 10**

*Rationale:* The paper presents a genuinely needed dataset with a careful experimental design and thorough ERP validation. However, several major weaknesses prevent a higher score:
- The conceptual disconnect between subjective relevance and externally-annotated ground truth (Critical Issue 1) undermines the core narrative
- The unvalidated SOTA claim (Major Issue 2) and suspiciously high within-subject sentence scores (Major Issue 3) raise validity concerns
- The small homogeneous sample and limited cross-subject performance limit practical impact
- Novelty cannot be fully assessed without external literature verification (Retrieval-Disabled Mode)

The paper's primary value is as a dataset contribution, but the current presentation overstates what has been demonstrated. Addressing the P0/P1 issues would substantially strengthen the paper.

**Post-Revision Target: [6.5, 7.5] / 10**

If the authors: (1) resolve the annotation disconnect through reframing and correlation analysis, (2) validate the within-subject sentence results with label-shuffling controls, (3) remove/qualify unsubstantiated claims, and (4) clarify temporal window choices — the paper would provide a solid, well-validated dataset contribution suitable for a datasets-and-benchmarks track at a major venue.