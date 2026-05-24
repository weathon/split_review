Now I have a clear picture of the calibration landscape. Let me finalize.

## Round 2 — Narrowing comparison

| Anchor | Score | Comparison to ARSS |
|--------|-------|-------------------|
| AR-1-to-3 | 5.00 | ARSS is clearly stronger — broader evaluation (3 datasets vs 1), more competitive, better ablations |
| GST | 6.25 | ARSS is comparable or slightly better — genuinely novel (first AR NVS), broader evaluation, but similar overclaiming issues |
| Cameras as Rays | 6.50 | Comparable — strong novelty in respective areas, but ARSS has broader empirical validation |
| 4DiM | 6.50 | Comparable — ARSS more focused but competitive; 4DiM more ambitious with some quality tradeoffs |
| LVSM | 7.67 | LVSM is clearly stronger — more thorough evaluation, cleaner wins over baselines (1.5-3.5 dB), better execution |

**Final score: 6.0.** The paper's genuine novelty as the first AR NVS framework with camera control is its strongest asset, but it's held back by overclaimed results (SEVA wins on SSIM/FID), a missing key ablation (camera autoencoder), and the AR-specific advantage not being fully demonstrated beyond fixed-length sequences. These place it below LVSM and roughly at the level of other accepted papers with real contributions but notable gaps.

Wait — I want to reconsider. The bracket was 5.5-7.5. The paper has real novelty and competitive results. The overclaiming is a real issue but fixable. The missing ablation is a gap but doesn't invalidate the approach.

Let me go with 6.0. The paper is between GST (6.25, which was accepted despite overclaiming issues but had weaker evaluation) and Cameras as Rays (6.50, strong novelty but limited evaluation). ARSS has broader evaluation than both but has the overclaiming issue and missing ablation — slightly below Cameras as Rays in novelty but with better evaluation breadth. Score: 6.0.

Actually, I think I need to settle on a final number. Let me go with **6.0**. This reflects: genuine contribution (first AR NVS), competitive results, but overstated claims and missing key ablation. This is in the accept range but with reservations.

Now let me produce the final consolidated review.Now let me write the final consolidated review.

---

## Summary
ARSS proposes the first decoder-only autoregressive transformer framework for novel view synthesis from a single image conditioned on a camera trajectory. The method integrates three components: (1) a causal video tokenizer for temporally coherent multi-view tokenization, (2) a camera autoencoder that compresses Plücker raymaps into 3D positional guidance tokens, and (3) a hybrid token permutation strategy that shuffles spatial order while preserving temporal causality. Evaluated on RealEstate10K, ACID, and zero-shot on DL3DV, ARSS achieves competitive results with state-of-the-art diffusion-based methods, with notably stronger performance on long-horizon error accumulation.

## Strengths
- **First AR framework for NVS with camera control**: The paper is genuinely the first to apply GPT-style causal autoregressive modeling to novel view synthesis with explicit camera trajectory conditioning. This is a non-trivial translation from single-image AR generation to multi-view 3D-aware generation, requiring solutions to temporal consistency, 3D guidance, and bi-directional spatial context that the paper addresses with well-motivated components.
- **Hybrid token permutation is well-validated**: The spatial-shuffle / temporal-preserve strategy (Section 3.2.3, Eq. 6) is a clean design choice. Table 2 and Figure 7 provide convincing evidence — "raster" order degrades at later frames, "full perm." loses temporal causality and produces incorrect geometry, while the proposed hybrid ordering yields the best metrics across PSNR, SSIM, LPIPS, and FID.
- **Video tokenizer is essential and well-ablated**: Table 3 shows that replacing the causal video tokenizer with per-frame VQ tokenization drops PSNR by 3.53 and nearly triples FVD (52.56 → 137.68). This directly supports the claim that temporal consistency in tokenization is critical for multi-view generation quality.
- **Slower error accumulation along trajectories**: Figure 6 demonstrates that ARSS maintains flatter degradation curves across all three metrics (PSNR, SSIM, LPIPS) compared to baselines, directly supporting the AR advantage for sequential view generation. This is a measured, quantitative demonstration of the structural benefit of the autoregressive approach.
- **Zero-shot generalization**: The model trained only on RealEstate10K/ACID transfers to DL3DV (Table 1, Figure 4) and to stylized AI-generated images (Figure 5) without fine-tuning, indicating the learned representations generalize beyond the training distribution.

## Weaknesses

### Fatal
None.

### Major
- **Overstated claims vs. mixed quantitative results**: The introduction and conclusion state the method "out-performs current state-of-the-art methods," but Table 1 shows a mixed picture. SEVA achieves better SSIM (0.670 vs. 0.624 on RealEstate10K; 0.664 vs. 0.623 on ACID) and better FID on ACID by a substantial margin (33.16 vs. 47.76). ARSS wins on PSNR, LPIPS, and FVD, but the paper's language does not acknowledge these trade-offs. The abstract is more accurate ("overall comparable to state-of-the-art") and the rest of the paper should be calibrated to match. This matters because the central empirical claim of the paper is overstated relative to the evidence.

- **Missing ablation of the camera autoencoder**: The camera autoencoder is presented as one of the three core contributions (Section 3.2.2, Eq. 5), yet no experiment removes or replaces it. There is no comparison against: (a) omitting camera tokens entirely, (b) using raw Plücker raymaps without compression, or (c) substituting with a simpler learned embedding of camera parameters. The reader cannot assess whether the autoencoder — with its dedicated architecture and geometry-constrained loss — actually improves generation quality over simpler alternatives. This is a significant gap given the component's prominence in the method.

### Minor
- **Causal-generation advantage not demonstrated beyond fixed-length sequences**: The paper's motivation emphasizes incremental extension of trajectories and reusing previously generated views as "accumulated knowledge" (Introduction, §1). However, all experiments evaluate fixed 17-frame sequences in one shot. Figure 6 demonstrates slower error accumulation along a fixed trajectory, but this is not the same as showing the model can generate a few frames, then condition on those to generate more — the very capability that distinguishes AR from joint generation. The model is trained causally and could in principle do this, but demonstrating it would substantially strengthen the paper's thesis.

- **SEVA omitted from error accumulation analysis**: Figure 6 — which is presented as a key advantage of the AR approach — does not include SEVA, the most competitive baseline from Table 1. The comparison is against weaker baselines (LVSM, MotionCtrl, RayZer, ViewCrafter), making the advantage appear larger than it may be against the strongest competitor.

### Trivial
- The paper states "our method out-performs current state-of-the-art methods" (line 114) while the abstract more accurately says "overall comparable to state-of-the-art" (line 14). Aligning these statements would improve consistency.
- Eq. 7 is presentationally incomplete — the target side of the cross-entropy is missing from the notation, making the training objective harder to parse than necessary.

## Nice-to-Haves
- A controlled experiment evaluating true causal extension (generate 5 frames → condition on generations → generate 5 more) would directly validate the motivational narrative around incremental trajectory construction.
- Training a latent diffusion model on the same video token space and comparing to ARSS would isolate the effect of the AR paradigm from the tokenizer, though this is a substantial undertaking.
- Measuring camera-control accuracy beyond visual quality — e.g., pose estimation from generated views — would strengthen the claim about precise 3D guidance.
- Reporting FID/FVD computation details (number of samples, feature network) for reproducibility.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"Missing baselines (ZeroNVS, MVSplat, ReconFusion)"** — REMOVED per hard rule: cannot verify existence or appropriateness of these as baselines from the paper alone. The paper already includes 6 baselines covering diffusion, feed-forward, and warping-based approaches.

- **"No comparison to a diffusion model on the same discrete token space"** — MOVED to Nice-to-Haves. Training an entire competing diffusion model for a controlled comparison is a substantial undertaking beyond standard expectations for an empirical paper introducing a new framework.

- **"The paper does not clarify whether camera tokens are predicted during AR training"** — REMOVED. The architecture description clearly states camera tokens are provided as input/conditioning (Section 3.2.3, Eq. 6–8 interleave camera tokens with visual tokens and feed them into the transformer as input). The model predicts visual tokens; camera tokens are 3D positional guidance, not prediction targets.

- **"Parallel decoding claim mentioned but never quantified"** — REMOVED. This is a forward-looking remark (end of §3.2.3) not presented as a core contribution or evaluated claim. It is an architectural possibility noted in passing.

- Strength Finder's claim that ARSS "significantly outperforms all diffusion and feed-forward baselines" — WEAKENED and removed as a standalone strength. The results are competitive but not uniformly superior; SEVA wins on SSIM and FID.

- **Harsh critic's claim that FID/FVD computation details are "missing"** — DEMOTED to Nice-to-Haves. These are standard evaluation details; their absence is minor.

## Novel Insights
The paper's most genuinely novel insight is that camera tokens derived from a geometry-constrained autoencoder over Plücker raymaps can serve as per-token 3D positional guidance in an autoregressive transformer, enabling the spatial-permutation training strategy that prior AR visual generation methods (e.g., Pang et al. 2025, Yu et al. 2024a) relied on for image generation to extend naturally to multi-view sequences. The coupling of the camera autoencoder's geometric constraints (unit-norm rays, orthogonality regularization) with the hybrid token permutation strategy is a clean design pattern that could transfer to other AR 3D generation tasks.

## Suggestions
- Tone down claims from "outperforms" to "competitive with" or "comparable to" state-of-the-art, particularly given the SSIM and FID results vs. SEVA.
- Add an ablation that removes or replaces the camera autoencoder (e.g., using raw Plücker embeddings without compression, or a learned embedding of camera parameters) to isolate its contribution.
- Include SEVA in the error accumulation analysis (Figure 6) to make the comparison against the strongest baseline complete.
- If feasible, demonstrate a true causal-extension experiment (generate first N frames, then condition on generated output for subsequent frames) to directly validate the AR advantage the introduction emphasizes.

## Score and Decision

**Calibration anchors reviewed:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| AR-1-to-3 | 5.00 | R1 | ARSS is stronger: broader eval, more competitive results, better ablations |
| GST | 6.25 | R1 | Comparable; ARSS has broader evaluation, GST has joint pose+view novelty |
| Cameras as Rays | 6.50 | R2 | Comparable; both have genuine novelty with some evaluation limitations |
| 4DiM | 6.50 | R2 | Comparable; ARSS is more focused, 4DiM more ambitious with tradeoffs |
| LVSM | 7.67 | R1 | LVSM is clearly stronger: cleaner wins, more thorough evaluation |

**Round-1 bracket:** 5.5 – 7.5. **Round-2 narrowing:** The paper sits between GST (6.25) and Cameras as Rays (6.50). ARSS has a genuinely novel framework with competitive results and broader evaluation than GST, but its quantitative claims are overstated and a key architectural contribution (camera autoencoder) is not directly validated through ablation. These gaps prevent it from reaching the LVSM tier (7.67) where execution quality and thoroughness are notably higher.

**Final score: 6.0 — Accept.** The paper makes a real contribution as the first AR framework for NVS with camera control, with a well-integrated architecture and competitive results. The missing camera autoencoder ablation and overstated claims are addressable in revision and do not invalidate the core contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>