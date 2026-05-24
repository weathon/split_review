Now I have a thorough understanding of the paper and can produce the consolidated review.

## Summary

This paper provides a theoretical analysis of the loss landscape of regularized neural networks using convex duality. For two-layer scalar-output networks, it characterizes the optimal solution set as a polytope linked to the dual optimum, identifies a "staircase of connectivity" — phase transitions in the connectivity of the optimal set as width varies across five regimes defined by two critical widths ($m^*$ and $M^*$), and constructs counterexamples showing non-unique minimum-norm interpolators. The results are extended to vector-valued networks (proving connectivity when $m \ge nc+1$) and parallel three-layer networks.

## Strengths

1. **Staircase of connectivity with explicit critical widths (Theorem 2, Figure 1):** The paper derives two critical widths $m^*$ and $M^*$ from the optimal polytope's irreducible solutions and proves five distinct topological regimes as width $m$ increases — from finite/disconnected, to emergence of nontrivial connected components, to full connectivity. This is a precise phase-transition description that goes beyond existing unregularized connectivity results and is specific to the regularized setting.

2. **Non-unique minimum-norm interpolators in higher dimensions (Proposition 2, Example 2, Figure 3):** The paper constructs an explicit training problem (with $n=5$, one-dimensional input) where the minimum-norm interpolation problem has infinitely many solutions, even without skip connections. This provides theoretical insight into the conditions needed for uniqueness, showing that unidimensional data, bias penalization, and free skip connections are all jointly necessary.

3. **Generalization to vector-valued and parallel deep networks (Theorem 4, Theorem 5):** The paper extends the connectivity result to vector-valued networks (connected when $m \ge nc+1$) and shows that for parallel three-layer networks the first-layer weight directions come from a finite set determined by the dual. These extensions demonstrate the breadth of the convex-duality framework beyond the scalar two-layer setting.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Undefined symbol $\mathcal{S}_i$ in Theorem 1.** The theorem statement (lines 140–145) uses $\mathcal{S}_i$ in the definition of $\bar{u}_i$ and $\bar{v}_i$, but this symbol is never defined in the main text. The reader cannot parse the core theorem without guessing what $\mathcal{S}_i$ refers to (presumably $\mathcal{K}_i \cap \{\|u\|_2 \le 1\}$ or similar). The paper should define $\mathcal{S}_i$ explicitly.

2. **Ambiguous reuse of $m^*$ across sections.** In §2 (line 111), $m^*$ is introduced as "a critical threshold" for strong duality of the convex reformulation, citing prior work. In §3.2 (line 180), $m^*$ is redefined as the minimum cardinality of irreducible solutions in the optimal polytope. The paper never clarifies whether these refer to the same quantity or different thresholds, and if they are the same, why the two characterizations coincide. This creates confusion for the reader.

3. **$m^*$ and $M^*$ not computed in the toy example.** The running example (Example 3.1, Figure 2) illustrates the staircase phenomenon for $m=1,2,3$ and states "$m=3 = \min\{m^*+M^*, n+1\}$" (line 233), but the actual numerical values of $m^*$ and $M^*$ for that dataset are never given. Stating them (e.g., "$m^*=1$, $M^*=2$" or whatever they are) would ground the abstract theorem and help the reader verify the phase transitions concretely.

### Trivial

None.

## Nice-to-Haves

- In the generalizations section, several key symbols ($\bar{\Theta}_i$, $\mathcal{C}_y$, $\mathcal{C}_y$) are mentioned but defined only in the appendix. Introducing them with one-line definitions in the main text would improve readability for readers who do not immediately consult the appendix.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Incomplete formal statement of non-uniqueness results for SB/SNB":** The paper states the claim in prose (line 247: "We first show that when the input is not unidimensional, we have non-unique optimal interpolators both for SB and SNB setting") and references a labeled proposition (\cref{p1:Nonunique}) that lives in the appendix. Per policy, missing appendix content from the parsed version should not be penalized. The claim is clearly stated in prose.
- **"Dual optimum dependence in the optimal polytope":** The paper explicitly addresses this (line 153): "for any choice of $\nu^{*}$ we know that $\mathcal{P}^{*}_{\nu^{*}}$ is the optimal set of [the convex problem], meaning the choice of $\nu^{*}$ does not matter." The reviewer's concern is addressed by the paper.
- **"Definition of $M^*$ and isolated-point claim":** The proof of why maximal-support irreducible solutions correspond to isolated points is in the appendix. Per policy, missing appendix proofs are not a valid weakness. The theorem statement is clear.
- **"Abstract overstates connectivity result":** The abstract says "topology of the global optima goes through a phase transition as the width changes" — this accurately describes Theorem 2's five regimes. No overstatement.
- **"Zero slot connectivity argument sketch is insufficient":** The paper provides a sketch (line 193) and notes the full proof is in the appendix. Standard practice for theory papers.
- **"Generalizations section uses undefined symbols":** These symbols ($\bar{\Theta}_i$, $\mathcal{C}_y$, etc.) are defined in the full submission's appendix. Per policy, this is not a valid weakness.
- **Strengths removed from Strength Finder:** None needed removal; all three identified strengths are concrete and specific.

## Novel Insights

The most incisive observation across the reviews is that the paper uses the same symbol $m^*$ in two potentially different roles (strong-duality threshold in §2 vs. minimum irreducible cardinality in §3.2) without clarifying their relationship. This is a genuine clarity gap that could confuse readers unfamiliar with the prior work of Pilanci & Ergen and Mishkin et al. Beyond this, the reviews do not surface any novel insight that the paper itself does not already articulate.

## Suggestions

1. Define $\mathcal{S}_i$ explicitly in the statement of Theorem 1 (or immediately before it). A one-line definition such as "$\mathcal{S}_i = \mathcal{K}_i \cap \{\|u\|_2 \le 1\}$" would suffice.
2. Clarify whether the $m^*$ in §2 (strong duality threshold) and the $m^*$ in §3.2 (minimum cardinality) are the same quantity. If they are, state this explicitly; if not, rename one to avoid confusion.
3. Add the computed values of $m^*$ and $M^*$ to the toy example in §3.2 so the reader can verify the staircase transition points concretely.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>