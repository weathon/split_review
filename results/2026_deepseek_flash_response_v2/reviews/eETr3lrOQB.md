Now I have sufficient data to produce the final review. Let me write it.

## Summary

VQ-Transplant proposes a two-stage framework for plug-and-play replacement of VQ modules in frozen, pre-trained visual tokenizers. The method first substitutes the VQ module while keeping the encoder-decoder frozen, then performs lightweight decoder adaptation (5 epochs on ImageNet-1k) to resolve the distributional mismatch. Experiments on the VAR tokenizer with five VQ algorithms show the framework can surpass the original model's reconstruction fidelity (0.81 vs 0.92 r-FID) while requiring only 44 GPU-hours versus 960 GPU-hours for full retraining. The paper also introduces MMD-VQ, a distribution-aligning VQ method using maximum mean discrepancy.

## Strengths

1. **Well-structured empirical demonstration of the decoder mismatch problem and its resolution.** Tables 3 and 7 cleanly show a two-step pattern: (a) after VQ module substitution alone, reconstruction degrades despite lower quantization error, then (b) after just 5 epochs of decoder adaptation, performance recovers and surpasses the original model. This systematic ablation — tracking the effect of each stage separately — is the paper's strongest analytical contribution and directly validates the core idea.

2. **Broad evaluation across VQ methods and configurations.** The framework is tested with five VQ algorithms (Vanilla, EMA, Online, Wasserstein, MMD) in both multi-scale (Table 3) and fixed-scale (Table 7) settings. The consistent pattern across all configurations — distribution-aligning methods work best, substitution degrades, adaptation recovers — demonstrates the framework's generality beyond any single VQ method.

3. **Substantial and well-documented efficiency gains.** VQ-Transplant requires 44 GPU-hours (22 hours on 2×A100) vs 960 GPU-hours for VAR from scratch (60 hours on 16×A100), a 21.8× speedup (Table 1), while improving r-FID from 0.92 to 0.81 (Table 2). This is a genuine reduction in the cost of iterating on VQ methods, enabled by the framework's design.

4. **Cross-dataset generalization demonstrated on three out-of-distribution benchmarks.** Section 5.3 evaluates VQ-Transplant on FFHQ, CelebA-HQ, and LSUN-Churches — datasets structurally distinct from the OpenImages/ImageNet-1k training data. The results achieve competitive or state-of-the-art r-FID against fully-trained baselines (e.g., r-FID 1.21 on FFHQ vs VQGAN-LC's 3.81 in Table 8).

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **MMD-VQ and Wasserstein VQ are empirically indistinguishable, weakening the secondary contribution.** Across all experiments, the two methods produce near-identical results with differences of 0.01–0.06 r-FID, and neither consistently outperforms the other (e.g., on FFHQ, Wasserstein VQ achieves 1.21 r-FID vs MMD VQ's 1.37; on CelebA-HQ, MMD VQ achieves 2.60 vs Wasserstein's 3.02). The paper's theoretical motivation for MMD-VQ (non-parametric, handles non-Gaussian features) is not backed by any experiment showing a setting where this advantage materializes. Since MMD-VQ is presented as a contribution (Section 4.2, contributions list), the lack of empirical differentiation is a gap. This does not affect the primary VQ-Transplant framework claim, but the paper should either demonstrate MMD's advantage or temper the associated claims.

2. **Cross-dataset evaluation (Tables 8–10) omits a key control.** The original frozen VAR tokenizer (with its native VQ module) evaluated directly on FFHQ, CelebA-HQ, and LSUN-Churches is not reported. Without this baseline, it is unclear whether the strong cross-dataset results are attributable to VQ-Transplant's adaptation or to the inherent robustness of the pre-trained VAR backbone. This comparison would isolate the added value of the transplant process.

3. **No uncertainty estimates reported.** The paper reports no confidence intervals, standard deviations, or significance tests for any metric. Given that the differences between methods are often small (e.g., 0.02 r-FID between Wasserstein and MMD VAR at K=4096 in Table 3) and adversarial training is known to be unstable, the reader cannot distinguish systematic improvement from stochastic variation. While this is standard practice in the visual tokenizer subfield, it remains a limitation that should be acknowledged.

4. **The "95% training cost reduction" framing conflates regimes.** The headline figure compares VQ-Transplant's integration cost (44 GPU-hours) against training VAR from scratch (960 GPU-hours). This is technically correct for a researcher who has the pre-trained backbone (which the paper states will be released), but an unwary reader could interpret this as "95% of all costs" including obtaining the pre-trained model. The paper is transparent about what is being compared, but the framing could be more precise.

### Trivial

- The from-scratch training comparison in Table 6 trains MMD VAR for only 5–7 epochs while the paper itself acknowledges tokenizers "typically require hundreds of epochs." This comparison has limited informativeness, though the paper is transparent about the caveat.

## Nice-to-Haves

- An analysis of why distribution-aligning VQ methods are more compatible with VQ-Transplant than alternatives (e.g., latent space geometry before/after substitution).
- A comparison against a simple baseline of fine-tuning the original VQ module with additional training, which would test whether the improvement is due to the new VQ method or simply more training.
- Evaluation on at least one non-VAR tokenizer backbone beyond the brief LDM-16 experiment in the appendix.

## Removed Points

- The claim that the "95% cost reduction" claim is a "structural" issue that "invalidates the headline efficiency claim" was downgraded to a Minor framing concern. The paper is transparent about comparing integration cost to full retraining cost, and the pre-trained backbone is released with the code.
- The claim that MMD-VQ's contribution is "not supported by evidence" was downgraded from "structural" to Minor. The paper's "superior reconstruction fidelity" claim is explicitly relative to vanilla VAR (not Wasserstein), and the theoretical motivation for MMD is genuine. The weakness is that the theoretical advantage is not empirically demonstrated.
- The claim that the from-scratch comparison in Table 6 is a "straw-man" was removed. The paper transparently acknowledges that from-scratch tokenizers need hundreds of epochs and only claims that VQ-Transplant is better in the same time budget — a legitimate comparison point.
- The claim that "5 epochs" is undermined by 20-epoch results was removed. The paper explicitly presents both results and notes the trade-off. The 5-epoch recipe still achieves the main claimed result (surpassing the original VAR tokenizer).
- Various formatting/style nitpicks were removed per instructions.
- Generic "no discussion of limitations" was removed; the paper's scoping is clear and the absence of a limitations paragraph is not a substantive weakness.

## Novel Insights

None beyond the paper's own contributions. The key empirical finding — that VQ module substitution causes a decoder mismatch that can be fixed with lightweight decoder adaptation, and that distribution-aligning VQ methods are the best suited for this — is the paper's own contribution and is well-demonstrated.

## Suggestions

- Add the original VAR tokenizer's performance on FFHQ, CelebA-HQ, and LSUN-Churches as a baseline in Tables 8–10.
- Report confidence intervals or standard deviations for at least the main r-FID comparisons (Tables 3 and 7).
- Either demonstrate a setting where MMD-VQ's non-parametric advantage over Wasserstein VQ materializes (e.g., with intentionally non-Gaussian feature distributions), or reframe MMD-VQ as "another distribution-aligning VQ method" rather than a novel contribution.
- Clarify the "95% cost reduction" framing to explicitly state that this saving is on the VQ integration step given a pre-trained backbone.

---

## Score Calibration Report

**Round 1 (Bracketing):** Searched for visual tokenization / VQ papers in three score bands.

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Low | IqGVIU4rvM.md (VQ-VAE + Diffusion Tokenizers) | 2.50 | R1 | Rejected; fundamental flaws, poor methodology. Clearly weaker than VQ-Transplant. |
| Low | YGWxpOI6Y0.md (VideoGPT+) | 3.40 | R1 | Rejected; limited VQ contribution. Weaker than VQ-Transplant. |
| Low | HfJxXbXlYJ.md (LLM2CLIP) | 3.00 | R1 | Rejected; unrelated to VQ. |
| Medium | yGnsH3gQ6U.md (Binary Spherical Quantization) | 5.75 | R1, R2 | Accepted; proposes novel BSQ method. Similar quality, slightly more novel quantization method but VQ-Transplant has cleaner experimental design. VQ-Transplant is comparable. |
| Medium | 0Nui91LBQS.md (SEED Tokenizer) | 6.33 | R1, R3 | Accepted; broader LLM-focused scope. More ambitious but with notable weaknesses. VQ-Transplant is focused and cleaner but narrower. |
| Medium | 3TnLGGHhNx.md (BPE Image Tokenizer) | 6.00 | R1, R2 | Accepted; split reviews (5,5,8). "Far behind SOTA" weakness more severe than any VQ-Transplant weakness. VQ-Transplant is stronger. |
| Medium | FlvtjAB0gl.md (Unified Language-Vision) | 6.25 | R1, R2 | Accepted; LLM-focused tokenization. Different sub-area. |
| Medium | mb2ryuZ3wz.md (Variable-length tokenizer) | 5.75 | R2 | Accepted; innovative idea but limited scaling. Similar tier to VQ-Transplant. |
| Medium | iqqpx8hgSQ.md (RAQ-VAE) | 5.50 | R2 | Rejected; unclear novelty, weak validation. VQ-Transplant is stronger. |
| High | GMwRl2e9Y1.md (Rotation Trick for VQ) | 8.00 | R1 | Strong accept; genuinely novel VQ contribution. Clearly stronger than VQ-Transplant. |

**Round 1 bracket:** 4.5 – 6.5 (the paper is clearly above the ~3.0 low anchors and well below the ~8.0 high anchors).

**Round 2 (Narrowing):** Searched within (4.5, 6.5), (5.5, 7.0), and (5.0, 6.5) to find more precise comparisons.

**Final score positioning:** VQ-Transplant is stronger than RAQ-VAE (5.50, Reject) and the BPE Tokenizer (6.00, Accept) which was described as "far behind SOTA" — a more serious weakness than any in VQ-Transplant. It is comparable to BSQ (5.75, Accept) and the variable-length tokenizer (5.75, Accept), though those papers have more technically novel core methods. VQ-Transplant's strengths are its focused scope, clean experimental validation, and genuine efficiency gains. Its main weakness is the weak secondary contribution (MMD-VQ) and missing controls.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>