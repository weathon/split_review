Now I have verified all claims against the paper. Let me construct the final review.

---

## Summary

This paper investigates whether the inductive bias of *locality* (the notion that neighboring pixels are more related than distant ones) is necessary for vision Transformers. The authors propose Pixel Transformer (PiT), which treats each individual pixel as a token with learned position embeddings — thereby completely removing locality. Across supervised classification (CIFAR-100, ImageNet at reduced resolution), self-supervised MAE pre-training, and image generation with DiT, PiT matches or outperforms patch-based ViT baselines of identical configuration. The paper's key analytical contribution is the juxtaposition of two scaling trends (fixed sequence length vs. fixed input size), which clarifies that the benefit of pixel-level tokens stems from increased resolution/sequence length rather than locality removal *per se*. The paper concludes that locality is not a necessary inductive bias for vision models.

## Strengths

1. **Genuinely thought-provoking finding supported across multiple tasks.** PiT outperforms equivalent ViT baselines in supervised classification (e.g., PiT-S 86.4% vs ViT-S 83.7% on CIFAR-100, Table 1a), self-supervised MAE fine-tuning (PiT-S 87.7% vs ViT-S 87.4%, Table 2b), and image generation (PiT-L FID 4.05 vs DiT-L/2 4.16, Table 3). This breadth across three distinct tasks — with different architectures (plain ViT vs. modulated DiT) and input representations (raw pixels vs. VQGAN latents) — provides substantial evidence that locality is not required for reasonable vision performance.

2. **Insightful dissection of two contradictory scaling trends.** The paper's analysis of the fixed-sequence-length trend (Figure 2a) vs. fixed-input-size trend (Figure 2b) is the paper's strongest intellectual contribution. It resolves an apparent tension with prior work (where larger patches with fixed token count seemed preferable) by showing that when input resolution is held constant, smaller patches (including pixel-level) monotonically improve accuracy. This analysis meaningfully advances the community's understanding of the relationship between patch size, sequence length, and input resolution.

3. **Ablation isolating patchification as the dominant locality mechanism.** By comparing the minor accuracy drop from removing position embeddings (1.5%) against the severe drop from pixel permutation (25.2% at 25K swaps), the paper convincingly shows that patchification imposes a much stronger locality prior. This motivates why removing patchification entirely (as PiT does) is a well-chosen test of locality's necessity. The paper also insightfully notes that the permutation experiment harms translation equivariance, identifying this as a remaining necessary inductive bias — a valuable nuance.

4. **Transparent self-awareness of limitations.** The paper explicitly acknowledges its computational constraints, the limited resolution of its experiments, and the fact that PiT is more an investigative tool than a practical method. This candor helps calibrate reader expectations.

## Weaknesses

### Fatal
None.

### Major

1. **Central claim is overstated relative to the evidence.** The paper's abstract and conclusion assert that "locality is not a necessary inductive bias" (line 39) and "locality is not fundamental" (line 398). However, the paper's own trend analysis (Figure 2a) shows that when the token budget is fixed, PiT is *worst* — locality helps under token constraints. The actual finding is more nuanced: *locality can be replaced by sufficiently many tokens when the input resolution is fixed, but remains beneficial when tokens are scarce.* The paper's detailed discussion in Section 3 (lines 208–213) articulates this nuance well, but this careful framing is absent from the abstract and conclusion, which make a stronger, less qualified claim. This mismatch between the paper's nuanced analysis and its headline message reduces its scientific precision.

2. **All evaluations on natural images are at very low resolutions.** CIFAR-100 experiments use the native 32×32; ImageNet experiments use 28×28 (line 183). While the paper is transparent about computational constraints (line 125), this directly limits confidence in whether the finding generalizes to standard 224×224 images. The fixed-input-size trend (Figure 2b) is only demonstrated at 28×28, and the claim is intended to apply broadly to vision architectures. Without at least one small-scale demonstration at a more representative resolution — even with a reduced-capacity PiT — the finding remains suggestive rather than conclusive. This is a meaningful scope gap, not a minor one, given the paper's strong general claim about the necessity of locality.

### Minor

1. **No error bars or multiple-seed reporting.** Performance differences in several comparisons are small (e.g., PiT-S vs ViT-S with MAE: 87.7% vs 87.4%). Single-run results leave it unclear whether these differences are reliable. Adding standard deviations over at least 3 runs would strengthen confidence.

2. **Pixel-permutation experiment conflates locality destruction with loss of translation equivariance.** The paper correctly notes (line 357) that pixel permutation damages both locality and translation equivariance, but does not attempt to disentangle them. The conclusion that "patchification is much more crucial" (line 355) is sound, but the experiment does not cleanly isolate locality's role. A complementary experiment shuffling pixels *within* PiT (where translation equivariance is preserved by weight sharing, but locality is already absent) would more directly test whether the learned position embeddings encode spatial structure — as the harsh critic notes.

3. **No efficiency or wall-clock comparison.** The paper mentions PiT's computational cost qualitatively but does not report actual training/inference times vs. ViT. Even rough numbers would help readers calibrate the practicality trade-off.

### Trivial
None.

## Nice-to-Haves

- **Visualize learned position embeddings** (e.g., via PCA or pairwise similarity) to check whether they recover 2D spatial structure after training, which would illuminate whether the network is truly "locality-free" in a meaningful sense.
- **A single small-scale experiment at 224×224** (e.g., PiT-T with FlashAttention on a subset or with reduced channels) to probe whether the fixed-input-size trend extends to standard resolutions.
- **Pixel-permutation experiment on PiT itself** to isolate the role of learned position embeddings vs. spatial structure in the pixel ordering.

## Removed Points

The following criticisms from the harsh reviewer were assessed against the actual paper and removed:

- **"ViT with 2×2 patches as baseline is nonstandard."** The paper uses 2×2 patches because at 28×28/32×32 input sizes, 16×16 patches would yield only 1–4 tokens — meaningless for a ViT. The paper also uses the standard ViT-B/16 (16×16 patches, 224×224) in Section 5 (line 337). The baseline choice is well-justified and the criticism reflects a mismatch between the reviewer's expectations and the paper's controlled experimental design.

- **"Absolute performance on CIFAR-100 is modest."** The paper does not claim state-of-the-art results. Its value lies in the controlled comparison between PiT and ViT of identical configuration. The paper explicitly notes (line 206) that results are "significantly lower than the state-of-the-art" due to low resolution. This criticism imposes an irrelevant standard.

## Novel Insights

The reviews surface one genuinely novel insight beyond the paper's own contributions: the tension between the paper's nuanced trend analysis and its bold headline claim highlights a recurring pattern in empirical ML papers — the "strong claim vs. careful evidence" gap. The paper's trend analysis (Figures 2a/2b) actually tells a more interesting and precise story than the abstract does: that locality is a capacity-efficiency trade-off, not a fundamental requirement. Reframing the paper's contribution around this trade-off (rather than the binary "locality is/is not necessary") would make it both more accurate and more useful to future architecture design. The suggestion to run a permutation experiment on PiT itself (to isolate what the learned position embeddings capture) is also a genuinely good idea that would cleanly separate two confounded variables in the current design.

## Suggestions

1. **Revise the abstract and conclusion** to match the paper's own nuanced analysis. Replace "locality is not necessary" with a more precise framing such as: *"When the token budget is sufficient, locality can be entirely replaced by learned position embeddings without loss of performance; locality becomes beneficial primarily when tokens are scarce."* This is closer to what the evidence actually shows and does not weaken the paper's novelty — it makes the claim more credible.

2. **Add a single controlled experiment at a higher resolution** (e.g., 64×64 or 112×112) with a tiny PiT variant to probe whether the fixed-input-size trend extrapolates beyond 28×28. Even a small-scale demonstration would substantially increase the impact and generalizability of the core claim.

3. **Report standard deviations** over multiple seeds for the main comparisons, especially those with small performance gaps (e.g., Table 2b).

4. **Add a supplementary experiment**: train PiT on a fixed random permutation of pixels (applied identically to all images) and compare with the original PiT. This would disentangle whether PiT's success relies on the learned position embeddings encoding spatial structure or whether the model is genuinely operating on a permutation-invariant set.

## Score and Decision

This paper presents a genuinely interesting investigation into an important question about inductive biases in vision models. Its key analytical contribution — the two trends in Figures 2a/2b — is insightful and useful to the community. The empirical evidence across three tasks is substantial for a finding paper operating under computational constraints. However, the central claim is overstated given the confound between token count and locality removal, and the low-resolution setting limits generalization confidence. The paper would benefit significantly from more precise framing and one higher-resolution demonstration. The strengths justify acceptance as an empirical investigation; the weaknesses are addressable in revision.

**MY FINAL SCORE:** <pineapple>6.0</pineapple>
**MY FINAL DECISION:** <orange>Accept</orange>