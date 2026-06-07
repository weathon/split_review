## Summary

This paper proposes R2PS, a framework for real-time pursuit strategies under partial observability that generalizes zero-shot to unseen graphs. It (1) proves that a DP algorithm for Markov PEGs yields optimal strategies under asynchronous evader moves (Theorem 2, Corollary 1), (2) introduces a computationally efficient belief preservation mechanism (~O(|V|) per step) for partial observability, and (3) combines belief preservation with the EPG framework for cross-graph RL training, learning a GNN-based pursuer policy. The experiments show strong zero-shot performance on unseen real-world graphs, consistently outperforming a PSRO policy trained directly on each test graph (e.g., 0.99 vs 0.03 on Downtown Map against the strongest evader).

## Strengths

1. **Theoretical extension of DP to asynchronous moves (Theorem 2, Corollary 1).** The paper proves that the same distance table D from Algorithm 1 (originally designed for synchronous moves) yields strictly optimal strategies for *both* the pursuer and evader when the evader moves asynchronously. This is a non-trivial extension of the synchronous-only result in prior work (Lu et al., 2025a) — the evader's policy in Eq. (3) conditions on the actual pursuer move, which changes the decision problem structure.

2. **Clean, computationally efficient belief preservation mechanism (Eq. 6-7, Lemma 2).** The belief update maintains a distribution over possible evader positions at only ~O(|V|) per timestep, avoiding the exponential observation-history space that makes general POSGs PSPACE-hard. Lemma 2 shows the mechanism reduces to the optimal perfect-information policy when observations are unlimited. Table 1 confirms its value: the belief-averaged DP pursuer consistently outperforms the position-extended variant across all 10 test graphs (e.g., 0.90 vs 0.73 on Downtown Map).

3. **Strong empirical demonstration of zero-shot generalization (Table 2).** The cross-graph RL policy, trained on 300 unseen graphs, consistently and often dramatically outperforms a PSRO policy trained directly *on each test graph*. Against the strongest asynchronous-move DP evader: R2PS achieves 0.99 vs PSRO's 0.03 on Downtown Map, 0.95 vs 0.04 on Times Square, 0.82 vs 0.24 on Big Ben, 0.95 vs 0.11 on Sydney Opera House.

4. **Verified real-time inference at scale (Table 3).** On large graphs (744–2065 nodes), RL inference takes 0.008–0.01 seconds on a GPU, while DP recomputation takes 6–139 seconds — a 600–14,000× speedup — while maintaining 33–76% success rates against the optimal asynchronous evader.

5. **Systematic ablation of belief updates (Table 4).** Performance degrades monotonically as belief update frequency decreases (every step → every 2 → every 3 steps) across all test graphs (e.g., Grid Map: 1.00 → 0.60 → 0.42; Scotland-Yard Map: 0.73 → 0.34 → 0.28), causally attributing benefit to the belief mechanism.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The DP time complexity comparison is imprecisely phrased.** Section 4.2 states "it takes over 2 minutes to run Algorithm 1 at each timestep." Algorithm 1 is a complete DP precomputation — the intended comparison is between per-timestep RL inference and per-graph-change DP recomputation under *dynamically changing* graphs. The surrounding context mentions this scenario, but the phrase "at each timestep" conflates two different timescales and creates a misleading impression that DP must be re-run at every game step. This should be clarified to avoid confusion.

2. **The PSRO baseline is under-documented.** The paper states PSRO uses "10 iterations (10000 episodes per iteration)" but does not specify (a) the oracle used for best response, (b) the PSRO policy architecture (is it the same GNN as R2PS?), or (c) whether 10 iterations was sufficient for convergence. While the comparison still demonstrates that cross-graph training transfers better than similarly-budgeted single-graph PSRO, the missing documentation makes it harder to assess the baseline's strength and interpret the comparison fairly.

3. **No discussion of limitations.** The paper lacks a limitations section. Several natural boundary conditions are not acknowledged: the belief update uses a uniform evader model by default (line 157), all results are for m=2 pursuers, the DP precomputation for training graphs is exponential in m, and the observation model (binary detection within range) is relatively simple. The "worst-case robust" framing would benefit from explicit qualification about the uniform-belief assumption, since a truly worst-case evader could potentially exploit this discrepancy.

4. **All success rates are point estimates without confidence intervals.** Tables 1–4 report success rates over 500 trials but include no standard deviations or confidence intervals. While the margins are often large enough to be clearly significant, adding statistical uncertainty estimates would strengthen the reporting and follow standard practice.

### Trivial

1. **Algorithm 1's condition on line 12** ("∃ n'_e ∈ V, (n_e, n'_e) ∈ E, D(s_p, n'_e) > D(s_p, s_e)") is hard to parse in the extracted text. An intuitive explanation of why this condition is needed would help readability.

2. **Observation range specification is slightly ambiguous.** Line 135 says "observation range of 2 means that the evader can be detected only when its distance to one pursuer is less than 3." Clarifying whether range k means graph distance ≤ k or < k throughout would help.

3. **Definition of "optimal" for the asynchronous case** (end of Section 2.1) is informal ("the worst-case termination timesteps... are maximized/minimized"). A more precise formulation would aid clarity for the paper's main theoretical claim.

## Nice-to-Haves

- A short proof sketch for Theorem 2 in the main text would help readers follow the key theoretical claim without consulting the appendix.
- Running PSRO with more iterations (e.g., 20–30) to verify whether R2PS's advantage persists against a more converged baseline would strengthen the comparison.
- Ablating the belief mechanism's contribution more directly by comparing "no belief (just Pos)" vs "belief with uniform model" vs "belief with ground-truth evader policy" for the DP pursuers (similar to what is done for RL in Table 4).

## Removed Points

These points were removed with justification:

- **Harsh Critic's claim about proof validity (Point 1, second sentence).** The critic says "all proofs are relegated to the appendix... Because the appendix was stripped by the parser, I cannot verify them." The hard rules require removing weaknesses about missing appendix content — the appendix exists in the original submission. The more general point about wanting a proof sketch in the main text is preserved as a Nice-to-Have.
- **Harsh Critic's claim that the uniform-belief assumption undermines the "worst-case robustness" claim (Point 2).** The paper trains against a provably optimal DP evader (the worst-case opponent), not against the belief model. The belief is the pursuer's internal representation, and the paper acknowledges the uniform assumption (line 157). The criticism conflates training adversary quality (which is provably worst-case) with belief model accuracy (which is a practical concession). The paper's "worst-case robust" claim is properly about the training adversary, not the belief model.
- **Harsh Critic's claim that the PSRO comparison is "uncharitable" and the framing is "too broad" (Point 3, second half).** The paper's framing of the comparison is specific: "outperform[ing] the PSRO policy directly trained on the test graphs." This is a fair comparison between cross-graph and per-graph training at comparable budgets. The critic's speculation that PSRO "may not have converged" is not verifiable from the paper.
- **Strength Finder strengths about "important problem" / "timely contribution."** Generic statements about problem importance were removed as they lack concrete evidence specific to this paper. All five kept strengths are grounded in specific theorems, tables, or equations.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Clarify Section 4.2:** Rephrase "at each timestep" when referring to Algorithm 1 recomputation — explicitly state it applies per graph-change event, not per game step.
2. **Document the PSRO baseline fully:** Add a sentence or short paragraph specifying the oracle, policy architecture, and any convergence checks.
3. **Add confidence intervals or standard deviations** to Tables 1–4.
4. **Add a brief limitations paragraph** to the conclusion (Section 6) acknowledging: the uniform-belief assumption, m=2 restriction, observation model simplicity, and DP's exponential cost in m for training graphs.
5. **Provide an intuitive explanation** of Algorithm 1's line 12 condition (the "∃ n'_e" check).
6. **Clarify the "optimal" definition** in Section 2.1 for the asynchronous case with a more precise formulation.

## Score and Decision

**Round 1 Bracketing (3 queries):** The paper sits between weak anchors (1.67–3.40 on low-quality PEG/RL papers) and strong anchors (8.0 on top GNN/RL theory papers). Middle-band anchors on pursuit-evasion and adversarial RL score 4.0–6.67.

**Round 2 Narrowing (2 queries):** Reading anchors in the 4.5–7.5 range yields the following anchors:

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| xAYOfMV264.md (Dual-Agent Adversarial RL) | 4.80 | R1/R2 | Weaker: limited evaluation, unclear contribution separation from prior work. R2PS is stronger empirically and theoretically. |
| DjHnxxlqwl.md (Urban Network Security Games) | 4.75 | R1 | Weaker: platform/benchmark paper with thin experiments. R2PS has more substantial contributions. |
| SPcmEiiDDo.md (Episodic Control Adversarial Policy) | 4.00 | R1 | Weaker: limited scope. R2PS has broader contribution and stronger results. |
| zwU9scoU4A.md (Mean Field Games on Sparse Graphs) | 6.67 | R1 | Stronger: deeper theoretical development. R2PS has stronger empirical validation but less theory depth. |
| 5e0yWSNGIc.md (Certified Training in RL) | 5.33 | R2 | Comparable but rejected due to novelty concerns. R2PS has clearer novelty. |
| Q00CO1Tm6M.md (POMDP Hardness) | 5.75 | R2 | Comparable but rejected due to presentation issues. R2PS has comparable quality but fewer presentation problems. |
| 99tKiMVJhY.md (Dec-POMFC) | 6.33 | R2 | Slightly stronger theoretical development. R2PS has more extensive/comparable empirical validation. |

**Final Score:** 5.5. The paper has a genuine contribution with both theoretical and empirical components, and the weaknesses are minor and addressable in revision. It is clearly above rejection-level papers (4.0–5.0) but not at the level of the strongest accepts (6.5+) given the documentation gaps and lack of limitations discussion.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>