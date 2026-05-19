- Decision: Reject
- Avg Score: 5.60
- Scores: 6, 5, 5, 6, 6
Now I have all the evidence I need. Let me synthesize the final review.

## Summary
This paper introduces Multiplayer Federated Learning (MpFL), a framework that models FL clients as rational players in an n-player game seeking a Nash equilibrium, and proposes PEARL-SGD, a communication-efficient local SGD algorithm for this setting. The paper provides theoretical convergence guarantees (linear in the deterministic setting, Õ(1/T) in the stochastic setting) and shows that with an appropriate synchronization interval τ, the communication complexity improves to Θ(√T). Experiments on synthetic quadratic games verify the theoretical predictions.

## Strengths
- **Novel game-theoretic FL formulation**: The paper introduces MpFL, which models clients as rational players with individual utility functions seeking a Nash equilibrium, directly addressing non-cooperative scenarios that prior FL frameworks do not handle. Section 2 and Figure 1 clearly articulate this distinction.
- **Provable linear convergence in the deterministic setting**: Theorem 3.3 proves deterministic PEARL-SGD converges linearly to the equilibrium for any τ>1 under convexity, smoothness, QSM, and SCO — a nontrivial result since local SGD for finite-sum minimization converges only to a neighborhood even without noise. The paper demonstrates tightness by recovering GDA rates when τ=1.
- **Communication complexity improvement in the stochastic setting**: Corollary 3.5 shows that PEARL-SGD achieves Õ(1/T) convergence with communication complexity Θ(√T) when τ is chosen optimally. This is a concrete theoretical improvement over the fully communicating baseline.
- **Precise characterization of player drift**: Lemma 3.8 provides a tight bound on the local error from multiple local SGD steps, analogous to client drift bounds in classical FL but derived for this new multiplayer setting.

## Weaknesses

### Fatal
None.

### Major
- **Empirical evaluation is limited to synthetic quadratic problems with minimal baselines.** Experiments only use constructed quadratic minimax and n-player games (Section 4). The sole comparative baseline is τ=1 (no local steps) of the same algorithm. For the minimax setting (Section 4.1), which is a special case of federated minimax optimization, a comparison to Local SGDA (Deng & Mahdavi, 2021; Sharma et al., 2022) would be a natural and feasible baseline. The paper claims "extensive numerical experiments" (Section 1) but does not demonstrate that PEARL-SGD offers any advantage over existing methods designed for overlapping settings. While the experiments correctly verify the theory, they do not establish the practical utility of the framework beyond self-validation. A single real-data experiment or a comparison to a relevant existing algorithm would substantially strengthen the paper.
- **Strong theoretical assumptions are not discussed in the context of practical applicability.** Convergence is proved under convexity (Assumption 2.1), quasi-strong monotonicity (Assumption 3.1), and star-cocoercivity (Assumption 3.2). The paper cites prior work using these assumptions (Loizou et al., 2021; Beznosikov et al., 2023) but does not discuss what realistic federated learning problems satisfy them, nor does it provide any non-quadratic example. Since the paper frames MpFL as a practical FL framework and not merely a theoretical exercise, the reader is left uncertain about the scope of applicability. The paper would benefit from discussing limitations or providing concrete examples beyond constructed quadratics.

### Minor
- **Missing comparison in the overlapping minimax setting.** The paper correctly distinguishes MpFL from federated minimax optimization (Section 2.2), noting that in MpFL each client is a single player. However, the minimax experiment (Section 4.1) is exactly a 2-player setting where each player is a single client. In this case, existing Local SGDA algorithms (which handle the minimax setting with multiple clients per player) are not directly applicable, but a 2-client Local SGDA or a simple baseline like independent per-player SGD (no communication) would help contextualize the results.
- **No discussion of the total communication volume.** The paper acknowledges the per-round overhead (line 125: "transferring D-dimensional vector... This is a significant computational overhead") and aims to reduce communication frequency. However, the central claim of "less communications" is expressed only in terms of round count. A back-of-the-envelope comparison of total communication volume (bits × rounds) versus classical FL would help the reader evaluate the practical trade-off, especially since broadcasting all n models each round is more expensive per round than classical FL's single-model broadcast.
- **The paper does not discuss privacy implications.** In MpFL, all players' full model parameters are broadcast to all other players every synchronization round, unlike classical FL where only aggregated model updates are shared. This is a significant privacy consideration worth acknowledging.

### Trivial
- In the experiment descriptions, the heatmap (Figure 3) is mentioned as showing log relative errors but the caption does not specify whether it is deterministic or stochastic.

## Nice-to-Haves
- A comparison of total communication volume (accounting for the D-dimensional broadcast) versus classical FL baselines, even analytically, would strengthen the "less communications" claim.
- A concrete ML-inspired application — e.g., a two-player robust learning task or a small-scale multi-agent RL problem — would demonstrate the framework's relevance beyond quadratic games.
- A brief discussion of what practical problems satisfy QSM and SCO, even if speculative, would help practitioners assess the framework's scope.

## Removed Points
These points were flagged but are removed or weakened after cross-checking against the paper:

1. **"The paper does not define L_max"** — REMOVED. L_max = max{L_1, ..., L_n} is explicitly defined in Theorem 3.3 (line 152) and Lemma 3.7 (line 201). The critic missed this.

2. **"The paper does not account for per-round communication cost scaling with n"** — REMOVED. Line 125 explicitly states: "Note that the synchronization step involves transferring D = (d_1+...+d_n)-dimensional vector... This is a significant computational overhead." The paper acknowledges this and frames τ>1 precisely as a way to reduce this overhead. What remains is a minor suggestion to also discuss total communication volume, not a missing acknowledgment.

3. **"No comparison to FedAvg or personalized FL methods (Ditto, pFedMe)"** — REMOVED. These methods solve a fundamentally different problem (cooperative FL where all clients minimize the same objective). MpFL is explicitly about non-cooperative settings; demanding comparison to methods that assume cooperation is a category error.

4. **"Data heterogeneity claim is misleading"** — REMOVED. The paper states (line 127) that convergence holds "without any assumption on players' data distributions D_i." This claim is about *data distributions*, not function properties. The assumptions on function classes (convexity, QSM, SCO) are orthogonal. The paper's statement is technically correct and standard in FL literature.

5. **"No comparison to non-cooperative baseline (independent training without communication)"** — WEAKENED to a minor point. Independent SGD without communication would not converge to a Nash equilibrium in a game, so it is not a meaningful baseline for the claim being tested. The critic's suggestion is addressed in the Nice-to-Haves.

6. **"Criticisms about missing appendix content, proof details, or related works"** — REMOVED per instructions (appendix content is stripped by the parser; missing related works cannot be verified without external sources).

7. **"Typos, formatting, and parsing artifacts"** — REMOVED per instructions.

## Novel Insights
The most interesting observation emerging from the reviews is the tension between the paper's framing as a practical FL framework and the strength of its theoretical assumptions. The paper is strongest when read as a theory contribution: it shows that local SGD can provably converge to a Nash equilibrium in an n-player convex game with QSM and SCO, and that periodic communication provably reduces communication rounds. However, the "FL" framing invites expectations (real data, comparisons to existing FL methods, privacy considerations) that the paper does not satisfy. This mismatch between framing and execution — rather than any technical flaw — accounts for most of the harsh criticism. A retooled version that either (a) fully embraces the theory framing with a proper survey of related distributed game-solving literature, or (b) adds realistic experiments and baselines to justify the FL framing, would be a stronger paper.

## Suggestions
1. **Add a baseline to the minimax experiment.** For the 2-player zero-sum setting (Section 4.1), compare against a simple Local SGDA implementation with the same τ parameter. This directly addresses the most straightforward overlapping setting.
2. **Discuss the practical scope of QSM and SCO.** Even a brief paragraph noting known problem classes (e.g., certain quadratic games, strongly convex-concave minimax, specific regularized objectives) that satisfy these conditions would help readers assess when MpFL applies.
3. **Include a total communication volume comparison.** Show analytically or empirically how the per-round D-dimensional broadcast trades off against the reduced round count, versus classical FL's d-dimensional broadcast.
4. **Acknowledge privacy limitations** in the conclusion or a limitations paragraph. The broadcast of all model parameters to all players is a departure from standard FL privacy norms and should be discussed.
