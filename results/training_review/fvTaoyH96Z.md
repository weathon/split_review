Now I have all the information I need. Let me compose the authoritative final review.

## Summary

The paper introduces a structured mathematical framework (a "structurized state space" model) for environmental generalization in deep RL, separating invariant task representations from task-agnostic background components, and proposes Non-Parameterized Randomization (NPR) — a method that randomizes task-agnostic elements of training environments without requiring a parameterized model of the test distribution. The authors present theoretical analysis identifying a "non-optimizable gap" in generalization and prove a lower bound on returns in unseen environments. Empirical results on zero-shot transfer between significantly different environments (e.g., MuJoCo-based navigation → BabyAI mazes, 2D car racing → 3D Torcs) show NPR substantially outperforming baselines.

## Strengths

1. **A structured formalization of the environmental generalization problem.** The decoupled state-space model (Def. 3.1), where \(s_t^e = \psi_t(I) \oplus \xi_t^e\), explicitly separates invariant task content from environment-specific background. This provides a clean vocabulary for discussing generalization across environments with different generative models, going beyond the shared-state-space assumption of Block-MDPs and Epistemic MDPs (Section 3.1, "Difference with Previous Models").

2. **Intuitive and practically motivated method.** The core idea of NPR — randomizing task-agnostic environmental components (room structure, object positions, background, track shape) without requiring a parameterized model of the target — is well-motivated by the limitations of standard Domain Randomization (which requires parameterized models of the target environment) and observation-space augmentation (which cannot change environment structure). The distinction is practically meaningful even if the "non-parameterized" label is somewhat imprecise.

3. **Ablation confirms randomization is necessary.** Section 5.3 shows that the "No-Rand" baseline (training without any randomization) achieves near-zero performance on all generalization tasks, directly establishing that the performance gains come from the NPR procedure rather than the base RL algorithm.

4. **Stable learning curves in randomized environments.** Figure 3 shows that baselines (particularly DrAC) often collapse to near-random performance in randomized training settings, while NPR maintains steady improvement, demonstrating practical stability from the soft-randomization and parallel learning scheme.

## Weaknesses

### Fatal
None.

### Major

1. **The bound in Proposition 3.3 contains questionable mathematical constructions that undermine the theoretical analysis.** The expression \(|S^{e}||S^{e}|^{2}\left|\frac{P(s_{t+1}^{e_1}|s_t^{e_1},a_t)}{|S^{e_2}|}-\frac{P(s_{t+1}^{e_2}|s_t^{e_2},a_t)}{|S^{e_1}|}\right|\) divides transition probabilities by state space cardinalities — an operation that lacks clear probabilistic meaning, especially in continuous state spaces (MuJoCo, car racing) where cardinalities are not defined. No justification is given for this construction, and the overall bound mixes Lipschitz constants, action-space sizes, and state-space sizes without clear derivation. Since the "non-optimizable gap" — a core conceptual claim — is derived from this bound, the theoretical foundation of the paper is weakened.

2. **Proposition 3.4 is asserted without meaningful derivation or supporting assumptions.** The claim that maximizing expected return equals maximizing \(P^{\pi}(I|\hat{I})\) under sparse rewards is stated as an equation without reasoning or proof. The connection between reward maximization and representation alignment does not obviously follow from the stated premises. This proposition is central to the argument about implicit invariant learning, and its lack of support weakens the paper's theoretical narrative.

3. **The method description is too vague for reproducibility.** The implementation of NPR is described only through high-level examples ("randomize the structure of the environment, randomize the background...") and general design principles ("soft randomizing with continuous and slow episodic change"). No algorithm, pseudocode, architectural details (network size, layer configuration, observation preprocessing, action mapping), or concrete implementation specifics are provided. For an empirical paper claiming state-of-the-art results on novel tasks, this level of detail is insufficient.

4. **The experimental results lack sufficient evidence to support the extraordinary transfer claims.** The paper reports 72.9% zero-shot success from MuJoCo-based navigation to BabyAI mazes and 283.4 reward from 2D car racing to 3D Torcs — environments with fundamentally different rendering, dynamics, and visual structure. While the paper states that pixel-based CNNs are used (Section 5.1), no qualitative analysis is provided (no example rollouts, attention maps, or visualization of what the policy actually sees or does). The absence of such verification makes it difficult to assess whether the agent actually solves the intended task or exploits spurious regularities. Standard generalization benchmarks (Procgen, DM Control Generalization) are not used, making comparison to the broader literature difficult.

### Minor

1. **The distinction between "parameterized" and "non-parameterized" randomization is not precisely defined.** The paper contrasts NPR with DR on the basis of requiring a "parameterized model" of the target environment, but any procedural randomization (e.g., changing room structure, object positions) still requires parameters of the procedural generator. The meaningful distinction is whether the randomization requires a *model of the test distribution* — this could be stated more clearly. The claimed advantage is also the key limitation: without such a model, the randomization may not cover the test distribution, and the bound in Theorem 4.1 may have large \(\alpha\) (a point the paper acknowledges in passing but does not evaluate).

2. **Theorem 4.1 is a standard domain-adaptation inequality applied to a new setting.** The bound \(\mathbb{E}_e[V^e] \geq \mathbb{E}_{\hat{\xi}}[\hat{V}] - \alpha\) where \(\alpha\) depends on KL divergence \(\mathbb{D}_{KL}(\rho(e)\|\rho(\hat{\xi}_t))\) is structurally similar to existing bounds in domain adaptation (e.g., Ben-David et al., 2007) and domain-randomization theory. The paper does not discuss this connection or clarify what is novel beyond the application context. The constant \(\delta_{max}\) is also not bounded without further assumptions and could be arbitrarily large in practice.

3. **No comparison to domain-adaptation or invariant-representation RL methods.** The baselines include PPO, DrQ, DrAC, and DR, but do not include methods that explicitly learn invariant representations for transfer (e.g., DARC, HAViR, or methods that align latent representations across domains). Including such baselines would better contextualize the results.

4. **Assumption 3.2 (Invariant Metric) and Definition 3.1 make strong implicit assumptions about identifiability.** The decomposition \(s_t^e = \psi_t(I) \oplus \xi_t^e\) with \(\psi_t\) reversible assumes that the invariant representation \(I\) can be recovered up to a time-dependent bijection — an identifiability condition that is not discussed or validated in the experimental settings.

### Trivial

- The notation in Proposition 3.3's bound is difficult to parse and appears to have typographical issues (e.g., \(|S^{e}||S^{e}|^{2}\) may be a formatting artifact).
- Table captions reference images that are not described in the text.

## Nice-to-Haves

- Evaluation on standard generalization benchmarks (Procgen, DM Control Generalization) to situate the method within existing work.
- Estimation of the KL divergence \(\mathbb{D}_{KL}(\rho(e)\|\rho(\hat{\xi}_t))\) between the randomization distribution and the test distribution, to assess whether the bound in Theorem 4.1 is practically meaningful.
- Ablation isolating which randomization component (structure, background, object positions) contributes most to generalization.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The experimental setup is internally inconsistent; Table 1 says training in Random-Square/Find-Obj but text says MuJoCo"** — Removed: There is no contradiction. "Random-Square" and "Find-Obj" are task names within the MuJoCo-based training environment. The paper consistently describes training in MuJoCo-based environments.
- **"No mechanism for how a policy trained on one type of observation could process another"** — Removed: The paper explicitly states (Section 5.1) that pixel-based RL methods with CNNs are used, providing a coherent mechanism: both training and testing observations are rendered as pixels and processed by the same CNN architecture.
- **"No derivation or proof is provided" (for Proposition 3.3, etc.)** — Removed per hard rule: The parser strips appendices from all papers. Proofs likely exist in the original submission's appendix.
- **"The claim of being first is contradicted by prior work on domain randomization"** — Removed: The claim is about being "the first to introduce a structured framework that uniformly describe the environmental generalization problem" (emphasis on the specific structured framework), not about being first to address generalization at all. The paper properly cites prior DR work.
- **"The paper does not engage with this literature"** — Removed: The paper explicitly discusses DR (Tobin et al., 2017), ADA (Raileanu et al., 2021), Block-MDPs (Zhang et al., 2020; Han et al., 2021), Epistemic MDPs (Ghosh et al., 2021), and other related work.
- **Various formatting/style nitpicks and speculation about missing content** — Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviews surface genuine concerns about the theoretical derivations but do not identify any novel synthesis or unrecognized connection that the authors themselves missed.

## Suggestions

1. **Revise Proposition 3.3.** Provide a clean derivation of the bound without dividing by state space cardinalities, or replace this proposition with a more rigorous information-theoretic or PAC-Bayesian analysis that properly motivates the "optimizable vs. non-optimizable" gap.

2. **Provide full implementation details.** Include pseudocode for NPR, network architecture specifications (number of layers, filter sizes, observation pre-processing), and a concrete description of how randomization is applied in each environment. This is essential for reproducibility.

3. **Add qualitative analysis of the transfer results.** Show example pixel observations from training and test environments, visualize rollouts of the learned policy in both settings, and provide attention maps or representation-space analysis (e.g., PCA/t-SNE) to demonstrate that the agent focuses on task-relevant content and ignores background variation.

4. **Include stronger baselines.** Add comparisons to domain-adaptation and invariant-representation RL methods (e.g., DARC, HAViR) and evaluate on at least one standard generalization benchmark (Procgen or DM Control Generalization) to enable comparison with the broader literature.

5. **Provide statistical rigor.** Report results with confidence intervals across multiple seeds (the paper uses 3 seeds for learning curves and 5 for Table 2, which is reasonable but could be expanded), and include statistical significance tests where appropriate.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>