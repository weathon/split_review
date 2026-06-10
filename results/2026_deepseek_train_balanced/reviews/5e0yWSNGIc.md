Now I'll produce the final review.

## Summary

This paper studies the side effects of certified adversarial training (specifically SA-DDQN) on learned Q-value functions in deep RL. It provides a theoretical existence proof in a constructed linear MDP showing that the SA-DDQN regularizer can cause Q-value overestimation and action reordering, then empirically compares SA-DDQN to vanilla DDQN on Atari games, finding that SA-DDQN produces elevated Q-values, less accurate non-optimal action values, and action-ranking inconsistencies. The paper also claims to refute the Bellemare et al. (2016) action-gap hypothesis.

## Strengths

- **Clean theoretical existence proof.** Theorem 3.4 (supported by Propositions 3.2 and 3.3) formally constructs a linear MDP and proves that minimizing the SA-DDQN regularized loss can produce a parameter vector with lower loss than the true optimal parameters while systematically overestimating values and reordering suboptimal actions. This is mathematically rigorous and demonstrates that the side effects are intrinsic to the optimization objective, not implementation artifacts.
- **Novel evaluation methodology.** The performance-drop curves $\mathcal{P}_i(p)$ — measuring how policy performance degrades when the $i$-th best action is forced in a fraction $p$ of states — provide a principled diagnostic for Q-function fidelity beyond optimal-action accuracy.
- **Striking empirical finding of action-ranking inversion.** In BankHeist (Section 6.1), forcing the predicted *worst* action causes less performance degradation than forcing the predicted *second-best* action ($\mathcal{P}_w(p) < \mathcal{P}_2(p)$). This vividly demonstrates a real failure of the learned value function under adversarial training.
- **Empirical consistency with the theoretical prediction.** The observation that SA-DDQN assigns higher Q-values than vanilla DDQN while achieving similar returns (Section 6.3) is consistent with the theoretical prediction that the regularizer inflates optimal-action estimates.

## Weaknesses

### Fatal

None.

### Major

1. **The action-gap "refutation" does not hold.** Section 6.4 claims to refute Bellemare et al. (2016) by showing that SA-DDQN increases both the action gap and overestimation. However, Bellemare et al.'s hypothesis was tied to their *consistent Bellman operator* — a specific modification to the backup operator. SA-DDQN increases the action gap through a completely different mechanism (an adversarial regularizer on the Q-function). Showing that one unrelated method increases both quantities does not refute the original hypothesis about a different method. The paper's own caveat ("we hypothesize that the consistent Bellman operator may cause a decrease in overestimation for a different reason") implicitly acknowledges this. This is listed as a contribution bullet, making the overclaim significant.

2. **Claims outrun the empirical evidence.** The paper repeatedly refers to "state-of-the-art adversarially trained deep neural policies" (plural) as though multiple methods were tested, but only evaluates SA-DDQN in the main body (supplementary material is promised to cover more recent methods). The key inconsonance result (action-ranking inversion) is only discussed for BankHeist. The paper does not specify how many Atari games were tested, does not list them, and does not report per-game statistics in the text. No random seeds are mentioned — results are averaged over only 10 episodes (Section 5), and the number of independent training runs is not stated. These omissions make it difficult to assess the generality and statistical reliability of the findings. The claim that "adversarially trained deep neural policies in certain MDPs completely lose all the information in the state-action value function" (conclusion) is supported by evidence from a single game.

3. **The overestimation claim is overstated.** The paper asserts that SA-DDQN "overestimates" Q-values because it assigns higher values than vanilla DDQN while achieving similar returns (Section 6.3, "clearly demonstrates"). This is a reasonable inference but not a proof — vanilla DDQN is not ground truth, and both policies could be biased in different directions. The theoretical proof (Theorem 3.4) shows overestimation is *possible*, not that it *must* occur empirically. The evidence is consistent with overestimation but the phrasing is too strong.

### Minor

4. **Limited statistical basis.** Results are averaged over only 10 evaluation episodes (Section 5), a very small sample for Atari games known to have high within-policy variance. No training seeds are reported. The standard errors are included but with n=10 they will be wide, making quantitative comparisons unreliable.

5. **No measurement of the robustness benefit.** The paper documents costs of adversarial training (corrupted Q-values) without measuring the benefits (actual robustness against adversarial perturbations). While the paper's primary scope is about exposing hidden costs, the introduction poses question (iv) about "fundamental trade-offs," making the absence of any robustness evaluation a gap in the paper's own stated framing.

### Trivial

None.

## Nice-to-Haves

- Connect the theory more directly to experiments by checking whether SA-DDQN's learned weights show the inflated/deflated pattern predicted by Proposition 3.3.
- Report a systematic table of per-game results for all tested Atari games, indicating which games exhibit inconsonance and which do not.
- Measure actual adversarial robustness (e.g., performance under PGD attacks or certified lower bounds) to contextualize whether the documented Q-value degradation corresponds to a worthwhile or gratuitous cost.

## Removed Points

The following points from the inputs were removed or downgraded per filtering rules:

- **Missing Section 4 (Methodology):** The critic noted this section is absent from the parsed text. This is a parser artifact — the section exists in the original submission. Removed.
- **"Confusing sentence" about Ezgi (2021):** This is a parser formatting artifact (garbled reference syntax), not an author error. Removed.
- **Missing related work section:** The paper covers relevant work in Section 2 (adversarial RL background) and discusses Q-value overestimation work in Section 6.3. The critic's specific concern is not accurate. Removed.
- **Demand for more baseline methods in main body:** The paper states supplementary material covers more recent studies. Requesting all methods in the main body exceeds standard page constraints. Downgraded to Nice-to-Have.
- **Strength Finder's praise of the "refutation":** This strength conflicts with verified weakness #1 and is removed.
- **Critic's speculation about alternate explanations for inaccuracy:** The suggestion that SA-DDQN might encode "a more robust ordering" is speculation without evidence in the paper. Removed.
- **Critic's scope-creep requests for exhaustive rollouts to ground overestimation:** Downgraded — the reasonable core of this concern is retained in weakness #3, but the demand for exhaustive rollouts across all games exceeds standard practice for deep RL evaluations on Atari.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Remove or substantially weaken the action-gap "refutation" claim. The evidence does not support it, and the paper's own caveats already undermine it.
2. Scale back the plural framing ("state-of-the-art adversarially trained deep neural policies") to match the actual evidence — name the specific method tested (SA-DDQN) throughout the main body.
3. Report the number of Atari games tested, list them, and show per-game results. Add training seed information or acknowledge the limitation.
4. Qualify the overestimation claim: replace "overestimation" with "value inflation relative to vanilla DDQN" or "elevated Q-values" unless ground-truth comparisons are provided.
5. Increase the number of evaluation episodes and report results from multiple training seeds.
6. Consider adding a robustness evaluation to give readers context on whether the documented costs reflect a necessary trade-off.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>