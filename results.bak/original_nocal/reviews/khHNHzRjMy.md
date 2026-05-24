Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

EmoSign introduces a dataset of 200 ASL video clips annotated by 3 Deaf native signers with professional interpretation experience, providing 7-point sentiment ratings, intensity scores for 10 emotion categories, and open-ended descriptions of emotion cues. The paper also benchmarks four multimodal LLMs (GPT-4o, AffectGPT, Qwen2.5-VL, MiniGPT4) across three input conditions (caption-only, video-only, video+caption) on sentiment analysis and emotion classification. The benchmark results show that current MLLMs perform poorly on vision-only emotion reasoning and rely heavily on text captions.

## Strengths

1. **First emotion-annotated ASL dataset with fine-grained labels from Deaf signers** — Table 1 shows that among seven ASL datasets, only EmoSign provides emotion labels, sentiment ratings, and cue descriptions. The three-layer annotation design (sentiment, 10-emotion intensity, and free-text cue descriptions) is more comprehensive than any prior ASL dataset, including FePh (which used binary labels, cropped faces, and hearing annotators).

2. **Annotation by Deaf native signers with professional interpretation experience** (Section 3.2) — This is a genuine methodological strength. The paper explicitly contrasts with prior work (FePh) that used hearing annotators, citing evidence that hearing individuals frequently misinterpret signers' facial expressions (Lim et al., 2024). The training process and pilot testing with native ASL speakers further support annotation quality.

3. **Qualitative analysis of emotion cues from native signers** (Section 3.4) — The thematic extraction of non-manual markers (facial expressions, head movements, sign modifications) from annotators' free-text descriptions provides genuinely useful documentation of how emotions manifest in ASL through the lens of native signers. This is arguably the most valuable and least contestable contribution.

4. **Controlled ablation study showing consistent pattern** — The three-condition design (caption-only, video-only, video+caption) across four models and two classification tasks (Tables 3, 4) yields a clear and consistent finding: models approach random performance on video-only input and improve substantially when text captions are provided. This demonstrates a real limitation of current MLLMs for visual emotion reasoning in ASL.

## Weaknesses

### Major

1. **Dataset scale is insufficient to serve as a reliable benchmark** — 200 utterances (~16 minutes) from 4 signers (Table 1 says 3 signers for the dataset; Section 3.4 clarifies 4 different signers in the videos) is very small for a claimed "new benchmark." With 10 emotion categories plus a 7-point sentiment scale, per-class counts are thin (e.g., only 5 neutral clips, surprise_neg and anger have ~25 samples each). The paper's defense citing Arodi et al. (2024) (831 samples, anomaly detection) and Krojer et al. (2024) (~70k samples) does not hold up — neither is comparable to a 200-clip emotion classification benchmark with ~11 output classes. Statistical significance cannot be established with this sample size, and the reported performance differences between models (e.g., GPT-4o vs. AffectGPT in Table 3) may be within noise. The paper itself frames the contribution as "establish[ing] a new benchmark" (Abstract), which the data do not yet support.

2. **Several emotion categories have unacceptably low inter-annotator agreement** — Table 2 reports Krippendorff's alpha values. The standard threshold for tentative conclusions is α ≥ 0.667 (Krippendorff, 2011). Multiple categories fall far below this: surprise_neg (0.119), disgust (0.166), anger (0.370), frustration (0.330), sadness (0.333). Alpha values near zero indicate annotators are essentially guessing or systematically disagreeing. The ground truth for these categories is unreliable, which directly undermines the benchmark results for those emotions (Table 4). The paper's comparison to MELD (Fleiss' κ=0.43) and IEMOCAP (Fleiss' κ=0.48) uses a different metric, making the comparison inexact, and those datasets are orders of magnitude larger. While sentiment (0.738) and joy (0.699) are acceptable, the low-agreement categories represent a structural limitation.

3. **VADER-based selection biases the dataset away from the phenomenon of interest** — The dataset selects the 100 most positive and 100 most negative utterances based on VADER sentiment analysis of their *text captions*, not on visual emotion content (Section 3.1). This means the dataset is enriched for clips where emotion is already predictable from text, and undersamples the cases where visual cues convey emotion differently than the caption — precisely the cases most interesting for studying visual emotion in ASL. The paper acknowledges this (Section 6: "VADER results differed from the annotators' results... contained rich non-manual markers that conveyed emotions differently than the text"), but this is noted as an incidental property rather than a fundamental design concern. The near-complete absence of neutral clips (5/200 in Figure 2B) is a direct consequence of this bias, making the dataset unnaturalistic and limiting its usefulness for studying the full spectrum of emotional expression.

4. **Benchmarks lack statistical rigor** — No confidence intervals, error bars, or significance tests are reported for any of the benchmark results. With only 200 samples and highly skewed class distributions, the reported performance numbers cannot be properly interpreted. Claims about model "bias" (e.g., positive emotion bias, Section 5.1) are drawn from confusion matrices with very few examples per cell. The paper reports per-class accuracy in Table 4 where some cells have as few as 5-10 test samples (e.g., surprise_neg has 25 total clips, split across train/test/conditions). These are insufficient for reliable conclusions about model behavior.

### Minor

1. **Core motivation not operationalized in dataset design** — The introduction (Section 1) frames the key challenge as disentangling grammatical from emotional functions of facial expressions in ASL ("systems must disentangle these dual functions rather than treating all facial expressions as emotional cues"). However, the dataset does not annotate this distinction. The free-text cue descriptions capture what annotators perceive as emotional cues, but there is no label indicating whether a facial expression is grammatical, emotional, or both. This gap between framing and execution does not invalidate the dataset but means the paper does not deliver on its stated motivation.

2. **Dataset construction details underspecified** — Section 3.1 describes a "manual inspection" step for "emotionally expressive text content" and selection of the top 100 positive/negative VADER scores, but does not report (a) the total number of utterances initially sampled from ASLLRP, (b) the full VADER score distribution, (c) the threshold values at which the "top 100" were cut, or (d) how many utterances were excluded during manual inspection. These details are needed for reproducibility.

3. **Emotion cue grounding task defined but not quantitatively evaluated** — Section 4.1 formalizes grounding as a core task, but Section 5.3 provides only qualitative analysis of a few examples (Figure 3). No quantitative metric (e.g., temporal IoU, frame-level recall) is reported. The paper acknowledges this is "preliminary," but listing it as one of three benchmark tasks over-promises relative to the execution.

### Trivial

None.

## Nice-to-Haves

- Report majority-class and random baselines for all benchmark tasks to contextualize model performance.
- Report bootstrapped confidence intervals for all benchmark metrics.
- Include confusion matrices in the main paper (currently deferred to Appendix A.5).
- Quantify the discrepancy between VADER text sentiment and annotator-assigned visual sentiment (Section 6 mentions they "differed" but does not quantify).
- Provide per-signer breakdown of annotation patterns and model performance, given the dataset has only 4 signers.

## Removed Points

These points were considered but removed after verification against the paper:

- **"3 signers (Section 3.4)"** — The paper states "4 different signers" in Section 3.4 (line 148). The 3 annotators are distinct from the signers depicted in the videos. The factual error is removed; the underlying scale criticism remains in Major weakness #1.

- **"Annotation time implies rushed labeling"** — The harsh critic's calculation (~54 sec/video) is speculative. The paper states annotators were trained, and the task was well-defined. Without direct evidence of quality issues beyond the reported alpha values, this is not a verifiable weakness.

- **"FePh is prior work undercutting the 'first' claim"** — The paper acknowledges FePh and explicitly differentiates EmoSign on multiple grounds (intensity scales, non-face cues, Deaf annotators, cue descriptions, sentiment labels). The "first" claim is appropriately scoped to sentiment labels and fine-grained emotion annotations.

- **"The benchmark experiments do not demonstrate meaningful differentiation"** — Overstated. The video+caption condition shows clear differentiation (GPT-4o wF1=76.72 vs. AffectGPT 64.37 for 3-class sentiment). The weakness about statistical rigor is retained; the claim that results are entirely uninformative is not.

- **General/speculative concerns from the strength-finding sweep** (e.g., "could the metric be measuring a proxy") — Not concrete enough to retain.

## Novel Insights

The review synthesis highlights a tension that the paper itself does not fully resolve: the VADER selection procedure produces a dataset where the most reliable signal (sentiment, joy) comes from text-predictable emotions, while categories where visual-ground-truth might differ most from text (subtle or mixed emotions, neutral affect with visual expressiveness) have the worst annotation agreement and the fewest samples. This means the dataset's design systematically undermines its ability to deliver on its own motivating ambition — studying visual emotion cues in ASL that go beyond what text captures. The finding that "models fail on vision-only" is robust as a binary observation, but the dataset cannot support the finer-grained conclusions about specific model biases that the paper attempts to draw.

## Suggestions

1. **Expand the dataset** to at least 1,000+ clips with a broader signer pool. The annotation pipeline is well-designed and ready to scale. The current 200 clips are a pilot, not a benchmark.

2. **Replace or complement VADER sampling** with a procedure that samples from the full sentiment distribution (including neutral) to avoid systematic text-predictability bias. Random sampling with post-hoc annotation would better serve the goal of studying visual emotion cues.

3. **Drop or redesign the unreliable emotion categories** (surprise_neg, disgust, anger, frustration, sadness with α < 0.40). Either merge them into broader categories where agreement is higher, add explicit annotation guidelines to improve consistency, or report benchmarks only for categories meeting a minimum agreement threshold.

4. **Add statistical grounding** to all benchmark results: bootstrap confidence intervals, significance tests, and random/majority-class baselines.

5. **Retain the qualitative emotion cue analysis** (Section 3.4) as a standalone contribution — it is valuable and not dependent on dataset size or annotation agreement.

6. **Operationalize the grammatical-vs-emotional distinction** if the paper continues to frame this as the core motivation: add annotation layers that explicitly label whether each identified cue serves a grammatical function, emotional function, or both.

## Score and Decision

The paper addresses a genuine gap and has a thoughtfully designed annotation pipeline with culturally competent annotators. The qualitative cue analysis is a solid descriptive contribution. However, the dataset is too small and too biased to serve as a reliable benchmark, the ground truth for several emotion categories is unreliable, and the benchmark experiments lack statistical rigor. The contribution is promising but not yet realized at the level required for a top venue.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>