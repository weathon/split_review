Now I have a solid understanding of the paper and the calibration anchors. Let me write the final review.

## Summary
This paper introduces the first graphical characterization of the minimal search space for single-node conditional causal bandits. The authors define the minimal globally interventionally superior set (mGISS) and prove that it equals the LSCA closure of the target's parents, with an elegant alternative characterization via Λ-structures. They establish an equivalence between conditional-intervention superiority in general SCMs and deterministic atomic-intervention superiority, enabling the graphical analysis. The C4 algorithm computes the mGISS in linear time $O(|V| + |E|)$. Experiments on real-world bnlearn graphs and random DAGs demonstrate substantial search space pruning (70–90%), and integration with a contextual UCB bandit shows improved cumulative regret.

## Strengths
- **Novel theoretical characterization:** This is the first work to fully characterize the minimal search space for single-node conditional interventions (as distinguished from Lee & Bareinboim's 2018 multi-node hard intervention result). The mGISS concept (Definition 5) and its closed-form characterization via LSCA closure (Theorem 12) and Λ-structures are well-defined and non-trivial.
- **Provocativeness of Proposition 4:** The equivalence between conditional-intervention superiority in fully probabilistic SCMs ($\succeq_Y^c$) and deterministic atomic-intervention superiority ($\succeq_Y^{\det,a}$) is a significant conceptual insight. It pivots from intractable probabilistic reasoning to a deterministic frame, enabling the purely graphical characterization downstream.
- **Elegant $\Lambda$-structure characterization:** Theorem 12's equivalence between the recursively defined LSCA closure and the intuitive $\Lambda(\text{Pa}(Y), \text{Pa}(Y))$ condition provides an immediately visualizable graphical rule. This resolves the failure of naive LCA heuristics (see Figure 1d).
- **Linear-time algorithm with correctness proof:** The C4 algorithm (Algorithm 1) leverages the connector mechanism (Definition 14, Lemma 15) to compute the closure in $O(|V| + |E|)$ time. The algorithmic design is clean and well-motivated by Lemma 15's structural insight.
- **Honest and focused empirical evaluation:** The experiments cleanly isolate the contribution (node-selection pruning) from the orthogonal policy optimization problem. Search space reduction figures (Figure 5, 6 in Appendix H) and regret curves (Figure 3) directly support the claims. Standard deviations are reported; run counts (300–500) are adequate.

## Weaknesses
### Fatal
None.

### Major
None.

### Minor
- **Algorithm 1 pseudocode iterates over all nodes but only defines connectors for ancestors of U:** Line 5 of Algorithm 1 iterates `for V ∈ V \ U` in reverse topological order; line 6 computes `C ← {c[V'] : V' ∈ Ch(V) ∩ An(U)}`. For nodes V not in An(U), no connector c[V] is ever initialized or used, yet the loop body still executes. This has no impact on correctness — non-ancestors cannot reach U through their children, so the intersection is empty and no connector is assigned nor S updated. However, as Definition 14 restricts its domain to `V ∈ An(U)`, the mismatch between the algorithm's loop range and the definition's domain is an exposition gap that could confuse readers (lines 6, line 34, Definition 14).
- **Regret baseline uses tabular contextual UCB, which does not scale to larger context spaces:** The paper uses one UCB per realization of $Z_X$ (Section 6, footnote 10), making the per-context UCB a tabular learner. As noted by the authors, this limits experiments to small/medium graphs from bnlearn. While the authors correctly note that their contribution is node selection (step i) rather than contextual bandit algorithm design (step ii), and the setup honestly isolates the value of their pruning, the scalability of the learning subroutine is an unresolved issue. The paper would benefit from a brief discussion of realistic integration paths (e.g., using linear contextual bandits or feature-based policies within each node's UCB).

### Trivial
None significant.

## Nice-to-Haves
- **Clarify non-ancestor handling in Algorithm 1:** Add an explicit filter or comment in the pseudocode restricting updates to `An(U)`, or initialize `c[V] = ⊥` for non-ancestors and note they are ignored. This is a presentational fix, not a correctness issue.
- **Discuss latent confounding boundaries:** A short paragraph (1–2) on how the deterministic reduction would be affected by unobserved confounders — since fixing $\mathbf{n}$ no longer captures the true uncertainty over unobserved variables, the $\Lambda$-structure criterion may become insufficient — would help position the paper's boundary clearly rather than leaving it as a generic "future work" statement.
- **Discuss mGISS robustness if $Z_X$ excludes some ancestors:** Add a brief remark on whether the mGISS characterization remains valid if the conditioning set $Z_X$ is strictly smaller than the full ancestor set $\text{An}(X) \setminus \{X\}$. If the pruning guarantee holds, stating this explicitly strengthens practical applicability; if not, it clarifies the boundary of the result.

## Removed Points

The following points from the original reviews were considered and removed:

- **Harsh critic's "Major" on tabular UCB scalability:** Downgraded to Minor/Nice-to-have. The paper's contribution is explicitly about pruning *which node* to intervene on (step i), not policy optimization within contexts (step ii). The tabular UCB is an intentional proof-of-concept isolation of step i's value. The authors acknowledge the limitation and frame their scope honestly. This is not a structural flaw.

- **Harsh critic's concern about Algorithm 1 non-ancestor initialization:** Downgraded from "Minor exposition issue affecting reproducibility" to Minor. The pseudocode is correct as-is — non-ancestors simply produce no connector assignment and are never added to the closure. The loop iterates broadly but the intersection `Ch(V) ∩ An(U)` ensures only ancestry-relevant nodes are processed. The reviewer's concern was about clarity, not correctness.

- **Strength: "Addresses an important problem":** Removed as generic/vague. The strengths in the review are restricted to concrete, paper-specific contributions.

- **Strength: "Good experimental design":** Removed as superficial. Replaced with the more specific strength about honest and focused empirical evaluation.

## Novel Insights
The equivalence between conditional-intervention superiority in fully probabilistic SCMs and deterministic atomic-intervention superiority (Proposition 4) is the conceptual core of the paper and a genuinely non-obvious result. This reduction means that worst-case dominance over all noise distributions and all context-respecting policies can be analyzed purely in a deterministic frame — effectively reducing an infinite-dimensional optimization problem over policies to a pointwise graph argument. The Λ-structure characterization (Theorem 12) further reveals that the mGISS is not merely a recursive construction but has a direct graphical form: a node belongs to the mGISS if and only if it can independently influence two disjoint sub-components of the target's parents through node-disjoint paths. This duality (recursive LSCA closure ↔ graphical Λ-structure) and its algorithmic exploitation via connectors (Lemma 15) is elegant and practically useful.

## Suggestions
- In the pseudocode, add a guard clause after line 5: `if V ∉ An(U) then c[V] ← ⊥; continue` — this clarifies intent without changing behavior.
- Add an explicit statement (1–2 sentences) in Section 7 or a remark in Section 3: "If the conditioning set $Z_X$ excludes some ancestors of $X$, the mGISS characterization of Theorem 13 still holds as a safe superset of optimal intervention targets since the superiority relation is defined for all valid $Z_X$."
- Consider extending the regret experiments to at least one larger bnlearn graph (e.g., water or mildew) to demonstrate that the pruning/regret gap persists beyond 109-node graphs.

## Score Calibration

**Round 1 — Bracketing:** I issued three queries across score bands. Results placed clearly above the weak anchors (IRIS 2.5, Sparse Causal Model 3.0) and below the strong anchors (unanimous 8s). This bracketed the paper somewhere in the (4, 8) range.

**Round 2 — Narrowing:** I pulled anchors in the (5, 7) range:
- Learning Good Interventions in Causal Contextual Bandits (avg 5.0, Reject): had consensus presentation issues, restrictive binary assumptions, unclear parameter tuning, and limited experiments. This paper is clearly stronger: it has coherent theory, clean characterization, and direct empirical validation.
- Adversarial Causal Bayesian Optimization (avg 6.0, Accept): had naming/notation ambiguity, weak motivation ("why adversarial?"), and the reviewer split on whether the contribution was genuinely novel vs. a standard bandit+Causal mashup. The current paper has a sharper problem definition, a uniquely graphical contribution (not just an algorithmic one), and cleaner framing.
- Causal Discovery via Bayesian Optimization (avg 6.5, Accept): had concerns about "too good to be true" results on synthetic data, missing baselines. The current paper's experiments are more modest but honest and directly support the claims.
- Efficient and Trustworthy Causal Discovery with Latent Variables (avg 6.0, Accept): strong theory but less focused experimental validation. The current paper balances theory and experiment better within its narrower scope.

This paper is noticeably stronger than the 5.0–6.0 anchors: it has a complete theoretical pipeline (equivalence proposition → graphical characterization → linear-time algorithm) that is internally consistent and empirically validated. It does not reach the 7.5–8.0 tier because its scope is bounded (explicitly no latent confounders, the contextual bandit experiment is tabular and proof-of-concept), and the empirical results, while solid, are not as extensive as the strong anchors typically demonstrate.

My placement: approximately **7.0** — solidly in the "clearly above the borderline, warranted acceptance" territory, comparable to a confident 6–7 anchor, without claiming the exceptional breadth that would elevate it to 8.

MY FINAL SCORE: <score>7</score>
MY FINAL DECISION: <decision>Accept</decision>