Now I have all the information I need. Let me construct the final consolidated review.

## Summary

This paper addresses the understudied problem of oversquashing in topological deep learning (TDL). It views simplicial complexes and their message-passing schemes as relational structures, enabling the extension of graph-theoretic oversquashing results — sensitivity bounds, curvature analysis, impact of depth and hidden dimensions — to higher-order architectures. The framework is instantiated on simplicial message passing, and experiments on graph classification benchmarks and a synthetic ring-transfer task examine how rewiring affects both graph and simplicial models.

## Strengths

- **First theoretical analysis of oversquashing in TDL.** The paper provides the first rigorous sensitivity bound for relational (including simplicial) message passing (Lemma 3.2) and extends results on depth-driven exponential sensitivity decay (Theorem 3.5) and hidden-dimension effects (Section 3.4) to higher-order architectures, directly addressing open problems identified by the TDL community (Papamarkou et al., 2024, directions 2 and 9).

- **A unifying formalism.** The relational-structure encoding (Definition 2.5) subsumes graph message passing, relational GCNs, simplicial networks, and CW networks under a single framework, making it possible to transfer analytical tools across architectures that previously had no common language for oversquashing analysis.

- **Empirical evidence that simplicial networks respond to rewiring similarly to graph networks.** The experiments on ENZYMES, MUTAG, NCI1, and PROTEINS (Table 1) demonstrate that rewiring generally improves or maintains performance for both graph and simplicial models, and the best rewiring algorithm often agrees between the lifted and unlifted settings (75% agreement on the reported datasets). This suggests the relational aggregation into an influence graph captures practically relevant structure.

- **Reproducibility commitment.** A reproducibility statement with an anonymous code link is provided.

## Weaknesses

### Major

- **The proposed rewiring algorithm is not specified.** Section 4 states "Our proposed relational rewiring algorithm is as follows" but provides no algorithm steps — the next text begins Section 5. While one can infer the approach (compute the collapsed adjacency matrix from Definition 4.1, then apply existing graph rewiring algorithms), the paper claims to propose a *new* heuristic but never defines it. The experiments section says "We apply relational rewiring for 40 iterations using three choices for REWIREALGO: SDRF, FoSR, AFRC" but never clarifies whether rewiring is applied to the collapsed graph or to each relation separately, how the collapsed graph is constructed for the experiments, or what criterion selects edges to add. This makes the claimed contribution of a "relational rewiring heuristic" unverifiable.

- **Experimental validation does not convincingly test the framework's core claims.** Several issues compound:
    1. **Tasks are standard graph classification, not simplicial tasks.** All benchmarks (ENZYMES, MUTAG, NCI1, PROTEINS) are graph classification problems on which simplicial models are evaluated via clique-complex lifts. This tests how well simplicial models perform on graph tasks, not whether the relational framework yields *new understanding* of simplicial-specific oversquashing behavior.
    2. **No baseline comparing the relational framework against its own influence graph.** The paper never compares message passing on the original simplicial complex against message passing on its aggregated influence graph. This is the most direct test of whether the framework provides useful abstraction beyond working directly with the graph-on-Hasse-diagram perspective.
    3. **The RINGTRANSFER synthetic benchmark may be vacuous for the simplicial setting.** A ring (cycle) graph has no 3-cliques, so its clique complex is the ring itself — "simplicial message passing" on this structure is graph message passing. The paper does not specify what simplicial lifting is used for this task, making it impossible to assess whether the reported trends reflect any genuinely topological effect.
    4. **Statistical rigor is weak.** Results are reported as mean ± standard error over 10 trials, but many changes are within one standard error. The claim about "75% agreement in best rewiring algorithm" is computed over only 4 datasets with no confidence intervals or significance tests. Green/red coloring shows about as many decreases as increases for some models (e.g., GIN on MUTAG decreases with SDRF and AFRC).

- **Section 5.3 is an incomplete placeholder.** The section begins with "2. There, we visualize the curvature..." — the "2." indicates a continuation of a list with no "1." in the main text, and the content is a single sentence with a figure reference. This suggests incomplete writing and undermines confidence in the paper's readiness.

### Minor

- **The relational-structure framework is presented as more novel than it is.** The paper acknowledges that this perspective aligns with augmented Hasse diagrams used in prior TDL literature (Hajij et al., 2023; Eitan et al., 2024; Papillon et al., 2024, as noted in Remark 2.7 and line 67). The framework's value lies in *applying* it to oversquashing analysis, not in introducing a fundamentally new formalism. The paper would be better served by being more explicit about what the relational lens enables that the Hasse-diagram perspective did not.

- **Theoretical results largely reduce oversquashing in TDL to graph oversquashing on the influence graph.** Lemma 3.2, Proposition 3.4, and Theorem 3.5 all eventually analyze the aggregated influence graph $\mathcal{G}(S,\mathbf{B})$, which discards the multi-relational structure that makes TDL distinct. While the paper frames this as a feature (unification), it means the results do not provide insight into how the *different* adjacency types (boundary vs. co-boundary vs. lower/upper) contribute differently to oversquashing — a question of genuine interest to the TDL community.

- **Assumption 2 (row-normalized shift operators) is restrictive for Theorem 3.5.** Many practical TDL models do not row-normalize their adjacency operators. The paper does not discuss whether the depth result holds under weaker conditions or how common normalization choices affect the bound.

- **The curvature adaptation (Definition 3.3) transfers coefficients (4, 3, 2) from existing graph curvature without justification for weighted directed graphs.** Proposition 3.4 inherits these constants from Fesser & Weber (2023), but the paper does not discuss whether the geometric interpretation of these coefficients carries over to the relational setting where edges are weighted and directed.

### Trivial

- The paper contains several forward references to equations and sections that do not align with the numbering in the extracted text (likely parser artifacts; the original submission may not have this issue).

## Nice-to-Haves

- A controlled experiment where simplicial message passing on a complex is compared to message passing on its influence graph, to test whether the relational framework identifies oversquashing patterns that the influence graph misses.
- A specification of the simplicial lifting used for the RINGTRANSFER task and a justification that the task can distinguish graph from simplicial behavior.
- Statistical significance tests (e.g., paired t-tests) for the rewiring comparisons in Table 1.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The central framework is a rephrasing of known ideas, not a novel contribution."** — Overstated. The paper's contribution is not the relational structure concept itself (which existing TDL work uses via Hasse diagrams) but the extension of oversquashing analysis through this lens. This is a genuine application to an open problem. Kept as a minor weakness (see Minor #1) rather than a fatal criticism.
- **"Proof sketches should be in the main text."** — This concerns content deferred to the appendix, which per the hard rules is standard practice; the appendix exists in the original submission.
- **"Notation is heavy / flow disrupted by forward references."** — A style/presentation nitpick.
- **"The paper does not specify how the collapsed graph is constructed for the experiments."** — The paper does define the collapsed adjacency matrix (Definition 4.1). The missing specification is about the algorithm steps, not the matrix definition.
- **"Missing ablation comparing influence graph baselines."** — Moved to Nice-to-Haves because it would strengthen the paper but is not a core flaw given the paper's exploratory scope.
- **Strength Finder's claim about "synthetic benchmark confirms theory."** — Removed per the rule that when a strength and weakness conflict, the weakness wins. The RINGTRANSFER experiment's validity for simplicial complexes is questionable (see Major weakness #2.3), so this claimed strength is unreliable.

## Novel Insights

None beyond the paper's own contributions. The reviews largely surface the gap between the paper's ambitious framing and its actual execution, rather than discovering unexpected findings.

## Suggestions

1. **Define the rewiring algorithm explicitly.** The paper should provide a step-by-step description: how the collapsed adjacency matrix is used, how edges are selected for addition, and how the algorithm terminates.
2. **Add a direct comparison against the influence graph baseline.** Run message passing on the original simplicial complex and on its aggregated influence graph, and compare oversquashing behavior. This would test the framework's added value.
3. **Specify the simplicial lifting for RINGTRANSFER.** If no higher-order simplices exist (as for a ring's clique complex), explain what structure the "simplicial" models are actually processing, or choose a synthetic task that genuinely tests higher-order message passing.
4. **Include significance tests for the rewiring results.** Report whether performance changes are statistically significant, and provide confidence intervals for the "75% agreement" claim.
5. **Complete Section 5.3** and ensure all sections are in final form before submission.
6. **Reduce the novelty framing.** Acknowledge more directly that the relational structure view aligns with existing Hasse-diagram perspectives and that the main contribution is the oversquashing analysis enabled *through* this lens, not the lens itself.

## Score and Decision

The paper tackles a genuinely important and understudied problem — oversquashing in topological deep learning — and provides the first theoretical analysis of this phenomenon in simplicial networks. The formal framework is clean and the intent to unify graph and topological message passing is laudable. However, the execution has several gaps that prevent the paper from being accepted in its current form: the core algorithmic contribution (rewiring) is underspecified to the point of being unverifiable; the experimental validation does not convincingly test the framework's claims (tasks are graph rather than simplicial, the synthetic benchmark may be vacuous for the simplicial case, and statistical rigor is weak); and an incomplete section suggests the paper is not fully prepared. The paper would need substantial revisions — particularly a complete algorithm specification and experiments that genuinely test the relational framework on simplicial-specific behavior — before it could be accepted.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>