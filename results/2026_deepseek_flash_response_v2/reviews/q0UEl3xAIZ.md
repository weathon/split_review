## Summary

This paper applies Goal-Oriented Environment Inference (GOEI), a Bayesian state-abstraction method previously validated on abstract environments, to the competitive card game "Hol's der Geier" (a five-card variant). It demonstrates that GOEI compresses 15,542 game observations down to 452 states (2.9% of the original space) while achieving a median reward rate of -0.010 against the Nash equilibrium opponent — practically comparable to the NE-vs-NE baseline of 0.000 and far outperforming tabular Q-learning (-0.079). The paper also analyzes which game features are preserved vs. discarded through mutual information and provides a systematic hyperparameter sensitivity study.

## Strengths

1. **Quantified, dramatic state reduction while maintaining near-optimal performance**: Table 1 and Section 4.1 show that GOEI reduces the observation space from 15,542 to 452 representative states (97.1% compression) while achieving a median reward rate of -0.010 against the NE opponent. This simultaneously demonstrates extreme compression and competitive performance in a realistic game — a direct extension and validation of GOEI beyond prior abstract-environment results (Takahashi et al., 2024). The compression is achieved via a principled Bayesian Occam's razor (Dirichlet process prior penalizes overly complex models).

2. **Principled theoretical foundation**: The Dirichlet process prior combined with variational Bayesian inference (Section 3.2) naturally penalizes models with more states when predictive performance is equivalent (higher ELBO for fewer states), meaning the 2.9% compression emerges from a well-founded model-comparison criterion rather than ad-hoc thresholding. This gives the method a principled advantage over heuristic state-aggregation approaches.

3. **Systematic outperformance of alternative methods**: Every GOEI configuration in Table 1 achieves a better median reward rate than every Q-learning configuration (best QL: -0.079; worst GOEI: -0.073). Learning curves in Figure 2A show GOEI reaches asymptotic performance far more rapidly. The gap is substantial across all hyperparameter settings.

4. **Interpretability analysis through mutual information**: Section 4.2 and Figure 3 analyze which of the five game features (SD, CT, AH, OH, RT) are preserved or discarded in the reduced states, finding that CT and RT are relatively preserved at early rounds, SD becomes relevant only at round 4, and AH/OH are almost completely reduced — a pattern consistent with the game's strategic structure. This begins to address the paper's stated goal of improving explainability.

5. **Thorough hyperparameter sensitivity analysis**: Section 4.3 systematically varies both the Dirichlet process concentration parameter α and the Dirichlet prior β, providing practical guidance with intuitive explanations for each parameter's effect, backed by data in Figure 4.

## Weaknesses

### Major

None — the weaknesses identified below are genuine but addressable; none invalidate the core finding that GOEI achieves dramatic state compression.

### Minor

1. **Training data includes the optimal opponent, making the near-optimal result partially expected**: GOEI trains on games of Rand vs. NE and is evaluated against the same NE strategy (Section 3.3). The training observations contain the NE opponent's complete behavior; a model learned from such data, when used for planning against the same opponent, should naturally yield near-zero expected reward (the NE-vs-NE result). The paper acknowledges this limitation in Section 5 but does not test whether GOEI can learn effective states from data lacking the NE strategy (e.g., Rand vs. Rand or Rand vs. π₀). The core state-reduction contribution (97% compression) remains valid regardless, but the claim that GOEI "achieves a nearly optimal strategy" is partly a consequence of the favorable training setup rather than purely the state-reduction mechanism.

2. **Tabular Q-learning is a weak baseline that does not isolate GOEI's specific contribution**: The comparison against tabular Q-learning on the full 15,542 observation space is informative but limited. Tabular Q-learning is well-known to fail on large discrete state spaces with sparse coverage. A more competitive baseline — Q-learning with state aggregation, linear function approximation, or a small neural network — would better isolate GOEI's specific Bayesian state-reduction contribution from the general benefit of generalization across observations. The paper's stated conclusion ("the poor performance of Q-learning indicates that the number of observations is too large") is correct but tautological when using tabular Q-learning.

3. **Claim of "indistinguishable from optimal" lacks formal statistical support**: The paper states the reward rate is "indistinguishable from the optimal one (≃ 0)" (Section 5) without any statistical test. The best median reward rate is -0.010 with quartiles [-0.012, -0.009] lying entirely below zero across 21 seeds, which may indicate a systematic (if tiny) negative reward — the agent is consistently losing by a small margin. A confidence interval or equivalence test (e.g., TOST) is needed to substantiate the "indistinguishable" claim at the stated level of precision.

4. **Mutual information interpretation partially overreaches**: The paper observes that AH and OH are "almost completely reduced throughout the game" but then claims they are "likely to be crucial" and "the required information is maintained in complex combinations of all the features" (Section 4.2). Mutual information on individual features cannot test whether the reduced states encode complex multi-feature interactions. The paper provides no evidence (e.g., testing whether the reduced states are sufficient to reconstruct relevant feature combinations, or whether the transition model accurately predicts outcomes) for this "complex combinations" hypothesis.

5. **At round 4, GOEI uses 408 states vs NE's 69 — the asymmetry is unaddressed**: The paper highlights that GOEI uses fewer states than NE at rounds 2 and 3, but at round 4 GOEI uses nearly 6× more states (408 vs. 69, from Table 1). This asymmetry is not discussed, despite round 4 containing the majority of states. It partially complicates the overall compactness narrative.

6. **No direct evaluation of the learned transition model's predictive accuracy**: The paper evaluates only the policy derived from the model via the Bellman equation, never directly measuring how well the learned transition probabilities P(s_{t+1} | a_t, s_t) predict actual outcomes. This is a missing sanity check that would validate that the reduced states genuinely capture meaningful game dynamics.

### Trivial

7. **The abstract's 2.9% figure uses the restricted observation count (15,542) rather than the full 28,477 possible observations**: While Section 3.3 explains the restriction (action sequences never caused by the NE strategy), the abstract does not clarify this. Readers may misinterpret the baseline.

8. **No concrete examples of what the learned states represent**: The paper reduces 15,542 observations to 452 states but provides no examples of which observations map to the same state, which would strengthen the explainability claims.

## Nice-to-Haves

- Test GOEI trained on data without NE (e.g., Rand vs. Rand or Rand vs. π₀) and evaluate against NE to decouple state-reduction quality from the presence of the optimal opponent in training data.
- Add a stronger baseline (Q-learning with tile coding, linear function approximation, or a small neural network) to more clearly isolate GOEI's specific contribution.
- Report a formal equivalence test (TOST) or confidence interval for the reward vs. zero claim.
- Directly evaluate the predictive accuracy of the learned transition model.
- Discuss the round-4 state asymmetry (GOEI 408 vs NE 69) explicitly.
- Provide qualitative examples of observations that map to the same reduced state.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a formal equivalence test for the reward rate relative to zero to substantiate the "indistinguishable from optimal" claim.
2. Include a more competitive baseline (function-approximation Q-learning) to provide a meaningful comparison that isolates GOEI's state-reduction mechanism.
3. Test GOEI with training data that does not include the NE opponent, demonstrating that state-reduction quality is not contingent on observing the optimal opponent.
4. Directly measure the predictive accuracy of the learned transition model as a sanity check.
5. Discuss the round-4 state count asymmetry and provide concrete examples of which observations map to the same reduced state.

## Calibration

**Round 1 (Bracketing):** Three queries on state abstraction / model-based RL / card games returned anchors spanning the full score range. The weak anchors (avg 1.67-3.00) were clearly inferior — poorly executed or trivial game applications. The strong anchors (avg 8.00) were theoretically rigorous, state-of-the-art papers in game-solving (DDCFR, tractable MARL via behavioral economics). The middle anchors (avg 4.00-5.75) were the most relevant comparison set. **Round-1 bracket: 4.0–6.0.**

**Round 2 (Narrowing):** Two queries pulling more anchors inside (3.5, 6.0) and (4.5, 7.0) confirmed the bracket. Full reviews were read for:
- **KrwEmd (avg 4.00)** — hand abstraction for poker; criticized as incremental and dependent on unpublished work. This paper is clearly stronger (novel, well-executed, with a real game and concrete compression numbers).
- **Abstract World Models (avg 4.75, Reject)** — theoretical state abstraction with simple navigation experiments; criticized for weak baselines and simple environments. Comparable in overall quality; this paper has more concrete empirical results but less theoretical depth.
- **RL Algorithms as Info-State Policies (avg 5.25, Reject)** — theoretical RL paper with mixed reviews (8,3,5,5); no experiments. Hard to compare directly, but this paper's applied contribution is more immediately verifiable.
- **RL-CFR (avg 5.25, Reject)** — action abstraction for HUNL poker with strong empirical results (beats ReBeL, Slumbot); rejected for lacking theory/optimality analysis. This paper is comparable: weaker baselines but cleaner scientific framing (principled Bayesian approach, explicit compression quantification).
- **EVPA (avg 5.75, Accept)** — online pruning/abstraction for poker with strong results against DeepStack. Stronger empirical scope.

**Final assessment:** This paper sits between the 4.75 (Abstract World Models) and 5.25 (RL-CFR) anchors — better than the former (more concrete, real-game results) and slightly weaker than the latter (less ambitious game, weaker baselines). The paper has genuine contributions (dramatic, principled state compression in a real game) but is held back by the favorable training setup (NE in training data), a weak baseline comparison, and insufficient statistical rigor for the "indistinguishable" claim.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>