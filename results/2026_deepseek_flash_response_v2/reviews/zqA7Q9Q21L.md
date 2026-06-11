Now I have enough calibration data to position the paper. Let me write the final review.

## Summary

This paper introduces R2PS, a framework for real-time pursuit strategies in graph-based pursuit-evasion games under partial observability. It extends a dynamic programming (DP) algorithm for Markov PEGs to handle asynchronous evader moves (proving optimality in Theorem 2/Corollary 1), proposes a belief preservation mechanism for partial observability (Section 3.2), and embeds this into the EPG cross-graph RL framework to train a GNN policy. The resulting policy achieves real-time inference (under 0.01s on GPU) with non-trivial success rates against strong evaders, and shows zero-shot generalization to unseen real-world graphs, outperforming per-graph-trained PSRO baselines.

## Strengths

1. **Clean theoretical extension of DP to asynchronous-move PEGs (Section 3.1).** Theorem 2 and Corollary 1 prove that the same DP distance table from Algorithm 1 yields strictly optimal strategies for both pursuer and evader when the evader can move asynchronously (i.e., predicts the pursuers' action). This is a sound formal contribution that extends prior synchronous-only results (Lu et al. 2025a/EPG). The proof (Lemma 1 → Theorem 2 → Corollary 1) is clearly structured.

2. **Belief preservation mechanism that handles partial observability efficiently (Section 3.2).** The belief update (Eqs. 6-7) costs only ~O(|V|) per timestep, avoiding exponential observation histories of full POSG formulations. Table 1 shows belief-averaged DP (DP_belief) substantially outperforms the position-extended version (DP_Pos) on all 10 test graphs (e.g., Grid Map: 0.78 vs 0.59, Eiffel Tower: 0.94 vs 0.69). Lemma 2 shows the extended policies collapse to the optimal perfect-information policy when observability is unlimited — a necessary consistency check.

3. **Zero-shot cross-graph RL policy outperforms per-graph-trained PSRO (Table 2).** R2PS, trained on 300 unseen graphs, consistently beats PSRO policies trained _directly on each test graph_. Against the strongest evader (DP_async), PSRO collapses to 0.00 on several graphs (Scotland-Yard, Hollywood, Sagrada Familia) while R2PS maintains non-zero performance (0.76, 0.38, 0.20). This is a meaningful comparison since PSRO has the advantage of per-task training. The paper further evaluates against a best-responding evader (BR_async), showing the method is empirically robust.

4. **Concrete real-time inference advantage (Section 4.2, Table 3).** The paper gives an explicit complexity comparison (O(n²m) for GNN inference vs ~O(n^{m+1}) for DP recomputation) and empirically demonstrates RL policy inference under 0.01s on GPU vs minutes for DP on graphs with 744–2065 nodes. This quantification grounds the "real-time" claim.

5. **Controlled belief ablation (Table 4).** Reducing belief update frequency (every 2/3 steps) degrades success rates substantially (e.g., Downtown Map: 0.92→0.61→0.39; Scotland-Yard: 0.73→0.34→0.28), demonstrating the belief mechanism is causally responsible for performance. The "known opponent" condition further shows that if policy information were available, performance would improve.

## Weaknesses

### Fatal
None.

### Major

1. **Missing key baseline: no direct comparison between the trained RL policy and DP_belief on test graphs.** The RL policy is trained with KL guidance from DP_belief, but the paper never shows whether the learned policy approaches, matches, or degrades DP_belief's quality on the test graphs. Table 1 reports DP_belief success rates (under the DP policy acting online) and Table 2 reports RL policy success rates — but these are against different evaders (DP_async/BR_async in Table 2 vs DP_async only in Table 1), making cross-comparison unreliable. Without a direct RL-vs-DP_belief comparison under identical conditions, a reader cannot assess whether the RL training adds value beyond distillation or whether the observed limitations (e.g., 0.20 on Sagrada Familia, 0.25 on The Bund against DP_async in Table 2) are inherited from the DP guidance or introduced by the RL training. This is the single most informative missing experiment.

2. **"Worst-case robust" framing is inflated relative to evidence.** The title and central framing claim "worst-case robust" pursuit strategies under partial observability. However: (a) The formal optimality proofs (Theorem 2, Corollary 1) apply to the perfect-information asynchronous setting, not to the partially observable regime where the paper operates. (b) The paper explicitly acknowledges (line 234) that D(·) "becomes an optimistic one under partial observability" — an optimistic estimator cannot ground a formal worst-case guarantee. (c) While the paper evaluates against a best-responding evader (BR_async), this constitutes _empirical_ robustness against specific opponents, not the formal worst-case guarantee that the title implies. The paper would benefit from reframing its contribution as "effective real-time pursuit with empirical robustness against strong evaders."

3. **No statistical reporting: all results are point estimates without variance or confidence intervals.** Success rates are averaged over 500 tests, but no standard deviations, confidence intervals, or error bars are reported anywhere — for the PSRO comparison, the scalability tests, or the ablations. This is a standard omission that makes it impossible to assess whether observed differences (e.g., Eiffel Tower 1.00 vs Sydney Opera House 0.95 in Table 2, or 0.49 vs 0.41 across large graphs in Table 3) are statistically meaningful.

### Minor

1. **Missing standard-RL baseline without DP guidance.** The learning curves (Figure 4, Appendix C.4) show β=0 (pure RL) vs β=0.1 on the training sets, but there is no full evaluation table showing how a pure RL policy (trained on the same 300 graphs without DP guidance) performs zero-shot on the test graphs. This would isolate the value of the DP-guided training signal.

2. **No RL ablation without belief (Pos-only guidance).** Table 4 abates belief update frequency but does not include a condition where the RL policy is trained using only the position-extended policy (Eq. 5) without any belief mechanism. This would be the cleanest way to isolate the belief contribution in the RL training setting.

3. **Speculative "exponential improvement" paragraph (lines 195–196).** The passage about cross-graph training leading to "exponential" improvement via "half space" division is presented as speculation ("Imagine", "In this ideal case") but sits uneasily in an otherwise rigorous paper. It should be clearly marked as intuition or removed.

4. **Scalability results show substantial degradation on larger graphs.** Success rates in Table 3 against DP_async drop compared to Table 2 on several graphs (e.g., Times Square: 0.95→0.56, Hollywood: 0.38→0.46 — actually slightly improved, but Sydney Opera House: 0.95→0.76). Several results (0.33, 0.41, 0.46 on large graphs) are modest. The paper describes this as "maintains desirable overall performance" which is somewhat optimistic.

5. **Belief mechanism's uniform-policy assumption is acknowledged but under-discussed.** The belief update (7) defaults to a uniform evader policy when the true policy is unknown. As the paper notes, this means the "belief" under the default setting is essentially a constrained breadth-first expansion over graph connectivity, not a true posterior. The ablation (Table 4, "Known Opponent" vs "Original") shows this assumption costs significant performance on some graphs (e.g., Times Square: 0.42 vs 0.27, The Bund: 0.54 vs 0.23). This limitation merits more prominent discussion.

### Trivial

None.

## Nice-to-Haves

- Analysis of distributional similarity between the 300 training graphs and the 10 test graphs to more precisely characterize the "zero-shot generalization" claim.
- Evaluations with larger pursuer teams (m=3) to test whether the approach scales in agent count.
- A condition in Table 4 ablating belief entirely (Pos-only) for the RL setting.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"PSRO comparison is not meaningful / inflates advantage"** (Harsh Critic). REMOVED: The critic claims PSRO is not designed for cross-graph generalization, making the comparison unfair. However, PSRO is trained _directly on each test graph_ (per-graph), while R2PS is zero-shot. R2PS outperforms PSRO despite being at a disadvantage (no test-graph training). This comparison actually provides _evidence_ for R2PS's strength, not a weakness. The critic's framing is inverted.

2. **"The paper never considers an evader that exploits partial observability"** (Harsh Critic). REMOVED: Factually incorrect — the paper evaluates against BR_async (a best-responding evader trained directly against the R2PS pursuers) in both Table 2 and Table 4. This evader is precisely designed to exploit the pursuers' strategy.

3. **"Lemma 2 does not help / is presented as assurance"** (Harsh Critic). REMOVED: Lemma 2 is presented as a consistency check (the extended policies reduce to the perfect-information optimal policy when Pos is a singleton). The paper's framing is clear and appropriate; the critic over-interprets the lemma's intended role.

4. **"Minimax policy is informal usage"** (Harsh Critic). REMOVED: The paper uses "minimax" descriptively for the structure of Eq 5 (min over pursuer actions, max over evader positions), which is standard usage.

5. **"Zero-shot claim deserves scrutiny due to domain similarity"** (Harsh Critic). REMOVED: Raised as speculation without evidence. The training set includes synthetic (Dungeon) and random Google Maps graphs; the test set includes specific famous locations. That both are urban street networks is the _point_ of the generalization experiment. A distributional similarity analysis would be nice-to-have, not a weakness.

6. **Pure formatting/style nitpicks, parser artifacts, and speculative concerns about stripped appendix content.** REMOVED under hard rules.

## Novel Insights

The interaction between the harsh critic and the strength finder reveals an important subtlety: the PSRO comparison that the critic dismisses as "not meaningful" is actually the paper's strongest piece of evidence when correctly interpreted. R2PS achieves zero-shot generalization that beats per-graph-trained PSRO — this is _harder_ than what the paper claims to show, not easier. The paper undersells this by not clearly highlighting that PSRO has the per-task training advantage. Separately, the critic's characterization of the belief mechanism under uniform default as a "constrained breadth-first expansion" rather than a true Bayesian posterior is a useful framing that would help readers calibrate expectations.

## Suggestions

1. **Add a direct RL-vs-DP_belief comparison** on the test graphs against identical evaders (DP_async). This is the single most important missing experiment — it clarifies whether the RL training preserves, improves, or degrades the DP guidance, and what the actual cost-quality tradeoff is.

2. **Add a standard RL baseline (β=0, no DP guidance)** trained on the same 300 training graphs and evaluated zero-shot on the test graphs. This isolates the value of the DP-guided training signal.

3. **Report confidence intervals or bootstrapped standard deviations** on all main results. With 500-test averages, standard errors are essentially free.

4. **Reframe the contribution title/abstract** from "worst-case robust" (which implies formal guarantees not provided under partial observability) to something like "effective real-time pursuit with empirical robustness" or "pursuit strategies robust to strong evaders."

5. **Add a Pos-only (no belief) RL ablation** to Table 4.

6. **Clearly mark the "exponential improvement" paragraph** as speculative intuition, or remove it.

7. **Add distributional similarity analysis** between training and test graphs to characterize the generalization gap more precisely.

## Score and Decision

### Calibration Anchors

**Round 1 (bracketing):**
- Low band: Topically similar papers scored 2.50–3.40 (Reject) — applying known methods to problem variants without substantial novelty.
- Middle band: Papers scored 4.00–6.67 — including Urban Network Security Games (4.75, Reject), PSRO Policy Population Growth (6.00, Accept), ACCES Games (6.50, Accept), Mean Field Games on Sparse Graphs (6.67, Accept).
- High band: Papers scored 8.00 (Accept) — clean, complete evaluations with significant theoretical advances and no major gaps.

**Round 2 (narrowing, target bracket 5.0–6.5):**
- Zero-Shot Generalization of GNNs (5.50, Reject): Mixed reviews with missing baselines and limited domain coverage. **Our paper has stronger theoretical contributions (DP extension, belief mechanism) but shares similar evaluation gaps (missing baselines). Slightly above this anchor.**
- PSRO Policy Population Growth (6.00, Accept): Clean focused contribution with good theory + experiments. **Our paper has broader scope but less complete evaluations; comparable but slightly below due to the missing DP_belief baseline and overclaiming issue.**
- ACCES Games (6.50, Accept): Strong theory (existence of NE, convergence proofs) with practical algorithm. Scale limitations noted by reviewers. **Our paper has comparable theoretical depth but more significant evaluation gaps; below this anchor.**

**Initial bracket:** 5.0–6.5 (exclusive of the very weak sub-4 papers and the very strong 8.0 papers).

**Final position:** After comparing against the round-2 anchors, the paper sits near the lower end of the bracket. It has genuine theoretical contributions (DP async extension, belief mechanism) and a compelling empirical result (zero-shot R2PS beats per-graph PSRO). However, the missing DP_belief vs RL comparison and inflated "worst-case" framing are significant enough gaps that the paper is not at the level of the 6.0+ accepted papers, which have cleaner evaluations and more precise claims. The paper is above the 4.75–5.50 reject-level papers which lack comparable algorithmic novelty.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>