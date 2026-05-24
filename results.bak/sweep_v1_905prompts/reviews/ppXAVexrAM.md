## Summary

ARSS proposes the first decoder-only autoregressive (GPT-style) framework for single-image novel view synthesis with explicit camera control. The method tokenizes multi-view image sequences using a video tokenizer, encodes camera trajectories into latent tokens via a learned camera autoencoder, and applies a hybrid token-order permutation (spatial shuffle, temporal fixed) that preserves temporal causality while enabling bi-directional spatial context. On RealEstate10K and ACID, ARSS achieves competitive results against diffusion-based methods (best PSNR and LPIPS, though behind SEVA on SSIM and FID), and the error accumulation analysis (Figure 6) convincingly demonstrates slower degradation along long camera trajectories.

## Strengths

- **First decoder-only autoregressive model to achieve competitive NVS against diffusion baselines.** Table 1 shows ARSS obtains the highest PSNR (19.02 on Re10K, 21.93 on ACID) and lowest LPIPS (0.269, 0.265) among all compared methods including SEVA, Genwarp, and LVSM. This is the first evidence that a causal next-token-prediction paradigm can match diffusion-based NVS on standard benchmarks.

- **Hybrid token-order permutation is well-motivated and convincingly validated.** Section 3.2.3 describes a strategy that permutes tokens within each frame's spatial grid while keeping the temporal order fixed. The ablation (Table 2) shows clear gains: hybrid ordering achieves 19.22 PSNR vs. 16.29 (raster) and 18.76 (full perm.), and Figure 7 provides visual confirmation that this design avoids geometry distortions.

- **Video tokenizer ablation demonstrates the importance of temporal encoding.** Table 3 reports that the video tokenizer (VidTok) achieves FVD 52.56 vs. 137.68 for per-frame VQ image tokenization — a ~62% improvement — quantitatively confirming that temporal structure in the latent space is critical for multi-view consistency.

- **Error accumulation analysis (Figure 6) is compelling and practically significant.** The per-frame metric curves show that ARSS maintains consistently higher quality and slower degradation than all baselines along 16-frame trajectories, directly demonstrating the advantage of the causal design over joint-generation diffusion methods.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Overclaiming in the introduction and conclusion.** The abstract appropriately says "overall comparable" to state-of-the-art methods, but the introduction (line 114) and the Discussion (line 492) state that the method "out-performs current state-of-the-art methods." This is not fully supported: against SEVA, ARSS wins on PSNR and LPIPS but loses on SSIM (0.624 vs. 0.670) and FID (47.60 vs. 46.98), and the paper acknowledges this trade-off in Section 4.2 ("it can show minor geometric inconsistencies (e.g., -6.6% SSIM, +22% FID)"). The claims in the intro and conclusion should be tempered to match the evidence.

- **No ablation isolates the camera autoencoder.** The camera autoencoder is described as a core component that provides "3D positional instruction tokens" (Section 3.2.2), yet there is no experiment comparing the full method against (a) removing camera tokens entirely, (b) replacing them with a simpler pose embedding (e.g., a linear projection of the 6‑DoF pose), or (c) using Plücker coordinates directly without the learned autoencoder. Without this ablation, the reader cannot assess how much the designed autoencoder contributes relative to simpler alternatives.

- **Ablation evaluation setup is unspecified.** Tables 2 and 3 do not state which dataset the ablations are performed on, and the PSNR of the "ours" row (19.22) differs from the main Re10K result (19.02) without explanation. The 0.2 dB gap could stem from a different split, different frame count, or different checkpoint; the paper must clarify the setup and explain any discrepancy so that the ablation numbers can be compared to the main results.

### Trivial

- **Camera autoencoder training details are missing.** The paper mentions it is "pre-trained" (line 100) but does not specify what data it is trained on, for how many iterations, or whether it is frozen or finetuned during the autoregressive training. These details affect reproducibility.

- **FSQ codebook dimensions and levels are not reported.** The paper states it uses VidTok with FSQ (line 345) but does not specify the number of dimensions or levels used for quantization.

- **Minor notation issue in Eq. (5) description.** The text after Eq. (5) says "where **d** is the normalized camera ray direction, **d** is the momentum term formulated as **m** = o × **d**." The second **d** should be **m**. (The equation itself is correct.)

## Nice-to-Haves

- A camera autoencoder ablation (as described in Minor) would substantially strengthen the paper's claims about 3D-aware conditioning.
- Reporting the error accumulation analysis (Figure 6) with confidence intervals or standard deviation bands across sequences would make the figure definitive.
- A comparison of inference cost (number of forward passes to generate a trajectory) against diffusion baselines would highlight a practical advantage of the autoregressive approach.
- Adding a table row indicating the training data scale and resolution of each baseline would help readers calibrate the comparison (the paper already notes that SEVA benefits from larger-scale training).

## Removed Points

These points were flagged during review but removed for the reasons stated:

- **Criticism about Plücker coordinates not being novel**: The paper never claims novelty for Plücker coordinates; it claims novelty for the full AR pipeline. This is a strawman.
- **Criticism about LVSM being non-generative**: The paper includes LVSM as a non-diffusion baseline, which is appropriate for NVS comparison. No issue.
- **Request for "more detail" on camera autoencoder architecture beyond "stacked 3D convolutional and downsampling blocks"**: For a camera autoencoder described in the main paper (not the primary contribution), this level of detail is standard. Appendix would be the place for more.
- **Complaint that Eq. (1)/(3) have LaTeX formatting errors**: These are parser artifacts from PDF extraction; the original submission is fine.
- **Missing related works**: Cannot be verified without external sources.

## Novel Insights

None beyond the paper's own contributions. The reviews surface known trade-offs (autoregressive vs. diffusion, metric-level patterns) but do not produce a new synthesis beyond what the paper already articulates.

## Suggestions

1. **Temper the claims** in the introduction and conclusion to match the abstract's phrasing ("overall comparable" or "competitive on several metrics").
2. **Add a camera autoencoder ablation** — at minimum compare full method vs. no camera tokens vs. a simple linear projection of 6‑DoF poses.
3. **Specify the ablation dataset and explain the PSNR gap** (19.22 vs. 19.02) directly in the table captions or a footnote.
4. **Report FSQ configuration** (number of dimensions, levels) for reproducibility.
5. **Add a training setup note** for the camera autoencoder (data, iterations, frozen/finetuned).

## Score and Decision

### Calibration Protocol

**Round 1 — Bracketing**: Three queries on autoregressive/visual NVS topics.

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| `15lk4nBXYb` (CCM-DiT) | 3.00 | 1 | Much weaker; limited evaluation |
| `I86z54CL2y` (GeoGS3D) | 3.40 | 1 | Weaker; narrower scope |
| `hrXt6Fdl2P` (FV-NeRV) | 2.60 | 1 | Much weaker; different task |
| `pOcGFvfgjS` (AR-1-to-3) | 5.00 | 1 | Similar paradigm; ARSS has stronger evaluation and clearer contribution |
| `NuHYh4YKNe` (Where Am I) | 6.25 | 1 | Comparable AR paradigm; ARSS has cleaner NVS focus |
| `zDJf7fvdid` (Zero-shot Video NVS) | 6.00 | 1 | Comparable quality; ARSS has stronger novelty |
| `KUz8QXAgFV` (Bridging AR/Masked) | 5.50 | 1 | Different task; less directly comparable |
| `QQBPWtvtcn` (LVSM) | 7.67 | 1 | Stronger paper; ARSS below this level |

**Round 1 bracket**: 5.0 – 6.5

**Round 2 — Narrowing**: One query within 4.5–6.5 on autoregressive NVS topics.

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| `pOcGFvfgjS` (AR-1-to-3) | 5.00 | 2 | ARSS is clearly stronger (more datasets, better ablations) |
| `NuHYh4YKNe` (Where Am I) | 6.25 | 2 | Comparable; ARSS slightly cleaner but both have overclaiming issues |
| `zDJf7fvdid` (Zero-shot Video NVS) | 6.00 | 2 | Comparable; ARSS has more novel contribution |
| `VLuJL8cnGk` (3D-free meets 3D Priors) | 5.00 | 2 | ARSS is stronger |

**Final score**: 6.0. The paper sits between AR-1-to-3 (5.00) and Where Am I (6.25), closer to the upper end. It makes a genuine contribution (first AR pipeline for NVS) with solid empirical validation, but the overclaiming and the missing camera autoencoder ablation prevent it from reaching the 6.5+ range. The weaknesses are all addressable.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>