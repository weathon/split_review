Now I have all the information needed. Let me synthesize the final review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
// List only reasonable points. Rank by severity.

### Fatal
// None

### Major
- weakness 1 — why it matters
- weakness 2 — why it matters

### Minor
- weakness 1 — why it matters

### Trivial
- weakness 1

## Nice-to-Haves
- suggestion that would improve but is not a core flaw

## Removed Points
Weaknesses that are removed keep the details of the S/W just in case they are useful

## Novel Insights
One paragraph synthesizing genuinely novel observations.

## Suggestions
- specific actionable suggestion

## Score and Decision

Let me write this now.

For the strengths:

1. **First ASL video dataset annotated for emotion by Deaf native signers** — Table 1 clearly shows EmoSign is the only dataset among six existing ASL corpora that includes "Emotion & sentiment labels" and "Emotion cue descriptions," with annotators explicitly identified as "Deaf native signers." This directly fills the gap identified in Section 1.

2. **Rich annotation design with three layers** — Annotators provided (1) 7-point sentiment ratings, (2) intensity ratings for 10 emotion categories, and (3) open-ended descriptions of specific visual emotion cues. Section 3.4 synthesizes these descriptions into concrete themes (e.g., non-manual markers as primary cue, sign modifications for emotional emphasis). No prior ASL dataset includes this kind of qualitative attribution data from native signers.

3. **Well-designed ablation study isolating modality reliance** — The three-condition setup (caption-only, video-only, video+caption) across Tables 3 and 4 cleanly demonstrates that models perform poorly on video-only inputs but improve substantially with captions, supporting the claim that current MLLMs are text-reliant.

4. **Inter-annotator agreement is systematically reported** — Table 2 provides Krippendorff's alpha for every label. The paper contextualizes these against MELD and IEMOCAP, showing that overall agreement is competitive with widely-used spoken-language emotion datasets.

For the major weaknesses:

1. **Dataset size severely limits benchmark reliability** — 200 utterances (~16 min) with only 4 signers is very small. The single-expression emotion test set has only 140 clips across 11 classes, meaning per-class counts range from ~5-20 examples. No confidence intervals, standard errors, or variance estimates are reported for any metric. Under these conditions, a 5-10 point difference between models or conditions could easily be noise. The paper draws strong conclusions ("models fail to integrate visual cues," "exhibit bias") from these small numbers. This is an evidential weakness: the benchmarks cannot reliably support the quantitative claims at the level of specificity asserted.

2. **Low inter-annotator agreement for several emotion categories undermines ground-truth reliability** — Krippendorff's alpha for Surprise_neg = 0.119, Disgust = 0.166, Frustration = 0.330, Sadness = 0.333, Anger = 0.370. These are well below the 0.67 threshold often considered the minimum for tentative conclusions. The paper notes that agreement is "better" than MELD (Fleiss κ = 0.43) and IEMOCAP (0.48), but those are different metrics and aggregate measures. For multiple individual categories, annotators barely agree beyond chance. The paper does not exclude low-agreement categories from analysis or discuss how this affects benchmark conclusions (e.g., "GPT-4o achieved 50% accuracy for Disgust" — on a ground-truth label that has α=0.166).

For minor weaknesses:

3. **VADER-based selection introduces an unexamined confound** (partially addressed in Section 6 but insufficiently). Clips were pre-filtered to include the 100 most positive and 100 most negative text captions. This preferentially selects clips where text and visual emotion may align, or where text sentiment is extreme, and explicitly excludes clips with neutral or mixed text sentiment — even if the signed emotion is interesting. The result is a dataset skewed toward text-correlated emotions, which likely makes the video-only condition harder for models (since the visual signal is pitted against a strong text signal used to define the sample) and limits the dataset's claim to be a general-purpose benchmark for emotional expression in ASL.

4. **Emotion cue grounding analysis is too thin** — The paper asserts models "fail to integrate visual cues" based on manual inspection of "several randomly selected videos" (unspecified count). While qualitative analysis is appropriate, the sample is too small and the analysis too informal to support the generalization drawn. The paper presents interesting example outputs (Figure 3) but does not quantify grounding accuracy or systematically catalog failure modes.

For the removed points - I need to remove:
- The criticism about FePh comparison / "first" claim: The paper already distinguishes from FePh clearly. 
- Criticisms about missing appendix content or missing related works.
- The reproducibility nitpick about preprocessing details.
- The formatting/style critiques.
- The Strength Finder's generic strengths about "addressing an important problem."
- Some of the harsh critic's speculative concerns.

Let me finalize everything and write the review.Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

EmoSign introduces a dataset of 200 ASL video clips annotated by three Deaf native signers with 7-point sentiment ratings, intensity scores for 10 emotion categories, and open-ended descriptions of emotion cues. The authors also benchmark four multimodal LLMs (GPT-4o, AffectGPT, Qwen2.5-VL, MiniGPT4) across three conditions (caption-only, video-only, video+caption) on sentiment analysis, single-label emotion classification, and a qualitative grounding task. The paper's core offering is the annotated dataset — the first of its kind for ASL — while the benchmarks serve as an initial diagnostic of current MLLM limitations.

## Strengths

- **First ASL dataset with emotion and sentiment labels annotated by Deaf native signers.** Table 1 shows EmoSign is the only dataset among six existing ASL corpora that includes emotion/sentiment labels and emotion cue descriptions, with annotators explicitly identified as "Deaf native signers." This directly fills the gap identified in Section 1: "the scarcity of emotion-labeled sign language data."

- **Rich, three-layer annotation design.** Annotators provided (1) 7-point sentiment ratings, (2) intensity ratings (0–3) for 10 emotion categories, and (3) open-ended descriptions of specific visual cues. Section 3.4 synthesizes these descriptions into concrete themes (non-manual markers as primary cue, sign modifications for emphasis, role of sentence context). No prior ASL dataset includes qualitative attribution data from native signers, and this is arguably the paper's most distinctive contribution.

- **Well-designed modality ablation.** The three-condition setup (caption-only, video-only, video+caption) in Tables 3 and 4 cleanly isolates modality contributions. Results consistently show poor video-only performance and text-dominant behavior, supporting the central observation that current MLLMs are text-reliant for emotion recognition in sign language.

- **Systematic inter-annotator agreement reporting.** Table 2 reports Krippendorff's alpha for every label, and Section 3.3 contextualizes the overall average (0.593) against MELD (Fleiss κ = 0.43) and IEMOCAP (0.48), demonstrating that annotation consistency is competitive with widely-used spoken-language emotion datasets.

## Weaknesses

### Fatal

None.

### Major

- **Dataset size severely limits the reliability of quantitative benchmark conclusions.** With only 200 utterances (~16 min, 4 signers), the single-expression test set has 140 clips across 11 classes, yielding per-class counts ranging from roughly 5–20 examples. No confidence intervals, standard errors, bootstrap estimates, or cross-validation results are reported for any metric. Under these conditions, a 5–10 point difference between models or modality conditions could easily fall within noise. The paper draws strong conclusions ("models fail to integrate visual cues," "exhibit bias toward positive emotions") from these point estimates. While the qualitative patterns are suggestive and consistent with intuition, the quantitative evidence is not robust enough to support the specificity of the claims made, particularly in the abstract and conclusion.

- **Low inter-annotator agreement for several emotion categories undermines ground-truth reliability for the benchmarks.** Krippendorff's alpha for Surprise_neg = 0.119, Disgust = 0.166, Frustration = 0.330, Sadness = 0.333, and Anger = 0.370. These are well below the 0.67 threshold often considered the minimum for tentative conclusions. The paper's comparison to MELD and IEMOCAP uses aggregate metrics (different from Krippendorff's alpha), which does not address the fact that for multiple *individual* categories, annotators barely agree beyond chance. The paper does not exclude or flag low-agreement categories in the benchmark analysis, even though metrics like "GPT-4o achieved 50% accuracy for Disgust" rest on ground-truth labels with α = 0.166. This should be discussed transparently, and conclusions from those categories should be softened.

### Minor

- **VADER-based selection introduces an unexamined confound.** Clips were pre-filtered by selecting the 100 most positive and 100 most negative *text captions* per VADER. This preferentially selects clips where text and visual emotion may align, or where text sentiment is extreme, and explicitly excludes clips with neutral or mixed text sentiment — even if the signed emotion is interesting. The result skews the dataset toward text-correlated emotions with strong polarity, making it less representative of the full spectrum of affective signing (e.g., subtle emotions, irony, contrast between text and sign). Section 6 mentions the VADER-annotator divergence but does not discuss how the selection procedure itself limits the dataset's claim to be a general-purpose emotion-in-ASL benchmark.

- **Emotion cue grounding analysis is too thin to support the strongest claims.** The paper states that models "fail to integrate visual cues" based on manual inspection of "several randomly selected videos" (no count given). While qualitative analysis is appropriate for a dataset paper, the sample is too small and the analysis too informal to support the generalization that "current models fail to integrate visual cues into emotional reasoning" (abstract). Figure 3 provides illustrative examples, but the paper would benefit from either a more systematic coding or a stronger caveat that these are preliminary observations.

- **No sign-language-specific baselines.** The paper benchmarks general-purpose MLLMs but does not include any model trained or fine-tuned on sign language video. Section 6 mentions this as future work, but as a benchmark paper, the absence of even a simple supervised baseline (e.g., fine-tuning a visual encoder on ASLLRP) makes it difficult to attribute the poor video-only performance to the model family rather than to the absence of sign-language-specific training.

### Trivial

- The emotion-cue descriptions in Section 3.4 are informative but could be more systematically organized (e.g., a table mapping specific non-manual markers to associated emotions).

## Nice-to-Haves

- **Bootstrap confidence intervals or small-scale cross-validation** would substantially strengthen the benchmark claims without requiring more data. If the dataset is too small for meaningful splits, that should be honestly stated and the quantitative claims softened.
- **Analysis of annotation disagreement as a feature.** Low-agreement categories (Surprise_neg, Disgust) could be analyzed to identify which emotions are genuinely confusable in ASL and why, turning a weakness into a diagnostic contribution.
- **Analysis of annotator confidence scores.** The paper collects self-reported confidence (0–100) for tie-breaking but never analyzes it. Whether confidence correlates with agreement or with specific video characteristics could be a useful diagnostic.

## Removed Points

- **Criticism that FePh comparison is insufficient / "first" claim needs checking:** The paper clearly distinguishes EmoSign from FePh along three specific dimensions (Section 2). This criticism is based on a misreading.
- **Formatting, typos, grammar, garbled text:** These are PDF-parser artifacts, not author errors.
- **Missing appendix content / missing related works:** The parser strips these sections; they exist in the original submission.
- **"No error bars" criticism that demands what is standard practice:** Actually retained as a Major weakness because the absence is material to the claims, but framed as a specific evidential limitation rather than a generic formatting complaint.
- **Strength Finder's generic or sycophantic strengths** (e.g., "addressed an important problem," "systematic pipeline" without specific anchor): Removed as insufficiently concrete or conflicts with verified weaknesses.
- **Criticism about reproducibility (hyperparameters, pre-processing details):** Trivial implementation details not material to evaluation.
- **Harsh critic's speculation that "the paper does not state whether videos were preprocessed":** The paper states frame rate (10 fps) and encoding; preprocessing details beyond that are a minor omission, not a fatal flaw. Downgraded from the critic's framing.

## Novel Insights

The most interesting cross-cutting observation from the reviews is that two distinct weaknesses — the small dataset size and the low per-category inter-annotator agreement — compound each other in the benchmark analysis. The benchmark already has very few examples per class; when the ground truth for those few examples is unreliable (e.g., Disgust with α=0.166), the resulting per-class accuracy numbers are essentially uninterpretable. This is a more fundamental issue than either weakness alone, and the paper does not acknowledge it. Additionally, the VADER selection procedure creates a subtle tension with the paper's framing: the dataset is positioned as a resource for studying *visual* emotional expression in ASL, yet the sampling criterion (text sentiment extremes) may systematically select clips where the visual emotion is aligned with — and perhaps predictable from — the text, reducing the benchmark's diagnostic value for isolating visual emotion understanding.

## Suggestions

1. **Add uncertainty quantification to benchmark results** (bootstrap confidence intervals or simple standard deviations across runs) and explicitly note the per-class sample sizes alongside per-class accuracy numbers in tables.
2. **Re-analyze the benchmarks after excluding or flagging low-agreement categories** (Surprise_neg, Disgust, Frustration, Sadness, Anger), or at minimum discuss how low agreement affects the reliability of those results.
3. **Expand Section 6 to explicitly discuss the VADER confound:** acknowledge that the selection biases the dataset toward text-correlated emotions and clarify what kinds of research questions the dataset is and is not suited for.
4. **Add a simple supervised baseline** (e.g., fine-tune a visual encoder on ASLLRP or use a sign-language-specific feature extractor) to contextualize the MLLM results.
5. **Increase the sample size for the grounding analysis** to at least 20–30 clips with systematic coding, or rename it explicitly as "illustrative case studies" and soften the corresponding claims in the abstract.

## Score and Decision

**Calibration:**

**Round 1 — Bracketing:**
- Low band (≤3.5): BdSL-SPOTER (1.50), EmotionTalk (2.67), EmoDialogCN (3.33), Unified FER (1.50) — clearly weaker papers
- Middle band (3.5–7.5): SpEmoC (4.67), Video2Reaction (4.00), MME-Emotion (5.00), EmoPrefer (5.20) — mixed evaluations
- High band (≥7.5): GUV (8.00), NavFoM (8.00), LLMs Multi-Turn (8.00), Gaia2 (8.00) — clearly much stronger works

Initial bracket: **4.0 – 6.0**

**Round 2 — Narrowing:**
- LexSign (4.50, Reject) — sign-language dataset with benchmarks, similar quality level. EmoSign has a more unique contribution (first ASL emotion dataset) but is smaller. Comparable.
- SpEmoC (4.67, Reject) — much larger (30K clips) but acted data. EmoSign is more novel but smaller. EmoSign is slightly weaker due to scale limitations.
- MME-Emotion (5.00, Accept Poster) — 6,500 clips, 20 models, comprehensive evaluation. EmoSign is clearly weaker.
- BAH Dataset (5.50, Accept Poster) — 1,427 videos, 10.6h, novel task (ambivalence/hesitancy). EmoSign addresses a more clearly important gap but is much smaller (16 min vs 10.6h, 4 vs 300 participants). EmoSign is weaker.
- EmotionHallucer (5.60, Accept Poster) — 41 models, solid methodology. EmoSign is weaker.
- Customizing Visual Emotion (4.50, Accept Poster) — comparable score, different domain.

EmoSign sits between the rejected dataset papers (LexSign 4.50, SpEmoC 4.67) and the accepted ones (MME-Emotion 5.00, BAH 5.50, EmotionHallucer 5.60). Its genuine novelty is offset by severe scale limitations and the compounding effect of low agreement + small N on benchmark credibility.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>