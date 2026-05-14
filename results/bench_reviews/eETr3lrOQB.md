Now I have a thorough understanding of the paper and calibration anchors. Let me write the consolidated review.

---

## Summary

VQ-Transplant proposes a framework for plug-and-play replacement of vector quantization (VQ) modules within pre-trained visual tokenizers. Instead of costly end-to-end retraining, the method substitutes the VQ module (Stage I), then adapts only the decoder for ~5 epochs (Stage II) to resolve the distribution mismatch between the new quantized space and the frozen decoder. The paper also introduces MMD-VQ, a VQ method using maximum mean discrepancy for distribution alignment. The framework achieves a 21.8× training speedup over the original VAR tokenizer while matching or exceeding its reconstruction fidelity (rFID 0.81 vs. 0.92) on ImageNet-1k.

## Strengths

- **Concrete, quantified efficiency gains**: Table 1 shows VQ-Transplant requires 22 GPU hours on 2× A100s vs. 60 hours on 16× A100s for the original VAR tokenizer — a 21.8× speedup. This directly supports the central claim of democratizing VQ research by dramatically lowering computational barriers.

- **Convincing internal evidence for the framework's mechanism**: Table 3 cleanly demonstrates the two-stage logic: VQ substitution alone degrades rFID (MMD VAR drops from 0.92 to 1.52 with K=4096), and decoder adaptation recovers it (0.91), confirming that decoder adaptation specifically addresses the substitution-induced mismatch rather than serving as generic fine-tuning.

- **Comprehensive VQ algorithm coverage**: The paper evaluates five distinct VQ algorithms (Vanilla, EMA, Online, Wasserstein, MMD) across both multi-scale and fixed-scale configurations, providing broad validation that VQ-Transplant works as a general framework rather than being tuned to one specific quantization method.

- **Well-designed synthetic experiments for MMD-VQ**: Appendix B uses a controlled bimodal Gaussian mixture distribution (varying separation ζ) to cleanly demonstrate MMD-VQ's advantage over Wasserstein VQ under non-Gaussianity, with codebook utilization dropping to 34.8% for Wasserstein vs. 75.6% for MMD at ζ=4.0.

## Weaknesses

### Fatal

None.

### Major

- **Missing decoder-only fine-tuning baseline for cross-dataset experiments**: Section 5.3 evaluates VQ-Transplant on FFHQ, CelebA-HQ, and LSUN-Churches, attributing strong reconstruction to the framework. However, since the original VAR tokenizer was trained on OpenImages (not these datasets), some portion of the gains may be attributable to simple decoder domain adaptation rather than VQ module replacement. Comparing against fine-tuning the original VAR decoder alone on each target dataset would cleanly isolate the contribution of VQ module substitution for cross-domain transfer. This does not threaten the core framework contribution (which is about enabling cheap VQ iteration), but it weakens the specific claim of cross-dataset generalization.

### Minor

- **MMD-VQ's practical advantage is marginal on current benchmarks**: The paper itself acknowledges (lines 1338-1341, Appendix B) that real-world encoder features are approximately Gaussian, making Wasserstein VQ sufficient, and MMD-VQ's advantage only materializes under non-Gaussianity. On ImageNet-1k, MMD VAR (rFID 0.81) marginally edges out what Wasserstein VAR achieves (rFID 0.83, Table 3). MMD-VQ is presented as a secondary contribution, but its practical value over Wasserstein VQ in current settings is slim. This does not undermine the paper but limits the impact of the secondary contribution.

- **Design choice of decoder-only vs. joint optimization is deferred to appendix**: The main text presents decoder-only adaptation as the primary approach, but Appendix C (Table 14) shows joint optimization yields slightly better results (e.g., MMD VAR rFID 0.87 vs. 0.91 for decoder-only with K=4096). The rationale for presenting decoder-only as the default is efficiency, which is reasonable given the paper's goals, but this trade-off discussion belongs in the main text rather than being relegated entirely to the appendix.

- **Fixed-scale VQ integration into multi-scale VAR could be more precisely specified**: Section 5 describes splitting 32-dim features into two 16-dim sub-vectors with parallel quantization, but the description of how these fixed-scale quantized features interface with VAR's multi-scale decoder architecture (which expects features at multiple resolutions) is brief. This does not prevent understanding but complicates exact reproduction.

### Trivial

- Quantization error (E) and codebook utilization (U) are used throughout tables but never receive a formal inline definition in the main text — they are only described informally in the Evaluation Metrics paragraph (Section 5).

## Nice-to-Haves

- A controlled experiment probing *why* the decoder-quantization mismatch occurs (e.g., measuring distributional distances between the original and new quantized latent spaces at different decoder layers) would strengthen the mechanistic understanding beyond the current empirical demonstration that adaptation works.

- Extending the decoder-only fine-tune baseline comparison (mentioned under Major Weaknesses) to all datasets would allow the cross-dataset results to be presented with stronger attribution.

- Comparing MMD-VQ head-to-head against Wasserstein VQ within the VQ-Transplant framework in a dedicated ablation (e.g., varying codebook sizes, adaptation epochs) would clarify when MMD-VQ is actually worth the additional complexity over the simpler Wasserstein approach.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **"Missing baseline that could explain the main result" (Harsh Critic point 1)**: The harsh critic claimed the paper cannot distinguish VQ replacement from decoder-only domain adaptation without a baseline of fine-tuning the original VAR decoder on ImageNet-1k. I have *weakened* and *moved* this concern to the cross-dataset experiments only (see Major Weaknesses). For the ImageNet-1k results, this baseline is less critical: VAR was trained on OpenImages (which contains ImageNet-1k), so ImageNet-1k is largely in-distribution, and the paper's Table 3 already shows that VQ substitution alone *degrades* performance (rFID 1.52) and adaptation recovers it (0.91), demonstrating the adaptation addresses VQ-induced mismatch, not generic domain shift. The core contribution — a framework for cheap VQ iteration — does not depend on this baseline.

- **"The framing that VQ-Transplant 'democratizes quantization research' overstates the contribution" (Harsh Critic, Abstract & Introduction note)**: This is a subjective judgment about rhetorical framing, not a substantive weakness. The paper quantifies a 21.8× cost reduction, which is a legitimate basis for the democratization language.

- **"Table 2 mixes results from different tokenizer architectures" (Harsh Critic, Section 5 note)**: Table 2 clearly labels FS VQ vs. MS VQ and includes citations for all external results. The comparison is transparent about what is being compared.

- **"Table 6 compares VQ-Transplant against from-scratch training... an uninformative straw-man"**: The paper itself acknowledges the expected outcome (lines 621-624) and includes this comparison for completeness. It does not draw strong conclusions from it.

- **"The paper should be more precise about 95% training cost reduction" (Harsh Critic)**: The cost reduction is concretely quantified in Table 1 (22 vs. 60 hours on fewer GPUs). The percentage is accurate arithmetic.

- **"Decoder-only adaptation choice is not justified in the main text" (Harsh Critic)**: The paper states the rationale clearly — preserving frozen encoder parameters and adapting only the decoder. This is the core design of the framework, not an unjustified choice. The trade-off vs. joint optimization is in Appendix C.

- **Strength Finder generic/superficial strengths removed**: "This paper addressed an important problem" and similar generic claims were dropped for lacking concrete evidence anchored in the paper.

- **"The LDM-16 discussion would benefit from a controlled experiment" (Harsh Critic, Appendix D note)**: This is asking the paper to do more than it claims; the LDM-16 experiment is clearly labeled as a compatibility check, not a controlled comparison.

## Novel Insights

The reviews reveal an interesting calibration insight: the core tension in evaluating this paper is whether the decoder adaptation is solving a genuine VQ-substitution mismatch or is simply performing domain-adaptive fine-tuning. The paper's strongest evidence against the latter interpretation is the U-shaped pattern in Table 3 — substitution hurts, adaptation recovers — which would not be expected from pure domain adaptation. However, the paper would benefit from making this argument explicit rather than relying on readers to infer it from the result tables.

## Suggestions

- For the cross-dataset experiments (FFHQ, CelebA-HQ, LSUN-Churches), add a decoder-only fine-tuning baseline of the original VAR tokenizer. This would cleanly isolate the contribution of VQ substitution from domain adaptation, strengthening the cross-dataset generalization claim. Even a single dataset (e.g., FFHQ) would suffice to demonstrate the pattern.

- Move the decoder-only vs. joint optimization trade-off discussion from Appendix C into the main text (even a brief paragraph in Section 4.1), since it directly addresses a natural reader question about why only the decoder is adapted.

- Add a one-sentence formal definition of quantization error E and codebook utilization U in the Evaluation Metrics paragraph of Section 5.

## Score and Decision

**Calibration anchor comparison:**

| Anchor | Avg Score | Comparison to VQ-Transplant |
|--------|-----------|----------------------------|
| LatentBit (`609DXrfkoA`) | 2.50 | Much weaker — unfinished generation results, unclear claims; VQ-Transplant is far more complete. |
| Image Tokenizer Needs Post-Training (`RYHzkIqHI4`) | 4.00 | Weaker — loss complexity issues, limited scope; VQ-Transplant has clearer contribution and more thorough experiments. |
| AlignTok (`ajnBafpqmE`) | 4.50 | Comparable — both propose leveraging pre-trained components for tokenizer efficiency, both have concerns about overfitting/attribution; VQ-Transplant has more quantified efficiency gains. |
| SSQ (`pBz9imKi56`) | 4.67 | Comparable — both have a strong central idea with a core unresolved tension; VQ-Transplant's tension (decoder mismatch) is better resolved than SSQ's (reconstruction-generation paradox). |
| WeTok (`QteJJF57yG`) | 5.00 | Comparable — both offer practical tokenizer improvements with strong results but limited novelty in individual components. |
| FVQ/VQBridge (`juM14y0caI`) | 6.00 | Stronger — more rigorous methodology, more impactful results (100% codebook usage at scale), more complete ablation story. |
| Latent Denoising Tokenizer (`1jBsi98fVe`) | 6.50 | Stronger — broader validation across six generative models, cleaner conceptual contribution, more thorough theoretical motivation. |
| AToken (`a4fSF5pGJq`) | 6.50 | Stronger — more ambitious scope (unified multi-modal tokenizer), larger engineering contribution, more impactful results. |

VQ-Transplant sits between the 4.5-5.0 range anchors. The core idea is genuinely useful and well-executed, the efficiency gains are concretely demonstrated, and experiments are extensive. The MMD-VQ contribution is marginal, the cross-dataset generalization claim needs a baseline to be fully convincing, and some presentation details could be clearer. These weaknesses are real but do not threaten the core framework contribution. Compared to FVQ (6.0), VQ-Transplant has a less rigorous ablation story; compared to WeTok (5.0), it has a fresher conceptual framing with similar validation thoroughness.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>