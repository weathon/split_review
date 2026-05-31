## Summary

EmoSign is a multimodal dataset of 200 ASL video clips annotated for sentiment (7-point Likert scale), 10 emotion categories (0–3 intensity), and free-text descriptions of emotion cues. Annotations were performed by 3 Deaf native ASL signers with professional interpretation experience. The paper benchmarks four multimodal LLMs (GPT-4o, AffectGPT, Qwen2.5-VL, MiniGPT4) on sentiment analysis, emotion classification, and qualitative emotion cue grounding tasks, demonstrating that current models fail to exploit visual cues and over-rely on text captions.

---

## Strengths

- **Genuine first-of-its-kind contribution**: No prior ASL dataset captures fine-grained sentiment, multi-category emotion intensity, *and* qualitative cue descriptions from Deaf native signers. FePh (the closest prior work) used hearing annotators, face-cropped video, and binary labels—EmoSign addresses all three deficiencies.

- **Culturally appropriate annotation methodology**: Recruiting Deaf native signers with professional interpretation expertise to distinguish grammatical from affective facial expressions is the correct design choice and is well-justified by existing literature on hearing-person misinterpretation of ASL cues (Lim et al., 2024).

- **Respectable inter-annotator agreement**: Average Krippendorff's α = 0.593 exceeds reported Fleiss' κ values for MELD (0.43) and IEMOCAP (0.48), which are widely used benchmarks in the field.

- **Multimodal ablation design reveals meaningful insights**: The three-way ablation (caption-only / video-only / video+caption) cleanly demonstrates that MLLMs are unable to ground emotions in visual ASL cues, with video-only performance often worse than chance or heavily biased toward "happy/neutral." This finding is reproducible and practically important.

- **High practical significance**: Misinterpretation of ASL signers' affect in legal and emergency-care settings has documented real-world harms; a dedicated benchmark motivates targeted research.

---

## Weaknesses

### Fatal
None.

### Major

1. **Dataset scale critically limits benchmark reliability.** The final corpus is 200 utterances (~16 minutes) from only 4 signers (one source dataset, ASLLRP). Emotion categories with already-sparse labels—surprise_neg (α = 0.119), disgust (α = 0.166), anger, fear (~25–30 clips each)—yield per-class accuracy estimates based on 7–30 test samples. Confidence intervals on these numbers are so wide that rank-ordering model performance per emotion (Table 4) is largely noise. The authors cite three similarly-sized benchmark papers to justify scale, but those are in domains where a single source provides diverse instances; 4 ASL signers is a severe coverage constraint.

2. **VADER-based selection introduces a systematic confound.** Videos were chosen by selecting the 100 highest and 100 lowest VADER text-sentiment utterances from ASLLRP. This procedure creates a corpus where the English captions are *by construction* emotionally extreme. When the "video-only" models perform poorly while the "caption-only" and "video+caption" models perform better, a natural explanation is that these particular videos were selected precisely because their textual content is unambiguously emotional—inflating the apparent text-modality advantage. The paper acknowledges in §6 that VADER results often differed from annotators' visual judgments, but does not analyze whether this confound affects the benchmark conclusions.

3. **Only 3 annotators with majority-vote aggregation.** For 10 separate emotion dimensions, a majority vote among 3 annotators resolves to a 2-vs-1 decision most of the time. This leaves ground-truth labels especially fragile for low-IAA categories (surprise_neg, disgust, frustration), where the "correct" label may reflect a single annotator's judgment.

### Minor

1. The emotion cue grounding evaluation (§5.3) is entirely qualitative—a manual inspection of "several randomly selected videos." No quantitative metric is provided, making this section essentially anecdotal and not reproducible as a benchmark.

2. The multi-label emotion classification task is mentioned as a benchmark task but is not actually evaluated. Reporting this as a limitation is appropriate, but it leaves the paper's benchmark section incomplete.

3. The single-expression classification task excludes multi-expression clips (37 of the 200 clips are removed), and the filtering further removes "combinations only present in a single sample," potentially shrinking per-class counts to near-zero. The extent of this reduction is not stated explicitly in the main text.

### Trivial
None worth listing.

---

## Nice-to-Haves

- A quantitative grounding metric (e.g., IoU over annotated face regions or temporal precision/recall) would substantially strengthen §5.3 and make the grounding task reproducible.
- Analysis of whether VADER-selected clips skew the text-modality advantage would help readers calibrate the benchmark conclusions.
- Reporting confidence intervals or bootstrap standard errors on per-class accuracy given small sample counts would improve interpretability of Table 4.

---

## Novel Insights

Beyond the paper's own contributions, the ablation design surfaces one genuinely interesting behavioral pattern: in the video+caption condition, several models reconstruct visual evidence post-hoc to be consistent with text sentiment (the same cue—e.g., hand trajectory—is described as anxious in video-only but energetic in video+caption for the same clip). This mode of "caption-guided confabulation" of visual evidence is a specific and concrete failure mode for MLLMs on non-verbal communication data, distinct from mere caption reliance, and it suggests a potential evaluation methodology for probing visual grounding fidelity in multimodal models more broadly.

---

## Suggestions

- Expand the corpus to at least 500–1,000 utterances across more than 4 signers before the final version; even including the full ASLLRP corpus with neutral clips annotated at lower cost would improve benchmark robustness.
- Provide a stratified split of the 200 samples or bootstrap confidence intervals on reported metrics so readers can interpret per-class accuracy numbers.
- Quantify the VADER confound: compute the correlation between VADER text sentiment and annotator sentiment scores, and analyze whether text-modality performance advantage is larger for videos where VADER and annotator scores agree.
- Add at least one quantitative evaluation for the grounding task, even if approximate (e.g., proportion of model-mentioned cues that match annotator-described cues by keyword matching).

---

## Score and Decision

EmoSign makes a genuine and well-motivated contribution to a neglected area—ASL affect recognition—with a sound annotation methodology and useful preliminary benchmarks. The core finding (MLLMs rely on captions rather than visual cues for ASL emotion) is credible and actionable. However, the dataset scale (200 clips, 4 signers) and the VADER-induced selection bias significantly limit the reliability and generalizability of the benchmark conclusions. Several reported per-class metrics are based on fewer than 15 test samples, rendering them uninformative. For a top ML venue whose audience will use this as a benchmark for future model development, these limitations are consequential enough to warrant revision.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>