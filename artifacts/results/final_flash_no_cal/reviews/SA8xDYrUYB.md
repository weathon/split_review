## Summary

Purrception adapts Variational Flow Matching (VFM) to vector-quantized (VQ) image latents by learning a categorical posterior over codebook indices while computing the velocity field in the continuous embedding space. On ImageNet-1k 256×256, the method converges faster (1.65–3.5×) than continuous and discrete flow matching baselines and achieves a competitive FID of 3.88 with 750M parameters. The hybrid formulation also provides a temperature knob absent in purely continuous or discrete flow models.

## Strengths

1. **Clear, theoretically grounded derivation from VFM.** Section 3.2 provides a clean derivation from VFM principles to the categorical posterior (Eq. 12), the resulting velocity field (Eq. 13), and the cross-entropy training objective (Eq. 14). The connection between the variational posterior and the practical training loss is explicit and well-motivated.

2. **Faster convergence is demonstrated across two architectures and multiple baselines.** Figure 3 shows Purrception reaching lower FID in fewer training iterations than CFM, CFM-endpoint, and DFM on both DiT-L/2 and DiT-XL/2. The specific speed-up factors (1.65×, 3.0×, 2.3×, 3.5×) are reported and the comparison uses matched training configurations and the same ODE solver.

3. **Principled temperature control with clear empirical characterization.** Section 3.2 (Eq. 15) introduces softmax temperature as a natural consequence of the categorical posterior. Figure 4 documents a U-shaped FID–temperature relationship with a clear optimum (τ≈0.8–0.9), and Figure 5 provides qualitative illustration of the sharpness–diversity trade-off. This is a genuine capability that neither continuous flow matching nor discrete flow matching offers.

4. **Competitive results among VQ-based generative models.** Table 1 reports FID 3.88 for Purrception (750M), which outperforms VQGAN (5.20), VQ-Diffusion (5.84), MaskGIT (6.18), and approaches LlamaGen-XL (3.39, comparable parameter count) and RQTransformer (3.80, 3.8B params). This validates that the hybrid formulation is practically useful.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Convergence comparison uses an asymmetric inference setup.** The convergence-speed claim (Section 4.1, Figure 3) is reported with Purrception using τ=0.9 at inference while the CFM and DFM baselines have no temperature knob. The paper does not show the convergence curves for Purrception with τ=1.0 (the training default). Because Figure 4 shows a modest FID difference between τ=0.9 and τ=1.0 (~0.2–0.3 FID points at 1M iterations), it is likely the qualitative speed-up claim would still hold — but the asymmetry makes it impossible to rule out that part of the apparent advantage comes from the temperature tuning rather than the hybrid formulation itself. The authors should add convergence curves at τ=1.0 to cleanly separate the two effects.

2. **The inference-time discretization of the continuous latent is not specified.** The paper states that a "quantized latent" is generated during sampling and passed to the decoder (Figure 2 caption), but it does not describe the actual mechanism (argmin over the codebook? sample from the final posterior?). This step is non-trivial because the ODE output z₁ is a continuous convex combination of codebook embeddings, while the VQ decoder was trained on hard discrete indices. The potential mismatch between training signal (cross-entropy on discrete indices) and inference (continuous → discrete mapping) is not discussed or ablated. Details may appear in the stripped appendix, but the main text should at least outline the procedure and note any quality impact.

3. **The quantitative comparison in Table 1 mixes confounding factors.** The baselines use different tokenizers (vq-f8 vs. vq-ds8-c2i), different backbones, and different training durations. For example, DiT-XL/2 and SiT-XL/2 use high-quality VAEs and longer training schedules (the paper acknowledges this, noting that top diffusion models train for approximately twice as many iterations). While the paper is transparent about these differences and draws appropriately cautious conclusions, the headline "competitive FID" should be read with the caveat that the table does not provide an apples-to-apples comparison on a fixed budget.

4. **FID sample size is not stated in Table 1.** The convergence plots use FID-10k, the temperature ablation uses FID-50k, but the main quantitative table (Table 1) only reports "FID ↓" without specifying the number of samples. This is a minor reporting gap.

5. **Classifier-free guidance is used but not explained.** Table 1 reports cfg=1.3, but the paper never explains how guidance is applied in the flow-matching setting (the main text only mentions "can incorporate guidance" in the Future Work section). A brief methodological note would improve reproducibility.

### Trivial

- Figure 3 annotation text reads "3.0x faster than CFM-endpoint" but the surrounding description references DFM in the corresponding speed-up factor (the annotation-to-claim mapping could be cleaner).
- The paper uses "Purrception" and "Purception" inconsistently (the latter appears in several figure captions and table headers).

## Nice-to-Haves

- An ablation training Purrception with a continuous MSE loss on the endpoint (replacing cross-entropy) would directly isolate the benefit of the discrete supervision.
- A controlled comparison against a continuous diffusion model (e.g., CDCD) applied to the same VQ latents with the same backbone would further clarify the advantage of the flow-matching perspective.
- Reporting results for multiple random seeds would strengthen the convergence claim.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Codebook size K not stated in main text**: The actual value of K is not given in the main text. This detail is almost certainly in Appendix C (implementation details), which was stripped by the parser. Removed per the rule that parser-stripped appendix content should not be treated as absent.
- **FID-10k is noisy for convergence tracking**: This is a known limitation of FID-10k, but it is standard practice in the literature for training-time monitoring, and the final results use FID-50k. The observation is correct but does not weaken the paper's claims.
- **Limited novelty / direct application of VFM**: The reviewer notes that the method is a direct application of VFM (Eijkelboom et al., 2024) with CatFlow to VQ image latents. This is descriptively accurate, but the paper's contribution is the *adaptation and empirical validation* of this framework for the challenging VQ image setting, which was not previously explored. Novelty is a matter of degree; the paper is appropriately positioned as an adaptation.
- **The method's final FID is not SOTA**: The paper openly acknowledges in the Limitations section that it does not match top-tier continuous diffusion models. The claim is "competitive," not "state-of-the-art," so this observation restates what the paper already says.
- **CDCD comparison could be more precise**: The paper discusses CDCD and notes differences (jointly learned embeddings, continuous relaxations, language domain). The critique that a "more precise distinction" is needed is subjective; the existing discussion is adequate for a Related Work section.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily validate and qualify the paper's claims rather than uncovering new interpretations.

## Suggestions

- Add convergence curves for Purrception with τ=1.0 to Figure 3, so the speed-up claim is separable from temperature benefits.
- Clearly describe the discretization step at inference (argmin, final-sample-from-posterior, or other) and add a brief analysis of its effect on sample quality.
- State the FID sample size in the caption of Table 1.
- Add a short explanation of how classifier-free guidance is applied (e.g., logit conditioning or velocity-field conditioning) in the main text.
- Standardize the spelling of "Purrception" throughout the paper and figures.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>