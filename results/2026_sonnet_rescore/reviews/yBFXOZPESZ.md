## Summary

ANO introduces an adaptive optimizer that decouples the update direction (sign of the momentum) from the update magnitude (instantaneous gradient norm), combined with a modified Yogi-style second-moment estimator that includes an explicit decay factor to improve memory control in non-stationary settings. The paper further proposes Anolog, which replaces the fixed β₁ with a logarithmic schedule to eliminate the need for momentum-coefficient tuning. The primary claim — that this design substantially improves performance in noisy and non-stationary regimes like reinforcement learning — is backed by rigorous RL experiments (IQM, 10 seeds, 95% confidence intervals across MuJoCo SAC and Atari PPO), while competitive but modest results on CIFAR-100 and GLUE corroborate that the design does not degrade in stable supervised settings.

---

## Strengths

- **Consistent, large RL gains supported by rigorous evaluation methodology**: In SAC-MuJoCo (Table 4), default Ano achieves a normalized average of 99.48 vs. Adam's 90.66 (rank 1.4 vs. 3.4). In PPO-Atari (Table 5), Ano achieves 95.99 normalized average vs. Adam's 87.54. Both use IQM with 10 seeds and 95% CI, following best practices (Henderson et al., 2018; Agarwal et al., 2021).

- **Noise-robustness directly quantified, not just asserted**: Table 1 shows that Ano's accuracy gap over Adam on CIFAR-10 with injected Gaussian noise grows systematically from −1.43 pp at σ=0 to −7.08 pp at σ=0.20, providing direct quantitative support for the direction-magnitude decoupling hypothesis.

- **Ablation cleanly isolates the contribution of each design component**: Table 6 shows that direction-only variants (Signum: 9393 DRL) and magnitude-decoupled variants (AdamGrad: 9855 DRL) each improve over Adam baseline (7880 DRL), and their combination in Ano reaches 10520 DRL, confirming independent contributions. Critically, pure sign-magnitude (YogiSignum: −286 DRL) collapses entirely, motivating the inclusion of gradient normalization.

- **No degradation on low-noise benchmarks — honest scope**: CIFAR-100 Ano = 70.31% vs. Adam 69.57% (Table 2); GLUE average 82.92 vs. Adam 82.64 (Table 3). The paper explicitly frames CV and NLP as "diagnostic checks," not superiority claims, demonstrating intellectual honesty.

- **Non-asymptotic convergence guarantee matching sign-based methods**: Section 5.1 derives Õ(K^{−1/4}) under standard smoothness and bounded-variance assumptions, explicitly acknowledging (in the Discussion) that this is weaker than O(K^{−1/2}) for Adam/SGD due to the fundamental cost of decaying step sizes in sign-based methods — a point the paper addresses transparently.

- **Hyperparameter robustness demonstrated visually**: Figure 3 shows that Ano maintains high reward across a broad β × η grid on the HalfCheetah proxy, while Adam's reward surface is sharply peaked, supporting the claim that gains are not merely artifacts of better tuning.

---

## Weaknesses

### Fatal
None.

### Major

- **Theory-practice mismatch not explicitly acknowledged**: Section 5.1 states the convergence theorem using the schedule η_k = η/k^{3/4} and β_{1,k} = 1 − 1/√k — the schedule corresponding to Anolog, not the fixed β₁ = 0.92 used in all Ano experiments (stated in Section 3: "We set β₁ = 0.92 and β₂ = 0.99"). The theorem is attributed to "Ano," but the conditions actually match Anolog. This is a common pattern in optimizer papers and does not undermine the empirical results, but the paper presents the theorem as if it directly covers the empirically evaluated Ano; a one-sentence clarification that the theoretical guarantee formally applies to the schedule in Section 5.1 (which corresponds to Anolog's setting) would be necessary for correctness.

### Minor

- **Lion's catastrophic failure on Humanoid is unexplained and leaves a fairness question**: Table 4 shows Lion (default) scoring 98.22 ± 32.33 on Humanoid-v5 — roughly 50× below every other optimizer (4,792–5,395). Even after 40 GPU-hour tuning, Lion reaches only 1,349 ± 1,222. This dramatically depresses Lion's normalized average (71.74), inflating Ano's relative margin in that comparison. If this reflects a real Lion–SAC incompatibility (e.g., sign updates interacting badly with entropy temperature tuning), it should be explained. If it reflects an avoidable configuration issue, the baseline is not fairly represented. Importantly, Ano remains dominant even excluding Lion from the comparison (vs. Adam 90.66, RMSprop 87.83, Adan 78.38), so this does not affect the core Ano vs. Adam claim — but it does leave a cloud over the Lion comparison specifically.

- **Duplicate "Adam" rows in Table 3 are unlabeled**: Both the Default and Tuned sections of Table 3 contain two rows identically labeled "Adam" with substantially different scores (e.g., 82.64 vs. 80.62 average in Default; 82.50 vs. 82.35 in Tuned). One is very likely AdamW or a different learning rate configuration. This makes it impossible to determine which Adam variant Ano is being compared against without additional clarification.

### Trivial

- **Anolog's logarithmic momentum schedule is labeled inconsistently in Table 6**: The Anolog ablation row labeled "Ano log k" uses β_{1,k} = 1 − 1/√k (the square-root schedule), while the row labeled "Ano √k" uses β_{1,k} = 1 − 1/k (the harmonic schedule). The labels appear swapped or misspecified relative to Section 4's definition of Anolog as β_{1,k} = 1 − 1/log(k+2). This needs clarification to properly follow the ablation logic.

---

## Nice-to-Haves

- A synthetic non-stationary experiment (e.g., quadratic with shifting optima) demonstrating that Ano's recovery after distributional shift is specifically faster due to the magnitude decoupling — rather than just the modified second moment — would make the design principle more mechanistically convincing beyond what the ablation shows.
- The hyperparameter robustness analysis (Figure 3) is conducted only at 100k steps on HalfCheetah; extending this to 1M steps across multiple environments would substantially strengthen the claim that robustness holds in the full training regime.
- A brief informal argument or one-sentence proof sketch for why β₂ ≥ 1/2 is sufficient to maintain v_k ≥ 0 under the modified Yogi update would make the algorithm description formally complete (by induction: when v_{k−1} > g_k², v_k = β₂v_{k−1} − (1−β₂)g_k² > β₂g_k² − (1−β₂)g_k² = (2β₂−1)g_k² ≥ 0 for β₂ ≥ 1/2).

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

**W-R1 (Harsh Critic): Modified second-moment instability (v_k < 0)** — Removed. The constraint β₂ ≥ 1/2 stated in Section 3 is sufficient to guarantee v_k ≥ 0 by induction. When v_{k−1} > g_k²: v_k = β₂v_{k−1} − (1−β₂)g_k² > β₂g_k² − (1−β₂)g_k² = (2β₂−1)g_k² ≥ 0 for β₂ ≥ 1/2. The paper correctly states the constraint; the instability scenario the critic constructs does not hold under it.

**W-R2 (Harsh Critic): Paper elides that Õ(K^{−1/4}) is worse than O(K^{−1/2}) for Adam/SGD** — Removed. Section 5.1's Discussion explicitly states: "Compared to adaptive schemes (SGD, Adam, Yogi) achieving O(K^{−1/2}), our Õ(K^{−1/4}) rate stems from a fundamental limitation of sign-based methods." The paper directly addresses this comparison.

**W-R3 (Harsh Critic): Noise injection is "artificial" and not equivalent to RL non-stationarity** — Partially removed/demoted. The paper itself calls Table 1 an "assess[ment of] noise robustness" and frames it as a supporting diagnostic, not the primary mechanistic justification. This is a reasonable framing for a supplementary analysis. However, the observation about Grams improving at σ = 0.01 being "weakly explained" is a fair minor note, left in Nice-to-Haves.

**W-R4 (Strength Finder, generic): "This paper addresses an important problem"** — Removed as generic. Retained only strengths grounded in specific evidence.

**W-R5 (Harsh Critic): Nesterov-style instability "deserves an additional sentence of intuition"** — Removed as a trivial/nitpick. The paper discusses this in Section 8 and explicitly notes it as a limitation; demanding further explanation is scope creep for a one-sentence limitations mention.

---

## Novel Insights

The paper surfaces an interesting asymmetry in optimizer design: using momentum only for directional information (its sign) while delegating magnitude to instantaneous gradient norms avoids the "self-cancellation" problem in Adam, where noise spikes in both momentum direction and magnitude partially cancel and reduce effective momentum size. The ablation (Table 6) provides clean empirical evidence that these two design axes (sign-direction and gradient-norm magnitude) independently contribute and their gains are near-additive in RL (Signum: 9393, AdamGrad: 9855, Ano: 10520, Adam baseline: 7880) — while YogiSignum (sign only, no norm) catastrophically fails at −286, showing that gradient normalization is not optional. This cleanly separates the contributions in a way that directly validates the paper's design thesis.

---

## Suggestions

1. Add a sentence in Section 5.1 clarifying that the convergence theorem uses the decaying β_{1,k} schedule (which corresponds to Anolog's design), and that a formal guarantee for constant-β₁ Ano remains open.
2. Resolve the Table 3 duplicate "Adam" rows by clearly labeling one as AdamW or specifying the differing hyperparameter configurations.
3. Investigate and report (even briefly) why Lion collapses on Humanoid-v5 — whether it's a known interaction between sign-based updates and SAC's temperature parameter, or an artifact of the tuning protocol.
4. In Table 6, confirm and fix the apparent label swap between "Ano log k" and "Ano √k" to match the schedule definitions in Section 4.
5. Consider adding a brief derivation sketch (even in a footnote) showing v_k ≥ 0 under β₂ ≥ 1/2, making the algorithm formally well-posed without relying on ε to paper over it.

---

## Score and Decision

**Originality**: The direction-magnitude decoupling angle has some precedent (Grams takes the opposite pairing), but the specific combination of momentum-sign direction with instantaneous gradient-norm magnitude plus the modified Yogi second moment is novel and clearly motivated. Moderate-to-high originality.

**Importance**: RL optimization is a real and difficult problem; a general-purpose optimizer that delivers consistent 8–12% normalized score gains across diverse MuJoCo and Atari environments is practically valuable.

**Claims well-supported**: The core RL claim is strongly supported with IQM, 10 seeds, CI95%, and ablations. The CV/NLP diagnostic claims are supported but inherently limited in scope (as the authors explicitly acknowledge).

**Soundness**: Strong empirically. The theory is at the standard level for optimizer papers (matching prior sign-based analyses) but has the common gap of the theorem not technically covering the constant-β₁ variant used in practice.

**Clarity**: Generally clear, but Table 3 duplicate rows and Table 6 schedule label inconsistency are genuine presentation issues.

**Community value**: Solid contribution to RL optimization; a pip-packaged optimizer ready to use in PyTorch/TF/JAX with reproducible code increases community value.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>4</claims_supported>
<soundness>4</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>