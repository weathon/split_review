Now I'll produce the final consolidated review.

---

## Summary

This paper proposes CaPT (CLIP as a Prior Teacher), a framework that integrates CLIP into semi-supervised learning via asymmetric-modalities co-training. It jointly trains a fully fine-tuned unimodal vision network and an adapter-tuned CLIP model that exchange co-pseudo labels through entropy-weighted fusion. The paper also presents Theorem 1.1 bounding pseudo-label error under a Gaussian-mixture model to motivate the approach. Empirically, CaPT achieves strong results across SSL benchmarks (e.g., +21.38% on CIFAR-100 with 1 label/class over RegMixMatch) with modest computational overhead (+8% memory, +11% time).

## Strengths

1. **Strong and consistent empirical results in extreme low-label regimes.** CaPT outperforms the second-best method by 21.38% on CIFAR-100 (82.51% vs. 60.49%) and 4.05% on EuroSAT (96.33% vs. 92.28%) under one-label-per-class (Table 3). On ImageNet with 10 labels/class, it beats RegMixMatch by 9.33% Top-1 (Table 2). These are not marginal gains; they reflect a qualitative shift where existing SSL methods collapse but CaPT does not.

2. **Well-designed ablation study validates every component.** Table 6 systematically ablates six variants (CaPT-Ada, CaPT-Deb, CaPT-Uni, only UPM, only MPM, w/o feat aug., equal weights), each causing a clear performance drop (0.57% to 16.51%). This convincingly shows that adapter-tuning, bidirectional information flow, feature-augmented consistency, and entropy-based weighting all contribute meaningfully.

3. **Low computational overhead relative to performance gains.** Table 4 shows CaPT adds only 8.00% more memory (5050 vs. 4676 MiB) and 11.18% more training time compared to FreeMatch, while improving accuracy by 6.23%. This stems from freezing CLIP's encoders and using feature-level Mixup instead of input-level strong augmentation — a practical design choice.

4. **Asymmetric-modalities design is a principled advancement over symmetric co-training.** The paper identifies that two unimodal ViTs (as in CLS) learn similar representations despite different initializations (Figure 3), and motivates why cross-modal (vision + vision-language) co-training produces more complementary representations. This is grounded in the co-training literature's requirement for view independence (Blum & Mitchell, 1998).

5. **Fine-grained evaluation partially addresses data contamination concerns.** Table 5 evaluates on 6 fine-grained datasets where CLIP's training corpus overlap is less of a concern. CaPT outperforms baselines on 5 of 6 datasets (e.g., 94.71% vs. 80.23% on Flowers102 with 1 label/class), showing the benefit is not limited to benchmarks CLIP may have seen.

## Weaknesses

### Major

1. **The main comparisons are confounded by CLIP's external knowledge, and the framing overstates the SSL-specific contribution.** The central tables (Tables 1-3) compare CaPT against standard SSL methods (FixMatch, FreeMatch, RegMixMatch, etc.) that use only the benchmark's labeled+unlabeled data plus standard supervised pre-training (ImageNet-21k). These methods do not have access to CLIP's cross-modal training on 400M image-text pairs. The 21.38% gap on CIFAR-100 highlighted in the abstract is almost certainly dominated by CLIP's external knowledge, not by the SSL algorithm design alone. The paper acknowledges this in passing (Section 4.4) but the primary narrative ("breaking label dependency") frames the comparison as a methodological victory rather than an expected outcome of incorporating a much larger pre-trained model. The paper does include adapter-tuned CLIP and CLIP zero-shot results in Table 1, and the fine-grained evaluation (Table 5) helps — but the headline claims and tables foreground the uncontrolled comparison. This is a framing issue, not a fatal flaw, but it inflates the apparent contribution significantly.

2. **Theorem 1.1 contains a 2^{d/2} factor that makes the bound vacuous for real images, and the theorem does not connect to the method.** The bound (Eq. 1) contains a multiplicative factor of 2^{d/2} where d is the input dimension. For any real image (e.g., d = 224×224×3 ≈ 150,528), 2^{d/2} is astronomically large (~10^22,000), rendering the bound trivially satisfied regardless of all other terms. The condition g/2 > r would need to counteract this exponential, which requires unrealistically large inter-class distances. Moreover, the theorem is about a nearest-prototype classifier in pixel space, not about modern SSL methods or about CaPT's mechanism (asymmetric co-training, adapter-tuning, entropy-weighted fusion). The theorem neither informs the method design nor plays any role in the evaluation. Contribution #1 ("theoretically establish the label dependency") is therefore unsupported. The empirical motivation (Figure 1) is already sufficient; the theorem should be removed or substantially reworked to connect to the actual method.

### Minor

3. **On STL-10, adapter-tuned CLIP alone outperforms the full CaPT framework.** From Table 1: on STL-10 with 4 labels/class, adapter-tuned CLIP achieves 96.86% while CaPT (unimodal network) achieves 96.07%. With 10 labels/class, adapter-tuned CLIP gets 97.15% vs. CaPT's 96.34%. Since CaPT's final reported accuracy is the unimodal network's, and the CLIP branch alone is better on these settings, the paper should discuss why the co-training framework does not uniformly improve the stronger branch, or report the best branch when it wins. The paper does note that the unimodal network is used because it has more learnable parameters and is fully fine-tuned, and CaPT does dramatically improve the unimodal network (from ~87% to ~96%), but the anomaly deserves explicit investigation.

4. **Missing variance estimates in key low-label experiments.** Tables 2 (ImageNet), 3 (one-label-per-class), and 5 (fine-grained datasets) report single numbers with no standard deviations. Table 1 does report ± values for three seeds. Given that the one-label-per-class setting could be highly sensitive to which specific image is selected, the absence of variance estimates undermines confidence in the headline numbers (e.g., 21.38% improvement on CIFAR-100 1-shot).

5. **Entropy weighting operates at the batch level, not per-sample.** Equations 11-12 compute a single entropy value per module per batch, so all samples in a batch share the same module weight. This cannot capture sample-specific reliability differences (e.g., when the unimodal network is confident on one sample but CLIP is confident on another). A per-sample weighting scheme would be more principled. The ablation (Table 6) compares entropy weighting only against a constant 0.5, not against per-sample weighting, so the benefit of the batch-level scheme specifically is not isolated.

6. **Feature-level Mixup is qualitatively different from the input-space strong augmentations used in the UPM branch.** The paper refers to feature Mixup as "strong augmentation" for CLIP (Section 3.2.2), but this is very different from aggressive input-space augmentations (RandAugment, etc.) applied in the UPM branch. This asymmetry in augmentation strength between the two branches is not discussed as a potential confound when interpreting which branch benefits more from co-training.

### Trivial

- None.

## Nice-to-Haves

- The pattern-homogeneity bottleneck claim (Figure 3) would benefit from quantitative evidence such as CKA similarity between the two branches, rather than qualitative attention maps alone.
- The per-batch entropy weighting could be extended to per-sample weighting; this would likely improve the method further.
- The EuroSAT case is interesting: CLIP zero-shot (49.46%) is poor, adapter-tuned CLIP (93.83%) is much better, and CaPT (96.60%) improves further. This suggests adapter-tuning + co-training rescues CLIP's domain gap — a positive result worth highlighting more clearly.

## Removed Points

- *Figure 1c not tabulated.* Acceptable for a conference paper; figures with quantitative heatmaps are standard.
- *"Reorganize tables to foreground CLIP-based comparisons."* Subjective presentation preference; the current organization is standard for SSL papers.
- *"Missing CKA analysis for pattern homogeneity."* Moved to Nice-to-Haves; qualitative attention maps are a reasonable starting point.
- *"Clarify whether SSL baselines use pre-trained ViTs."* The paper explicitly states: "USB adopts the pre-trained ViTs" and "our unimodal network uses the same training configuration and backbone as USB" (Section 4.1).
- *"Pure formatting/style nitpicks."* These are parser artifacts, not author errors.
- *"Missing appendix content."* The parser strips these; they exist in the original submission.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the contribution** around "how to effectively integrate vision-language models into SSL" rather than "breaking label dependency." The current framing overclaims relative to what is actually demonstrated.

2. **Remove or substantially rework Theorem 1.1.** The 2^{d/2} factor makes it vacuous for image data, and it does not connect to the method. The empirical Figure 1 is sufficient motivation. If a theoretical contribution is desired, it should address the co-training dynamics of asymmetric modalities or when an external prior provably helps SSL.

3. **Add variance estimates to Tables 2, 3, and 5.** This is essential for the one-label-per-class results, where the specific seed could determine which image is selected.

4. **Investigate and discuss the STL-10 anomaly.** If adapter-tuned CLIP alone outperforms CaPT, this should be analyzed rather than left as an unexplained observation.

5. **Consider per-sample entropy weighting** as a natural extension that could improve the method further.

## Score and Decision

**Round 1 bracket:** Based on the calibration search, the paper sits between the weak band (avg scores 2.5–3.4, rejected, "Multi-Vision Multi-Prompt" at 2.50, "LLM2CLIP" at 3.00) and the strong band (avg scores 8.0, accepted, "Compositional Entailment Learning" at 8.00). The most informative anchors are SemiCLIP (5.80, Accept) and GPS-SSL (5.33, Reject).

**Round 2 narrowing:** SemiCLIP (5.80, Accept) is the closest topical anchor: it also uses CLIP in a semi-supervised setting but is a different task (fine-tuning CLIP vs. using CLIP as a teacher for SSL). CaPT has more dramatic empirical results (+21.38% vs. +1.72–6.58%) and cleaner ablations, but also has more significant issues (Theorem 1.1, STL-10 anomaly, framing inflation). GPS-SSL (5.33, Reject) uses CLIP as prior knowledge for SSL and was criticized for the same "unfair comparison" issue; CaPT handles this better (includes CLIP baselines) but adds additional weaknesses. The Cleaning Label Noise paper (4.50, Reject) was similarly criticized for unfair comparison. CaPT sits above GPS-SSL and the cleaning label noise paper, but below SemiCLIP when accounting for all issues.

**Final calibration:** Compared to SemiCLIP (5.80, Accept), CaPT has stronger results but weaker theoretical grounding and a more significant confound issue. Compared to GPS-SSL (5.33, Reject), CaPT has stronger controls (CLIP baselines included) and better ablations. The paper's core contribution — the asymmetric co-training framework — is solid and well-validated, but the inflated framing and flawed theorem prevent a higher score.

**Anchors consulted:**
| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/HfJxXbXlYJ.md | 3.00 | 1 | Weaker: CLIP extension paper with limited novelty |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/FwkYeLovHk.md | 3.33 | 1 | Weaker: weak-to-strong generalization for CLIP |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/j1FLTvgyAh.md | 2.50 | 1 | Weaker: multi-prompt CLIP few-shot learning |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/hgayrNSbri.md | 3.40 | 1 | Weaker: image captioning retrieval augmentation |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/97D725GJtQ.md | 5.80 | 1,2 | Comparable but different setting: SemiCLIP fine-tunes CLIP semi-supervised; accepted but had novelty concerns |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/1rgMkDWfYV.md | 4.50 | 1 | Bottom of bracket: label cleaning with CLIP; rejected due to unfair comparison concern |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/xrazpGhJ10.md | 5.50 | 1,2 | Comparable: SemCLIP for semantic alignment; rejected for limited novelty |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/gqjEhvUC6H.md | 4.50 | 1 | Bottom of bracket: data de-duplication for CLIP training |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/3i13Gev2hV.md | 8.00 | 1 | Stronger: hyperbolic VLM with compositional entailment; clearly a stronger paper |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/ExZ5gonvhs.md | 5.33 | 2 | Relevant: GPS-SSL uses CLIP prior for SSL; rejected for unfair comparison and limited novelty |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/RgWATMmWmz.md | 4.75 | 2 | Bottom of bracket: CLIP for weakly supervised learning |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/Tn6lrFbiP4.md | 6.33 | 2 | Stronger: bridging information asymmetry in video retrieval |
| /home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/2y8XnaIiB8.md | 5.50 | 2 | Comparable: vision-language dataset distillation |

**Final assessment:** The paper proposes a well-designed, practically useful framework for integrating CLIP into SSL, with strong empirical results and clean ablations. However, the framing overstates the contribution (the dominant mechanism is CLIP's external knowledge, not a new SSL principle) and the theoretical component (Theorem 1.1) is vacuous for real images and disconnected from the method. The paper would benefit from honest reframing and removal of the theorem.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>