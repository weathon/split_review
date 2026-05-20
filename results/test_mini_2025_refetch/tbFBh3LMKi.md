## Summary

This paper proposes Uni-O4, a unified framework that uses a single PPO-style on-policy objective for both offline and online reinforcement learning, eliminating the need for extra conservatism or explicit regularization when transitioning between phases. The method comprises three stages: (1) ensemble behavior cloning with disagreement-based regularization to handle multi-modal datasets, (2) multi-step offline policy improvement via an approximate-model-based OPE method (AM-Q), and (3) standard online PPO fine-tuning. Uni-O4 achieves a total score of 1322.0 across 20 D4RL Gym, Adroit, and Kitchen tasks—the highest reported among the compared methods—and demonstrates stable online fine-tuning with real-world robot validation.

## Strengths

- **State-of-the-art offline performance across diverse domains.** Table 1 shows Uni-O4 achieves a total normalized return of 1322.0 across 20 D4RL tasks, surpassing the previous best (BPPO, 1253.4) by 5.5%. On Antmaze (Table 2), it scores 447.9 total, outperforming IQL (378.0) by 18%. This breadth of improvement across locomotion, manipulation, and navigation tasks substantiates the claim of superior offline initialization.

- **Clean, unified objective enables stable online fine-tuning without extra regularization.** Figures 3–4 show Uni-O4 fine-tunes stably from a high-scoring offline initialization, avoiding the initial performance drops seen in CQL, SAC, and Off2on (Figure 1). The V-values of Uni-O4 rise smoothly from ~20 to ~35 while baselines stagnate or drop, providing direct evidence that aligning the offline and online objectives yields stable fine-tuning.

- **OPE accuracy is empirically sufficient for guiding multi-step improvement.** Figure 6(a) shows AM-Q achieves ~80% exact accuracy and ~95% accuracy within a 20% error margin across all MuJoCo tasks, providing empirical validation that the OPE procedure can guide multi-step policy improvement without online rollouts.

- **Computational efficiency advantage.** The paper reports Off2on requires ~18 hours while Uni-O4 completes in ~30 minutes (Appendix A.12), making the approach practical for real-world robot learning where training time is a critical constraint.

## Weaknesses

### Fatal

None.

### Major

1. **The claim of guaranteed monotonic improvement via AM-Q is not supported by the provided theory.** The paper states at line 135: "Given the OPE bound, we can replace the online evaluation with AM-Q to guarantee monotonicity." However, Theorem 2 bounds only the model approximation error in AM-Q itself: |J(π, T) − J(π, T̂)| ≤ Q_max·H(H−1)/2·√(2D_KL(Tπρ ∥ T̂πρ)). This is a bound on *evaluation error* for a single policy, not a guarantee that the *difference* between two policies' evaluations (J(π_new) − J(π_old)) preserves the correct ordering. If AM-Q incorrectly ranks a worse policy as better—an event consistent with the ~20% error rate in Figure 6(a)—the behavior policy can be replaced with a worse one, breaking monotonicity. The paper does not analyze how OPE errors compound across multiple replacement steps. The empirical results are strong, so this overclaim does not invalidate the method, but the theoretical framing should be corrected to acknowledge that safety is empirical rather than formally guaranteed.

### Minor

2. **Real-world robot evaluation is limited relative to the strength of the claims.** The paper claims Uni-O4 "excels in real-world experiments... surpassing SOTA sim2real and offline-to-online methods" (line 55), but the evidence rests on a single task (walking on a latex mattress). The bar charts in Figure 5 report average returns without visible error bars (though the caption states five trials were run). The robot hardware is not specified. This is acceptable as a proof-of-concept and a welcome addition, but the claims should be softened to match the limited scope.

3. **The ratio notation in Equation 7 is inverted relative to standard PPO convention.** In Equation 7, the importance sampling ratio is defined as r(πⁱ) = πⁱ_k(a|s) / πⁱ(a|s). Standard PPO (Equation 1) uses r(π) = π(a|s) / π_k(a|s), i.e., new/old. The paper's convention reverses this. While the overall gradient direction would be correct if the implementation follows the standard convention, readers may find this notation confusing.

4. **No analysis of how false positives/false negatives in OPE affect fine-tuning.** The paper reports ~80% OPE accuracy, meaning ~20% of policy replacement decisions may be incorrect. It would be informative to analyze whether false positives (replacing with a worse policy) or false negatives (failing to replace with a better policy) dominate, and whether the method is robust to such errors. The scatter plot suggested by the reviewer (OPE accuracy vs. final score per task) would be a straightforward addition.

### Trivial

5. The axis labels and scaling of Figure 6(d) are not described in the text caption, making it hard to interpret what "Normalized Scores" refers to.

## Nice-to-Haves

- An ablation that strips the multi-step OPE stage entirely (skipping directly from ensemble BC to online PPO) would isolate the benefit of OPE-based offline improvement from the ensemble initialization.
- Reporting confidence intervals on the "total" row in Tables 1 and 2 (rather than just per-task std) would strengthen the statistical claims.
- Wall-clock breakdown for each stage of Uni-O4 (ensemble BC training, IQL fitting, dynamics model training, multi-step OPE, online PPO) would help practitioners.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Incomplete reporting of baseline online fine-tuning protocols**: The critic asked which online algorithm is used for IQL/CQL baselines. Details about baseline configurations are standard appendix content, which was stripped by the parser. This does not reflect an omission by the authors.
- **Theorem 1 not accounting for Z(s)**: The critic claimed the lower bound in Theorem 1 does not account for normalization Z(s). This is factually incorrect — Z(s) ≥ 1, so log Z(s) ≥ 0, making the claimed bound (which drops Z(s)) a valid lower bound.
- **Hyperparameter sensitivity and wall-clock times**: These are standard appendix details stripped by the parser.
- **Related work being a "list"**: A stylistic observation, not a substantive weakness.
- **Missing comparison against simpler baseline mentioned in "Strengthening the Paper"**: The suggestion to compare against "ensemble BC + direct online PPO" (skipping OPE) is a reasonable proposal, not a weakness of the current paper.
- **Criticism about halfcheetah-medium-replay not being SOTA**: No method is SOTA on all tasks; the paper claims highest *total* score, which is accurate.
- **BC baseline initialization concern for Antmaze**: The critic asked whether "filter BC" is the same initialization used by Uni-O4 — this is a question, not a confirmed weakness, and the footnote* clarifies the BC column uses filter BC while Uni-O4 uses ensemble BC, which is a deliberate design difference.

## Novel Insights

The harsh critic and strength finder largely converge on the paper's empirical strengths but diverge on the theoretical framing. The most interesting tension is the gap between the paper's claim of "guaranteed" monotonic improvement (which the theory does not actually provide) and the genuinely strong empirical results. This creates an opportunity: the paper's real contribution is demonstrating that even with an imperfect OPE (~80% accuracy), the multi-step improvement scheme works well in practice across 26 tasks. This is a *robustness* finding, not a guarantee finding, and reframing it as such would make the paper stronger. The strength finder correctly identifies that the empirical evidence (OPE accuracy at 20% error margin approaching 95%) partially bridges this gap, but neither reviewer draws the connection to the broader observation that *principled approximate OPE can be good enough for policy selection even when formal guarantees are unavailable*.

## Suggestions

1. Reframe the theoretical claims: replace "guarantee monotonicity" with an honest statement that Theorem 2 bounds OPE error from model approximation, and that the empirical results demonstrate this bound is tight enough in practice for reliable multi-step improvement. Add a limitations paragraph acknowledging the lack of formal monotonicity guarantees.

2. Add error bars or individual trial markers to Figure 5's bar charts for the real-world experiments, and specify the robot hardware.

3. Clarify the gradient computation for the ensemble BC objective (Equation 6): explain whether stop-gradient is applied to the max term during training.

4. Fix the ratio notation in Equation 7 to match the standard PPO convention (r(πⁱ) = πⁱ(a|s) / πⁱ_k(a|s)).

5. Include a scatter plot of per-task OPE accuracy vs. final offline score to assess robustness to OPE errors.

## Score and Decision

### Calibration Report

**Round 1 — Bracketing:** Three queries for similar topics (offline RL unified framework, online fine-tuning, PPO objective) with score filters:
- Weak anchors (avg < 3.5): ZK1NnjpjEs (3.0, LLM RL), 6PcJEFKvBD (2.33, OPE package), 2nrn8LRpex (2.5, SAC+BC offline), MtjPIDWyWK (3.0, action sequence planner)
- Middle anchors (3.5 < avg < 7.5): S77skzM12O (5.75, PROTO O2O), sxus3NNiuf (6.0, OPT O2O), HN0CYZbAPw (6.5, WSRL), SQnitDuow6 (5.5, RLHF)
- Strong anchors (avg > 7.5): 8BAkNCqpGW (8.0, confounded POMDPs), tPNHOoZFl9 (8.0, LLM finetuning), v593OaNePQ (8.0, search from demos), or8mMhmyRV (7.75, skill design)

**Round 1 bracket:** 4.5–7.5

**Round 2 — Narrowing:** Two queries targeting (4.0, 6.5) and (6.5, 7.5):
- In (4.0, 6.5): 228XQpErvW (4.5, ISMAQ O2O), sxus3NNiuf (6.0, OPT O2O), S77skzM12O (5.75, PROTO), 0WqAnYWi7H (4.4, UARL)
- In (6.5, 7.5): RMgqvQGTwH (7.0, hybrid on-policy NPG), dbuFJg7eaw (7.0, safe policy fine-tuning), TFKIfhvdmZ (7.0, PPO for QD-RL)

**Read in full:** S77skzM12O / PROTO (5.75) — weaker experiments, concerns about theoretical novelty; HN0CYZbAPw / WSRL (6.5) — accepted poster, strong analysis but only 8 datasets; RMgqvQGTwH / hybrid NPG (7.0) — accepted poster, strong theory but limited to comblock env; 228XQpErvW / ISMAQ (4.5) — weaker results, rejected.

**Final comparison:** Uni-O4 outperforms PROTO (5.75) and ISMAQ (4.5) empirically on every axis. It has broader experimental scope than WSRL (6.5, accepted poster) — 26 tasks vs. 8 tasks, plus real robot — with a cleaner method than OPT (6.0, rejected). The main weakness is an overclaimed theoretical guarantee, which WSRL does not have. Comparing against the hybrid NPG paper (7.0, accepted poster), Uni-O4 has much stronger empirical breadth but weaker theory. The paper lands between 6.5 (WSRL) and 7.0 (hybrid NPG), slightly closer to 6.5 due to the theoretical overclaim.

**MY FINAL SCORE: 6.5**

**MY FINAL DECISION: Accept**