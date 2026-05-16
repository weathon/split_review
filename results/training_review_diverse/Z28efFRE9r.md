## Summary

AuthFace proposes a two-stage blind face restoration method that: (1) fine-tunes SDXL on only 1.5K extremely high-quality (8K+) professional face images with photography-guided annotations to create a face-oriented diffusion prior, and (2) trains a ControlNet with a time-aware latent facial feature loss that weights intermediate diffusion steps where eyes and mouth shapes emerge. The method achieves state-of-the-art results on real-world BFR benchmarks (MANIQA, MUSIQ, CLIPIQA) and produces visibly sharper facial details. The central claim is that quality-first fine-tuning on a tiny curated set, combined with the proposed time-aware loss, produces more "authentic" restorations than prior T2I-based BFR methods.

## Strengths

- **State-of-the-art perceptual quality on real-world benchmarks.** AuthFace achieves the best MANIQA, MUSIQ, and CLIPIQA scores across LFW-Test, WebPhoto-Test, and WIDER-Test, often by large margins (e.g., MANIQA on LFW: 0.6431 vs. next-best 0.5528; Table 1). The qualitative figures corroborate this with visibly sharper skin texture, eyelashes, and fewer artifacts around glasses and teeth.

- **Face-oriented fine-tuning on a tiny curated dataset is shown to improve the generative prior.** The ablation (Table 2, Exp. a vs. b) demonstrates that replacing the original SDXL prior with the fine-tuned version improves CLIPIQA from 0.6276 to 0.6833 on WebPhoto and MUSIQ from 67.01 to 72.35, while qualitative comparisons (Fig. 2b) show the fine-tuned model produces less over-smoothed skin in T2I generation.

- **Time-aware facial feature loss provides a measurable improvement over constant-weight alternatives.** The ablation (Table 2, Exp. c vs. d) shows the time-aware weighting raises MUSIQ from 68.52 to 74.11 on WebPhoto and MANIQA from 0.6449 to 0.6624 on CelebA, while reducing artifacts around glasses and improving eyebrow/skin texture (Fig. 5). The core insight — that intermediate diffusion steps matter most for facial structure — is well motivated by the visualization in Fig. 6.

## Weaknesses

### Fatal
None.

### Major

- **No identity preservation metric is reported.** The paper's title and framing center on "authentic" face restoration, yet no face-recognition based identity similarity (e.g., ArcFace/FaceNet cosine distance between restored output and reference) is evaluated. This is a standard evaluation in prior BFR work (CodeFormer, GFP-GAN, BFRffusion all report it). Without this, it is impossible to rule out the scenario where the fine-tuned prior biases toward a particular face style at the expense of identity fidelity. The "authentic" claim is incomplete without evidence that identity is preserved, not just that perceptual quality scores are high. This is the single most important gap to address.

### Minor

- **Time-aware loss is under-validated.** The ablation compares the proposed logit-normal weighting only against a constant weight, not against natural alternatives (e.g., uniform weight over steps 300–700, linear decay, or Gaussian centered at intermediate steps). The parameters `m` and `s` of the weighting function are never reported, and the non-standard definition `logit(t) = log(1/(t(1-t)))` (rather than the standard `log(t/(1-t))`) is not explained or justified. The paper's argument that intermediate steps matter is qualitatively supported (Fig. 6), but whether the *specific* logit-normal form outperforms simpler schemes is not demonstrated.

- **Worse FID than SUPIR is noted but not discussed.** On CelebA, LFW, and WebPhoto, AuthFace's FID is substantially worse than SUPIR (CelebA: 50.93 vs. 35.01; WebPhoto: 90.04 vs. 73.44). The paper acknowledges this in passing ("except for FID") but provides no analysis or plausible explanation (e.g., reduced diversity from the fine-tuned prior, or a trade-off between per-image quality and distributional fidelity). FID is a key metric and this omission weakens the evaluation.

- **FID is omitted from the ablation study.** The ablation table (Table 2) reports PSNR, MANIQA, MUSIQ, and CLIPIQA but not FID or LPIPS, both of which are reported in the main comparison (Table 1). This is a significant omission since FID is the one metric where AuthFace underperforms, and the ablation could help disentangle which component is responsible.

- **Null prompts in Stage II disconnect the text-conditional prior from restoration.** The ControlNet is trained with null/empty prompts (line 149), meaning the text-conditional capability developed during fine-tuning (photography-guided annotations) is not leveraged during restoration. The paper does not discuss this design choice or test whether prompts derived from the degraded image could further improve results.

### Trivial
None.

## Nice-to-Haves

- Evaluate identity similarity (ArcFace/FaceNet) on both CelebA-Test (against GT) and LFW (against same-identity reference). This is the single most impactful addition.
- Compare the time-aware loss against 2–3 simpler weighting schemes (uniform over steps 300–700, linear, Gaussian) to validate the specific logit-normal choice.
- Report the chosen `m` and `s` values and how they were selected.
- Add FID and LPIPS to the ablation table.
- Provide a brief discussion of the FID gap — is it reduced diversity, or does FID penalize the method's fine-grained detail enhancement?
- Include inference cost (time, model size) for practical consideration.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The fine-tuning on 1.5K images is not validated for generalization"** — The model generalizes to four held-out test sets (CelebA-Test, LFW-Test, WebPhoto-Test, WIDER-Test) that contain different images from the 1.5K training set, and the ablation shows the fine-tuned prior outperforms the original SDXL on these sets. Concerns about overfitting are not supported by the evidence and are adequately addressed by the existing experiments.

- **"Missing related works"** — Per policy, this cannot be included without external verification.

- **"No ablation of annotation quality"** — This is a wishlist item. The paper's scope is demonstrating that the full recipe (quality images + photography annotations + time-aware loss) works; dissecting the annotation component is a follow-up direction, not a missing experiment that invalidates the contribution.

- **"The constant-weight setting likely used a poorly chosen weight"** — Speculative. The ablation shows a clear trend (time-aware > constant > none), which is informative even if the constant weight was suboptimal.

- **"Formatting nitpicks and typos"** — Parser artifacts, not author errors.

## Novel Insights

The reviews surface a tension that the paper itself does not address: AuthFace achieves best perceptual quality (MANIQA, MUSIQ, CLIPIQA) and LPIPS yet has markedly worse FID than SUPIR. This suggests the method excels at per-instance detail recovery but may reduce output diversity or introduce a systematic bias toward the fine-tuning dataset's face distribution. Whether this trade-off is inherent to the quality-first fine-tuning strategy (small, homogeneous dataset) or to the loss design is an open question that would benefit from explicit analysis. The missing identity metric is the most critical blind spot — if identity similarity turns out to be competitive, the paper's claims are solid; if not, the "authentic" framing is misleading.

## Suggestions

1. **Add identity preservation evaluation as a new table.** Compute ArcFace cosine similarity between restored and reference high-quality images on CelebA-Test (full-frame and face-cropped). On LFW-Test (which has multiple images per identity), compute identity similarity between the restored output and a high-quality reference of the same person. Compare against all baselines in Table 1. This is the single most important addition to substantiate the "authentic" claim.

2. **Specify m and s values** and add one or two alternative weighting schemes to the ablation (e.g., uniform over t ∈ [300, 700] or a Gaussian centered at the midpoint). Show that the logit-normal form is measurably better.

3. **Add FID and LPIPS to the ablation table** (Table 2) so readers can trace which component affects which metric.

4. **Add a brief discussion of the FID gap** — e.g., whether the fine-tuned prior reduces diversity, or whether the method trades distributional fidelity for per-instance detail.

## Score and Decision

**Overall assessment**: The paper presents a well-motivated approach with visually compelling results and strong quantitative performance on most perceptual metrics. The face-oriented fine-tuning recipe is clever and the time-aware loss is a sensible innovation. The main weakness — absence of identity preservation evaluation — is a genuine gap but does not invalidate the paper's other contributions (perceptual quality, artifact reduction). With reasonable rebuttal evidence on identity similarity and a few clarifications, the paper would be a solid contribution to the field.

**Originality**: Good — fine-tuning T2I priors for BFR is relatively new and the specific recipe (tiny HQ dataset + photography annotations + time-aware loss) is novel.

**Importance**: High — blind face restoration is a practical problem and improving perceptual quality matters.

**Claims support**: Partially — perceptual quality claims are well supported; "authentic" claim is incomplete without identity evaluation.

**Soundness**: Generally sound experiments but with noted gaps (missing identity metric, FID not discussed, limited loss ablation).

**Clarity**: Clear writing and well-structured.

**Value**: Positive — the qualitative improvements are real and the dataset is a useful resource.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>