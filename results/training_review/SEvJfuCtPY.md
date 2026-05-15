Now I have all the information needed. Let me craft the final consolidated review.

---

## Summary

This paper analyzes how a two-layer denoising autoencoder learns the velocity field for a flow-based generative model on a high-dimensional two-mode Gaussian mixture. The key insight is that without time dilation, the phase where the mode probability (high-level feature) is learned disappears in the infinite-dimensional limit. The authors propose a piecewise-linear time dilation that preserves this phase, enabling a decomposition into two learning phases — one for the mode probability and one for the mode variance. Asymptotic (heuristic) equations characterize the learned parameters in each phase, and an experiment on MNIST demonstrates that focusing training on phase-transition times improves feature accuracy.

## Strengths

- **Novel time-dilation technique with clear motivation (Section 3).** The paper identifies a concrete problem: the speciation time at $t_s = 1/\sqrt{d}$ vanishes as $d\to\infty$, causing the mode-probability phase to disappear. The piecewise-linear dilation (Equation 12) stretching $[0,\kappa/\sqrt{d}]$ to $[0,1]$ directly addresses this. This is a clean, well-motivated solution that builds on and extends the analyses of Cui et al. (2024) and Biroli et al. (2024).

- **Asymptotic characterization revealing clean two-phase separation (Results 1 & 2, Corollaries 1 & 3).** The closed-form equations for the neural network overlaps show that in Phase I the network only estimates $p$ (mode probability), while in Phase II it only estimates $\sigma^2$ (mode variance). Corollary 1 gives $m=1,\ \omega=\kappa t,\ \tanh(b)=2(p-1/2)$ with no dependence on $\sigma^2$, and Corollary 3 gives $c = \tau\sigma^2/(1+(\sigma^2-1)\tau^2)$ with no dependence on $p$. This clean modularization is a genuine structural insight about how diffusion models decompose a complex learning task.

- **MSE discontinuity as a practical phase-transition signal (Corollary 5).** The observation that the test MSE jumps from $\sigma^2+4p(1-p)$ at $t=0$ to $\sigma^2$ at $t=0^+$ without dilation, while the dilated schedule gives a smooth transition, provides a concrete diagnostic for detecting phase boundaries without prior knowledge of the data distribution. This connects theoretical phase structure to observable training dynamics.

- **MNIST proof-of-concept validates the practical utility (Section 6.2).** The U-Turn method identifies $t\in[0.3,0.5]$ as the critical interval for digit-class assignment. Training with doubled sampling density in this interval improves the generated proportion of digit 0 from 88.2% to 81.0% (closer to the true 80%). This demonstrates that the theoretical insight about phase-aware training transfers beyond the tractable Gaussian mixture setting to realistic SDE-based models.

## Weaknesses

### Fatal
None.

### Major

- **Heuristic derivations limit the strength of the theoretical claims.** The paper explicitly describes Results 1 and 2 as derived "at the level of rigor of theoretical physics" (lines 195, 238). While this level of rigor is standard in the statistical physics of ML community and the paper is transparent about it, there is a tension with the abstract's phrasing of "sharp asymptotic characterization." A reader trained in rigorous probability theory will find the gap between "sharp" and "heuristic" jarring. The paper would benefit from a clear self-contained statement of the assumptions and limit procedures under which the heuristic derivation is expected to hold, and an honest discussion of where rigorous proof would be needed to fully validate the claims.

- **Experimental validation lacks statistical grounding.** The Gaussian mixture experiment (Figure 1) reports results from a single training run with no error bars — only $K=2000$ ODE rollout realizations (which are post-training). The configuration uses a single $(n=128, d=5000, p=0.8, \kappa=4)$ setting. Similarly, the MNIST experiment reports single proportions (88.2%, 81.0%, 81.1%) without confidence intervals or multiple-seed statistics. Without a sense of variability, the reader cannot assess whether the observed improvements are significant or whether the method is robust to different random initializations.

### Minor

- **Sample complexity claim is not experimentally verified.** The paper claims that $\Theta_d(1)$ samples suffice to learn the velocity field, and the theory is consistent with this (finite $n$ as $d\to\infty$). However, no experiment varies $n$ to demonstrate how small $n$ can be or how the learned parameters converge as $n$ grows. A simple ablation showing estimated $p$ vs. $n$ for fixed large $d$ would substantially strengthen this claim.

- **No comparison to alternative non-uniform schedules on MNIST.** The MNIST experiment compares the U-Turn-guided schedule only to uniform sampling. It is unclear whether the improvement is due to the specific U-Turn method or simply to any non-uniform schedule that up-weights early times (e.g., importance sampling based on loss magnitude, or a hand-designed schedule oversampling early times). An additional baseline would isolate the benefit of the phase-aware approach.

- **The U-Turn schedule selection uses the already-trained model, creating a form of data-dependent selection.** The paper first trains a model with uniform sampling, uses U-Turn on that model to identify critical times, then trains a new model from scratch with the identified schedule. While training from scratch mitigates double-dipping, this procedure is still a form of data-dependent schedule selection and its statistical properties (e.g., overfitting risk) are not discussed.

### Trivial
None — the paper is well-organized and clearly written for its target audience.

## Nice-to-Haves

- A systematic study of how the estimated $p$ depends on $\kappa$ (the dilation hyperparameter) for finite $d$, bridging the $\kappa\to\infty$ limit taken in Corollary 6.
- Plots showing the evolution of the overlaps $m(t), \omega(t), c(t)$ alongside theoretical predictions from Corollaries 1 and 3 to visually confirm the two-phase behavior.
- A brief discussion of how the time-dilation idea might generalize to data distributions beyond two-mode Gaussians (e.g., mixtures with more components, or features at multiple scales).

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Criticisms about missing appendix/derivations/proofs.** The parser strips supplementary sections from all papers; the derivations exist in the original submission. The paper's own characterization of the derivations as "heuristic" and "at the level of rigor of theoretical physics" is retained as a valid concern (see Major weakness above), but complaints that proofs are entirely absent from the submission are invalid.
- **Claim that Proposition 1 is imprecise.** The proposition clearly states the distribution of $X_t$ (Gaussian on the orthogonal subspace) and gives explicit limit distributions for $\nu_1$ and $M_2$. The notation is standard for this community.
- **Criticism that Corollaries depend on unproven Results.** This is a tautology about what a corollary is, not a valid weakness.
- **Formatting and stylistic nitpicks.** The PDF extraction artifacts (garbled symbols, missing line breaks) are parser errors.
- **Missing related works.** As per instructions, I cannot verify the existence of missing references.

## Novel Insights

The reviews collectively surface a subtle tension that the paper itself does not fully address: the time-dilation trick is elegant but introduces its own hyperparameter $\kappa$, and Corollary 6 requires $\kappa\to\infty$ to recover $p$ exactly. This suggests that in practice there is a trade-off between how much one dilates (which determines how well $p$ is learned) and the computational cost of simulating the ODE over a longer dilated interval. The paper does not characterize this trade-off, and doing so would significantly strengthen the practical guidance for applying the method. Additionally, neither review observes that the clean phase-separation result (Corollaries 1 and 3) depends on taking $d\to\infty$ *then* $n\to\infty$ — the order of limits matters, and the finite-$n$, finite-$d$ regime where both $p$ and $\sigma^2$ may be partially entangled in both phases is left unexplored. This is a natural direction for follow-up work rather than a flaw in the current paper.

## Suggestions

1. **Add error bars to all experiments.** Report means and standard deviations over at least 5 random seeds for both the Gaussian mixture and MNIST experiments. This single change would substantially increase confidence in the results.
2. **Add a sample-complexity ablation.** Vary $n$ from small (say 4, 8, 16, …) to 256 for fixed $d=5000$ and show how the estimated $p$ and $\sigma^2$ converge. This would directly support the $\Theta_d(1)$ claim.
3. **Add a non-uniform baseline for MNIST.** Compare the U-Turn schedule against a simple early-time oversampling schedule (e.g., sample times with density proportional to $1/t$) to isolate the benefit of the phase-aware approach over generic non-uniformity.
4. **Tone down "sharp" in the abstract** to "asymptotic" or "heuristic asymptotic" to better match the paper's own characterization of the derivations.
5. **Discuss the $\kappa$ trade-off.** Provide practical guidance on choosing $\kappa$ and show how the learned $p$ depends on $\kappa$ for finite $d$.

## Score and Decision

The paper makes a genuine contribution: the time-dilation technique is clean, well-motivated, and demonstrably effective. The asymptotic analysis (even if heuristic) reveals a clean modular structure that deepens our understanding of how diffusion models decompose feature learning across timescales. The MNIST proof-of-concept shows the ideas transfer beyond synthetic data. However, the experimental validation is noticeably thin — no error bars, no parameter variation, no baselines — which limits the strength of the empirical conclusions. The paper is acceptable for a venue that values theoretical insight over exhaustive experimentation, but would benefit from targeted experimental additions before publication.

Overall assessment: the core idea is solid and well-presented; the main weaknesses are in the experimental evaluation, not in the conceptual contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>