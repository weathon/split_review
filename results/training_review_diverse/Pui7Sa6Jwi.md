Now I have verified all the claims against the paper. Let me write the consolidated review.

---

## Summary

This paper proposes CLEAR, a representation learning framework for visual offline RL that explicitly models exogenous distractions. The paper formalizes the problem as an ExoPOMDP, identifies theoretically why standard latent dynamics models incorporate "superfluous information" from distractions, and introduces a method with separate encoders for agent state and exogenous factors, regularized by inverse-dynamics-based objectives. Empirical results on the DeepMind Control Suite with multiple distraction types show that CLEAR substantially outperforms prior methods, achieving near-oracle performance in the hardest settings (e.g., ~99 on Walker-Walk with 2×2 Grid vs. ~70 for the best baseline).

## Strengths

1. **Principled information-theoretic identification of the distraction problem.** The paper formalizes visual offline RL as an ExoPOMDP and derives (Equation 2) that maximizing predictive information in standard latent dynamics models inevitably captures "superfluous information" about exogenous factors that cannot be minimized without explicit modeling. This provides a clean theoretical diagnosis of why methods like SLAC degrade under distractions (Section 2.2).

2. **Novel controllability-based regularization.** CLEAR uses a min-max objective (Equations 6–7) that maximizes action predictability from state representations while minimizing it from exogenous representations. This is a principled way to enforce that the state encoder captures only controllable factors. The ablation study (Table 3, Figure 5) confirms the regularization is critical: without it, representations can "flip" or become degenerate.

3. **Strong empirical performance across distraction levels.** On the DMC Suite with clean, video, and grid distractions, CLEAR consistently achieves the highest or near-highest normalized scores (Table 1). The gap is most dramatic on harder distractions — e.g., on Walker-Walk with 2×2 Grid, CLEAR matches its clean-environment performance while the best baseline (InfoGating) drops substantially, showing the method successfully identifies the controllable agent even among multiple identical-looking agents.

4. **Qualitative and quantitative validation of disentanglement.** Ground-truth state regression (Table 2) shows CLEAR maintains low MSE across all distraction levels. The compositional decoder visualizations (Figure 4) demonstrate that the model cleanly separates the agent from background distractions, and even recovers occluded background content.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Incomplete derivation from the information-theoretic objective to the training loss.** The paper defines an information-theoretic objective J(θ) (Equation 3) and states a lower bound can be derived, jumping directly to Equation 4–5 without showing the algebraic steps. Additionally, there is an inconsistency: the exogenous encoder is defined as p_θ(ê_t|o_t) (line 74), but the KL divergence in Equation 5 uses p_θ(ê_t|o_t, ê_{t-1}) without explanation. The overall loss is plausible and the method works well empirically, but the paper's framing as a fully-derived "information-theoretic framework" is weakened by these gaps. The derivation should either be completed in the paper or the paper should more candidly describe the loss as inspired by information-theoretic principles followed by practical design choices.

2. **Min-max optimization details are underspecified.** The paper describes optimizing Equation 7 via "alternating fashion" (line 120) but does not specify update frequencies, learning rates, or whether the inner maximization is taken to convergence. Stability of this adversarial training is not discussed. While these details may appear in the (parser-stripped) appendix, the main text should at least summarize the procedure.

3. **Ablation study limited to one environment.** The ablation in Table 3 is conducted only on Cheetah with Multiple Videos distraction. The claim that the regularization term is "broadly helpful" would be strengthened by ablating on at least one additional environment/distraction combination (e.g., Walker-Walk or the Grid setting).

4. **No discussion of statistical significance.** Several baselines show high variance (e.g., SLAC Hopper Clean at 28.4 ± 11.1, Iso-Dream Cheetah Grid at 16.0 ± 31.9). The paper reports standard errors but does not perform significance tests or discuss whether differences between methods are reliable.

5. **One claim is slightly overstated.** The paper states "CLEAR is the only latent dynamics method that can consistently remove superfluous information and maintain a level of invariance" (line 167). On Hopper-Hop, CLEAR does not achieve full distraction-robustness (the paper acknowledges this on line 177), so "consistently" is too sweeping given this exception. Qualifying the claim would be more accurate.

6. **No limitations paragraph.** The paper does not discuss limitations of the compositional decoder (e.g., the assumption that state and exogenous factors are spatially separable via a pixel-wise mask; failure cases when distractions overlap with the agent or move in sync with it), nor cases where the ExoPOMDP assumptions might be violated.

### Trivial

- The qualitative results (Figure 4) are compelling but not quantified across seeds — reporting the fraction of seeds that achieve the desired disentanglement pattern would strengthen the presentation.

## Nice-to-Haves

- **Additional distraction types.** The paper tests static backgrounds, video overlays, and a grid of agents. Testing other exogenous variations (e.g., camera shake, lighting changes, occlusions) would broaden the empirical scope, though the current set is already reasonable within the paper's stated scope.
- **Statistical significance testing.** A simple test (e.g., overlapping confidence intervals or paired bootstrap) would help readers assess whether reported improvements are reliable given the observed variance.
- **Limitations discussion.** A short paragraph discussing when the compositional decoder's spatial-separability assumption might fail and potential failure modes of the adversarial training would strengthen the paper.

## Removed Points

These points are flagged to be removed; treat them with caution.
- **Criticism about baselines not being re-tuned / hyperparameter disclosure.** The paper explicitly states that hyperparameter details are in Appendices G and H (line 231). Since the parser strips appendices, this criticism reflects missing appendix content, not an author error.
- **Claim that the lower bound "may not actually be a valid bound."** The paper's lower bound follows standard variational bounding techniques (ELBO of an SSM + VAE) that are well-established in the cited literature (Hwang et al., 2023; Hafner et al., 2020). While the derivation steps are not shown, there is no evidence the bound is invalid — this is an overly strong characterization of a presentation gap.
- **Criticism that the paper should test on more environment types (camera shake, lighting, occlusions).** These are outside the paper's stated scope; the paper constructs its own challenging distractions (video, grid) because existing benchmarks lack dynamic distractions. Demanding additional distraction types amounts to scope creep beyond what would strengthen the paper's core contribution.
- **Complaint about the compositional decoder not being "forced by the ExoPOMDP assumptions."** The paper explicitly states at line 134: "assuming the state variables and exogenous variables occupy different parts of the visual observation, we employ a compositional decoder." This is transparently a practical design choice, not a claim of theoretical necessity. The reviewer's framing as a weakness is unwarranted.

## Novel Insights

The most instructive finding from this review is that **the cleanest evidence for the paper's core claim comes not from the offline RL scores alone but from the combination of the ground-truth regression (Table 2) with the qualitative analysis (Figures 4–5).** Table 2 shows that SLAC's state representations degrade in MSE as distractions increase, while CLEAR's stay low — but the paper also notes that low MSE does *not* guarantee good RL performance (e.g., SLAC on Cheetah Grid has low MSE but poor RL score). This asymmetry, combined with the ablation showing that *without* regularization the representations can flip or degenerate even though reconstruction quality remains high (Figure 5), makes a compelling case that the inverse-dynamics regularization is doing qualitatively different work from simply improving reconstruction. The failure mode of "flipped" representations (state encoder captures the video background, exogenous encoder captures the agent) is particularly instructive — it shows that the information-theoretic objective J_ELBO alone is insufficient to break symmetry, and that controllability (action predictability) is the right inductive bias to resolve this ambiguity.

## Suggestions

1. Provide the full derivation from Equation 3 to Equation 5 in a short appendix (or clarify which steps follow standard results from Hwang et al., 2023). In particular, explain the transition from I(Ê_t; O_t|Ŝ_t) - I(Ê_t; O_t) to the KL term involving ê_{t-1} — either correct the conditioning or clarify that the encoder is actually p_θ(ê_t|o_t, ê_{t-1}).
2. Add a brief note on the min-max optimization procedure: update frequency for ψ vs. θ, learning rates, and any early-stopping or gradient-clipping used for stability.
3. Add a limitations paragraph discussing the spatial-separability assumption of the compositional decoder and potential failure cases.
4. Soften the claim on line 167 from "the only latent dynamics method that can consistently" to "the only latent dynamics method that can broadly" or add the caveat that full consistency was not achieved on Hopper.
5. Run ablations on at least one additional environment (e.g., Walker-Walk) to strengthen the claim about the regularization term's general utility.

## Score and Decision

This paper makes a clear contribution: it identifies a genuine problem (superfluous information in latent dynamics models under distractions), provides a clean theoretical diagnosis, and proposes a method that demonstrably outperforms existing approaches, especially on the hardest distraction settings. The weaknesses are all addressable: the derivation can be completed, the ablation can be extended, and a limitations paragraph can be added. No weakness threatens the core findings. I recommend acceptance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>