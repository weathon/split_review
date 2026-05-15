Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper extends Energy Discrepancy (ED)—a recently proposed contrastive loss that avoids MCMC during training—from continuous to discrete spaces. The authors introduce three families of discrete perturbations (Bernoulli noise, deterministic transformations, and neighbourhood structures) and use importance sampling to estimate the intractable contrastive potential, with both uninformed and gradient-informed proposals. Empirically, the method achieves strong results on Ising model recovery, density estimation, graph generation, and discrete image modelling, often matching or exceeding MCMC-based approaches while only requiring parallelisable energy evaluations.

## Strengths

- **Novel connection between ED and importance sampling enables principled gradient-informed proposals in discrete spaces.** By reformulating the contrastive potential as an importance-sampling expectation (Eq. 8), the paper derives gradient-informed proposals for Bernoulli and neighbourhood perturbations (Eqs. 13–14). This interpretation is new for discrete ED and is empirically validated: ED-∇Bern consistently outperforms ED-Bern across multiple tasks (Tables 1 and 3).

- **Strong empirical results across diverse discrete tasks, with training that avoids MCMC entirely.** The method recovers the ground-truth coupling matrix of an Ising model (Figure 1), achieves the best average MMD on graph generation (Table 2), outperforms all baselines on four out of five discrete density estimation tasks (Table 1), and obtains competitive NLL on Omniglot and Caltech-101 Silhouettes (Table 3). These results demonstrate that ED can serve as a viable alternative to MCMC-based training in several important settings.

- **Computational efficiency from parallelisable, short negative-sample generation.** The paper highlights that ED requires only \(M\) (here 32) evaluations of the energy function per data point, all executed in parallel, unlike the sequential MCMC steps of contrastive divergence (Section 6.4). This practical advantage is supported by the method outperforming CD-1 by a large margin (Table 6) while using comparable compute.

- **Systematic taxonomy of discrete perturbations.** The paper classifies perturbations into three principled families (Bernoulli, deterministic transformations, neighbourhood-based), providing concrete formulas and algorithms for each. This framework is extensible to other discrete spaces beyond \(\{0,1\}^d\) (Section 3.1).

## Weaknesses

### Fatal
None.

### Major

- **Theorem 1 (consistency of the loss estimator) is stated without proof, and its correctness is not obvious.** The theorem claims there exist N and M such that the stabilised loss approximates the true ED arbitrarily well. However, no proof or even a sketch is provided. The stabilisation parameter \(w\) introduces a fixed offset that does not vanish with increasing M, and the logarithm of a finite importance-sampling sum is biased; how these interact with the claimed consistency guarantee is left unaddressed. This makes the theoretical grounding of the loss function incomplete. (The paper is otherwise an empirical systems paper, so this does not invalidate the experimental results, but it does mean the theoretical claims are overstated.)

- **No wall-clock or FLOPs comparison is provided to substantiate the central efficiency claim.** The paper repeatedly emphasises that ED is more efficient than MCMC-based methods because it requires only parallelisable energy evaluations (e.g., Section 6.4). However, no actual runtime measurements, FLOPs counts, or NLL-vs-time plots are reported. Without such data, a reader cannot judge whether the performance gap on MNIST (where ED methods are 35–45% worse in NLL than MCMC baselines, Table 3) is worth the computational savings. This is a critical missing piece for a paper whose main practical selling point is efficiency.

- **The deterministic transformation (ED-Pool) is underspecified, hampering reproducibility.** The paper introduces "ED-Pool with mean-pooling transformation" (Section 3.1, Table 2) but never explains how mean pooling is applied to binary data, what the preimage of a pooled representation is, or how the inverse neighbourhood is sampled. While the general framework (sampling uniformly from the preimage of \(g\)) is described, the specific implementation for mean pooling is not. This makes it impossible to reproduce or independently assess this variant, which achieves competitive results on graph generation.

### Minor

- **Equation (10) contains a sign error in the exposition.** The paper writes \(U_q(\mathbf{y}) \approx \log\frac{1}{M}\sum_i \exp(-U(\mathbf{x}_-^i)) + \log w_{\mathbf{y}}\), but the correct expression (derived from Eq. 8) is \(U_q(\mathbf{y}) \approx -\log\frac{1}{M}\sum_i \exp(-U(\mathbf{x}_-^i)) - \log w_{\mathbf{y}}\). Fortunately, the actual loss function (Eq. 15) appears to be correctly derived, suggesting this is a typo in the exposition rather than an error in the implementation. The authors should correct this to avoid confusion.

- **Proposition 1's "mild conditions on \(q\)" are never stated, nor explicitly verified for the discrete perturbations proposed.** The paper asserts that discrete perturbations are valid under Proposition 1 (line 81) but does not specify what conditions the original result requires or why Bernoulli noise, deterministic transforms, and grid neighbourhoods satisfy them. While the strong empirical results across multiple tasks suggest the method works in practice, the theoretical claim is not fully established. This is a gap in presentation rather than a fatal flaw—many empirical papers use theoretical frameworks from prior work without re-proving them—but it should be addressed for clarity.

- **Gradient-informed proposals rely on a Taylor expansion that the authors acknowledge is "technically not well-defined for discrete data" (line 154).** The paper is transparent about this limitation and argues the inner product is still meaningful, which is standard practice in the discrete EBM literature (Grathwohl et al., 2021; Zanella, 2020). Nonetheless, this is a heuristic approximation, and the paper would benefit from further justification or a study of when this approximation breaks down.

- **No ablation study for the number of negative samples \(M\), perturbation strength \(\varepsilon\), temperature \(\tau\), or stabilisation parameter \(w\).** The method has several hyperparameters whose influence on performance is not systematically examined. For practitioners, it is unclear how to set these values or how sensitive the method is to their choice.

- **Quantitative evaluation of Ising model recovery is limited to qualitative heatmaps (Figure 1).** Reporting a quantitative metric (e.g., Frobenius norm error of the learned coupling matrix \(J\)) would significantly strengthen the claim that ED recovers the correct energy landscape.

### Trivial
None beyond those listed above (which are already at the appropriate severity level).

## Nice-to-Haves
- Wall-clock training time comparison (NLL vs. compute time) for ED vs. PCD/GWG on one dataset would substantiate the main efficiency claim.
- Ablation of \(M\) (number of negative samples) showing how NLL varies, to help practitioners choose this parameter.
- Analysis of why ED-∇Grid fails to improve over ED-Grid on images (beyond the brief conjecture about local modes).
- Application to molecular generation (QM9) or text data would strengthen claims of general applicability.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"The paper claims 'comparable' performance on image modelling, contradicted by Table 3."** The paper actually says "comparable performance to the baseline methods **on the Omniglot dataset**" (emphasis added) and explicitly acknowledges the MNIST gap ("Despite the performance gap compared to the contrastive divergence methods on the MNIST dataset"). The reviewer misread this passage.

- **"Equation (2) omits the negative sign."** The equation is correct: \(-\nabla_\theta \mathbb{E}_{p_{\text{data}}}[\log p_\theta(\mathbf{x})] = \mathbb{E}_{p_{\text{data}}}[\nabla_\theta U_\theta(\mathbf{x})] - \mathbb{E}_{p_\theta}[\nabla_\theta U_\theta(\mathbf{x})]\). The negative sign is present on the left-hand side. The reviewer's confusion is unfounded.

- **"The sign error in Eq. (10) affects every experiment."** The loss function (15) is correctly derived—the sign error is an exposition typo in (10) only. The actual algorithm (Algorithm 1) and loss (15) do not propagate this error.

- **"Proposition 1 is cited from continuous settings and the paper never verifies it holds for discrete perturbations."** The paper correctly cites Proposition 1 from prior work and states it applies "under mild conditions on \(q\)" (line 53). The paper then describes discrete perturbations "as per Proposition 1" (line 81). While the paper could more explicitly verify the conditions, this is a presentation gap, not an indication the result does not hold. The strong empirical results corroborate the theoretical claim.

- **"Gradient-informed proposal Taylor expansion assumes differentiability in discrete space."** The paper explicitly acknowledges this limitation ("technically not well-defined for discrete data," line 154) and argues the approximation is still meaningful, citing standard practice in the field. This is transparent and not a hidden flaw.

- **"The paper does not address the second limitation (variance of contrastive potential cannot be controlled)."** The paper proposes gradient-informed proposals and \(w\)-stabilisation as remedies for this limitation (Section 4) and the \(w\)-stabilisation provably provides a lower bound (Section 4.2). While a detailed variance analysis is missing, the paper does address the limitation.

- **Weaknesses that are pure formatting/style nitpicks or parser artifacts.** None applicable.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Provide wall-clock timing comparisons** between ED and MCMC-based methods (GWG, DULA) on at least one dataset to substantiate the efficiency claim that is central to the paper's motivation.
2. **Add a proof sketch or a finite-sample bound for Theorem 1**, or at minimum clarify the role of \(w\) and how consistency is achieved (e.g., if \(w\) should decay with \(N\) or \(M\)).
3. **Correct the sign error in Eq. (10)** and clarify that this does not affect the loss (15) or the implementation.
4. **Specify the deterministic transformation implementation** (how mean pooling is applied to binary data and how the preimage is sampled) for reproducibility.
5. **Include quantitative Ising model evaluation** (e.g., Frobenius norm error of learned \(J\)) alongside the qualitative heatmaps.
6. **Add ablations for key hyperparameters** \(M\), \(\varepsilon\), \(\tau\), and \(w\) on at least one dataset to guide practitioners.

## Score and Decision

The paper makes a genuine contribution—extending energy discrepancy to discrete spaces with a clean importance-sampling framework and demonstrating strong results on several tasks. The core idea is sound, and the empirical evaluation (density estimation, graph generation) is compelling. However, the paper has two significant weaknesses: Theorem 1 is stated without proof (undermining the theoretical claims), and the central efficiency advantage is never measured quantitatively. The MNIST gap is larger than one would hope, but the paper is transparent about it. These issues are addressable and do not invalidate the paper's contributions. On balance, the paper does more than enough to warrant acceptance at a good venue.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>