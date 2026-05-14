Here is my final consolidated review.

---

## Summary

EmoSign introduces the first ASL video dataset annotated for sentiment, emotion categories, and open-ended emotion cue descriptions by Deaf native ASL signers with professional interpretation experience. The dataset comprises 200 utterances (≈16 minutes of video) from the ASLLRP corpus, annotated by three signers across 10 emotion categories with a 7-point sentiment scale. The paper benchmarks four multimodal LLMs (GPT-4o, AffectGPT, Qwen2.5-VL, MiniGPT4) on three tasks, finding that models perform near chance in video-only conditions and rely heavily on text captions.

## Strengths

- **First ASL dataset with fine-grained emotion/sentiment labels and qualitative cue descriptions annotated by Deaf native signers.** Table 1 shows EmoSign is the only ASL corpus that includes emotion and sentiment labels alongside open-ended cue descriptions. The annotation was performed by three Deaf native ASL signers with professional interpretation experience (Section 3.2), directly addressing a genuine gap in sign language resources. The open-ended cue descriptions (Section 3.4) document how emotions manifest through non-manual markers, sign modifications, and role/context — qualitative insights that no prior dataset offers.

- **Systematic ablation across three input conditions reveals a consistent pattern of model reliance on text.** The benchmark design (caption-only, video-only, video+caption) across Tables 3 and 4 produces a coherent picture: all four models perform near chance in video-only conditions, and video+caption does not substantially outperform caption-only. This pattern is consistent across models despite different prompting strategies, strengthening the finding that current MLLMs fail to meaningfully integrate visual emotional information from sign language videos.

- **Identification of reproducible model biases (positive sentiment bias, defaulting to "neutral" or "happy").** Section 5.1 documents specific failure modes: AffectGPT consistently outputs "Neutral" in video-only conditions, GPT-4o and Qwen2.5 skew positive, and MiniGPT4 defaults to "happy" even for negative ground truth. These documented biases are valuable for future work on debiasing multimodal emotion recognition.

- **Valuable qualitative documentation of emotion cues from native signer perspectives.** The synthesis of annotator descriptions (Section 3.4) into three common themes — non-manual markers, sign modifications, and role/context — provides a foundation for understanding how emotion is visually expressed in ASL, separate from grammatical functions.

## Weaknesses

### Major

- **VADER-based selection confounds the paper's central claim about model failure to use visual cues.** The dataset was constructed by selecting the 100 most positive and 100 most negative utterances based on *text caption* sentiment scores from VADER (Section 3.1). This means every video was chosen because its English caption expressed strong emotion, not because the visual signing contains discernible emotional cues. The paper's core claim — that "current multimodal models fail to integrate visual cues into emotional reasoning" — is weakened by this confound: we cannot cleanly distinguish between "models cannot use visual emotion cues in ASL" and "these particular videos do not contain strong visual emotion cues." The paper acknowledges that "VADER results differed from the annotators' results" (Section 6), which actually supports the concern. While the annotators could identify visual cues (suggesting some visual content exists), the experimental design does not control for this confound, and the near-chance video-only results are exactly what one would expect if the visual content is emotionally ambiguous. This is the most consequential weakness in the paper.

- **Very small dataset size limits generalizability and benchmark reliability.** With only 200 utterances from 4 signers, drawn from a single lab-controlled corpus (ASLLRP), the dataset is orders of magnitude smaller than most ASL datasets (Table 1). The single-expression emotion classification subset used for the key benchmark is only 140 clips. No confidence intervals, standard errors, or statistical significance tests are reported. With this sample size, reported accuracy differences between conditions (often single-digit) fall within random variation. The paper acknowledges the size limitation ("Considering the cost of time and budget, we start with 200 utterances") but the benchmark conclusions are presented without the statistical caution this sample size demands.

- **Low inter-annotator agreement on several emotion categories makes those ground-truth labels unreliable.** Krippendorff's alpha for surprise-negative is 0.119, disgust = 0.166, frustration = 0.330, and several others are below 0.38 (Table 2). These values are in the "poor agreement" range by conventional standards. The paper's comparison to MELD (Fleiss' kappa = 0.43) and IEMOCAP (Fleiss' kappa = 0.48) is informative but uses different metrics on different scales, making direct comparison inexact. The emotion classification benchmark (Table 4) relies on majority-vote labels from these annotations; with only 3 annotators, majority vote cannot recover reliable signal when two annotators disagree systematically. The reported 0% accuracy for several emotions under video-only may partly reflect noisy labels rather than model failures.

### Minor

- **Different prompting strategies across models create a confound in benchmark comparisons.** GPT-4o receives a single structured prompt covering all three tasks simultaneously (Appendix A.3), while AffectGPT, Qwen2.5, and MiniGPT4 are tested with separate, simpler prompts for each task (Appendix A.4). The paper transparently explains this (the open-source models "were unable to consistently produce clean output when prompted to respond to all three benchmark tasks at once"), but it means performance differences between models are partially confounded with prompt design. The main conclusion (models rely on text) is consistent across all models despite this, but fine-grained model comparisons are not clean.

- **Emotion cue grounding task receives only qualitative evaluation.** The paper lists grounding as one of three benchmark tasks (Section 4.1) but provides no quantitative evaluation — only a manual analysis of a few examples (Section 5.3). The paper frames this as "preliminary understanding" but still presents it as a benchmark task alongside the others, which is misleading.

- **The 10 fps sampling justification relies on a motion-capture study.** The paper cites Bigand et al. (2021) for the claim that "there is no significant intelligibility loss for ASL isolated signs from 30 to 10 fps." The cited reference studies kinematic bandwidth using motion capture data, not video-based emotion recognition. Generalizing from motion capture to visual sampling rates for emotion perception is a stretch.

### Trivial

- Minor: The paper reports MiniGPT4 caption-only sentiment achieving wAcc of 1.92 and wF1 of 5.92 on 3-class, and 0.00 on 7-class — performance *below* random baseline. This is not contextualized with chance-level comparisons.

## Nice-to-Haves

- Validation of visual emotion content in selected videos (e.g., correlation between annotator-reported visual cues and their labels) would directly address the VADER confound concern.
- Finetuning even a small sign-language-specific model on the dataset would strengthen claims about utility.
- An analysis of how many caption texts contain explicit emotion words (e.g., "upset", "happy") that enable keyword-matching solutions would contextualize the caption-only results.

## Removed Points

These points are flagged to be removed; treat them with caution:

- Criticism about FePh comparison being unfair or that the paper overstates novelty relative to FePh: The paper acknowledges FePh and provides specific, well-reasoned differences (face-only cropping, hearing annotators, binary labels only). This is legitimate differentiation.
- Criticism that the Krippendorff's alpha vs. Fleiss' kappa comparison "is not meaningful": Both are chance-corrected agreement measures; the comparison is imperfect but still informative as contextualization. This is weakened but not entirely removed — kept as an observation in the Major weakness section.
- Criticism about missing fine-tuning experiments: The paper explicitly lists this as future work (Section 6), which is appropriate for a dataset paper.
- Criticism about the grounding task not having quantitative evaluation: The paper does acknowledge this limitation implicitly by calling it "preliminary," but it remains listed as a minor weakness above.
- Claim that "performance differences between models are therefore confounded with prompt design" — this is a genuine concern and kept in Minor weaknesses.
- The strength finder's "High-quality annotations with inter-annotator agreement comparable to or exceeding existing datasets" — this conflicts with the verified weakness about low alpha for several emotions. The weakness wins; the comparison is informative but the low-agreement emotions are a real problem.

## Novel Insights

None beyond the paper's own contributions. The key tension that emerges from this review is that the paper's most interesting finding (models fail to use visual emotional cues in ASL) is itself compromised by the selection methodology that may have produced videos where the visual channel is emotionally ambiguous. This is a novel methodological insight: when constructing an emotion dataset for a visual language by filtering on text sentiment, one inadvertently creates a dataset that cannot cleanly answer questions about visual emotion understanding.

## Suggestions

1. **Address the VADER confound directly**: Provide an analysis showing that the selected videos do contain visually identifiable emotional content (e.g., annotator confidence distributions, correlation between visual cue descriptions and labels, examples of videos with strong vs. weak visual cues). This is essential to support the claim that models fail on visual emotion understanding rather than on visually neutral content.

2. **Add uncertainty estimates and baselines**: Report bootstrapped confidence intervals for all benchmark results, especially given the small sample size (140 clips for emotion classification). Include random-guess and majority-class baselines.

3. **Restrict or caveat the emotion categories with low agreement**: Either exclude emotions with Krippendorff's alpha below a reasonable threshold (e.g., 0.33) from the benchmark, or clearly state which labels are unreliable and discuss the implications.

4. **Expand the dataset or reframe the contribution**: The 200-utterance, 4-signer scale is appropriate as a pilot or proof-of-concept, but the paper's claims (e.g., "first comprehensive dataset") and conclusions would be better served by either (a) substantially expanding the dataset before publication, or (b) reframing the paper as a pilot study with appropriately scaled claims.

5. **Standardize prompting across models**: If possible, use identical prompting strategies for all models; if architecture constraints prevent this, clearly flag the confound in the analysis and avoid fine-grained cross-model comparisons.

## Score and Decision

**Calibration anchors** (all from ICLR 2026 human-reviewed papers):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| BANZ-FS (GMR9BUsPbq) | 7.00 | Sign language dataset with 35k+ instances, multiple sources, comprehensive — far larger scale and stronger execution |
| VideoReasonBench (1Mblo6U8kp) | 5.50 | Well-designed benchmark, 18 models evaluated, strong task design — better scoped and executed |
| LexSign (mOFGOK6Vmo) | 4.50 | Sign language dataset + benchmark, rejected for writing issues and missing details — similar structure but larger scale |
| HandReader (OGvXBluCHd) | 3.50 | Method paper with SOTA results, missing ablations — comparable quality tier |
| EmoDialogCN (KkuINI7YJz) | 3.33 | Large-scale emotion dataset (400h) but methodological gaps — much larger but less unique annotation |
| EmotionTalk (U7qDPmezw7) | 2.67 | Chinese emotion dataset, 23.6h — criticized as mostly dataset with limited novelty |
| HumanVideo-MME (joh5J1nYAE) | 2.50 | Benchmark with weak justification — comparable weakness level |
| BdSL-SPOTER (mUqgxqe8XK) | 1.50 | Incomplete paper with missing content — EmoSign is better executed |

EmoSign sits between LexSign (4.50, rejected) and HandReader/EmoDialogCN (3.3-3.5) on the quality spectrum. It has a genuine and well-motivated contribution — the first emotion-labeled ASL dataset with native Deaf signer annotations and qualitative cue descriptions — but is held back by three interconnected problems: very small scale (200 utterances, 4 signers), a VADER-based selection procedure that confounds the paper's central experimental claim, and unreliable ground truth for several emotion categories. These are structural issues that cannot be fully resolved in a rebuttal.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>