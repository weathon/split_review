Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes DIPOLE (Dichotomous Diffusion Policy Improvement), a novel RL algorithm for diffusion/flow-matching policies. The key idea is to replace the unstable exponential-weighted regression (standard in KL-regularized RL) with a greedified objective whose optimal policy naturally decomposes into two dichotomous policies: a positive (reward-maximizing) policy weighted by \(\sigma(\beta G)\) and a negative (reward-minimizing) policy weighted by \(1-\sigma(\beta G)\). During inference, the policy score is a linear combination \((1+\omega)\nabla\log\pi^+ - \omega\nabla\log\pi^-\), which mirrors classifier-free guidance and enables controllable greediness. The method is evaluated on 39 offline RL tasks (ExORL, OGBench), offline-to-online settings, and a 1-billion-parameter VLA model for autonomous driving on NAVSIM.

## Strengths

1. **Elegant and principled dichotomous decomposition with a clear CFG connection.** The derivation from the greedified objective (Eq. 5) through Theorem 1 to the decomposition (Eq. 7–8) and the CFG-like inference rule (Eq. 10) is mathematically sound and internally coherent. The fact that the optimal policy's score is a linear combination of positive and negative policy scores, controlled by a single parameter \(\omega\), is a genuinely novel insight with practical value. The contrast with CFGRL's heuristic approach (Section 3.2) is correctly drawn.

2. **Extensive and well-executed empirical evaluation.** The paper evaluates across 39 offline tasks (ExORL + OGBench), offline-to-online settings, and a large-scale VLA model on NAVSIM — all with 8 seeds and standard deviations. DIPOLE achieves best or near-best performance in most categories (e.g., Walker stand 953 vs. next-best 873; humanoidmaze-medium-navigate 68 vs. next-best 60; Table 1–2). The offline-to-online gains (e.g., humanoidmaze-m: 61→97) are large and consistent.

3. **Scalability to a real-world-sized model.** Fine-tuning a 1-billion-parameter vision-language-action model (DP-VLA) with DIPOLE on NAVSIM achieves a PDMS of 94.8, substantially surpassing the imitation pre-trained baseline (88.3) and all prior published methods including the DPPO fine-tuned variant (89.0). This is a strong demonstration that the method is practically viable at scale.

4. **Stable training via bounded sigmoid weights.** A core claim of the paper — that the sigmoid-weighted losses avoid the loss explosion of exponential weighting — is empirically supported: the *DIPOLE w/o rs* variant (no rejection sampling) already outperforms the heuristic CFGRL on most ExORL tasks, isolating the benefit of the dichotomous design.

## Weaknesses

### Fatal
None.

### Major
None. The paper's weaknesses are not severe enough to undermine acceptance.

### Minor

1. **The greedified objective (Eq. 5) is introduced as a design choice rather than derived from standard RL foundations.** The paper regularizes toward a value-aware reference \(\mu(a|s)\cdot\sigma(\beta G(s,a))/Z(s)\) and cites related work doing similar things, which is honest. However, the objective is posted rather than derived (e.g., from a variational bound or trust-region interpretation), and the paper does not discuss whether the greedified KL formulation admits a policy improvement guarantee over the original reference \(\mu\). This weakens the theoretical framing somewhat, though it does not invalidate the empirical results or the internal logic from Eq. 5 onward. A short discussion acknowledging this design choice and its implications would suffice.

2. **Computational cost of training two models is not discussed for standard RL benchmarks.** For the VLA experiment, LoRA modules are used, keeping overhead modest. But for the standard RL experiments (ExORL, OGBench), the paper does not state whether full diffusion models are trained for \(\pi^+\) and \(\pi^-\) or whether parameter-efficient methods are used. If two full models are trained, this doubles parameters and training cost relative to single-policy methods like FQL or CFGRL. This does not make the method impractical (many successful RL methods use two models), but the omission is noticeable.

3. **NAVSIM test-split evaluation, while clearly framed, could invite misinterpretation.** The paper responsibly states that the navtest variant is "trained on the test split without using any ground-truth" and frames it as a "human take-over" scenario. Both navtrain (+1.4 PDMS) and navtest (+6.5 PDMS) results are reported. However, the substantial gain on navtest could be misinterpreted by readers as a standard test-set result rather than an additional exploratory demonstration. A more emphatic caveat in the main text (not just the setup paragraph) would help.

### Trivial
None.

## Nice-to-Haves

- A sensitivity study on \(\omega\) for a representative task would strengthen the "controllable" claim and help practitioners choose this hyperparameter.
- An ablation that compares the full two-model design against a single-model variant using the same greedified objective but without the decomposition (directly training \(\pi^*\)) would isolate the benefit of the dichotomous approach.
- For the VLA experiment, reporting whether the navtrain gain (+1.4) is statistically significant would be useful.

## Removed Points

- The harsh critic's statement that "weighted regression can only achieve greedy reward maximization when the temperature parameter is set to a large value" is imprecise: the paper's point (Section 3.1) is about the *optimality-stability trade-off*, not about impossibility at small \(\beta\). The claim is defensible in context and not a weakness.
- The harsh critic's suggestion that baselines' hyperparameters may not have been re-tuned. The paper states it uses default or reported hyperparameters; this is standard practice and not a weakness.
- Strength Finder's generic strengths about "important problem" and "well-motivated" are dropped as lacking concrete evidence.
- The harsh critic's framing of the NAVSIM issue as "evaluation fairness concern" — the paper explicitly flags the test-split training as a non-standard scenario. The concern is valid but demoted from Critical to Minor. The critic's demand for the navtrain variant to be "the primary comparison" is already satisfied by the paper's presentation.

## Novel Insights

None beyond the paper's own contributions. The core insight — that a greedified KL-regularized objective leads to a dichotomous policy decomposition with CFG-like controllable inference — is the paper's own novel contribution, and the reviews do not surface any additional synthesis beyond it.

## Suggestions

1. Add a brief paragraph acknowledging that Eq. (5) is a design choice (regularizing toward a value-weighted reference) rather than a derived bound, and discuss whether a policy improvement guarantee holds relative to \(\mu\).
2. Add a sentence on computational cost: state whether the two policies for standard RL benchmarks are full models or if weight-sharing/LoRA is used; report relative training time vs. a single-policy baseline.
3. Add a one-sentence caveat beside the navtest result in the main text clarifying that this variant is an exploratory scenario, while the navtrain result is the standard evaluation.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing.** Three queries targeting bands (≤3.5), (3.5–7.5), (≥7.5).

- Low-band anchors: anchor_id=eM8Db7ukSB (2.50, Reject), cr3FWHXgEZ (3.00, Withdrawn), IsJaTCzyBA (2.50, Withdrawn), MKM8iEaowV (3.00, Reject). All are clearly weaker papers with limited experiments or unclear contributions. → DIPOLE is well above this band.
- Mid-band anchors: A2JF06XcPG (4.00, Reject), VJZ477R89F (7.33, Accept Oral), ckUU5XySLn (4.00, Reject), sOSdvn2sM2 (5.50, Reject). DIPOLE is stronger than the 4.0 and 5.5 papers (more extensive experiments, clearer contribution) and comparable to the 7.33 paper (different domain).
- High-band anchors: oBXfPyi47m (8.00, Poster), Ahdsg2nkNH (8.00, Poster), 248ysaRatx (8.00, Poster), kkBOIsrCXh (8.00, Poster). These are on unrelated topics (control variates, quantum, navigation foundation model) — not useful for direct comparison.

**Initial bracket:** [5.0, 7.5]

**Round 2 — Narrowing.** Two queries within (5.5, 7.5).

- h06nffFJqi (6.50, Poster) — discrete diffusion guidance analysis; different problem.
- 60VgwdzxDM (6.00, Poster) — One-Step Flow Q-Learning; strong D4RL results but narrower scope (state-based D4RL only). DIPOLE has broader evaluation and a more novel algorithmic idea. → DIPOLE slightly stronger.
- b7Ftp6U78i (6.00, Poster) — inference-time scaling via search; different approach.
- k0Kb1ynFbt (6.00, Oral) — exploratory diffusion for unsupervised RL; different setting.
- 8zoxC9e23q (6.00, Poster) — SQDF, KL-regularized RL for diffusion fine-tuning; similar theoretical framing but on image generation. DIPOLE has more extensive decision-making benchmarks. → DIPOLE comparable or stronger.
- L2rfd2Czbj (6.67, Poster) — wd1, weighted policy optimization; similar idea of avoiding unstable ratios, strong theory. DIPOLE comparable in theoretical depth, broader in application domain.
- AZ6lqcvHLX (6.67, Oral) — half-order fine-tuning for diffusion; different technical approach.

**Final score determination:** DIPOLE is clearly stronger than the 4.0–5.5 papers in this space (more extensive evaluation, clearer contribution) and compares favorably with the 6.0–6.7 papers (comparable theoretical novelty, broader experimental validation including a real-world-scale autonomous driving deployment). The paper's main weaknesses — the design-choice nature of Eq. 5 and the lack of computational cost discussion — are minor and addressable. The paper sits above the 6.0–6.7 cluster but below the 7.33 DiffusionNFT anchor (which had more striking efficiency results and a novel RL-on-forward-process paradigm).

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>