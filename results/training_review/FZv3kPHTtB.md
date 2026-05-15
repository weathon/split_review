Here is the final consolidated review:

---

## Summary

Shot2Story is a new multi-shot video understanding benchmark containing 20K web videos (10–40s) with shot-level visual and narration captions (human-verified from MiniGPT-4/GPT-4 bootstrapping) and full-video summaries averaging 202 words (human-verified from GPT-4). The paper defines four tasks — single-shot video captioning, single-shot narration captioning, multi-shot video summarization, and retrieval with shot descriptions — and provides baseline experiments. The core dataset contribution is genuine and fills a gap: no existing benchmark offers shot-level captions for both visual and audio modalities plus a long-form human-verified summary for multi-shot videos.

## Strengths

- **Comprehensive shot-level annotations with human verification**: The dataset provides separate visual and narration captions for every shot, plus a human-verified full-video summary (avg. 201.8 words). This is a clear step beyond prior benchmarks (MSRVTT, ActivityNet Caps, VAST) that lack either shot-structure, audio captions, or human verification (Table 1; Section 2.3–2.4). The annotation pipeline uses LLM bootstrapping with human correction, achieving realistic scale.

- **Empirical evidence that shot structure and ASR are important in summarization**: In the multi-shot summarization experiments (Table 4), SUM-shot (with shot structure + ASR, CIDEr 8.6) outperforms SUM-holistic (no shot structure, C 6.3) and SUM-shot w/o ASR (C 4.7). This directly supports the paper's claim that both shot boundaries and audio signals matter for multi-shot understanding.

- **Honest reporting of results**: The authors report that the two-stage pipeline (SUM-text, C 9.2) outperforms the end-to-end SUM-shot (C 8.6), and they acknowledge that "better model design needs to be explored." The weaknesses are visible rather than hidden.

- **Diverse task definitions**: The four proposed tasks collectively probe different aspects of multi-shot understanding (visual-only captioning, narration captioning, summarization, retrieval), creating a flexible testbed for future research.

## Weaknesses

### Fatal
None.

### Major

1. **Annotation quality is not quantified.** The paper relies on human correction of LLM-generated captions/summaries but provides no inter-annotator agreement statistics, no correction-rate analysis, no spot-check results, and no empirical measure of quality beyond the authors' assertions. Given that the paper contrasts itself with VAST (which "directly uses predicted captions without any human verification"), the lack of quality metrics for its own human-verification process is a significant gap for a dataset paper. Phrases like "review and correct" and "quality is assured" are not substitutes for empirical validation.

2. **The zero-shot QA evaluation has serious validity concerns.** (a) The GPT-3.5-based judge is not validated against human judgments or standard exact-match/F1 metrics, making the numerical results difficult to interpret. (b) Video-ChatGPT (V+T) is reported as 49.3 on MSRVTT-QA, whereas the original Video-ChatGPT paper reports 63.5 on the same dataset — a large discrepancy that the paper does not explain. (c) The claimed "transferability" rests on only two datasets, one of which (ActivityNet-QA) has a substantially different video length distribution (avg. 3 min vs. 16.7s). Absent a validated evaluation protocol, the QA results that the paper highlights as "surprisingly good" are not reliable evidence.

3. **Missing ablation for the summary-usefulness claim in QA.** The paper claims that "generated imperfect summaries can already significantly boost the performance … of video question-answering." However, no experiment isolates the contribution of the summary vs. raw shot captions. A controlled ablation that feeds shot-level captions (without summarization) into the same Vicuna model would directly test whether the summarization step adds value beyond the underlying caption data. The within-model comparison (Video-ChatGPT V+T 49.3 → Video-ChatGPT T 53.7) shows that using the summary helps Video-ChatGPT, but this does not isolate summarization from the fact that any informative text could produce the gain.

4. **The retrieval experiments do not demonstrate the dataset's unique value.** The baselines (Alpro, CLIP4clip, UMT) are evaluated zero-shot without any fine-tuning on the Shot2Story training split. None of them use shot-level information or ASR text. This measures general zero-shot transfer but does not show why the dataset's annotations — shot-level captions, narration captions, or ASR — are valuable for retrieval. The statement that ASR "presents an opportunity to harness ASR as a natural linkage" is unsupported speculation, as no experiment actually uses ASR in retrieval.

### Minor

1. **The two-stage SUM-text outperforming end-to-end SUM-shot creates an unresolved tension.** The paper claims explicit shot structure is beneficial (SUM-shot > SUM-holistic), which is supported. However, SUM-text (which has no explicit shot structure in its LLM input) outperforms SUM-shot across all metrics. The paper acknowledges this but does not reconcile it with the claim that shot structure is critical. A controlled comparison that feeds shot-boundary markers into SUM-text would help.

2. **The VALOR comparison in narration captioning is not especially informative.** VALOR processes raw audio while the paper's model uses ASR text — fundamentally different input modalities. The large gap (VALOR CIDEr 13.5 vs. Ours V+A 168.7) is expected and tells the reader little about the dataset's properties.

3. **Filtering thresholds are stated without ablation.** The thresholds (CLIP similarity 0.25, inter-shot similarity 0.9, PySceneDetect threshold 11) are described but not justified through ablation. Without sensitivity analysis, it is unclear whether the dataset is representative of natural multi-shot web videos or strongly biased by these choices.

4. **Cross-reference error.** The text points to Table~\ref{tab:shot_visual_cap} (the single-shot captioning table) when introducing the QA results, but the actual QA results are in Table~\ref{tab:zr_qa}.

### Trivial
None.

## Nice-to-Haves

- A human evaluation of the QA judgments on a subset (100+ examples) to validate the GPT-3.5 judge, or reporting standard exact-match/F1 alongside GPT-based scores.
- A retrieval experiment that fine-tunes a baseline using the shot captions and ASR text, demonstrating whether the dataset's annotations improve retrieval quality.
- An ablation for the summarization model where explicit shot-boundary markers are added to SUM-text to isolate the value of shot structure from the two-stage advantage.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The zero-shot QA experiment does not support the claim that summaries boost performance"** (overstated): The paper does provide within-model evidence (Video-ChatGPT V+T 49.3 → Video-ChatGPT T 53.7 with summary text). The experiment is imperfect (missing raw-caption ablation) but not completely unsupportive. This is subsumed by the weaker, specific point about the missing ablation above (Major point 3).

- **"SUM-text outperforming SUM-shot contradicts the claim that shot structure is beneficial"** (strawman): The paper's claim is that shot structure helps relative to holistic processing (SUM-shot > SUM-holistic supports this). SUM-text is a different paradigm (two-stage, pre-generated captions + LLM). The critic conflates "shot structure" with "end-to-end training." The paper correctly distinguishes these.

- **"Table 5 does not exist" / broken references** (parser issue): The extracted text does not contain a "Table 5" reference. The cross-reference from QA text to `tab:shot_visual_cap` is a genuine error (kept as Minor point 4), but the rest is parser-related.

- **"VALOR comparison is uninformative"** softened to Minor point 2 rather than a major weakness, as the paper uses VALOR only as a baseline and does not rest a central claim on it.

- **"The figure `fig:video_demo` does not appear"** (parser issue): Figures are stripped by the PDF parser; no conclusion can be drawn about the original submission.

- **"No example of subjective description removal in main text"**: The paper states this is shown in the supplementary (Supp. Sec.~\ref{supp_sec:human_anno_shot}), which the parser strips. Not a main-text weakness.

- **Strength Finder strength about retrieval creating "a valuable new benchmark"** — this is generic; the retrieval tasks are listed but the experiments are too preliminary to call this a strength. Moved here.

## Novel Insights

None beyond the paper's own contributions. The reviews identify gaps in validation but do not surface independent novel observations about the problem or approach.

## Suggestions

1. **Add annotation quality metrics.** Report inter-annotator agreement (e.g., pairwise CIDEr/BLEU between independent annotator corrections on a random 200-shot sample) and the average edit distance/correction rate between MiniGPT-4 outputs and final captions. This is essential for a dataset paper claiming human-verified quality.

2. **Add the controlled QA ablation.** Feed raw shot captions (without summarization) into Vicuna and compare with the summary-based results. This would directly test whether summarization adds value beyond the caption data.

3. **Validate the GPT-3.5 judge.** Report correlation with human judgments on a subset (at least 100 examples), or switch to standard exact-match/F1 evaluation and explain the discrepancy with published Video-ChatGPT numbers on MSRVTT-QA.

4. **Add a retrieval experiment that uses the dataset's annotations.** Fine-tune at least one baseline using the shot captions and/or ASR text to demonstrate that the annotations enable better retrieval performance.

5. **Reconcile the SUM-text vs. SUM-shot tension.** Add an ablation that feeds explicit shot-boundary markers (e.g., "[Shot 1]", "[Shot 2]") into the SUM-text pipeline to isolate the effect of shot structure from the two-stage advantage.

## Score and Decision

The dataset itself is a genuine, well-motivated contribution that fills a real gap in the video understanding landscape. The shot-level separation of visual and narration captions, combined with human-verified long-form summaries, is not available in any existing benchmark. However, the paper's experimental validation is materially insufficient to support its central claims:
- The quality of the human-verified annotations is asserted but never measured.
- The headline result (zero-shot QA outperforming Video-ChatGPT) rests on an unvalidated evaluation judge and unexplained discrepancies with prior reported numbers.
- The summary-usefulness claim lacks a direct ablation.
- The retrieval experiments do not demonstrate why the dataset's annotations matter.

These gaps are fixable with additional experiments and analysis, but in their current form they prevent the paper from convincingly demonstrating why the community should adopt this benchmark. The paper needs major revisions.

**MY FINAL SCORE: <pineapple>5.0</pineapple>**
**MY FINAL DECISION: <orange>Reject</orange>**