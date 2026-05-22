Now I have all the evidence I need. Let me produce the final consolidated review.

## Summary

The paper proposes ARSS, a decoder-only autoregressive transformer framework for novel view synthesis from a single image along a predefined camera trajectory. It combines a video tokenizer (for temporally consistent discrete tokens), a camera autoencoder (to encode Plücker raymaps into 3D positional guidance tokens), and a hybrid token permutation strategy (spatial shuffle while preserving temporal order) to enable causal next-token prediction for multi-view sequences. Experiments on RealEstate10K, ACID, and zero-shot DL3DV show competitive results against diffusion-based and transformer-based baselines.

## Strengths

- **First decoder-only autoregressive model for camera-controlled novel view synthesis.** The paper demonstrates a complete framework (Sections 3.2.1–3.2.3) that integrates a causal transformer with camera conditioning tokens, producing competitive results on standard benchmarks (Table 1). Prior autoregressive visual generation methods (e.g., LlamaGen, VAR) focused on single images; extending this paradigm to multi-view camera-controlled generation with explicit temporal causality is a genuine departure from joint-denoising diffusion approaches.

- **Hybrid token permutation strategy is well-motivated and experimentally validated.** Section 3.2.3 (Eq. 6) introduces spatial-only shuffling with preserved temporal order. Ablation Table 2 shows this outperforms raster order by +2.93 PSNR and full spatiotemporal permutation by +0.46 PSNR, providing direct evidence that the design choice is effective for autoregressive multi-view generation.

- **Video tokenizer ablation shows substantial temporal consistency gains.** Table 3 compares VQ image tokenizer vs. video tokenizer: FVD drops from 137.68 to 52.56 (≈62% reduction) with corresponding PSNR gains, directly validating the claim that temporal encoding is critical for multi-view sequences.

- **Error accumulation analysis demonstrates slower degradation over long trajectories.** Figure 6 shows per-frame metrics across 17 frames with consistently flatter degradation slopes than several baselines (LVSM, MotionCtrl, RayZer, ViewCrafter), supporting the claimed advantage of causal autoregressive generation for long camera sweeps.

- **Qualitative zero-shot generalization to out-of-distribution inputs.** Figure 5 shows plausible novel views from AI-generated oil-painting and cartoon images, and quantitative zero-shot results on DL3DV (Table 1: 16.70 PSNR) outperform compared methods, suggesting meaningful generalization beyond training distribution.

## Weaknesses

### Fatal
None. While several significant issues exist, none unambiguously invalidate the paper's core claims from the evidence on the page.

### Major

- **Camera autoencoder — a core claimed contribution — is never ablated.** The paper presents the camera autoencoder as a key innovation (Section 3.2.2): "we propose to pair each discrete token with a 3D positional guidance token extracted from the pre-defined camera trajectory." Yet Section 4.3 (ablation studies) only varies token permutation strategies (Table 2) and tokenizer types (Table 3). No experiment removes or replaces the camera tokens (e.g., with a learned placeholder, sinusoidal positional embeddings, or no camera conditioning at all). Without this, the reader cannot attribute any performance gain to the camera encoder. The camera autoencoder's reconstruction quality (e.g., Plücker map PSNR or angular error) is also never quantitatively evaluated, and its training procedure (data, epochs, whether trained jointly with the transformer) is not described. This is a significant gap because the paper's claimed novelty depends in part on this module.

- **Baseline adaptation to the single-view setting is not described, leaving the quantitative comparison hard to interpret.** Section 4.1 lists six baselines (LVSM, RayZer, SEVA, Genwarp, MotionCtrl, ViewCrafter) but provides no description of how each method was adapted to the specific setting of (a) single-view input, (b) generating a fixed-length 16-frame sequence along a predefined trajectory, and (c) the same resolution and evaluation protocol. Several baselines (e.g., RayZer, ViewCrafter) are designed for multi-view or video input and may perform poorly when given only one view. Table 1 reports ViewCrafter at 12.67 PSNR and RayZer at 12.97 PSNR on RealEstate10K — values notably lower than other baselines (LVSM at 18.29, SEVA at 18.73). Without details on how baselines were adapted, it is unclear whether these low scores reflect genuine limitations of those methods or a protocol mismatch. This does not invalidate the results, but it substantially weakens the headline claim that ARSS "outperforms current state-of-the-art methods."

### Minor

- **SEVA, the strongest competitor, is excluded from the error accumulation analysis (Figure 6).** Figure 6 compares LVSM, MotionCtrl, RayZer, ViewCrafter, and ARSS, but omits SEVA — the method that achieves the closest metrics to ARSS (e.g., on ACID: SEVA SSIM 0.664 vs. ARSS 0.623; SEVA FID 33.16 vs. ARSS 47.76). Including SEVA would substantially strengthen the error accumulation comparison. The paper does not explain this omission.

- **Overclaiming "outperforms" vs. the paper's own data.** The abstract states results are "overall comparable to state-of-the-art," while the body (line 114, line 490) claims the method "out-performs current state-of-the-art methods." Table 1 tells a mixed story: vs. SEVA, ARSS leads on PSNR (+1.1% on Re10K, +0.7% on ACID) and LPIPS (-21% on Re10K, -19% on ACID) but trails on SSIM (-6.6% on ACID) and FID (+22% on ACID, +1.3% on Re10K). The body does acknowledge these tradeoffs (lines 419–429), but the claims in the abstract/introduction and the claims in the discussion section are not well-calibrated to the evidence.

- **No statistical significance or variance reported.** All metrics in Tables 1–3 are reported as point estimates without standard deviations, confidence intervals, or number of runs/random seeds. Given the modest gap between some conditions (e.g., "full perm." vs. "ours" in Table 2: 0.46 PSNR), variance information is needed to assess whether differences are meaningful.

- **Slight PSNR discrepancy between main results and ablation.** Table 1 reports ARSS at 19.02 PSNR on RealEstate10K, while Table 2's "ours" row reports 19.22 PSNR. The ablation does not specify its evaluation dataset; if these numbers come from the same benchmark, the discrepancy (~0.2 PSNR) should be explained.

### Trivial

- Eq. (1) contains a stray formatting artifact: `x_{<i}}` with an extra closing brace (line 195).
- The paper states "image tokenizer fails to capture inter-frame relationships, often lead to temporal artifacts" — minor grammatical issue.

## Nice-to-Haves

- **Ablation of camera autoencoder** (as described in Weaknesses) is the single most important missing experiment.
- **Report camera autoencoder reconstruction quality** (Plücker map PSNR/angular error) to confirm that the latent tokens encode meaningful 3D geometry.
- **Include SEVA in the error accumulation analysis** (Figure 6).
- **Report standard deviations** for all metrics to establish statistical significance.
- **Describe baseline adaptation protocol** in detail: which specific codebases were used, what input was given to each method, how camera trajectories were aligned.

## Removed Points

**Points from the harsh critic that were removed or significantly weakened:**

1. *"RayZer and ViewCrafter PSNR values are far below the 18–20 range typical of published single-view NVS methods... this discrepancy strongly suggests a protocol mismatch."* — The claim that "18–20 PSNR is typical" relies on knowledge of published results not present in the paper. The critic's specific conclusion (protocol mismatch) is speculative. The more defensible version (missing adaptation details) is retained as a Major weakness above. The dramatic "structural flaw" framing is not justified from the paper alone.

2. *"The paper provides no description of how each baseline was adapted... making the reported numbers uninterpretable. This is a structural flaw."* — Weakened from "structural/fatal" to "Major." The numbers are not inherently uninterpretable — the paper shows consistent trends across multiple metrics and datasets, and the qualitative results provide corroborating evidence. The missing description is a significant omission but does not invalidate the results.

3. *"State-of-the-art claim overstates results... the paper fails to acknowledge these weaknesses."* — The paper does acknowledge the mixed comparison with SEVA (lines 419–429 note the SSIM/FID tradeoffs explicitly). This is retained as a Minor weakness about inconsistent claim calibration ("comparable" vs. "outperforms"), not as an evidential failure.

4. *"Fatal weaknesses that currently invalidate the central claims."* — No single verified weakness is fatal. The camera autoencoder oversight and missing baseline details are significant but addressable gaps. The paper's core contribution — the overall ARSS framework with hybrid token permutation and video tokenization — is validated by the ablations and qualitative results that do exist.

5. *Specific reproducibility nitpicks* (missing appendix content, training log artifacts, etc.) — Removed per hard rules.

6. *Strength Finder — "Camera autoencoder with geometric constraints for 3D positional tokens"* — Removed as a strength because it conflicts with the verified weakness (no ablation of this component), per the rule that when a strength and weakness disagree, the weakness wins.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the same issues the paper's own discussion section partially acknowledges (tokenizer limitations, training from scratch).

## Suggestions

1. Add an ablation study that replaces camera tokens with a simple alternative (e.g., learnable placeholder tokens or sinusoidal positional embeddings for each token's spatial location) and reports the resulting metrics. This is essential to validate the camera autoencoder contribution.
2. Describe in detail how each baseline was adapted to the single-view sequential setting — include which codebase version, input format, and evaluation trajectory were used.
3. Include SEVA in the error accumulation analysis (Figure 6) and report per-frame metrics for all methods on matched trajectories.
4. Calibrate claims: the abstract's "overall comparable" is more accurate than the body's "outperforms" given the mixed results against SEVA on SSIM/FID.
5. Report standard deviations or confidence intervals for all quantitative metrics.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>