I now have all the information I need. Let me produce the final consolidated review.

## Summary

This paper identifies underestimation of the cost value function as a key cause of constraint violations during training in Constrained RL, and proposes MICE (Memory-driven Intrinsic Cost Estimation), which stores unsafe trajectories in a flashbulb-memory-inspired module and generates an intrinsic cost based on trajectory similarity to stored unsafe experiences. The combined extrinsic-intrinsic cost is used in a CPO-style trust-region optimization. Experiments on Safety Gym and Safety MuJoCo show that MICE substantially reduces constraint violations while maintaining competitive reward performance.

## Strengths

- **Empirical identification and validation of cost value underestimation in CRL.** Figure 2 directly plots cost value estimate minus true value for CPO and PID Lagrangian across multiple environments, showing systematic negative deviation. The paper also provides a formal argument (drawing on Thrun & Schwartz 2014; Fujimoto et al. 2018) connecting the minimization operation in cost value updates to underestimation bias. This diagnosis of a root cause of constraint violations is a genuine contribution to the CRL literature.

- **Consistent and significant reduction of constraint violations across diverse domains.** Experiments on four Safety Gym tasks and three Safety MuJoCo tasks (Figures 3 and 4) show that MICE achieves substantially lower cumulative costs during training while maintaining reward performance comparable to or exceeding baselines. In Safety MuJoCo, MICE achieves zero constraint violations during training. The method matches the constraint satisfaction of zero-violation methods (Saute, Simmer) while surpassing their policy performance.

- **Novel memory-driven mechanism that outperforms naive additive baselines.** The ablation study (Figure 6) compares MICE against versions that add constants (5, 10, 15) to the cost value, showing that constant addition degrades policy performance while MICE maintains both low violations and robust rewards. This validates that the memory-driven signal carries task-relevant information beyond a simple positive bias.

- **Theoretical analysis providing constraint bounds and convergence guarantees.** The paper provides a worst-case constraint violation bound for the MICE update (Theorem 2) that is tighter than CPO's bound (includes a subtractive −I term from intrinsic costs), and a convergence guarantee for the extrinsic-intrinsic cost value function under standard tabular Q-learning assumptions (Theorem 3). These represent a genuine attempt to ground the method formally.

## Weaknesses

### Fatal

None.

### Major

- **The intrinsic cost breaks the Markovian assumption of the CMDP framework used for theoretical analysis.** The intrinsic cost \(c_t^I\) (Eq. 3) depends on the entire trajectory \(\tau(t)\) up to time \(t\) via \(l_2(t) = \sum_i \|W(\tau_i^m(t)-\tau(t))\|_2\). This makes the combined cost \(c^E + c^I\) history-dependent — it is not a function of the current state-action pair alone. Yet Theorems 1–3 and Lemma 1 all rely on the standard CMDP assumption that costs depend only on the current state–action pair. The paper does not discuss this mismatch or attempt to re-frame the problem (e.g., by augmenting the state with the generator's latent representation, which would make it Markovian again). Consequently, the theoretical guarantees as stated do not formally apply to the actual algorithm. This does not invalidate the empirical results, but it does mean the theoretical contribution is overclaimed.

### Minor

- **The generator \(G_\phi\) and its integration with the trust-region update are underspecified.** The paper states that a "random projection layer" compresses trajectories into a latent space and that \(G_\phi\) is trained via regression to Eq. 3's intrinsic cost labels, but provides no architecture details, training procedure (e.g., learning rate, update frequency), or ablation. Since the intrinsic cost is the core novelty, this lack of specificity hurts reproducibility.

- **The ablation study does not fully isolate the memory mechanism.** The comparison against constant addition (5, 10, 15) tests whether the memory signal is more informative than a fixed offset, which is useful. However, no experiment removes the memory/intrinsic cost entirely and replaces it with a simple decaying exploration bonus or random signal. The comparison to CPO (which has no intrinsic cost) partially addresses this, but CPO differs in multiple respects from MICE-CPO beyond the intrinsic cost, so the comparison is not a clean ablation of the memory component alone.

- **Euclidean distance in high-dimensional state–action spaces is used without justification.** The \(l_2\) distance in Eq. 3 between concatenated state–action trajectories is a strong assumption in high-dimensional spaces (e.g., Safety Gym). No discussion of alternatives (cosine similarity, learned embeddings, etc.) or empirical comparison is provided.

- **The connection between flashbulb memory and the specific form of Eq. 3 is high-level.** The paper motivates the approach with the cognitive concept of flashbulb memory but does not operationalize the connection beyond the general idea of "storing unsafe experiences." The specific choices (L2 distance, sigmoid scaling, discount \(\gamma_I^k\)) are not derived from or justified by the cognitive analogy.

### Trivial

- The number of random seeds (6) is standard but modest for the variance shown in some environments; more seeds would increase confidence.

- The sensitivity analysis for memory capacity (Figure 7c,d) tests only three values (16, 32, 64), which is a narrow range.

## Nice-to-Haves

- A comparison against a learned similarity metric (e.g., a small neural network embedding trained to predict trajectory similarity) would strengthen the justification for using Euclidean distance.
- Providing the generator architecture details (layers, activations, training frequency) in an appendix would improve reproducibility.
- A clearer statement about whether the method is used primarily on-policy (via CPO trust regions) or whether the Q-update (Eq. 6) is also intended for off-policy use would resolve reader confusion.

## Removed Points

These points are flagged for removal, treat them with caution:

- **"The advantage function uses V_C instead of V_C^{EI} causing inconsistency"** (Harsh Critic Issue #3). This is factually incorrect. Lemma 1 intentionally relates \(J_C^{EI}(\pi')\) to \(J_C(\pi)\). Using \(V_C^\pi\) in \(A_C^{EI}\) is mathematically correct: the telescoping sum \(\mathbb{E}[\sum \gamma^t (c_t^E + c_t^I + \gamma V_C^\pi(s_{t+1}) - V_C^\pi(s_t))]\) collapses to \(J_C^{EI}(\pi') - J_C(\pi)\). The harsh critic misread this derivation.

- **"The Q-update is underspecified for off-policy learning / replay buffer"** (Harsh Critic Issue #2, as a fatal flaw). The experiments use MICE-CPO, which is an on-policy trust-region method (based on CPO). The Q-update (Eq. 6) is a conceptual illustration of the extrinsic-intrinsic value function, not the actual training algorithm used in experiments. The off-policy concern does not apply to the implemented method.

- **"No ablation removes the memory component entirely"** (Harsh Critic, Missing Experiments). The paper compares MICE against CPO, which has no memory component. CPO serves as the de facto "no memory" baseline. A dedicated controlled ablation would be nice-to-have but the absence is not a weakness — the comparison is already made.

- **"The underestimation claim is supported only by two baselines"** — Figure 2 shows CPO and PID Lagrangian, two of the most representative CRL methods, across multiple environments. This is sufficient empirical evidence for the claim.

- **"Theorem 3 uses tabular assumptions but experiments use neural networks"** — This is standard practice in RL theory (Q-learning convergence proofs use tabular assumptions). All cited works (Thrun & Schwartz, Fujimoto et al.) do the same.

- **"Adding constants to the cost is equivalent to changing the constraint threshold"** — This is incorrect; the constant is added to the cost value function target (Eq. 6), not to the constraint threshold \(d\). The two are not equivalent; changing the update target affects learning dynamics differently from changing the constraint.

- Pure formatting/style nitpicks and reproduction concerns about missing appendices/proofs (the PDF parser strips these; they exist in the original submission).

## Novel Insights

The most interesting observation emerging from the reviews is that the paper identifies a precise mechanism — underestimation bias in cost critics — that previous CRL work has largely overlooked despite its practical importance. Most prior work focuses on optimization stability or constraint satisfaction guarantees at convergence, but MICE demonstrates empirically that the *learning process* itself introduces systematic bias in cost estimates that leads to avoidable violations. The flashbulb-memory analogy, while not deeply operationalized, provides a fresh cognitive grounding for why retaining and comparing against past unsafe experiences can correct this bias. The theoretical gap around the non-Markovian intrinsic cost suggests an actionable direction: reformulating MICE as operating in an augmented state space (including the trajectory embedding from the generator) would restore the CMDP assumptions and clean up the analysis.

## Suggestions

1. **Address the non-Markovian issue explicitly.** Either (a) augment the state with the generator's latent embedding (making the combined cost a function of the augmented state and thereby restoring the Markov property), or (b) restructure the theoretical analysis around a POMDP or history-dependent reward/cost framework. In either case, clearly state the assumptions under which Theorems 1–3 hold.

2. **Provide full generator architecture and training details.** Specify the number of layers, activation functions, latent dimension, learning rate, update frequency relative to policy updates, and a qualitative example showing similarity scores between trajectories.

3. **Add a cleaner ablation.** Include an experiment that uses a simple decaying bonus (e.g., \(c^I_t = \alpha / (t+1)\)) as the intrinsic cost, to test whether the trajectory-memory mechanism specifically is needed or whether any decaying exploratory cost signal would suffice.

4. **Justify or replace Euclidean distance.** Provide an empirical comparison between L2 distance and cosine similarity or a learned embedding for the trajectory comparison in Eq. 3.

5. **Clarify the relationship between the Q-update (Eq. 6) and the trust-region optimization (Eq. 9).** State explicitly whether Eq. 6 is used in the implementation or only as motivation, and if used, describe how the Q-target is computed from on-policy trajectory data.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>