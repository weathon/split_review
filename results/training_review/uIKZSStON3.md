Now I have a thorough understanding of the paper and can verify the reviewer's claims against the actual text. Let me synthesize the final review.

---

## Summary

This paper proposes ICEE (In-context Exploration-Exploitation), an extension of Decision Transformers to multi-episode in-context RL. ICEE leverages the insight that maximum-likelihood training of a sequence model captures epistemic uncertainty in its predictive distribution, enabling exploration-exploitation trade-offs purely through Transformer inference without explicit Bayesian inference or gradient-based adaptation. The paper introduces an unbiased training objective (importance-weighting by the inverse of the behavior policy) and a cross-episode return-to-go design that conditions on whether the current episode improves upon past episodes. Experiments are conducted on discrete Bayesian optimization (compared against GP+EI) and small grid-world RL tasks (Dark Room, Dark Key-to-Door).

## Strengths

- **Novel integration of EE into in-context RL with a clean theoretical motivation.** The paper derives that the predictive distribution of a maximum-likelihood-trained sequence model contains epistemic uncertainty (Section 3, Eqs. 1–7, lines 52–73), and uses this insight to design an EE mechanism that operates entirely through Transformer forward passes. This avoids the expensive RL training trajectories required by prior in-context methods like Algorithm Distillation.

- **Unbiased training objective that corrects for behavior-policy bias.** The importance-sampling correction (Eq. 9, line 104) is a principled solution to the bias introduced by data-collection policies. This is empirically validated in the Dark Room (Biased) experiment (Fig. 3d), where ICEE significantly outperforms its biased variant, confirming the correction enables effective exploration even when training data are systematically skewed.

- **Cross-episode return-to-go design for policy improvement without optimal demonstrations.** The binary indicator $\tilde{c}_k$ (whether episode $k$ achieves the best return so far, Section 5, lines 118–126) enables the model to improve across episodes without requiring expert or learning trajectories for training. This is a sensible architectural contribution over single-episode Decision Transformers.

- **Use of cheap data-collection policies for training.** The paper shows that ICEE can be trained on trajectories from a simple $\epsilon$-greedy heuristic or biased action-sampling scheme (Section 6, lines 181–184; Section 7, lines 199–203), avoiding the expensive RL algorithm runs needed by AD. This directly addresses the computational bottleneck identified in the introduction.

## Weaknesses

### Fatal
None. The paper's core claims are not invalidated, though several are substantially weakened by the issues below.

### Major

- **The method requires exact knowledge of the data-collection policy $\pi$ — a fundamental scope limitation not adequately acknowledged.** The unbiased objective (Eq. 9) requires $\pi_k(a|o)$ in the denominator. In both the RL and BO experiments, $\pi$ is known by construction (ε-greedy cheating policy or the analytically defined action-sampling distribution). However, the abstract and introduction frame the contribution in general offline-RL terms ("collected from a number of policies," "offline data"), and the paper never discusses how $\pi$ would be obtained for realistic offline datasets where the behavioral policy is unknown or must be estimated. If $\pi$ must be estimated, the correction becomes an approximation whose error could dominate. This does **not** invalidate the paper — the method works in settings where $\pi$ is known — but the scope should be stated precisely, and the paper currently overclaims generality.

- **The RL experiments do not convincingly isolate the EE mechanism from a simpler improvement-signal explanation.** AD-sorted (which sorts episodes by $\epsilon$ in descending order, thereby mimicking improving performance) is described as being able to "solve the games at the end of the sequence" (line 260) and nearly matches ICEE's performance. This is a significant concern: the cross-episode RTG $\tilde{c}_k$ and AD-sorted's ordering both encode the same improvement signal, so the observed performance gain may stem primarily from conditioning on improvement — not from an EE mechanism driven by epistemic uncertainty. The paper's claim that EE "emerges" from epistemic uncertainty (line 29) is not directly tested; the decreasing action entropy (Fig. 5) is consistent with either EE or simply learning a deterministic mapping.

- **BO evaluation is insufficient to support "state-of-the-art" claims.** The only GP baseline is Expected Improvement (EI), a basic acquisition function. The paper claims "state-of-the-art BO method" (line 185) and "state-of-the-art EE" (line 271), but comparing against a single, decades-old acquisition function does not establish SOTA performance. Modern BO methods (entropy search, GP-UCB with learned schedules, trust-region Bayesian optimization, etc.) are not compared. The speed advantage is genuine and valuable, but the "SOTA quality" claim is not supported.

- **The cross-episode RTG design has an unanalyzed distribution mismatch between training and inference.** During training, $\tilde{c}_k=1$ only when an episode achieves the best return so far — which may be rare (~1/K of episodes). At inference, $\tilde{c}_k$ is always set to 1 (line 148). The paper does not analyze whether this distribution shift causes instability or degeneracy in the model's action predictions.

### Minor

- **No confidence intervals or variance estimates are reported for RL results** (Section 7, Fig. 2). Plots show averages across 100 games but without error bars, making it impossible to assess whether the gap between ICEE and AD-sorted is statistically significant or within run-to-run variability.

- **The RL evaluation is confined to small grid worlds (9×9) with simple dynamics.** The paper does not test on environments with more severe partial observability, larger state spaces, or continuous actions. While this does not invalidate the results, it limits the strength of the claims about general in-context RL capability.

- **No empirical validation that the model's predictive distribution actually reflects epistemic uncertainty.** Section 3 provides a theoretical argument (infinite-data limit) that the predictive distribution captures epistemic uncertainty, but no experiment measures whether the trained model's predictive entropy correlates with actual uncertainty (e.g., overconfident predictions for out-of-distribution game parameters). The action entropy plot (Fig. 5) is indirect and does not distinguish epistemic from aleatoric uncertainty or deterministic mapping.

- **The paper does not test generalization to different numbers of episodes** (varying $K$ between training and evaluation) or to sequence lengths longer than those seen during training.

### Trivial
None of note.

## Nice-to-Haves

- Evaluate ICEE on settings where $\pi$ is unknown and must be estimated (e.g., behavioral cloning from a fixed dataset), to clarify the method's practical applicability.
- Compare against a true meta-RL method (e.g., MAML, PEARL) on the same grid-world tasks, to contextualize the in-context learning advantage.
- Include ICEE-biased curves on the unbiased RL tasks (Figs. 2a–c) for completeness, rather than only stating they "achieved similar performance."

## Removed Points

These points were flagged by reviewers but are removed as they are factually incorrect, based on misunderstanding, or violate the review guidelines.

- **"Training and test distributions both GP-generated; in-distribution evaluation."** Factually incorrect. Training uses GP-sampled functions (Matérn 5/2), but testing uses 16 standard optimization benchmark functions from the bayeso library (line 185). These are different function families, so the evaluation is at least partially out-of-distribution.
- **"ICEE merely matches the behavior of the best episodes."** The "Source" baseline is the *average* of the data-collection policy across random ε values, not the best (ε=0). ICEE matching this average is notable because the data-collection policy *cheats* (knows the goal location), while ICEE must discover it from scratch.
- **"The speed advantage is trivial."** This dismisses a genuine practical contribution. Avoiding per-iteration GP fitting is the entire point of the approach and is a meaningful efficiency gain.
- **"MGDT is a strawman."** MGDT is included to show what performance looks like *without* in-context learning (line 214), which is a legitimate baseline role.
- **"Selective reporting of ICEE-biased."** The paper explicitly states that ICEE-biased is not shown in Figs. 2a–c because it "achieves similar performance as ICEE does" (line 262). This is transparent reporting, not selective omission.
- **"AD requiring hundreds of episodes is a comparison to a different experimental setup."** The abstract refers to results reported in the prior AD paper (Laskin et al., 2023), not to a direct in-paper comparison. Citing prior results as motivation is standard practice.
- **"The paper claims AD requires hundreds of episodes but ICEE's training data still requires generating K episodes per game."** The "hundreds vs tens" claim refers to inference-time episodes needed to solve a new task, not training data generation cost. Training data generation is a one-time offline cost, not a per-task cost.
- **"Eq. 9 assumes π is the same every timestep."** The notation $\pi_k(a_{k,t}|o_{k,t})$ indexes policy per-episode $k$, with the episode subscript $k$ matching the paper's definition (line 82). This is a natural and clear formulation; no hidden assumption is made about intra-episode policy variation beyond what is stated.
- **Formatting/style nitpicks and requests for missing appendix content** that the PDF parser stripped.
- **Generic or unsubstantiated strengths** from the Strength Finder that lack specific evidence or conflict with verified weaknesses.

## Novel Insights

The most interesting observation that emerges across these reviews is the tension between the paper's theoretical framing (epistemic uncertainty drives EE) and the empirical evidence (AD-sorted nearly matches ICEE). This suggests that the cross-episode improvement signal — rather than uncertainty-driven exploration — may be doing most of the work. If this holds, the paper's most practical contribution is the multi-episode improvement-conditioned architecture and the bias-correction objective, not the uncertainty-based EE mechanism per se. This is worth stating explicitly because it reframes the contribution: ICEE is more accurately described as "in-context policy improvement via return-to-go conditioning" than "in-context exploration-exploitation via epistemic uncertainty." The unbiased objective (Eq. 9) remains a genuinely useful tool for correcting biased training data, but its connection to EE is secondary to its role in enabling effective conditioning on the improvement signal.

## Suggestions

1. **Acknowledge the known-π limitation prominently** in the abstract and introduction, and discuss when $\pi$ can or cannot be obtained in practice. This would substantially clarify the paper's scope.
2. **Add an ablation that controls for the improvement signal** — e.g., train ICEE with $\tilde{c}_k$ always set to 1 (or removed entirely) and compare to AD-sorted. If performance drops to AD-sorted levels, it confirms the improvement signal is the main driver.
3. **Compare against at least one additional BO method** (e.g., GP-UCB, entropy search) to substantiate or retract the "SOTA" claim.
4. **Report confidence intervals** for all RL results, especially given the modest number of test games (100).
5. **Directly measure epistemic uncertainty** in the model's predictions (e.g., ensemble disagreement, predictive entropy on held-out game configurations) to empirically support the theoretical claim in Section 3.

## Score and Decision

The paper proposes a clean and sensible extension of Decision Transformers to multi-episode in-context learning, with a principled unbiased training objective and an interesting theoretical motivation. However, the experimental evidence is too narrow to fully support the central claims. The RL experiments do not convincingly demonstrate that EE (rather than the improvement signal) drives performance, the BO evaluation relies on a single baseline, and the method's dependence on known behavior policies is a scope limitation that is not adequately acknowledged. The paper would benefit from substantially stronger experiments and more precise claims.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>