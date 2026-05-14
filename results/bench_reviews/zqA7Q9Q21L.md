Now I have a thorough understanding of the paper and the calibration anchors. Let me write the final consolidated review.

---

## Summary

This paper addresses real-time pursuit strategies in graph-based pursuit-evasion games (PEGs) under partial observability. It makes three contributions: (1) a theoretical proof that a dynamic programming (DP) algorithm yields strictly optimal strategies when the evader moves asynchronously (seeing the pursuer's action first), (2) a belief preservation mechanism that extends DP-based policies to the partially observable setting by maintaining a distribution over possible evader positions, and (3) integration of this belief mechanism into the EPG framework to train a GNN-based pursuer policy that achieves zero-shot generalization to unseen real-world graphs.

## Strengths

- **Rigorous async-move theory**: Theorem 2 and Corollary 1 provide a clean proof that the DP-induced distance table yields strictly optimal strategies for both pursuer and evader under asynchronous moves. Lemma 1 establishes the minimax structure of the DP table, and Theorem 3 characterizes when capture is impossible. This is a non-trivial extension of prior DP analysis.

- **Belief preservation mechanism is principled and practical**: The belief update (Eq. 7) provides an efficient Õ(|V|) per-timestep method to track evader position uncertainty without the exponential blowup of full history tracking. Lemma 2 guarantees that when observability is unlimited, both the position-set policy and belief-averaged policy reduce to the provably optimal perfect-information policy. Empirically, belief averaging (DPbelief) consistently and substantially outperforms the naive position-set minimax policy (DPPos) across all test graphs (Table 1).

- **Effective zero-shot generalization**: The combination of belief preservation with cross-graph EPG training yields a GNN policy that, trained on synthetic and random graphs (never seeing test graphs), consistently outperforms PSRO trained directly on the test graphs against multiple evader strategies including the provably optimal DPasync evader (Table 2). Performance also scales well with more pursuers (Table 8) and larger observation ranges (Table 7).

- **Strong empirical efficiency**: The GNN policy runs in O(n²m) per timestep, achieving ~0.01s inference on graphs with ~2000 nodes versus >100s for DP recomputation (Table 3). This makes real-time pursuit feasible on dynamically changing graphs.

- **Thorough ablations**: Table 4 demonstrates that belief updates are crucial (reducing update frequency sharply degrades performance), and that incorporating known opponent policy further improves success. Table 7 shows monotonic improvement with observation range, confirming the policy can leverage better sensing without retraining.

## Weaknesses

### Fatal

None.

### Major

- **"Worst-case robust" framing conflates theoretical and empirical contributions**: The theoretical guarantees (Theorem 2, Corollary 1) apply to the asynchronous-move, perfect-information setting. The extension to partial observability via belief preservation is empirically validated — the paper explicitly acknowledges the distance table becomes "an optimistic estimator" under partial observability (Section 5.1). However, the title, abstract, and conclusion repeatedly use "worst-case robust" language for the partially observable setting without clearly separating the proved (async-move) from the empirical (partial observability) claims. The empirical evidence against DPasync and BRasync is strong, but the framing should be more precise about where theoretical guarantees end and empirical validation begins.

### Minor

- **PSRO baseline details are sparse**: The PSRO comparison uses 10 iterations × 10k episodes on each test graph. While this serves the valid purpose of demonstrating that zero-shot cross-graph generalization beats per-graph training, the paper does not report PSRO hyperparameters, network architecture, or population size. PSRO is known to need careful tuning and more iterations can help. However, this does not threaten the core claim — the paper's contribution is zero-shot generalization, and PSRO's scaling limitations in large state spaces are well-documented.

- **Belief update uses a uniform evader transition model**: When the evader's policy is unknown, the belief propagation (Eq. 7) assumes uniform movement to neighbors. The paper acknowledges this (line 440-441) and shows that knowing the true opponent policy improves results (Table 4, "Known Opponent" column). While the uniform assumption works well in practice, a brief analysis or empirical test of how the approximation error behaves under strategically evasive evaders (e.g., those that move to maximize pursuer uncertainty) would strengthen understanding of the mechanism's limits.

### Trivial

- The paper would benefit from a clearer separation in the introduction between which claims are theoretically proved (async-move optimality) and which are empirically demonstrated (partial observability robustness).

## Nice-to-Haves

- A small-scale comparison against a true POMDP/POSG solver (e.g., POMCP) on small graphs could help contextualize how close the belief-averaged DP policy is to optimal under partial observability, even if only on toy instances.
- Visualizations of belief evolution during pursuit (how the belief distribution shrinks upon observation and expands when unobserved) would help readers build intuition for the mechanism.
- A discussion of whether the uniform belief assumption could be replaced with a learned belief updater in future work.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Harsh Critic: "No proof that the resulting policy is robust against an evader that optimally exploits the pursuer's partial observability"** — REMOVED. The paper never claims theoretical optimality under partial observability. It explicitly states the distance table becomes an "optimistic estimator" (line 610). The empirical evaluation uses BRasync (best response directly trained against the RL policy) as a strong adversarial test.

- **Harsh Critic: "PSRO severely undertrained / 10 iterations is insufficient to reflect true potential"** — REMOVED as a major criticism. PSRO's scaling limitations are well-known. The comparison serves a specific purpose: demonstrating that zero-shot cross-graph generalization outperforms direct per-graph training. The paper should include more PSRO configuration details (raised as minor), but the comparison is not fundamentally unfair.

- **Harsh Critic: "Technical novelty beyond EPG is modest / belief update is simplistic"** — REMOVED as a standalone criticism. Building on prior work is standard practice, and simplicity that works efficiently is a feature. The async-move theoretical analysis is a genuine novel contribution, and the belief mechanism enables partial observability handling that EPG alone does not address.

- **Harsh Critic: "No ablation showing the effect of cross-graph diversity"** — REMOVED. This is scope creep; the paper already has substantial ablations (belief update frequency, known opponent, observation range, pursuer count).

- **Harsh Critic: "Missing comparisons with POMCP-style approaches on smaller graphs"** — MOVED to Nice-to-Haves. While such a comparison would be informative, it is not standard to require POMDP solver comparisons for a paper whose primary contribution is in graph-based PEGs with RL generalization.

- **Strength Finder: "Comprehensive experiments across 10 real-world graphs"** — KEPT as part of "Effective zero-shot generalization" strength. This is well-supported.

- **Harsh Critic: "The RL training pipeline (Section 4) is directly adopted from EPG"** — REMOVED as a criticism. The paper explicitly credits EPG and uses it as a framework. The contribution is extending EPG to handle partial observability via belief preservation, which EPG did not address.

- **Harsh Critic: "No formal bound or analysis of belief-update approximation error"** — PARTIALLY KEPT (as minor). The paper acknowledges the uniform assumption and tests against known opponent policy. A formal analysis would be nice but is not essential for an empirical systems contribution. The harsh critic's framing of this as a fatal gap is removed.

## Novel Insights

The paper's demonstration that a simple uniform belief-propagation mechanism, when combined with DP-derived distance tables and cross-graph adversarial RL, achieves strong zero-shot generalization under partial observability is genuinely interesting. It suggests that in graph-based PEGs, the perfect-information DP solution contains enough structural information that even a coarse belief approximation can effectively guide pursuit under limited observability — the distance table, though an "optimistic estimator" under partial observability, apparently provides a useful signal when averaged over likely evader positions.

## Suggestions

- Revise the title, abstract, and introduction to clearly delineate: (a) what is theoretically proved (async-move optimality under perfect information), and (b) what is empirically demonstrated (robustness under partial observability). Consider phrases like "empirically worst-case robust" for the partially observable setting.
- Add PSRO configuration details (network architecture, population size, hyperparameters) to Appendix C, even if brief, so readers can assess the fairness of the comparison.
- Consider adding a brief discussion (even one paragraph) about when the uniform belief assumption might fail — e.g., against an evader that deliberately exploits the pursuer's belief model to create uncertainty.

---

## Score Calibration

**Anchor papers considered:**

| Path | Avg Score | Comparison to paper under review |
|------|-----------|----------------------------------|
| QEcSLhfOoQ (Minimax Optimal Adversarial RL) | 6.50 | Stronger theory (matching bounds) but less practical; our paper has weaker theory but stronger empirical results — slightly below |
| vRwuBOxbsJ (Solving Football, 2p0s Diff Games) | 5.20 | Similar pattern of theory + practical gains; our paper has clearer contributions and stronger empirical evidence — above |
| tpjCWgyE6j (Policy Regret in POMGs) | 6.00 | Technically dense theory paper; our paper has complementary strengths (practical method vs. pure theory) — comparable |
| SwWxnZvgF4 (RL for Saddle-Point Equilibria) | 3.00 | Limited setting and novelty concerns; our paper clearly above |
| S0jIiiMtf4 (Infinite Horizon Markov Economies) | 6.00 | Theoretical framework with practical demonstration; our paper has more direct empirical validation — comparable |
| 61jN0L0aoJ (Beyond Minimax Diff Games) | 3.50 | Single case study, limited contribution; our paper clearly above |
| NtGE93iQXd (Robust Multi-Objective Optimization) | 2.50 | Flawed methodology; our paper clearly above |

The paper under review has a solid theoretical result (async-move optimality), an effective practical mechanism (belief preservation), and strong empirical validation (zero-shot generalization across unseen graphs). The primary weakness — imprecise framing of "worst-case robust" across proved and empirical claims — is addressable. This positions the paper in the 6.0 range, comparable to accepted posters like QEcSLhfOoQ (6.50) and S0jIiiMtf4 (6.00), and clearly above the rejected papers in the 2.5–3.5 range.

**Originality**: The async-move optimality proof and belief preservation for partial observability in graph-based PEGs are genuinely novel. The integration with EPG is a natural but non-trivial extension.

**Importance**: Real-time pursuit under partial observability is a practically important problem for security applications. The paper addresses a clear gap: existing RL methods for PEGs assume perfect information or do not generalize across graphs.

**Claims supported**: The theoretical claims are well-proved. The empirical claims are well-supported by experiments against strong adversaries (DPasync, BRasync) across diverse test graphs. The "worst-case robust" framing under partial observability is empirically supported but the paper could more precisely separate proved claims from empirical claims.

**Soundness**: The theoretical analysis is rigorous. The experimental design is reasonable. The PSRO comparison could be strengthened with more configuration details.

**Clarity**: The paper is generally well-written and organized. The main improvement needed is clearer separation of theoretical vs. empirical contributions in the framing.

**Value to community**: The belief preservation mechanism provides a practical template for handling partial observability in graph-based adversarial settings. The async-move analysis closes a gap in the theoretical understanding of DP-based PEG solutions.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>