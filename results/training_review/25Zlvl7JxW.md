Now I have the full picture. Let me compose the final consolidated review.

---

## Summary

This paper proposes HQGS, a 3D Gaussian Splatting framework for novel view synthesis under image degradations (low resolution, JPEG compression, blur, noise, and mixed). The key contributions are: (1) an Edge-Semantic Fusion Guidance (ESFG) module that extracts edge-aware and semantic features to guide Gaussian primitive placement toward detail-rich regions, and (2) a Structural Cosine Similarity Loss (L_SCS) that enforces global low-frequency structural consistency. Experiments on LLFF and DeblurNeRF datasets across five degradation types show consistent improvements over NeRF-based and 3DGS-based baselines, with particular strength under severe degradation.

## Strengths

- **Unified framework covering multiple degradation types.** Unlike prior methods that target specific degradations (e.g., NeRFLiX for blur, SRGS for low resolution), HQGS handles five degradation scenarios and achieves the best or second-best results on all of them (Tables 1, 2). This directly supports the claim of a general solution.

- **Significant quantitative gains validated by thorough ablation.** The ESFG module yields a 1.38 dB PSNR improvement over vanilla 3DGS (Table 3, V6 vs. V1 on blurry 'Wine'), and the L_SCS loss adds another 0.87 dB over L1 alone (Table 4, V4 vs. V1). The ablations systematically isolate each component's contribution.

- **Strong robustness under increasing degradation severity.** Under noise variance 50, HQGS maintains 26.31 dB PSNR vs. 23.21 dB for SRGS and 23.32 dB for NeRFLiX (Table 6). Under 8× downsampling, HQGS leads by 1.26 dB over SRGS and 1.71 dB over NeRFLiX. The margin grows with degradation strength, which is the paper's headline robustness claim and it is well-supported.

- **Favorable training-time vs. quality trade-off.** Figure 8 shows that 5 minutes of HQGS training already exceeds the PSNR and LPIPS of 3DGS trained for 9 minutes on blurry scenes, demonstrating practical utility.

## Weaknesses

### Fatal

None. The paper's core claims (that edge-guided feature modulation improves 3DGS under degradation, and that the proposed loss helps global structure) are supported by experimental evidence. The reported results are consistent and the improvements are credible.

### Major

- **The ESFG module's feature-to-Gaussian mapping is underspecified to the point of being unreproducible from the paper alone.** The description (lines 82–84) states that after down-sampling I′ and E′ to shape N×H/2×W/2×3 and concatenating per camera, MLPs produce I′_M and E′_M of shape M/2×3, where M is the number of Gaussian primitives. Three critical gaps remain: (1) *Dynamic M* — M changes during training due to 3DGS cloning/splitting/pruning, yet MLPs have fixed input/output dimensions. How the network adapts to a varying output size M/2 is not explained. (2) *2D-to-3D correspondence* — How features extracted from 2D image coordinates map to specific 3D Gaussian primitives (which are in 3D space, not in 1:1 correspondence with pixels) is unspecified. (3) *Cross-attention dimensions* — The attention operates on features of dimension 3 (E′_M, I′_M ∈ ℝ^{M/2×3}), which is mechanically unusual and no details are given about how query/key/value are handled or what the attention weights are applied to. While the general idea (edge guidance for Gaussian placement) is conceptually clear, a researcher attempting to re-implement HQGS from the paper alone would be blocked by these ambiguities. Code release is promised and would resolve this, but as a published description it is insufficient.

- **The robustness evaluation training protocol is not stated.** Section 4.4 constructs progressive degradation test sets (noise σ=0,10,25,50; resolution 1×,2×,4×,8×) but does not specify whether models are trained at a single degradation level and tested across levels (which would genuinely test robustness) or trained separately at each level (which would just repeat the main results at different severities). The paper's main robustness claim hinges on this distinction, and the protocol must be stated explicitly. Given that Section 3.1 defines fixed training degradations (noise σ=10, 4× downsampling), it is likely the former design, but this should be confirmed.

### Minor

- **The L_SCS loss uses the degraded input's edge map to define low-frequency regions of the *target* clean image.** Equation 6 defines R_S = (1 − ∇I′) ⊙ R and T_S = (1 − ∇I′) ⊙ T, where ∇I′ is the normalized gradient of the *input* (degraded) image. If the input is blurry, its edge map misses edges present in the clean target, so (1 − ∇I′) will erroneously include some high-frequency regions from the target in the "low-frequency" loss. The paper does not discuss this mismatch or why it is not harmful in practice. A discussion or a variant using the rendered image's own gradient would strengthen the analysis.

- **The cross-attention branch underperforms the edge-only variant.** In Table 3, V4 (cross-attention between SAF and EAF) achieves 27.70 dB, while V3 (EAF alone) achieves 27.88 dB. Yet the final model V6 includes cross-attention. The paper reports the numbers but does not discuss why the attention mechanism hurts when used alone yet contributes positively in the full configuration. A brief analysis (e.g., that cross-attention acts as regularization when combined with concatenation, or that the features are complementary but need joint training) would be helpful.

- **The claim about Gaussian primitive redistribution (Figure 2b) is supported only by qualitative visual comparison.** The paper asserts that ESFG "distributes more Gaussian primitives in detailed areas" but provides no quantitative evidence (e.g., a count of primitives near detected edges before vs. after ESFG). Given that this is the central motivation for the ESFG module, a quantitative validation would significantly strengthen the paper.

- **Notation inconsistency for the ⊙ operator.** The paper states that ⊙ denotes matrix multiplication (lines 80, 90), but uses it for operations that are clearly element-wise (Hadamard) products between tensors of incompatible dimensions for matrix multiplication (e.g., ∇I′ ⊙ I where both are N×H×W×3, and Sigmoid(F′_M) ⊙ μ where F′_M ∈ ℝ^{M/2×3} but μ ∈ ℝ^{M×3}). This is confusing and should be corrected.

### Trivial

- Table 5's comparison across high-frequency operators (Gaussian filter, Laplace, Sobel) is presented without discussing computational overhead. This is a minor omission.

## Nice-to-Haves

- Evaluation on real-world degraded data (e.g., hand-held blurry captures, Internet photos with unknown compression) would strengthen the claim of general applicability to real-world conditions. The paper uses synthetic degradations on LLFF (real scenes) and DeblurNeRF (synthetic scenes). While this is standard practice in the field, the abstract's reference to "common in real-world data collection" invites the natural expectation of at least one real-degradation experiment.
- A simple baseline that conditions 3DGS on a learned image feature *without* edge maps would isolate the contribution of edge-specific guidance beyond general feature conditioning.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism about baseline retraining fairness (NVSR adaptation).** The reviewer speculates that "baselines may not be properly tuned" without evidence. The paper states all methods are retrained on low-high pairs following standard protocol; this is common practice.
- **Criticism about "code not released."** The paper promises code release, which is standard. (Hard rule.)
- **"General framework" claim as unsupported.** The reviewer argues that synthetic degradation does not prove real-world applicability. While this is a valid nuance, it is scope creep — almost all papers in this sub-area evaluate on synthetic degradations. It is noted above as a Nice-to-Have rather than a weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an independent observation about the method or the problem that the paper itself does not already convey.

## Suggestions

1. **Clarify the ESFG module's feature-to-Gaussian mapping.** Provide pseudocode or a precise description of how the MLPs handle dynamic M, how 2D features are associated with specific Gaussians, and how the cross-attention is dimensioned. This is the single most important fix.
2. **Explicitly state the training protocol in Section 4.4.** A single sentence — e.g., "All models are trained at [noise σ=10 / 4× downsampling] and tested on the progressive test sets without fine-tuning" — resolves the ambiguity.
3. **Address the L_SCS edge-map mismatch in the text**, explaining why using the input's ∇I′ is acceptable or proposing an alternative.
4. **Add quantitative evidence for Gaussian redistribution** — e.g., the average number of primitives within edge-adjacent regions before vs. after ESFG on a representative scene.
5. **Correct the ⊙ operator description** to "element-wise (Hadamard) multiplication."

## Score and Decision

**Overall assessment:** The paper tackles an important and well-motivated problem, proposes a clean approach, and provides strong experimental evidence across multiple degradation types. The core technical contribution — using edge-guided features to modulate Gaussian positions — is conceptually sound and empirically validated. The main weakness is the underspecification of the ESFG module's inner workings, which makes the method difficult to reproduce from the paper alone. However, this is a presentation gap rather than a fundamental flaw; the approach demonstrably works, and code release is promised. The paper would benefit from a more precise description, but the contribution is solid.

**Originality:** Good — the idea of using edge-semantic fusion to guide Gaussian primitive distribution under degradation is novel.  
**Importance:** High — robust NVS under realistic degradations is practically relevant.  
**Claims support:** Mostly well-supported, with the notable exception of ESFG's underspecification.  
**Soundness:** Good empirical methodology; ablation studies are structured and informative.  
**Clarity:** Fair — the core ideas are clear but the ESFG implementation description needs substantial improvement.  
**Value to community:** Moderate-high — the method is practical and the problem is broad.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>