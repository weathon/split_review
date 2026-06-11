Now I have enough to calibrate. Let me compare:

- **bjxuqI4KwU (7.50)**: Pure theory on SCM identifiability — a more fundamental theory result, but no algorithm and no experiments. The paper under review has a comparable theoretical contribution plus an algorithm and empirical validation.
- **SKulT2VX9p (6.67)**: Combines existing ideas (MPDAG + fairness); reviewers flagged limited novelty. The paper under review has a more original contribution — the LSCA closure and Λ-structure are genuinely new constructs.
- **8muemqlnG3 (6.50)**: Good paper but with baseline gaps and "too good to be true" concerns. Our paper is cleaner.
- **YcW8i9VCf5 (6.00)**: Conceptual clarity issues around relationship to CBO. Our paper is clearer and better validated.

The paper under review is cleaner than the 6.5-6.67 papers (more original contribution, honest scoping) but slightly below the 7.5 pure-theory anchor (narrower scope, with a small but real experiment issue). I'll score it at **7.0**.

Now let me write the final review.

## Summary
This paper introduces the conditional causal bandit problem — where arms are single-node conditional interventions — and provides a complete graphical characterization of the minimal set of nodes (mGISS) guaranteed to contain the optimal intervention. The key theoretical result equates the mGISS to the LSCA closure of the parents of the reward variable Y, reformulated elegantly via Λ-structures. The authors propose the C4 algorithm computing this set in O(|V|+|E|) time, and validate the approach on random and real-world graphs (over 90% pruning on large sparse graphs).

## Strengths
- **Non-trivial equivalence between conditional and deterministic atomic superiority (Proposition 4):** The proof that X ≽^c_Y W ⇔ X ≽^{det,a}_Y W reduces a problem involving arbitrary policies, observable conditioning sets, and probabilistic SCMs to a simpler deterministic atomic-intervention problem. This equivalence is surprising, practically enabling, and the linchpin that makes the entire graphical characterization tractable.
- **Complete graphical characterization of the mGISS (Theorem 13):** The paper proves that the LSCA closure of Pa(Y), L^∞(Pa(Y)), equals the mGISS. The Λ-structure reformulation (Theorem 12) is elegant and makes the closure operation immediately intuitive as a structural reachability condition. This goes well beyond the partial comparison rules of Lee & Bareinboim (2020).
- **Linear-time C4 algorithm with clean connector mechanism (Algorithm 1, Theorem 16):** The connector-based algorithm computes the closure in a single reverse-topological pass. Lemma 15 characterizes the connector as the unique first closure node on any downward path, giving the algorithm a strong intuitive foundation. The O(|V|+|E|) complexity makes it practical as a preprocessing step.
- **Substantial empirical search-space pruning on realistic graphs:** Over 90% node reduction on the largest bnlearn graphs. The trend that larger, sparser graphs benefit more aligns with the Λ-structure theory.
- **Uniqueness of the mGISS (Proposition 6):** Eliminates ambiguity — there is exactly one correct answer for a given graph, strengthening the result's applicability.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **Regret metric uses estimated rather than true optimal arm (Footnote 11):** The regret computation uses "the estimated best arm, defined as the arm that most runs concluded to be the best at the end of training." Standard regret is defined against the true optimal arm. Since bnlearn datasets have fully specified distributions, the true optimum is in principle computable offline. Using an estimated best arm makes the metric partially self-validating — if the algorithm converges to a suboptimal node, the reported regret understates the true gap. The bandit curves still demonstrate faster convergence under pruning, but the "better nodes" claim is weakened. This is fixable and does not undermine the core theoretical contribution.

### Trivial
- The paper would benefit from an intuition sketch for Proposition 4 in the main text — the forward direction (expectational ⇒ pointwise for every noise unit) is non-trivial, and a paragraph explaining the structural reason (e.g., how ancestor-inclusive Z_X enables policy reconstruction) would improve self-containedness.

## Nice-to-Haves
- **Comparison to hard-intervention baselines adapted to this setting:** The bandit experiment compares CondIntUCB with vs. without mGISS pruning (an ablation). While the paper correctly notes no algorithm for conditional causal bandits exists, adapting a hard-intervention method would further demonstrate practical gains.
- **Scalability discussion for CondIntUCB:** Per-context UCB has context count exponential in ancestor count. The paper could discuss when this becomes prohibitive, especially since C4 is advocated as a general pre-processing step.
- **Robustness to graph misspecification:** The paper mentions unioning results across candidate graphs. A brief discussion or experiment on mGISS sensitivity to edge additions/deletions would strengthen the practical story.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **"The proof of Proposition 4 cannot be assessed, and the quantifier structure merits scrutiny" — REMOVED.** The proof is in the stripped appendix — a parser artifact, not an author error. The criticism speculates about potential gaps without evidence from the paper. The observation about quantifier non-triviality is kept as a Trivial suggestion, but the implication that Proposition 4 might be wrong is unfounded speculation.
- **"No comparison to any existing causal bandit method" — DEMOTED to Nice-to-Have.** The paper explicitly states no algorithm for conditional causal bandits exists (line 313). The suggested hard-intervention baselines address a different problem; adapting them is non-trivial and outside scope. The mGISS vs. brute-force ablation is a reasonable validation of the pruning claim.
- **"Minimal elements in a preorder are not generally unique" (re: Proposition 6) — REMOVED.** The critic acknowledges the proof is in the appendix and speculates about necessary special properties. Without access to the proof, this speculation is not verifiable against the paper.
- **"Limited discussion of the Z_X assumption" — MOVED to Nice-to-Have as part of graph misspecification discussion.** The paper does discuss the ancestor-inclusion assumption (footnote 3, Section 2), and it is reasonable under no-latent-confounders. Discussing strict-subset cases is a scope extension.

## Novel Insights
The Λ-structure characterization (Theorem 12) is genuinely elegant: the LSCA closure — defined through a recursive process — is exactly the set of nodes that can reach two members of the base set via internally-disjoint paths. This transforms a closure operation into a purely structural reachability condition, which both simplifies the proofs and naturally yields the linear-time C4 algorithm. The insight that "a node matters iff it can influence the target's parents through multiple independent pathways" is both intuitive and rigorous.

## Suggestions
- Compute regret against the true optimal arm (obtainable from bnlearn models' known distributions) in a revision to make the bandit results fully trustworthy.
- Add a small worked example (e.g., the Asia graph) tracing C4 step by step, showing connectors at each node, to make the algorithm's operation concrete for readers.

---

**Calibration summary:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| MVpvyeVeyI (CBO unknown graphs) | 3.40 | R1 | Much weaker — limited novelty, scope issues |
| IPayPEGwdE (Causal contextual bandits) | 5.00 | R1 | Weaker — binary-only, limited experiments, impractical |
| pOoKI3ouv1 (Robust agents learn causal models) | 5.75 | R2 | Weaker — controversial (score variance 1-8) |
| YcW8i9VCf5 (Adversarial CBO) | 6.00 | R1,R2 | Weaker — conceptual clarity issues, limited novelty |
| l11DZY5Nxu (Robust root cause diagnosis) | 6.50 | R2 | Comparable but more applied, less theoretical depth |
| 8muemqlnG3 (Causal discovery via BO) | 6.50 | R1 | Comparable — good paper with baseline/credibility concerns |
| SKulT2VX9p (Interventional fairness) | 6.67 | R2 | Slightly weaker — combines existing ideas, novelty concerns |
| bjxuqI4KwU (Linear SCM identification) | 7.50 | R2 | Slightly stronger — more fundamental theory, but no algorithm |
| FhQSGhBlqv (Causal discovery hidden vars) | 7.50 | R2 | Stronger — broader scope, fully developed theory |

**Round 1 bracket:** 6.0 – 7.5
**Round 2 narrowing:** The paper is cleaner than the 6.5-6.67 anchors (more original, better validated) but not quite at the 7.5 level (narrower scope, small experiment issue). **Final score: 7.0.**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>