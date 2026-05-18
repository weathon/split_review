Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper introduces Discrete Inversion, a method for inverting discrete diffusion models (multinomial diffusion and masked generative models) by recording residuals between target and predicted logits using the Gumbel-max trick—analogous to recording Gaussian noise in DDPM Inversion for continuous diffusion. The approach is evaluated on image editing (Paella, VQ-Diffusion on PIE-Bench) and text sentiment editing (RoBERTa), demonstrating near-perfect reconstruction and competitive editing quality.

## Strengths

1. **First inversion method for discrete diffusion models, with strong empirical reconstruction.** The paper provides the first demonstration of precise inversion for discrete diffusion models, including both multinomial diffusion and masked generative models. Reconstruction results are near-perfect: PSNR=inf, SSIM=1.00 for VQ-Diffusion image inversion (Table 1) and 100% hit rate for text inversion (Table 4), while masked generation baselines fail completely. This is a genuine capability advance for discrete generative models.

2. **Competitive structure preservation in image editing.** Discrete Inversion with Paella achieves the lowest structure distance (11.34) among all compared methods (Table 2), including continuous diffusion models (DDIM+SD1.4 with various editing techniques). Background preservation metrics (PSNR, LPIPS, MSE, SSIM in Table 3) also favor the proposed method, supporting the claim that the latent space encodes structural information from the original image.

3. **Cross-modal validation.** The method is validated across two image model architectures (Paella, VQ-Diffusion) and a text model (RoBERTa), with consistent positive results. This cross-modal scope makes the versatility claim credible.

4. **Clear conceptual framing and practical utility.** The paper correctly identifies a real limitation of existing discrete models—the inability to inject information from the input during editing beyond brute-force masking. The proposed method addresses this gap and enables editing without predefined masks, attention map manipulation, or ODE trajectories (which discrete models lack).

## Weaknesses

### Fatal

None.

### Major

1. **Poor exposition quality in Section 3.2 undermines trust in the method's presentation.** The methods section contains sentence fragments (line 113 begins with "Since" without a completed main clause; a dangling "Since" ends line 114; line 117 begins with lowercase "the" as an orphaned fragment), abrupt topic transitions (a statement about latent space guarantees at line 115–116 interrupts the masked-model derivation mid-flow), and hyperparameter discussion (lines 119–120) inserted before the core latent definition appears at line 179. While the *mathematical definitions* are present and correct ($z_t$ for both model classes, three noise injection strategies with equations), the organization and prose quality are substantially below the standard expected for a conference paper. A reader unfamiliar with DDPM Inversion would struggle to reconstruct the algorithm from this section. This is not a parser artifact—the fragments and disjointed flow are structural issues in the text as written.

2. **Critical ablations and parameter studies are absent.** The paper introduces three noise injection strategies (linear, variance preserving, max), states "linear strategy gives best results" (line 206), but provides no ablation table or quantitative comparison. The hyperparameters $\tau$, $\lambda_1$, $\lambda_2$ are described as allowing "finer control over the editing process" (line 119), yet no systematic study of their effect is presented. Since these parameters directly control the editing-quality trade-off, the absence of any analysis is a significant gap.

### Minor

3. **Text evaluation relies on a proprietary, black-box classifier (ChatGPT-4).** The evaluation reports structural preservation and sentiment correctness using ChatGPT-4 as an oracle (Section 4.2, Table 5). The prompts used to query ChatGPT are deferred to the supplementary materials. Using a proprietary model whose behavior can change with updates makes exact reproduction impossible. While LLM-as-judge is increasingly common, its use here as the sole evaluation methodology for a central empirical claim is a weakness.

4. **Novelty articulation could be sharper.** The paper correctly acknowledges its connection to DDPM Inversion (Huberman-Spiegelglas et al., 2024), describing the approach as "generaliz[ing] the concept" (Related Work). However, it does not fully articulate *why* extending inversion to discrete spaces is technically non-trivial. The Gumbel-max trick substitution is mathematically natural, and the paper would benefit from identifying specific difficulties (e.g., the absence of an ODE trajectory is mentioned but not analyzed; the non-differentiable sampling step is noted but its implications for information control are not explored).

5. **The Gaussian mutual information analysis (Section 3.3) is tangentially relevant.** This section derives mutual information for a toy Gaussian DDPM and plots it in Figure 3. The paper acknowledges it is a "prototypical example" and uses it to motivate $\lambda$ scheduling (deferred to Supplementary). It provides some theoretical intuition, but it is not directly about discrete models and does not connect to the proposed method's specific design decisions. It would be stronger if paired with an analogous discrete analysis or explicitly linked to the noise injection strategies.

6. **Cross-architecture comparisons in Table 2 mix multiple confounds.** Discrete Inversion on Paella/VQ-Diffusion is compared against Stable Diffusion v1.4 with DDIM inversion. These differ in model capacity, training data, tokenization (VQ-VAE vs. latent diffusion), and inference compute. The headline metric ("lowest structure distance 11.34") is informative but the paper does not discuss these confounds. This does not invalidate the results, but readers should interpret the comparison cautiously.

### Trivial

7. **The "Since" fragments and orphaned sentences in Section 3.2 (lines 113–117)** should be repaired for grammatical completeness and logical flow.

8. **Table/Figure references and equation formatting contain minor garbling** (line 198: "$\tilde{y}=$" missing backslash rendering; stray numerals on lines 123–176 appear to be figure artifacts). These are likely parser issues in the extracted text rather than the original submission.

## Nice-to-Haves

- An ablation table comparing the three noise injection strategies and varying $\tau$, $\lambda_1$, $\lambda_2$ would significantly strengthen the paper.
- Replacing or supplementing the ChatGPT-4 evaluation with standard automated metrics (e.g., a trained sentiment classifier, BLEU/ROUGE for structure) would improve reproducibility.
- A brief analysis of why editing works better for masked generative models than multinomial diffusion (mentioned in the conclusion but not analyzed) would be informative.

## Removed Points

These points from the reviewers are flagged for removal; treat them with caution:

- **"Algorithm pseudocode is missing"**: The paper references "Algorithm 1" and "Algorithm 2." These were likely in environments stripped by the parser; the rules instruct us to treat this as a parser artifact.
- **"PSNR=inf undermines editing claims"**: The paper explains that identical reconstruction arises because the inversion preserves the token sequence. Perfect reconstruction does not prevent editing—the latents are modified during editing. This is a strength, not a tension.
- **"λ₁+λ₂=1 contradicts earlier formulation"**: The λ₁+λ₂=1 constraint applies specifically to the variance-preserving strategy. The linear strategy only requires λ₂>0. These are separate strategies with separate parameterizations; there is no contradiction.
- **"Section 3.3 is irrelevant and should be removed"**: The section provides a prototypical Gaussian analysis to motivate λ scheduling. While tangential, it is not irrelevant. It belongs as a Minor weakness, not a removal-worthy one.
- **"Equations are partially garbled"**: The equations in the extracted text are intact and coherent (linear strategy eq. 186–188, variance preserving eq. 194–198, max strategy eq. 202–203). The garbling the reviewer perceives appears to be formatting artifacts from the PDF extraction, not content errors.
- **Several generic strength entries from the Strength Finder**: Claims like "this paper addressed an important problem" without specific evidence were filtered.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the same observations: the method is conceptually straightforward and the experiments are broadly supportive, but the exposition and evaluation rigor need improvement. The harsh critic's claim that the method is impossible to evaluate is not supported by the actual mathematical content of the paper.

## Suggestions

1. **Rewrite Section 3.2 entirely.** Structure it as: (a) establish the analogy between Gaussian reparameterization and Gumbel-max trick, (b) present the inversion algorithm for masked generative models with a clean definition of $z_t = y_0 - \hat{y}_{0|t}$, (c) present the inversion algorithm for multinomial diffusion with $z_t = y_{t-1} - \hat{y}_{t-1}$, (d) discuss hyperparameters and noise injection strategies, each with motivation. Include a diagram or pseudocode showing the inversion-and-editing pipeline end-to-end.

2. **Add ablation studies** comparing the three noise injection strategies quantitatively and showing the effect of varying $\tau$, $\lambda_1$, $\lambda_2$ on the editing quality / reconstruction fidelity trade-off.

3. **Strengthen text evaluation** by supplementing ChatGPT-4 evaluation with a standard sentiment classifier (e.g., a fine-tuned RoBERTa sentiment model) and reporting n-gram overlap metrics for structural preservation.

## Score and Decision

**Originality**: Moderate. Extending DDPM Inversion to discrete spaces via the Gumbel-max trick is a natural extension, but the paper is the first to do so and applies it to a meaningful range of architectures and modalities.

**Importance of research question**: High. Controlled editing in discrete generative models is an important capability that has been lacking.

**Claims well supported**: Partially. The reconstruction claims are strongly supported. The editing claims are moderately supported but missing ablation studies temper confidence.

**Soundness of experiments**: Moderate. Reasonable metrics and benchmarks, but missing ablations and reliance on a proprietary evaluation oracle for the text domain are weaknesses.

**Clarity of writing**: Below standard. Section 3.2 needs significant structural and prose revision.

**Value to the research community**: Moderate. The method enables a new capability (discrete inversion) that will likely be built upon.

The paper has a real and useful contribution—first inversion for discrete diffusion models—and the experimental results are broadly positive. However, the exposition quality in the core methods section is below the standard expected for a top conference, key ablations are missing, and the text evaluation relies on a non-reproducible oracle. These issues are fixable with revision but are substantive enough in the current form to warrant rejection. A substantially revised version could be competitive.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>