Now I have all the information I need. Let me write the consolidated review.

## Summary

EmoSign introduces the first ASL video dataset annotated for sentiment and emotion labels by Deaf native signers with professional interpretation experience. Alongside 200 ASL video clips with sentiment ratings, 10 fine-grained emotion categories, and open-ended emotion cue descriptions, the paper provides benchmark results from four multimodal LLMs under caption-only, video-only, and video+caption conditions. The key finding is that current MLLMs perform poorly in the video-only condition and rely heavily on text captions, revealing a text-bias problem that is particularly consequential for sign language understanding.

## Strengths

- **First dedicated emotion-annotated ASL dataset with culturally appropriate methodology.** EmoSign fills a genuine gap: prior ASL datasets focus on translation and lack emotional annotations, while existing emotion datasets (e.g., FePh) use hearing annotators who may misinterpret signers' facial expressions. The annotation team consists of 3 Deaf native ASL signers with professional interpretation experience, who are uniquely positioned to distinguish grammatical from emotional facial expressions. This is methodologically and ethically sound (Abstract, Sections 2, 3.2).

- **Ablation study design cleanly isolates modality contributions.** The paper evaluates models under three conditions (caption-only, video-only, video+caption), providing a clear picture of how much each modality contributes. The consistent finding — that video-only performance is near-chance (e.g., GPT-4o video-only wF1 24.43 for 3-class sentiment, vs. 76.72 in video+caption) while adding captions dramatically improves scores — is a clean experimental demonstration of text bias in current MLLMs (Tables 3, 4).

- **Qualitative emotion cue descriptions provide a unique resource.** Beyond categorical labels, annotators provided free-text descriptions of specific emotion cues (e.g., mouth morphemes, signing speed/size, head thrusts, non-manual markers). These descriptions, summarized thematically in Section 3.4, offer a rich qualitative resource grounded in native signer expertise that goes beyond what any existing sign language dataset provides.

- **The emotion cue grounding analysis (Section 5.3, Figure 3) is insightful despite being preliminary.** The qualitative comparison showing that the same visual cue (e.g., a facial expression) is interpreted differently by models depending on whether the caption is available compellingly illustrates the text-over-visual bias problem.

## Weaknesses

### Fatal
None.

### Major

- **Low inter-annotator agreement on several emotion categories undermines ground-truth reliability.** Krippendorff's alpha for surprise_neg (0.119), disgust (0.166), frustration (0.330), sadness (0.333), and anger (0.370) are well below the 0.67 threshold commonly considered the minimum for tentative conclusions. The paper's comparison to MELD (Fleiss' kappa = 0.43) and IEMOCAP (Fleiss' kappa = 0.48) uses a different metric (Krippendorff's alpha vs. Fleiss' kappa) and does not directly establish that these low-agreement labels are reliable enough to serve as ground truth. Because the multi-class emotion classification task (Table 4) uses these low-agreement labels, the benchmark conclusions for specific emotion categories are on uncertain footing. The paper acknowledges that positive emotions have higher agreement but does not adequately discuss the implications of the very low agreement on negative emotions for validity of the benchmarks.

- **Missing critical baselines: no random-chance or majority-class baselines, and no fine-tuned models.** The paper reports model accuracies and F1 scores but never provides the most basic baselines. For 3-class sentiment, the majority-class baseline (always predicting "negative") would achieve ~57.5% accuracy; knowing this makes the video-only results look even worse, but the absence of such baselines makes it impossible to interpret whether any observed performance is meaningful. More importantly, the paper uses only zero-shot inference on generic MLLMs. Without testing a simple fine-tuned model (e.g., an emotion classifier trained on facial landmarks, or a finetuned sign-recognition model), the benchmarks reveal LLM limitations rather than dataset difficulty or ASL-specific challenges. The paper acknowledges this in future work but the absence limits what can be concluded.

- **Small dataset size without uncertainty quantification.** The single-expression emotion classification uses 140 clips across 11 classes, with per-class counts ranging from 25 to 65. No confidence intervals, standard deviations, or statistical tests are reported. Per-class accuracies (Table 4) can swing by 10+ points with a handful of misclassifications, making it unclear which observed differences between models or conditions are meaningful. Several per-class cells show caption-only outperforming video+caption (e.g., GPT-4o surprise_neg: caption 14% vs. video+cap 0%; disgust: caption 30% vs. video+cap 50%), yet aggregate conclusions emphasize video+caption superiority. The paper cites other papers with similar-sized datasets (Arodi et al., 2024; Krojer et al., 2024) as justification, but the multi-class classification task with 11 classes at this sample size is more problematic than those works' setups.

### Minor

- **VADER-based selection limits the dataset's ability to test text-visual divergence.** The paper selects the 100 most positive and 100 most negative utterances based on VADER text sentiment scores. This means the dataset systematically prioritizes clips where emotional signal is present in the text, making it harder to test the paper's motivating scenario — cases where visual emotion cues convey something different from the text. The paper acknowledges in the limitations (Section 6) that "VADER results differed from the annotators' results" and that clips contained "rich non-manual markers that conveyed emotions differently than the text," but this tension is not explored quantitatively. A stratified sample including clips where text is neutral but visual signing is emotionally expressive would better support the paper's claims about visual emotion understanding. This does not invalidate the core findings (the ablation design is still informative), but it narrows the scope of what the benchmark tests.

- **The emotion cue grounding task is described but not quantitatively evaluated.** Section 4.1 describes grounding as a benchmark task, but the paper only provides a qualitative analysis (Section 5.3) of three randomly selected examples. No quantitative grounding metric (e.g., frame-level localization accuracy, attention alignment) is reported, making the analysis illustrative rather than systematic. This is acceptable as a preliminary exploration but does not constitute a benchmark.

- **No analysis of VADER-annotator disagreement.** The paper mentions that VADER scores differ from Deaf annotators' judgments but provides no quantitative comparison (correlation, distribution of differences). Understanding this disagreement is important: if VADER-filtered clips have annotator labels that systematically differ from VADER predictions, that would actually strengthen the case that visual cues carry independent emotional information, but this analysis is not conducted.

### Trivial
- Table 4: Abbreviated column headers (HP, SP(P), SP(N), WR, SD, FR, DG, FS, AG, NE) require looking up the legend, making the table hard to scan.
- Section 6: The sentence about VADER in limitations is grammatically broken ("we found VADER results differed from the annotators' results often contained rich non-manual markers").

## Nice-to-Haves
- Reporting per-class performance with confidence intervals (e.g., bootstrap) would clarify which observed differences are reliable.
- Including a fine-tuned baseline (e.g., a simple video classifier or adapter-tuned MLLM) would strengthen the claim that the dataset enables progress rather than just revealing known MLLM limitations.
- Stratified analysis of model errors (e.g., confusion matrices discussed in the main text rather than relegated to the appendix) would strengthen the failure analysis.
- Verbatim examples of the free-text emotion cue descriptions from annotators would substantiate the qualitative contribution.
- A comparison of sentiment predictions from VADER vs. annotator majority vote would clarify how much text-based and visual-based emotion signals diverge in the selected data.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Criticism that VADER selection makes the central claim untestable (from harsh critic, Point 1).** This overstates the problem. The ablation design (video-only vs. caption-only vs. video+caption) directly tests whether models can extract emotional information from visual cues. If the VADER selection made the dataset purely text-driven, models would achieve zero performance on video-only — yet GPT-4o reaches 40.72 wAcc on 3-class sentiment video-only, indicating visual signal exists. The finding that models heavily rely on text is robustly demonstrated. The critic's implication that this is a "circular evaluation" misunderstands the experimental design.

2. **Claim that AffectGPT's 33.33 wAcc is "exactly the baseline of always predicting neutral."** If AffectGPT always predicted neutral, accuracy would be ~2.5% (~5 neutral clips out of 200 for 3-class sentiment), not 33.33%. The critic's arithmetic is incorrect. The model's behavior is more complex than stated.

3. **Criticism that the paper's comparison to MELD/IEMOCAP Fleiss' kappa is invalid because of differing metrics.** While Krippendorff's alpha and Fleiss' kappa are different statistics, they measure related constructs (inter-rater reliability for nominal data), and contextualizing agreement with widely-used benchmarks is a standard practice. The valid concern is that the low absolute alpha values on negative emotions are still concerning — this is already reflected in the major weakness section.

4. **Missing related works (per instructions, I do not have external sources to verify their existence).**

5. **Formatting/style nitpicks, typos, grammar issues** (these are parser artifacts or minor presentation issues per instructions).

6. **Criticism about missing appendix content** (the parser strips these; they exist in the original submission).

7. **Claim that the grounding task description mentions frame-level annotations that don't exist.** The paper describes the grounding task's goal as "identify video frames and spatial regions" (Section 4.1) and then provides qualitative analysis. This is adequately scoped as preliminary. The paper does not claim to have produced frame-level grounding annotations.

8. **Strength from Strength Finder about VADER-based selection being a methodological strength** — this conflicts with the verified minor weakness about VADER selection limiting scope, so per instructions the weakness wins. Moved here.

9. **Strength from Strength Finder about inter-annotator agreement being "competitive"** — this conflicts with the verified major weakness about low IAA. Per instructions, the weakness wins.

## Novel Insights

The review reveals a paper with a genuinely valuable core contribution — the first ASL emotion dataset annotated by culturally qualified annotators — but whose execution is limited by scale and rigor. The most striking pattern across the reviews is the tension between the paper's framing ("current multimodal models fail to integrate visual cues") and the experimental design used to support it. The finding itself appears robust (ablations cleanly show text-dependence), but the mechanisms claimed — that ASL-specific visual emotion cues are being ignored — cannot be cleanly separated from the general fact that these MLLMs are bad at fine-grained visual understanding of any kind. The low inter-annotator agreement on negative emotions is not just a footnote but a structural concern: if native signers disagree substantially on which negative emotion is being expressed, then the benchmark is evaluating models against a noisy standard that may not capture a consistent visual signal. The paper would benefit from reframing its contribution more modestly — as a pilot resource and diagnostic benchmark revealing MLLM text bias, rather than as a definitive demonstration that models "fail to integrate visual cues" in ASL specifically.

## Suggestions

1. **Add missing baselines.** Report majority-class and random-chance baselines for every task. This is quick to compute and dramatically improves interpretability.

2. **Address the low IAA directly.** Stratify the analysis: report benchmark performance separately for high-agreement emotions (sentiment, joy, excited) and low-agreement emotions (surprise_neg, disgust, frustration). If models also perform poorly on high-agreement emotions, the core claim about visual cue integration is strengthened.

3. **Quantify VADER-annotator divergence.** Report the correlation or confusion between VADER text sentiment and annotator visual sentiment. If they diverge significantly, this should be presented as a feature (the dataset captures text-visual mismatch) rather than a bug.

4. **Include at least one fine-tuned baseline.** Even a simple classifier trained on video features (e.g., I3D, CLIP video features) would establish whether the dataset contains learnable visual signal and would strengthen the claim that generic MLLMs specifically underperform.

5. **Reframe the scope.** The paper's contributions are genuinely valuable but are better described as a pilot resource and diagnostic benchmark than as a definitive demonstration of visual cue failure. Adjusting the claims to match the scale and rigor would make the paper stronger.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Comparison |
|------|-----------|-----------|
| `/home/wg25r/review_agent/human_reviews_2026/GMR9BUsPbq.md` (BANZ-FS) | 7.00 | Significantly more comprehensive (35k instances vs. 200 clips). EmoSign addresses a different gap but at much smaller scale. |
| `/home/wg25r/review_agent/human_reviews_2026/bLFW2T3UHq.md` (Grounding or Guessing?) | 5.50 | Stronger technical contribution with novel metric. EmoSign's dataset contribution is more novel but technically shallower. |
| `/home/wg25r/review_agent/human_reviews_2026/oSX9aenbea.md` (MME-Emotion) | 5.00 | Much larger (6k videos) but some methodology concerns. EmoSign fills a clearer gap but is much smaller. Both accepted. EmoSign is comparable in rigor but weaker in scale. |
| `/home/wg25r/review_agent/human_reviews_2026/EhA4znYsuG.md` (EmoPrefer) | 5.20 | Accepted poster. Similar magnitude of contribution but with data quality concerns. EmoSign has more authentic annotations but similar scale problems. |
| `/home/wg25r/review_agent/human_reviews_2026/CPtKeEcLsU.md` (SpEmoC) | 4.67 | Rejected despite larger scale due to acted data and model validation concerns. EmoSign has more authentic data but smaller scale. Similar magnitude of weaknesses. |
| `/home/wg25r/review_agent/human_reviews_2026/KzpAcxWjOC.md` (ESI-Bench) | 3.50 | Rejected. Methodology concerns. EmoSign has a clearer gap and better motivation. |
| `/home/wg25r/review_agent/human_reviews_2026/U7qDPmezw7.md` (EmotionTalk) | 2.67 | Withdrawn/rejected. Small actor pool. EmoSign has more novelty but similar data quality concerns. |
| `/home/wg25r/review_agent/human_reviews_2026/VKGTGGcwl6.md` (LLMs Get Lost) | 8.00 | Far stronger execution across all dimensions. Not directly comparable (different subfield). |

EmoSign's core contribution — the first emotion-annotated ASL dataset with culturally appropriate annotators — is genuinely novel and fills a clear gap. However, the small scale (200 clips, 16 minutes), low inter-annotator agreement on critical negative emotion categories, absence of basic baselines (random/majority-class, fine-tuned models), and lack of uncertainty quantification collectively prevent the paper from achieving the rigor expected at a top venue. Compared to the anchors, it sits between the accepted poster papers (~5.0-5.5 range with acknowledged limitations) and the rejected papers (~3.5-4.67 range with more severe problems). The novelty of the gap and the quality of the annotation methodology push it above the rejected papers, but the missing baselines and small scale hold it below the stronger accepted papers.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>