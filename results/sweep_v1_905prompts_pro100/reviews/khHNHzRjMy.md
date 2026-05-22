Now I have enough data to calibrate. Let me synthesize my analysis.

**Round 1 Bracket:** Based on anchors — OV-MER (5.40, similar emotion dataset+benchmark), EmpathyRobot (6.00, first-of-its-kind dataset+benchmark), M4U (4.25, MLLM benchmark), VL-ICL Bench (6.50, MLLM benchmark) — this paper plausibly sits in the **4.5–6.0** range.

**Round 2 Narrowing:** OV-MER at 5.40 is the closest comparison (emotion dataset + benchmark, some evaluation limitations). EmpathyRobot at 6.00 had more data and more comprehensive evaluation but was criticized as incremental. Our paper has less data but a more genuinely novel domain (ASL is truly underexplored). I place it at **5.5**, slightly above OV-MER due to stronger domain novelty and annotation quality, but below EmpathyRobot due to smaller scale and less comprehensive evaluation.

Now let me write the review.

---

Before writing, let me verify each harsh critic claim against the paper:

**HC #1 - No train-test split:** The paper evaluates four pre-trained MLLMs in zero-shot fashion. There is no model training. The entire dataset of 200 videos serves as the test set. This is standard for zero-shot benchmarking. The criticism is largely a misunderstanding. REMOVE the fatal framing but retain the valid sub-point about no confidence intervals as Minor.

**HC #2 - Dataset size and selection bias:** The paper acknowledges VADER selection in Section 6. 200 examples with selection bias is a real limitation for a benchmark. KEEP as Major.

**HC #3 - Emotion cue grounding not quantitative:** The paper calls it a benchmark task but only provides qualitative analysis. The paper itself says "preliminary understanding" — it's partially self-aware. KEEP as Minor — the paper frames it as a task but doesn't quantitatively evaluate it, which is a presentation/claim issue.

**HC #4 - Low IAA:** This is a real issue. α of 0.119 for surprise_neg and 0.166 for disgust means those categories' ground truth is unreliable. KEEP as Major.

**Section notes on merging joy/excited:** Minor, keep.

**Section notes on introduction promising more:** The introduction mentions disentangling grammatical vs emotional functions. The paper doesn't operationalize this in benchmarks. Keep as Minor.

Now for the Strength Finder:

**Strength 1 - Deaf native signer annotation:** Well-supported by Section 3.2, Table 2. Genuine strength. KEEP.

**Strength 2 - Benchmark exposing model failure on visual cues:** Well-supported by Tables 3-4. KEEP.

**Strength 3 - Cue grounding analysis with Figure 3:** Interesting and well-illustrated. KEEP but note it's qualitative.

**Strength 4 - Annotation pipeline with confidence and justifications:** Valid, KEEP.

**Strength 5 - Transparent VADER selection discussion:** Valid, KEEP.

**Strength 6 - Qualitative themes from annotator descriptions:** Valid, KEEP.

Let me now write the full review.Now let me write the consolidated review.

---

## Summary

EmoSign introduces the first ASL video dataset annotated with sentiment, emotion labels, and free-text cue descriptions, all provided by Deaf native ASL signers with professional interpretation experience. The dataset comprises 200 utterances (~16 minutes) drawn from the ASLLRP corpus, pre-selected via VADER for emotional salience. The paper benchmarks four multimodal LLMs (GPT-4o, AffectGPT, Qwen2.5-VL, MiniGPT4) across three input conditions (video-only, caption-only, video+caption) on sentiment analysis and emotion classification, finding that current models fail to extract emotional information from visual signing cues and over-rely on text captions.

## Strengths

- **Genuinely novel dataset filling a clear gap.** Table 1 convincingly demonstrates that no existing ASL dataset provides emotion or sentiment labels. The combination of sentiment ratings, 10 emotion categories with intensity, and free-text cue descriptions — all from Deaf native signers — is unique and directly addresses a well-motivated need in both sign language research and multimodal emotion recognition.

- **Annotation quality and depth.** The use of three Deaf native ASL signers with professional interpretation experience is a significant methodological strength that distinguishes this work from prior efforts (e.g., FePh used hearing annotators). The annotation pipeline captures not just labels but also annotator confidence (0–100 scale) and open-ended justifications, yielding a richer dataset than simple categorical labeling. The Krippendorff's α of 0.593 on average, with sentiment agreement at 0.738, is reasonable for emotion annotation and compares favorably to widely-used benchmarks like MELD and IEMOCAP.

- **Benchmark results reveal a clear and important signal.** Tables 3 and 4 demonstrate a consistent pattern: video-only performance is near-chance (AffectGPT defaults to neutral; GPT-4o defaults to happiness/frustration), caption-only is strong, and video+caption sometimes *worse* than caption-only for emotion classification. This directly supports the paper's central claim that current MLLMs cannot integrate visual emotional cues from signing — they rely on text shortcuts. This is a substantive empirical finding with implications beyond ASL.

- **Transparent handling of limitations.** The paper openly discusses the VADER selection bias, the controlled lab setting of ASLLRP, and the absence of multi-label evaluation (Section 6). This transparency strengthens credibility.

- **Qualitative cue themes provide reusable insights.** The distillation of annotator descriptions into themes (facial expressions, sign modifications, contextual disambiguation) in Section 3.4 gives concrete guidance for future model design.

## Weaknesses

### Major

- **Small, selection-biased dataset limits benchmark generality.** The 200 utterances (≈16 minutes, 4 signers) were filtered by VADER to the 100 most positive and 100 most negative captions. While the paper acknowledges this in Section 6, the consequences for benchmarking are underdiscussed. Zero-shot evaluations on this narrow, distributionally-shifted set may produce idiosyncratic performance patterns — e.g., the video+caption vs. caption-only comparison may partly reflect VADER's text-level sentiment signal rather than genuine multimodal integration. A dataset of this size also cannot support training or fine-tuning, which bounds its utility for future work. The paper cites comparably small datasets (Arodi et al., 2024; Krojer et al., 2024) that have proven valuable, but those address different problem settings where small expert-annotated sets are the norm.

- **Low inter-annotator agreement on several negative emotion categories undermines the emotion classification benchmark.** Krippendorff's α is 0.119 for surprise_neg, 0.166 for disgust, and below 0.4 for sadness (0.333), frustration (0.330), fear (0.351), and anger (0.370). Treating majority-voted labels as ground truth for these categories is questionable — the benchmark is measuring model performance against a noisy target. The paper compares its α to Fleiss' κ from MELD and IEMOCAP, but (a) these are different agreement statistics and (b) low scores in prior work do not make low scores here unproblematic. The emotion classification results (Table 4) should be interpreted with caution, especially per-class accuracy for low-agreement categories. The paper does not discuss how the reliability ceiling affects benchmark validity.

### Minor

- **Emotion cue grounding is presented as a benchmark task but evaluated only qualitatively.** Section 4.1 lists "Emotion Cue Grounding" as the third benchmark task, defining it as identifying "video frames and spatial regions relevant to sentiment analysis and emotion classification." Section 5.3 then reports "manual inspection of several randomly selected videos." There are no metrics, no quantitative comparison against the human-annotated cue descriptions, and no reproducible protocol. The analysis itself is interesting (Figure 3), but calling it a benchmark task overstates what was done. The paper should either provide a quantitative grounding protocol or reframe this as qualitative analysis.

- **No statistical reliability measures for benchmark results.** All metrics in Tables 3–4 are point estimates on 200 examples with no confidence intervals, bootstrapped standard errors, or any quantification of uncertainty. For a zero-shot benchmark intended for model comparison, some measure of statistical reliability would allow future work to determine whether score differences are meaningful. This is addressable with bootstrap resampling and does not require a train-test split.

- **Merging "joy" and "excited" into "happiness" is post-hoc and not fully justified.** The Jaccard similarity of 0.81 is high, but the paper should also report results on the original categories to verify that this simplification does not artificially inflate scores. The original annotation distinguished these for a reason.

- **The introduction promises disentanglement of grammatical vs. emotional facial expressions, but the benchmarks do not operationalize this challenge.** The tasks (sentiment analysis, emotion classification) are standard and do not require models to distinguish, e.g., raised eyebrows for yes/no questions from raised eyebrows indicating surprise. This is a gap between motivation and execution.

- **Multi-expression subset (37 clips) is acknowledged but not benchmarked.** Section 4.1 mentions separating the dataset into single-expression and multi-expression subsets, but only single-label classification is evaluated. Including even a simple multi-label evaluation would better reflect the real co-occurrence of emotions that signers reported and strengthen the paper's coverage.

### Trivial

- The paper mentions prompts are in Appendix A.3–A.4 (removed in this version); prompt sensitivity for GPT-4o is not discussed even qualitatively.
- Per-signer breakdown would help rule out signer-identity effects given only 4 signers.

## Nice-to-Haves

- Adding simple interpretable baselines (e.g., a VADER-only classifier on captions, or a pre-trained facial emotion recognizer on frame crops) would quantify how much signal the visual channel actually carries versus text alone, and would ground the claim that MLLMs fail to exploit available visual information.
- Bootstrapped confidence intervals on all metrics would significantly improve the benchmark's reusability for model comparison.
- Providing a fixed, documented evaluation protocol (even for zero-shot: exact prompts, API version, sampling parameters) would help future studies produce comparable numbers.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Harsh Critic #1: "No train–test split or cross-validation."** REMOVED as a fatal claim. The paper evaluates pre-trained MLLMs in zero-shot fashion — there is no model training, so the entire dataset is the test set. This is standard for zero-shot benchmarking. The valid sub-concern about lack of confidence intervals is retained as Minor.

- **Harsh Critic: "The paper does not mention whether GPT-4o was called separately for each video (incurring a cost)."** REMOVED. Cost is not a scientific concern, and Section 4.2 describes the inference setup adequately.

- **Harsh Critic: demands for train/validation/test split with stratification.** REMOVED. This misunderstands the zero-shot evaluation paradigm.

- **Strength Finder: generic claims about "addressing an important problem."** REMOVED — these are not concrete strengths specific to this paper.

- **Strength Finder: claims about "promising future work directions."** REMOVED — future work proposals are not evaluable strengths.

## Novel Insights

The benchmark results contain a genuinely counterintuitive finding: for emotion classification, providing video alongside captions can *reduce* performance compared to captions alone (Table 4 — GPT-4o wF1 drops from 55.89 (caption-only) to 55.09 (video+caption); Qwen2.5 wAcc is similar between conditions). This suggests that for current MLLMs, visual signing cues act as noise rather than signal when text is available, which is a stronger and more specific claim than the generic "models don't use visual cues." The Figure 3 analysis showing the same visual cue interpreted oppositely depending on caption availability provides a concrete mechanism for this failure: models use text to post-hoc rationalize visual observations rather than independently extracting emotional content from vision.

## Suggestions

- Reframe "Emotion Cue Grounding" as a qualitative analysis rather than a benchmark task, or provide a quantitative evaluation protocol (e.g., precision of model-identified frames against human-labeled temporal segments).
- Add bootstrap confidence intervals to all benchmark metrics for reusability.
- Report per-signer metrics (or at minimum check for signer effects) to verify the benchmark measures emotion understanding rather than signer identity.
- Discuss how low IAA for negative emotion categories affects the reliability of the emotion classification benchmark, and consider multi-label or soft-label evaluation to account for annotator uncertainty.
- Evaluate on the multi-expression subset to better match the dataset's own structure.

## Score and Decision

**Round 1 bracket:** 4.5–6.0 (anchored by OV-MER at 5.40, EmpathyRobot at 6.00).

**Round 2 narrowing:** OV-MER (5.40, Reject) is the closest structural match — a first-of-its-kind emotion recognition dataset + benchmark. Our paper has stronger domain novelty (ASL is truly underexplored vs. open-vocabulary MER), more careful annotation (Deaf native signers vs. LLM-assisted), but much less data and less comprehensive evaluation. EmpathyRobot (6.00, Reject) had 10K samples and fine-tuning experiments but was criticized as incremental. Our paper is more novel but smaller in scale. I place EmoSign at **5.5** — a genuine contribution with real novelty and interesting findings, but the small/biased dataset, low IAA on key categories, and overclaimed grounding task prevent a higher score.

**Anchor comparison summary:**
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| MDPE (EqCbc4wrzy) | 2.50 | R1 | Much weaker — poorly motivated deception dataset |
| MCIL (gNoqEdT2wO) | 2.33 | R1 | Much weaker — incremental benchmark with limited novelty |
| OV-MER (f1uXrAjpOH) | 5.40 | R1/R2 | Closest match. Similar structure, our paper has stronger domain novelty but smaller scale |
| EmpathyRobot (F6h0v1CTpC) | 6.00 | R1/R2 | Slightly stronger — 10K samples, fine-tuning, more comprehensive, but more incremental |
| VL-ICL Bench (cpGPPLLYYx) | 6.50 | R2 | Stronger — comprehensive, well-executed MLLM benchmark |
| PixelProse (UwbX8KOZgK) | 4.20 | R2 | Weaker — synthetic captions, less novelty |
| ScalePerson (3iGponpukH) | 4.75 | R2 | Weaker — narrower domain benchmark |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>