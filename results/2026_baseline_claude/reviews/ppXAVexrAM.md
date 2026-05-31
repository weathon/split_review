## Summary

ARSS presents a GPT-style decoder-only autoregressive framework for novel view synthesis (NVS) from a single image conditioned on a camera trajectory. The system combines a video tokenizer (VidTok) for temporal consistency, a camera autoencoder converting Plücker raymaps into latent 3D positional tokens, and an autoregressive transformer that permutes spatial token orders while preserving temporal ordering. The paper claims to be the first application of causal AR models to camera-controlled multi-view generation, reporting competitive results on RealEstate10K, ACID, and zero-shot evaluation on DL3DV.

---

## Strengths

- **Genuine novelty of the application.** Applying a GPT-style causal autoregressive model to camera-controlled NVS is a real first. The motivation—enabling strictly causal, incrementally extensible view generation along a trajectory—is well-articulated and distinguishes AR models from diffusion models on a fundamental modeling level.

- **Hybrid spatial/temporal permutation is well-justified and empirically validated.** The design choice to permute spatial order while preserving temporal order is principled, and Table 2 + Figure 7 clearly demonstrate that "raster" ordering degrades for distant frames while "full permutation" breaks temporal coherence. The ablation is controlled and convincing.

- **Video tokenizer ablation is decisive.** Table 3 shows a 62% FVD improvement over VQ image tokenization and large gains across all metrics, strongly validating the use of a temporally-aware tokenizer for multi-view generation.

- **Error accumulation analysis (Figure 6)** is a meaningful evaluation dimension for sequential view generation—tracking per-frame quality degradation across a trajectory is more informative than aggregate scores, and ARSS shows the slowest quality decay.

- **Zero-shot evaluation on DL3DV** demonstrates reasonable generalization beyond training distributions.

---

## Weaknesses

### Fatal
None.

### Major

1. **Quantitative claims do not uniformly support "outperforms state-of-the-art."** On RealEstate10K, SEVA achieves better SSIM (0.670 vs. 0.624) and FID (46.98 vs. 47.60). On ACID, SEVA is again better in SSIM and FID. ARSS leads in PSNR and LPIPS, but the abstract and discussion section claim broad superiority that is inconsistent with the mixed metric picture. The cherry-picking pattern—emphasizing per-pixel fidelity metrics while glossing over perceptual/distributional metrics—should be resolved with a more balanced interpretation.

2. **Discrepancy between Table 1 and Table 2.** The PSNR of "ours" is listed as **19.02** in Table 1 (main comparison) but **19.22** in Table 2 (ablation). This 0.2 dB gap is unexplained. If the ablation condition uses a different evaluation protocol, split, or checkpoint, it needs to be explicitly stated; otherwise it undermines the credibility of both tables.

3. **Comparison fairness is structurally compromised but inadequately discussed.** ARSS is trained from scratch at 256×256 resolution on RealEstate10K and ACID, while SEVA was fine-tuned from large pre-trained video diffusion models on much larger and higher-resolution data. The paper mentions this in the discussion but continues to benchmark them side by side as if they are comparable systems. A short compute/data table would clarify the regime each method operates in.

### Minor

1. **Resolution of 256×256 is a significant practical limitation.** For 2026 NVS, this resolution is well below community standards, and results at this scale may not translate to higher resolutions. The paper does not analyze whether the AR approach scales with resolution.

2. **Inference speed is not reported.** Autoregressive decoding over 4×32×32 = 4,096 tokens per generation is potentially very slow compared to a single diffusion denoising pass. Without profiling, the practical trade-off between the claimed causal/incremental advantages and inference cost is unclear.

3. **Camera autoencoder notation error in Eq. 5.** The text states "d is the normalized camera ray direction, **d** is the momentum term formulated as m = o × d" — the momentum term is clearly **m**, not **d**. The reconstruction loss variables in Eq. 5 use d̂ and m̂ correctly, but the text description conflates d and m.

4. **SEVA excluded from DL3DV comparison** because DL3DV was in its training set. While the exclusion is appropriate, the paper should make explicit that this means the DL3DV results do not provide a head-to-head comparison against the strongest baseline.

### Trivial
None beyond parser artifacts in the extracted text.

---

## Nice-to-Haves

- Report inference time (tokens/second or frames/second) vs. baselines to quantify the cost of the AR approach.
- Include a comparison at higher resolution (e.g., 512×512 or 768×768) even if only qualitative, to assess whether the video tokenizer quality bottleneck can be resolved.
- Report scene-level diversity metrics or out-of-domain qualitative comparisons beyond AI-generated cartoon images.

---

## Novel Insights

The paper's most substantive insight is that temporal ordering should be strictly preserved during token permutation for multi-view generation, while spatial ordering within frames can be freely randomized. This is not obvious: one might expect that since novel views are related by 3D geometry, full randomization should work better. The ablation compellingly shows that full permutation hurts because early frames' tokens guide late frames—temporal causality is a hard structural constraint for camera trajectories, not just a design preference. The use of camera tokens as "3D positional instruction tokens" (enabling the model to decode any spatially-shuffled token given its 3D location) is a clean generalization of the positional instruction idea from 2D AR generation to the NVS domain.

---

## Suggestions

- Resolve the 19.02 vs. 19.22 PSNR discrepancy with a clear explanation (different checkpoint? evaluation split?).
- Reframe the comparison against SEVA as "competitive under significantly different resource regimes" rather than claiming overall superiority, given the mixed metric picture.
- Add an inference-speed table to let readers make informed practical decisions.
- Fix the camera loss notation: replace the second "d is the momentum term" with "m is the momentum term" in the text below Eq. 5.

---

## Score and Decision

ARSS makes a genuine and timely contribution by demonstrating that AR models can perform camera-controlled NVS. The core insight—preserving temporal but randomizing spatial token order—is both principled and empirically validated. Performance is competitive under constrained training conditions. However, inflated claims of superiority, an unexplained metric discrepancy between tables, and the absence of inference-speed analysis are real weaknesses that require author attention before the paper is fully ready. The work is above the median and worth presenting to the community, but needs revision on the comparison framing and internal consistency.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>