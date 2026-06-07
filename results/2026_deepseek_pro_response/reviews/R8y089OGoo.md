Now I have a clear picture. Let me summarize my calibration:

**Round 1 bracket: 6.0–7.5**

**Round 2 anchors read in full:**
- **DAC (6.50)**: Diffusion Actor-Critic for offline RL. D4RL only, no real-world experiments. DIPOLE is clearly stronger — broader evaluation, real-world NAVSIM experiment, more novel math.
- **FISOR (7.50)**: Safe offline RL with feasibility-guided diffusion. Strong theoretical framework, well-received. DIPOLE has broader applicability but the comparison gaps (CFGRL missing from key benchmarks, modest standalone gains, Jaco underperformance) keep it below FISOR's level.

**Final score: 7.0** — DIPOLE is clearly above the 6.25–6.50 tier (SRPO, EFM, DAC) thanks to broader evaluation, more novel math, and large-scale real-world experiment, but lands below 7.50 (FISOR) due to missing comparisons and domain limitations.

Let me now write the final review.

Actually wait, I should double-check: is the paper really clearly better than DAC (6.50)? DAC got contribution scores of 2, 3, 2, 2. DIPOLE has a more novel contribution (dichotomous decomposition + CFG connection). DAC only evaluated on D4RL; DIPOLE on 39 tasks + NAVSIM. Yes, DIPOLE is clearly better.

And is DIPOLE really below FISOR (7.50)? FISOR had 3 ratings of 8 and one of 6. The critiques were about (1) hard constraint guarantees may not actually be 100% in practice, (2) missing baselines from hard-constraint safe RL. DIPOLE has: (1) CFGRL missing from OGBench/offline-to-online, (2) modest standalone gains w/o RS, (3) Jaco underperformance. These are somewhat comparable in severity. But FISOR's theoretical contribution (connecting HJ reachability to safe RL) and the safety guarantee claim are more impactful for their domain. DIPOLE's weaknesses around missing comparisons are arguably more directly addressable.

I'll go with 7.0. Let me write the final review now.Now let me write the final review.

## Summary

DIPOLE reformulates KL-regularized RL for diffusion policies by substituting the unstable exponential weighting with a greedified sigmoid-weighted reference policy. The key insight is that the optimal policy decomposes into a ratio of two dichotomous policies — one reward-seeking (π⁺, weighted by σ(βG)), one reward-avoiding (π⁻, weighted by 1−σ(βG)) — each trained with bounded weights, then combined at inference via a CFG-like score interpolation controlled by a greediness factor ω. The method is evaluated on 39 offline RL tasks across ExORL and OGBench, plus a 1B-parameter VLA model on the NAVSIM autonomous driving benchmark.

## Strengths

- **Mathematically elegant decomposition**: The derivation from the greedified KL-regularized objective (Eq. 5) through Theorem 1 to the dichotomous decomposition (Eq. 7–8) is clean and well-motivated. The identity σ/(1−σ) = exp(βG) allows the unstable exponential to be absorbed into a ratio of bounded sigmoid-weighted terms — a genuinely clever resolution of the optimality-stability trade-off identified in Section 3.1.

- **Stable training via bounded regression weights**: Unlike exp-weighted regression (Eq. 4) whose weights can explode, the dichotomous policy losses (Eq. 9) use strictly bounded weights σ(βG) ∈ (0,1) and 1−σ(βG) ∈ (0,1). This precludes loss explosion while still enabling greedy optimization through the ω parameter at inference.

- **Strong empirical results across diverse benchmarks**: Full DIPOLE with rejection sampling achieves the best score on 8 of 9 ExORL tasks (Table 1) with substantial margins on several (e.g., Walker-stand: 953 vs. IFQL's 873; Quadruped-walk: 928 vs. 883). On OGBench (Table 2), DIPOLE attains best or competitive aggregate scores across all 6 task categories — humanoid locomotion, maze navigation, soccer, and dexterous manipulation — demonstrating broad domain generality. Table 3 shows strong offline-to-online transfer (e.g., humanoidmaze-m: 61→97, antsoccer: 43→90).

- **Scalability to billion-parameter models**: Training a 1B-parameter VLA model (DP-VLA) with DIPOLE on the NAVSIM benchmark yields a 6.5-point PDMS improvement on the test split (88.3 → 94.8, Table 4), with gains in both safety (NC, DAC, TTC) and progress (EP) metrics. This is non-trivial evidence of real-world applicability beyond standard RL simulators.

- **Principled connection to classifier-free guidance**: Eq. (10) shows ∇_a log π* = (1+ω)∇_a log π⁺ − ω∇_a log π⁻, directly mirroring the CFG formulation. This provides a theoretically grounded RL interpretation for why CFG-style score combination works for policy optimization and yields ω as a tunable inference-time greediness parameter.

- **Informative ablation with DIPOLE w/o rs**: The inclusion of a variant without rejection sampling in Table 1 helps isolate the contribution of the training method. DIPOLE w/o rs outperforms CFGRL (the most conceptually similar prior work) on 5 of 9 ExORL tasks, confirming that the dichotomous training objective provides gains beyond CFGRL's uniform-threshold approach.

## Weaknesses

### Fatal

None.

### Major

- **CFGRL — the closest prior method — is not compared on OGBench or offline-to-online**: CFGRL (Frans et al., 2025) uses a CFG-like mechanism for diffusion policy improvement and is the most directly comparable prior work, acknowledged as such by the authors (line 119: "Our final formulation also has some similarity with CFGRL"). Yet CFGRL appears only in the ExORL comparison (Table 1) and is absent from OGBench (Table 2) and offline-to-online experiments (Table 3). This omission is significant because OGBench contains more challenging long-horizon tasks where DIPOLE's claimed advantages (stability, greedy optimization) would be most consequential to demonstrate against the closest conceptual competitor.

- **Jaco domain results reveal limitations**: On the two Jaco tasks in ExORL (Table 1), full DIPOLE achieves only 117 and 110, substantially trailing FQL (224 and 222) and IFQL (193 and 181). DIPOLE w/o rs gets only 84 and 63. The Jaco domain — an arm manipulation setting — is where the gap between DIPOLE and alternatives is largest. This suggests the method may not transfer well to certain manipulation domains, which is a meaningful limitation for a method claiming broad applicability.

- **DIPOLE w/o rs gains over CFGRL are modest and mixed**: On ExORL, DIPOLE w/o rs wins 5 of 9 tasks against CFGRL but loses on 4 (Walker-run, Quadruped-run, Cheetah-run, Cheetah-run-backward). Moreover, it trails IFQL (which also uses rejection sampling) on all 9 tasks — though this is an asymmetric comparison since IFQL uses RS while DIPOLE w/o rs does not. The standalone contribution of the dichotomous training scheme — the paper's core intellectual contribution — shows mixed evidence on its own. The paper would be strengthened by a direct ablation replacing the dichotomous decomposition with standard exponential-weighted regression plus the same rejection sampling, which would cleanly attribute the gains to the decomposition rather than to inference-time post-processing.

### Minor

- **DPPO comparison on NAVSIM is incomplete**: Table 4 shows DPPO only on the navtest split (PDMS 89.0), not on navtrain. Since DIPOLE navtrain achieves 89.7, one cannot assess whether DIPOLE is consistently better than DPPO or whether the gap is within noise across data splits. The paper does not claim DIPOLE beats DPPO on navtrain, but the missing comparison prevents a complete evaluation.

- **Offline-to-online reference policy update could be clearer**: The paper states that in offline-to-online RL, μ = π_{k−1} (line 123), but the derivation of the dichotomous decomposition (Eq. 5–8) is presented assuming a fixed μ. While the iterative application is conceptually straightforward (retrain π⁺ and π⁻ with the new μ at each step), a brief sentence clarifying this in the main text would improve readability.

- **Naming inconsistency**: The Ren et al. (2025) method is consistently called "DPPO" in the experiments (Table 4, line 223) but is referred to as "DDPO" in the related work (line 233: "DDPO (Ren et al., 2025)"). This should be resolved.

- **Lemma 1 extension to sigmoid weights is assumed rather than argued**: The paper states "Following Lemma 1, we can train the positive and negative policies" (line 107), but Lemma 1 (Eq. 4) was stated for exponential weighting exp(βG). The extension to sigmoid weights is correct (weighted regression with any weight w(s,a) recovers μ·w(s,a)), but the paper never makes this generalization explicit, leaving a small logical gap.

### Trivial

None.

## Nice-to-Haves

- A direct ablation replacing the dichotomous decomposition with standard exponential-weighted regression plus the same rejection sampling would cleanly attribute gains to the proposed decomposition.
- Including DPPO on navtrain would complete the NAVSIM comparison and allow a direct DIPOLE vs. DPPO comparison on the same data split.
- A sensitivity analysis of β and ω — two parameters that both control greediness — would help practitioners understand their interaction and tuning practicalities.
- Discussing the computational cost of training two diffusion policies (π⁺ and π⁻) versus one would be useful for practitioners considering adoption.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The core method's contribution is confounded with rejection sampling (evidential)"** — This was framed by the harsh critic as a fatal-seeming criticism. However, rejection sampling is a standard component in diffusion RL methods (used by IDQL, IFQL, and others). DIPOLE w/o rs does show standalone gains over CFGRL on 5/9 tasks. The concern has been reframed as a Major weakness about modest standalone gains rather than as a fatal confound.

- **"The offline-to-online mechanism is underspecified in the main text (methodological gap)"** — The harsh critic claimed the derivation "assumes a fixed μ" making the iterative online setting ill-defined. In reality, the closed-form solution applies for any given μ, and retraining at each iteration with updated μ is a natural interpretation. Demoted to minor.

- **"The paper claims 'perfect controllability over the greediness of action generation' (line 24) without evidence"** — The phrase "perfect controllability" refers to the continuous tunability of ω at inference (Eq. 10). A controllability sweep would be nice to have but demanding one is scope creep. Removed.

- **"Pseudo-closed-loop training vs. true closed-loop evaluation mismatch for NAVSIM"** — The paper uses pseudo-closed-loop for training efficiency and the official closed-loop simulator for evaluation, which is standard practice. No evidence of bias was presented by the critic. Removed.

- **Strength Finder claim that "DIPOLE w/o rs still outperforms CFGRL on most tasks"** — While technically true (5/9), this framing overstates the evidence. The results are mixed and this has been noted in the weaknesses.

- **Strength Finder generic claims about "problem importance" and "interesting question"** — These are superficial and have been removed.

- **Harsh critic's claim that Lemma 1's extension to sigmoid weights is insufficiently justified** — This is a presentation clarity issue, not a mathematical flaw. The extension is straightforward. Kept as minor.

## Novel Insights

The paper's reformulation of KL-regularized RL through a greedified sigmoid-weighted reference policy — and the resulting decomposition into dichotomous policies connected to CFG — is mathematically novel. The observation that the optimality-stability trade-off in exponential-weighted regression can be resolved by absorbing the exponential into a ratio of bounded sigmoid-weighted policies (via σ/(1−σ) = exp) is a genuinely non-obvious contribution. The connection to classifier-free guidance (Eq. 10) provides a principled RL interpretation for a widely-used diffusion sampling technique.

## Suggestions

- Add CFGRL comparisons on OGBench and offline-to-online experiments — this is the single most impactful improvement to validate the method's contribution against its closest conceptual competitor.
- Include an ablation that replaces the dichotomous decomposition with exponential-weighted regression + the same rejection sampling, to isolate the contribution of the decomposition itself.
- Add DPPO on navtrain for a complete NAVSIM comparison.
- Clarify the extension of Lemma 1 from exponential to sigmoid weights with a brief justification (e.g., "since weighted regression with any weight function w(s,a) recovers μ·w(s,a), Lemma 1 extends directly to sigmoid weights").
- Fix the DDPO/DPPO naming inconsistency in related work (line 233).

---

**Calibration comparison across all retrieved anchors:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| CFDG (O2O RL with CFG diffusion) | cXxfVkRCHJ | 3.00 | R1 | DIPOLE is substantially stronger — more novel math, broader evaluation, real-world experiment |
| BDQL (Behavior Diffusion Q-learning) | gEdg9JvO8X | 3.67 | R1 | DIPOLE clearly stronger — broader evaluation, more principled contribution |
| SRPO (Score Regularized Policy Opt) | xCRr9DrolJ | 6.25 | R1/R2 | DIPOLE is stronger — more novel decomposition, broader benchmarks (39 vs. D4RL only), real-world NAVSIM experiment |
| EFM/QIPO (Energy-Weighted Flow Matching) | HA0oLUvuGI | 6.25 | R1/R2 | DIPOLE is stronger — more clearly novel contribution, broader evaluation, large-scale experiment |
| DAC (Diffusion Actor-Critic) | ldVkAO09Km | 6.50 | R2 | DIPOLE is stronger — more extensive evaluation, real-world demonstration, more elegant math |
| CTRL (Conditioning Diffusion with RL) | svp1EBA6hA | 6.50 | R2 | Different domain (image generation conditioning); DIPOLE has comparable quality with broader RL evaluation |
| DMBP (Diffusion Model-Based Predictor) | ZULjcYLWKe | 7.00 | R2 | Different problem (robustness); DIPOLE has comparable quality |
| FISOR (Feasibility-Guided Safe Offline RL) | j5JvZCaDM0 | 7.50 | R2 | FISOR is slightly stronger — more complete theoretical framework with safety guarantees; DIPOLE is close but has more comparison gaps |

**Round 1 bracket: 6.0–7.5.** Round 2 narrowed this to a comparison against DAC (6.50 — DIPOLE clearly stronger) and FISOR (7.50 — DIPOLE slightly weaker due to comparison gaps and domain limitations). Final score: **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>