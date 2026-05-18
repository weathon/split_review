Now I have sufficient calibration data. Let me write the consolidated review.

---

## Summary

This paper introduces ARSS, the first decoder-only autoregressive transformer for novel view synthesis from a single image conditioned on a camera trajectory. The method combines a video tokenizer (for temporally consistent discrete tokens), a camera autoencoder (to encode Plücker raymaps into 3D positional guidance tokens), and an autoregressive transformer with random spatial permutation (preserving temporal order). Experiments on RealEstate10K, ACID, and zero-shot DL3DV show competitive results against diffusion-based and transformer-based baselines, with the best or second-best PSNR and LPIPS across datasets.

## Strengths

- **First decoder-only AR model for NVS with competitive quantitative results.** Table 1 shows ARSS achieves the highest PSNR (19.02 on Re10K, 21.93 on ACID, 16.70 on DL3DV) and lowest LPIPS (0.269, 0.265, 0.347) among all compared methods, demonstrating that a causal autoregressive approach can compete with state-of-the-art diffusion models on this task.

- **Video tokenizer ablation convincingly validates temporal consistency design.** Table 3 shows replacing the video tokenizer with a VQ image tokenizer degrades FVD from 52.56 to 137.68 (~62% drop) while also substantially hurting PSNR (19.22→15.69) and SSIM (0.565→0.437), directly supporting the claim that temporal encoding is critical for multi-view consistency.

- **Hybrid spatial permutation strategy is well motivated and validated.** Table 2 and Figure 7 show the proposed strategy (spatial permutation with temporal order preserved) outperforms both full permutation (PSNR 19.22 vs. 18.76) and raster order (19.22 vs. 16.29), providing concrete evidence for the design choice in Section 3.2.3.

- **Error accumulation analysis shows slower degradation over long trajectories.** Figure 6 plots per-frame metrics across 16 frames and shows ARSS maintains the flattest degradation curves compared to five baselines across PSNR, SSIM, and LPIPS, supporting the claim that the causal autoregressive structure handles long camera sweeps well.

## Weaknesses

### Major

- **The core claimed advantage of autoregressive models — causal, incremental generation — is not experimentally validated.** The paper motivates AR by arguing that diffusion methods "generate target views jointly" and are "hard to adapt to new input or generate based on accumulated knowledge" (Introduction). Yet all experiments evaluate on fixed-length sequences of 17 frames with predetermined trajectories. There is no experiment showing that ARSS can *incrementally extend* generation (e.g., generate 5 more frames after seeing the first 12 without retraining), adapt to a changing trajectory at inference time, or handle arbitrarily long sequences. Without this, the central thesis of why AR is *naturally suited* for view synthesis over diffusion remains unsubstantiated, and the contribution reduces to "an autoregressive model that works about as well as diffusion models on fixed-length benchmarks."

- **Baseline comparison transparency is insufficient, making fairness hard to assess.** The paper compares against MotionCtrl, Genwarp, LVSM, SEVA, ViewCrafter, and RayZer but does not specify how each is configured for the task. For instance: (a) MotionCtrl is originally designed for camera+object motion control given an *input video*, not a single image — how was it adapted? (b) Genwarp relies on estimated depth and warping — does it receive ground-truth camera poses or operate monocularly? (c) SEVA trains at higher resolution and on different data scales, noted but not factored into the comparison. Without these details, it is impossible to determine whether comparisons are apples-to-apples, and the claimed quantitative superiority may be overstated.

### Minor

- **No ablation on the camera encoder itself.** The camera autoencoder is presented as a key contribution that converts Plücker raymaps into "3D positional instruction tokens." However, there is no ablation comparing it against simpler alternatives: using raw camera extrinsics/intrinsics as embeddings, sinusoidal positional encodings conditioned on camera parameters, or removing camera tokens entirely. This makes it unclear how much the camera encoder actually contributes versus the token ordering or other design choices.

- **Camera autoencoder loss hyperparameters are underspecified.** Equation (5) defines four loss terms with weights λ₁–λ₄, but the paper does not report their values, how they were chosen, or sensitivity analysis. This hurts reproducibility.

### Trivial

- **Inconsistency between abstract and intro/conclusion.** The abstract states the method "achieves overall comparable to state-of-the-art," while the introduction and conclusion claim it "out-performs current state-of-the-art methods." These are different strength claims and should be reconciled.

## Nice-to-Haves

- An experiment demonstrating incremental generation (e.g., generating frame 9–16 after seeing frames 1–8, compared to a diffusion baseline that re-denoises) would directly validate the paper's core motivation.
- A controlled baseline re-evaluation specifying exactly what input each baseline receives and how hyperparameters are configured would strengthen the quantitative comparisons.
- An ablation that removes or simplifies the camera encoder (e.g., replacing camera tokens with a single global camera embedding per frame or sinusoidal encodings) would justify this design choice.
- Reporting the λ values for Eq. (5) and briefly discussing sensitivity.

## Removed Points

- *Criticism about the "L2SM" label in Figure 6* (should be "LVSM"): This is a parser-induced formatting artifact, not an author error. Treat with caution if encountered.
- *Criticism about missing training/validation split details*: RealEstate10K and ACID have standard splits used in prior work; this is adequately grounded.
- *Criticism about missing related works*: The reviewer does not have external sources to verify existence of claimed missing references.
- *Strength Finder's generic strengths* (e.g., "this paper addressed an important problem"): Removed per filtering rules; only concrete, evidence-grounded strengths are retained above.

## Novel Insights

The reviews surface one genuinely novel observation not made explicit in the paper: the error accumulation analysis (Figure 6) provides the strongest *indirect* evidence for the AR advantage, but it evaluates on pre-defined 17-frame sequences rather than interactive extension. This gap — between indirect evidence and the paper's stated motivation — is where the most impactful future work lies. The paper could be significantly strengthened by directly demonstrating the ability to incrementally extend generation, which would turn a circumstantial claim into a demonstrated capability.

No other insight beyond the paper's own contributions emerged from these reviews.

## Suggestions

1. **Add an incremental generation experiment.** Take a trained ARSS model, generate frames 1–8, then condition on those 8 frames plus the next camera poses to generate frames 9–16. Compare this against a diffusion baseline that would need to re-denoise all frames or use a sliding window. This directly validates the paper's central thesis and would substantially strengthen the contribution.

2. **Specify baseline configurations.** For every baseline in Table 1, add a footnote or appendix section describing: (a) the exact input each method receives, (b) whether it was adapted from its original setting and how, (c) whether hyperparameters were tuned on a validation set.

3. **Add a camera encoder ablation.** Compare the proposed camera encoder against (i) no camera tokens, (ii) a single global camera embedding per frame, (iii) sinusoidal positional encodings of the camera pose.

4. **Report λ₁–λ₄ values** and briefly describe how they were selected. Even "chosen via grid search over [0.01, 0.1, 1, 10]" improves reproducibility.

5. **Resolve the abstract/intro inconsistency** regarding "comparable" vs. "outperforms."

## Score and Decision

**Calibration procedure:** Three rounds of calibration_search over the ICLR 2026 human review corpus.

*Round 1 (bracketing):* Three queries covering the weak (score 0–3), mid (4–7), and strong (8–10) bands, anchored on NVS and autoregressive topics. Returned anchors ranged from 2.00 (rejected) to 8.50 (accepted oral/poster). The most topically similar anchor in the weak band (CAMEO, 3.00) had fundamental novelty and evaluation limitations not present here. Mid-band anchors included ArchonView (5.00, Reject), CameraNoise (5.50, Reject), Prioritizing Faithfulness (5.50, Reject), 3DScenePrompt (5.00, Accept Poster), and Aligned NVS (5.00, Accept Poster). Strong-band anchors (8.00+) addressed different problem settings (text-to-3D, permutation-equivariant geometry) and were not directly comparable. **Initial bracket: 4.5–6.0.**

*Round 2 (narrowing):* Two queries targeting scores 4.5–6.0 and 6.0–7.5, returning ArchonView (5.00), AR4D (4.50), 3DScenePrompt (5.00), XFactor (6.00), RoRE (6.00), and others. I read ArchonView (5.00), XFactor (6.00), and 3DScenePrompt (5.00) in full. ArchonView is the most directly comparable paper — both introduce AR to NVS — and scored 5.00 (Reject). ARSS is slightly stronger than ArchonView on evaluation coverage (3 datasets including zero-shot, scene-level rather than object-centric) but weaker on ablation thoroughness and analysis depth. Against XFactor (6.00, Accept Oral), ARSS falls short in evaluation rigor and insight clarity. **Final score: 5.0.**

*Anchors consulted (all rounds):*

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| /home/.../nLRJkpyXGe.md (CAMEO) | 3.00 | R1 | Weaker — limited novelty, insufficient evaluation |
| /home/.../3dNKozB8U7.md | 3.00 | R1 | Weaker — different problem (4D Gaussians) |
| /home/.../imblpbUryY.md | 2.67 | R1 | Weaker — sparse NVS with geometry rectification |
| /home/.../w09tBdYcls.md | 2.00 | R1 | Weaker — visual odometry |
| /home/.../vjvwYexMQn.md (Aligned NVS) | 5.00 | R1 | Similar — accepted poster, comparable quality with different gaps |
| /home/.../2wSORykWAc.md (Prioritizing Faithfulness) | 5.50 | R1 | Similar — rejected, comparable rigor |
| /home/.../TT3gmYaqyc.md (CameraNoise) | 5.50 | R1 | Similar — rejected, missing comparisons |
| /home/.../qqij8fCGDl.md (CamPilot) | 4.50 | R1 | Slightly weaker — camera control reward feedback |
| /home/.../kI27Niy4xY.md (VIST3A) | 8.00 | R1 | Stronger — text-to-3D, oral acceptance |
| /home/.../DTQIjngDta.md (π³) | 8.00 | R1 | Stronger — permutation-equivariant geometry |
| /home/.../DM0Y0oL33T.md | 8.00 | R1 | Stronger — different domain |
| /home/.../VaS6xcDrTb.md | 8.50 | R1 | Stronger — rotation estimation |
| /home/.../PZQHihJlfm.md (ArchonView) | 5.00 | R2 | Most similar — AR for NVS, rejected; ARSS slightly stronger on evaluation but weaker on ablations |
| /home/.../8A4AQyJO9m.md (AR4D) | 4.50 | R2 | Weaker — 4D generation |
| /home/.../aJJppqAm6r.md (XFactor) | 6.00 | R2 | Stronger — oral acceptance, clearer insight, more thorough evaluation |
| /home/.../3XxoBwMusJ.md (3DScenePrompt) | 5.00 | R2 | Similar — accepted poster, comparable quality with fairness concerns |
| /home/.../BR2ItBcqOo.md (RoRE) | 6.00 | R2 | Stronger — ray embedding |
| /home/.../QXc2NBJFHr.md | 6.00 | R2 | Stronger — self-supervised NVS |
| /home/.../UNeL5NdLzc.md | 6.00 | R2 | Stronger — spherical neural field |

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>