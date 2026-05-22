## Summary

EmoSign introduces the first multimodal dataset for emotion understanding in American Sign Language, comprising 200 ASL video clips annotated by 3 Deaf native signers with professional interpretation experience. The annotations cover sentiment (7-point scale), 10 discrete emotion categories with intensity ratings, and open-ended descriptions of emotion cues. The paper also provides benchmark results for four multimodal LLMs across sentiment analysis, emotion classification, and cue grounding tasks.

## Strengths

- **First dedicated ASL emotion dataset annotated by Deaf native signers**: Table 1 makes clear that EmoSign is the only existing ASL dataset with fine-grained emotion/sentiment labels and open-ended cue descriptions from Deaf native signers, distinguishing it from prior datasets like FePh (hearing annotators, binary labels only) and translation-focused corpora (ASLLRP, How2Sign, etc.). This directly fills a genuine gap.

- **Qualitative documentation of emotion cues through native signer perspectives**: Section 3.4 provides concrete themes from annotators' descriptions — non-manual markers (furrowed brows, mouth shapes, head thrusts), sign modifications (size, speed, repetition, fingerspelling for emphasis), and the importance of sentential context for disambiguation. This culturally grounded, expert-informed analysis goes well beyond the binary facial-expression labels of prior work and is the paper's most distinctive contribution.

- **Systematic multimodal ablation across tasks and models**: Tables 3 and 4 present a consistent three-condition ablation (caption-only, video-only, video+caption) across four MLLMs for both sentiment and emotion classification. The finding that video-only performance is near-floor for all models, and that caption-only roughly matches video+caption for emotion classification, is empirically informative and highlights a concrete limitation in current MLLMs.

- **Culturally competent annotation pipeline**: Annotators were Deaf native ASL signers with professional interpretation experience, the interface was refined through pilot tests with first-language ASL speakers (Section 3.2), and Krippendorff's alpha values are reported honestly with no suppression of low-agreement categories.

## Weaknesses

### Major

- **Low inter-annotator agreement for most emotion categories undermines the emotion classification benchmark.** Krippendorff's alpha values for 7 of 10 emotion categories fall below 0.4 (surprise_neg: 0.119, disgust: 0.166, sadness: 0.333, fear: 0.351, anger: 0.370, surprise_pos: 0.381, frustration: 0.330). Standard thresholds for Krippendorff's alpha generally consider >0.67 as the minimum for tentative conclusions. Values below 0.4 indicate annotators could not reliably distinguish these emotions in the videos. This means the "ground truth" labels for these categories are noisy, making the emotion classification benchmark — which reports per-class accuracy and F1 across all 11 classes (Table 4) — difficult to interpret as a meaningful measure of model capability. The paper compares with MELD (Fleiss' kappa = 0.43) and IEMOCAP (Fleiss' kappa = 0.48), but these are different statistics on different modalities; a direct comparison is imprecise. The sentiment labels (alpha=0.738) and joy (0.699) have acceptable reliability, but the benchmark treats all emotion categories as equally valid. The Limitations section (Section 6) does not discuss this inter-annotator reliability problem, which is a notable omission.

- **Dataset size (200 utterances, ~16 minutes) is too small to support robust multi-class benchmarking.** With 200 examples across 11 classes, several categories have only 25–50 instances (surprise_neg: 25, fear: 30, disgust: 30, anger: 25). No confidence intervals or bootstrapped metrics are reported anywhere. For a 10-class emotion classification task with unreliable labels, single-digit percentage differences in per-class accuracy are not statistically meaningful. The paper acknowledges the size limitation (citing similar-sized datasets in other domains) but then draws broad conclusions about model "failures to integrate visual cues" and "biases" from these benchmarks — conclusions that would require a more robust evaluation to support.

### Minor

- **The claim that models "fail to integrate visual cues" is partially contradicted by the sentiment analysis results.** For the sentiment task, video+caption substantially outperforms caption-only across nearly all models (e.g., GPT-4o: 76.72 vs. 49.53 wF1 on 3-class sentiment, Table 3). This *is* integration; the models clearly benefit from visual information. The paper's framing in the Abstract ("fail to integrate") and Introduction ("lack of visual grounding") is stronger than the evidence supports. A more nuanced statement — e.g., that models integrate visual cues for sentiment but not for fine-grained emotion classification, and that grounding analysis shows visual reasoning is often shallow — would be more accurate.

- **The average Krippendorff's alpha value reported (0.593) does not match the values in Table 2.** Summing the 11 listed values gives approximately 0.418. This may be a table formatting issue or a computational discrepancy, but it should be clarified.

- **The cue grounding analysis (Figure 3) is compelling but based on a small hand-selected sample.** The paper states "several randomly selected videos" were manually inspected. Defining systematic failure categories and quantifying their frequency across a larger sample would turn an interesting qualitative observation into a reproducible finding.

### Trivial

- The paper would benefit from confidence intervals on all reported benchmark metrics (Tables 3 and 4), given the small sample size.
- MiniGPT4's caption-only sentiment performance (wAcc=1.92) suggests it cannot follow the prompt; including such a model adds little.

## Nice-to-Haves

- An analysis of *why* agreement is low for negative emotions (e.g., is the disagreement systematic across annotators, or tied to specific video characteristics?) would help future dataset builders.
- Restricting the formal emotion classification evaluation to only the reliably annotated categories (sentiment, happiness/joy) and presenting the rest as exploratory would better align claims with evidence.
- Reporting confusion matrices in the main text (the paper references them in the appendix, which is standard; this is not a weakness, merely a nice-to-have for completeness).
- A breakdown of results by signer to assess cross-signer generalization.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Criticism that confusion matrices are "only referenced but not shown"**: The paper states "Confusion matrices can be found in Appendix A.5.1/A.5.2." The appendix is stripped by the parser; this is standard practice and not a valid criticism.
- **Criticism about missing appendix content and proofs**: Parser artifacts; original submission contains these.
- **Demand for confidence intervals as a "fatal" missing element**: For an empirical systems paper that honestly reports all metrics, this is a minor/elevational point, not a fatal flaw. Many benchmark papers in this space report point estimates.
- **Claim that MELD/IEMOCAP comparison is "misleading" because of different statistics**: The comparison is directional, not exact, but contextualizing reported reliability against well-known datasets is standard practice.
- **Criticism about "unfair comparison" where the asymmetry favors baselines**: Not applicable; the paper compares models under equal conditions.
- **Request for larger dataset / more signers / more training data**: These are acknowledged scope limitations that every dataset paper faces; the paper is transparent about them.
- **Formatting/style nitpicks and typos**: Parser artifacts, not author errors.

## Novel Insights

The most genuinely novel observation from the reviews is the asymmetry between the sentiment and emotion classification results: sentiment benefits substantially from video+caption integration (Table 3), while emotion classification does not (Table 4). This suggests that current MLLMs can extract coarse affective information (positive/negative/neutral) from visual cues in sign language, but fail at the finer-grained distinctions that require understanding the specific visual markers unique to sign language emotional expression. This asymmetry is more interesting and revealing than the blanket "models fail to integrate" narrative the paper currently emphasizes, and it connects directly to the paper's own qualitative finding that Deaf signers identify emotions through nuanced, culturally specific cues (head thrusts, mouth morphemes, sign modification patterns) that off-the-shelf vision encoders are not trained to capture.

## Suggestions

1. **Restructure the paper's narrative** to center the qualitative cue analysis from native signers (Section 3.4) as the primary contribution, with the benchmarks presented as exploratory baselines rather than definitive evaluations. The abstract's strong claims about models "failing to integrate" should be softened to reflect the mixed evidence.

2. **Either restrict the emotion classification benchmark** to only those categories with acceptable agreement (sentiment at alpha=0.738, happiness/joy at 0.699) or add a careful analysis of how label noise from low-agreement categories affects the conclusions. Present the low-agreement categories in the main evaluation as a separate, clearly-caveated analysis.

3. **Add confidence intervals or bootstrapped error estimates** for all quantitative results in Tables 3 and 4. With N=200 and per-class samples as low as 25, point estimates alone are misleading.

4. **Expand the qualitative grounding analysis** (Section 5.3) into a systematic taxonomy of failure modes (e.g., text-driven hallucination, visual cue misinterpretation, sign language illiteracy in models) with frequency counts across a random sample, turning the interesting observations in Figure 3 into a reproducible finding.

5. **Address inter-annotator reliability in the Limitations section** (Section 6), discussing why agreement is low for certain categories and what this implies for the usability of those labels.

## Score and Decision

**Round-1 bracket**: [4.0, 6.0] — the paper sits between the weak rejected anchors (~2–3) and the strong SL papers (~6.4), in the range where dataset papers with solid methodology but limited quantitative scope typically land.

**Round-2 anchors used for narrowing**:
- DTVLT (4.60, Reject): A benchmark dataset paper with similar framing issues. EmoSign has more novel domain-specific content but weaker quantitative validation. **Comparable or slightly stronger.**
- VRG-SLT (5.00, Reject): A sign language translation paper with questionable SOTA claims. EmoSign's contribution is more clearly original. **Comparable.**
- Open-vocabulary MER (5.40, Reject): An emotion recognition dataset with novel paradigm but annotation quality concerns. EmoSign has better annotation methodology (expert Deaf annotators) but smaller scope. **Comparable.**
- Sign2GPT (5.75, Accept): A sign language paper with concrete SOTA results. EmoSign's quantitative evidence is weaker. **Weaker.**
- EmpathyRobot (6.00, Reject): A 10K-sample dataset with some reviewer concerns about framing. EmoSign is smaller and has lower annotation reliability. **Weaker.**

**Final calibration**: The paper's qualitative contributions (Deaf-native-signer cue descriptions, culturally competent methodology) are genuinely novel and valuable — distinguishing it from the lower end of the bracket. But the quantitative benchmarks, which the paper heavily emphasizes in its framing, are significantly undermined by low inter-annotator agreement and small sample size. On balance, the paper is most comparable to anchors around 4.6–5.4. The signal-to-noise ratio in the quantitative results is too low to support the current strong claims.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>