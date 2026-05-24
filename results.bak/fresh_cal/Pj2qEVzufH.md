Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

---

## Summary

This paper proposes a mutual information shaping technique for 3D Gaussian Splatting that enforces correlations between Gaussians belonging to the same object. Rather than shaping Jacobians (which is expensive and fails after multiple parameter perturbations), the method shapes activations of the attribute-decoding network via an InfoNCE contrastive loss. This yields a representation where perturbing network parameters produces coherent changes across all Gaussians of an object, enabling efficient scene editing (segmentation, removal, movement, colorization) while only fine-tuning ~7% of Gaussians in about 1 minute.

## Strengths

- **Lightweight fine-tuning with concrete efficiency numbers.** The method samples only ~7% of Gaussians during fine-tuning and completes training in roughly 1 minute on a single RTX 3090 (Section 4.1, Section 4.2). This is a specific, verifiable advantage over full-set optimization methods.

- **Significant mIoU improvement on open-vocabulary 3D segmentation.** Table 1 shows that the method outperforms both NeRF-based (LERF, LERF-Mask) and 3DGS-based (Gaussian Grouping, JacobiGS) baselines by an average of 11% mIoU on the LERF-Mask dataset. Qualitative results (Fig. 4) show sharper boundaries and cleaner relevance maps.

- **Clear qualitative demonstration of consecutive-edit consistency.** Figure 6 shows that JacobiGS (the direct adaptation of Xu et al.'s approach) produces distortion after a second perturbation (the door behind the carton deforms), while the proposed method maintains coherent motion across multiple perturbations. This directly supports the paper's central claim about enabling sequential editing without reshaping.

- **Comparable reconstruction quality after shaping.** Table 2 shows PSNR on Mip-NeRF 360 and D-NeRF remains comparable to the baseline 3DGS, demonstrating that correlation shaping does not degrade view synthesis quality.

- **Automated 2D-to-3D mask association pipeline.** The method uses SAM (Kirillov et al., 2023) and DEVA (Cheng et al., 2023) to lift consistent 2D object masks to 3D Gaussian labels (Section 3.5, Fig. 3), providing a practical and fully automated supervision source for contrastive learning without manual 3D annotations.

## Weaknesses

### Fatal

None.

### Major

- **No quantitative evaluation of editing tasks.** The paper's central claim is enabling "efficient scene editing" and "consistent sequential edits," yet object removal (Fig. 5), object movement (Fig. 6), and colorization are shown only qualitatively. No metrics (e.g., CLIP score, LPIPS, FID, user study, or positional accuracy for movement) are reported for any editing task. The single quantitative table (Table 1) addresses only segmentation. While qualitative results for Fig. 6 are compelling, the paper makes quantitative-sounding claims (e.g., "significant performance improvements in... object removal and inpainting") that are unbacked by numbers. This is a significant evidential gap for a core advertised contribution.

### Minor

- **No efficiency comparison against baselines.** The paper reports its own training time (~1 minute, 7% Gaussians) but does not report comparable training time, peak GPU memory, or inference cost for Gaussian Grouping or JacobiGS. The claim of "lightweight" relative to prior work is therefore asserted rather than demonstrated numerically.

- **Unclear which layer's activations are shaped.** The derivation (Section 3.3) considers the weights \(W^{(l)}\) of the \(l\)-th linear layer and states that "\(\partial h\) corresponds to repeated activations \(\sigma(h^{(l-1)})\)." However, the paper does not specify **which** layer \(l\) is used for the contrastive loss in practice (e.g., the last layer, the first, or all layers), nor does it ablate this choice. This ambiguity hinders reproducibility.

- **No description of the 7% Gaussian sampling strategy.** The paper states that "we only sample about 7% of all the Gaussians during finetuning" but does not describe how this subset is selected (random? based on objectness scores? by spatial region?). The contribution of the sampling strategy to efficiency and performance is therefore unclear.

- **No analysis of mask quality or its effect on contrastive learning.** The 2D-to-3D mask lifting (Eq. 9) assigns a Gaussian's label based on the 2D mask of the pixel where it contributes most. The paper does not discuss how often Gaussians have ambiguous contributions (e.g., near object boundaries), how mask noise propagates to the contrastive loss, or how robust the method is to mask errors. This is relevant because the entire contrastive supervision depends on mask quality.

### Trivial

None.

## Nice-to-Haves

- Include a quantitative metric for editing quality (e.g., CLIP score for colorization, positional drift for movement, or a user study for removal plausibility). Even one automated metric would significantly strengthen the editing claims.
- Report comparative efficiency numbers (training time, GPU memory) for Gaussian Grouping and JacobiGS under the same hardware setup.
- Add an ablation showing the effect of using activation shaping vs. directly shaping Jacobians on the same network architecture.
- Clarify the choice of perturbation magnitude \(\sigma_s\) used in editing (Section 4.3) and whether results are representative or cherry-picked.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Theoretical derivation is "flawed"/"unsupported" (Harsh Critic Critical Issue #1).** The paper states (line 167): *"A detailed derivation and the proof of Eq. 7"* — this is in the appendix/supplementary, which the parser strips. The harsh critic's claim that "no derivation is provided" is incorrect; the derivation exists in the original submission. The mathematical specificity of the critique (outer product structure, matrix-valued cosine similarity) cannot be evaluated without seeing the appendix. This weakness is removed per the rule about missing appendix content.

- **"Table 1 is missing."** The table exists in the paper as an embedded image (line 249). Its absence in the reviewer's copy is a parser artifact.

- **"Missing comparison to original JacobiNeRF."** The paper constructs JacobiGS as a faithful adaptation of Xu et al.'s approach to 3DGS for fair comparison. This is a standard and appropriate methodology.

- **"No comparison to LangSplat."** Comparison to Gaussian Grouping (the most closely related 3DGS editing method) and JacobiGS is provided. Criticizing the absence of every possible baseline is scope creep.

- **"Missing related works."** Per instructions, these are not included as the reviewer cannot verify omissions independently.

- **Formatting/style nitpicks and typo claims.** These are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the key tension in the paper well: a promising technique with clear qualitative advantages and strong segmentation results, but with a significant evaluation gap in the quantitative assessment of editing tasks — which is the paper's claimed raison d'être. Neither reviewer identified a hidden flaw or missed connection to prior work that would fundamentally change how the contribution is perceived.

## Suggestions

1. **Add at least one quantitative editing metric.** The most impactful addition would be measuring positional consistency for object movement (e.g., deviation of the object centroid from the intended trajectory after multiple perturbations) or a perceptual similarity score (CLIP score or LPIPS) for object removal/colorization against ground-truth edited views. Even a small-scale user study (e.g., "which result looks more realistic?") would considerably strengthen the editing claims.

2. **Report comparative training time and memory.** Measure and report Gaussian Grouping's and JacobiGS's fine-tuning time and peak GPU memory on the same hardware (RTX 3090) so the "lightweight" claim is empirically substantiated.

3. **Clarify the implementation ambiguities:** (a) which layer \(l\) is used for the activation shaping loss and why, (b) how the 7% Gaussian subset is sampled, (c) the perturbation magnitude \(\sigma_s\) used in editing experiments and how it is set.

4. **Discuss mask quality limitations.** A brief analysis of how often SAM+DEVA produces inconsistent masks across views, and how the regularization loss \(\mathcal{L}_R\) (neighbor smoothness) mitigates this, would improve the paper's completeness and practical utility.

## Score and Decision

**Originality:** The activation-shaping approach (shaping activations instead of Jacobians to maintain consistency across sequential edits) is a novel extension of the JacobiNeRF idea to 3DGS with a practical efficiency benefit.

**Importance of research question:** Enabling coherent, efficient scene editing in 3DGS is timely and impactful for graphics, AR/VR, and robotics.

**Claims support:** The segmentation claim is well-supported (Table 1, +11% mIoU). The editing consistency claim is qualitatively supported (Fig. 6 shows a clear advantage over JacobiGS) but lacks quantitative backing. The lightweight claim is supported by absolute numbers but not by controlled comparison.

**Soundness of experiments:** Segmentation evaluation is sound (standard dataset, multiple baselines). Editing evaluation is qualitative only — insufficient to fully validate the central claim.

**Clarity of writing:** The paper is clearly structured and economically written. The theoretical section (3.3) could benefit from more exposition in the main text, though details are in the appendix.

**Value to the community:** The approach is practical (1 minute fine-tuning, automated mask lifting) and addresses a real gap in 3DGS editing. With added quantitative editing metrics and implementation clarifications, this would be a useful contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>