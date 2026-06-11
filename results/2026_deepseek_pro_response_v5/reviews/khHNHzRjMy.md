Now I have a clear picture from the calibration. Let me finalize the review.

**Bracket analysis:**

Round 1 bracketing placed EmoSign between ~4.5 and ~6.0. The strong reject anchors (1.67-2.33) had fundamentally flawed methodology. The weak anchors (3.33-4.33) had more substantial problems than EmoSign. The middle anchors established that 6.0 was the accept threshold (MMWorld), with everything below rejected.

Round 2 narrowed this: EmoSign compares favorably to MMToM-QA (4.75) — which had unfair baselines and synthetic domain gap — but is below OV-MER (5.40), a more ambitious emotion recognition dataset paper with its own issues. EmoSign's VADER confound (partially undermining quantitative claims), small scale, and the fact that emotion cue grounding isn't truly a benchmark place it around 5.0, between these two anchors.

---

## Summary

EmoSign introduces the first ASL video dataset with emotion and sentiment labels: 200 utterances from ASLLRP, annotated by 3 Deaf native ASL signers with professional interpretation experience. Each video receives sentiment ratings (7-point scale), 10-category emotion intensity ratings, and free-text descriptions of visual emotion cues. The paper benchmarks four multimodal LLMs under caption-only, video-only, and video+caption conditions on sentiment analysis, emotion classification, and qualitative emotion cue grounding, finding that models over-rely on text and perform poorly on vision-only emotion recognition.

## Strengths

- **Deaf native ASL signer annotators**: Using Deaf native signers with professional interpretation experience (Section 3.2) is the most important methodological choice in the paper, directly addressing the documented problem that hearing individuals systematically misinterpret signers' facial expressions due to the dual grammatical/emotional function of non-manual markers (Lim et al., 2024). This distinguishes EmoSign from prior work like FePh, which used hearing annotators.

- **Multi-condition modality ablation isolating text dominance**: The three-condition design (caption-only, video-only, video+caption) in Section 4.2 cleanly reveals modality reliance. Table 3 shows video-only sentiment performance is uniformly poor (GPT-4o wF1 = 5.97 on 7-class), while Table 4 shows caption-only emotion classification often matches or exceeds video+caption (GPT-4o wF1: 55.89 caption-only vs. 55.09 video+caption), providing clear evidence of text over-reliance.

- **Rich, multi-layered annotation schema**: The three annotation layers per video — 7-point sentiment, 10-category emotion intensity with 0–3 scale, and free-text cue descriptions (Section 3.2) — go substantially beyond FePh's binary presence/absence labels. The open-ended cue descriptions enable the thematic synthesis in Section 3.4 of how emotions manifest through facial expressions, sign modifications, and contextual markers — independently valuable documentation.

- **Transparent per-label agreement reporting**: Table 2 reports Krippendorff's alpha for every individual label, honestly revealing low agreement on difficult categories (surprise_neg: 0.119, disgust: 0.166) alongside higher values (sentiment: 0.738, joy: 0.699). This transparency is commendable and unusual.

- **Qualitative analysis revealing text-driven reinterpretation of visual cues**: Figure 3 demonstrates a specific mechanism: models reinterpret identical visual cues in opposite emotional directions depending on caption availability. MiniGPT4 interprets the same signing as joyful without captions but as conveying concern with captions. The observation that Qwen2.5 claims "the exact content of the sign language cannot be determined without audio" documents a fundamental model misunderstanding worth recording.

- **Systematic positioning against existing ASL datasets**: Table 1 comprehensively compares EmoSign against six prior ASL datasets across size, signer fluency, source, and label types, making the gap it fills unambiguous.

## Weaknesses

### Fatal

None.

### Major

- **VADER-based selection creates a circularity that partially undermines the sentiment benchmark findings**: The dataset was constructed by running VADER on English captions and selecting the 100 most positive and 100 most negative utterances (Section 3.1). This means text captions are predictive of the sentiment polarity around which the dataset was built. The finding that caption-only performance is competitive on sentiment analysis (Table 3) is therefore at least partially a construction artifact — captions carry the same signal used to select videos. The paper acknowledges in Section 6 that "VADER results differed from the annotators' results" but never quantifies this divergence (e.g., correlation between VADER scores and final annotator sentiment labels), leaving the reader unable to assess how much of the caption-only performance reflects the selection procedure vs. genuine linguistic emotion recognition. This primarily affects interpretation of the sentiment benchmarks; the emotion classification results (where VADER only guaranteed polarity, not specific emotion categories) and the qualitative findings (Section 5.3) are less impacted.

### Minor

- **Low inter-annotator agreement on several emotion categories limits per-category benchmark reliability**: Krippendorff's alpha for surprise_neg (0.119), disgust (0.166), sadness (0.333), frustration (0.330), and fear (0.351) are below commonly accepted thresholds. While the paper is transparent about this (Table 2), the low agreement means per-category accuracies in Table 4 for these categories are noisy. The paper's main claims about modality reliance do not hinge on specific per-category performance, so this does not invalidate core findings, but it limits the benchmark's usefulness for fine-grained emotion recognition.

- **Emotion cue grounding is presented as a benchmark but delivered as qualitative anecdotes**: Section 4.1 lists emotion cue grounding alongside sentiment analysis and emotion classification as a benchmark task, but Section 5.3 provides only manual inspection of "several randomly selected videos" with no quantitative metrics, systematic protocol, or reproducible evaluation criteria. The paper is honest that this is a "preliminary understanding" (line 284), but the framing overstates what is provided. The qualitative findings themselves (Figure 3) are genuinely insightful.

- **Small dataset with limited signer diversity**: With 200 utterances from only 4 signers (Section 3.4), individual signer idiosyncrasies could influence results. The paper acknowledges size constraints (line 87: "Considering the cost of time and budget, we start with 200 utterances") and notes similarly-sized datasets have proven valuable for benchmarking, but the limited scale and signer pool remain practical limitations for training or fine-tuning.

### Trivial

- The paper contextualizes its Krippendorff's alpha against MELD and IEMOCAP, which report Fleiss' kappa. While both measure inter-rater agreement and the directional comparison is informative, the metrics are not numerically identical, making the direct numerical comparison imprecise.

## Nice-to-Haves

- Report the correlation between VADER scores and final annotator sentiment labels (e.g., Spearman correlation) so readers can directly assess the severity of the construction confound.
- Report per-signer performance breakdowns to understand whether individual signer characteristics drive variance in results.
- Leverage the collected annotator confidence scores (Section 3.2) to filter evaluations to high-confidence samples, mitigating noise from low-agreement emotion categories.
- Develop a systematic evaluation protocol for emotion cue grounding — even a small-scale quantitative comparison using the cue descriptions from Deaf annotators (Section 3.4) as reference would strengthen this into a proper benchmark.
- Report or explain the absence of results for the multi-expression subset (37 clips, mentioned in Section 4.1).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic: "10 fps sampling rate may not be optimal for continuous signing with emotional expression"** — REMOVED. The paper explicitly justifies 10 fps by citing Bigand et al. (2021) (line 217): "no significant intelligibility loss for ASL isolated signs from 30 to 10 fps, and most of the energy of SL motion may lie below 6 or 7 Hz." This is a substantiated choice, not an oversight.

- **Harsh Critic: "The introduction promises a disentanglement challenge the paper does not engage with empirically"** — REMOVED. The paper's introduction describes the dual grammatical/emotional function of facial expressions as motivation for why emotion recognition in ASL is uniquely difficult, not as a promise to operationalize disentanglement as a benchmark task. The benchmarks are appropriately scoped to emotion recognition. The framing is motivational context, not a gap between promise and delivery.

- **Harsh Critic: "The paper should report what proportion of ASLLRP utterances were considered and the full distribution of VADER scores"** — REMOVED as a standalone criticism. This is folded into the Major weakness about the VADER confound and the Nice-to-Have about reporting VADER-annotator correlation.

- **Strength Finder: generic strengths about "the problem is important" or "the gap is genuine"** — REMOVED. These are not concrete contributions specific to this paper.

## Novel Insights

The paper's qualitative analysis (Figure 3) reveals a specific failure mode in multimodal LLMs that goes beyond aggregate metrics: when the same video is shown with vs. without captions, models reinterpret identical visual cues in opposite emotional directions to align with the text. This is a sharper, more mechanistic finding than "models over-rely on text" — it shows that text doesn't just dominate, it actively rewrites the visual interpretation. Additionally, the finding that Qwen2.5 asserts sign language comprehension requires audio reveals a fundamental conceptual gap in model training that documentation like this can help address. These observations have implications beyond sign language for how we understand multimodal model reasoning.

## Suggestions

- Center the qualitative analysis (Section 5.3, Figure 3) more prominently. The finding that models reinterpret identical visual cues based on caption availability is the paper's strongest and most defensible contribution — more so than the quantitative benchmarks, which are partially entangled with the VADER selection procedure.
- Add a simple quantitative diagnostic: report the Spearman correlation between VADER sentiment scores and final annotator sentiment labels on the 200 videos. This would allow readers to directly assess the construction confound.
- For the emotion cue grounding task, either develop a systematic evaluation protocol (even on a subset) or relabel it in Section 4.1 as "qualitative analysis" rather than a "benchmark task" to accurately reflect what is provided.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| R-KinetiQuery (lMW9d1AqC9) | 1.67 | R1 | Sign language to SQL — fundamentally flawed methodology, clearly worse |
| Multimodal Class-Incremental Learning (gNoqEdT2wO) | 2.33 | R1 | Benchmark with significant design issues, clearly worse |
| KidSat (JEmNgjuQHU) | 2.00 | R1 | Satellite imagery dataset, different domain, clearly worse |
| M4U (GVNYi74t5L) | 4.25 | R1 | Multilingual benchmark with validity issues, EmoSign has stronger annotation |
| Multimodal Continual Learning (Pa6SiS66p0) | 4.33 | R1 | CL benchmark, EmoSign has clearer contribution |
| OV-MER (f1uXrAjpOH) | 5.40 | R2 | Most directly comparable — emotion recognition dataset; more ambitious scope but data leakage issues; EmoSign is slightly weaker due to smaller scale and VADER confound |
| MMToM-QA (sMFqEror1b) | 4.75 | R1 | Multimodal ToM benchmark with unfair baselines; EmoSign has more rigorous annotation and clearer gap |
| MMWorld (tRNKe2Vgqt) | 6.00 | R1 | Large-scale video benchmark, accepted; EmoSign is clearly weaker on scale and benchmark validity |
| LVBench (uHgVrGF2Wn) | 4.50 | R2 | Long video benchmark; EmoSign fills a more specific and important gap |
| TemporalBench (Wto5U7q6I2) | 4.20 | R2 | Temporal understanding benchmark; EmoSign has clearer contribution and better qualitative findings |
| Motion-Grounded Video Reasoning (tEei1bolt3) | 5.00 | R2 | Video reasoning benchmark with motion grounding; comparable quality level |

**Round 1 bracket**: 4.5–6.0. The paper is clearly above the strong-reject anchors (1.67–2.33) and weak anchors (3.33–4.33), and clearly below the strong anchors (7.5+). It sits among the middle-range dataset/benchmark papers.

**Round 2 narrowing**: EmoSign is comparable to Motion-Grounded Video Reasoning (5.00) and slightly better than MMToM-QA (4.75) due to more rigorous annotation and a clearer contribution, but below OV-MER (5.40) due to smaller scale and the VADER confound partially undermining quantitative results. The accept threshold for comparable benchmark papers is ~6.0 (MMWorld), which EmoSign does not reach.

Final score: 5.0 — a weak reject. The dataset fills a genuine gap and the qualitative analysis is genuinely insightful, but the VADER confound, small scale, and the gap between claimed and delivered benchmarks prevent acceptance in current form.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>