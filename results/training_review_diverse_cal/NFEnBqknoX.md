Now I have a thorough understanding of the paper and can verify all reviewer claims against the actual text. Let me construct the final review.

## Summary

This paper introduces Discrete Inversion, the first approach to enable precise inversion for discrete diffusion models (multinomial diffusion and masked generative models). The method records noise sequences and residuals during the forward process, then re-injects them for exact reconstruction and controlled editing without predefined masks or attention manipulation. Experiments across image (Paella, VQ-Diffusion) and text (RoBERTa) domains demonstrate near-perfect reconstruction and effective editing.

## Strengths

- **First inversion method for discrete diffusion models**: The paper explicitly fills a recognized gap — ODE-based inversion methods (DDIM, flow matching) do not apply to discrete spaces, and no prior work addressed this. The core idea of using the Gumbel-Max trick and residual recording is principled and well-motivated (Sec. 1, abstract).

- **Near-perfect reconstruction empirically validated**: Table 1 shows Discrete Inversion with Paella achieves PSNR = inf, SSIM = 1.0, LPIPS = 0.0, MSE = 0.0 — exact reconstruction through the VQ-VAE process — massively outperforming the masked-inpainting baseline (LPIPS 0.686, SSIM 0.348). This is expected from the method design but is convincingly demonstrated.

- **Best structure preservation in image editing**: Table 2 shows Discrete Inversion with Paella achieves the lowest structure distance (11.34) among all compared methods, including continuous diffusion models (DDIM+SD1.4 with P2P at 18.64), while maintaining competitive CLIP similarity. This is a meaningful achievement since discrete models typically lack editing capability.

- **Transforms RoBERTa into a controllable text editor**: Section 4.2 demonstrates that RoBERTa — a model designed for understanding — can perform controlled sentiment editing via Discrete Inversion, achieving 98.8% reconstruction accuracy (Table 4) and 79.8% sentiment correctness with 85.3% structure preservation (Table 5), far above the masked-generation baseline. This showcases the method's generality across model architectures.

- **Systematic analysis of noise injection strategies**: Section 3.2 formally analyzes three injection schemes (linear, variance-preserving, max) and identifies the linear strategy as best, providing practical guidance. The linear strategy is theoretically grounded in the Gumbel-Max trick.

## Weaknesses

### Fatal
None.

### Major

- **Text editing evaluation relies on ChatGPT-4 as a classifier without human validation or established automatic metrics**. The paper evaluates structure preservation and sentiment correctness using ChatGPT-4 as a judge (Sec. 4.2, Table 5) but provides no calibration against human ratings, no exact prompts used (deferred to supplementary), and no validation that ChatGPT's judgments are reliable for this specific task. The paper mentions "details of using ChatGPT for evaluation can be reviewed in Supplementary Materials" but even detailed prompts would not address the lack of human validation. While the reported improvements are large (~30% → ~80%), the evaluation method undermines confidence in the text editing claims. This is the most significant weakness because it affects a non-trivial part of the experimental validation. The image editing results (which use standard metrics like PSNR, LPIPS, CLIP similarity, structure distance) remain credible.

### Minor

- **Overstated claim about RoBERTa as a "competitive generative model"**: The paper's contributions list (end of Sec. 1) claims Discrete Inversion can "transform a model primarily trained for understanding tasks, such as RoBERTa, into a competitive generative model for text generation and editing." The experiments only demonstrate controlled sentiment editing on a specific dataset — there is no evaluation of unconditional generation fluency, diversity, sample quality, or comparison to actual generative language models. The claim goes beyond what the evidence supports. Replacing "competitive generative model" with "enables controlled text editing in RoBERTa" would better match the results.

- **No quantitative ablation or sensitivity analysis of the hyperparameters (τ, λ₁, λ₂) that control editing**: These parameters are described as central to the method's flexibility (Sec. 3.2), and the paper states "we empirically find that linear strategy gives best results" (line 206), but no quantitative comparison or sensitivity analysis is provided for either the strategy choice or the parameter values. A small table or figure showing structure distance / CLIP score for different settings would substantiate the design choices and help readers apply the method.

- **Mutual information analysis in Sec. 3.3 is for a Gaussian DDPM, not for discrete diffusion**: The analysis (Remark 3.1, Figure 3) provides a closed-form MI derivation for a continuous DDPM, motivating λ scheduling. The paper acknowledges this limitation (lines 231-232: "Since the inversion involves model forward function call which is difficult to analyze") and says the analysis "motivates" scheduling choices. However, the connection to the discrete case remains indirect, and no experiments directly leverage this analysis. The section feels better suited to the appendix.

### Trivial

- Some prose in Sec. 3.2 has a fragmented structure, jumping between masked models and multinomial diffusion mid-paragraph, making the method description harder to follow than necessary.

## Nice-to-Haves

- A brief discussion of computational overhead (number of forward passes, wall-clock time) would help readers assess practical applicability.
- An ablation showing structure preservation / edit quality for different (λ₁, λ₂) values would strengthen the noise injection analysis.
- Human evaluation or standard automatic metrics (e.g., BLEU for structure, a sentiment classifier for correctness) for the text editing task would substantiate the ChatGPT-based evaluation.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Method description insufficiently clear / relies too heavily on appendix"** (Harsh Critic Issue 1): The main text provides the core mathematical formulations (z_t definitions for both model types, noise injection equations, sampling procedures). Algorithm 1 and Algorithm 2 referenced to the appendix is standard practice for space-constrained papers. The "incomplete sentences" (e.g., "Since …") noted by the reviewer are parser artifacts, not author errors. Downgraded from Critical to Minor — the description could be better structured but is fundamentally present.
- **"Reconstruction metrics need clarification"** (Harsh Critic Other Observation): The paper already explicitly states (line 251) that metrics are calculated between original and inverted images, and explains the PSNR=inf result. This concern is already addressed by the paper.
- **"Continuous comparison is not a fair head-to-head"**: The paper acknowledges this, and the primary comparison is against the masked-generation baseline. This is a non-issue.
- **"No comparison to other discrete-space editing methods"**: The paper compares against masked inpainting (the standard approach for discrete models). Requesting comparisons to prompt-to-prompt style methods from the continuous domain is scope creep and methodologically inappropriate.
- **"Weaknesses about missing algorithms/appendix"**: Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an observation that the authors themselves did not already articulate.

## Suggestions

1. **Add human validation or standard metrics for text editing evaluation**. The simplest fix: have human annotators rate a sample of generated sentences (e.g., 100–200 examples) for structure preservation and sentiment correctness, then report agreement with ChatGPT. Alternatively, use BLEU/chrF for structural similarity and an off-the-shelf sentiment classifier for correctness. This would resolve the most significant concern without changing the paper's scope.

2. **Tone down the RoBERTa claim**: Replace "competitive generative model" with language about enabling controlled editing in understanding-focused models. The results are impressive enough without overclaiming.

3. **Add a brief quantitative comparison of noise injection strategies**: Even a small table showing structure distance and CLIP score for the linear, variance-preserving, and max strategies (at one or two settings of λ₁, λ₂) would substantiate the claim that linear works best and help practitioners apply the method.

## Score and Decision

**Originality**: 7/10 — First inversion method for discrete diffusion is genuinely novel.  
**Importance of research question**: 8/10 — Fills a clear gap; controlled editing in discrete generative models is timely.  
**Claims support**: 6/10 — Image editing claims are well-supported; text editing claims are weakened by ChatGPT-only evaluation and an overstated RoBERTa claim.  
**Soundness of experiments**: 6/10 — Image experiments are sound with standard metrics; text editing evaluation methodology is a concern.  
**Clarity of writing**: 6/10 — Core ideas are communicated but the methods section could be better organized; parser artifacts in the extracted text do not affect this assessment of the original.  
**Value to community**: 7/10 — The method will likely be adopted for discrete-space editing tasks.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>