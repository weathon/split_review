- Decision: Accept
- Avg Score: 5.50
- Scores: 5, 5, 6, 6
Now I have all the information needed. Let me construct the final consolidated review.

## Summary

This paper introduces **Shot2Story**, a benchmark of ~20K multi-shot videos with per-shot visual captions, per-shot narration (audio) captions, and comprehensive human-verified video summaries. The dataset fills a clear gap in existing video understanding benchmarks by explicitly modeling shot structure, separating visual and audio signals, and providing long-form summaries that capture event progression. Three tasks are formulated: single-shot captioning, multi-shot summarization, and retrieval with shot descriptions. Preliminary experiments demonstrate the value of shot structure and ASR for multi-shot understanding and show that summaries learned on Shot2Story transfer to zero-shot video QA on MSRVTT-QA and ActivityNet-QA, outperforming Video-ChatGPT without any QA-specific instruction tuning.

---

## Strengths

1. **Well-motivated, carefully constructed benchmark filling a real gap**: The paper persuasively argues that existing video captioning benchmarks treat multi-shot videos coarsely (holistic captions or annotator-chosen boundaries), while Shot2Story provides per-shot visual and narration captions plus composed summaries that track subject identity and event progression across shots (Table 1, Sec. 2.5). The hybrid annotation pipeline (MiniGPT-4 proposals → human correction; GPT-4 summaries → human verification) is pragmatic for scaling while maintaining quality. The average summary length of 201.8 words exceeds the combined per-video caption length of ActivityNetCaps and YouCook2, and the narration captions are unique among multi-event video datasets of this scale.

2. **Controlled experiments isolating the value of shot structure and ASR**: In multi-shot summarization (Table 4), SUM-shot (with explicit shot boundaries) outperforms SUM-holistic (no shot structure) by +2.3 CIDEr (8.6 vs 6.3), and SUM-shot without ASR drops to 4.7 CIDEr. These are clean within-model comparisons that directly support the paper's claims that modeling shot boundaries and leveraging audio signals are necessary for this task. The patterns are consistent across B, M, and R metrics as well.

3. **Strong zero-shot video QA transfer demonstrating summary utility**: The SUM-shot model (trained only on Shot2Story) generates video summaries for MSRVTT-QA and ActivityNet-QA, which are then fed to Vicuna for answer generation. It achieves 56.8% on MSRVTT-QA and 47.4% on ActivityNet-QA, surpassing Video-ChatGPT in a text-only evaluation (53.7% and 37.4%) without any QA-specific instruction tuning (Table 6). This demonstrates that summaries learned on Shot2Story generalize to longer, out-of-domain videos and that comprehensive summaries are a useful intermediate representation for downstream tasks.

4. **Novel retrieval settings probing fine-grained video-text alignment**: Three retrieval settings (T2V, T2S, V2T) use shot-level descriptions as queries (Sec. 4.5, Table 3). The finding that T2V (R@1 66.3 for UMT) is harder than T2S (R@1 68.6) confirms the hypothesis that retrieving a full video from a shot-level description requires more detailed understanding — validating the benchmark's capacity for fine-grained evaluation.

---

## Weaknesses

### Fatal

None.

### Major

1. **SUM-text training setup is underspecified, weakening the summarization comparison (Table 4)**: The paper describes SUM-text as a two-stage model: "first generating captions using our video-shot captioning model for each video shot, then embed the generated captions into a text prompt as the input to the LLM." However, it is **never stated** what the LLM (Vicuna) in SUM-text is trained on during the summarization stage. If the LLM is fine-tuned on **(ground-truth) human-annotated shot captions** paired with summaries, then at test time it receives noisier **generated** captions — a train-test mismatch that would disadvantage its own evaluation. Conversely, if it is fine-tuned on generated captions, the comparison with end-to-end methods is fairer. The paper provides no statement either way, and the caption "E2E means whether the model is trained in an end-to-end approach" does not clarify what training data the non-end-to-end model uses. This ambiguity undermines confidence in the paper's conclusion that "better model design needs to be explored for end-to-end video summarization" — the gap between SUM-text (9.2 CIDEr) and SUM-shot (8.6) may be partly or entirely artifactual. **This is not fatal** (the dataset contribution does not depend on this specific result), but it is the most significant evidential gap in the paper. *(Verified: Sec. 3.3, lines 185–210, and Table 4.)*

2. **No annotation quality metrics reported**: The dataset's value depends critically on the accuracy and consistency of the shot captions and summaries. The paper describes a hybrid pipeline (MiniGPT-4 proposals → human correction; GPT-4 summaries → human verification) but reports **zero quality statistics** — no inter-annotator agreement, correction rates, fraction of summaries requiring significant rewriting, or edit distances between GPT-4 output and human-corrected versions. Without these, readers cannot assess the true reliability of the annotations. The single example in the supplementary is illustrative but not quantitative. *(Verified: Sec. 2.3–2.4 — no agreement metrics or correction statistics appear anywhere in the paper.)*

### Minor

3. **Ambiguity in zero-shot QA evaluation setup (Table 6)**: The paper states "for a direct comparison, we evaluate Video-ChatGPT on question-answering in the same methodology as ours." The table shows a "Video-ChatGPT (T)" row with text-only input, but it is not explicitly stated whether this "T" input is (a) the **same generated summary** that the paper's method uses, or (b) raw ASR text. If (b), the comparison is unfair since the summaries are richer. The phrase "same methodology" strongly implies (a), but the paper should state this explicitly. Additionally, MovieChat achieves 51.5 on ActivityNet-QA (vs. the paper's 47.4) — the paper does not discuss why MovieChat performs better on this benchmark despite not using the paper's summaries. While MovieChat uses visual inputs and instruction tuning, this discrepancy warrants discussion. *(Verified: Sec. 4.4, lines 214–241, Table 6.)*

4. **Limited baseline coverage for proposed tasks**: For single-shot captioning (Table 2), only two variants of the paper's own model (V vs. V+A) are compared — no existing video captioning methods (e.g., MART, SwinBERT, or other LLM-based approaches) are evaluated, making it difficult to gauge how challenging the new task is relative to established baselines. For retrieval (Table 3), only pretrained models are reported without fine-tuning on the dataset's splits. While acceptable for initial benchmarking, showing at least one fine-tuned baseline would demonstrate that the retrieval splits support discriminative learning and provide a reference for future work. *(Verified: Tables 2 and 3.)*

5. **No limitations or failure case discussion**: The paper lacks a limitations section. It does not discuss what types of videos are poorly covered (e.g., those without speech, with many shots >8, long-form content), potential biases introduced by the LLM-based annotation pipeline, or systematic failure modes of the proposed models beyond a brief mention of hallucinations in one example (Fig. 3). Adding this would strengthen the paper's scholarship. *(Verified: No limitations section in the paper.)*

### Trivial

6. **Marginal and mixed signal from ASR in single-shot captioning (Table 2)**: Adding ASR improves BLEU by +0.2 and METEOR by +0.2 but hurts ROUGE by −0.5 and CIDEr by −1.4. The paper already acknowledges this as "posing integration challenges," which is an appropriate conclusion. The scores are so close that they may be within noise, but the paper does not report variance or significance. This is very minor given the measured conclusion.

---

## Nice-to-Haves

- **A controlled ablation for SUM-text**: Train the SUM-text LLM on generated captions (from the single-shot model) rather than ground-truth captions, and compare the two. This would cleanly separate the benefit of the two-stage architecture from any advantage conferred by cleaner training inputs.
- **A human-annotated summary upper bound for the QA task**: Having human-written summaries (already available in the dataset) as an oracle input to Vicuna on MSRVTT-QA / ActivityNet-QA would show the headroom available for improving summary quality.
- **Fine-tuned retrieval baselines**: Fine-tuning at least one of the reported retrieval models (e.g., CLIP4Clip) on the Shot2Story retrieval splits would demonstrate learnability and provide a stronger reference point.
- **Threshold sensitivity analysis**: A brief justification or ablation for the filtering thresholds (CLIP similarity >0.25, inter-shot similarity <0.9, scene change threshold 11) would strengthen the data preparation description.

---

## Removed Points

*These points were flagged for removal. They are included here for transparency but should not be weighted in the evaluation.*

1. **"Table 1 comparison is uneven"** — The table caption explicitly states: "The summary length of ActivityNet and YouCook2 are their combined length of captions in one video." The comparison is properly qualified. Removed: the paper already addresses this.
2. **"VAST has 27M videos vs. your 20K — trade-off"** — The paper's claim is about annotation *detail* and *quality*, not scale. The trade-off between scale and detail is inherent in dataset construction; the paper does not claim to be superior in scale. Removed: not a valid weakness.
3. **"Video-ChatGPT is not a competitive baseline for summarization"** — Including a well-known general video model as a reference point is standard practice. The paper does not overclaim based on this comparison. Removed: overly harsh and not material.
4. **"Thresholds seem arbitrarily chosen"** — Thresholds in data filtering pipelines are nearly always heuristic; the paper's thresholds are reasonable and consistent with common practice. Removed: generic criticism lacking a specific demonstrated problem.
5. **"Table column headers are garbled"** — The extracted LaTeX is correct; any garbling is a PDF-parser artifact, not a paper issue. Removed per formatting-artifact rule.
6. **Generic formatting/style nitpicks** — Removed per instructions.

---

## Novel Insights

The two reviewer inputs converge on the assessment that Shot2Story is a genuinely useful benchmark, but they disagree sharply on severity. The harsh critic characterizes the experimental gaps as potentially undermining the paper's conclusions (particularly the SUM-text training ambiguity), while the strength finder emphasizes the clean controlled experiments and zero-shot transfer results. The novel synthesis here is that these positions can be reconciled: the paper's **core contribution — the dataset and its annotation paradigm — is solid and independently valuable**, and the key claims about shot structure and ASR importance are supported by controlled within-model ablations (SUM-shot vs. SUM-holistic, SUM-shot with/without ASR) that are *not* affected by the SUM-text training ambiguity. The SUM-text ambiguity primarily affects one specific claim about end-to-end vs. two-stage architectures, not the main contributions. The missing annotation quality metrics are a genuine gap that should be addressed but do not invalidate the dataset's value given the human-verification step already described.

---

## Suggestions

1. **Clarify the SUM-text training setup**: Explicitly state (a) whether the LLM in SUM-text is trained on ground-truth shot captions or generated captions, and (b) if the former, how the train-time and test-time inputs differ. If the experiment has already been run with generated captions, report those results.
2. **Add annotation quality statistics**: Report inter-annotator agreement on a held-out subset (e.g., using CIDEr or BERTScore between two annotators' versions of the same shot), correction rates (what fraction of MiniGPT-4 captions needed changes, how major), and edit distance between GPT-4 summaries and human-corrected versions.
3. **Clarify the QA setup**: State explicitly: "For the Video-ChatGPT (T) baseline, we provide the same generated video summary (from our SUM-shot model) as input, along with the question."
4. **Discuss the MovieChat result on ActivityNet-QA**: Acknowledge that MovieChat outperforms the paper's method on ActivityNet-QA (51.5 vs. 47.4) and explain why — e.g., MovieChat uses visual features and instruction tuning, while the paper's method is text-only and zero-shot.
5. **Add a limitations section**: Discuss coverage gaps, potential biases from the LLM-based pipeline, and failure modes.

---
