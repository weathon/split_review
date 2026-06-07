## Summary

TD-JEPA introduces a temporal-difference (TD) variant of latent-predictive representation learning for zero-shot reinforcement learning. The core contribution is replacing the Monte Carlo target (Eq. 5) with a TD target (Eq. 7/9), enabling off-policy, multi-policy, multi-step latent prediction from offline reward-free transitions. The method trains explicit state and task encoders, a policy-conditioned predictor, and latent-space policies, enabling zero-shot optimization for any reward in the span of learned features. The paper provides theoretical analysis (gradient-matching theorems, non-collapse guarantee, policy evaluation bound) and evaluates on 65 tasks across 13 datasets from ExoRL and OGBench.

## Strengths

1. **Novel and well-motivated formulation**: The shift from MC to TD latent-prediction (Eq. 7→9) extends latent-predictive learning beyond the one-step/on-policy limitations of prior work. The connection to the Bellman equation for successor features (lines 88–92) is a non-obvious insight that enables a genuine new capability — learning representations predictive of long-term dynamics across multiple policies from off-policy, offline one-step transitions.

2. **Gradient-matching theorems (Th. 1, 3) provide substantive theoretical grounding**: The paper proves that gradients of the latent-predictive losses w.r.t. the representations match those of explicit successor-measure approximation losses. This extends prior analyses (Tang et al., 2023; Voelcker et al., 2024) from single-policy one-step prediction to the multi-policy multi-step setting. The non-collapse guarantee (Th. 2) and policy evaluation bound (Th. 4) add further theoretical scaffolding.

3. **Clear empirical advantage on pixel-based DMC**: Table 1 shows TD-JEPA achieves **628.8 ± 5.5** on DMC_RGB (avg over 4 domains), substantially outperforming the next-best baseline BYOL-γ* at 582.4 ± 9.8 — a gap of ~46 points. This addresses what the paper correctly identifies as "one of the most challenging settings for unsupervised RL so far" (line 36).

4. **Comprehensive evaluation**: 65 tasks across 13 datasets, 7 baselines, two observation modalities (proprio/RGB), with probability-of-improvement analysis (Fig. 2), ablation studies (Fig. 3: prediction target, symmetric vs. asymmetric encoders), and fast-adaptation experiments (Fig. 4). The inclusion of representation learning methods (BYOL*, BYOL-γ*, ICVF*) adapted to the zero-shot framework is a strong design choice.

5. **Fast adaptation results (Fig. 4)**: Frozen TD-JEPA state encoders enable rapid offline and online RL adaptation, often matching or exceeding training from scratch. This demonstrates a practical secondary benefit beyond zero-shot performance.

## Weaknesses

### Fatal

None.

### Major

1. **Theoretical assumptions limit the force of the results.** Theorems 1–4 rely on assumptions (A1)–(A3): orthonormal representations, a uniform state distribution, and symmetric transition matrices for all policies. A uniform state distribution is almost never satisfied in any RL setting of interest, and symmetric dynamics require reversibility. The paper correctly notes (line 157) that "they can be relaxed, at the price of more involved proofs," but the practical algorithm (Alg. 1) differs substantially from the idealized linear-tabular setting — it uses nonlinear function approximation, target networks, EMA updates, covariance regularization, and coupled predictor+encoder optimization. The gradient-matching argument is elegant but shows gradients match at the *optimal predictor for each loss*, not along the joint training trajectory of the practical algorithm. The theorems provide useful intuition, but their force as justification for the empirical success of the practical algorithm is limited. This gap is wider than the paper's tone conveys.

### Minor

2. **Empirical advantage is concentrated in DMC_RGB.** In the other three evaluation suites, results are competitive but mixed:
   - **DMC proprio**: TD-JEPA 661.2 ± 8.3 vs FB 648.2 ± 4.1 (modest advantage, CIs overlap)
   - **OGBench_RGB**: 41.34 ± 0.45 vs BYOL-γ* 41.58 ± 0.64 (statistically tied)
   - **OGBench proprio**: 37.98 ± 0.77 vs FB 39.04 ± 0.66 (FB numerically higher)
   The paper's "matches or outperforms" framing is accurate, but the abstract's emphasis on "especially in the challenging setting of zero-shot RL from pixels" is more cleanly supported for DMC_RGB than for OGBench_RGB (where TD-JEPA is tied with BYOL-γ*). The probability-of-improvement analysis (Fig. 2) correctly shows significance in RGB domains overall, but per-suite the advantage is uneven.

3. **No hyperparameter sensitivity analysis.** TD-JEPA has multiple interacting components (loss balancing, EMA rates, covariance regularization coefficients, latent dimensions d_φ and d_ψ). The paper does not report how robust results are to these choices, which would substantially increase confidence given the method's complexity (4+ networks trained simultaneously).

4. **BC regularization in OGBench mentioned but not discussed as potential confound.** Footnote 4 notes that BC regularization is applied in OGBench based on Park et al. (2025b). If BC regularization interacts differentially with representation quality (helping methods with better representations more), this could confound the OGBench results. A brief discussion of this possibility would strengthen the analysis.

### Trivial

None.

## Nice-to-Haves

- A cleaner ablation isolating the TD-vs-MC comparison (holding architecture and policy-conditioning constant, varying only the loss objective) would directly test the paper's central claim about off-policy TD being the source of improvement.
- The paper would benefit from an analysis decomposing the DMC_RGB gain: how much comes from the improved state encoder vs. the TD loss vs. multi-step prediction.
- Reporting per-task effect sizes would sharpen conclusions where CIs overlap across methods.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Explicit state encoder as a comparison risk** (Harsh Critic): The paper explicitly states (footnote 6) that this protocol *improves* baseline performance (1.3× and 2.4× higher for pixel-based methods). This works in baselines' favor, not TD-JEPA's, and strengthens the evaluation rather than weakening it.
- **Chicken-and-egg problem in actor loss**: The critic acknowledges this is common to all successor-feature methods, not specific to TD-JEPA. Not a meaningful weakness.
- **Worst-case bound of Theorem 4**: Standard for theoretical bounds in this literature. Not a meaningful criticism.
- **Baseline tuning budgets**: The paper states baselines were "tuned over comparable hyperparameter grids" — standard practice.
- **Statistical rigor about overlapping CIs**: The paper already uses the standard boldfacing convention for overlapping CIs and provides probability-of-improvement analysis.
- **Missing appendix content / missing proofs**: Parser strips these; they exist in the original submission.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- In the camera-ready version, consider adding a targeted ablation that isolates the TD-vs-MC comparison (fix architecture and policy-conditioning, swap only the loss objective) on a subset of domains.
- Report hyperparameter sensitivity for key parameters (EMA rate, latent dimensions, regularization coefficient).
- Discuss the potential interaction of BC regularization with representation learning quality in OGBench.

## Score and Decision

**Calibration summary:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Proto Successor Measure | s9SVlWOcLt.md | 6.75 | R1/R2 | Weaker experiments (2 envs vs 65), rejected; TD-JEPA is clearly stronger |
| Conservative World Models | X5qi6fnnw7.md | 4.75 | R1 | Incremental contribution, rejected; TD-JEPA is substantially stronger |
| π2vec: Policy Representation with SF | o5Bqa4o5Mi.md | 5.25 | R1 | OPE-focused, less ambitious; TD-JEPA is stronger |
| Distributional Analogue to SR | OMwD6pGYB4.md | 5.75 | R2 | Narrower scope; TD-JEPA is stronger |
| General-Purpose Model-Free RL (MR.Q) | R1hIXdST22.md | 7.50 | R2 | Comparable evaluation scope, similar theory-practice gap; TD-JEPA has cleaner baseline comparisons but MR.Q accepted at similar score |
| Bridging State and History Reps | ms0VgzSGF2.md | 6.75 | R2 | Theory-focused, mixed reviews (3,8,8,8); TD-JEPA has stronger empirical contribution |

**Round 1 bracket**: [6.5, 8.5], based on clear superiority over the 4.75–6.75 anchors.

**Round 2 narrowing**: Comparing to the 7.50 MR.Q anchor (accepted with similar strengths and weaknesses — strong evaluation, theory with assumptions, hyperparameter concerns) and the 6.75 bridging paper (accepted but theory-focused with weaker experiments), TD-JEPA sits between them. It has stronger experiments than the 6.75 anchor and a cleaner contribution than the 7.50 anchor. 

**Final score: 7.0** — a strong paper with a genuine contribution (the TD latent-prediction formulation is novel, well-motivated, and supported by thorough experiments), but with meaningful limitations (concentrated empirical advantage, theory-practice gap wider than ideal) that prevent it from being in the top tier.

**Decision: Accept**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>