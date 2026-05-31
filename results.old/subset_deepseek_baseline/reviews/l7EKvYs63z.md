## Summary

This paper proposes DISCO (Diffusion-free SCORE matching), a method that learns a single, time-independent score function by minimizing a weighted mixture of \(q\)-weighted Fisher divergences. Unlike diffusion models that learn a family of time-dependent scores, DISCO yields a faithful estimate of the slightly perturbed data distribution, making exact conditional sampling straightforward via simple score clamping. The method is demonstrated to achieve competitive unconditional sample quality on FFHQ-64 and CIFAR-10 while dramatically outperforming diffusion-based heuristics in conditional sampling fidelity, even on elementary toy problems where prior methods produce biased samples.

## Strengths

- **Principled objective for conditional sampling:** The paper identifies a fundamental shortcoming of diffusion models—they cannot provide exact conditional samples—and directly addresses it by learning a single score that allows conditioning via (5). The derivation from a mixture of \(q\)-weighted Fisher divergences is theoretically sound, and Theorem 1 establishes that the practical DISCO loss has the same gradients as this principled objective.

- **Strong empirical validation of conditional sampling:** The low-dimensional experiments (Figure 1, Table 1) convincingly show that diffusion-based heuristics (Replacement, Gradient Guidance, TDS) produce highly biased conditional samples even on simple 2D problems, whereas DISCO (using tempered SMC) recovers the ground-truth conditional distribution. This provides a clean demonstration of the core advantage.

- **Competitive image generation and inpainting:** DISCO achieves FID scores close to EDM on FFHQ-64 (2.65 vs. 2.39) and outperforms it on unconditional sample quality compared to the “EDM Masked” baseline. In inpainting, DISCO consistently beats all heuristic baselines (Replacement, Gradient Guidance, RePaint, TDS) in both LPIPS and SSIM, approaching the performance of the task-specific EDM Masked model which was directly trained on conditional objectives.

## Weaknesses

### Fatal

None.

### Major

- **Training requires accurate posterior sampling from \(p_0(\mathbf{x}|\mathbf{x}_t)\):** The DISCO loss (13) involves sampling from \(p_0(\mathbf{x}|\mathbf{x}_t)\), which is intractable for continuous data. The paper resorts to using the empirical distribution (mini-batch or kNN approximations). While the empirical distribution is a valid proxy for the true data distribution, the approximation may introduce bias, especially with small mini-batches or in high dimensions where the nearest-neighbor assumption becomes noisy. The paper does not analyze how this approximation error affects the learned score or how sensitive the final model is to mini-batch size. This is a practical limitation that could undermine the theoretical guarantees.

- **Unconditional sample quality is not state-of-the-art:** The claim that DISCO “matches state-of-the-art diffusion models” is overstated. On CIFAR-10, DISCO achieves FID 3.58 vs. EDM’s 1.97—a clear gap. While FFHQ-64 results are close (2.65 vs. 2.39), this does not constitute matching state-of-the-art performance across benchmarks. The contribution is better framed as “competitive while enabling exact conditional sampling.”

### Minor

- The paper introduces “Masked DISCO Training” to handle conditional sampling points, and analogously defines “Masked DM Training” as a baseline to compare against. The masked training for DM is described as a heuristic that does not guarantee consistency—this is a valid point, but the evaluation of DISCO also uses masked training, so the comparison is fair. However, the paper could elaborate on why the masked term does not change the global optimum (appendix reference is given, but the argument is not summarized in the main text).

- The method for sampling from the conditional distribution is described as “tempered SMC” but no details are provided in the main paper or appendix (the appendix was stripped). This makes it hard to assess the computational cost and hyperparameters required to achieve asymptotically exact samples.

### Trivial

None.

## Nice-to-Haves

- A sensitivity analysis of the mini-batch size or kNN parameters used during training would strengthen confidence in the method’s robustness.
- An ablation study isolating the effect of the masked training objective (\(\gamma\) in (14)) on final sample quality and conditional fidelity could be informative.
- Comparison to other energy-based models without diffusion (e.g., deep energy models trained with score matching or contrastive divergence) would help contextualize the innovation.

## Novel Insights

Beyond the paper’s own contributions, the key insight is that the noise-conditioned training typical of diffusion models can be reinterpreted as a collection of proposals for a \(q\)-weighted Fisher divergence, allowing one to learn only the score of the clean (slightly perturbed) distribution. This reframing reveals that the time-dependent score fields of diffusion models are not a necessary ingredient for good generative performance; they are merely a tool to inform the model away from the data manifold. By replacing the family of scores with a single score plus noise-weighted proposals, the paper opens a route to score-based models that are both generative and sound for probabilistic inference.

## Suggestions

- Provide a more detailed explanation of the tempered SMC procedure used for conditional sampling, including algorithmic steps, kernel design, and computational cost relative to standard diffusion samplers.
- Include an empirical study of how the mini-batch size used for posterior sampling affects the learned score (e.g., by measuring the score error on held-out data).
- Clarify in the main text that the global optimum of the masked loss remains the true score (briefly summarize the proof in the appendix), to reassure readers that the masked objective does not corrupt the target.

## Score and Decision

**Score:** 7.5

**Decision:** Accept

The paper makes a substantial contribution by identifying a fundamental limitation of diffusion models for probabilistic reasoning and proposing a principled and effective alternative. The theoretical derivation is solid, the experiments clearly validate the advantage in conditional sampling, and the image results demonstrate that the approach does not sacrifice generation quality. The major weakness—the reliance on empirical posterior approximation during training—deserves further study but does not invalidate the paper’s core claims. The paper is of clear value to the community and moves beyond incremental improvements to diffusion models.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>