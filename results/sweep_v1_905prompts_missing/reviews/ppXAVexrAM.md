Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper presents ARSS, the first decoder-only autoregressive transformer framework for novel view synthesis (NVS) from a single image with camera control. The method combines a video tokenizer for temporally consistent discrete tokens, a camera autoencoder that converts Plücker raymaps into 3D positional guidance tokens, and a hybrid spatial-permutation strategy that shuffles token order within frames while preserving temporal causality. Experiments on RealEstate10K, ACID, and zero-shot DL3DV show that ARSS is competitive with diffusion-based NVS methods and demonstrates notably slower error accumulation over long camera trajectories.

## Strengths

- **First decoder-only AR model for camera-controlled NVS.** The paper is the first to apply a GPT-style causal autoregressive model to novel view synthesis with explicit camera conditioning. The method is sound and the overall pipeline (video tokenizer → camera tokens → spatial-permuted AR transformer) is coherently designed.

- **Hybrid token permutation strategy is well-motivated and ablated.** The spatial-only permutation (Section 3.2.3) is a principled adaptation of AR generation to multi-view data. The ablation in Table 2 shows clear gains over raster order (+3.3 PSNR) and full spatiotemporal permutation (+0.46 PSNR), and Figure 7 visually confirms that temporal causality reduces error accumulation in later frames.

- **Comprehensive evaluation across multiple datasets with zero-shot generalization.** The paper evaluates on two in-domain datasets (RealEstate10K, ACID) and one zero-shot benchmark (DL3DV), plus qualitative results on AI-generated images. The error accumulation analysis (Figure 6) is a strong piece of evidence that directly validates the causal AR advantage: ARSS maintains flatter quality degradation curves than all diffusion-based baselines across all per-frame metrics.

- **Ablation on tokenizer choice is informative.** Table 3 shows that replacing the VQ image tokenizer with the video tokenizer improves FVD by ~62% (137.68 → 52.56), confirming the importance of temporal consistency in the tokenization stage.

## Weaknesses

### Major

- **Overclaimed "outperforms" language contradicts the own evidence.** The abstract states that ARSS "achieves overall comparable to state-of-the-art view synthesis approaches," which is accurate. However, the Introduction (line ~113) claims "our method out-performs current state-of-the-art methods," and the Discussion (line ~507) repeats "our method outperforms state-of-the-art methods." Against the strongest competitor SEVA, the results are genuinely mixed: on RealEstate10K, ARSS is better on PSNR (+0.29 dB), LPIPS (−23%), and FVD (−12%), but worse on SSIM (−6.9%) and FID (+1.3%); on ACID the pattern is similar (PSNR +0.16 dB, LPIPS −19%, but SSIM −6.2%, FID +44%). These are competitive results, not a clear outperformance. The blanket "outperforms" claim in the body is misleading and should be harmonized with the more measured language in the abstract.

- **Missing ablation of the camera autoencoder.** The camera autoencoder is presented as a core contribution — it converts Plücker raymaps into 3D positional tokens that are interleaved with visual tokens. Yet there is no ablation study isolating its effect. The paper does not compare against simpler alternatives (e.g., flattening the Plücker map into a per-frame embedding prepended to each frame's token sequence, or using raw camera parameters as additive embeddings per token). Without this control, the reader cannot assess whether the autoencoder design is necessary or whether the same performance could be achieved with a cheaper conditioning mechanism. This weakens the engineering contribution and should be addressed.

### Minor

- **No statistical variance reported for any metric.** All results in Table 1 are single-point estimates. Given that PSNR differences against SEVA are 0.1–0.3 dB, it is impossible to know whether these reflect genuine improvements or noise from data splits or training randomness. Standard deviations or bootstrapped confidence intervals should be reported.

- **The camera autoencoder loss weights (λ₁–λ₄ in Eq. 5) are not specified.** The values matter for reproducibility; without them the loss formulation cannot be re-implemented exactly.

- **Minor inconsistency: "outperforms" vs "comparable."** As noted above, the abstract and the body sections disagree on the strength of the results. This needs to be resolved.

### Trivial

None.

## Nice-to-Haves

- The paper notes that random spatial permutation "allows parallel decoding" (citing Pang et al., 2025) but does not implement or evaluate this. A discussion or preliminary experiment would strengthen the practical appeal.
- Inference wall-clock time or FLOPs comparison with diffusion baselines would help readers assess the practical trade-offs, since AR generation of 16 frames × 1024 tokens sequentially may have different latency characteristics than joint diffusion.

## Removed Points

These points from the reviewers are flagged to be removed — treat them with caution:

- **"Eq. (7) seems incomplete"** — The reviewer acknowledges it is likely a formatting artifact. Equation (7) is a straightforward reformulation of the cross-entropy objective; the missing target term is a PDF extraction issue, not an author error.
- **"Figures 3 and 4 not visible to me"** — This is a PDF extraction limitation, not a paper flaw.
- **"Title is a bit dramatic"** — Pure style nitpick with no substantive bearing on evaluation.
- **"8 H100 GPUs is not trivial"** — The paper never claims lightweight training; it says trained "from scratch using limited public datasets." 8 H100s is a standard academic setup for this scale of work.
- **"The paper's core thesis... most novel insight is from Strength Finder"** — The Strength Finder claim about "per-frame error analysis... a direct benefit not easily obtained by joint-denoising diffusion models" is valid, but some of its other generic strengths (e.g., "camera autoencoder provides explicit 3D positional guidance") are assertions made by the paper itself rather than verified findings, so they are noted as claims rather than confirmed strengths.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Harmonize the claims.** Replace "outperforms state-of-the-art" with "competitive with" or "comparable to" throughout the body, consistent with the abstract language. The mixed metrics against SEVA do not support a blanket "outperforms" claim.

2. **Add an ablation of the camera autoencoder.** The simplest baseline: flatten the Plücker raymap per-frame into a single embedding vector that is prepended to each frame's token sequence, rather than per-token interleaved camera tokens. If the full autoencoder is not clearly better, the claimed contribution needs rethinking; if it is better, the ablation would strengthen that claim.

3. **Report variance.** Add standard deviations or confidence intervals to Table 1, at minimum for the primary metrics (PSNR, SSIM, LPIPS).

4. **Specify λ₁–λ₄ values** for Eq. (5) and provide architecture details for the camera autoencoder.

## Score and Decision

**Round 1 Bracket:** 4.5–6.5. The paper is clearly above weak rejected papers (~3.0–3.5) that have fundamental methodology flaws, and clearly below top papers (≥7.5) with transformative contributions and flawless execution.

**Round 2 Narrowing:** Compared against four anchors in the 4.5–7.0 range:
- **AR-1-to-3** (5.00, Reject) — very similar autoregressive NVS approach but with weaker evaluation (single synthetic dataset). ARSS is stronger (multiple benchmarks, zero-shot, ablations).
- **Training-free Camera Control** (5.80, Accept) — different approach, comparable overall quality. ARSS addresses a harder task with sounder methodology but has overclaiming issues.
- **Where Am I** (6.25, Accept) — similar AR approach for joint pose+view. ARSS has a less ambitious scope but cleaner method. Comparable quality of execution, though that paper's higher variance (3,8,6,8) reflects reviewer disagreement.
- **ControlAR** (6.25, Accept) — well-ablated controllable AR image generation. ARSS has weaker validation of its conditioning mechanism (missing camera autoencoder ablation) and thus sits below this anchor.

**Positioning:** ARSS is stronger than AR-1-to-3 (5.0) but weaker than ControlAR (6.25) and comparable to Training-free Camera Control (5.80). The overclaiming and missing camera autoencoder ablation prevent it from reaching the 6.0+ tier. The strongest advantages — the error accumulation analysis and the novelty of first decoder-only AR for NVS — are real but tempered by evidential gaps.

**Final Score: 5.5**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>