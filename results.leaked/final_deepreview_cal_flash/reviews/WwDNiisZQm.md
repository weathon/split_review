Now I have all the information needed to write the consolidated review.

## Summary

This paper introduces Content-Aware Mamba (CAM) for learned image compression, proposing two mechanisms to address Mamba's rigid raster-scan order and strict causality when applied to 2D images: (1) Content-Adaptive Token Permutation (CTP), which clusters latent tokens by feature similarity and reorders the scan to group semantically related tokens, and (2) Global-Prior Prompting (GPP), which injects sample-specific global priors into the SSM by conditioning its output matrix on cluster-derived prompts. The resulting CMiC model achieves SOTA BD-rate savings over VTM-21.0 (15.91–21.34% across Kodak, Tecnick, CLIC) while reducing parameters by 56% and GPU memory by 78% relative to the prior best Mamba-based compressor MambaIC.

## Strengths

- **State-of-the-art rate-distortion performance with strong evidence.** CMiC achieves BD-rate reductions of 15.91%, 21.34%, and 17.58% over VTM-21.0 on Kodak, Tecnick, and CLIC respectively (Table 1), outperforming all prior Mamba-based LIC models (MambaVC, MambaIC) on both BD-rate and efficiency. The RD curves (Figs. 4–6) show consistent gains across all bitrates.

- **Clean component-level ablation quantifying individual contributions.** Ablation (Table 2) shows CTP alone improves BD-rate by 1.8–2.4%, GPP alone adds 0.5–1.4%, and their combination yields 2.7–3.6% total gain. The two components are clearly complementary, and the gains are meaningfully decomposed.

- **Substantial efficiency-accuracy advantage over competing Mamba-based codecs.** CMiC reduces parameters by 56%, FLOPs by 57%, decoding latency by 39%, and peak GPU memory by 78% compared to MambaIC (Table 1), while improving BD-rate. This validates the claim that a single content-adaptive scan can outperform multi-directional 2D scanning at lower cost.

- **Well-designed visualizations supporting the claimed mechanisms.** ERF comparisons (Figs. 7–9) show that GPP extends the gradient-based receptive field beyond the causal scan path, and CTP reshapes it toward semantically related regions. The clustering visualizations (Fig. 10) confirm that tokens are grouped by semantically meaningful features (e.g., red doors, sky, feathers), supporting the claim that permutation is content-aware.

- **Structural ablation validating CAM block design.** Table 4 compares CAM blocks against Conv, 2D Mamba, attention-only, and CAM-only variants at comparable parameter/FLOP budgets, demonstrating that the hybrid window-attention + CAM design outperforms all alternatives.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Gradient flow through the hard clustering and permutation is not explicitly specified.** The paper describes centroids updated via non-gradient EMA (Algorithm 1) and notes that the projection \(\mathcal{A}(\cdot)\) is differentiable, but does not explain how gradients from the rate-distortion loss flow through the hard argmax assignment (Γ) and the discrete permutation (π). A traceable path exists — the gather/scatter operation is differentiable, so gradients reach the feature extractor via the permuted token values — but the paper should make this explicit, for instance by stating whether straight-through estimation, soft assignments during training (the ERF computation in §4.5 uses "soft clustering"), or another approach is employed. This omission leaves the "end-to-end" claim imprecisely supported.

- **The non-causality claim would benefit from more precise phrasing.** The paper consistently uses "mitigates" and "relaxes" strict causality, which is appropriate. However, the caption of Fig. 9 states GPP "introduces non-causality beyond raster scan," and the associated text says the model can "see beyond the strictly causal scan." Since the forward SSM remains causal (each token depends only on its predecessors), the effect shown is primarily that the ERF (computed via backpropagation) reveals gradient influence through the global prompt, not that the forward inference uses future tokens. Distinguishing forward causality from gradient-based influence would tighten the argument and avoid potential misinterpretation.

- **A non-content-adaptive permutation baseline would strengthen the CTP ablation.** The ablation shows CTP outperforms the fixed raster-scan baseline, but does not compare against a non-content-adaptive reordering (e.g., sorting by a simple hand-crafted feature, or a fixed random permutation). Such a control would isolate whether the gains come from semantic grouping or merely from breaking the spatial order. The current evidence (cluster visualizations in Fig. 10, BD-rate gains in Table 2) makes the semantic interpretation plausible, but the control would make it conclusive.

- **Some training hyperparameters are missing.** The EMA decay λ for centroid updates and the learning rate schedule are not specified. The paper provides initial learning rate (10⁻⁴), optimizer (Adam), K-Means iterations (T=5), and cluster count (K=64), which covers the most critical settings, but full reproducibility requires the missing values.

- **The method labeled "MambaC" in Table 1 should be "MambaIC" for consistency with the text and the cited paper (Zeng et al., 2025).** This is a minor naming inconsistency.

### Trivial
None.

## Nice-to-Haves

- A forward-only ERF measurement (e.g., input perturbation without backpropagation) would complement the gradient-based analysis of GPP's effect.
- An analysis of how clustering quality evolves during training could help understand the interaction between the EMA-updated centroids and the gradient-updated feature extractor.

## Removed Points

These points were raised in the input reviews but are removed after verification against the paper:

- **Criticism that the clustering initialization is "not justified"**: The paper explicitly states the initialization is "inspired by VQ-VAE" and divides the first batch into K consecutive segments. This is a standard and adequately justified initialization.
- **Claim that the ERF evidence is "misinterpreted"**: The paper computes ERF via the standard gradient-based method (Luo et al., 2016). The ERF patterns in Fig. 9 correctly show that GPP expands the gradient receptive field beyond the causal scan path. The paper's interpretation is sound; the only issue is a wording precision point (captured in Minor weaknesses).
- **Criticism that the paper does not discuss "how the gradient from the rate-distortion loss reaches the projection layer \(\mathcal{A}(\cdot)\)"**: The paper explicitly states "the mapping \(\mathcal{A}(\cdot)\) is differentiable and trained end-to-end for the final rate-distortion objective" (Sec. 3.4). The gradient path through the differentiable prompt computation is clear.
- **Request for FLOPs computation details (e.g., "standard profile tool")**: Standard practice in the field; not a meaningful weakness.
- **Criticism that the paper should "cite FLOPs carefully"**: Already standard practice; the paper reports FLOPs measured on 2K-resolution images uniformly.

## Novel Insights

The most interesting observation that emerges from the reviews is the tension between the paper's "non-causality" framing and the actual mechanism: GPP does not make the SSM's forward recurrence bidirectional, yet it demonstrably expands the gradient-based effective receptive field to cover the entire image. This suggests that conditioning the SSM output matrix C on a global, content-derived prompt can serve as a practical substitute for multi-directional scanning — a finding that could inform future SSM designs for vision beyond compression. The intermediate observation that only 23–26 of 64 centroids are activated per image (Table 5), with semantically consistent centroids emerging (e.g., Centroid #10 for edges, #26 for red/yellow textures, #33 for smooth blue/green areas), provides interesting evidence that the codebook learns a shared semantic vocabulary across images.

## Suggestions

1. **Clarify gradient flow**: Explicitly state how gradients pass through the hard clustering and permutation — whether via straight-through estimation, soft assignments during training, or by treating the permutation as a differentiable gather operation with stop-gradient on the assignment indices. A brief note in Sec. 3.3 or the training details would suffice.
2. **Rephrase the ERF causality discussion**: Distinguish between forward inference (where the SSM remains causal) and gradient-based analysis (where GPP creates non-causal influence paths). Change the Fig. 9 caption from "introduces non-causality" to "introduces non-causal gradient influence" or similar.
3. **Add a control ablation for CTP**: Compare CTP against a non-content-adaptive reordering (e.g., fixed random permutation, or sorting by token norm) to empirically confirm that semantic grouping is the source of gain, not merely breaking spatial order.
4. **Report missing hyperparameters**: Include the EMA decay λ for centroid updates and the learning rate schedule (or a statement that a constant rate was used).

## Score and Decision

**Calibration Anchors Used:**

*Round 1 (Bracketing):*
- RmmrHEH6Nx (GroupMamba, 3.00) — Lower anchor, Mamba for vision but not compression; weaker method.
- cagNCwQEEN (Multimodal Instruction Tuning with Hybrid SSM, 3.40) — Lower anchor.
- KgJwbsfN7G (MambaVC, 4.80) — Direct LIC competitor, similar topic; CMiC is substantially stronger in novelty, results, and evaluation depth.
- XKQ2qzajbU (GlobalMamba, 5.00) — Image serialization for Mamba; different domain.
- 4UiLqimGm5 (Coordinate-Aware Modulation, 7.00) — Neural fields; CMiC is slightly below in theoretical depth but comparable in empirical rigor.
- CxXGvKRDnL (Progressive Compression with Diffusion, 8.00) — High anchor, diffusion-based compression; CMiC is in a different methodological class.

*Round 2 (Narrowing within bracket 4.5–7.5):*
- iDe1mtxqK5 (Spatial-Mamba, 7.00) — Structure-aware state fusion for vision Mamba; CMiC has more specific architectural contribution for compression but less theoretical unification.
- PQpvhUrA1C (AR Pretraining with Mamba, 5.75) — Accepted. CMiC has stronger architectural novelty and more comprehensive evaluation.
- 0A6f1b66pE (Unleashing SSM in VLM, 4.60) — Lower anchor; CMiC is clearly stronger.
- UAKnJMIBwf (MambaPEFT, 6.00) — Accepted. CMiC comparable in quality with different focus.

*Bracket formed in Round 1:* 5.0–7.0. The paper is clearly above MambaVC (4.80) and comparable to AR Pretraining with Mamba (5.75) and MambaPEFT (6.00) but below Spatial-Mamba (7.00) in theoretical depth.

*Round 2 narrowing:* Compared against these anchors, CMiC's novel architectural components (CTP, GPP), SOTA compression results with strong efficiency, and thorough ablation/visualization work position it above the 5.75–6.00 accepted anchors. The weaknesses (gradient flow clarity, causality phrasing, missing control ablation) are all addressable and do not undermine the core contribution. The paper sits closer to the upper end of the bracket.

**Final Score:** 6.5  
**Decision:** Accept

The paper presents a well-motivated, novel adaptation of Mamba for image compression. The two proposed mechanisms (CTP and GPP) are clearly described and empirically validated with SOTA results across three standard benchmarks. The evaluation is comprehensive, including component ablations, structural ablations, complexity analysis, and informative visualizations. The weaknesses are minor clarity issues that can be resolved in revision; none threaten the core contribution. The work advances the state of the art in Mamba-based learned image compression and provides insights (content-adaptive scanning, global-prior prompting) that may inform future SSM designs for vision.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>