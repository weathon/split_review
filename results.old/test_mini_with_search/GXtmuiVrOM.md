Now I have sufficient context. Let me produce the final consolidated review.

---

## Summary

This paper introduces DORAEMON, a method that automatically shapes the training distribution over dynamics parameters in Domain Randomization by maximizing the entropy of the distribution subject to a constraint that the policy's probability of success remains above a threshold α. The approach uses importance sampling to estimate success rates under candidate distributions without additional rollouts, a KL constraint for stability, and a backup optimization to recover from constraint violations. Experiments on six simulated MuJoCo tasks and a real-world 7-DoF robotic pushing task (PandaPush) show that DORAEMON consistently achieves better or faster convergence in global success rate and higher training-distribution entropy compared to Fixed-DR, LSDR, and AutoDR baselines.

## Strengths

- **Novel constrained-optimization formulation (Eq. 3)** — Framing DR distribution selection as entropy maximization under a success-rate constraint is a principled departure from prior work. Unlike LSDR (which requires a reference distribution) and AutoDR (confined to uniform boundary-based updates), the formulation directly captures the trade-off between diversity and policy viability. The paper cleanly motivates why maximizing entropy subject to a success constraint is the right objective.

- **Efficient distribution updates via importance sampling** — DORAEMON reuses training data for distribution updates via IS (Eq. 6), requiring "no additional environment interactions… besides episodes naturally experienced at training time" (line 35). The backup optimization (Eq. 7) provides a recovery mechanism when the IS estimate overestimates success rates. This efficiency advantage over LSDR (which requires frequent Monte-Carlo policy evaluations) is empirically demonstrated.

- **Consistent improvement across six simulation tasks (Fig. 2)** — DORAEMON achieves higher global success rates on the maximum-entropy distribution ν_max than LSDR, AutoDR, and Fixed-DR across all six MuJoCo environments, while reaching higher training-distribution entropy. The HalfCheetah 2D heatmap (Fig. 3) further shows DORAEMON solving the task over the widest range of dynamics parameters.

- **Successful sim-to-real transfer with 17-dimensional dynamics (Tab. 1, Sec. 5.3)** — On the PandaPush task, DORAEMON achieves 90% real-world success, compared to LSDR 80%, AutoDR 70%, Fixed-DR 20%, and No-DR 0%. This is the most demanding validation and directly demonstrates practical value on a task where LSDR scales poorly and AutoDR is data-inefficient.

- **Hyperparameter and success-threshold analysis (Fig. 4)** — The paper systematically studies the effect of α and how DORAEMON tracks different success thresholds J_LB, showing predictable behavior and controllable trade-offs between performance and generalization. This goes beyond typical sensitivity analysis.

- **Illustrative toy problem with known ground truth (Sec. 4.2)** — The inclined-plane example provides an interpretable validation where the feasible parameter range is analytically known. DORAEMON correctly identifies the feasible range regardless of α, building confidence before scaling to complex tasks.

## Weaknesses

### Fatal
None.

### Major

- **Critic conditioning across methods is not explicitly stated.** At line 128, the paper says DORAEMON "additionally condition[s] the critic network with the true dynamics parameters, as in \cite{peng2018sim, akkaya2019rubik}." It does **not** state whether the baselines (LSDR, AutoDR, Fixed-DR, No-DR) also use the same critic conditioning in the reported experiments. If DORAEMON is the only method benefiting from this privileged information, the comparison conflates the effect of the distribution-shaping mechanism with the effect of critic conditioning. This is a significant omission: the paper must explicitly confirm that all methods share the same RL algorithm (SAC), network architecture, and critic conditioning. Without this clarification, the reported gains cannot be cleanly attributed to DORAEMON's entropy-maximizing distribution update. I note that AutoDR (Akkaya et al.) is itself a source of the critic conditioning trick, so it is plausible that the AutoDR baseline also uses it, but the paper never states this, and for LSDR and Fixed-DR it is even less clear. This must be clarified in the rebuttal.

### Minor

- **No diagnostics on importance sampling reliability.** The success-rate constraint is approximated via IS (Eq. 6). In the PandaPush environment with 17 randomized parameters, IS weights can become degenerate if distributions diverge. The paper acknowledges potential overestimation and introduces a backup optimization (Eq. 7) but provides no analysis of IS effective sample size, no diagnostics on when estimates are reliable, and no empirical study of how often the backup triggers or successfully recovers feasibility. While not fatal (the method still works well in practice), a basic ESS analysis for one environment (e.g., HalfCheetah) would meaningfully strengthen confidence in the constraint enforcement.

- **Degradation in Walker2D and Swimmer tasks.** The paper acknowledges (line 262) that "the degradation in performance over time in the Walker2D and Swimmer tasks is likely due to the agent's exposure to harder/infeasible parameters, which destabilize training." The mitigation (tracking the best policy) is standard practice, but the degradation suggests the method can exhibit instability on certain tasks. The final (not best) global success rates are not reported, so it is unclear how severe the degradation is relative to the best-policy numbers shown. Reporting final performance alongside best performance would give readers a more complete picture.

### Trivial

None.

## Nice-to-Haves

- A controlled ablation of DORAEMON *without* critic conditioning would cleanly isolate the contribution of the entropy-maximizing distribution update from any benefit of the privileged critic input. This is the single most informative experiment the authors could add.
- Effective sample size (ESS) diagnostics for the IS estimator during training, even for one environment, would increase confidence in the constraint evaluation.
- Reporting final (not just best) global success rates for all Sim2Sim tasks would clarify the practical impact of the degradation observed in Walker2D and Swimmer.

## Removed Points

These points were raised by one or more reviewers but are removed with justification:

- **Missing table data (PandaPush numbers).** The harsh critic noted that table data is a "placeholder command" (`\input{03_tables/sim2real_results}`). This is a parser artifact — the table content was in an external file not merged during extraction. The actual submission contains the table.
- **Toy problem 1D→17D leap.** The harsh critic argued the toy problem (1D) does not address scaling to 17 dimensions. This is scope creep: toy problems are by design simplified illustrations. The paper already validates on 17D (PandaPush). The leap is addressed by the actual experiments.
- **Backup optimization description as incomplete.** The harsh critic claimed it is "not specified how this guarantee is achieved." The paper explains at lines 139–144 that the backup finds "a sufficiently close distribution that has maximum (approximated) in-distribution success rate" via Eq. 7. The paper does not claim a formal guarantee — it describes a heuristic that "we observed… to be crucial." The description is adequate for an empirical paper.
- **LSDR implementation question in high dimensions.** The harsh critic asked whether LSDR was approximated. The paper directly addresses this at line 313: LSDR's Monte-Carlo estimation "grows exponentially with the number of randomized dynamics," explaining the higher variance. No further clarification needed.
- **"Fatal" classification of critic conditioning concern.** The harsh critic classified this as a rejection-level issue. As argued in the Major weaknesses section above, it is a significant omission but not fatal — it can be resolved through clarification or a controlled ablation. The paper's core contribution (entropy-constrained distribution shaping) is not invalidated by this ambiguity.
- **Several generic "Strengthening the Paper" points** (return distribution violin plots, sensitivity analysis of ε and K) are reasonable suggestions that would improve the paper but do not rise to the level of weaknesses; they are captured in Nice-to-Haves and Suggestions.

## Novel Insights

None beyond the paper's own contributions. The reviewers' main novel observation — the critic conditioning confound — is a legitimate methodological concern about experimental reporting rather than a scientific insight about the problem itself.

## Suggestions

1. **Clarify baseline implementation details.** Explicitly state whether LSDR, AutoDR, and Fixed-DR baselines use the same SAC algorithm, the same critic architecture, and the same critic conditioning on true dynamics parameters. If some baselines do not use critic conditioning, add an ablation of DORAEMON without it.
2. **Report effective sample size (ESS) for the IS estimator** for at least one environment (e.g., HalfCheetah or Hopper) to demonstrate that the IS approximation is reliable under the chosen KL trust region ε.
3. **Report final (not just best) global success rates** for all Sim2Sim tasks to quantify the practical impact of the Walker2D/Swimmer degradation.
4. **Consider a KL constraint on the policy** (as suggested in the paper's own Limitations section, line 327) to directly address the degradation issue rather than relying on post-hoc best-policy tracking.

## Score and Decision

My final score is calibrated against the following anchor papers from the human-review corpus, identified through two rounds of retrieval:

**Round 1 (bracketing: 5.0–7.0)**
- *Statistical Guarantees for Offline Domain Randomization* (avg 6.0) — pure theory paper on DR; no experiments. DORAEMON is stronger empirically. (round 1, score range 4–7)
- *DexNDM* (avg 6.0) — sim-to-real dexterous manipulation with a controversial neural dynamics model. DORAEMON has cleaner formulation and less contested claims. (round 1, score range 4–7)
- *Manipulation as in Simulation* (avg 6.5) — depth denoising for sim-to-real. Strong results, missing baseline concern. DORAEMON is comparable. (round 1, score range 4–7)
- *Emergent Dexterity via Diverse Resets* (avg 5.0) — diverse reset framework. Limited tasks. DORAEMON is stronger. (round 1, score range 4–7)

**Round 2 (narrowing within bracket)**
- *Statistical Guarantees for Offline Domain Randomization* (avg 6.0) — see above. (round 2, score 4.5–7)
- *DexNDM* (avg 6.0) — see above. (round 2, score 5–7.5)
- *Distributions as Actions* (avg 6.0) — RL action-space framework; different topic but comparable score anchor.

DORAEMON is a genuine contribution with a clean formulation and reasonable experimental support, including real-robot validation. The main unresolved weakness (critic conditioning ambiguity) is significant but resolvable. The paper is comparable to the 6.0-level anchors above — slightly stronger on the empirical front than the theory-only ODR paper, slightly weaker on polish than Manipulation as in Simulation (6.5) due to the degradation issue and missing diagnostics. A score of 6.0 is appropriate: a solid paper with addressable weaknesses, acceptable as a poster.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>