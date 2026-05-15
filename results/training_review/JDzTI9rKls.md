Now I have all the information I need. Let me write the consolidated review.

## Summary

The paper presents Vlearn, an off-policy deep RL method that learns exclusively from a state-value function (V-function) rather than a state-action-value function (Q-function). The key idea is to use a weighted importance sampling (WIS) loss — moving the importance weight from the Bellman target to the entire squared error — combined with TRPL for policy updates and standard design choices (twin critics, weight clipping, target networks). The method is evaluated on high-dimensional continuous control tasks (DMC dog, MyoSuite myoHand) where Q-function-based methods struggle, and demonstrates strong empirical performance.

## Strengths

- **Strong empirical performance on challenging high-dimensional tasks**: Vlearn consistently outperforms SAC, MPO, PPO, TRPL, and V-trace on 38–39 dimensional action space tasks (DMC dog tasks, MyoSuite myoHand). On Humanoid-v4 (17-d actions), it achieves a 25% improvement over SAC. These results on problems where standard off-policy methods fail are practically meaningful. [Evidenced by Figures 2, 3 and accompanying text in Section 4.1]

- **Systematic ablation study confirming necessity of design choices**: Figure 4 (right) ablates the core components — no importance sampling, PPO loss instead of TRPL, no twin critics, increased importance weight truncation — showing each is necessary for stable learning. The replay buffer size ablation (Figure 4 left) further demonstrates robustness across buffer sizes. This supports the claim that transferring the WIS loss from linear to deep RL requires non-trivial design choices.

- **Principled handling of three distinct policies**: Section 3.4 correctly distinguishes between the current policy (optimized), the old policy (trust region reference), and the behavioral policy (importance sampling), storing log-probabilities alongside transitions. This avoids a common conflation in off-policy trust-region methods.

- **Theoretical motivation via Theorem 1 and bandit variance analysis**: The paper establishes that the WIS loss (Equation 4) is an upper bound on the naive importance-weighted Bellman loss (Equation 2) with the same optimum (Theorem 1), extending a known linear result to nonlinear function approximation. The bandit analysis yields closed-form estimators showing that WIS produces the self-normalized importance sampling estimator, which has well-known variance advantages over V-trace's squared self-normalized estimator.

## Weaknesses

### Fatal

None.

### Major

- **Missing TRPL+Q-function baseline prevents attribution of improvement to the V-function**: The paper combines a V-function objective with TRPL, a strong on-policy trust region method. The ablation shows that replacing TRPL with PPO degrades performance (Figure 4 right). However, no baseline combines TRPL with a Q-function critic, so it is unclear whether the performance gains on high-dimensional tasks come from (a) using a V-function instead of a Q-function, or (b) from TRPL's stability in high-dimensional action spaces. The paper's claim that "eliminating the state-action-value function facilitates a streamlined learning process" (Abstract) would be better supported by a TRPL+Q-function variant. As it stands, SAC and MPO use both Q-functions and different policy updates, confounding the two factors. This is not fatal — the overall system works — but the specific attribution claim is undersupported.

### Minor

- **Theorem 1 proof is deferred to the appendix with only a sketch in the main text, and the sketched argument (Jensen's inequality) is not obviously complete for the stated expressions**: The paper states the proof "relies on Jensen's Inequality" and is "an extension of Neumann & Peters (2008)," but the main text does not show how Jensen's inequality applies to the expression E[ρ(V − target)²] ≥ (V − E[ρ·target])² given that ρ is a weight, not a probability. The connection L_WIS ≥ L_base is the method's theoretical motivation, and the current exposition requires readers to trust the appendix. Since the paper's primary contribution is empirical, this does not invalidate the results, but the theoretical claim should be made verifiable in the main text.

- **V-trace comparison is a valid objective-level ablation but does not represent V-trace's potential with n-step returns**: The paper deliberately removes n-step returns from both Vlearn and V-trace "to eliminate any external factors" (Section 4). This is a methodologically sound choice for isolating the effect of the objective function. However, the paper's language ("V-trace fails to learn," "V-trace cannot make any meaningful progress") overgeneralizes — V-trace with n-step returns is known to work in distributed on-policy settings, and the controlled setup strips V-trace of mechanisms it was designed to use. The comparison supports the claim that the WIS objective is better suited for this specific 1-step off-policy setting, but the paper should be more measured in drawing conclusions about V-trace's general inadequacy.

- **Wide confidence intervals on some MyoSuite tasks limit per-task conclusions**: The paper honestly reports that Vlearn "does not outperform all baselines on all tasks" and aggregates via IQM. Some individual MyoSuite tasks (e.g., KeyTurn-Hard, PenTwirl-Hard) show overlapping confidence intervals across methods. The aggregated IQM advantage is clear, but per-task superiority on these harder variants is less definitive.

### Trivial

- The paper states that "naively using the WIS loss with non-linear function approximations results in poor performance" (Section 3.2) without citing prior evidence for this claim. This appears to be the authors' empirical observation; it would be helpful to note this as a finding from preliminary experiments rather than as a cited fact.

## Nice-to-Haves

- An empirical analysis of the bias-variance trade-off of the WIS estimator vs. V-trace in the full MDP setting (e.g., tracking gradient norms or value prediction variance over training) would strengthen the variance reduction claim beyond the bandit analysis.

- Reporting wall-clock time and parameter counts would quantitatively support the "streamlined learning process" and "computational efficiency" claims in the abstract and conclusion.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Criticism that the V-trace comparison is "unfair" / a "straw-man"** — The paper is transparent about its experimental design (no n-step for either method, controlling for all other components). This is a valid controlled comparison of objective functions, not an attempt to evaluate V-trace at its full algorithmic potential. The point is moved to Minor with softened language.

2. **Criticism about missing discussion of existing V-function learning attempts** — The paper adequately covers V-trace, Retrace, and Tree Backup. C51, QR-DQN, and other cited methods are Q-based and thus outside the paper's specific scope (off-policy V-function-only learning). The critic's claim that the paper is missing relevant prior work is not well-supported.

3. **Criticism that "naively using WIS loss... gives no reference"** — This is the authors' own empirical observation about why prior deep RL work avoided the WIS loss. The paper then explains the design choices required to make it work. Not a weakness.

4. **Strength Finder's claim of "Rigorous variance analysis"** — The bandit analysis is well-motivated and correct, but it is a simplified (stateless) analysis that provides intuition rather than a proof for the general MDP case. Moved to appropriate framing.

5. **Strength Finder's claim of "Reproducible evaluation"** — This is a standard expectation rather than a distinctive strength. The paper meets reasonable reproducibility standards.

## Novel Insights

The reviews surface one novel perspective not fully articulated in the paper: the WIS loss can be understood as converting the V-function learning problem into a form that is structurally analogous to Q-function learning (weighted regression against a target), but without the action-conditional input. This reframing suggests that challenges historically associated with V-function-only off-policy learning may stem not from a fundamental limitation of V-functions but from the choice of objective (target-weighting vs. loss-weighting). The paper's empirical results provide supporting evidence for this view, though the attribution to the V-function specifically (rather than to TRPL) remains unsettled.

## Suggestions

1. **Add a TRPL+Q-function baseline** to the ablation study. This would isolate whether the performance gains come from the V-function or from TRPL's policy update mechanism. Implement by replacing the V-function critic in Vlearn with a SAC-style Q-function critic while keeping TRPL for policy optimization.

2. **Provide a self-contained proof sketch of Theorem 1** in the main text, even if the full proof remains in the appendix. Showing how Jensen's inequality connects L_WIS and L_base would make the theoretical motivation verifiable without requiring readers to trust the supplement.

3. **Temper claims about V-trace** to reflect that the comparison is an objective-level ablation with 1-step returns. Acknowledge explicitly that V-trace with n-step returns (its original design) may perform differently, and that the comparison isolates the effect of importance weight placement.

4. **Add empirical variance diagnostics** (e.g., gradient variance or value estimate variance over training) comparing Vlearn and V-trace on the same tasks, going beyond the bandit analysis.

5. **Report computational overhead** (wall-clock time, parameter count, memory) to quantitatively support claims of a "streamlined" and "efficient" learning process.

## Score and Decision

The paper makes a genuine contribution by demonstrating that a V-function-only off-policy method can work well on high-dimensional control tasks where Q-function methods struggle. The empirical results are strong and the ablation study is thorough. However, the evidence does not fully disentangle whether the improvement stems from the V-function or from TRPL's stability, leaving a gap in the attribution of the method's success. The theoretical claim (Theorem 1) is deferred to the appendix with an insufficient sketch. These issues are addressable and do not invalidate the paper's core empirical contribution, but they weaken the interpretive claims.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>