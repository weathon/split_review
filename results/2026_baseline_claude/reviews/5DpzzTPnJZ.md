## Summary

This paper studies plasticity loss in deep reinforcement learning through a theoretical lens grounded in network optimization. The authors formally identify two causal mechanisms: (1) rank collapse of the Neural Tangent Kernel (NTK) Gram matrix when the RL non-stationary initialization violates the random-initialization assumption, and (2) a Θ(1/k) gradient magnitude decay arising from the growing replay buffer's dilution of new data. Building on the second mechanism, the paper proposes **Sample Weight Decay (SWD)**, a lightweight experience replay sampling strategy that assigns linearly decaying weights to older samples, thereby restoring gradient magnitude. Experiments span MuJoCo (TD3), ALE (Double DQN), and DMC (SimBa-SAC), showing consistent improvements over baselines.

---

## Strengths

- **Principled theoretical framing of a known empirical phenomenon.** Proposition 1 + Theorem 3 cleanly derive that the initial gradient at round k has a 1/k factor for the distributional-shift term due to the recursive expansion of the replay buffer. This gives a precise, mathematically grounded account of why plasticity degrades — a gap the field has previously addressed only with empirical intuition.

- **Simple, orthogonal algorithm with broad applicability.** SWD is a four-line change to replay buffer sampling (Algorithm 1); it requires no network modification, no architectural change, and is compatible with existing plasticity remedies (validated by the SWD+S&P combination in Figure 8). The bucket-based approximation further removes computational overhead.

- **Comprehensive evaluation protocol.** The paper evaluates on three benchmark suites (MuJoCo, ALE, DMC) with three different base algorithms (TD3, DDQN, SAC/SimBa), multiple UTD ratios, hyperparameter grids, and multiple decay strategies. Statistical rigor is maintained via IQM with stratified bootstrap CIs (Agarwal et al., 2021).

- **Clever reverse-validation design.** The SWA (Sample Weight Augmentation) ablation — the exact inverse of SWD — provides clean controlled evidence: SWA degrades gradient norms, GraMa, and performance simultaneously, directly confirming the theoretical causal story.

- **UTD robustness.** Figure 7 shows SWD is effective (and improves further) at UTD=5, where plasticity loss is most severe, which is exactly the regime where gradient dilution matters most.

---

## Weaknesses

### Fatal
None.

### Major

1. **Theory-to-algorithm gap in SWD's specific functional form.** Theorem 3 establishes a 1/k scaling for the new-data gradient contribution. The natural correction would be an inverse-k reweighting (upweight new samples by factor k). Instead, SWD uses a linear age-decay $w_i = \max(w_{\min}, 1 - \mathrm{age}_i/T)$, which is a different functional form. The paper empirically confirms linear decay outperforms exponential/polynomial (Table 13), but does not theoretically justify why linear decay is the right antidote to 1/k attenuation. This leaves the theory-to-algorithm mapping imprecise.

2. **The NTK section (4.1) contributes no new theorem.** It recaps prior work (Du et al., 2019; Allen-Zhu et al., 2019) and observes that RL violates random-initialization conditions. No new formal result about NTK rank behavior in RL is derived. The section functions as conceptual motivation but does not deliver on the claim of a "unified theory" for NTK degeneration in RL.

3. **Narrow comparison with other plasticity methods.** Figure 8 benchmarks SWD against ReGraMa, S&P, and Plasticity Injection only on Humanoid Run with SimBa-SAC. MuJoCo (TD3) and ALE (DDQN) experiments (Figures 2–3) compare exclusively against vanilla baselines. It is unknown whether SWD outperforms or complements other methods in those settings.

4. **Potential circularity in plasticity measurement.** GraMa (the adopted plasticity metric) is a gradient-magnitude-based metric. SWD is designed to inflate gradient magnitude via recency weighting. Using GraMa to validate a gradient-magnitude intervention creates a partially circular argument. A second independent plasticity metric (e.g., dead neuron fraction, effective rank, or performance on novel tasks) would strengthen the causal story.

### Minor

1. **The FQI analysis relies on the H+1 boundary elimination.** The cleanest result in Theorem 3 is obtained by setting $\hat{f}_{H+1} \equiv 0$, which eliminates the target-drift term entirely. In practice, TD bootstrapping retains the target-drift term at all other steps; the Θ(1/k) conclusion holds exactly only when target drift is zero. The practical implications for multi-step TD algorithms are not discussed.

2. **Algorithm connectivity to online RL is implicit.** The theory analyzes episodic FQI with a monotonically growing buffer ($|\mathcal{D}_h^k| = k$). Most practical RL implementations use finite FIFO replay buffers, where old data is eventually discarded. In this regime, k effectively stops growing, and the 1/k attenuation argument should plateau. The paper does not address this regime shift.

3. **Figure 8 numbers are hard to compare cross-figure.** The aggregate scores in Figure 8 (~240 IQM) are much lower than Figure 1 (~680 IQM for SAC+SWD), suggesting different normalizations or different task subsets. No clarification is provided in the main text.

### Trivial

- GraMa figure captions (Figure 6) note "a larger GraMa value indicates a *weaker* learning capability," which contradicts the Section 6.3 title "alleviating plasticity loss" as shown by higher GraMa. This sign convention is confusing and should be clarified (GraMa as defined by Liu et al. 2025 apparently measures gradient magnitude, where higher = better plasticity, contradicting the caption).

---

## Nice-to-Haves

- A direct comparison showing SWD performance in the MuJoCo and ALE settings against ReDo/ReGraMa/S&P would significantly strengthen Q4.
- A discussion of how SWD interacts with finite FIFO replay buffers (the most common implementation) would ground the theory better in practice.
- Reporting wall-clock training time overhead of SWD vs. PER more explicitly in the main paper (rather than relegating to Appendix D) would help practitioners.

---

## Novel Insights

The paper's most genuinely novel observation is the precise identification of the Θ(1/k) dilution of new-data gradient contributions as an inherent mathematical consequence of the replay buffer's empirical distribution recursion (Proposition 1 → Theorem 3). While recency-biased replay has been explored heuristically before, formalizing it as a specific gradient-attenuation mechanism in the NTK + FQI framework — and separating this from the NTK rank collapse mechanism — provides a cleaner conceptual decomposition of plasticity loss than previously available. The insight that RL differs from supervised learning not in learning rate or architecture but in the sequential initialization problem (each round starts from the previous round's argmin rather than from random) is a crisp and underappreciated framing.

---

## Suggestions

- Derive or at least bound the effect of SWD on the gradient magnitude analytically: show that with SWD's weighting the 1/k coefficient is replaced by a larger term, and quantify by how much.
- Run the plasticity method comparison (Figure 8) on at least one additional environment (e.g., MuJoCo Humanoid with TD3) to establish whether SWD's superiority is general or specific to SimBa-SAC.
- Add at least one non-gradient-based plasticity metric (effective rank, dead neuron fraction) alongside GraMa to avoid the circularity concern.

---

## Score and Decision

The paper makes a genuine theoretical contribution by formalizing gradient attenuation as a Θ(1/k) mechanism in RL plasticity loss. SWD is simple, principled, and empirically effective across multiple settings. The major weaknesses — the theory-to-algorithm functional form gap, the underdeveloped NTK section, and the narrow cross-method comparison — are real but do not invalidate the core contribution. The experimental evidence is broad and statistically rigorous. This is a solid contribution to an active and important research direction.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>