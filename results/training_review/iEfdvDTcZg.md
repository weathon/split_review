Now I have all the evidence I need. Let me compile the final review.

## Summary

This paper conducts a large-scale empirical study of how the feature learning strength parameter $\gamma$ interacts with the learning rate $\eta$ in neural networks trained with SGD in the online setting. It maps out a phase portrait of the $\gamma$-$\eta$ plane across MLPs, CNNs, ResNets, and Vision Transformers, identifies scaling laws $\eta^* \propto \gamma^2$ (lazy regime) and $\eta^* \propto \gamma^{2/L}$ (ultra-rich regime), catalogs dynamical phenomena (catapults, silent alignment, stepwise loss drops), and provides a toy linear network model that analytically reproduces the observed scaling boundaries. The paper argues that with appropriate $\eta$ scaling, large-$\gamma$ networks match or outperform $\gamma=1$ networks in the online setting.

## Strengths

- **First systematic empirical mapping of the $\gamma$-$\eta$ plane across diverse architectures and losses**: The paper sweeps over nine orders of magnitude in both $\gamma$ and $\eta$ for MLPs, CNNs, ResNets, and Vision Transformers on MNIST-1M, CIFAR-5M, and TinyImageNet (Figures 1c,d). This yields a unified phase portrait — revealing a "triangle of optimizability" and power-law boundaries — that goes well beyond the limited regimes studied in prior work.

- **Identification and characterization of the under-explored "ultra-rich" ($\gamma\gg1$) regime**: The paper demonstrates that with proper $\eta$ scaling, large-$\gamma$ networks exhibit novel dynamics — silent alignment, stepwise loss drops, progressive sharpening at the end of silent alignment — that had previously been confined to toy models or small-scale settings. This catalog of phenomena is a useful empirical contribution.

- **Analytical toy model reproducing the observed scaling boundaries**: Section 4 develops a minimal deep linear network (reduced to a one-parameter model) that analytically yields the $\eta_{\min}$, $\eta_{\text{crit}}$, and $\eta_{\max}$ scalings for both MSE and cross-entropy losses (Table 1, Figure 7). The model shows how the depth-dependent $\gamma^{2/L}$ scaling follows from the Hessian of a multi-layer network, providing a theoretical anchor for the empirical phase portraits.

- **Hessian analysis linking spectral scaling to $\gamma$ regime**: The paper tracks Hessian eigenvalues across training and documents a clear transition from $\gamma^{-2}$ scaling (lazy, Gauss-Newton dominated) to $\gamma^{-2/L}$ scaling (rich) at convergence (Figure 3a). It also observes that in the rich regime, many eigenvalues grow to large scale, contrasting with the "$C$ outliers" picture common in classification — a new empirical finding.

- **Evidence of functional and representational convergence across large $\gamma$**: Function-output comparisons and kernel-target alignment (Figure 6) suggest that different large-$\gamma$ networks learn similar functions and maintain high alignment scores, while lazy networks cluster separately. This provides a suggestive picture of universality in the ultra-rich limit.

## Weaknesses

### Fatal
None.

### Major

- **The central scaling laws lack quantitative empirical validation**: The paper claims $\eta_{\max} \propto \gamma^{2/L}$ and $\lambda_{\max} \propto \gamma^{-2/L}$ at large $\gamma$, but these are supported only by visual inspection of phase portrait boundaries (dashed lines in Figures 1c,d). No fitted exponents, confidence intervals, or residual analyses are reported. For the $\gamma^{2/L}$ scaling in particular — where $L$ varies across architectures — it is unclear whether the data specifically support the claimed exponent or merely a general positive power. Given that these scaling laws are the paper's primary quantitative contribution, this lack of rigorous validation is a significant gap.

- **The claimed performance advantage of large $\gamma$ rests on thin evidence**: The abstract and contributions state that "optimal online performance is often found at large $\gamma$" and that larger $\gamma$ "yields equal or better generalization to $\gamma=1$." The main evidence is a single plot (Figure 2b) of test accuracy vs. $\gamma$ for one architecture (CNN) on CIFAR-5M with MSE loss (three seeds). The paper does not show analogous accuracy plots for cross-entropy loss, for other architectures (MLPs, ResNets, ViTs), or for other datasets. The effect at large $\gamma$ appears to plateau with marginal gains, which conflicts with the "often" in the abstract. The paper's own qualifier that "the returns are marginal past some point" (Figure 2 caption) further softens the headline claim. This claim needs substantially broader evidence to be convincing.

### Minor

- **The toy model, while useful, is presented with overly strong explanatory language**: The paper states the width-1, depth-$L$ linear network on a single example "explains all observed scaling relationships" and "analytically reproduces our phase portraits" (Section 4). The model provides useful analytical scaling derivations, but there is no argument connecting it to deep nonlinear networks on large datasets. The agreement could follow from dimensional analysis that any simple model would produce. The paper would be strengthened by presenting this model more cautiously — e.g., as a minimal model that *suggests* possible scalings, rather than one that *explains* the behavior of realistic networks. The absence of the two-parameter catapult model (deferred to the stripped appendix) also makes this section feel incomplete.

- **The use of synthetic and heavily augmented datasets limits generality of conclusions**: The online setting requires large datasets (MNIST-1M generated by a diffusion model, CIFAR-5M heavily augmented from CIFAR-10, TinyImageNet with strong augmentation). While the paper cites evidence (refinetti2023neural) that CIFAR-5M trajectories match CIFAR-10, the paper itself does not validate that the reported phenomena (especially the large-$\gamma$ performance advantage) reproduce on standard (non-augmented, non-synthetic) datasets. This is a limitation worth explicit discussion.

- **The function comparison (Figure 6a) relies on visual inspection without quantitative metrics**: The paper claims "strong agreement" between large-$\gamma$ networks based on scatter plots of function outputs, but does not report $R^2$, correlation coefficients, or other similarity metrics. Similarly, the CKA alignment curves are said to "agree" after time rescaling, but the degree of agreement is not statistically quantified.

### Trivial
None.

## Nice-to-Haves
- Testing whether the scaling laws hold for adaptive optimizers (Adam, SGD+Momentum), which are standard in practice.
- Directly comparing online vs. offline performance on the same dataset to confirm the claimed contrast with Petrini et al. (2022).
- Varying batch size over at least one order of magnitude to verify that the phase portrait is stable.
- Reporting Hessian eigenvalue evolution for at least one additional architecture beyond the CNN.

## Removed Points
These points are flagged to be removed; treat them with caution.

1. **Criticism about cross-entropy loss constants being "arbitrary and unexplained"**: The paper explicitly explains (lines 425–426) that $p_0 = (1+e)^{-1}$ and $p_1 = 1-p_0$ are chosen so the loss minimum occurs at $\tilde{f}(w)=1$. This is not arbitrary — the reviewer misread the section.

2. **Criticism about the "factor of $L$" being dismissed as "sloppy"**: The paper's footnote clearly acknowledges the factor and explains why it does not affect scaling ($L = \Theta(1)$). The reviewer overstates this as sloppiness.

3. **Criticism questioning whether the reference refinetti2023neural is "publicly verifiable"**: Hard rule — references cited in the paper are assumed to exist and be available. This criticism must be removed.

4. **Criticism about the Figure 3a caption being truncated**: Acknowledged by the reviewer as likely a parser artifact. This is a formatting issue, not an author error.

5. **Criticism that the time rescaling is "not specified"**: The rescaling $\tau = \eta t / \gamma$ is specified multiple times (lines 57, 248, 398). The reviewer missed these statements.

6. **Criticism about the toy model not being connected via "scaling argument, limit, or perturbation analysis"**: While the criticism that the model is simple is valid (kept in Minor), the claim that the paper provides *no* connection is overstated. The model analytically derives the same scaling exponents observed empirically, which is a valid form of theoretical support for a scaling law — the limitation is about generality, not absence of argument.

7. **Strength about "Demonstration of online training benefits for large $\gamma$" (from Strength Finder)**: This conflicts with the verified weakness that the evidence for this claim is thin. The weakness wins, so this strength is removed.

## Novel Insights
The reviews collectively highlight an important tension in this paper: the gap between the ambitious scope of its claims and the robustness of their validation. The harsh critic correctly identifies that the scaling laws — presented as precise power laws with specific depth-dependent exponents — are not quantitatively fitted, and that the headline claim about large-$\gamma$ performance rests on a single accuracy plot. The strength finder correctly notes that the paper's architecture sweep and phase portrait are genuinely novel and useful. The synthesis is that this paper has a real empirical contribution (the phase portrait, the catalog of phenomena, the Hessian analysis) that is valuable even if the stronger quantitative claims are overstated. The toy model is a useful theoretical anchor but should not carry the burden of "explaining" all observed behavior in realistic networks. The paper would be substantially improved by either providing rigorous quantitative validation of its scaling claims or honestly reframing itself as a qualitative empirical study.

## Suggestions
1. **Quantitatively validate the scaling exponents**: For at least one architecture, fit $\eta_{\max}$ vs. $\gamma$ on log-log axes for the ultra-rich regime and report the fitted exponent with confidence intervals. Do the same for $\lambda_{\max}$ scaling in the Hessian analysis. This would substantiate the paper's central quantitative claim.
2. **Broaden the evidence for large-$\gamma$ performance**: Show test accuracy vs. $\gamma$ for at least one additional architecture (e.g., MLP or ViT) and for cross-entropy loss. Alternatively, tone down the claim to match the evidence.
3. **Tone down the toy model's claimed explanatory power**: Reframe Section 4 as presenting a minimal model that *suggests* or *reproduces* the scalings, rather than one that *explains* them in realistic networks. Add a paragraph discussing when the model's assumptions break down.
4. **Add quantitative metrics to the function/representation comparison**: Report $R^2$ for the function scatter plots and a similarity score (or correlation) for the CKA alignment across $\gamma$ values.

## Score and Decision

This paper makes a genuine empirical contribution through its comprehensive mapping of the $\gamma$-$\eta$ phase portrait across architectures, its catalog of dynamical phenomena in the under-explored ultra-rich regime, and its Hessian analysis linking spectral scaling to $\gamma$. The toy model provides a useful theoretical complement by analytically deriving the observed scaling boundaries. However, the paper overstates its claims in two key areas: the scaling laws are not quantitatively validated with fitted exponents and confidence intervals, and the claim that large $\gamma$ yields optimal performance rests on thin evidence from a single architecture-dataset combination. These gaps prevent the paper from fully establishing its central quantitative contributions. The paper would significantly benefit from either addressing these validation gaps or reframing its contribution as a qualitative empirical study.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>