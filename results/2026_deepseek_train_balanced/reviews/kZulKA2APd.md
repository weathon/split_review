Now I'm ready to write the final consolidated review.

## Summary

This paper proposes PRGDA (Perturbed Recursive Gradient Descent Ascent), an algorithm that combines SPIDER-style variance reduction with perturbed gradient descent to find second-order stationary points (SOSPs) in stochastic nonconvex-strongly-concave minimax optimization and nonconvex-strongly-convex bilevel optimization. The main theoretical contributions are: (1) PRGDA is claimed to be the first stochastic algorithm guaranteed to converge to an SOSP in minimax optimization, achieving $\tilde{O}(\kappa^3\epsilon^{-3})$ gradient complexity that matches the best known rate for finding *first-order* stationary points; (2) for bilevel optimization, PRGDA obtains improved gradient complexity over StocBiO with iNEON, the prior best second-order method. Numerical experiments on matrix sensing tasks illustrate saddle-point escape behavior.

## Strengths

- **First stochastic SOSP guarantee for nonconvex-strongly-concave minimax.** The paper identifies that prior second-order stationary-point methods for minimax problems (Cubic-GDA, MCN, Perturbed GDmax) are restricted to deterministic or finite-sum settings (lines 38–40). PRGDA is presented as the first algorithm with SOSP guarantees in the genuinely stochastic setting where full gradients are unavailable — a genuine gap in the literature. This claim is stated in the abstract (line 4), contribution list (line 57), and supported by the comparison in Table 1.

- **Gradient complexity matching first-order rates in minimax.** Theorem 1 (line 198) states an SFO complexity of $\tilde{O}(\kappa^3\epsilon^{-3})$ to reach an $O(\epsilon,\sqrt{\rho_\Phi\epsilon})$ SOSP. This matches the $\tilde{O}(\epsilon^{-3})$ gradient complexity of SREDA and Acc-MDA, which only target first-order stationary points. Obtaining second-order guarantees at no extra asymptotic cost is a non-trivial theoretical achievement.

- **Improved bilevel complexity over prior second-order methods.** Theorem 2 (line 200) gives $Gc(f,\epsilon)=\tilde{O}(\kappa^3\epsilon^{-3})$ and $Gc(g,\epsilon)=\tilde{O}(\kappa^7\epsilon^{-3})$, which the paper reports as an improvement over StocBiO with iNEON (Huang et al., 2022b) — the only prior stochastic bilevel method with second-order guarantees.

- **Pure first-order oracle for the minimax case.** For minimax optimization, PRGDA requires neither Hessian matrices nor Hessian-vector products (line 40, line 57). This is a clean practical advantage over cubic-regularized methods (Cubic-GDA, MCN) for the minimax setting.

## Weaknesses

### Fatal

None.

### Major

- **Experimental validation is thin relative to the paper's motivating scope.** Both experiments (robust optimization, Section 7.1; hyper-representation learning, Section 7.2) are based on the *same* underlying problem — matrix sensing — with noise-free synthetic data ($b_i = \langle A_i, M^*\rangle$ exactly, line 220). The algorithm is theoretically designed for *stochastic* optimization, yet the experiments lack observation noise and test only one problem family. The paper motivates PRGDA with GANs, adversarial training, meta-learning, and hyperparameter optimization (line 10), but provides no experiment in any of these domains. This creates a mismatch between claimed applicability and demonstrated behavior. While theory papers are not required to run large-scale experiments, the paper's own framing invites empirical support that the current evidence does not provide.

- **No variance or confidence reporting.** The paper reports running each algorithm "5 times and the mean value" (line 226) for Table 3, but no standard deviations, error bars, or confidence intervals appear anywhere. For a stochastic algorithm where variance is central to the analysis, omitting measures of variability makes it impossible to assess whether observed differences are meaningful.

### Minor

- **No proof sketch or intuition in the main text.** Section 6 presents Theorem 1 and Theorem 2 as a bare list of parameter settings and a complexity conclusion, with no high-level reasoning, roadmap, or intuition about why the chosen parameters interact to yield the claimed bound. The paper's primary contribution is theoretical, but a reviewer cannot assess the soundness of the argument from the main text alone. This is not uncommon in theory papers, but it substantially limits what can be evaluated from the submission.

- **"Pure first-order" terminology is ambiguous for the bilevel case.** The contribution list states "our method is pure first-order and does not require any calculation of second-order derivatives" (line 57). For the minimax case this is accurate (line 40). However, for the bilevel case, PRGDA uses AID which requires Hessian-vector products of $g$ (line 172–175), and Theorem 2 explicitly reports $HV(g,\epsilon)$ and $JV(g,\epsilon)$ complexity. While the paper defines a "first-order method" as using only first-order information of $\Phi$ (line 107), the broader claim at line 57 is potentially misleading without disambiguation.

- **No discussion of limitations.** The paper does not acknowledge that Assumptions 3 and 5 (Lipschitz second/third derivatives) are strong smoothness conditions that may not be satisfied by common objectives such as neural networks with ReLU activations, nor that the experiments are limited to noise-free synthetic data. A brief limitations section would improve the paper's completeness.

- **Hyperparameters are shared from a Pullback paper for standard nonconvex optimization** (Chen et al., 2021a) without explaining their relevance to the minimax/bilevel setting or how they relate to the theoretical parameter choices in Theorem 1/2. A brief bridge between theory and experiment would strengthen the presentation.

### Trivial

- The paper contains minor formatting artifacts common to PDF parsing (e.g., garbled characters in equations, image-based tables that are not machine-readable). These are parser issues, not paper problems, and do not affect evaluation.

## Nice-to-Haves

- An ablation study removing the perturbation mechanism (running PRGDA without perturbation) would directly demonstrate the value of the escape phase and support the "escaping saddle point" claim.
- A proof sketch (even one paragraph) explaining how the descent phase controls gradient norm, how the escaping phase exploits negative curvature, and how SPIDER variance interacts with the perturbation would help readers assess the theoretical contribution.
- An experiment on a small real-world benchmark (e.g., simple GAN on MNIST, or hyperparameter optimization on a small regression task) would substantially strengthen the empirical support.

## Removed Points

The following points from the inputs were removed or demoted for the reasons stated:

- **Criticism that experiments merely "confirm what theory predicts"** — Running baselines to demonstrate saddle-point escape is standard validation practice, not a weakness.
- **Claim that variance reduction "challenges the premise of PRGDA"** because StocBiO escapes saddles via noise while variance-reduced methods do not — The paper *itself* makes this observation (line 251) and frames it as motivation for adding explicit perturbation. The critic misreads this.
- **Claim that the comparison with first-order methods is "not like-for-like"** — Comparison tables contrasting methods with different properties (saddle-escape capability vs. not) are standard and informative; the last column of Table 2 explicitly tracks this distinction.
- **Claim about Acc-MDA achieving better $\kappa$ dependence** — Cannot be independently verified; falls under "missing related works" which I am instructed not to raise.
- **Claim that proofs are "entirely in the appendix" as a structural weakness** — This is standard practice; the lack of a proof *sketch* (kept as Minor) is the real issue.
- **Criticism about hyperparameters being "fixed across problem scales" without tuning** — Fixed hyperparameters across dimensions in synthetic benchmarks are standard; this is not a genuine weakness.
- **Claim that assumptions are "too strong" without discussing whether they hold for common objectives** — The paper does cite prior work using the same assumptions. Only the lack of *discussion* about their practical scope is retained as Minor.

## Novel Insights

None beyond the paper's own contributions. The two reviews reflect a standard tension: a novel theoretical result with genuine contributions to the literature, paired with empirical support that is too narrow to match the paper's own motivational framing. The most interesting observation from the reviews is the interplay between variance reduction and saddle escape — the paper's own experiments show that variance-reduced methods (MRBO, VRBO) are *worse* at escaping saddles than plain StocBiO because reduced gradient noise removes natural perturbation. PRGDA is designed to address this by adding explicit perturbation, but the paper does not discuss this design tension in the main text.

## Suggestions

1. Add at least one experiment on a real benchmark from the domains listed in the introduction (GANs, adversarial training, meta-learning, hyperparameter optimization) to bridge the gap between motivation and validation.
2. Include standard deviations or confidence intervals in all experimental figures and tables.
3. Add a brief proof sketch or high-level roadmap in Section 6 to help readers assess the theoretical contribution without reading the full appendix.
4. Clarify that the "pure first-order" claim applies to the minimax case, and for bilevel describe the Hessian-vector product requirements transparently.
5. Add a limitations paragraph discussing the strong smoothness assumptions and the scope of the empirical validation.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>