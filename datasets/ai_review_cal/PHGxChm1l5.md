- Decision: Accept
- Avg Score: 6.33
- Scores: 5, 6, 8
I now have a thorough understanding of the paper and have verified all the reviewer claims against the actual text. Let me produce the consolidated review.

---

## Summary

CoVLM proposes an architecture that integrates a detection network into an LLM via special communication tokens (`<visual>`, `<previsual>`, `<box>`, `<prebox>`) that mediate iterative, bidirectional interaction between language generation and visual detection. The LLM can generate a token to trigger top-down ("find regions relevant to this entity/relation") and bottom-up ("here are the detected regions, continue generating") communication at each step, rather than relying on a single holistic image embedding. The paper reports large gains on compositional reasoning benchmarks (HICO-DET, Cola, ARO) and competitive results on referring expression comprehension and VQA.

## Strengths

1. **Novel "communicative decoding" architecture for compositionality.** The core idea — using special tokens to enable the LLM to dynamically query a detection network mid-generation, receive region features back, and continue decoding — is genuinely novel and well-motivated. The paper makes a clean architectural departure from prior work (including KOSMOS-2) where vision-to-language feedback does not exist. The mechanism is clearly described in Section 3.2 and Figure 2.

2. **Large and consistent gains on three compositional reasoning benchmarks.** In Table 1, CoVLM 1.4B outperforms KOSMOS-2 by +17.74 mAP (Full) on HICO-DET, +13.81 Top-1 accuracy on Cola, and +12.58 Top-1 accuracy on ARO. These are far beyond typical margins and directly support the claim that iterative V-L communication improves compositionality.

3. **Zero-shot performance exceeding supervised methods on rare HOI categories.** On the HICO-DET Rare split (Table 3), CoVLM 1.4B achieves 50.82 mAP zero-shot, surpassing all supervised methods (best: RLIPv2-ParSeDA at 43.23). This is a strong signal that the architecture itself — not just data scale — delivers generalization on long-tail compositions.

4. **Competitive zero-shot referring expression comprehension without instruction tuning.** CoVLM 2.8B achieves the best results on RefCOCOg (val 61.23, test 62.33) and RefCOCO+ (all splits) among zero-shot models, including KOSMOS-2 which used instruction fine-tuning for this task format. This shows the communication tokens transfer to object localization tasks beyond the compositional reasoning setting.

## Weaknesses

### Fatal
None.

### Major

1. **Detection network training is underspecified, harming reproducibility.** The detection network is described as "similar to YOLOX" and takes concatenated image embeddings + LLM hidden state as input. The paper states the whole model is "fully fine-tuned during pre-training" (line 113), but provides no information about: (a) the training objective/loss function for the detection head — is it a standard detection loss (YOLOX-style classification + regression), or is it trained only through the language modeling objective via the ROI features fed back to the LLM? (b) initialization — are the detection network weights from a pretrained YOLOX checkpoint, or randomly initialized? (c) how bounding box supervision is obtained during pre-training — the GroundingDINO pipeline (Section 3.4) generates pseudo-labels for inserting communication tokens, but it is never stated whether these pseudo-labels are used as supervision for the detection head. The detection network is the central mechanism for both top-down and bottom-up communication; without specifying its training objective and supervision, the method cannot be fully reproduced.

2. **HICO-DET evaluation protocol is incompletely specified.** The paper describes a two-step procedure (verb existence via perplexity comparison, then object/location prediction using the model's generative output) but does not specify how bounding boxes for the subject (person) and object are *selected* from the detection network's multiple proposals for final mAP evaluation (lines 224-225). The detection network outputs `N×N×4` bounding boxes with confidence scores, and after NMS "we keep a set of bounding boxes as regions of interest" — but the paper never explains how these are reduced to the single human box and single object box required for HICO-DET evaluation, or what matching/assignment rules are applied. Given that the reported Full mAP (39.00) is dramatically higher than KOSMOS-2 (21.26) and even exceeds supervised methods on the Rare split, a precise description of the evaluation pipeline is essential for the results to be credible.

### Minor

3. **CoVLM 2.8B results are absent from the main compositional reasoning table.** Table 1 only reports CoVLM 1.4B on ARO, Cola, and HICO-DET. The 2.8B variant is evaluated on referring expression comprehension and VQA, but not on the three compositional reasoning benchmarks where the paper's core claims lie. This makes it impossible to assess whether the gains scale with model size, and weakens the claimed margin over baselines (many of which use 2.7B–3B parameter LLMs).

4. **ARO evaluation for generative models does not specify output-to-category mapping.** For ARO, the paper feeds "entity_A relation" as prompt and "consider[s] the model output as predicted entity_B" (line 162). ARO has 890 candidate object categories; it is unclear how the free-form text output is mapped to these categories (e.g., handling of synonyms, plurals, partial matches). This could introduce evaluation noise that affects the reported improvements (~3% over BLIP-2).

5. **No variance or error bars reported for any metric.** All results in Tables 1–4 and the VQA figure are reported as point estimates without standard deviations, confidence intervals, or information about the number of runs. Given the modest sample sizes for Cola (420 images) and the multiple processing steps in the HICO-DET pipeline, variance reporting would substantially strengthen the reliability of the claims.

6. **VQA human evaluation lacks sufficient methodological detail.** The paper conducts a human evaluation on 1000 samples and reports 57.11% (CoVLM) vs. 56.62% (BLIP-2), concluding the gap is "negligible" (line 271). However, the paper provides no details about: number of annotators, task instructions, inter-annotator agreement, or whether the human raters were evaluating the same metric as the automated VQA score. This limits the strength of the claim; the human evaluation is better treated as suggestive than conclusive.

7. **No ablation of the communication tokens or key hyperparameters.** The paper does not ablate the effect of removing `<previsual>`, `<visual>`, or the iterative re-ranking step. The detection network's GroundingDINO thresholds (0.35 box, 0.25 word, line 106) and the number of kept proposals *m* are stated but not analyzed for sensitivity. Given that these are the core components claimed to deliver the gains, ablation experiments would significantly strengthen the paper's central thesis.

### Trivial

- The random selection between two token assignment forms (Step 3, line 111) is stated without rationale or ablation.
- KOSMOS-2's RefCOCO advantage is attributed to instruction fine-tuning, but CoVLM could also be instruction fine-tuned; the choice not to do so is a limitation that could be more explicitly discussed.

## Nice-to-Haves

- Comparison with at least one strong contemporary VLM on compositional reasoning (e.g., LLaVA-1.5 7B or InstructBLIP) to contextualize the absolute performance level.
- Analysis of inference cost: the detection network runs at every `<visual>` or `<previsual>` token, which could be many times per caption. A runtime or FLOPs comparison with standard VLMs would help assess practicality.
- Discussion of whether the GroundingDINO-based pre-training pipeline introduces systematic biases (e.g., over-representation of objects GroundingDINO detects well).

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"KOSMOS-2 outputs only text (no boxes)"** — Factually wrong. The paper itself states (line 60) that "KOSMOS-2 generates a location token denoting a discretized bounding box for each visual entity." KOSMOS-2 does localize; the claimed apples-to-oranges concern on HICO-DET is unfounded.
- **"No comparison with methods that use iterative grounding, such as GRILL"** — Factually wrong. GRILL is compared in Table 4 (RefCOCOg test: 47.50). The reviewer may have missed this.
- **"The framing that previous VLMs 'feed one single image as a whole into LLMs' is misleading"** — This is a matter of interpretation, not a concrete weakness. The paper is describing a general architectural pattern (holistic image embeddings), not making an absolute claim.
- **"No comparison with methods that use iterative grounding" on compositional tasks** — No standard iterative-grounding baseline exists for ARO/Cola/HICO-DET zero-shot evaluation; GRILL (for referring expression) is the most closely related and is already compared.

## Novel Insights

The most insightful observation that emerges from synthesizing the reviews is that the paper's weaknesses are **not about the validity of its core thesis** (iterative communicative decoding improves compositional reasoning) but rather about the **completeness of its exposition**. The harsh critic's strongest points — missing training details for the detection network and under-specified HICO-DET evaluation protocol — are genuinely important but addressable. Together, the reviews reveal a pattern common to ambitious systems papers: the architectural novelty is clear and compelling, but the system-level implementation details that would enable verification and reproduction are omitted. This is not a fatal flaw if the authors can supply the missing information; it is a completeness gap rather than a correctness one. The fact that none of the reviews identified a flaw in the core reasoning about why iterative communication should help compositionality is itself informative — the paper's conceptual contribution appears sound.

## Suggestions

1. **Specify detection network training in full detail.** Provide: (a) the loss function (if any) for the detection head — is it YOLOX's standard loss, or is the detection network trained purely through the language modeling objective? (b) initialization source; (c) whether GroundingDINO pseudo-labels are used as supervision, and if so, how they are incorporated.

2. **Write out the HICO-DET evaluation algorithm step by step.** Specifically: after the detection network produces proposals for both the person and the object, how are the final single box for each selected? What NMS threshold, what score threshold, what association rule between the verb classification and the box proposals? Without this, the headline 20% improvement cannot be fully assessed.

3. **Add CoVLM 2.8B results to the main compositional reasoning table** (ARO, Cola, HICO-DET) to show whether gains scale with model size and to provide a fairer comparison with baselines in the 2.7B–3B parameter range.

4. **Include ablation experiments** removing `<previsual>`, `<visual>`, and the iterative re-ranking, to isolate which component drives the gains. Report variance across at least 3 runs for all main metrics.

5. **Provide more details on the VQA human evaluation** (number of annotators, instructions, agreement metric) or replace it with a more standard analysis (e.g., exact-match vs. soft-match accuracy with synonyms).
