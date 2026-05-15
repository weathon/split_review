Now I have a thorough understanding of the paper and can evaluate each reviewer claim against the actual text. Let me compose the final review.

---

## Summary

This paper proposes CDAM (Class Distribution-induced Attention Map), a training-free method for open-vocabulary semantic segmentation. The key insight is that even when CLIP-based methods produce noisy patch-level predictions, the full class distributions of patches belonging to the same object are highly correlated. CDAM uses Jensen-Shannon divergence between patch-wise class distributions to construct an attention map for CLIP's final layer, assigning higher attention weights to patches likely belonging to the same object. The method also includes multi-scale aggregation, augmented text prompts, and entropy-based background thresholding. CDAM can be integrated into existing training-free CLIP-based segmentation methods (MaskCLIP, SCLIP, ClearCLIP, GEM) without retraining, and shows consistent mIoU improvements across multiple benchmarks with minimal inference overhead (≤34 ms).

## Strengths

- **Novel and well-motivated core idea**: The observation that patch-wise *class distributions* (rather than hard predictions) are robust for identifying same-object patches is empirically verified: distribution similarity correctly identifies same-class patches 78.9%/79.4% of the time on VOC21 (vs. 67.0%/70.8% for direct prediction). Using JS divergence to exploit this for attention map construction is a clean, principled approach (Section 3.2.1).

- **Consistent and substantial performance gains**: CDAM improves mIoU across all four tested baselines (MaskCLIP, SCLIP, ClearCLIP, GEM) on multiple datasets with and without background classes (Tables 1, 2). The ablation study (Table 3) isolates the contribution of each component (AttnCDAM, multi-scale, ATP, entropy thresholding), showing that all four modules contribute positively.

- **Training-free and computationally efficient**: CDAM does not require retraining or fine-tuning and adds at most 34 ms of inference overhead (Section 4.3). It is approximately 200× faster than CaR, making it practical for applications where training is infeasible.

- **Principled evaluation protocol**: The paper adopts a unified protocol (TCL) that prohibits dataset-specific hyperparameter tuning and renaming tricks, and does not apply PAMR post-processing. This is a transparent and fair approach for comparing training-free methods.

## Weaknesses

### Major

- **The GEM baseline reproduction is concerning and requires clarification**: The paper reports reproduced GEM numbers that are dramatically lower than the original published results (original: ~45 mIoU on VOC21 with PAMR). The paper explains that it strips renaming tricks and removes PAMR post-processing, and a significant drop is expected, but the magnitude of the claimed drop (to single digits) is extreme. Since the table is an image in the extracted text, the exact numbers cannot be verified here, but if the reported GEM baseline is genuinely in the range of 4–5 mIoU on VOC21, this raises questions about the reproduction fidelity. The paper defers reproduction details to supplementary material (which is not available in the extracted text). **This does not invalidate the CDAM contribution** — the gains on MaskCLIP, SCLIP, and ClearCLIP are independent and still stand — but it weakens the quantitative evidence on the GEM variant and undermines the comparison with "state-of-the-art" claims. The authors must either provide a convincing explanation for this gap or replace the GEM baseline with a faithful reproduction.

### Minor

- **The central observation of correlated class distributions lacks statistical rigor**: Section 3.2.1 reports point estimates (78.9%, 79.4%, etc.) but provides no variance, number of trials, or description of the sampling procedure across images/patches. Since this observation is the foundation of the entire method, reporting at least standard deviations or confidence intervals would substantially strengthen the paper. The reference to supplementary material is noted, but this is a case where main-paper numbers should be self-contained.

- **Hyperparameter sensitivity is not analyzed in the main paper**: The temperature τ=0.1, entropy modulation α=2.5, and the set of seven scaling factors M are all fixed across datasets, which is good practice under the unified protocol. However, no sensitivity analysis appears in the main text (only referenced to supplementary). Without demonstrating that results are robust to reasonable variations in these values, there is a risk that the reported gains depend on cherry-picked settings.

- **The abstract slightly overstates compatibility**: The abstract claims CDAM "can be synergetically used together" with other prior arts, while Section 4.2 (line 137) acknowledges that CaR and CLIP-DIY are "structurally incompatible" because they use CLS tokens while CDAM relies on local visual tokens. The limitation is properly disclosed, but the broad claim in the abstract could mislead readers.

- **The integration of CDAM with CLIP's last attention layer could be described more precisely**: Section 3.2.4 states CDAM is "incorporate[d] into the last attention layer" and that features from layer L-1 are used as values, but it does not explicitly state whether the query/key projections from the last layer are bypassed (as in MaskCLIP's identity replacement) or retained. From the formulation (Eq. 2–3), it is clear that CDAM replaces the attention map entirely, but making this explicit would aid reproducibility.

### Trivial

- The thresholding component (Section 3.3) uses `H(S)_center` defined as the average of the maximum and minimum entropy values. "Center" is an unusual and potentially misleading term for this quantity (which is essentially the midpoint of the range, not a mean/centroid). Consider "midpoint" or simply describing the formula directly.

## Nice-to-Haves

- Including a sensitivity analysis for τ, α, and M (even as a brief main-paper table or plot) would strengthen confidence in the method's robustness.
- Adding comparison with adaptive thresholding baselines (e.g., Otsu) for background segmentation.
- Reporting failure cases where distribution similarity breaks down (e.g., visually distinct objects with similar semantics).
- Extending experiments to additional ViT backbones (SigLIP, EVA-CLIP) to demonstrate generality beyond OpenCLIP ViT-B/16.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *Criticism about GEM numbers being "impossible" to explain* — The paper explicitly strips PAMR and renaming tricks under a unified protocol. While the magnitude of the reported drop is surprising, the harsh critic's claim that it "cannot be explained" is an overstatement. This is retained as a Major concern (above) but in weakened form.
- *"Table 1 formatting is garbled"* — This is a parser artifact, not an author error. Removed per Hard Rules.
- *"Section 2.2 on background subtraction is largely textbook"* — The section briefly surveys classic methods and explains why they are not directly applicable. This is reasonable context-setting. Removed.
- *"PAMR not being applied changes the performance landscape"* — The paper is fully transparent about this and explicitly states it in Section 4.1. Removed per Hard Rules (strawman — paper already disclosed this).
- *"Qualitative results are selective"* — Applies to virtually all qualitative evaluations. Removed per Hard Rules (generic nitpick).
- *"No standard deviations or multiple runs"* — For deterministic zero-shot segmentation with frozen CLIP, single-run evaluation is standard practice in this field. Moved to Nice-to-Haves.
- *Strength from Strength Finder about "empirical verification"* — Retained as valid strength. However, the Strength Finder's framing of "the single most important piece of evidence is that CDAM consistently and substantially improves mIoU" is accurate.
- *"The method's use of self-self attention mechanisms"* in related works — This is a description, not a specific strength/weakness claim. Removed as generic.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify the GEM reproduction**: Provide the exact GEM numbers reported in Table 1 in the main text and include a brief explanation in the paper body (not just supplementary) of why these differ from the original GEM paper — specifically, quantify the effect of removing PAMR, renaming tricks, and any other protocol differences.

2. **Add error bars to the core observation**: Report the variance or confidence intervals for the distribution similarity experiment in Section 3.2.1, or at minimum describe the sampling methodology (number of images sampled, patches per image, number of random trials).

3. **Include a brief hyperparameter sensitivity paragraph**: Even a single small table or paragraph showing mIoU on VOC21 for 3–4 values of τ and α would significantly strengthen the paper.

4. **Make the layer integration explicit**: Add a sentence clarifying that CDAM *replaces* the standard attention map (Softmax(QK^T)/√d) in CLIP's last layer, analogous to MaskCLIP's identity replacement, and that query/key projections are bypassed.

## Score and Decision

The paper presents a novel, well-motivated, and training-free approach to improving open-vocabulary semantic segmentation. The core idea is clever, the ablation study is well-structured, and CDAM shows consistent improvements across multiple baselines and datasets with minimal overhead. The main quantitative concern — the anomalously low GEM baseline numbers — does not invalidate the other results but needs clarification. The remaining issues (statistical rigor, hyperparameter sensitivity, presentation precision) are addressable and do not threaten the paper's core contribution. Overall, the paper makes a solid contribution to the field.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>