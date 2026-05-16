Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

SHIFT is a diffusion-based adversarial state perturbation attack for RL that removes the traditional $l_p$-norm constraint. It uses a history-conditioned diffusion model with classifier-free guidance (for history alignment), policy gradient guidance (to alter semantics toward a target action), and autoencoder-based realism guidance (to suppress artifacts). Evaluated across four Atari games against six defenses (SA-DQN, WocaR-DQN, CAR-DQN, Diffusion History, DP-DQN, vanilla DQN), it reduces episode rewards by more than 50% and is the only attack shown to compromise the strongest diffusion-based defenses.

## Strengths

1. **Removes the $l_p$-norm constraint to enable semantic perturbations.** The paper clearly identifies that existing $l_p$-norm-constrained attacks (PGD, MinBest, PA-AD) cannot alter semantic content even at large budgets (Section 1, Figure 1c). SHIFT replaces this constraint with realism and history-alignment objectives, directly enabling semantic changes that fool defenses which easily denoise $l_p$-bounded perturbations.

2. **Breaks state-of-the-art defenses that resist all prior attacks.** Table 1 shows SHIFT reduces episode reward substantially across 4 Atari games against 6 defenses. Figure 3a demonstrates that PGD, MinBest, PA-AD, PGD-TC, Blurred, and Shifting attacks all fail against DP-DQN on Freeway, while SHIFT succeeds — and simultaneously achieves lower reconstruction error and Wasserstein distance than those attacks.

3. **Principled combination of classifier-free guidance (history conditioning), classifier guidance (policy gradient), and autoencoder-based realism enhancement.** Theorem 1 shows that in the RL setting the two guidance mechanisms are additively computable without cross-terms, because the policy gradient depends only on the target action and the classifier-free gradient depends only on the history. The autoencoder guidance (Section 3.2.3) demonstrably removes artifacts such as the "two balls" anomaly (Figure 1d vs. 1e).

4. **Formal characterization of stealthiness.** Definitions 1–5 provide a vocabulary for valid, realistic, semantics-changing, and history-aligned states. This framework is accompanied by quantitative metrics (reconstruction error for static stealthiness, Wasserstein distance for dynamic stealthiness), and Figure 3a shows SHIFT outperforms all compared attacks on both metrics.

## Weaknesses

### Fatal
None.

### Major

1. **Comparative evaluation against prior attacks is shown for only one environment.** The paper's central claim is that SHIFT "uniquely" breaks defenses that prior attacks cannot. However, the head-to-head comparison with PGD, MinBest, PA-AD, PGD-TC, Blurred, and Shifting attacks is presented only for Freeway (Figure 3a). Table 1 reports SHIFT's own performance across four environments (Pong, Freeway, Seaquest, Boxing), but does not show whether prior attacks also fail against the same defenses on those environments. Given that SHIFT is computationally heavier than PGD or MinBest (0.2s vs. 0.02s per perturbation), it is important to verify that cheaper attacks cannot achieve comparable results on multiple games. The paper's strongest claim rests on evidence from a single environment.

### Minor

2. **Theory-practice gap in the formal definitions (Section 3.1).** Definitions 1–5 define valid states ($S^*$), realistic states, and semantics-changing states via projection onto the set of states reachable by any policy in the MDP — a set that is intractable to compute for high-dimensional Atari environments. The paper acknowledges this (Section 3.1: "ensuring strict validity is intractable with limited amount of data") but then uses the true state $s_t$ as a proxy for $\mathrm{Proj}_{S^*}(\tilde{s})$ in experiments (Figure 2). The $l_2$ distance to $s_t$ is a valid upper bound on the realism measure (since $s_t \in S^*$ by construction), and the practical approximation is reasonable. However, the elegant formal framework is not directly operationalized — semantic change is inferred from action manipulation rates rather than verified against the formal definitions. The paper would benefit from either (a) developing a computable proxy for projection onto $S^*$ (e.g., via a trained classifier) and measuring against it, or (b) explicitly framing the definitions as motivation and using pragmatic measures (reconstruction error, Wasserstein distance) as primary evidence.

3. **Missing no-attack baselines in Table 1.** Table 1 reports SHIFT's attack performance across various defenses, but does not show the reward each defense achieves under clean (no-attack) conditions. Without this, it is harder to assess the absolute impact — e.g., if SA-DQN already achieves low reward even without attack, SHIFT's impact is less impressive. The paper should report clean reward for each defense to contextualize the attack results.

4. **Missing ablation studies.** The method has three interacting components: (a) history conditioning (classifier-free guidance), (b) policy gradient (classifier guidance), and (c) autoencoder realism guidance. No ablation isolates the contribution of each component. The most critical missing ablation is removing autoencoder guidance to measure the hit to realism vs. attack success. Similarly, removing policy guidance would test whether the conditioned diffusion model alone can induce semantic change. These ablations are standard practice for a method paper and would strengthen the attribution of SHIFT's success.

5. **Real-time feasibility claim is not fully justified.** The paper reports ~0.2s per perturbed state with EDM (Section 4.1) and claims this is "feasible for real-time applications." Standard Atari RL settings use frame skipping (typically 4 frames), giving ~67ms between agent actions. At 0.2s per perturbation, SHIFT is ~3× slower than the action interval, which is not real-time in the strict sense. The paper should either provide a more nuanced discussion of the computational trade-off (e.g., attacking at a lower frequency, or parallelized generation) or moderate the real-time claim.

### Trivial

6. **The paper uses true history (rather than perturbed history) for conditioning** during generation, which is acknowledged as an approximation (Section 3.2.1). The effect of divergence between true and perturbed history over the course of an episode is not studied.

7. **Target action selection uses a myopic Random Non-Optimal method**, which the paper notes as a limitation (Section 5), but alternative selection strategies are not explored.

## Nice-to-Haves

- **Human evaluation or detector study** to confirm that perturbed states are visually plausible to human observers or can evade an independent anomaly detector (beyond the autoencoder used by the attack itself).
- **Extension of comparative evaluation** to at least 2 additional environments (e.g., Pong and Seaquest) against DP-DQN, comparing SHIFT to PGD (at multiple budgets) and one additional prior attack.
- **Sensitivity analysis** on history length $k$ and autoencoder gradient steps.

## Removed Points

These points from the reviewer inputs are flagged to be removed; treat them with caution.

1. **Criticism that the $l_2$ distance does not give a valid upper bound on the realism measure (Critical Issue 1).** The reviewer claimed that "this is only true if the true state is the closest point in $S^*$ to the perturbed state." This is incorrect. Since the true state $s_t$ is itself an element of $S^*$ (it is a state actually reached by the MDP), the distance from $\tilde{s}$ to $s_t$ is always an upper bound on the distance to the nearest point in $S^*$ — i.e., $\|\mathrm{Proj}_{S^*}(\tilde{s}) - \tilde{s}\|_2 \leq \|s_t - \tilde{s}\|_2$. The paper's claim is mathematically correct.

2. **Criticism that Theorem 1's "no interference" claim is invalidated by the autoencoder guidance (Critical Issue 2).** The reviewer argued that the autoencoder guidance "implicitly admits interference." This misunderstands the theorem. The "no interference" claim is about the two gradient terms (classifier-free and classifier guidance) being additively computable without cross-terms because they depend on different conditioning variables. The autoencoder guidance is a separate, additional mechanism addressing realism degradation from strong policy guidance — not evidence of interference between the two guidance methods. The theorem is technically sound.

3. **Criticism about Figure 3a axes not being clearly labeled.** This is a parser artifact and/or presentation nitpick; the paper text explains the axes.

4. **Criticism that the paper does not cite prior unrestricted attack work in RL.** The paper cites Song et al. (2018) for the connection to unrestricted adversarial examples in supervised learning. Asking for extensive related work on unrestricted attacks in RL is scope creep; no such well-known prior work is established in the RL attack literature.

5. **Various formatting/style nitpicks** (typos, figure clarity, etc.) — these are parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the expected tension between the paper's formal theoretical apparatus (which is elegant but not fully operationalized) and its empirical evidence (which is strong but concentrated in a single comparative environment). The most useful takeaway is that the paper's central claim — that SHIFT uniquely breaks defenses other attacks cannot — would benefit from broader comparative evidence across more environments, and the method's contributions would be better understood with component ablations.

## Suggestions

1. **Extend the comparative evaluation:** Run PGD (at multiple $\epsilon$ budgets), MinBest, and one additional prior attack against DP-DQN on at least two more environments (e.g., Pong and Seaquest) and report results alongside SHIFT. This is the single most important addition to support the paper's core claim.

2. **Add no-attack baselines to Table 1** showing the clean reward of each defense method.

3. **Run a 3-way ablation** comparing (i) full SHIFT, (ii) SHIFT without autoencoder guidance, and (iii) SHIFT without policy guidance, reporting reward, manipulation rate, reconstruction error, and Wasserstein distance.

4. **Clarify or moderate the "real-time" claim.** Either provide evidence that 0.2s per state is sufficient for the specific deployment scenario (e.g., attacking at lower frequency), or acknowledge that the attack currently operates at a sub-real-time rate.

5. **Reconsider whether the formal definitions (Definitions 1–5) need to be retained as a full theoretical framework** or can be presented as motivational scaffolding with practical measurements serving as the primary evidence.

## Score and Decision

The paper presents a novel, well-motivated attack method that goes beyond existing $l_p$-norm-constrained approaches and demonstrates strong empirical results against state-of-the-art defenses. The core weakness is that the comparative evidence for the central claim (SHIFT uniquely breaks defenses) is concentrated on a single environment. The missing ablations and no-attack baselines are addressable. The formal theory-practice gap is acknowledged and the paper's practical approximations are reasonable. Overall, the contribution is significant and the method is sound, but the empirical scope of the comparative evaluation needs broadening. The paper merits acceptance after moderate revisions.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>