Now I have verified the relevant claims against the actual paper. Let me construct the consolidated review.

---

## Summary

This paper introduces Multiplayer Federated Learning (MpFL), a framework that models FL clients as rational players with individual utility functions seeking a Nash equilibrium, and proposes PEARL-SGD (Per-Player Local SGD). The algorithm allows each player to perform multiple local SGD steps before synchronizing via a central server. The paper provides convergence guarantees under quasi-strong monotonicity (QSM) and star-cocoercivity (SCO) assumptions, showing linear convergence in the deterministic setting and Õ(1/T) convergence with Θ(√T) communication rounds in the stochastic setting. Experiments on quadratic games validate the theory.

## Strengths

1. **Novel game-theoretic formulation bridging FL and multiplayer games.** The paper explicitly models clients as strategic players with potentially competing objectives, which classical FL's cooperative paradigm cannot address. This framing is clearly motivated (Section 1) and properly distinguished from both classical FL and federated minimax optimization (Section 2.2). The scope and differences from existing frameworks are transparently discussed.

2. **Rigorous theoretical analysis with tight rates.** The convergence analysis is thorough and non-trivial. Key lemmas (3.7–3.9) cleanly isolate the player drift and local error terms. The deterministic result (Theorem 3.3) recovers the τ=1 SGDA rate of Loizou et al. (2021) as a special case, confirming tightness. The decreasing step-size result (Theorem 3.6) achieves exact convergence without a pre-specified horizon, which is a meaningful differentiator from many local SGD analyses that only give neighborhood convergence under constant step-sizes.

3. **Explicit handling of heterogeneous data without similarity assumptions.** The paper states (line 127 and Section 2.1) that no restrictive assumptions on data distributions or function similarity between players are needed. The analysis holds in the fully heterogeneous setting, which is stronger than standard FL analyses that often require bounded gradient dissimilarity.

4. **Clean experimental validation that matches the theory.** The experiments (Figures 2, 3, 4) cover both minimax (n=2) and multiplayer (n=5) settings. The deterministic case shows overlapping convergence curves for all τ as predicted; the stochastic case shows clear communication savings as τ increases, directly confirming Corollary 3.5. The heatmap (Figure 3) independently verifies the predicted γ ∝ 1/τ relationship.

5. **The paper is transparent about its own limitations.** It explicitly states "no communication gain is achieved via our analysis" in the deterministic setting (line 26) and acknowledges that the per-round communication vector has dimension D = Σ d_i, which is "a significant computational overhead" (line 125). This candor is commendable and should be recognized.

## Weaknesses

### Fatal
None.

### Major

1. **The title and high-level framing overclaim relative to the paper's own internal comparison.** The paper claims "less communications" (title, abstract), but the comparison is against the τ=1 baseline *within MpFL* — not against classical FL or any external baseline. Since every round in MpFL transmits D = Σ d_i parameters (scaling with the number of players), while classical FL transmits only d (one model), a reader could reasonably infer a different claim than what is actually proved. The paper acknowledges this overhead (line 125) but never provides a total-bit-cost comparison (e.g., total transmitted parameters vs. communication rounds) to show the regime where τ>1 actually transmits *fewer total bits* than τ=1. The communication complexity result is stated in terms of rounds (T/τ = Θ(√T)), which is standard in the local SGD literature, but the title's "less communications" is ambiguous. Adding a simple total-communication-cost analysis (e.g., total bits = R × D = (T/τ) × D) and showing the crossover point where the round savings dominate the per-round overhead would substantiate the claim.

### Minor

2. **The theory covers a specific, not broad, class of games, and the paper could be more explicit about this.** The QSM and SCO assumptions inherited from SGDA (Loizou et al., 2021) together induce a strongly-monotone-like structure on the joint gradient operator 𝔽. The paper notes that QSM is "more general than strong monotonicity" (line 140), which is correct — QSM only requires the inequality at x⋆ rather than all pairs. Nevertheless, the combination of QSM+SCO is restrictive, and the paper does not provide easily verifiable sufficient conditions on the individual f_i that would imply these assumptions. The motivating examples (Cournot competition, electricity markets, mobile robot control) are not checked against QSM+SCO. Adding a paragraph with concrete sufficient conditions (e.g., strongly convex f_i(·; x⁻ⁱ) with Lipschitz cross-gradient interactions) would increase the practical value of the theory. This does not invalidate the results but limits the paper's reach.

3. **Practical selection of τ depends on unknown problem parameters.** The optimal τ = O(√(μT / L_max)) (Corollary 3.5) depends on the strong monotonicity modulus μ and the maximum smoothness constant L_max. The decreasing step-size result (Theorem 3.6) avoids needing T in advance but still requires τ to be set beforehand based on these unknown quantities. The paper provides no practical guidance (e.g., grid search over τ, doubling strategy, or estimation of μ/L_max from local data) for how a practitioner would choose τ. This is a common gap in optimization theory but worth flagging.

### Trivial

None.

## Nice-to-Haves

- A plot or table comparing total transmitted parameters under τ=1 vs. τ>1 in the stochastic setting, showing the crossover point where larger τ actually saves total bandwidth.
- A brief comparison (even qualitative/discussion-only) to parallel best-response dynamics or consensus-based distributed Nash seeking, to position MpFL within the broader game-theoretic optimization literature.

## Removed Points

- **Criticism that MpFL "eliminates two of FL's defining features" (privacy, server aggregation without sharing raw models).** The paper explicitly acknowledges the per-round communication cost and the difference from classical FL (line 125: "different from communication from classical FL where the dimension does not scale with n"). The paper is proposing a *new framework* (MpFL) that relaxes classical FL assumptions; criticizing it for not preserving all FL properties is a category error. MpFL is presented as an extension beyond cooperative FL, not a drop-in replacement.

- **Claim that QSM+SCO "forces the problem to be strongly monotone."** The paper correctly states QSM is "more general than strong monotonicity" (line 140). QSM only requires the inequality at x⋆, not for all pairs (x, y). The critic's assertion that QSM+SCO implies strong monotonicity is factually incorrect. The combined assumptions are strong but not equivalent to full strong monotonicity.

- **"The paper never discusses existence/uniqueness of Nash equilibrium."** Assumption 3.1 explicitly states "There exists a unique equilibrium x⋆." The existence and uniqueness are built into the assumption. This is standard — the QSM assumption itself guarantees uniqueness.

- **"No comparison to other game-theoretic learning algorithms."** This is a scope-expansion request. The paper positions itself within the FL literature and explicitly compares to federated minimax optimization and classical FL (Section 2.2). Requesting a broader survey of distributed Nash seeking is outside the paper's stated scope and would not change its contribution.

- Several minor presentation and formatting nitpicks from the reviewer (parser artifacts, appendix references) — these are parser issues, not author errors.

## Novel Insights

The most interesting observation from the reviews is that PEARL-SGD's ability to achieve *exact* convergence (not just to a neighborhood) under decreasing step-sizes (Theorem 3.6) while maintaining the same asymptotic communication complexity as the constant-step-size neighborhood result is a genuinely non-trivial technical achievement. Most local SGD analyses in the minimax/game setting stop at neighborhood convergence. That the paper's analysis preserves exact convergence without additional correction mechanisms (e.g., gradient tracking) and without requiring data similarity assumptions is a meaningful technical contribution that receives less emphasis than it deserves.

## Suggestions

1. Revise the title or abstract to clarify that "less communications" means fewer synchronization rounds compared to the fully-synchronized MpFL baseline (τ=1), not compared to classical FL or in terms of total data transmitted. Add a brief total-communication-cost analysis (even in the appendix) showing the parameter regime where τ>1 actually reduces total transmitted bits.

2. Add a paragraph in Section 2 or 3 providing sufficient conditions on the individual f_i that imply QSM+SCO (e.g., strong convexity in xⁱ + bounded cross-gradient interactions), so practitioners can determine whether their problem falls within the theory's scope.

3. Include a brief practical discussion of how τ could be chosen in practice (e.g., via the observable quantities or a simple grid search), or at minimum acknowledge the limitation transparently.

## Score and Decision

The paper makes a solid contribution: it introduces a well-motivated new framework, provides rigorous non-trivial convergence theory, validates it experimentally, and is transparent about its scope and limitations. The weaknesses are about framing and completeness, not correctness. The communication cost concern (Major weakness 1) is real and should be addressed, but it does not invalidate the core theoretical contribution. The paper deserves acceptance with minor revisions.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>