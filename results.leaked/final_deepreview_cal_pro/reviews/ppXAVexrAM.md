Now I have enough anchors to calibrate. Let me compile my final review.

**Bracket summary:**
- Round 1 bracket: **5.0–6.5**
- Round 2 narrowed: compared against AR-1-to-3 (5.00), 3D-free+3D (5.00), CamTrol (5.80), GST (6.25), GenXD (6.25), 4DiM (6.50). ARSS is clearly stronger than the 5.00 anchors and comparable to or slightly below the 5.80–6.25 anchors, placing it at **5.5**.

---

## Summary
ARSS proposes the first decoder-only autoregressive transformer framework for novel view synthesis from a single image conditioned on a camera trajectory. The method uses a video tokenizer to compress multi-view sequences, a camera autoencoder to encode Plücker raymaps into 3D positional tokens, and a causal transformer with a hybrid spatial-shuffle/temporal-order token permutation strategy. Experiments on RealEstate10K, ACID, and DL3DV show competitive results against diffusion-based baselines, with particularly strong perceptual metrics and slower error accumulation over long trajectories.

## Strengths
- **First application of causal AR transformers to camera-controlled NVS**: This is a genuinely novel technical direction. Prior AR visual generation work focused on single-image generation; this paper extends the paradigm to multi-view synthesis with explicit 3D camera control, representing a non-trivial integration of video tokenization, camera encoding, and hybrid token ordering.

- **Well-ablated core design choices**: The ablation on token permutation strategies (Table 2, Figure 7) convincingly shows that the hybrid ordering (spatial shuffle + temporal order preserved) is necessary — raster order degrades badly at later frames, and full spatiotemporal permutation introduces geometric errors by allowing distant views to be generated first. The video tokenizer ablation (Table 3) demonstrates a 62% FVD improvement over per-frame VQ tokenization, validating the temporal modeling claim.

- **Competitive quantitative results, particularly on perceptual metrics**: On RealEstate10K, ARSS achieves best LPIPS (0.269 vs. SEVA's 0.349, a ~23% improvement) and best FVD (50.51 vs. 57.56), while PSNR is comparable to SEVA (19.02 vs. 18.73). On ACID, the same pattern holds (LPIPS 0.265 vs. 0.326). The method also shows convincing zero-shot generalization to DL3DV and to out-of-distribution AI-generated images (Figure 5).

- **Slower error accumulation over long trajectories**: Figure 6 shows ARSS maintains higher PSNR/SSIM and lower LPIPS than all baselines at every frame index, with visibly flatter degradation slopes. This provides partial evidence for the claimed benefit of the autoregressive causal structure.

## Weaknesses

### Fatal
None.

### Major
- **The core causal motivation is not experimentally demonstrated.** The paper's introduction argues that AR models are attractive because their causal structure enables incremental extension and reuse of generations when trajectories change — this is the stated *raison d'être* for choosing AR over diffusion. Yet every experiment evaluates fixed-length trajectory generation from scratch. There is no experiment showing ARSS can append views to an existing sequence without recomputation, reuse internal state for a modified trajectory, or otherwise exploit causality in a way a diffusion model cannot. The error accumulation analysis (Figure 6) shows slower per-frame quality degradation, which is a quality property of the sequential generation process, but it does not demonstrate the *architectural* advantages (incremental extension, state reuse) that motivate the paper. This gap between motivation and evidence weakens the significance of the contribution.

### Minor
- **Claims oscillate between "comparable" and "out-performs."** The abstract accurately states the method is "overall comparable to state-of-the-art," but the introduction and discussion assert ARSS "out-performs current state-of-the-art methods." The results do not unambiguously support "out-performs": ARSS wins on PSNR, LPIPS, and FVD against SEVA, but loses on SSIM (0.624 vs. 0.670 on Re10K) and FID (47.60 vs. 46.98). The evidence supports "competitive" or "comparable," not a decisive win. The paper should align its claims with its data.

- **Camera autoencoder contribution is not ablated.** The camera autoencoder (Section 3.2.2) is presented as a key architectural novelty, with a dedicated geometric loss (Eq. 5). However, there is no ablation comparing it to a simpler conditioning method (e.g., a linear projection or small MLP applied to Plücker coordinates). Without this comparison, it is unclear whether the autoencoder is load-bearing or an arbitrary design choice. This is a moderate evidential gap.

- **Several baseline numbers raise concerns about protocol validity.** ViewCrafter (PSNR 12.67, FID 121.25 on Re10K) and RayZer (PSNR 12.97, FID 324.23) produce results far below what would be expected from published work. While the paper's main claims do not depend on these baselines (the comparison with SEVA and LVSM is what matters), the paper does not adequately explain why these methods perform so poorly — whether due to domain mismatch, resolution inconsistency, or evaluation protocol issues. Clarification would strengthen the evaluation's credibility.

### Trivial
- Figure 6 legend contains "L2SM" which is a typo for "LVSM." This suggests the figure was not carefully proofread.

## Nice-to-Haves
- An experiment demonstrating the causal architectural advantage — e.g., a trajectory-extension task where new views are appended conditioned on previously generated outputs without recomputing the full sequence, compared against a diffusion baseline that must re-denoise the entire trajectory — would transform the paper's contribution from "AR can do NVS" to "AR is *better* for NVS in ways that matter."
- Inference cost (time, memory, token-generation steps) relative to diffusion methods is never reported. For a method motivated by practical deployment, this information would be valuable.
- A more detailed head-to-head analysis with SEVA (per-frame metrics, failure cases, compute budget) would make the comparison more informative than the current "roughly ties" summary.

## Removed Points
These points were raised by the harsh critic but are removed from the final review after verification:

- **"The baseline comparison is not demonstrably fair" (as a fatal concern):** While the ViewCrafter and RayZer numbers are suspiciously low, the paper's core claims rest on the comparison with SEVA and LVSM, where the comparison appears fair. The low baseline numbers are a minor concern (retained above as Minor), not a fatal flaw. The harsh critic's framing overstates the severity.

- **"The absence of more recent generic NVS methods (e.g., MVSplat, pixelSplat) is noticeable":** REMOVED. These are feed-forward methods that typically require multiple input views and operate under different assumptions. The paper's baselines (SEVA, LVSM, Genwarp, MotionCtrl, ViewCrafter, RayZer) cover the relevant single-image-to-multi-view generative methods. Scope creep.

- **Demand for the camera autoencoder comparison to be a "fatal" gap:** DEMOTED to Minor. While an ablation would strengthen the paper, the autoencoder is a reasonable design choice and the method's overall results remain valid without this specific ablation.

- **"MotionCtrl is a video generation method not designed for single-image NVS"**: REMOVED. The paper acknowledges this by including it as a comparison point; readers can assess its relevance. Including broader baselines is not a weakness.

## Novel Insights
The paper's hybrid token ordering strategy — randomly shuffling spatial tokens within each frame while strictly preserving temporal order across frames — is a simple but effective reconciliation of the tension between causal (uni-directional) transformers and bi-directional image data. The ablation (Figure 7) reveals a clear failure mode for each alternative: full spatiotemporal permutation causes distant views to be generated before nearby ones, losing the benefit of accumulated knowledge, while raster ordering forces a uni-directional model to learn bi-directional spatial context, causing degradation at later frames. This insight — that temporal causality and spatial flexibility can be cleanly separated — may generalize to other video-frame autoregressive tasks beyond NVS.

## Suggestions
- Add an experiment that directly tests the causal advantage: given a generated trajectory, extend it with new views *without recomputing the previous ones*, and compare against a diffusion baseline that must regenerate the entire sequence.
- Ablate the camera autoencoder against a simple MLP or linear projection applied to Plücker coordinates to establish whether the learned compression and geometric losses are necessary.
- Tone down claims from "out-performs" to "is competitive with" or "matches" to align with the quantitative evidence.
- Fix the "L2SM" typo in Figure 6.
- Report inference time/memory compared to diffusion methods to help readers assess practical trade-offs.

## Score and Decision

**Calibration anchors considered:**

| Anchor | Avg Score | Round | Comparison to ARSS |
|--------|-----------|-------|---------------------|
| AR-1-to-3 (pOcGFvfgjS) | 5.00 | R1/R2 | ARSS is stronger: more datasets, better ablations, stronger baselines |
| 3D-free+3D priors (VLuJL8cnGk) | 5.00 | R1/R2 | ARSS is stronger: more rigorous evaluation, clearer methodology |
| CamTrol (KI1zldOFz9) | 5.80 | R2 | ARSS is comparable; both have novelty but also notable gaps |
| GST (NuHYh4YKNe) | 6.25 | R1/R2 | ARSS is slightly weaker: GST has broader scope (pose+view), but ARSS has cleaner evaluation |
| GenXD (1ThYY28HXg) | 6.25 | R2 | ARSS is weaker: GenXD has broader scope and larger-scale data |
| 4DiM (d2UrCGtntF) | 6.50 | R2 | ARSS is clearly weaker: 4DiM handles dynamics, mixed data training, broader evaluation |
| LVSM (QQBPWtvtcn) | 7.67 | R1 | ARSS is clearly weaker: LVSM has stronger results, better scaling analysis, more thorough evaluation |

ARSS sits between the 5.00 and 6.25 anchors. It is clearly stronger than the 5.00 papers (AR-1-to-3, 3D-free+3D) but does not reach the 6.25+ tier (GST, GenXD, 4DiM, LVSM) due to the unsupported causal motivation and missing ablations. The paper makes a genuine contribution — first AR decoder-only transformer for NVS — but the gap between its stated motivation and experimental evidence holds it back. **Score: 5.5.**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>