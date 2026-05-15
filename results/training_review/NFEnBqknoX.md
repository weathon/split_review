Now I have a thorough understanding of the paper and can cross-check every claim. Here is my final synthesized review.

---

## Summary

This paper introduces Discrete Inversion, a method that records prediction residuals (differences between a discrete diffusion model's logit predictions and ground-truth targets) during a forward pass and re-injects them during reverse sampling to enable reconstruction and controlled editing. The method is demonstrated on masked generative models (Paella), multinomial diffusion (VQ-Diffusion), and, in a more speculative extension, a non-diffusion masked language model (RoBERTa). The core idea is presented as a discrete analogue of DDPM Inversion, leveraging the Gumbel-Max trick analogously to how continuous methods use the Gaussian reparameterization trick.

## Strengths

- **First inversion framework for discrete diffusion models.** The paper correctly identifies that no prior work provides inversion for multinomial diffusion or masked generative models, and it proposes a concrete solution. The connection to DDPM Inervation via the Gumbel-Max trick (Section 3.2) is a reasonable conceptual bridge between continuous and discrete settings.

- **Near-perfect reconstruction across modalities.** The method achieves PSNR = inf for Paella reconstructions (Table 1) and 99.7% accuracy / 0.99 STS for text reconstruction with RoBERTa (Table 4). These results confirm that the recorded residuals carry enough information to exactly reproduce the original data — a necessary property for any inversion method.

- **Editing without masks or attention manipulation.** The image editing results (Table 2) show that Discrete Inversion + Paella achieves the lowest structure distance (11.34) among all compared methods, including continuous diffusion baselines (DDIM+SD1.4 with Prompt-to-Prompt: 21.62). This demonstrates a genuine advantage: the method preserves structure without requiring user-provided masks or cross-attention hacking.

- **Model-agnostic formulation.** The method is validated on three structurally different discrete models — a masked generative model (Paella), a multinomial diffusion model (VQ-Diffusion), and a masked language model treated as a generative model (RoBERTa). While the strength of validation varies across these (see Weaknesses), the algorithmic formulation itself is modular and not tied to a single architecture.

## Weaknesses

### Fatal
None.

### Major

- **The RoBERTa experiments are poorly scoped and overclaimed.** The paper explicitly calls RoBERTa "a text discrete diffusion model" (Section 4.2), which is factually incorrect — RoBERTa is a masked language model trained with a discriminative MLM objective, not a diffusion model with a forward/reverse Markov chain. The "inversion" performed on RoBERTa is a heuristic iterative remasking procedure. The claim that this "transform[s] a model primarily trained for understanding tasks... into a competitive generative model" is unsupported: there is no comparison against any actual text generative model (GPT, T5, BART) on fluency, diversity, or generation quality. The evaluation relies entirely on ChatGPT-4 as a classifier for "structure preservation" and "sentiment correctness" (Table 5), without human validation or analysis of classifier biases. The single qualitative example in Table 6 is not sufficient to demonstrate generative capability. These experiments should either be substantially strengthened (human evaluation, comparisons to actual generative models, corrected characterization of RoBERTa) or removed from the paper.

- **The reconstruction comparison (Table 1) pits the method against a strawman baseline.** The only baseline for discrete reconstruction is masked inpainting, where "all image tokens are replaced with randomly sampled tokens" so the model "lacks any prior information about the original image" — as the paper itself states. Any method that stores information about the original will trivially outperform this. A meaningful discrete reconstruction baseline would compare against the unmodified model's own reconstruction ability (e.g., running the full reverse process from random noise and measuring similarity), or against sampling from the closed-form posterior \(q(x_{t-1}|x_t, x_0)\) without residual injection. The current comparison inflates the apparent contribution.

### Minor

- **The mutual information analysis (Section 3.3, Remark 3.1) is for a Gaussian DDPM, not the discrete models the paper actually uses.** The paper acknowledges this ("since the inversion involves model forward function call which is difficult to analyze"), but this means the analysis provides only indirect intuition. It does not analyze information flow in the proposed discrete residual space. This does not harm the empirical results but weakens the theoretical support.

- **The recorded "latent" is a prediction residual, not recovered sampling noise.** In continuous DDPM Inversion, the recorded \(z_t\) is the actual Gaussian noise used in the reparameterization \(x = \mu + \sigma z\). Here, the recorded \(z_t = y_0 - \hat{y}_{0|t}\) is the difference between the model's prediction and the ground-truth logits. While the paper draws an analogy via the Gumbel-Max trick, the residual is not independent Gumbel noise — it depends on both the data and the model's predictions at that specific timestep. This means the latent does not "obey the prior" in the way continuous inversion latents do. The three injection strategies (linear, variance preserving, max) are heuristics to manage this mismatch, and the paper empirically settles on the linear strategy without deeper analysis of why. This does not invalidate the method's usefulness for editing, but the framing as "inversion" should be more carefully qualified.

### Trivial

- No substantive formatting issues beyond parser artifacts.

## Nice-to-Haves

- An ablation with \(\lambda_1 = 0\) (no residual injection) to demonstrate that the recorded residuals are causally necessary for the observed reconstruction and editing quality.
- Comparison against a principled discrete baseline: sampling from the posterior \(q(x_{t-1}|x_t, x_0)\) without caching residuals would isolate the value of the residual injection itself.
- Failure cases and analysis of when Discrete Inversion struggles (the paper notes multinomial diffusion is less robust and style transfer is weak, but no examples or analysis are shown).
- Human evaluation for the text editing task to validate the ChatGPT-based metrics.

## Removed Points

These points are flagged to be removed; treat them with caution.

- Harsh critic's claim that "the method is trivial and does not constitute 'inversion' in any meaningful sense" and "no actual inversion of the diffusion process occurs." The paper draws a clear analogy to DDPM Inversion via the Gumbel-Max trick, which is the standard reparameterization for categorical distributions. The method follows the same stochastic-trajectory-recording paradigm as existing non-ODE inversion methods. Recording residuals is the discrete analogue of recording Gaussian noise in continuous DDPM Inversion (Huberman-Spiegelglas et al., 2024). The claim that this is "memorization via residual caching" rather than inversion is a redefinition, not a refutation of the paper's stated contribution. The underlying method is simple but correctly framed.

- Harsh critic's claim that "all comparisons against 'masked generation' (inpainting) are fundamentally unfair and invalidate the reported results." This overstates: the editing experiments (Table 2) include comparisons against multiple continuous diffusion baselines (DDIM+SD1.4 with Prompt-to-Prompt, DDPM+SD1.4, etc.), not just masked generation. The editing comparisons against continuous methods are informative and show genuine advantages (lowest structure distance). The reconstruction comparison is indeed weak but is a separate and acknowledged limitation.

- Harsh critic's claim about the "dataset is custom and not released." Per hard rules, release status of cited entities is not a valid criticism.

- Strength Finder's claim about "introduction of a new text-editing benchmark" providing "a standardized evaluation resource." The paper mentions a Sentiment Editing dataset but does not demonstrate that it will serve as a standardized resource for future work. This conflicts with the verified weakness that the text experiments lack rigor.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a recurring tension: the method is clear and empirically effective for image editing, but its framing as "inversion" in the discrete setting carries theoretical baggage that the paper does not fully resolve. The latent is a prediction residual, not recovered sampling noise, and the connection to Gumbel noise is heuristic. This tension does not make the method wrong, but it means the contribution is better described as "residual-guided editing for discrete generative models" than as "inversion" in the strict ODE-noise-recovery sense.

## Suggestions

1. **Revise or remove the RoBERTa experiments.** Either drop them entirely (the image experiments stand on their own) or: (a) stop calling RoBERTa a diffusion model; (b) compare against actual text generative models; (c) add human evaluation to validate the ChatGPT-based metrics; (d) substantially downscale the claim from "competitive generative model" to "proof-of-concept for extending residual-guided editing to MLM-based architectures."

2. **Add a meaningful discrete reconstruction baseline.** Compare against the unmodified model's reconstruction (e.g., sampling from random noise with the same prompt) or against posterior-based sampling without residual injection, so the reader can assess the value added by caching residuals.

3. **Acknowledge the theoretical gap more explicitly.** The paper should clearly state that the discrete residuals \(z_t\) are prediction errors rather than recovered sampling noise, and explain why this still enables useful editing despite not constituting "inversion" in the strict ODE sense.

4. **Show failure cases and limitations with examples.** The conclusion mentions that multinomial diffusion editing is less robust and style transfer is weak — show these failures visually so users understand the method's boundaries.

## Score and Decision

**Originality:** Moderate. Extending stochastic residual-recording to discrete spaces via the Gumbel-Max trick is a natural but previously unexplored connection.

**Importance of research question:** Moderate. Discrete diffusion models lack editing capabilities, and a principled solution would have impact.

**Support for claims:** Mixed. The image editing claims are well-supported (valid comparisons against continuous methods, clear metrics). The RoBERTa claim of transforming RoBERTa into a "competitive generative model" is unsupported.

**Soundness of experiments:** Moderate. The image experiments are sound; the text experiments are not. The reconstruction baseline is too weak.

**Clarity of writing:** Adequate. The method description is clear, though the paper contains some garbled text from the PDF extraction process (parser artifact).

**Value to community:** Moderate. The method provides a practical tool for editing with discrete generative models, even if the theoretical framing needs refinement.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>