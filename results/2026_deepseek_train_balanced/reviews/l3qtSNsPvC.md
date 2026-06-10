Here is the consolidated final review:

---

## Summary

This paper develops a signal sampling theory for graphons — continuous limits of dense graph sequences. It proves a Poincaré inequality on graphon signal spaces (Theorems 1–2) that characterizes which subsets of the node continuum are uniqueness sets for bandlimited graphon signals, and connects Gaussian elimination on finite-graph Laplacian eigenvectors to consistent recovery of these uniqueness sets across convergent graph sequences (Theorem 3, Proposition 3). A practical algorithm is proposed and evaluated on GNN transferability and positional encoding acceleration tasks.

## Strengths

- **Graphon Poincaré inequality (Theorems 1–2, Section 4.1):** The paper generalizes Pesenson's discrete-graph Poincaré inequality to the continuous graphon setting, using a novel construction of an auxiliary graphon Γ(S). This proves that, under a bandwidth condition, the complement of a set satisfying the inequality is a uniqueness set for the Paley-Wiener space — a result that prior to this work existed only for finite graphs. The proof requires no continuity or smoothness assumption on the graphon (stated in contributions, line 51), distinguishing it from other graphon signal processing work.

- **Consistency of uniqueness sets across convergent graph sequences (Theorem 3 / Proposition 3, Section 4.2):** The paper proves that Gaussian elimination on the Laplacian eigenvectors of a finite graph Gₙ sampled from a graphon yields samples that converge (in a distributional sense) to a uniqueness set for the graphon PW space. This goes beyond prior per-graph sampling approaches: the sampling problem is solved once at the limit level and the result transfers to any large graph in a convergent sequence.

- **Computational complexity advantage of the algorithm (Section 5, lines 340–342):** By running the greedy sampling heuristic on a coarse q-node graph rather than the original n-node graph, the cost is reduced from O(p|E|) to O(pq²) when q ≪ n. The runtime analysis is concretely stated.

- **No smoothness/continuity assumption for the main theoretical result (line 51–52):** The Poincaré inequality and related theory do not require continuity or smoothness of the graphon, which is a meaningful relaxation relative to other graphon signal processing frameworks.

## Weaknesses

### Fatal

None.

### Major

- **Unsubstantiated bridge between theory and algorithm (Section 5 vs. Sections 3–4):** The paper claims (line 322) that the algorithm is "motivated by Theorems 1–4" and asserts (line 329) that "by Proposition 3, this procedure yields a uniqueness set for Gₙ with high probability." However, Proposition 3 is a statement about Gaussian elimination on the Laplacian eigenvectors of Gₙ — a procedure the algorithm does **not** implement. Instead, the algorithm uses: (i) a coarsened graphon representation via equipartition, (ii) the greedy heuristic from Anis et al. (2016) on the coarse graph, and (iii) local heat kernel PageRank clustering for node selection within intervals. The paper provides no formal argument that this three-step procedure approximates or inherits the guarantees of Proposition 3. The connection between the theoretical framework and the implemented method is asserted, not proved, making it impossible for the experiments to validate the theory. This is the paper's most consequential weakness: the theory and the algorithm operate in separate logical tracks, and the paper conflates them.

- **Insufficient baselines (Section 6):** Every experiment compares only against random sampling. Given that the algorithm builds on Anis et al.'s greedy heuristic, that method run directly on the full graph is a natural and necessary baseline. GE on the finite graph's eigenvectors (which the theory says should work) is another. Leverage-score, effective-resistance, and volume sampling are also standard in graph subsampling. Without these, it is impossible to assess whether the proposed method's modest gains over random sampling (e.g., 0.49 vs. 0.46 on Cora, Table 1) represent a meaningful advance or are obtainable by simpler off-the-shelf approaches.

### Minor

- **Experiments measure proxy tasks, not the theoretical construct (Section 6):** The paper's central theoretical object is the *uniqueness set* for Paley-Wiener spaces — a set that permits perfect reconstruction of bandlimited signals. Yet the experiments measure GNN classification accuracy on subsampled graphs (Table 1) and downstream classification with subsampled positional encodings (Table 2). Neither task verifies whether the sampled nodes actually form a uniqueness set, whether signals in the relevant PW space can be reconstructed, or whether the Poincaré inequality is satisfied. A direct reconstruction experiment (e.g., measure bandlimited signal reconstruction error from graphon-sampled vs. randomly sampled nodes) would substantially strengthen the paper's case that the theory has practical bite.

- **No conclusion or discussion of limitations:** The paper ends abruptly after the experiments. There is no section synthesizing the contributions, discussing when the assumptions hold or fail, acknowledging the gap between theory and algorithm, or outlining limitations of the graphon framework for real-world sparse graphs. For a paper making multiple theoretical claims, this omission undermines reader confidence that the authors have considered the scope and limitations of their results.

- **Runtimes are unclearly scoped (Table 1):** The table caption states "runtime for models trained on the full graph," but the reported values (~0.9s for Cora, CiteSeer, PubMed) are faster than typical full GNN training. It is unclear whether these numbers measure total training time, per-epoch time, or only the subsampling computation. The paper should clarify what the timing numbers include and whether the comparison is apples-to-apples.

### Trivial

- The paper labels the first experimental setting "transferability" (contribution 4, line 55), but the standard meaning in the graphon/GNN literature is training on one graph and testing on another drawn from the same model, not training on a subsample and testing on the full graph. The paper defines its usage in context, so this is a labeling imprecision rather than an error.

## Nice-to-Haves

- Directly validate the theoretical mechanism: run an experiment that checks whether the sampled nodes actually satisfy the uniqueness property by reconstructing bandlimited graph signals from the samples and measuring reconstruction error, comparing graphon-sampled nodes against randomly sampled ones.
- State one complete, interpretable theoretical bound (e.g., for the well-separated block setting of Theorem 4) with all constants defined in terms of block sizes, kernel properties, and eigenvalue gaps, so the reader can assess what the theory guarantees.
- Include a discussion of when the dense-graphon approximation is reasonable for real-world graphs that are often sparse, and whether the need for node labels/ordering (line 345) is a practical limitation.

## Removed Points

The following points from the input reviews were removed with justification:

- **Criticism that theoretical results are unverifiable without appendix:** The hard rules prohibit penalizing papers for content stripped by the PDF parser (appendices, proofs). The constants in Theorem 3 are defined in the appendix and in Schiebinger (2015), which is standard for theoretical papers.
- **Criticism about missing justification for essential spectrum claim (line 135):** The paper cites "App. graphon_functional_analysis" for this — standard practice.
- **Criticism about Lipschitz assumptions discussed in commented-out text:** The commented-out content was not part of the submitted paper; the parser erroneously included it.
- **Criticism about Theorem 4 conditions being unexplained:** The conditions are stated formally with explicit inequalities, which is standard for a theoretical result at this venue.
- **Various formatting/style nitpicks** per the hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviews identified the theory-algorithm disconnect and the weak baselines, but did not surface a genuinely novel observation about the paper that the authors themselves had missed.

## Suggestions

1. **Clarify the relationship between theory and algorithm.** The paper should either (a) redesign the algorithm to actually implement the Gaussian elimination on eigenvectors procedure that Proposition 3 guarantees, or (b) re-frame the paper to present the theory and the algorithm as two separate contributions, each with its own validation, and remove the claim (line 329) that Proposition 3 justifies the algorithm.
2. **Add baselines.** At minimum, compare against Anis et al.'s greedy heuristic run directly on the full graph and against the GE-based approach on the finite graph.
3. **Add a direct uniqueness-set validation.** Measure bandlimited signal reconstruction error from the sampled nodes to test whether the Poincaré inequality / uniqueness set theory actually holds.
4. **Write a proper conclusion** that discusses limitations, when assumptions hold or fail, and future work.
5. **Clarify runtime measurements** in Table 1 — state explicitly what is being timed and whether the comparison is fair.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>