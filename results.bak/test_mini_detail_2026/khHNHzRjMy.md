Now I have all the information I need. Let me compile the final review.

**My round-1 bracket:** 3.5 to 7.5 (after reading the weak, middle, and strong band anchors).

**My round-2 bracket:** 4.5 to 6.0. Here's my reasoning:
- Clearly above SpEmoC (4.67, rejected) and LexSign (4.50, rejected) — EmoSign's annotation design is more novel and careful (Deaf native signers, fine-grained labels, open-ended cues).
- Comparable to MME-Emotion (5.00, accepted) — both have interesting contributions with validity concerns around annotation quality.
- Below EmotionHallucer (5.60, accepted) — that paper had more rigorous evaluation with 41 models and a clear benchmark protocol.
- Significantly below BANZ-FS (7.00) — which had much larger scale (35k vs. 200 instances).

Within this bracket, EmoSign sits around **5.0**. The core dataset contribution is genuinely novel and well-motivated, but the low inter-annotator agreement on several emotions and the lack of uncertainty quantification on a 200-clip benchmark are real concerns that prevent a higher score.

---

## Summary

This paper introduces EmoSign, a dataset of 200 ASL video clips annotated by 3 Deaf native signers with sentiment ratings (7-point scale), fine-grained intensity ratings for 10 emotions, and open-ended descriptions of emotion cues. The authors benchmark 4 multimodal LLMs across three conditions (video-only, caption-only, video+caption) on sentiment analysis, emotion classification, and emotion cue grounding. The results show that current models perform poorly on video-only inputs and exhibit a positive bias, improving substantially when text captions are available.

## Strengths

- **First dedicated emotion-labeled ASL dataset annotated by Deaf native signers.** EmoSign is the only ASL dataset where annotations for sentiment, emotion intensity, and emotion cue descriptions were provided by Deaf ASL native signers with professional interpretation experience. This directly addresses the limitation of prior work like FePh that used hearing annotators and binary labels (Table 1, Section 2).

- **Carefully designed three-condition ablation reveals meaningful limitations of current MLLMs.** The benchmark uses a controlled design (caption-only, video-only, video+caption) across four models, showing that all models perform poorly on video-only emotion recognition and improve substantially when captions are added. The positive bias finding (Section 5.1) and specific failure modes (e.g., models claiming they need audio, GPT-4o defaulting to "happiness" or "frustration") are diagnostic and support the paper's central thesis.

- **Open-ended descriptions of emotion cues provide a uniquely valuable qualitative resource.** The annotation pipeline collects free-text descriptions of specific emotion cues (e.g., furrowed brows, signing speed, head thrusts, mouth morphemes), summarized in Section 3.4. This goes beyond simple label-based datasets and enables the kind of fine-grained grounding analysis that the paper begins to explore in Section 5.3.

## Weaknesses

### Fatal

None.

### Major

- **Low inter-annotator agreement on 6 of 10 emotion categories undermines benchmark validity for those labels.** Krippendorff's alpha values reported in Table 2 include surprise_neg (0.119), disgust (0.166), frustration (0.330), sadness (0.333), fear (0.351), and anger (0.370) — all well below the 0.67 threshold generally considered the minimum for tentative conclusions. The paper uses majority-vote aggregation, but when three annotators disagree this heavily, the majority label may not represent a reliable signal. The downstream emotion classification benchmark (Table 4) treats these labels as ground truth without any caveat or separate treatment. The Limitations section (Section 6) does not mention this issue at all. This is the single most significant weakness in the paper. At minimum the authors should: (a) report benchmark results separately for high-agreement (alpha ≥ 0.5: sentiment, joy, excited, worry, surprise_pos) and low-agreement subsets, (b) provide per-annotator breakdowns so readers can assess disagreement patterns, and/or (c) acknowledge this directly as a limitation that tempers conclusions drawn from low-agreement categories.

- **The paper's claim about VADER-based selection creating a strongly bimodal sentiment distribution is acknowledged but its implications for the positive-bias finding are not discussed.** The paper selected the top-100 and bottom-100 VADER text sentiment scores, yielding only 5 neutral clips (Figure 2B). When the paper reports that models exhibit a "positive bias" in the video-only condition (Section 5.1), it attributes this to model training objectives (helpful, harmless, honest). But an alternative (or contributing) explanation is simply that the dataset contains many genuinely positive utterances, so defaulting to "positive" is a rational response to the skewed base rate. The paper should either control for this or explicitly discuss the confound.

### Minor

- **No confidence intervals or uncertainty quantification on benchmark results with a 200-clip dataset.** The emotion classification benchmark uses 140 single-expression clips across 11 labels (Table 4). Several classes may have only ~10-15 test samples, meaning a single misclassification can swing per-class accuracy by 7-10 percentage points. The absence of any bootstrapped confidence intervals or error bars makes it impossible to tell which performance differences between models or conditions are meaningful.

- **The emotion cue grounding analysis (Section 5.3) is illustrative but not systematic.** The paper analyzes one sample across four models and draws qualitative conclusions about model failures. While these observations are suggestive and align with the quantitative results, claims about specific failure patterns (e.g., "models construct explanations consistent with text sentiment rather than independently recognizing visual cues") would be substantially stronger with a systematic analysis — e.g., human ratings of model-generated cue descriptions, or a tally of how often each failure type occurs across the full dataset.

- **The comparison of inter-annotator agreement to MELD (Fleiss' kappa = 0.43) and IEMOCAP (Fleiss' kappa = 0.48) mixes different metrics.** Krippendorff's alpha and Fleiss' kappa are related but not directly comparable, and the comparison uses the average alpha (0.593), which is inflated by high-agreement labels like sentiment (0.738) and joy (0.699). The paper would be more informative if it reported agreement per-label separately and noted that Krippendorff's alpha and Fleiss' kappa are different measures.

### Trivial

None.

## Nice-to-Haves

- Add a cross-dataset control: evaluate models on a random (non-VADER-filtered) subset of ASLLRP to test whether the VADER selection drives the positive bias finding.
- For the emotion classification benchmark, report per-class sample counts alongside accuracy numbers so readers can gauge reliability.
- Provide per-annotator labels and a disagreement analysis — this could turn a weakness into an insight about systematic ambiguity in ASL emotion cues (e.g., distinguishing grammatical from affective facial expressions).
- Systematically count how often each model demonstrates "lack of understanding about sign language" (e.g., claiming audio is needed) across the dataset, rather than just reporting one example.

## Removed Points

These points were raised in the reviews but are removed from the main assessment for the following reasons:

- **"Missing quantitative comparison between FePh and EmoSign on overlapping emotion categories"** — Removed as scope creep. The paper already explains the key differences in annotation design (hearing vs. Deaf annotators, binary vs. fine-grained labels, facial-cropped vs. full-frame). A direct quantitative comparison would require re-annotating FePh, which is beyond the paper's stated scope.

- **"Claims about inspiring new architectures are overclaimed"** — Removed. The paper's statement "This work can inspire new architectures..." (Abstract) is a mild, aspirational future-looking remark, not a strong claim. It does not overstate the paper's contributions.

- **Strength: "Inter-annotator agreement is comparable to or better than established emotion recognition datasets"** — Removed because this conflicts with the verified weakness about low agreement on several emotion categories. The comparison uses different metrics (Krippendorff's alpha vs. Fleiss' kappa) and the average alpha (0.593) masks very low values for 6 of 10 emotions.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Address the label reliability issue head-on.** The most impactful change is to either (a) report benchmark results separately for emotions with alpha ≥ 0.5 vs. < 0.5, or (b) provide a per-annotator analysis showing whether model errors align with annotator disagreements. This would either strengthen confidence in the benchmark or honestly delineate its limits.

2. **Add bootstrapped confidence intervals** to the wF1 and wAcc results in Tables 3 and 4. With only 200 (or 140) clips, readers need to know which performance gaps are reliable.

3. **Discuss the VADER selection confound in the positive-bias analysis.** A brief paragraph acknowledging that the bimodal sentiment distribution could influence the observed bias, and ideally a control experiment (even a conceptual one), would substantially strengthen that finding.

4. **Expand the qualitative grounding analysis** into a systematic evaluation — e.g., have annotators judge whether model descriptions correctly identify the specific emotion cues present in the video, and report agreement rates per model.

5. **Add the low inter-annotator agreement to the Limitations section.** This is the most significant limitation of the dataset and should be acknowledged directly.

## Score and Decision

I performed two rounds of calibration search:

**Round 1 (bracketing):** Queried for sign language / emotion dataset papers with score bands (-1,3.5), (3.5,7.5), (7.5,11). Read anchors including BANZ-FS (7.00, strong dataset paper, Accept), LexSign (4.50, rejected), EmoDialogCN (3.33, withdrawn/rejected), BdSL-SPOTER (1.50, rejected). This placed the initial bracket at 3.5–7.5.

**Round 2 (narrowing):** Queried for emotion dataset benchmark papers in 4.5–6.5 and 3.5–5.5 bands. Read full reviews of EmotionHallucer (5.60, Accept Poster), MME-Emotion (5.00, Accept Poster), SpEmoC (4.67, Reject). Compared against BANZ-FS (7.00, read in full).

**Full anchor comparison:**
- **BANZ-FS (7.00):** Large-scale (35k instances), rigorous evaluation, multiple domains. EmoSign is significantly smaller and less thoroughly evaluated. EmoSign scores below this anchor.
- **EmotionHallucer (5.60):** First benchmark for emotion hallucinations, evaluated 41 models, well-designed adversarial protocol. EmoSign's dataset contribution is more original, but EmotionHallucer's evaluation is more rigorous. EmoSign slightly below this anchor.
- **MME-Emotion (5.00):** Large emotion benchmark (6k videos), accepted despite validity concerns (one reviewer scored 2). Similar quality level — both have novel contributions and annotation reliability concerns. EmoSign at a similar level.
- **SpEmoC (4.67):** Large-scale but rejected due to limited novelty (standard data pipeline) and insufficient empirical validation. EmoSign has a more novel contribution and more careful annotation design (Deaf native signers vs. pseudo-labeling). EmoSign above this anchor.
- **LexSign (4.50):** Rejected due to thin technical contribution and limited novelty. EmoSign's annotation design is more distinctive. EmoSign above this anchor.

**Final position:** EmoSign's core contribution — the first ASL emotion dataset with Deaf native signer annotations — is genuinely novel and well-motivated. The annotation design (fine-grained intensity, open-ended cue descriptions), three-condition ablation benchmarks, and qualitative findings about model limitations all strengthen the paper. However, the low inter-annotator agreement on several emotion categories and the insufficient discussion of annotation reliability in the Limitations section are significant weaknesses that must be addressed. After calibrating against the reviewed anchors, I place EmoSign at the same tier as MME-Emotion (5.00) and slightly below EmotionHallucer (5.60). A score of **5.0** reflects a solid, novel contribution that is held back by addressable but real methodological concerns.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>