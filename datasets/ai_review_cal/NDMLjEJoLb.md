- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 8, 3
Now I have a thorough understanding of the paper and have verified the relevant claims. Here is my consolidated final review.

---

## Summary

This paper proposes a prompt-mixing algorithm for text-to-image diffusion models that draws an analogy between the Black-Scholes option-pricing model and the diffusion denoising process. It maps diffusion quantities (CLIP score, scheduler variance, remaining steps) to Black-Scholes variables, computes a score for each text prompt at every denoising step, and conditions the model on the lowest-scoring prompt. Experiments are conducted on 4 prompt-pair scenarios (20 images total) with comparisons to vanilla SD, linear interpolation, alternating/step-wise switching, and CLIP-min selection.

## Strengths

- **Novel conceptual framing**: The paper is the first to connect option pricing theory to prompt mixing in diffusion models, defining explicit variable mappings (spot price = CLIP score, volatility = scheduler variance, etc.) and producing a concrete, reproducible algorithm (Algorithm 1). This cross-domain analogy is creative and opens a new direction for prompt selection.

- **Qualitative evidence of improved blending**: Figures 1 and 2 show that the Black-Scholes method produces images that more visibly combine features of both prompts (e.g., parrot colors on dog shape) compared to baselines, which exhibit missing characteristics, artifacts, or bias toward one prompt.

- **Systematic scenario coverage**: The evaluation spans 4 distinct complexity types (single object, multiple objects, object+background, style blending), demonstrating the method is tested across varied blending challenges rather than a single simple case.

- **Honest scope boundaries**: Section 6 explicitly acknowledges the method may not apply to non-Gaussian or one-step diffusion models, providing clear limitations.

## Weaknesses

### Major

- **No ablation validating the Black-Scholes formula itself**: The paper's core claim is that the Black-Scholes formula provides a meaningful selection signal. Yet there is no ablation comparing Black-Scholes selection against simpler alternatives — e.g., always picking the lowest CLIP score (CLIP-min), lowest CLIP score with a time-decay factor, or random selection among low-scoring prompts. The existing CLIP-min baseline is close to the method but the only difference is the Black-Scholes formula, and without an ablation the paper does not demonstrate that the formula's specific structure (the log-ratio, normal CDF terms, etc.) matters. This severely undercuts the central contribution.

- **Evaluation scope is too thin for the claims made**: Quantitative results are reported for only 4 prompt pairs with 5 images each (20 images total). No error bars, confidence intervals, or statistical tests are provided. The paper claims "superior results" and "significant benefits," but the sample is too small to distinguish systematic improvement from noise. A method paper claiming a novel selection rule should demonstrate robustness over substantially more diverse prompts and random seeds.

- **Contradiction regarding "no hyperparameter tuning"**: The abstract and introduction claim the method "operates without human intervention or hyperparameter tuning." However, Section 4.2 (line 210) states: *"Based on our experiments for the vanilla combination using Stable Diffusion 2.1... we opted for a constant value of 0.25 for the strike price."* This is a manually set hyperparameter determined through experimentation, directly contradicting the claim.

- **Missing comparisons to relevant baselines cited in the paper**: Attention-based guidance methods (Chefer et al. 2023, Hong et al. 2023, Zheng et al. 2023) and mixing-time approaches (Zhu et al. 2023, 2024) are discussed in the related work and the introduction acknowledges they "excel at guiding the model toward distinct scene entities." These are natural competitors for the concept-blending task and should be included as baselines. Their absence leaves the positioning of the method unclear relative to the most relevant prior work.

- **The Black-Scholes mapping is heuristic and its behavior is unanalyzed**: The paper defines mappings between Black-Scholes and diffusion variables, but no analysis shows that (a) the Black-Scholes score correlates with "which prompt needs attention" or (b) the formula behaves as intended (e.g., choosing different prompts in early vs. late steps, or systematically focusing on the deficient prompt). The risk-free rate r=1/T is chosen "to yield equal proportions of returns" without principled justification. Without understanding the selection dynamics, the method reads as CLIP-min with a time-dependent multiplier of unknown utility.

### Minor

- **No discussion of the per-step decoding cost as a limitation**: Computing the "extrapolated clean latent" z_{0,t} and evaluating its CLIP score at every denoising step requires a forward pass through the UNet and VAE decoder per step. The paper reports runtime (~44s) but does not acknowledge this as a practical limitation or compare the cost-benefit tradeoff against simpler methods.

- **Potential stability concern with per-step text conditioning changes**: Algorithm 1 switches text embeddings at every denoising step. Stable Diffusion was trained with a fixed text condition throughout generation. The paper does not analyze whether the method's improvements arise from intelligent selection or from the network exploiting conditioning artifacts from rapid switching.

### Trivial

- The BLIP and DINO metric descriptions (lines 197–205) do not provide specific citations to the original methods; adding these would improve reproducibility.
- Section 3.2.2–3.2.3 (thermodynamic and SDE analogies) is extensive but none of the PDE, free-energy, or SDE concepts are used in the algorithm. This space could be repurposed for analysis or ablation.

## Nice-to-Haves

- Adding error bars or confidence intervals would substantially strengthen the quantitative claims.
- An analysis of which prompt is selected at each denoising step for a few examples would build intuition about the method's behavior.
- Extending the evaluation to 15–20 diverse prompt pairs would make the "superior results" claim credible.

## Removed Points

These points from the reviewers are excluded or demoted with justification:

- **"CLIP scores reported are surprisingly low (0.33 for CLIP-combined)"**: The paper describes 0.25 as "reasonable alignment" and 0.33 is higher than that, so this is not a valid criticism. The specific numbers cannot be verified from the paper text (Table 1 is an image), and the critic provides no reference distribution for what CLIP scores "should" be in this setting. **Removed as not a valid weakness.**

- **"KID score (6.25) is very high, indicating poor image quality"**: The specific KID value cannot be verified from the prose (it is in the table image), and no baseline KID values for this task are provided to contextualize what "high" means. **Removed as unverifiable from paper text.**

- **"The baseline for 'Step' uses a fixed switching range that was presumably not tuned for each prompt"**: This is speculation about the baseline, not a flaw in the paper. The Step baseline follows Patashnik et al. (2023) as described. **Removed as speculation.**

- **"BLIP score for text-image alignment is not standardly used as a sole metric"**: BLIP score is a standard metric for text-image alignment in generation tasks. **Removed as factually inaccurate.**

- **"DINO score... needs a citation or validation"**: The paper's DINO description is a reasonable use of self-supervised feature similarity for concept preservation. While a citation would be nice, this is not a substantive weakness. **Demoted to Trivial.**

- Various formatting/presentation nitpicks and generic scope-creep demands ("should the paper also address X") are removed per the filtering rules.

- Strength Finder's claim about "Fully automated, data-efficient procedure without human intervention" is partially contradicted by the manually tuned K=0.25, so it is not included in Strengths.

## Novel Insights

None beyond the paper's own contributions. The cross-analogy between Black-Scholes and diffusion is creatively drawn, but neither reviewer surfaces an insight about the paper that was not already stated by the authors.

## Suggestions

1. **Ablate the Black-Scholes formula**: Compare against at least two simpler selection rules — (a) "lowest CLIP score with a time-dependent multiplier" and (b) "random selection among the bottom-K CLIP-scoring prompts." If Black-Scholes outperforms these, its specific form is justified.

2. **Scale the evaluation**: Report results on at least 15–20 prompt pairs with multiple seeds per pair, including error bars. Add attention-based baselines (Chefer et al., Hong et al.) and mixing-time baselines (Zhu et al.) to properly situate the method.

3. **Analyze selection dynamics**: For 2–3 examples, show which prompt is selected at each denoising step and how the Black-Scholes score evolves. This would build intuition and demonstrate the method is doing something non-trivial.

4. **Resolve the hyperparameter contradiction**: Either remove the "no tuning" claim and acknowledge K as a tunable parameter, or provide evidence that the method is robust to a wide range of K values.

5. **Report per-step cost as a limitation**: Explicitly discuss the computational cost of the per-step CLIP evaluation and whether it affects practical usability.
