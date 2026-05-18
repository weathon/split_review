Now I have thoroughly verified the reviewer claims against the paper. Let me synthesize the final review.

## Summary

This paper proposes CLIP-DETR, a framework that integrates pretrained CLIP knowledge into DETR-based object detection through two training-only modules: **AlignNet**, which applies contrastive learning between ROI-pooled encoder features and CLIP-derived category+scale embeddings, and **DynQL**, which trains the decoder with multiple query sets at varying noise levels. On COCO, the method achieves 57.3 mAP with a CLIP-RN50x64 backbone and shows consistent gains on LVIS and open-vocabulary benchmarks.

## Strengths

- **Category- and scale-aware feature alignment is well-validated.** AlignNet's incorporation of object scale [w,h] alongside CLIP text embeddings yields a clear +0.8 AP improvement over category-only alignment (Table 5: 49.1 vs 48.3), and the ablation study showing that full bbox coordinates [cx,cy,w,h] underperform scale-only [w,h] (48.7 vs 49.1) provides an actionable and non-obvious design insight. This goes beyond typical region-text contrastive methods that only align with labels.

- **Diverse noise levels in DynQL are shown to improve decoder robustness.** The ablation in Table 6 demonstrates that a uniform distribution of noise levels (β from 0.1 to 0.9) across five DynQuery sets outperforms fixed-noise variants (49.7 vs 49.0 for β=0.5), supporting the paper's claim that exposing the decoder to a spectrum of query-object distances is beneficial. The systematic sweep over number of query sets (Table 7) further strengthens this finding, showing 5 sets as optimal.

- **Training-only design preserves inference efficiency.** Both AlignNet and DynQL are removed at inference (stated in Section 3.3 and Figure 1), meaning CLIP-DETR incurs zero additional computational cost at test time versus the baseline DETR architecture — a practical advantage over methods that permanently modify the architecture.

- **Thorough ablation studies across multiple design dimensions.** The paper independently ablates each component (Table 4), the content of attribute features (Table 5), noise level distribution (Table 6), and number of query sets (Table 7), all using a consistent 12-epoch Deformable-DETR baseline. This allows readers to isolate each design choice's contribution.

## Weaknesses

### Fatal
None.

### Major

- **The headline COCO result (57.3 mAP, +5.1%) is uninterpretable due to a missing backbone-controlled baseline.** The paper claims "When using the CLIP image encoder as the backbone, our method provided an even larger improvement of 5.1% mAP over the baseline" (line 175). However, the baseline reported in Table 1 — Deformable-DETR — uses a ResNet-50 backbone (46.5 mAP), *not* a CLIP-RN50x64 backbone. The appropriate baseline — Deformable-DETR with the same CLIP-RN50x64 backbone, without AlignNet and DynQL — is never reported. This means the 5.1% figure conflates the gain from switching to a stronger backbone with the gain from the proposed method. The paper does show a controlled 3.9% improvement with ResNet-50 backbone, but the stronger headline number cannot be attributed to the method alone. Reporting Deformable-DETR with the CLIP backbone is necessary to make the result meaningful.

### Minor

- **Direct comparison with DINO's denoising training is missing.** DynQL's core idea — training the decoder with extra queries at varying distances from GT — is closely related to the denoising training in DN-DETR and DINO. While the paper acknowledges this connection (line 21, lines 35–36), it never compares DynQL against DINO's denoising scheme under identical conditions (same backbone, same training setup). The ablation in Table 6 effectively tests noise distributions, but without a DINO-denoising baseline, the reader cannot tell whether DynQL's improvement comes from using CLIP-derived features as the base, from the multi-level noise discretization, or simply from the extra decoder queries generically. A controlled comparison would isolate the novelty.

- **The self-attention masking for DynQL is underspecified.** The paper states (line 134): "each DynQuery set can only interact with its own set and the conventional query set, while the conventional queries remain isolated from the DynQuery sets." This describes an asymmetric attention mask (DynQL→Conventional: attend; Conventional→DynQL: no attend), which is technically feasible. However, the exact masking pattern — which attention heads, how the mask is applied across decoder layers — is never specified, and the design choice is not justified. This makes reproduction unnecessarily difficult and also makes it hard to assess how DynQL differs from DINO, where denoising queries use full bidirectional attention with regular queries.

- **No direct evidence that AlignNet improves the encoder feature map beyond the pooled GT locations.** The contrastive loss in AlignNet is computed only on ROI-pooled features from ground-truth bounding boxes — a small number of spatial locations per image, all corresponding to foreground objects. The paper claims this "enhances the encoded feature map" (line 65) and makes it "more sensitive to objects" (Figure 1), but provides no feature-space analysis (e.g., feature similarity maps, attention map comparisons before/after AlignNet, or probe experiments) to show that the improvement generalizes across the full H×W spatial domain. The downstream mAP gains provide indirect evidence, but the claimed mechanism — that AlignNet produces a globally more discriminative source memory — remains unsubstantiated.

- **No variance estimates in ablation studies.** Tables 4–7 report single-run mAP values. Given that differences of 0.2–0.4 AP are common within random seed variation, several results (e.g., 52.1 vs 51.9 in Table 5) may not be statistically significant. Multi-seed runs with mean and std would substantially strengthen confidence in the reported design decisions.

### Trivial
- The paper refers to AlignNet as a "module" (Figure 1) when it is primarily a contrastive loss with a linear projection layer. This is a minor terminological overstatement.
- The paper does not explicitly state whether the CLIP text encoder is retained at inference for open-vocabulary classification. It is implicitly used (class embeddings are needed for the classification head), but this should be stated.

## Nice-to-Haves
- A discussion of limitations: AlignNet's reliance on GT boxes during training, the computational overhead of DynQL during training, and the scope of open-vocabulary gains.
- Training-time compute/memory overhead of DynQL (multiple query sets) relative to the baseline Deformable-DETR.

## Removed Points
These points are flagged to be removed by the instructions; treat them with caution.
- **Missing comparisons with Grounding DINO and YOLO-World**: The paper's choice of baselines (OV-DETR, CORA, Deformable-DETR, DINO, Co-DETR) is defensible for a DETR training-scheme paper. A demand for a different set of baselines is a matter of taste, not a structural weakness.
- **"AlignNet is not a network module" — stylistic nitpick**: Calling a contrastive-loss-plus-linear-projection a "module" is standard terminology in the field; this does not affect the technical contribution.
- **Criticism about self-attention masking being "contradictory"**: The paper's description is asymmetric but internally consistent (DynQL→Conventional attends, Conventional→DynQL does not). The critic's stronger claim that this is "functionally identical" to DINO's denoising is incorrect — DINO uses full bidirectional attention. The underlying concern (underspecification) is kept in Minor.
- **Criticism about the 5.1% gain being "unsubstantiated" without clarification**: Kept in Major as the missing CLIP backbone baseline concern; the stronger framing as fully unsubstantiated is removed since the ResNet-50 controlled result (3.9%) does provide partial evidence.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Report Deformable-DETR with CLIP-RN50x64 backbone** (without AlignNet/DynQL) as a proper baseline in Table 1. This is essential to decompose the 57.3 mAP result into backbone gain vs. method gain.
2. **Add a controlled comparison between DynQL and DINO's denoising scheme** under identical conditions (same backbone, same training schedule, same number of extra queries). This would isolate whether the benefit comes from multi-level noise, CLIP-derived features, or the asymmetric attention masking.
3. **Specify the exact attention masking pattern** for DynQL: provide a matrix diagram or a precise description of which rows/columns are zeroed. Justify why asymmetric masking is preferred over full bidirectional attention.
4. **Provide feature-space evidence for AlignNet's effect on the encoder**: compare feature similarity maps, Grad-CAM activations, or recall using encoder-only ROI heads with and without AlignNet training.
5. **Report means and stds over 3+ seeds** for the ablation tables, particularly for the small-gap comparisons in Tables 5, 6, and 7.
6. **Add a limitations section** covering AlignNet's GT-box requirement, DynQL's training overhead, and the scope/caveats of open-vocabulary generalization.

## Score and Decision

The paper proposes a plausible and well-motivated direction — using CLIP to supervise both encoder feature alignment and decoder query diversity in DETR — and provides systematic ablation studies that validate several design choices. The controlled ResNet-50 results (3.9% gain) and open-vocabulary improvements do support the method's effectiveness.

However, the missing CLIP-backbone baseline undermines the headline 57.3 mAP / +5.1% result, making it impossible to attribute the gain to the proposed modules versus the stronger backbone. Combined with the underspecified attention masking and the absence of a direct comparison against the most closely related prior work (DINO denoising), the paper's claimed improvements cannot be fully verified. These are addressable issues, but they are substantive enough that the paper in its current form does not meet the bar for acceptance.

**MY FINAL SCORE: <pineapple>5.0</pineapple>**
**MY FINAL DECISION: <orange>Reject</orange>**