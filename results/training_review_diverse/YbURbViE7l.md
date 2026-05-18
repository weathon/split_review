Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper introduces GOttack, an adversarial attack framework for GNN node classification that leverages graph orbit information (specifically orbits 15 and 18) to select candidate nodes for edge perturbations. The method pre-filters the search space to nodes in these periphery orbits, then uses a linearized surrogate loss to pick the optimal edge modification. The paper reports that GOttack achieves the highest average misclassification rate (52.08%) across 15 attack settings, outperforming Nettack (47.02%) while reducing computational overhead by filtering candidates to roughly 23% of all nodes. It also presents evidence that existing gradient-based attacks disproportionately select nodes in these same orbits.

## Strengths

- **Empirically demonstrated attack effectiveness**: Table 2 shows GOttack achieves the highest overall average misclassification rate (52.08%) across three backbone GNNs and five datasets, outperforming the second-best method Nettack (47.02%). It yields the best performance in 7 out of 15 single-edge settings.

- **Novel topology-driven candidate selection**: The core idea of using graph orbits to pre-filter the candidate set for structural attacks is well-motivated and different from existing degree-based or gradient-only approaches. This provides a principled way to reduce the search space from O(n²) to a much smaller set of nodes.

- **Efficiency gain is supported**: GOttack reduces the candidate set to approximately 23% of nodes via orbit filtering. The paper reports end-to-end time costs (Table 4) and notes that orbit discovery on CORA takes only 0.17 seconds, demonstrating that the pre-processing overhead is modest.

- **Evidence of correlation with gradient-based attacks**: Table 5 shows that 97.5% of Nettack's initial attacks in Polblogs involve 1518-orbit nodes, despite only 9.41% of nodes belonging to this category. This is an interesting empirical finding that connects the proposed method's design intuition to existing attack behavior.

- **Effectiveness against defenses**: Table 3 shows GOttack achieves the highest overall misclassification rate (33.07%) against four defense models, marginally ahead of SGA (32.5%), confirming the attack operates under realistic settings.

## Weaknesses

### Fatal

None. The paper's core empirical claims — that GOttack achieves competitive or better misclassification rates with reduced candidate search — are supported by the reported results. The weaknesses below are significant but do not invalidate the central contribution.

### Major

- **Abstract overclaims runtime improvement**: The abstract states GOttack "completes training in approximately 55% of the time required by the fastest competing model." The main text (line 191) correctly qualifies this as relative to Nettack on BlogCatalog specifically. These statements are inconsistent — the 55% figure is not relative to the overall fastest method (the paper notes SGA is more scalable, line 199). The abstract's phrasing is misleading and should be corrected to reflect what is actually measured.

- **Theorem 1 is stated as a formal result but is neither proven nor directly connected to the attack**: Theorem 1 asserts that nodes in orbits 15/18 have longer random walk hitting times, making them optimal for remote connections. No proof, derivation, or even proof sketch is provided. More importantly, the connection between hitting times and the actual attack optimization (surrogate loss based on a linearized GCN) is never established. The empirical validation on line 222 measures label distance changes, not hitting times. This does not invalidate the method — the attack works regardless — but it means the theoretical framing as stated is unsupported. The paper would be stronger framing this as an empirically motivated heuristic rather than a formal theorem.

- **Missing ablations to isolate the orbit-selection contribution**: The paper compares GOttack against full attack methods (Nettack, SGA, PRBCD, FGA) that differ in multiple design choices (surrogate model, candidate selection, optimization strategy). There is no ablation that isolates whether the orbit-based candidate selection itself provides the benefit, e.g., comparing GOttack against a version with degree-based or random candidate selection while keeping the gradient-based optimization identical. Without this, it is unclear how much of the performance comes from orbit filtering vs. other design choices.

### Minor

- **Defense evaluation protocol is underspecified**: The paper describes a "direct poisoning attack" (Section 4.1) but does not explicitly state whether defense models (RGCN, GCN-Jaccard, GCN-SVD, MedianGCN) are retrained on the poisoned graph or applied post-hoc with fixed weights. In the standard poisoning attack protocol, the model is trained on the perturbed graph, and the results are likely obtained under this convention, but the paper should state this clearly.

- **Selection of orbits 15/18 specifically vs. other periphery orbits is pragmatic rather than principled**: The paper acknowledges (lines 205-206) that orbits 19, 27, and 39 "could fit the periphery definition" but excludes them due to "scarcity." This is a reasonable practical choice but limits the generality claim. The paper does not test whether alternative orbit pairs or combinations would perform similarly.

- **Claim of a "universal attack strategy" (lines 17, 23) overstates a correlation finding**: Table 5 shows that nodes Nettack happens to select disproportionately belong to orbits 15/18. The paper presents this as having "uncovered a universal attack strategy commonly employed by several well-known gradient-based models." This is a post-hoc correlation — the paper has not shown that Nettack or other methods explicitly or implicitly use orbit information. The finding is interesting but should be described as an observed empirical pattern, not a discovered strategy.

- **Surrogate model differs across compared methods**: GOttack and other attacks (except SGA) use GCN as surrogate, while SGA uses SGC (line 175). This is standard practice (each method uses its recommended surrogate), but the paper should at minimum discuss whether this choice could influence relative performance.

- **Single-orbit vs. dual-orbit justification**: The paper notes (lines 207-208) that single-orbit experiments showed "similar efficacy" with larger time complexity. If one orbit suffices for effectiveness, the necessity of the dual-orbit (1518) scheme is unclear. The efficiency argument is plausible but the paper does not report the relative candidate set sizes or runtimes for the single-orbit vs. dual-orbit variants.

### Trivial

- Line 224: The "Defenses and Availability" subsection contains a sentence fragment ("3 that can attack i) a graph of any size...") that appears to be an incomplete draft note.
- Figure 2 caption ("Nodes u, z and w have 15 and 18 orbits respectively") is ambiguous — it is unclear whether "have 15 and 18 orbits" means these nodes are in orbit categories 15 and 18, or that they have 15 and 18 distinct orbits.
- The name "GOttack" is used extensively without explicit definition (presumably "Graph Orbit Attack").

## Nice-to-Haves

- An ablation comparing orbit-based candidate selection against degree-based, centrality-based, and random candidate selection while keeping the gradient-based optimization step identical would cleanly isolate whether the topological selection causes the observed performance.
- Reporting runtime ratios for all datasets (not just BlogCatalog vs. Nettack) would give a more complete picture of the efficiency claim.
- A discussion of why Theorem 1 (hitting times) relates to the surrogate loss (linearized GCN) would tighten the theoretical framing, or alternatively, dropping the theorem framing and treating the periphery orbits as an empirically discovered pattern.

## Removed Points

- *"Results are relegated to the appendix (Section D)"*: Removed per policy — appendices exist in the original submission but are stripped by the parser.
- *"The 55% claim is a cherry-pick"* (in the strong sense that it's fabricated): The main text correctly says "55% of the time taken by Nettack" on BlogCatalog. This is an honest statement of one data point. The issue is the abstract's overclaim, which is kept in Major.
- *"The GOttack name is never defined"* (as a major issue): Moved to Trivial. "GOttack" clearly derives from "Graph Orbit Attack" in context.
- *"Theorem 1 is unproven and the entire attack is a heuristic"* (framed as fatal): The paper's core contribution is empirical, not theoretical. The method's effectiveness does not depend on Theorem 1 being formally proven — the empirical results stand on their own. The theorem issue is kept in Major because of the formal framing, not because it invalidates the contribution.

## Novel Insights

None beyond the paper's own contributions. The observation that orbits 15/18 correlate with nodes targeted by gradient-based attacks is the paper's most interesting finding, but the reviews do not identify a deeper insight the authors missed.

## Suggestions

1. Correct the abstract to state the efficiency claim relative to the specific method (Nettack) and dataset (BlogCatalog) actually measured, not "the fastest competing model."
2. Either provide a proof sketch for Theorem 1 or re-frame it as an empirically motivated observation/hypothesis and drop the formal Theorem label.
3. Add an ablation using the same surrogate model with different candidate-selection strategies (orbit-based, degree-based, random) to isolate the contribution of orbit filtering.
4. Explicitly state whether defense models are retrained on poisoned graphs in the defense evaluation.
5. Tone down the "universal attack strategy" language to reflect that this is a correlational finding, not evidence that existing attacks implicitly use orbits.

## Score and Decision

The paper presents a novel and well-motivated approach to structural attacks on GNNs using graph orbit information. The empirical results show competitive or superior misclassification rates with meaningful efficiency gains. However, the abstract overclaims runtime improvements, the theoretical framing (Theorem 1) is unsupported, the evaluation lacks critical ablations to isolate the orbit-selection contribution, and several claims are overstated relative to the evidence. The contributions are real but the presentation and experimental rigor need significant improvement.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>