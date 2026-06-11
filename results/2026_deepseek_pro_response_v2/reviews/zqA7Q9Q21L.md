Now I have enough calibration data. Let me finalize.

**Round 2 comparison:**
- **STAGE (5.50, rejected):** The paper under review is clearly stronger — it has more diverse evaluation across 10 real-world graphs, stronger practical validation (Table 3 inference-time results), and a more complete pipeline. STAGE had concerns about computational complexity and limited baselines.
- **Dec-POMFC (6.33, accepted):** Comparable in contribution level. Both address partial observability in multi-agent settings, both have theoretical + practical contributions. Dec-POMFC had some restrictive assumptions and limited benchmark concerns. The paper under review has stronger practical validation but more notable evaluation weaknesses (PSRO comparison fairness, unaddressed RL-DP gap).
- **DRDA for POSGs (7.00, accepted):** The paper under review is clearly weaker. DRDA has deeper theoretical contributions (last-iterate convergence proofs, generalized Nash distribution) and more rigorous analysis. The paper under review's theoretical contributions are more incremental.

**Final score: 6.0.** The paper has genuine contributions (belief preservation mechanism, inference-time advantage, theoretical extension) and substantial empirical validation, but the PSRO comparison fairness and unaddressed RL-DP gap are material weaknesses that prevent a higher score.

Now let me write the final review.

---

Actually, let me reconsider the score once more. Looking at the NfgTransformer (6.00, accepted) — that paper had very split reviews (3, 8, 5, 8) with a reviewer questioning whether the equivariance claim was truly novel. The paper under review doesn't have such fundamental concerns — its contributions are well-scoped and validated, just with some evaluation gaps.

I think 6.0 is appropriate but on the lower side. I could also justify 6.5 given the strength of the belief mechanism and inference-time results. Let me go with 6.0 to be conservative given the PSRO and RL-DP issues.

Actually, one more thought: the paper clearly demonstrates practical value. The inference-time advantage alone (0.01s vs 101s on 1805-node graphs) is a significant contribution. The belief mechanism with thorough ablation is another. The theoretical extension, while incremental, is correct and complete. The PSRO comparison weakness is real but not fatal — the paper could address it in rebuttal by clarifying what PSRO received. The RL-DP gap is real but only on 3/10 graphs.

I'll go with 6.0 and an Accept decision (borderline).Now let me write the final review.

---

## Summary

This paper proposes R2PS, a framework for learning worst-case robust real-time pursuit strategies in graph-based pursuit-evasion games (PEGs) under partial observability. The work consists of three parts: (1) a theoretical extension proving that a DP distance-table algorithm from prior work yields optimal strategies under asynchronous evader moves, (2) a belief-preservation mechanism that tracks possible evader positions and weights them to construct observation-based pursuer policies, and (3) embedding this belief mechanism into an EPG-style cross-graph RL pipeline to train a GNN policy that generalizes zero-shot to unseen graphs.

## Strengths

- **Belief preservation mechanism is well-motivated, clearly designed, and empirically validated (Section 3.2, Table 1).** The belief-averaged policy (Eq. 6) consistently and substantially outperforms the position-extended minimax policy (Eq. 5), with improvements of 0.15–0.25 across all 10 test graphs (e.g., Grid Map: 0.78 vs 0.59; Eiffel Tower: 0.94 vs 0.69; Downtown: 0.90 vs 0.73). The ablation on belief update frequency (Table 4) further confirms that per-timestep belief maintenance is essential: reducing updates to every 2 or 3 steps causes severe degradation (e.g., Downtown drops from 0.92 to 0.61 to 0.39). This is a practical, effective mechanism for handling partial observability.

- **Inference-time advantage is convincingly demonstrated and constitutes the paper's strongest empirical result (Section 4.2, Table 3).** The paper provides an O(n²m) complexity bound for RL inference vs ~O(n^{m+1}) for DP recomputation, and validates it with concrete timing measurements: on the 1,805-node Times Square graph, RL inference takes 0.0098s (GPU) while DP takes 101s (CPU) — a four-order-of-magnitude gap. Across all seven large test graphs, the pattern holds. This directly supports the real-time applicability claim under dynamically changing graph structures.

- **The theoretical extension to asynchronous moves (Section 3.1) is clean and rigorous.** Lemma 1 establishes the minimax fixed-point property of the DP distance table. Theorem 2 proves that μ* guarantees capture within d steps and ν* avoids capture within less than d steps under asynchronous moves, with Corollary 1 certifying strict optimality. Theorem 3 closes the analysis by showing D(s)=∞ implies the evader can never be captured. The chain of reasoning is logically complete.

- **Zero-shot generalization across diverse graph topologies is demonstrated.** The RL policy, trained on 300 held-out synthetic and real-world graphs, is evaluated on 10 unseen real-world test graphs spanning grid, board-game, and 7 famous location maps (100–231 nodes in Table 1, scaled to 744–2,065 in Table 3) with varying average degrees (2.33–3.91) and diameters (18–38). The policy maintains non-trivial success rates even on the largest unseen graphs (e.g., 0.56 on Times Square at 1,805 nodes, 0.76 on Sydney Opera House at 744 nodes).

## Weaknesses

### Fatal

None.

### Major

- **The PSRO comparison does not isolate the effect of cross-graph training and is insufficiently analyzed.** The paper's headline empirical claim is that the proposed method "consistently outperforms the policy directly trained on the test graphs by the existing game RL approach" (abstract), resting on the PSRO comparison in Table 2. However, it is unclear whether PSRO was equipped with the same partial-observability machinery (belief preservation, Pos tracking) as the proposed method. If PSRO was not given these domain-specific mechanisms, the comparison measures whether belief preservation helps — not whether cross-graph training produces better strategies than in-distribution training. The paper should clarify what partial-observability handling PSRO received. The PSRO results (0.00 success against DP_async on 4 out of 10 graphs) also raise questions about whether the 10-iteration configuration was sufficient for PSRO to demonstrate its capabilities, although the 100K total episode budget is matched to the proposed method's 100K episodes.

- **The learned RL policy substantially underperforms the simpler DP_belief baseline on several graphs, and this is not acknowledged (Table 1 vs Table 2).** Comparing DP_belief (Table 1, observation range 2, against DP_async) with the RL policy (Table 2, against DP_async): on Hollywood Walk of Fame (0.48 vs 0.38), Sagrada Familia (0.36 vs 0.20), and The Bund (0.57 vs 0.25), the RL policy is meaningfully worse. Since the RL policy was trained with the DP_belief policy as guidance (β=0.1 KL term in Eq. 8), this gap represents a failure of policy distillation on these graphs. The paper does not discuss this gap, which undermines confidence in the RL training pipeline and makes it difficult to assess when the computationally cheaper DP alternative would be preferable.

### Minor

- **"Worst-case robust" framing is somewhat overclaimed relative to the BR_async results (Table 4).** The title and abstract emphasize "worst-case robust" strategies. Against the DP_async evader (the provably optimal evader in the paper's framework), the RL policy performs well. However, against the adaptively trained BR_async evader, success rates drop to 0.10 (Hollywood), 0.20 (Sagrada Familia), 0.27 (Times Square), and 0.23 (The Bund). The primary "worst-case" claim against DP_async is defensible, but the paper should more carefully delineate what adversarial settings the robustness does and does not extend to.

- **No variance or statistical significance reported for any success rates.** Success rates in Tables 1–4 are averaged over 500 tests (stated in Section 5.1), but no standard deviations, confidence intervals, or statistical tests are provided. This matters for borderline comparisons and for the BR_async results where some rates are very low and likely noisy.

- **Training and test graph distributions are not characterized.** The training set consists of 150 Dungeon maps + 150 Google Maps locations (max 500 nodes), while test graphs are 10 specific real-world locations. The paper does not analyze whether the training graphs differ systematically from the test graphs in topology, degree distribution, or size, which affects how strong the zero-shot generalization claim is.

### Trivial

None.

## Nice-to-Haves

- A within-architecture baseline (same GNN+SAC+belief-preservation, trained on each test graph individually) would cleanly isolate the contribution of cross-graph training from architectures and partial-observability mechanisms.
- Analysis of why policy distillation fails on Hollywood Walk of Fame, Sagrada Familia, and The Bund (e.g., does the GNN struggle with certain graph topologies?) would turn a weakness into an informative result.
- A discussion of when the uniform evader-policy assumption (Eq. 7) may be misleading would strengthen the belief mechanism analysis.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Without the appendix proofs it is difficult to assess their depth"** — REMOVED per hard rule: the parser strips appendix sections; proofs exist in the original submission.
- **"The shift between discounted-reward Nash equilibrium and timestep-based definition is not explicitly reconciled"** — REMOVED. The paper explicitly defines the asynchronous optimality criterion at line 49: "we say that a strategy is optimal... if the worst-case termination timesteps of all possible trajectories... are maximized/minimized." This is a clearly stated game extension, not a conceptual tension.
- **"The paper does not report PSRO results against BR_async"** — REMOVED as a standalone criticism. The BR_async evader is trained as a best-responder to the proposed method specifically; testing PSRO against it would not be directly meaningful without also training a best-responder against PSRO.
- **"The 'exponential improvement' argument (lines 195-196) is heuristic and not supported by formal analysis"** — REMOVED. The paper explicitly frames this as a hypothetical ideal case ("Imagine that a half space is excluded... In this ideal case...") and does not present it as a formal claim.
- **Strength Finder's unqualified PSRO superiority as the "single most important piece of evidence"** — contextualized given PSRO comparison concerns.

## Novel Insights

The belief preservation mechanism — averaging over a weighted belief distribution rather than taking the pessimistic max over all possible evader positions — addresses a concrete failure mode in partially observable pursuit: when the possible-position set grows large, the pure minimax policy becomes overly conservative and stagnates at "rest points." The empirical gap between DP_Pos and DP_belief (Table 1) demonstrates that this simple design choice has substantial practical consequences, and the ablation on belief update frequency (Table 4) shows the mechanism is genuinely load-bearing. This insight — that maintained belief distributions can productively guide minimax decision-making under partial observability in graph-based adversarial settings — is the paper's most transferable contribution.

## Suggestions

- Clarify exactly what observation model and input features PSRO received during training. If PSRO did not receive belief/Pos tracking, acknowledge that the comparison conflates partial-observability handling with cross-graph training.
- Add standard deviations or confidence intervals to Tables 1–4, or at minimum note the number of evaluation episodes and whether differences are statistically significant.
- Discuss the DP_belief vs. RL gap on the three problematic graphs — acknowledging limitations builds credibility and helps readers understand when each approach is appropriate.
- Qualify the "worst-case robust" claim to distinguish between robustness to graph structure changes (well-supported) and robustness to adaptively trained adversarial opponents (partially supported, with BR_async caveats).

## Calibration

**Round 1 bracket:** 5.5–7.0. The paper is stronger than 3.0-level rejected papers (major methodological gaps) and stronger than ~4.75-5.33 middle-band papers (platforms with thin experiments, evaluation fairness concerns, contradictory results). It falls short of 8.0 accepted papers (exceptionally clean execution, no significant methodological concerns).

**Round 2 narrowing:** Compared against Dec-POMFC (6.33, accepted), NfgTransformer (6.00, accepted), STAGE (5.50, rejected), and DRDA (7.00, accepted). The paper is comparable to Dec-POMFC in contribution level (both address partial observability with theory + practice), clearly better than STAGE (stronger validation, more complete pipeline), and clearly weaker than DRDA (shallower theoretical contributions).

**Anchor papers compared:**
- `fvTaoyH96Z` (2.33, Round 1): Environmental generalization in RL — much weaker, rejected for fundamental methodological gaps.
- `NIhRwzqhUz` (3.00, Round 1): Partially dynamic TSP — weaker, rejected for limited novelty.
- `DjHnxxlqwl` (4.75, Round 1): Urban Network Security Games platform — weaker, thin experiments, platform-focused rather than method-focused.
- `xAYOfMV264` (4.80, Round 1): Dual-agent adversarial framework — weaker, evaluation fairness concerns and contradictory results.
- `mxkm1Pr2PM` (5.33, Round 1/2): GNN as Mean Field Game — weaker, more conceptual, less empirical validation.
- `5btqauRdz0` (5.50, Round 2): Zero-shot GNN generalization (STAGE) — weaker, concerns about computational complexity and limited baselines.
- `DKfcxPxunu` (5.75, Round 2): Multi-task routing with zero-shot generalization — comparable in ambition but weaker execution.
- `4YESQqIys7` (6.00, Round 2): NfgTransformer — comparable, innovative game-theoretic architecture with split reviews.
- `GvsCOOPxoI` (6.17, Round 2): Provable learning for DEC-POMDPs — comparable, theoretical contributions with some experimental concerns.
- `klpdEThT8q` (6.25, Round 2): MA²E for partial observability in MARL — comparable, accepted with similar contribution level.
- `99tKiMVJhY` (6.33, Round 2): Dec-POMFC — most similar anchor, comparable contribution level with theory + experiments.
- `KD5nJUgeW4` (7.00, Round 2): DRDA for POSGs — clearly stronger, deeper theoretical contributions with convergence proofs.
- `stUKwWBuBm` (8.00, Round 1): Tractable MARL via behavioral economics — much stronger, deeper theory and cleaner execution.
- `KbetDM33YG` (8.00, Round 1): Online GNN evaluation — much stronger, novel problem with thorough validation.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>