## Summary
This paper presents R2PS, the first approach to worst-case robust real-time pursuit strategies for graph-based pursuit-evasion games (PEGs) under partial observability. The contribution spans three levels: (1) theoretical proof that the same DP distance table yields optimal strategies for both synchronous and asynchronous evader moves (Lemma 1, Theorem 2, Corollary 1, Theorem 3), (2) a belief preservation mechanism (Eqs 4–7) that efficiently compresses observation history into a tractable belief state for partially observable decision-making, and (3) a cross-graph RL training scheme that embeds belief preservation into the EPG framework, producing a GNN policy that generalizes zero-shot to unseen real-world graphs. The method substantially outperforms PSRO trained directly on test graphs and achieves real-time inference (~0.008s vs 6–139s for DP).

## Strengths
- **Theoretical unification of synchronous and asynchronous settings under a single DP framework**: Lemma 1 establishes a minimax fixed-point property of the distance table D, and Theorem 2 proves that μ* (Eq 1) guarantees capture within d steps while ν* (Eq 3) guarantees evasion for at least d steps against any opponent. Theorem 3 characterizes when evasion is perpetual (D(s)=∞). This extends prior work (Lu et al., 2025a) which addressed only synchronous moves.
- **Effective belief preservation mechanism for partial observability**: The belief update (Eq 7) and belief-averaged policy (Eq 6) operate in Õ(|V|) per timestep, avoiding exponential history blowup. Table 1 shows DP_belief substantially outperforms DP_Pos across all 10 test graphs (e.g., 0.94 vs 0.69 on Eiffel Tower, 0.87 vs 0.47 on Sydney Opera House). Lemma 2 guarantees both reduce to the optimal perfect-information policy when observations are unlimited.
- **Strong zero-shot generalization dramatically outperforming PSRO**: Table 2 shows the R2PS policy (trained on 300 unseen graphs) achieves far higher success rates against DP_async compared to PSRO trained directly on the same test graphs (e.g., 0.99 vs 0.03 on Downtown Map, 0.95 vs 0.04 on Times Square). The multi-opponent evaluation across 10 diverse real-world topologies provides thorough evidence.
- **Real-time feasibility convincingly demonstrated**: Table 3 shows ~0.008s inference on large graphs (744–2065 nodes) vs 6–139s for DP recomputation. The formal complexity analysis (O(n²m) for RL vs Õ(n^(m+1)) for DP) aligns with empirical results.
- **Belief update design validated through informative ablations**: Table 4 shows reducing belief update frequency sharply degrades performance (Downtown Map: 0.92 → 0.61 → 0.39 against BR_async), while using known opponent information in the belief update improves performance — confirming the mechanism is both essential and capable of leveraging better opponent models when available.

## Weaknesses

### Fatal
None.

### Major
- **The "worst-case robust" claim is overstated relative to BR_async results**: Against BR_async — an evader trained for 30,000 episodes specifically to exploit the learned pursuer policy — success rates drop to 0.27 (Times Square), 0.10 (Hollywood), 0.20 (Sagrada Familia), and 0.23 (The Bund). The DP evader ν* is provably optimal in the game-theoretic sense (Theorem 2), but the gap between DP_async and BR_async results demonstrates the learned RL policy has exploitable blind spots that the DP-optimal evader does not probe. The paper's framing as achieving "worst-case robust" strategies should be tempered — the robustness demonstrated is with respect to the game-theoretic optimal evader, not a fully adaptive worst-case adversary trained against the specific policy. The paper should explicitly acknowledge this distinction and discuss it as a limitation.
- **No statistical measures reported for any experimental results**: Across Tables 1–4, no variance, standard deviation, standard error, or confidence intervals are reported. While Table 1 averages over 500 tests, the absence of uncertainty measures in Tables 2–4 makes it impossible to assess whether observed differences are statistically meaningful — particularly for comparisons where the gap is modest (e.g., DP_belief vs DP_Pos on Sagrada Familia: 0.36 vs 0.24).

### Minor
- **Only m=2 pursuers tested empirically**: The DP complexity scales exponentially in m (Õ(n^(m+1))), which is precisely the regime where the RL approach should provide the greatest advantage. Testing with m=3 on smaller graphs would strengthen the scalability argument.
- **The initial-position-revealed assumption deserves explicit discussion**: The partial observability model assumes the evader's initial position is revealed (line 135) and only becomes uncertain after the game begins. While motivated by a guard/intruder scenario, this makes the problem substantially easier than standard POMDP formulations. The paper would benefit from discussing how this affects problem difficulty and whether the approach degrades under greater initial uncertainty.
- **No limitations section**: The conclusion (Section 6) is entirely positive. A brief limitations discussion acknowledging the BR_async gap, m=2 limitation, and initial-position assumption would improve scholarly presentation.

### Trivial
- **Asynchronous move definition could be clearer in Section 2.1**: Line 49 says the evader "decide[s] after the pursuers' move" but does not explicitly state what information the evader observes. Equation (3) in Section 3.1 clarifies this (n_p is the pursuer's chosen action), but a reader encountering Section 2.1 alone may be confused.
- **Training graph statistics sparse**: Line 238 mentions "150 random urban locations from Google Maps" without providing statistics (node counts, degree distributions) about the training graphs.

## Nice-to-Haves
- Incorporating best-response training (e.g., PSRO-style population updates) into the training loop could help close the BR_async performance gap and move the policy closer to genuine worst-case robustness.
- Providing proof sketches for Lemma 1 and Theorem 2 in the main text would help readers assess plausibility without consulting the appendix.
- Discussing sensitivity to the uniform evader-policy assumption in the belief update (Eq 7) would strengthen the analysis, since Table 4 shows using the true opponent policy improves performance.

## Removed Points
These points are flagged to be removed, treat them with caution:
- HC's claim that "the introduction sets up a straw-man comparison" — REMOVED. The paper correctly notes that prior work does not handle the evader-having-stronger-observations case, and the paper itself addresses this asymmetry. The criticism misreads the claim.
- HC's point about "the relationship to the broader POMDP literature is underdeveloped" — REMOVED per hard rule: do not mention missing related works.
- HC's speculation that "PSRO might be undertrained" — REMOVED as speculative; 10 iterations × 10K episodes is a standard and reasonable PSRO budget, and the performance gap is large enough to be convincing.
- HC's point about proof sketches being only in appendix — MOVED to Nice-to-Haves as a presentation preference.
- SF generic strengths about "important problem" — DROPPED as they lack concrete grounding.

## Novel Insights
The core insight — that the same DP distance table D simultaneously encodes optimal strategies for both synchronous and asynchronous move settings, and that this table can be combined with a belief-averaging mechanism to create a computationally tractable partially observable policy — represents a genuinely novel unification. Prior work treated these as separate problems; the paper shows they collapse into a single framework, enabling efficient cross-graph RL training for zero-shot generalization.

## Suggestions
- Temper the "worst-case robust" claim to "robust against the game-theoretic optimal evader" and add a brief discussion of the BR_async gap as a limitation.
- Report standard deviations or confidence intervals for all experimental results, especially Tables 2–4.
- Add a concise limitations subsection.

## Score Calibration
**Round-1 bracket**: 5.5–7.0, based on comparison against TSP generalization (3.00, Reject), Breaking Curse of Multiagency RMG (5.00, Reject), Dec-POMFC (6.33, Accept), and HEPi (8.00, Accept).

**Round-2 narrowing**: Compared against:
- GRAD (5.33, Accept): Our paper is clearly stronger — more theoretical depth, more comprehensive experiments, clearer practical value.
- Dec-POMFC (6.33, Accept): Comparable — similar theory+experiments profile, comparable limitations. Our paper has stronger empirical results.
- ACCES (6.50, Accept): Our paper has comparable theoretical contribution and stronger empirical evaluation.
- Beyond Worst-case Attacks (7.00, Accept): Our paper falls below this — BWA has a more compelling theoretical framework and better-justified claims.

**Final score**: 6.0. The paper makes a solid contribution with genuine theoretical and practical value, but the "worst-case robust" overclaiming and missing statistical rigor prevent a higher score.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>