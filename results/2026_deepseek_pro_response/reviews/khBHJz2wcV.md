Now I have a complete calibration picture. Let me write the final review.

**Round 1 bracket**: 5.0–7.0

**Round 2 narrowing**: The most relevant anchors are:
- ORW-CFM-W2 (6.00): reward fine-tuning of flow matching. Our paper has broader evaluation and more novelty, but similar level of theoretical rigor.
- DRaFT (6.00): reward fine-tuning of diffusion models. More polished large-scale experiments, less novelty. Comparable overall.
- Physics-Informed Diffusion Models (5.75): training-time physics constraints. Our paper is more novel with broader evaluation.

The paper is clearly above 5.75 and comparable to the 6.00 anchors. Its joint state-parameter evolution is genuinely novel, the evaluation is broad, and the ablations are well-designed. The major weaknesses (unexamined one-step approximation, missing inference-time baselines) prevent a higher score but are addressable. **Final score: 6.0, Accept.**

---

## Summary
This paper proposes a post-training framework for fine-tuning flow-matching generative models to enforce parameter-dependent PDE constraints while jointly inferring latent physical parameters. The key technical idea is a joint state-parameter evolution where a surrogate base flow for the unknown parameter α is constructed using an inverse predictor φ and a one-step estimate from the base model. The method is cast as a stochastic optimal control problem via Adjoint Matching with weak-form PDE residuals as reward, and introduces a scaled memoryless noise schedule for numerical stabilization. Experiments span four PDE families (Darcy, elasticity, Helmholtz, Stokes) and one natural-image domain transfer.

## Strengths
- **Novel joint state-parameter evolution via surrogate base flow**: The central technical contribution — augmenting the flow to evolve both state x and latent parameter α using a surrogate base flow derived from the inverse predictor φ — is genuinely novel and well-motivated. Its value is clearly demonstrated in the Stokes experiment (Figure 5), where the joint model achieves MMD_α ≈ 0.07–0.13 versus 0.22–0.28 for ablations at comparable residual levels. In Helmholtz (Table 2), the full joint AM achieves the best residuals and lowest MMD_x among all methods.

- **Scaled memoryless noise schedule as a practical extension**: The generalization of the canonical memoryless noise schedule to σ²(t) = (1−κ)2η_t provides a theoretically consistent control-fidelity knob. The practical motivation — mitigating blow-ups near t→0 for pixel-space PDE models — is clearly articulated and well-justified.

- **Strong ablation design**: The comparison hierarchy (Base AM, Base AM+φ, PBFM) with shared noise seeds across all methods cleanly isolates the contribution of joint α flow from the inverse predictor and the Adjoint Matching mechanism. The controlled trade-off ablations in Figure 3 (Darcy) give practitioners clear levers for navigating the residual-vs.-diversity and residual-vs.-fidelity trade-offs.

- **Computationally practical**: Fine-tuning on Darcy requires only 20 gradient steps and completes in under 15 minutes on a single NVIDIA L40S, with no inference-time overhead.

- **Broad empirical evaluation**: The method is tested across four PDE families with distinct mismatch types (observation noise, BC misspecification, damping mismatch, forcing mismatch), plus a cross-domain demonstration on natural images, showing the framework's generality.

## Weaknesses

### Fatal
None.

### Major
- **The one-step approximation for the surrogate base flow is presented without discussion of its validity**: Equation (line 89), $\hat{x}_1 = x_t + (1-t)v_t^{\text{base}}(x_t)$, is exact only for straight-line conditional trajectories but is an approximation for the learned marginal vector field. This bias propagates through φ into $\hat{\alpha}_1$ and then into the surrogate base vector field $v_{t,\alpha}^{\text{base}}$ that anchors the entire joint evolution. The paper presents this estimate as a straightforward computation without acknowledging the approximation or characterizing when it holds. This matters because the joint evolution mechanism — the paper's central technical claim — depends on this estimate.

- **Missing inference-time guidance baselines**: The Related Work section discusses inference-time guidance methods (Huang et al., 2024; Xu et al., 2025; Christopher et al., 2024) in detail, yet none appear as experimental baselines. These are natural competitors for post-training or inference-time constraint enforcement. Their absence is most noticeable on Darcy and Helmholtz, where the paper's own ablations are compared but no external inference-time method anchors the results.

### Minor
- **PBFM comparison framing should acknowledge the paradigm distinction**: PBFM embeds physics constraints during training, while the proposed method is post-training. The paper compares them head-to-head (Tables 1–2) without explicitly acknowledging this paradigm difference. A reader cannot cleanly attribute observed differences to the training-time vs. post-training distinction versus genuine differences in constraint enforcement quality.

- **FM+ECI results on elasticity reported without discussion**: Table 1 shows FM+ECI achieving zero BC error but catastrophically violating the PDE interior ($\mathcal{R}_{\text{weak}} \approx 10^3$). The paper notes the result in passing (line 181) but does not discuss why this baseline — designed for hard constraint enforcement — performs so poorly. A brief analysis would strengthen the comparison's informativeness.

- **MMD values reported without uncertainty estimates**: With 256 samples, MMD values are reported to two decimal places without confidence intervals. Minor differences (e.g., MMD_x = 0.07 vs. 0.09 in Table 2) may not be statistically meaningful. Bootstrap confidence intervals would be straightforward to compute.

- **No limitations section**: A paper deploying multiple approximations (one-step estimate, surrogate base flow, inverse predictor under distribution shift, weak-form residual as proxy) should discuss failure modes and validity regimes. Its absence makes it harder to assess the method's scope.

- **Natural-image experiment connection to core thesis is thin**: Section 4.6 applies the joint evolution to parametric recoloring of natural images. While this demonstrates architectural generality, a polynomial color transform is not a physical constraint. The experiment would benefit from clearer framing of what it validates and what it does not.

### Trivial
- The initialization $\alpha_0^{\text{base}} \sim \mathcal{N}(0,I)$ (line 91) lacks physical motivation. A brief justification would help readers.
- The abstract states the method "effectively address[es] ill-posed inverse problems" but the paper provides no analysis of uniqueness — it shows parameters are plausible under the PDE residual, not uniquely identified.

## Nice-to-Haves
- An empirical characterization of the one-step estimate's fidelity (e.g., comparing $\hat{x}_1$ to the actual final sample $x_1$ along base trajectories) would strengthen confidence in the surrogate base flow.
- An analysis of φ's prediction accuracy on fine-tuned samples at different stages of training would address the distribution-shift concern.
- Including at least one inference-time guidance baseline for Darcy or Helmholtz would anchor the results against an independent reference point.
- Bootstrap confidence intervals for MMD metrics.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Harsh Critic's claim that the one-step approximation is "fatal/structural"**: The approximation is genuine but the empirical results suggest it is benign in practice. The paper uses the OT path which encourages approximately straight trajectories. Demoted from Fatal to Major.
- **Harsh Critic's claim about φ distribution shift being a critical evidential weakness**: The paper has a regularization mechanism ($v_{t,\alpha}^{\text{reg}}$ and running state cost $f(\alpha)$) designed precisely to address this. While an ablation would be informative, the concern is not a gap in the method. Removed from Major; the suggestion remains in Nice-to-Haves.
- **Strength Finder's claim that "the weak-form PDE residuals with stochastic local test functions" is a core strength**: This is a sensible design choice rather than a novel contribution. Moved to supporting context.
- **Harsh Critic's demand for analysis of the scaled noise schedule proof**: The proof is in the stripped appendix (Lemma 1, Appendix D.4). Cannot verify, but the practical motivation is independently clear. Not treated as a weakness.
- **Harsh Critic's concern about the sparse observations guidance mechanism description**: The paper explicitly states details are in Appendix E.4 (stripped). The main text description (line 169) is adequate for understanding the approach.

## Novel Insights
The paper's key insight — that an inverse predictor φ trained on base-distribution samples can serve double duty as both a residual evaluator and a surrogate base flow constructor for joint state-parameter evolution — is genuinely novel. This bridges a gap between physics-informed learning (which typically requires paired data or known parameters) and post-training preference optimization (which typically handles only fixed constraints). The empirical finding that the joint flow yields substantially better parameter-distribution fidelity (MMD_α) at comparable residual levels compared to variants treating α separately (Figure 5) validates this design and could inform future work in physics-constrained generative modeling.

## Suggestions
- Add a limitations subsection discussing validity regimes of the one-step estimate, the inverse predictor under distribution shift, and the weak-form residual as a proxy for full PDE satisfaction.
- Re-frame the PBFM comparison to acknowledge the training-time vs. post-training paradigm distinction, clarifying what the comparison does and does not establish.
- Discuss the FM+ECI failure on elasticity — even a brief note on why hard BC projection may be incompatible with PDE consistency in this setting.
- Compute bootstrap confidence intervals for MMD values and report them alongside point estimates.

## Score and Decision

**Calibration anchors:**
| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| Flow Matching + Simulator Feedback (DoDNJdDntB) | 4.20 | R1 | Our paper is substantially stronger: broader evaluation, more novel contribution, better ablation design |
| Physics-Informed Diffusion Models (tpYeermigp) | 5.75 | R1/R2 | Our paper has more novelty (joint evolution vs. adapting virtual observables) and broader evaluation (4 PDEs vs. 2 tasks) |
| ORW-CFM-W2 (2IoFFexvuw) | 6.00 | R2 | Comparable; our paper has broader evaluation and more novel mechanism, ORW-CFM-W2 has more theoretical analysis |
| DRaFT (1vmSEVL19f) | 6.00 | R2 | Comparable; DRaFT has more polished large-scale experiments, our paper has more novel technical contribution |
| Solving DEs with Constrained Learning (5KqveQdXiZ) | 5.25 | R1 | Our paper is stronger in both novelty and evaluation breadth |

The paper sits clearly above the 5.75 anchor and is comparable to the 6.00 anchors. The joint state-parameter evolution mechanism is genuinely novel, the evaluation is broad, and the ablation design is strong. The major weaknesses (unexamined one-step approximation, missing inference-time baselines) are addressable and do not invalidate the core contribution. **Score: 6.0, Accept.**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>