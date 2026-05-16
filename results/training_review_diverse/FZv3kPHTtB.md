Now I have a thorough understanding of the paper and can verify each reviewer claim against the actual text. Let me compose the final consolidated review.

## Summary

Shot2Story introduces a large-scale multi-shot video benchmark with 20K videos, providing per-shot visual and narration captions (human-corrected from MiniGPT-4 seeds) and human-verified GPT-4-generated video summaries averaging 201.8 words. The benchmark uniquely combines three properties: shot-level annotation granularity, audio (narration) captions tied to visual references, and long-form video summaries. The paper defines several tasks — single-shot captioning, narration captioning, multi-shot summarization, video retrieval with shot descriptions — and demonstrates through baselines that (a) ASR text is critical for multi-shot understanding, (b) explicit shot structure helps summarization over holistic processing, and (c) generated summaries transfer to zero-shot video QA, outperforming Video-ChatGPT on MSRVTT-QA (56.8 vs. 53.7) and ActivityNet-QA (47.4 vs. 37.4).

## Strengths

- **Novel benchmark with comprehensive multi-shot annotations**: Shot2Story provides 20K videos with per-shot visual and narration captions plus human-verified video summaries (avg 201.8 words), uniquely combining multi-shot structure, audio captions, and detailed summaries — exceeding prior datasets on all these dimensions (Table 1, Section 2.4). The human verification step distinguishes it from machine-only datasets like VAST.

- **Demonstrates importance of ASR and shot structure for video understanding**: Controlled experiments show adding ASR text improves summarization (SUM-shot with ASR CIDEr 8.6 vs. without ASR 4.7, Table 4) and that explicit shot-level processing (SUM-shot) outperforms holistic processing (SUM-holistic, CIDEr 8.6 vs. 6.3, Table 4), providing clear evidence that both audio and shot structure are critical.

- **Zero-shot video QA via generated summaries provides the strongest validation**: The paper achieves strong zero-shot QA on MSRVTT-QA (56.8) and ActivityNet-QA (47.4) by converting video to summary then feeding to an LLM, outperforming Video-ChatGPT (53.7 and 37.4 respectively, Table 6) — despite not using any instruction tuning — demonstrating that detailed summaries serve as effective intermediate representations for downstream tasks.

- **Efficient annotation pipeline using LLM assistance**: Using MiniGPT-4 to generate initial shot captions followed by human correction achieves ~3× speedup compared to writing from scratch (Section 2.3), offering a practical methodology for scaling detailed video annotations.

- **Novel retrieval tasks with shot descriptions**: The paper introduces three retrieval settings (T2V, T2S, V2T) that require finer-grained video understanding than standard text-video retrieval, and shows that T2V (video-level retrieval from a shot description) is harder than T2S (shot-level retrieval), validating the dataset's challenge (Table 5, Section 3.6).

## Weaknesses

### Fatal
None.

### Major

- **No inter-annotator agreement statistics reported for any annotation stage**: The paper describes a multi-stage annotation pipeline (MiniGPT-4 seeding → human correction for shot captions; GPT-4 generation → human verification for summaries), yet reports no agreement metrics (e.g., Fleiss' κ, pairwise overlap, or even coarse proxy metrics like agreement on object mentions or speaker identity) for any stage. For a benchmark intended to serve as a gold-standard evaluation resource, the reliability of the ground-truth labels is foundational. This is especially concerning for the narration captions, which require annotators to identify "which person in the video is talking" and "which object the speaker is referring to" — tasks that are inherently subjective and likely have non-trivial disagreement rates. Without this information, the reader cannot assess whether the annotations are consistent enough to serve as a reliable evaluation benchmark. **This is the most significant gap and should be addressed with at least a sample-based agreement study.**

- **Insufficient external baselines for single-shot video captioning**: Table 2 compares only two variants of the authors' own architecture (V vs. V+A), with no comparison to any existing video captioning model (e.g., Video-LLaMA, BLIP-2 fine-tuned for video, VideoChat-based variants). This makes it impossible to assess whether the dataset presents a genuinely new challenge or is simply well-aligned with this particular backbone. The retrieval experiments (Table 5) include strong baselines (Alpro, CLIP4Clip, UMT), so including even one external captioning baseline would strengthen the paper's claims about task difficulty. Similarly, the narration captioning task compares only to VALOR (audio-only), omitting modern audio-visual models that could serve as stronger baselines.

### Minor

- **QA evaluation relies on GPT-3.5 as automatic judge without human validation**: The zero-shot QA results (Table 6) — which provide the paper's strongest evidence for the value of summaries — are evaluated by having GPT-3.5 produce a binary correctness judgment, following Video-ChatGPT's methodology. No human validation of this automatic judge is reported, nor is its agreement with human evaluators measured. While this is standard practice in the current literature, a small human evaluation (e.g., 100–200 samples) to confirm that GPT-3.5 judgments align with human judgments would substantially increase confidence in the central QA result.

- **Dataset filtering thresholds are given without justification or ablation**: The filtering pipeline uses thresholds (CLIP similarity >0.25, adjacent-shot similarity <0.9, PySceneDetect threshold of 11) that are reported without any analysis of how they were chosen or what effect they have on the resulting dataset composition. The CLIP threshold of 0.25 is notably low and the paper does not explain whether this was empirically determined. An ablation on even a small sample (e.g., measuring how many videos pass at different thresholds) would increase trust that the filtering does not introduce systematic biases.

- **Limited discussion of limitations and potential biases**: The paper does not discuss potential biases from the filtering pipeline (e.g., over-representation of talking-head or product-review videos, exclusion of videos with low visual-ASR correlation) or from using GPT-4 as a summary generator. While no paper needs an exhaustive limitations section, some discussion of the scope and potential blind spots would improve scientific candor.

### Trivial
None.

## Nice-to-Haves

- A small-scale ablation study validating the filtering thresholds (CLIP similarity, adjacent-shot similarity, static-content detector threshold) on a held-out sample.
- Human quality control statistics for the summary verification step: number of annotators per summary, proportion accepted without correction, edit distance distribution.
- Including at least one open-source video captioning baseline (e.g., Video-LLaVA or BLIP-2 on video) for the single-shot captioning task to anchor task difficulty relative to existing benchmarks.

## Removed Points

**These points are flagged to be removed, treat them with caution:**

- **"Dataset release details should be stated explicitly"** — Removed per hard rule: questions about existence, release status, or availability of cited resources must be removed. The paper cites HDvila100M as the source and describes the annotation pipeline; whether the annotations will be released is a separate matter that does not affect the technical contribution.

- **"The CLIP threshold of 0.25 is very low — effectively removing only near-zero correlation"** — The critic's characterization of "very low" is a subjective opinion without empirical backing. The threshold is mentioned in the Minor weaknesses as lacking justification, which is fair; the specific claim that it is "very low" is removed as opinion.

- **Criticisms about missing appendix content / Supp. Sec. references** — Removed per hard rule: the parser strips appendix sections from all papers; they exist in the original submission. The paper references Supp. Sec. for prompts and examples, and these are assumed to be present in the full version.

## Novel Insights

The reviews surface one genuinely novel observation beyond the paper's own contributions: the two-stage SUM-text model (generate shot captions first, then summarize via LLM) outperforms the end-to-end SUM-shot model on summarization metrics (CIDEr 9.2 vs. 8.6, Table 4). This suggests that current end-to-end architectures that directly map frames to long-form text lose information compared to a pipeline that explicitly produces intermediate shot-level representations — an interesting finding that the paper itself treats honestly as a challenge for future work, but that the reviewer rightly highlights as a non-obvious result that could inform architecture design for long-video understanding. None of the other insights from the reviews go substantially beyond what the paper already claims or demonstrates.

## Suggestions

1. **Add inter-annotator agreement statistics** for a sample of at least 100–200 annotations across shot captions, narration captions, and summaries. Even a coarse proxy — e.g., agreement on whether the same subject is mentioned, or whether the speaker referent is identified — would substantially increase trust in the benchmark as a gold standard. This is the single highest-leverage improvement.

2. **Validate the GPT-3.5 QA judge** on a human-annotated sample (100–200 QA pairs). Report Cohen's κ between GPT-3.5 and human judgments for both yours and Video-ChatGPT's outputs to ensure the comparison is fair and the absolute numbers are meaningful.

3. **Add at least one external baseline** for single-shot video captioning by evaluating a recent open-source video captioning model (e.g., Video-LLaVA, BLIP-2, or InstructBLIP on video frames) on the test set. This would anchor the task difficulty relative to existing research and make the benchmark immediately useful to the community.

4. **Briefly justify the filtering thresholds** (CLIP similarity >0.25, adjacent-shot <0.9, PySceneDetect threshold 11) — either with a small ablation or with a citation to established practice — and add a limitations paragraph discussing potential biases from the filtering pipeline.

## Score and Decision

This paper makes a solid contribution: the Shot2Story benchmark fills a genuine gap (multi-shot videos with shot-level visual + narration captions + long summaries), the annotation pipeline is practical and scalable, and the zero-shot QA transfer result provides compelling evidence of the dataset's value. The weaknesses are real but addressable — the lack of inter-annotator agreement statistics is the most significant, and insufficient external baselines limit the immediate utility of the single-shot tasks. Neither weakness is fatal; both can be resolved within the revision timeline. The paper is a strong candidate for acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>