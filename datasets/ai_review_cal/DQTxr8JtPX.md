- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 3, 3, 5
Now I have all the information needed to write the final review. Let me synthesize everything carefully.

---

## Summary

This paper studies influence quantification in multi-agent reinforcement learning. It introduces the *total impact measurement* (TIM) and *state impact measurement* (SIM) for the average-reward setting, providing approximation algorithms with convergence guarantees (Theorems 5.6, 5.9), error bounds (Theorems 5.3, 5.8), and stability analyses under policy changes (Theorem 5.11). The theoretical framework is validated in a small random environment with analytical ground truth and demonstrated qualitatively in a three-agent coin game.

---

## Strengths

1. **First provable convergence guarantees for influence measurement in average-reward MARL.** Theorems 5.6 and 5.9 provide almost-sure convergence for TIM and SIM approximation algorithms — a property absent from prior work (Kok et al., 2005; Zhang & Lesser, 2013; Wang et al., 2020, 2021), which lack formal approximation-quality guarantees. This is the paper's primary and clearest contribution.

2. **Quantitative error bounds linking Q-function approximation quality to influence estimation error.** Theorems 5.3 and 5.8 prove that TIM/SIM approximation error is bounded by twice the infinity-norm error of the underlying Q-function approximation. This provides a clean, actionable guarantee: improve the Q-estimate, and the influence estimate improves proportionally.

3. **Decentralized algorithm requiring only observable joint actions.** The TIM/SIM approximations (Equations 12, 17) need no knowledge of other agents' policies, reward functions, or transition probabilities — only observations of joint actions and the (independently learned) Q-function. This is a practical advantage over methods requiring transition-probability estimates (Zhang & Lesser, 2013) or counterfactual action probabilities (Jaques et al., 2018).

4. **Stability analysis under policy changes.** Theorem 5.11 proves continuity of TIM and SIM in the policy parameters under standard regularity conditions. This is practically important during learning when policies evolve, and is not addressed in prior influence-measurement work.

5. **Well-executed random-environment experiments with analytical ground truth.** Figures 1a–1c demonstrate monotonic convergence of TIM/SIM approximation error to zero against analytically computed values, including under dynamically evolving policies (Figure 1c). This directly corroborates the theoretical convergence results.

---

## Weaknesses

### Fatal
None. The theoretical core is sound given its stated assumptions, and the paper is transparent about where those assumptions are not met.

### Major

- **SIM — a core claimed contribution — is not evaluated in the coin game.** SIM is introduced alongside TIM in the abstract, Section 1, and Section 5.2 as a co-equal contribution that quantifies *state-dependent* influence. The coin game section mentions training a neural network for SIM (line 303), but presents *no SIM results whatsoever* in this complex environment. All coin-game analysis (Figure 2a–c) reports only TIM. Since the coin game is the paper's showcase for "complex, dynamic settings," the absence of SIM results there means a central claimed capability is empirically unsubstantiated. The random-environment SIM results (Figure 1b) are valuable but insufficient to demonstrate the method's practical utility for state-dependent influence in realistic settings.

- **The convergence guarantees (Theorems 5.6, 5.9) do not formally apply to the paper's main complex-environment experiment.** The paper explicitly states that deep SARSA "satisfies Assumption 5.4 but not necessarily Assumption 5.5" (line 303), and Assumption 5.5 (almost-sure convergence of the Q-parameter iteration) is required for the convergence theorems. This means the coin game results — which are presented as demonstrating the method's applicability to complex settings — operate outside the theoretical framework that is the paper's primary contribution. The paper acknowledges this limitation, but the disconnect between what the theory guarantees and what the main experiment demonstrates is significant. The coin game results remain *potentially* informative, but they cannot carry the weight of the paper's central claim of "reliable" detection.

### Minor

- **Coin game experiments lack ground-truth validation.** Unlike the random environment (where analytical TIM/SIM is computed and compared), the coin game results are interpreted purely qualitatively against the known penalty structure — "as anticipated," "mirroring the unique penalty structure" (line 305). This is a self-consistency check rather than a genuine validation, because the TIM estimates are being evaluated only against what the authors already know about the environment. A direct comparison against computed or simulated ground-truth values would have substantially strengthened the claims.

- **No empirical comparison with prior influence-detection methods.** The paper's claim of providing a "reliable" method for influence detection invites comparison with alternatives from the same problem space (e.g., Jaques et al., 2018; Wang et al., 2020, 2021). While the paper's primary contribution is theoretical (convergence guarantees that prior work lacks), some empirical demonstration — even a limited one on a common task — would help contextualize the practical value of TIM/SIM. As written, the empirical section validates only that the algorithms converge (consistent with theory), not that they outperform or complement existing techniques.

- **Assumption 3.2 (strictly positive policies, ergodicity) is restrictive and its practical implications are under-discussed.** The theory requires every action to have positive probability in every state. The paper uses Boltzmann policies (which satisfy this), but near-deterministic policies that emerge after learning could violate the assumption. The paper does not discuss how severely violations affect the method, nor does it provide robustness experiments. This limits readers' ability to assess the method's operational scope.

### Trivial
- The max-min formulation of the impact sample (Definition 5.1) could be sensitive to outlier Q-values; a brief discussion of alternative formulations (variance, interquartile range) and their trade-offs would be beneficial.

---

## Nice-to-Haves

- **Validate TIM/SIM against ground truth in the coin game**, e.g., by exhaustive simulation or dynamic programming under the learned near-deterministic policies, plotting approximation error over learning steps as done for the random environment.
- **Include SIM results for key states in the coin game** — e.g., SIM heatmaps for states where agent roles differ qualitatively — to demonstrate the additional information that state-dependent influence provides beyond TIM.
- **Add a deliberate experiment where Assumption 3.2 is violated (near-deterministic policies)** to assess the practical robustness of the approximations.
- **Discuss computational complexity** of the impact sample (which requires max/min over all actions of agent *i*, O(|Aⁱ|) per sample) and possible approximations for large action spaces.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The framework itself imposes no structure beyond the binary independence test."** The original critic acknowledged this "is not a weakness per se." The framework is explicitly designed as a general foundation; its generality is a feature, not a flaw.
- **"The continuity result's proof likely follows from standard continuity of stationary distributions."** This is speculative about proof difficulty, not a substantive criticism of the paper.
- **"The claim about relying only on observing actions is slightly misleading because Q-estimation needs rewards."** The TIM/SIM approximation algorithm (Equations 12, 17) genuinely only needs observed actions and the Q-function. The Q-estimation is a separate component. The claim is technically accurate as stated in the abstract.
- **Formatting/style nitpicks and speculation about appendix content.** These reflect parser artifacts or reviewer knowledge gaps, not author errors.

---

## Novel Insights

The synthesis of the reviews reveals a paper whose theoretical contribution is solid but whose empirical package falls short of the standard set by its own theory. The random-environment experiments are well-designed, directly validating the convergence results against ground truth. However, the coin game — the paper's demonstration in a "complex, dynamic setting" — operates outside the formal guarantees, validates only the more straightforward TIM (not SIM), and relies on qualitative interpretations rather than quantitative ground-truth comparisons. This creates an asymmetric weakness: the strongest evidence supports the simplest setting, while the weakest evidence accompanies the most impressive-sounding claims. Addressing this asymmetry (by adding ground-truth validation and SIM results to the coin game, and/or acknowledging the empirical gap more transparently) would substantially strengthen the paper.

---

## Suggestions

1. Either add SIM results to the coin game experiments or explicitly acknowledge that the coin game validates only TIM (not SIM) and temper the contribution claims accordingly.
2. Include ground-truth validation for the coin game (e.g., via simulation or dynamic programming for small sub-problems) to match the evidential standard set by the random-environment experiments.
3. Add a brief discussion of Assumption 3.2's practical restrictiveness — when it holds, when it does not, and what happens when it is violated.
4. Even a simple empirical comparison with one prior method (e.g., measuring correlation between TIM and influence estimates from Wang et al., 2021 on a common task) would contextualize the contribution.

---
