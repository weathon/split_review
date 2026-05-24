Now I have enough information to synthesize. Let me write the final consolidated review.

## Summary
This paper introduces the conditional causal bandit problem, where arms are single-node conditional interventions, and provides a complete graphical characterization of the minimal set of nodes guaranteed to contain the optimal intervention node. The main theoretical result (Theorem 13) proves that this minimal globally interventionally superior set (mGISS) equals the LSCA closure of the parents of the reward variable. The paper also presents a linear-time algorithm (C4, Theorem 16) that computes this closure, and empirical results showing substantial search-space reduction on random and real-world graphs.

## Strengths
1. **Novel problem formulation with a complete graphical characterization (Theorem 13).** The paper is the first to define and solve the minimal search space problem for single-node conditional interventions. The characterization of mGISS as the LSCA closure of Pa(Y) is clean, and the Λ-structure test (Theorem 12) provides an intuitive, visually accessible understanding of which nodes must be in the search space.

2. **Linear-time C4 algorithm (Algorithm 1, Theorem 16).** The connector-based algorithm runs in O(|V|+|E|) and is simple enough to serve as a practical preprocessing step for any causal bandit algorithm. This is a concrete, implementable deliverable that gives the theoretical characterization immediate practical value.

3. **Convincing search-space reduction experiments (Section 6, Figures 5–6).** On real-world graphs from the bnlearn repository, the mGISS prunes over 90% of the search space for larger models. The random graph experiments systematically show that sparser graphs benefit more, consistent with the theory. These experiments directly validate the practical relevance of the theoretical characterization.

4. **Elegant theoretical machinery (Λ-structures, LSCA closure, connector concept).** The paper builds from clear definitions (conditional-intervention superiority, deterministic atomic-intervention superiority) through Proposition 4 establishing their equivalence, to the graphical characterization. The Λ-structure is a particularly nice conceptual device that bridges the graph-theoretic and intervention-theoretic views.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
1. **The bandit regret experiment (Figure 3) only compares mGISS vs. brute-force (all nodes) and lacks competitive baselines.** Without comparisons to other node-selection strategies — e.g., only parents of Y, only LSCAs without closure, or random subsets of the same size — the regret improvement cannot be attributed to the specific mGISS selection rather than simply having fewer arms. The experiment demonstrates that pruning helps, but does not distinguish *which* pruning is effective. This is the paper's clearest evaluative gap, though it does not threaten the theoretical contribution.

2. **The key equivalence (Proposition 4) between conditional and deterministic atomic superiority is not even sketched in the main text.** While the full proof resides in the appendix (standard practice for this venue), the proposition is the linchpin that connects the paper's core setting (conditional interventions) to the tractable deterministic atomic case used for the graphical characterization. A one-paragraph proof sketch explaining the bidirectional reasoning — even informally — would significantly improve the paper's self-containedness and reader confidence.

3. **The assumption that all ancestors of X are always in Z_X is stated but never relaxed or discussed.** The paper acknowledges this assumption (Footnote 3 notes "we are not claiming that all variables in An(X)\{X} need to be in Z_X for the best decision to be made"), but practitioners facing settings where some ancestors are unavailable or unobserved receive no guidance on how this affects the mGISS characterization. A brief discussion or pointer to future work on this point would be useful.

### Trivial
- The degenerate case where Y has no parents (no node can affect Y except Y itself, which is excluded) is not explicitly discussed. The paper restricts to Y with "at least one parent" for results, but acknowledging this edge case would improve completeness.

## Nice-to-Haves
- A proof sketch of Proposition 4 in the main text.
- Additional baselines in the bandit experiment (parents-only, LSCAs without closure, random subsets of matched size).
- A brief discussion of what happens when some ancestors cannot be conditioned on.

## Removed Points
These points were flagged by the reviewers but are removed from the main evaluation for the reasons stated below:
1. **"Proposition 4 not adequately justified; appendix unavailable."** — The paper states "All proofs... can be found in the appendix." The appendix is stripped by the parser; this is standard practice. Per policy, criticisms about missing appendix proofs are removed. The retained Minor weakness 2 captures the spirit of this concern (desire for a main-text sketch) without penalizing the paper for standard appendix usage.
2. **"The quantifier structure of Definition 1 is too strong."** — This criticism misunderstands the paper's modeling choice. A worst-case definition of superiority (∀ SCM, ∃ policy g, ∀ Z_X, Z_W, ∀ h) is standard in causal bandits (cf. Lee & Bareinboim 2018) and is a definitional choice, not a flaw. The paper never claims this is a weak condition; it defines superiority and then characterizes its consequences.
3. **"Experiments do not empirically verify the central theoretical claim."** — The theoretical claim (mGISS contains the optimal node) is a *guarantee* proved as Theorem 13. The experiments demonstrate the practical benefit of this guarantee (search-space reduction, regret improvement). Validating a theorem empirically by constructing SCMs where the optimum is "known a priori" is not standard for a theoretical guarantee and would constitute a different kind of experiment than what the paper aims to provide.
4. **"Code and appendix not available for review."** — Code is submitted as supplementary material. The appendix exists in the original submission. Per policy, parser artifacts do not constitute author omissions.
5. **"The paper does not discuss Y having no parents."** — Retained as a Trivial weakness for completeness, as the paper acknowledges the restriction.
6. Several generic strengths from the Strength Finder ("the paper addresses an important problem," "the paper is well-motivated") are removed as too generic to be informative.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **Strengthen the bandit experiment (Figure 3).** Add at least two baselines: (a) a random subset of nodes of the same size as the mGISS, and (b) a heuristic subset such as Pa(Y) ∪ LSCA(Pa(Y)) without the full closure. This would demonstrate that the mGISS is not just *any* small set but the *right* small set.
2. **Add a proof sketch of Proposition 4 in the main text.** Even a paragraph outlining the bidirectional reasoning would help readers who cannot access the appendix during initial review and would improve the paper's self-containedness in the published version.
3. **Explicitly discuss the limitation of the ancestor-inclusion assumption.** A sentence or two on what happens if some ancestors are unobserved would help practitioners apply the results correctly.

## Score and Decision

I now calibrate the score against the retrieved anchors. Round 1 bracketing placed the paper in the (5.5, 7.5) range. Round 2 narrowed this by comparison with specific anchors:

| Anchor | Path | Score | Round | Comparison |
|--------|------|-------|-------|------------|
| Counterfactual Structural Causal Bandits | gjvTNxVd2f.md | 5.50 | 1,2 | This paper has more genuine novelty (first full characterization for conditional interventions) and cleaner theory; the ctf-SCB was seen by some reviewers as incremental. The current paper is stronger. |
| Contextual Causal Bayesian Optimisation | QW0PchhVaD.md | 4.50 | 1 | The current paper has stronger theoretical contributions and more complete empirical validation. |
| Goal-Oriented Sequential Bayesian Experimental Design | i2blv7QxtJ.md | 5.00 | 2 | The current paper provides a more complete theoretical solution (closed-form characterization vs. a learned policy) and received no criticism about novelty being incremental. |
| On the identifiability of causal graphs with multiple environments | ta8BKRa1bl.md | 6.00 | 1,2 | Comparable in theoretical depth; the current paper additionally provides a practical linear-time algorithm. |
| ActiveCQ | CWpQsAubxy.md | 6.50 | 2 | Stronger empirical validation, but addresses a different problem (active estimation vs. search-space reduction). Current paper is in a similar tier. |

The strongest anchor of the most comparable papers is the 5.50 Counterfactual SCB, which was found slightly incremental. The current paper is novel (first characterization for conditional interventions), well-executed (clean theory + linear-time algorithm), and adequately validated (convincing search-space reduction + reasonable bandit experiments). The main evaluative gap — the bandit experiment's lack of competitive baselines — is a minor weakness that does not threaten the core theoretical contribution. A score of **6.0** positions the paper solidly above the incremental extensions (5.0–5.5) and in line with solid theoretical contributions that also demonstrate practical value.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>