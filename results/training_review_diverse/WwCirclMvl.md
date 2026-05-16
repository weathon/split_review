Here is my final consolidated review after carefully verifying all claims against the paper.

---

## Summary

This paper introduces the first framework for posterior sampling via Langevin Monte Carlo (LMC) in offline reinforcement learning. For low-rank MDPs, the proposed Lin-LMC-PPS algorithm obtains frequentist sub-optimality bounds that interpolate between worst-case $\tilde{\mathcal{O}}(H^2 d\sqrt{C_\pi/K})$ and best-case $\tilde{\mathcal{O}}(H^2 \sqrt{d C_\pi/K})$, achieving a $\sqrt{d}$ improvement over LCB-based methods in favorable eigenvalue regimes. For general MDPs with overparameterized neural networks, the paper proposes a novel decoupling design (training an auxiliary linear model on top of the trained network to apply LMC perturbations without leaving the NTK regime), yielding bounds scaling with effective dimension $\tilde{d}$ rather than the full parameter dimension. Experimental results on synthetic problems show LMC-based posterior sampling can be competitive with exact Thompson sampling and LCB methods while enjoying constant-time action selection.

---

## Strengths

- **First LMC-based posterior sampling framework for offline RL.** The paper correctly identifies a gap — posterior sampling is underused in offline RL partly due to intractability — and provides the first tractable alternative via LMC. This is clearly stated and well-motivated in Sections 1 and 3.

- **Frequentist (high-probability) sub-optimality bounds instead of Bayesian.** The analysis in Theorems 1 and 2 provides worst-case frequentist bounds, which are stronger than the expected Bayesian bounds of prior posterior sampling work (Uehara & Sun, 2021). This is explicitly highlighted and is a genuine improvement.

- **Data-adaptive interpolation in linear MDPs (Theorem 1).** The bound adapts to the eigenvalue spectrum of the empirical covariance matrix, automatically interpolating between $\tilde{\mathcal{O}}(H^2 d \sqrt{C_\pi/K})$ and $\tilde{\mathcal{O}}(H^2 \sqrt{d C_\pi/K})$. The $\sqrt{d}$ improvement over LCB-based methods in the best case is a real theoretical advance, and the paper provides a clear explanation (Section 4.1, "Tight confidence bounds") of why posterior sampling avoids the function-space enlargement that causes the extra $\sqrt{d}$ factor.

- **Novel decoupling design for neural function approximation (Algorithm 3).** The two-phase approach — training the network with GD first, then applying LMC to an auxiliary linear model on top — is a clever solution to the technical difficulty that direct weight perturbation would move the network out of the NTK regime. The theoretical analysis in Theorem 2 yields bounds that depend on effective dimension $\tilde{d}$ rather than the prohibitive $md$, and improves over NTA23 by $\sqrt{C_\pi}$.

- **Computational complexity analysis.** Section 6 provides a concrete comparison showing Lin-LMC-PPS costs $\mathcal{O}(\min\{d,K\} K d)$ versus $\mathcal{O}(\min\{K d^2, d^3 + K d\})$ for exact posterior sampling, with particular advantage when $d \gg K$ (e.g., NTK settings). This is an important practical strength that is well-articulated.

- **Honest discussion of limitations.** The paper openly acknowledges the gap between LMC-based PS and optimal bounds (Section 6), leaving it as an open problem. This strengthens credibility.

---

## Weaknesses

### Fatal
None.

### Major

- **Experiments do not evaluate the proposed neural algorithm.** The paper proposes Neural-LMC-PPS (Algorithm 3) which uses a two-phase design with an auxiliary linear model. However, the experimental section (line 189) states: *"For Neural-LMC-PPS, we directly apply noisy gradient updates to the network, instead of using an auxiliary linear model, to approximate posterior samples."* This means the experiments test a simplified variant — direct LMC on network weights — not the algorithm that is theoretically analyzed (Algorithm 3). While the paper acknowledges this and points to the supplementary, it creates a disconnect between the theoretical contribution and its empirical validation. The neural experiments therefore do not validate the specific algorithmic design that is the paper's main technical contribution for the neural setting. The authors should either test Algorithm 3 directly (even on a smaller problem), or explicitly reframe the neural experiments as evaluating a heuristic variant and discuss the limitations of the current validation. The linear MDP experiments (Lin-LMC-PPS) do test the proposed algorithm, so this weakness is specific to the neural setting.

### Minor

- **No error bars, confidence intervals, or multiple seeds in experimental results.** All figures (Figures 1–3) report single curves without any measure of variability. Given that LMC involves injected Gaussian noise and the baselines (Thompson sampling) are themselves stochastic, it is impossible to assess whether the observed performance differences are meaningful or due to variance. The claim that LMC-PPS *"slightly outperforms the exact posterior sampling method (Thompson)"* is unsupported without statistical rigor. This is a standard expectation in empirical ML, even for theory papers with supporting experiments.

- **Data splitting reduces effective sample size by a factor of $H$.** The neural algorithm uses only $K' = \lfloor K/H \rfloor$ episodes per timestep (Section 3.2), losing a factor of $H$ in sample size. This is reflected in the bound (the dominant term scales with $K'$ not $K$) but is not discussed as a practical limitation. For long horizons, this reduction is substantial and could significantly degrade empirical performance compared to approaches that use all $K$ episodes at each step.

- **The $\sqrt{d}$ improvement over LCB methods only materializes in favorable eigenvalue regimes.** The paper's worst-case bound $\tilde{\mathcal{O}}(H^2 d \sqrt{C_\pi/K})$ matches PEVI's worst-case bound; the $\sqrt{d}$ improvement occurs only when the eigenvalue decay is favorable (best case). While the interpolation property is correctly presented, the framing in the introduction/abstract could be read as suggesting a uniform improvement. The paper would benefit from being more explicit that in the worst case the bound is not improved over LCB methods.

- **Strong assumptions for the neural analysis.** Theorem 2 relies on approximate completeness (Assumption 4.1), overparameterization ($m$ polynomial in $K$), the NTK regime, and data splitting. The paper does not discuss how to verify these assumptions in practice or what happens when they are violated. This is common in the NTK-based RL theory literature but limits the practical guidance the theory provides.

### Trivial
- The description of how the LMC noise level $\tau$ is set (a formula is given but the intuition behind its scaling could be clearer).
- The $o_m(1)$ terms in Theorem 2 vanish only as $m \to \infty$, meaning the bound is asymptotic in network width — standard for NTK analyses but worth noting.

---

## Nice-to-Haves
- A brief empirical check that the two-phase auxiliary-linear-model variant (Algorithm 3) works, even on a small-scale problem, would significantly strengthen the claim.
- A discussion of heuristic choices for hyperparameters ($\tau$, $\lambda$, $M$) and their robustness would help practitioners.
- A comment on whether the data splitting technique can be avoided (e.g., via martingale concentration without splitting) would be a useful pointer for future work.

---

## Removed Points

These points were raised by reviewers but are removed with justification below:

- *"No code or data release mentioned"* — Removed per the rule against reproducibility nitpicks about artifacts impractical or not standard to include.
- *"The paper does not compare to more recent empirical offline RL methods (CQL, IQL, etc.)"* — The harsh critic themselves correctly notes this is unreasonable given the paper is theoretically oriented. Removed as out-of-scope.
- *"The bound includes an o_m(1) term..."* — Standard in NTK literature. Not a weakness of this paper.
- *"The √d improvement in best case contradicts pessimistic claims"* — The paper is transparent about the interpolation; no contradiction exists.
- *"The paper should cover additional domains/tasks"* — Scope creep; the paper's depth in its chosen direction is sufficient.

---

## Novel Insights

Beyond the paper's own contributions, the most interesting insight emerging from the reviews is the tension between theoretical tractability and practical implementation in the neural setting. The paper's key technical innovation (the auxiliary linear model to decouple training from perturbation) was motivated by the need to stay within the NTK regime for analysis, but the experiments opted for a simpler direct-LMC approach. This reveals a broader methodological point: the theoretical machinery (NTK regime, data splitting, auxiliary models) required to obtain provable guarantees may be at odds with the most natural practical implementation. The paper would be strengthened by explicitly discussing this gap and what the theory implies about the conditions under which the simpler variant might still be expected to work.

---

## Suggestions

1. **Test Algorithm 3 directly**, or alternatively remove the neural experiments and reframe as a theory-only paper with experiments limited to the linear case. The current hybrid approach validates neither the theoretical algorithm nor a clearly separate practical variant.

2. **Add error bars / confidence intervals** to all experimental figures (at least 5 independent seeds). This is essential for any claim about comparative performance between stochastic algorithms.

3. **Explicitly discuss the K' = K/H limitation** as a practical concern and note whether alternative concentration approaches could mitigate it.

4. **Clarify the scope of the √d improvement**: add a sentence in the introduction or Section 4.1 noting that in the worst-case eigenvalue regime the bound matches (rather than improves upon) LCB-based methods.

---

## Score and Decision

This paper makes a significant theoretical contribution — it is the first to propose and analyze LMC-based posterior sampling for offline RL, obtaining sample-efficient bounds for both linear and neural function approximation. The theoretical work is novel, technically deep, and clearly presented. The experimental evaluation, however, has a structural disconnect for the neural setting: it does not test the proposed algorithm (Algorithm 3), and the results lack basic statistical rigor (no error bars). These are real weaknesses, but they do not invalidate the theoretical contributions, which are the paper's primary value. With the experimental issues addressed, this would be a strong paper.

**Score: 6.5** — solid accept. The theoretical contributions are publishable and valuable as-is; the experimental issues are fixable and do not undermine the core claims.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>