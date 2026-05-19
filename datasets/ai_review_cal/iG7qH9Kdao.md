- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 3
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper conducts a large-scale empirical study of three Diffusion Transformer (DiT) variants — PixArt-α, LargeDiT, and U-ViT — for text-to-image generation, training models from 0.3B to 8B parameters on datasets up to 600M images. The central finding is that U-ViT's full self-attention design scales more effectively than cross-attention DiTs and can match SDXL UNet performance at 2.3B parameters with substantially lower inference latency. The paper also explores token-concatenation for extending U-ViT to image editing and analyzes how long captions and dataset size improve text-image alignment.

## Strengths

1. **Controlled large-scale comparison of DiT architectures under identical conditions.** Figures 3–6 compare PixArt-α, LargeDiT, and U-ViT at matching parameter scales (0.6B and ~2B) using the same VAE, text encoder, data, and training steps. This is the largest controlled comparison of these architectures in the literature. The 2B U-ViT converges faster and achieves higher final TIFA/ImageReward than equivalently-sized cross-attention variants, providing genuine evidence for the architecture's scaling advantages.

2. **2.3B U-ViT matches SDXL UNet with 75% lower inference latency.** Figure 5 shows the 2.3B U-ViT achieving equivalent TIFA and ImageReward to SDXL U-Net after 500K steps. Table 1 reports end-to-end latency of 0.35s vs 1.38s on H100 at 256×256 resolution despite 3× theoretical GMACs — a practically meaningful efficiency advantage that goes beyond simple parameter counting.

3. **Ablations isolating the role of skip connections.** Figure 7(c) trains a small U-ViT with and without skip connections under identical settings. Removing skip connections degrades convergence, confirming this design choice (which distinguishes U-ViT from in-context conditioning in DiT) is critical. This ablation is clean and informative.

4. **Informative analysis of information density from long captions and dataset scaling.** Section 6.3 and Figure 14 show that both long captions and larger datasets increase the percentage of TIFA element phrases present in captions across ten element types (animal/human, object, color, etc.), providing a measurable explanation for why these scaling choices improve text-image alignment beyond simply noting that longer captions help.

## Weaknesses

### Fatal

None.

### Major

1. **Unsubstantiated claims about editing performance against SOTA methods.** Section 5.2 states that token concatenation "outperforms Canny ControlNet trained on SD3-Medium on TIFA-COCO and all metrics in BrushBench" but provides **zero numerical results** — no table, no scores. The comparison with BrushNet is also only qualitative (three cherry-picked examples in Figure 10). After saying "We quantitatively compare our token concatenation approach with current state-of-the-art inpainting method BrushNet," the paper immediately pivots to "We show some qualitative outputs." This is a significant evidential gap. Claims of outperforming established methods must be backed by standard metrics (FID, LPIPS, CLIP score, or at minimum the promised TIFA-COCO and BrushBench numbers).

2. **No human evaluation supporting central performance claims.** The paper's core findings — "U-ViT scales more effectively," "U-ViT matches SDXL UNet" — rest entirely on TIFA and ImageReward, both automated proxy metrics. TIFA measures VQA accuracy on generated images and is a reasonable alignment proxy, but the paper makes strong comparative claims ("scales more effectively," "better performance") without any human preference study, side-by-side comparison, or standard perceptual metrics (FID, CLIP score on diverse prompts). The claims may be valid, but the evidence is thinner than the strength of the conclusions warrants.

### Minor

3. **Inconsistency between abstract/contributions and body results.** The abstract claims "a 2.3B U-ViT model can get better performance than SDXL UNet," and the contributions list says it "can outperform SDXL's UNet." However, the body (Section 3.4, Figure 5 caption) states it "matches SDXL U-Net in both TIFA and ImageReward after 500K steps." "Better" and "outperform" are stronger than "matches." This discrepancy should be resolved.

4. **Data scaling experiment uses only two data points.** The claim "U-ViT scales better than UNet with larger data size" (Section 6.2, Figure 13) is based on comparing 250M vs 600M images — a single relative comparison that could also reflect dataset distribution differences (LensArt vs SSTK). Without intermediate data sizes, the experiment shows both models improve with more data and U-ViT improves more in this one instance, but this is a weak basis for a general claim about "scaling" behavior. Adding at least one intermediate data size (e.g., 400M) would substantially strengthen this claim.

5. **Identical hyperparameters across architectures may obscure relative advantages.** The paper uses the same learning rate (8e-5), warmup schedule, and batch size for all DiT variants (Section 3.1). While this is stated as a deliberate choice for fair comparison, cross-attention models (PixArt-α, LargeDiT) and self-attention models (U-ViT) may respond differently to these settings. The paper does not include any sensitivity analysis or hyperparameter search, so the observed advantage of U-ViT could partially reflect suboptimal tuning for other architectures. A minimal ablation (e.g., varying learning rate for one scale) would increase confidence in the comparisons.

6. **Fixed CFG scale (7.5) for all models without ablation.** The evaluation uses a single CFG scale, which can have different optimal values for different architectures. This could systematically disadvantage some models. A CFG sweep or justification that 7.5 is near-optimal for all compared architectures would address this.

### Trivial

- The paper uses "SD2 U-Net" as a baseline for PixArt-α and LargeDiT experiments but switches to "SDXL U-Net" for U-ViT experiments. While this progression is clear on close reading, it can confuse readers who expect consistent baselines throughout. A brief clarifying statement about why different UNet baselines are used in different sections would help.

## Nice-to-Haves

- **Error bars or multiple seeds:** Training large T2I models from scratch is expensive, but reporting results from a single run limits statistical confidence. Bootstrapped confidence intervals on the evaluation metrics would help.
- **Training compute analysis:** The paper reports inference latency but not training GPU-hours. Given the paper's focus on scaling, training efficiency is directly relevant.
- **Full description of curated datasets:** LensArt and SSTK are not publicly available, and details about sourcing, filtering, and deduplication are minimal. Additional documentation would aid reproducibility.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Typographical and formatting critiques** (e.g., "typos and awkward phrasings"): Removed per Hard Rules — these are parser artifacts, not author errors.
- **"Reproducibility: The datasets LensArt and SSTK are proprietary and not described sufficiently"**: The paper describes them as curated datasets with concrete sizes (250M, 350M). The existence claim is not in doubt. A softened version is retained as a Nice-to-Have.
- **"No statistical significance / no error bars"**: Moved to Nice-to-Have since multiple-seed training of 8B-parameter models is not standard practice in this cost regime.
- **"Results would be stronger with human evaluation"** (repeated framing): The core concern is retained in Weaknesses (Major #2); the repeated mentions throughout the harsh critic's report are merged.
- **Strength Finder's "outperforms BrushNet" framing**: Overstated — the paper only provides qualitative comparisons to BrushNet. The strength is adjusted to reflect what the paper actually demonstrates (outperformance over channel concatenation with numbers; qualitative-only vs BrushNet).
- **"Comparison in Fig. 7(a) does not keep parameter count constant"**: The paper is explicitly examining the effect of architecture design (down/up sampling + channel count), not running a parameter-matched comparison. This is not a valid critique of the experiment's stated purpose.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the work that the paper itself does not articulate.

## Suggestions

1. **Provide the missing quantitative numbers for editing comparisons.** The claim about outperforming Canny ControlNet on TIFA-COCO and BrushBench must be backed by a results table with standard metrics. If these numbers are not available, the claims should be scaled back to what the evidence supports (qualitative demonstration of feasibility).

2. **Resolve the "better" vs "matches" inconsistency** between the abstract/contributions and Section 3.4. Choose one framing and apply it consistently.

3. **Add at least one intermediate data size** (e.g., 400M) to the data scaling experiment to move from a two-point comparison to a genuine scaling curve.

4. **Conduct a minimal hyperparameter sensitivity analysis** (e.g., vary learning rate by ±2× for one model scale across architectures) to show the reported rankings are not artifacts of a single setting.

5. **Consider adding a small-scale human preference study or standard perceptual metrics** (FID, CLIP score on a diverse prompt set) for the key comparison (2.3B U-ViT vs SDXL UNet) to validate that the TIFA/ImageReward gap corresponds to real perceptual differences.
