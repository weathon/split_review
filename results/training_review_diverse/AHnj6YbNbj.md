## Summary

The paper proposes Ambient Space Flow Transformers (ASFT), a flow matching generative model that operates directly in ambient (data) space using a conditionally independent point-wise training objective (CICFM). This eliminates the two-stage compressor+generator paradigm that dominates current practice. The method represents data as coordinate→value maps and uses a modified PerceiverIO architecture with spatial-aware latents and multi-level decoding. Empirical results span images (FFHQ, LSUN-Church, ImageNet-128/256) and 3D point clouds (ShapeNet, Objaverse), showing competitive or state-of-the-art performance with a single domain-agnostic architecture.

## Strengths

- **Single-stage training in ambient space eliminates the need for domain-specific compressors.** The paper directly addresses the complexity of two-stage latent-space approaches. The CICFM objective allows the model to be trained end-to-end without training a VAE, VQGAN, or other compressor, and the same architecture trivially adapts across images and 3D point clouds by changing only coordinate/value dimensionality. This is demonstrated concretely (Section 4).

- **Conditionally independent point-wise objective enables training sub-sampling and resolution-agnostic inference.** The CICFM loss (Eq. 3) decomposes the velocity field point-wise, allowing the model to be trained on only 12% of image pixels (saving >20% Gflops, Figure 4b) and to generate at resolutions up to 2048×2048 despite being trained only on 256×256 images (Section 4.5). This is a novel capability not available in two-stage latent-space models and is well-supported by evidence.

- **Competitive or superior performance across images and 3D point clouds with a single domain-agnostic architecture.** On FFHQ-256 and Church-256, ASFT-L achieves FID 2.18 and 5.51, outperforming all function-space baselines (∞-Diff: 3.87, 10.36; Table 1). On ShapeNet, ASFT-B (108M) beats LION (110M) on Airplane MMD (0.2861 vs 0.3564) and 1-NNA (75.55 vs 76.30; Table 5). On Objaverse, ASFT substantially outperforms CLAY on ULIP-I (0.2976 vs 0.2066) and P-FID (0.3638 vs 0.9946; Table 6). These span different data domains using the same training recipe.

- **Scalability demonstrated with increasing model size and training compute.** Figure 4a shows consistent FID-50K improvement when scaling from ASFT-S to ASFT-XL and with more training iterations. This supports the practical utility of the approach.

## Weaknesses

### Fatal

None.

### Major

- **Missing architectural ablations for claimed innovations.** The paper introduces two modifications to the vanilla PerceiverIO — spatial-aware latents and multi-level decoding — and states they are critical for performance (line 103: "we make two key modifications to boost the performance"). Yet no controlled experiment isolates these components. Without an ablation, the reader cannot tell whether improvements come from the PerceiverIO's natural handling of coordinates, from the specific modifications, or from increased capacity. Similarly, the number of latent vectors $L$ and their dimensionality are not studied. This weakens the technical contribution and makes it difficult to attribute the method's success to the architectural choices rather than the overall framework. (The decoder count ablation in Figure 4b is helpful but does not test the architectural modifications themselves.)

### Minor

- **ImageNet-256 results are behind several ambient-space baselines, and the abstract's claim of "outperforming comparable approaches" is slightly overstated.** ASFT-XL achieves FID 3.74, which is worse than RIN (3.42), HDiT (3.21), Simple Diffusion U-ViT (2.77), and VDM++ U-ViT (2.12). To the paper's credit, the main text (lines 144) honestly discusses these comparisons, acknowledges the VAE pretraining data advantage of latent-space models, and notes the ×2.72 parameter gap for the largest models. However, the abstract's phrasing ("outperforming comparable approaches") is too broad given these numbers, especially relative to RIN (also a transformer-based ambient-space model). The paper is better characterized as achieving *competitive* performance on ImageNet-256 with a domain-agnostic architecture.

- **Objaverse comparison may not be fully controlled.** The paper acknowledges that CLAY is not open-source and that the exact evaluation setting (rendering pipeline, point sampling protocol, metric implementation) may differ across papers (lines 293). The reported improvement is large (P-FID 0.3638 vs 0.9946), but some gap could reflect evaluation differences rather than generative quality. The paper provides its settings for reproducibility but does not run controlled baselines on available open-source models like Shap-E under the same pipeline. This limits confidence in the reported margin.

- **Resolution-agnostic generation lacks quantitative evaluation.** Section 4.5 shows compelling qualitative results (images at 2048×2048, point clouds with 128k points) but provides no quantitative metrics (e.g., FID at higher resolutions, or MMD/COV for upsampled point clouds). Given that the paper highlights resolution-agnostic inference as a key contribution, the purely qualitative evidence weakens the claim. Computing FID at higher resolutions is not straightforward (the ImageNet validation set is 256×256), so this is not a fatal omission, but some proxy evaluation would strengthen the paper.

- **No statistical significance or confidence intervals.** Key metrics (FID, MMD, COV, 1-NNA) are reported as point estimates without variance across multiple runs or seeds. For ShapeNet in particular, where metrics can vary with initialization, this is a gap.

- **Inference cost not systematically reported.** The paper reports Gflops savings from sub-sampling (Figure 4b) but does not report wall-clock training time, inference time, or a head-to-head compute comparison with latent-space models. The paper argues ASFT avoids two-stage training, but the cost of operating in ambient space (where the transformer processes many more tokens) is not quantified.

### Trivial

None.

## Nice-to-Haves

- An ablation study on a smaller proxy task (e.g., CIFAR-10 or a synthetic 2D function dataset) isolating the contributions of spatial-aware latents and multi-level decoding would significantly strengthen the technical contribution.
- For the Objaverse comparison, running the same rendering and evaluation pipeline on an open-source baseline like Shap-E would provide a more controlled comparison.
- Quantitative evaluation of resolution-agnostic generation, perhaps using held-out high-resolution data or proxy metrics.
- A discussion acknowledging that the spatial-aware latent assignment (nearest-neighbor grouping in coordinate space) is itself a design choice that assumes coordinate-space proximity is a useful prior — which may not hold for all data types (e.g., graphs with non-Euclidean structure).

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The ImageNet tables do not report the number of decoded coordinate-value pairs used during training for these runs."** — Factually wrong. Line 112 explicitly states: "we set the number of decoded coordinate-value pairs to 4096 for images with resolution 128×128, 8192 for images with resolution 256×256." Removed for factual inaccuracy.
2. **Criticism about code/model release** — "The paper would be significantly stronger if it committed to releasing the trained ASFT models." Per hard rules, remove criticisms questioning release status of cited entities.
3. **"Limitation discussion" about Objaverse baseline fairness** — Already acknowledged by the paper itself (lines 293). Retained in weakened form in Minor section above.
4. **Missing appendix checks** — Criticisms about missing appendix content are removed per hard rules (parser strips appendices).

## Novel Insights

Beyond the paper's own contributions, the most interesting meta-point that emerges from the reviews is a tension: the paper's stated goal is domain-agnostic single-stage ambient-space generation, and on this axis the evidence is quite strong (FFHQ, Church, ShapeNet, Objaverse all deliver competitive or leading results). However, the paper also presents ImageNet-256 results, and when evaluated on that axis alone — the de facto standard for image generation quality — the method falls short of the best ambient-space models. This creates a disconnect between the paper's framing (as a general-purpose approach) and the community's default evaluation norm (ImageNet FID as a proxy for "is this method good?"). A clearer articulation that the paper is not trying to beat DiT/SiT on ImageNet but to demonstrate viability across domains would preempt this concern.

## Suggestions

- Add a controlled ablation of spatial-aware latents and multi-level decoding on a small-scale task (e.g., CIFAR-10 or a synthetic function dataset). Without this, the paper's architectural claims remain unsubstantiated.
- Tone down the abstract claim from "outperforming comparable approaches" to "achieving competitive performance across domains" to better reflect the ImageNet-256 results.
- For the Objaverse evaluation, either run open-source baselines (e.g., Shap-E) through the same pipeline, or add a stronger caveat about potential incomparability with CLAY's reported numbers.

## Score and Decision

The paper presents a clean, well-motivated framework with genuine contributions: single-stage ambient-space flow matching, a conditionally independent point-wise objective, and demonstrated domain-agnostic capability across images and 3D point clouds. The strongest evidence comes from FFHQ/Church (where ASFT outperforms all function-space models) and ShapeNet (where ASFT beats LION with comparable parameter counts). The main weaknesses are the missing architectural ablations (a significant methodological gap) and uneven evidence quality on ImageNet-256 and Objaverse. These are real but addressable weaknesses; they do not undermine the core contribution. The paper represents a solid step toward domain-agnostic generative modeling.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>