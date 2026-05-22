## Summary

This paper develops a theoretical framework for saddle-to-saddle dynamics as a mechanism for simplicity bias across neural network architectures. The key contributions are: (i) extending the embedded-fixed-point hierarchy of Fukumizu & Amari (2000) to convolutional and self-attention architectures (Theorems 1–2); (ii) identifying invariant manifolds that map to effective network width, formalizing the link between weight geometry and functional simplicity (Theorem 3); and (iii) analyzing the gradient-flow dynamics for two concrete activation classes—linear-in-weights (Section 5.1, Theorem 4) and quadratic-in-weights (Section 5.2, Proposition 5)—which reveal two distinct timescale-separation mechanisms (data-driven vs. initialization-driven) that produce the predicted low-rank and sparse weight structures. The paper validates these predictions with simulations across linear, ReLU, convolutional, self-attention, and quadratic networks, and uses the theory to predict how width, data distribution, and initialization affect stage-like learning.

## Strengths

- **Extension of embedded fixed points to modern architectures (convolutional, self-attention) and invariant manifolds.** Theorems 1 and 3 genuinely go beyond Fukumizu & Amari (2000) by covering weight constructions (Equations 6–7) that correspond to the saddles actually visited during training, and by showing that invariant manifolds tie directly to effective width. These results are architecture-agnostic and provide the structural backbone of the framework.

- **Two distinct timescale-separation mechanisms with testable predictions.** The paper cleanly disentangles data-driven separation (linear case → low-rank weights, Theorem 4) from initialization-driven separation (quadratic case → sparse weights, Proposition 5). The predictions that width affects plateaus in self-attention but not in linear networks (Figure 2A), and that equal singular values eliminate plateaus only in the linear case (Figure 2B), are non-obvious and directly verified.

- **Clear identification of conditions for saddle-to-saddle dynamics and counterexamples.** Section 7 specifies two necessary conditions (escape paths follow invariant manifolds; initialization is near one) and provides concrete failure cases (tanh networks, large random initialization), which usefully delineates the theory's scope and prevents overclaiming.

- **Testable predictions validated by simulations.** Section 6 translates the theory into quantitative predictions about width, data distribution (power-law exponent), initialization structure, and initialization scale, all supported by simulations in Figure 2.

## Weaknesses

### Fatal
None.

### Major

- **Title, abstract, and introduction claim broader dynamical coverage than rigorously proven.** The paper's framing asserts that the theory "explains" saddle-to-saddle dynamics across architectures including ReLU networks, but the rigorous dynamical analysis (Section 5) is restricted to two-layer networks where the activation is a homogeneous polynomial in the weights—specifically linear (Section 5.1) and quadratic (Section 5.2) cases. For ReLU networks, the structural results (Theorems 1, 3) apply because ReLU is homogeneous, but the *dynamics* that drive saddle-to-saddle transitions are not proven—they are shown only empirically (Figures 1D–E). The paper explicitly acknowledges this boundary in Section 5 ("we must work with concrete architectures") and Section 7, but the abstract and title imply a unified dynamical explanation that the paper does not fully deliver for the most widely used activation function. This is a scope-calibration issue rather than a technical flaw: the paper's genuine contributions are substantial, but the framing should more precisely match what is proven vs. conjectured or empirically suggested.

- **The quadratic-case dynamics analysis is heuristic rather than rigorous.** Proposition 5 analyzes a simplified system (Equation 14) that drops coupling terms from the full gradient flow (Equation 44, in appendix). The paper correctly notes this is an approximation, but the gap between the scalar intuition *v̇ᵢ = vᵢ²* and the actual bilinear dynamics (involving matrices Σ<sub>yZ</sub> and both *vᵢ* and **uᵢ**) is large. The claim that one unit dominates "almost surely" when weights reach O(1) relies on heuristic reasoning about this approximation, not a rigorous analysis of the full dynamics. The simulations are consistent, but the theoretical mechanism is not proven to extend beyond the initial transient where the approximation holds.

### Minor

- **Experiments lack statistical characterization.** All loss curves in Figures 1–2 appear to be single runs, with no error bars, confidence intervals, or multi-seed statistics. This is especially limiting for claims about quantitative scaling (e.g., plateau length vs. singular-value gap, or plateau length vs. width in self-attention), where variance across random seeds would inform the reliability of the predictions. While single-run plots are common in theoretical papers, the specificity of the predictions calls for at least some quantification of variability.

- **Quadratic-case analysis could benefit from a controlled numerical validation of the predicted timescale.** The paper presents the scalar *v̇ᵢ = vᵢ²* intuition but does not provide a controlled experiment that isolates the predicted scaling—e.g., tracking the ratio of the largest weight to the second-largest weight across random seeds during the first plateau, to verify that the dominance predicted by Proposition 5 actually materializes in the full dynamics.

### Trivial
None.

## Nice-to-Haves

- A brief comparison of Theorem 4 with the deep-matrix-factorization convergence results of Arora et al. (2018, *Implicit Regularization in Deep Matrix Factorization*) would help position the linear-case contribution relative to that closely related line of work.
- A systematic ablation table testing the two conditions for saddle-to-saddle dynamics (Section 7) by deliberately violating each condition independently would strengthen the empirical evidence for the theory's boundary conditions.

## Removed Points

The following points from the reviewer inputs were identified as not valid or not relevant to this paper:

- **"Taylor expansion argument for ReLU fails because ReLU is non-differentiable"**: The paper does not use a Taylor expansion argument for ReLU. The Taylor-expansion discussion in the "General nonlinear activation" subsection is about tanh and the specific activation *uᵀx·tanh(uᵀx)*, not about ReLU. The paper's ReLU results are empirical, not derived via Taylor expansion. Removed as a misreading.
- **"Theorem 3(iv) requires φ to be both homogeneous of degree 1 and additive (linear)—this is a very strong condition"**: The paper already states this condition clearly ("If φ(z; u) is linear in u") and explicitly notes this case applies to linear networks. The reviewer is restating what the paper already says, not identifying a weakness. Demoted from consideration.
- **Reproducibility complaints about undisclosed hyperparameters / artifacts / appendix content**: The parser strips appendix content; hyperparameters are described in Appendix I which is not available. Standard for conference submissions; not a valid criticism.
- **"Missing related works"**: The paper has a dedicated related-work section (Appendix A) and cites the relevant literature extensively (Saxe et al., 2014, 2019; Fukumizu & Amari, 2000; Jacot et al., 2022; etc.). The mention of Arora et al. (2018) is a suggestion, not a missing essential reference.
- **Strength Finder items that are generic or superficial**: Removed strengths that were generic praise of importance/scope without specific evidence, or that conflicted with verified weaknesses.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface a genuinely novel observation that the paper itself does not already articulate.

## Suggestions

1. **Re-scope the title and abstract** to more precisely reflect that the rigorous dynamical analysis covers networks with polynomial weight-dependence (linear and quadratic), while the framework's structural components (fixed points, invariant manifolds) apply more broadly and are supported by empirical evidence for activations like ReLU. For example: "A Theoretical Framework for Saddle-to-Saddle Dynamics Explaining Simplicity Bias in Linear, Quadratic, and Empirically in ReLU Networks."

2. **Strengthen the quadratic-case analysis** by providing a controlled numerical experiment that tracks the growth ratio of the leading unit relative to others across multiple random seeds during the first plateau, directly validating the "one unit dominates" claim of Proposition 5.

3. **Add multi-seed statistics** to at least the key quantitative predictions (Figures 2A, 2B, 2D) to characterize variability and support claims about plateau-length scaling.

4. **Discuss the relationship to Arora et al. (2018)** on implicit regularization in deep matrix factorization, since Theorem 4 covers similar low-rank alignment dynamics for two-layer linear networks.

## Score and Decision

**Calibration report.** All anchors retrieved across rounds:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| FVQzqSIJcC | 3.00 | R1 low | Weak paper on feature learning; the current paper is substantially stronger in theory and scope |
| 8xcmfwomnI | 3.00 | R1 low | Weak paper on OOD via simplicity; the current paper has more rigorous theory |
| KkJfaicdd8 | 3.00 | R1 low | Unrelated (Hopfield networks); not comparable |
| zbiWoFe60O | 3.20 | R1 low | Topological invariance paper; the current paper has stronger empirical validation |
| B4zcoLvjw0 | 6.00 | R1 mid | Directly comparable: saddle-to-saddle dynamics paper with rigorous first-escape theory but limited experiments and the rest as conjecture. Current paper has broader architectural scope, more complete dynamics analysis for two cases, and more experiments, but the anchor has tighter scope-calibration. Comparable quality. |
| XyrNcsJhyN | 4.50 | R1 mid | Entropic confinement paper with interesting ideas but framing issues; current paper is more rigorous |
| WX8uuLUSR4 | 3.60 | R1 mid | Conflicting biases paper; the current paper is more focused and has stronger theoretical contributions |
| Vhohl7EcvO | 5.00 | R1 mid | Noise stability paper with mixed reviews; the current paper is more coherent |
| IlyesljaNb | 6.00 | R2 | Intrinsic training dynamics paper; similar quality and rigor level; comparable |
| Zunww3FHPU | 6.50 | R2 | Latent space dynamics paper; less directly comparable but similar score band |
| Pwnf1vsucu | 5.60 | R2 | Implicit models expressivity paper with polarizing reviews (8,8,2,2,8); current paper is more solid |
| NEDh1WmsgO | 5.00 | R2 | Catastrophic forgetting paper; unrelated |
| qBAV2DEvAC | 5.50 | R2 | Implicit bias / scaling laws paper; comparable quality level |
| g6kof5fSba | 6.00 | R2 | Loss of plasticity paper with similar dynamical-systems framing; comparable |

**Round 1 bracket:** 3.5–7.5 (the paper is clearly stronger than the ~3.0 reject-level anchors and weaker than the ~8.0 oral-level anchors, placing it in the middle band).  
**Round 2 narrowing:** The paper sits alongside the 5.5–6.5 anchors. It has broader scope and more testable predictions than B4zcoLvjw0 (6.0), but also a scope-calibration weakness that paper avoids. It is comparable in rigor and contribution to IlyesljaNb (6.0) and g6kof5fSba (6.0). The scope-overclaim issue prevents it from reaching the 6.5–7.0 range where papers with both breadth and tight claim-calibration sit.  
**Final score:** 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>