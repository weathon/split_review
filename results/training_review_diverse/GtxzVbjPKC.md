Now I have a thorough understanding of the paper. Let me also verify the reviewer's claim about "LA-EG combination sometimes hurts" by checking the Physical Deception table carefully.

The reviewer claims LA-EG does not improve over EG alone in Physical Deception. The table shows EG=0.56±0.27, LA-EG=0.51±0.14, and the caption says "Closer to 0.5 is better." Thus 0.51 IS closer to 0.5 than 0.56 — the reviewer's factual claim is incorrect. Let me now write the full review.

## Summary

This paper proposes applying Variational Inequality (VI) optimization methods—specifically nested Lookahead-VI (nLA) and Extragradient (EG)—to the MADDPG algorithm for multi-agent reinforcement learning. The authors introduce a VI reformulation of the MADDPG actor-critic update, present three algorithms (LA-MADDPG, EG-MADDPG, and LA-EG-MADDPG), and evaluate them on two matrix games (rock-paper-scissors, matching pennies) and two MPE tasks (predator-prey, physical deception). The key idea is that VI methods designed for non-convergent rotational dynamics in games (inspired by GAN training) may help stabilize MARL optimization.

## Strengths

1. **Clear VI formalization of the joint actor-critic update**: The paper defines the operator \(F_{\text{MADDPG}}\) (Eq. labeled F_MADDPG) that stacks the critic gradients (TD-error minimization) and actor policy gradients across all agents, casting the joint training problem as a VI. While the match is not exact (see weaknesses), this formalization provides a coherent mathematical lens and enables principled application of VI-specific optimizers.

2. **Quantitative equilibrium evaluation on zero-sum games with clear improvements**: On rock-paper-scissors and matching pennies (Fig. 1), LA-MADDPG consistently reduces the squared distance to the analytically known Nash equilibrium, whereas the Adam baseline diverges. The distance-to-equilibrium metric is more informative than reward alone, and the variance reduction from lookahead is visually evident. The baseline's eventual divergence while LA remains stable is a genuine empirical finding.

3. **Behavioral improvement in multi-agent coordination**: In Predator-prey (Fig. 2), the paper reports that LA-MADDPG produces policies where both adversary agents learn to chase the good agent (balanced participation), whereas the baseline has one adversary's policy diverge. This goes beyond aggregate reward metrics and speaks to the quality of the learned joint policy.

4. **Identifies a reward saturation pitfall**: The paper demonstrates (Fig. 3, Section 5.2) that in rock-paper-scissors, the baseline achieves near-zero average reward (correct in expectation) while producing a degenerate policy (repeatedly choosing the same action), whereas LA-MADDPG learns near-optimal action alternation despite not maximizing raw reward. This is a useful cautionary observation for the MARL community regardless of the paper's main results.

5. **Well-specified algorithms with clear pseudocode**: Algorithms 1 (nLA procedure) and 2 (LA-MADDPG) provide implementable specifications of the proposed methods, including the nested lookahead mechanism with two levels and the integration with the base optimizer.

## Weaknesses

### Fatal
None.

### Major

1. **The VI motivation is partially mismatched with the actor-critic structure**. The paper motivates VI methods using the rotational dynamics of zero-sum games (Section 1), then defines \(F_{\text{MADDPG}}\) stacking critic and actor gradients. However, the actor-critic pair within each agent is not a standard game — the critic minimizes TD-error while the actor maximizes expected return, and their coupling operates through target networks at different timescales. This is closer to bilevel optimization than a simultaneous-move game. The paper does not characterize the Jacobian of \(F_{\text{MADDPG}}\) (e.g., measure its antisymmetric component empirically or theoretically) to confirm that the rotational dynamics VI methods are designed for actually exist in this setting. Without this link, the observed improvements could stem from the averaging/smoothing effect of nLA rather than from addressing VI-specific rotational structure. This ambiguity weakens the core conceptual claim.

2. **Insufficient statistical evidence**. Only 5 random seeds are used per condition, and several reported differences fall within one standard deviation of the baseline. For example, in Physical Deception (Table 1): LA-MADDPG achieves 0.53±0.11 vs baseline 0.45±0.16, and EG-MADDPG reports 0.56±0.27 — the latter has error bars spanning nearly the entire range of plausible values. No confidence intervals, hypothesis tests, or effect-size metrics are reported. Given the well-known high variance in MARL that the paper itself acknowledges in the introduction, 5 seeds is insufficient to establish that the observed improvements are statistically significant rather than due to chance.

3. **Narrow experimental scope and minimal hyperparameter tuning**. The evaluation covers only 4 environments, two of which are trivial 2-player matrix games (RPS with 3 actions, Matching Pennies with 2 actions). The MPE benchmark is low-dimensional and not representative of modern MARL challenges. The paper explicitly states that hyperparameters for the proposed methods were not extensively tuned: "For LA, we only used α=0.5 and randomly selected a few k values" (Section 5.2). Furthermore, **no numerical values for learning rates, batch size, discount factor, soft-update parameter τ, or replay buffer size are reported anywhere in the paper**, making it impossible to assess whether the baseline is reasonably configured or to reproduce the results. The claim that VI methods yield "significant performance improvements" cannot be sustained on this evidence base.

4. **No comparison against simpler stabilization alternatives within MADDPG**. The paper compares only against vanilla MADDPG with Adam. It does not test whether simpler modifications — e.g., a smaller soft-update τ, more aggressive Polyak averaging, increased gradient steps per environment step, or larger replay buffers — achieve similar or better gains. Such ablations are necessary to disentangle whether nLA/EG provide value beyond generic stabilization. Without them, the paper cannot rule out that the observed improvements come from some form of smoothing rather than from addressing VI-specific rotational dynamics.

### Minor

1. **Target network interaction with lookahead is unexamined**. The LA update averages actor and critic parameters directly, while target networks are updated independently via Polyak averaging (Eq. 3). The paper does not discuss whether applying lookahead to the target networks as well would be beneficial or harmful, or whether this partial averaging could cause instability. This is a gap in the algorithmic analysis.

2. **Computational overhead not discussed**. EG requires an extra forward-backward pass per update (roughly 2× gradient computation), and nLA requires storing snapshot copies of all networks plus periodic averaging. The paper does not report wall-clock time, memory overhead, or parameter counts, making it difficult to assess the practical cost of the proposed methods.

3. **Unclear why VI methods should help in cooperative settings**. The paper applies LA-MADDPG to Physical Deception, which is described as cooperative (all good agents share a reward, and the adversary's reward depends only on its own policy). The rotational-dynamics motivation from zero-sum games does not obviously apply here, but the paper offers no alternative explanation for why VI methods would help.

### Trivial

1. **"Shifting" of the replay buffer is referenced in figure captions but never explained** (the buffer size and when FIFO overwrite begins are not reported), making the dotted lines in Figures 1-2 uninterpretable.

2. **The figure showing learned policies in RPS (Fig. 3)** — the right-column images showing "actions from the respective learned policies evaluation" are not well explained. The caption says "each row represents what actions players have chosen in one step of the episode" but doesn't clarify the encoding (e.g., what each color/symbol means), reducing the figure's evidentiary value.

## Nice-to-Haves

- A hyperparameter sensitivity analysis for α (e.g., {0.3, 0.5, 0.7}) and k values on at least one environment would substantially strengthen claims of robustness.
- An ablation comparing LA-MADDPG against MADDPG with a smaller τ (faster target updates) would clarify whether LA provides benefits beyond generic smoothing.
- Testing on at least one more challenging MARL benchmark (e.g., an MPE variant with 4+ agents or a SMAC scenario) would improve generalizability.
- Code release would address reproducibility concerns, especially given the sensitivity of MARL results to implementation details.

## Removed Points

- **"LA-EG-MADDPG does not improve over EG alone"** (from Critical Issue 2d): Factually incorrect. In Physical Deception, LA-EG achieves 0.51 vs EG's 0.56, and the caption states "Closer to 0.5 is better." LA-EG improves over EG alone.
- **"LA-EG combination sometimes hurts"**: For Physical Deception, as shown above, this is incorrect. For RPS (Fig. 1a), LA-EG tracks between LA and EG — better than EG and baseline but worse than LA alone. This is not a "hurt" relative to the baseline and is consistent with the higher-capacity method (nLA on top of EG) being more complex.
- **"We did not achieve full convergence... undercuts the claim of improvement"**: The paper is transparent about this limitation. Showing improvement over baseline without full convergence is entirely valid; the criticism misinterprets the nature of empirical ML research.
- **"The paper does not credit or compare to existing MARL research that already uses similar stabilizers (MAPPO, HATRPO)"**: These are fundamentally different on-policy algorithms with trust-region constraints, not optimization wrappers for off-policy MADDPG. Comparing against them would be a different paper with a different scope. The underlying concern (simpler MADDPG variants) is kept as **Major Weakness #4** above.
- **Criticism about Figure 6 (Fig. 3) being "poorly described"**: The caption actually explains the encoding ("each row represents what actions players have chosen in one step of the episode"). The reviewer overstated the clarity issue; however, the specific encoding/colors are not explained, so this is kept as a Trivial point.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an observation that the paper itself misses — the main value from the review process is the identification of the methodological gap between the VI motivation and the actual actor-critic structure, which the paper does not address.

## Suggestions

1. **Ground the VI connection empirically**: Compute and report the antisymmetric component of the Jacobian of \(F_{\text{MADDPG}}\) during training (e.g., \(\|F(\mathbf{z}) - \nabla \Phi(\mathbf{z})\|\) where \(\Phi\) is a potential function). This would directly test whether rotational dynamics are present and whether LA/EG reduce them — turning the VI motivation from an analogy into measurable evidence.

2. **Expand the experimental base**: Increase seeds to at least 20, report 95% confidence intervals or bootstrap tests, and report the numerical values of all hyperparameters used (learning rates, batch size, τ, γ, buffer capacity). Add at least one environment with more agents (e.g., MPE with 3+ adversaries, or a simple SMAC scenario).

3. **Add a critical ablation**: Compare LA-MADDPG against MADDPG with a reduced τ (e.g., 0.001 instead of 0.01) and against MADDPG with 2× or 5× gradient steps per update. If LA still improves over these variants, the case for VI-specific benefits is much stronger.

4. **Characterize the regime where each method excels**: Present learning curves with shaded error regions for all methods, and state which version (LA vs EG vs LA-EG) is recommended for which type of interaction structure (fully competitive, fully cooperative, mixed).

## Score and Decision

The paper asks a well-motivated question and introduces a clean algorithmic idea. The VI formalization is a useful framing, and the preliminary results on zero-sum games are suggestive. However, the experimental evidence is too thin to support the claimed conclusions: 5 seeds without statistical testing, minimal hyperparameter tuning (with the paper self-admitting "randomly selected a few k values"), unreported hyperparameter values for both baseline and proposed methods, and evaluation on only 4 environments (2 of which are trivial). The core conceptual link between rotational VI dynamics and the actor-critic structure is asserted but not validated. These gaps collectively prevent the paper from meeting the acceptance bar for a competitive conference venue. The idea has merit and could become a solid contribution with substantially stronger experiments and a clearer grounding of the VI connection, but the present submission is preliminary.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>