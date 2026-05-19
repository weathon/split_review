- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 5, 5
Now I have a thorough understanding of the paper and can verify the claims against the actual content. Let me produce the final consolidated review.

---

## Summary

This paper proposes a synchronous (jointly-trained) method for scene text image machine translation (Scene TIMT) that unifies text region detection, source-language recognition, and target-language translation in a single end-to-end framework. The key architectural contribution is a Bridge-and-Fusion (BAF) module that uses cross-attention between cropped local visual features and textual features to improve translation. The authors also construct a large bilingual scene-text dataset (STST800K). The core evidence is that joint training + multi-modal fusion outperforms separately-trained pipeline approaches, especially on complex-layout datasets like ReCTS.

---

## Strengths

- **Joint training advantage isolated via GT OCR test (Table 4).** Even when ground-truth OCR is provided (eliminating recognition and reading-order errors), the proposed method outperforms the strongest pipeline baseline MCTIT. The paper explicitly highlights the larger gain on ReCTS (complex layout) vs. OCRMT30K, which directly supports the central motivation that joint learning helps beyond simply avoiding OCR error propagation.

- **BAF module provides measurable, specific gains (Table 7).** Ablations show that removing BAF or using only visual/textual features drops BLEU by 1.8–3.0 points on OCRMT30K and ReCTS. The "Visual Only" and "Textual Only" ablations are joint-training controls, so the drop isolates the contribution of multi-modal fusion.

- **State-of-the-art results on four diverse benchmarks against credible pipeline baselines.** On ReCTS with predicted coordinates, BLEU improves from 60.1 (best pipeline, MCTIT) to 62.2. The improvement is consistent across Chinese→English and English→Chinese datasets. The pipeline baselines are the more important comparison and are evaluated with GT coordinates + OCR, making the comparison fair.

- **Creation of a large-scale bilingual Scene TIMT dataset (STST800K).** 800K synthetic images from COCO + WMT22 pairs, plus real data relabeling with reading order and translations. This addresses a genuine data scarcity problem for paragraph-level scene-text translation.

- **Handles complex reading orders and ambiguities better than pipelines (Figure 4).** The qualitative case studies show concrete examples where the synchronous method corrects reading-order errors (non-zigzag layout) and resolves lexical ambiguity (e.g., "xiaomi" as trademark vs. "millet") using visual context — directly addressing the paper's stated motivation.

- **Competitive with large VLMs despite being a smaller task-specific model (Tables 5–6).** The method achieves 65.8 BLEU on ReCTS vs. 44.2 for Qwen-VL-max (whole image translation) and is comparable to AnyTrans, demonstrating that synchronous small-model training is a viable alternative.

---

## Weaknesses

### Fatal
None.

### Major

- **End-to-end baselines (UNITS, TESTR) are poorly specified, weakening the full evaluation picture.** The paper states (line 184) that these models were adapted "by training them for translation instead of recognition" — in one sentence with no architectural detail. No information is given about whether the recognition vocabulary was replaced, a separate decoder was added, or recognition output was fed into an external translation model. The reported scores are dramatically lower than the proposed method. While the paper's core claims do not depend on this comparison (the pipeline baselines and ablation provide the main evidence), the opaque specification and unexplained gap make this part of the evaluation scientifically sloppy. The paper should either describe the adaptation in detail, demonstrate that the resulting baseline is competitive, or remove these baselines and qualify the SOTA claim to cover only comparisons with pipeline methods.

### Minor

- **The "Remove BAF" ablation conflates two variables.** "Remove BAF" switches from joint training to separate training *and* removes the BAF module simultaneously. This makes it impossible to tell how much of the BLEU drop (42.73 vs. 50.47 on OCRMT30K) is due to losing multi-modal fusion vs. losing joint training. The "Visual Only" and "Textual Only" ablations partially address this (they use joint training without BAF), but a direct "joint training without BAF" variant using both features concatenated or summed would cleanly isolate the fusion mechanism's contribution.

- **The claim that BAF can compensate for recognition errors via position embeddings is asserted but untested.** The paper states (line 86): "even if the recognition result is wrong, BAF module is still able to guide cross-attention layer to collect visual information for translation according to position-related part in the query." This is a central claim for the BAF module's robustness, but no experiment directly validates it (e.g., by intentionally corrupting recognition tokens and measuring BLEU recovery with vs. without BAF). The case study in Figure 4 provides qualitative evidence for one example, but a targeted quantitative test would strengthen the paper.

- **No quality metrics reported for the relabeling process.** The real datasets were relabeled using an LLM API + human proofreading, but no inter-annotator agreement, acceptance rate, or error analysis is reported (Section 4.1.2). Since these labels serve as ground truth for evaluation, some quality assurance metrics would improve confidence. The concern is partially mitigated because pipeline baselines are re-evaluated on the same labels.

- **No error bars or confidence intervals on main results.** Tables 2–4 report single-point BLEU/Hmean estimates. Given the stochasticity in both detection and translation, reporting variance (e.g., bootstrap CI or multiple seeds) would make the improvements more convincing.

### Trivial

- **The loss weight α is stated to be "not sensitive" and can be set to 0.1, 0.5, or 0.9, but no sensitivity analysis is shown.** A brief ablation table would verify this claim.

- **IoU > 0.5 threshold for detection Hmean is coarse, and precision/recall are not reported separately.** This is standard practice in scene text, but separate reporting would add nuance.

---

## Nice-to-Haves

- Add a joint-training variant without BAF that feeds both visual and textual features via simple concatenation, to isolate the BAF cross-attention design.
- Directly test BAF's robustness to recognition errors by corrupting tokens and measuring BLEU recovery with vs. without BAF.
- Stratify results by layout complexity (e.g., number of text regions, spatial arrangement) to deepen the analysis of where joint training helps most.
- Report statistical significance or confidence intervals for main results.
- Show a brief ablation of loss weight α to verify the "not sensitive" claim.

---

## Removed Points

These were flagged for removal during consolidation. Treat with caution if referenced elsewhere.

- **"End-to-end baselines are invalid / undermine the SOTA claim entirely."** Overstated. The end-to-end baselines are poorly specified (a real issue, kept as Major), but the paper's core SOTA claim rests on the pipeline baseline comparison and ablations, not on the end-to-end baselines. The claim does not collapse.
- **"Related work is fragmented; Non-textual MMT section is irrelevant."** Subjective organizational preference; the section provides relevant background distinguishing MMT sub-areas. Removed per formatting/style rule.
- **"Improvement over pipeline baselines is modest and confounded by data/compute."** The "Remove BAF" ablation controls for architecture and training data, showing that the advantage persists even in a controlled setting. The critic acknowledged this. Removed because the confounding concern is already addressed.
- **"Better use of multi-modal feature is asserted not quantified."** This is abstract-level phrasing, not a technical weakness. Removed.
- **"Three-step training not motivated."** The paper states "for quicker converging" (line 160). Brief but sufficient. Removed.
- **"VLM comparison is not a strong baseline."** The comparison is reported for context, not as a primary baseline. The paper does not claim beating VLMs as a core contribution. Removed.
- **"Training data mixture ratio not specified."** Minor implementation detail; rule against nitpicking reproducibility. Removed.
- **"Missing tokenization details."** Ruled out per reproducibility nitpicking rule. Removed.

---

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation that the BAF module's position-embedding robustness claim is untested is a useful methodological critique but not a novel insight about the problem domain. The strength finder's observation that Table 4 provides the cleanest evidence for joint training (even with GT OCR, the synchronous model wins) is well-articulated but already present in the paper's own analysis.

---

## Suggestions

1. **Clarify or remove the end-to-end baselines.** Either detail how UNITS/TESTR were adapted for translation (replaced decoder vocabulary? added a translation head?) and show the adaptation produces a competitive baseline, or drop those comparisons and qualify the SOTA claim as "improves over pipeline approaches."
2. **Add a joint-training-without-BAF ablation.** Keep the training protocol identical to "Best" but use a simple fusion (e.g., concatenation) instead of the BAF cross-attention module. This would cleanly separate the contribution of joint training from the contribution of the BAF architecture.
3. **Directly test BAF robustness to recognition errors.** Artificially corrupt a fraction of recognition tokens at inference and measure BLEU with vs. without BAF.
4. **Report quality metrics for dataset relabeling.** Provide a sample-level acceptance rate, inter-annotator agreement (if multiple proofreaders), or error categorization for the LLM-generated translations.
5. **Add error bars.** Repeat the main experiments with 3 random seeds or use bootstrap resampling to report confidence intervals.

---
