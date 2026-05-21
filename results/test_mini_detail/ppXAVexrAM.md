Now I have a thorough understanding of the paper, the reviews, and the calibration anchors. Let me compose the final consolidated review.

## Summary

ARSS introduces the first decoder-only autoregressive framework for single-image novel view synthesis (NVS), replacing the joint-denoising paradigm of diffusion models with a next-token prediction process that naturally enforces causality along a camera trajectory. The method combines a causal video tokenizer, a camera autoencoder that encodes Plücker raymaps into 3D positional tokens, and a hybrid token permutation strategy that preserves temporal order while shuffling spatial tokens to accommodate bi-directional visual context within a causal transformer. Evaluated on RealEstate10K, ACID, and zero-shot on DL3DV, ARSS achieves competitive or state-of-the-art results against diffusion-based and transformer-based baselines, with notably slower error accumulation over long camera trajectories (Figure 6).

## Strengths

1. **First decoder-only AR model for NVS with camera control.** The paper presents a genuinely novel paradigm: applying a GPT-style causal transformer to multi-view novel view synthesis, with interleaved camera tokens providing explicit 3D positional guidance. This is a clear architectural contribution distinct from prior autoregressive image generation work (LlamaGen, VAR) and from diffusion-based NVS methods.

2. **Competitive quantitative results across benchmarks.** On RealEstate10K, ARSS achieves the best PSNR (19.02) and LPIPS (0.269) among all compared methods including the strong diffusion baseline SEVA. On zero-shot DL3DV, ARSS wins on all four reported metrics (PSNR 16.70, SSIM 0.449, LPIPS 0.347, FVD 91.25). The paper honestly acknowledges mixed results against SEVA on SSIM and FID, but the overall picture is competitive.

3. **Slowest error accumulation along camera trajectories.** Figure 6 is the paper's strongest direct evidence for the value of autoregressive generation in NVS. ARSS maintains the highest per-frame PSNR/SSIM and lowest LPIPS with flatter degradation slopes than LVSM, MotionCtrl, RayZer, and ViewCrafter across 17 frames. This validates that the causal, sequential generation structure accumulates less error over long sweeps.

4. **Hybrid token permutation strategy thoroughly ablated.** Table 2 shows that the proposed spatial-only permutation (preserving temporal order) substantially outperforms both raster ordering (+2.93 PSNR) and full spatiotemporal permutation (+0.46 PSNR), with supporting visual evidence in Figure 7. This is a clean, informative ablation.

5. **Video tokenizer choice validated.** Table 3 shows VidTok improves FVD by ~62% over a VQ image tokenizer (52.56 vs. 137.68), demonstrating that temporal-aware tokenization is critical for multi-view sequences. The 16-frame temporal receptive field of VidTok is explicitly noted and its impact quantified.

6. **Strong zero-shot generalization.** Beyond the DL3DV results, Figure 5 shows plausible novel views from AI-generated, cartoonish, and oil-painting-style inputs far from the training distribution, demonstrating practical robustness.

## Weaknesses

### Fatal
None.

### Major

1. **Gap between claimed advantages and evaluation.** The paper repeatedly motivates the AR approach by arguing that causal, sequential generation enables capabilities that joint-diffusion methods lack — specifically the ability to "incrementally extend and reuse existing generations when the trajectory changes" (Section 1). Yet the evaluation tests only fixed-trajectory generation, exactly the same task setting used for the diffusion baselines. There is no experiment that (a) extends a trajectory beyond the predefined frames, (b) modifies a camera path mid-generation, or (c) reuses previously generated views when conditioning on a new trajectory. While the error accumulation analysis (Figure 6) partially demonstrates the value of sequential generation for long trajectories, the claimed flexibility advantages over diffusion are never tested. This does not invalidate the paper's core contribution (building an effective AR NVS system), but it means the paper's framing overreaches relative to what is demonstrated.

2. **Camera autoencoder is never ablated.** Camera tokens are a core contribution providing "3D positional guidance" and enabling the random spatial permutation strategy. Yet there is no ablation that removes or replaces them (e.g., using learned positional embeddings or omitting camera conditioning entirely) to quantify their contribution. Without this, we cannot isolate whether the method's performance is driven by the camera encoder design, the video tokenizer, the permutation strategy, or interactions among them. This is a clear methodological gap.

### Minor

3. **SEVA excluded from error accumulation analysis (Figure 6).** SEVA is the strongest diffusion baseline and achieves the closest results to ARSS. Its absence from the per-frame quality comparison undermines the most direct evidence for ARSS's sequential advantage. The paper should either include SEVA or explicitly state why it cannot be evaluated (e.g., if SEVA does not produce per-frame metrics or cannot be adapted to long trajectories).

4. **Quantitative results against SEVA are mixed, especially on ACID.** On RealEstate10K, ARSS wins on PSNR and LPIPS but loses on SSIM (-6.6%) and marginally on FID (+1.3%). On ACID, the gap widens: ARSS wins on PSNR and LPIPS but is substantially worse on FID (+44%, 47.76 vs. 33.16) and SSIM (-6.2%). The paper's conclusion (Section 5) states that the method "outperforms state-of-the-art methods leveraging diffusion models and transformers," which overstates the case against SEVA. The abstract's more measured phrasing ("overall comparable") is more appropriate.

5. **No inference speed or efficiency comparison.** The paper mentions parallel decoding as an advantage of the shuffled-token approach but provides no latency, throughput, or memory comparison with any diffusion baseline. For a paper claiming practical advantages of AR over diffusion, this is a notable absence.

### Trivial

6. **Training at 256×256 resolution only.** The paper honestly acknowledges this limitation and notes the tokenizer as the bottleneck, but the low resolution means the visual results lag behind higher-resolution diffusion baselines.

7. **The paper's description of Eq. (5) contains a typo** — the text says "d is the normalized camera ray direction, d is the momentum term" where the second "d" should be "m." This is a minor presentation issue.

## Nice-to-Haves

- **Trajectory extension/modification experiments.** Running experiments where (a) a fixed trajectory is generated then extended, and (b) the camera path is modified mid-generation, would directly validate the paper's motivational claims and strengthen the contribution considerably.
- **Ablation of the camera autoencoder.** Replacing camera tokens with simple learned positional embeddings (per-frame or per-token) and measuring the performance drop would isolate the value of explicit 3D guidance.
- **Failure case analysis.** The paper discusses the tokenizer quality limitation but provides no examples of failure modes (e.g., large view changes, complex geometry).
- **Including SEVA in the error accumulation plot** to provide a complete picture of how different generative paradigms handle long trajectories.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The orthogonality regularization in Eq. (5) is trivially zero"** — Factually incorrect. The term uses reconstructed d̂ and m̂, not ground truth d and m, so it enforces the Plücker identity on reconstructions, which is a meaningful geometric constraint.
- **"Modest margins on DL3DV"** — ARSS wins *all* metrics (PSNR +0.84 over LVSM, SSIM +0.040) on a challenging zero-shot benchmark. Describing this as "modest" misrepresents the results.
- **"Compute parity with baselines not discussed"** — Standard practice in the field; not a weakness specific to this paper.
- **"Camera autoencoder not described in enough detail"** — The paper specifies "stacked 3D convolutional and downsampling blocks" and "symmetric 3D convolutional and upsampling blocks," which is adequate for a conference paper; code will be released.
- **"Missing related works"** — Cannot be verified without external sources.
- **"Formatting/style nitpicks"** — Parser artifacts, not author errors.

## Novel Insights

The harsh critic correctly identifies that the paper's motivational framing overreaches compared to what is actually evaluated — the claimed advantages of causal, sequential generation (trajectory extension, mid-generation modification) are never tested. This is an important observation because it reveals a recurring tension in AR-for-vision papers: the language modeling framing suggests capabilities (e.g., context extension, in-context modification) that are genuinely novel for vision but require dedicated experiments to validate. The error accumulation analysis partially bridges this gap, but a full validation would require task designs that explicitly test for advantages that joint-generation models cannot replicate. Separately, the missing camera autoencoder ablation is a missed opportunity — the paper's strongest design innovation (interleaved camera tokens as 3D positional guidance) lacks a controlled experiment that would make its importance unambiguous.

## Suggestions

1. **Re-frame the paper's claims to match what is evaluated.** Replace language about "extending and reusing generations" with clear statements about the well-demonstrated advantages: (a) competitive quality with a different generative paradigm, (b) slower error accumulation over long sequences, and (c) the novelty of applying decoder-only AR to NVS with camera control.

2. **Add a camera autoencoder ablation.** This is the single most impactful missing experiment — replacing camera tokens with learned positional embeddings and measuring the performance drop would directly quantify the value of the proposed 3D positional guidance.

3. **Include SEVA in the error accumulation analysis or explain why it cannot be included.** This would strengthen the paper's strongest evidence for AR's sequential advantages.

4. **Add an inference speed/latency comparison.** Even a simple table showing generation time per frame for ARSS vs. a diffusion baseline would address a natural question readers will have.

## Score and Decision

**Calibration:** 

*Round 1 (bracketing):*
- Low band (<3.5): ARVideo (3.40, Withdrawn), GeoGS3D (3.40, Withdrawn), Poly-Autoregressive (2.33, Withdrawn) — all clearly weaker than ARSS.
- Middle band (3.5–7.5): NVS-Solver (6.00, Accept Poster), Bridging AR and Masked (5.50, Reject), 3D-free meets 3D priors (5.00, Reject), U3D (5.00, Withdrawn).
- High band (>7.5): LVSM (7.67, Accept Oral), NoPoSplat (8.00, Oral), DMV3D (8.00, Spotlight) — ARSS is clearly below these.

Initial bracket: **5.0–6.5**.

*Round 2 (narrowing):*
- In-bracket anchors: NVS-Solver (6.00), GTA (6.25), Efficient-3DiM (7.25), Diffusion² (6.25).
- ARSS vs. NVS-Solver (6.00): Both propose novel NVS paradigms. NVS-Solver is cleaner (training-free) but has a more incremental contribution. ARSS has a more novel paradigm (first AR NVS) but weaker evaluation completeness (untested claimed advantages, missing ablations). Comparable quality overall.
- ARSS vs. GTA (6.25): GTA is a well-executed but incremental attention mechanism modification. ARSS has a more paradigm-shifting contribution but more evaluation gaps. Slightly weaker than GTA.
- ARSS vs. Efficient-3DiM (7.25): Efficient-3DiM has a clear, well-demonstrated practical contribution (10× training speedup) with strong consensus. ARSS's contribution is more novel but less thoroughly validated. Clearly below Efficient-3DiM.
- ARSS vs. 3D-free meets 3D priors (5.00, Reject): ARSS is significantly stronger in novelty, writing quality, and experimental thoroughness.

Final comparison: ARSS sits between the rejected 5.00-level papers and the accepted 6.00–6.25 poster papers. It has a genuine novelty advantage over the latter but carries evaluation gaps that the accepted papers do not. The most comparable anchor is NVS-Solver (6.00), and ARSS is approximately at that level — novel enough to warrant acceptance but with real weaknesses that the authors should address.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>