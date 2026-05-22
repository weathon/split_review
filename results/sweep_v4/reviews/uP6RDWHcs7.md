## Summary

Marginal Flow introduces a density estimation framework where the model $q_\theta(x)$ is defined as a Monte Carlo average over a parametric distribution $q(x|w)$ whose parameters $w$ are sampled from a learnable distribution $q_\theta(w)$. By drawing $w$ through an unconstrained neural network $f_\theta(z)$ applied to a base distribution, the model achieves simultaneous exact density evaluation and efficient single-step sampling — a combination not available in most existing generative models. The framework is flexible: it supports arbitrary parametric families for $q(x|w)$, lower-dimensional manifold learning, multi-modal targets, and training with both forward and reverse KL divergence. Experiments on synthetic data, Wishart mixtures, SBI, and image latent spaces demonstrate orders-of-magnitude speedups in training and inference over normalizing flows, flow matching, and free-form flows.

## Strengths

1. **Simultaneous exact density evaluation and efficient sampling (Table 1, Figure 3).** Marginal Flow is the only model in the comparison that provides both efficient exact likelihood and efficient single-step sampling. The runtime benchmarks (Figure 3) confirm orders-of-magnitude advantage across dimensions 100–100,000 for both operations.

2. **Orders-of-magnitude faster training convergence (Figure 7).** On five synthetic datasets, Marginal Flow reaches near-optimal test log-likelihood in seconds of wall-clock time, while Normalizing Flow, Flow Matching, and Free-form Flow require orders of magnitude longer to converge. This is a clean and well-executed set of experiments.

3. **Principled manifold learning without architectural constraints (Figure 4).** Unlike Normalizing Flows and Flow Matching, Marginal Flow can learn densities on lower-dimensional manifolds by simply choosing a lower-dimensional base distribution, while still providing exact density evaluation. The spiral toy example cleanly demonstrates this capability.

4. **Framework flexibility — choice of $q(x|w)$ (Section 4.3).** The Wishart experiment demonstrates that switching $q(x|w)$ from Gaussian to Wishart enables learning distributions on positive-definite matrices up to $100\times100$ ($d=5050$), a setting where Normalizing Flows are computationally prohibitive. This concretely validates the claimed flexibility.

5. **Reverse KL training without observations (Figure 8).** Marginal Flow achieves lower test reverse KL than Normalizing Flow on all four synthetic datasets, with visibly sharper density heatmaps. This is a genuine advantage enabled by the model's efficient sampling.

## Weaknesses

### Major

1. **Missing comparison to the most natural baseline: a well-tuned GMM.** The paper's motivation (Section 2.1, Figure 1) explicitly contrasts Marginal Flow with a finite GMM, arguing that resampling $w$ yields smoother, more expressive densities than optimizing fixed mixture components. Yet no experiment quantitatively compares Marginal Flow against a GMM trained by EM with a large number of components (e.g., 500–1000). Without this baseline, it is unclear whether the claimed benefits of marginalization versus simple mixture optimization translate to measurable performance gains on any task. This is the single most consequential gap in the evaluation.

2. **No evaluation on standard high-dimensional density estimation benchmarks.** The paper claims Marginal Flow is a general-purpose density estimation framework, but all non-manifold density evaluation experiments are on 2D synthetic data. The Wishart experiment (d=55, d=5050) is on a manifold, and the image latent experiments (10D–20D) are qualitative. There are no experiments on standard high-dimensional density estimation tasks (e.g., UCI tabular datasets with 50–100 dimensions) where log-likelihood is reported. This limits the evidence for the claim that the framework is a general alternative to methods like Normalizing Flows or Flow Matching in high-dimensional settings.

3. **Wishart experiment gap raises questions about baseline configuration (Figure 9).** Marginal Flow achieves test KL ≈ 0.0088 versus ≈ 0.82 for Normalizing Flow — two orders of magnitude difference. While this could reflect a genuine advantage, the paper does not provide sufficient analysis (e.g., architecture details, hyperparameter tuning effort for NF) to rule out the baseline being poorly configured for the Cholesky parameterization task. A sensitivity study or comparison with a stronger NF variant would substantiate the result.

### Minor

1. **No ablation of $N_c$ (number of Monte Carlo components).** The paper argues that modeling capacity is decoupled from $N_c$ due to resampling (Section 2.1), but never shows how density quality or runtime varies with $N_c$ (e.g., 10, 100, 1000). Since $N_c$ determines memory and compute at evaluation time, understanding this trade-off is important for practitioners.

2. **Stochastic density reproducibility.** The density $q_\theta(x)$ depends on a random draw of $\{w_i\}$, so repeated evaluations at the same $x$ yield different values. The paper does not discuss the variance of these estimates or whether a fixed seed / large $N_c$ is expected to stabilize them. This is not a flaw in the method, but a practical detail that should be addressed.

3. **Image latent experiments are qualitative only (Figures 10, 11).** The manifold learning on MNIST and JAFFE is visually interesting, but no quantitative density evaluation (e.g., log-likelihood on held-out latents) or reconstruction quality metrics are reported. These experiments demonstrate the model's flexibility but do not provide evidence of superiority over simpler alternatives (e.g., a GMM on the same latent space).

### Trivial

None.

## Nice-to-Haves

- An ablation comparing the neural-network-based $q_\theta(w)$ to a direct optimization of fixed mixture weights (i.e., an EM-trained GMM with matched component count) would directly substantiate the central motivation.
- Reporting the variance of the estimated log-likelihood across different random seeds for $w_i$ would address the stochastic density concern.
- Visualizing the learned distribution $q_\theta(w)$ (e.g., for the 2D synthetic experiments) would build intuition about what the neural generator has learned.

## Removed Points

- **"Stochastic density and the 'exact' claim" (Harsh Critic issue #3):** The critic argues that the model's likelihood is "misleading" because the marginal is approximated. However, the model *is defined* as $q_\theta(x) := \frac{1}{N_c}\sum q(x|w_{\theta,i})$ (Eq. 2), not as an approximation to some other distribution. Evaluating this expression is exact by construction. The Table 1 checkmark is therefore correct. VAEs cannot evaluate their marginal likelihood exactly without intractable integration. Removed as factually incorrect.

- **Criticism about "Efficient training" ✓ in Table 1 for GANs:** The critic argues GANs should also be marked ✓ for efficient training. The table marks GANs as ✗, which is standard — GAN training involves a minimax game and is notoriously unstable and computationally demanding per iteration. The comparison reflects standard convention from Bond-Taylor et al. (2021). Removed as a subjective disagreement.

- **"Suspiciously large gap in Wishart experiment" (Harsh Critic issue #4, speculative framing):** The critic asserts the gap "suggests the NF baseline may be poorly configured." This is speculation about the baseline setup. The paper does report that it compares against NFs parameterizing the Cholesky factor. Without evidence of poor tuning, this is not a verified flaw. Demoted to Major weakness #3 above (more neutrally framed as a need for additional analysis).

- **Strength Finder items about SBI being "state-of-the-art":** The SBI results are deferred entirely to the appendix (which is stripped in the PDF). Without access to the results, this claimed strength cannot be verified. Removed.

- **Strength Finder: generic strengths** about "addressing important problems" — removed as generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The key insight — marginalizing over resampled component parameters drawn from a learnable neural generator to achieve exact density evaluation and efficient sampling simultaneously — is well articulated by the authors.

## Suggestions

1. **Add a GMM baseline to the synthetic experiments.** Train a GMM via EM with a large number of components (matching or exceeding the effective capacity of the Marginal Flow) and compare test log-likelihood on the 2D synthetic datasets. This directly tests whether the resampling mechanism provides value beyond optimized finite mixtures.

2. **Evaluate on a standard high-dimensional density estimation benchmark** (e.g., UCI tabular datasets like POWER, GAS, HEPMASS, MINIBOONE with 6–50 dimensions) and report test log-likelihood. This would substantially strengthen the claim of being a general-purpose framework.

3. **Ablate $N_c$** on at least one synthetic dataset, showing test log-likelihood vs. $N_c$ (e.g., 10, 50, 100, 500, 1000) and the corresponding evaluation runtime.

---

**Calibration Anchor Comparison:**

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| kRjLBXWn1T — "Correcting Flows with Marginal Matching" | 5.25 (Reject) | Similar topic (flow-based models), comparable empirical scope. Marginal Flow has a cleaner framework and stronger empirical convergence results. Slightly higher. |
| 2OMyAFjiJJ — "Flow matching achieves almost minimax optimal convergence" | 6.00 (Accept) | Theoretical paper with no experiments. Marginal Flow is empirically grounded with diverse tasks but lacks theoretical analysis. Similar quality, different type. |
| kBNIx4Biq4 — "Lifting Architectural Constraints of Injective Flows" | 6.50 (Accept) | Addresses a related problem (removing flow constraints) with thorough experiments. Marginal Flow has a novel framework but less exhaustive evaluation. Slightly lower. |
| 6Z8rZlKpNT — "Normalizing Flows for OOD Detection" | 3.40 (Reject) | Limited novelty, application-focused. Marginal Flow is substantially more novel and better evaluated. Much higher. |
| 2whSvqwemU — "FM-TS: Flow Matching for Time Series Generation" | 3.00 (Reject) | Poor reproducibility, limited novelty. Marginal Flow is far stronger in both contribution and evaluation. Much higher. |
| DoDNJdDntB — "Flow Matching for Posterior Inference with Simulator Feedback" | 4.20 (Reject) | Application-focused with mixed reviews. Marginal Flow has a more general contribution and stronger evidence. Higher. |

## Score and Decision

The paper proposes a genuinely novel density estimation framework with clean theoretical motivation and strong empirical results on the tasks it evaluates. The key weaknesses are the missing GMM baseline (despite motivating against GMMs), the lack of high-dimensional density estimation benchmarks, and insufficient analysis of the Wishart experiment gap. These are addressable gaps rather than fatal flaws. The contribution — simultaneous exact likelihood and efficient sampling via learned marginalization — is valuable and well-demonstrated on the evaluated tasks.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>