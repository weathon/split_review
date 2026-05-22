Now I have all the information I need. Let me synthesize the final consolidated review.

---

## Summary

ARSS proposes a decoder-only autoregressive (GPT-style) framework for novel view synthesis from a single image, conditioned on a camera trajectory. The method has three main components: a video tokenizer (VidTok with FSQ) for temporally consistent discrete visual tokens, a camera autoencoder that compresses Plücker ray maps into camera tokens for 3D positional guidance, and a hybrid token-order permutation that shuffles tokens spatially within each frame while preserving temporal causality. The method is evaluated on RealEstate10K, ACID, and zero-shot on DL3DV, achieving competitive results — best PSNR/LPIPS on Re10K and best across all metrics on DL3DV zero-shot.

## Strengths

1. **First decoder-only AR model for NVS with camera control.** The paper correctly identifies that existing diffusion-based NVS methods generate all views jointly, making it hard to impose causal structure along a trajectory. ARSS demonstrates that a GPT-style next-token-prediction pipeline can be adapted for view synthesis, using camera tokens as 3D positional instruction tokens. This is a genuinely novel direction that opens a new axis for NVS research.

2. **Hybrid token-order permutation is well-motivated and ablated.** The ablation study (Table 2) shows that permuting tokens only within their spatial grid while preserving temporal order yields PSNR 19.22, substantially better than raster order (16.29) and full permutation (18.76). The visual results in Figure 7 confirm the design choice avoids both the geometric artifacts of full permutation and the blurring of raster order. This directly supports the paper's core claim about adapting causal AR to bidirectional visual data.

3. **Competitive zero-shot generalization on DL3DV.** On the DL3DV benchmark (zero-shot), ARSS surpasses all baselines on every metric — PSNR 16.70 vs. next-best LVSM 15.86, SSIM 0.449 vs. 0.409, LPIPS 0.347 vs. 0.400 (Table 1). The qualitative results on AI-generated images (Figure 5) further demonstrate out-of-distribution robustness. These results are the strongest evidence that the camera-token-guided AR structure transfers to unseen scenes.

4. **Video tokenizer ablation proves temporal-consistency advantage.** Substituting the video tokenizer (VidTok) with a per-frame VQ image tokenizer drops FVD from 52.56 to 137.68 (Table 3), a 62% relative degradation. This cleanly demonstrates that temporal encoding in the tokenizer is critical for multi-view consistency.

## Weaknesses

### Major

1. **Unfair error accumulation comparison (undermines a core claim).** The paper argues in §4.2 (Error Accumulation Analysis) and Figure 6 that ARSS "accumulates significantly less error over time" than baselines (MotionCtrl, ViewCrafter, RayZer, LVSM, SEVA). However, none of these baselines are designed to generate frames *sequentially* conditioned on their own previous outputs — they produce all target views jointly (SEVA, LVSM) or per-frame independently with warping (Genwarp). The observed slower degradation may partly reflect asymmetric evaluation conditions (ARSS gets access to its own previously generated content; the baselines do not) rather than fundamentally superior long-horizon behavior. No baseline is adapted to an autoregressive mode. This comparison needs to be either (a) made fair by adapting at least one baseline to use its own outputs, or (b) explicitly caveated as an apples-to-oranges comparison that only illustrates ARSS's own degradation trajectory. Without this, the central motivational argument for AR modeling is not fully supported.

2. **Missing ablation on the camera conditioning mechanism.** The camera autoencoder is presented as a core contribution (§3.2.2), yet the paper never tests whether the complex geometry-aware design is actually necessary. Critical missing baselines include: (a) removing camera tokens entirely and using only camera poses as a global condition (e.g., via cross-attention or adaptive layer norm), (b) replacing the autoencoder with a simple MLP that projects Plücker coordinates to the same latent dimension, (c) using raw camera parameters concatenated with visual tokens. Without these ablations, it is unclear whether the dedicated autoencoder's geometry-aware loss and 3D-convolutional architecture contribute meaningfully to the results, or whether most of the performance comes from the AR backbone and video tokenizer.

3. **Camera token representation is underspecified.** The paper describes the camera autoencoder as producing "latent features" (§3.2.2) that are inserted into the transformer sequence alongside discrete (FSQ-quantized) visual tokens. It is never stated whether these camera features are themselves quantized or continuous. If they are continuous, the mechanism by which they interface with a transformer expecting categorical token indices (e.g., a projection layer, a separate embedding strategy) is not described. If they are quantized, the codebook size, training procedure, and quantization loss are omitted. This ambiguity makes the method difficult to reproduce and assess. (Note: continuous conditioning tokens are feasible in practice, but the paper must specify the integration mechanism.)

### Minor

4. **Overclaiming of results.** The abstract says "comparable to state-of-the-art" while the introduction claims the method "out-performs current state-of-the-art methods." Table 1 shows a mixed picture: ARSS leads on PSNR and LPIPS on Re10K (19.02, 0.269) but trails SEVA on SSIM (0.624 vs. 0.670) and FID on ACID (47.76 vs. 33.16). The authors should calibrate these claims.

5. **Unsupported parallel decoding claim.** The paper states (line 257) that random permutation "allows parallel decoding" and "the system has the capacity to predict multiple tokens at one time," but all reported results use sequential next-token prediction. Parallel decoding is never demonstrated. This claim should either be removed or supported with experiments.

6. **No inference sampling details.** No mention of temperature, top-k sampling, or any decoding strategy for the AR head. These are standard in AR visual generation and can significantly affect quality.

7. **Tokenizer ablation confounds multiple variables.** Table 3 substitutes a VQ image tokenizer for the VidTok video tokenizer, but this simultaneously changes VQ vs. FSQ *and* image vs. video temporal encoding. A cleaner control would keep FSQ but use per-frame encoding (no temporal convolution), isolating the effect of temporal modeling.

### Trivial

8. **Equation (5) notation.** The variable name is overloaded — the loss uses `d` for both the ground-truth ray direction and the predicted direction without clear notational separation (hats on predictions are missing in the regularization terms).

9. **No computational cost comparison.** FLOPs, parameters, or inference time are not reported, which is relevant since the paper claims ARSS is "lighter" than SEVA.

## Nice-to-Haves

- **Error bars / confidence intervals** on the main quantitative results would strengthen the evaluation, given the inherent variance in generative models.
- **Failure case analysis** — the Discussion section notes tokenizer quality as a bottleneck but provides no concrete failure examples or diagnostics (e.g., FVD breakdown by camera motion magnitude).
- **Details on camera autoencoder pre-training** — the paper says it is "pre-trained" but does not specify training data, iterations, or whether its weights are frozen during AR training.

## Removed Points

- *Camera token representation is fatal / structurally invalid* — the harsh critic claimed continuous features "cannot be treated as tokens in a causal transformer." This is factually incorrect: continuous conditioning features (projected to the embedding dimension) are standard in AR models (e.g., class embeddings, CLIP text embeddings). The criticism is valid as an underspecification issue (needs clarification), not a structural flaw. **Demoted to Minor**.
- *Full-perm is a straw-man baseline* — the harsh critic claimed this was a straw-man, but the paper includes the natural "raster" baseline (standard AR without spatial permutation), which performs poorly. The ablation is reasonable. **Removed**.
- *Missing related works* — cannot be verified by this reviewer. **Removed**.
- *Missing appendix content* — parser-stripped content. **Removed**.
- *Formatting/style nitpicks* — parser artifacts. **Removed**.
- *Strength Finder's generic strengths* — generic statements about "addressing an important problem" are removed. Only concrete, evidence-backed strengths retained.

## Novel Insights

The key insight that emerges from combining the two reviews is that the paper's central thesis — causal AR is a natural fit for sequential view synthesis — is intuitively appealing and partially supported, but the evidence offered is weaker than it first appears. The error-accumulation comparison against non-AR baselines is the headline result (Figure 6), yet it is the very comparison that is most skewed by asymmetric evaluation. Conversely, the paper's strongest and cleanest evidence comes not from the long-trajectory claim but from two simpler ablations: (1) the token-order permutation ablation (Table 2) cleanly shows that spatial-within-temporal shuffling beats both raster and full permutation, and (2) the video tokenizer ablation (Table 3) demonstrates that temporal encoding in the tokenizer is far more impactful than any camera-conditioning design choice tested. This suggests the paper's most robust contributions are the hybrid permutation and the application of a video tokenizer to NVS, while the camera autoencoder and the "AR is better for long sequences" framing need stronger validation.

## Suggestions

1. **Clarify the camera token integration.** Explicitly state whether camera features are quantized or continuous, and describe the mechanism (projection layer, etc.) that allows them to interface with the discrete-token transformer.
2. **Fix the error accumulation comparison.** Either adapt a baseline (e.g., ViewCrafter) to condition on its own previous outputs, or reframe the analysis as a comparison of each method's *own* degradation rate without claiming cross-method superiority.
3. **Add camera-conditioning ablations.** Test the simplest possible camera conditioning (e.g., cross-attention on pose vectors) against the proposed autoencoder to isolate its contribution.
4. **Calibrate claims.** Use language matching the results (e.g., "competitive with" rather than "outperforms") and clearly discuss where the method trails baselines (e.g., SSIM, FID on ACID).
5. **Demonstrate parallel decoding or remove the claim.**
6. **Report inference sampling parameters** (temperature, top-k).

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Comparison to ARSS |
|--------|-----------|-------------------|
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/QQBPWtvtcn.md` (LVSM) | 7.67 | Significantly stronger — cleaner methodology, more thorough evaluation, clearer contributions. ARSS is less polished. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/NuHYh4YKNe.md` (Where Am I) | 6.25 | Comparable — both use AR with camera tokens for view prediction, both have clarity issues. ARSS has better zero-shot results but more underspecification. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/zDJf7fvdid.md` (Zero-shot NVS via Diffusion) | 6.00 | ARSS is slightly weaker — comparable results but more methodological gaps. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/dTGH9vUVdf.md` (FreeVS) | 5.80 | Comparable — both have genuine contributions but significant clarity gaps and missing ablations. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/pOcGFvfgjS.md` (AR-1-to-3) | 5.00 | ARSS is somewhat stronger — more comprehensive evaluation (multiple datasets, zero-shot), better results, though both have similar underspecification issues. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/15lk4nBXYb.md` (CCM-DiT) | 3.00 | Much weaker paper — unclear methodology, minimal evaluation. ARSS is substantially stronger. |
| `/home/wg25r/split_review/datasets/deepreview_13k_calibration/P4o9akekdf.md` (No Pose, No Problem) | 8.00 | Significantly stronger — clean contribution, rigorous experiments. ARSS does not approach this quality. |

### Overall Assessment

The paper opens a genuinely interesting direction (decoder-only AR for NVS) and demonstrates competitive results, particularly in zero-shot settings. However, the methodological transparency is lacking in several key areas (camera token integration, fairness of the error-accumulation comparison, missing camera-conditioning ablation), and these gaps prevent the paper from fully supporting its core claims in its current form. The contribution is potentially significant but needs more rigor.

**Score:** 5.5  
**Decision:** Reject

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>