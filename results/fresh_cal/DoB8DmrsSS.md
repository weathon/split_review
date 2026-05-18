Now I have all the information I need. Let me carefully construct the final review.

---

## Summary

This paper proposes SHIFT, a diffusion-based adversarial attack on RL agents that moves beyond traditional $l_p$-norm constraints. The method trains a history-conditioned diffusion model with classifier-free guidance, then augments it with policy (classifier) guidance to steer the victim's actions and autoencoder guidance to maintain realism. Empirical evaluation across four Atari environments shows SHIFT reduces cumulative reward by over 50% against five defenses (including diffusion-based defenses DP-DQN and Diffusion History that prior attacks could not break), while maintaining low reconstruction error and Wasserstein distance.

## Strengths

**1. Genuinely novel attack paradigm for RL security.** SHIFT is the first attack to replace $l_p$-norm constraints with a diffusion-based generative model that can alter object positions and other semantic content (Figure 1). This moves beyond an entrenched limitation of prior work and opens a new direction for both attack and defense research.

**2. Strong empirical evidence of breaking previously robust defenses.** Table 1 shows SHIFT reduces reward across all tested defenses (SA-DQN, WocaR-DQN, CAR-DQN, Diffusion History, DP-DQN), including diffusion-based defenses that were immune to PGD, MinBest, PA-AD, and high-sensitivity attacks (Figure 3a). This is the paper's most compelling empirical result.

**3. Formal framework for semantics-aware attacks.** Definitions 1–5 (valid, realistic, semantics-changing, history-aligned, approximately history-aligned states) provide a principled vocabulary for describing attacks that target semantic content rather than pixel-level perturbations. This is a conceptual advance over the ad-hoc $l_p$ ball formulation.

**4. Simultaneous attack effectiveness and stealthiness.** Figure 3a shows SHIFT achieves lower reconstruction error and Wasserstein-1 distance than all baselines while simultaneously being far more effective at reward reduction. This combination is what makes the attack genuinely threatening.

**5. Theoretical justification for combining two guidance mechanisms.** Theorem 1 proves that classifier-free guidance (history conditioning) and classifier guidance (policy gradient) can be combined without interference because the two conditioning variables are independent. This is non-trivial and enables the core method.

**6. Practical speed optimization via EDM.** Table 2 shows EDM reduces sampling time to ≈0.2s per perturbed state versus DDPM's prohibitive cost, making the attack potentially feasible in deployment scenarios.

## Weaknesses

### Fatal
None.

### Major

**1. Missing ablation isolates the source of attack success.** The paper compares SHIFT (unconstrained, diffusion + policy guidance + autoencoder guidance) against $l_p$-constrained baselines (PGD, MinBest, PA-AD, etc.). This conflates two effects: removing the $l_p$ constraint and adding semantic/policy guidance. Without an ablation that runs the *same diffusion backbone without policy guidance* (or with the policy guidance replaced by an $l_p$ projection), we cannot tell whether the attack's success comes from (a) simply having an unconstrained generative model, or (b) the specific semantic steering. The paper does show in Figure 2 that the conditional diffusion model (without policy guidance) generates states close to true states, but this doesn't quantify attack effectiveness. A simple control: run the history-conditioned diffusion model to generate perturbed states *without* policy guidance and measure the resulting reward. This would directly show the marginal benefit of the policy guidance component.

**2. Gap between conceptual framework and operational measurement.** Definitions 3–5 rely on the projection operator $\mathrm{Proj}_{S^*}$ and the reachable set $S(H_{t-1})$, but these are never computed or approximated in the experiments. The paper acknowledges this (line 142: "our attack uses the true history $\tau_{t-1}$ to approximate the victim's belief $H_{t-1}$, as the latter requires projecting each perturbed state onto $S^*$ and is computationally expensive"), but this means the theoretical definitions are decoupled from the empirical evaluation. The actual claims about "semantics change" are supported only by anecdotal visual evidence (Figure 1) and proxy metrics (reconstruction error, Wasserstein distance). The paper would be substantially strengthened by at least showing that a discriminator cannot distinguish SHIFT-generated states from true states, or by any direct (even small-scale) validation that the definitions' properties are met.

### Minor

**3. The "real-time" claim is overstated.** Atari environments typically run at 60 fps (~16 ms per frame). The paper reports 0.2 s per perturbed state (~200 ms), which is an order of magnitude slower than the frame rate. While the paper acknowledges the latency, describing 0.2 s as "feasible for real-time applications" (line 214) is misleading — it is feasible for offline or pre-computed attacks, but not for frame-synchronous online perturbation. The core contribution does not depend on real-time performance, so this should be caveated more honestly.

**4. The introduction claims SHIFT "breaks all known defenses" but evaluates only five specific defenses.** This overclaim is common in the ML security literature but should be tightened (e.g., "breaks all defenses considered" or "breaks existing state-of-the-art defenses"). The paper does reasonably scope its evaluation to leading defenses, so this is a phrasing issue rather than an empirical gap.

**5. The target action selection ("Random Non-Optimal") is acknowledged as myopic but the potential gain of non-myopic selection is never quantified.** The conclusion notes this limitation (line 227), but a simple analysis of an oracle upper bound or a lookahead-based target selection on one environment would clarify how much headroom exists.

**6. The probing defense experiment (Figure 3b) is presented as a key finding but remains under-analyzed.** The paper does not discuss how the victim would use probed true states (e.g., Kalman filter, diffusion inpainting, or simple replacement), and does not discuss the cost/benefit trade-off of probing. This section reads as a preliminary observation rather than a rigorous defense analysis. It could be expanded or de-emphasized.

### Trivial
None.

## Nice-to-Haves
- An ablation that replaces policy guidance with a simple unconstrained baseline (e.g., random unstructured noise without norm limit) to separate the effect of "no constraint" from the effect of "semantic structure."
- Reporting training cost (GPU hours, epochs) for the diffusion model and autoencoder.
- A small-scale human evaluation of realism (e.g., "which of these two frames is perturbed?") for a sample of ~100 images per method would substantially strengthen the semantics claims.

## Removed Points

These points were raised by one or both reviewers but are removed or demoted for the reasons given below. Treat them with caution.

- *"White-box assumption limits practical threat"* — The paper explicitly adopts the standard worst-case threat model used throughout the RL security literature. This is not a weakness; it is a stated assumption that the reader can evaluate.
- *"Reference policy π_ref not specified"* — The paper does specify it (line 136: "a well-trained policy π_ref (independent of the agent's policy) with exploration to ensure coverage"). The critic misread this section.
- *"10 runs is too few"* — 10 runs is standard for Atari benchmarks in this subfield. Not a meaningful weakness.
- *"No evaluation on continuous-control environments"* — The paper explicitly focuses on vision-based discrete-action environments (Atari), which is a standard benchmark for RL security. Expanding to MuJoCo would be out of scope for this paper's contribution.
- *"Statistical significance tests missing"* — Not standard practice for this type of RL attack evaluation.
- *"PGD TC budget inconsistency"* — Minor experimental detail that could be clarified; does not affect the paper's main claims.
- *"Computational cost of training not reported"* — Nice-to-have but not a weakness.
- *"Should compare against a baseline that removes l_p constraint but doesn't use diffusion"* — This is addressed in the Nice-to-Haves above; it is not a standard baseline and would not isolate the semantic guidance effect, which is the paper's claimed contribution.
- Strength Finder's generic strength about "addressing an important problem" — Removed because it is generic and not specific to this paper.

## Novel Insights

The harsh critic correctly identifies the central tension: the paper compares its unconstrained attack against constrained baselines, making it impossible to attribute success to the semantic guidance versus simply having more degrees of freedom. However, the strength finder rightly highlights that Figure 3a shows SHIFT simultaneously has *lower* detectability metrics (reconstruction error, Wasserstein distance) than all baselines *and* higher attack success — this cross-metric dominance cannot be explained by "more freedom" alone, because an unconstrained random-noise baseline would have high detectability. The reviews collectively suggest that the paper's strongest evidence is in this cross-metric comparison (Figure 3a) and the direct visual demonstration (Figure 1), while its weakest link is the missing ablation isolating policy guidance. The combined picture is of a solid but incomplete empirical package: the core idea is clearly valuable, but a single well-chosen ablation would substantially raise confidence.

## Suggestions

1. **Add the critical ablation:** Run SHIFT with the same diffusion backbone but without policy guidance (and without autoencoder guidance) as an attack baseline. Report the resulting reward and manipulation rate. This directly answers whether semantic steering or just unconstrained generation drives success.

2. **Operationalize one of the definitions.** Train a binary discriminator on clean vs. perturbed states (or a small human evaluation — even 100 examples per condition is enough) to directly measure whether the generated states are "realistic" and "semantically different." This would close the gap between the formal framework and the evaluation.

3. **Soft-pedal "real-time."** Replace "feasible for real-time applications" with a more precise statement about pre-computation strategies or the specific conditions under which 0.2 s latency is acceptable.

4. **Caveat "all known defenses."** Replace with "state-of-the-art defenses considered in our evaluation" to match what the paper actually demonstrates.

## Score and Decision

The paper proposes a genuinely novel attack paradigm with a strong formal grounding and convincing (though incomplete) empirical results. The missing ablation is a real gap but is addressable. The weaknesses are not fatal; they point to a need for additional experiments rather than a flaw in the core idea. The contribution — demonstrating that diffusion models can generate semantic-level adversarial perturbations that break previously robust defenses — is significant and timely.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>