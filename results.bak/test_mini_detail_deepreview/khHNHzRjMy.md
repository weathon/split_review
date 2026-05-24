Now I have a thorough understanding of the paper and the calibration landscape. Let me write the final consolidated review.

## Summary

EmoSign introduces a dataset of 200 ASL video clips (16 minutes total) annotated by three Deaf native ASL signers with sentiment labels, fine-grained emotion intensity ratings across 10 categories, and open-ended descriptions of emotion cues. The paper also presents zero-shot benchmark evaluations of four multimodal LLMs (GPT-4o, AffectGPT, Qwen2.5-VL, MiniGPT4) on sentiment and emotion classification tasks across ablation conditions (video-only, caption-only, video+caption). The dataset addresses a genuine gap — no existing ASL dataset provides emotion/sentiment labels annotated by culturally qualified Deaf signers.

## Strengths

- **First ASL dataset with fine-grained emotion annotations from Deaf native signers.** Table 1 shows that EmoSign is the only ASL dataset among seven compared that provides emotion labels, sentiment labels, and emotion cue descriptions. This directly fills the gap identified in the introduction that "the scarcity of emotion-labeled sign language data compounds these difficulties" for studying affective expression in sign language.

- **Rich qualitative emotion cue descriptions from culturally qualified annotators.** Section 3.4 documents detailed patterns from the annotators' open-ended responses — non-manual markers (furrowed brows, pursed lips, head thrusts, body tilting), sign modifications (size, speed, repetition, finger-spelling for emphasis), and role/context markers (eye gaze shifts, signing space changes). This qualitative analysis is the paper's most novel contribution and would be difficult to replicate without native ASL fluency.

- **Well-designed annotation pipeline with appropriate cultural competence.** Section 3.2 describes a rigorous process: training sessions, pilot testing with ASL-first individuals, a 7-point sentiment scale, intensity ratings for 10 emotions based on established models (Ekman, Russell), confidence ratings, and free-response cue descriptions guided by prior literature. Using three Deaf ASL signers with professional interpretation experience — who can distinguish grammatical from emotional facial expressions — is a meaningful improvement over prior work (e.g., FePh) that used hearing annotators.

- **The ablation study design reveals genuine model limitations.** The three-condition setup (video-only, caption-only, video+caption) in Tables 3 and 4 provides informative evidence that current general-purpose MLLMs perform poorly on sign language video emotion recognition, with video-only performance at or near chance across most models. The finding that video+caption generally outperforms video-only but sometimes underperforms caption-only suggests models rely heavily on text — a result consistent with prior research cited in the paper (Liang et al., 2024b; Xiao et al., 2024).

## Weaknesses

### Major

- **The VADER text-sentiment selection criterion creates a bias that undercuts the paper's central motivation.** The paper motivates EmoSign by arguing that emotion in sign language operates through visual channels (facial expressions, signing speed, body movement) that are distinct from linguistic content. Yet the dataset construction (Section 3.1) selects only the 100 most positive and 100 most negative utterances *based on VADER scores of their text captions*. This systematically biases the sample toward cases where the text sentiment is extreme and — by construction — where the text and visual emotion are likely aligned, while filtering out the very cases most informative for the paper's research question: videos where text is neutral but visual emotion is strong, or where the two channels diverge. The limitation is acknowledged in Section 6 ("VADER results differed from the annotators' results"), but this acknowledgment does not resolve the structural selection bias: the dataset simply does not contain the cases needed to study visual emotion cues independently of text. The paper's strongest contribution (the qualitative cue analysis in Section 3.4) survives this criticism, but the dataset's fitness for the claimed purpose is materially impaired.

- **Low inter-annotator agreement on several key emotion categories makes ground-truth labels unreliable for those categories.** Table 2 reports Krippendorff's alpha values that are very low for several emotions: surprise_neg (0.119), disgust (0.166), frustration (0.330), sadness (0.333), anger (0.370), fear (0.351). At alpha < 0.2, surprise_neg and disgust have agreement barely distinguishable from chance. The paper reports the average (0.593) and compares favorably to MELD and IEMOCAP, but those use a different metric (Fleiss' kappa) and the comparison is not directly applicable. More importantly, the paper does not discuss how noisy labels on these categories propagate to the benchmark evaluations — accuracy and F1 scores for these classes (e.g., 25 clips for anger, 30 for disgust) may reflect annotation noise more than model capability.

- **The benchmark evaluation is presented as a core contribution but lacks statistical rigor.** With only 200 clips and per-class counts as low as 25 (anger) or 30 (disgust/fear), no confidence intervals, standard errors, or statistical tests are reported for any benchmark result. The qualitative grounding analysis (Section 5.3) is conducted on an unspecified "randomly selected" subset with no systematic protocol, quantification, or sample size. The observation that "models fail to integrate visual cues" is directionally supported by the data, but the strength of the claim exceeds what the evidence supports given the small evaluation set and the absence of any statistical reliability measures.

### Minor

- **The claim that "current multimodal models fail to integrate visual cues" overgeneralizes from the evaluated models.** All four tested MLLMs (GPT-4o, AffectGPT, Qwen2.5-VL, MiniGPT4) are general-purpose models, none designed or fine-tuned for sign language understanding. The paper frames its evaluation as "baselines" (which is appropriate), but the abstract and conclusion use language suggesting a broader finding about "current multimodal models" generally, which is not fully supported by evaluating four models zero-shot on a single small dataset. Including at least one sign-language-specific model (e.g., LLaVA-SLT, cited in Related Work) would have made the comparison more informative.

- **The paper does not analyze why agreement is low for specific emotion categories (surprise_neg, disgust, frustration, etc.).** Is it because the cues are inherently ambiguous in these clips? Because the categories conflate multiple distinct expressions? Or because some clips genuinely contain blended emotions that annotators weigh differently? This analysis (even brief) would strengthen the dataset contribution and help users of the dataset understand which labels to trust.

- **Missing distribution of annotation counts per clip.** The paper notes "minimally 1, maximally 3" annotators per clip but does not report how many clips had fewer than 3 annotations. Clips with 1 or 2 annotations contribute noisier labels to the ground truth, and this could disproportionately affect certain emotion categories.

### Trivial

- None beyond what follows from the parser-stripped appendix (formatting artifacts in the extracted text are parser issues, not author errors).

## Nice-to-Haves

- **Broaden the VADER filter or remove it.** A stronger version of this paper would sample a broader range of ASLLRP utterances without pre-filtering by text sentiment, then analyze the relationship between text sentiment and visual emotion as a research question in itself. Alternatively, if the filter is retained, reframe the contribution as studying "emotion expression in ASL when the accompanying text is emotionally salient," which is a narrower but more defensible scope.
- **Add a fine-tuning experiment.** The paper repeatedly suggests models need adaptation for sign language, but does not show whether even simple fine-tuning (e.g., linear probing) on this dataset would improve performance. Such an experiment would directly validate the dataset's utility.
- **Include a comparison to a non-sign-language emotion dataset** (e.g., MELD) to clarify whether the poor video-only performance is specific to sign language or reflects general MLLM limitations in visual emotion recognition.
- **Report the number of clips skipped by annotators and why**, which would help assess annotation difficulty across emotions.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **Criticism that "no model is designed for sign language" implying the benchmark is invalid.** Removed because the paper frames these as *baselines* — zero-shot evaluation of general models is standard practice for establishing initial performance on a new dataset. The paper does not claim these models should work well on sign language. However, the overgeneralization from 4 models to "current multimodal models" is retained as a Minor weakness.

2. **Criticism that the paper lacks comparison to non-sign-language emotion datasets.** Moved to Nice-to-Have because this is a suggestion for strengthening, not a flaw. The paper's scope is sign language specifically.

3. **Criticism about missing related work.** Removed per instruction: I cannot verify missing references without external knowledge sources.

4. **Criticism about not reporting how many videos were discarded at each selection stage.** Removed as speculative — the paper describes its selection process at the level appropriate for a 9-page submission. This is a minor completeness issue at most.

5. **Strength about "Systematic pre-processing using VADER ensures emotional diversity while avoiding acted emotions"** from the Strength Finder. Removed because this strength conflicts with the verified weakness (VADER selection bias undermines the dataset's purpose). Per instructions, when a strength and weakness disagree, the weakness wins.

6. **Strength about "Inter-annotator agreement contextualized against MELD and IEMOCAP"** weakened because the metric comparison is not apples-to-apples (Krippendorff's alpha vs. Fleiss' kappa, different annotation setups). The paper does report it reasonably for context, but this is more limited than the Strength Finder claimed.

7. **Generic strengths about "addressing important problem" or "filling a critical gap"** without specific evidence anchor — removed as generic/superficial per filtering rules.

## Novel Insights

The most interesting emergent observation from synthesizing the reviews is that the paper's strongest contribution (qualitative emotion cue descriptions from native signers in Section 3.4) is almost orthogonal to its most criticized element (VADER text-filter selection). The qualitative analysis documents specific visual patterns — mouth morphemes, sign speed/size modifications, body shifts — that would be equally valuable regardless of how clips were selected, and this analysis is not undermined by the selection bias. This suggests the paper would be substantially stronger by positioning the qualitative findings as the primary contribution, with the benchmark as a secondary exploratory analysis, rather than the current framing where the benchmark is presented co-equally. The reviews collectively surface a disconnect between what the paper claims as its contribution (a comprehensive benchmark dataset) and what it actually delivers best (culturally-grounded documentation of emotion cues in ASL).

## Suggestions

1. **Reframe the contribution.** Make the qualitative analysis of emotion cues (Section 3.4) the centerpiece. The benchmark should be explicitly presented as an exploratory baseline, not as evidence for general claims about MLLM capabilities. Change "establishing baseline model performance" to "providing initial zero-shot results as a reference point."

2. **Address or remove the VADER filter.** Either broaden the selection to include neutral-text clips (even a modest expansion to 300-400 clips) and analyze the divergence between text sentiment and visual emotion as a research question, or explicitly reframe the dataset as "emotion expression in ASL when the accompanying text is emotionally salient."

3. **Discuss low-agreement emotion categories.** Add an analysis section on why surprise_neg (alpha=0.119) and disgust (alpha=0.166) have very low inter-annotator agreement. Is this a property of the stimuli, the category definitions, or annotation noise? Provide guidance for dataset users on which labels are reliable.

4. **Add confidence intervals to benchmark results.** With 200 samples, bootstrapped confidence intervals are straightforward to compute and would substantially improve the scientific value of the benchmark tables.

5. **Tone down the benchmark claims.** Replace phrases like "current multimodal models fail to integrate visual cues into emotional reasoning" with "the four general-purpose MLLMs we evaluated show limited ability to recognize emotions from sign language video alone in a zero-shot setting."

## Score and Decision

Now let me calibrate using the anchor comparisons.

**Round 1 bracket:** 3.5 – 5.5

**Anchor comparisons:**

| Anchor Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| TeacherActivityNet (TadxJc1XAE) | 3.00 (Reject) | R1 | Much weaker: small non-diverse dataset, trivial YOLO modification, no culturally competent annotation, no qualitative analysis. EmoSign is clearly stronger. |
| MDPE (EqCbc4wrzy) | 2.50 (Reject) | R1 | Weak deception dataset paper. EmoSign has better motivation, better annotation design, and addresses a clearer gap. EmoSign is stronger. |
| Representing Signs as Signs (flgrH5nK4H) | 4.00 (Reject) | R2 | Comparable level: addresses a real gap (one-shot ISLR) but limited methodological novelty and sparse comparisons. EmoSign has a clearer unique contribution (emotion annotations from Deaf signers) but similar-scale concerns about the dataset. EmoSign is slightly stronger on novelty but weaker on evaluation rigor. |
| VRG-SLT (7kRFnSFN89) | 5.00 (Reject) | R2 | Sign language translation paper with VQ-VAE + RAG. Mixed reviews (3,8,3,6). More technically sophisticated but had novelty/overclaiming concerns. EmoSign has clearer gap-filling novelty but is less technically complex. Similar tier. |
| OV-MER (f1uXrAjpOH) | 5.40 (Reject) | R1,R2 | Emotion recognition dataset + benchmark. Larger scale, novel task definition, but concerns about LLM annotation bias and evaluation leakage. EmoSign addresses a more concrete underexplored gap and has more culturally competent annotation, but is smaller in scale. OV-MER somewhat stronger overall. |
| Uni-Sign (0Xt7uT04cQ) | 6.40 (Accept) | R1 | Large-scale (1,985h) CSL dataset + unified framework. SOTA results across multiple benchmarks. EmoSign is not at this level in terms of scale, technical contribution, or evaluation breadth. |
| SignAvatars (L2kbdthX5M) | 6.25 (Reject) | R1,R2 | Large-scale 3D SL motion dataset (70K videos, 3D mesh annotations). Technical sophistication in pose estimation pipeline. EmoSign is substantially smaller scale and less technically ambitious. |

**Narrowing and final score:** The paper sits between the 4.00 (Representing Signs) and 5.40 (OV-MER) anchors. It is stronger than Representing Signs because it fills a clearer gap with culturally competent annotation and provides genuinely novel qualitative insights. It is weaker than OV-MER because of the VADER selection bias, smaller scale (200 vs. thousands of clips), weaker benchmark evidence, and lack of confidence intervals. The VADER bias is a genuine structural issue that prevents the paper from being a strong contribution. The qualitative cue analysis is genuinely novel but currently plays a secondary role. **Final score: 4.5** — the paper has real merit in addressing an underexplored gap with culturally appropriate methodology, but the VADER selection bias and the gulf between its ambitious claims and the evidence provided prevent it from being a strong paper.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>