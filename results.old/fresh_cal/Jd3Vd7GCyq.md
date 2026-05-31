Here is the consolidated final review.

---

## Summary

This paper studies the computational complexity of computing the positive non-clashing teaching dimension of concept classes represented as balls in a graph. It makes four main contributions: (1) NP-hardness of STRICT NON-CLASH even for teaching dimension \(k=2\), settling an open question from Chalopin et al. (2024); (2) near-tight exponential running-time upper and lower bounds (with only a logarithmic factor gap); (3) fixed-parameter tractability of the more general NON-CLASH problem parameterized by vertex integrity (a less restrictive parameter than the previously used vertex cover number); and (4) W[1]-hardness for the combination of feedback vertex number, pathwidth, and \(k\), ruling out FPT for several natural parameters (including treewidth).

## Strengths

- **Settles open problem with tight NP-hardness for constant teaching dimension (Theorem 1).** Prior work left open whether STRICT NON-CLASH is NP-hard when \(k\) is a fixed constant; Theorem 1 proves NP-hardness already for \(k=2\) (the smallest non-trivial case, as \(k=1\) is trivially solvable). The reduction targets split graphs — the same class used in prior hardness for large \(k\) — making the result directly comparable and answering the open question.

- **Near-tight exponential running-time bounds (Theorem 4 and Proposition 5).** The paper improves the prior upper bound from \(2^{\mathcal{O}(n^2\cdot d)}\) to \(2^{\mathcal{O}(n\cdot d\cdot k\cdot\log n)}\) and establishes an ETH-based lower bound of \(2^{o(n\cdot d\cdot k)}\). The gap is now only a logarithmic factor in the exponent, whereas earlier work had an exponential gap between its \(2^{o(n\cdot d)}\) lower bound and \(2^{\mathcal{O}(n^2\cdot d)}\) upper bound.

- **Fixed-parameter tractability for a less restrictive parameter (Theorem 17).** Prior FPT results used the vertex cover number (a highly restrictive parameter). Theorem 17 proves NON-CLASH is FPT parameterized by vertex integrity, which is strictly less restrictive. The proof introduces a novel "blueprint" notion (Definition 2) and a kernelization that reduces the instance to size bounded only by the parameter — a substantial technical achievement.

- **W[1]-hardness excluding FPT for many natural parameters (Theorem 18).** Provides a W[1]-hardness reduction showing that NON-CLASH parameterized by feedback vertex number plus pathwidth plus \(k\) is not FPT (under standard assumptions). This answers an open question from Chalopin et al. (2024) and, by extension, rules out FPT for treewidth and clique-width as well.

- **First complexity analysis of the non-strict (general) setting.** While prior work focused on the strict variant (all balls present), this paper addresses the more general NON-CLASH problem where not all balls need be present — a more natural and practically relevant setting.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Pathwidth bound argument could be cleaner (Section 5).** In the proof of Theorem 18, after deleting the feedback vertex set \(\{x_1, x_d, f_x \mid x \in \mathcal{X}\}\), the remaining graph \(G'\) is described as consisting of subdivided caterpillars (pathwidth 2) and "a vertex with multiple pendent subdivided caterpillars and (simple) paths." The paper then adds a step about "deleting one further vertex from each connected component" to reach constant pathwidth. The reasoning is correct but the presentation is unnecessarily convoluted: a more straightforward argument would note that each component of \(G'\) already has bounded pathwidth (at most 2 or 3) without the additional deletion step, or would explain more clearly why the extra deletion is needed for the mixed-type components. This does not affect correctness but could confuse a reader.

### Trivial

- **Notation overloading for \(\sim_B\).** The symbol \(\sim_B\) is used for both an equivalence relation on connected components (Definition 1) and, via overloading, for individual vertices and balls (line 107: "\(v \sim_B w\)"). The paper acknowledges this overloading explicitly, but it can still cause confusion on first reading, especially given the density of definitions in Section 4.

## Nice-to-Haves

- The caption text for Figure 1 is somewhat terse ("The dotted edge corresponds to the absence of that edge"). Slightly more descriptive captions (e.g., explaining what each part of the figure encodes) would help readability.

## Removed Points

These points were raised by one or more reviewers but are removed per consolidation guidelines. Treat them with caution — they may reflect real concerns that could be explored in discussion but are not verified weaknesses after cross-checking against the paper as presented.

- **Criticism: Proposition 5 stated without algorithmic justification / no sketch provided.** The proof (and algorithm description) is standardly deferred to the appendix, which is stripped by the parser. The main text states the bound and its relationship to prior work. Per policy, weaknesses about missing appendix proofs are removed.

- **Criticism: Lemma 19 correctness proof absent from main text for the W[1]-hardness reduction.** The full correctness proof is standardly deferred to the appendix. The reduction construction is described in detail in the main text. Per policy, removed.

- **Criticism: FPT algorithm (Theorem 17) relies on a chain of lemmas whose proofs are not fully visible in the main text.** The main text provides definitions, lemma statements, and a high-level description of how they fit together; detailed proofs are in the appendix. Per policy, removed.

- **Criticism: Lemmas 2 and 3 stated without proof sketch for the NP-hardness reduction.** Again, proofs are in the appendix. The reduction construction is described. Per policy, removed.

- **Criticism: "Strengthening the Paper on Its Own Terms" suggestions about providing sketches for the FPT algorithm and W[1]-hardness correctness.** These suggestions ask for content that would normally appear in the appendix or as expanded main-text sketches. Per policy, removed.

- **Criticism about missing related works or absent references.** Per policy, removed as the reviewer lacks the external sources to confirm existence.

- **Criticism about reproducibility / undisclosed hyperparameters / missing implementation details.** Not applicable to theory papers; removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- In the pathwidth argument of Theorem 18, clarify why the additional "delete one further vertex" step is needed (or remove it if the components after feedback vertex deletion already have bounded pathwidth without it). This would eliminate a source of reader confusion.
- Consider adding a brief remark when overloading \(\sim_B\) for vertices and balls that the overloading is purely for notational convenience and is defined via the equivalence classes \([u]_{\sim_B}\) and \([B_r(u)]_{\sim_B}\), to help readers who may not immediately grasp the convention.

## Score and Decision

MY FINAL SCORE: <score>9.0</score>
MY FINAL DECISION: <decision>Accept</decision>