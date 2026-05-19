- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 8, 6
Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

This paper proposes MM-FSS, the first multimodal approach to few-shot 3D point cloud semantic segmentation (FS-PCS). It introduces a cost-free multimodal setup that leverages class names (textual modality) during meta-learning and inference, and uses 2D image features *implicitly* during pretraining only — no 2D images are needed at test time. The method employs a shared 3D backbone with two heads (intermodal and unimodal), a Multimodal Correlation Fusion (MCF) module to aggregate correlations from different modalities, a Multimodal Semantic Fusion (MSF) module to refine correlations using text-guided semantic weighting, and a Test-time Adaptive Cross-modal Calibration (TACC) module. Experiments on S3DIS and ScanNet show consistent and substantial improvements over prior state-of-the-art (e.g., +4.3% to +10.2% mIoU across settings).

## Strengths

1. **Novel and well-motivated multimodal FS-PCS setup.** The paper is the first to explore multimodality in the few-shot 3D point cloud segmentation literature. The cost-free framing — using class names (always available during annotation) as the textual modality and 2D features only during pretraining — is practical and clearly scoped (Section 1, Section 3.1).

2. **Consistent and substantial empirical gains.** MM-FSS outperforms prior SOTA across all settings on both S3DIS and ScanNet (Tables 1 and 2). Gains are especially large in the more challenging 2-way settings (e.g., +10.2% on ScanNet 2-way 1-shot, +8.7% on S3DIS 2-way 5-shot), supporting the claim that multimodal information directly improves few-shot generalization.

3. **Systematic ablation validation.** The paper provides controlled ablations isolating each component: MCF alone (+0.76%), MSF alone (+1.52%), their combination (+2.14%), and the full system with TACC (+4.04% over the baseline in 1-shot, Table 3a–3f). The modality ablation (Table 3d) separately tracks the contribution of image and text modalities. The TACC adaptive indicator is shown to outperform any fixed coefficient (Table 3e).

4. **Practical and efficient design.** The implicit use of the 2D modality (pretraining only) means the method works on datasets without 2D images (e.g., S3DIS, via transferred pretrained weights from ScanNet). The complexity overhead over COSeg is modest (29.21G vs. 27.76G FLOPs, +2.5M params, Table 3g) despite large performance improvements.

5. **Qualitative evidence supports quantitative results.** Visual comparisons (Figures 3, 4) show MM-FSS producing cleaner segmentation masks with fewer false positives than COSeg, consistent with the reported mIoU gains.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **No ablation isolating the specific fusion architecture from the mere presence of text.** The paper shows that adding the text modality yields the largest single jump (+3.28 mIoU in 1-shot ScanNet, Table 3d) and that the proposed fusion modules outperform the baseline. However, a simple text-integration baseline — e.g., taking the UF-only features and concatenating text similarity scores as additional channels to the correlation map before decoding, without the MSF module or its learned weighting — is not evaluated. Such a baseline would directly demonstrate whether the architectural complexity of MCF+MSF is necessary or whether any reasonable text injection achieves similar gains. The existing MSF-linear comparison (Table 3f) is a step in this direction but still operates within the MSF module structure; a simpler non-MSF baseline would strengthen the evidence for the specific fusion design. This does not undermine the paper's core claim (multimodality helps), but it modestly weakens the evidence for the uniqueness of the architectural contribution.

2. **Absence of variance/confidence intervals for main results.** The episodic evaluation protocol produces notable variance between splits (e.g., ScanNet 2-way 1-shot: S0=43.99 vs. S1=34.43, a 9.56 mIoU gap). The paper reports only mean mIoU across two splits without standard deviations or confidence intervals. While reporting split-level results is standard practice in FS-PCS, adding error bars or 95% confidence intervals across evaluation episodes would significantly strengthen the reliability of the reported gains, especially for smaller margins (e.g., the +2.7% in ScanNet 1-way 1-shot).

3. **Several implementation details not specified in the main paper.** The following details are absent from the main text: the numeric value of the prototype count $N_P$, whether the LSeg text encoder is kept frozen during meta-learning, the backbone initialization strategy (from scratch vs. pretrained), and the batch size during meta-learning. Some of these may reside in the supplementary material (referenced as `sec:moredetails`), but the main paper would benefit from at least stating the key values (especially $N_P$ and the freezing status of components).

4. **Ambiguity in baseline configuration labeling.** In Table 3a, the "no MCF, no MSF" row (40.69) matches the "UF head only" row of Table 3b. This consistency is inferable but not explicitly stated, which briefly slows interpretation of the ablation.

### Trivial
None.

## Nice-to-Haves
- A minimally simple text integration baseline (e.g., text similarity scores concatenated to UF-only correlations) to cleanly separate the benefit of *having text* from the benefit of the *proposed fusion architecture*.
- Confidence intervals or standard deviations for the main results and key ablations.
- A failure case analysis showing where text guidance misleads the model (e.g., due to ambiguous class names), which would improve scientific depth.

## Removed Points

*These points were flagged for removal from the final review. Treat them with caution.*

- **"Missing 2D-3D alignment details (projection parameters, handling of occlusions, loss formulation)"** — The paper explicitly references the appendix (`sec:moredetails`) and cites Peng et al. (OpenScene) for these details. Per review policy, missing appendix details that the parser strips are not valid criticisms.
- **"Unfair comparison — COSeg† should also get text via simple addition"** — COSeg† is a control for backbone quality (no text), not a fair comparison target. The main comparisons are against the original COSeg. The critic's framing proposes a new baseline that does not exist in the literature.
- **"Missing architectural details of IF/UF heads"** — The paper states "following the design of its third stage" of Stratified Transformer, which provides sufficient architectural identity for a conference paper; exact channel dimensions are reasonably deferred to the appendix.
- **"Support point sampling details missing"** — The paper states points are voxelized at 0.02m grid size and randomly sampled to a maximum of 20,480 points per block (line 244), which addresses this concern.
- **"Freezing strategy not stated"** — The paper explicitly states: "Second, we conduct meta-learning to train the model end-to-end while freezing the backbone and IF head" (line 115). This is clearly stated.

## Novel Insights

None beyond the paper's own contributions. The reviews surface useful suggestions (additional baselines, variance reporting) but do not uncover a conceptual weakness or alternative interpretation that the paper missed.

## Suggestions
1. Add a simple text integration baseline: compute text-query similarity from IF features and add it as an additional channel to the UF-only correlation map before the decoder head, bypassing MCF and MSF. This would cleanly separate the value of *having text* from the value of the *proposed fusion mechanism*.
2. Report 95% confidence intervals or standard deviations across evaluation episodes (or across multiple random seeds) for the main results and key ablations.
3. Explicitly state the numeric value of $N_P$, the backbone initialization method, and whether the text encoder is frozen, either in the main paper or a dedicated implementation table.
