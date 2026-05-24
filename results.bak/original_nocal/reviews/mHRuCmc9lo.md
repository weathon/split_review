Now I have a thorough understanding of the paper and the reviews. Let me construct the final consolidated review.

---

## Summary

This paper studies how a decision maker should optimally act when forecasts come with only partial calibration guarantees. The authors formalize a minimax robust decision framework parameterized by the class $\mathcal{H}$ of calibration tests that the forecaster passes, characterize the optimal policy via duality (Theorem 3.1), and prove a striking sharp transition: once $\mathcal{H}$ contains the decision-calibration indicators, the robust policy collapses to the plug-in best response (Theorems 4.1–4.2). For cases where decision calibration is unavailable, they show that "free" $\mathcal{H}$-calibration emerges from standard squared-loss training (self-orthogonality, Proposition 4.4) and from post-hoc binning (Proposition 4.5), yielding tractable robust policies.

## Strengths

1. **General framework connecting calibration to robust decision making.** The paper innovatively treats partial calibration as defining an ambiguity set of conditional expectations, then applies a minimax lens to derive optimal policies. This is a clean conceptual advance over prior work that either required full calibration or settled for regret-type guarantees. The framework is articulated precisely in Equations (2)–(5) and Figure 1.

2. **Sharp, non-obvious transition result (Theorems 4.1–4.2).** The finding that adding the $|\mathcal{A}|$ decision-calibration indicators to $\mathcal{H}$ is *sufficient* to recover plug-in best-response optimality is a genuine theoretical surprise. The proof sketch (invariance of the plug-in policy's utility under $\mathcal{H}_{\text{dec}}$ constraints) is transparent and credible. The contrast with swap-regret guarantees (Section 4.1, lines 173–183) is correctly drawn: swap regret leaves open the possibility of a dominating policy that is not bottlenecked by action-remapping, whereas the minimax result closes this gap.

3. **Practical bridges from standard training (Propositions 4.4, 4.5).** Self-orthogonality under squared-loss training (Proposition 4.4) is a clean observation that connects the framework to standard ML pipelines without additional algorithmic intervention. The closed-form robust policy for bin-wise calibration (Proposition 4.5) is immediately deployable with off-the-shelf post-hoc recalibration.

4. **Simultaneous plug-in optimality across multiple decision problems (Corollary 4.3).** The observation that a single forecaster can be simultaneously optimal for many downstream decision makers (if it passes the union of their decision-calibration tests) is a practically useful guarantee for shared forecasting platforms.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Experimental evaluation lacks statistical rigor and scope.** The experiments (Section 5) report only single-run mean utilities without standard errors, confidence intervals, or multiple random seeds. Given that the observed utility differences are on the order of 0.01–0.02 (e.g., 0.393 vs. 0.412 under the plug-in adversary for Bike Sharing), these could be within the noise range. The evaluation is also narrow: only two regression datasets, only the self-orthogonality case ($\mathcal{H} = \{h(v)=v\}$), and only one-dimensional outcomes. The paper's most striking theoretical claim (the decision-calibration collapse) is not tested experimentally. While the paper's primary contribution is theoretical, the empirical section as presented is too thin to independently validate the framework's practical behavior.

2. **The handling of approximate $\mathcal{H}$-calibration is deferred to an appendix that is not available in the main text.** The paper acknowledges (line 91) that "in Appendix B we also discuss scenarios in which only approximate $\mathcal{H}$-calibration is available." Since all practical settings involve finite-sample approximation error, the main body would benefit from at least a qualitative discussion of robustness to $\epsilon$-approximate calibration (e.g., how quickly the minimax value degrades). The current framing in the main text presents the results as exact, which could misleadingly suggest stronger practical guarantees than are established in the visible text.

3. **The construction of adversarial test distributions used in experiments is not described in the main text.** Table 1 reports performance under two adversarial evaluations that "respect $\mathcal{H}$-calibration," but how these adversaries are constructed algorithmically is absent from the main body. This harms verifiability of the empirical claims. (If this is detailed in the appendix, it should at least be summarized in the main text.)

### Trivial
- The paper could benefit from a brief statement clarifying that the marginal of $f(X)$ is held fixed because the expectation in Equation (5) is over $X \sim \mathcal{D}$ (the true, fixed distribution). This is implicit from the definitions but not explicitly restated, which could prevent the kind of misinterpretation raised in review.

## Nice-to-Haves
- Extending the experiments to a multiclass classification task with decision calibration would provide direct validation of Theorem 4.1.
- Reporting error bars and multiple-trial statistics would substantially strengthen the empirical claims.
- An algorithm box (pseudocode) for computing $a_{\text{robust}}$ given a calibration set and finite $\mathcal{H}$ would improve reproducibility.
- A visualization of the worst-case $q^*(v)$ for the self-orthogonality setting would build intuition.

## Removed Points

The following points from the reviews were removed with justification:

- **"The minimax formulation (5) fixes the marginal distribution of forecasts while the calibration constraints (2) are joint moment conditions, and the paper does not justify why marginal uncertainty can be ignored."** — This criticism misinterprets the problem setup. The formulation fixes the distribution of $X$ (hence $f(X)$) because the decision maker has access to a calibration sample from $\mathcal{D}$. The adversary chooses $q$, the conditional expectation, not the marginal. This is a clear modeling choice, not an oversight. The paper states (lines 93–103) that $\mathcal{Q}$ consists of "candidate conditional expectations" and the objective is an expectation over $X\sim\mathcal{D}$. The critic's suggestion to also let the adversary choose the marginal would be a different (broader) problem that the paper never claims to solve. A brief clarifying statement would help, but this is not a weakness of the presented formulation.

- **"The paper's main results assume exact $\mathcal{H}$-calibration... the analysis of approximate calibration is deferred to an appendix"** characterized as a structural limitation. — The paper explicitly acknowledges this scope limitation (line 91) and references Appendix B. Purely theoretical papers routinely state results for exact conditions and discuss approximations separately. This is standard practice, not a flaw.

- **"Without the proof (in the appendix), it is impossible to assess technical assumptions (e.g., compactness of the policy space, existence of a dual)"** — Standard for conference papers; proofs are in the appendix. The main text states that the dual objective is concave and the primal admits a saddle point (line 127, 147). No grounds to doubt the technical correctness given the paper's framing.

- **"Proposition 4.4 is a standard first-order condition... the paper should note that stationarity is only approximate in practice"** — This applies to essentially every paper using gradient-based training. It is a generic implementation detail.

- **"The experiments do not compare with any baseline beyond plug-in"** — The paper's robust rule is itself compared to the plug-in baseline, which is the natural comparison. Adding recalibration baselines would be nice but is not a required comparison for this paper's contribution.

- **Various formatting/presentation nitpicks** — These are parser artifacts or minor style preferences.

## Novel Insights

None beyond the paper's own contributions. The most noteworthy observation is the cross-review disagreement about the marginal-fixing issue: one reviewer interprets it as a structural gap, but a close reading of the paper shows it is a clear modeling choice (the adversary chooses only $q$; the marginal of $f(X)$ is determined by the fixed $X$ distribution). The paper could preempt this confusion with one clarifying sentence, but the formulation is correct as written.

## Suggestions

- Add a brief clarifying sentence in Section 2 when introducing Equation (5): state explicitly that the marginal distribution of $X$ (hence $f(X)$) is held fixed because it is determined by the true distribution $\mathcal{D}$ from which the decision maker has a calibration sample; the adversary's choice is restricted to the conditional expectation $q$.
- Include at least a summary of how the adversarial test distributions in Section 5 are constructed, or add a sentence pointing to the appendix section.
- Add standard errors or bootstrap confidence intervals to Table 1, and run experiments with multiple random train/calibration/test splits.
- Add a brief discussion in the main text (1–2 paragraphs) on how the results change under $\epsilon$-approximate $\mathcal{H}$-calibration, or at minimum state the known degradation rate from Appendix B.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>