## Summary

This paper argues that high-dimensional diffusion models do not actually learn the statistical quantities (posterior, score, velocity field) they are assumed to learn, because data sparsity causes the fitting target of the training objective to degrade from a weighted sum of multiple samples to a single sample. The authors support this with empirical degradation rates on ImageNet (Tables 1–2) showing high degradation rates for most timesteps, and propose a "Natural Inference" framework that unifies existing sampling methods (DDPM, DDIM, Euler, DPM-Solver, etc.) as linear combinations of $x_0$ predictions and noise, free of statistical concepts.

---

## Strengths

- **Empirical demonstration of weighted-sum degradation on real datasets**: Tables 1 and 2 compute degradation rates for ImageNet-256 and ImageNet-512 under both VP and Flow mixing, showing that for many timesteps ($t < 600$), the posterior probability mass concentrates on a single training sample, with degradation rates approaching 1.00. This provides concrete quantitative evidence for the degradation phenomenon.
- **Mathematical derivation of the degradation mechanism**: Equations 13–15 derive the posterior form $p(x_0|x_t)$ from a discrete empirical data distribution, showing that the posterior mean is a weighted sum with weights inversely proportional to distance. The analysis makes the link between data sparsity and target collapse explicit.
- **Unified expression of diverse inference methods**: Section 4.3 and Appendix C show that first-order methods (DDPM, DDIM, Euler, SDE Euler, Flow Matching Euler) and higher-order methods (DPM-Solver, DPM-Solver++, DEIS) can all be expressed as a linear combination of $x_0$ predictions plus noise, with signal coefficients summing to $\sqrt{\bar{\alpha}_t}$ and noise coefficients summing to $\sqrt{1-\bar{\alpha}_t}$. This provides a coherent algebraic common structure.
- **Frequency-domain perspective (Section 3.3)**: The interpretation of the training objective as filtering and completing noise-submerged frequency components offers an intuitive, visual way to think about what the model does, complementing the algebraic analysis.

---

## Weaknesses

### Fatal
None.

### Major

1. **The paper does not provide direct evidence that degradation prevents the model from learning the posterior mean.** The Bayes-optimal solution of the training objective is $\mathbb{E}[x_0|x_t]$. When the posterior is sharply peaked at a single sample, the posterior mean *is* approximately that sample — the model can still learn this mapping. The paper's argument that degradation "hinders learning" conflates two distinct claims: (a) the posterior mean is approximately a single sample (which the degradation analysis demonstrates), and (b) the model cannot learn this posterior mean. Claim (b) does not follow from (a). The paper does not compare the learned model's predictions to the true posterior mean on any controlled problem, nor does it show that prediction error correlates with degradation rate. Without this evidence, the paper's central thesis rests on a logical gap.

2. **The paper contains no generative training or sampling experiments whatsoever.** Given the strong claims about how diffusion models "actually work," the complete absence of any generative experiment — even on a toy dataset — is a significant weakness. The paper would be substantially strengthened by (a) training a diffusion model on a low-dimensional synthetic problem where the true posterior is computable and showing whether the learned function deviates from it, or (b) demonstrating that the Natural Inference perspective enables a new sampler or improved performance. As it stands, the paper remains a theoretical reinterpretation whose practical implications are unverified.

### Minor

1. **The Natural Inference framework is a valid algebraic reformulation but does not constitute a novel discovery.** The fact that first-order linear update rules $x_{t-1} = d_{t-1}x_t + e_{t-1}y_t + g_{t-1}\epsilon_{t-1}$ can be unrolled into linear combinations of $\{y_i\}$ and $\{\epsilon_i\}$ follows directly from the definitions of these samplers. The paper does not derive any new sampler from this framework or show that it enables capabilities not already possible. The pedagogical value of the unification is real, but the paper's framing as a "novel inference framework" that "opens up a promising new direction" overstates its contribution.

2. **The degradation threshold of 0.9 is arbitrary, and the analysis treats each $x_t$ in isolation.** The results would be more informative as a continuous function of posterior probability rather than a binary threshold. Additionally, the analysis considers each $(x_0, x_t)$ pair independently, but during training the model sees the aggregate distribution of pairs — generalization depends on this aggregate, not on individual posteriors. The paper does not address how the model might interpolate across the data manifold despite individual degradation.

3. **The frequency-domain interpretation (Section 3.3) essentially restates Dieleman (2024)** (which the paper cites), and adds limited new insight beyond what the blog post already presents.

### Trivial
None.

---

## Nice-to-Haves

- Train a diffusion model on a controlled low-dimensional problem where the true posterior mean is computable, and measure the error between the model's predictions and the true posterior mean as a function of degradation rate. This would directly test whether degradation correlates with failure to learn.
- Propose and evaluate a new sampler derived from the Natural Inference framework that departs from existing methods and achieves better results (e.g., lower FID, faster sampling) — this would turn the reformulation into a practical contribution.
- Present the degradation statistics as a continuous function of the posterior probability rather than a binary 0.9 threshold, and discuss sensitivity to this threshold.

---

## Removed Points

These points were flagged by the reviewers but are removed from the main review for the following reasons:

- **Criticism that the "Natural Inference" coefficients are only approximate for higher-order methods** — The paper acknowledges this explicitly ("the approximation error decreases as the number of sampling steps increases") and provides figures showing this. This is a known feature of the analysis, not a flaw.
- **Criticism that symbolic computation is "a workaround, not a proof"** — The paper uses symbolic computation as a practical tool to verify coefficient sums, which is standard practice for complex algebraic computations. This does not undermine the validity of the results.
- **Criticism about the paper not addressing the "train-test consistency"** — The paper explicitly frames this as an advantage (Section 4.4, bullet 1). The criticism misreads what the paper claims.
- **"The frequency perspective adds no new insight beyond Dieleman (2024)"** — While the core frequency perspective predates this paper, the paper integrates it into a broader argument about degradation and the Natural Inference framework, which goes beyond the original blog post.

---

## Novel Insights

None beyond the paper's own contributions. The reviewers' inputs surface a genuine logical gap in the paper's central argument (degradation does not imply failure to learn the posterior mean) that was not addressed by the paper itself. The insight that the paper's reasoning conflates two logically distinct claims — that the posterior mean collapses to a single sample, and that the model therefore cannot learn statistical quantities — is the most useful observation to emerge from the review process.

---

## Suggestions

1. **Add a controlled experiment**: Train a diffusion model on a low-dimensional synthetic mixture of Gaussians where the true posterior mean is analytically computable. Compare the learned model's predictions to the true posterior mean at varying noise levels. If degradation causes learning failure, prediction error should increase when the posterior is peaked. This single experiment would directly test the paper's central hypothesis.
2. **Temper the claims**: The paper's framing ("first rigorous analysis," "opens up a promising new direction") outpaces the evidence presented. Softening these claims to match what is actually demonstrated — that the posterior mean collapses in high dimensions and that inference methods can be understood as linear combinations of $x_0$ predictions — would align the paper's language with its contributions.
3. **Leverage the Natural Inference framework to derive something new**: Even a simple variant of an existing sampler, justified by the framework and evaluated on a standard benchmark (e.g., CIFAR-10 or ImageNet FID), would transform the framework from a post-hoc unification into a generative tool.

---

## Score and Decision

**Calibration anchors (all rounds):**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Instability in Diffusion ODEs (R8V7QB6DDY) | 2.80 | 1 | Weaker — analysis is less directly supported by empirical data |
| Diffusion Models are Kelly Gamblers (IaeZcYpRxD) | 3.00 | 1 | Similar — both are theoretical reinterpretations with limited experiments |
| Generative Diffusion Models for High-Dim Time Series (N4xPiyv6fN) | 3.00 | 1 | Similar scope but different topic |
| Unconditional CNN denoisers (Nt9DnwHFsC) | 3.50 | 2 | Similar — both analyze what diffusion models learn internally |
| Diffusion models are optimal for hypothesis testing (rqiSfqoNqP) | 3.50 | 2 | Similar — theoretical paper on diffusion model limitations |
| Elucidating the design space (um7F9IxlwD) | 3.50 | 2 | Similar — unifying framework paper, though with more experiments |
| Collapse Errors (iSO1WFjSKh) | 4.00 | 2 | Stronger — identifies a concrete failure mode with experimental validation |
| Selective Underfitting (yqTajvdkjv) | 3.33 | 2 | Similar — analyzes what diffusion models actually learn |
| Diffusion Bridge or Flow Matching? (xBJXnorMJ7) | 4.50 | 2 | Stronger — combines theory with comprehensive experiments |

**Round 1 bracket**: The paper falls between 2.8 and 4.5. Its empirical evidence (Tables 1–2) places it above the 2.8–3.0 anchors, but the absence of generative experiments and the logical gap in the central argument keeps it below 4.0.

**Round 2 narrowing**: The paper is most comparable to the 3.33–3.50 anchors (Selective Underfitting, Unconditional CNN denoisers). It has slightly more concrete empirical evidence than those papers (actual degradation statistics on ImageNet), but its central claim is less directly supported by the evidence presented. It is clearly weaker than Collapse Errors (4.00) which provides experimental validation for its identified phenomenon.

**Final score**: 3.5. The paper identifies a real and interesting phenomenon (weighted-sum degradation) and offers a coherent unifying framework for inference. However, its core claim — that this degradation prevents learning of statistical quantities — lacks direct evidence and contains a logical gap (degradation of the posterior to a single sample does not imply the model cannot learn the posterior mean). The absence of any generative experiments further weakens the case. The paper reads as a provocative position piece rather than a substantiated analysis, and the contribution is not commensurate with the strength of the claims.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>