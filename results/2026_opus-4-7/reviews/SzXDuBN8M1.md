Round 1 bracket: between 6 and 8 based on Proto Successor Measure (6.75, similar topic) and the strong-anchor accepts (8.0).## Summary
TD-JEPA is a zero-shot unsupervised RL algorithm that jointly trains a state encoder φ, task encoder ψ, policy-conditioned multi-step predictor T, and latent-parameterized policies via a novel off-policy temporal-difference latent-predictive loss. The authors prove gradient-matching results connecting TD-JEPA to successor-measure approximation in an idealized tabular/linear setting, and empirically evaluate across 65 tasks/13 datasets on ExoRL and OGBench in both proprioceptive and pixel-based regimes.

## Strengths
- **Novel gradient-matching theory** (Thms 1 and 3) extends prior single-policy one-step latent-predictive analyses (Tang et al., 2023) to the multi-policy, multi-step TD setting, formally linking the self-supervised objective to successor-measure approximation losses.
- **Off-policy TD instantiation** (Eq. 9; Alg. 1) enables training entirely on offline reward-free transitions, a practically significant advance over on-policy methods such as BYOL-γ.
- **Strong pixel-based zero-shot performance**: DMC_RGB 628.8 vs. next-best 582.4; OGBench_RGB 41.34 ties top (Table 1). Probability-of-improvement analysis (Fig. 2) shows TD-JEPA is consistently among the top, with statistically significant advantages in visual domains.
- **Broad, honest evaluation** across 65 tasks / 13 datasets with a unified architectural protocol, and self-built BYOL*/BYOL-γ*/ICVF* baselines that are sometimes competitive with TD-JEPA — strengthening rather than weakening the comparison.
- **Fast-adaptation results** (Fig. 4) show frozen TD-JEPA representations enable sample-efficient offline/online fine-tuning, demonstrating downstream utility beyond zero-shot.

## Weaknesses

### Fatal
None.

### Major
- **Theorem 2 does not match Algorithm 1.** The non-collapse proof assumes a continuous-time relaxation in which optimal predictors are recomputed at each step (App. B.3), whereas Alg. 1 instead uses EMA targets and adds explicit covariance/orthonormality regularizers L_REG(φ), L_REG(ψ). The related-work section (Sec. 5) explicitly acknowledges this regularizer is needed to "avoid collapse, which we also observe in TD-JEPA." The theoretical guarantee thus does not cover the implemented algorithm; the regularizer is doing the actual non-collapse work, but its sensitivity is not discussed in the body and no collapse-without-regularizer ablation is provided. The theorem should be relabeled or extended to the regularized objective.
- **Theorems 1, 3, 4 rest on strong symmetry assumptions (A1–A3).** A3 (symmetric P^π_z) is essentially never satisfied in antmaze/cube/locomotion settings, and footnote 3 explicitly breaks the φ/ψ symmetry by defining π_z via T_φ (not T_ψ). The body presents results under A1–A3 with relaxations only pointed to App. C. The theorems should be framed as motivation, not as guarantees about the implemented algorithm; the conclusion does acknowledge this as the main limitation.

### Minor
- **Abstract slightly overstates proprioceptive results.** On OGBench proprio, TD-JEPA's 37.98 ties HILP and trails FB (39.04); TD-JEPA is not best on antmaze-mm/ms/ls/me, cube-single/double, scene, or puzzle-3x3 (Table 1). The conclusion's "matches in proprioception, exceeds in pixels" is accurate and the abstract should be calibrated to it.
- **Asymmetric-encoder ablation is only modestly supportive.** Fig. 3 (right) shows the asymmetric design beats the symmetric variant "more often than not" — a weak win that only loosely validates the Sec. 3.2 motivation for separate φ and ψ.
- **Fig. 4 omits BYOL-γ\*.** Since BYOL-γ* is TD-JEPA's closest competitor in zero-shot performance, leaving it out of the fine-tuning study makes it unclear whether the "fast adaptation from learned state encoders" property is specific to TD-JEPA or generic to self-predictive state encoders.
- **"Which dynamics to model?" analysis is shallow.** The qualifier that behavioral modeling helps on expert-like OGBench data is delivered in one sentence; the inconsistent result deserves a sharper diagnosis.

### Trivial
None retained.

## Nice-to-Haves
- A clean factorial ablation (one-step vs. multi-step × behavioral vs. policy-conditional × MC vs. TD), holding architecture fixed.
- λ sensitivity sweep and a "no L_REG → collapse" demonstration.
- More prominent presentation of the gradient-matching argument in the body; it is the paper's most distinctive theoretical contribution.

## Removed Points
These points are flagged to be removed; treat them with caution.
- *"Baselines are partly the authors' own work."* The asymmetry is openly disclosed (Sec. 6, footnote 5), and several rebuilt baselines (notably BYOL-γ*) sometimes beat TD-JEPA — the comparison is harder, not easier, for the authors. Per the rule against penalizing asymmetric comparisons that favor the baseline, removed.
- Generic strengths from the strength-finder (importance of problem, generality of the eval) without specific anchors were dropped or merged into concrete strengths.

## Novel Insights
None beyond the paper's own contributions. The gradient-matching extension to multi-policy, multi-step TD is itself a meaningful new theoretical observation contributed by the paper.

## Suggestions
- Reframe Theorem 2 to honestly cover Alg. 1's regularized objective, or relabel as motivational and back L_REG with a sensitivity/collapse ablation.
- Calibrate the abstract to "matches in proprioception, exceeds in pixels," matching the conclusion.
- Add BYOL-γ* to Fig. 4 to isolate the source of fast-adaptation benefits.
- Bring more of the gradient-matching result and the A3-relaxation discussion into the body.

## Score Calibration

Anchors retrieved:
- Round 1: `fnO5h1CFyh` (DHTM, 3.00, R) — weak anchor; very different scope. `It4KL6XnPq` (Foundation Policies with Memory, 3.00, R) — uses ExORL but limited contribution. `473sH8qki8` (Reward as Observation, 2.00, R). `OZ3NXrF3gQ` (RFPO, 2.50, R). `s9SVlWOcLt` (Proto Successor Measure, 6.75, R) — closest topical match. `o5Bqa4o5Mi` (π2vec, 5.25, A). `OMwD6pGYB4` (Distributional SR, 5.75, R). `X5qi6fnnw7` (Conservative World Models, 4.75, R) — closely related (FB extension). `agPpmEgf8C` (Predictive auxiliary objectives, 8.00, A). `DzGe40glxs`, `7BLXhmWvwF`, `9pW2J49flQ` (each 8.00, A) — strong anchors not topically as close.
- Round 2: `s9SVlWOcLt` (6.75, R, repeat). `OMwD6pGYB4` (5.75, R). `9sOR0nYLtz` (FB-CPR Zero-Shot Humanoid Control, 6.50, A) — very close topic, also FB-style zero-shot. `ms0VgzSGF2` (Bridging Self-Predictive RL, 6.75, A). `3mnWvUZIXt` (Principled Video Representations for RL, 7.25, A). `2pJpFtdVNe` (Preference Elicitation Offline RL, 6.80, A). `lUYY2qsRTI` (Delphic Offline RL, 7.50, A).

Round-1 bracket: 6 to 7.5. Round 2 anchors place TD-JEPA closest to FB-CPR (6.5 accept; comparable scope, broad eval, similar theory-empirics balance) and Bridging Self-Predictive RL (6.75 accept; closely related theoretical bridging contribution). TD-JEPA has stronger empirical breadth than Proto Successor Measure (6.75 reject) and clearly stronger contribution than Conservative World Models (4.75 reject). The Theorem-2/algorithm mismatch and abstract overclaim weigh against pushing above the 6.75–7 anchors. Settling at **6.5**, just at the FB-CPR anchor.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>