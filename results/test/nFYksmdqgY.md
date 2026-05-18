Now I have all the information I need. Let me compose the final consolidated review.

---

## Summary

This paper proposes an unsupervised multi-modal machine translation (UMMT) method that uses cross-modal contrastive learning to align source and target language representations via images. The method introduces sentence-level and token-level contrastive objectives during initialization, enabling the model to learn source-to-target mapping from monolingual image-text pairs before iterative back-translation. Experiments on Multi30K and COCO show consistent improvements over both text-only and multi-modal baselines, with the model requiring no image input at inference time and demonstrating out-of-domain generalization on IWSLT.

## Strengths

- **Novel cross-modal contrastive initialization for UMT**: The paper proposes using sentence-level and token-level contrastive learning with images as language-agnostic pivots to initialize unsupervised MT — directly addressing the initialization bottleneck. The approach shows clear gains: an average +5.1 BLEU over MASS and +2.3 BLEU over the prior SOTA SG across four language directions (Section 4.5, Table 1, verified from text lines 167–169).

- **Inference-time image-free pipeline**: Unlike prior UMMT systems (UMMT, PVP) that require images as input during inference, the proposed model is trained with visual data but tested without any image input (Section 4.2, line 134). This is a practical advantage explicitly discussed and controlled for in the evaluation.

- **Demonstrated out-of-domain generalization**: The method achieves improvements on text-only IWSLT14 EN-DE and IWSLT17 EN-FR (Table 6, Section 5.3) using only the 70K image-text pairs for initialization — without additional images or text-to-image retrieval. This shows the cross-modal alignment transfers beyond the multi-modal domain, which prior UMMT works did not demonstrate.

- **Comprehensive ablation isolating each component**: Table 3 cleanly separates the contributions of cross-modal initialization (~5.1 BLEU), language modeling (~5.3 BLEU), and token-level contrastive (~1 BLEU over sentence-level). Text-to-image retrieval (Table 4) and PCA visualization (Figure 2) directly confirm semantic alignment is achieved.

## Weaknesses

### Fatal

None.

### Major

- **Ambiguous data split for initialization vs. evaluation (needs clarification)**: The initialization data consists of "75,000 monolingual image-text pairs for each language, combining half of the COCO and Multi30K datasets" (line 132). For Multi30K, "half" clearly means half of the 29K training set (14,500). However, for COCO, the paper reports working with the "Caption 2015 set, consisting of 121,000 image-text pairs" (line 123), and the evaluation includes a "MsCOCO test set" with 461 instances. The paper does **not** explicitly state whether those 461 test images were excluded from the 121K pool from which the 60,500 half was drawn. If any test-set images appear in the initialization data, the reported BLEU scores would be compromised. This is a documentation gap that the authors **must** clarify — while it is very likely that standard train/test splits were used (the paper follows Huang et al. 2020), the omission is consequential enough that the experiments cannot be fully trusted without an explicit statement. The paper should also state whether the 60,500 COCO initialization pairs were drawn exclusively from the training split. (Note: this does **not** invalidate results on Multi30K Flickr2016/Flickr2017, as those test sets are separate from Multi30K training.)

- **Inconsistent claim about outperforming UNMT in Table 5**: Section 5.2 states: "As shown in Table 5, our model exhibit significant improvements compared to other baselines, even outperforming UNMT (Lample et al., 2018a) that underwent back-translation training" (line 210). Table 5 is titled "BLEU scores **without back-translation**" and includes MUSE (word-by-word baseline) as a comparison. The text is ambiguous about whether the UNMT comparison is a separate claim about the full model or is also attributed to Table 5. If the former, the writing is misleading and the connection to Table 5 is unclear. If the latter, it is a direct contradiction since a w/o-BT model cannot be said to outperform UNMT (which uses BT) within a table about w/o-BT scores. The authors must clarify what Table 5 actually shows and reconcile the claim with the reported numbers. (The exact numerical values in the table image cannot be verified from the text extraction but the text-level inconsistency is clear.)

### Minor

- **Text-only baselines are outdated**: The text-only comparisons are against MUSE (2018), UNMT (2018a), XLM (2019), and MASS (2019). More recent unsupervised MT methods such as CRISS or mBART unsupervised variants are not discussed. While the paper's primary comparison is against other UMMT methods (where the comparison is fair and up-to-date through SG 2023), this weakens the generality of the claim that cross-modal initialization surpasses strong text-only approaches. The paper should either add more recent text-only baselines or explicitly scope this claim to the UMMT setting.

- **Image encoder choice (ViT) is not controlled across multi-modal baselines**: The paper uses a pretrained ViT as image encoder. Prior UMMT baselines (UMMT, PVP, SG) may use different visual features (e.g., ResNet, VGG). If ViT provides stronger visual representations, some of the reported improvement may stem from the encoder choice rather than the contrastive alignment method itself. An ablation using the same visual backbone as prior work would strengthen the attribution.

- **No variance or significance reporting**: Ablation studies (Table 3) and main results (Tables 1–2) do not report run-to-run variability or statistical significance. Given the small test set sizes (1,000 and 461 instances), variance could be meaningful. Adding multi-seed runs or significance tests would increase confidence in the reported gains.

- **Missing analysis of token-level selective attention**: The token-level contrastive learning uses selective attention (Section 3.3) but there is no qualitative analysis of whether attention actually aligns text tokens to semantically relevant image patches. An attention map visualization would substantiate the fine-grained alignment claim.

### Trivial

None.

## Nice-to-Haves

- A discussion of limitations — e.g., what happens when images are abstract or ambiguous, or when source/target language images have incomplete semantic overlap — would strengthen the paper.
- Comparing the *quality of initialization* more directly (e.g., comparing after-initialization-but-before-BT performance against a text-only initialized model using the same encoder/decoder architecture and training data) would better isolate the impact of cross-modal alignment.

## Removed Points

- **"Potential data contamination could invalidate *all* results"** (from Harsh Critic, excessively harsh framing): The concern is legitimate but the reviewer exaggerated its severity. Even if overlap existed (which is unlikely given standard practices), contaminating 461 test images in a 75K initialization set would not automatically invalidate results on all datasets — Multi30K Flickr2016 and Flickr2017 remain unaffected. The core concern is kept in Major as a documentation gap.
- **"Table 5 shows Ours (w/o BT)=18.7, UNMT=20.1 EN-DE"** (specific numerical values): These exact numbers cannot be verified from the text extraction (Table 5 is an embedded image). The broader inconsistency claim is kept. The specific values may or may not be accurate — the review focuses on the textual inconsistency which is verifiable.
- **Several generic strengths from Strength Finder** (removed as generic/superficial): The original strengths list contained claims like "this paper addressed an important problem" and "this paper targeted an interesting question" which lack specific evidence. Only verified, citation-grounded strengths are kept.

## Novel Insights

The most interesting tension across the reviews is that while both the Harsh Critic and the Strength Finder agree the paper's core idea is well-motivated, they fundamentally disagree on whether the experimental validation is sound. The Harsh Critic raises legitimate documentation gaps (data splits, claim consistency) that, if resolved, would likely shift the assessment significantly. The paper's main vulnerability is not its method but its presentation — the actual contributions (inference-time image-free, cross-modal initialization with token-level granularity, out-of-domain generalization) are genuinely novel within the UMMT space and are supported by consistent positive results across multiple settings. The data contamination concern, while needing clarification, is unlikely to be an actual flaw given standard dataset splits; it is primarily a documentation failure. The Table 5 inconsistency is more concerning because it touches the paper's central narrative about initialization quality.

## Suggestions

1. **Explicitly state** that test-set images (Flickr2016, Flickr2017, MsCOCO test) were excluded from the 75K initialization pool, and describe the exact split used for COCO (e.g., "we used the Karpathy training split for COCO Captions and took a random 60,500 subset, ensuring no overlap with the 461-image test set").
2. **Clarify Table 5**: State clearly what models are being compared, and either (a) correct the claim about outperforming UNMT if the numbers don't support it, or (b) clarify that "even outperforming UNMT" refers to the full model (after BT) and is a separate claim from the w/o-BT results shown in Table 5.
3. **Add variance estimates** (at minimum, report BLEU across 3 seeds for the main conditions).
4. **Add attention map visualizations** for the token-level selective attention component to substantiate the fine-grained alignment claim.

## Score and Decision

The paper presents a well-motivated method with consistent empirical gains over strong baselines, and the core contributions (cross-modal contrastive initialization, inference-time image-free pipeline, out-of-domain generalization) are genuinely novel within the UMMT space. However, two documentation gaps — the ambiguous data split description and the inconsistent claim around Table 5 — prevent unconditional acceptance. These issues are addressable in a revision and do not undermine the core contribution, but they must be resolved before the paper can be fully trusted.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>