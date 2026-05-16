Now I have all the information I need to verify each claim. Let me synthesize the final review.

---

## Summary

The paper proposes the Epistemic Graph Neural Network (EpiGNN), a GNN architecture that treats node embeddings as epistemic states (probability distributions over primitive relations) and uses bilinear composition and intersection-style pooling to simulate the algebraic closure algorithm. The model achieves state-of-the-art results on systematic relational reasoning benchmarks (CLUTRR, Graphlog) while using orders of magnitude fewer parameters than neuro-symbolic methods, and succeeds on new multi-path disjunctive reasoning benchmarks (RCC-8, IA) where neuro-symbolic approaches fail.

## Strengths

1. **Epistemic inductive bias yields strong systematic generalization.** The core design—embedding nodes as probability distributions over primitive relations, composing them via bilinear functions (Eq. 4), and pooling with min/product—is shown to be critical. The ablation study (Table 4) confirms that removing the epistemic constraint or the bilinear form of φ significantly degrades performance, establishing that these choices are not arbitrary but empirically necessary.

2. **First method to handle multi-path disjunctive reasoning in this setting.** The paper identifies a blind spot in existing neuro-symbolic methods (their implicit assumption that a single relational path suffices) and introduces two new benchmarks (RCC-8, IA) that require aggregating partial information from multiple paths. On these benchmarks, EpiGNN-min substantially outperforms neuro-symbolic baselines (R5, NCRL) and edge transformers, especially on the hardest configurations (k=9, b=3; Figure 4).

3. **Extreme parameter efficiency.** The model uses |ℛ|n + n³/m² parameters, and in practice is at least two orders of magnitude smaller than competing neuro-symbolic methods (Figure 5), without sacrificing accuracy on the primary benchmarks.

4. **Clean theoretical motivation.** Proposition 2 establishes that EpiGNN can exactly capture directional algebraic closure under appropriate parameterizations, providing a principled connection between the neural architecture and a well-understood symbolic reasoning algorithm.

5. **Competitive on inductive KGC despite being designed for systematic reasoning.** Table 3 shows EpiGNN achieving best or second-best Hits@10 on several WN18RR and FB15k-237 inductive splits, demonstrating versatility beyond its intended setting.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The path-selection strategy in the forward-backward model is unexamined.** When multiple paths exist between h and t, the paper randomly selects one shortest path to define ℰ_{h,t} (line 134). No ablation compares this against alternatives (e.g., using all entities on any path, union of all shortest paths, or all reachable entities), and no variance analysis is provided to show the model is robust to the random choice. The "w/o fwd-backwd" ablation removes the entire forward-backward component, not the path selection strategy specifically. This is a methodological gap: the forward-backward design is motivated by multi-path reasoning, yet a key sub-component relies on a single arbitrary path. That said, this is not a fatal issue—even the forward-only model (which avoids this selection entirely) performs strongly—but it weakens the forward-backward component's justification.

2. **The forward-only model used for inductive KGC is under-described.** The paper states "we use the forward-only EpiGNN to efficiently score all entities in the knowledge graph with respect to the query relation r" (line 214) but does not specify whether scoring is done via cross-entropy between the final entity embedding and the relation embedding, or some other mechanism. Since the inductive KGC experiments serve as an important demonstration of versatility, this should be clarified.

### Trivial

1. **Minor clarity issue with a_{1j} initialization.** The paper fixes a_{1j} = one-hot(j) to ensure identity composition works correctly (line 110). The reasoning follows from the initialization of h⁰ = (1,0,...,0), but the mapping of primitive relation indices to coordinates is never explicitly defined. Adding one sentence to explain this mapping would improve readability.

## Nice-to-Haves

1. **Empirical analysis of learned composition tensors.** Proposition 2 is an expressivity guarantee ("there exists a parameterization such that..."), which by its nature does not require empirical validation. However, an analysis showing that the learned a_{ij} tensors approximate the known RCC-8 or IA composition tables (e.g., KL divergence or accuracy of the most likely composed relation) would strengthen the narrative that EpiGNN actually uses this alignment in practice.

2. **Concrete parameter counts for each experiment.** The paper provides the analytical parameter formula and Figure 5, but citing explicit numbers (e.g., "on CLUTRR with n=X, m=Y: EpiGNN = Z parameters vs. R5 = W parameters") would make the efficiency claim more tangible.

3. **Sum pooling comparison.** The paper cites Schockaert (2024) for the theoretical incompatibility of sum pooling with the epistemic view. An empirical ablation confirming that sum pooling indeed performs worse would be a useful control, though not required given the theoretical argument.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Proposition 2 is informal and its empirical relevance is not tested."** — Removed. Expressivity results ("there exists a parameterization") are theoretical guarantees about representational capacity, not empirical claims. Demanding that they be validated by checking whether learned parameters match the ideal case misunderstands the nature of such claims. This is a nice-to-have but not a weakness.

- **"Error bars / standard deviations not reported for RCC-8/IA."** — Removed. The paper explicitly states (line 212): "We report the average accuracy and 2σ errors across 10 seeds for CLUTRR and 3 seeds for RCC-8, IA and Graphlog." Variance information is reported for all experiments.

- **"Benchmark generation details missing from main text."** — Removed. The paper references App. C and App. E for full details; these sections exist in the original submission but were stripped by the parser.

- **"No comparison of pooling variants (min vs. product vs. sum) in ablation."** — Moved to Nice-to-Have. The paper provides a theoretical justification (Schockaert, 2024) for why sum pooling is incompatible. An empirical demonstration would strengthen the claim but is not a missing control.

- **"Statistical testing lacking."** — Removed. Error bars are reported (2σ for CLUTRR, 3-seed results with variance for all others), which is standard practice for this class of benchmarks.

## Novel Insights

The reviews surface a key tension in the paper that the authors do not fully address: the forward-backward model is motivated by the need to handle multiple paths and different composition orderings, yet it relies on randomly selecting a single shortest path for the aggregation set ℰ_{h,t}. This design choice sits uneasily with the multi-path motivation. A more interesting question than "is this ablated?" is whether the forward-backward component is even needed in its current form: since the forward-only model (standard message passing over all paths) already handles multi-path settings (RCC-8, IA) well, and the main benefit of the forward-backward model appears on single-path CLUTRR (where path ordering matters), the path-selection randomness may be less consequential than the critic assumes. The paper would benefit from disentangling whether the forward-backward model's value comes from its path-aggregation mechanism or simply from the additional signal it provides by composing forward and backward embeddings at intermediate nodes.

## Suggestions

1. Add an ablation comparing the random shortest-path selection against using all entities on all paths (or the union of all shortest paths) for ℰ_{h,t}. If the variance is low or the alternative doesn't improve results, state this explicitly.
2. Clarify the scoring mechanism used for inductive KGC (forward-only model).
3. Provide a brief analysis—perhaps in the appendix—visualizing the learned a_{ij} tensors against the ground-truth composition tables for RCC-8 or IA, to empirically substantiate the claimed alignment with ACA.
4. Add one sentence explaining the correspondence between primitive relation coordinates and the identity relation (coordinate 1) to clarify the a_{1j} initialization.

## Score and Decision

This is a strong paper with a well-motivated architecture, thorough experiments, honest limitations, and a clear advance over prior work (especially the new multi-path benchmarks). The weaknesses are minor and addressable; none threaten the core claims. The paper makes real contributions to systematic relational reasoning.

**Score:** 7.5

**Decision:** Accept

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>