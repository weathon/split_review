Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper proposes SHIFT, a diffusion-based adversarial state perturbation attack for RL that goes beyond traditional \(l_p\)-norm constraints. The attack uses a history-conditioned diffusion model with classifier-free guidance for temporal consistency, combined with classifier guidance from the victim's policy to enforce target actions and an autoencoder-based realism enhancer. Evaluations across four Atari games and five defense methods (including the strongest diffusion-based defenses DP-DQN and Diffusion History) show that SHIFT reduces cumulative reward by over 50% and achieves high manipulation/deviation rates, whereas existing \(l_p\)-constrained attacks fail against these defenses.

## Strengths

- **Novel formulation of semantics-changing unrestricted attacks for RL.** SHIFT is the first RL attack to systematically generate perturbed states that (a) alter semantic content (e.g., changing the pong ball's position) while (b) remaining on the data manifold of realistic states and (c) respecting temporal consistency. This breaks the longstanding reliance on \(l_p\)-norm constraints as a proxy for stealthiness. The formal definitions of valid, realistic, and history-aligned states (Definitions 1–5) provide a useful conceptual framework for future work on semantics-aware attacks.

- **Strong empirical evidence that SHIFT defeats state-of-the-art defenses.** Table 1 shows across Pong, Freeway, Boxing, and Breakout that SHIFT consistently drives rewards down against all five defenses (SA-DQN, WocaR-DQN, CAR-DQN, Diffusion History, DP-DQN). Figure 3a demonstrates that PGD, MinBest, PA-AD, temporally-correlated PGD, and high-sensitivity direction attacks all fail against DP-DQN (defense maintains high reward), while SHIFT succeeds (reward drops to near zero). This supports the core claim that \(l_p\)-constrained attacks cannot alter semantic content sufficiently to fool diffusion-based defenses.

- **Theoretical and practical combination of classifier-free and classifier guidance.** Theorem 1 shows that the two guidance mechanisms (history alignment via classifier-free, action manipulation via classifier) are additive in the reverse diffusion process, enabling simultaneous satisfaction of all three attack objectives. The use of EDM (5 reverse steps, ~0.2s per frame) makes the attack feasible for real-time scenarios, and the DDPM vs. EDM ablation (Table 2) shows the efficiency-performance trade-off is favorable.

- **Probing-based defense analysis provides a constructive countermeasure.** Figure 3b evaluates a practical probing defense (occasionally revealing true states) and shows that more frequent probing monotonically improves reward and reduces manipulation rates. This is a useful starting point for future work on defenses against semantics-aware attacks.

## Weaknesses

### Fatal

None.

### Major

- **The paper claims SHIFT "avoids detection" and is "stealthy" but never evaluates this claim against any actual detection mechanism.** The abstract claims the attack generates states that are "realistic and history-aligned to avoid detection," the introduction claims detection avoidance "by both humans and AI," and the conclusion reiterates "stealthy attacks." However, the experiments never run a single detector (trained anomaly detector, human study, or even a simple threshold-based classifier on clean vs. perturbed states). The reconstruction error and Wasserstein distance reported in Figure 3a are *proxy metrics* — they measure distance to the true state and temporal smoothness, which are reasonable starting points but do not constitute a test of detectability. For example, a state with low reconstruction error could still be easily flagged by a temporal inconsistency detector if the ball teleports by even one pixel. The paper's central claim that SHIFT "avoids detection" is unsubstantiated in its current form. **This is the most consequential weakness because it directly concerns a headline property of the method.**

### Minor

- **No comparison against other unrestricted attacks.** The paper compares SHIFT only against \(l_p\)-constrained attacks (PGD, MinBest, PA-AD, etc.). Showing that an unrestricted attack outperforms restricted ones is natural for the paper's narrative, but without comparing against other forms of unrestricted attacks (e.g., an unconditional diffusion model with policy guidance but no history conditioning, or a GAN-based unrestricted attack), it is unclear which components of SHIFT drive the improvement. The paper shows one qualitative example of an unconditional model producing unrealistic states (Figure 1d), but a quantitative comparison is needed. This limits the ability to isolate the contributions of history conditioning, autoencoder realism, and policy guidance.

- **Clean (unattacked) reward baselines for each defense are not reported.** Table 1 shows the reward of each defense under SHIFT, but without the corresponding clean reward (no attack), it is impossible to separate performance loss caused by the attack from the inherent cost of the defense itself (regularization-based defenses like SA-DQN and WocaR-DQN often reduce clean reward). Reporting manipulation/deviation rates partially addresses this, but clean reward baselines are standard practice in this literature and would significantly strengthen the evaluation.

- **The mechanism by which SHIFT defeats diffusion-based defenses (DP-DQN, Diffusion History) is not analyzed.** The paper briefly notes that "the agent only has access to the perturbed history" (line 204) and that SHIFT states are history-aligned, implying the denoiser may reconstruct them faithfully rather than detecting them as perturbed. However, no empirical analysis is provided — e.g., comparing the denoiser's output on SHIFT states vs. clean states, or measuring whether the denoised state still leads to bad actions. Such an analysis would clarify whether the attack defeats the defense by evading detection entirely, by exploiting the pessimism mechanism, or by some other means.

- **Threat model is strong and its practical plausibility is under-discussed.** The paper acknowledges it considers "the worst-case scenario where the attacker has access to a clean environment" (line 36–38), which is a standard practice. However, SHIFT additionally requires collecting trajectory data from the clean environment to train a diffusion model and an autoencoder. The paper does not discuss when such unrestricted access to the environment is realistic (e.g., could an attacker pre-train on a simulator before deploying on a real system?) or how the attack's effectiveness degrades with limited data. This does not invalidate the contribution — worst-case analysis is valuable — but greater discussion of scope would improve the paper.

- **The theoretical claim in Theorem 1 is less deep than advertised.** The theorem states that the reverse process combining classifier-free and classifier guidance takes the additive form \( \mu_i + \sigma_i^2 \nabla \log \pi(\bar{a}_t \mid \tilde{s}_t^i) \). While this formula is practically useful, the claim that the two mechanisms "do not interfere" (line 163) is somewhat tautological — the gradient from classifier guidance is evaluated on a state being generated conditioned on history, so there is indirect influence. The theorem essentially follows from the definition of the two guidance mechanisms rather than proving a non-trivial property. Clarifying this would prevent overclaiming.

### Trivial

- Specific hyperparameter values (\(\zeta_1, \zeta_2\), guidance scale schedule \(\Gamma(i)\), autoencoder architecture details, number of diffusion training steps) are not reported. These are important for reproducibility.

- The paper does not include the limitations about the threat model or the lack of detector evaluation in the Conclusion's limitations paragraph (Section 5), even though these are the most significant limitations.

## Nice-to-Haves

- An ablation of the history length \(k\) (currently fixed at 4) to show sensitivity.
- An experiment varying the amount of training data available to the attacker, to characterize when the threat model is plausible.
- A study of the effect of the myopic target action selection vs. a more sophisticated selection (e.g., targeting actions with lowest Q-values).

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism that the paper "conflates semantics with realism" and that prior attacks "can certainly change game states."** The paper provides Definition 3 (semantics-changing via projection onto valid states) and shows qualitative evidence (Figure 1c) that PGD at \(l_\infty=15/255\) leaves object positions unchanged. The critic's claim is a subjective interpretation disagreement with the paper's own definition, not a factual error. *Reason: removed as a strawman / subjective disagreement.*

- **Criticism that the paper "never acknowledges" its stronger threat model.** The paper explicitly says "We consider the worst-case scenario where the attacker has access to a clean environment" (line 36–38). It is clearly acknowledged. *Reason: factually incorrect — the paper does discuss this.*

- **Criticism that the comparison with \(l_p\)-constrained attacks is "fundamentally unfair" and makes the conclusion "hollow."** Comparing against existing attacks within their own paradigm is the standard way to demonstrate a paradigm shift. The paper's narrative requires showing that \(l_p\)-constrained attacks fail and an unrestricted attack succeeds. The lack of unrestricted baselines is a real limitation (listed under Minor), but the claim that the comparison is "fundamentally unfair" overstates the issue. *Reason: overclaimed; the real concern (missing unrestricted baselines) is already captured as a Minor weakness.*

- **Criticism that the paper conflates semantics with "unrealistic states" in the introduction.** The paper's Definition 3 is precise. The critic's reading is a matter of interpretation. *Reason: subjective reading.*

- **Criticism about the paper not computing Proj\(_{S^*}\) directly.** The paper acknowledges that \(l_2\) distance to the true state is "an upper bound on the realism measure" (around line 148). Using a computationally feasible proxy is standard practice. *Reason: the paper acknowledges this limitation itself.*

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Run a detector evaluation.** Train a simple binary classifier (or use the autoencoder's reconstruction error as an anomaly detector) on clean vs. SHIFT-perturbed states and report detection AUC / precision-recall. This would directly substantiate (or refute) the stealthiness claim.
2. **Add clean reward baselines** for each defense method in Table 1. Without these, readers cannot decompose attack-induced loss from defense-inherent regularization loss.
3. **Add at least one unrestricted attack baseline.** The simplest would be: train an unconditional diffusion model (or use a pre-trained generative model), apply policy guidance without history conditioning or autoencoder guidance, and evaluate quantitatively. This would isolate the contribution of history alignment.
4. **Analyze the DP-DQN denoiser output.** Show a comparison of the denoiser's reconstructions on clean states, PGD-perturbed states, and SHIFT-perturbed states (both visually and quantitatively via action agreement). This would clarify the mechanism by which SHIFT defeats the defense.
5. **Report the specific hyperparameter values** \(\zeta_1, \zeta_2\), \(\Gamma(i)\) schedule, and autoencoder architecture in the main text or appendix.

## Score and Decision

The paper presents a genuinely novel attack methodology and supports its core empirical claim (that SHIFT breaks current defenses) with clear evidence across multiple environments and defenses. However, the headline claim of stealthiness remains unvalidated, and the evaluation would benefit from additional baselines and ablations. These weaknesses are addressable and do not undermine the core contribution.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>