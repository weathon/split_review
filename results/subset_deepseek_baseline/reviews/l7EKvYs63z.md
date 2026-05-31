## Summary

This paper introduces DISCO (Diffusion-free SCORE matching), a method for learning a single time-independent score function for a slightly perturbed data distribution. The key idea is to minimize a weighted mixture of Fisher divergences with Gaussian proposals at different noise levels, which avoids the need for the time-indexed score fields used in diffusion models. The main advantage is that conditional sampling becomes straightforward—one simply clamps the observed variables in the learned score field—enabling asymptotically exact conditional inference. Experiments on 2D distributions and image datasets (CIFAR-10, FFHQ-64) show that DISCO achieves competitive unconditional sample quality while dramatically outperforming diffusion-based heuristics in conditional sampling fidelity.

## Strengths

- **Principled theoretical framework**: The paper provides a clean derivation of the DISCO loss (Theorem 1) showing that minimizing the proposed objective is equivalent to minimizing a weighted mixture of Fisher divergences, with the global optimum being the true score of the slightly perturbed data distribution. The masked training variant is also shown to preserve the same global optimum.

- **Addresses a fundamental limitation of diffusion models**: The paper correctly identifies that exact conditional sampling is intractable for diffusion models because conditioning information is only available for clean data, not for noisy latent variables. DISCO elegantly sidesteps this by learning a single score field, making conditional sampling as simple as clamping observed coordinates.

- **Strong empirical validation on conditional sampling**: The low-dimensional experiments (Figure 1, Table 1) convincingly demonstrate that diffusion-based heuristics (Replacement, Gradient Guidance, TDS) produce biased conditional samples even on simple 2D problems, while DISCO matches the ground truth distribution. The quantitative inference quality metrics show DISCO achieving an order of magnitude lower Wasserstein distance than all baselines.

- **Competitive unconditional generation**: DISCO achieves FID of 2.65 on FFHQ-64 (vs EDM 2.39) and 3.58 on CIFAR-10, demonstrating that learning a single score field does not necessarily sacrifice sample quality. This challenges the prevailing assumption that diffusion processes are essential for high-quality score-based generation.

## Weaknesses

### Major

1. **Unclear conditional sampling procedure for high-dimensional data**: The paper claims that conditional sampling is "de-facto trivial" by fixing observed variables, but never specifies the actual sampling algorithm used for image inpainting experiments. For low-dimensional experiments, "tempered SMC" is mentioned in a figure caption but not explained in the main text or appendix (which is stripped). If the same ODE solver (Heun sampler) is used with clamped variables, the paper should discuss whether this produces exact conditional samples or introduces approximation error, and how this relates to the asymptotic guarantees claimed. This is a critical missing detail that undermines the core claim of "exact conditional sampling" in high dimensions.

2. **Mixed empirical results against the EDM Masked baseline**: The paper introduces EDM Masked as a baseline that trains on masked diffusion objectives. In Table 2, EDM Masked outperforms DISCO on most inpainting metrics (e.g., on FFHQ-64: Wide LPIPS 0.104 vs 0.119, Narrow LPIPS 0.016 vs 0.027, Super-Resolve LPIPS 0.048 vs 0.068). The paper dismisses EDM Masked as not providing "consistent conditionals," but the empirical results show it produces better inpainting quality. The paper should more honestly discuss this trade-off between conditional consistency and practical performance. Additionally, on CIFAR-10 unconditional generation, EDM Masked achieves better FID (2.59) than DISCO (3.58), so the claim of "better unconditional samples on FFHQ-64" is dataset-dependent.

3. **Scalability concerns for posterior sampling during training**: DISCO training requires sampling from \(p_0(\mathbf{x} | \mathbf{x}_t)\), which for the empirical data distribution is a softmax over all training points. The paper mentions mini-batch approximation or kNN, but only tests on CIFAR-10 (50k images) and FFHQ-64 (70k images). For larger datasets like ImageNet (1.2M images), the mini-batch approximation may introduce significant bias, and kNN in pixel space may be ineffective. The paper does not discuss how this scales or provide experiments on larger datasets.

4. **Theoretical gap between global optimum and practical optimization**: The paper proves that the global minimum of \(\mathcal{L}_{\text{DISCO}}^{\text{mask}}\) is the same as \(\mathcal{L}_{\text{DISCO}}\), but this assumes sufficient model capacity and convergence to the global optimum. In practice, the masked loss changes the optimization landscape, and the paper does not analyze whether this introduces bias in finite-capacity models or affects convergence. The empirical success on 2D data is encouraging, but the high-dimensional results show some degradation compared to diffusion models.

### Minor

- The paper claims DISCO "yields a more faithful representation of the underlying data distribution" but the evidence for this is primarily from 2D examples (Figure 2). The FID scores on image datasets are competitive but not state-of-the-art, and the claim of "faithful representation" is not directly measured beyond FID.
- The related work discussion of Li et al. (2023) and Sun et al. (2025) is useful but these are relatively obscure references; the paper could better contextualize how DISCO differs from more well-known approaches.
- The paper does not report uncertainty or confidence intervals for the FID scores in Table 3, which is standard practice for generative model evaluation.

## Nice-to-Haves

- Clarify the exact conditional sampling algorithm used for image inpainting (e.g., is it the same ODE solver with clamped variables? If so, discuss approximation error and how it relates to the "asymptotically exact" claim).
- Include experiments on a larger dataset (e.g., ImageNet 64x64) to demonstrate scalability of the posterior sampling approximation.
- Provide an ablation study on the effect of the mini-batch size for posterior sampling during training.
- Compare with more recent conditional sampling methods for diffusion models (e.g., DPS, MCG) to strengthen the baseline comparison.

## Novel Insights

The paper's core insight is that one can learn a single score field for a slightly perturbed data distribution by minimizing a mixture of Fisher divergences with proposals at different noise levels, without needing to learn the scores of those noisy distributions. This is a clever reinterpretation of diffusion training: the noisy distributions serve only as proposals to ensure the score is learned far from the data manifold, not as targets for separate score fields. This reframing reveals that the time-dependence in diffusion models is not strictly necessary for learning expressive score functions, and that the diffusion process itself is what makes conditional sampling intractable. The paper thus provides a principled path to score-based models that can serve as sound probabilistic reasoners.

## Suggestions

- Clearly specify the conditional sampling algorithm used for image experiments in the main text. If using an ODE solver with clamped variables, state this explicitly and discuss the approximation error relative to exact conditional sampling.
- Add a discussion of the trade-off between conditional consistency (where DISCO excels) and inpainting quality metrics (where EDM Masked sometimes excels), and explain why practitioners might prefer one over the other.
- Include an analysis of how the mini-batch size for posterior sampling affects training stability and final model quality.

## Score and Decision

The paper presents a novel and principled approach to score matching that directly addresses a fundamental limitation of diffusion models—exact conditional sampling. The theoretical contribution is solid, and the low-dimensional experiments convincingly demonstrate the failure of existing heuristics and the success of DISCO. The image experiments show competitive unconditional generation and reasonable inpainting performance. However, the lack of clarity on the high-dimensional conditional sampling procedure and the mixed results against the EDM Masked baseline are significant concerns that should be addressed. Overall, the paper makes a valuable contribution to the community and the core ideas are sound.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>