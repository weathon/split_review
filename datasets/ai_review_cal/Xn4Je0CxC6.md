- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3
Now I have all the evidence I need. Let me produce the final consolidated review.

## Summary

This paper proposes LRRL, a method that uses an Exp3 adversarial bandit to dynamically select the learning rate during deep RL training. The bandit receives feedback based on the agent's cumulative returns, and the arm probabilities are updated via a time-decayed weight mechanism. Experiments with DQN on Atari games show that LRRL can match or exceed the performance of oracle-tuned single learning rates and individual exponential-decay schedulers, while using a single run instead of multiple tuning runs.

## Strengths

- **Well-motivated problem with a clean approach.** The paper correctly identifies that fixed LR schedulers are poorly suited to RL's non-stationary objective (Section 2, lines 16–20). Using an adversarial bandit that adapts based on policy performance is a conceptually neat solution, and Algorithm 1 provides a clear implementation. The method is straightforward enough to be practical.

- **Positive results against a strong (oracle) baseline.** Table 1 shows that a single LRRL run with 5 arms matches or exceeds the *best single learning rate* (tested individually) on Breakout (LRRL 253 vs. DQN 217) and Seaquest (LRRL 6 799 vs. DQN 5 881), while remaining competitive on Asteroids and Pong. Comparing against the oracle-tuned LR rather than a default is a strong test — it demonstrates that LRRL can save the cost of grid search.

- **Impressive gains over individual schedulers on several games.** Table 2 shows LRRL with scheduler arms substantially outperforms each individual exponential-decay scheduler on Breakout (233 vs. 151) and Seaquest (13 864 vs. 6 612). These are sizeable improvements.

- **Optimizer-agnostic test with two optimizers.** Table 3 tests LRRL with both Adam and RMSProp-M on three additional games (Asterix, Ms. Pacman, Space Invaders), showing that LRRL with Adam outperforms both DQN-Adam and DQN-RMSProp-M. This partially supports the claim of general applicability across optimizers.

## Weaknesses

### Fatal
None.

### Major
None that threaten the core claims. See Minor section for important limitations.

### Minor

- **No comparison against existing adaptive LR methods.** The related work (Section 2) discusses ADAMBS, IDBD (Sutton, 1992), and meta-gradient RL (Xu et al., 2020), all of which adapt learning-related parameters during training. None of these are used as baselines. Without an experimental comparison, the reader cannot judge whether LRRL adds value over the closest prior approaches or whether a simpler method like IDBD would achieve similar results.

- **No ablation of the bandit design choices.** The weight update in Eqs. (1)–(2) deviates from standard Exp3: it adds a decay factor δ, a step-size α, and divides the feedback by exp(wₙ(k)). The feedback is also transformed into an "improvement in performance" f'ₙ (raw return minus running average). None of these design choices are ablated. The paper does not compare against standard Exp3, ε-greedy over arms, or UCB. Consequently, it is unclear whether the performance gains come from the bandit framework itself or from these specific (and somewhat ad-hoc) modifications.

- **Evaluation scope is narrower than the claims.** The abstract and introduction (line 22) describe LRRL as "algorithm-agnostic," but the method is only tested with DQN (a single value-based algorithm) on 7 Atari games. No policy-gradient method (PPO, A2C) is evaluated. The empirical scope supports claims about DQN with different optimizers, but not the broader "any optimizer" or "deep RL" generality asserted in the text.

- **"DQN" baseline means different things across tables without clear explanation.** In Table 1, DQN is the oracle best single learning rate (Figure 2 caption: "the DQN algorithm reaching the best performance among possible learning rates"). In Table 2, the DQN column is Adam without LR decay with initial LR 6.25×10⁻⁵ — a different baseline. Both choices are individually reasonable, but the column header "DQN" is ambiguous and the paper never explains that these are different configurations. This forces the reader to reconstruct the experimental setup from context.

- **No statistical significance testing.** The Table 1 caption claims results are bolded *"if significantly better than others"* but no statistical test (e.g., bootstrapped confidence intervals, paired test) is reported. Several comparisons have heavily overlapping standard deviations (Asteroids in Table 1, Video Pinball in Table 2, Asterix in Table 3), making it unclear whether the observed differences are reliable.

- **Bandit hyperparameters not reported.** The paper defines several LRRL-specific hyperparameters (α, δ, j, λ, κ) but never states their numerical values in the main text. These may be in a missing appendix; if so, the parser stripped them. As presented, this is a reproducibility gap. Additionally, no sensitivity analysis for these parameters is provided.

### Trivial

- **RMSProp-M results are mixed.** In Table 3, LRRL with RMSProp-M underperforms DQN without LRRL in two out of three games (Asterix: 6 499 vs. 11 464; Ms. Pacman: 2 696 vs. 3 301). The paper acknowledges this ("underperforms... due to its slow convergence") but offers no investigation. This limits confidence in LRRL's optimizer-agnostic claim.

## Nice-to-Haves

- A comparison against a simple hand-tuned cosine or linear decay schedule would strengthen the claim that adaptivity to *performance* (rather than just step count) matters.
- Extending the evaluation to a policy-gradient algorithm (e.g., PPO on MuJoCo) would substantially broaden the empirical support for the claimed generality.
- Reporting learning curves with confidence bands (not just max averages) would help readers assess when LRRL pulls ahead or falls behind.

## Removed Points

These points were flagged by the harsh critic but are removed or demoted after cross-checking against the paper:

- **"DQN baseline is an oracle, not a practical baseline" (removed).** The critic claims this comparison is problematic. On inspection, comparing LRRL against the *best* single learning rate (Table 1) is a strong, informative baseline — it directly demonstrates that LRRL saves the user from needing to know which LR works best. The paper also reports non-oracle baselines (Table 2: Adam without decay). The criticism misinterprets the purpose of this comparison.

- **"Inconsistent baselines across tables" (demoted to Minor: ambiguous labeling).** The different DQN values across tables are not an inconsistency; they reflect different experimental setups (LRRL with different arm sets vs. LRRL with schedulers). The real problem is unclear labeling, not an experimental flaw that "undermines every cross-table claim."

- **"Figure 2 raises question about hand-tuned decay schedules" (removed).** Table 2 already compares LRRL against three exponential-decay schedules. The suggestion that a hand-tuned schedule might do as well is speculation unsupported by the data.

- **"Strengthening section — fix baseline inconsistency" (removed, subsumed).** The baseline labeling issue is already covered under the Minor weakness above. There is no inconsistency to "fix"; the paper should clarify the labels.

- **Strength Finder: "novel adaptive learning-rate selection" (kept but subsumed into Strengths).** This is accurate.

- **Strength Finder: generic strengths about "important problem" (removed as generic/superficial).**

- **All formatting, appendix, related-work, reproducibility nitpicks not verified from the paper itself were removed per instructions.**

## Novel Insights

The reviews collectively surface a recurring tension: the paper presents a practical, well-motivated method and shows it works on concrete games, but does not dig deep enough to identify *why* it works or whether the specific design is necessary. The harsh critic's structural observations (missing ablations, absent comparisons to related adaptive methods) and the strength finder's evidence of actual improvements converge on the same conclusion: the concept is sound and the headline results are promising, but the contribution is not yet sufficiently isolated from alternative explanations to be considered a strong advance. The most interesting open question — whether LRRL's performance-inspired bandit feedback fundamentally differs from what a well-tuned decay schedule or a simpler Exp3 variant would produce — remains unanswered by the paper as presented.

## Suggestions

1. **Clarify what "DQN" means in each table.** Add a footnote or parenthetical: "DQN with best single LR (Table 1)" and "DQN with Adam, fixed LR 6.25×10⁻⁵, no decay (Table 2)."
2. **Add an ablation comparing LRRL's custom weight update against standard Exp3 and ε-greedy.** This directly addresses whether the specific design matters.
3. **Add an experimental comparison against at least one related adaptive method** (e.g., meta-gradient RL or a hand-tuned IDBD variant) to contextualize LRRL against prior work rather than just describing it.
4. **Report statistical significance** (e.g., 95% bootstrap CIs) for the main comparisons, especially where error bars overlap.
5. **State all LRRL hyperparameters** (α, δ, j, λ, κ) and ideally provide a sensitivity study.
