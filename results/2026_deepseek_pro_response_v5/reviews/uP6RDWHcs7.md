Now I have all the anchor comparisons I need. Let me synthesize everything into the final review.

**Anchor comparison summary:**

| Anchor | Score | Comparison |
|--------|-------|------------|
| qOgLmcJxxF (round 2) | 5.75 | Sample-efficient diffusion, theory paper with presentation issues. Our paper is stronger: cleaner presentation, broader experiments, more novel mechanism. |
| Jyh0DR4fFE (round 1) | 6.00 | Injective flows for star-like manifolds. Comparable: novel method with evaluation limitations (narrow applicability). Our method is more flexible and broadly applicable. |
| iXbUquaWbl (round 2) | 6.50 | GMM priors for diffusion samplers. Our paper is weaker on evaluation rigor — iXbUquaWbl has actual numbers in main text and more systematic experiments. |
| kBNIx4Biq4 (round 1) | 6.50 | Lifting architectural constraints of injective flows. More thorough evaluation including FID on images. Our core mechanism is comparably novel but evaluation is weaker. |

**Round 1 bracket**: 5.0–6.5
**Round 2 narrowing**: The paper sits between qOgLmcJxxF (5.75) and iXbUquaWbl (6.50), closest to Jyh0DR4fFE (6.00) but with a more significant evaluation gap (N_c unstudied). 
**Final score: 5.5**

The unstudied N_c dependency pulls the score below 6.0, but the genuine novelty, flexibility, and diverse experiments keep it well above rejection territory.

Now let me write the final review.

One more thing: for the decision — this is a borderline paper. Scores of 5-6 at ICLR typically correspond to borderline accept/reject. Given the major but fixable weaknesses, I'll go with "Reject" — the evaluation gaps (especially N_c) are too significant to accept in current form, but the paper could be strong with revisions.

Actually, let me reconsider. Looking at the anchors:
- Jyh0DR4fFE at 6.00 was accepted
- kBNIx4Biq4 at 6.50 was accepted
- qOgLmcJxxF at 5.75 was rejected
- iXbUquaWbl at 6.50 was accepted

For a 5.5 score, the decision should be Reject (though borderline).## Summary

This paper introduces Marginal Flow, a density estimation framework that models a target distribution as a finite-sample approximation to a marginal density ∫q(x|w)q_θ(w)dw. The core mechanism generates mixture component parameters w_i by pushing base samples through an unconstrained neural network f_θ, and resamples those w_i at each training iteration. This avoids Jacobian determinants, ODE solvers, and bijectivity constraints, enabling exact density evaluation, efficient single-step sampling, and manifold learning by simply reducing the base distribution dimension. The paper demonstrates the framework on synthetic densities, simulation-based inference, Wishart mixtures on positive-definite matrices, and manifold learning in VAE latent spaces.

## Strengths

- **Genuinely novel marginalization mechanism**: The core idea — learning a distribution over component parameters via an unconstrained NN with resampling — cleanly separates expressiveness from component count. Figure 1 provides compelling evidence: a fixed-set GMM with the same nominal number of components collapses to discrete blobs, while Marginal Flow's resampling produces a smooth density matching the ground truth. This mechanism is what distinguishes the method from both standard mixture models and flow-based approaches.

- **Manifold learning without architectural compromise**: As shown in Figure 4 and Section 2.3, Marginal Flow learns a density on a lower-dimensional manifold simply by choosing m < d in the base distribution — no special architectural modifications needed. The MNIST and JAFFE experiments (Figures 10-11) further demonstrate this capability, showing smooth interpolation along 1D learned manifolds with visible disentanglement of class and style.

- **Scalability demonstrated on a hard problem**: The Wishart mixture experiment (Section 4.3, Figure 9) shows Marginal Flow handling 100×100 positive-definite matrices (d=5050) via forward KL training — a setting described as "computationally prohibitive" for Normalizing Flows. At d=55, Marginal Flow achieves ~100× lower test KL than NF.

- **Training flexibility via dual efficiency**: Because Marginal Flow is efficient at both sampling and density evaluation, it supports both forward KL (log-likelihood) and reverse KL training. Figures 7 and 8 demonstrate this dual capability, with faster convergence than NF/FM/FFF on synthetic datasets under forward KL and comparable or superior reverse KL performance versus NF — the only other model capable of exact reverse KL training.

- **Modular parametric family**: The framework cleanly separates the learnable part (f_θ generating w) from the base density family q(x|w), validated concretely by swapping from Gaussian to Wishart distributions with no change to core architecture (Section 4.3).

## Weaknesses

### Fatal

None.

### Major

- **N_c is never reported or studied, making the headline speed claims uncalibrated**: The number of Monte Carlo samples N_c used to approximate the marginal integral is the single most important hyperparameter controlling the speed-vs-quality tradeoff. At any evaluation, the model computes an average over exactly N_c component densities — N_c forward passes through f_θ plus N_c evaluations of q(x|w). Yet the paper never reports what values of N_c were used in any experiment (line 145 defers to the appendix for runtime details, but N_c values are absent from the main text regardless), never ablates sensitivity to N_c, and never shows how density quality varies with N_c. The claim of being "orders of magnitude faster" (Figure 3, lines 145, 254, 323) is therefore uncalibrated: the reader cannot distinguish whether the speed comes from the architectural design (no Jacobian/ODE/inversion) or from using a small N_c that may sacrifice density quality.

- **SBI benchmark results have no quantitative numbers in the main text**: The paper claims "state-of-the-art results" on the SBI benchmark (line 280) but provides zero numbers in the main body — everything is deferred to an appendix figure ("Due to space constraints we report results in the Appendix in Figure 14"). A claim of state-of-the-art performance on a standard benchmark cannot be evaluated by a reader from the main text alone. Similarly, the few-sample regime results that support convergence-speed claims are only in appendix figures (line 254: "In the Appendix in Figure 13, we show the learned densities").

### Minor

- **The "not a mixture model" framing is overstated**: The paper explicitly states "Marginal Flow is not a mixture model" (line 216), yet Eq. 2 is literally a finite mixture formula and Section 2.2 acknowledges the model "resembles a mixture model with N_c components" (line 143). The distinction (resampling vs. fixed components) is real and important, but the categorical denial of being a mixture model is semantic overreach.

- **No limitations discussed**: The paper lacks any limitations section or paragraph. Given that the model is a Monte Carlo approximation, the dependence on N_c and the choice of parametric family q(x|w) are natural limitations that should be discussed.

- **Image manifold experiments are qualitative only**: The MNIST and JAFFE experiments (Section 4.4) show visually plausible manifolds but provide no quantitative metrics (e.g., log-likelihood on held-out latents, FID of decoded samples) to assess the quality of the learned densities. Claims about "disentanglement" are interpretative without quantitative support.

- **The claim that bijections "struggle to learn new modalities" is too categorical**: Line 199 states this as a general fact, but modern flow architectures with expressive coupling layers can handle multi-modal targets. The qualitative demonstration in Figure 5 is fine, but the blanket dismissal goes too far.

### Trivial

- Training objective implementation details (how forward and reverse KL are computed in practice) are deferred entirely to Appendix A.2 (line 228). A brief summary in the main text would aid readability.

## Nice-to-Haves

- An empirical study of how N_c affects density estimation quality and runtime, showing the Pareto frontier of N_c vs. test log-likelihood and wall-clock time.
- A direct ablation comparing training with fixed w_i (no resampling, i.e., neural-parameterized GMM) vs. resampling, controlling for N_c.
- Moving SBI quantitative results into the main text as at least a summary table.
- Quantitative metrics for the manifold learning experiments (MNIST/JAFFE).
- A discussion of the Monte Carlo approximation error and its implications.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Comparison to mixture density networks (Bishop 1994)**: REMOVED per hard rule — we do not flag missing related works, as we lack external sources to confirm their relevance.
- **NF Cholesky parameterization may not be the strongest NF for Wishart task**: REMOVED per hard rule — this is speculation about a baseline that, if true, would favor the baseline, not the authors' method.
- **"Few-sample regime" as a strength**: De-emphasized since the key evidence is in appendix-only figures and the claim is generic.
- **Claims about the appendix being "stripped by the parser" preventing evaluation**: REMOVED per hard rule — the appendix exists in the original submission; we evaluate what is in the main text.
- **The harsh critic's point about the "gap between marginalization framing and finite-mixture mechanism"**: Partially REMOVED as a separate weakness — the paper already acknowledges at line 143 that the model "resembles a mixture model" and at line 64 that the resampling "induces an approximation to the marginal distribution." The remaining valid concern (N_c not studied) is captured in the Major weakness above.

## Novel Insights

The paper's most distinctive insight is that resampling mixture component parameters during training — rather than optimizing a fixed set — allows a finite-component density estimator to behave like a genuinely continuous marginal distribution. This bridges the gap between mixture models (which collapse to discrete placements with small component counts) and continuous latent-variable models (which require expensive architectural constraints). The manifold-learning capability that falls out naturally from simply reducing the base distribution dimension is a genuinely elegant property not shared by flow-based or diffusion-based approaches.

## Suggestions

- Make an N_c ablation study the centerpiece of additional experiments: show test log-likelihood and wall-clock time as functions of N_c on at least two datasets (one synthetic, one SBI task). This would transform the "orders of magnitude faster" claim from uncalibrated to precisely characterized.
- Add a summary table of SBI C2ST scores in the main text, even if the full figure stays in the appendix.
- Add a brief limitations paragraph discussing: the N_c approximation tradeoff, sensitivity to the choice of q(x|w), and regimes where the method may underperform.
- Consider adding a simple quantitative metric (e.g., log-likelihood on held-out VAE latents) to the MNIST/JAFFE manifold experiments.

## Score and Decision

**Round 1 bracket**: 5.0–6.5, based on comparison against anchors spanning strong reject to strong accept on similar topics (density estimation, normalizing flows, manifold learning).

**Round 2 narrowing**: Retrieved anchors at 5.75 (qOgLmcJxxF — theoretical diffusion paper, rejected), 6.00 (Jyh0DR4fFE — injective flows for star-like manifolds, accepted), 6.25 (oAMArMMQxb — score-based multimodal sampling, accepted), and 6.50 (iXbUquaWbl — GMM priors for diffusion, accepted). The paper is clearly stronger than the 5.75 anchor (cleaner presentation, broader experiments, more novel mechanism), comparable to the 6.00 anchor (both have novel methods with evaluation limitations), and weaker than the 6.50 anchors (less thorough evaluation). The N_c study gap — the most important hyperparameter going unexamined — pulls the score below 6.0.

**Final assessment**: The paper presents a genuinely novel and flexible framework with distinctive capabilities (manifold learning without architectural compromise, modular parametric families, dual KL training). However, the complete absence of any study on N_c — the single most important hyperparameter controlling the speed-vs-quality tradeoff — leaves the headline efficiency claims fundamentally uncalibrated. Combined with the relegation of SBI quantitative results entirely to the appendix, the evaluation is not yet sufficient to fully substantiate the paper's central claims. The method itself is sound and the paper has the bones of a strong contribution, but the evaluation needs substantial strengthening.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>