- Decision: Reject
- Avg Score: 3.75
- Scores: 6, 3, 3, 3
Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper distinguishes between "gradient noise" (variance of stochastic gradient) and "search direction noise" (gap between optimizer's update direction and the steepest descent direction) to analyze the role of momentum in DNN training. It derives closed-form expressions for the "degree of smoothing" δ for SGD, SHB (stochastic heavy ball), and NSHB/normalized momentum. Using convergence bounds, the paper estimates the critical batch size and back-computes upper bounds on gradient variance, enabling a numerical comparison of δ across optimizers. The central empirical finding is that δ tracks test accuracy across batch sizes for ResNet18 on CIFAR-100, with SHB maintaining a non-zero δ for large batches (explaining its large-batch generalization advantage), while SGD and NSHB δ decay to zero.

---

## Strengths

1. **Novel distinction between gradient noise and search direction noise.** Prior work treated "stochastic noise" monolithically as gradient variance. The paper shows that momentum reduces gradient variance (Section 3.3, Table 1) while increasing search direction noise (Eqs. \ref{eq:shb}, \ref{eq:nshb}), resolving an apparent contradiction in the literature. This conceptual reframing is genuinely useful.

2. **Closed-form δ expressions for momentum methods.** The paper derives explicit formulas for δ^SHB and δ^NSHB (Eqs. \ref{eq:shb}, \ref{eq:nshb}) that depend on η, b, β, gradient variance C², and gradient norm K² — extending the prior analysis of Sato & Iiduka (limited to SGD). The SHB formula includes a term (β̂ K²) that does not vanish as batch size grows, providing a concrete theoretical mechanism for SHB's large-batch advantage.

3. **Explanation of SHB's large-batch generalization.** The paper gives a clean, nontrivial explanation (Section 5): SHB's δ does not approach zero for large batches because of the K² term, so SHB continues to smooth the objective even at large b, while SGD and NSHB lose their smoothing and fall into sharp minima. This explains experimental observations by Shallue et al. and Kunstner et al. that were previously not well-understood theoretically.

4. **Empirical estimation of gradient variance from critical batch size.** Section 3.3 provides a method to estimate C² by back-calculating from experimentally determined critical batch sizes (Table 1). While the estimates are upper bounds, the approach connects convergence theory to experiment in a creative way.

5. **Figure 1's δ-vs-accuracy relationship is visually compelling.** The right panel of Figure \ref{fig:01} shows a unimodal relationship between δ and test accuracy, with optimal δ in a middle range — directly supporting the claim that an appropriate level of stochastic noise (neither too much nor too little) leads to good generalization.

---

## Weaknesses

### Fatal
None.

### Major

1. **The Gaussian-to-ball-uniform approximation in the smoothing derivation is not properly justified.** In the core theoretical argument (lines 188–196), the paper models the search direction noise as $u_t \sim \mathcal{N}(0, (1/\sqrt{d})I_d)$, then approximates this with $u_t \sim B(0;1)$ (uniform on the unit ball) by appealing to the fact that "the standard normal distribution in high dimensions $d$ is close to a uniform distribution on a sphere with radius $\sqrt{d}$" (citing Vershynin). There are two issues: (i) The Vershynin result concerns $\mathcal{N}(0, I_d)$ approximating the *sphere* of radius $\sqrt{d}$, not the *ball* used in Definition 1; (ii) the paper's own $u_t$ is scaled by $1/\sqrt{d}$ relative to the standard normal, so the connection to the relevant object (ball $B(0;1)$) is unclear. The paper treats this as a brief aside (hence the "≈" sign) but the entire smoothing claim — that SHB updates are approximately gradient descent on $\hat{f}_δ$ — depends on this step. Without a rigorous justification or a validation that the approximation error is small for the actual noise distributions encountered during training, this part of the theoretical framework is incomplete.

2. **The $C^2$ values are upper bounds used as point estimates, inflating the quantitative δ comparison.** The paper derives $C^2 < b^* ε^2 / (η·factor)$ — an *upper bound*, not an estimate. These upper bounds are then plugged directly into the δ formulas (Eqs. \ref{eq:sgd}–\ref{eq:nshb}) and treated as exact values for the quantitative comparison in Figures \ref{fig:delta} and \ref{fig:01}. The true $C^2$ could be much smaller, especially for SHB where the bound is 25.3 (the true value could be 1 or less). Since the degree of smoothing depends on $\sqrt{C^2}$, this inflates SHB's δ relative to other optimizers, and the claim that "SHB always has a greater degree of smoothing than SGD" relies on a comparison of upper bounds rather than estimates with known tightness. The qualitative observation that SHB δ contains a $K^2$ term that does not vanish at large batches is robust, but the precise δ values and the exact gap between optimizers are not.

3. **The central claim — that δ "dominates model generalizability" — is tested in only one experimental setting.** The main δ-versus-test-accuracy results (Figures \ref{fig:delta}, \ref{fig:04}, \ref{fig:01}) are all for training ResNet18 on CIFAR-100 with η=0.1, β=0.9. While Table 1 shows C² estimates for several architectures and datasets, there is no evidence that the δ-vs-accuracy correlation holds for those settings. The paper acknowledges this limitation (line 62), but the headline claim ("δ dominates model generalizability") significantly outstrips the evidence. Without varying architectures, datasets, learning rates, or momentum values, it is impossible to know whether the observed correlation is a general phenomenon or specific to this configuration.

4. **No training loss curves are reported.** The paper reports only test accuracy (Figure \ref{fig:04}). Without training loss curves, it is impossible to distinguish whether SHB's lower peak accuracy at moderate batch sizes is due to excessive smoothing (as the paper claims) or to underfitting / higher training loss. If SHB simply converges to a point with higher training loss, the mechanism is not smoothing-induced overfitting but rather poorer optimization. Training curves would provide crucial evidence for the paper's causal narrative.

### Minor

1. **The "contradiction resolved" framing is overstated.** The paper defines gradient noise and search direction noise as distinct quantities, then shows momentum reduces the former and increases the latter. This is a useful reframing but not the resolution of a logical paradox — the two statements "momentum reduces noise" and "noise improves generalization" were only contradictory because "noise" was used ambiguously in previous work. The paper's genuine contribution is the quantification of search direction noise, not the resolution of a deep inconsistency.

2. **The claim that "NSHB has almost no experimental value" is too strong given the data.** At moderate batch sizes (e.g., b=2^8), NSHB achieves similar test accuracy to SGD (~65% vs ~68%), which is the standard baseline. This is comparable to many widely-used training recipes. The claim (line 339) would require evidence across architectures, datasets, and hyperparameters that NSHB never provides any benefit — which the paper does not have.

3. **The paper does not address whether δ changes during training.** The analysis treats δ as a constant determined by hyperparameters, but in practice the gradient variance (C²) and gradient norm (K²) evolve over the course of training. The smoothing effect may vary in magnitude across different phases of training (e.g., initial vs. final stages). This could affect the interpretation of the results.

4. **The stopping condition ε=0.5 and the method for determining b* are not fully justified.** The paper uses ε=0.5 as a threshold for convergence but does not discuss sensitivity to this choice or how it was selected. Different ε values would shift the estimated critical batch sizes and hence the C² upper bounds.

### Trivial
None.

---

## Nice-to-Haves

- **Comparison to Adam.** The paper focuses on SGD, SHB, and NSHB. Since adaptive methods dominate practice and also have momentum-like terms, showing where Adam's δ falls in the framework would significantly strengthen the claim that δ is "a hidden factor in DNN training."
- **Causal experiment.** An experiment where synthetic isotropic noise of known magnitude is injected into the update (e.g., adding Gaussian noise with controlled variance to the gradient) would directly test whether δ drives generalization rather than merely correlating with it.
- **Sensitivity analysis for ε.** Reporting how the C² estimates change for different ε thresholds (e.g., ε ∈ {0.25, 0.5, 1.0}) would help assess the robustness of the quantitative results.

---

## Removed Points

- **Point about missing proofs in appendix.** The critic notes "the proof is not given in the main text (reference to appendix)." This is standard for conference papers and the appendix is present in the original submission — removed per Hard Rules.
- **Point about questionable existence/release of cited works.** The critic does not raise this, so not applicable.
- **Point about A4 assumption being strong ("gradient norms can be large early in training").** This is a known and standard assumption in the optimization literature. Its violation during early training does not undermine the analysis, which concerns the overall training trajectory. Removed as generic speculation.
- **Point about Assumption 3.1 (bounded iterates) not being verified.** The paper acknowledges this is a standard assumption used in prior work (Kingma et al., Reddi et al.). It is clearly stated and the paper is transparent about using it. Removed as a nitpick about a well-accepted assumption.
- **Point about Lemma 2 not addressing curvature.** The critic claims "it depends on the function's curvature" — but Lemma 2 is a Lipschitz bound, which is valid regardless of curvature. The critic's deeper point (that "too large" isn't well-defined) is fair, but the specific criticism about curvature is factually wrong. Removed.

---

## Novel Insights

None beyond the paper's own contributions. The two reviews largely agree on the paper's strengths and weaknesses, though the harsh critic overstates the severity of the sphere/ball distributional approximation (treating it as fatal when the core qualitative predictions — SHB's non-vanishing δ term, the δ-vs-accuracy correlation — survive even with a different noise distribution) and the paper's own stated limitation partially preempts the experimental-scope criticism.

---

## Suggestions

1. **Fix the smoothing derivation.** Either provide a rigorous justification for the Gaussian-to-ball-uniform approximation (e.g., show that for the Lipschitz functions considered, the difference between convolution with the spherical and ball distributions is bounded by a controlled constant), or derive δ directly under the Gaussian noise model without invoking the ball-uniform smoothing definition.

2. **Report confidence intervals on δ.** Run the critical-batch-size experiment multiple times and propagate uncertainty through the C² bounds to δ. Show that the qualitative gap between SHB and SGD/NSHB holds under worst-case (lowest plausible C_SH², highest plausible C_SGD²) assumptions.

3. **Expand experimental scope for the central claim.** At minimum, show the δ-vs-test-accuracy relationship for one additional architecture (e.g., WideResNet) or one additional dataset (e.g., CIFAR-10). If the correlation holds, this would significantly strengthen the paper.

4. **Add training loss curves.** Report training loss alongside test accuracy to distinguish between the smoothing mechanism and alternative explanations (underfitting, optimization failure).

5. **Tone down the "contradiction resolved" and "NSHB has no value" framings.** These are overclaims that invite criticism without adding substance. The paper's contribution stands on the δ formulas and the explanation of SHB's large-batch behavior.

---
