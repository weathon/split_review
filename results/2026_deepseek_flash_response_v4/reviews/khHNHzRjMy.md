Now let me produce the final consolidated review.

## Summary

This paper introduces EmoSign, a multimodal dataset of 200 ASL video utterances (~16 min, 4 signers) annotated by 3 Deaf native signers with professional interpretation experience. Annotations include 7-point sentiment ratings, intensity scores for 10 emotion categories, and free-text descriptions of emotion cues. The paper presents benchmark evaluations of four MLLMs across caption-only, video-only, and video+caption conditions. This is the first dedicated emotion-annotated ASL dataset with native-signer perspectives on how emotions manifest in signing.

## Strengths

- **First dedicated emotion-annotated ASL dataset with native Deaf signer annotations, including qualitative cue descriptions (Section 3.4).** The paper fills a clear gap — no prior sign-language dataset provides sentiment, emotion intensity, and open-ended descriptions of how emotions manifest in ASL from native signers. The qualitative synthesis (non-manual markers, sign modification, context dependence) is genuinely valuable and goes beyond the binary-label approach of FePh.

- **Three-condition ablation cleanly reveals that current MLLMs perform poorly on video-only emotion recognition and are heavily text-reliant (Tables 3, 4).** The results are striking: GPT-4o achieves only 5.97 wF1 on 7-class sentiment in the video-only condition, and AffectGPT collapses to near-uniform neutral (wF1=0.04). The finding that the same visual cue is interpreted differently with vs. without text captions (Figure 3) is an informative qualitative result about model behavior.

- **Community-engaged data collection process with Deaf annotators who have professional interpretation experience (Section 3).** The paper documents months of trust-building with the Deaf community, collaboration with Deaf universities, and a thoughtful annotation protocol that distinguishes grammatical from emotional facial expressions. This is a methodological strength that sets the work apart from datasets annotated by hearing non-signers.

## Weaknesses

### Major

- **Inter-annotator agreement is low for most emotion categories, undermining ground-truth reliability for several labels.** Krippendorff's alpha values reported in Table 2 show that 6 of 10 emotion categories have alpha < 0.4, with surprise_negative (0.119) and disgust (0.166) being essentially at chance. Only joy (0.699) exceeds the conventional threshold of 0.667. The paper's comparison of the average alpha (0.593) to Fleiss' kappa values from MELD (0.43) and IEMOCAP (0.48) is directionally suggestive but not directly comparable (different statistics). The per-category picture is more concerning than the average suggests. Models evaluated against noisy ground truth for these categories will have ceiling-limited performance, and the paper does not discuss which labels are reliable enough to draw conclusions from.

- **No confidence intervals or variance estimates for any benchmark metric.** On a 200-sample, 11-class dataset where several classes have very few examples (e.g., neutral sentiment has only 5 clips), a single prediction change can shift accuracy by several percentage points. The benchmark tables (Tables 3, 4) report point estimates without confidence intervals, train/test splits are not described, and there is no discussion of statistical significance. This makes it impossible to assess whether reported differences between models or conditions are meaningful. The dataset size is acknowledged but its implications for the reliability of the benchmark conclusions are not adequately discussed.

### Minor

- **The VADER-based pre-selection creates a confound between text sentiment and label distribution that is not analyzed.** The dataset was constructed by selecting the top 100 most positive and 100 most negative utterances by VADER text sentiment. This produces a deliberately bimodal distribution (only 5 neutral clips) and systematically excludes videos where text and visual emotion diverge — precisely the most interesting cases for studying visual emotion understanding. The paper mentions in the limitations (line 330) that "VADER results differed from the annotators' results" but does not quantify this divergence. The caption-only benchmark condition also involves captions that were pre-filtered for emotional salience, making the task easier than on naturally distributed data.

- **Table 1 lists 3 signers but Section 3.4 mentions "4 different signers."** This inconsistency needs clarification. Also, the paper states that "a very small fraction of clips were skipped" yielding "minimally 1, maximally 3 annotators" per clip but does not specify how many clips have fewer than 3 annotations, which affects confidence in the majority-vote ground truth.

- **The emotion cue grounding analysis (Section 5.3) is purely qualitative.** While the observations about model behavior are interesting (models constructing explanations consistent with text rather than visual content, models claiming they need audio), the analysis of "several randomly selected videos" does not support systematic conclusions. This is appropriately labeled as preliminary, but the framing could be more cautious.

### Trivial

None.

## Nice-to-Haves

- Quantify the divergence between VADER-based text sentiment and annotator-assigned visual sentiment. A simple agreement/disagreement analysis would directly support the paper's claim that visual information matters.
- Add bootstrapped confidence intervals to benchmark results.
- Clarify whether certain emotion categories (especially those with alpha < 0.3) should be merged or excluded from evaluation.
- Expand the limitations section to directly address dataset size, low-agreement categories, and VADER selection bias rather than focusing primarily on future model improvements.

## Removed Points

The following points from the source reviewers were removed after verification against the paper:

1. **"Dataset accessibility concern" (Harsh Critic)** — "Code and data will be made publicly available after acceptance." Per hard rule, the review cannot question the existence or release status of cited resources.

2. **"FePh hearing annotators claim needs citation"** — This is about the paper's characterization of related work ("appears to have"), not a weakness of the paper's own contribution. Removed per hard rule about missing references.

3. **"Abstract claim contradicted by results" (overstated version)** — The Harsh Critic claimed the abstract's statement that models "fail to integrate visual cues" is contradicted by Table 3 (video+caption outperforming caption-only for sentiment analysis). However, the paper's video-only results are indeed very poor (near chance for several models), and the abstract's claim is defensible in context. The paper also qualifies this in Section 5.2 for emotion classification. Retained as a minor overclaim rather than removed entirely.

4. **"Krippendorff's alpha vs. Fleiss' kappa comparison is misleading" (overstated)** — The paper compares its average Krippendorff's alpha (0.593) to Fleiss' kappa values from MELD (0.43) and IEMOCAP (0.48). While these are different statistics, the comparison is directionally valid (0.593 > 0.43/0.48) and the paper uses it to contextualize rather than prove a point. The stronger concern is the disaggregated per-category values, which is retained as a major weakness.

5. **Generic evaluation criticism without specific anchor** — Several of the Harsh Critic's sweeping concerns ("the evaluation lacks rigor" without concrete evidence) were demoted or removed as per the filtering protocol.

## Novel Insights

None beyond the paper's own contributions — the finding that MLLMs interpret the same visual cue differently depending on whether text captions are present (Figure 3) is the most insightful qualitative result, but it is already presented in the paper.

## Suggestions

1. **Add confidence intervals to all benchmark results** — Bootstrapped estimates would help readers assess uncertainty on this small dataset.
2. **Analyze VADER-annotator divergence** — Quantify how often text sentiment and visual sentiment agree/disagree to demonstrate the value of visual emotion understanding.
3. **Discuss label reliability per category** — Acknowledge which emotion categories have reliable enough annotations to evaluate against and whether low-agreement categories should be pooled or dropped.
4. **Resolve the 3-vs-4 signer discrepancy** and report exactly how many clips have fewer than 3 annotations.
5. **Expand the limitations section** to directly discuss dataset size constraints, low-inter-annotator-agreement categories, and selection bias from VADER filtering.

---

### Calibration Anchors

**Round 1 — Bracket:** Plausible score range 4.0–6.5 based on initial comparison to weak anchors (<3.5: clearly worse) and strong anchors (>7.5: clearly better).

**Round 2 — Narrowing anchors:**

| Paper | Path | Avg Score | Decision | Comparison |
|---|---|---|---|---|
| SignAvatars | L2kbdthX5M.md | 6.25 | Reject | Larger-scale SL dataset (70K vids) but derivative (pose estimates). EmoSign has original annotations and clearer focus, but much smaller scale. EmoSign is slightly weaker. |
| Uni-Sign | 0Xt7uT04cQ.md | 6.40 | Accept | Large CSL dataset (1,985h) + method. Far larger in scale and technical contribution. EmoSign is clearly below this. |
| Open-vocab MER | f1uXrAjpOH.md | 5.40 | Reject | Emotion recognition dataset with LLM-human annotation. Similar concerns about annotation reliability. EmoSign has stronger community engagement but similar scale limitations. Comparable. |
| BabyView | P8uOZmypb6.md | 5.40 | Reject | Large (493h) developmental egocentric video dataset. Some reviewers question whether value is demonstrated beyond existing data. EmoSign fills a clearer gap but is vastly smaller. Slightly weaker. |
| ILLUSION | qnlG3zPQUy.md | 6.00 | Accept | Large-scale (1.3M) deepfake dataset. Much larger scale but similar role as a benchmark dataset. EmoSign is weaker in scale. |
| Sign2GPT | LqaEEs3UxU.md | 5.75 | Accept | SLT method paper, not directly comparable. |
| Representing Signs as Signs | flgrH5nK4H.md | 4.00 | Reject | ISLR method paper. EmoSign is stronger as a dataset contribution. |

**Final position:** The paper is above the very weak tier (<3.5) and the 4.0 method paper. It is comparable to BabyView (5.40) and Open-vocab MER (5.40) in overall quality — genuine contributions with meaningful limitations. It is below SignAvatars (6.25) and Uni-Sign (6.40) due to significantly smaller scale and weaker annotation reliability for several categories.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>