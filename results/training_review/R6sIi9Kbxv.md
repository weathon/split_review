Now I have all the information needed. Let me synthesize the final review.

---

## Summary

The paper proposes Video Q-Former, a video-language model that enhances spatiotemporal feature extraction for video LLMs. It introduces (1) an attentive pooling module that decouples spatial and temporal representations via learnable queries, and (2) a spatio-temporal Q-Former that replaces the standard FFN with three "video experts" (spatial, temporal, summary) coupled with a cross-attention mask to control query-to-feature visibility. The model is evaluated on zero-shot video QA, video captioning, video summarization, and video-based text generation benchmarks.

## Strengths

- **Novel architectural design for explicit spatiotemporal modeling.** The paper directly addresses two known limitations of prior video LLMs: Video-ChatGPT's average pooling cannot model inter-frame relationships, and Video-LLaMA's cascaded Q-Formers lose information and lack explicit spatiotemporal features. The attentive pooling module (Section 3.1) decouples spatial and temporal video features via learnable queries, and the spatio-temporal Q-Former with three video experts (SP-FFN, T-FFN, SM-FFN) extracts semantic-aligned representations concurrently. The ablation study (Table 6) confirms that both components outperform their respective baselines (average pooling and original Q-Former) on MSRVTT captioning.

- **Reported large-margin gains over baselines on zero-shot video QA.** On the Video-ChatGPT benchmark, Video Q-Former reports 70.1% accuracy on MSRVTT-QA and 77.4% on MSVD-QA — improvements of ~13% and ~10% over the second-best method (Table 2). It also outperforms VideoChat (which uses a Q-Former structure and more pre-training data) on these datasets, lending some credence to the architectural advantage even though the comparisons are not tightly controlled.

- **Ablation of video experts spans both captioning and QA tasks.** Unlike the claim that all ablations are on captioning, Table 7 ablates the spatial/temporal/summary experts on ActivityNet-QA (a video QA benchmark), demonstrating that temporal features are more important for longer videos and temporal understanding. Table 8 does the same for MSRVTT captioning, and the combined model outperforms either expert alone in both settings, supporting the value of explicit spatiotemporal modeling.

- **Computational efficiency compared to a naive baseline.** Table 1 shows that the spatio-temporal Q-Former with 16 frames has roughly half the FLOPs of feeding all per-frame Q-Former tokens directly to the LLM, a genuine practical advantage.

## Weaknesses

### Major

- **Uncontrolled baseline comparisons undermine the headline SOTA claim.** The paper compares its zero-shot QA results (Table 2) to published numbers from Video-ChatGPT and Video-LLaMA, but these baselines use different LLM backbones (Video-ChatGPT uses LLaMA; the authors use Vicuna, which is instruction-tuned from LLaMA and likely stronger for dialogue), different vision encoders, different pre-training data, and different frame sampling. The paper does not re-implement any baseline under matched conditions. A 10–13% gap under these circumstances is not reliable evidence that the proposed architecture is the source of improvement — it could partly reflect the stronger Vicuna backbone, larger pre-training data (15M examples), or differences in tuning. The comparison to VideoChat is somewhat fairer since both use a Q-Former, but the gap there is only ~1 point, which is modest.

- **Missing comparisons to more recent video LLMs.** The paper compares only to Video-ChatGPT, Video-LLaMA, LLaMA-Adapter, and VideoChat — all from 2023. By the current date (2026), models like Video-LLaVA, LLaMA-VID, and LLaVA-NeXT have been available. The claimed "state-of-the-art" status cannot be verified without comparison to these contemporary approaches, and the significance of the contribution is unclear if these later models already achieve stronger or comparable results. This is the most actionable gap in the paper.

- **Key component ablation (Table 6) is conducted only on video captioning, not on QA.** The attentive pooling vs. average pooling and spatio-temporal Q-Former vs. original Q-Former comparisons — which directly test the paper's headline architectural innovations — are performed on MSRVTT captioning, not on the zero-shot QA benchmarks that drive the SOTA claim. While Table 7 does ablate video experts on QA (ActivityNet-QA), it does not ablate the attentive pooling module or the full spatio-temporal Q-Former versus original Q-Former on QA. Without this, the paper cannot demonstrate that its core architectural changes are responsible for the large QA gains.

### Minor

- **Implementation details of the MoE-style experts are underspecified.** The paper states that "different experts are employed to process different query embeddings in parallel" (line 66–67), suggesting a fixed assignment of query type to expert (spatial queries → SP-FFN, temporal → T-FFN, summary → SM-FFN). This is not a traditional mixture-of-experts with learned routing, yet the paper invokes the MoE framing (citing Shazeer et al. 2017, Bao et al. 2022) without clarifying the routing mechanism or providing ablation on learned vs. fixed assignment. The ambiguity does not invalidate the contribution but hurts reproducibility.

- **The attentive pooling module's dimensionality logic is unclear.** The paper states that a single spatial pooling query Q_s ∈ ℝ^{1×D} cross-attends to video embedding x ∈ ℝ^{T×N×D} and produces v_t ∈ ℝ^{T×D}. With a single query, standard cross-attention would produce a 1×D output, not T×D. The intended interpretation is likely that the query is applied per-frame, but this is never clarified. Similarly for the temporal query. This is a presentation issue that makes the method harder to follow and reproduce.

- **The ChatGPT-based evaluation metric is used without discussion of its limitations.** The zero-shot QA evaluation (line 106) follows the Video-ChatGPT benchmark protocol, which uses ChatGPT to score responses from 0–5. While using an established benchmark is acceptable, the paper provides no analysis of how well this automated scoring correlates with human judgment. This is a community-wide concern rather than a paper-specific flaw, but it would strengthen the work to acknowledge and discuss the limitation.

### Trivial

- Table 1 has a typo in the header: "Comparsion" → "Comparison."
- The paper does not report results on additional standard video QA benchmarks such as NExT-QA or iVQA, which would provide a fuller picture.
- No ablation is provided for the number of spatial/temporal queries (beyond reporting that 64 are used) or for the cross-attention mask design, though these are not critical for the paper's main claims.

## Nice-to-Haves

- A controlled experiment ablating the LLM backbone (e.g., running the proposed architecture with LLaMA instead of Vicuna) would help isolate the contribution of the spatiotemporal design from the LLM choice.
- Ablation of the two-stage training strategy (freezing vs. unfreezing attention layers) would clarify whether the schedule is necessary.
- Attention visualizations from the attentive pooling module, showing that spatial queries focus on within-frame regions and temporal queries attend across frames, would strengthen the qualitative evidence.

## Removed Points

These points were raised by reviewers but removed or corrected after verification against the paper:

1. **"Ablations only on video captioning"** — Removed because Table 7 ablates video experts on ActivityNet-QA (a QA benchmark), contradicting the claim that all ablations are on captioning. However, the key component ablation (Table 6) IS only on captioning, which is kept as a Major weakness with corrected framing.

2. **"No justification for two-stage training schedule"** — Removed as a general request for rationale that is a nice-to-have, not a flaw. The paper states the schedule is designed "to better leverage the pre-trained parameters of BLIP-2" (line 88), which is a reasonable motivation even without an ablation.

3. **"Comparison to VideoTeller is not controlled"** — Removed because the paper explicitly notes this as a strength ("even without pre-training on the 0.5 million video-text pairs mentioned by Video-Teller," line 135), turning the asymmetry in the paper's favor.

4. **"Video captioning baselines (VideoCoCa, GIT) are not specialized video LLMs"** — Removed because the captioning experiments (Table 4) are presented as competitive rather than SOTA, and the paper is not claiming a headline contribution here. Comparing to strong VLP models in captioning is standard.

5. **Critique that baselines' inference FLOPs are not reported** — Removed because Table 1 provides FLOPs for the proposed method against a naive Q-Former baseline, which is the relevant efficiency comparison for the paper's architecture claim.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add controlled comparisons.** Re-implement Video-ChatGPT's average pooling and Video-LLaMA's cascaded Q-Former under the same LLM (Vicuna), vision encoder (ViT-G/14), and pre-training data used in this paper. This would directly test whether the proposed architecture is responsible for the observed gains.

2. **Add comparisons to recent models.** Include results from Video-LLaVA, LLaMA-VID, or other contemporary video LLMs to substantiate the SOTA claim.

3. **Run the key component ablation (Table 6) on zero-shot QA benchmarks.** This is the single most impactful addition: showing that attentive pooling and the spatio-temporal Q-Former outperform their baselines on MSRVTT-QA and MSVD-QA would directly support the headline claim.

4. **Clarify the attentive pooling dimensionality** — explain whether the spatial query is broadcast/applied per-frame or if there is a dimension mismatch in the notation.

5. **Clarify the MoE routing mechanism** — specify whether expert assignment is fixed by query type or learned through a gating function.

## Score and Decision

The paper proposes a well-motivated architecture with plausible design improvements and shows large reported gains on standard benchmarks. However, the experimental evaluation has two significant gaps: (1) the headline SOTA results are based on comparisons to uncontrolled baselines with different LLMs, training data, and vision encoders, and (2) no comparisons to more recent video LLMs are provided, making the "state-of-the-art" claim unverifiable. The paper also lacks a direct ablation of its core architectural components on the QA tasks that form the basis of its main claim. These are major weaknesses that prevent the paper from supporting its central claims in its current form.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>