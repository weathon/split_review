- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5
Now I have all the information needed to produce the final consolidated review.

## Summary

This paper proposes applying variational inequality (VI) optimization methods — specifically nested-Lookahead-VI (nLA-VI) and Extragradient (EG) — to the MADDPG multi-agent reinforcement learning algorithm. The authors introduce three variants (LA-MADDPG, EG-MADDPG, LA-EG-MADDPG) and evaluate them on rock-paper-scissors, matching pennies, and two Multi-Agent Particle Environments (Predator-prey, Physical deception). The central idea — leveraging VI solvers designed for equilibrium-finding problems to stabilize MARL training — is novel and interesting, but the execution has significant gaps.

## Strengths

- **Novel adaptation of VI solvers to MARL training**: The paper identifies an underexplored connection between the VI optimization literature (developed primarily for GANs and adversarial settings) and MARL. The three proposed algorithms (LA-MADDPG, EG-MADDPG, LA-EG-MADDPG) are clearly described with pseudocode (Algorithms 1–2) and are reproducible. This opens a new direction for improving optimization stability in MARL.

- **Positive empirical evidence on zero-sum games**: In rock-paper-scissors and matching pennies (Figure 1), LA-MADDPG consistently reduces the squared distance to the analytically known Nash equilibrium, while the baseline Adam-based MADDPG diverges. The reduction in across-seed variance is also notable and practically relevant given the well-known reproducibility challenges in MARL (cited by the authors). These results are the cleanest evidence supporting the paper's claims.

- **Insight about reward saturation as a misleading metric**: Section 5.2 and Figure 3 demonstrate that in RPS, the baseline MADDPG can achieve saturating rewards while playing suboptimal deterministic strategies (always choosing the same action, producing ties), whereas LA-MADDPG learns to alternate actions at equilibrium despite lower raw reward. This methodological observation — using distance-to-equilibrium rather than raw rewards — is a valid and useful caution for the MARL community.

## Weaknesses

### Fatal
None.

### Major

- **The "game between actor and critic" framing is overstated and undermines the theoretical motivation**: Line 223 states "Even if N=1, there is still a game between the actor and critic." This mischaracterizes the actor-critic relationship. In standard actor-critic, the critic estimates a value function to assist the actor; their objectives are aligned (both serve maximizing expected return), not adversarial. While the coupled dynamics do create a non-trivial optimization landscape, calling it a "game" (with the implication of rotational VI dynamics) is misleading and unsupported. Since the VI motivation in the paper rests heavily on rotational dynamics in zero-sum games, this overreach weakens the paper's core narrative. The paper does not provide any diagnostic evidence (e.g., spectral analysis of the Jacobian of F_MADDPG, gradient norm cycling) to show that the observed improvements actually stem from mitigating rotational components as opposed to other effects (e.g., effective learning rate reduction from averaging).

- **Experiments are too limited to support the strength of the claims**: (a) In Predator-prey (Figure 2), only LA-MADDPG is compared against the baseline — EG-MADDPG and LA-EG-MADDPG are absent, making the evaluation incomplete. (b) The paper acknowledges "minimal tuning" of hyperparameters (α=0.5 fixed, k values randomly selected) and that "we did not achieve full convergence to the Nash equilibrium with any of the algorithms" (lines 373-374). This makes it impossible to assess whether the gains reflect the methods' potential or are artifacts of specific hyperparameter choices; the baseline's tuning status is also not clarified. (c) Only 5 seeds are used and the main figures (Figure 1) do not display confidence intervals/error bands, only mean lines. The paper discusses variance qualitatively but does not quantify it visually.

- **Internal inconsistency in the Physical deception evaluation**: The paper states "This game has no 'competitive component' for the adversary: its reward depends solely on its own policy" (line 331), yet evaluates methods using adversary win rate where "closer to 0.5 is better" (Table 1, line 397: "Agents reach equilibrium when both teams win with equal probability"). If the adversary's reward is independent of the good agents' actions, there is no game-theoretic reason that 0.5 win rate corresponds to an equilibrium. The evaluation metric for this environment is not well-justified given the paper's own characterization of the game.

### Minor

- **The conclusion overstates the findings**: The paper claims the experiments "consistently demonstrated the effectiveness of the VI variants" (line 446), but the evidence is mixed: EG-MADDPG performs similarly to the baseline on RPS/matching pennies, and not all variants were tested on all environments. Results on Physical deception have overlapping standard deviations (Table 1: LA 0.53±.11 vs Baseline 0.45±.16).

- **No analysis connecting the VI rationale to observed improvements**: The paper motivates VI methods through rotational dynamics in zero-sum games but applies them to mixed-motive settings (Predator-prey, Physical deception) without empirically verifying that rotational dynamics are present in the MADDPG training of those environments. A diagnostic analysis (e.g., measuring the antisymmetric component of the Jacobian, computing gradient norms over time) would have significantly strengthened the paper's causal claims.

### Trivial
None.

## Nice-to-Haves

- A comparison with simple Polyak averaging or learning rate annealing would help isolate whether Lookahead's benefit comes from its VI-specific design or from a lower effective learning rate.
- Showing individual runs alongside means would be helpful given only 5 seeds and no error bands.
- A brief discussion of how the number of inner steps (k) between lookahead updates affects the dynamics would make the algorithm description more complete.

## Removed Points

These were flagged by reviewers but are removed from the main evaluation:

- *"The dotted lines marking 'start of shifting' of the replay buffer are not explained in the text"* — The figure captions explicitly explain this as "the start of the 'shifting' (in first-in-first-out order) of the experiences in the buffer." The critic missed this.
- *"The number of seeds (5) is modest"* treated as a major issue — 5 seeds is standard for MARL experiments of this kind. The issue is the lack of visible error bars, which is retained as a minor weakness.
- *"Criticisms about fairness of comparison due to minimal tuning"* framed as a fatal issue — the paper openly discloses its tuning limitations. It is retained as a minor-to-moderate weakness but not elevated to fatal.
- *"The claim that 'all variation methods based on gradient descent...have no hope of converging' is too strong"* — This sentence in the introduction is about VIs generally, not MARL specifically, and is a standard motivating statement in the VI literature. It is a minor rhetorical flourish, not a technical error.
- *Several of the Strength Finder's generic strengths* (e.g., "addresses an important problem," "targets an interesting question") — these are removed because they lack specific evidence tied to the paper's content.

## Novel Insights

None beyond the paper's own contributions. The core tension exposed by the reviews is that the paper attempts to borrow theoretical machinery (VI methods) designed for well-characterized problem classes (monotone operators, bilinear games) but applies it to a setting (MADDPG in mixed-motive MARL) where the problem structure is not established. The reviews collectively surface that the paper would benefit from either (a) providing empirical diagnostics that the operator F_MADDPG actually exhibits rotational dynamics, or (b) reframing the contribution more modestly as an empirical exploration of optimization stabilization wrappers for MADDPG, without the strong VI theoretical framing.

## Suggestions

1. **Provide diagnostic evidence** connecting the VI motivation to the observed results. A natural addition would be to compute the Jacobian of F_MADDPG during training, decompose it into symmetric and antisymmetric parts, and show that VI methods reduce the rotational component. This would turn a heuristic motivation into a verifiable claim.
2. **Complete the experimental evaluation** by testing EG-MADDPG and LA-EG-MADDPG on the Predator-prey environment, adding confidence intervals/shaded regions to all plots, and systematically ablating the lookahead parameters (α, k) on at least one environment.
3. **Tone down the "game between actor and critic" characterization.** The actor-critic dynamics are coupled but not adversarial. The VI framing is valid as a modeling choice (VI(F, ℝᵈ) is well-defined for any continuous F), but calling it a "game" invites confusion.
4. **Reconcile the Physical deception evaluation** with the game's stated properties. If the adversary's reward depends solely on its own policy, justify why 0.5 win rate is an equilibrium condition, or use a different metric.
5. **Add a comparison with a simple baseline** such as MADDPG with Polyak averaging of parameters or a lower learning rate, to help isolate whether the improvement is due to the VI-specific design or simply to stabilization via temporal averaging.
