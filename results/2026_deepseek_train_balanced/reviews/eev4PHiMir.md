## Summary

This paper studies the stationary distribution of SGD. It first proves a "Law of Balance" (Theorem 1): under rescaling symmetry in the loss, SGD drives the parameter norm difference ||u||² − ||w||² to zero at stationarity — a non-perturbative effect that distinguishes SGD from both GD and naive Langevin dynamics. It then applies this result to derive closed-form stationary distributions for diagonal linear networks of arbitrary depth and width, revealing a phase transition at a critical noise level T_c, depth-dependent power-law tails, and a "fluctuation inversion" where variance decreases as noise increases. The analysis establishes a provable qualitative difference between D=1 and D>1 networks.

## Strengths

- **Nonperturbative Law of Balance (Theorem 1)** — The paper proves that under rescaling symmetry, ||u||² − ||w||² decays at a rate governed by T and the gradient covariance matrices, with explicit O(1) bounds at stationarity (Eq. 65–66). This result is independent of the loss function and architecture, cleanly separating SGD from both GD and isotropic Langevin dynamics. The connection to Noether's theorem is conceptually insightful and elevates the result beyond a technical lemma.

- **First closed-form stationary distribution for a globally nonconvex nonlinear model** — For diagonal linear networks of arbitrary depth and width, the paper derives analytical stationary distributions (Eq. 148–149, Eq. 165) that expose nontrivial structure: a phase transition at T_c = β₂/α₃, power-law tails with depth-dependent exponent v^{−5+3/(D+1)}, and fluctuation inversion. These are concrete, analytically derived predictions that cannot be obtained from local approximations or isotropic-noise models — a significant technical achievement within the studied model class.

- **Provable qualitative distinction between depths (Theorem 2)** — The paper proves that for D=1, log|v_i| − log|v_j| is conserved at stationarity, whereas for D>1, |v_i|² − |v_j|² decays to zero. This establishes a fundamental dynamical difference between shallow and deep diagonal networks and corroborates earlier findings (ziyin2022exact).

- **Width–depth–learning-rate scaling law** — From the D→∞ limit, the paper derives the scaling relation d/D · S/η = const (Eq. 228), connecting architectural choices (width/depth) to training hyperparameters (batch size/learning rate). This extends the known η/S scaling (hoffer2017train) to incorporate architecture, producing a testable prediction.

## Weaknesses

### Fatal

None.

### Major

- **Claims about practical deep learning outstrip what the diagonal-linear-network model can support.** The paper asserts that its theory "offers a direct explanation of why the divergence of loss does not happen" for the edge-of-stability phenomenon (line 213), that deeper models have "a generalization advantage" and "an optimization advantage" (line 176), and that the scaling law d/D · S/η = const governs training (line 228). These are stated as general truths about deep learning, but the entire analysis is confined to diagonal linear networks — a toy model whose limited expressivity the paper itself acknowledges (line 96). The edge-of-stability explanation is particularly problematic: that phenomenon involves discrete-time dynamics in non-diagonal, nonlinear networks operating at large learning rates where the continuous-time SDE (Eq. 3) is a poor approximation. The paper provides no bridging argument, no experiment on non-diagonal real-world architectures that isolates the claimed mechanism, and no test of whether the discrete-time SGD stationary distribution matches the SDE prediction in the regime where the phase transitions occur. The MNIST experiment (Fig. 3, right) tests only η ∝ 1/D on fully-connected tanh networks (not diagonal linear networks), providing only weak qualitative support for a scaling law that involves width, depth, batch size, and learning rate jointly.

- **Domain of validity of the continuous-time SDE approximation is not examined.** The paper replaces discrete-time SGD (Eq. 1) with a continuous-time SDE (Eq. 3) and acknowledges this at line 16. However, the most striking predictions — the phase transition at T_c, the collapse to a delta distribution, the fluctuation inversion — occur at large T = η/S, i.e., large learning rate or small batch size, which is precisely where the continuous-time approximation is weakest. The paper never discusses when the approximation breaks down, whether the predicted phenomena survive in discrete time, or whether the stationary distribution of the continuous SDE approximates the long-run behavior of discrete SGD in the regimes studied. This is a gap that directly affects the credibility of the paper's headline claims.

### Minor

- **Experimental validation lacks statistical rigor.** The experiments show single trajectories or histograms without error bars, multiple seeds, or systematic hyperparameter sweeps. The power-law tail prediction v^{−5+3/(D+1)} is a crisp, falsifiable quantitative claim, but Fig. 3 (left) only shows a curve resembling a power law without extracting the exponent or providing confidence intervals. While illustrative experiments are acceptable for a theory paper, the strength of the claims (phase transitions, scaling law) warrants at least basic quantitative validation.

- **Positive definiteness assumption for C₁ and C₂ is stated without justification.** The balancing bounds (Eq. 65–66) rely on C₁ and C₂ being positive definite, described as "common" (line 59). The paper does not characterize when this holds or provide counterexamples, leaving the generality of the O(1) stationarity bound incompletely specified.

- **The five-regime classification (Fig. 3) and maximum likelihood estimator analysis depend on a specific data distribution** (x∼N(0,1) with Gaussian noise). It is unclear how generic these regimes are, and the paper does not test whether the qualitative picture changes with different data statistics.

- **No limitations section.** The paper acknowledges the continuous-time approximation (line 16), the restricted model class (line 96), and the Δ>0 and E[xy]>0 assumptions (lines 115, 150) in passing, but never synthesizes them into an honest assessment of the theory's scope. This makes it harder for readers to calibrate the strength of the conclusions.

### Trivial

None.

## Nice-to-Haves

- Validate the power-law tail exponent quantitatively with log-log fits and confidence intervals for several depths.
- Provide a short derivation sketch of how the Fokker-Planck equation is solved (in main text) to make the paper's central technical contribution more self-contained.
- Test the scaling law on real networks by jointly varying width, depth, learning rate, and batch size in controlled experiments.
- Explicitly note that the continuous-time approximation's validity is weakest where the most striking predictions arise, and offer a numerical test of whether the predictions survive in discrete-time SGD.
- Add a brief limitations paragraph.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"O(1) vs O(T²) conflation"** — The harsh critic claimed the paper confuses per-step and stationary-distribution differences. In fact, line 67 explicitly distinguishes "per unit time step" (O(T²)) from "at stationarity" (O(1)). The criticism misreads the paper.

- **"Straw man about ReLU networks"** — The footnote on line 39 ("had it been the case, no linear network or ReLU network can be trained with SGD") is a valid hypothetical consequence of the naive Langevin model's divergence prediction, not a rhetorical straw man.

- **"Missing derivations in main text"** — The critic notes the stationary distribution derivation is absent from the main text. Per instructions, the appendix (where derivations reside) is stripped by the parser. This is a parsing artifact, not an author failing.

- **"Prior work comparison underdeveloped"** — The paper acknowledges Ref. [mori2022power]'s result (line 122) and delineates its own advance as extending to deeper networks via symmetry. The comparison is adequate.

- **Strength Finder generic/superficial strengths** — None found; all listed strengths are specific and evidence-backed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Scope the claims to match the model.** Rewrite the Discussion and parts of Section 3 to clearly separate what is proven for diagonal linear networks from what is hypothesized about real networks. The edge-of-stability and generalization-advantage claims should be demoted to suggestive observations or hypotheses motivated by the toy model, not presented as explanations of empirically observed phenomena.
2. **Address the continuous-time gap explicitly.** Add a paragraph that discusses when the SDE approximation is reliable and when it is expected to fail. Provide at least a numerical comparison between the SDE stationary distribution and discrete-time SGD trajectories for the diagonal linear network at large T.
3. **Add error bars and quantitative validation.** Include multiple seeds and, for the power-law tail prediction, extract the exponent via log-log regression with confidence intervals.
4. **Add a limitations paragraph** synthesizing: the diagonal-linear-network model class, the continuous-time approximation, the Δ>0 and E[xy]>0 assumptions, and what empirical validation would be needed to extend the conclusions to realistic architectures.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>