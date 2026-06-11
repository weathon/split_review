Now I have a thorough comparative picture. Let me write the final review.

## Comparison to anchors:

- **"3D-free meets 3D priors" (5.00, Reject)**: This paper has limited novelty (largely a combination of existing methods), restricted to 6 fixed viewpoints, and inconsistent results. ARSS is clearly stronger — it has genuine novelty (first AR-based NVS), handles arbitrary trajectories, and has more systematic evaluation.

- **"CamTrol" (5.80, Accept)**: Training-free camera control for video generation. Reviewers flagged pipeline fragility, missing ablations, limited novelty, and inconsistent results. ARSS has cleaner technical design and better ablations, but similar evaluation-gap issues.

- **"GST" (6.25, Accept)**: AR framework for joint localization and view prediction. Split reviews (3,8,6,8) due to overclaimed novelty and evaluation gaps. ARSS is comparable — both are AR-based approaches with camera tokenization — but ARSS has a more honest abstract and better ablation studies, while GST has more comprehensive evaluation breadth.

ARSS lands between CamTrol (5.80) and GST (6.25) in terms of novelty and contribution, but below both in evaluation completeness due to the SEVA omission from Figure 6 and the overclaim issue. I place it at **5.5**.

---

## Summary
ARSS proposes the first decoder-only autoregressive transformer framework for novel view synthesis from a single image with camera trajectory control. The method combines three components: a causal video tokenizer (VidTok) for multi-view tokenization, a geometry-constrained camera autoencoder that compresses Plücker raymaps into 3D positional tokens, and a hybrid token-ordering strategy that permutes tokens spatially within each frame while preserving strict temporal causality across frames. Experiments on RealEstate10K, ACID, and DL3DV demonstrate competitive results against diffusion-based baselines.

## Strengths
- **First application of causal AR to camera-controlled NVS**: The paper credibly fills a real gap — no prior work applies GPT-style decoder-only AR modeling to novel view synthesis with explicit camera trajectory control. The related work survey (Section 2) confirms AR visual generation methods target single-image generation, and diffusion-based NVS methods operate non-autoregressively.

- **Camera autoencoder with principled geometric constraints**: The loss function (Eq. 5) enforces unit-length ray directions and direction–momentum orthogonality in addition to reconstruction, going beyond naive coordinate encoding. The ablation on permutation strategies (Table 2) indirectly validates the importance of structured 3D positional tokens — without them, raster and full-perm strategies fail.

- **Hybrid permutation strategy well-validated**: The spatial-shuffle / temporal-preserve token ordering (Eq. 6) is the paper's most interesting technical contribution. Table 2 shows raster order collapses to PSNR 16.29 (vs. 19.22) and full spatial+temporal permutation drops to 18.76 with visible geometric errors (Figure 7), demonstrating temporal order must be preserved for causal structure to function.

- **Video tokenizer ablation is convincing**: Table 3 shows replacing VidTok with per-frame VQ tokenization causes FVD to explode from 52.56 to 137.68 and PSNR to drop from 19.22 to 15.69, directly demonstrating temporal consistency in tokenization is essential for multi-view generation.

- **Zero-shot generalization demonstrated**: The method transfers to DL3DV (Table 1, PSNR 16.70 vs. MotionCtrl 14.58, LVSM 15.86) and out-of-distribution AI-generated stylized images (Figure 5), showing the learned representations are not overfit to training-domain statistics.

## Weaknesses

### Fatal
None.

### Major
- **"Outperforms SOTA" claim is not supported by the paper's own evidence**: The introduction (L88) and discussion (L281) state ARSS "outperforms current state-of-the-art methods." Table 1 tells a more qualified story. On RealEstate10K, ARSS (19.02 PSNR / 0.624 SSIM / 47.60 FID) vs. SEVA (18.73 / 0.670 / 46.98): ARSS *trails* on SSIM by 6.9% and on FID (where lower is better, SEVA is ahead). On ACID, ARSS trails SEVA on SSIM (0.623 vs. 0.664) and substantially on FID (47.76 vs. 33.16). The abstract's "overall comparable" phrasing is accurate; the body's repeated "outperforms" is not. For a view synthesis method, trailing on SSIM — which directly measures structural consistency — against the strongest baseline is a meaningful gap the claims should reflect.

- **SEVA is absent from the error accumulation analysis (Figure 6), the experiment most directly testing the paper's core motivation**: The central motivation (L13–15) is that causal AR generation should produce better long-horizon consistency and less error accumulation than diffusion. Figure 6 is designed to demonstrate this, but SEVA — the only baseline competitive with ARSS in Table 1 — is missing. The analysis compares against LVSM, MotionCtrl, RayZer, and ViewCrafter, all of which substantially underperform ARSS in overall metrics (3–6 dB behind in PSNR). Winning an error-accumulation comparison against methods already far behind does not isolate the effect of the AR architecture; it mostly confirms the overall performance gap. Without SEVA in this figure, the paper's core architectural argument remains untested against the baseline that could challenge it.

### Minor
- **Unexplained discrepancy between Table 1 and Tables 2–3**: The main results (Table 1) report 19.02 PSNR / 0.624 SSIM / 0.269 LPIPS / 47.60 FID for ARSS on Re10K. The ablation tables (Tables 2–3) report 19.22 PSNR / 0.565 SSIM / 0.294 LPIPS / 60.11 FID for "ours." These are substantially different numbers (the ablation "ours" has worse SSIM, LPIPS, and FID), suggesting different evaluation splits or protocols. The paper does not explain this gap.

- **Camera autoencoder pre-training details are vague**: Section 3.2.2 describes the autoencoder architecture in general terms ("stacked 3D convolutional and downsampling blocks") and mentions it is "pre-trained," but does not specify on what data, for how long, or with what hyperparameters.

- **Parallel decoding claim stated but never evaluated**: L177–178 claims parallel decoding as "another advantage" of random spatial shuffling, but no inference-time speed comparison or any evaluation is provided.

### Trivial
None.

## Nice-to-Haves
- Reporting statistical significance or variance for metrics in Table 1, given the margin between ARSS and SEVA is often under 1 dB PSNR.
- Exploring the implications of the training-data asymmetry (ARSS trained from scratch at 256×256 vs. diffusion baselines fine-tuned from large pretrained models) more explicitly rather than only noting it as a limitation in the Discussion.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Training-from-scratch asymmetry as a major methodological gap**: The harsh critic framed this as a significant gap requiring exploration. The paper explicitly acknowledges this asymmetry in the Discussion (L281–282: "different from the current diffusion-based view synthesis method that mostly finetuned from pre-trained models, our method is trained from scratch using limited public datasets with relatively low resolution"). The paper frames its contribution as a proof-of-concept; acknowledging the limitation is sufficient. Demoted to Nice-to-Have.
- **Request for ablation on camera autoencoder vs. direct Plücker ray encoding**: This asks for an additional experiment beyond the paper's scope as a first-demonstration paper. The autoencoder's value is already indirectly validated by the permutation ablation (Table 2).
- **Tension between qualitative narrative and quantitative evidence regarding SEVA (harsh critic claim)**: The paper states SEVA "often suffer[s] from distortions and inaccurate camera pose alignment" (L194) while SEVA achieves better SSIM. However, the paper also acknowledges its own "minor geometric inconsistencies" (L231) and the qualitative claim about SEVA's distortions is about a specific failure mode (anchor-view interpolation causing inconsistency), which can coexist with better average SSIM. This is a framing choice, not an error.

## Novel Insights
The paper's hybrid token-ordering strategy — spatial permutation with temporal preservation — is a genuinely novel adaptation of single-image AR techniques to the multi-view setting. The finding that preserving temporal order is essential (full permutation degrades quality) while spatial shuffling is beneficial (raster order degrades even more) provides an interesting insight about what structure the causal mask should respect in visual AR models. This could inform future work in AR video and multi-view generation beyond this specific NVS application.

## Suggestions
- Add SEVA to the error accumulation analysis (Figure 6), or explain why it cannot be included (e.g., if SEVA's anchor-view-then-interpolate paradigm doesn't produce per-frame results in a comparable way). Either way, this gap should be addressed.
- Replace "outperforms" with "competitive with" or "comparable to" in the body text, consistent with the abstract, and explicitly discuss the SSIM vs. LPIPS trade-off between ARSS and SEVA.
- Clarify the evaluation protocol and explain the Table 1 vs. Tables 2–3 numerical discrepancy.
- Either evaluate the parallel decoding claim with inference-time measurements or remove it.

---

**Anchor comparison summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| PAR modeling (MI0UiWeqOl) | 2.33 | 1 | Much weaker — different domain, limited contribution |
| NeDDF (mYo9r0CwUf) | 2.33 | 1 | Much weaker — niche rendering method |
| IC-Light (u1cQYxRI1H) | 0.50 | 1 | Outlier; not comparable |
| Aircraft monitoring (EjIKerYk1O) | 2.33 | 1 | Different domain |
| Direct Gaussian Attribute Diffusion (rWIrdAo2xC) | 2.83 | 1 | Weaker — limited evaluation scope |
| Ctrl123 (CFOQd4tqn1) | 4.00 | 1 | Weaker — diffusion NVS with consistency issues |
| Latent Posterior Sampling (lMcoxeMYYw) | 4.25 | 1 | Different approach (probabilistic 3D) |
| GeoGS3D (I86z54CL2y) | 3.40 | 1 | Weaker — less novel |
| FreeVS (dTGH9vUVdf) | 5.80 | 1,2 | Similar quality — generative NVS on trajectories |
| CamTrol (KI1zldOFz9) | 5.80 | 1,2 | Comparable — camera control, evaluation gaps noted |
| 3D-free meets 3D priors (VLuJL8cnGk) | 5.00 | 1,2 | ARSS is clearly stronger — more novel, better evaluation |
| U3D (dyYc8GFdD5) | 5.00 | 1 | ARSS is stronger — more focused contribution |
| ImageFolder (QE1LFzXQPL) | 6.25 | 1 | Stronger — more mature AR image generation work |
| SEED Tokenizer (0Nui91LBQS) | 6.33 | 1 | Stronger — more polished contribution |
| SeTok (n64NYyc6rQ) | 6.20 | 1 | Stronger — vision tokenization for MLLMs |
| DnD Transformer (wryFCrWB0A) | 6.20 | 1 | Stronger — more mature AR contribution |
| LVSM (QQBPWtvtcn) | 7.67 | 1 | Much stronger — comprehensive transformer NVS |
| NoPoSplat (P4o9akekdf) | 8.00 | 1 | Much stronger — polished 3D reconstruction |
| TetSphere (8enWnd6Gp3) | 7.60 | 1 | Much stronger — different domain |
| MOS (Y6aHdDNQYD) | 8.00 | 1 | Different domain |
| GST (NuHYh4YKNe) | 6.25 | 2 | Slightly stronger — similar AR approach, more comprehensive |
| Zero-shot NVS via Video Diffusion (zDJf7fvdid) | 6.00 | 2 | Slightly stronger — cleaner evaluation |
| CamI2V (dIZB7jeSUv) | 5.50 | 2 | Comparable — camera-controlled generation |
| MagicDrive3D (0uFTqvQhML) | 5.00 | 2 | ARSS is stronger — more focused |
| Pseudo-Generalized Dynamic VS (QuVlUn4T2G) | 6.75 | 2 | Stronger — more mature dynamic NVS |

**Round 1 bracket**: 4.5–6.5. The paper is clearly above the weak reject anchors (2.33–4.25) and below the strong anchors (6.25+).

**Round 2 narrowing**: CamI2V (5.50) and CamTrol (5.80) sit close to ARSS in quality. GST (6.25) is slightly above. ARSS has stronger novelty than CamTrol but similar evaluation gaps. The paper is comparable to CamI2V (5.50) in overall quality — both have genuine contributions with fixable evaluation shortcomings. Final score: **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>