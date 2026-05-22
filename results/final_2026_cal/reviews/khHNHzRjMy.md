Now I have my calibration anchors. Let me synthesize the review.

My Round 1 bracket: between 3.5 and 7.5. The weak anchors (avg 1.5–3.33) were papers with fundamental flaws or minimal contributions; the strong anchors (7.5+) were high-impact papers. EmoSign clearly belongs in the middle bracket.

Round 2 narrowing (4.5–7.0): I examined:
- **BANZ-FS (7.0)** — large sign language dataset, clean methodology; EmoSign is significantly weaker in scale and benchmark rigor.
- **SpEmoC (4.67, Reject)** — large emotion dataset but rejected; EmoSign has more genuine novelty (first ASL emotion dataset vs. a standard pipeline applied at scale).
- **BAH Dataset (5.5, Accept Poster)** — small dataset (1,118 videos, 8.26h) for a novel emotion construct, similar "first-of-its-kind" framing with baseline benchmarks. EmoSign is comparable but slightly weaker: much smaller (200 vs 1,118), only 4 signers vs 224 participants, VADER selection bias, lower IAA on several emotions.
- **MME-Emotion (5.0, Accept Poster)** — emotion benchmark with 6,500 clips but validity concerns; EmoSign has less data but a more clearly needed contribution.

My final score: **5.0**. The paper's core contribution—the first ASL emotion dataset with culturally competent annotations from Deaf native signers and qualitative cue descriptions—is genuine and fills a real gap. However, the small scale (200 utterances, 4 signers), VADER-based selection bias, low inter-annotator agreement on several emotions, and the over-interpretation of benchmark results prevent it from being a stronger paper. The dataset should be accepted as a foundation, but the benchmark framing needs recalibration.

Now let me write the full review.## Summary

EmoSign introduces the first ASL video dataset annotated specifically for emotion understanding: 200 utterances from 4 signers, labeled by 3 Deaf native signers with professional interpretation experience on sentiment (7-point scale), 10 emotion categories with intensity, and open-ended descriptions of emotion cues. Benchmarks on 4 MLLMs (GPT-4o, Qwen2.5, AffectGPT, MiniGPT4) across caption-only, video-only, and video+caption conditions show that current models struggle to recognize emotions from visual cues alone and exhibit positive/neutral bias.

---

## Strengths

**1. First ASL emotion dataset annotated by culturally competent Deaf native signers.** This directly addresses a genuine gap — existing ASL datasets (Table 1) focus on translation and lack emotional annotations. The paper explicitly distinguishes EmoSign from FePh (the closest prior work), noting that FePh used cropped faces, binary labels, and likely hearing annotators. EmoSign's use of Deaf native signers with professional interpretation experience for fine-grained sentiment and emotion annotation is a principled design choice.

**2. Qualitative emotion cue descriptions are a unique and underexploited contribution.** Annotators provided open-ended descriptions of what visual cues (facial expressions, head movements, mouth morphemes, signing speed/size, body language) led to their emotion judgments. Section 3.4 summarizes themes such as non-manual markers as primary cues, sign modifications for emphasis, and the role of sentence context. This kind of culturally grounded qualitative data is not available in any other sign language dataset and has the potential to inform future model design.

**3. Systematic ablation across modalities reveals a consistent and interpretable pattern.** The three-condition design (caption-only, video-only, video+caption) is well-conceived. Tables 3–4 show that for sentiment analysis, video+caption consistently outperforms both unimodal conditions, while for emotion classification, caption-only ≈ video+caption ≫ video-only. This clean pattern supports the central claim that models rely heavily on text and fail to effectively integrate visual emotion cues in ASL.

**4. Honest and reasonably thorough limitations section.** Section 6 acknowledges the VADER text-sentiment selection bias, the lack of real-world complexity (multiple speakers, varied settings), and the opportunity for fine-tuning sign-language-specific models. The paper is transparent about what it does not do, even if some of these issues deserve more prominence.

---

## Weaknesses

### Fatal

None.

### Major

**1. Dataset size (200 utterances, 4 signers, ~16 min) fundamentally limits the strength of the benchmark conclusions.** The paper's narrative weight falls heavily on the benchmark findings — the abstract, introduction, and conclusion all state that "current multimodal models fail to integrate visual cues" and "exhibit bias towards positive emotions." However, with 200 clips split across 10+ emotion categories and 7 sentiment levels, many evaluation cells contain single-digit samples (Table 4 per-emotion cells range from ~7–23 samples). The single-expression subset (140 clips) divided across 11 labels gives ~13 samples/class on average, and several classes have fewer. The findings are plausible but the evidence is thin: zero-shot inference on a very small, VADER-filtered sample does not support strong, general claims about inherent model incapacity. **The benchmark findings should be reframed as illustrative pilot baselines, not as decisive evidence of model failure.** The paper cites prior work suggesting small datasets can be valuable for benchmarking, but this does not change the fact that per-cell sample sizes are too small for reliable conclusions.

**2. The VADER-based selection pipeline introduces a systematic bias that is under-discussed in its implications.** Clips were selected as the top-100 positive and top-100 negative utterances according to VADER sentiment analysis of *text captions*, not of the signing. This deliberately enriches for clips where text sentiment is extreme and potentially misaligned with visual emotion. The Limitations section mentions this only briefly ("VADER results differed from the annotators' results") without quantifying the disagreement or analyzing its effect on benchmark interpretations. The dataset therefore does not represent naturalistic emotional expression in ASL — it represents cases where text-based sentiment *may* conflict with visual emotion. Low video-only performance could partly reflect dataset difficulty (the most extreme VADER-filtered clips) rather than model incapacity.

**3. Inter-annotator reliability is well-reported but problematic for several emotion categories.** Average Krippendorff's alpha is 0.593 (below the conventional 0.67 threshold for tentative conclusions), and several categories are near chance: surprise_negative (0.119), disgust (0.166), frustration (0.330), sadness (0.333), anger (0.370), surprise_positive (0.381), fear (0.351). Only sentiment (0.738) and joy (0.699) reach acceptable levels. The comparison to MELD (Fleiss' κ=0.43) and IEMOCAP (Fleiss' κ=0.48) uses a different agreement metric and does not address the fact that those are far larger datasets. With only 3 annotators and majority-vote adjudication, the ground truth for low-agreement emotions is essentially one annotator's opinion in many cases. This undermines the validity of per-emotion classification benchmarks for these categories.

### Minor

**1. No statistical significance or confidence intervals for benchmark results.** With 200 samples, reported differences between conditions or models could be within noise. Bootstrap confidence intervals or significance tests would substantially strengthen the reliability of the benchmark claims.

**2. No per-signer analysis or signer demographic information.** The dataset has 4 signers from ASLLRP, but the paper does not report their ages, genders, or regional variation. Per-signer breakdowns of model performance could reveal whether results are driven by signer-specific expressiveness patterns.

**3. The qualitative grounding analysis (Figure 3) is framed as systematic but is anecdotal.** The paper states "we manually inspected several randomly selected videos" but shows only one example and claims cues were "verified" without describing a systematic verification procedure. The analysis is valuable as illustration but should not be presented as evidence of model behavior beyond the specific examples shown.

**4. The model comparison is confounded by model size and architecture.** MiniGPT4 is substantially smaller than GPT-4o, making direct behavioral comparisons uneven. The paper acknowledges this indirectly but sometimes implies cross-model conclusions (e.g., "GPT-4o better captures emotions").

**5. The multi-expression subset (37 clips) is defined but not evaluated.** The paper defines this subset and then does not report results on it, which raises the question of why it was defined. Either evaluate it or remove it from the task definition.

### Trivial

None beyond the scope of what the paper already addresses.

---

## Nice-to-Haves

- Quantify the disagreement between VADER text sentiment and annotator visual sentiment (e.g., a scatter plot), which would directly demonstrate why visual annotations are needed.
- Convert the qualitative emotion cue descriptions into a structured taxonomy with frequency counts per cue type and emotion.
- Limit the emotion classification benchmark to high-agreement emotions (sentiment, joy, worry) or report results with and without low-agreement categories.
- Report confidence intervals via bootstrapping for all benchmark metrics.

---

## Removed Points

- **Criticism about "FePh appears to have hired hearing annotators" being speculative** — The paper uses appropriately hedged language ("appears to have"), cites a relevant reference (Lim et al. 2024), and this is a minor framing point, not a weakness.
- **Formatting nitpicks, typos, capitalization, missing appendix content, missing references** — These are parser artifacts or style issues that do not affect evaluation.
- **Reproducibility concerns about undisclosed hyperparameters or implementation details** — Standard for a dataset/benchmark paper; training details are not the primary contribution.
- **Criticism about "not controlling for model size/architecture" as a fatal flaw** — Demoted to Minor since the paper primarily compares behavioral patterns across conditions, not raw performance between models.
- **"Missing comparison between VADER and annotators"** — Moved to Nice-to-Haves since it is a missed opportunity rather than a flaw.
- **Strength Finder claim about "dataset avoids acted emotions" being an unambiguous strength** — While valid, it is a methodological choice that also limits control; kept as a moderate strength.
- **Generic strengths from Strength Finder about "addressing an important problem"** — Removed as generic/superficial; only specific, evidence-backed strengths kept.

---

## Novel Insights

The most interesting tension in this paper is between its two contributions. The dataset itself — particularly the qualitative emotion cue descriptions — is genuinely novel and culturally grounded in ways that typical emotion datasets are not. However, the paper's rhetorical energy is spent on benchmark results that are too thin to carry that weight. The reviews reveal a structural mismatch: the qualitative annotation data (Section 3.4) is the part most likely to drive future work, yet it receives the least analytical treatment. A more productive direction for the authors would be to convert the cue descriptions into a formal taxonomy (facial expression types, signing speed modulations, head/body movement patterns, mouth morphemes) and report their frequency by emotion — turning the observational summaries into a reusable resource. This would strengthen the dataset's value far more than adding more zero-shot model evaluations.

---

## Suggestions

1. **Reframe the benchmark section explicitly as preliminary pilot baselines.** Replace language like "current models fail to integrate visual cues" with "initial results suggest models struggle with visual-only emotion recognition on this dataset, warranting further investigation." The dataset contribution stands on its own; over-claiming on the benchmarks weakens the paper.
2. **Quantify the VADER–annotator disagreement.** A simple scatter plot of VADER text sentiment vs. annotator sentiment score would directly demonstrate the gap the dataset addresses and clarify the selection bias.
3. **Deepen the qualitative analysis of emotion cue descriptions.** Code the open-ended responses into a structured taxonomy with inter-annotator cue frequencies. This would make the descriptive findings replicable and immediately useful for model design.
4. **Add confidence intervals or bootstrap estimates to all benchmark metrics.** With 200 samples, this is essential for readers to assess whether reported differences are meaningful.
5. **Consider limiting the main benchmark to high-agreement emotion categories** (sentiment, joy, worry) or clearly separating results for low-agreement categories with appropriate caveats.

---

## Score and Decision

**Calibration anchors used:**

| anchor_id | avg_score | round | comparison to EmoSign |
|---|---|---|---|
| mUqgxqe8XK (BdSL-SPOTER) | 1.50 | R1 | Weaker; rejected BdSL recognition paper |
| U7qDPmezw7 (EmotionTalk) | 2.67 | R1 | Weaker; withdrawn emotion dataset paper |
| KkuINI7YJz (EmoDialogCN) | 3.33 | R1 | Weaker; withdrawn Mandarin emotion dataset |
| ijEi63QLsr (HOI evaluation) | 3.00 | R1 | Not comparable domain |
| GMR9BUsPbq (BANZ-FS) | 7.00 | R1 | Stronger; larger sign language dataset, cleaner benchmarks |
| CPtKeEcLsU (SpEmoC) | 4.67 | R1 | Comparable scale different; rejected, less novel pipeline |
| jUrmXDgQct (Video2Reaction) | 4.00 | R1 | Different domain, comparable methodology quality |
| mOFGOK6Vmo (LexSign) | 4.50 | R1 | Comparable sign language dataset paper |
| oSX9aenbea (MME-Emotion) | 5.00 | R2 | Similar score; emotion benchmark, comparable execution quality |
| bLFW2T3UHq (Grounding or Guessing) | 5.50 | R2 | Similar score; SLT paper with very mixed reviews |
| jYDHVscRO3 (BAH Dataset) | 5.50 | R2 | Slightly stronger; similar small-scale "first-of-its-kind" dataset |
| ahWmeQG3K2 (EmotionHallucer) | 5.60 | R2 | Slightly stronger; emotion hallucination benchmark |

**Round 1 bracket:** [3.5, 7.5]  
**Round 2 narrowing:** Anchors in (4.5, 7.0) gave a range of 4.67–5.60. EmoSign is most comparable to BAH (5.5) and MME-Emotion (5.0) but slightly weaker than both — BAH has 5× more data and participant diversity, while EmoSign compensates with a more novel gap and better annotation transparency. Final score anchored at 5.0.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>