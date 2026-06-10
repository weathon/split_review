## Summary

This paper provides a theoretical convergence analysis of Adam under the $(L_0,L_1)$-smooth (non-uniform smoothness) condition, proving that Adam provably converges faster than Gradient Descent with Momentum (GDM) and Stochastic GDM (SGDM) in both deterministic and stochastic settings. It introduces a novel stopping-time technique that enables Adam's minimum-gradient-norm convergence rate to match existing lower bounds across all problem hyperparameters, and also yields a parameter-agnostic Adam scheduler. The paper addresses the long-standing puzzle of why Adam empirically outperforms SGDM despite standard $L$-smooth analysis placing them on equal footing.

## Strengths

1. **First provable convergence separation between Adam and GDM under $(L_0,L_1)$-smoothness.** Theorem 1 gives Adam an upper bound of $\Theta(L_0\Delta_1/\varepsilon^2)$ matching the known lower bound for first-order deterministic optimizers, while Theorem 2 establishes a new lower bound for GDM of $\tilde{\Omega}((L_1^2\Delta_1^2+L_0\Delta_1)/\varepsilon^2)$ that exhibits a quadratic dependence on the initial function value gap $\Delta_1$ that Adam's bound avoids. No prior work had established such a separation.

2. **A new GDM lower bound that corrects the hyperparameter-order flaw in prior work.** Existing lower bounds for GD under $(L_0,L_1)$-smoothness (Proposition 1, from Crawshaw et al.) select the counterexample *after* fixing the learning rate, which reverses standard practice. Theorem 2 proves the same $\tilde{\Omega}$ rate holds when hyperparameters are chosen *after* the problem is fixed — matching how lower bounds are conventionally formulated (Carmon et al., Arjevani et al.) — and extends the result to incorporate momentum. The construction places counterexamples for different hyperparameter values over different coordinates, a simple but effective trick.

3. **Novel stopping-time technique achieving optimal convergence across all problem hyperparameters.** The sub-optimal $\sigma_0^3$ dependence in Theorem 3 is eliminated in Theorem 5 via a stopping time $\tau = \min\{t: \|\nabla f(w_{t+1})\|^2 \le \mathcal{O}(\sigma_0^2(1-\beta_2))\}$. The paper explains why naive conditioning-on-events fails (it breaks closed-form expectations), while the stopping-time approach maintains closed-form expressions via the optimal stopping theorem. The resulting rate $\Theta(L_0\sigma_0^2\Delta_1/\varepsilon^4)$ matches the lower bound across all problem hyperparameters.

4. **Concrete algorithmic insight into why the EMA mechanism matters.** The remark in Section 4.1 (line 128) explains why Adam outperforms AdaGrad under $(L_0,L_1)$-smoothness: AdaGrad's accumulating conditioner makes the learning rate decay too aggressively in later stages, while Adam's exponential moving average avoids this. This identifies the EMA mechanism as the crucial algorithmic feature, grounded in the $(L_0,L_1)$ condition's structural requirement that updates stay $\mathcal{O}(1)$ in norm.

5. **Parameter-agnostic Adam via the stopping-time technique.** Theorem 6 shows Adam with scheduler $\eta = 1/\sqrt{t}$, $\beta_2 = 1 - 1/\sqrt[4]{t^3}$ achieves $\tilde{\mathcal{O}}(1/\sqrt[4]{T})$ convergence without knowledge of problem parameters, demonstrating the stopping-time technique's independent applicability.

## Weaknesses

### Fatal
None.

### Major

1. **The SGDM non-convergence claim (Theorem 4) is supported by only an intuitive sketch in the main text.** The claim is extraordinary: that there exist instances satisfying Assumptions 1 and 2 where SGDM fails to converge *for any learning rate and momentum coefficient*, i.e., $\min_{t\in[T]} \mathbb{E}\|\nabla f(w_t)\| \ge L_1\Delta_1$ for all $T$. The main text gives only a one-paragraph intuition (lines 211-213): that $(L_0,L_1)$-smoothness can cause exponential gradient growth, converting non-heavy-tailed noise into effectively heavy-tailed noise. For a claim of this strength — which starkly contrasts with concurrent work (Li et al., 2023) showing SGD can converge with high probability under the same assumptions — the main text should provide at minimum a concrete one-dimensional construction and a sketch of the proof mechanics. The current presentation asks the reader to take the strongest result in the paper on faith.

2. **The algorithm analyzed is a scalar-adaptive variant of Adam, not the per-coordinate version used in practice.** The paper uses a single scalar adaptive learning rate $\eta/(\lambda + \sqrt{\nu_t})$ where $\nu_t$ is based on the *norm* of the gradient, rather than per-coordinate scaling. The authors acknowledge this (line 76) and claim the proof is "readily adaptable to the per-coordinate version," but note that "the convergence rate for the per-coordinate Adam is subject to the dimensionality $d$" and that decoupling from dimensionality "remains an unresolved issue." The per-coordinate adaptivity is the defining feature of Adam; a scalar-adaptive version is closer to normalized GD or a simplified AdaGrad-norm variant. Since the paper's title claims to analyze the convergence of "Adam," and the broader narrative frames the results as explaining Adam's practical success, this gap between what is analyzed and what practitioners use should be given more prominence and discussion.

### Minor

1. **The stopping-time result (Theorem 5) changes the metric from average gradient norm to minimum gradient norm.** The lower bound from Arjevani et al. is stated for the average gradient norm; Theorem 5 proves a bound on $\mathbb{E}\min_{t\in[T]}\|\nabla f(w_t)\|$. While $\min \le$ average makes the comparison valid (a lower bound on average implies one on min), the paper does not always articulate this distinction clearly. The claim that the rate "matches the lower bound with respect to all problem hyperparameters" (line 251) would benefit from explicitly noting the metric change.

2. **The condition $\varepsilon \le 1/\operatorname{poly}(\dots)$ in the stochastic theorems is very strong and appears with little discussion.** This restricts the analysis to the small-$\varepsilon$ regime. The paper does not discuss whether this is an artifact of the proof technique or an inherent limitation of the problem setting.

3. **The relationship between the SGDM non-convergence result (Theorem 4) and the concurrent high-probability convergence result of Li et al. (2023) is addressed in only a single paragraph (line 215).** The paper correctly notes the in-expectation vs. high-probability distinction and the worse dependence on $\Delta_1$ in Li et al.'s bound, but this surface-level discussion undersells an interesting tension that deserves deeper treatment.

### Trivial
None.

## Nice-to-Haves

- The paper's hyperparameter choices for the stochastic theorems (e.g., $\eta \propto \varepsilon^2$, $1-\beta_2 \propto \varepsilon^4$) are referred to as "a proper choice" but could be stated explicitly in the main text for clarity.
- A brief discussion on whether the lower bound for the full $(L_0,L_1)$-smooth class (as opposed to the $L$-smooth subclass) might be higher than the Arjevani et al. bound would sharpen the "matching" claim.

## Removed Points

These points were raised by reviewers but removed after verification against the paper; treat with caution.

- *"Every theorem is informal with no formal content"* — REMOVED. The theorems DO contain quantified claims (iteration complexity $T \ge \Theta(\dots)$ and gradient norm bounds $\le \varepsilon$) stated with clear asymptotic notation. The "Informal" label simply hides numerical constants, which is standard practice for main-text theorem statements in optimization theory. A reader can determine the dependency on each problem parameter from the stated bounds.

- *"Lower bound matching is imprecise because the lower bounds are established under $L$-smoothness, not $(L_0,L_1)$-smoothness"* — REMOVED. The paper addresses this directly: when $L_1=0$, $(L_0,L_1)$-smoothness reduces to $L$-smoothness, so lower bounds for the latter carry over (line 124). The paper also explicitly acknowledges where its upper bounds have suboptimal dependencies (Remark 1, lines 193-196) and addresses them with the stopping-time technique.

- *Formatting/presentation nitpicks about empty proof environments* — REMOVED. These are parser artifacts, not author errors.

- *Criticisms about missing appendix content* — REMOVED. The appendix was stripped by the parser; the original submission contains these proofs.

## Novel Insights

Beyond the paper's own contributions, the meta-review surfaces that the most important structural contribution may not be the separation results themselves (which, while novel, rely on standard proof techniques), but rather the **stopping-time technique applied to the adaptive gradient denominator**. The difficulty the paper identifies — that the correlation between the stochastic gradient and the adaptive learning rate creates an error term $\eta\frac{\sigma_0^2(1-\beta_2)\|g_t\|^2}{\sqrt{\beta_2\nu_{t-1}}\nu_t}$ that resists standard bounding because $\sqrt{\nu_t}$ is not lower-bounded — is a fundamental problem in Adam analysis. The observation that this term can be interpreted as an "approximate telescoping" series and then controlled via a carefully chosen stopping time that preserves closed-form expectations under the optimal stopping theorem is a genuinely new proof technique. This technique may generalize to other adaptive optimizers and deserves attention as a methodological contribution in its own right, separate from the specific separation claims.

## Suggestions

1. Expand the SGDM non-convergence proof sketch in the main text. Even a simple one-dimensional construction showing why all learning rates fail would substantially strengthen the paper. The current one-paragraph intuition is too thin for a claim of this magnitude.

2. Add a paragraph clarifying what changes (and what does not) when extending from scalar-adaptive to per-coordinate Adam. The footnote about dimensionality is good but undersells the impact: if the per-coordinate rate carries a $\sqrt{d}$ factor, this affects the practical relevance of the separation claim.

3. When stating the stopping-time result, explicitly note the metric change from average to minimum gradient norm and explain why the comparison to the Arjevani et al. lower bound remains valid despite this change.

4. Discuss the $\varepsilon \le 1/\text{poly}(\dots)$ condition more thoroughly: is it a proof artifact or an inherent limitation? Could it be relaxed?

## Score and Decision

This paper addresses an important and well-motivated question, makes genuine theoretical contributions (the GDM lower bound that fixes the hyperparameter-order flaw, the stopping-time technique, and the parameter-agnostic result), and is transparent about its limitations. The two major weaknesses — the thin proof sketch for the SGDM non-convergence claim and the scalar-adaptive simplification — are real but do not invalidate the core contributions. The paper is above the acceptance threshold for a top venue and would benefit from a revision that addresses the SGDM non-convergence sketch and tightens the framing around the scalar-adaptive versus per-coordinate gap.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>