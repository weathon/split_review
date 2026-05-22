## Summary

EmoSign introduces the first dedicated ASL emotion dataset (200 utterances, ~16 minutes) annotated by 3 Deaf native signers across three tiers: sentiment (7-point scale), 10 emotion categories, and free-text emotion cue descriptions. The paper benchmarks 4 multimodal LLMs (GPT-4o, AffectGPT, Qwen2.5-VL, MiniGPT4) under caption-only, video-only, and video+caption ablations, finding that models rely heavily on text and struggle with visual-only emotion recognition in sign language.

## Strengths

- **Fills a genuine and clearly documented gap.** Table 1 systematically compares EmoSign against all major ASL datasets (YouTube-ASL, OpenASL, ASL STEM Wiki, ASLLRP, How2Sign, MS-ASL), and none contain affective annotations. This is not incremental.

- **High-quality annotation pipeline with Deaf native signers.** The three-tier annotation (sentiment, emotion presence, and open-ended cue descriptions) goes beyond binary labels. The use of Deaf signers with professional interpretation experience addresses a documented problem that hearing annotators misinterpret signers' facial expressions (citing Lim et al., 2024). The cue descriptions are a genuinely novel data type not found in prior sign language datasets.

- **Systematic modality ablation reveals meaningful findings.** Tables 3–4 demonstrate that caption-only performance often matches or exceeds video-only (e.g., GPT-4o caption-only wF1=55.89 vs. video-only wF1=20.76 on emotion classification), and video+caption consistently outperforms both unimodal conditions. This provides concrete evidence that current models fail to leverage visual signing cues, a finding directly relevant to the community.

- **Insightful qualitative analysis.** Figure 3 shows models interpret the same visual cue differently depending on text availability (MiniGPT4 describes "joyful expression" in video-only but "upset or frustrated" with captions), demonstrating text-guided rather than visually-grounded reasoning — a finding specific to sign language.

## Weaknesses

### Fatal

None.

### Major

- **VADER-based pre-selection introduces a methodological confound that is acknowledged but under-explored.** The dataset is constructed by filtering ASLLRP utterances through VADER English text sentiment to select the "100 most positive and 100 most negative" clips (Section 3.1, lines 117–119). Yet the paper's central thesis is that emotion in sign language is conveyed through visual cues that may diverge from linguistic content. Section 6 (line 388) states "VADER results differed from the annotators' results often" — but the paper never quantifies this divergence, nor analyzes whether benchmark results differ for aligned vs. divergent clips. This isn't fatal (the divergence is arguably a feature for studying the text-visual gap), but the lack of analysis leaves a key methodological question unaddressed.

- **Low inter-annotator agreement on several emotion categories undermines per-emotion benchmark validity.** Table 2 reports Krippendorff's alpha of 0.119 (surprise_neg), 0.166 (disgust), 0.330 (frustration), and 0.370 (anger). With only 3 annotators and majority vote, these labels are determined by 2-of-3 agreement at near-chance levels. Table 4 then reports per-emotion accuracy for these categories (disgust: 14–50%, anger: 0–33%) on very small counts (~10–25 clips). The paper compares overall average alpha (0.593) to MELD and IEMOCAP kappa scores, but these are different metrics applied to different tasks, making the comparison imprecise. The paper does not discuss implications of low agreement for benchmark interpretability, nor report agreement-conditioned results.

- **No statistical reporting despite very small sample sizes.** With 200 total utterances and some emotion categories appearing in as few as 25 clips (Figure 2C), per-emotion accuracy numbers are inherently noisy. The paper reports no confidence intervals, variance across runs, or significance testing. For instance, the difference between GPT-4o video+caption wAcc (35.97) and Qwen2.5 video+caption wAcc (34.96) on emotion classification (Table 4) cannot be assessed for significance. This limits the interpretability of the benchmark results.

### Minor

- **Uninvestigated anomalies in model performance.** MiniGPT4's caption-only wAcc of 1.92% and wF1 of 5.92% on 3-class sentiment (Table 3) is near zero, suggesting a potential setup issue or model failure mode the paper does not investigate. GPT-4o's video-only wAcc of 40.72% on 3-class sentiment is surprisingly high and may reflect label-distribution bias, but is not analyzed.

- **Emotion cue grounding analysis is purely qualitative.** Section 5.3 is based on "manually inspecting several randomly selected videos" (line 277), making it anecdotal. The free-text cue descriptions are the dataset's most novel component, yet the paper provides only brief thematic summaries (Section 3.4) and a few cherry-picked examples (Figure 3) rather than systematic coding of cue types across emotions.

- **Inconsistency in emotion granularity.** Joy and excited are merged into "happiness" based on Jaccard similarity of 0.81 (Section 4.1), yet surprise_pos and surprise_neg remain separate despite likely similar co-occurrence patterns. The paper does not justify why some categories are merged while others with comparable overlap are not.

### Trivial

None.

## Nice-to-Haves

- Systematically code the free-text cue descriptions by type (facial expression, signing speed, body movement, etc.) across emotion categories, rather than treating them qualitatively. This would substantially increase the paper's value.
- Report results conditioned on annotation agreement (e.g., unanimous vs. 2/3 agreement) to disambiguate benchmark interpretability despite noisy labels.
- Add bootstrap confidence intervals on benchmark metrics given the small dataset.
- Expand the limitations discussion to address low inter-annotator agreement implications and small per-category sample sizes.

## Removed Points

These points are flagged to be removed per filtering rules:
- "Annotator training may have primed cue types": This is a valid concern raised by the harsh critic, but the training session is standard practice for annotation alignment and the paper describes it as walkthrough/clarification (line 123). Not actionable.
- "Reproducibility concerns about models": Per hard rules, we do not question the existence or availability of cited models.

## Novel Insights

The paper's most valuable observation is that multimodal LLMs exhibit fundamentally text-dependent emotion reasoning for sign language — not merely text-biased, but text-dependent, with visual-only performance often near chance and models interpreting identical visual cues in opposite emotional directions depending on caption availability (Figure 3). This is a finding that generalizes beyond sign language to the broader question of whether current VLMs genuinely integrate visual information for affective reasoning, or merely use it to confirm text-based predictions.

## Scoring Anchors

**Round 1 brackets:**
- Weak (<3.5): R-KinetiQuery (1.67), MDPE (2.50), ShadowPunch (3.00) — all rejected papers with various fundamental issues
- Middle (3.5–7.5): Open-vocabulary MER (5.40, reject), SignAvatars (6.25, reject), Uni-Sign (6.40, accept), MM-GRAPH (4.50, reject)
- Strong (>7.5): TANGO (8.50), PhysBench (8.00), LOKI (8.00)

**Round 1 bracket: 4.0–6.0**

**Round 2 narrowing:**
- Open-vocabulary MER (5.40, reject): Proposes a new paradigm with larger-scale dataset construction but suffers from data leakage issues, missing dataset statistics, and questionable ground truth. EmoSign is arguably more soundly designed despite being smaller.
- Uni-Sign (6.40, accept): Much larger scale (1,985 hours, new dataset), technical novelty in pre-training framework, SOTA results. EmoSign is clearly weaker in scale and technical contribution but addresses a different, equally important niche.
- Face-Human-Bench (5.75, reject): Comprehensive benchmark for face/human understanding with 900+ items. Similar benchmark contribution scope. EmoSign has stronger novelty in its annotation methodology.
- On generalization of neural networks for multimodal reasoning (5.67, accept): Systematic evaluation across architectures. Different focus but similar scale of contribution.

**Round 2 bracket: 4.5–5.5**

EmoSign is positioned slightly above Open-vocabulary MER (5.40) given its cleaner methodology and genuine novelty in the sign language emotion space, but below Uni-Sign (6.40) due to limited scale and missing statistical rigor. The paper fills a real gap with a thoughtfully designed but small dataset, and its main findings (model text-dependence) are clear despite noisy labels. Score: 5.0.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>