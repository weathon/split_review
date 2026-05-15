Now I have a thorough understanding of the paper. Let me write the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal

### Major

### Minor

### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me now compose the full review.

---

# Final Consolidated Review

## Summary

This paper proposes a synchronous (jointly-trained) framework for scene text image machine translation (Scene TIMT), unifying text detection, recognition, and translation into a single model. A Bridge & Fusion (BAF) module is introduced to fuse visual and textual features for translation, and a large-scale dataset (STST800K) is created for Chinese↔English scene text translation. The method achieves state-of-the-art translation performance on four benchmarks across two language directions.

## Strengths

1. **Joint learning consistently outperforms pipeline approaches** — The paper demonstrates this through multiple experimental conditions. Table 4 shows that even when pipeline methods receive ground-truth OCR results, the synchronous method achieves higher BLEU/COMET scores, especially on the layout-complex ReCTS dataset (BLEU 36.62 vs. 33.31). The "Remove BAF" ablation (separate training) in Table 7 also shows translation scores dropping substantially compared to the joint-trained "Best" configuration, confirming the benefit of joint optimization.

2. **BAF multi-modal fusion improves over single-modality translation** — The ablation in Table 7 compares using both visual and textual features (via BAF) against using only visual features or only textual features. The "Best" configuration outperforms both "Visual Only" and "Textual Only" on all four test sets, demonstrating that the multi-modal fusion mechanism effectively combines complementary information.

3. **Creation of a large-scale Scene TIMT dataset** — STST800K (800K image-translation pairs for both translation directions, with paragraph-level coordinates and reading order) fills a gap in the literature. Prior datasets either lacked translation labels (HierText, CTW1500) or were smaller (OCRMT30K). Using both synthetic data (COCO images + WMT22 bilingual pairs) and real data (relabeled via LLM and human proofreading) provides scale and diversity for training.

4. **Consistent SOTA across multiple benchmarks** — The method achieves top results on Chinese→English (OCRMT30K, ReCTS) and English→Chinese (HierText, CTW1500), with the gap over pipeline baselines being particularly pronounced on the more challenging ReCTS dataset with complex layouts.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Ablation study partially conflates joint training and BAF module effects** — The "Remove BAF" condition in Table 7 differs from "Best" in two ways: (a) training the spotting and translation modules separately, and (b) removing BAF. The observed drop in translation scores could stem from either change. While the "Visual Only" and "Textual Only" conditions do use joint training without BAF fusion and partially address this, neither condition tests joint training with both modalities processed through a simpler alternative (e.g., concatenation or addition without cross-attention). Thus, the specific contribution of BAF's cross-attention fusion mechanism over a simpler multi-modal baseline is not fully isolated. This does not threaten the paper's core claims (joint learning + multi-modal fusion > pipeline is well-supported), but it weakens the fine-grained claim about BAF's specific design.

2. **Reading order improvement is claimed but not directly evaluated** — The paper repeatedly motivates the synchronous approach by referencing reading order prediction errors (abstract, Section 1, Section 4.4.4), and Section 3.3 notes that "layout analysis [is] implicitly embedded in this sequence generation process, including paragraph segmentation and reading order prediction." However, the evaluation relies solely on translation metrics (BLEU, COMET) and detection Hmean — none of which directly measure reading order accuracy. The qualitative case study in Figure 4 is illustrative but anecdotal. A direct reading order metric (e.g., pairwise ordering accuracy, paragraph-level edit distance) would strengthen the claim.

3. **End-to-end baseline adaptation is underspecified** — The paper adapts text spotting models (UNITS, etc.) for translation by "training them for translation instead of recognition," but provides no details on how this was done — whether the output vocabulary, loss function, decoding procedure, or architecture were modified. While this does not invalidate the main results (the paper also outperforms pipeline baselines with GT OCR in Table 4, a cleaner comparison), it limits reproducibility of the end-to-end baseline comparisons.

4. **Loss weight α sensitivity is asserted without evidence** — The paper states that α "is not sensitive in training and could be set as 0.1, 0.5 or 0.9" (Section 3.6) with no supporting experiment shown. Given that α directly controls the trade-off between detection+recognition and translation during joint training, this claim could be trivially verified with a brief sensitivity study.

5. **Global self-attention in BAF is not ablated** — Section 3.4 claims that the self-attention layer applied to the visual feature "collect[s] global visual information which is helpful for translation," but no ablation removes or replaces this component to verify its contribution separately from the rest of the BAF module.

### Trivial
- The COMET model differs between main results (XCOMET-XL) and the AnyTrans comparison (wmt-22-comet-da). The paper explains this is to match AnyTrans's evaluation setup, which is reasonable, but it slightly limits within-paper comparability.
- The STST800K dataset description is detailed, but the exact train/test split between it and the existing benchmarks could be stated more explicitly.

## Nice-to-Haves
- A direct reading order accuracy metric (e.g., percentage of paragraphs with correct word ordering).
- An ablation with joint training + both modalities fused via a simple method (e.g., concatenation or averaging) to isolate BAF's cross-attention design.
- A sensitivity experiment for the loss weight α.
- Attention visualizations from the BAF module for the ambiguity/proper noun case studies.

## Removed Points
These points were identified in the reviewer inputs but are removed or weakened here after verification against the paper:

- **"Ablation study lacks a condition with joint training but no BAF"** — REMOVED as factually incorrect. The "Visual Only" and "Textual Only" conditions (Section 4.4.3) both use joint training without BAF fusion. The critic's claim that "Without a condition that uses joint training but omits BAF... the effect of BAF cannot be isolated" overlooks these existing conditions.
- **"BAF design is a straightforward application of existing attention mechanisms; novelty is limited"** — REMOVED as a subjective opinion/nitpick that does not identify any actual flaw in the paper's contribution. Many effective methods build on standard attention mechanisms.
- **"STST800K is described but never used as a test set"** — REMOVED; this misunderstands the dataset's purpose. It is a training dataset, not a test set.
- **"VLM comparison provides only partial conditions" and "VLM OCR ability stated without quantified evidence"** — REMOVED; the paper acknowledges API limitations for Qwen-vl-max (Section 4.4.2) and the claim is supported by Table 5 results (which are in figures but referenced in the text).
- **"Figure 1 is not visible"** — REMOVED; this is a parser/text-extraction artifact.

## Novel Insights
None beyond the paper's own contributions. The reviews did not surface a perspective that the paper itself does not already articulate.

## Suggestions
1. Add a direct reading order evaluation metric to substantiate claims about layout improvement.
2. Include an ablation that uses joint training with both visual and textual features but replaces BAF with a simpler fusion (e.g., concatenation followed by a linear projection) to isolate the benefit of the cross-attention design.
3. Specify how end-to-end baselines (UNITS, etc.) were adapted for translation, or replace them with a stronger pipeline baseline using a modern OCR.
4. Report a brief sensitivity analysis for the loss weight α (values 0.1, 0.5, 0.9) to support the "not sensitive" claim.
5. Clarify the train/test split between STST800K and the evaluation benchmarks.

## Score and Decision

This paper makes a genuine contribution to an underexplored problem: end-to-end scene text translation in complex layouts. The core results are consistent and convincing — the joint training and multi-modal fusion framework outperforms both pipeline baselines (even with GT OCR input) and adapted text spotters across four benchmarks. The STST800K dataset is a valuable resource. The weaknesses (ablation design, missing reading order metric, baseline specification) are real but moderate — they do not invalidate the paper's main claims, and most are addressable in revision or rebuttal.

**Score: 6.0**

**Decision: Accept**

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>