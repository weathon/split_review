Now I have all the information needed to write the consolidated review. Let me organize my analysis carefully.

---

## Summary

This paper studies equilibrium propagation (EP) under weight asymmetry and finite nudge. It analytically separates the two bias sources, extends holomorphic EP (hEP) to asymmetric complex-differentiable systems, introduces a Jacobian homeostatic loss to mitigate asymmetry-induced bias, and demonstrates training on ImageNet 32×32. The paper is a **theoretical + empirical methods paper**.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal
None.

### Major
- weakness 1 — why it matters

### Minor
- weakness 1 — why it matters

### Trivial
- weakness 1

## Nice-to-Haves
- suggestion

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

## Summary

This paper studies equilibrium propagation (EP) under the dual challenges of weight asymmetry and finite nudge amplitude. It analytically separates these two sources of bias, extends holomorphic EP (hEP) to non-symmetric complex-differentiable dynamical systems, and proposes a Jacobian homeostatic loss that penalizes the skew-symmetric part of the Jacobian to mitigate asymmetry-induced bias. The method is demonstrated on Fashion MNIST, CIFAR-10/100, and ImageNet 32×32. The paper is a **theoretical and empirical methods contribution**.

## Strengths

1. **Clean analytical isolation of two previously confounded bias sources.** The paper derives a precise relation (Eq. 13: $\dudb = J^{-1}J^{\top}\delta$) linking the asymmetry of the Jacobian at the fixed point to the misalignment between the hEP and RBP neuronal error vectors. This formal separation of finite-nudge bias from asymmetry bias—and the expansion in Eq. 14 showing the first-order role of the skew-symmetric component $A$—goes beyond prior work that treated the two as a combined phenomenon (Scellier & Bengio 2017, Laborieux et al. 2022).

2. **Extension of holomorphic EP to asymmetric complex-differentiable systems.** The paper generalizes the Cauchy-integral estimator (Eq. 4–5) to non-symmetric vector fields and provides continuous-time approximations (Eq. 9–10) that avoid separate free/nudged phases. This is a principled extension that applies to a broader class of dynamical systems than the original symmetric-energy-function formulation.

3. **Novel homeostatic objective that targets functional symmetry.** The loss in Eq. 15 ($\mathcal{L}_{\text{homeo}} = \mathbb{E}_\varepsilon[\|J_F\varepsilon\|^2 - \varepsilon^{\top}J_F^2\varepsilon]$) directly penalizes the skew-symmetric part of the Jacobian without requiring weight symmetry, making it applicable to architectures without reciprocal connectivity (e.g., the antisymmetric architecture in Fig. 4e–h). The paper verifies that this loss improves Jacobian symmetry and error-vector alignment across layers (Fig. 4c–d, g–h, l).

4. **Empirical study of symmetry degradation during training.** Figure 3 quantifies how forward-backward weight alignment degrades for both RBP and hEP over time, and shows that cosine similarity between hEP and RBP error vectors becomes negative in deep layers for RBP-trained networks. This provides mechanistic evidence for why EP under asymmetry fails on harder tasks.

## Weaknesses

### Major
None.

### Minor

1. **ImageNet 32×32 result uses the oracle gradient estimate, not the full finite-nudge pipeline.** The ImageNet experiment (Table 5, row "hEP (True $\dudb$)") computes neuronal errors via forward-mode automatic differentiation, not the proposed Cauchy-integral estimator (Eq. 7) that would be needed in a setting without AD access. The full method—Cauchy estimate (N=2) combined with homeostatic loss—is only demonstrated up to CIFAR-100, where the gap to the oracle result is already non-trivial (81.4% vs. 84.3% on CIFAR-10, and 51.1% vs. 53.8% on CIFAR-100). The paper claims its strategy "allows training deep dynamical networks without perfect weight symmetry on ImageNet 32×32" (Discussion), but the ImageNet evidence omits the finite-nudge component of the pipeline. This does not undercut the paper's core contributions—the homeostatic loss is clearly validated at ImageNet scale—but the practical claim about the full method is incompletely supported.

2. **The homeostatic loss requires non-local computations, but the paper does not resolve this despite a biologically/neuromorphically motivated framing.** The loss in Eq. 15 requires computing $J_F\varepsilon$ and $J_F^2\varepsilon$ (Jacobian–vector products) at the free fixed point. The paper cites prior work on local learning rules for similar objectives (Stock & Gökmen 2022; Meulemans et al. 2021) but does not show that the *specific* combined loss can be implemented locally, nor does it provide a local approximation. Given the paper's motivation (Abstract: "biological or analog neuromorphic substrates"; Introduction: "physical neural networks"), this creates a gap between framing and method. This does not diminish the paper as an algorithmic/theoretical contribution—the loss clearly improves performance in simulation—but the biological/non-digital plausibility claims are not matched by the proposed mechanism.

3. **No ablation isolating the two terms of the homeostatic loss.** The loss has two components: $\|J_F\varepsilon\|^2$ (Frobenius-norm penalty) and $-\varepsilon^{\top}J_F^2\varepsilon$ (symmetry-promoting term). The paper claims the loss improves performance by reducing asymmetry, but without an ablation it is unclear how much of the gain comes from the symmetry term versus the Jacobian-norm minimization (which could improve training through regularization, fixed-point stabilization, or other channels). The RBP control (Table 5) shows the loss does not help RBP, suggesting specificity, but does not resolve which term drives the effect under hEP.

4. **The "hEP w/o homeo" baseline on CIFAR-10 (60.4%) is suspiciously low and unexplained.** This is a network with the same architecture as the successful homeostatic run, but it barely outperforms chance (60.4% vs. 10% random). The paper does not report learning curves for this condition or discuss whether training instability, failure of fixed-point convergence, or gradient collapse explains this floor-level performance. Without understanding why the plain hEP baseline is so low, it is difficult to fully attribute the 24-point improvement to asymmetry correction versus resolving a training failure mode that may have unrelated causes.

5. **Expansion assumptions not explicitly stated.** The key relation in Eq. 14 ($\dudb = \delta - 2S^{-1}A\delta + o(S^{-1}A\delta)$) uses a first-order expansion in $S^{-1}A$ but does not explicitly state the required conditions (invertibility of $S$, smallness of $\|S^{-1}A\|$ in some norm). These may be violated during early training, and the paper does not discuss this limitation.

### Trivial

1. The derivation from $\|A\|^2 = \tfrac{1}{2}(\|J\|^2 - \operatorname{tr}(J^2))$ to Eq. 15 (the expectation over $\varepsilon$) is telegraphic; a few intermediate steps would improve clarity.

## Nice-to-Haves

- **Symmetric hEP + homeostatic control.** Adding homeostatic loss to the *symmetric* hEP baseline would clarify whether the loss is beneficial specifically for asymmetry or provides generic regularization.
- **Fixed-point convergence monitoring.** The theory assumes the system converges to a fixed point for all $\beta$ on the complex path. Reporting whether this was monitored for asymmetric networks would strengthen the empirical validation.
- **Computational cost discussion.** The homeostatic loss requires per-sample Jacobian-vector products; a brief discussion of the computational overhead (especially for ImageNet) would help practitioners assess the trade-off.

## Removed Points

These points are flagged to be removed per instructions; treat them with caution.

1. **Missing hyperparameter details (λ_homeo, epochs, schedule).** Per the hard rules, missing hyperparameters are reproducibility nitpicks removed from evaluation. These details are assumed available in the original submission's (stripped) appendix.

2. **"The antisymmetric architecture gains are smaller and unexplained."** The paper explicitly acknowledges the small improvement on simpler tasks (line 321: "the improvement...was measurable, but small") and uses this to motivate the harder CIFAR-10/100/ImageNet experiments. This is not an unexplained weakness.

3. **"The paper should also cover additional tasks/domains."** This is scope creep; the paper's depth in its chosen direction (ImageNet 32×32) is sufficient.

## Novel Insights

Beyond the paper's own contributions, the reviews highlight an interesting tension: the two bias sources (finite nudge and Jacobian asymmetry) interact non-trivially at scale. The Cauchy integral removes nudge bias exactly for any holomorphic system, but its practical effectiveness depends on the nudge trajectory staying within the holomorphic domain of the fixed-point function—a condition that may be harder to satisfy as asymmetry grows. Conversely, the homeostatic loss demonstrably stabilizes the Jacobian structure, which may also improve the conditioning of the Cauchy estimate indirectly. Whether these two mechanisms reinforce or interfere with each other at scale is an open question the paper raises but does not answer.

## Suggestions

1. Add the Cauchy-estimate row for ImageNet 32×32 (even N=2 with modest computational budget) or clearly state in the abstract and contributions that the ImageNet scaling claim applies to the homeostatic loss component specifically, while the full pipeline (Cauchy + homeostatic loss) has been validated up to CIFAR-100.

2. Include an ablation study separating the two terms in Eq. 15 on at least one dataset (e.g., CIFAR-10) to establish that the symmetry-promoting $-\varepsilon^{\top}J_F^2\varepsilon$ term is necessary for the observed gains.

3. Discuss the locality gap honestly in Section 5: explicitly state that the current formulation of the homeostatic loss is non-local and that a local approximation remains open for future work, rather than relying on citations to related but not identical local learning rules.

4. Report learning curves or diagnostic metrics (e.g., gradient norm, fixed-point convergence residual) for the "hEP w/o homeo" CIFAR-10 condition to clarify whether the 60.4% baseline reflects asymmetry bias specifically versus a training collapse.

## Score and Decision

The paper makes a solid contribution: it clarifies a previously muddled source of bias in generalized EP, extends hEP to asymmetric systems in a principled way, and demonstrates that a homeostatic Jacobian penalty can dramatically improve training performance. The weaknesses identified (incomplete full-pipeline scaling, unverified causality of the loss mechanism, a non-local objective in a biologically-motivated paper) are real but reparable. They do not invalidate the core contributions but do require tempering of claims and additional analysis.

**Score: 7.0**

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>