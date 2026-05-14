Now I have all the information needed to write the consolidated review. Let me compose it.

---

## Summary

This paper proposes VQ-Transplant, a framework that decouples VQ module development from the expensive end-to-end training of visual tokenizers. The approach replaces the native VQ module in a frozen pre-trained tokenizer (primarily VAR) with a new quantization algorithm, then performs lightweight decoder adaptation (5 epochs on ImageNet-1k) to resolve decoder-quantizer mismatch. The paper also introduces MMD-VQ, a distribution-aligned quantization method using maximum mean discrepancy. The framework is evaluated across multiple VQ algorithms, codebook sizes, and datasets.

## Strengths

- **Genuine practical value**: The framework addresses a real bottleneck in VQ research—the prohibitive cost of end-to-end tokenizer retraining—with a pragmatic reuse strategy. Table 6 provides a clean comparison: on the same ImageNet-1k dataset, VQ-Transplant achieves rFID 0.81 in 22 GPU-hours versus from-scratch training's rFID 1.26 in 25–35 GPU-hours, confirming the efficiency advantage on equal footing.

- **Comprehensive VQ algorithm evaluation**: Five distinct quantization algorithms (Vanilla, EMA, Online, Wasserstein, MMD) are evaluated across both multi-scale (Table 3) and fixed-scale (Table 7) configurations, with consistent results showing that distribution-aligned VQ methods (MMD, Wasserstein) outperform alternatives after adaptation.

- **Well-motivated MMD-VQ with controlled synthetic validation**: Appendix B's controlled experiments on synthetic bimodal distributions clearly demonstrate MMD-VQ's advantage over Wasserstein VQ under non-Gaussianity. At ζ=4.0, MMD-VQ maintains 75.6% codebook utilization vs. Wasserstein VQ's 34.8% and lower quantization error (1.240 vs. 1.502). The paper honestly acknowledges that on standard benchmarks, where features are approximately Gaussian, the two methods perform similarly—this intellectual honesty strengthens the contribution.

- **Cross-dataset generalization demonstrated**: The framework generalizes to datasets structurally distinct from the VAR pre-training data, achieving rFID 1.21 on FFHQ and rFID 2.60 on CelebA-HQ (Tables 8–9), outperforming published baselines trained from scratch.

- **Thorough adaptation analysis**: Tables 4–5 track rFID improvement across individual adaptation epochs and extend to 20 epochs, with Figure 3 showing clear downward trends. The joint optimization alternative in Appendix C (Table 14) provides additional design-space exploration.

## Weaknesses

### Major

None that are fatal.

### Minor

- **Missing "original VQ + decoder adaptation" baseline**: The paper reports that after adaptation, transplanted VQ modules match or exceed the original VAR tokenizer's reconstruction fidelity (e.g., MMD VAR rFID 0.81 vs. VAR's 0.92). However, there is no control experiment where the original VAR's native VQ module is kept frozen and only the decoder undergoes the identical 5-epoch adaptation protocol. This makes it impossible to determine how much of the reported improvement stems from the new VQ algorithm versus simply from the additional adversarial fine-tuning of the decoder. The paper does show that substitution without adaptation degrades performance (Table 3: MMD VAR rFID 1.52 vs. VAR's 0.92), confirming that adaptation is necessary after transplant—but the missing baseline would clarify whether the VQ module itself contributes meaningful gains over the original. This weakens the paper's claim about the superiority of transplanted VQ modules specifically, though it does not undermine the framework's value proposition (cheap VQ experimentation).

- **Efficiency comparison in Table 1 conflates dataset sizes**: The abstract and Table 1 claim a 21.8× speedup and 95% cost reduction by comparing VQ-Transplant on ImageNet-1k (1.2M images, 2×A100, 22h) against VAR from-scratch training on OpenImages (~9M images, 16×A100, 60h). This is not a like-for-like comparison since OpenImages is roughly 7.5× larger than ImageNet-1k. Table 6 provides the fair comparison (same dataset, comparable GPU-hours) and still shows a clear advantage, but the prominently featured 21.8× figure is misleading as stated.

- **"Plug-and-play" generality claim is supported only on VAR**: The abstract states the framework enables "plug-and-play integration of arbitrary VQ algorithms into pre-trained visual tokenizers," but the primary evaluation uses only the VAR tokenizer. The LDM-16 experiment in Appendix D (Table 16) achieves substantially worse results (rFID 2.68–2.93 after adaptation vs. 0.87 for the continuous original), which the paper attributes to the LDM decoder being pre-trained on continuous rather than quantized features. The paper does acknowledge this limitation in Appendix D, but the abstract's unqualified language overpromises relative to the evidence.

### Trivial

- No dedicated limitations section in the main paper body. Key limitations (LDM-16 performance gap) are discussed only in the appendix. A brief limitations paragraph in the main text would improve transparency and help readers calibrate expectations.

## Nice-to-Haves

- **Downstream generation evaluation**: Testing the transplanted tokenizers in actual image generation pipelines (e.g., using VAR or LlamaGen generators) would significantly strengthen the practical message. Currently, only reconstruction quality is evaluated.

- **Broader tokenizer architecture testing**: Beyond VAR and LDM-16, testing on VQGAN or other tokenizer families would better support the generality claim.

- **Ablation isolating Stage I vs. Stage II contributions**: A clean 2×2 ablation (original VQ ± adaptation, new VQ ± adaptation) would clearly disentangle how much each stage contributes.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic claim that the missing baseline makes "the conclusion that the transplanted VQ modules improve reconstruction fidelity unsubstantiated" and that "the paper in its current form does not meet the bar for acceptance."** → **Downgraded from fatal to minor.** The paper's core contribution is the *framework* (transplant + adaptation), not the claim that any individual VQ module is inherently superior. The framework's value is demonstrated by Table 3: substitution alone degrades performance, adaptation recovers and often exceeds original quality. The missing baseline would strengthen the paper but does not invalidate the central contribution. Additionally, the harsh critic's claim that Table 6 is "not directly tied to the key claim" is incorrect—Table 6 directly supports the efficiency claim by showing from-scratch training on the same dataset yields far worse results for similar compute.

- **Harsh Critic claim that the speedup comparison is "methodologically unsupported and potentially inflated" at a fatal level.** → **Downgraded to minor presentation issue.** Table 6 provides the fair comparison the critic demands, and it still shows a clear efficiency advantage (22h for VQ-Transplant achieving rFID 0.81 vs. 25–35h from-scratch achieving only rFID 1.26–1.40). The problem is that Table 1/abstract present a conflated number, not that the efficiency claim is false.

- **Harsh Critic claim that the LDM results make the framework generality claim invalid.** → **Downgraded to minor.** The paper honestly reports and discusses the LDM-16 results in Appendix D, identifying specific reasons (decoder pre-trained on continuous features vs. quantized). The abstract language should be qualified, but this is an overclaim issue, not a methodological flaw.

- **Strength Finder's "95% cost reduction" claim.** → **Removed from strengths.** As noted above, the 95% figure is based on a cross-dataset comparison. The genuine efficiency advantage is better represented by Table 6's same-dataset comparison.

- **Harsh Critic claim that "the novelty relative to existing VQ-loss designs (e.g., Wasserstein VQ) is modest."** → **Removed.** This is a subjective assessment; MMD-VQ's synthetic experiments in Appendix B clearly demonstrate a concrete advantage over Wasserstein VQ under non-Gaussianity that is theoretically motivated and empirically validated.

## Novel Insights

Beyond the paper's own contributions, the cross-dataset results (Section 5.3) reveal an interesting finding that the reviewers collectively highlight: a pre-trained encoder-decoder from a VAR tokenizer, combined only with a transplanted VQ module and minimal decoder adaptation, achieves state-of-the-art reconstruction on structurally distinct datasets like FFHQ and CelebA-HQ. This suggests that the VAR encoder's learned representations transfer surprisingly well across domains, and that the VQ module—rather than the encoder—may be the primary bottleneck in cross-domain generalization for discrete tokenizers. The paper could have made more of this observation.

## Suggestions

1. **Add the original-VQ + decoder adaptation baseline.** Adapt the original VAR tokenizer's decoder for 5 epochs using the exact same recipe (DINO-S discriminator, DiffAug, CR, LeCAM) with the native VQ module frozen. Report rFID, r-IS, LPIPS, PSNR, SSIM. This is a straightforward experiment that would definitively answer whether the new VQ modules provide gains beyond fine-tuning alone.

2. **Qualify the speedup claim.** Replace the 21.8× number in the abstract with the same-dataset comparison from Table 6, or clearly state that the comparison is against the reported cost of training VAR on OpenImages (a larger dataset) and provide the fair ImageNet-1k comparison alongside it.

3. **Add a brief limitations paragraph to the main paper.** Move the key points from Appendix D (LDM-16 results, decoder pre-training requirement) into a short "Limitations" section before the conclusion.

4. **Qualify "plug-and-play" language in the abstract.** Change to something like "plug-and-play integration of new VQ modules into pre-trained discrete visual tokenizers" to accurately reflect the demonstrated scope.

## Score and Decision

### Anchor Comparison

| Anchor | Path | Avg Score | Comparison |
|--------|------|-----------|------------|
| Quantize-then-Rectify (ReVQ) | 6193b311kq.md | 3.50 | Similar concept (pre-trained VAE → VQ-VAE). VQ-Transplant is more comprehensive: tests 5 VQ methods vs. 1, includes cross-dataset generalization, introduces a novel VQ method, and achieves better results. |
| Image Tokenizer Needs Post-Training | RYHzkIqHI4.md | 4.00 | Focused on tokenizer post-training for generation. VQ-Transplant has stronger empirical validation and clearer practical value. |
| WeTok | QteJJF57yG.md | 5.00 | New tokenizer with architectural innovations. Comparable contribution level. WeTok has breakthrough rFID (0.12) but more complex training; VQ-Transplant addresses a different problem (efficiency/reuse) with a simpler approach. |
| VQBridge (FVQ) | juM14y0caI.md | 6.00 | Strong VQ training contribution with downstream generation results and scaling analysis. VQ-Transplant is slightly behind in thoroughness and downstream validation but addresses a complementary problem. |
| Latent Denoising Tokenizer (L-DeTok) | 1jBsi98fVe.md | 6.50 | Well-polished, simple method with comprehensive experiments across 6 generative models. VQ-Transplant is below this level in terms of downstream validation and clarity of claims. |
| CSVQ | b5oUWQ0ObU.md | 2.50 | VQ tokenizer with codebook innovations. VQ-Transplant is substantially stronger in empirical scope and results. |
| HieraTok | zj9Mm4bCAo.md | 3.00 | Multi-scale tokenizer. VQ-Transplant's framework approach and cross-dataset results represent a clearer contribution. |

VQ-Transplant sits between the ReVQ/Image-Tokenizer-Post-Training tier (~3.5–4.0) and the VQBridge/L-DeTok tier (~6.0–6.5). It is clearly stronger than the rejected papers in the 3.0–4.0 range but lacks the downstream validation and claim-discipline of the 6.0+ papers. It is most comparable to WeTok (5.00) in overall contribution quality, though the two papers make different types of contributions. The framework addresses a real practical need, the empirical results are solid, and the MMD-VQ synthetic experiments are well-executed. However, the missing baseline, inflated speedup claims, and overstated generality prevent a higher score.

**Originality:** The framework concept of decoupling VQ from encoder-decoder training is a fresh angle on a known problem. MMD-VQ is a modest but well-motivated extension of distribution-aligned VQ.

**Importance:** The problem—enabling VQ research under resource constraints—is real and practically important. The framework genuinely lowers the barrier to experimenting with new VQ algorithms.

**Claim support:** Claims are mostly well-supported, but the speedup claim conflates datasets and the "plug-and-play" generality is not fully demonstrated. The missing baseline weakens confidence in the VQ-module-specific claims.

**Soundness:** Experimental methodology is generally sound. The synthetic experiments in Appendix B are particularly well-designed. The LDM-16 results are honestly reported. Main weakness is the missing control experiment.

**Clarity:** The paper is well-organized and well-written. Tables are informative and the two-stage framework is clearly diagrammed. A dedicated limitations section would improve clarity.

**Value to community:** The framework has clear practical value for researchers who want to experiment with VQ algorithms but lack the resources to train full tokenizers. The code release further increases value.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>