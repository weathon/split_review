Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes Diffusion Implicit Policy (DIP), a framework for scene-aware motion synthesis that disentangles motion prior learning (via a diffusion model trained on unpaired AMASS data) from scene interaction optimization (via differentiable reward functions applied at inference time). The core technical contribution is an implicit policy that adjusts the diffusion sampling distribution's centroid in a "GAN Inversion manner" — backpropagating interaction-based rewards through the diffusion model's predicted clean motion rather than directly modifying the noised latent. The method also incorporates ControlNet-based keyframe control, motion inpainting for historical consistency, and rotation power-space blending for multi-task transitions. Experiments on ShapeNet-cluttered scenes, PROX, and Replica show competitive or superior results compared to methods requiring paired motion-scene training data.

## Strengths

- **Training-data barrier removal.** The paper's central claim — that scene-aware motion synthesis can be achieved without paired motion-scene training data — is clearly delineated and supported. The motion diffusion model is trained solely on unpaired AMASS motion data; scene interaction is handled entirely at inference via reward-based optimization (Sec. 3.4–3.5). This is a genuine departure from prior work (SceneDiffuser, DIMOS, SAMP) that requires paired data, and it opens the door to leveraging abundant unpaired motion capture data.

- **Strong empirical results across diverse scene types.** On navigation tasks (Table 1), DIP achieves the lowest finish time (3.35s), closest goal distance (0.03m), and lowest penetration (0.95 vs. 2.62 for DIMOS). On interaction tasks (Table 2), it shows lower mean penetration for sitting (0.81±0.43) and lying (1.15±0.68) than DIMOS. In the user study across PROX and Replica (Table 3), DIP obtains the highest ratings in diversity (3.82/5), interaction plausibility (3.81/5), and overall performance (3.90/5), all without using any paired motion-scene training data. These results convincingly demonstrate the viability of the unpaired approach.

- **Novel technical components with clear motivation.** Two specific design choices are well-motivated and supported: (a) optimizing the sampling centroid through the predicted clean motion x̂₀^φ (rather than directly modifying μ_t), with the justification that direct modification harms motion continuity (Sec. 3.5); and (b) time-variant motion blending in rotation power space rather than linear pose-space interpolation, which enables stable multi-task transitions (Sec. 3.6). These are non-trivial engineering contributions that likely generalize beyond this specific setting.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Ambiguous gradient notation in the implicit policy update (Eq. 10).** The update is written as:  
  `̃μ_t = μ_t + β̃_t · ∇ℛ_ip(𝒮, x̂_0^φ(μ_t, t-1, c))`  
  The notation `∇ℛ_ip(𝒮, x̂_0^φ(...))` is ambiguous: it could mean the gradient of ℛ_ip w.r.t. its second argument (∂ℛ_ip/∂x̂_0) or the gradient w.r.t. μ_t computed through the composition ℛ_ip∘φ. The paper invokes the GAN Inversion analogy ("given Generator x=G(z), adjust latent code z via loss ℒ(x)"), which in standard GAN inversion *does* backpropagate through the generator, suggesting the intended reading is the full gradient w.r.t. μ_t via autograd through φ. However, the paper does not explicitly state that it backpropagates through φ or show the chain-rule expansion. This is a clarity issue, not a methodological error — the "fully differentiable" design (Sec. 3.5, line 169) and the GAN inversion framing both point to the correct autograd-based implementation. Still, the paper should disambiguate the notation (e.g., `∇_{μ_t}` or an explicit chain-rule expression) so that readers can verify correctness without guessing.

- **Claim of generality for "more general tasks and versatile scenes" is asserted rather than demonstrated.** The abstract claims the method shows "feasibility of utilizing the DIP for motion synthesis in more general tasks and versatile scenes," but the evaluation covers only three task types (locomotion, sitting, lying) and furniture-based indoor scenes. While the evaluation across ShapeNet, PROX, and Replica does demonstrate generalization across *scene types*, the claim about *task* generality is unsupported. The reward functions (contact, penetration, smoothness, goal achievement) encode domain knowledge about rigid indoor human-scene interaction and would likely need redesign for outdoor scenes, non-rigid interactions, or tasks like carrying objects. The paper should either scope this claim down or add caveats about the reward functions' current scope.

- **Foot contact metric mismatch is acknowledged but not quantified.** The locomotion results (Table 1) show an inferior foot contact score. The paper explains this by stating "our method focuses more on foot vertex contact, whereas the contact score calculation is based on foot joints" (Sec. 4.2). This is a plausible explanation, but no vertex-based contact metric is reported to verify it. Without this verification, the reader cannot distinguish between a genuine weakness and a metric mismatch. Reporting a vertex-based foot contact score (or a per-vertex ground-contact distance) would resolve the ambiguity and would be straightforward to compute given the SMPL-X mesh.

### Trivial

- **User study methodology is underspecified.** The paper reports that 1,200 ratings from 15 participants were collected for each method (Sec. 4.4), but does not describe whether participants were blind to method identity, whether the order of presented motions was randomized, or whether the same initial state was shown across methods. These are standard reporting practices for user studies and should be included for reproducibility. Given the magnitude of the observed differences (e.g., DIP 3.90/5 vs. DIMOS 3.44/5 overall), this does not undermine the conclusions, but it should be documented.

## Nice-to-Haves

- An ablation in the **main paper** (not just supplementary) comparing three variants: (i) the proposed implicit policy optimization, (ii) direct μ_t adjustment without going through x̂_0^φ, and (iii) the method without any test-time reward optimization. This would help isolate the contribution of each component and is the current paper's most noticeable missing experiment from the main text.

- A concise mathematical definition of at least the two most important reward terms (contact ℛ_cont and non-penetration ℛ_pene) in the main paper, rather than deferring all six to supplementary. This would make the method more self-contained without bloating the paper.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The implicit policy gradient update may be incorrect / omits the Jacobian of φ."** — The reviewer assumed ∇ℛ_ip(𝒮, x̂_0^φ(...)) means gradient w.r.t. x̂_0 only, ignoring the Jacobian through φ. However, the paper's GAN Inversion analogy and explicit statement that "the reward functions are fully differentiable" (Sec. 3.5) strongly imply the intended implementation uses autograd to compute the full gradient w.r.t. μ_t through φ (as is standard in GAN inversion and PyTorch/TensorFlow pipelines). The notation is ambiguous but not incorrect. This concern is addressed by the Minor weakness above (presentation clarity), not a structural flaw. Had the paper actually omitted the Jacobian in implementation, this would be fatal; but there is no evidence of that.

- **"The novelty rests almost entirely on the implicit policy integration, which has a methodological gap."** — This follows from the above point and is removed for the same reason.

- **"Missing ablations in the main paper"** and **"Reward function details not in the main paper."** — The paper explicitly references supplementary for ablations (Sec. 4, last paragraph) and reward formulations (Sec. 3.4). This is standard practice in graphics/CV conferences with page limits. Moved to Nice-to-Haves.

## Novel Insights

The most interesting observation from the reviews is the tension between the paper's framing and its actual contribution: the paper presents the implicit policy as an "optimization" (complete with argmax formulation in Eq. 8–9), but in practice it is closer to guided sampling — a one-step gradient adjustment of the distribution centroid at each denoising step, without any iterative inner-loop optimization. This is actually a strength (it keeps inference efficient), but the "optimization" framing sets up expectations of convergence guarantees and rigorous derivation that the paper then does not meet. Reframing the method as "reward-guided diffusion sampling" rather than "joint optimization" would better align the presentation with what the method actually does and avoid the notational ambiguity that triggered the reviewer's concern.

## Suggestions

1. **Clarify the gradient computation in Eq. 10.** Add a subscript or explicit text: e.g., `̃μ_t = μ_t + β̃_t · ∇_{μ_t} ℛ_ip(𝒮, φ(μ_t, t-1, c))`, and note that this is computed via automatic differentiation through φ. This immediately resolves the ambiguity that was the reviewer's main concern.

2. **Add a vertex-based foot contact metric** to Table 1 or as a supplementary table to support the claim about foot vertex contact vs. joint-based scoring.

3. **Qualify the generality claim** in the abstract/conclusion: state that the method generalizes across scene types (ShapeNet, PROX, Replica) while noting that task generality depends on the reward function design.

4. **Add a single ablation in the main paper** showing DIP vs. DIP w/o implicit policy (keeping only diffusion denoising). A single row in Table 1 would suffice.

## Score and Decision

The paper makes a clear contribution (unpaired scene-aware motion synthesis), achieves strong empirical results across multiple scene types, and introduces technically sound components (GAN-inversion centroid adjustment, power-space blending). The main weakness is a presentation ambiguity in the gradient notation that has been over-interpreted as a methodological flaw but is straightforward to clarify. The remaining issues (scope claims, foot contact metric, user study documentation) are minor. The paper would benefit from clarifications but in its current form already presents a compelling advance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>