Here is my synthesized final review.

---

## Summary

This paper introduces Marvel, a framework for offline-to-online (O2O) safe reinforcement learning. It identifies two specific challenges in naively transferring offline safe RL policies to online finetuning: (1) erroneous Q-estimations caused by the mismatch between offline regularized objectives and online learning, compounded by sparse cost signals in offline data, and (2) a Lagrange multiplier mismatch where offline training produces multipliers orders-of-magnitude away from what online finetuning requires. Marvel addresses these with two components: Value Pre-Alignment (VPA), which re-fits both Q-functions on the offline dataset using the online learning objective before online interaction begins, and Adaptive PID Control (aPID), which dynamically adjusts the PID gains for multiplier updates to quickly stabilize cost during online finetuning. Experiments across 10 environments show that Marvel outperforms several O2O RL baselines adapted to the safe setting.

## Strengths

- **Concrete, numerically grounded diagnosis of the Lagrangian mismatch problem.** The paper identifies a specific, measurable failure: in BallCircle, BEAR-lag produces a pretrained Lagrange multiplier of ~1500, whereas SAC-lag online requires ~0.65 (Section 3.2). This orders-of-magnitude gap turns a vague intuition into a verifiable, targeted challenge, and directly motivates the aPID design.

- **Ablation cleanly separates the contributions of VPA and aPID.** Figure 5 compares Marvel (VPA+aPID) against VPA+dual-ascent, aPID-only, and VPA+PID (fixed PID gains). The results show that: (a) VPA alone produces cost violations that take a long time to resolve, (b) aPID alone cannot overcome erroneous Q-functions, (c) VPA+PID still produces frequent cost violations near the threshold, and (d) only the full VPA+aPID combination yields fast, stable learning. The aPID-vs-PID comparison is particularly informative because it demonstrates that the *adaptive* gain adjustment matters, not just using PID control.

- **Fair baseline construction by retrofitting aPID into all competitors.** The paper states that "aPID is used to update Lagrange multipliers in all these baseline methods, which in fact already improves the performance of these methods compared to their original designs" (line 278). This prevents a common evaluation pitfall where a proposed method's advantage is actually due to a better multiplier-update mechanism rather than the full framework. By holding the multiplier update constant, the evaluation correctly isolates VPA's contribution.

- **Compatibility demonstrated with a non-safe-RL offline method.** Figure 4 shows Marvel works when the offline phase uses BEAR-lag, which was not designed for safe RL. This provides evidence that Marvel does not require a carefully tuned offline safe RL algorithm as a prerequisite.

- **Single set of aPID hyperparameters across all 10 environments.** The paper reports (line 290) that aPID parameters are fixed across environments without per-task tuning, which is a nontrivial robustness property worth noting.

## Weaknesses

### Major

None. The paper's core claims (Marvel accelerates safe O2O RL, VPA and aPID are both necessary) are supported by the end-to-end results and ablations. The issues below are addressable but do not invalidate the paper's main contributions.

### Minor

- **The Spearman correlation evidence for VPA's central mechanism is overstated.** Table 1 shows that for *random* (OOD) rollouts, VPA's improvement on cost Q-value correlation is modest — 0.1254 in CarRun and 0.3579 in BallCircle, compared with pre-VPA values of -0.2431 and -0.2521. For CarRun, a correlation of 0.1254 means the cost Q-ranking after VPA has almost no monotonic relationship with the true cost ranking for OOD state-actions. The paper claims this "clearly demonstrates the effectiveness of VPA" (line 194) without acknowledging these weak results. Since VPA is motivated as a fix for erroneous Q-estimations that would otherwise harm online exploration, the fact that its primary diagnostic metric is near-zero for the most challenging case (OOD cost estimation in CarRun) is a gap the paper should discuss. Possible mitigations (e.g., online exploration starts near the offline policy distribution, not from random states) are plausible but not presented.

- **No variance reporting in the main results.** Figure 3 shows learning curves averaged over 5 seeds but provides no error bars, confidence intervals, or standard deviations (line 273 confirms averaging only). In safe RL, where cost constraint satisfaction is the primary criterion, variance across seeds is known to be substantial. Without any measure of dispersion, the reader cannot assess whether the visible gaps between Marvel and baselines are statistically meaningful. This is a presentation gap common in RL papers but still noteworthy.

- **Single cost threshold (20) across all 10 environments.** The paper tests only one constraint regime (line 270). Safe RL methods can behave very differently when the threshold is tight versus loose (e.g., threshold 5 vs. threshold 50). Without varying \(c_{th}\), it is unclear whether Marvel's advantage generalizes or is specific to this regime.

- **The "optimistic reward, pessimistic cost" description of VPA is imprecise and potentially misleading.** The paper states VPA "optimistically estimat[es] rewards and pessimistically estimat[es] costs" (line 42-43), but then explains that the entropy term "can result in **both** higher rewards and costs for state-action pairs with high entropy" (line 166), and the difference is only in the *magnitude* of the entropy coefficient. Both Q and Qc receive entropy bonuses; the reward Q gets a larger one. This is better described as "asymmetric optimism" (more entropy for reward than cost), not "optimistic reward, pessimistic cost." The terminology suggests cost Q-values are deflated, which is not what the equations implement.

### Trivial

- **Notation confusion for the entropy coefficients.** The prose (line 166) says "the coefficient \(\alpha\) for the Qc-network lower than \(\alpha_c\) for the Q-network," but equations (5)-(6) use \(\alpha^{VPA}\) (reward Q) and \(\alpha_c^{VPA}\) (cost Q). The variable names are swapped between text and equations, creating an obstacle for readers trying to verify the asymmetry claim.

## Nice-to-Haves

- A controlled experiment isolating VPA's effect with a *fixed* (non-adaptive) Lagrange multiplier at a known good value (e.g., 0.65 for BallCircle). The ablation in Figure 5 uses dual ascent for the "VPA only" condition, which conflates VPA's effect with the adaptive properties of dual ascent. A fixed-multiplier condition would cleanly test whether VPA independently fixes the Q-estimation problem.
- A quantitative summary table reporting final mean ± std reward, cost, and violation frequency across all methods and environments, complementing the learning curves.
- Analysis of computational overhead: how many gradient updates does VPA require, and how does the total compute compare to baselines?
- Testing with varied cost thresholds (e.g., 10, 20, 40) to verify generality.

## Removed Points

- **Missing comparison with GUID / Guided Online Distillation.** The paper explicitly acknowledges GUID as the only prior O2O safe RL work (line 121) and justifies exclusion on grounds of unfair comparison due to GUID's use of GPT-2-scale models versus typical small RL policy networks (line 275). This is a reasonable scope decision, not an omission. *Removed per rule: paper already addresses this with a valid justification.*
- **Missing aPID hyperparameter values / missing appendix content.** The appendix was stripped by the parser; the original submission contains these. *Removed per rule: hard rule about appendix being stripped.*
- **Results deferred to appendix for 4 environments.** Standard space limit. *Removed per rule: appendix stripped by parser, deferring to appendix is normal practice.*
- **Baseline design concern (aPID in all baselines stacks against Marvel).** The paper explicitly explains this is intentional and notes it "already improves the performance of these methods" (line 278). The Strength Finder correctly identifies this as a design strength (fairer comparison). *Removed per rule: conflict with verifiable paper content and strength.*

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Acknowledge and discuss the weak Spearman correlations for OOD cost estimation in CarRun. Either explain why this is less concerning than it appears (e.g., online exploration initializes from the offline policy distribution, not from random state-actions), or add it as a limitation.
2. Add error bars (standard deviation or confidence intervals) to the learning curves in Figure 3. The data from 5 seeds is sufficient.
3. Clarify the entropy coefficient notation — use the same variable names in the prose (line 166) as in equations (5)-(6) to avoid confusion.
4. Reconsider the "optimistic reward, pessimistic cost" framing. The actual mechanism is asymmetric entropy bonuses, which is a more nuanced (and honest) description.
5. Add a table of final numerical results (mean ± std) for all methods and environments.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>