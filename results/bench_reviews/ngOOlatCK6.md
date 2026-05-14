Now I have all the information I need. Let me write the final consolidated review.

## Summary

The paper studies single-node conditional causal bandits, where arms are conditional interventions on a single node of a known causal graph, and the reward is a target variable Y. The main contribution is a complete graphical characterization of the minimal set of nodes (mGISS) guaranteed to contain the optimal intervention node: it equals the LSCA closure of the parents of Y (Theorem 13). The paper also presents the C4 algorithm that computes this set in linear O(|V|+|E|) time, and provides experiments on random and real-world graphs showing substantial pruning of the ancestor search space.

## Strengths

- **Novel graphical characterization of the minimal intervention set**: Theorem 13 proves that mGISS_Y(G) = L^∞(Pa(Y)), providing a clean, graph-theoretic characterization of the minimal set of nodes guaranteed to contain the optimal conditional intervention. The Λ-structure formulation (Theorem 12) gives an elegant alternative characterization that is both intuitive and useful for proofs.

- **Equivalence linking conditional and deterministic atomic superiority**: Proposition 4 establishes that X ⪰^c_Y W ⇔ X ⪰^{det,a}_Y W, which is a nontrivial technical bridge. This allows the paper to reason in the simpler deterministic atomic setting while the results apply to conditional interventions. The proof (in the appendix, checked against the paper) is sound: the (⇒) direction correctly instantiates Definition 1 on the deterministic SCM with point-mass noise distribution, and the (⇐) direction correctly constructs a policy g* from h* using Lemma 22.

- **Linear-time C4 algorithm with correctness proof**: Algorithm 1 runs in O(|V|+|E|) time and is proven correct via the connector characterization (Lemma 15, Theorem 16). The connector idea — where c[V] is the unique first node in L^∞(U) reachable from V — is intuitive and grounds the algorithm cleanly.

- **Substantial search-space pruning on real-world graphs**: Figure 6 (Appendix H) shows over 90% reduction in the ancestor search space for several large bnlearn models (pathfinder, munin, and the railway dataset), directly demonstrating practical applicability.

- **Regret improvement from node-space pruning**: Figure 3 shows that using mGISS with a UCB-based conditional bandit algorithm yields faster convergence and lower cumulative regret across four real-world models, with standard deviations reported.

## Weaknesses

### Fatal
None.

### Major
- **Experiments do not directly verify the central claim that mGISS contains the optimal node**: The regret experiments (Figure 3) compare brute-force (all ancestors) vs. mGISS and show improved regret from pruning. However, this only demonstrates that a smaller action set reduces regret — it does not verify that the empirically optimal node actually lies in the mGISS. The random graph experiments (Figure 5, Appendix H) report the fraction of ancestors retained, but without ground-truth verification that the optimal intervention belongs to the retained set. The paper would be substantially stronger with an experiment that runs the full brute-force search for enough rounds to identify the best node empirically, and then checks that it belongs to mGISS.

- **Single-node intervention setting is restrictive**: The paper assumes no latent confounders and only single-node interventions. While these are stated limitations and the paper acknowledges they are "left as future work" (Section 7), the restriction to single-node interventions removes the most natural baseline: intervening on multiple parents simultaneously. The paper argues that "restricting to single-node interventions in fact makes the problem more challenging" (page 2), but never quantitatively demonstrates that the single-node setting is indeed more challenging than multi-node interventions on the same graphs, nor provides examples where single-node conditional interventions yield strictly better results than multi-node hard interventions.

### Minor
- **Selection bias in experiment design**: The paper always picks Y as "the node with the most ancestors" (Section 6). This maximizes pruning potential but introduces a systematic bias toward favorable results. Results should be averaged over multiple Y choices per graph (e.g., random Y, Y with fewest parents) to demonstrate robustness.

- **No comparison to naive pruning baselines**: The experiments compare mGISS vs. all ancestors (brute-force), but do not compare against a baseline of random subsets of ancestors of equal size to mGISS. Such a comparison would disentangle whether the benefit comes from mGISS specifically containing better nodes, or simply from having fewer arms. This is important because the regret improvement from fewer arms in any bandit problem is trivial — what needs to be shown is that mGISS retains the right arms.

### Trivial
- Figure 3 does not include confidence intervals or error bars for key time steps, though the paper states standard deviations were computed.

## Nice-to-Haves
- A discussion of what graph structures cause mGISS to be large versus small (beyond the observation that dense graphs retain more nodes) would help practitioners understand when to expect pruning to be effective.
- An extension (even partial) to pruning the policy space for remaining nodes is a natural next step that some results in Section 7 gesture toward but do not develop.

## Removed Points
These points are flagged to be removed; treat them with caution:
1. *Proposition 4 proof gap* — The harsh critic claims the proof conflates pointwise and expectation-based inequalities. This is not correct: the (⇒) direction correctly instantiates Definition 1 on the deterministic SCM with δ(m), and since Definition 1 quantifies over ALL SCMs (including deterministic ones), the inequality holds pointwise. The proof is sound.
2. *Lemma 23 circularity* — The critic claims the induction assumes what it tries to prove. The proof is a standard induction on a topological order where the induction hypothesis applies to parents that precede Y in the order; there is no circularity.
3. *Lemma 33 / transitivity concern* — The critic questions transitivity of the superiority relation. Proposition 27 correctly proves transitivity for the max-based formulation of ⪰^{det,a}_Y, which is how the relation is defined. The concern about "same x for all n" reflects a misunderstanding of the definition.
4. *Lemma 24 SCM construction validity* — The critic claims the constructed SCM "may not satisfy standard conditions." The construction uses unit step functions and Bernoulli noise, which are standard building blocks for SCM counterexamples; the criticism is vague and unsupported.
5. *Claim about exponential policy space for remaining nodes* — The paper explicitly scopes its contribution to node selection: "In this paper, we find the minimal set of nodes that need to be considered by the agent in step (i). The value of X chosen in step (ii) can be selected by an MAB algorithm." Criticizing the paper for not addressing policy-space pruning is scope creep.
6. *Strength Finder's listed strengths that are generic or conflict with weaknesses* — The claim that "Proposition 4... is a nontrivial theoretical contribution" is kept as a real strength. However, some phrasing from the Strength Finder that is generic or conflicts with verified weaknesses has been filtered.

## Novel Insights
The most striking insight from this review process is that the harsh critic's central allegations of proof errors (Proposition 4, Lemma 23, Lemma 33) are uniformly incorrect upon careful reading of the paper. The paper's proofs are structurally sound; the critic appears to have misread the quantifier structure of Definitions 1 and 2, leading to phantom flaws. This leaves the experimental weaknesses (failure to directly verify optimality of mGISS, selection bias in Y choice, no random-subset baseline) as the paper's real limitations. These are significant but addressable — they weaken the empirical claims without touching the theoretical contribution. The paper's core theoretical result (Theorem 13) stands as a genuine contribution to the causal bandits literature.

## Suggestions

1. **Add a direct optimality verification experiment**: For each real-world dataset, run the full brute-force algorithm for enough rounds to empirically identify the best node, then verify that it lies in the mGISS. Report the frequency with which the optimal node is retained.

2. **Include a random-subset baseline**: Compare mGISS against random subsets of ancestors of equal size. This controls for the trivial effect of action-set reduction and isolates mGISS's specific benefit.

3. **Average over multiple Y choices**: For each graph, repeat experiments with Y chosen as the node with fewest parents, a random ancestor, and the node with the most ancestors, to eliminate selection bias.

4. **Clarify the single-node vs. multi-node comparison**: Provide a concrete worked example (with SCM and structural equations) where single-node conditional interventions are genuinely more challenging than multi-node hard interventions, or acknowledge that this claim is a framing device.

## Score and Decision

**Anchors used for calibration:**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| /home/wg25r/review_agent/human_reviews_2026/gjvTNxVd2f.md (Counterfactual SCB) | 5.50 | Similar type of contribution (causal bandits theory extension). This paper has cleaner theoretical results and a more complete characterization. |
| /home/wg25r/review_agent/human_reviews_2026/QW0PchhVaD.md (Contextual Causal BO) | 4.50 | Comparable theoretical depth. This paper's graphical characterization is more complete and the algorithm more efficient. |
| /home/wg25r/review_agent/human_reviews_2026/R2mMw1lesm.md (Transportability SCB) | 3.50 | This paper avoids the "incremental contribution" criticism that brought that paper down — it tackles a genuinely new problem (conditional interventions). Significantly stronger. |
| /home/wg25r/review_agent/human_reviews_2026/bOfiLeoUJf.md (Query-Specific Graph Pruning) | 4.67 | Similar structure (graph pruning + algorithm). This paper's theoretical characterization is more complete (necessary and sufficient conditions). |
| /home/wg25r/review_agent/human_reviews_2026/ta8BKRa1bl.md (Causal graph identifiability) | 6.00 | Both are strong theoretical papers with solid proofs. This paper's experimental evaluation is weaker. |
| /home/wg25r/review_agent/human_reviews_2026/V7pT2ZRoTB.md (Theoretical Guarantees for Causal Discovery) | 4.50 | Both provide theoretical guarantees. This paper's characterization is more directly applicable. |
| /home/wg25r/review_agent/human_reviews_2026/6VnyYkg37h.md (Causally Disentangled World Models) | 3.00 | This paper is substantially stronger — the theory is rigorous, the proofs are complete, and the claims are well-supported (albeit with weak experiments). |
| /home/wg25r/review_agent/human_reviews_2026/hisAy19yMP.md (Average Causal Effects) | 5.50 | Comparable in theoretical rigor. This paper's contribution is more self-contained and algorithmically complete. |

The paper presents a clean theoretical contribution (complete graphical characterization of the minimal intervention set for conditional causal bandits) with a correct, well-structured proof and an efficient linear-time algorithm. The experimental evaluation is the main weakness — it provides indirect evidence but does not directly verify the central claim, and lacks proper baselines to rule out trivial explanations. The paper falls between "Accept (Poster)" territory (comparable to 5-5.5 anchor papers in causal bandits) and a stronger accept, held back primarily by experimental shortcomings.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>