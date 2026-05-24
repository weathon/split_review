## Summary

This paper proposes **Marginal Flow**, a density estimation framework that defines a model $q_\theta(x)$ as a finite mixture $q_\theta(x) = \frac{1}{N_c}\sum_i q(x|w_{\theta,i})$ where the parameters $w_{\theta,i}$ are resampled from a learnable distribution $q_\theta(w)$ at each evaluation. The key innovation is that $q_\theta(w)$ is never evaluated — only sampled — via an unconstrained neural network $f_\theta(z)$ that transforms a base distribution into parameter space. This design simultaneously enables exact density evaluation, efficient single-step sampling, training with any objective (forward or reverse KL), learning on lower-dimensional manifolds, and flexibility to choose the parametric family $q(x|w)$. The paper validates the approach on synthetic data, simulation-based inference, Wishart matrices, and latent-space manifold learning on MNIST/JAFFE.

## Strengths

- **Novel and well-motivated framework.** The core idea — marginalizing over resampled parameters from a learnable distribution rather than optimizing a fixed set of mixture components — is conceptually simple, clearly explained (Figure 1), and unambiguously distinguishes Marginal Flow from a standard GMM. The framework simultaneously achieves properties (exact density, efficient sampling, no architectural constraints, manifold learning, flexible training objectives) that no single prior method achieves, as systematically shown in Table 1.

- **Empirical evidence of orders-of-magnitude speed advantage.** Figure 3 shows runtime for sampling and exact density evaluation across dimensions $10^2$–$10^5$, where Marginal Flow is consistently faster than NF, FM, and FFF, often by 10–100×. This is concrete, quantitative support for the central efficiency claim. Figure 7 further demonstrates that Marginal Flow reaches high test log-likelihood orders of magnitude faster in wall-clock time during training.

- **Demonstrated effectiveness on challenging tasks beyond 2D toy data.** The Wishart mixture experiment (Figure 9, $d=55$ and $d=5050$) shows that Marginal Flow achieves test KL ≈ 0.0088 vs. NF's ≈ 0.82 and can scale to settings where NF is computationally prohibitive. The reverse KL training experiments (Figure 8) show successful training without any data, which is only possible for models with efficient exact likelihood and efficient sampling simultaneously.

- **Flexibility is concretely demonstrated across multiple axes.** The paper validates: (a) lower-dimensional manifold learning (Figure 4 spiral), (b) multi-modality handling (Figure 5), (c) training with both forward and reverse KL, (d) custom parametric families (Gaussian → Wishart for positive-definite matrices), and (e) conditioning (SBI, image manifolds). This breadth supports the claimed flexibility.

## Weaknesses

### Major

- **No analysis of how $N_c$ affects the approximation quality, and no guidance for choosing it.** The model is defined as $q_\theta(x) = \frac{1}{N_c}\sum_i q(x|w_{\theta,i})$, and the paper correctly states this density is exact for the defined model. However, the framework is motivated as an approximation to the marginal in Eq. 1, where $N_c$ controls fidelity. The paper neither discusses the variance of the density estimator as a function of $N_c$, nor provides any empirical analysis (e.g., "how does test log-likelihood change with $N_c$?"), nor recommends a default value. The paper states "the modeling capacity is not directly linked to $N_c$ anymore" (line 68), which is a strong claim about the marginalization benefit that requires empirical support — without it, the reader cannot assess the cost-quality trade-off that is central to the method's practical deployment. This is the single most important unaddressed question in the paper.

- **High-dimensional density accuracy is not validated on standard benchmarks.** The synthetic experiments are 2D. The Wishart experiment goes to $d=55$ (density accuracy) and $d=5050$ (manifold reconstruction only, no density accuracy). The image latent spaces are 10–20D. The paper does not evaluate on common high-dimensional density estimation benchmarks (e.g., POWER, GAS, HEPMASS, MINIBOONE from the NF literature). Figure 3 demonstrates impressive runtime scaling but does not validate that the learned density is accurate at those high dimensions. The central practical question — whether the mixture approximation works in moderate-to-high dimensions with a tractable $N_c$ — remains partially unanswered.

### Minor

- **Image manifold experiments (Section 4.4) are purely qualitative.** While the MNIST and JAFFE visualizations are interesting and show coherent interpolation behavior, no quantitative evaluation is provided: no held-out log-likelihood, no comparison to a baseline (e.g., a Gaussian conditioned on label, or a standard VAE prior), and no assessment of manifold coverage. The synthetic spiral (Figure 4) provides evidence for the manifold-learning claim in 2D, but the image experiments do not demonstrate that Marginal Flow's learned density is more accurate than simpler alternatives.

- **Uniform base distribution in multi-modal comparison (Figure 5) may handicap baselines.** The paper states "For a fair comparison, all models use a uniform base distribution." However, Normalizing Flows and Flow Matching typically perform better with a Gaussian base. Since the target mixture has Gaussians with different covariances, a uniform base may artificially handicap bijective models. The paper should acknowledge this or provide a comparison with each model using its typical configuration.

- **Runtime comparison lacks the $N_c$ value used.** Figure 3 is a centerpiece of the efficiency claim, but the main text does not state what $N_c$ was used for Marginal Flow. The paper refers to "Appendix A.3.1" for details, but since runtime is linear in $N_c$, the reader cannot judge whether the speed advantage is robust or configured to be favorable. Reporting runtime as a function of $N_c$ alongside accuracy would be more informative.

### Trivial

- None.

## Nice-to-Haves

- A brief quantitative summary of the SBI results (e.g., C2ST scores) in the main text (Section 4.2) would strengthen the claim of state-of-the-art performance, which is currently deferred to the appendix.

## Removed Points

- **"Bias of the log-density estimator in reverse KL training"** — Removed. The reparameterization gradient through $w_i = f_\theta(z_i)$ with fixed base samples $z_i$ provides a standard, unbiased Monte Carlo gradient estimator of $\nabla_\theta \mathbb{E}[\log q_\theta(x)]$. This criticism reflects a misunderstanding of the gradient estimation procedure.

- **"SBI results only in appendix"** — Removed. The appendix was stripped by the parser; the paper explicitly states the full results are in Figure 14 of the appendix. The claim is supported in the submitted artifact.

- **"Missing implementation details"** — Removed. The paper states these are in Appendix A.1 and A.3. Reproducibility concerns about details that exist in the appendix (which was stripped by the parser) should not be counted as weaknesses.

- **"Missing related works"** — Removed per instructions.

- Generic "evaluation lacks rigor" / "evidence is weak" framing without specific anchors — Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's characterization: the core idea is novel and well-supported empirically, but the analysis of the Monte Carlo approximation ($N_c$) is a gap that the paper itself does not adequately address.

## Suggestions

1. **Add an analysis of $N_c$.** In a few synthetic settings (e.g., 2D checkerboard, higher-dimensional tabular data), show how test log-likelihood and its Monte Carlo variance change as a function of $N_c$. Provide a practical recommendation for $N_c$ (or an adaptive scheme). This would directly address the main open methodological question.

2. **Validate density accuracy on a standard high-dimensional benchmark.** Evaluate on POWER, GAS, HEPMASS, or MINIBOONE and report test log-likelihood with confidence intervals. Even if Marginal Flow does not achieve state-of-the-art log-likelihood, showing competitive accuracy at the reported speed advantage would be a compelling result.

3. **Quantify the image manifold experiments.** On MNIST, compute held-out log-likelihood of the latent-space density under the learned conditional model and compare to a simple baseline (e.g., a label-conditioned Gaussian in VAE space).

4. **State the $N_c$ used in Figure 3 in the main text** and ideally add a panel showing runtime vs. $N_c$ vs. accuracy to expose the trade-off.

## Score and Decision

**Round 1 bracket:** After reading the paper and the initial calibration search (weak anchors ~3.0–3.25, middle anchors ~4.0–6.25, strong anchors ~8.0), I placed the paper in the **5–7 range**.

**Round 2 narrowing:** I retrieved additional anchors focused on density estimation and flow-based methods in the (4.5, 6.5) and (6.0, 7.5) bands. Comparing the paper to:

- *Injective flows for star-like manifolds* (6.0, accepted ICLR): That paper proposes exact determinant computation for a restricted manifold class. Marginal Flow has broader scope, more experiments across diverse domains, and a simpler, more broadly applicable idea. **Marginal Flow is clearly the stronger paper.**

- *Lifting Architectural Constraints of Injective Flows* (6.5, accepted): Comparable contribution level, both address limitations of existing flow-based methods. That paper has stronger empirical validation (ablations, tabular benchmarks) but narrower scope. Marginal Flow has broader applications (Wishart, SBI, manifolds) but weaker analysis of its own method ($N_c$ choice). **Comparable overall.**

- *Subtractive Mixture Models via Squaring* (7.2, accepted): Strong theoretical results (exponential expressiveness proofs) and good experiments. Marginal Flow lacks comparable theoretical analysis of expressiveness but has broader empirical validation across more diverse tasks. **Slightly weaker due to missing theoretical grounding.**

- *Flow-based Variational Mutual Information* (6.0, accepted): Flow-based extension of existing estimators. Marginal Flow has comparable novelty and broader experimental validation. **Similar quality.**

**Final score:** After the narrowing pass, the paper sits at the upper end of the 5–7 bracket — it has a genuinely novel idea, clear empirical strengths, and broad validation across diverse tasks. However, the missing analysis of $N_c$ and the lack of high-dimensional benchmark validation are real gaps that prevent the paper from being a strong accept (7+). A 6.0 reflects a solid accept: the contribution is clear and demonstrated, but with specific, addressable weaknesses.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>