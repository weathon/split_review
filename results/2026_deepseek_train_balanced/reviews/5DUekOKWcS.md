## Summary

This paper proposes AFedPG, an asynchronous federated reinforcement learning framework using policy gradient updates. It introduces a delay-adaptive lookahead technique that cancels second-order Hessian correction terms arising from the dynamic data collection in RL (a challenge absent in supervised FL), and provides both global and FOSP convergence guarantees with \(\mathcal{O}(\epsilon^{-2.5}/N)\) sample complexity per agent — matching synchronous FedPG while strictly improving time complexity from \(\mathcal{O}(t_{\max}/N)\) to the harmonic mean \(\mathcal{O}(\bar{t})\). Empirical results on four MuJoCo tasks with varying agent counts validate the approach.

## Strengths

1. **Delay-adaptive lookahead technique with exact algebraic cancellation of second-order terms.** Equation (179) shows \((1-\alpha)\nabla^2 J(\theta_k)(\theta_{k-1}-\theta_k) + \alpha\nabla^2 J(\theta_k)(\tilde{\theta}_k-\theta_k) = 0\) by construction of \(\tilde{\theta}_k\), eliminating the Hessian correction terms that arise uniquely in RL's online data-collection setting (and have no analogue in supervised FL). This is a principled, directly motivated design — not a generic heuristic.

2. **First convergence guarantees for asynchronous federated policy-based RL.** The paper provides both global convergence (Theorem 1: \(\mathcal{O}(K^{-2/5})\)) and FOSP convergence (Theorem 2: \(\mathcal{O}(K^{-2/7})\)) rates that account for delays \(\delta_k\), concurrency \(\omega_k\), and function approximation bias. These match the structure of state-of-the-art single-agent normalized PG rates (Fatkhullin et al. 2023) while adding linear speedup in \(N\) and handling asynchronous delays.

3. **Provably lower time complexity than synchronous FedPG for any heterogeneity pattern.** The average waiting time \(\bar{t} = 1/\sum_i 1/t_i\) is strictly less than \(t_{\max}/N\) (synchronous) for any finite \(t_i\), with equality only when all agents are identical. This is a formal guarantee, not an asymptotic claim, and the improvement grows with \(t_{\max}/t_{\min}\).

4. **Controlled ablation confirms the lookahead is empirically necessary.** The vanilla variant (AFedPG without the delay-adaptive lookahead) performs substantially worse across all environments (line 333, Figure 6), directly isolating the contribution of the core methodological innovation.

5. **Evaluation across multiple environments and agent counts with proper randomization.** Experiments cover four MuJoCo tasks with \(N=2,4,8\) agents, 10 random seeds, and 95% confidence intervals, comparing against single-agent PG, synchronous FedPG, and A3C.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Key assumptions are referenced but never stated in the main text.** Theorems 1 and 2 (lines 230, 241) invoke "Assumption \ref{assum:policy}" and "Assumption \ref{assum:func_approx}" but these are not defined anywhere in the visible text. The global convergence bound includes a bias term \(\sqrt{\epsilon_{\text{bias}}}/(1-\gamma)\) from function approximation error, but the nature of this error — and the regularity conditions on the policy parameterization — are opaque. The main text should at minimum summarize the assumptions (e.g., smoothness constants, bounded score functions) to make the convergence results interpretable.

2. **Empirical evaluation scope is limited.** (a) All four environments are continuous-control MuJoCo tasks from the same benchmark family. (b) Only one heterogeneity level is tested (\(t_{\max}/t_{\min} \approx 4\), line 331), despite the abstract claiming "various computing heterogeneity scenarios" and the theoretical advantage growing with larger ratios. (c) The methodology for simulating heterogeneity is not described (artificial delays? varying batch sizes? different hardware?). (d) With only 10 random seeds, smoothed 95% confidence intervals may appear tighter than warranted for high-variance environments like Humanoid.

3. **Momentum buffer mixes gradients with different delays, but this is not discussed.** Algorithm 1 Step 5 computes \(d_{k-\delta_k} \leftarrow (1-\alpha)d_{k-1-\delta_{k-1}} + \alpha\,g(\cdot)\), where \(\delta_k\) and \(\delta_{k-1}\) can differ arbitrarily. The buffer therefore contains gradients with different staleness levels. The normalized update controls step magnitude but does not address directional bias from this mixed-staleness. It is unclear whether the convergence analysis restricts the delay sequence (e.g., bounded delay, non-increasing delay) to handle this.

4. **Key hyperparameters are unspecified.** The functional form of \(\alpha_{k-\delta_k}\) (how it depends on delay \(\delta_k\)) is never given — it is merely described as "depending on the delay." Learning rate schedules for \(\eta_k\) and \(\alpha_k\) are absent. Network architecture (layers, hidden units, activation functions) is not stated; the paper defers to "practical settings in stable-baselines3" without specifying which settings. These details matter for reproducibility.

5. **Novelty framing could be more precise.** The paper claims "for the first time" about asynchronous policy-based FedRL (lines 22, 57, 66). While the federated setting with private environments is genuinely distinct, asynchronous policy gradient with stale gradients is well-studied in A3C and related methods. The paper correctly uses A3C as a baseline and distinguishes itself, but the "first" framing would benefit from a more explicit delineation: the key novelty is the delay-adaptive lookahead and its integration with the federated setting, not asynchrony per se.

### Trivial

- The time complexity expression for FedPG in Table 1 (\(\mathcal{O}(t_{\max}/N\,\epsilon^{-2.5})\)) could more clearly note that it is per-agent global time (total wall time divided by \(N\)), not per-iteration waiting time.

## Nice-to-Haves

- Testing a wider range of heterogeneity ratios (e.g., \(2\times, 10\times, 20\times\)) would directly validate the theoretical claim that the time advantage grows with \(t_{\max}/t_{\min}\).
- Sketching the key lemmas (ascent lemma, return smoothness) at a high level in the main text would make the analysis more self-contained without needing the appendix.
- A centralized training baseline (pooling all data on one agent) would contextualize how much performance is lost or gained through federated training.

## Removed Points

These points from the input reviews were identified for removal, with justifications:

- **Criticism about missing appendix proofs** — The parser strips appendices from all papers; these exist in the original submission. Removed per hard rule.
- **Criticism about the second-order Taylor expansion requiring Lipschitz Hessian as a "strong assumption"** — The cancellation in Eq. 179 is exact algebra by construction (plugging \(\tilde{\theta}_k = \theta_k + \frac{1-\alpha}{\alpha}(\theta_k - \theta_{k-1})\) yields exact zero), not dependent on smoothness. Smoothness conditions are standard for bounding Taylor remainders elsewhere. Removed as the framing overstates the concern.
- **Criticism about missing IMPALA comparison** — IMPALA is a non-federated method; requesting it as a baseline is scope-creep. Also falls under the rule against citing "missing related works." Removed.
- **Criticism about missing centralized training baseline** — The paper already compares with \(N=1\) PG (single-agent training). Removed.
- **Formatting nitpicks about Table 1** — Pure presentation artifact. Removed.
- **Complaint about proof sketches being absent from main text** — Detailed derivations belong in the appendix; the main text states the rates. Removed per missing-appendix rule.
- **Strength Finder's generic/superficial strengths** — Several claimed strengths from the Strength Finder were generic (e.g., "this paper addressed an important problem") and removed per filtering rules.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. State the key assumptions (or at minimum a plain-language summary of them) in the main text near the convergence theorems.
2. Describe how heterogeneity was simulated, and ideally add experiments with a wider range of \(t_{\max}/t_{\min}\) ratios (e.g., \(2\times\), \(10\times\), \(20\times\)).
3. Provide the functional form of \(\alpha_{k-\delta_k}\) and the learning rate schedules in the main text or supplement.
4. Discuss the mixed-staleness issue in the momentum buffer: either explain restrictions needed for the analysis, or note that the analysis handles it through existing error bounds.
5. Frame the novelty more precisely by separating what is inherited from A3C-style asynchrony versus what is new (the federated setting + delay-adaptive lookahead).

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>