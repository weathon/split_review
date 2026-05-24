Now I have a clear picture from the calibration. Let me synthesize everything into the final consolidated review.

## Final Review

Based on my analysis of the paper and the calibration anchors, here is my bracketing:
- **Round 1 bracket**: Between 3.5 and 7.5 (mid-range)
- **Round 2 anchors**: VQBridge (6.0), WeTok (5.0), AlignTok (4.5), RepTok (6.0), Image Tokenizer Post-Training (4.0)
- The paper is stronger than align-and-fine-tune papers at 4.0-4.5 but weaker than tightly-controlled VQ papers at 6.0. This places it around **5.0**.

Let me now write the review.

---

## Summary

This paper proposes VQ-Transplant, a framework that enables plug-and-play replacement of VQ modules in pre-trained visual tokenizers (specifically VAR) without end-to-end retraining. By freezing the encoder-decoder and only substituting the VQ module plus a lightweight 5-epoch decoder adaptation, the method achieves 21.8× training speedup over full VAR training while improving reconstruction fidelity (0.81 rFID vs 0.92 rFID). The paper also introduces MMD-VQ, a distribution-aligned VQ method using maximum mean discrepancy. Experiments span five VQ methods, multi-scale and fixed-scale settings, and cross-dataset generalization.

## Strengths

- **Novel and practically motivated framework.** Decoupling VQ module development from full tokenizer training is a clean, useful idea that directly addresses a real bottleneck. The paper correctly identifies that adversarial training of full encoder-decoder architectures is prohibitively expensive for most researchers, and VQ-Transplant offers a concrete path forward.

- **Comprehensive evaluation across VQ methods.** Tables 3 and 7 evaluate five quantization algorithms (Vanilla, EMA, Online, Wasserstein, MMD) in both multi-scale and fixed-scale configurations, demonstrating the framework's generality. The consistent finding that distribution-alignment methods (Wasserstein, MMD) transfer better is a genuine insight.

- **Convincing from-scratch comparison (Table 6).** When VQ-Transplant is compared against training the same MMD VAR architecture from scratch on the same dataset (ImageNet-1k) for comparable or longer GPU time, VQ-Transplant achieves substantially better rFID (0.91 vs 1.40-1.34 for K=4096). This directly supports the claim that retaining the pre-trained encoder-decoder is critical.

- **Cross-dataset generalization.** Tables 8-10 show strong reconstruction on FFHQ (rFID 1.21), CelebA-HQ (2.60), and LSUN-Churches (1.79) using the same ImageNet-adapted decoder, validating that the approach extends beyond the training distribution.

- **Detailed ablation on adaptation length.** Table 5 and Figure 3 track rFID improvement from 5 to 20 epochs, showing continued improvement (0.91→0.79 for K=4096, 0.81→0.74 for K=8192), which gives practical guidance for the cost-quality trade-off.

## Weaknesses

### Major

- **Dataset confound in the primary comparison against VAR.** The headline claim (VQ-Transplant achieves 0.81 rFID vs VAR's 0.92 rFID) compares a model whose decoder was adapted on ImageNet-1k (5 epochs) against a VAR baseline that was trained on OpenImages and evaluated zero-shot on ImageNet-1k. The improvement may partly come from the decoder seeing ImageNet-1k data during adaptation rather than from the VQ module change alone. The paper acknowledges this in Section 5.3 but does not control for it in the main results. A cleaner experiment would retrain the native VAR VQ on ImageNet-1k under comparable compute. Table 6 partially mitigates this (same-dataset comparison of VQ-Transplant vs from-scratch MMD VAR), but the central comparison against the published VAR number (0.92) remains confounded.

- **Headline result uses different codebook size.** The best result of 0.81 rFID uses K=8192, while the VAR baseline uses K=4096. In the matched comparison (Table 3, both at K=4096 and 680 tokens), MMD VAR achieves 0.91 vs 0.92 — a much smaller gap. The paper does not test whether simply increasing the codebook size in standard VAR training would yield similar improvements. The 0.81 vs 0.92 framing is thus partly attributable to increased codebook capacity rather than the VQ method or transplant framework.

- **Factual error: "ImageNet-1k is a subset of OpenImages"** (Section 5.3). This is incorrect. ImageNet-1k and OpenImages are separate datasets with different image sources and annotations. While this claim is not central to the method, it appears in a section meant to motivate cross-dataset generalization and undermines trust in the paper's understanding of its own experimental setup.

### Minor

- **r-IS arrow direction is reversed.** In Tables 2, 3, and 5, r-IS is marked with ↓ (lower is better), but higher values indicate better reconstruction (e.g., VAR: 198.6, MMD VAR K=8192: 201.0). The paper claims MMD VAR "outperform[s]" VAR on r-IS, which is true if higher is better, but contradicts the arrow direction. Table 7 uses τ-IS↑ (correct direction), adding inconsistency. This is sloppy and reduces confidence in the reported metrics.

- **FFHQ comparison uses different token counts.** Table 8 compares VQ-Transplant (512 tokens) against baselines from the literature that use 256 tokens. The rFID advantage (1.21 vs 3.81) is likely inflated by the 2× token budget. The paper should test at 256 tokens for a fair comparison, or at minimum note this confound explicitly.

- **Selective metric emphasis.** The VAR baseline beats or ties VQ-Transplant on LPIPS (0.100 vs best 0.104), PSNR (24.37 vs 24.37), and SSIM (63.9 vs 63.8) at matched settings (Table 3, K=4096). The paper emphasizes rFID and r-IS where it wins, while downplaying metrics where it does not. Full reporting is good, but the narrative is selective.

- **No error bars or variance estimates.** Multiple tables report single-run numbers. Given the known instability of adversarial GAN training, this is a gap. While 5 VQ methods × multiple codebook sizes provides breadth, readers cannot assess whether differences of 0.01-0.02 rFID are meaningful.

### Trivial

- **Inconsistent notation:** Table 7 uses τ-FID and τ-IS (with correct ↑ for IS) while all other tables use r-FID and r-IS (with incorrect ↓ for IS). The different symbols are never defined.
- The speedup calculation in Table 1 uses vastly different GPU counts (2×100 A100 vs 16×100 A100), making the "21.8×" number dependent on the specific hardware allocation, not just algorithmic efficiency.

## Nice-to-Haves

- **Test VQ-Transplant on the original training set (OpenImages).** Applying the transplant on OpenImages and comparing directly against the published VAR numbers would fully control the dataset confound and make the comparison airtight.
- **Compare at matched codebook size K=4096 for headline results.** The current headline (0.81 at K=8192 vs 0.92 at K=4096) mixes variables. Showing K=4096→K=8192 scaling for native VAR VQ would isolate the codebook size effect.
- **Error bars or multiple seeds** for the main experiment, especially given adversarial training's variability.
- **Analysis of when VQ-Transplant fails.** Are there VQ methods where decoder adaptation cannot recover performance? Characterizing failure modes would strengthen the framework's contribution.

## Removed Points

These points from the reviews are flagged to be removed — treat them with caution:

- **"95% cost reduction lacks baseline"** — The critic requests retraining original VAR on ImageNet-1k as the baseline for the cost claim. Table 6 already shows VQ-Transplant vs from-scratch training of the same architecture on the same data, which is the relevant controlled baseline for the cost reduction claim. The missing baseline (retraining native VAR on ImageNet-1k) is a different experiment that would be nice but is not required to support the cost claim.
- **"Missing analysis of what is lost in Stage I"** — The paper analyzes this in detail (Section 5.1): substitution alone yields quantization error improvement but worse rFID, demonstrating decoder-quantization mismatch. The analysis is present and clear.
- **"Stage II decoder adaptation uses same techniques as full VAR training"** — This is correct but the paper explicitly quantifies the cost (22 hours total on 2× A100 vs 60 hours on 16× A100), demonstrating that "lightweight" is justified by compute numbers, not by architectural difference.
- **Strength Finder claims about "21.8× speedup"** — This is real but the comparison uses different hardware configurations (2× vs 16× GPU), so the exact multiplier depends on hardware allocation efficiency; the claim is directionally correct but the precise factor should be read with this caveat.

## Novel Insights

The harsh critic's observation that **distribution-alignment VQ methods (Wasserstein, MMD) consistently transfer better under VQ-Transplant** is not just a finding the paper already makes — it is actually an insight that receives relatively little analytical depth in the paper itself. The paper reports this pattern (Tables 3 and 7) but mostly uses it to justify MMD-VQ's design. The deeper implication is interesting: VQ methods that minimize distributional mismatch between features and codebook also minimize the downstream decoder-quantization gap, suggesting that the compatibility of a VQ module with a pre-trained decoder is related to how much the quantized distribution preserves the original latent geometry. This connection between "good VQ properties" and "transferability" is underexplored in the paper and could be a direction for future work.

## Suggestions

1. **Control for the dataset confound** by retraining the native VAR VQ (or applying VQ-Transplant with the native VQ module) on ImageNet-1k for 5 epochs and reporting the result. This would directly show whether the improvement is from the data or the method.
2. **Present the matched-codebook-size comparison (K=4096, 680 tokens) as the primary result** and frame the K=8192 result as a complementary scaling study. This would avoid the uncontrolled-variable criticism.
3. **Fix the r-IS arrow direction** (change ↓ to ↑ in Tables 2, 3, 5) and harmonize the notation between tables.
4. **Add a note** acknowledging the FFHQ token count confound, or provide a 256-token comparison.
5. **Correct the "ImageNet-1k is a subset of OpenImages" error** in Section 5.3.

## Score and Decision

**Calibration Anchors:**
| Paper | Avg Score | Round | Comparison to this paper |
|-------|-----------|-------|--------------------------|
| VQBridge (juM14y0caI) | 6.0 | R1/R2 | Stronger controlled experiments and ablation rigor; this paper has more novel framework idea but weaker controls |
| WeTok (QteJJF57yG) | 5.0 | R2 | Similar evaluation issues (comparison fairness); comparable scope of experiments |
| AlignTok (ajnBafpqmE) | 4.5 | R2 | Shares "freeze encoder, adapt decoder" spirit; this paper has broader VQ method coverage |
| RepTok (0b6a2SE23v) | 6.0 | R2 | Stronger in novelty and clean evaluation; this paper lacks RepTok's experimental precision |
| Image Tokenizer Post-Training (RYHzkIqHI4) | 4.0 | R1/R2 | This paper has a cleaner framework and stronger results |
| MATT (IyV1QEc95F) | 4.5 | R1 | Different domain but similar module-replacement concept; this paper has better experiments |

The paper has a genuine contribution (decoupling VQ development from full tokenizer training) and broad experimentation, but the evaluation contains confounds that prevent its strongest claims from being convincingly supported. It sits between the tighter VQ papers at 6.0 and the weaker post-training papers at 4.0-4.5, closer to the 5.0 anchor (WeTok) which has a similar profile of a good idea with some comparison fairness issues.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>