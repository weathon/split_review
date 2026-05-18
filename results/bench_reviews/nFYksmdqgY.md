Now I have everything I need. Let me synthesize the final review.

## Final Analysis Summary

**Paper:** Cross-modal contrastive learning (sentence + token level) for unsupervised MT initialization using images as pivots.

**Key cross-checks:**
- **Data confound (Criticism 1):** Valid concern but overstated. The 75k image-text pairs = ~0.74% additional data beyond the 10.145M sentences used in LM. A 5.1 BLEU gain from 0.74% more text data alone is extremely implausible. Nevertheless, a text-only contrastive baseline would strengthen the claim. → **Minor weakness, not fatal.**
- **Unfair SG comparison (Criticism 2):** The paper states "all entries ... are tested without image input given." The SG adaptations and UMMT*/PVP* adaptations were all done by Fei et al. (2023) — the SG paper itself. There's no evidence of unfairness. → **Removed.**
- **Data leakage (Criticism 3):** The paper doesn't specify which COCO split (train/test) was used for the "half of COCO" training images, and whether it overlaps with the MsCOCO test set (461 instances). Following Huang et al. (2020) suggests they used the standard split, but this should be documented explicitly. → **Minor weakness.**
- **ViT frozen/fine-tune (Section notes):** Not specified. → **Trivial.**
- **Strength Finder** is mostly accurate. Strength #3 about ablation isolating contributions is partially undercut by the data confound issue (weakness wins), but the ablation still shows cross-modal initialization is crucial even accounting for the caveat.

Let me write the review.

Score calibration: This paper has real empirical contributions (novel method, solid benchmarks, 2+ BLEU over SOTA UMMT, 5+ over text-only). It's stronger than the 5.0 anchor (sign language paper with 0.2 BLEU) and comparable to the 6.0-7.0 papers. The weaknesses are addressable and don't threaten core claims. I'd place it around 6.0-6.5.## Summary

This paper proposes a novel unsupervised multi-modal machine translation (UMMT) method that uses cross-modal contrastive learning (at both sentence and token levels) to align source and target languages in a shared semantic space via images as language-agnostic pivots. The key idea is to leverage monolingual image-text pairs to create a strong initialization for back-translation, without requiring images at inference time. Experiments on Multi30K, IWSLT, and Czech-English show consistent improvements over both text-only (MASS, XLM) and multi-modal (UMMT, PVP, SG) state-of-the-art methods, with an average +5.1 BLEU over MASS and +2.3 BLEU over SG.

## Strengths

- **Novel and well-motivated approach for the UMT initialization problem.** The paper identifies that proper initialization is critical for UMT (as established by prior work) and develops a principled cross-modal contrastive method that directly addresses it. The use of images as alignment pivots is well-justified by the observation that visual semantics are language-agnostic.

- **Large and consistent empirical gains across diverse settings.** The method achieves +5.1 BLEU over the text-only baseline MASS and +2.3 BLEU over the previous multi-modal SOTA SG across four language directions on Multi30K (Table 1). These gains hold on out-of-domain IWSLT (Table 6) and on Czech-English, a typologically distant language pair (Table 7). The cross-modal initialization alone (before back-translation) already surpasses a fully trained UNMT system (Table 5), which is a strong result.

- **Ablation and analysis provide supportive evidence for the alignment mechanism.** Text-to-image retrieval (Table 4) and PCA visualization (Figure 2) confirm that the contrastive objectives bring text and image representations closer, and that source and target languages become better aligned in the shared space. The token-level objective adds a ~1 BLEU refinement over sentence-level alone.

- **Inference-time image-free.** Unlike prior UMMT systems that require images at inference (e.g., UMMT, PVP), the proposed method only uses images during initialization and is tested without image input, making it more practical.

## Weaknesses

### Fatal
None.

### Major
None. The criticisms raised about the paper are addressable in a revision and do not undermine the central contribution.

### Minor

1. **Missing controlled ablation for the data confound.** The cross-modal initialization adds 75k image-text pairs plus a contrastive objective on top of the text-only baseline. A text-only contrastive baseline (e.g., SimCSE-style on the captions without images) would cleanly isolate the contribution of the visual modality. That said, 75k sentences represent only ~0.74% additional data relative to the 10.145M sentences already used in language modeling, making it extremely unlikely that the 5.1 BLEU gain stems from "more text" alone — but the experiment would strengthen the central claim.

2. **Unclear COCO train/test split.** The paper uses "half of COCO Caption 2015" for training but does not specify whether this is the standard training split or a random subset. The Multi30K evaluation includes an MsCOCO test set (461 instances). The authors should explicitly state which COCO split was used and confirm it is disjoint from any test set images. Following Huang et al. (2020) makes this likely but the paper should document it.

3. **SG baseline comparison documentation.** The paper asserts that all UMMT baselines are "tested without image input given," but only explicitly describes visual-hallucination adaptations for UMMT* and PVP*. Since SG is from the same paper (Fei et al., 2023) that performed these adaptations, the comparison is likely fair — but adding a clarifying sentence about SG's inference setup would eliminate ambiguity.

### Trivial

- The ViT image encoder training dynamics (frozen vs. fine-tuned) are not specified, making the method hard to reproduce fully. The paper should state whether ViT parameters are updated during cross-modal initialization.

## Nice-to-Haves

- A text-only contrastive initialization baseline (e.g., SimCSE or a cross-lingual contrastive loss on additional monolingual text) to directly decompose the contributions of "cross-modal" vs. "extra data + contrastive objective."
- Cross-lingual retrieval (source-to-target sentence similarity) as a metric to quantify whether the common space brings languages closer, complementing the current text-to-image retrieval.
- An analysis varying the number of image-text pairs used in cross-modal initialization to show scaling behavior.

## Removed Points

These points are flagged to be removed; treat them with caution:
1. **"Unfair comparison with SG"** — The paper states all UMMT systems are tested without image input. SG (Fei et al., 2023) is from the same paper that performed hallucination adaptations for UMMT and PVP, so the comparison is fair. The critic's concern is speculative and not supported by evidence.
2. **Section-by-section notes about missing appendix/proofs** — The parser strips these sections; they exist in the original submission.
3. **"Pure formatting/style nitpicks"** (ambiguous footnotes/symbols in tables, etc.) — These are presentation details that don't affect the scientific content.
4. **"Token-level gain not tested for significance"** — Statistical significance testing is not standard practice for BLEU-based translation evaluation in this community; this is a nice-to-have, not a weakness.
5. **"Text-to-image retrieval doesn't measure cross-lingual alignment"** — The PCA visualization (Figure 2) directly shows cross-lingual alignment. The retrieval task confirms the cross-modal alignment that enables the cross-lingual one. Both analyses support the claim.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation that the paper itself does not already make.

## Suggestions

1. **Add a text-only contrastive initialization baseline.** Fine-tune the model on the same 75k captions with a SimCSE-style contrastive loss (without images) during initialization. If the cross-modal model still outperforms, the role of images is directly confirmed. If the gap narrows, the paper should acknowledge that part of the gain comes from the contrastive objective itself, while still claiming the rest is attributable to cross-modal alignment.

2. **Clearly document the COCO split.** State explicitly: "We use the COCO Caption 2015 training split (half of it, following Huang et al. (2020)), which is disjoint from the COCO test images used in the Multi30K MsCOCO test set."

3. **Specify whether ViT is frozen or fine-tuned.** Add one sentence to Section 4.3 or 4.2 describing whether the ViT parameters are updated during cross-modal initialization.

## Score and Decision

**Calibration anchors (batch-retrieved, ranked by avg score):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/uAFHCZRmXk.md` | 8.00 | Strong analysis paper with comprehensive controls and deep investigation. The paper under review has a stronger applied contribution but weaker controls. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/bqoHdVMIbt.md` | 7.00 | Multimodal domain generalization paper with solid experiments and acceptance. Comparable novelty and experimental scope. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/LuVulfPgZN.md` | 6.00 | Novel OOM generalization problem with reasonable method. The paper under review has stronger empirical results and clearer practical contribution. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/eeaKRQIaYd.md` | 5.00 | Unsupervised sign language paper with similar problem framing but very weak results (0.2 BLEU). The paper under review achieves 18+ BLEU and is substantially stronger empirically. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/P7s4WYF1rf.md` | 4.33 | Multilingual CLIP adaptation, rejected for limited novelty. The paper under review has stronger methodological novelty. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/g7DHM6MRE4.md` | 3.50 | Weak applied MT paper with limited scientific contribution. The paper under review is substantially stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/MyotJECv0D.md` | 2.50 | Very weak correlational analysis, rejected. Not comparable. |

The paper under review has a well-motivated novel method, strong and consistent empirical results across multiple benchmarks and language pairs, and supportive analysis. The weaknesses are addressable and do not threaten the core claims. Relative to the calibration anchors, the paper sits comfortably above the 5.0–6.0 range and below the 8.0 analysis papers — it is a solid empirical contribution with minor methodological gaps.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>