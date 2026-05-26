Now let me do calibration search to bracket the score.Let me read the most topically similar anchors in detail.Round 1 bracket: ARSS sits between the weak-reject anchors (CCM-DiT 3.0, ARVideo 3.4) and middle-tier autoregressive NVS anchors (AR-1-to-3 5.0, Training-free Camera Control 5.8). Most similar anchor by setup is AR-1-to-3 (5.0): both propose first/novel AR-style NVS from single image, both have clear overclaiming and ablation gaps. Round-1 bracket: **[4.0, 6.0]**.Based on round 2 narrowing, ARSS sits comparable to AR-1-to-3 (5.0 reject) and 3D-free meets 3D priors (5.0 reject) — similar AR-style NVS with overclaiming and ablation gaps. It's below VD3D (6.2 accept), GenXD (6.25 accept), and CameraCtrl (6.5 accept), which have cleaner contributions and better-supported claims. It's clearly above ARVideo (3.4 reject) and CCM-DiT (3.0 reject). Round-2 bracket narrowed to **[4.5, 5.5]**.

Now I'll write the final review.

## Summary
ARSS proposes the first decoder-only GPT-style autoregressive framework for single-image novel view synthesis (NVS) with a pre-defined camera trajectory. The three concrete pieces are (1) a video tokenizer (VidTok) for temporally coherent discrete tokens, (2) a camera autoencoder that compresses Plücker raymaps into per-token camera "positional instruction" embeddings, and (3) a hybrid permutation strategy that randomly shuffles spatial token order within each frame while preserving temporal causality. The model is trained from scratch on RealEstate10K/ACID and zero-shot evaluated on DL3DV, achieving results competitive with SEVA on most metrics at lower training scale.

## Strengths
- **Genuinely novel architectural framing**: A decoder-only causal AR model applied to camera-controlled scene-level NVS from a single image is, as far as the paper claims, not previously done. Prior AR work (PAR, RAR, LlamaGen) is image-only; prior AR NVS work (AR-1-to-3) operates on objects with diffusion-based per-step generation. ARSS combines pieces in a coherent way.
- **Hybrid permutation ablation is well-supported**: Table 2 cleanly shows hybrid spatial-only permutation (19.22 PSNR / 0.565 SSIM / 0.294 LPIPS / 60.11 FID) outperforms both raster (16.29 PSNR) and full spatial+temporal permutation (18.76 PSNR) across all four metrics. Figure 7 provides qualitative support.
- **Tokenizer ablation supports the video-tokenizer choice**: Table 3 shows the video tokenizer substantially improves FVD (52.56 vs. 137.68 for VQ image tokenizer) and other metrics, supporting the temporal-consistency argument.
- **Error accumulation analysis (Figure 6)**: ARSS maintains the highest PSNR/SSIM and lowest LPIPS at every timestep with flatter degradation slopes than the baselines shown, providing genuine evidence that the AR/temporal-causal design has measurable downstream effects.
- **Zero-shot generalization on DL3DV**: ARSS beats the in-distribution numbers of MotionCtrl and LVSM on DL3DV across all five metrics (16.70 PSNR, 0.449 SSIM, 0.347 LPIPS, 84.96 FID, 91.25 FVD), supporting reasonable generalization (with caveats about which baselines were available).

## Weaknesses

### Fatal
None. The contribution is real and the experiments support a defensible (parity-at-lower-scale) claim, though not the claim the paper actually makes.

### Major
- **Internal inconsistency between claimed and actual headline result.** The abstract states results "achieve overall comparable to state-of-the-art" while the intro ("our method out-performs current state-of-the-art methods"), Section 4.2 ("consistently outperforms most of the baselines"), and Section 5 ("our method outperforms state-of-the-art methods") all claim outperformance. Looking at Table 1: against SEVA on RE10K, ARSS wins PSNR (19.02 vs 18.73) and LPIPS (0.269 vs 0.349) but loses SSIM (0.624 vs 0.670) and FID (47.60 vs 46.98). On ACID, ARSS wins PSNR/LPIPS but loses SSIM (0.623 vs 0.664) and FID (47.76 vs 33.16) — the ACID FID gap is large (44%). The abstract's framing is the accurate one; the body's repeated "outperforms" is overstated.
- **Camera autoencoder — a claimed core contribution — is essentially unablated.** Section 3.2.2 introduces a non-trivial design (3D-conv encoder/decoder + custom geometry loss in Eq. 5 with four terms including unit-norm and orthogonality regularizers) but there is no ablation against natural alternatives (e.g., raw Plücker raymaps fed as input channels, per-frame pose-MLP embeddings) and no ablation of the geometry-constraint terms λ₃ and λ₄. Tables 2 and 3 ablate only token order and tokenizer choice. With this gap, the claim that the camera autoencoder is a necessary design choice is empirically unsupported.
- **The motivating advantage of AR is never tested.** The introduction argues diffusion makes it "less straightforward to impose a strictly causal structure along a camera path or to incrementally extend and reuse existing generations when the trajectory changes." But all experiments generate fixed 17-frame sequences at training horizon. There is no experiment showing extended trajectory generation beyond 17 frames, KV-cache reuse across edited trajectories, or interactive appending of views. Figure 6's analysis stays within the 16-frame window. The paper's central pitch — that AR is the right choice because of incremental, causal use — rests on a property the paper never demonstrates.

### Minor
- **Resolution/compute mismatch with baselines is unaddressed.** Section 4.1 says everything is evaluated at 256×256, while Section 5 acknowledges SEVA benefits from "large-scale, high-resolution training data." The paper does not state at what resolution SEVA/ViewCrafter/MotionCtrl checkpoints were actually run, whether they were re-trained on the same split, or whether high-resolution baselines were downsampled — PSNR/SSIM behave very differently across resolutions, so this matters for fair quantitative comparison.
- **Equation 5 variable definitions are garbled.** The text says "**d** is the normalized camera ray direction, **d** is the momentum term formulated as **m** = **o** × **d**." One of the **d**'s should be **m**, and the origin **o** is not defined.
- **Equation 7 appears truncated / unclear.** Eq. 7 as written has the form CE(f_θ([S, [x_21^P_2(1), …, x_ln^P_l(n)]]) — missing parenthesis and unclear what is prediction vs. target. The treatment of camera tokens under the CE loss is also ambiguous (are they supervised? predicted? prefilled only?).
- **GenWarp missing from Table 1.** GenWarp appears throughout Figures 3–4 and the surrounding text discussing qualitative comparisons, but is absent from the quantitative table.
- **RayZer's anomalously low numbers warrant comment.** RayZer scores 12.97 / 12.64 PSNR — substantially below all other entries. Either RayZer is being applied outside its intended single-image-generation setting and this should be flagged, or the configuration is fair and the gap deserves explanation.
- **"Parallel decoding" is asserted but never demonstrated.** The last paragraph of Section 3.2.3 claims the system "has the capacity to predict multiple tokens at one time" but no experiment is reported. Either ground this claim or remove it.
- **The 22% relative FID and ~7% relative SSIM gaps vs. SEVA are characterized as "minor geometric inconsistencies."** A 22% relative FID hit is not minor for NVS evaluations.
- **Tokenizer ablation (Table 3) lacks confounder control.** VQ baseline reaches only 15.69 PSNR — large enough a gap (~3.5 PSNR) that one suspects training/codebook/compute confounds rather than a clean "video vs. image tokenizer" attribution. State which VQ tokenizer, training data, codebook size, and matched compute.

### Trivial
None retained — per parser-error rules.

## Nice-to-Haves
- A compute-matched comparison with SEVA (parameters, training tokens, GPU-hours, inference FLOPs). The "competitive at lower scale" framing is the strongest defensible story; quantifying it would make the contribution crisp.
- A per-component decomposition of the Figure 6 error-accumulation result: is the slower degradation from the video tokenizer, the camera tokens, or causal generation? Currently the paper reports the joint effect.
- At least one qualitative demonstration of extending beyond the 17-frame training horizon or reusing KV cache on an edited trajectory.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **(From harsh critic) "DL3DV zero-shot comparison excludes the strongest baselines."** The paper's caption explicitly notes that SEVA/ViewCrafter/RayZer trained on DL3DV, so excluding them from zero-shot eval is methodologically correct. Including them with a note would be informative but their absence is principled, not deceptive. Demoted.
- **(From harsh critic) "Novelty is largely combination of existing pieces (VidTok, LlamaGen, PAR/RAR-style shuffling)."** The paper acknowledges these explicitly. The combination targeted at camera-controlled NVS is itself the contribution, and the framework is genuinely new in that setting. Removed as overclaim by the reviewer.
- **(From strength finder) "Strong quantitative results across multiple benchmarks (best/second-best across all metrics)."** Verified to be over-stated — ARSS does not lead on SSIM on RE10K (0.624 vs 0.670 SEVA) or FID on ACID (47.76 vs 33.16 SEVA). Trimmed to a more accurate "competitive with SEVA, ahead on PSNR/LPIPS, behind on SSIM/FID" framing in the main strengths.
- **(From strength finder) "Best across all five metrics on DL3DV zero-shot."** Only true because the strongest diffusion baseline (SEVA) is excluded from DL3DV by training-overlap reasons. Kept in strengths but with caveat.

## Novel Insights
None beyond the paper's own contributions. The most distinctive empirical signal is the error-accumulation analysis (Figure 6) showing flatter per-frame degradation than baselines — but the paper does not isolate the cause, so this remains an observation rather than an insight.

## Suggestions
1. Reconcile claims to evidence: change "outperforms state-of-the-art" throughout the body to the abstract's "comparable to state-of-the-art," and lean into the "competitive at smaller scale" angle that Table 1 actually supports.
2. Add the camera-autoencoder ablation: compare against raw Plücker channels, per-frame pose-MLP embeddings, and the autoencoder without the orthogonality/unit-norm losses. Without this, one of three claimed contributions is empirically unsupported.
3. Add at least one experiment exercising the AR/causal extension property the introduction motivates — beyond-horizon generation, KV-cache reuse on trajectory edits, or interactive view appending. Even a qualitative demonstration would meaningfully strengthen the case.
4. State explicitly the resolution/checkpoint/training configuration used for each baseline in Table 1; report compute (params, GPU-hours, inference FLOPs) for ARSS vs. SEVA.
5. Fix the variable definitions in Eq. 5 and clarify Eq. 7 (what is predicted, what is target, are camera tokens supervised).
6. Add GenWarp to Table 1, or state explicitly why it is omitted; explain RayZer's anomalous numbers or fix the configuration.
7. Either run a parallel-decoding experiment or remove the parallel-decoding claim.

## Axis-by-Axis Assessment
- **Originality**: Reasonable. First decoder-only causal AR for camera-controlled scene-level NVS is a genuine contribution, though the technical pieces (video tokenizer, spatial permutation, Plücker-from-camera) are reuse with adaptation.
- **Importance of research question**: Real. AR vs. diffusion for NVS is a legitimate axis to explore and has practical implications for interactive/extendable world models.
- **Whether claims are well-supported**: Partly. The headline "outperforms" claim is not supported by Table 1 against SEVA. The "comparable" framing in the abstract is supported. The "causal/extendable" motivation is not tested.
- **Soundness of experiments**: Adequate but with notable gaps — camera autoencoder unablated, baseline-resolution configuration unspecified, GenWarp missing from quantitative table.
- **Clarity of writing**: Mixed. Architecture is clearly described, but Eq. 5 has garbled variable definitions and Eq. 7 is hard to parse.
- **Value to the research community**: Modest. A clean working AR-for-NVS recipe is valuable if released; the error-accumulation result is a useful empirical data point.

## Anchors Used

**Round 1 (bracketing):**
- `15lk4nBXYb.md` — CCM-DiT (3.00, weak band) — also camera-pose controllable on RE10K but DiT-based; ARSS is more novel.
- `MI0UiWeqOl.md` — Poly-Autoregressive (2.33, weak band) — different domain; not closely comparable.
- `hWlCc7Iksi.md` — ARVideo (3.40, weak band) — incremental AR with random order; ARSS is more concrete.
- `I86z54CL2y.md` — GeoGS3D (3.40, weak band) — different setting; not closely comparable.
- `KI1zldOFz9.md` — Training-free Camera Control (5.80, mid band) — training-free vs. ARSS's from-scratch; cleanly accepted.
- `NuHYh4YKNe.md` — GST: Where Am I (6.25, mid band) — read in full; AR + camera tokenization, similar in spirit; ARSS is below this.
- `0n4bS0R5MM.md` — VD3D (6.20, mid band) — read in full; Plücker camera control on transformer video, cleanly accepted; ARSS is below this.
- `pOcGFvfgjS.md` — AR-1-to-3 (5.00, mid band) — read in full; most directly comparable; same tier as ARSS.
- `QQBPWtvtcn.md` — LVSM (7.67, strong band) — baseline of ARSS; clear strength.
- `P4o9akekdf.md` — NoPoSplat (8.00, strong band) — clean accept; ARSS is well below.
- `QQ6RgKYiQq.md` — MovingParts (8.00, strong band) — different setting.
- `5UKrnKuspb.md` — NeuralPlane (8.00, strong band) — different setting.

Round-1 bracket: **[4.0, 6.0]**.

**Round 2 (narrowing):**
- `pOcGFvfgjS.md` — AR-1-to-3 (5.00) — re-anchor, comparable.
- `VLuJL8cnGk.md` — 3D-free meets 3D priors (5.00) — read in full; scene-level NVS reject with similar overclaim/limited-novelty profile.
- `b9dBNNeDd3.md` — Set Autoregressive Modeling (4.60) — AR for image generation; not as topically close.
- `j3rxIH0M9H.md` — MOVIS (4.50) — multi-object NVS, reject.
- `1ThYY28HXg.md` — GenXD (6.25) — comprehensive 3D/4D generation, accept; ARSS below.
- `0n4bS0R5MM.md` — VD3D (6.20) — re-anchor, ARSS below.
- `KI1zldOFz9.md` — Training-free Camera Control (5.80) — re-anchor.
- `zu7cBTPsDb.md` — MVTokenFlow (6.00) — accept, more comprehensive than ARSS.
- `Z4evOUYrk7.md` — CameraCtrl (6.50) — accept; established technique, clean execution; ARSS below.

Round-2 narrowing: ARSS sits comparable to AR-1-to-3 (5.0) and 3D-free meets 3D priors (5.0), and below the cluster at 5.8–6.5 (VD3D, GenXD, CameraCtrl, MVTokenFlow, Training-free CC). Final score sits in [4.5, 5.0]. The verifiable overclaiming, the unablated key component, and the never-tested motivating property push it slightly below AR-1-to-3 (which had cleaner if narrower claims).

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>