- Decision: Reject
- Avg Score: 4.75
- Scores: 6, 5, 5, 3
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper presents the first finite-time convergence analysis for single-timescale actor-critic (AC) with deep neural network approximation in continuous state and action spaces under Markovian sampling. The main result establishes that the reward estimator, critic error, and actor gradient converge at rate \(\widetilde{\mathcal{O}}(T^{-1/2})+\widetilde{\mathcal{O}}(m^{-1/2})\) to a stationary point under a set of stated assumptions. The paper addresses a genuine gap in the literature, as prior single-timescale AC analyses either assumed finite action spaces, i.i.d. sampling, or linear function approximation.

## Strengths

1. **First finite-time analysis in a challenging setting.** Table 1 convincingly shows that no prior single-timescale AC analysis simultaneously handles continuous state/action spaces, deep neural network approximation, and Markovian sampling for both actor and critic. This is a non-trivial advance over prior work (Chen et al., 2021; Olshevsky & Gharesifard, 2023; Chen & Zhao, 2024; Tian et al., 2024), each of which relaxes at least two of these practical elements.

2. **Explicit convergence rate.** Theorem 4.9 provides concrete rates \(\widetilde{\mathcal{O}}(T^{-1/2})+\widetilde{\mathcal{O}}(m^{-1/2})\) for the reward estimator, critic error (\(\|z_t\|^2\)), and actor gradient norm (\(\|\nabla J(\theta_t)\|^2\)), matching the state of the art in simpler settings and showing explicit dependence on network width \(m\).

3. **Novel Lipschitz condition for continuous action spaces via total variation distance.** Assumption 4.7(c) generalizes prior finite-action Lipschitz conditions to continuous distributions using \(d_{TV}\). Proposition 4.8 demonstrates this is satisfied by a broad class of policies (truncated Gaussian, Beta, uniform) with neural-network-parameterized means — a genuine technical enabler for continuous-action analysis.

4. **Novel treatment of Markovian noise in continuous spaces.** The analysis constructs Lemma C.1 to characterize stationary-distribution distances in continuous spaces, enabling rigorous control of Markovian sampling for both actor and critic without requiring i.i.d. resampling. This is a meaningful technical contribution over prior work that assumed i.i.d. sampling for at least one component.

## Weaknesses

### Fatal

None.

### Major

1. **Assumptions 4.3, 4.4, and 4.5 are strong and their plausibility for continuous spaces with neural networks is not adequately substantiated.** These are the assumptions that make the analysis tractable but collectively represent a significant gap between the claimed "practical" setting and the conditions required by the proof.

   - **Assumption 4.5 (Exploration):** Requires a uniform spectral gap \(\langle \widehat{V}(\omega), D_\theta(I-P_\theta)\widehat{V}(\omega)\rangle \ge \lambda_2 \|\widehat{V}(\omega)\|^2\) on a continuous state space, for all policies \(\theta\) and all neural network outputs. The only justification is a contrapositive argument (insufficient exploration ⇒ assumption fails). No concrete continuous MDP is given where this condition provably holds. While the paper correctly notes that analogous "sufficient exploration" assumptions are standard in prior work (Bhandari et al., 2018; Zou et al., 2019; Wu et al., ), those prior works operate in finite state/action spaces where the spectral gap corresponds to a finite matrix; the extension to infinite-dimensional operators on \(L^2(S)\) requires additional justification that is not provided.

   - **Assumption 4.3 (Smoothness of \(\omega^*(\theta)\)):** Requires the global minimizer \(\omega^*(\theta)\) of a non-convex neural network objective to be \(L_*\)-Lipschitz and \(L_s\)-smooth in the actor parameter \(\theta\), with the gradient \(\nabla\omega^*(\theta)\) also Lipschitz. The paper cites Tian et al. (2024), but that work addresses finite action spaces. For neural networks in general, it is not obvious that the global minimizer of \(\mathbb{E}_{s\sim\mu_\theta}[(\widehat{V}(\omega;s)-V_\theta(s))^2]\) should vary smoothly with \(\theta\) — the objective is non-convex and the minimizer may be non-unique. This is critical because the coupling analysis measures \(\|z_t\| = \|\omega_t - \omega^*(\theta_t)\|\) against a moving target.

   - **Assumption 4.4 (Regularity):** Requires \(\|\widehat{V}(\omega)-\widehat{V}(\omega^*(\theta))\|\ge \lambda_1\|\omega-\omega^*(\theta)\|\) for all \(\theta,\omega\). This is a uniform lower bound on the sensitivity of the network output to parameter changes, which is known to be violated by overparameterized networks due to permutation symmetries and other redundancies (multiple parameter vectors can represent the same function). While the projection step keeps parameters near initialization, the assumption is stated globally for all \(\omega\) in the domain, which is stronger than what NTK-based arguments typically provide (local, high-probability bounds).

2. **Experiments provide only weak support for the theoretical claims.** The experiments use a single environment (Pendulum) with no baselines, no ablation studies, and no gradient norm plots that would directly test Theorem 4.9. The reported metric is average return rather than \(\|\nabla J(\theta_t)\|^2\), making the connection to the main theorem indirect. Network widths of 64–200 are not clearly in the "overparameterized" regime required by the theory (which typically needs width scaling with sample size). Confidence intervals are wide, and there is no comparison to alternative algorithms or ablations (e.g., removing the reward estimator \(\eta_t\)).

### Minor

3. **The policy gradient theorem for continuous MDPs requires regularity conditions that are not explicitly stated.** The paper invokes the policy gradient theorem (Sutton et al., 1999) via Eq. (3) without specifying the conditions (smoothness of the transition kernel, interchange of derivative and integral, etc.) needed for it to hold in continuous state-action spaces. While Assumptions 4.6–4.7 provide partial coverage, a self-contained treatment would explicitly connect these assumptions to the existence of \(\nabla J(\theta)\) in the form given.

4. **All problem constants are hidden in \(\widetilde{\mathcal{O}}\).** Theorem 4.9 does not reveal how the bound depends on the mixing time, Lipschitz constants (\(B, L_*, L_s, L_l, L_\pi\)), spectral gap (\(\lambda_2\)), or neural network depth (\(K\)). The statement "\(\widetilde{O}\) hides polynomials of all other problem parameters" is too vague to assess whether the bound is meaningful for realistic parameter ranges.

### Trivial

5. The paper's framing of being "first in continuous spaces" is technically correct but could be tempered — the result is contingent on assumptions whose verification for continuous spaces is non-trivial, which somewhat narrows the claimed advance.

## Nice-to-Haves

- Providing at least one concrete continuous MDP (e.g., a linear-quadratic regulator with a truncated Gaussian policy) where all assumptions can be verified to hold would significantly strengthen the paper.
- Including gradient norm plots in the experiments would directly support Theorem 4.9.
- An ablation study showing the effect of the reward estimator \(\eta_t\) and the projection step.
- A more detailed discussion of how Assumption 4.5 relates to known spectral properties of Markov operators on continuous state spaces (e.g., Lyapunov conditions, Harris ergodicity).

## Removed Points

These points from the reviewer inputs are removed with justification:

- **Criticism about missing appendix content (proof of Proposition 4.8, Lemma C.1, Lemma C.5, etc.):** The parser strips appendix material from all papers; these proofs exist in the original submission and cannot be verified or faulted from the extracted text. Removed per hard rule.
- **Criticism about "no norm or inner product defined on functions of continuous actions or state-action pairs":** The paper defines an inner product on functions of state via Eq. (2) (line 68–74). The operators \(D_\theta\) and \(P_\theta\) map between state-function spaces, so this is sufficient. The critic estimates the state-value function, not the action-value function, so an action-function inner product is not needed. Removed as factually incorrect.
- **Criticism about the injectivity claim for Assumption 4.4 being "inconsistent with the neural network architecture described":** The reviewer's "injectivity" framing is a characterization, not the paper's claim. The paper discusses that "optimal and suboptimal points are distinguished." While the assumption is strong, it is not clearly inconsistent with the architecture given the projection constraint. The substantive concern (assumption strength) is retained in Major weakness 1; the "inconsistent" framing is removed as an overstatement.
- **Claim in Strengths about "empirical validation on a continuous control task ... strongly corroborates our theoretical findings":** The experiments are too limited (single environment, no direct metric test) for this strength to carry weight. Removed.
- **Speculative claims from the harsh critic about what "may not hold" without evidence from the paper's text:** E.g., "If \(\omega^*(\theta_t)\) can jump discontinuously with policy changes, the coupling analysis breaks" — this is speculation, not a verified flaw. The weakness is retained as the unsubstantiated nature of the assumption itself; the hypothetical consequence is removed.

## Novel Insights

None beyond the paper's own contributions. The synthesis of the two reviews does not reveal a new perspective that the paper itself does not already articulate.

## Suggestions

1. **Strengthen the justification of Assumptions 4.3, 4.4, and 4.5 for continuous spaces.** At minimum, provide one concrete example of a continuous MDP (e.g., a linear system with a truncated Gaussian policy) where all assumptions are satisfied and the constants are finite. For Assumption 4.5, connect it to known spectral properties of Markov operators on Polish spaces or cite references where such uniform spectral gaps are established for continuous state chains.

2. **Relax Assumption 4.4** by replacing the global deterministic lower bound with a high-probability or local version, using NTK-type arguments that hold in a neighborhood of initialization — this would bring the assumption closer to what can be rigorously established for overparameterized networks.

3. **Add a lemma stating the regularity conditions on the MDP (transition kernel, reward) needed for the policy gradient theorem to hold in continuous spaces**, and verify that Assumptions 4.1–4.7 imply them.

4. **Strengthen the experimental section:** Include at least one additional continuous control environment, report gradient norm over iterations, compare with a baseline (e.g., a two-timescale variant or linear function approximation), and include an ablation of the reward estimator.

5. **Partially unroll the \(\widetilde{\mathcal{O}}\) notation** for the most interpretable constants (e.g., mixing time, Lipschitz constants) to give readers a sense of how the bound scales with problem parameters.
