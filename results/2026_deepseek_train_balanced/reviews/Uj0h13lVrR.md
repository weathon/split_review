## Summary

This paper proposes extending GFlowNets to stochastic environments by incorporating an entropy-ratio parameterization into the detailed balance condition, using a KL divergence training objective, and dynamically adjusting a parameter \(\gamma\) based on reward variance to control exploration-exploitation. The motivation — handling stochastic transitions in GFlowNets — is legitimate, but the proposed solution is not mathematically sound.

## Strengths

- **Clear problem identification.** The paper correctly identifies that existing GFlowNet methods primarily target deterministic environments and that stochastic transitions pose a meaningful challenge. This motivation is well-framed in Sections 1 and 3.

## Weaknesses

### Fatal

1. **Equation 3 defines transition probabilities in terms of the agent's policy — a category error (Section 4.2).**  
   The paper states as a given:
   \[
   P(s_{t+1}|(s_t,a_t)) = \frac{H_{\text{high}}(s_{t+1})}{\gamma H_{\text{high}}(s_{t+1}) + (1-\gamma)H_{\text{low}}(s_{t+1})}
   \]
   where \(H_{\text{high}}(s) = \exp(-\beta_{\text{high}}\cdot H(s))\), \(H_{\text{low}}(s) = \exp(-\beta_{\text{low}}\cdot H(s))\), and \(H(s) = H(\pi(\cdot|s))\) is the *policy's* entropy at state \(s\). This makes the environment's transition probability a function of the agent's policy at the *next* state — a circular dependency. The transition dynamics of an MDP are a fixed property of the environment, not a function of the agent's learned policy. Furthermore, the RHS depends only on \(s_{t+1}\) and not on \((s_t, a_t)\), which is physically meaningless as a transition probability. No derivation or justification is provided for this equation; it is simply asserted. Because Eq. 3 underlies the entire theoretical framework (the KL objective in Eq. 4, the dynamics loss in Eq. 6, and the role of \(\gamma\)), this flaw is fatal — the core contribution rests on an unsupported assertion.

2. **The KL divergence in Eq. 4 is not a valid KL divergence between two probability distributions.**  
   \[
   \min_\theta D_{KL}\left(\pi_B((s_t,a_t)|s_{t+1}) \;\middle\|\; \frac{F((s_t,a_t)) \cdot r_\gamma(s_{t+1})}{F(s_{t+1})}\right)
   \]
   The right-hand argument is a ratio of scalar flow values and an entropy ratio — it is not established to be a normalized probability distribution over the same space as \(\pi_B((s_t,a_t)|s_{t+1})\). A KL divergence is defined between two probability distributions; the paper provides no argument that the RHS satisfies this condition. The training objective is therefore not well-defined.

### Major

3. **The \(\gamma\) update rule references an undefined quantity (Section 6, Algorithm 1).**  
   The rule \(\gamma_{t+1} = \gamma_t + \eta(\text{Var}(R(s_{t+1})) - \text{Var}(R(s_t)))\) uses \(\text{Var}(R(s_t))\), the variance of the reward at an individual state. On a single trajectory, a state is typically visited once per episode, yielding one reward value. The paper never explains how \(\text{Var}(R(s_t))\) is estimated — whether via an exponential moving average across episodes, an ensemble, or a batch estimate. As written, this rule is not implementable. Additionally, the conceptual motivation for using the *difference* in reward variance between *consecutive states* on a *single trajectory* to drive the exploration-exploitation trade-off is not supported by any analysis or reference.

4. **Algorithm 1 does not match the theoretical derivation.**  
   The theory (Eq. 4–5) derives a KL objective involving the flow function \(F(s_{t+1})\) in the denominator and additional terms \((\log\frac{H_{\text{high}}(s')}{\gamma H_{\text{high}}(s')})\). Algorithm 1 (line 10) implements:
   \[
   D_{KL} = \sum_{s,a,s'} \pi_\theta(s,a|s') \left[\log\pi_\theta(s,a|s') - \log F(s,a) - \log r_\gamma(s')\right]
   \]
   This expression is missing the \(+\log F(s')\) term (or equivalent) that should appear from expanding the KL, and replaces the theoretically-derived extra terms with a simpler expression. The paper does not explain which objective is used in the experiments, nor does it connect the algorithm to Eq. 4.

5. **The dynamics loss (Eq. 6) is presented without derivation.**  
   Equation 6:
   \[
   \mathcal{L}(\gamma) = -\sum_{s,a} \mu_\pi(s) H(\pi(\cdot|s)) \left( \log r_\gamma(s) + (1-\gamma)(1-H(\pi(\cdot|s)))\log(1-r_\gamma(s)) \right)
   \]
   is described as "derived" but no algebraic steps are shown connecting it to the KL objective or the detailed balance condition. The \((1-\gamma)(1-H(\pi(\cdot|s)))\) term is unexplained. While the practical approximation (Eq. 10) is clearer as a binary classification loss with entropy weighting, the lack of principled derivation makes the method feel assembled from components.

6. **SAC is claimed as a baseline but never appears in the experiments.**  
   The contributions list (line 32) claims the method outperforms "Stochastic GFlowNets (SGFN), PPO, SAC and MCMC." However, the experimental section (lines 207–209) lists baselines as "vanilla GFlowNets... Stochastic GFlowNets (SGFN)... Metropolis-Hastings MCMC... and PPO." No SAC results appear in any figure or table, and SAC is never mentioned in the experimental sections. This discrepancy between claimed and actual baselines undermines the empirical claims.

### Minor

7. **No formal analysis or convergence proofs despite abstract's claim.**  
   The abstract states "Detailed proofs and analysis demonstrate the efficacy of this methodology." The paper contains no theorems, convergence guarantees, or proof that the proposed objective has the correct fixed point (i.e., \(P_F^\top(x) \propto R(x)\)). Section 6 is entirely qualitative prose.

8. **No explanation of how \(H_{\text{high}}\) and \(H_{\text{low}}\) are computed in practice.**  
   The paper defines these as exponentials of the policy entropy but does not discuss whether they require separate density estimation, empirical counts, or other computational machinery. The free parameters \(\beta_{\text{high}}\) and \(\beta_{\text{low}}\) are introduced without guidance on how to set them.

9. **Experimental reporting is incomplete.**  
   Results are presented only as figures with no numerical values or error bars (the paper states five random seeds are run but only reports the mean). No ablation studies are provided despite the method having multiple interacting components (KL objective, entropy-ratio estimation, dynamic \(\gamma\), dynamics loss). GridWorld results are only shown for \(\alpha = 0.25\).

### Trivial

10. **No limitations section** is included, which is unusual for a paper proposing a new method.

## Nice-to-Haves

- Error bars on experimental figures and numerical results in tables would significantly strengthen the empirical evaluation.
- An ablation study disentangling the effects of the KL objective, entropy-ratio estimation, and dynamic \(\gamma\) adjustment would help identify which components drive performance.
- Sensitivity analysis for \(\beta_{\text{high}}\), \(\beta_{\text{low}}\), \(\eta\), and initial \(\gamma\) would be informative.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Strength from Strength Finder: "Explicit entropy-ratio parameterization of transition dynamics"** — This is the paper's central claimed contribution, but it is built on the unsupported Eq. 3, which is a fatal flaw. A claimed contribution cannot serve as a strength when its theoretical foundation is unsound.
- **Strength from Strength Finder: "Adaptive γ update rule driven by reward variance"** — The γ update rule refers to an undefined quantity (variance from a single sample), so the claimed strength is not verifiable from the paper as written.
- **Strength from Strength Finder: "Practical, discretized approximation of the dynamics loss"** — The practical approximation (Eq. 10) is indeed concrete, but without a sound theoretical foundation, a tractable approximation of an unsupported loss does not constitute a genuine strength. This is a restatement, not a verified merit.
- **Harsh Critic: "Section 6 (Analysis) has no formal analysis"** — Already folded into Minor weakness #7 above (verified: the section is indeed qualitative).
- **Harsh Critic: "Exponentials for H_high/H_low without justification"** — Already covered in Minor weakness #8 above.
- **Harsh Critic: "No code or reproducibility details"** — Stripped per hard rule: the paper cites "open-source code" with a superscript reference. Criticizing missing links or footnotes is a formatting/reproducibility nitpick, and the hard rules state to remove such criticisms.
- **Harsh Critic: "Missing related works"** — Stripped per hard rule: the instructions state not to flag missing related works.
- **Harsh Critic: "Pan et al. (2023) already handles stochasticity"** — The paper cites Pan et al. as Stochastic GFlowNets in Section 4.1 and positions itself as an extension. This is more a matter of positioning than a factual error about the paper's content.
- **Harsh Critic: Claim about H_high/H_low being "free parameters"** — This is a genuine concern but is already captured in weakness #8. The framing as a separate "for a top venue" criticism is overblown; many papers introduce parameters with minimal guidance.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a fundamental theoretical incoherence in the paper's core equation (Eq. 3) that invalidates the claimed contributions, but this is not a novel insight — it is a verification that the paper's stated claims do not withstand scrutiny.

## Suggestions

- The theoretical foundation needs to be fundamentally reworked. Equation 3 cannot be simply asserted; any relationship between policy entropy and transition dynamics requires a principled derivation from the environment's actual transition probabilities.
- If the entropy-ratio idea is to be salvaged, it should be framed as a learned weighting or correction term in the flow-matching objective (analogous to entropy regularization in soft RL), not as a redefinition of environment dynamics.
- The algorithmic implementation must be reconciled with the theoretical derivation — currently they differ in substantive ways.
- The \(\gamma\) update rule needs a concrete specification of how \(\text{Var}(R(s))\) is estimated.
- The experiments need numerical results, error bars, ablations, and the SAC baseline that was promised.

## Score and Decision

MY FINAL SCORE: <score>2.0</score>
MY FINAL DECISION: <decision>Reject</decision>